# Collier chien - schema KiCad

Revision 0.2, 14 octobre 2026. Schema uniquement, conserve localement.

Ouvrir collier_chien.kicad_pro dans KiCad 10. Le PDF reprend les quatre feuilles.

## Alimentation originale conservee

La feuille alimentation.kicad_sch est une copie exacte, octet pour octet, de harvester.kicad_sch extrait de Hardware/Kicad/edu_rak_2026_kicad.zip. Aucun composant, fil, reglage ou symbole de cette feuille n'a ete modifie. Les resistances NC sont laissees telles quelles. C22 est conservee, sans modification ni exploitation pour le dimensionnement du collier, conformement a la demande. Les avertissements provenant de ces elements ne donnent lieu a aucune correction.

Le BQ25570 est celui du projet EDU RAK. Les valeurs et commandes originales sont conservees, y compris EN, VOUT_EN, VBAT_OK, les connecteurs de stockage et les reglages. La sortie buck est nominalement proche de 3.36 V avec ROUT1 = 4.64 M et ROUT2 = 8.25 M.

Le connecteur J3 de la feuille originale se trouve entre VOUT et le rail PWR : poser son cavalier pour alimenter le RAK et l'accelerometre, comme prevu par cette interface. Le drapeau PWR_FLAG sur la feuille MCU declare cette alimentation externe via le cavalier ; il ne remplace pas physiquement le cavalier. Le choix des commandes EN/VOUT_EN suit la feuille originale et doit etre applique sur le montage pour activer la sortie.

## Feuilles du collier

- RAK3172(H), EU868, alimentation PWR, programmation UART2/RUI3 et SWD.
- LIS2HH12 : acceleration XYZ par I2C2, adresse 0x1E, INT1 vers PA1.
- Surveillance VBAT_OK vers PA0 par le pont R8/R9, place sur la feuille MCU pour laisser la feuille BQ intacte.

Le signal VBAT_OK utilise VSTOR comme niveau haut. Le pont 1 M / 2 M en abaisse le niveau vers le MCU. La correspondance des niveaux et le fonctionnement aux seuils devront etre mesures.

## Connecteurs propres au collier

| Connecteur | Broches |
|---|---|
| J20 antenne 868 MHz | centre RF 50 ohms, blindage GND |
| J21 UART2 | 1 PWR, 2 GND, 3 TX module, 4 RX module |
| J22 SWD | 1 reference PWR, 2 GND, 3 SWDIO, 4 SWCLK, 5 NRST |

Utiliser des interfaces logiques 3.3 V. Croiser TX/RX pour UART. Eviter deux sources d'alimentation simultanees. Les numeros J20 a J22 evitent les collisions avec les connecteurs originaux de la feuille BQ.

## Verification et limites

Les fichiers PDF, netlist et rapport ERC sont regeneres par KiCad. Les controles portent sur l'integration et les connexions des feuilles du collier. Les avertissements de la feuille BQ originale sont conserves et ne doivent pas etre interpretes comme des corrections a effectuer dans cette demande. SA0/SDO du LIS2HH12, declaree bidirectionnelle par son symbole, est reliee a GND pour fixer l'adresse en mode I2C.

La source de recuperation d'energie, le stockage externe et l'autonomie restent a dimensionner selon l'usage. Les pointes de courant pendant les emissions LoRa et la tenue du rail doivent etre validees sur banc avant PCB. Aucun routage ni firmware n'est fourni.

Sources : archive KiCad EDU_RAK_2026 et fiches bq25570.pdf, RAK3172.pdf et LIS2HH12.pdf presentes dans Datasheets.
