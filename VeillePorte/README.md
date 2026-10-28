# Projet KiCad retenu — VeillePorte

Ouvrir `veilleporte_complet.kicad_pro` pour modifier le schéma et le PCB.

- Schéma : `veilleporte_complet.kicad_sch`
- PCB : `veilleporte_complet.kicad_pcb` — contour 40 × 60 mm, 4 couches cuivre.
- Implantation côté composants : `implantation.png`
- Implantation côté dessous : `implantation_dos.png`
- Rapport DRC : `pcb_drc.json` — 0 erreur, 3 avertissements d’empreintes, 58 connexions restantes.
- PDF A2 : `veilleporte_complet.pdf`
- Netlist : `veilleporte_complet.net`
- Rapport ERC : `erc_complet.json`
- Bibliothèques d’empreintes : `fp-lib-table` et `footprints/`
- Bibliothèque de symboles : `sym-lib-table` et `VeillePorte.kicad_sym`

Le RAK3172 est placé au centre, l’antenne AE1 en bord de carte, et les connecteurs J3/J4/J19/J21/J22/J23/J10 sont conservés ; J3, J4 et J19 sont au dos. Le module Pololu 3692 se raccorde par J23 ; l’ordre du câble figure dans `../docs/CAPTEUR_IR.md`. Le schéma BQ25570 original reste conservé dans les références EDU_RAK.

**Routage de première passe :** 47 segments de piste et 11 vias. Les nets I²C, IR_INT, IR_XSHUT, SWDIO, SWCLK, UART2_TX, UART2_RX, NRST et BOOT0 sont routés. Six zones GND/PWR couvrent les quatre couches cuivre.

**État :** le routage est incomplet et la carte ne doit pas être fabriquée. Il reste 58 connexions non routées, dont la liaison RF vers AE1 et des réseaux de commutation/alimentation du BQ25570. Les trois avertissements DRC concernent des discordances d’empreinte sur J10, J22 et AE1. Le modèle CST est une référence 30 × 60 mm ; l’accord de l’antenne sur cette carte 40 × 60 mm et dans son boîtier reste à vérifier.
