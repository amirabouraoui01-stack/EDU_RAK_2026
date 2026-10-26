> Révision IR : les vues PCB ci-dessous sont historiques (avant IR). Le nouveau schéma utilise le module VL53L4CD.

# Galerie des schémas

[Accueil](../README.md) · [PDF complet](../VeillePorte/veilleporte.pdf)

Images issues des exports KiCad actuels. Elles montrent les fichiers de conception, pas une carte fabriquée.

## PCB routé — 60 × 30 mm

![Face avant, cuivre et implantation](assets/pcb_avant.png)

![Face arrière en miroir, plan de masse et pistes](assets/pcb_arriere.png)

[Ouvrir le PCB](../VeillePorte/archive_avant_ir/veilleporte.kicad_pcb) · [Lire les contrôles et les hypothèses](../VeillePorte/PCB.md).

## RAK3172 et antenne générique 868 MHz

![RAK3172 et antenne 868 MHz indicative](assets/schema_rak3172.png)

[Feuille RAK3172](../VeillePorte/rak3172.kicad_sch).

## Accélération — VL53L4CD

![VL53L4CD, I²C et INT1](assets/schema_ir.png)

[Feuille capteur IR](../VeillePorte/capteur_ir.kicad_sch).

## Alimentation — BQ25570 — supercapacité 4 V

![BQ25570 EDU RAK avec éléments NC et C22 conservés](assets/schema_bq25570.png)

[Feuille BQ25570](../VeillePorte/alimentation.kicad_sch), adaptée aux seuils de la supercapacité 4 V.
