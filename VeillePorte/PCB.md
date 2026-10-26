# PCB IR : à réaliser

Le PCB précédent est conservé dans [archive_avant_ir](archive_avant_ir/veilleporte.kicad_pcb). Il contient encore le LIS2HH12 et ne correspond pas au schéma IR 0.4. Les résultats ci-dessous concernent uniquement cette ancienne carte.

# PCB routé — 60 × 30 mm

La carte `veilleporte.kicad_pcb` contient 47 empreintes avec leurs références, champs et nets. Le contour nominal mesure 60 × 30 mm entre les axes des lignes Edge.Cuts. Les connexions sont routées sur deux couches, avec un plan de masse au dos. AE1 reste une antenne externe indicative ; l’antenne physique se raccordera à J20.

Le placement regroupe les inductances et capacités autour du BQ25570, l’accéléromètre et son découplage, et le RAK3172 avec un connecteur RF proche. Les connecteurs UART/SWD se trouvent en bordure. Les repères des composants sont conservés sur F.Fab pour éviter les collisions avec les pads ; ils ne constituent pas tous une sérigraphie imprimée.

Contrôle KiCad : **0 violation DRC, 0 connexion manquante et 0 problème de parité schéma/PCB**. Aucun diagnostic n’a été masqué. Le rapport complet est dans `pcb_drc.json`. Ce résultat valide les contraintes géométriques configurées ; il ne remplace pas les essais électriques.

## Hypothèses à communiquer au fabricant

| Paramètre | Valeur retenue |
|---|---|
| Dimensions | 60 × 30 mm |
| Couches cuivre | 2 |
| Épaisseur totale | 0,8 mm, hypothèse FR4 |
| Espacement cuivre minimum | 0,15 mm |
| Pistes de signal usuelles | 0,20 mm |
| Largeur de piste minimum | 0,15 mm |
| Vias courants | Diamètre 0,60 mm, perçage 0,30 mm |
| Retrait du plan de masse | 0,65 mm du contour nominal |

L’espacement de 0,15 mm permet les pads fins du LIS2HH12 ; le fabricant doit accepter cette valeur. Les thermiques et vias du pad exposé du BQ nécessitent une revue d’assemblage. La feuille BQ25570 reste inchangée, y compris les résistances NC et C22, conservées non montées selon le schéma.

## Liaison d’antenne et essais

La liaison RF reste sur la face avant, avec une courte section élargie de 1,45 mm et des transitions de 0,35 mm au module et au connecteur. Cette géométrie prépare une liaison proche de 50 Ω sous l’hypothèse d’une carte FR4 de 0,8 mm ; l’impédance n’est pas certifiée et doit être recalculée avec l’empilage réel. La zone au dos sous la liaison est réservée au retour de masse, sans piste de signal.

Avant fabrication finale : confirmer l’empilage, contrôler le placement et les boucles du BQ avec sa fiche technique, vérifier les modèles et empreintes, puis prévoir les essais de démarrage, de courant radio, d’accélération et d’antenne. Aucun prototype n’a encore été mesuré. Le stockage, la fixation près de la porte et le firmware restent à définir.

Le routage des signaux a utilisé [Freerouting 2.5.0](https://github.com/freerouting/freerouting/releases/tag/v2.5.0), après placement et préparation de la RF, puis import et corrections dans KiCad 10.0.6.

![Face avant, pistes et implantation](../docs/assets/pcb_avant.png)

![Face arrière, plan de masse et pistes, vue miroir](../docs/assets/pcb_arriere.png)

Si l’éditeur PCB était déjà ouvert lors de la modification du fichier, le fermer sans enregistrer l’ancienne vue puis rouvrir ce fichier pour charger le placement actuel.
