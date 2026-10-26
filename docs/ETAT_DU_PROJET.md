# État de VeillePorte — révision 0.5

Une [vue complète A2](SCHEMA_COMPLET.md) est disponible en présentation 0.6 : une page avec les fils entre blocs, 44 composants, 43 groupes de connexions identiques à la référence, 0 erreur ERC et 3 avertissements conservés. Aucun changement électrique n’est introduit par cette présentation.

[Accueil](../README.md) · [Câblage](CAPTEUR_IR.md)

| Partie | État |
|---|---|
| Schéma | RAK3172 + BQ25570 + raccordement module VL53L4CD Pololu 3692 |
| Accéléromètre | Retiré du schéma actif |
| Alimentation BQ25570 | Réglé pour supercapacité 4 V ; options NC et C22 conservées |
| Interface IR | J23, I²C, interruption directe sur PA1, XSHUT vers PB5 |
| ERC | 0 erreur, 3 avertissements conservés |
| Vérification netlist | 74 comparaisons de connexions réussies |
| PCB IR | À réaliser ; dimensions visées 60 × 30 mm |
| Ancien PCB | Archivé avec LIS2HH12, non compatible avec la révision IR |
| Firmware, LoRaWAN, tableau de bord | À développer |
| Antenne et boîtier | Piste fine CST : S11 ≈ −12,01 dB à 868 MHz, 82 620 cellules ; panneau et boîtier à intégrer |
| Alimentation et essais physiques | À valider |

Les trois avertissements ERC concernent la différence entre le symbole BQ embarqué et la bibliothèque installée, les noms GND/EN sur la même masse et les labels local/global de masse. Aucun avertissement n’est masqué. [Rapport ERC](../VeillePorte/erc.json) · [Vérification des raccordements et du BQ](verification_schema.json).

Les anciens DRC à zéro et le rapport `verification_pcb.json` décrivent uniquement la carte avant IR ; ils ne valident pas un nouveau PCB. La commande `python tools/verifier_schema.py` contrôle le schéma IR et la conservation octet pour octet du BQ.

## Révision 0.5 : alimentation et présentation

Q1/R14 supprimés, interruption directe compatible. BQ adapté à la supercapacité 4 V et VBAT_OK relié à VOUT_EN ; voir [les calculs](ALIMENTATION.md). Six cadres organisent la feuille RAK. Le PCB reste à réaliser pour cette révision.
