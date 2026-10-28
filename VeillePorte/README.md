# Projet KiCad retenu — VeillePorte

Ouvrir **veilleporte_complet.kicad_pro**. Le PCB courant est **veilleporte_complet.kicad_pcb** ; les anciennes versions sont conservées dans `../archives/2026-10-28_avant_reprise_40x60.zip`.

La carte mesure **40 × 60 × 1,6 mm**, en quatre couches. L’épaisseur de 1,6 mm reprend le fichier `project_v1.kicad_pcb` de Dorian DIANA. Le radiateur issu de CST est conservé dans une zone de **30 × 20 mm**, soit un quart de la surface de carte. Le FR4 reste présent sous l’antenne ; aucun plan de cuivre ne passe sous sa zone rayonnante.

| Couche | Utilisation actuelle |
|---|---|
| F.Cu | Composants, alimentations, trajet RF et raccords locaux aux vias |
| In1.Cu | Liaisons de signaux, dont celles du RAK3172 |
| In2.Cu | Plan GND, sans piste de signal |
| B.Cu | Composants au dos, autres liaisons et raccords locaux |

Des remplissages GND sur les faces externes rejoignent le plan In2.Cu par les vias de masse. Le PCB comporte **427 segments et 55 vias, dont 19 GND**. Tous les vias sont percés à **0,30 mm minimum**. L’audit de chaque segment figure dans `exports/audit_pistes.csv` ; les courts raccords aux pastilles ou vias sont distingués des segments droits et à 45°.

Les **47 empreintes du schéma** sont présentes. Le capteur reste le module externe VL53L4CD Pololu 3692 raccordé à J23 : le détecteur lui-même ne se trouve pas sur cette carte. Les connecteurs J3/J4/J19/J21/J22/J23 sont placés sur les côtés. J10 fournit deux pastilles traversantes de perçage 1 mm pour souder directement les fils du panneau solaire.

R12, C6 et L1 gardent leurs empreintes **0603**. R12 vaut 0 Ω ; C6/L1 restent non montés pour l’adaptation RF. **C22 est conservé non monté**. La branche de court-circuit de l’IFA touche sa pastille GND ; la géométrie du cuivre est inchangée par rapport au générateur CST. La zone d’exclusion et les contours de l’empreinte sont maintenant orientés avec le radiateur.

## Vérifications

- `pcb_drc.json` : **0 erreur, 0 avertissement, 0 connexion manquante et 0 problème de concordance schéma/PCB**.
- `erc_complet.json` : **0 erreur, 3 avertissements connus**, conservés visibles : symboles BQ25570 et RAK différents des copies de bibliothèque, et label local/global de même nom.
- `exports/verification_pcb.json` : dimensions, vias, couches, DNP et empreintes RF.
- Le fil RF inutile se terminant dans le vide a été supprimé du schéma, sans changer le réseau électrique.

## Vues et exports

- [Vue 3D](exports/vue_3d.png)
- [Dessus](exports/vue_dessus.png) · [Dessous](exports/vue_dessous.png)
- [Assemblage STEP avec cuivre et modèles montés](exports/veilleporte.step)
- [Implantation dessus](implantation.svg) · [Implantation dessous](implantation_dos.svg)
- [Schéma PDF A2](veilleporte_complet.pdf) · [Netlist](veilleporte_complet.net)

**Validation RF restante :** le DRC valide les règles géométriques et les connexions, pas l’accord de l’antenne ni l’impédance de la ligne RF. Le CST historique utilisait une carte 30 × 60 mm de 0,8 mm ; le PCB courant est 40 × 60 mm de 1,6 mm. L’empilage réel, l’accord à 868 MHz, le panneau solaire et le boîtier doivent être repris dans la simulation et contrôlés sur prototype avant fabrication en série. Aucun fichier Gerber n’est présenté comme prêt à fabriquer.
