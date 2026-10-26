# ColisCare — suivi des chocs pendant le transport

[Accueil](../README.md) · [Architecture électronique](ARCHITECTURE.md)

## Besoin

Un colis fragile peut subir un choc sans marque évidente sur son carton. ColisCare vise à fournir un indicateur de manipulation pour aider à décider d’inspecter le contenu. Un choc détecté ne prouve pas que l’objet est endommagé et ne détermine pas la responsabilité d’un transporteur.

## Fonctionnement à développer

1. Fixer le boîtier dans l’emballage pour que sa position reste stable.
2. Configurer la plage, la fréquence de mesure et les seuils du LIS2HH12.
3. Détecter les dépassements et regrouper les échantillons d’un même choc pour éviter les doubles comptages.
4. Préparer un bilan : identifiant du boîtier, compteur, pic mesuré, indication de saturation et temps écoulé depuis le démarrage.
5. Transmettre par LoRa 868 MHz lorsqu’une passerelle configurée est accessible.

Le temps écoulé n’est pas une date absolue. La synchronisation horaire, la conservation après coupure et le service de réception restent à développer. Sans stockage persistant testé, une coupure pourrait faire perdre les événements. La carte ne possède pas de GPS ni de liaison directe avec un téléphone.

## Matériel conservé

| Élément | Rôle |
|---|---|
| LIS2HH12 | Accélération sur trois axes et interruption |
| RAK3172 | Acquisition, traitement et transmission LoRa |
| BQ25570 | Circuit d’alimentation existant ; source et stockage à dimensionner |
| J20 et antenne externe | Liaison 868 MHz |
| PCB 60 × 30 mm | Support du boîtier placé dans le colis |

La feuille BQ25570, les résistances NC et C22 sont conservées. Les chemins historiques `Collier_Chien/` restent identiques. Le firmware ColisCare n’est pas encore réalisé.

## Essais prévus

| Essai | Observation attendue |
|---|---|
| Repos dans plusieurs orientations | Pas de faux choc dû à la gravité statique |
| Manipulations normales | Séparation entre mouvement courant et choc à signaler |
| Chocs contrôlés sur emballage d’essai | Répétabilité, saturation et effet de la fixation |
| Vibrations prolongées | Pas de comptage de chaque vibration comme un choc distinct |
| Absence puis retour de couverture | Comportement et reprise de transmission définis |
| Coupure d’alimentation | Conservation ou perte des données vérifiée |
| Émission LoRa | Courant de pointe et stabilité du rail |

Les seuils dépendent de l’objet et de son emballage. L’autonomie, la portée et la capacité à mesurer des chocs très courts restent à valider ; le capteur peut saturer.
