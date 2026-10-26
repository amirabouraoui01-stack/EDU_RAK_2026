"""Verifie les exports natifs CST et leur correspondance aux fichiers publies."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1]/'VeillePorte/cst'
report=json.loads((P/'synthese_cst.json').read_text(encoding='utf-8'))
for sample in [report['reference'],report['controle_meme_geometrie']['maillage_initial'],report['controle_meme_geometrie']['maillage_modere']]:
    assert hashlib.sha256((P/sample['modele']).read_bytes()).hexdigest()==sample['sha256_cst']
    data=(P/sample['export']).read_bytes()
    assert hashlib.sha256(data).hexdigest()==sample['sha256_export']
    text=data.decode();assert 'GHz' in text.splitlines()[0] and 'dB' in text.splitlines()[0]
    rows=[]
    for line in text.splitlines()[2:]:
        if line.strip():rows.append(tuple(map(float,line.split())))
    assert len(rows)==sample['echantillons']==1001
    assert all(b[0]>a[0] for a,b in zip(rows,rows[1:]))
    near=min(rows,key=lambda v:abs(v[0]-.868))
    assert abs(near[0]-.868)<1e-6
    assert abs(near[1]-sample['S11_868_dB'])<1e-6
    assert sample['cellules']<=100000 and sample['critere_energie_atteint']
assert report['reference']['S11_868_dB']<=-10
print('Exports CST et empreintes des modeles coherents ; reference adaptee a 868 MHz dans le modele simplifie.')
