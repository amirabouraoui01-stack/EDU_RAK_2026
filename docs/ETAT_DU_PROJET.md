# État du projet — 26 octobre 2026

[Accueil](../README.md) · [Galerie](GALERIE.md)

| Partie | État |
|---|---|
| Schéma de VeillePorte | Quatre feuilles, révision 0.3 pour les feuilles propres au projet |
| BQ25570 | Fichier EDU RAK strictement inchangé |
| RAK3172 et LIS2HH12 | Raccordements vérifiés dans les exports |
| Antenne AE1 | Symbole générique externe 868 MHz, raccord RF vérifié |
| PDF et netlist | Actualisés avec KiCad 10.0.6 |
| Contrôle d’intégration | 85 comparaisons de connexions réussies, références uniques |
| ERC | **0 erreur, 4 avertissements documentés** |
| PCB | 47 composants, 60 × 30 mm, routage deux couches et plan de masse |
| DRC et connectivité PCB | 0 violation, 0 connexion manquante, 0 problème de parité |
| Boîtier et firmware | À réaliser |
| Essais et autonomie | À mesurer |

## Résultats de vérification

Le [rapport reproductible](verification_schema.json) confirme que la feuille BQ possède les mêmes octets que `harvester.kicad_sch` de l’archive pédagogique. Les résistances NC et C22 restent intactes.

Les contrôles portent sur les alimentations, les masses, I²C, INT1, VBAT_OK, UART2, SWD, BOOT0, reset, RF, les inductances et diviseurs du BQ. Le raccordement graphique d’AE1 à RF est contrôlé séparément, car cette antenne externe est volontairement exclue du PCB et de la nomenclature.

L’entrée EN du BQ était sans commande. Elle est désormais reliée à la masse depuis la feuille RAK, par le label global existant. Cette correction d’intégration ne change pas la feuille BQ. La commande VOUT_EN est déjà reliée à VSTOR dans le fichier original.

Les quatre pages du PDF ont été inspectées visuellement. Le rendu de la feuille BQ conserve sa présentation originale, y compris les éléments non montés.

## Avertissements ERC conservés

Le [rapport KiCad](../Collier_Chien/erc.json) contient quatre avertissements. L’empreinte LBOOST1 est désormais fournie dans une bibliothèque locale :

| Avertissement | Explication et suite |
|---|---|
| Copie du symbole BQ25570 différente | Symbole embarqué original conservé ; aucune substitution automatique |
| Plusieurs noms sur un net | EN est reliée à GND ; KiCad choisit `'EN` comme nom dans la netlist |
| Label local/global de masse | Deux formes de label désignent la même masse |
| SA0/SDO contre sortie d’alimentation | Broche bidirectionnelle du symbole reliée à GND pour sélectionner l’adresse I²C |

Les avertissements sont laissés visibles. Les éléments NC et C22 ne sont pas modifiés pour nettoyer le rapport.

## Reproduire les contrôles

Après export de la netlist et du rapport ERC avec KiCad :

```text
python tools/verifier_schema.py
```

Le script fonctionne avec Python standard. Il compare l’alimentation avec l’archive de référence, contrôle les raccordements et actualise le rapport de vérification.

## Ce qui reste à valider

- Choix de la source d’énergie et du stockage externe.
- Démarrage, tolérances du rail PWR et courant pendant les transmissions.
- Contact magnétique, entrée GPIO, filtrage et cadence LoRaWAN.
- Liaison RF, modèle réel d’antenne et comportement à proximité du environnement de la porte.
- Revue du PCB, conception du boîtier et firmware, puis essais du montage.

Le [PCB routé et son rapport](../Collier_Chien/PCB.md) sont disponibles. Les contrôles géométriques passent avec les règles configurées. L’épaisseur de 0,8 mm et l’espacement de 0,15 mm restent à confirmer avec le fabricant ; la validation RF et électrique reste à effectuer.

Un ERC sans erreur confirme certains raccordements ; il ne démontre pas le fonctionnement physique ni une autonomie. Aucun prototype VeillePorte n’a encore été mesuré. Les anciens PCB EDU RAK rangés dans les références ne sont pas des PCB de VeillePorte.

## Nouvelle application : VeillePorte

Le suivi d’ouverture de porte pour accompagner les personnes atteintes de la maladie d’Alzheimer remplace le suivi des colis. Le matériel et les rapports du 14 octobre sont inchangés. Le contact magnétique n’est pas encore intégré : les contrôles existants ne valident pas cette nouvelle fonction. Firmware, LoRaWAN, horaires, tableau de bord et tests de disponibilité restent à réaliser. Voir [le scénario](VEILLEPORTE.md).
