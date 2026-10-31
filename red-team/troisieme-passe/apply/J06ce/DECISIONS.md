# J06ce — variante R6 pour trois articles de J06

Demande du groupe BM2 (objection BASELINE-BM2-ANNEXE-I-D353-127), appliquée par le groupe R6. Voir `apply/R6/DECISIONS.md`.

Trois corrections (`replace`), sur la proposition en production (J06bf et X1 déjà appliqués) :

| Article | Occurrences remplacées | Contexte |
|---|---|---|
| Annexe III à l'article D353-127 (LEGIARTI000039049075) | 2 | pénalité de l'article 7 versée au fonds ; « non-versement au fonds » |
| Annexe III à l'article D353-32 (LEGIARTI000039049222) | 3 | pénalité versée au fonds (2) ; « directives du conseil de gestion du fonds » (tiers payant) |
| Annexe III à l'article D353-190 (LEGIARTI000039048922) | 2 | pénalité de l'article 6 versée au fonds ; « directives du conseil de gestion du fonds » |

- Défaut vérifié : « fonds national de l'habitation », organisme que le code ne connaît plus (les cinq seules mentions en vigueur sont dans ces modèles de convention). L811-1 : les aides personnelles au logement « sont financées par le fonds national d'aide au logement » ; L811-2 : ce fonds « est administré par un conseil de gestion » ; R812-1 : « Les directives élaborées par le conseil de gestion du fonds national d'aide au logement fixent les modalités de liquidation et de paiement des aides personnelles au logement » (même formule que D321-33, D353-48, D353-101).
- Changement : substitution de « fonds national d'aide au logement » à chaque occurrence, aucun autre changement ; motif et notes complétés. Pour l'annexe III à D353-127, le `proposed_quote` du bilan d'impact qui contenait l'ancienne désignation est mis à jour (le `source_quote` reste celui de la source) ; le certificat sera recalculé par le coordinateur.
- Même coordination que l'annexe I à l'article D. 353-127 (`apply/J06cb`, en attente).

`python3 -B apply/check_changes.py J06ce` : `problems: []` (les diagnostics de réduction et de renvois sont ceux des lots existants, inchangés). Revue IA, sans validation par un juriste.
