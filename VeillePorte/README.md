# VeillePorte — schéma IR 0.4

[Accueil](../README.md) · [PDF](veilleporte.pdf) · [Câblage IR](../docs/CAPTEUR_IR.md)

Ouvrir `veilleporte.kicad_pro` dans KiCad 10. Le schéma principal rassemble `alimentation.kicad_sch`, `rak3172.kicad_sch` et `capteur_ir.kicad_sch`.

Le LIS2HH12 est remplacé par le connecteur J23 pour un module externe VL53L4CD Pololu 3692. Q1 adapte l’interruption, PB5 pilote XSHUT en drain ouvert. C11/C13 assurent le découplage ; les rappels I²C sont sur le module. Le BQ25570, ses résistances NC et C22 sont identiques au fichier d’origine.

La bibliothèque locale `VeillePorte.kicad_sym` conserve aussi des symboles historiques inutilisés. Le schéma actif ne contient plus U3 LIS2HH12, R12/R13 ni C12.

La netlist `veilleporte.net` et `erc.json` correspondent au schéma IR. Le PCB précédent et son DRC sont dans [archive_avant_ir](archive_avant_ir/README.md). Le PCB IR, le firmware et les essais restent à réaliser.
