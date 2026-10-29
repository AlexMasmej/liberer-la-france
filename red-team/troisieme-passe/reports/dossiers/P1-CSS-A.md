# Dossier P1-CSS-A — qualification des alertes « renvoi vers une abrogation proposée » (Code de la sécurité sociale, paquet A)

Red-team juridique indépendante, troisième passe. Rédigé le 26 octobre 2026 sur l'instantané figé `20261026T230545Z` (corpus de référence au 18 octobre 2026). Alertes d'origine : audit GLOBAL `global-reference-audit-20261025T2341Z`, requalifiées dans `reports/p1-work/P1-CSS-A.json` (39 clusters, 107 alertes, toutes au statut « live »).

**Avertissement.** Il s'agit d'une revue faite par une IA. Elle ne vaut pas validation par un juriste. La seconde passe continue en production : 46 des 77 textes référents lus et 14 des 39 cibles sont encore au statut d'inventaire `pending`. Ces conclusions restent donc provisoires. Aucune écriture n'a été faite en production, dans l'instantané ou dans les preuves scellées. Aucun script de production n'a été lancé. Aucune consultation en ligne n'a été nécessaire.

## 1. Synthèse

| Classification des 107 alertes | Nombre |
|---|---|
| alerte écartée | 70 |
| coordination manquante | 24 |
| incohérence du projet | 10 |
| risque juridique | 1 |
| faux positif | 2 |
| couvert par un autre dossier | 0 |
| non examiné | 0 |

Ces alertes donnent **19 objections** (une par effet juridique distinct) :

| Priorité | confirmé | à confirmer | Total |
|---|---|---|---|
| P0 | 0 | 0 | 0 |
| P1 | 6 | 0 | 6 |
| P2 | 11 | 2 | 13 |

Les plus importantes :

- **RT-P1-CSS-A-12 (P1, risque juridique).** D653-1 ouvre le départ anticipé pour carrière longue des avocats. Il désigne la pension comme « la pension prévue à l'article L. 653-1 », article que le projet abroge. Le motif de L653-1 demandait cette coordination ; elle n'a pas été faite. Sans elle, un droit à pension en cours de constitution est fragilisé.
- **RT-P1-CSS-A-04 (P1).** La proposition travail L3133-7 supprime la journée de solidarité au motif que la CSA « demeure régie par l'article L. 137-40 » du CSS. Or le lot sécurité sociale abroge ce même L137-40. On aurait deux énoncés législatifs contraires dans la même loi, et un besoin de financement de l'autonomie qui n'est pas identifié.
- **RT-P1-CSS-A-05 (P1).** Le périmètre de la réduction générale (L241-13 I) inclut encore la CSA sans borne temporelle. Le plafond du coefficient et l'imputation (III, VII) ne sont plus définis de façon certaine après la bascule, et l'année de bascule n'est pas traitée. La même difficulté se pose pour le FNAL (CCH L813-4), hors de ce paquet.
- Trois autres P1 opposent deux propositions entre elles. R137-2 maintient le représentant obligatoire de L138-22, qui est abrogé (A-01). R123-48 déclare maintenu l'agrément de R123-4, qui est abrogé (A-14). R931-1-28 rétablit pour les SGAPS la délibération annuelle de R931-3-13, qui est abrogée (A-15).

## 2. Méthode

1. Pour chaque cluster, lecture intégrale par `tools/cite.py` de la proposition d'abrogation de la cible : source, NOTA, bornes, proposition, motif, notes de revue et statut d'inventaire. Relevé de ses clauses de transition et de neutralisation des renvois.
2. Pour chaque texte référent, lecture intégrale du texte qui porte le renvoi : la proposition si le statut est `rewrite_draft`, la source si `retained_unchanged`. Lecture aussi du motif et des notes. Vérification que le renvoi vise bien le même code et le même article. Les numéros ont été contrôlés par identifiant de version.
3. Critères de qualification :
   - **alerte écartée** : le renvoi est historique ou transitoire, ou il est neutralisé par une clause expresse de la cible ou du texte référent ;
   - **coordination manquante** : un texte maintenu applique encore la règle comme vivante, même si la clause de la cible en neutralise l'effet. La priorité est alors P2 ;
   - **incohérence du projet** : une proposition réécrite s'appuie activement sur la règle abrogée ;
   - **risque juridique** : une faveur ou un droit est menacé.
4. Contrôles complémentaires en lecture seule (SQL `mode=ro`, `query_only`) :
   - toutes les versions LEGI de L138-20, L653-1, L653-2, R351-4 et D653-1 ;
   - le contexte de R137-1, R137-3, L137-6 et L137-9 ;
   - la recherche des autres référents aux mêmes cibles dans le corpus.
5. Chaque citation du fichier JSON a été vérifiée mécaniquement contre le texte de l'instantané (normalisation des seuls espaces). Les empreintes reportées sont celles des fichiers `evidence/cited/20261026T230545Z/`.

## 3. Périmètre réellement lu

Tous les articles ci-dessous ont été lus en entier : source, NOTA, proposition, motif et notes. Chacun est identifié par son code, son numéro, son identifiant de version, son état, ses bornes, le statut de son brouillon et son statut d'inventaire. La colonne « Issue » renvoie aux objections (`A-xx` = `RT-P1-CSS-A-xx`).

