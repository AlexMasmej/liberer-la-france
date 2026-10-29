# Y02 : troisième balayage (S9, S10), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py`, SQLite `mode=ro`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-Y02.json`, 45 articles et 63 pistes, toutes dans le Code de la sécurité sociale (51 S9, 12 S10). Chaque article du paquet et chaque cible a été lu en entier, avec sa source, sa proposition et son motif ; les notes ont été lues quand elles servaient à la qualification. Pour S9, les `removed_provisions` de la loi visée ont aussi été lues dans son lot. Exports : `evidence/cited/production-20261029/`.

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 0 |
| m | 2 (R762-36, R243-45-1 en S10) |
| déjà réglé | 33 |
| faux positif | 28 |

Corrections : aucune. `apply/Y02/changes.json` ne contient ni changement, ni demande, ni renonciation. `python3 -B apply/check_changes.py Y02` donne `problems` vide.

Constat général : chaque décret ou annexe qui organisait la formalité retirée d'une loi réduite (accord préalable statistique de L162-1-15, rapports de charte de L162-17-9, déclaration d'intention de L165-3-3, agrément de L161-38 et de L162-31, approbations de L652-1 et L243-6-5, seconde notification de L133-11, etc.) porte déjà sa coordination, avec sa transition. Les faux positifs S9 viennent de mots-clés homonymes : une autre déclaration ou un autre certificat, l'« inscription » à l'ordre du jour, l'autorisation sanitaire de L6122-1 CSP, la mise en demeure maintenue. Les faux positifs S10 sont des dérogations ou des exceptions dont la règle visée existe encore.

## Défauts mineurs (non corrigés : articles non modifiés par ailleurs)

- **R762-36** (LEGIARTI000038673139), S10 vers R762-8 : « Le délai d'attente prévu au 3° du I de l'article R. 762-8 ne s'applique pas à cette assurance. » Le 3° de R762-8 proposé n'a plus de délai (ouverture « A compter de la date d'effet de l'adhésion »). La phrase est donc redondante, sans effet : en AT-MP volontaire, aucun délai ne s'applique de toute façon. Elle pourrait viser simplement « Aucun délai d'attente ne s'applique ». La note « non les délais maladie-maternité de R762-8 » est devenue inexacte (F10).
- **R243-45-1** (LEGIARTI000038787043), S10 vers L243-6-5 : « l'entrée en vigueur prévue au IV de l'article L. 243-6-5 ». La transition de L243-6-5 figure dans son dernier alinéa, après le VI, et non au IV. La date est la même, et le IV de R243-45-1 en donne déjà la bonne ancre. Renvoi imprécis, sans effet.

## Une ligne par piste

