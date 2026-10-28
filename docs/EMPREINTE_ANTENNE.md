# Empreinte de l’antenne IFA 868 MHz dans KiCad

L’empreinte personnalisée est générée depuis la géométrie de l’antenne simulée dans CST :

- Fichier : [`IFA_868_CST_30x20_PisteFine.kicad_mod`](../VeillePorte/footprints/VeillePorte_Antennes.pretty/IFA_868_CST_30x20_PisteFine.kicad_mod)
- Bibliothèque projet : [`fp-lib-table`](../VeillePorte/fp-lib-table), bibliothèque `VeillePorte_Antennes`
- Composant du schéma : `AE1`, dans [`veilleporte_complet.kicad_sch`](../VeillePorte/veilleporte_complet.kicad_sch)
- Générateur : [`build_antenna_footprint.py`](../tools/build_antenna_footprint.py)
- Correspondance des géométries CST/KiCad : [`empreinte_antenne.json`](empreinte_antenne.json)

Les trois pastilles de l’empreinte correspondent à une pastille RF personnalisée et deux pastilles de masse portant toutes deux le numéro 2. Le keepout cuivre de la zone rayonnante couvre les quatre couches du PCB. La pastille RF inclut les conducteurs du radiateur, du point d’alimentation et du court-circuit IFA. Le groupe de pads est déclaré comme *net tie*, car le court-circuit RF–masse fait partie de cette antenne.

Dans le schéma, AE1 possède deux broches : 1 sur `/RF_ANT` et 2 sur `GND`. La broche RF est reliée au RAK par R12 de 0 Ω ; C6 et L1 conservent leurs empreintes d’adaptation 0603 non montées. La branche de court-circuit de l’IFA rejoint la pastille de masse située à x = −4 mm dans le repère local. L’autre pastille GND est décalée à x = +2,5 mm pour laisser accessible l’entrée RF. Le groupe de pastilles 1/2 est un net tie intentionnel.

La zone rayonnante occupe 30 × 20 mm sur le PCB 40 × 60 mm, soit un quart de sa surface. Le substrat FR4 reste présent sous le cuivre d’antenne ; l’exclusion des plans de cuivre couvre les quatre couches. Le contour de référence 30 × 60 mm du modèle CST n’est plus dessiné comme s’il était le contour du PCB actif.

Le PCB est entièrement connecté et son DRC ne relève aucune erreur ni avertissement. La piste, les pastilles, les zones d’exclusion et les contours de l’empreinte ont maintenant une orientation cohérente. Le cuivre du radiateur conserve ses dimensions CST.

**L’accord radio reste à revalider.** Le fichier CST source utilisait un substrat de 0,8 mm ; la carte courante reprend les 1,6 mm du projet de Diana et passe à quatre couches. Le plan GND interne est sur In2.Cu. Le DRC ne démontre ni une impédance de 50 Ω ni une résonance à 868 MHz sur cet empilage. La carte, le panneau solaire et le boîtier réels doivent être intégrés à la nouvelle simulation et contrôlés au prototype.
