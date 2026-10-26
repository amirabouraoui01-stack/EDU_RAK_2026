# BQ25570 — réglage pour supercapacité 4 V maximum

[Accueil](../README.md) · [Valeurs calculées](reglage_bq25570.json)

## Hypothèses et changement autorisé

Amira indique une supercapacité 4 V et demande de régler les résistances d’hystérésis. Cette nouvelle demande remplace la consigne précédente de conserver toute la feuille BQ à l’identique. Le fichier d’origine reste dans l’archive EDU RAK. Les éléments NC, C22 et les autres composants BQ ne changent pas.

Faute de référence complète, 4 V est traité comme une tension maximale à ne pas atteindre en réglage nominal, et non comme une consigne de charge. La capacité, l’ESR, les courants admissibles et la tension du panneau restent à relever.

## Équations et valeurs retenues

Avec VBIAS nominal = 1,21 V, les équations 2 à 5 de la [datasheet TI SLUSBH2G](https://www.ti.com/lit/ds/symlink/bq25570.pdf) donnent :

```text
VBAT_OV       = 1,5 × VBIAS × (1 + ROV2/ROV1)
VBAT_OK_bas   = VBIAS × (1 + ROK2/ROK1)
VBAT_OK_haut  = VBIAS × (1 + (ROK2+ROK3)/ROK1)
VOUT          = VBIAS × (1 + ROUT2/ROUT1)
```

| Réglage | Résistances | Résultat nominal |
|---|---|---|
| Fin de charge | ROV1 = 6,19 MΩ ; ROV2 = 6,81 MΩ | 3,8118 V |
| Seuil bas / reprise | ROK1 = 4,22 MΩ ; ROK2 = 7,87 MΩ ; ROK3 = 464 kΩ | 3,4666 V / 3,5996 V |
| Hystérésis VBAT_OK | Même pont ROK | 133,0 mV |
| Rail RAK et module Pololu | ROUT1 = 4,99 MΩ ; ROUT2 = 7,87 MΩ | 3,1184 V |

Les sommes valent respectivement 13 MΩ, 12,554 MΩ et 12,86 MΩ. **Employer des résistances de précision 0,1 % pour ces sept résistances**, pas les tolérances génériques de l’ancienne carte. ROK1 et ROK2 gardent leur valeur mais leur précision est maintenant spécifiée.

TI donne une précision globale de seuils de ±2 % avec résistances à 0,1 %. La limite de charge majorée à +2 % vaut environ 3,888 V ; avec une enveloppe conservatrice de +2,2 %, environ 3,896 V, sous 4 V. Ce calcul statique ne couvre pas les dépassements transitoires ni une mauvaise connexion du stockage.

## Fonctionnement réel de l’hystérésis

VOUT_EN n’est plus forcé à VSTOR : il reçoit VBAT_OK. Le buck reste éteint jusqu’au seuil haut, puis alimente PWR via J3. En décharge, il s’arrête au seuil bas. Cela évite de compter uniquement sur un futur logiciel pour arrêter la charge utile. La radio et le capteur s’arrêtent alors : le tableau de bord doit afficher un état périmé/inconnu en l’absence de messages.

L’hystérésis de régulation de charge VBAT_OV est interne au BQ ; ROK3 règle l’écart de VBAT_OK, pas cette hystérésis interne. VBAT_OK est suivi par PA0 à travers R8 = 1 MΩ et R9 = 3,3 MΩ ; ce pont ne pilote pas VOUT_EN.

## Pourquoi réduire la sortie à environ 3,12 V

Le rail précédent d’environ 3,36 V laissait peu de marge entre la tension de stockage et la sortie buck près de la coupure. Le RAK3172 et le module Pololu 3692 sont compatibles avec le nouveau rail. La marge obtenue doit encore être vérifiée en émission, avec les tolérances, le courant et l’ESR réels. Ce rail n’est pas automatiquement compatible avec toutes les cartes marquées 3,3 V.

Le buck est donné jusqu’à environ 110 mA typiques selon les conditions TI. Le courant capteur et le courant radio s’additionnent ; décaler leurs phases actives et mesurer les pointes avant d’annoncer une alimentation validée. La tension d’entrée solaire doit également respecter les contraintes de VIN et de VBAT_OV de TI. J19 reste sur VSTOR ; la protection interne liée à VBAT ne doit pas être supposée effective pour tout branchement externe.

## Essais nécessaires

Faire varier lentement la tension de stockage pour relever la coupure et la reprise, vérifier la fin de charge sans dépasser la limite réelle du composant, observer PWR et VBAT_OK pendant une mesure puis une émission radio, et tester une recharge lente sous faible lumière. La tension maximale seule ne permet pas de calculer l’autonomie : il faut aussi connaître la capacité et les pertes. Pour une supercapacité, l’énergie entre deux tensions dépend de `0,5 × C × (Vhaut² − Vbas²)`.