| # | Article | LEGIARTI | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|---|---|
| 1 | L461-5 | LEGIARTI000036393199 | S10/F5 | L461-1 | faux positif | non |
| 2 | D138-1 | LEGIARTI000036851318 | S9/F1+F5 | L138-15 | faux positif | non |
| 3 | L756-4 | LEGIARTI000037063454 | S10/F5 | L635-1 | faux positif | non |
| 4 | R315-16 | LEGIARTI000037258467 | S9/F1+F5 | L315-2 | déjà réglé | non |
| 5 | R148-6 | LEGIARTI000037262076 | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| 6 | R148-5 | LEGIARTI000037262084 | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| 7 | R148-3 | LEGIARTI000037262087 | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| 8 | R148-1 | LEGIARTI000037262091 | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| 9 | R148-7 | LEGIARTI000037262097 | S9/F1+F5 | L162-1-15 | déjà réglé | non |
| 10 | R165-78 | LEGIARTI000037498416 | S9/F1+F5 | L162-17-9 | déjà réglé | non |
| 11 | R165-79 | LEGIARTI000037498506 | S9/F1+F5 | L162-17-9 | déjà réglé | non |
| 12 | R165-80 | LEGIARTI000037498533 | S9/F1+F5 | L162-17-9 | déjà réglé | non |
| 13 | R382-19 | LEGIARTI000037854495 | S10/F5 | L225-1 | faux positif | non |
| 14 | R165-81 | LEGIARTI000037858626 | S9/F1+F5 | L165-3-3 | faux positif | non |
| 15 | R165-81 | LEGIARTI000037858626 | S9/F1+F5 | L165-1 | faux positif | non |
| 16 | R133-44 | LEGIARTI000037877089 | S9/F1+F5 | L133-11 | déjà réglé | non |
| 17 | R441-3 | LEGIARTI000038423383 | S9/F1+F5 | L441-2 | déjà réglé | non |
| 18 | R441-3 | LEGIARTI000038423383 | S9/F1+F5 | L441-4 | faux positif | non |
| 19 | R441-1 | LEGIARTI000038423393 | S9/F1+F5 | L441-2 | déjà réglé | non |
| 20 | R441-1 | LEGIARTI000038423393 | S9/F1+F5 | L441-4 | faux positif | non |
| 21 | D461-9 | LEGIARTI000038423460 | S9/F1+F5 | L461-5 | faux positif | non |
| 22 | D767-1 | LEGIARTI000038651645 | S9/F1+F5 | L767-2 | déjà réglé | non |
| 23 | R162-50-6 | LEGIARTI000038654931 | S9/F1+F5 | L165-1 | faux positif | non |
| 24 | R762-36 | LEGIARTI000038673139 | S10/F5 | R762-8 | m | non |
| 25 | R862-13-1 | LEGIARTI000038701715 | S9/F1+F5 | L862-4 | déjà réglé | non |
| 26 | R162-33-3-1 | LEGIARTI000038738236 | S9/F1+F5 | L174-18 | faux positif | non |
| 27 | R162-33-3-1 | LEGIARTI000038738236 | S9/F1+F5 | L133-4 | faux positif | non |
| 28 | R243-45-1 | LEGIARTI000038787043 | S9/F1+F5 | L243-6-5 | déjà réglé | non |
| 29 | R243-45-1 | LEGIARTI000038787043 | S10/F5 | L243-6-5 | m | non |
| 30 | R652-13 | LEGIARTI000038788548 | S9/F1+F5 | L652-1 | déjà réglé | non |
| 31 | R182-2-3 | LEGIARTI000038789212 | S9/F1+F5 | L182-2-3 | faux positif | non |
| 32 | R217-10 | LEGIARTI000038789938 | S9/F1+F5 | L217-3-1 | déjà réglé | non |
| 33 | R162-50 | LEGIARTI000038790420 | S9/F1+F5 | L162-31 | déjà réglé | non |
| 34 | R162-48 | LEGIARTI000038790422 | S9/F1+F5 | L162-31 | déjà réglé | non |
| 35 | R133-9-1 | LEGIARTI000038790609 | S9/F1+F5 | L133-4 | déjà réglé | non |
| 36 | L241-6 | LEGIARTI000038834567 | S10/F5 | L821-1 | faux positif | non |
| 37 | L162-1-7-4 | LEGIARTI000038887549 | S10/F5 | L162-1-7 | faux positif | non |
| 38 | R161-76-2 | LEGIARTI000038956277 | S9/F1+F5 | L161-38 | déjà réglé | non |
| 39 | R161-76-4 | LEGIARTI000038956300 | S9/F1+F5 | L161-38 | déjà réglé | non |
| 40 | R161-76-5 | LEGIARTI000038956312 | S9/F1+F5 | L161-38 | déjà réglé | non |
| 41 | R161-76-6 | LEGIARTI000038956315 | S9/F1+F5 | L161-38 | faux positif | non |
| 42 | R161-76-8 | LEGIARTI000038956322 | S9/F1+F5 | L161-38 | déjà réglé | non |
| 43 | D243-15 | LEGIARTI000039222800 | S9/F1+F5 | L243-15 | faux positif | non |
| 44 | R862-11-3 | LEGIARTI000039222837 | S9/F1+F5 | L862-4 | faux positif | non |
| 45 | R862-11-3 | LEGIARTI000039222837 | S10/F5 | L862-4 | faux positif | non |
| 46 | R862-11-3 | LEGIARTI000039222837 | S10/F5 | R243-18 | faux positif | non |
| 47 | R862-11-2 | LEGIARTI000039222845 | S9/F1+F5 | L862-4 | faux positif | non |
| 48 | R862-11-1 | LEGIARTI000039222849 | S9/F1+F5 | L862-4 | déjà réglé | non |
| 49 | R138-22 | LEGIARTI000039222962 | S9/F1+F5 | L138-20 | déjà réglé | non |
| 50 | R138-22 | LEGIARTI000039222962 | S9/F1+F5 | L138-15 | déjà réglé | non |
| 51 | L821-5 | LEGIARTI000041398624 | S10/F5 | L581-3 | faux positif | non |
| 52 | R243-43-2 | LEGIARTI000041404430 | S9/F1+F5 | L243-6-3 | faux positif | non |
| 53 | R412-4 | LEGIARTI000041435656 | S9/F1+F5 | L441-2 | faux positif | non |
| 54 | R642-4 | LEGIARTI000041727798 | S9/F1+F5 | L642-4-2 | déjà réglé | non |
| 55 | D544-2 | LEGIARTI000041824226 | S9/F1+F5 | L544-3 | déjà réglé | non |
| 56 | D162-19 | LEGIARTI000041967886 | S9/F1+F5 | L162-31 | déjà réglé | non |
| 57 | D134-11 | LEGIARTI000041967963 | S10/F5 | D225-2 | faux positif | non |
| 58 | R165-82 | LEGIARTI000042270790 | S9/F1+F5 | L165-3-3 | déjà réglé | non |
| 59 | R165-82 | LEGIARTI000042270790 | S9/F1+F5 | L165-1 | faux positif | non |
| 60 | R165-82 | LEGIARTI000042270790 | S9/F1+F5 | L162-33 | faux positif | non |
| 61 | R165-7 | LEGIARTI000042270857 | S9/F1+F5 | L165-1 | faux positif | non |
| 62 | R165-7 | LEGIARTI000042270857 | S9/F1+F5 | L165-1-5 | déjà réglé | non |
| 63 | R612-17 | LEGIARTI000042363266 | S9/F1+F5 | L612-6 | déjà réglé | non |

Les citations exactes de chaque piste figurent dans `audit/sweeps/Y02.json`, au champ `evidence`.

## Points pour l'auteur

- Aucun arbitrage politique n'est ouvert par ce paquet.
- Les deux défauts `m` pourront être repris à l'occasion d'une prochaine modification de R762-36 et de R243-45-1.
- Vérification hors paquet : D162-18 (LEGIARTI000006735376) et R162-46 (LEGIARTI000006746796) sont déjà coordonnés avec la suppression de l'agrément de L162-31 (R162-46 est abrogé à cette date). Non examiné : les articles D441-1 et suivants, qui organisent la tenue du registre des accidents bénins. C'est là que pourrait subsister une condition d'accès au registre retirée de L441-4.
