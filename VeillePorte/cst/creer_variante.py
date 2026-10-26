"""Prepare une macro CST native pour une variante IFA. Ne lance pas CST."""
import argparse,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--nom',default='veilleporte_868_accord');p.add_argument('--cap-x',type=float,default=8.5);p.add_argument('--feed-x',type=float,default=6);p.add_argument('--right-x',type=float,default=28);p.add_argument('--maillage',type=int,default=12)
a=p.parse_args();assert re.fullmatch(r'[A-Za-z0-9_]+',a.nom)
P=Path(__file__).resolve().parent;q=lambda path:str(path).replace('\\','/')
if (P/(a.nom+'.cst')).exists():raise SystemExit('Ce modele existe deja ; choisir un autre --nom pour conserver les resultats.')
assert .5<a.cap_x<28 and 2.5<a.feed_x<27
assert 27<a.right_x<29.5
assert 8<=a.maillage<=40
lines=(P/'geometrie_ifa.vba.txt').read_text(encoding='utf-8').replace('StoreParameter "x_feed", "6"',f'StoreParameter "x_feed", "{a.feed_x}"').replace('.Set "StepsPerWaveNear", "12"',f'.Set "StepsPerWaveNear", "{a.maillage}"').splitlines()
lines=[line.replace('Solver.FrequencyRange "0.6", "1.2"','Solver.FrequencyRange "0.6", "1.136"') for line in lines]
lines=[line.replace('StoreParameter "x_right", "28"',f'StoreParameter "x_right", "{a.right_x}"').replace('StoreParameter "x_end", "28"',f'StoreParameter "x_end", "{a.right_x}"') for line in lines]
lines=[line.replace('.Set "StepsPerBoxNear", "15"',f'.Set "StepsPerBoxNear", "{max(15,round(a.maillage*1.25))}"') for line in lines]
lines[:0]=[f'StoreParameter "cap_x", "{a.cap_x}"']
extra=['With Brick','.Reset','.Name "Terminal_cap"','.Component "VeillePorte"','.Material "PEC"','.Xrange "0.5", "cap_x"','.Yrange "54.5", "59.5"','.Zrange "pcb_h", "pcb_h+cu_t"','.Create','End With','Solid.Add "VeillePorte:Antenna", "VeillePorte:Terminal_cap"']
i=lines.index('With DiscretePort');lines[i:i]=extra
macro=['Option Explicit','Sub Main()','On Error GoTo Failed','Dim f As Integer','Dim s As String','Dim detail As String','f = FreeFile',f'Open "{q(P/(a.nom+".log"))}" For Output As #f','Print #f, "RUN_STARTED"','Close #f','s = ""']
for line in lines:macro.append('s = s & "'+line.replace('"','""')+'" & vbCrLf')
macro+=['AddToHistory "VeillePorte - IFA capacite terminale", s',f'SaveAs "{q(P/(a.nom+".cst"))}", True','f = FreeFile',f'Open "{q(P/(a.nom+".log"))}" For Append As #f','Print #f, "MODEL_BUILT"','Close #f','Solver.Start','Save','SelectTreeItem "1D Results\\S-Parameters\\S1,1"','With ASCIIExport','.Reset',f'.FileName "{q(P/("s11_"+a.nom+".txt"))}"','.Execute','End With','f = FreeFile',f'Open "{q(P/(a.nom+".log"))}" For Append As #f','Print #f, "S11_EXPORTED"','Close #f','Exit Sub','Failed:','detail = Err.Description','f = FreeFile',f'Open "{q(P/(a.nom+".log"))}" For Append As #f','Print #f, "ERROR: " & detail','Close #f','End Sub']
(P/(a.nom+'.bas')).write_text('\r\n'.join(macro)+'\r\n',encoding='utf-8')
(P/(a.nom+'.vba.txt')).write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(P/(a.nom+'.bas'))
