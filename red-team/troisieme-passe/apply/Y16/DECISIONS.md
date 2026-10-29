# Y16 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Exports : `evidence/cited/production-20261029/`. Paquet : `audit/sweeps/packet-Y16.json`, soit 53 articles de l'annexe III du CGI et 56 pistes (55 S9, 1 S10). Pour chaque piste S9, la ligne `removed_provisions` et la proposition de la loi visée ont été lues. Contrôle : `python3 -B apply/check_changes.py Y16` donne 3 lignes construites, 3 validées et `problems` vide. Les diagnostics sont voulus : réductions déclarées sur les trois lignes, et longueur de 41 terdecies (ratio 2,82 par rapport à la source, du fait de la proposition de seconde passe déjà plus longue).

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 3 (41 quindecies, 41 terdecies, 43 bis), corrigées |
| m | 0 piste ; 4 notes ou motifs périmés relevés, non corrigés |
| déjà réglé | 27 |
| faux positif | 26 |

Corrections : 3 lignes en mode `replace` (41 terdecies ; 41 quindecies et 43 bis, jusque-là maintenus à l'identique, passent en `rewrite_draft`). Aucune demande à un autre groupe, rien d'écarté (`skipped` vide). Pas de fermeture de faille.

## Défauts confirmés et corrigés

- **41 quindecies** (LEGIARTI000006297806, maintenu) et **41 terdecies** (LEGIARTI000025624706), pistes S9 vers CGI 131 ter (LEGIARTI000026949261), G (F1 et F5), corrigés ensemble.
  - Défaut : 131 ter 1 proposé ouvre le régime des valeurs étrangères aux produits futurs des séries émises avant 1976 « sans autorisation préalable, y compris lorsque la série n'a pas été autorisée », sans « demande spéciale ». Pourtant, 41 quindecies maintenu dit encore que le régime « n'a d'effet pour aucune émission qu'à dater de la notification de l'autorisation ministérielle ». Quant à 41 terdecies, il garde la demande spéciale préalable sans réserver les produits futurs. Les notes de ces deux articles (« Aucune ouverture aux nouvelles émissions n'est décidée ») décrivaient la source de 131 ter, pas sa proposition. Les notes de 131 ter annonçaient d'ailleurs cette coordination des annexes.
  - Correction : les deux alinéas source de 41 quindecies sont repris mot pour mot. Ils sont bornés aux produits perçus avant la réforme, ce qui conserve la rétroactivité favorable de 1955. Pour les produits perçus ensuite, aucune demande, autorisation ni notification n'est exigée, et les autorisations acquises sont conservées. Pour 41 terdecies, un dernier alinéa reprend la même dispense, et ses trois premiers alinéas sont inchangés. Aucune formalité de remplacement. La borne du 1er janvier 1976 ne bouge pas. Mesure : `obligations-historiques-fin-autorisation` (coordination, pas une seconde réduction).
- **43 bis** (LEGIARTI000025631743, maintenu), piste S9 vers CGI 6 (LEGIARTI000046197457), G (F1 et F5), corrigé.
  - Défaut : CGI 6 proposé retire l'irrévocabilité et la forclusion de l'option d'imposition distincte de l'année du mariage ou du PACS (« Après l'expiration de ces délais, elle peut être exercée ou révoquée, d'un commun accord »). Le 2° du I de 43 bis soumettait encore définitivement le couple à l'imposition commune faute d'option dans les délais de 175. La note (« option irrévocable ») décrivait la source de 6.
  - Correction : le 2° du I reçoit une seconde phrase. Après ces délais, l'option peut être exercée ou révoquée d'un commun accord, dans les conditions et le délai de réclamation du 5 de 6, et la réclamation commune vaut déclaration rectificative, sans dépôt séparé. Une transition reprend exactement celle de 6 proposé : années civiles commençant après l'entrée en vigueur, années antérieures inchangées. Le reste de l'article est repris mot pour mot. Mesure : `ir-option-couple-rectification` (coordination).

## Défauts mineurs relevés, non corrigés (articles non modifiés, F10)

- 49 septies I ter (LEGIARTI000006298491) et 49 septies I quinquies (LEGIARTI000028390844) : les notes disent que le corpus législatif exige encore l'agrément. Or 244 quater B proposé (LEGIARTI000053544409) l'a retiré.
- 324 AH (LEGIARTI000006299395) : le motif et les notes disent que 1502 I proposé « ne contient toujours pas la dispense totale ». Or 1502 proposé (LEGIARTI000051219159) la contient désormais.
- 369 (LEGIARTI000026848794) : le dernier alinéa renvoie à « l'article 369 de l'annexe III ». C'est une autoréférence, sans effet.
- Hors paquet : la raison de 41 quaterdecies (LEGIARTI000025625001), maintenu, est elle aussi rédigée par rapport à la source de 131 ter. L'article (autorité qui accorde l'autorisation) reste utile pour les produits antérieurs. Il n'a pas été modifié.

