# VL53L4CD — raccordement du module Pololu 3692

[Accueil](../README.md) · [Schéma](../VeillePorte/capteur_ir.kicad_sch)

Le projet utilise le module complet, pas le composant nu. [Documentation et schéma du fabricant](https://www.pololu.com/product/3692). Le module contient son régulateur 2,8 V, les adaptations I²C et les résistances de rappel. Son adresse I²C 7 bits est `0x29`.

| J23, câble du projet | Nom sur module | Liaison côté carte |
|---|---|---|
| 1 | VIN | PWR nominal environ 3,36 V |
| 2 | GND | Masse commune |
| 3 | SDA | PA11, broche 10 RAK3172 |
| 4 | SCL | PA12, broche 9 |
| 5 | VDD | Sortie 2,8 V du module vers grille Q1 uniquement |
| 6 | GPIO1 | Source Q1 ; drain vers PA1, rappel R14 à PWR |
| 7 | XSHUT | PB5, broche 30, drain ouvert |

**Cet ordre est celui du câble J23, pas l’ordre physique des pastilles Pololu.** Relier les fils en suivant les noms du module. Ne pas relier VDD à PWR. XSHUT : commander bas pour arrêter, haute impédance pour laisser démarrer ; ne jamais imposer un niveau haut PWR ou activer un rappel interne haut sur cette ligne.

GPIO1 reste dans le domaine 2,8 V. Q1 BSS138 et R14 100 kΩ adaptent son signal au domaine MCU. Vérifier les niveaux et temps de montée sur banc. Les rappels SDA/SCL sont déjà sur le module ; R12/R13 sont retirées. C11 et C13 découplent l’alimentation du câble près de J23.

## Détection et énergie

Cible proche stable : porte fermée ; distance supérieure valide : ouverte. Deux seuils et une temporisation évitent les oscillations. Une mesure invalide, un capteur débranché ou un reflet parasite doivent conduire à inconnu tant que le comportement n’a pas été caractérisé. Le capteur n’identifie pas la personne ni le sens de passage.

Le mode ULP et le mode distance ne fournissent pas les mêmes données. Les 55 µA annoncés par ST à 1 Hz concernent une configuration ULP du capteur ; ils ne constituent pas le budget total du module et de la carte. La disparition de la cible doit être testée avec ce mode ; ne pas supposer qu’une interruption de présence signale aussi toute ouverture. Voir [le pilote ULP ST](https://www.st.com/en/embedded-software/stsw-img034).

Prévoir des acquisitions espacées ou le mode autonome approprié, le sommeil MCU et des transmissions limitées aux changements plus un message périodique. Mesurer la consommation moyenne et les pointes : Pololu indique environ 25 mA typiques en mesure active et jusqu’à 40 mA de pointe. Ces pointes doivent être vérifiées avec le BQ25570 et le stockage ; aucune autonomie à « 10 % » n’est calculable sans les caractéristiques du stockage.

## État

Schéma de raccordement réalisé, firmware non développé, montage non testé. Le PCB antérieur avec accéléromètre est archivé ; le nouveau PCB reste à concevoir. La feuille BQ25570 est inchangée.
