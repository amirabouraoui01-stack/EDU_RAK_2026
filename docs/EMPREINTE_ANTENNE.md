# Empreinte de l’antenne IFA 868 MHz dans KiCad

L’empreinte personnalisée est générée depuis la géométrie de l’antenne simulée dans CST :

- Fichier : [`IFA_868_CST_30x20_PisteFine.kicad_mod`](../VeillePorte/footprints/VeillePorte_Antennes.pretty/IFA_868_CST_30x20_PisteFine.kicad_mod)
- Bibliothèque projet : [`fp-lib-table`](../VeillePorte/fp-lib-table), bibliothèque `VeillePorte_Antennes`
- Composant du schéma : `AE1`, dans [`veilleporte_complet.kicad_sch`](../VeillePorte/veilleporte_complet.kicad_sch)
- Générateur : [`build_antenna_footprint.py`](../tools/build_antenna_footprint.py)
- Correspondance des géométries CST/KiCad : [`empreinte_antenne.json`](empreinte_antenne.json)

Les trois pastilles de l’empreinte correspondent à une pastille RF personnalisée et deux pastilles de masse portant toutes deux le numéro 2. Le keepout cuivre de la zone rayonnante couvre les quatre couches du PCB. La pastille RF inclut les conducteurs du radiateur, du point d’alimentation et du court-circuit IFA. Le groupe de pads est déclaré comme *net tie*, car le court-circuit RF–masse fait partie de cette antenne.

Dans le schéma, AE1 a deux broches : broche 1 sur `/RF` et broche 2 sur la masse du projet (`'EN`, le net de masse global utilisé par cette feuille). L’export de netlist KiCad confirme l’empreinte et ces deux réseaux. La bibliothèque de l’empreinte s’ouvre avec le projet KiCad grâce à `${KIPRJMOD}`.

## Utilisation

Ouvrir `VeillePorte/veilleporte_complet.kicad_pro` et consulter le PCB 40 × 60 mm déjà implanté. La première passe a laissé RF vers AE1 non routé pour respecter le keepout. Vérifier l’accord du modèle sur le contour réel, les plans de masse et les distances au panneau solaire et au boîtier, puis relancer le DRC.

Le PCB VeillePorte est présent, mais son routage est incomplet et le modèle d’antenne CST doit encore être adapté au contour 40 × 60 mm. Ne pas fabriquer la carte dans cet état.

Cette empreinte est une traduction de la géométrie simplifiée CST, pas un modèle de fabrication validé. Vérifier les largeurs minimales de cuivre et de masque auprès du fabricant et mesurer l’accord RF sur le premier prototype.
