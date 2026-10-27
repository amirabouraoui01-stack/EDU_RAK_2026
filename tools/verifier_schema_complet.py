"""Vérifie les fichiers actifs, le BQ source, les réseaux RF et l’antenne."""
import json,re,hashlib,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'VeillePorte'
def parse(text):
    stack=[];root=None
    for t in re.findall(r'"(?:\\.|[^"\\])*"|[^\s()]+|[()]',text):
        if t=='(':
            n=[]
            if stack:stack[-1].append(n)
            else:root=n
            stack.append(n)
        elif t==')':stack.pop()
        else:stack[-1].append(json.loads(t,strict=False) if t.startswith('"') else t)
    return root
def kids(n,k):return [x for x in n if isinstance(x,list) and x and x[0]==k]
def one(n,k):return next(iter(kids(n,k)))
def read(name):return parse((P/name).read_text(encoding='utf-8'))
def properties(symbol):return {item[1]:item[2] for item in kids(symbol,'property')}

sch=read('veilleporte_complet.kicad_sch')
netlist=read('veilleporte_complet.net')
components=kids(one(netlist,'components'),'comp')
nets=kids(one(netlist,'nets'),'net')
assert len(components)==45 and len(nets)==43
refs={one(comp,'ref')[1]:comp for comp in components}
assert len(refs)==len(components),'References dupliquees dans la netlist'
assert not {'U3','R12','R13','C12','Q1','R14'} & set(refs),'Composant de l’ancienne détection encore présent'

antenna=refs['AE1']
assert one(antenna,'value')[1]=='Antenne IFA imprimée 868 MHz'
assert one(antenna,'footprint')[1]=='VeillePorte_Antennes:IFA_868_CST_30x20_PisteFine'
net_of={(one(node,'ref')[1],one(node,'pin')[1]):one(net,'name')[1]
        for net in nets for node in kids(net,'node')}
assert net_of[('AE1','1')]==net_of[('U1','12')]==net_of[('J20','1')]=='/RF'
assert net_of[('AE1','2')]=="'EN"
assert net_of[('U2','6')]==net_of[('U2','13')] and net_of[('U2','6')]!=net_of[('U2','19')]

source_zip=ROOT/'references/EDU_RAK_2026/Hardware/Kicad/edu_rak_2026_kicad.zip'
with zipfile.ZipFile(source_zip) as archive:
    source_name=next(name for name in archive.namelist() if name.endswith('harvester.kicad_sch'))
    source_bytes=archive.read(source_name)
source=parse(source_bytes.decode('utf-8'))
original={properties(symbol)['Reference']:properties(symbol) for symbol in kids(source,'symbol')}
active={properties(symbol)['Reference']:properties(symbol) for symbol in kids(sch,'symbol')}
assert original.keys() <= active.keys(),'Composant du BQ25570 source manquant'
allowed={'ROV1':'6.19M','ROV2':'6.81M','ROK3':'464k','ROUT1':'4.99M','ROUT2':'7.87M'}
precision=set(allowed)|{'ROK1','ROK2'}
for ref,old in original.items():
    new=active[ref]
    ignored={'Tolerance'} if ref in precision else set()
    assert old.keys()-ignored==new.keys()-ignored,f'Champs modifiés hors réglage autorisé : {ref}'
    for field,value in old.items():
        if field=='Value' and ref in allowed:
            assert new[field]==allowed[ref]
        else:
            assert new[field]==value,f'Champ BQ modifié : {ref}.{field}'
    if ref in precision:assert new.get('Tolerance')=='0.1%',f'Précision non spécifiée : {ref}'
for ref in ('C22','ROK1B1','ROK2B1','ROK3B1','ROV1B1','ROV2B1','ROUT1B1','ROUT2B1'):
    assert active[ref]['Value']==original[ref]['Value'],f'Valeur NC/C22 modifiée : {ref}'

erc=json.loads((P/'erc_complet.json').read_text(encoding='utf-8'))
vs=[v for s in erc['sheets'] for v in s['violations']]
assert not [v for v in vs if v['severity']=='error']
report={'projet_final_unique':True,'format':'A2','composants_netlist':len(components),'groupes_de_connexions':len(nets),'antenne_empreinte':one(antenna,'footprint')[1],'antenne_RF':'/RF','antenne_masse':"'EN",'BQ_original_composants_conserves':len(original),'BQ_valeurs_autorisees':allowed,'resistances_precision_0_1%':sorted(precision),'NC_et_C22_conserves':True,'sha256_BQ_source':hashlib.sha256(source_bytes).hexdigest(),'erc_erreurs':0,'erc_avertissements':len(vs),'sha256_schema_complet':hashlib.sha256((P/'veilleporte_complet.kicad_sch').read_bytes()).hexdigest()}
(ROOT/'docs/verification_schema_complet.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
