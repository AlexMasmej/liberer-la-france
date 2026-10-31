# R6 — application des demandes de correction émises par BM1 et BM2 (paquet `audit/baseline/requests-R6.json`)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite `mode=ro`, `query_only`), le 31 octobre 2026. Une consultation de Légifrance le 31 octobre 2026 : ordonnance n° 2026-648 du 22 juillet 2026 (JORFTEXT000054456926), art. 1er, 4° et 12°. Revue IA, sans validation par un juriste.

Décompte : 12 demandes ; 10 appliquées, 0 fusionnée (aucune des douze cibles n'a de changement en attente dans un dossier de `audit/baseline/fix-folders-2.json`), 2 non appliquées (notes seulement). Dossiers : `apply/R6` (5), `apply/W01ce` (1), `apply/J06ce` (3), `apply/B08ce` (1), tous validés (`problems` vide).

## Appliquées dans `apply/R6` (articles sans propriétaire)

1. **travail D3141-37** (LEGIARTI000018534227, maintenu) — demande BM1 (BASELINE-BM1-D3141-11) — appliquée, `replace`, passage en `rewrite_draft` (`coordination_only`).
   - Défaut vérifié : la source dit « aux contrôleurs agréés de la caisse d'affiliation dont il relève, qu'il est à jour de ses obligations envers celle-ci » ; L3141-33 proposé dispose « L'exercice de cette mission n'est soumis ni à un agrément ni à son renouvellement » et limite la communication aux « seules pièces nécessaires à la vérification de leurs obligations relatives aux congés payés qui ne sont pas déjà légalement à la disposition de la caisse » ; D3141-11 proposé abroge l'agrément. Les notes de L3141-33 et de D3141-11 demandaient cette coordination.
   - Changement : justification à tout moment conservée envers l'inspection du travail et les officiers de police judiciaire ; communication aux contrôleurs de la caisse limitée selon L. 3141-33 ; transition ; aucune formalité de remplacement. Bilan d'impact `coordination_only` ajouté.
   - Non touché : R3143-1 (la dispense de sanction est portée par L3141-33 proposé).

2. **css D323-3** (LEGIARTI000006736472) — demande BM2 (BASELINE-BM2-L323-4-1) — appliquée, `replace`, texte, motif, notes et bilan d'impact de la demande repris tels quels (format `<br />` de la proposition en production conservé).
   - Défaut vérifié : L323-4-1 proposé ouvre la sollicitation « sans durée minimale préalable » ; la proposition de D323-3 gardait « En cas d'interruption de travail de plus de trois mois » (déjà contraire aux trente jours de la loi n° 2025-1403) et subordonnait la communication à l'examen de préreprise que R4624-29 (maintenu) réserve aux arrêts de plus de trente jours.
   - Changement : seuil retiré ; examen de préreprise « le cas échéant […] lorsque l'assuré peut en bénéficier » ; transition. R4624-29 n'est pas étendu (extension de faveur non décidée).

3. **travail R3232-3** (LEGIARTI000018533840), 4. **R3232-4** (LEGIARTI000043128618), 5. **R3232-6** (LEGIARTI000022357066) — demandes BM2 (BASELINE-BM2-R3232-7) — appliquées, `replace`.
   - Défaut vérifié : L3232-8 (« L'Etat rembourse à l'employeur une fraction de l'allocation complémentaire ») est au corpus à l'état ABROGE (2008-05-01 → 2013-06-17, loi n° 2013-504 du 14 juin 2013) ; L3232-7 met l'allocation à la charge de l'employeur ; le 1° de L3232-9 n'est qu'une habilitation de modalités. La proposition de R3232-3 organisait pour l'avenir une part de l'Etat de 50 % sur ce seul fondement ; R3232-4 et R3232-6 organisaient son versement et son paiement direct. Les notes disaient à tort L3232-8 « absent du corpus actif ».
   - Changement : taux de 50 % limité aux périodes couvertes par L3232-8 avant son abrogation ; aucun remboursement pour l'avenir sur ce fondement ; états nominatifs et paiement direct rattachés aux « périodes mentionnées à l'article R. 3232-3 » ; dispense de visa, délai de trois mois, compétence préfectorale et dispense de proposition préalable inchangés ; droits antérieurs préservés. Même sens que R3232-7 corrigé (`apply/BM2`, en attente). Bilans d'impact de R3232-4 et R3232-6 : phrase de `scope_limitations` mise à jour (le fondement n'est plus « incertain », il est éteint).
   - Point laissé à l'auteur : rétablir une participation de l'Etat exigerait une disposition législative. R3232-8 (avance par l'Etat au travailleur à domicile, remboursée par l'employeur) n'est pas modifié.

## Non appliquées (`skipped`)

- **travail R2145-5** (LEGIARTI000045680792) — demande BM1 (BASELINE-BM1-R2145-4) : notes seulement (défaut m). Aucun dossier en attente ne modifie l'article ; conformément à la consigne, non appliquée. La rectification demandée reste pertinente si R2145-5 est modifié un jour.
- **cch R315-77** (LEGIARTI000006897047, Z05) — demande BM1 (BASELINE-BM1-R315-78) : notes seulement (défaut m). Aucun dossier en attente ne modifie l'article ; non appliquée. Les notes disent encore à tort L315-20 et L315-21 « absents du corpus ».

## Dossiers de variante

- `apply/W01ce` : css R752-20 (W01), demande BM1 (BASELINE-BM1-D752-6). Voir son DECISIONS.md.
- `apply/J06ce` : cch annexes III à D353-127, III à D353-32, III à D353-190 (J06), demande BM2 (BASELINE-BM2-ANNEXE-I-D353-127). Voir son DECISIONS.md.
- `apply/B08ce` : cch annexe V à D353-127 (B08), même demande. Voir son DECISIONS.md.

## Points pour l'auteur

- R752-19, R752-20-1, R752-21 et R752-22 (css) renvoient encore à L. 752-3-1, renuméroté L. 760-15 ; hors paquet, non corrigés.
- Participation de l'Etat à l'allocation complémentaire de rémunération mensuelle minimale : base légale abrogée en 2013 ; un rétablissement relève de la loi.
- « inspection générale de l'équipement » (annexe I à D353-127) : successeur hors corpus, non corrigé (déjà signalé par BM2).

Revue IA : rien de ceci ne vaut validation par un juriste.
