# Y16mf : variante du balayage M06 pour deux articles du groupe Y16

Ce dossier porte les corrections du balayage M06 sur deux articles qui appartiennent au groupe Y16. J'ai lu la production en lecture seule le 29 octobre 2026. Le détail des pistes est dans `apply/M06/DECISIONS.md` et `audit/sweeps/M06.json`.

## Corrections

- **46 AZA sexies** (annexe III, LEGIARTI000018663273) : G F3, base légale éteinte.
  - Défaut : CGI 200 quaterdecies est en état PERIME depuis le 1er juillet 2026 (LEGIARTI000051213097). Ce crédit était réservé aux prêts dont l'offre a été émise avant le 1er janvier 2011.
  - Correction : abrogation (`full_repeal`). Aucun document ne peut plus être exigé sur le fondement de cet article.
  - Transition : les crédits antérieurs, ainsi que leurs contrôles, reprises et recours, restent régis par leurs règles. La dispense des pièces de chantier déjà décidée est conservée.
- **111-0 D** (annexe III, LEGIARTI000029043440) : G F3, renvoi mort.
  - Défaut : le I renvoyait à « la déclaration annuelle de récolte prévue à l'article 407 du code général des impôts ». L'article 407 est ABROGE depuis le 1er juillet 2025 (LEGIARTI000041985072).
  - Correction : le renvoi est retiré. La période de calcul et le fond ne changent pas.
  - Mises à jour : les citations proposées du substantive_impact et la note qui disait 302 P et 407 « absents du corpus ».

## Contrôle

`python3 -B apply/check_changes.py Y16mf` donne 2 lignes construites et validées, et `problems` est vide.

Revue IA : rien de ceci ne vaut validation par un juriste.
