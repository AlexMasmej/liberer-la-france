# B01zb — variante du balayage Z02 pour un article attribué à B01

**SWEEP-Z02-L757-5** : version de L757-5 applicable à Mayotte au 1er janvier 2028 (LEGIARTI000054467074, VIGUEUR_DIFF, ordonnance n° 2026-647). L'article n'avait pas de proposition : la correction est donc en mode `new`.

- **Qualification** : défaut G (S19b, F4).
  - Le a du 2° remplace des mots de L842-5 (« les conditions mentionnées à l'article L. 512-2 ») que L842-5 proposé ne contient plus.
  - Il rétablirait à Mayotte une condition de séjour régulier des enfants étrangers. Or L842-5 et L512-2 proposés la suppriment.
- **Ce qui change** : seul le a est retiré.
- **Ce qui est repris tel quel** :
  - le 1° (CESEDA applicable à Mayotte, pour le titre du bénéficiaire) ;
  - l'ancien b, qui ajoute l'alinéa sur le statut civil de droit local.
- **Lignes du lot** :
  - `normative_reduction` avec la policy `editorial_direction_2026_10_19` ;
  - `coordination_only` sous la mesure `prestations-familiales-fin-conditions-entree-enfants`, la même que celle de L842-5.
- **Contrôle** : `python3 -B apply/check_changes.py B01zb` donne `problems` vide.
- **Point laissé à l'auteur** : garder à Mayotte une condition propre de séjour régulier des enfants serait un choix politique distinct, que le projet n'a pas tranché.

Revue IA, non validée par un juriste.
