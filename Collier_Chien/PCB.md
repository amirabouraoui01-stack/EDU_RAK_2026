# PCB préliminaire — 60 × 30 mm

La carte `collier_chien.kicad_pcb` contient 47 empreintes importées du schéma, leurs références, champs et nets. Le contour nominal mesure 60 × 30 mm entre les axes des lignes Edge.Cuts. Deux couches cuivre sont prévues. AE1 reste une antenne externe indicative, exclue du PCB.

Le placement initial organise les composants en rangées et garde les empreintes dans le contour. Il devra être affiné pour rapprocher le découplage des circuits, réduire les boucles du BQ25570, positionner les connecteurs et préparer la liaison RF 50 Ω. Aucune piste ni zone cuivre n’est encore réalisée.

Contrôle KiCad : **0 problème de parité schéma/PCB**, 116 éléments non connectés et 86 violations DRC. Les violations portent sur la sérigraphie et les dégagements ; les huit violations cuivre concernent les pads du LIS2HH12 espacés de 0,15 mm face à la règle par défaut de 0,20 mm. Les règles doivent être définies selon les capacités du fabricant avant routage. Aucun contrôle n’a été désactivé.

Le rapport est dans `pcb_drc.json`. Cette version n’est pas un dossier de fabrication. La feuille BQ25570 reste inchangée, y compris NC et C22.

Si l’éditeur PCB était déjà ouvert lors de la modification du fichier, le fermer sans enregistrer l’ancienne vue puis rouvrir ce fichier pour charger le placement actuel.
