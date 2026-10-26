# Historique du projet

## 26 octobre 2026 — révision 0.5, supercapacité 4 V et lisibilité

- Q1 et R14 supprimés après vérification des seuils GPIO ; VL53L4CD Pololu conservé.
- BQ25570 : OV ~3,812 V, arrêt ~3,467 V, reprise ~3,600 V et rail ~3,118 V ; résistances de précision 0,1 %.
- VBAT_OK commande VOUT_EN ; R9 passe à 3,3 MΩ pour le suivi PA0.
- Cette demande de réglage remplace la conservation intégrale de la feuille BQ ; options NC et C22 inchangées.
- Feuille RAK organisée en six cadres fonctionnels ; exports et contrôles actualisés.


## 26 octobre 2026 — schéma IR 0.4

- Remplacement du LIS2HH12 par le raccordement du module externe Pololu 3692 / VL53L4CD.
- J23, Q1 BSS138 et R14 pour l’interface ; XSHUT sur PB5 en drain ouvert.
- Suppression de R12/R13 et C12 ; rappels I²C fournis par le module.
- ERC : 0 erreur, 3 avertissements historiques ; BQ25570 inchangé.
- Ancien PCB et son DRC archivés ; le PCB IR reste à réaliser.


## Renommage des fichiers — VeillePorte

- Dossier actif `VeillePorte/`, fichiers principaux `veilleporte.*` et bibliothèque `VeillePorte.kicad_sym`.
- Liens, références KiCad et outils actualisés.
- Feuille BQ25570 et cuivre du PCB conservés.


## 26 octobre 2026 — VeillePorte

- Nouvelle application : suivi des ouvertures de porte dans l’accompagnement des personnes atteintes de la maladie d’Alzheimer.
- Présentation, scénario, spécification, disponibilité et essais adaptés à LoRaWAN.
- Contact magnétique explicitement indiqué comme restant à intégrer.
- Matériel et feuille BQ25570 inchangés ; rapports existants conservés comme contrôles de la base.


## 26 octobre 2026 — définition de la première version

- Détection, regroupement des chocs, bilan radio et critères d’essai spécifiés.
- Limites de mesure et perte des données après coupure explicitées.
- Étapes de choix et de validation de l’alimentation identifiées, sans changement matériel.

## 26 octobre 2026 — ColisCare

- Nouvelle application : suivi des chocs pendant les livraisons fragiles.
- Présentation, bannière, architecture et protocole d’essais adaptés.
- Circuit, fichiers KiCad, exports et feuille BQ25570 conservés à l’identique.
- Les noms historiques des fichiers et l’historique ci-dessous restent conservés.

## 14 octobre 2026 — routage du PCB

- Placement regroupé par fonction et connecteur RF rapproché du RAK3172.
- Routage de toutes les connexions sur deux couches, plan de masse au dos.
- Zone réservée sous la liaison RF pour garder son retour de masse.
- Hypothèses documentées : épaisseur 0,8 mm et isolation minimale 0,15 mm.
- Contrôle final : 0 violation DRC, 0 connexion manquante, 0 problème de parité.
- Aperçus des deux faces et documents actualisés.

## 14 octobre 2026 — empreinte LBOOST1

- Bibliothèque locale LPS4018-223MRC importée depuis SmartPot, avec le modèle 3D.
- Enregistrement sous le nom exact demandé par le schéma, sans modification de la feuille BQ25570.
- L’erreur de bibliothèque d’empreinte absente disparaît ; ERC : 0 erreur, 4 avertissements.

## 14 octobre 2026 — révision 0.3

- Antenne externe générique 868 MHz ajoutée au schéma, sans modèle physique imposé.
- EN du BQ reliée à la masse depuis la feuille RAK3172 ; feuille BQ inchangée.
- Nouvelle vérification des connexions, du PDF et de l’ERC.
- Page d’accueil personnalisée pour le collier d’Amira.
- Guides d’architecture, d’avancement et de mise en service ; galerie de schémas.
- Ressources EDU RAK regroupées dans `references/EDU_RAK_2026/`.

## 14 octobre 2026 — révision 0.2

- BQ25570 restauré à l’identique du fichier EDU RAK.
- Résistances NC et C22 conservées.
- Connecteurs du collier repérés J20 à J22 ; surveillance VBAT_OK sur la feuille MCU.

## 14 octobre 2026 — révision 0.1

- Premier schéma du collier avec RAK3172 et LIS2HH12.
- I²C, interruption, UART2, SWD et sortie RF.
