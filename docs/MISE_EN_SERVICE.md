# Préparer la mise en service

[Accueil](../README.md) · [Architecture](ARCHITECTURE.md)

Ce guide prépare les futurs essais : il n’existe pas encore de prototype VeillePorte validé.

## Ouvrir les fichiers

Ouvrir [le projet](../VeillePorte/veilleporte.kicad_pro) dans KiCad 10. La bibliothèque `VeillePorte.kicad_sym` fournit les symboles locaux ; la feuille BQ utilise ses symboles embarqués. Le [PDF](../VeillePorte/veilleporte.pdf) permet une lecture sans KiCad.

## Alimentation

Suivre les [réglages supercapacité 4 V](ALIMENTATION.md) et confirmer la référence du stockage avant branchement. J3 relie le buck au rail PWR d’environ 3,118 V. VOUT_EN est piloté par VBAT_OK pour couper puis relancer le buck selon l’énergie disponible. Les seuils doivent être mesurés sur banc. Ne pas connecter une alimentation externe en parallèle sur PWR.

## Interfaces

| Connecteur | Brochage |
|---|---|
| J20 RF | Centre RF 50 Ω ; blindage GND |
| J21 UART2 | 1 PWR ; 2 GND ; 3 TX module ; 4 RX module |
| J22 SWD | 1 référence PWR ; 2 GND ; 3 SWDIO ; 4 SWCLK ; 5 NRST |

Utiliser un adaptateur UART logique 3,3 V, croiser TX/RX et partager la masse. Éviter deux sources d’alimentation simultanées sur PWR. La méthode de programmation doit correspondre au firmware installé.

AE1 est un symbole indicatif : avant les essais radio, choisir et connecter sur J20 une antenne réelle adaptée à 868 MHz. La liaison RF et son environnement doivent être validés.

## Vérifier les fonctions

Après développement du firmware, vérifier le VL53L4CD à l’adresse I²C 7 bits `0x29`, XSHUT en drain ouvert et l’interruption PA1 directe, sans rappel interne. Suivre [le guide IR](CAPTEUR_IR.md).

| Essai | Mesures à relever |
|---|---|
| Démarrage | État de la source/du stockage, délai, rail PWR |
| Veille | Courant et configuration de réveil |
| Acquisition | Axes, fréquence et consommation |
| Émission | Courant de pointe, chute de PWR, durée, puissance RF |
| Autonomie | Capacité réelle, fuite, cadence, conditions de récupération |

Ces essais doivent précéder l’intégration finale à la porte d’essai.
