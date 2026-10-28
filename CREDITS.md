# Crédits et origine

Projet VeillePorte développé pour **Amira**, compte [amirabouraoui01-stack](https://github.com/amirabouraoui01-stack).

## Base pédagogique

La base est la plateforme [EDU_RAK_2026 de DorianDIANA](https://github.com/DorianDIANA/EDU_RAK_2026). Ses ressources sont conservées dans [references/EDU_RAK_2026](references/EDU_RAK_2026/README.md), avec l’historique Git.

La feuille `VeillePorte/alimentation.kicad_sch` provient de `harvester.kicad_sch` extrait de l’archive KiCad EDU RAK ; les réglages de tension et la commande VOUT_EN sont adaptés en révision 0.5, sur demande d’Amira. Les résistances NC et C22 sont laissées telles quelles, à la demande d’Amira.

Les feuilles RAK3172 et LIS2HH12 sont adaptées au projet. Les symboles viennent de la base EDU RAK et des bibliothèques KiCad. AE1 est un symbole générique d’antenne externe, à port RF passif, exclu du PCB et de la nomenclature.

## Inspiration de présentation

[SmartPot_RAK3172 de MaxBarbe](https://github.com/MaxBarbe/SmartPot_RAK3172) inspire l’organisation : projet personnel au premier plan, aperçu des fichiers, état explicite et références séparées. Ses fichiers de pot, de PCB et d’antenne ainsi que ses résultats de simulation ne sont pas repris comme résultats de VeillePorte.

## Fiches techniques

- [RAK3172 — RAKwireless](https://docs.rakwireless.com/Product-Categories/WisDuo/RAK3172-Module/Datasheet/).
- [BQ25570 — Texas Instruments](https://www.ti.com/product/BQ25570).
- [LIS2HH12 — STMicroelectronics](https://www.st.com/resource/en/datasheet/lis2hh12.pdf).
- [Copies locales](references/EDU_RAK_2026/Datasheets/).

Les droits des fichiers d’origine restent ceux de leurs auteurs. Aucune nouvelle licence globale n’est attribuée aux ressources tierces.

## Modèle 3D RAK3172

Le modèle STEP du module provient du [répertoire officiel RAKwireless](https://rakwireless-downloads-center-prod.s3.eu-central-1.amazonaws.com/3D_File/WisDuo/3D_RAK3172.stp), téléchargé le 28 octobre 2026. Le décalage du modèle est corrigé dans l’empreinte locale ; ses dimensions ne sont pas utilisées pour modifier les pastilles du module. Le boîtier 3D du BQ25570 provient de la bibliothèque KiCad Texas VQFN RGR 20, 3,5 × 3,5 mm.
