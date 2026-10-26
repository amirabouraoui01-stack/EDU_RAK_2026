# Architecture de VeillePorte

[Accueil](../README.md) · [Schéma PDF](../VeillePorte/veilleporte.pdf)

## Détection IR

Le module Pololu 3692 avec VL53L4CD remplace le LIS2HH12. SDA va à PA11 (broche 10), SCL à PA12 (broche 9). GPIO1 est adapté de 2,8 V vers PWR par Q1 BSS138 et R14 100 kΩ avant PA1 (broche 6). XSHUT va à PB5 (broche 30), piloté exclusivement en drain ouvert. [Brochage et contraintes](CAPTEUR_IR.md).

## Radio à 868 MHz

Le RAK3172(H) fournit la sortie RF sur sa broche 12. J20 représente le connecteur RF de la future carte. **AE1** représente une antenne externe générique pour **868 MHz**, raccordée au même signal RF par label. Elle est exclue de la nomenclature et du PCB : aucun modèle d’antenne réel n’est encore choisi.

La fréquence est une spécification du projet ; le symbole ne réalise pas une adaptation RF. Le futur PCB devra prévoir une liaison 50 Ω et une antenne adaptée. La proximité du boîtier et du environnement de la porte doit être prise en compte lors des essais. Aucune portée ou performance d’antenne n’est annoncée comme mesurée.

## Énergie et stockage

La feuille BQ25570 est identique à celle d’EDU RAK. Les valeurs, les éléments NC et C22 sont conservés. La sortie buck est réglée à environ **3,36 V nominaux** : `1,21 × (1 + 8,25 / 4,64)`.

La commande EN active bas est reliée à GND **sur la feuille RAK3172**, par son label global d’origine. VOUT_EN est déjà reliée à VSTOR dans la feuille originale. J3 permet le raccordement de la sortie buck à PWR avec un cavalier. J4 donne accès au cavalier d’entrée et J19 au stockage sur VSTOR : ces interfaces restent celles du schéma pédagogique.

Le pont R8/R9, 1 MΩ / 2 MΩ, adapte VBAT_OK vers PA0, broche 29. La source de récupération et le stockage de VeillePorte restent à dimensionner ; l’autonomie et la tenue pendant les transmissions doivent être mesurées.

## Programmation

UART2 est accessible sur J21, SWD sur J22. BOOT0 est maintenu bas ; SW1 assure le reset. [Brochages et préparation des essais](MISE_EN_SERVICE.md).

## État de porte

Le capteur vise une cible fixée à la porte. Distance courte stable : fermé ; distance plus grande valide : ouvert. La disparition de cible et les mesures invalides doivent être qualifiées sur banc, avec un état inconnu pour les cas ambigus. La communication prévue reste LoRaWAN ; aucune réception garantie n’est revendiquée.
