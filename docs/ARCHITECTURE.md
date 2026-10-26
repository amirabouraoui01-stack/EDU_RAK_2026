# Architecture de VeillePorte

[Accueil](../README.md) · [Schéma PDF](../Collier_Chien/collier_chien.pdf)

## Mesure de mouvement

Le LIS2HH12 fournit trois axes d’accélération. Les résistances R12/R13 rappellent le bus I²C au rail PWR. CS à PWR sélectionne I²C ; SA0 à GND fixe l’adresse `0x1E`. RES est reliée à GND, INT2 est inutilisée.

| Signal | RAK3172 | LIS2HH12 |
|---|---|---|
| SDA | Broche 10 / PA11 | Broche 4 |
| SCL | Broche 9 / PA12 | Broche 1 |
| INT1 | Broche 6 / PA1 | Broche 12 |
| PWR | Broche 24 / VDD | Broches 2 / CS, 9 / Vdd, 10 / Vdd_IO |
| Masse | Broches GND | Broches 3 / SA0, 5 / RES, 6, 7, 8 |

La fréquence, la plage, le FIFO et les seuils de réveil seront configurés dans le firmware. La séquence lecture et transmission n’est pas encore implémentée.

## Radio à 868 MHz

Le RAK3172(H) fournit la sortie RF sur sa broche 12. J20 représente le connecteur RF de la future carte. **AE1** représente une antenne externe générique pour **868 MHz**, raccordée au même signal RF par label. Elle est exclue de la nomenclature et du PCB : aucun modèle d’antenne réel n’est encore choisi.

La fréquence est une spécification du projet ; le symbole ne réalise pas une adaptation RF. Le futur PCB devra prévoir une liaison 50 Ω et une antenne adaptée. La proximité du boîtier et du environnement de la porte doit être prise en compte lors des essais. Aucune portée ou performance d’antenne n’est annoncée comme mesurée.

## Énergie et stockage

La feuille BQ25570 est identique à celle d’EDU RAK. Les valeurs, les éléments NC et C22 sont conservés. La sortie buck est réglée à environ **3,36 V nominaux** : `1,21 × (1 + 8,25 / 4,64)`.

La commande EN active bas est reliée à GND **sur la feuille RAK3172**, par son label global d’origine. VOUT_EN est déjà reliée à VSTOR dans la feuille originale. J3 permet le raccordement de la sortie buck à PWR avec un cavalier. J4 donne accès au cavalier d’entrée et J19 au stockage sur VSTOR : ces interfaces restent celles du schéma pédagogique.

Le pont R8/R9, 1 MΩ / 2 MΩ, adapte VBAT_OK vers PA0, broche 29. La source de récupération et le stockage de VeillePorte restent à dimensionner ; l’autonomie et la tenue pendant les transmissions doivent être mesurées.

## Programmation

UART2 est accessible sur J21, SWD sur J22. BOOT0 est maintenu bas ; SW1 assure le reset. [Brochages et préparation des essais](MISE_EN_SERVICE.md).

## Détection d’ouverture à intégrer

Un contact magnétique passif et un aimant seront placés sur le cadre et la porte. La référence du contact, la logique ouvert/fermé, le GPIO libre, la polarisation et la protection du câble restent à choisir avant modification du schéma. Un circuit ouvert peut aussi correspondre à un câble coupé : cette première version ne distinguera pas automatiquement ces situations.

La communication visée est LoRaWAN avec passerelle, serveur réseau et application de réception. Le tableau de bord doit afficher la fraîcheur des données ; une absence de message ne prouve pas que la porte est fermée.
