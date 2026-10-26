"""Verifier les exports KiCad et la preservation de la feuille BQ (Python standard)."""
import json,re,zipfile,hashlib,copy
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def parse(text):
    stack=[];result=None
    for t in re.findall(r'"(?:\\.|[^"\\])*"|[^\s()]+|[()]',text):
        if t=='(':
            n=[]
            if stack:stack[-1].append(n)
            else:result=n
            stack.append(n)
        elif t==')':stack.pop()
        else:stack[-1].append(json.loads(t,strict=False) if t.startswith('"') else t)
    return result
def kids(n,k):return [x for x in n if isinstance(x,list) and x and x[0]==k]
def one(n,k):return next(iter(kids(n,k)))
def prop(n,k):return next(x[2] for x in kids(n,'property') if x[1]==k)
def read(path):return parse(path.read_text(encoding='utf-8'))
P=ROOT/'VeillePorte'
with zipfile.ZipFile(ROOT/'references/EDU_RAK_2026/Hardware/Kicad/edu_rak_2026_kicad.zip') as z:
    name=next(n for n in z.namelist() if n.endswith('harvester.kicad_sch'))
    original=z.read(name)
original_bq=parse(original.decode('utf-8'))
active_bq=read(P/'alimentation.kicad_sch')
allowed={'ROV1':'6.19M','ROV2':'6.81M','ROK3':'464k','ROUT1':'4.99M','ROUT2':'7.87M'}
old_components={prop(s,'Reference'):s for s in kids(original_bq,'symbol')}
active_components={prop(s,'Reference'):s for s in kids(active_bq,'symbol')}
assert old_components.keys()==active_components.keys(),'Composants BQ ajoutes ou retires'
for ref,s in active_components.items():
    c=copy.deepcopy(s)
    if ref in set(allowed)|{'ROK1','ROK2'}:
        c[:]=[x for x in c if not(isinstance(x,list) and x and x[0]=='property' and x[1]=='Tolerance')]
    if ref in allowed:
        assert prop(s,'Value')==allowed[ref]
        next(x for x in kids(c,'property') if x[1]=='Value')[2]=prop(old_components[ref],'Value')
    assert c==old_components[ref],f'Modification BQ non attendue : {ref}'
doc=read(P/'veilleporte.net');actual={}
refs=[one(c,'ref')[1] for c in kids(one(doc,'components'),'comp')]
assert len(refs)==len(set(refs)),'References dupliquees'
for net in kids(one(doc,'nets'),'net'):
    for node in kids(net,'node'):actual[(one(node,'ref')[1],one(node,'pin')[1])]=one(net,'name')[1]
count=0
def same(*pins):
    global count
    assert len({actual[p] for p in pins})==1,[(p,actual[p]) for p in pins]
    count+=len(pins)-1
assert not {'U3','R12','R13','C12','Q1','R14'} & set(refs),'Ancien composant encore present'
same(('U1','24'),('J23','1'),('J3','2'),('J21','1'),('J22','1'),('R11','1'),*[('C'+str(i),'1') for i in [8,9,10,11,13]])
same(('U1','11'),*[('U1',n) for n in ['17','18','23','28']],('J23','2'),*[('U2',n) for n in ['1','5','9','15','17','21']],('J20','2'),('J21','2'),('J22','2'),('R10','2'),('R9','2'),('SW1','2'),*[('C'+str(i),'2') for i in [8,9,10,11,13]])
same(('U1','10'),('J23','3'))
same(('U1','9'),('J23','4'))
same(('U1','6'),('J23','6'))
same(('U1','30'),('J23','7'))
assert actual[('J23','5')]!=actual[('J23','1')],'VDD module court-circuite avec PWR'
same(('U1','29'),('R8','2'),('R9','1'))
same(('U2','13'),('U2','6'),('R8','1'))
same(('U1','12'),('J20','1'))
same(('U1','2'),('J21','3'));same(('U1','1'),('J21','4'))
same(('U1','7'),('J22','3'));same(('U1','8'),('J22','4'))
same(('U1','22'),('J22','5'),('SW1','1'),('R11','2'))
same(('U1','21'),('R10','1'))
same(('U2','14'),('J3','1'),('LBUCK1','2'),('COUT1','2'))
same(('U2','16'),('LBUCK1','1'));same(('U2','20'),('LBOOST1','2'))
same(('U2','2'),('LBOOST1','1'),('CIN1','1'),('CIN2','1'),('J4','2'))
same(('U2','19'),('U2','3'),('J19','2'),('CSTOR1','1'),('CBYP1','1'))
assert actual[('U2','6')]!=actual[('U2','19')],'VOUT_EN encore force a VSTOR'
same(('U2','8'),('ROUT2','1'),('ROK3','1'),('ROV2','1'))
same(('U2','12'),('ROUT2','2'),('ROUT1','1'))
same(('U2','7'),('ROV2','2'),('ROV1','1'))
same(('U2','11'),('ROK2','2'),('ROK1','1'))
same(('U2','10'),('ROK3','2'),('ROK2','1'))
same(('U2','4'),('CREF1','1'))
# AE1 est volontairement externe : exclue du netlist PCB, controle geometrique du schema.
sheet=read(P/'rak3172.kicad_sch')
ae=next(s for s in kids(sheet,'symbol') if prop(s,'Reference')=='AE1')
assert '868' in prop(ae,'Value') and one(ae,'in_bom')[1]=='no' and one(ae,'on_board')[1]=='no'
sym=next(s for s in kids(one(sheet,'lib_symbols'),'symbol') if s[1]==one(ae,'lib_id')[1])
pin=next(p for sub in kids(sym,'symbol') for p in kids(sub,'pin'))
x,y,a=map(float,one(ae,'at')[1:]);px,py,pa=map(float,one(pin,'at')[1:])
assert a==0
start=(round(x+px,4),round(y-py,4));graph={}
for wire in kids(sheet,'wire'):
    points=[tuple(map(float,k[1:])) for k in kids(one(wire,'pts'),'xy')]
    graph.setdefault(points[0],[]).append(points[1]);graph.setdefault(points[1],[]).append(points[0])
seen=set();todo=[start]
while todo:
    pnt=todo.pop()
    if pnt in seen:continue
    seen.add(pnt);todo.extend(graph.get(pnt,[]))
assert any(t[1]=='RF' and tuple(map(float,one(t,'at')[1:3])) in seen for t in kids(sheet,'label')),'Antenne sans raccord RF'
erc=json.loads((P/'erc.json').read_text(encoding='utf-8'))
violations=[v for s in erc['sheets'] for v in s['violations']]
errors=sum(v['severity']=='error' for v in violations)
assert errors==0,'Erreurs ERC presentes'
report={'date':'2026-10-26','revision':'0.5 supercapa 4V et IR direct','feuille_bq_identique':False,'modifications_bq_autorisees':'5 valeurs de resistance, precision 0.1%, VBAT_OK vers VOUT_EN et annotations','composants_bq_hors_reglage_conserves':True,'resistances_NC_et_C22_conservees':True,'sha256_reference_bq':hashlib.sha256(original).hexdigest(),'sha256_feuille_bq':hashlib.sha256((P/'alimentation.kicad_sch').read_bytes()).hexdigest(),'references_uniques':True,'comparaisons_de_connexions':count,'antenne_868MHz_raccordee':True,'antenne_externe_exclue_du_pcb_et_bom':True,'erc_erreurs':errors,'erc_avertissements':sum(v['severity']=='warning' for v in violations),'types_avertissements':[v['type'] for v in violations]}
(ROOT/'docs/verification_schema.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=False))
