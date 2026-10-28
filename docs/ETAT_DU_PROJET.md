# État du projet VeillePorte

[Accueil](../README.md) · [Schéma final](SCHEMA_COMPLET.md)

| Élément | État retenu |
|---|---|
| Schéma | Une page KiCad A2 avec alimentation, RAK3172, capteur IR, interfaces et antenne |
| BQ25570 | Seuils calculés pour stockage 4 V max ; composants NC et C22 conservés |
| Capteur | Module VL53L4CD Pololu 3692 externe relié par J23 |
| Antenne | Empreinte IFA 868 MHz liée à RF et masse ; résultats CST préliminaires |
| ERC | 0 erreur, 3 avertissements connus |
| Netlist | 47 composants ; 44 groupes de connexions |
| PCB | Routage quatre couches terminé : 40 × 60 × 1,6 mm, 47 empreintes, 427 segments, 55 vias dont 19 GND ; perçage minimum 0,3 mm. Plan GND In2.Cu. DRC et concordance schéma/PCB : 0 erreur, 0 avertissement, 0 connexion manquante. Pastilles de fils solaires sur J10, connecteurs latéraux, RF en 0603 et C22 DNP conservés. Vues et STEP dans `../VeillePorte/exports/`. Accord RF sur le nouvel empilage et boîtier à revalider. |
| Firmware et LoRaWAN | À développer et tester |
| Boîtier et panneau | Panneau solaire environ 50 × 50 mm ; géométrie et matériaux à intégrer |
| Mesures physiques | Non réalisées ; consommation, autonomie, portée et détection restent à valider |

L’antenne simplifiée atteint un S11 simulé d’environ −12,01 dB à 868 MHz avec 82 620 cellules. Cela ne démontre ni un gain ni un rendement suffisant. Le diagramme farfield reste à exporter depuis CST.

Les trois avertissements ERC connus portent sur les symboles BQ25570 et RAK3172 différents des copies en bibliothèque, et les labels locaux/globaux de même nom. Aucun n’est masqué. Voir le [rapport ERC](../VeillePorte/erc_complet.json) et le [rapport de vérification](verification_schema_complet.json).




