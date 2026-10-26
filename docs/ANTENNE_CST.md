# Antenne 868 MHz — étude CST

[Accueil](../README.md) · [Modèles, macros et hypothèses](../VeillePorte/cst/README.md)

L’étude utilise un PCB 30 × 60 mm et une zone rayonnante de 30 × 20 mm. Une antenne en F inversé à quatre branches, avec une charge terminale imprimée, est calculée dans CST Studio Suite 2026. Les plans de masse occupent les 40 autres millimètres de longueur.

L’ancien [modèle de référence avec plaque](../VeillePorte/cst/veilleporte_868_reference.cst) donne environ **−14,07 dB à 868 MHz**, avec 81 000 cellules et le critère d’énergie atteint. Les points sous −10 dB couvrent approximativement 863,18 à 872,82 MHz dans ce modèle simplifié. [Synthèse et paramètres](../VeillePorte/cst/synthese_cst.json).

Les fichiers CST sont réellement générés et les traces `s11_*.txt` sont exportées par le solveur. La [synthèse numérique](../VeillePorte/cst/resultats_simulation.json) et les [courbes](../VeillePorte/cst/comparaison_s11.svg) permettent de comparer les essais. Un bon S11 décrit l’adaptation de cette simulation ; il ne garantit pas le rendement ou la portée de l’appareil.

## Nouvelle forme à piste fine

Le modèle actif est [veilleporte_868_piste_basse.cst](../VeillePorte/cst/veilleporte_868_piste_basse.cst). Le rectangle plein est supprimé et remplacé par un retour de 0,5 mm. S11 simulé ≈ **−12,01 dB à 868 MHz**, 82 620 cellules ; minimum vers 865,32 MHz. [Synthèse de cette variante](../VeillePorte/cst/synthese_piste_fine.json).

## Intégration à prévoir

Le panneau d’Amira mesure environ 50 × 50 mm et comporte deux fils. Le boîtier devra tenir compte de cette largeur et préserver la zone rayonnante. Le [croquis](../VeillePorte/cst/implantation_proposee.svg) montre une disposition possible, sans recouvrement du radiateur par le panneau. La matière du boîtier, la colle, les fils et le support de porte restent à définir.

Le panneau et le boîtier ne sont pas encore inclus dans le calcul. Le conducteur est PEC ; les pertes cuivre ne sont donc pas représentées. Le FR4 est supposé, le plan de masse et son pont sont simplifiés. La convergence complète, le gain réalisé et le rendement restent à étudier. La licence a refusé un raffinement dépassant 100 000 cellules ; les calculs retenus respectent cette limite.

Le PCB électronique doit encore être repris pour réserver la zone antenne ; aucune intégration KiCad ni fabrication n’a été réalisée à cette étape.
