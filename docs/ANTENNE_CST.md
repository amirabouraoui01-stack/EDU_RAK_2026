# Antenne 868 MHz — étude CST

[Accueil](../README.md) · [Modèles, macros et hypothèses](../VeillePorte/cst/README.md)

L’étude utilise un PCB 30 × 60 mm et une zone rayonnante de 30 × 20 mm. La variante active est une antenne en F inversé à quatre branches et retour de piste fin, calculée dans CST Studio Suite 2026. Les plans de masse occupent les 40 autres millimètres de longueur.

L’ancien [modèle de référence avec plaque](../VeillePorte/cst/veilleporte_868_reference.cst) donne environ **−14,07 dB à 868 MHz**, avec 81 000 cellules et le critère d’énergie atteint. Les points sous −10 dB couvrent approximativement 863,18 à 872,82 MHz dans ce modèle simplifié. [Synthèse et paramètres](../VeillePorte/cst/synthese_cst.json).

Les fichiers CST sont réellement générés et les traces `s11_*.txt` sont exportées par le solveur. La [synthèse numérique](../VeillePorte/cst/resultats_simulation.json) et les [courbes](../VeillePorte/cst/comparaison_s11.svg) permettent de comparer les essais. Un bon S11 décrit l’adaptation de cette simulation ; il ne garantit pas le rendement ou la portée de l’appareil.

## Nouvelle forme à piste fine

Le modèle actif est [veilleporte_868_piste_basse.cst](../VeillePorte/cst/veilleporte_868_piste_basse.cst). Le rectangle plein est supprimé et remplacé par un retour de 0,5 mm. S11 simulé ≈ **−12,01 dB à 868 MHz**, 82 620 cellules ; minimum vers 865,32 MHz. [Synthèse de cette variante](../VeillePorte/cst/synthese_piste_fine.json).

## Diagramme de rayonnement (*farfield*)

Le modèle actif contient un moniteur de champ lointain à **868 MHz** et le solveur avait atteint le critère d’énergie de −40 dB. Les fichiers de calcul CST sont dans le cache local, qui n’est pas transféré par Git. Le fichier texte et l’image du diagramme n’ont pas encore été exportés ; il faut ouvrir le modèle dans CST, recalculer si le résultat n’apparaît pas, puis sélectionner `Farfields → farfield (f=0.868)` et tracer le diagramme 3D. Le S11 de −12,01 dB ne donne pas à lui seul le gain, le rendement ni la forme du diagramme.

## Intégration à la carte

Une empreinte KiCad locale a été créée à partir de la géométrie CST et assignée au symbole AE1 du schéma complet. Sa broche 1 va au réseau `/RF`, sa broche 2 au réseau de masse. Elle réserve une zone de 30 × 20 mm à l’extrémité de la carte ; les pistes du radiateur sont du cuivre intégré à l’empreinte. Consulter le guide [Empreinte antenne KiCad](EMPREINTE_ANTENNE.md).

Le PCB électronique doit encore être placé et routé en conservant cette zone d’antenne. La simulation ne représente pas encore le panneau, le boîtier, la colle ni le support.

## Intégration mécanique à prévoir

Le panneau d’Amira mesure environ 50 × 50 mm et comporte deux fils. Le boîtier devra tenir compte de cette largeur et préserver la zone rayonnante. Le [croquis](../VeillePorte/cst/implantation_proposee.svg) montre une disposition possible, sans recouvrement du radiateur par le panneau. La matière du boîtier, la colle, les fils et le support de porte restent à définir.

Le panneau et le boîtier ne sont pas encore inclus dans le calcul. Le conducteur est PEC ; les pertes cuivre ne sont donc pas représentées. Le FR4 est supposé, le plan de masse et son pont sont simplifiés. La convergence complète, le gain réalisé et le rendement restent à étudier. La licence a refusé un raffinement dépassant 100 000 cellules ; les calculs retenus respectent cette limite.

La présence de l’empreinte dans le schéma ne constitue pas un placement PCB validé ni une autorisation de fabrication.
