# Empreinte de l’antenne IFA 868 MHz dans KiCad

L’empreinte personnalisée est générée depuis la géométrie de l’antenne simulée dans CST :

- Fichier : [`IFA_868_CST_30x20_PisteFine.kicad_mod`](../VeillePorte/footprints/VeillePorte_Antennes.pretty/IFA_868_CST_30x20_PisteFine.kicad_mod)
- Bibliothèque projet : [`fp-lib-table`](../VeillePorte/fp-lib-table), bibliothèque `VeillePorte_Antennes`
- Composant du schéma : `AE1`, dans [`veilleporte_complet.kicad_sch`](../VeillePorte/veilleporte_complet.kicad_sch)
- Générateur : [`build_antenna_footprint.py`](../tools/build_antenna_footprint.py)
- Correspondance des géométries CST/KiCad : [`empreinte_antenne.json`](empreinte_antenne.json)

Les trois pastilles de l’empreinte correspondent à une pastille RF personnalisée et deux pastilles de masse portant toutes deux le numéro 2. La pastille RF inclut les conducteurs du radiateur, du point d’alimentation et du court-circuit IFA. Le groupe de pads est déclaré comme *net tie*, car le court-circuit RF–masse fait partie de cette antenne.

Dans le schéma, AE1 a deux broches : broche 1 sur `/RF` et broche 2 sur la masse du projet (`'EN`, le net de masse global utilisé par cette feuille). L’export de netlist KiCad confirme l’empreinte et ces deux réseaux. La bibliothèque de l’empreinte s’ouvre avec le projet KiCad grâce à `${KIPRJMOD}`.

## Utilisation

Ouvrir `VeillePorte/veilleporte_complet.kicad_pro`, puis lancer **Mettre à jour le PCB depuis le schéma**. Placer AE1 au bout de la carte en conservant sa zone de 30 × 20 mm. L’empreinte ajoute un keepout cuivre sur les couches avant et arrière autour du radiateur ; vérifier son placement, les plans de masse, la connexion de masse, les distances au panneau solaire et au boîtier, puis exécuter le DRC après création du PCB.

Le dépôt ne contient pas encore de PCB réimplanté pour cette nouvelle version du capteur. L’ancienne carte routée appartient au projet accéléromètre et ne doit pas servir de carte de fabrication pour VeillePorte.

Cette empreinte est une traduction de la géométrie simplifiée CST, pas un modèle de fabrication validé. Vérifier les largeurs minimales de cuivre et de masque auprès du fabricant et mesurer l’accord RF sur le premier prototype.
