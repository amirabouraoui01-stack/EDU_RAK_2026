# Épaisseur reprise du projet de Dorian DIANA

Le fichier de référence `project_v1.kicad_pcb` contient `(general (thickness 1.6))` et un diélectrique FR4. Source : [DorianDIANA/EDU_RAK_2026](https://github.com/DorianDIANA/EDU_RAK_2026).

Le PCB VeillePorte conserve **1,6 mm**. Le projet de référence est en deux couches ; il ne fournit donc pas l’empilage de fabrication de notre version quatre couches. Le plan GND de VeillePorte reste sur **In2.Cu**, conformément à la consigne. Les épaisseurs entre couches doivent être fixées avec le fabricant avant de valider l’impédance RF.

Le modèle CST historique est en 0,8 mm : ses résultats ne valident pas directement le PCB actuel de 1,6 mm.

Empreinte SHA-256 du fichier de référence local : `3f54d9cf4ab187ff8aa5eaa4cb46a5ca2c2f9026fb8f00ce81043be4f11e0017`.
