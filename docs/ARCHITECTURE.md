# Architecture du projet final

[Accueil](../README.md) · [Projet KiCad](../VeillePorte/veilleporte_complet.kicad_pro) · [PDF A2](../VeillePorte/veilleporte_complet.pdf)

## Détection de porte

Le module Pololu 3692/VL53L4CD observe une cible fixée sur la porte depuis le cadre. J23 porte les signaux suivants : VIN, GND, SDA, SCL, NC, GPIO1 et XSHUT. J23 décrit le câble défini pour le projet, pas l’ordre physique des broches sur le module. Voir [le guide de câblage](CAPTEUR_IR.md).

GPIO1 rejoint PA1 du RAK3172 ; XSHUT rejoint PB5 et doit être commandé bas ou haute impédance. Le mode basse consommation et la détection de disparition de cible devront être caractérisés sur banc.

## Calcul et radio

Le RAK3172 traite les états puis transmet les transitions et les messages périodiques par LoRaWAN 868 MHz. Le symbole AE1 est relié à la broche RF du RAK et utilise l’empreinte IFA imprimée personnalisée. J20 reste un accès coaxial sur le même réseau RF : la conception du PCB devra choisir comment utiliser ce connecteur sans mettre une antenne externe en parallèle avec l’antenne imprimée.

## Énergie

Le BQ25570 récupère l’énergie du panneau et alimente le rail PWR depuis le stockage. Ses résistances définissent une charge maximale nominale d’environ 3,812 V, un arrêt du buck vers 3,467 V, une reprise vers 3,600 V et un rail proche de 3,118 V. Le stockage est indiqué comme une supercapacité de 4 V maximum ; sa référence, sa capacité et son ESR restent à confirmer. Voir [les calculs et limites](ALIMENTATION.md).

## Limites d’état

Une distance mesurée ne permet pas d’identifier une personne ou le sens de passage. En l’absence de mesure valide ou de message récent, l’application devra présenter un état inconnu. La portée radio, l’autonomie et la fiabilité de détection ne sont pas encore mesurées.

