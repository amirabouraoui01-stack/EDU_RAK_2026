# Architecture de VeillePorte

[Accueil](../README.md) · [Schéma PDF](../VeillePorte/veilleporte.pdf)

## Détection IR

Le module VL53L4CD Pololu 3692 utilise I²C (SDA PA11, SCL PA12). GPIO1 rejoint directement PA1 sans rappel MCU ; XSHUT rejoint PB5 en drain ouvert. Q1 et R14 sont supprimés après vérification des niveaux logiques. [Câblage](CAPTEUR_IR.md).

## Radio à 868 MHz

Le RAK3172(H) fournit la sortie RF sur sa broche 12. J20 représente le connecteur RF de la future carte. **AE1** représente une antenne externe générique pour **868 MHz**, raccordée au même signal RF par label. Elle est exclue de la nomenclature et du PCB : aucun modèle d’antenne réel n’est encore choisi.

La fréquence est une spécification du projet ; le symbole ne réalise pas une adaptation RF. Le futur PCB devra prévoir une liaison 50 Ω et une antenne adaptée. La proximité du boîtier et de l’environnement de la porte doit être prise en compte lors des essais. Aucune portée ou performance d’antenne n’est annoncée comme mesurée.

## Énergie et stockage

Le réglage BQ25570 est adapté à une supercapacité 4 V maximum. La sortie nominale vaut environ 3,118 V. VBAT_OK pilote désormais VOUT_EN : arrêt du buck vers 3,467 V et reprise vers 3,600 V. La limite de charge vaut environ 3,812 V, avec résistances de précision 0,1 %. [Calculs et limites](ALIMENTATION.md).

Le pont R8/R9 (1 MΩ / 3,3 MΩ) adapte le signal d’état du stockage pour PA0. J3 relie VOUT à PWR ; J19 reste relié à VSTOR dans cette version. La référence exacte du stockage, sa capacité et son ESR restent à confirmer ; ne pas confondre ce point avec une interface VBAT protégée.

## Programmation

UART2 est accessible sur J21, SWD sur J22. BOOT0 est maintenu bas ; SW1 assure le reset. [Brochages et préparation des essais](MISE_EN_SERVICE.md).

## État de porte

Le capteur vise une cible fixée à la porte. Distance courte stable : fermé ; distance plus grande valide : ouvert. La disparition de cible et les mesures invalides doivent être qualifiées sur banc, avec un état inconnu pour les cas ambigus. La communication prévue reste LoRaWAN ; aucune réception garantie n’est revendiquée.
