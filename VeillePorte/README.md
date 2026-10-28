# Projet KiCad retenu — VeillePorte

Ouvrir `veilleporte_complet.kicad_pro` pour modifier le schéma complet.

- Schéma : `veilleporte_complet.kicad_sch`
- PCB : `veilleporte_complet.kicad_pcb` — associé au projet et au schéma sous le même nom
- Aperçu du placement : `implantation.png`
- Rapport DRC : `pcb_drc.json` — 0 erreur, 28 avertissements; le PCB reste à router
- PDF A2 : `veilleporte_complet.pdf`
- Netlist : `veilleporte_complet.net`
- Rapport ERC : `erc_complet.json`
- Bibliothèques d’empreintes : `fp-lib-table` et `footprints/`
- Bibliothèque de symboles : `sym-lib-table` et `VeillePorte.kicad_sym`

Le module Pololu 3692 se raccorde par J23 ; l’ordre du câble figure dans `../docs/CAPTEUR_IR.md`. Le schéma BQ25570 original reste conservé dans les références EDU_RAK.
