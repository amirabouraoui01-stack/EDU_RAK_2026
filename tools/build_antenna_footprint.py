from pathlib import Path
import ast,re,json,uuid
P=Path(__file__).resolve().parents[1]/'VeillePorte';source=P/'cst/veilleporte_868_piste_basse.vba.txt'
s=source.read_text(encoding='utf-8');params={k:float(v) for k,v in re.findall(r'StoreParameter "([^"]+)", "([^"]+)"',s)}
def calc(expr):
    def visit(n):
        if isinstance(n,ast.Expression):return visit(n.body)
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)):return n.value
        if isinstance(n,ast.Name):return params[n.id]
        if isinstance(n,ast.UnaryOp) and isinstance(n.op,ast.USub):return -visit(n.operand)
        if isinstance(n,ast.BinOp):
            a,b=visit(n.left),visit(n.right)
            if isinstance(n.op,ast.Add):return a+b
            if isinstance(n.op,ast.Sub):return a-b
            if isinstance(n.op,ast.Mult):return a*b
            if isinstance(n.op,ast.Div):return a/b
        raise ValueError(expr)
    return visit(ast.parse(expr,mode='eval'))
rects=[]
for block in re.findall(r'With Brick\n(.*?)End With',s,re.S):
    name=re.search(r'\.Name "([^"]+)"',block)[1]
    if name in ['PCB','GND_top','GND_bottom','GND_bridge']:continue
    x1,x2=[calc(v) for v in re.search(r'\.Xrange "([^"]+)", "([^"]+)"',block).groups()]
    y1,y2=[calc(v) for v in re.search(r'\.Yrange "([^"]+)", "([^"]+)"',block).groups()]
    assert x1<x2 and y1<y2
    rects.append((name,x1,x2,y1,y2))
assert 'Terminal_cap' not in [r[0] for r in rects]
name='IFA_868_CST_30x20_PisteFine';lib=P/'footprints/VeillePorte_Antennes.pretty';lib.mkdir(exist_ok=True)
f=lambda v:f'{v:.6f}'.rstrip('0').rstrip('.') if v else '0'
pr=[]
for _,x1,x2,y1,y2 in rects:
    # Repere KiCad = CST translate au pied RF et miroir de l'axe Y.
    points=[(x1-6,40.51-y1),(x2-6,40.51-y1),(x2-6,40.51-y2),(x1-6,40.51-y2)]
    pr.append('(gr_poly (pts '+' '.join(f'(xy {f(x)} {f(y)})' for x,y in points)+') (width 0) (fill yes))')
out=f'''(footprint "{name}" (version 20241229) (generator "pcbnew")
 (layer "F.Cu")
 (descr "Antenne IFA 868 MHz : copie 2D du modele CST piste fine ; RF=1 GND=2, court-circuit DC intentionnel")
 (tags "antenna IFA 868MHz CST VeillePorte")
 (attr smd exclude_from_pos_files exclude_from_bom)
 (net_tie_pad_groups "1,2")
 (property "Reference" "AE" (at 10 -22 0) (layer "F.SilkS") (effects (font (size 1 1))))
 (property "Value" "IFA_868_CST" (at 10 -23.5 0) (layer "F.Fab") (effects (font (size 1 1))))
 (fp_text user "RF 1" (at 0 2.5) (layer "F.Fab") (effects (font (size .7 .7))))
 (fp_text user "GND 2" (at -4 2.5) (layer "F.Fab") (effects (font (size .7 .7))))
 (fp_text user "ZONE ANTENNE : PAS DE CUIVRE SOUS LES PISTES" (at 9 -20.8) (layer "F.Fab") (effects (font (size .65 .65))))
 (fp_rect (start -6 -19.5) (end 24 40.5) (stroke (width .1) (type dash)) (fill none) (layer "F.Fab"))
 (fp_rect (start -6 .5) (end 24 40.5) (stroke (width .1) (type dash)) (fill none) (layer "Dwgs.User"))
 (fp_rect (start -6.25 -19.75) (end 24.25 1.75) (stroke (width .05) (type default)) (fill none) (layer "F.CrtYd"))
 (fp_rect (start -6.25 -19.75) (end 24.25 1.75) (stroke (width .05) (type default)) (fill none) (layer "B.CrtYd"))
 (pad "1" smd custom (at 0 -.01) (size 1 .02) (layers "F.Cu" "F.Mask")
  (options (clearance outline) (anchor rect)) (primitives {' '.join(pr)}))
 (pad "2" smd rect (at -4 1) (size 1 1) (layers "F.Cu" "F.Mask"))
 (pad "2" smd rect (at 0 1) (size 1 1) (layers "F.Cu" "F.Mask"))
 (zone (net 0) (net_name "") (layers "F.Cu" "B.Cu") (hatch edge .5)
  (connect_pads (clearance 0)) (min_thickness .25) (filled_areas_thickness no)
  (keepout (tracks not_allowed) (vias not_allowed) (pads allowed) (copperpour not_allowed) (footprints allowed))
  (fill (thermal_gap .3) (thermal_bridge_width .3))
  (polygon (pts (xy -6 .5) (xy -.75 .5) (xy -.75 -.15) (xy .75 -.15) (xy .75 .5) (xy 24 .5) (xy 24 -19.5) (xy -6 -19.5))))
)'''
(lib/(name+'.kicad_mod')).write_text(out+'\n',encoding='utf-8',newline='\n')
table=P/'fp-lib-table';t=table.read_text(encoding='utf-8');entry='  (lib (name "VeillePorte_Antennes") (type "KiCad") (uri "${KIPRJMOD}/footprints/VeillePorte_Antennes.pretty") (options "") (descr "Antennes imprimees issues des modeles CST VeillePorte"))\n'
if 'VeillePorte_Antennes' not in t:t=t.rstrip()[:-1]+entry+')\n';table.write_text(t,encoding='utf-8',newline='\n')
report={'empreinte':'VeillePorte_Antennes:'+name,'source_cst':str(source.name),'rectangles_radiateur':len(rects),'borne_1':'RF','borne_2':'GND','net_tie':'1,2 : court-circuit DC de l IFA volontaire','repere':'xKiCad=xCST-6 ; yKiCad=40.5-yCST ; ancre pad1 y=-0.01 mm','zone_antenne_mm':[30,20],'PCB_reference_mm':[30,60,.8],'plan_masse':'A creer sur le PCB : 30x40mm, deux faces et liaisons entre masses ; non fourni comme cuivre plein dans l empreinte','rectangles_CST':rects,'modes_soudure':'pas de pate a braser sur le radiateur ; ouverture de masque sur les pistes'}
(P.parent/'docs/empreinte_antenne.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Empreinte creee :',lib/(name+'.kicad_mod'),'rectangles :',len(rects))
