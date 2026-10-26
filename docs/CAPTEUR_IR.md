# VL53L4CD — module Pololu 3692, révision 0.5

[Accueil](../README.md) · [Schéma](../VeillePorte/capteur_ir.kicad_sch) · [Alimentation](ALIMENTATION.md)

Le module Pololu VL53L4CD reste retenu pour ses possibilités de détection ULP. Le VL53L1X Pimoroni PIM373 du lien Kubii est un autre module, avec un autre brochage et un autre pilote ; ce changement n’est pas appliqué. Aucune comparaison d’autonomie réelle entre ces deux cartes n’a été mesurée.

| J23, câble défini pour le projet | Module Pololu | Carte RAK3172 |
|---|---|---|
| 1 | VIN | PWR, environ 3,118 V |
| 2 | GND | Masse |
| 3 | SDA | PA11, broche 10 |
| 4 | SCL | PA12, broche 9 |
| 5 | Non câblé | NC ; ne pas utiliser VDD du module |
| 6 | GPIO1 | PA1, broche 6, entrée sans rappel interne |
| 7 | XSHUT | PB5, broche 30, drain ouvert |

**J23 ne reproduit pas l’ordre physique des pastilles Pololu.** Suivre leurs noms pour fabriquer le câble. VDD est une sortie du module et reste non connectée. SDA/SCL sont déjà adaptés à VIN sur la carte Pololu ; ses rappels sont conservés.

## Pourquoi Q1 a été retiré

GPIO1 est une sortie à drain ouvert avec rappel à 2,8 V sur le module. Le STM32WLE5 du RAK accepte un niveau haut à partir de 0,7 × VDD. Même en majorant le rail prévu à environ 3,19 V, cela représente environ 2,24 V : le niveau 2,8 V est suffisant sans translation supplémentaire. Q1 et R14 ne sont donc pas nécessaires. Ne pas ajouter de rappel PA1 à PWR, pour laisser le module imposer son propre niveau haut. Vérifier les niveaux et les fronts avec le câble réel.

XSHUT se commande uniquement bas ou haute impédance, sans rappel MCU au rail PWR. L’extinction matérielle arrête la détection ; laisser le module actif dans son mode autonome lorsqu’il doit surveiller la cible.

## Ce qui est inclus sur une carte de capteur

Un régulateur d’alimentation et un adaptateur de signaux ont des fonctions différentes. L’indication « 3–6 V » sur un module n’indique pas à elle seule la tension de sa sortie INT. Pour le Pimoroni PIM373, le fabricant annonce une compatibilité 3,3 V / 5 V ; son brochage n’est pas celui utilisé ici. Le schéma détaillé de son interruption n’a pas été confirmé pendant cette revue.

## Énergie et détection

Les 55 µA annoncés par ST correspondent à une configuration ULP à 1 Hz sous 2,8 V du capteur, pas à la consommation totale du système. Le mode ULP ne fournit pas les distances du mode standard. Caractériser l’ouverture et la disparition de cible avant de choisir la stratégie de réveil. Une mesure invalide doit rester distincte d’une porte certainement ouverte. La fréquence d’acquisition détermine le risque de manquer une ouverture brève.

Mesurer les courants moyens et de pointe, notamment le régulateur et les rappels de la carte. Éviter de superposer mesure active du capteur et émission radio avant d’avoir vérifié le budget du buck. Ni l’énergie disponible ni l’autonomie ne se déduisent de la seule indication « 10 % ».

Sources : [Pololu 3692](https://www.pololu.com/product/3692), [seuils GPIO STM32WLE5](https://www.st.com/resource/en/datasheet/stm32wle5cc.pdf), [pilote ULP ST](https://www.st.com/en/embedded-software/stsw-img034), [Pimoroni PIM373](https://shop.pimoroni.com/products/vl53l1x-breakout).