## Pistes, une ligne chacune

| Article (annexe III) | Piste | Qualification | Correction |
|---|---|---|---|
| 2 quindecies D | S9 → CGI 31 | déjà réglé | — |
| 2 duovicies | S9 → CGI 31 | déjà réglé | — |
| 41 quindecies | S9 → CGI 131 ter | G | corrigé |
| 41 duovicies I | S9 → CGI 150 VB | faux positif | — |
| 46 AZA quater | S9 → CGI 53 A | faux positif | — |
| 46 E | S9 → CGI 202 ter | faux positif | — |
| 49 septies I ter | S9 → CGI 244 quater B | déjà réglé | — |
| 111-0 E | S9 → CGI 302 D bis | déjà réglé | — |
| 111-0 E | S9 → CGI 302 G | faux positif | — |
| 111-0 F | S9 → CGI 302 D bis | déjà réglé | — |
| 111-0 H | S9 → CGI 302 D bis | faux positif | — |
| 250 A | S9 → CGI 638 A | faux positif | — |
| 251 A | S9 → CGI 638 A | faux positif | — |
| 324 AH | S9 → CGI 1502 | déjà réglé | — |
| 336 ter | S9 → CGI 1622 | déjà réglé | — |
| 360 bis | S9 → CGI 219 | déjà réglé | — |
| 366 L | S9 → CGI 219 | déjà réglé | — |
| 359 | S9 → CGI 219 | déjà réglé | — |
| 46 AZA sexies | S9 → CGI 6 | faux positif | — |
| 41 sexdecies K | S9 → CGI 125 D | faux positif | — |
| 315 terdecies | S9 → CGI 1406 | déjà réglé | — |
| 2 octodecies B | S9 → CGI 31 | faux positif | — |
| 74 | S9 → CGI 286 | faux positif | — |
| 74 | S9 → CGI 277 A | faux positif | — |
| 315 nonies | S9 → CGI 1406 | déjà réglé | — |
| 46 quater-0 YZH | S9 → CGI 223 A | faux positif | — |
| 85 L | S9 → CGI 277 A | déjà réglé | — |
| 85 I | S9 → CGI 277 A | déjà réglé | — |
| 321 G bis | S9 → CGI 1406 | faux positif | — |
| 321 F | S9 → CGI 1406 | faux positif | — |
| 321 G | S9 → CGI 1406 | faux positif | — |
| 41 terdecies | S9 → CGI 131 ter | G | corrigé |
| 360 | S9 → CGI 219 | déjà réglé | — |
| 374 | S9 → CGI 231 | déjà réglé | — |
| 41-0 bis E | S9 → CGI 204 | faux positif | — |
| 38 sexdecies V | S9 → CGI 204 | faux positif | — |
| 49 septies ZO | S9 → CGI 53 A | faux positif | — |
| 49 septies ZB bis | S9 → CGI 53 A | faux positif | — |
| 358 | S9 → CGI 219 | déjà réglé | — |
| 43 bis | S9 → CGI 6 | G | corrigé |
| 281 H | S9 → CGI 793 | déjà réglé | — |
| 281 F | S9 → CGI 793 | déjà réglé | — |
| 46 quindecies QA | S9 → CGI 238 bis | déjà réglé | — |
| 46 AW ter | S9 → CGI 200 | déjà réglé | — |
| 46 AW bis | S9 → CGI 200 | déjà réglé | — |
| 2 sexdecies-0 A ter | S9 → CGI 31 | faux positif | — |
| 322 K | S9 → CGI 1477 | faux positif | — |
| 322 N | S9 → CGI 1477 | déjà réglé | — |
| 40 A | S9 → CGI 96 | faux positif | — |
| 38 | S9 → CGI 53 A | déjà réglé | — |
| 369 | S9 → CGI 231 | déjà réglé | — |
| 369 | S10 → CGI 231 | faux positif | — |
| 284 | S9 → CGI 867 | faux positif | — |
| 49 septies I quinquies | S9 → CGI 244 quater B | déjà réglé | — |
| 111-0 D | S9 → CGI 302 G | faux positif | — |
| 46 AW quater | S9 → CGI 200 | déjà réglé | — |

Le détail des citations (avec identifiant LEGIARTI) figure dans `audit/sweeps/Y16.json`.

## Points laissés à l'auteur

- Les séries émises à l'étranger avant 1976 encore en circulation ne sont pas dénombrées. L'effet pratique des corrections de 41 terdecies et 41 quindecies est donc probablement faible, mais il supprime une contradiction réelle entre la loi et le décret.
- 43 bis : les formulaires de déclaration et les modalités de réclamation du LPF, hors corpus, devront accueillir la réclamation commune prévue par 6 proposé.

## Résumé

56 pistes : 3 G (toutes corrigées), 27 déjà réglées, 26 faux positifs. 3 corrections, en mode `replace`, validées sans problème par l'outil. Revue IA, non validée par un juriste.
