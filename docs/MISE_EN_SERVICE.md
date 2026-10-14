# Préparer la mise en service

[Accueil](../README.md) · [Architecture](ARCHITECTURE.md)

Ce guide prépare les futurs essais : il n’existe pas encore de prototype du collier validé.

## Ouvrir les fichiers

Ouvrir [le projet](../Collier_Chien/collier_chien.kicad_pro) dans KiCad 10. La bibliothèque `Collier.kicad_sym` fournit les symboles locaux ; la feuille BQ utilise ses symboles embarqués. Le [PDF](../Collier_Chien/collier_chien.pdf) permet une lecture sans KiCad.

## Alimentation

Choisir une source et un stockage compatibles avec [la fiche BQ25570](../references/EDU_RAK_2026/Datasheets/bq25570.pdf). Vérifier polarité, tension, fuite et capacité. Les connexions J4 et J19 restent celles du schéma original. EN est reliée à GND depuis la feuille RAK ; VOUT_EN est reliée à VSTOR sur la feuille BQ.

Le cavalier **J3 de la feuille BQ** relie la sortie buck à PWR. Vérifier le rail avant de brancher les autres blocs : la valeur nominale est environ 3,36 V, avec des tolérances et une dépendance aux conditions de charge.

## Interfaces

| Connecteur | Brochage |
|---|---|
| J20 RF | Centre RF 50 Ω ; blindage GND |
| J21 UART2 | 1 PWR ; 2 GND ; 3 TX module ; 4 RX module |
| J22 SWD | 1 référence PWR ; 2 GND ; 3 SWDIO ; 4 SWCLK ; 5 NRST |

Utiliser un adaptateur UART logique 3,3 V, croiser TX/RX et partager la masse. Éviter deux sources d’alimentation simultanées sur PWR. La méthode de programmation doit correspondre au firmware installé.

AE1 est un symbole indicatif : avant les essais radio, choisir et connecter sur J20 une antenne réelle adaptée à 868 MHz. La liaison RF et son environnement doivent être validés.

## Vérifier les fonctions

Après développement du firmware : vérifier la réponse I²C du LIS2HH12 à `0x1E`, lire les axes et relever INT1 sur PA1. Tester le réveil et le FIFO si utilisé. Consigner la plage et la fréquence configurées.

| Essai | Mesures à relever |
|---|---|
| Démarrage | État de la source/du stockage, délai, rail PWR |
| Veille | Courant et configuration de réveil |
| Acquisition | Axes, fréquence et consommation |
| Émission | Courant de pointe, chute de PWR, durée, puissance RF |
| Autonomie | Capacité réelle, fuite, cadence, conditions de récupération |

Ces essais doivent précéder l’intégration finale au collier.
