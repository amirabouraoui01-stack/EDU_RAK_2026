# Projet KiCad retenu — VeillePorte

Ouvrir `veilleporte_complet.kicad_pro` pour modifier le schéma et le PCB.

- Schéma : `veilleporte_complet.kicad_sch`
- PCB : `veilleporte_complet.kicad_pcb` — contour 40 × 60 mm, 4 couches cuivre.
- Implantation côté composants : `implantation.svg`
- Implantation côté dessous : `implantation_dos.svg`
- Rapport DRC : `pcb_drc.json` — 0 erreur de géométrie/isolement, 2 avertissements de discordance d’empreinte (J10/J22), 106 connexions à réaliser avant fabrication.
- PDF A2 : `veilleporte_complet.pdf`
- Netlist : `veilleporte_complet.net`
- Rapport ERC : `erc_complet.json`
- Variante en cours deux couches : `veilleporte_v2_2couches.kicad_pcb` (brouillon DRC : 19 erreurs, 61 connexions non résolues ; ne pas fabriquer).
- Bibliothèques d’empreintes : `fp-lib-table` et `footprints/`
- Bibliothèque de symboles : `sym-lib-table` et `VeillePorte.kicad_sym`

Le RAK3172 est placé au centre, l’antenne AE1 en bord de carte, et les connecteurs J3/J4/J19/J21/J22/J23/J10 sont conservés ; J3, J4 et J19 sont au dos. Le module Pololu 3692 se raccorde par J23 ; l’ordre du câble figure dans `../docs/CAPTEUR_IR.md`. Le schéma BQ25570 original reste conservé dans les références EDU_RAK.

**Répartition des couches demandée pour la prochaine révision quatre couches :**

| Couche | Usage prévu |
|---|---|
| F.Cu | Distribution des alimentations VCC et boucles locales du BQ25570 ; garder le trajet RF vers AE1 sur cette couche |
| In1.Cu | Plan GND continu, avec vias de masse depuis les composants SMD |
| In2.Cu | Signaux numériques issus du RAK3172 (I²C, IR, UART et SWD), avec vias d’échappement aux pastilles SMD |
| B.Cu | Autres signaux et connexions restantes |

Le PCB a été repris au stade implantation : 47 empreintes, aucune piste et aucun via. Un plan GND est préparé sur In1.Cu. Les autres couches sont disponibles pour le routage suivant cette répartition. Le RAK a été tourné pour rapprocher sa sortie RF de l’antenne ; les composants d’alimentation ont été regroupés autour du BQ25570, et le connecteur solaire J10 déplacé en bas à gauche, hors de la zone rayonnante. Le contour d’encombrement de l’antenne a été corrigé dans le PCB et sa bibliothèque locale, sans modifier son cuivre.

**État :** implantation préparée, routage à faire après validation de cette implantation. Le DRC affiche 106 connexions non résolues, ce qui est attendu pour ce PCB sans pistes ; la carte ne doit pas être fabriquée. Deux avertissements concernent les empreintes J10 et J22. Le modèle CST reste une référence 30 × 60 mm ; l’accord de l’antenne sur cette carte 40 × 60 mm et dans son boîtier reste à vérifier.
