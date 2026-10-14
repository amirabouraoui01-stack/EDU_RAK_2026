# Schéma KiCad du collier — révision 0.3

[Accueil du projet](../README.md) · [PDF](collier_chien.pdf) · [État et contrôles](../docs/ETAT_DU_PROJET.md)

Ouvrir `collier_chien.kicad_pro` dans KiCad 10. Le schéma principal rassemble alimentation, RAK3172 et accéléromètre. La bibliothèque locale utilise `${KIPRJMOD}`.

## Choix conservés

La feuille `alimentation.kicad_sch` est identique, octet pour octet, à `harvester.kicad_sch` de l’archive [EDU RAK](../references/EDU_RAK_2026/Hardware/Kicad/edu_rak_2026_kicad.zip). Les résistances NC et C22 sont conservées sans correction. La commande EN est reliée à la masse depuis la feuille RAK, sans modifier ce fichier.

RAK3172(H) est retenu pour la radio visée à 868 MHz ; LIS2HH12 mesure l’accélération XYZ par I²C2. AE1 représente une antenne externe générique 868 MHz, exclue du PCB et de la nomenclature. Son modèle physique reste à choisir.

## Fichiers

| Fichier | Rôle |
|---|---|
| collier_chien.kicad_sch | Racine et accès aux feuilles |
| alimentation.kicad_sch | Feuille BQ25570 originale |
| rak3172.kicad_sch | Module, antenne indicative, UART/SWD et surveillance |
| accelerometre.kicad_sch | LIS2HH12, I²C et interruption |
| Collier.kicad_sym et sym-lib-table | Symboles locaux |
| fp-lib-table et footprints/LPS4018-223MRC.pretty | Empreinte locale de LBOOST1 |
| 3dmodels/LPS4018-223MRC.step | Modèle 3D de l’inductance |
| collier_chien.pdf | Export de lecture |
| collier_chien.net | Export des connexions |
| erc.json | Rapport électrique KiCad |

Les références J20/J21/J22 évitent les collisions avec les connecteurs du BQ. [Architecture et brochages](../docs/ARCHITECTURE.md) · [Mise en service](../docs/MISE_EN_SERVICE.md).

Le PCB et le firmware ne sont pas encore réalisés. Les empreintes, le stockage, les pointes radio et l’autonomie restent à valider avant fabrication.
