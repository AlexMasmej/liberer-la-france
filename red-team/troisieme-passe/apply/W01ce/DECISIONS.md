# W01ce — variante R6 pour un article de W01

Demande du groupe BM1 (objection BASELINE-BM1-D752-6), appliquée par le groupe R6. Voir `apply/R6/DECISIONS.md`.

**css R752-20** (LEGIARTI000021647722, maintenu) — appliquée, `replace`, passage en `rewrite_draft` (`coordination_only`).

- Défaut vérifié en production : les trois renvois (premier et deuxième alinéas du I, premier alinéa du II) visent « L. 752-3-1 », dont la dernière version au corpus (LEGIARTI000053280475) est à l'état TRANSFERE au 23 juillet 2026. L'ordonnance n° 2026-648 du 22 juillet 2026 (JORFTEXT000054456926, lue sur Légifrance le 31 octobre 2026), art. 1er, 4°, dispose que « l'article L. 752-3-1, qui devient l'article L. 760-15 » ; son 12° ne modifie que le premier alinéa, le V bis et le V ter, de sorte que les 1° et 2° du I visés par R752-20 subsistent. Aucune clause générale de substitution des références dans l'ordonnance. L. 760-15 n'est pas au corpus (réserve documentaire).
- Changement : texte de la source reproduit sans autre modification que la substitution de « L. 760-15 » à « L. 752-3-1 » aux trois occurrences ; notes et bilan d'impact rectifiés (L752-3-1 n'est pas « manquant »). Cohérent avec D752-6 corrigé (`apply/W03ca`, en attente), qui renvoie déjà à L. 760-15.
- Non touchés, hors paquet : R752-19, R752-20-1, R752-21, R752-22 portent les mêmes renvois.

`python3 -B apply/check_changes.py W01ce` : `problems: []` (diagnostic attendu : renvoi L752-3-1 retiré, L760-15 ajouté). Revue IA, sans validation par un juriste.
