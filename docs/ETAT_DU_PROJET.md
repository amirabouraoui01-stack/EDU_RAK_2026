# État de VeillePorte — révision IR 0.4

[Accueil](../README.md) · [Câblage](CAPTEUR_IR.md)

| Partie | État |
|---|---|
| Schéma | RAK3172 + BQ25570 + raccordement module VL53L4CD Pololu 3692 |
| Accéléromètre | Retiré du schéma actif |
| Alimentation BQ25570 | Fichier d’origine strictement inchangé |
| Interface IR | J23, I²C, interruption via Q1/R14, XSHUT vers PB5 |
| ERC | 0 erreur, 3 avertissements conservés |
| Vérification netlist | 78 comparaisons de connexions réussies |
| PCB IR | À réaliser ; dimensions visées 60 × 30 mm |
| Ancien PCB | Archivé avec LIS2HH12, non compatible avec la révision IR |
| Firmware, LoRaWAN, tableau de bord | À développer |
| Antenne et boîtier | À concevoir |
| Alimentation et essais physiques | À valider |

Les trois avertissements ERC concernent la différence entre le symbole BQ embarqué et la bibliothèque installée, les noms GND/EN sur la même masse et les labels local/global de masse. Aucun avertissement n’est masqué. [Rapport ERC](../VeillePorte/erc.json) · [Vérification des raccordements et du BQ](verification_schema.json).

Les anciens DRC à zéro et le rapport `verification_pcb.json` décrivent uniquement la carte avant IR ; ils ne valident pas un nouveau PCB. La commande `python tools/verifier_schema.py` contrôle le schéma IR et la conservation octet pour octet du BQ.
