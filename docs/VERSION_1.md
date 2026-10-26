# VeillePorte — première version IR

[Accueil](../README.md) · [Câblage](CAPTEUR_IR.md)

Le module VL53L4CD est fixé au cadre, face à une cible sur la porte. Le firmware reste à développer.

## États à qualifier sur banc

- Fermé : cible proche, mesure valide et stable.
- Ouvert : distance valide supérieure au seuil d’ouverture pendant une durée définie.
- Inconnu : mesure invalide, perte de communication, démarrage non stabilisé ou situation ambiguë de cible absente.

Deux seuils distincts et une temporisation éviteront les oscillations. Tester explicitement une ouverture faisant sortir la cible du faisceau : le traitement de cette situation doit être défini après essais, sans confondre une panne avec une ouverture.

Le mode ULP détecte une proximité avec une interruption ; il ne fournit pas les distances du mode standard. La stratégie basse consommation dépendra des essais de disparition de cible, de la vitesse d’ouverture et de l’énergie disponible. Une ouverture rapide peut être manquée si les acquisitions sont trop espacées.

## Communication

Transmettre l’état initial, les transitions confirmées et un message périodique par LoRaWAN. Inclure version de format, identifiant technique de porte, session, séquence, état et compteur depuis démarrage. Le tableau de bord enregistre l’heure de réception, élimine les doublons et applique les horaires configurés. Des données expirées s’affichent comme inconnues. Après coupure, le compteur en RAM repart à zéro ; le stockage persistant n’est pas implémenté.

Le dispositif n’identifie personne, ne détermine pas un sens de passage et ne garantit pas la réception d’un événement. Utiliser des identifiants fictifs sur une porte d’essai.

## Validation prévue

Tester cible proche/éloignée/absente, mesures invalides, lumière ambiante, oscillation autour du seuil, ouverture rapide, réseau absent, doublons et redémarrage. Mesurer consommation moyenne, pointes et autonomie dans l’obscurité. Le panneau solaire est disponible selon Amira ; sa référence et les caractéristiques du stockage restent à relever.

Réaliser ensuite le PCB IR, le boîtier et l’antenne, et une démonstration pédagogique de 1 à 2 semaines. Les rapports de l’ancien PCB ne valident pas cette version.
