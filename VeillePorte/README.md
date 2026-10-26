# Schéma KiCad de VeillePorte — révision 0.3

[Accueil du projet](../README.md) · [PDF](veilleporte.pdf) · [État et contrôles](../docs/ETAT_DU_PROJET.md)

Ouvrir `veilleporte.kicad_pro` dans KiCad 10. Le schéma principal rassemble alimentation, RAK3172 et accéléromètre. La bibliothèque locale utilise `${KIPRJMOD}`.

## Choix conservés

La feuille `alimentation.kicad_sch` est identique, octet pour octet, à `harvester.kicad_sch` de l’archive [EDU RAK](../references/EDU_RAK_2026/Hardware/Kicad/edu_rak_2026_kicad.zip). Les résistances NC et C22 sont conservées sans correction. La commande EN est reliée à la masse depuis la feuille RAK, sans modifier ce fichier.

RAK3172(H) est retenu pour la radio visée à 868 MHz ; LIS2HH12 mesure l’accélération XYZ par I²C2. AE1 représente une antenne externe générique 868 MHz, exclue du PCB et de la nomenclature. Son modèle physique reste à choisir.

## Fichiers

| Fichier | Rôle |
|---|---|
| veilleporte.kicad_sch | Racine et accès aux feuilles |
| alimentation.kicad_sch | Feuille BQ25570 originale |
| rak3172.kicad_sch | Module, antenne indicative, UART/SWD et surveillance |
| accelerometre.kicad_sch | LIS2HH12, I²C et interruption |
| VeillePorte.kicad_sym et sym-lib-table | Symboles locaux |
| fp-lib-table et footprints/LPS4018-223MRC.pretty | Empreinte locale de LBOOST1 |
| 3dmodels/LPS4018-223MRC.step | Modèle 3D de l’inductance |
| veilleporte.pdf | Export de lecture |
| veilleporte.net | Export des connexions |
| erc.json | Rapport électrique KiCad |

Les références J20/J21/J22 évitent les collisions avec les connecteurs du BQ. [Architecture et brochages](../docs/ARCHITECTURE.md) · [Mise en service](../docs/MISE_EN_SERVICE.md).

Le [PCB routé](veilleporte.kicad_pcb) contient 47 composants dans un contour de 60 × 30 mm, sur deux couches avec un plan de masse. [Routage, contraintes et contrôles](PCB.md). Le firmware reste à réaliser. L’empilage, les empreintes, le stockage, les pointes radio et l’autonomie doivent être validés avant la fabrication finale.
