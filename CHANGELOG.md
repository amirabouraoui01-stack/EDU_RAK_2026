# État publié — 27 octobre 2026

## 2026-10-28 — PCB quatre couches routé

- Sauvegarde du projet avant reprise dans `archives/2026-10-28_avant_reprise_40x60.zip`.
- PCB 40 × 60 × 1,6 mm ; zone antenne 30 × 20 mm, court-circuit IFA et exclusion de cuivre corrigés.
- Plan GND In2.Cu, 19 vias GND, perçages des vias ≥ 0,3 mm ; RF 0603 et C22 non monté conservés.
- Pastilles de fils solaires sur J10 et connecteurs latéraux.
- Routage connecté : 427 segments, 55 vias ; DRC et parité schéma/PCB sans violation ni connexion manquante.
- Export STEP, vues 3D, audit des pistes, PDF et netlist actualisés. Accord radio à revalider sur l’épaisseur de 1,6 mm et dans le boîtier.

Version retenue du projet VeillePorte :

- Schéma KiCad A2 unique, netlist et rapport ERC à jour.
- Antenne IFA 868 MHz issue de l’étude CST reliée à RF et à la masse dans le schéma.
- BQ25570 configuré pour stockage supercondensateur 4 V maximum ; NC et C22 sont conservés.
- Module VL53L4CD Pololu 3692 relié par J23.
- PCB, firmware, farfield exporté et validations physiques restent à réaliser.

L’historique des modifications antérieures est conservé dans l’historique Git.


- PCB KiCad créé depuis le schéma complet ; empreinte d’antenne CST AE1 importée. Placement et routage restant à faire.

- PCB : contour Edge.Cuts arrondi 60 x 70 mm, empilement cuivre 4 couches ; DRC sans erreur de contour.

- Implantation du PCB : RAK3172 au centre, connecteurs en périphérie, dégagement d’antenne maintenu ; aucun routage effectué.
