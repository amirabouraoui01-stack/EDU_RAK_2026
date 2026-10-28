# Antenne IFA 868 MHz — version retenue

[Accueil](../README.md) · [Modèle CST et fichiers](../VeillePorte/cst/README.md) · [Empreinte KiCad](EMPREINTE_ANTENNE.md)

Le modèle retenu est une antenne imprimée en F inversé, sur une carte théorique de 30 × 60 × 0,8 mm. Le radiateur occupe l’extrémité de 30 × 20 mm ; le plan de masse couvre les 40 mm restants. Le grand rectangle de réglage a été remplacé par un retour de piste de 0,5 mm.

## Résultat CST disponible

- S11 à 868 MHz : **−12,01 dB**.
- Minimum échantillonné : **−13,51 dB vers 865,32 MHz**.
- Maillage : **82 620 cellules** ; critère d’énergie −40 dB atteint.
- [Modèle CST](../VeillePorte/cst/veilleporte_868_piste_basse.cst) · [Export S11](../VeillePorte/cst/s11_veilleporte_868_piste_basse.txt) · [Synthèse](../VeillePorte/cst/synthese_piste_fine.json).

Le moniteur farfield est défini à 868 MHz, mais son diagramme n’a pas encore été exporté comme image ou fichier de données. Le S11 n’indique pas à lui seul le gain, le rendement ou la forme du rayonnement. L’export sera à réaliser dans CST après ouverture du modèle et chargement ou recalcul des résultats.

## Hypothèses et limites

La simulation est une carte seule avec substrat FR4 supposé (εr = 4,3 ; tan δ = 0,02) et conducteurs PEC. Elle simplifie le plan de masse, le pont entre faces et l’excitation 50 Ω. Elle ne comprend ni le RAK3172 détaillé, ni le connecteur, ni le panneau solaire 50 × 50 mm, ni les fils, le boîtier, la colle ou le support de porte. Le rendement, l’accord final et la portée ne sont donc pas validés.

L’empreinte KiCad AE1 est une traduction géométrique des conducteurs CST ; elle réserve 30 × 20 mm à l’extrémité de la carte. Le PCB VeillePorte est implanté sur un contour de 40 × 60 mm et possède une première passe de routage. La liaison RF vers AE1 reste à router et à contrôler avec son keepout ; J20 n’est pas retenu comme seconde antenne. Le modèle CST 30 × 60 mm ne correspond pas encore au contour PCB final.

Le croquis d’implantation panneau/boîtier est une hypothèse mécanique, pas un résultat de simulation. La géométrie doit être recalculée avec les matériaux réels puis mesurée au VNA sur prototype.

