# Schéma électrique retenu

[Accueil](../README.md) · [Projet KiCad](../VeillePorte/veilleporte_complet.kicad_pro) · [Schéma](../VeillePorte/veilleporte_complet.kicad_sch) · [PDF A2](../VeillePorte/veilleporte_complet.pdf)

Le seul schéma de conception actif est une page A2. Il réunit le BQ25570, le RAK3172, le connecteur du module VL53L4CD Pololu 3692, l’antenne IFA 868 MHz, UART, SWD, reset, BOOT0 et le suivi du stockage.

J23 est le câble vers le module, pas son brochage physique. Sa broche 5 est non connectée. Les liaisons d’alimentation, de masse, I²C, interruption, XSHUT et interfaces sont tracées dans le schéma.

## Antenne

AE1 utilise l’empreinte locale VeillePorte_Antennes:IFA_868_CST_30x20_PisteFine. La broche 1 est sur /RF ; la broche 2 est sur le net de masse du projet. J20 est aussi sur le réseau RF : le routage du PCB devra choisir la topologie RF finale.

## Vérifications actuelles

Le netlist KiCad compte 45 composants et 43 groupes de connexions. Le rapport ERC indique 0 erreur et 3 avertissements conservés : symbole BQ intégré différent de la bibliothèque, alias de masse EN/GND et labels local/global de masse. Le script de vérification contrôle le netlist final, le raccordement de l’antenne et les réglages autorisés du BQ25570 à partir de l’archive EDU RAK.

- [Netlist finale](../VeillePorte/veilleporte_complet.net)
- [Rapport ERC final](../VeillePorte/erc_complet.json)
- [Rapport de vérification](verification_schema_complet.json)

Le PCB, le firmware et les essais physiques restent à réaliser. Le schéma ne valide pas le fonctionnement sur banc.

