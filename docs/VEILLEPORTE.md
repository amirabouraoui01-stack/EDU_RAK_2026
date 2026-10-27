# Spécification fonctionnelle de VeillePorte

[Accueil](../README.md) · [Schéma KiCad retenu](../VeillePorte/veilleporte_complet.kicad_pro)

## Usage visé

Un capteur VL53L4CD fixé sur le cadre observe une cible fixée sur la porte. Le boîtier vise à transmettre les changements d’état au personnel via le RAK3172 et LoRaWAN. Les horaires de surveillance et l’affichage relèvent du futur tableau de bord.

Le dispositif ne reconnaît personne, ne donne pas le sens du passage et ne confirme pas qu’une personne a quitté la pièce. C’est un prototype pédagogique, pas un équipement clinique ou de sécurité certifié.

## États à qualifier

- **Fermé** : cible proche, mesure valide et stable.
- **Ouvert** : mesure valide au-delà du seuil d’ouverture pendant la temporisation.
- **Inconnu** : cible absente ou mesure invalide, communication perdue, démarrage non stabilisé ou situation ambiguë.

Deux seuils distincts et une temporisation doivent limiter les oscillations. La disparition de la cible doit être caractérisée sur la porte d’essai : elle ne doit pas être automatiquement confondue avec une ouverture certaine.

## Communication prévue

Transmettre l’état initial, les transitions confirmées et un message périodique de présence. Le futur tableau de bord enregistrera l’heure de réception, éliminera les doublons et affichera l’état comme inconnu lorsque les données sont trop anciennes. Un message LoRaWAN émis ne prouve pas qu’il a été reçu. Les compteurs en mémoire vive repartent à zéro après coupure tant qu’aucun stockage persistant n’est prévu.

## Matériel retenu

Le schéma final comprend le RAK3172, le BQ25570 configuré pour une supercapacité limitée à 4 V, le raccordement du module Pololu 3692/VL53L4CD par J23 et l’empreinte de l’antenne IFA 868 MHz. Le PCB, le firmware, le boîtier et le tableau de bord restent à réaliser.

Utiliser des identifiants fictifs et aucune donnée de patient pendant la démonstration.

