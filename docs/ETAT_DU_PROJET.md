# État du projet VeillePorte

[Accueil](../README.md) · [Schéma final](SCHEMA_COMPLET.md)

| Élément | État retenu |
|---|---|
| Schéma | Une page KiCad A2 avec alimentation, RAK3172, capteur IR, interfaces et antenne |
| BQ25570 | Seuils calculés pour stockage 4 V max ; composants NC et C22 conservés |
| Capteur | Module VL53L4CD Pololu 3692 externe relié par J23 |
| Antenne | Empreinte IFA 868 MHz liée à RF et masse ; résultats CST préliminaires |
| ERC | 0 erreur, 3 avertissements connus |
| Netlist | 45 composants et 43 groupes de connexions |
| PCB | Implantation reprise en 40 × 60 mm, 4 couches, 47 empreintes ; aucune piste ni via. RAK orienté pour rapprocher RF de l’antenne, alimentation regroupée autour du BQ25570, J10 hors de la zone rayonnante. Plan GND préparé sur In1.Cu. Routage à réaliser : F.Cu alimentations/RF, In2.Cu signaux RAK, B.Cu autres connexions. DRC : 0 erreur géométrique, 2 avertissements d’empreinte J10/J22, 106 connexions non résolues. Aperçus : `../VeillePorte/implantation.svg` et `../VeillePorte/implantation_dos.svg`. |
| Firmware et LoRaWAN | À développer et tester |
| Boîtier et panneau | Panneau solaire environ 50 × 50 mm ; géométrie et matériaux à intégrer |
| Mesures physiques | Non réalisées ; consommation, autonomie, portée et détection restent à valider |

L’antenne simplifiée atteint un S11 simulé d’environ −12,01 dB à 868 MHz avec 82 620 cellules. Cela ne démontre ni un gain ni un rendement suffisant. Le diagramme farfield reste à exporter depuis CST.

Les trois avertissements ERC connus portent sur le symbole BQ, les noms EN/GND sur la même masse et les labels locaux/globaux. Aucun n’est masqué. Voir le [rapport ERC](../VeillePorte/erc_complet.json) et le [rapport de vérification](verification_schema_complet.json).




