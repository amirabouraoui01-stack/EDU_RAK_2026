# Projet KiCad retenu — VeillePorte

Ouvrir `veilleporte_complet.kicad_pro` pour modifier le schéma complet.

- Schéma : `veilleporte_complet.kicad_sch`
- PCB importé : `veilleporte.kicad_pcb` — composants du schéma importés, placement et routage à terminer
- Rapport DRC du PCB : `pcb_drc.json` — connexions à terminer avant fabrication
- PDF A2 : `veilleporte_complet.pdf`
- Netlist : `veilleporte_complet.net`
- Rapport ERC : `erc_complet.json`
- Bibliothèques d’empreintes : `fp-lib-table` et `footprints/`
- Bibliothèque de symboles : `sym-lib-table` et `VeillePorte.kicad_sym`

L’empreinte d’antenne imprimée AE1 est importée sur le PCB. Le module Pololu 3692 se raccorde par J23 ; l’ordre du câble figure dans `../docs/CAPTEUR_IR.md`. Le schéma BQ25570 original reste conservé dans les références EDU_RAK.
