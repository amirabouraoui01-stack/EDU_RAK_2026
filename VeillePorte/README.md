# Projet KiCad retenu — VeillePorte

Ouvrir `veilleporte_complet.kicad_pro` pour modifier le schéma et le PCB.

- Schéma : `veilleporte_complet.kicad_sch`
- PCB : `veilleporte_complet.kicad_pcb` — contour 40 × 60 mm, 4 couches cuivre.
- Implantation côté composants : `implantation.png`
- Implantation côté dessous : `implantation_dos.png`
- Rapport DRC : `pcb_drc.json` — 8 avertissements de sérigraphie/empreintes, 110 connexions à router.
- PDF A2 : `veilleporte_complet.pdf`
- Netlist : `veilleporte_complet.net`
- Rapport ERC : `erc_complet.json`
- Bibliothèques d’empreintes : `fp-lib-table` et `footprints/`
- Bibliothèque de symboles : `sym-lib-table` et `VeillePorte.kicad_sym`

Le RAK3172 est placé au centre, l’antenne AE1 en bord de carte, et les connecteurs J3/J4/J19/J21/J22/J23/J10 sont conservés ; J3, J4 et J19 sont au dos. Le module Pololu 3692 se raccorde par J23 ; l’ordre du câble figure dans `../docs/CAPTEUR_IR.md`. Le schéma BQ25570 original reste conservé dans les références EDU_RAK.

**État :** le placement et le contour sont préparés, mais le PCB n’est pas routé et ne doit pas être fabriqué en l’état. Le keepout de l’antenne couvre les quatre couches cuivre. Le modèle CST est une référence 30 × 60 mm ; l’accord de l’antenne sur ce contour 40 × 60 mm reste à vérifier dans CST.
