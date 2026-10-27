# Préparer les essais de VeillePorte

[Accueil](../README.md) · [Projet KiCad retenu](../VeillePorte/veilleporte_complet.kicad_pro) · [Spécification](VEILLEPORTE.md)

Le schéma est disponible, mais aucun prototype VeillePorte n’a encore été validé sur banc. Ce guide liste les vérifications à effectuer après réalisation du PCB et du firmware.

## Alimentation

Confirmer la référence de la supercapacité et sa tension maximale avant branchement. Le BQ25570 est réglé pour une capacité limitée à 4 V : fin de charge vers 3,812 V, arrêt du buck vers 3,467 V, reprise vers 3,600 V, rail PWR proche de 3,118 V. J3 relie le buck au rail. Mesurer ces seuils, le rail et ses creux pendant les acquisitions et les émissions.

## Interfaces

| Interface | Affectation |
|---|---|
| J20 RF | Accès coaxial au réseau RF ; vérifier son usage avec l’antenne IFA imprimée |
| J21 UART2 | PWR, GND, TX module, RX module |
| J22 SWD | PWR, GND, SWDIO, SWCLK, NRST |
| J23 capteur | VIN, GND, SDA, SCL, NC, GPIO1, XSHUT |

Utiliser un adaptateur UART logique 3,3 V, croiser TX/RX et partager la masse. Ne pas alimenter PWR par deux sources en parallèle. Pour J23, suivre les noms des broches du module Pololu 3692, pas leur position physique : sa broche VDD reste non connectée.

## Qualification de la porte

Après développement du firmware, tester cible proche, cible éloignée, cible absente, mesure invalide, démarrage, lumière ambiante, mouvement lent et ouverture rapide. Régler deux seuils et une temporisation pour éviter les oscillations. Mesurer les ouvertures manquées et les délais de mise à jour.

Le mode ULP du capteur ne fournit pas les distances du mode normal. Vérifier que l’absence de cible et une panne de capteur produisent un état inconnu plutôt qu’une ouverture certaine.

## Énergie et radio

Mesurer courant de veille, courant moyen, pointes radio, tension du stockage et autonomie dans l’obscurité. Tester réseau absent, redémarrage, messages dupliqués et expiration des données sur le futur tableau de bord. Un paquet transmis n’est pas une preuve de réception.

Avant routage, réserver la zone de 30 × 20 mm de l’antenne IFA. J20 et AE1 partagent le réseau RF : déterminer la topologie d’alimentation RF pour éviter une branche ouverte ou une antenne externe en parallèle avec l’antenne imprimée.

