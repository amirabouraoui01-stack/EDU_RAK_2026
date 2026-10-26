"""Recalcule les seuils depuis la netlist et controle la marge supercapacite 4 V."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'VeillePorte/veilleporte.net').read_text(encoding='utf-8')
def value(ref):
    match=re.search(r'\(comp\s+\(ref "'+re.escape(ref)+r'"\).*?\(value "([^"]+)"\)',text,re.S)
    assert match,ref
    raw=match[1];return float(raw.rstrip('Mk'))*({'M':1e6,'k':1e3}.get(raw[-1],1))
ov=1.815*(1+value('ROV2')/value('ROV1'))
low=1.21*(1+value('ROK2')/value('ROK1'))
high=1.21*(1+(value('ROK2')+value('ROK3'))/value('ROK1'))
out=1.21*(1+value('ROUT2')/value('ROUT1'))
assert 1.95<low<high<ov<4
assert ov*1.022<4,'Marge surtension insuffisante'
for group in [('ROV1','ROV2'),('ROK1','ROK2','ROK3'),('ROUT1','ROUT2')]:
    assert 11e6<=sum(value(ref) for ref in group)<=13e6,group
# Majoration conservative de regulation et tolerance pour l'interface Pololu/RAK.
assert out*.978>2.6 and out*1.022<3.6
assert .7*out*1.022<2.6,'Marge de niveau haut IR insuffisante'
assert value('R8')==1e6 and value('R9')==3.3e6
stored=json.loads((ROOT/'docs/reglage_bq25570.json').read_text(encoding='utf-8'))
for key,v in [('VBAT_OV_nominal_V',ov),('VBAT_OK_bas_nominal_V',low),('VBAT_OK_haut_nominal_V',high),('VOUT_nominal_V',out)]:
    assert abs(stored[key]-v)<1e-9,(key,v)
print(f'OV {ov:.4f} V ; bas {low:.4f} V ; haut {high:.4f} V ; VOUT {out:.4f} V ; marges statiques OK.')
