# Modèle CST retenu — antenne IFA 868 MHz

Le seul modèle conservé dans cette version est [veilleporte_868_piste_basse.cst](veilleporte_868_piste_basse.cst). Il utilise une carte théorique de 30 × 60 × 0,8 mm et un radiateur à quatre branches en F inversé. Le retour fin fait 0,5 mm ; la plaque de réglage utilisée pendant les essais précédents est absente de cette version.

- S11 à 868 MHz : −12,01 dB.
- Minimum échantillonné : −13,51 dB vers 865,32 MHz.
- Maillage : 82 620 cellules, critère d’énergie −40 dB atteint.
- [Export S11](s11_veilleporte_868_piste_basse.txt) · [Synthèse](synthese_piste_fine.json) · [Commandes géométriques](veilleporte_868_piste_basse.vba.txt).

![Géométrie CST de la piste retenue](veilleporte_868_piste_basse.png)

Le moniteur farfield est réglé à 0,868 GHz. Son diagramme n’est pas encore exporté en image ou en fichier de données. Le S11 ne suffit pas à conclure sur le gain ou le rendement.

## Hypothèses

Substrat FR4 supposé, εr = 4,3 et tan δ = 0,02 ; conducteur PEC ; masse sur les 40 mm côté électronique et zone antenne sans masse dessous. Le port discret 50 Ω et le pont de masse sont des simplifications.

Le panneau solaire 50 × 50 mm, les fils, le boîtier, la colle, le RAK, le connecteur et le support ne sont pas inclus. Le résultat ne prédit donc pas l’accord une fois assemblé.

Pour générer une nouvelle variante, utiliser creer_variante.py depuis ce dossier. Le script prépare une macro CST à lancer manuellement ; Python ne réalise pas la simulation.

