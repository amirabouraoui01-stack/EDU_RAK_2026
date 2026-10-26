# Schéma complet sur une page

[Accueil](../README.md) · [Projet KiCad](../VeillePorte/veilleporte_complet.kicad_pro) · [Schéma](../VeillePorte/veilleporte_complet.kicad_sch) · [PDF](../VeillePorte/veilleporte_complet.pdf)

La vue recommandée est `veilleporte_complet.kicad_pro`. Elle contient une seule page A2 avec l’alimentation BQ25570, le RAK3172, le connecteur du module IR, l’antenne indicative, UART, SWD, BOOT/reset et le suivi du stockage.

Les liaisons entre fonctions sont tracées : alimentation et masse, I²C SDA/SCL, interruption IR, XSHUT, état du stockage, UART, SWD, reset, BOOT0 et RF. Les symboles et étiquettes PWR/GND répétés restent des connexions conventionnelles aux mêmes rails. Un croisement de fils sans point ne représente pas une jonction ; les points indiquent les dérivations.

J23 est le câble vers le module Pololu 3692 externe, pas son brochage physique. La broche 5 de J23 reste non connectée ; suivre les noms de pastilles décrits dans [le guide IR](CAPTEUR_IR.md).

## Contrôles

Les 44 composants et les 43 groupes de connexions de la netlist sont identiques à ceux de la version par feuilles. Le contrôle ERC donne 0 erreur et 3 avertissements conservés (symbole BQ d’origine, noms EN/GND et labels local/global de masse). [Rapport d’équivalence](verification_schema_complet.json) · [ERC complet](../VeillePorte/erc_complet.json).

Après réexport des deux netlists et du rapport ERC : `python tools/verifier_schema_complet.py`. Le contrôle compare les ensembles de broches connectées, indépendamment du nom choisi par KiCad pour chaque net.

## Fichiers conservés

`veilleporte.kicad_pro` et ses feuilles restent la référence de la révision 0.5 ayant servi à créer cette vue. Une future modification électrique de la vue complète devra être reportée dans cette référence ou explicitement traitée comme une nouvelle révision avant comparaison. La vue complète a sa propre netlist et son rapport ERC pour éviter de mélanger les exports.

Le PDF est conçu pour le format A2 : zoomer à l’écran ou imprimer au format approprié. Le PCB IR, le firmware et les essais physiques restent à réaliser ; cette réunion des feuilles ne valide pas le fonctionnement sur banc.
