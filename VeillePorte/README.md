# VeillePorte — schéma 0.5

**Vue complète recommandée : ouvrir [veilleporte_complet.kicad_pro](veilleporte_complet.kicad_pro).** Le [schéma unique](veilleporte_complet.kicad_sch) et le [PDF A2](veilleporte_complet.pdf) réunissent les fonctions avec leurs branchements. [Guide et vérification d’équivalence](../docs/SCHEMA_COMPLET.md). Les fichiers décrits ci-dessous constituent la référence par feuilles conservée.

Le schéma complet relie maintenant AE1 à l’empreinte personnalisée de l’antenne IFA 868 MHz. Voir [la bibliothèque et son utilisation dans KiCad](../docs/EMPREINTE_ANTENNE.md) et [l’étude CST du farfield](../docs/ANTENNE_CST.md).

[Accueil](../README.md) · [PDF](veilleporte.pdf) · [Câblage IR](../docs/CAPTEUR_IR.md)

Ouvrir `veilleporte.kicad_pro` dans KiCad 10. Le schéma principal rassemble `alimentation.kicad_sch`, `rak3172.kicad_sch` et `capteur_ir.kicad_sch`.

Le LIS2HH12 est remplacé par le connecteur J23 pour un module externe VL53L4CD Pololu 3692. GPIO1 rejoint directement PA1 ; PB5 pilote XSHUT en drain ouvert. Q1 et R14 sont supprimés. C11/C13 assurent le découplage ; les rappels I²C sont sur le module. Le BQ25570 est adapté à la supercapacité 4 V ; ses options NC et C22 sont conservées.

La bibliothèque locale `VeillePorte.kicad_sym` conserve aussi des symboles historiques inutilisés. Le schéma actif ne contient plus U3 LIS2HH12, R12/R13 ni C12.

La netlist `veilleporte.net` et `erc.json` correspondent au schéma IR. Le PCB précédent et son DRC sont dans [archive_avant_ir](archive_avant_ir/README.md). Le PCB IR, le firmware et les essais restent à réaliser.
