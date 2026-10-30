# X7 : demandes laissées par M02 (apply/W08mb, `requests`) sur des articles sans propriétaire

Périmètre : 13 des 15 demandes de `apply/W08mb/changes.json`. D5134-1 et D5134-3 appartiennent à W08 et sont déjà traités dans `apply/W08z`.

Méthode :
- Texte lu en production, en lecture seule, le 29 octobre 2026 (`CITE_PRODUCTION=1 python3 -I tools/cite.py`, sqlite en `mode=ro`) : source, proposition, motif, notes et ligne de lot.
- Les 13 versions sont en vigueur au 18 octobre 2026 (`VIGUEUR`, du 2008-05-01 ou du 2009-06-01 jusqu'en 2999). Aucune n'est abrogée dans sa source et aucune n'a de version future. Il n'y a donc aucun `skipped`.
- Toutes ont un brouillon : 3 en `rewrite_draft` (D5134-10, R5133-2, R5133-4) et 10 en `retained_unchanged`. Le mode est donc `replace` partout.
- Contrôle : `python3 -B apply/check_changes.py X7` donne 13 lignes construites, 13 validées et `problems: []`.

## Vérifications de base légale

- **Emplois-jeunes.** L5134-1 à L5134-19 sont tous au corpus, à l'état ABROGE, avec une fin de vigueur au 2015-08-08. Aucun n'a de version en vigueur ni à venir. Les articles L5134-19-1 et suivants (CUI) sont distincts et non touchés.
- **Prime de retour à l'emploi.** L5133-1 n'a que deux versions, vérifiées dans les tables `articles` et `documents` :
  - LEGIARTI000006903513 : MODIFIE, du 2008-05-01 au 2009-06-01 ;
  - LEGIARTI000019869164 : ABROGE, du 2009-06-01 au 2011-01-01.

  Il n'a aucune version en vigueur ni à venir. L5133-2 à L5133-7 sont abrogés à la même date.
- **Renvois entrants** (sources et propositions en vigueur, neuf recueils) :
  - aucun renvoi par numéro à D5134-5, D5134-9 à D5134-13 ni à R5133-1 à R5133-8, en dehors de R5133-5 qui renvoie à R5133-1 ;
  - R5423-3 (5°) du code du travail et R844-5 (15°) du CSS visent la prime par L. 5133-1 pour l'exclure des ressources. Ces exclusions favorables ne sont pas touchées.

## Décisions (une ligne par article, toutes appliquées en `full_repeal`, `coordination_only`)

Objection SWEEP-M02-D5134-REGIME. Formule et transition reprises de D5134-1 et D5134-3 (`apply/W08z`). La phrase médiane est propre à chaque article et ferme seulement les conventions postérieures à l'abrogation législative.

| Article | Version | Avant | Décision |
|---|---|---|---|
| D5134-5 | LEGIARTI000018526699 | maintenu (contrôle préfectoral) | Abrogé. Les contrôles des conventions antérieures restent régis par les anciennes règles. |
| D5134-9 | LEGIARTI000018526687 | maintenu (15 924,55 € par an, versés par avance) | Abrogé. Les aides des conventions antérieures sont conservées. |
| D5134-10 | LEGIARTI000018526685 | réécrit (reprise après vacance étendue, clause sur le contrat unique) | Abrogé. L'extension proposée disparaît (`removed_provisions` et `reform_policy_id` remis à null). Les conventions antérieures gardent la règle de la source. |
| D5134-11 | LEGIARTI000018526683 | maintenu (avenants de 36 mois, prime de consolidation) | Abrogé. Les avenants et primes antérieurs sont conservés. |
| D5134-12 | LEGIARTI000018526681 | maintenu (reversement de l'aide différée) | Abrogé. Les créances des employeurs nées d'avenants antérieurs sont conservées. |
| D5134-13 | LEGIARTI000018526679 | maintenu (proratisation sous 35 h) | Abrogé. Le calcul est conservé pour les conventions antérieures. |

Objection SWEEP-M02-R5133-REGIME. Formule reprise mot pour mot de R5133-1 proposé (`apply/W08mb`) :
- abrogation à l'entrée en vigueur du décret ;
- maintien des primes dues au titre de reprises antérieures, ainsi que des indus, remises, créances, prescriptions et recours ;
- aucune prime, condition ni formalité de remplacement.

| Article | Version | Avant | Décision |
|---|---|---|---|
| R5133-2 | LEGIARTI000020529420 | réécrit (preuve libre pour les demandes « nouvelles et en cours ») | Abrogé. L'assouplissement proposé est sans objet (champs de réduction remis à null). |
| R5133-3 | LEGIARTI000020529418 | maintenu (1 000 €) | Abrogé. Le montant reste acquis aux primes antérieures. |
| R5133-4 | LEGIARTI000020529416 | réécrit (anticipation sans demande, contrat unique) | Abrogé. La réécriture est sans objet (champs de réduction remis à null). |
| R5133-5 | LEGIARTI000020529413 | maintenu (une prime par 18 mois, renvoi à R5133-1) | Abrogé en même temps que R5133-1, ce qui supprime le renvoi à un article abrogé. |
| R5133-6 | LEGIARTI000020529411 | maintenu (rattachement ASS, RMI, API) | Abrogé. Les liquidations antérieures gardent leurs règles. |
| R5133-7 | LEGIARTI000020529409 | maintenu (indus, échelonnement, remise pour précarité) | Abrogé pour l'avenir. L'échelonnement et la remise restent ouverts pour tout indu antérieur. |
| R5133-8 | LEGIARTI000020529407 | maintenu (information écrite avant récupération) | Abrogé pour l'avenir. La garantie reste applicable aux indus antérieurs. |

Dans les 13 notes de revue, les affirmations inexactes sont corrigées : « L5134-1 à L5134-11 sans résultat dans travail.json » et « L5133-1 absent du corpus ».

## Diagnostics (voulus)

- **Longueur :** le corps d'abrogation avec sa transition est plus long que les sources, qui sont courtes.
- **Renvois :** L5134-7, L5134-19 ou L5133-1 sont ajoutés. Ils sont nommés uniquement pour dater l'abrogation et délimiter la transition, comme dans W08z et W08mb. Le renvoi à R5133-1 est retiré de R5133-5.

## Points laissés à l'auteur et au coordinateur

1. **Dépendance.** Appliquer X7 avec `apply/W08mb` (R5133-1, D5134-2, D5134-6, D5134-7, D5134-8) et `apply/W08z` (D5134-1, D5134-3). Le règlement D5134-1 à D5134-13 et le règlement R5133-1 à R5133-8 sont alors abrogés d'ensemble.
2. **Deux formules dans la famille D5134.** W08z (D5134-1, D5134-3) et X7 suivent la formule « … portant la présente modification … Aucune pièce, déclaration ou condition de remplacement n'est exigée » avec la transition « conventions et contrats … jusqu'à leur terme ». W08mb (D5134-2, D5134-6 à D5134-8) emploie la formule « … portant la présente abrogation » avec la transition « conventions conclues et aides attribuées … versements, reversements … ». Les deux formules sont équivalentes au fond. Une harmonisation rédactionnelle est possible, mais elle est hors du périmètre de X7.
3. **Faveurs proposées retirées.** D5134-10, R5133-2 et R5133-4 portaient des faveurs créées par les propositions antérieures pour des situations futures : reprise élargie, preuve libre, anticipation sans demande. Elles deviennent sans objet faute de base légale. Les situations antérieures gardent les règles de la source. Aucun droit acquis n'est retiré.
4. **Faits non vérifiés.**
   - Le nombre de conventions emplois-jeunes ou de primes éventuellement encore en cours n'est pas établi.
   - Les textes abrogeants (2011 et 2015) n'ont pas été consultés au JORF. Les dates viennent du corpus LEGI.
5. **Blocs non recalculés.** Les blocs `reference_coherence` (D5134-13, R5133-4) et `benefit_review` (R5133-4) des lignes datent de l'état antérieur. `check_changes` ne les recalcule pas, et le validateur ne les a pas refusés.

Revue IA, sans validation par un juriste.
