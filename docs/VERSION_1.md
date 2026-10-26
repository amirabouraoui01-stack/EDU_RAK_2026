# ColisCare — définition de la première version

[Accueil](../README.md) · [Scénario et essais](COLISCARE.md)

Cette spécification décrit le comportement à développer. Le firmware et les essais matériels ne sont pas encore réalisés.

## Démonstration visée

Fixer le boîtier dans un emballage d’essai contenant un objet non fragile. Montrer qu’il distingue le repos d’un choc contrôlé, compte les événements distincts et transmet un bilan à une passerelle de réception configurée.

## Détection et comptage

Les accélérations calibrées `ax`, `ay`, `az` sont exprimées en g. Pour la première démonstration, utiliser un indicateur indépendant de l’orientation : `A = sqrt(ax² + ay² + az²)`. Au repos, A est proche de 1 g ; ce n’est pas une mesure d’accélération dynamique débarrassée de la gravité.

| État | Comportement attendu |
|---|---|
| Initialisation | Vérifier le capteur ; une panne de lecture doit être visible dans le statut |
| Surveillance | Commencer un événement lorsque A dépasse le seuil haut configurable |
| Événement en cours | Conserver le plus grand A et signaler toute saturation par axe |
| Fin d’événement | Attendre que A reste sous le seuil bas pendant une durée configurable ; augmenter le compteur une seule fois |
| Réarmement | Attendre la durée de séparation configurée avant d’accepter un autre événement |

Le seuil bas doit être inférieur au seuil haut. Seuils, durée de retour au calme, séparation, plage et fréquence seront fixés à partir de mesures ; aucune valeur n’est présentée comme un seuil universel de dommage. La séparation peut fusionner deux impacts proches : ce compromis doit être mesuré.

Les saturations doivent être identifiées à partir des mesures de chaque axe, sans présenter le pic tronqué comme une mesure exacte. La première version ne reconnaît pas automatiquement les dommages, la hauteur de chute ni les responsabilités.

## Bilan transmis

Le bilan comprend une version de format, un identifiant de boîtier, un numéro de séquence, le temps écoulé depuis le démarrage, le compteur de chocs terminés, le pic maximal depuis le démarrage et les statuts de saturation et de défaut capteur. Le format binaire sera défini avec le firmware et le décodeur de réception.

Regrouper les événements dans un bilan périodique plutôt qu’émettre pour chaque échantillon. La cadence et la configuration radio restent à déterminer. Le choix entre LoRa point à point et LoRaWAN doit correspondre au matériel de réception disponible.

En l’absence de réception, conserver au minimum le compteur et le pic en mémoire vive pendant que le boîtier est alimenté. Un succès d’émission local ne prouve pas la réception distante. Après une coupure, les données en mémoire vive sont perdues ; la conservation persistante n’est pas incluse dans cette première démonstration.

## Critères de réussite sur banc

- Aucun choc au repos dans les orientations testées ; noter la durée de chaque essai.
- Un événement continu au-dessus du seuil donne un seul incrément.
- Deux événements séparés par le retour au calme et le réarmement donnent deux incréments.
- Le pic du bilan correspond au maximum des échantillons acquis ; les saturations sont signalées.
- Un défaut du capteur est distingué d’une absence de chocs.
- Le bilan reçu contient le même compteur et la même séquence que le journal de test.
- Après coupure, le compteur repart à zéro conformément au comportement documenté.

Ces critères vérifient le prototype, pas l’intégrité d’un colis. Les chocs plus courts que l’acquisition peuvent être manqués ; la capacité de détection doit être évaluée avec la fixation et l’emballage réels.

## Alimentation : décision préalable aux essais matériels

Le BQ25570 et sa feuille sont conservés à l’identique, y compris les résistances NC et C22. Le rail nominal de la conception existante est environ 3,36 V. Aucun modèle de batterie, de supercondensateur ou de source de récupération n’est encore retenu.

Avant de choisir ces éléments, inventorier le matériel disponible, définir la durée de transport et les conditions de récupération d’énergie. À l’intérieur d’un carton opaque, une récupération solaire ne peut pas être supposée disponible.

Relever ensuite le courant moyen de mesure, l’énergie par transmission, le courant de pointe et la chute du rail pendant l’émission. Ces mesures permettront de dimensionner le stockage et de vérifier le démarrage. Ne pas considérer un connecteur de stockage comme compatible avec n’importe quelle batterie : ses connexions et les seuils du circuit existant doivent être examinés avant branchement.

## Ordre de réalisation

1. Inventorier le matériel et identifier la réception LoRa disponible.
2. Choisir l’environnement de programmation compatible avec le module utilisé.
3. Lire et journaliser les axes sur banc, puis implémenter le comptage.
4. Ajouter la transmission et son décodeur.
5. Mesurer la consommation et valider l’alimentation.
6. Tester dans un emballage et consigner les résultats.
