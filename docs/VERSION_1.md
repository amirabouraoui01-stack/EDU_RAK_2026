# VeillePorte — première version

[Accueil](../README.md) · [Scénario](VEILLEPORTE.md)

Spécification à développer ; aucun firmware VeillePorte n’est actuellement fourni.

## Comportement

1. Au démarrage, lire et stabiliser l’état du contact, puis transmettre l’état initial sans compter une ouverture fictive.
2. Filtrer les rebonds pendant une durée configurable et confirmer chaque transition stable.
3. Compter uniquement les transitions fermé vers ouvert ; transmettre aussi les fermetures.
4. Envoyer un état périodique et un numéro de séquence pour suivre la disponibilité et dédupliquer les messages.
5. À la réception, enregistrer l’heure serveur et appliquer les horaires d’alerte configurés pour la porte.

La référence du contact, le GPIO, la logique électrique, la durée de filtrage, la cadence radio et le délai d’expiration restent à définir et à tester. Aucun choix de broche n’est appliqué au schéma à ce stade.

## Données et affichage

Le message comprendra une version, un identifiant technique de porte, un identifiant de session, une séquence, l’état stable et le compteur depuis le démarrage. Le tableau de bord affichera ouvert, fermé ou inconnu, la dernière réception et les événements pendant les horaires actifs. Un doublon ne doit pas créer deux alertes. Le format binaire et le décodeur restent à écrire.

L’heure de réception n’est pas l’heure exacte d’ouverture. Sans couverture, l’affichage expire vers inconnu ; il n’y a pas de garantie de livraison ni de reconstitution de tous les événements. Après redémarrage, le compteur en mémoire vive repart à zéro et une nouvelle session doit être distinguée. Aucun nom de patient n’est transmis.

## Critères d’essai

| Essai | Résultat attendu |
|---|---|
| Démarrage porte ouverte ou fermée | État initial correct sans fausse transition |
| Ouverture puis fermeture | Deux transitions, une ouverture comptée |
| Rebonds du contact | Un seul événement par transition stabilisée |
| Porte maintenue ouverte | État ouvert conservé, pas de nouvelles ouvertures fictives |
| Message dupliqué | Une seule entrée pour la même session/séquence |
| Horaires actifs ou inactifs | Historique conservé, signalement selon la configuration |
| Absence de messages | État inconnu après le délai configuré |
| Retour réseau et redémarrage | Nouvel état initial/synchronisé, ancienne donnée non présentée comme actuelle |
| Éclairage faible et émission | Mesures de récupération, consommation, stabilité et autonomie |

Ces critères sont destinés à une porte d’essai. Les rapports ERC/DRC actuels concernent la base matérielle sans contact magnétique.

## Ordre de réalisation

Choisir le contact et son montage, intégrer l’entrée au schéma sans modifier la feuille BQ25570, actualiser le PCB et les contrôles, développer la lecture puis LoRaWAN et le tableau de bord, et effectuer les essais. L’antenne réelle, le boîtier 3D et le dimensionnement du stockage restent à réaliser.