| # | Cible abrogée (lue en entier) | Textes référents lus en entier | Alertes | Issue |
|---|---|---|---|---|
| 0 | css L138-22 `LEGIARTI000006741145` (VIGUEUR, 2004-12-21→2999-01-01, rewrite_draft, seconde passe : completed) | css L138-7 `LEGIARTI000006740397` (VIGUEUR, 2004-12-21→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-3 `LEGIARTI000006742133` (VIGUEUR, 2004-12-21→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-5-6 `LEGIARTI000006742404` (VIGUEUR, 2003-12-19→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-5-3 `LEGIARTI000021535696` (VIGUEUR, 2009-12-28→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-5-2 `LEGIARTI000026798837` (VIGUEUR, 2012-12-19→2999-01-01, rewrite_draft, seconde passe : completed)<br>css R137-2 `LEGIARTI000029007635` (VIGUEUR, 2014-05-30→2999-01-01, rewrite_draft, seconde passe : pending)<br>css L245-5-1 `LEGIARTI000037064538` (VIGUEUR, 2018-06-14→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-4 `LEGIARTI000044627452` (VIGUEUR, 2021-12-25→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-2 `LEGIARTI000044627461` (VIGUEUR, 2021-12-25→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-1 `LEGIARTI000044627476` (VIGUEUR, 2021-12-25→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-5-5 `LEGIARTI000053282639` (VIGUEUR, 2025-12-31→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-5-1 A `LEGIARTI000053282643` (VIGUEUR, 2025-12-31→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L245-6 `LEGIARTI000053282660` (ABROGE_DIFF, 2025-12-31→2028-01-01, rewrite_draft, seconde passe : completed) | 13 | A-01, A-02, alerte écartée |
| 1 | css L380-2 `LEGIARTI000037947779` (VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | css D380-5 `LEGIARTI000032919973` (VIGUEUR, 2016-07-22→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R380-4 `LEGIARTI000034623626` (VIGUEUR, 2017-05-06→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R380-3 `LEGIARTI000034623630` (VIGUEUR, 2017-05-06→2999-01-01, retained_unchanged, seconde passe : pending)<br>css L380-3-1 `LEGIARTI000036390105` (VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css D380-1 `LEGIARTI000038405793` (VIGUEUR, 2019-01-01→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R380-6 `LEGIARTI000039222872` (VIGUEUR, 2020-01-01→2999-01-01, retained_unchanged, seconde passe : pending)<br>css L241-2 `LEGIARTI000046805562` (VIGUEUR, 2023-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 9 | A-07, alerte écartée |
| 2 | css L137-40 `LEGIARTI000042675240` (VIGUEUR, 2021-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | travail L3133-7 `LEGIARTI000033020869` (VIGUEUR, 2016-08-10→2999-01-01, rewrite_draft, seconde passe : pending)<br>css D311-2 `LEGIARTI000046021908` (VIGUEUR, 2022-07-04→2999-01-01, retained_unchanged, seconde passe : pending)<br>css L223-9 `LEGIARTI000046808945` (ABROGE_DIFF, 2026-01-01→2027-01-01, rewrite_draft, seconde passe : completed)<br>css L241-6-2 `LEGIARTI000046813028` (VIGUEUR, 2022-12-25→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L241-10 `LEGIARTI000051284555` (VIGUEUR, 2025-02-28→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L241-13 `LEGIARTI000053280526` (ABROGE_DIFF, 2026-01-01→2028-01-01, rewrite_draft, seconde passe : completed) | 6 | A-04, A-05, A-06, alerte écartée |
| 3 | css L243-7-6 `LEGIARTI000041396065` (VIGUEUR, 2019-12-28→2999-01-01, rewrite_draft, seconde passe : completed) | css R243-18 `LEGIARTI000047437198` (VIGUEUR, 2023-04-14→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R243-17 `LEGIARTI000047437207` (VIGUEUR, 2023-04-14→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R243-59 `LEGIARTI000053220874` (VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | 6 | alerte écartée |
| 4 | css R244-4 `LEGIARTI000006749087` (VIGUEUR, 2002-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | css L244-4 `LEGIARTI000006742089` (VIGUEUR, 1989-07-12→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L244-1 `LEGIARTI000029961352` (ABROGE_DIFF, 2015-01-01→2029-01-01, rewrite_draft, seconde passe : completed)<br>css R382-84 `LEGIARTI000034623071` (VIGUEUR, 2017-05-06→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R243-44 `LEGIARTI000035656864` (VIGUEUR, 2017-09-28→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R644-2 `LEGIARTI000047265913` (VIGUEUR, 2023-03-05→2999-01-01, retained_unchanged, seconde passe : pending) | 5 | A-08, A-09, alerte écartée |
| 5 | css R133-7 `LEGIARTI000006746985` (VIGUEUR, 2006-12-14→2999-01-01, rewrite_draft, seconde passe : pending) | css R133-37 `LEGIARTI000018503716` (VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft, seconde passe : pending)<br>css D861-4-1 `LEGIARTI000038336334` (VIGUEUR, 2019-04-05→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R133-9-1 `LEGIARTI000038790609` (VIGUEUR, 2019-07-08→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R133-20 `LEGIARTI000046176912` (VIGUEUR, 2022-08-13→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R114-11 `LEGIARTI000048831095` (VIGUEUR, 2023-12-31→2999-01-01, rewrite_draft, seconde passe : pending) | 5 | alerte écartée |
| 6 | css L245-1 `LEGIARTI000044627476` (VIGUEUR, 2021-12-25→2999-01-01, rewrite_draft, seconde passe : completed) | css R138-10 `LEGIARTI000028093189` (VIGUEUR, 2013-10-21→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R138-19 `LEGIARTI000042389712` (VIGUEUR, 2021-01-01→2999-01-01, rewrite_draft, seconde passe : pending)<br>css L241-2 `LEGIARTI000046805562` (VIGUEUR, 2023-01-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L138-20 `LEGIARTI000051287267` (VIGUEUR, 2025-02-28→2999-01-01, rewrite_draft, seconde passe : completed) | 4 | A-03, alerte écartée |
| 7 | css L137-16 `LEGIARTI000044626637` (VIGUEUR, 2022-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | css D137-1 `LEGIARTI000038895141` (VIGUEUR, 2019-10-01→2999-01-01, rewrite_draft, seconde passe : pending)<br>css L213-1 `LEGIARTI000048701101` (VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 4 | alerte écartée |
| 8 | css L137-11-1 `LEGIARTI000038724885` (VIGUEUR, 2019-07-05→2999-01-01, rewrite_draft, seconde passe : completed) | cgi 83 `LEGIARTI000054373766` (VIGUEUR, 2026-07-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css R137-6 `LEGIARTI000025125509` (VIGUEUR, 2012-01-09→2999-01-01, retained_unchanged, seconde passe : pending)<br>css L241-3 `LEGIARTI000051289018` (VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 3 | A-06, alerte écartée |
| 9 | css R244-6 `LEGIARTI000006748866` (VIGUEUR, 2002-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | css L244-4 `LEGIARTI000006742089` (VIGUEUR, 1989-07-12→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L244-1 `LEGIARTI000029961352` (ABROGE_DIFF, 2015-01-01→2029-01-01, rewrite_draft, seconde passe : completed)<br>css R642-2 `LEGIARTI000047266010` (VIGUEUR, 2023-03-05→2999-01-01, retained_unchanged, seconde passe : pending) | 3 | A-09, alerte écartée |
| 10 | css L245-5-2 `LEGIARTI000026798837` (VIGUEUR, 2012-12-19→2999-01-01, rewrite_draft, seconde passe : completed) | css R245-16-2 `LEGIARTI000019268747` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R245-16-1 `LEGIARTI000019268750` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending) | 3 | alerte écartée |
| 11 | css L133-4-10 `LEGIARTI000033686497` (VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | css L243-2 `LEGIARTI000033713045` (VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css R133-9-4 `LEGIARTI000034702487` (VIGUEUR, 2017-05-11→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R155-4 `LEGIARTI000035656783` (VIGUEUR, 2017-09-28→2999-01-01, rewrite_draft, seconde passe : pending) | 3 | A-11, alerte écartée |
| 12 | css L653-1 `LEGIARTI000037055732` (VIGUEUR, 2018-06-14→2999-01-01, rewrite_draft, seconde passe : completed) | css D653-1 `LEGIARTI000038774519` (VIGUEUR, 2019-07-08→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R653-4 `LEGIARTI000038893089` (VIGUEUR, 2019-11-01→2999-01-01, retained_unchanged, seconde passe : pending)<br>css R351-4 `LEGIARTI000053335565` (VIGUEUR, 2026-01-01→2999-01-01, retained_unchanged, seconde passe : pending) | 3 | A-12, A-13 |
| 13 | css L137-41 `LEGIARTI000042675242` (VIGUEUR, 2021-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | css L223-9 `LEGIARTI000046808945` (ABROGE_DIFF, 2026-01-01→2027-01-01, rewrite_draft, seconde passe : completed)<br>css L241-6-2 `LEGIARTI000046813028` (VIGUEUR, 2022-12-25→2999-01-01, rewrite_draft, seconde passe : completed) | 3 | alerte écartée |
| 14 | css L137-12 `LEGIARTI000053282399` (VIGUEUR, 2025-12-31→2999-01-01, rewrite_draft, seconde passe : completed) | css L213-1 `LEGIARTI000048701101` (VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L241-3 `LEGIARTI000051289018` (VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 3 | alerte écartée |
| 15 | css L137-15 `LEGIARTI000047452686` (VIGUEUR, 2023-09-01→2999-01-01, rewrite_draft, seconde passe : completed) | css L213-1 `LEGIARTI000048701101` (VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft, seconde passe : completed)<br>css L241-3 `LEGIARTI000051289018` (VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 3 | alerte écartée |
| 16 | css R123-4 `LEGIARTI000038790647` (VIGUEUR, 2019-07-08→2999-01-01, rewrite_draft, seconde passe : pending) | css R123-48 `LEGIARTI000006748131` (VIGUEUR, 1999-12-29→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | A-14 |
| 17 | css L815-13 `LEGIARTI000048697753` (VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | css R815-48 `LEGIARTI000006753886` (VIGUEUR, 2007-01-13→2999-01-01, rewrite_draft, seconde passe : pending)<br>css L815-6 `LEGIARTI000044522717` (VIGUEUR, 2022-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 2 | alerte écartée |
| 18 | css L245-5-4 `LEGIARTI000006742401` (VIGUEUR, 2003-12-19→2999-01-01, rewrite_draft, seconde passe : completed) | css R245-16-2 `LEGIARTI000019268747` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R245-16-1 `LEGIARTI000019268750` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | alerte écartée |
| 19 | css L245-5-6 `LEGIARTI000006742404` (VIGUEUR, 2003-12-19→2999-01-01, rewrite_draft, seconde passe : completed) | css R245-16-2 `LEGIARTI000019268747` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending)<br>css R245-16-1 `LEGIARTI000019268750` (VIGUEUR, 2008-07-31→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | alerte écartée |
| 20 | css R931-3-13 `LEGIARTI000030585379` (VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | css R931-1-28 `LEGIARTI000030575584` (VIGUEUR, 2015-05-11→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | A-15 |
| 21 | css L552-4 `LEGIARTI000043982562` (VIGUEUR, 2022-09-01→2999-01-01, rewrite_draft, seconde passe : completed) | css D552-6 `LEGIARTI000041445916` (VIGUEUR, 2020-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | alerte écartée |
| 22 | css L646-3 `LEGIARTI000048683487` (VIGUEUR, 2023-12-28→2999-01-01, rewrite_draft, seconde passe : completed) | css L162-14-1 `LEGIARTI000048688021` (VIGUEUR, 2023-12-28→2999-01-01, rewrite_draft, seconde passe : completed)<br>css D221-1-1 `LEGIARTI000053501200` (VIGUEUR, 2026-02-19→2999-01-01, rewrite_draft, seconde passe : pending) | 2 | alerte écartée |
| 23 | css L137-17 `LEGIARTI000037064366` (VIGUEUR, 2018-06-14→2999-01-01, rewrite_draft, seconde passe : completed) | css L213-1 `LEGIARTI000048701101` (VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | 2 | alerte écartée |
| 24 | css L323-2 `LEGIARTI000051289831` (VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, seconde passe : completed) | travail L323-21 `LEGIARTI000006648776` (VIGUEUR, 1988-01-01→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | faux positif |
| 25 | css L244-8 `LEGIARTI000006742099` (VIGUEUR, 1988-01-06→2999-01-01, rewrite_draft, seconde passe : completed) | travail L1254-26 `LEGIARTI000030436639` (VIGUEUR, 2015-04-04→2999-01-01, rewrite_draft, seconde passe : completed) | 1 | alerte écartée |
| 26 | css L752-3 `LEGIARTI000031323829` (VIGUEUR, 2015-10-16→2999-01-01, rewrite_draft, seconde passe : completed) | css R752-6 `LEGIARTI000006752562` (VIGUEUR, 1985-12-21→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | A-11 |
| 27 | css R815-47 `LEGIARTI000006753878` (VIGUEUR, 2007-01-13→2999-01-01, rewrite_draft, seconde passe : pending) | css R815-48 `LEGIARTI000006753886` (VIGUEUR, 2007-01-13→2999-01-01, rewrite_draft, seconde passe : pending) | 1 | alerte écartée |
| 28 | css L932-51 `LEGIARTI000024041065` (VIGUEUR, 2011-05-19→2999-01-01, rewrite_draft, seconde passe : pending) | css L931-25 `LEGIARTI000030438945` (VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | A-16 |
| 29 | css L912-2 `LEGIARTI000006745476` (VIGUEUR, 2006-06-24→2999-01-01, rewrite_draft, seconde passe : pending) | css R931-1-3 `LEGIARTI000030585263` (VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | A-17 |
| 30 | css D848-2 `LEGIARTI000031674559` (VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | css D848-5 `LEGIARTI000031674673` (VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | 1 | alerte écartée |
| 31 | css R174-16-2 `LEGIARTI000034623683` (VIGUEUR, 2017-07-01→2999-01-01, rewrite_draft, seconde passe : pending) | css R162-30-1 `LEGIARTI000034623661` (VIGUEUR, 2017-07-01→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | A-17 |
| 32 | css R244-2 `LEGIARTI000039346816` (VIGUEUR, 2020-01-01→2999-01-01, rewrite_draft, seconde passe : pending) | css R762-12 `LEGIARTI000038673046` (VIGUEUR, 2019-07-01→2999-01-01, rewrite_draft, seconde passe : pending) | 1 | A-10 |
| 33 | css R215-1 `LEGIARTI000038789435` (VIGUEUR, 2019-07-08→2999-01-01, rewrite_draft, seconde passe : pending) | css R226-1 `LEGIARTI000038789394` (VIGUEUR, 2019-07-08→2999-01-01, rewrite_draft, seconde passe : pending) | 1 | alerte écartée |
| 34 | css R382-94 `LEGIARTI000006749801` (VIGUEUR, 2006-11-01→2999-01-01, rewrite_draft, seconde passe : pending) | css D758-3 `LEGIARTI000041968156` (VIGUEUR, 2020-05-25→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | alerte écartée |
| 35 | css L245-12 `LEGIARTI000006742167` (VIGUEUR, 1997-12-23→2999-01-01, rewrite_draft, seconde passe : completed) | css L136-1-3 `LEGIARTI000045232415` (ABROGE_DIFF, 2022-02-26→2029-01-01, retained_unchanged, seconde passe : completed) | 1 | faux positif |
| 36 | css D543-2 `LEGIARTI000006737260` (VIGUEUR, 2002-08-08→2999-01-01, rewrite_draft, seconde passe : pending) | css D133-2 `LEGIARTI000046356419` (VIGUEUR, 2023-01-01→2999-01-01, retained_unchanged, seconde passe : pending) | 1 | A-18 |
| 37 | css L162-5-2 `LEGIARTI000006740742` (VIGUEUR, 2004-08-17→2999-01-01, rewrite_draft, seconde passe : completed) | css L162-5 `LEGIARTI000051140851` (VIGUEUR, 2025-02-07→2999-01-01, rewrite_draft, seconde passe : completed) | 1 | alerte écartée |
| 38 | css L136-7-1 `LEGIARTI000051287401` (VIGUEUR, 2025-07-01→2999-01-01, rewrite_draft, seconde passe : completed) | css L131-8 `LEGIARTI000053538201` (VIGUEUR, 2026-02-01→2999-01-01, rewrite_draft, seconde passe : completed) | 1 | A-19 |

Lectures complémentaires, toutes dans l'instantané :

- CSS L653-1 : toutes les versions (une seule). L653-2 : trois versions, dont `LEGIARTI000053280412` en vigueur depuis le 31 décembre 2025. L653-5 `LEGIARTI000037055761`.
- R351-4 : huit versions de 1985 à 2026. Le renvoi à L723-10 a été remplacé par L653-1 en 2019. D653-1 : version unique.
- L138-20 : treize versions. L137-6 en sort de façon définitive en 2015.
- R137-1, R137-3, L137-6, L137-9 (contexte de R137-2).
- Extraits ciblés de R138-21, D653-2, R663-4 et D173-21-2. Ce sont des homonymes (R. 138-22, R. 653-1, D. 653-1) et non des référents aux cibles.

## 4. Constats

### P1

**RT-P1-CSS-A-01 — R137-2 maintient le représentant obligatoire abrogé (incohérence du projet, confirmé).**
- Ce que dit la cible : L138-22 proposé dispose que les entreprises non établies « ne sont plus tenus, sur son seul fondement, de désigner ou de maintenir un représentant résidant en France ».
- Ce que dit le référent : R137-2 proposé (pending) dispose que les assureurs « désignent leur représentant dans les conditions prévues à cet article ». Il réserve aussi, sans borne, « la responsabilité du représentant prévue à l'article L. 138-22 ». Ses notes tiennent l'obligation pour légale et non supprimée.
- Effet : un décret imposerait une obligation dont la base législative a disparu. Il serait illégal ou inopérant, et il rétablirait une formalité que l'orientation supprime.
- Discordance préexistante : R137-2 vise des « organismes d'assurances » alors que L138-22 vise toutes les entreprises de la section L138-20, dont la liste ne comporte plus L137-6. Elle ne modifie pas la conclusion.

**RT-P1-CSS-A-04 — Journée de solidarité et CSA : deux lots contradictoires (incohérence du projet, confirmé).**
- Lot travail : L3133-7 (pending) supprime le travail non rémunéré et affirme que « La contribution de solidarité pour l'autonomie due par les employeurs demeure régie par l'article L. 137-40 du code de la sécurité sociale ». Ses notes ajoutent que la recette « n'est pas supprimée dans ce lot ».
- Lot sécurité sociale : L137-40 (completed) l'abroge pour toutes les sommes versées après la loi. Ses notes renvoient l'examen de la journée de solidarité à « une coordination distincte ».
- Effet : antinomie dans la même loi. Les deux sources de financement de l'autonomie disparaissent ensemble sans financement identifié. C'est une fragilité à signaler à l'auteur ; ce dossier ne la tranche pas.
- Correction minimale : rendre le 2° de L3133-7 neutre, en conservant les deux suppressions.

**RT-P1-CSS-A-05 — La réduction générale garde la CSA dans son périmètre (incohérence du projet, confirmé).**
- L241-13 I proposé cite « la contribution prévue à l'article L. 137-40 » sans réserve.
- Or ce I fixe à la fois le plafond du coefficient maximal (III, troisième alinéa) et la clé d'imputation (VII).
- La famille voisine a été bornée : L241-10 III et V, avec la formule « L'extinction de la fraction … ne crée aucune créance au titre d'une contribution fictive ».
- Effet probable pour tous les employeurs éligibles : un coefficient maximal qui dépasse le plafond légal recalculé, ou une fraction sans support d'imputation. L'année de bascule n'est pas traitée alors que le calcul est annuel.
- Même question pour le FNAL (CCH L813-4), hors du paquet.

**RT-P1-CSS-A-12 — Carrière longue des avocats (risque juridique, confirmé).**
- D653-1 (retained, pending) dispose : « La pension prévue à l'article L. 653-1 peut être liquidée avant l'âge prévu à l'article L. 161-17-2… ».
- L653-1, que le projet abroge de façon favorable, ne fait que subordonner le versement au paiement des cotisations. La liquidation et l'abaissement d'âge relèvent de L653-2, dont le II renvoie à L351-1-1.
- Le motif de L653-1 demande expressément de « remplacer cette désignation réglementaire par le fondement approprié de liquidation, sans fermer les carrières longues ». Ce n'est pas fait. D173-21-2 renvoie à D653-1.
- Effet : contestation possible du départ anticipé, alors que le droit est en cours de constitution. P1 et non P0, car une interprétation téléologique reste probable.

**RT-P1-CSS-A-14 — Agrément des directeurs d'établissements avec hébergement (incohérence du projet, confirmé).**
- R123-4 proposé abroge l'agrément, « y compris sur le fondement du renvoi au présent article figurant à l'article R. 123-48 ».
- R123-48 proposé énonce au contraire : « Elle ne supprime pas l'agrément distinct prévu à l'article R. 123-4 ».
- Les deux décrets se contredisent frontalement. L'agrément risque d'être maintenu.

**RT-P1-CSS-A-15 — Délibération annuelle des SGAPS sur l'égalité professionnelle (incohérence du projet, confirmé).**
- R931-3-13 est abrogé.
- R931-1-28 réécrit dispose : « Pour l'application de l'article R. 931-3-13, le conseil délibère annuellement… ».
- Effet : la formalité est maintenue pour les SGAPS seulement, contrairement à l'orientation et à l'égalité de traitement avec les institutions de prévoyance.

### P2

- **A-02 (incohérence).** L138-7 recouvre la contribution des grossistes « en application des articles L. 138-20, L. 138-22 et L. 138-23 ». Ses notes croient L138-22 maintenu.
- **A-03 (coordination).** L138-20 et R138-19 visent sans borne L245-1, L245-5-1 et L245-6. Leurs notes affirment le maintien de ces contributions. La note de L245-1 elle-même relève cette lacune.
- **A-06 (coordination).** D311-2 (CSA) et R137-6 (contribution sur les rentes L137-11-1) calculent ou précomptent encore des contributions supprimées. Le motif de R137-6 dit : « aucune suppression de cette contribution n'est décidée ».
- **A-07 (coordination).** Bloc réglementaire de la cotisation subsidiaire maladie L380-2 (D380-1, D380-5, R380-3, R380-6 et R380-4 réécrit) : textes non bornés, motifs contraires (« Pas de suppression de L380-2 »). La clause de L380-2, « y compris par renvoi réglementaire », limite l'effet. Ces textes restent nécessaires au stock et à L380-3-1.
- **A-08 (incohérence).** R382-84 réécrit maintient « sous les sanctions prévues aux articles R. 244-4 et R. 244-5 ». Même mécanisme dans P1-CSS-B (cluster R244-5) : une seule objection doit être retenue.
- **A-09 (coordination).** R243-44, R644-2 et R642-2 rendent applicables R244-4, R244-5 et R244-6, qui sont abrogés.
- **A-10 (incohérence).** R762-12 réécrit rend applicable R244-2, qui est abrogé (dernier ressort sur les recours en remise).
- **A-11 (coordination).** R133-9-4, R155-4 (troisième alinéa) et R752-6 désignent encore les ministres d'arrêtés fondés sur L133-4-10 et L752-3, qui sont abrogés. Conflit de source préexistant sur la désignation (R133-9-4 : budget et sécurité sociale ; R155-4 : budget seul).
- **A-13 (coordination, à confirmer).**
  - R653-4 1° conserve « sans préjudice des dispositions de l'article L. 653-1 ».
  - R351-4 1° exclut des périodes équivalentes par renvoi à L653-1. Avant 2019, ce renvoi visait L723-10 ; la renumérotation paraît erronée (le rachat relève de L653-5).
  - Effet incertain après abrogation. Réserve documentaire sur l'ancien L723-10.
- **A-16 (coordination).** L931-25 punit encore la méconnaissance de L932-51, qui est abrogé (rapport sur l'intermédiation).
- **A-17 (coordination).** R931-1-3 b) exige le respect de L912-2 (clause de réexamen, abrogée). R162-30-1 impose la circulation du tableau de R174-16-2 (abrogé).
- **A-18 (coordination, à confirmer).** D133-2 réserve D543-2 (abrogé). Les petites allocations de rentrée scolaire pourraient être différées jusqu'à la fin de l'exercice.
- **A-19 (coordination).** L131-8 3° ter affecte sans borne la contribution L136-7-1 III, qui est supprimée. La note de la cible demandait cette borne.

### Alertes écartées (70) et faux positifs (2)

| Motif | Clusters ou référents concernés |
|---|---|
| Neutralisation expresse dans le texte référent | Famille L245-x vers L138-22 : 11 alertes. L223-9, L241-6-2, L241-10 (CSA/CASA). L213-1 4° (plage L137-10 à L137-17). L241-3 I 1°. L241-2 (clause finale). L243-2. L244-1 et L244-4. L380-3-1. L815-6. R815-48. D552-6. D848-5. L162-5. Travail L1254-26. |
| Coordination exacte avec la transition de la cible | R243-18, R243-59 (paragraphe substitué en place, structure ordinale intacte), R245-16-1 et R245-16-2, R133-9-1, R138-10 (période historique de l'ancien c de L138-11). |
| Renvoi neutralisé par la clause de la cible | Plages R133-3 à R133-7 de R133-37, D861-4-1, R133-20 et R114-11 (R133-7 dispose qu'aucun modèle n'est obligatoire). R243-17 (exceptions applicables aux seules majorations anciennes encore dues, motif explicite). R226-1 et D758-3 (plages de compétences ou d'extension sans rétablissement). |
| Faveur ou affectation dont l'objet disparaît avec la charge, sans charge rétablie | CGI 83 2°-0 quater. L162-14-1 5°. D221-1-1 5° (rubrique comptable). D137-1 (condition du taux réduit, applicable aux seuls faits anciens). |
| Faux positif (homonyme d'un autre code) | Travail L323-21 vise l'ancien L. 323-2 du code du travail. L136-1-3 vise L. 245-12 du CASF. |

Suggestion rédactionnelle, non comptée comme objection : borner à R133-6 les plages « R. 133-3 à R. 133-7 », comme le demandent les notes de R133-7.

## 5. Propositions de correction (présentées séparément des constats)

Les passages ci-dessous sont des propositions de la red-team. Ils ne sont inscrits nulle part. Ils préservent les suppressions décidées, les transitions des faits anciens et les faveurs, et n'instituent aucune formalité de remplacement.

### RT-P1-CSS-A-01 (P1, incohérence du projet)

**Texte proposé.** Remplacer le corps proposé de R137-2 par : « Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant abrogation de l'article L. 138-22. À compter de cette date, aucun organisme d'assurance ou assimilé n'est tenu, sur le fondement du présent article, de désigner ou de maintenir un représentant, agréé ou non, ni de présenter un registre fiscal spécial aux agents chargés du contrôle ; aucune liste annuelle de représentants n'est communiquée à ce titre. Ces organismes accomplissent leurs obligations déclaratives et de paiement directement ou par un mandataire de leur choix, sans condition de résidence en France. Les responsabilités personnellement encourues par un représentant à raison des opérations déclaratives et des sommes dues avant cette date restent régies par les dispositions antérieures, avec leurs prescriptions et voies de recours. Les pouvoirs de contrôle et de présentation de documents prévus à l'article R. 243-59 demeurent applicables ; les documents antérieurement conservés restent utilisables sous les garanties qui leur sont applicables. Les obligations fiscales ayant un fondement autonome ne sont pas modifiées. Aucun agrément, registre ou déclaration de remplacement n'est exigé. » Mettre à jour le motif et les notes (prémisse « non supprimée » erronée).

**Justification.** Le texte réglementaire réécrit maintient, comme règle vivante, une obligation légale de représentation que la proposition L138-22 abroge : effet probable sur les assureurs étrangers (désignation exigée sans base légale), contraire à la suppression décidée ; pas de perte de droit certaine, donc P1 et non P0.

**À préserver.** Responsabilités déjà encourues, prescriptions et recours ; dettes et déclarations dues ; contrôles R243-59 (trente jours d'avis, contradictoire 30/60 jours) ; obligations fiscales autonomes ; suppression de l'agrément et du registre 1004 bis déjà proposée ; aucune formalité de remplacement.

**Autres options.** Conserver l'actuelle rédaction R137-2 limitée aux désignations et responsabilités antérieures à l'abrogation de L138-22 (« Pour les seules opérations antérieures… »), si l'on veut garder la suppression de l'agrément fiscal pour le stock.

**Dépendances.** Adopter avec L138-22 proposé ; décrets et formulaires d'identification du représentant à coordonner (déjà signalé dans les notes de L138-22).

### RT-P1-CSS-A-02 (P2, incohérence du projet)

**Texte proposé.** Dans la proposition L138-7, remplacer la première phrase par : « La contribution est recouvrée et contrôlée en application des articles L. 138-20 et L. 138-23. L'article L. 138-22 ne s'applique qu'aux obligations et responsabilités nées avant l'entrée en vigueur de son abrogation, dans les conditions prévues par cet article. » Corriger la note.

**Justification.** Renvoi actif à un article abrogé dans la base de recouvrement d'une contribution maintenue ; la clause de L138-22 empêche d'en tirer une obligation nouvelle, l'effet est surtout rédactionnel.

**À préserver.** Suppression des majorations, pénalités et taxations provisionnelles propres à la contribution ; principal, imputations, restitutions, prescriptions et recours ; produit CNAM de L138-8.

**Autres options.** Reprendre la clause type des propositions L245-x (« la désignation ou le maintien d'un représentant résidant en France ne peut être exigé sur le fondement de l'article L. 138-22 après l'entrée en vigueur de son abrogation »).

**Dépendances.** Indépendant ; même rédaction que la réserve des L245-x.

### RT-P1-CSS-A-03 (P2, coordination manquante)

**Texte proposé.** Ajouter à la proposition L138-20 : « Pour les contributions instituées aux articles L. 245-1, L. 245-5-1 et L. 245-6, le présent article ne s'applique qu'aux contributions demeurant légalement dues au titre des charges comptabilisées ou des années civiles antérieures à leur suppression, dans les conditions transitoires prévues par ces articles. Il ne peut fonder aucune déclaration ni aucun recouvrement au titre des charges ou années qui leur sont soustraites. » Ajouter à R138-19 : « Pour les contributions prévues aux articles L. 245-1, L. 245-5-1 et L. 245-6, la déclaration ne porte que sur les contributions demeurant dues au titre des charges ou années antérieures à leur suppression ; aucune déclaration à néant n'est exigée pour les charges ou années suivantes. » Corriger les deux notes.

**Justification.** Le cadre de recouvrement et de déclaration continue de viser sans borne des contributions supprimées ; les propositions L245-x et L241-2 empêchent tout fait générateur nouveau, l'effet est limité.

**À préserver.** Modèle facultatif et dépôt commun de R138-19 (y compris pour le stock) ; suppression de la majoration de support ; recouvrement, contrôles, restitutions et recours du stock ; contributions L138-1 et L138-10 maintenues.

**Autres options.** Insérer dans L138-20 une clause générale identique à la dernière phrase de L241-2 (« Les renvois … ne constituent pas un fondement autonome de prélèvement »).

**Dépendances.** Avec L245-1 à L245-6 et R245-4 à R245-7 ; R245-18 (renvoi à R245-4, calendrier différent de L245-6) reste à coordonner, hors paquet.

### RT-P1-CSS-A-04 (P1, incohérence du projet)

**Texte proposé.** Remplacer le 2° de la proposition L3133-7 par : « 2° La suppression de la journée de solidarité est sans incidence sur le régime de la contribution de solidarité pour l'autonomie, qui relève exclusivement du code de la sécurité sociale, y compris des dispositions transitoires de l'article L. 137-40 de ce code pour les sommes versées avant son abrogation. Le travail supplémentaire supprimé ne peut être rétabli au motif du maintien ou de la suppression de cette contribution. » Corriger motif et notes des deux articles (référence croisée).

**Justification.** Deux propositions législatives adoptées ensemble affirmeraient l'une la survie, l'autre la suppression de la même contribution : contradiction normative directe, effet probable d'interprétation et de financement.

**À préserver.** Suppression de la journée de solidarité sans réduction de salaire ni récupération ; rémunérations et repos des heures antérieures ; droits APA/PCH ; restitution des indus CSA anciens ; aucune contribution de remplacement.

**Autres options.** Si l'auteur entend conserver la CSA, retirer l'abrogation de L137-40 et ses coordinations (L241-6-2, L223-9, L241-10, L241-13, D311-2) ; cette option revient sur une coupe déjà rédigée et relève d'une décision expresse.

**Dépendances.** Avec L137-40, L3133-8 à L3133-12 et L3134-1 (travail) ; décision de l'auteur sur le financement de l'autonomie (CNSA).

### RT-P1-CSS-A-05 (P1, incohérence du projet)

**Texte proposé.** Dans le I de L241-13, remplacer « la contribution prévue à l'article L. 137-40 du présent code » par « la contribution prévue à l'article L. 137-40 du présent code, pour les seules rémunérations sur lesquelles elle demeure légalement due ». Ajouter un IX : « IX. – Pour les rémunérations versées à compter de l'entrée en vigueur de la suppression de la contribution prévue à l'article L. 137-40, le taux de cette contribution n'est plus inclus dans le périmètre de la réduction ni dans la valeur maximale du coefficient mentionnée au troisième alinéa du III. Il en va de même, pour les revenus afférents aux périodes d'activité postérieures à leur suppression, des contributions mentionnées à l'article L. 813-4 du code de la construction et de l'habitation. Pour l'année civile au cours de laquelle intervient l'une de ces suppressions, la réduction est calculée distinctement pour les rémunérations relevant de chaque régime, selon des modalités fixées par décret, sans double compte. L'extinction de la fraction de la réduction correspondant à une contribution supprimée ne réduit pas les fractions imputables sur les cotisations et contributions maintenues et ne crée aucune créance au titre d'une contribution supprimée. Les réductions afférentes aux rémunérations antérieures et leurs régularisations demeurent régies par les règles qui leur étaient applicables. » Coordonner D241-7 (valeur T).

**Justification.** La réduction générale est calculée et imputée pour tous les employeurs éligibles ; un périmètre incluant une contribution supprimée rend probable un décalage du coefficient maximal et de l'imputation dès la bascule.

**À préserver.** Calcul distinct optionnel par affectation temporaire du contrat unique, facteur congés des missions, III bis, Mayotte, cumul avec L241-18 et L241-18-1 ; aucune baisse de la réduction sur les cotisations maintenues.

**Autres options.** Conserver le coefficient maximal et imputer la fraction devenue sans objet sur les autres cotisations : baisse supplémentaire non décidée et non financée, à réserver à une décision expresse (l'allègement de 3 % de policy reste distinct).

**Dépendances.** Avec L137-40, CCH L813-4 (FNAL, hors paquet), D241-7 (valeur T et formule) et la régularisation annuelle de D241-10 ; dépend de l'allègement de 3 % encore non institué.

### RT-P1-CSS-A-06 (P2, coordination manquante)

**Texte proposé.** D311-2 : insérer après « à l'article L. 137-40 » les mots « , pour les rémunérations versées avant l'entrée en vigueur de sa suppression ». R137-6 : « L'organisme chargé du versement des rentes déclare et acquitte la contribution mentionnée à l'article L. 137-11-1, due au titre des rentes versées avant l'entrée en vigueur de sa suppression, dans les conditions prévues aux articles R. 243-29 et R. 243-30 ou R. 741-80 et R. 741-81 du code rural et de la pêche maritime. Aucune déclaration ni retenue n'est exigée pour les rentes versées à compter de cette date. » Corriger les motifs.

**Justification.** Textes réglementaires maintenus qui organisent encore le calcul ou la déclaration de contributions supprimées ; les clauses législatives de suppression empêchent toute perception nouvelle, l'effet est limité.

**À préserver.** Calcul par mission et taux AT-MP du secteur public (D311-2) ; restitutions des indus et recours ; déductibilité CGI 83 2°-0 quater pour les contributions effectivement acquittées ; censure de 2012.

**Autres options.** Abroger R137-6 pour l'avenir avec maintien pour le stock, sur le modèle de R815-47.

**Dépendances.** Avec L137-40 et L137-11-1 ; R243-29/R243-30 et textes ruraux inchangés.

### RT-P1-CSS-A-07 (P2, coordination manquante)

**Texte proposé.** D380-1 : ajouter « IV. – Le présent article ne s'applique qu'aux cotisations dues au titre des années d'assujettissement antérieures à l'abrogation de l'article L. 380-2, dans les conditions transitoires de cet article. » D380-5 I, R380-3 et R380-6 : après « mentionnées à l'article L. 380-2 », insérer « , pour les seules années au titre desquelles elle demeure légalement due, ». R380-4 : ajouter « V. – Le présent article ne s'applique à la cotisation mentionnée à l'article L. 380-2 qu'au titre des années pour lesquelles elle demeure légalement due en application des dispositions transitoires de cet article. » Corriger les motifs et notes de D380-1, R380-3 et R380-4.

**Justification.** Le bloc réglementaire de la cotisation subsidiaire maladie reste rédigé comme permanent et ses motifs nient la suppression ; la clause de L380-2 interdit l'établissement de la cotisation « y compris par renvoi réglementaire », d'où un effet limité.

**À préserver.** Pour les années antérieures : abattement de 0,5 PASS, plafond de 8 PASS, dégressivité, prorata, non-cumul avec L380-3-1, preuve de la part exacte des époux ou partenaires, appel contradictoire et paiement en trois échéances, suppression de l'assiette forfaitaire de 5 PASS. Cotisation L380-3-1 des frontaliers inchangée.

**Autres options.** Abroger D380-1 pour les années nouvelles par un article de transition autonome reprenant la formule pour le stock.

**Dépendances.** Avec L380-2 et L380-3-1 (inchangé) ; échanges LPF L152 pour les seules années anciennes.

### RT-P1-CSS-A-08 (P2, incohérence du projet)

**Texte proposé.** Dans R382-84, supprimer « , sous les sanctions prévues aux articles R. 244-4 et R. 244-5, » et ajouter à la fin : « Les manquements antérieurs à l'abrogation des articles R. 244-4 et R. 244-5 relèvent des dispositions transitoires de ces articles. »

**Justification.** Une proposition réécrite assortit une déclaration de sanctions dont le projet abroge le fondement ; la clause de R244-4 interdit leur prononcé, l'effet est limité mais la contradiction est active.

**À préserver.** Délai d'un mois, affiliation d'office ou à la requête, modèles facultatifs, garanties sur les données sensibles, droits acquis.

**Autres options.** Aucune autre.

**Dépendances.** Avec R244-4 à R244-6 ; dédoublonner avec P1-CSS-B (cluster R244-5).

### RT-P1-CSS-A-09 (P2, coordination manquante)

**Texte proposé.** R243-44 : « Les dispositions des articles R. 155-4, R. 133-3 et R. 244-7 s'appliquent au recouvrement des cotisations mentionnées au premier alinéa de l'article L. 243-2. Les manquements antérieurs à l'abrogation des articles R. 244-4 et R. 244-5 relèvent des dispositions transitoires de ces articles. » R644-2 : supprimer « R. 244-4 et R. 244-5 » de la liste et ajouter la même phrase transitoire. R642-2 : supprimer « R. 244-6 » de la liste.

**Justification.** Textes de recouvrement maintenus qui rendent encore applicables des contraventions abrogées ; la clause de la cible et la loi pénale plus douce neutralisent l'effet.

**À préserver.** Procédures de recouvrement, privilège, prescriptions et oppositions ; remises de R243-20 et échéanciers de R613-5 ; infractions autonomes (R244-3, travail dissimulé, obstacle au contrôle).

**Autres options.** Aucune autre.

**Dépendances.** Avec R244-4 à R244-6 et P1-CSS-B ; vérifier aussi R382-100, R382-103, D242-27 et R711-16 (non signalés par l'audit).

### RT-P1-CSS-A-10 (P2, incohérence du projet)

**Texte proposé.** Dans R762-12, supprimer « et R. 244-2 » et ajouter : « Les recours contre les décisions de remise relèvent des règles de droit commun relatives au taux du ressort ; les décisions juridictionnelles rendues avant l'abrogation de l'article R. 244-2 conservent les voies et délais de recours qui leur étaient applicables. »

**Justification.** La proposition réécrite rend applicable un article abrogé ; la règle de droit commun issue de l'abrogation est plus favorable, mais le renvoi peut être lu comme maintien du dernier ressort.

**À préserver.** Deux délais d'un mois de régularisation ; dispenses, remises et échéanciers ; aucune dette rétroactive.

**Autres options.** Aucune autre.

**Dépendances.** Avec R244-2 ; notifications de voies de recours à adapter.

### RT-P1-CSS-A-11 (P2, coordination manquante)

**Texte proposé.** R133-9-4 et R752-6 : « Le présent article est abrogé à compter de l'entrée en vigueur de l'abrogation de l'article [L. 133-4-10 / L. 752-3]. L'arrêté pris sur son fondement ne s'applique plus qu'aux [prélèvements afférents aux cotisations recouvrées / communications effectuées] avant cette date. » R155-4 : supprimer le troisième alinéa.

**Justification.** Désignations ministérielles d'arrêtés dont la base législative est abrogée ; effet limité, avec un conflit de source préexistant sur le ministre compétent.

**À préserver.** Régularisations et remboursements des prélèvements anciens ; secret et protection des données transmises ; procédure de contrainte et délai d'un mois de R155-4.

**Autres options.** Conserver R133-9-4 pour la seule liquidation des prélèvements anciens.

**Dépendances.** Avec L133-4-10 et L752-3 ; arrêtés non fournis.

### RT-P1-CSS-A-12 (P1, risque juridique)

**Texte proposé.** Remplacer D653-1 par : « La pension de retraite du régime d'assurance vieillesse de base des avocats peut être liquidée avant l'âge prévu à l'article L. 161-17-2, en application du II de l'article L. 653-2, pour les assurés qui justifient, dans ce régime et, le cas échéant, dans un ou plusieurs autres régimes obligatoires, de périodes d'assurance ou de périodes reconnues équivalentes d'une durée minimale au moins égale à celle fixée à l'article D. 351-1-1, à l'âge et dans les conditions fixées audit article et selon les modalités fixées aux articles D. 351-1-2 et D. 351-1-3. L'abrogation de l'article L. 653-1 ne peut être opposée à une demande de liquidation anticipée ; les pensions liquidées avant cette abrogation conservent leurs droits. »

**Justification.** Le texte qui ouvre le départ anticipé pour carrière longue des avocats désigne la pension par l'article abrogé ; perte ou contestation d'un droit à pension probable sans coordination, sans être certaine (interprétation téléologique possible).

**À préserver.** Départ anticipé carrière longue des avocats, conditions de durée tous régimes, périodes équivalentes, paramètres D351-1-1 à D351-1-3, pensions liquidées, renvoi de D173-21-2.

**Autres options.** Désignation neutre sans renvoi au II de L653-2 (« La pension de retraite de base des avocats ») si la concordance L653-2 II / D653-1 doit encore être vérifiée.

**Dépendances.** Avec L653-1 et L653-2 (inchangé) ; D173-21-2 renvoie à D653-1 et reste correct.

### RT-P1-CSS-A-13 (P2, coordination manquante)

**Texte proposé.** R653-4 1° : supprimer « , sans préjudice des dispositions de l'article L. 653-1 ». R351-4 1° : après vérification de la concordance historique L723-10 → L653-x, remplacer « L. 653-1 » par la référence exacte (vraisemblablement « L. 653-5 ») avec une clause « La présente coordination ne réduit pas les périodes reconnues équivalentes retenues pour les pensions liquidées avant son entrée en vigueur. »

**Justification.** Renvois réglementaires maintenus à L653-1 dans le calcul des périodes ; l'un est neutralisé, l'autre repose sur une discordance de source préexistante dont l'effet après abrogation est incertain.

**À préserver.** Six catégories de périodes validables des avocats (R653-4), arrondi et dates de R351-4, versement effectif, pensions liquidées.

**Autres options.** Laisser R351-4 inchangé en le signalant comme réserve documentaire si la concordance ne peut être établie.

**Dépendances.** Avec L653-1 ; table de concordance de la recodification de 2018-2019 (L723-x → L653-x) à obtenir.

### RT-P1-CSS-A-14 (P1, incohérence du projet)

**Texte proposé.** Remplacer la dernière phrase de R123-48 par : « Elle ne supprime pas l'agrément des agents comptables régi par la présente sous-section. À compter de l'entrée en vigueur de l'abrogation de l'article R. 123-4, les directeurs des établissements ou œuvres sociales fonctionnant en permanence et comportant hébergement ne sont soumis à aucun agrément au titre de leur nomination, ni sur le fondement de la présente sous-section ni sur celui de cet article. »

**Justification.** Deux décrets proposés se contredisent frontalement sur l'agrément des directeurs d'établissements avec hébergement ; maintien probable de l'agrément que le projet supprime.

**À préserver.** Agrément des agents comptables ; exclusions existantes ; assimilation de la nomination à un agrément pour R123-45 ; nominations et agréments antérieurs ; qualifications et protections des personnes hébergées.

**Autres options.** Si l'agrément R123-4 doit être conservé, retirer l'abrogation de R123-4 (contraire à l'orientation).

**Dépendances.** Avec R123-4 ; vérifier la cohérence avec R123-49 à R123-52 et avec le dossier ouvert des douze coordinations (R123-1, R123-1-1), sans le modifier.

### RT-P1-CSS-A-15 (P1, incohérence du projet)

**Texte proposé.** Remplacer l'alinéa de R931-1-28 commençant par « Pour l'application de l'article R. 931-3-13 » par : « L'abrogation de l'article R. 931-3-13 s'applique aux sociétés de groupe assurantiel de protection sociale dans les mêmes conditions et à la même date. Aucune délibération annuelle particulière du conseil sur l'égalité professionnelle et salariale, ni examen particulier d'un rapport ou d'un plan, n'est exigé de ces sociétés sur le fondement du présent article. Les délibérations déjà prises conservent leurs effets ; les obligations légales distinctes d'égalité professionnelle et salariale, de prévention des discriminations, d'information, de consultation et de négociation demeurent applicables. »

**Justification.** La proposition réécrite énonce elle-même, pour les SGAPS, l'obligation annuelle que le projet supprime pour les institutions de prévoyance : maintien probable d'une formalité.

**À préserver.** Suppression des limites d'âge, plancher des limites librement stipulées, autonomie du contrat de travail, obligations légales d'égalité et de non-discrimination.

**Autres options.** Remplacer en outre « R. 931-3-13 à R. 931-3-14-1 » par « R. 931-3-14 et R. 931-3-14-1 » dans le premier alinéa.

**Dépendances.** Avec R931-3-13.

### RT-P1-CSS-A-16 (P2, coordination manquante)

**Texte proposé.** Dans L931-25, remplacer « L. 932-49 à L. 932-51 » par « L. 932-49 et L. 932-50 » et ajouter : « Les faits commis avant l'abrogation de l'article L. 932-51 relèvent des règles d'application de la loi pénale plus douce. »

**Justification.** Incrimination maintenue qui vise une obligation abrogée ; la loi pénale plus douce neutralise l'effet, mais le texte pénal doit être exact.

**À préserver.** Sanctions des incapacités (trois ans, 75 000 €) et des manquements L932-49 et L932-50 (six mois, 7 500 €) ; compte rendu du délégataire.

**Autres options.** Aucune autre.

**Dépendances.** Avec L932-51.

### RT-P1-CSS-A-17 (P2, coordination manquante)

**Texte proposé.** R931-1-3 b) : supprimer « dans le respect des dispositions de l'article L. 912-2, ». R162-30-1 : supprimer « et celles mentionnées à l'article R. 174-16-2 » et ajouter « Les informations relatives aux périodes antérieures à l'abrogation de l'article R. 174-16-2 déjà disponibles peuvent être utilisées dans le respect des règles de protection des données. »

**Justification.** Textes maintenus qui visent encore des formalités supprimées ; les clauses des cibles empêchent leur rétablissement, effet limité.

**À préserver.** Trois voies de constitution et minima ; stipulations de réexamen librement convenues ; communications électroniques de suivi des dépenses ; dotations et répartition L174-8.

**Autres options.** Aucune autre.

**Dépendances.** Avec L912-2 et R174-16-2.

### RT-P1-CSS-A-18 (P2, coordination manquante)

**Texte proposé.** D133-2, second alinéa : remplacer « Sous réserve des dispositions des articles D. 543-2 du présent code et L. 823-7 » par « Sous réserve de l'article L. 823-7 du code de la construction et de l'habitation et, pour les rentrées scolaires antérieures à l'abrogation de l'article D. 543-2, des dispositions de cet article, » et ajouter : « Le présent alinéa ne permet pas de différer le versement de l'allocation de rentrée scolaire due au titre des rentrées postérieures à cette abrogation. »

**Justification.** La réserve de D133-2 vise un article abrogé ; le paiement des petites ARS pourrait être différé jusqu'à la fin de l'exercice, ce qui affaiblit la faveur créée par l'abrogation de D543-2.

**À préserver.** Seuil de non-recouvrement des petits indus, versement intégral des ARS, réserve CCH L823-7.

**Autres options.** Laisser le report possible et le documenter comme choix de gestion.

**Dépendances.** Avec D543-2.

### RT-P1-CSS-A-19 (P2, coordination manquante)

**Texte proposé.** Au 3° ter de L131-8, après « l'article L. 136-7-1 », insérer « légalement due au titre des faits générateurs antérieurs à sa suppression, ainsi que ses régularisations et restitutions, ».

**Justification.** Affectation sans borne d'une contribution supprimée ; une affectation ne crée pas de prélèvement, effet documentaire.

**À préserver.** Toutes les autres affectations, la répartition CSG à 6,6 % avec compensation, les fractions de la taxe sur les salaires pour le stock.

**Autres options.** Ajouter à L131-8 la clause générale de L241-2 sur l'absence de fondement autonome des renvois d'affectation.

**Dépendances.** Avec L136-7-1 ; examiner aussi L131-8 3° pour la CSG sur les jeux (L136-8 I 3°).

## 6. Incertitudes restantes et éléments non examinés

- **Seconde passe en cours.** 46 référents et 14 cibles sont `pending`. Toute proposition citée peut changer : avant d'appliquer une correction, il faut comparer les empreintes de `P1-CSS-A.json` (`proposed_sha256`, `reason_sha256`, `review_notes_sha256`).
- **Versions à fin de validité programmée (ABROGE_DIFF).** L223-9 (fin le 1er janvier 2027), L241-13 et L245-6 (1er janvier 2028), L244-1 (1er janvier 2029), L136-1-3 (1er janvier 2029). Les versions successeurs ne figurent pas dans l'instantané. Les corrections portent sur la version courante seulement. Pour L223-9 et L244-1, cela ne change pas la qualification « écartée ».
- **Réserves documentaires.**
  - Contenu de l'ancien L723-10 et concordance de 2019 (A-13).
  - CGI 1004 bis absent (A-01).
  - Arrêtés d'application (modèle de contrainte R133-7, taux L133-4-10, seuil L752-3, listes D848-5, répartition L174-8) non fournis.
  - Textes CASF, CSP et CIBS non fournis.
  - R382-94 se termine par la mention « abrogée. » dans le droit importé : anomalie de source déjà signalée par sa proposition. Elle n'a pas d'incidence sur l'alerte D758-3.
- **Référents non signalés par l'audit et non examinés ici.**
  - Pour L137-40 : L382-39, L382-41, L243-1-3, L759-7.
  - Pour L380-2 : L242-13, R114-10-2, L759-11.
  - Pour R244-4 et R244-5 : R382-100, R382-103, D242-27, R711-16.
  - Pour L752-3 : de nombreux homonymes et référents (D752-6 à D752-8, R752-19 à R752-22, etc.) dont le rattachement n'a pas été vérifié.
  - Ils peuvent porter les mêmes coordinations que A-05, A-07 et A-09. Ils relèvent peut-être d'autres paquets.
- **Dédoublonnage avec P1-CSS-B.** Le cluster R244-5 de P1-CSS-B porte sur les mêmes référents (L244-4, L244-1, R382-84, R243-44, R644-2). Il devrait renvoyer à A-08 et A-09.
- **Dossiers ouverts.** Aucun cluster du paquet ne touche les articles réservés à d'autres dossiers (D351-9, R123-1, R123-1-1, D224-7, D224-8, R152-8, R153-2, R151-1, R151-3, R612-7, R216-2, R281-4, R213-5, D227-5, D227-6, L224-10, L228-1, L281-6, L216-3, R611-2). La correction A-14 (R123-48) est voisine du dossier des douze, mais n'en modifie aucun article.
- **Fond non évalué.** Ce dossier ne juge pas l'opportunité des suppressions : CSA, forfait social, cotisation subsidiaire maladie, contributions médicaments, récupération ASPA, journée de solidarité. Il signale seulement les besoins de financement non identifiés, sans les chiffrer.
- **Validation.** Aucune validation par un juriste n'est revendiquée.

## 7. Fichiers produits

- `reports/dossiers/P1-CSS-A.md` (le présent rapport)
- `reports/dossiers/P1-CSS-A.json` : 19 objections, avec articles, empreintes, passages vérifiés, références et preuves.
- `reports/p1-work/P1-CSS-A-classification.jsonl` : 107 lignes, une par `finding_id`.
- Preuves : `evidence/cited/20261026T230545Z/` (exports de `tools/cite.py`).
