# VeillePorte — ouvertures de porte et accompagnement

[Accueil](../README.md) · [Première version](VERSION_1.md)

## Usage visé

Un boîtier IR sur le cadre, face à une cible sur la porte de chambre, vise à signaler son ouverture au personnel dans l’accompagnement des personnes atteintes de la maladie d’Alzheimer. Les horaires de surveillance sont configurés dans l’application. Le prototype est démontré sur une porte d’essai, avec des identifiants fictifs.

Le dispositif détecte un changement de distance, sans identifier le patient, le soignant ou le visiteur. Il ne détermine pas le sens de passage, une sortie effective ou une situation de danger. Il ne verrouille pas la porte et ne remplace pas l’accompagnement humain.

## Éléments nécessaires

| Élément | État |
|---|---|
| RAK3172 et BQ25570 | Base électronique existante conservée |
| Ancien LIS2HH12 | Retiré du schéma actif ; ancienne carte archivée |
| Module VL53L4CD Pololu 3692 | Raccordement intégré au schéma ; PCB à actualiser |
| Panneau solaire | Disponible selon Amira ; caractéristiques à relever |
| Stockage | Référence et dimensionnement à confirmer |
| Antenne 868 MHz et boîtier 3D | À concevoir pour le projet |
| Réseau LoRaWAN et tableau de bord | À configurer et développer |

## Alimentation et disponibilité

L’éclairage d’un couloir ou d’une chambre peut être insuffisant pour assurer une alimentation solaire continue. Mesurer l’énergie récoltée, la consommation, les pointes radio et l’autonomie dans l’obscurité avant d’annoncer une durée de fonctionnement. Le fichier BQ25570 reste strictement inchangé, avec ses résistances NC et C22.

Une perte de réseau ou d’alimentation doit rendre l’état affiché inconnu après expiration d’un délai défini. Un message radio émis ne prouve pas qu’il a été reçu. Aucun fonctionnement clinique ni délai de livraison garanti n’a été validé.

## Démonstration pédagogique

Tester les ouvertures/fermetures, les oscillations autour du seuil, une ouverture prolongée, les horaires, une perte de couverture et un redémarrage. Prévoir un suivi de 1 à 2 semaines conformément au cadre du cours, en mesurant les événements manqués et la consommation. Aucun nom de patient ni donnée médicale n’est nécessaire à la démonstration.

## Révision IR active

Le raccordement VL53L4CD est dessiné ; voir [CAPTEUR_IR.md](CAPTEUR_IR.md). La logique de porte repose sur une mesure valide, deux seuils et une temporisation, pas sur un contact. Les références à la stabilisation désignent le filtrage temporel de cet état. Le PCB IR et les essais restent à réaliser.
