"""Compare toutes les connexions de la page complete avec la version par feuilles."""
import json,re,hashlib
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
def signature(name, without_antenna=False):
    d=read(name)
    components={(one(n,'ref')[1],one(n,'value')[1]) for n in kids(one(d,'components'),'comp')}
    if without_antenna:components={item for item in components if item[0]!='AE1'}
    nets=set()
    for net in kids(one(d,'nets'),'net'):
        nodes={(one(n,'ref')[1],one(n,'pin')[1]) for n in kids(net,'node')}
        if without_antenna:
            nodes={node for node in nodes if node[0]!='AE1'}
        if nodes:nets.add(frozenset(nodes))
    return components,nets
oldc,old=signature('veilleporte.net');newc,new=signature('veilleporte_complet.net',without_antenna=True)
assert oldc==newc,('Composants differents',oldc-newc,newc-oldc)
assert old==new,('Connexions differentes hors antenne',old-new,new-old)
full=read('veilleporte_complet.net')
antenna=next(c for c in kids(one(full,'components'),'comp') if one(c,'ref')[1]=='AE1')
assert one(antenna,'footprint')[1]=='VeillePorte_Antennes:IFA_868_CST_30x20_PisteFine'
netlist_nets=kids(one(full,'nets'),'net')
def antenna_on(net_name,pin):
    net=next(n for n in netlist_nets if one(n,'name')[1]==net_name)
    return ('AE1',pin) in {(one(node,'ref')[1],one(node,'pin')[1]) for node in kids(net,'node')}
assert antenna_on('/RF','1')
assert antenna_on("'EN",'2')
erc=json.loads((P/'erc_complet.json').read_text(encoding='utf-8'))
vs=[v for s in erc['sheets'] for v in s['violations']]
assert not [v for v in vs if v['severity']=='error']
report={'page_unique':True,'format':'A2','composants_netlist':len(kids(one(full,'components'),'comp')),'groupes_de_connexions':len(netlist_nets),'connexions_de_reference_identiques_hors_antenne':True,'antenne_empreinte':'VeillePorte_Antennes:IFA_868_CST_30x20_PisteFine','antenne_RF':'/RF','antenne_masse':"'EN",'erc_erreurs':0,'erc_avertissements':len(vs),'sha256_schema_complet':hashlib.sha256((P/'veilleporte_complet.kicad_sch').read_bytes()).hexdigest()}
(ROOT/'docs/verification_schema_complet.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
