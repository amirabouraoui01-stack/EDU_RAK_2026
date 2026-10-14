# Collier chien : mesure d'acceleration et LoRa

Revision 0.1, 14 octobre 2026. **Schema uniquement**, sans PCB ni firmware.

Ouvrir `collier_chien.kicad_pro` dans KiCad 10, puis le schema. Les symboles sont inclus dans `Collier.kicad_sym` et references par `sym-lib-table` : aucune bibliotheque privee de Dorian n'est necessaire. Le PDF contient les quatre feuilles.

## Architecture

- **U1 RAK3172(H)** : module LoRa EU868, alimentation nominale 3.31 V, programmation UART2/RUI3 et acces SWD.
- **U2 BQ25570** : recuperation d'energie, charge d'un supercondensateur externe et sortie buck.
- **U3 LIS2HH12** : acceleration XYZ, bus I2C2, adresse 0x1E, interruption INT1 vers PA1 pour le reveil.

La reference demandee oralement « BQ2770 » est interpretee comme **BQ25570**, conformement au schema et aux fiches techniques EDU_RAK_2026 indiques par l'utilisateur.

## Connecteurs

| Connecteur | Broches |
|---|---|
| J1 recuperation d'energie | 1 : entree DC positive, 2 : GND |
| J2 stockage | 1 : VBAT, 2 : GND ; supercondensateur externe >= 5.5 V |
| J3 antenne | centre : RF 50 ohms, blindage : GND ; antenne 868 MHz |
| J4 UART | 1 : 3V3, 2 : GND, 3 : TX module, 4 : RX module |
| J5 SWD | 1 : reference 3V3, 2 : GND, 3 : SWDIO, 4 : SWCLK, 5 : NRST |

Utiliser un adaptateur UART logique 3.3 V et croiser TX/RX. J4/J5 donnent acces au rail : eviter une alimentation simultanee par le programmateur et le BQ25570.

## Reglages de l'alimentation

Les resistances de programmation sont a 1 %. Avec VBIAS typique = 1.21 V :

| Reglage | Calcul | Resultat nominal |
|---|---|---|
| Sortie | 1.21 x (1 + 8.25/4.75) | 3.312 V |
| Fin de charge VBAT_OV | 1.5 x 1.21 x (1 + 8.66/7.15) | 4.013 V |
| Stockage faible | 1.21 x (1 + 8.25/4.12) | 3.633 V |
| Reprise | 1.21 x (1 + (8.25 + 0.681)/4.12) | 3.833 V |

VOC_SAMP relie a VSTOR selectionne le MPPT 80 %. EN actif bas est relie a GND. VBAT_OK commande directement VOUT_EN : la charge est coupee en dessous du seuil et reactivee apres recuperation du stockage. Le signal VBAT_OK est adapte au RAK par le pont R8/R9 (rapport 2/3), car sa tension haute est celle de VSTOR, pas celle de 3V3.

J1 suppose une **source DC de recuperation**, par exemple un petit panneau solaire adapte au MPPT 80 %. Une source piezoelectrique demanderait un redressement, une limitation de tension et un autre reglage MPPT. Ne pas raccorder directement une source alternative. Respecter les limites de VIN_DC de la fiche TI : demarrage a froid a partir d'environ 0.6 V typiques et entree de service <= 5.1 V.

## Points a dimensionner avant un PCB

Le choix de la source d'energie et de la capacite de stockage n'a pas ete fourni. J2 conserve donc le principe de stockage externe EDU RAK. L'autonomie depend de la capacite, de la fuite, de la puissance recoltee, de la cadence de mesure et des transmissions.

Le BQ25570 annonce jusqu'a 110 mA de sortie **typiques**, sans garantie de cette valeur dans toutes les conditions. La fiche RAK du depot indique 87 mA typiques en TX a 20 dBm / 868 MHz. Verifier au banc les pointes TX, la chute du 3V3, la marge du buck et le demarrage : les capacites de decouplage ne garantissent pas a elles seules la tenue d'une transmission. Ne pas supposer que le fonctionnement radio maximal est valide.

Les capacites 100 uF et 22 uF doivent conserver leur capacite utile sous polarisation ; leurs boitiers sont indicatifs pour cette revision de schema. Choisir les inductances a partir de leur courant de saturation, resistance serie et des limites maximales TI. Les composants ne constituent pas une nomenclature d'achat qualifiee.

## Verification et sources

Export PDF et netlist par KiCad 10.0.6. Verification automatique des nets de chaque broche par rapport a la table de connexions attendue. Le rapport `erc.json` contient le controle electrique KiCad. Un avertissement SA0/SDO contre le drapeau d'alimentation GND est attendu : en mode I2C, cette broche selectionne l'adresse et doit etre reliee a GND ; le symbole la declare bidirectionnelle pour son autre fonction SPI. Aucune exclusion globale des controles n'est appliquee.

Inspiration : `Hardware/Kicad/edu_rak_2026_kicad.zip`, archive presente dans ce depot. Le nouveau schema supprime le BME280, les connecteurs GPIO generaux et les elements de demonstration, et conserve les trois composants utiles au collier.

Sources : fiches `Datasheets/bq25570.pdf`, `Datasheets/RAK3172.pdf`, `Datasheets/LIS2HH12.pdf` du depot ; [TI BQ25570](https://www.ti.com/product/BQ25570), [ST LIS2HH12](https://www.st.com/resource/en/datasheet/lis2hh12.pdf), [RAK3172](https://docs.rakwireless.com/Product-Categories/WisDuo/RAK3172-Module/Datasheet/). Les symboles sont issus du projet EDU RAK et des bibliotheques installees KiCad ; leurs proprietes fabricant sont conservees.
