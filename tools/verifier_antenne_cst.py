"""Vérifie le seul modèle CST conservé pour l’antenne IFA 868 MHz."""
from pathlib import Path
import json,hashlib

P=Path(__file__).resolve().parents[1]/'VeillePorte/cst'
d=json.loads((P/'synthese_piste_fine.json').read_text(encoding='utf-8'))
assert hashlib.sha256((P/d['modele']).read_bytes()).hexdigest()==d['sha256_cst']
data=(P/d['export']).read_bytes()
assert hashlib.sha256(data).hexdigest()==d['sha256_export']
lines=data.decode('utf-8').splitlines()
assert 'GHz' in lines[0] and 'dB' in lines[0]
rows=[tuple(map(float,line.split())) for line in lines[2:] if line.strip()]
assert len(rows)==1001
assert all(b[0]>a[0] for a,b in zip(rows,rows[1:]))
near=min(rows,key=lambda item:abs(item[0]-.868))
assert abs(near[0]-.868)<1e-6
assert abs(near[1]-d['S11_868_dB'])<1e-6
assert min(rows,key=lambda item:item[1])[1]==d['S11_minimum_dB']
assert d['cellules']<=100000 and d['critere_energie_atteint']
geometry=(P/d['geometrie']).read_text(encoding='utf-8')
assert 'Terminal_cap' not in geometry and all(name in geometry for name in ['Retour_1','Retour_2','Retour_3'])
assert d['ancienne_plaque_supprimee'] and d['largeur_retour_mm']==.5
print('Modèle CST retenu, S11, géométrie et empreintes des exports cohérents.')
