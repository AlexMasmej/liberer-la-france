# P1-TRAVAIL-B — qualification des alertes « renvoi vers une abrogation proposée » (code du travail)

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z` (corpus au 18 octobre 2026). Revue faite le 26 octobre 2026. Cette revue est faite par une IA. Elle ne vaut pas validation par un juriste. La seconde passe continue en production : toutes les conclusions sont provisoires et doivent être confrontées aux propositions courantes avant correction.

## 1. Résultat en bref

- **139 alertes** dans 71 clusters. Chacune est qualifiée dans `reports/p1-work/P1-TRAVAIL-B-classification.jsonl`, avec `read_in_full=true`.
- Répartition : **84 alertes écartées**, **8 faux positifs**, **35 coordinations manquantes**, **11 incohérences du projet**, **1 risque juridique**. Aucune alerte n'a été classée `couvert par dossier` ou `non examiné`.
- **20 objections** dans `reports/dossiers/P1-TRAVAIL-B.json` : **6 en P1** (toutes confirmées) et **14 en P2** (12 confirmées, 2 à confirmer).
- Plusieurs objections reposent sur des **constats connexes**, découverts en lisant les cibles et leurs notes : RT-01, RT-03 (L7123-26, R7123-12), RT-19 (R3132-22) et RT-20. Ce sont souvent les plus graves. L'alerte mécanique qui y a conduit était, elle, souvent sans effet.

**Contrat unique : rien n'est cassé dans ce paquet.** Les textes lus appliquent tous la même règle : préavis de 15 jours, aucune indemnité ordinaire avant un an, puis 0,20 mois par année totale, plafond de 6 mois, due seulement si l'employeur rompt. Les textes concernés sont L7221-2, L1251-32, L1237-19-1 5° et L6222-18. Leurs réserves sont également respectées :
- le minimum de la rupture conventionnelle collective n'est pas soumis au seuil d'un an ;
- l'indemnité de fin de mission et l'indemnité de fin de contrat restent dues pour les anciens contrats ;
- le préavis ne vaut pas autorisation pour les salariés protégés.

**Protections autonomes : elles restent distinctes.** Les abrogations du CDD laissent intactes les protections de grossesse, de maternité et d'adoption (L1225-4 retenu, L1225-6 et L1225-38 bornés aux anciens CDD, plages L1225-70 à L1225-72). Il en va de même de l'inaptitude constatée (L1243-1 et L1243-4 pour les anciens contrats), de la prorogation radioprotectrice (L1243-12) et des autorisations pour salariés protégés (L1237-18-5, R342-30 CCH). Aucune objection ne porte donc sur ces protections. Le risque relevé sur le contrat unique est d'une autre nature : c'est la prime de fin de mission maintenue pour les seuls intérimaires étrangers détachés (RT-18, à confirmer).

## 2. Méthode

1. J'ai lu les deux briefs. J'ai extrait le paquet `reports/p1-work/P1-TRAVAIL-B.json` (71 cibles, 139 alertes, 107 textes qui renvoient distincts par code et identifiant de version, soit 177 versions).
2. Pour chaque cluster, j'ai lu en entier, par SQL en lecture seule sur `corpus.sqlite`, la source, la proposition, le motif et les notes de la cible. J'ai fait de même pour chaque texte qui renvoie : sa proposition s'il est `rewrite_draft`, sa source s'il est `retained_unchanged`, avec motif et notes dans les deux cas. J'ai vérifié, au cas par cas, que le numéro cité vise bien la cible (même code, même version en vigueur).
3. Lorsque les notes d'une cible désignaient des textes à coordonner, je les ai lus aussi : D1221-18, D1221-19, R1221-5, R1221-13, L7123-11, L7123-26, R7123-11, R7123-12, R*7123-9, L7124-4, L7124-5, L8291-1, R8291-2, R8292-1 à -3, R8293-1, R8294-1 à -5, R8295-1 à -3, R6231-4, R6231-5, L3132-20, L3132-23, R3132-17, R3132-22, L5221-8, L2312-26, L3133-7 à -12, L1237-19-9, L1237-19-10, D1233-37 à -40, L1251-32, L1225-4, L1225-38, et les deux versions de L5427-1.
4. Toutes les pièces citées ont été sauvegardées par `tools/cite.py -q` dans `evidence/cited/20261026T230545Z/` : 177 identifiants du paquet et 31 numéros connexes. Chaque passage cité dans le JSON a été vérifié automatiquement : il figure littéralement dans le champ indiqué, aux espaces près. Les empreintes du JSON ont été recalculées sur la base selon la convention de `tools/corpus.py`.
5. J'ai appliqué la grille de l'addendum, puis regroupé les alertes en une objection par effet juridique distinct. RT-19 regroupe des renvois résiduels sans effet normatif : ils ne doivent pas être comptés comme autant de contradictions.
6. Aucune écriture en production. Aucun script de production lancé. Ni `snapshot.py` ni `sealed_evidence.py`. Une seule consultation web : EUR-Lex, le 26 octobre 2026, qui a renvoyé une page vide. Les références européennes sont donc citées sans texte consulté et marquées « à vérifier ».

## 3. Périmètre réellement lu (cibles et textes qui renvoient, par cluster)

| # | Cible (abrogation proposée) | Textes qui renvoient, lus en entier | Alertes | Qualification |
|---|---|---|---|---|
| 0 | travail L1237-19-11 (LEGIARTI000035623992, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | travail D1233-44 (LEGIARTI000036248518, VIGUEUR, 2017-12-23→2999-01-01, rewrite_draft)<br>travail D1233-43 (LEGIARTI000036248524, VIGUEUR, 2017-12-23→2999-01-01, rewrite_draft)<br>travail D1233-48-1 (LEGIARTI000047777578, VIGUEUR, 2023-07-03→2999-01-01, rewrite_draft)<br>travail D1233-48-2 (LEGIARTI000047777580, VIGUEUR, 2023-07-03→2999-01-01, retained_unchanged)<br>travail D1233-41 (LEGIARTI000047779119, VIGUEUR, 2023-07-03→2999-01-01, rewrite_draft)<br>travail D1233-48-3 (LEGIARTI000048173286, VIGUEUR, 2023-10-08→2999-01-01, retained_unchanged) | 8 | coordination manquante → RT-07 ×8 |
| 1 | travail L2 (LEGIARTI000042654546, VIGUEUR, 2021-06-01→2999-01-01, rewrite_draft) | css Annexe (1) à l'art. A931-11-17 (LEGIARTI000006734907, VIGUEUR, 1998-07-24→2999-01-01, rewrite_draft)<br>css Annexe I à l'art. R434-32 (5) (LEGIARTI000028675245, VIGUEUR, 2006-02-06→2999-01-01, retained_unchanged) | 8 | faux positif ×8 |
| 2 | travail L1225-6 (LEGIARTI000053279277, VIGUEUR, 2025-12-31→2999-01-01, rewrite_draft) | travail L1225-70 (LEGIARTI000006900958, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged)<br>travail L1225-72 (LEGIARTI000006900964, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged)<br>travail R1227-5 (LEGIARTI000018537740, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail L1142-3 (LEGIARTI000026799923, VIGUEUR, 2012-12-19→2999-01-01, rewrite_draft)<br>travail L1225-71 (LEGIARTI000035643521, VIGUEUR, 2017-09-24→2999-01-01, retained_unchanged) | 6 | alerte écartée ×6 |
| 3 | travail L1251-36 (LEGIARTI000035644052, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail L1251-37-1 (LEGIARTI000035638998, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft)<br>travail L1251-37 (LEGIARTI000035644047, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft)<br>travail L1255-9 (LEGIARTI000035644059, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft)<br>travail L1251-58-4 (LEGIARTI000037379976, VIGUEUR, 2018-09-07→2999-01-01, rewrite_draft) | 5 | alerte écartée ×5 |
| 4 | travail L1221-11 (LEGIARTI000006900850, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L1221-12 (LEGIARTI000006900851, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail R1524-4 (LEGIARTI000037560601, VIGUEUR, 2018-11-07→2999-01-01, rewrite_draft)<br>travail R7122-16 (LEGIARTI000049816490, VIGUEUR, 2024-07-01→2999-01-01, retained_unchanged)<br>css L133-5-1 (LEGIARTI000043747397, VIGUEUR, 2021-07-03→2999-01-01, rewrite_draft) | 4 | alerte écartée ×3; coordination manquante → RT-19 ×1 |
| 5 | travail L5422-11 (LEGIARTI000006903833, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R5142-5 (LEGIARTI000018526191, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged)<br>travail L5422-3 (LEGIARTI000037388297, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft)<br>travail L5427-1 (LEGIARTI000048600544, ABROGE_DIFF, 2024-01-01→2028-01-01, rewrite_draft)<br>css L213-1 (LEGIARTI000048701101, VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft) | 4 | alerte écartée ×2; coordination manquante → RT-19 ×2 |
| 6 | travail L1251-35 (LEGIARTI000035644037, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail L1255-8 (LEGIARTI000035644066, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft)<br>travail L1251-40 (LEGIARTI000036262126, VIGUEUR, 2017-12-22→2999-01-01, rewrite_draft)<br>travail L1251-58-4 (LEGIARTI000037379976, VIGUEUR, 2018-09-07→2999-01-01, rewrite_draft)<br>travail L1251-58-5 (LEGIARTI000037379978, VIGUEUR, 2018-09-07→2999-01-01, rewrite_draft) | 4 | alerte écartée ×4 |
| 7 | travail L1251-33 (LEGIARTI000019869550, VIGUEUR, 2010-01-01→2999-01-01, rewrite_draft) | travail L1251-58-4 (LEGIARTI000037379976, VIGUEUR, 2018-09-07→2999-01-01, rewrite_draft)<br>travail L1262-2 (LEGIARTI000038156567, VIGUEUR, 2020-07-30→2999-01-01, rewrite_draft) | 4 | alerte écartée ×3; risque juridique → RT-18 ×1 |
| 8 | travail L6231-3 (LEGIARTI000037386084, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | travail R6231-3 (LEGIARTI000039351864, VIGUEUR, 2019-11-09→2999-01-01, retained_unchanged)<br>travail R6232-1 (LEGIARTI000039355507, VIGUEUR, 2019-11-09→2999-01-01, retained_unchanged)<br>travail R6233-1 (LEGIARTI000039355540, VIGUEUR, 2019-12-31→2999-01-01, rewrite_draft)<br>travail L6356-1 (LEGIARTI000054319153, VIGUEUR, 2026-06-27→2999-01-01, rewrite_draft) | 4 | coordination manquante → RT-08 ×1; alerte écartée ×3 |
| 9 | travail L1237-19-14 (LEGIARTI000036703230, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | travail D1233-48-1 (LEGIARTI000047777578, VIGUEUR, 2023-07-03→2999-01-01, rewrite_draft)<br>travail D1233-38 (LEGIARTI000047779099, VIGUEUR, 2023-07-03→2999-01-01, rewrite_draft)<br>travail D1233-48-3 (LEGIARTI000048173286, VIGUEUR, 2023-10-08→2999-01-01, retained_unchanged)<br>travail L5422-1 (LEGIARTI000048590547, VIGUEUR, 2025-01-01→2999-01-01, rewrite_draft) | 4 | coordination manquante → RT-07 ×3; alerte écartée ×1 |
| 10 | travail L3334-3 (LEGIARTI000019870599, VIGUEUR, 2008-12-05→2999-01-01, rewrite_draft) | a3 39 (LEGIARTI000053218832, VIGUEUR, 2025-12-29→2999-01-01, rewrite_draft)<br>css L911-6 (LEGIARTI000006745971, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged)<br>css L242-4-3 (LEGIARTI000038836895, VIGUEUR, 2019-10-01→2999-01-01, retained_unchanged) | 3 | alerte écartée ×3 |
| 11 | travail L1243-8 (LEGIARTI000006901219, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L1242-11 (LEGIARTI000006901205, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail L1243-4 (LEGIARTI000024026880, VIGUEUR, 2011-05-19→2999-01-01, rewrite_draft)<br>travail L6222-18 (LEGIARTI000037386025, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | 3 | alerte écartée ×3 |
| 12 | travail L3132-21 (LEGIARTI000031013455, VIGUEUR, 2015-08-08→2999-01-01, rewrite_draft) | travail R3135-2 (LEGIARTI000018534331, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail R3132-16 (LEGIARTI000031213116, VIGUEUR, 2015-09-25→2999-01-01, retained_unchanged) | 3 | alerte écartée ×1; coordination manquante → RT-04 ×2 |
| 13 | travail L2312-51 (LEGIARTI000039261890, VIGUEUR, 2019-10-23→2999-01-01, rewrite_draft) | travail L2315-93 (LEGIARTI000035628367, VIGUEUR, 2018-01-01→2999-01-01, retained_unchanged)<br>travail L2315-92 (LEGIARTI000036262604, VIGUEUR, 2018-01-01→2999-01-01, retained_unchanged)<br>cch R342-30 (LEGIARTI000046112679, VIGUEUR, 2023-01-01→2999-01-01, retained_unchanged) | 3 | alerte écartée ×3 |
| 14 | travail L1237-18-5 (LEGIARTI000036702967, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | travail D1237-4 (LEGIARTI000036247026, VIGUEUR, 2017-12-23→2999-01-01, retained_unchanged)<br>travail D1237-5 (LEGIARTI000036247054, VIGUEUR, 2017-12-23→2999-01-01, rewrite_draft)<br>travail L1237-19-1 (LEGIARTI000052437244, VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft) | 3 | incohérence du projet → RT-05 ×2; alerte écartée ×1 |
| 15 | travail L6231-6 (LEGIARTI000038951785, VIGUEUR, 2019-08-23→2999-01-01, rewrite_draft) | travail R6232-1 (LEGIARTI000039355507, VIGUEUR, 2019-11-09→2999-01-01, retained_unchanged)<br>travail R6233-1 (LEGIARTI000039355540, VIGUEUR, 2019-12-31→2999-01-01, rewrite_draft)<br>travail L6356-1 (LEGIARTI000054319153, VIGUEUR, 2026-06-27→2999-01-01, rewrite_draft) | 3 | alerte écartée ×3 |
| 16 | travail L5424-23 (LEGIARTI000048600579, VIGUEUR, 2024-01-01→2999-01-01, rewrite_draft) | travail D5424-68 (LEGIARTI000049816580, VIGUEUR, 2024-07-01→2999-01-01, retained_unchanged) | 3 | coordination manquante → RT-09 ×3 |
| 17 | travail L6351-6 (LEGIARTI000021343608, VIGUEUR, 2009-11-26→2999-01-01, rewrite_draft) | a2 202 C (LEGIARTI000036437229, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft)<br>travail L2315-17 (LEGIARTI000054140233, VIGUEUR, 2026-05-28→2999-01-01, retained_unchanged) | 2 | alerte écartée ×2 |
| 18 | travail L3134-11 (LEGIARTI000006902633, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L3134-14 (LEGIARTI000006902636, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail L3134-15 (LEGIARTI000006902637, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged) | 2 | coordination manquante → RT-19 ×1; alerte écartée ×1 |
| 19 | travail L7123-14 (LEGIARTI000023755150, VIGUEUR, 2011-03-24→2999-01-01, rewrite_draft) | travail R7124-33 (LEGIARTI000018521452, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged)<br>travail R7123-14 (LEGIARTI000024504198, VIGUEUR, 2011-08-27→2999-01-01, retained_unchanged) | 2 | alerte écartée ×1; incohérence du projet → RT-03 ×1 |
| 20 | travail L4532-12 (LEGIARTI000006903274, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R4741-5 (LEGIARTI000018527380, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft)<br>travail R4741-4 (LEGIARTI000036483813, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | 2 | alerte écartée ×2 |
| 21 | travail R1221-8 (LEGIARTI000024214311, VIGUEUR, 2011-08-01→2999-01-01, rewrite_draft) | travail R1221-12 (LEGIARTI000024214305, VIGUEUR, 2011-08-01→2999-01-01, rewrite_draft)<br>travail R7122-20 (LEGIARTI000044212130, VIGUEUR, 2021-10-16→2999-01-01, rewrite_draft) | 2 | alerte écartée ×2 |
| 22 | travail L3133-11 (LEGIARTI000033020848, VIGUEUR, 2016-08-10→2999-01-01, rewrite_draft) | travail L3134-16 (LEGIARTI000033008282, VIGUEUR, 2016-08-10→2999-01-01, retained_unchanged)<br>travail L3422-1 (LEGIARTI000033021064, VIGUEUR, 2016-08-10→2999-01-01, retained_unchanged) | 2 | coordination manquante → RT-13 ×2 |
| 23 | travail L3123-15 (LEGIARTI000035653060, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | travail R3123-1 (LEGIARTI000033453089, VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft) | 2 | incohérence du projet → RT-10 ×2 |
| 24 | travail L1243-13 (LEGIARTI000035643980, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail L1233-72-1 (LEGIARTI000036261982, VIGUEUR, 2017-12-22→2999-01-01, rewrite_draft)<br>travail L1233-68 (LEGIARTI000037388640, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | 2 | alerte écartée ×2 |
| 25 | travail R6332-33 (LEGIARTI000037934331, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | travail D6331-70 (LEGIARTI000038023454, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft)<br>travail D6235-10 (LEGIARTI000051395713, VIGUEUR, 2025-03-31→2999-01-01, retained_unchanged) | 2 | coordination manquante → RT-11 ×2 |
| 26 | travail L4622-9-3 (LEGIARTI000043890111, VIGUEUR, 2022-03-31→2999-01-01, rewrite_draft) | travail L4624-8-2 (LEGIARTI000043890473, VIGUEUR, 2024-01-01→2999-01-01, retained_unchanged)<br>travail L4641-2-1 (LEGIARTI000043891901, VIGUEUR, 2022-03-31→2999-01-01, retained_unchanged) | 2 | coordination manquante → RT-12 ×2 |
| 27 | travail L3142-9 (LEGIARTI000033022000, VIGUEUR, 2016-08-10→2999-01-01, rewrite_draft) | travail L7221-2 (LEGIARTI000047293314, VIGUEUR, 2023-03-11→2999-01-01, rewrite_draft)<br>css L168-1 (LEGIARTI000054137747, VIGUEUR, 2026-05-28→2999-01-01, rewrite_draft) | 2 | alerte écartée ×2 |
| 28 | travail L8256-8 (LEGIARTI000024197823, VIGUEUR, 2011-09-30→2999-01-01, rewrite_draft) | travail L8253-1 (LEGIARTI000049049509, VIGUEUR, 2024-01-28→2999-01-01, retained_unchanged)<br>travail L8323-3 (LEGIARTI000049050064, VIGUEUR, 2024-01-28→2999-01-01, retained_unchanged) | 2 | alerte écartée ×2 |
| 29 | travail R8293-2 (LEGIARTI000049153202, VIGUEUR, 2024-04-01→2999-01-01, rewrite_draft) | travail R8295-2 (LEGIARTI000049153210, VIGUEUR, 2024-04-01→2999-01-01, rewrite_draft)<br>travail R8295-3-1 (LEGIARTI000049153249, VIGUEUR, 2024-04-01→2999-01-01, retained_unchanged) | 2 | incohérence du projet → RT-02 ×2 |
| 30 | travail L1221-12-1 (LEGIARTI000028393578, VIGUEUR, 2013-12-25→2999-01-01, rewrite_draft) | travail L1221-12 (LEGIARTI000006900851, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 31 | travail L1243-1 (LEGIARTI000029946319, VIGUEUR, 2014-12-22→2999-01-01, rewrite_draft) | travail L1242-11 (LEGIARTI000006901205, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 32 | travail L1243-3 (LEGIARTI000006901214, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L1242-11 (LEGIARTI000006901205, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 33 | travail L1242-5 (LEGIARTI000035653074, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | travail L1248-3 (LEGIARTI000006901239, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 34 | travail L7313-14 (LEGIARTI000006904736, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L7313-17 (LEGIARTI000006904739, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 35 | travail R6341-19 (LEGIARTI000038031774, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | travail R6341-20 (LEGIARTI000018522493, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 36 | travail R5522-79 (LEGIARTI000031689007, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft) | travail R5522-71 (LEGIARTI000018524426, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 37 | travail D5427-9 (LEGIARTI000018524676, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail D5427-13 (LEGIARTI000018524668, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | coordination manquante → RT-19 ×1 |
| 38 | travail L5221-9 (LEGIARTI000042920238, VIGUEUR, 2021-05-01→2999-01-01, rewrite_draft) | travail R5224-1 (LEGIARTI000018525570, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged) | 1 | coordination manquante → RT-14 ×1 |
| 39 | travail R4227-40 (LEGIARTI000018532053, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R4216-30 (LEGIARTI000018532370, ABROGE_DIFF, 2008-05-01→2027-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 40 | travail R3262-9 (LEGIARTI000018533512, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R3262-46 (LEGIARTI000018533419, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 41 | travail L3132-29 (LEGIARTI000031013521, VIGUEUR, 2015-08-08→2999-01-01, rewrite_draft) | travail R3135-2 (LEGIARTI000018534331, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 42 | travail L2523-8 (LEGIARTI000006902410, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R2523-12 (LEGIARTI000018534812, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged) | 1 | coordination manquante → RT-15 ×1 |
| 43 | travail D1253-7 (LEGIARTI000018537284, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R1253-43 (LEGIARTI000018537186, VIGUEUR, 2008-05-01→2999-01-01, retained_unchanged) | 1 | coordination manquante → RT-19 ×1 |
| 44 | travail R7123-10-1 (LEGIARTI000043532234, VIGUEUR, 2021-11-01→2999-01-01, rewrite_draft) | travail R7123-11 (LEGIARTI000024504230, VIGUEUR, 2011-08-27→2999-01-01, rewrite_draft) | 1 | incohérence du projet → RT-03 ×1 |
| 45 | travail D4622-36 (LEGIARTI000025279995, VIGUEUR, 2012-07-01→2999-01-01, rewrite_draft) | travail D4622-37 (LEGIARTI000029236950, VIGUEUR, 2014-07-14→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 46 | travail L5134-23-2 (LEGIARTI000026549793, VIGUEUR, 2012-11-01→2999-01-01, rewrite_draft) | travail L5134-25-1 (LEGIARTI000031087287, VIGUEUR, 2015-08-19→2999-01-01, rewrite_draft) | 1 | incohérence du projet → RT-17 ×1 |
| 47 | travail L3133-9 (LEGIARTI000033020858, VIGUEUR, 2016-08-10→2999-01-01, rewrite_draft) | travail L3422-1 (LEGIARTI000033021064, VIGUEUR, 2016-08-10→2999-01-01, retained_unchanged) | 1 | coordination manquante → RT-13 ×1 |
| 48 | travail L1255-8 (LEGIARTI000035644066, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail L5132-14 (LEGIARTI000033024468, VIGUEUR, 2016-08-10→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 49 | travail L1152-5 (LEGIARTI000006900822, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail L8113-5 (LEGIARTI000033025205, VIGUEUR, 2016-08-10→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 50 | travail R3142-29 (LEGIARTI000033509590, VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft) | travail R3142-25 (LEGIARTI000033509603, VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 51 | travail R4624-50 (LEGIARTI000029235122, VIGUEUR, 2017-01-01→2999-01-01, rewrite_draft) | travail R1262-14 (LEGIARTI000033769259, VIGUEUR, 2017-01-01→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 52 | travail L1242-8-1 (LEGIARTI000035643961, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail L1243-12 (LEGIARTI000035644025, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 53 | travail L2261-27-1 (LEGIARTI000035609246, VIGUEUR, 2017-09-24→2999-01-01, rewrite_draft) | travail D2261-4-5 (LEGIARTI000036206358, VIGUEUR, 2017-12-16→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 54 | travail R7232-22 (LEGIARTI000033747535, VIGUEUR, 2016-12-30→2999-01-01, rewrite_draft) | travail R7524-2 (LEGIARTI000037563343, VIGUEUR, 2018-11-07→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 55 | travail L1153-5-1 (LEGIARTI000037380160, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | travail D1151-1 (LEGIARTI000038025995, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | 1 | incohérence du projet → RT-16 ×1 |
| 56 | travail L6331-39 (LEGIARTI000042914274, VIGUEUR, 2022-01-01→2999-01-01, rewrite_draft) | travail R6523-1 (LEGIARTI000041611735, VIGUEUR, 2020-02-21→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 57 | travail L6331-42 (LEGIARTI000025009571, VIGUEUR, 2011-12-23→2999-01-01, rewrite_draft) | travail R6523-1 (LEGIARTI000041611735, VIGUEUR, 2020-02-21→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 58 | travail R5221-27 (LEGIARTI000043320735, VIGUEUR, 2021-04-01→2999-01-01, rewrite_draft) | travail R5221-45 (LEGIARTI000043320779, VIGUEUR, 2021-04-01→2999-01-01, retained_unchanged) | 1 | coordination manquante → RT-14 ×1 |
| 59 | travail R6331-39 (LEGIARTI000018522878, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | travail R6331-40 (LEGIARTI000044969974, VIGUEUR, 2022-01-01→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 60 | travail D4622-56 (LEGIARTI000046565199, VIGUEUR, 2022-11-17→2999-01-01, rewrite_draft) | travail D4622-27-6 (LEGIARTI000046862246, VIGUEUR, 2025-01-01→2999-01-01, rewrite_draft) | 1 | incohérence du projet → RT-06 ×1 |
| 61 | travail R5213-72 (LEGIARTI000038032411, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft) | travail R5213-86-4 (LEGIARTI000049123990, VIGUEUR, 2024-02-12→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 62 | travail D3325-1 (LEGIARTI000029026634, VIGUEUR, 2014-05-30→2999-01-01, rewrite_draft) | travail R3324-16 (LEGIARTI000049905634, VIGUEUR, 2024-07-07→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 63 | travail D6211-3 (LEGIARTI000049754363, VIGUEUR, 2024-07-01→2999-01-01, rewrite_draft) | travail R5523-15-43 (LEGIARTI000050742418, VIGUEUR, 2024-12-06→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 64 | travail R6332-25-2 (LEGIARTI000051818948, VIGUEUR, 2025-06-30→2999-01-01, rewrite_draft) | travail R6332-25 (LEGIARTI000051821081, VIGUEUR, 2025-06-30→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 65 | travail R7232-9 (LEGIARTI000033747451, VIGUEUR, 2016-12-30→2999-01-01, rewrite_draft) | css D133-21 (LEGIARTI000050740376, VIGUEUR, 2024-12-06→2999-01-01, rewrite_draft) | 1 | coordination manquante → RT-19 ×1 |
| 66 | travail D3171-4 (LEGIARTI000043128637, VIGUEUR, 2021-02-13→2999-01-01, rewrite_draft) | css D241-25 (LEGIARTI000051434553, VIGUEUR, 2025-04-07→2999-01-01, rewrite_draft) | 1 | alerte écartée ×1 |
| 67 | travail L1221-16 (LEGIARTI000006900855, VIGUEUR, 2008-05-01→2999-01-01, rewrite_draft) | css R133-14 (LEGIARTI000054167679, VIGUEUR, 2026-07-01→2999-01-01, rewrite_draft) | 1 | coordination manquante → RT-19 ×1 |
| 68 | travail L2312-28 (LEGIARTI000035609818, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | cch R342-30 (LEGIARTI000046112679, VIGUEUR, 2023-01-01→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 69 | travail L2312-30 (LEGIARTI000035609822, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | cch R342-30 (LEGIARTI000046112679, VIGUEUR, 2023-01-01→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |
| 70 | travail L2312-68 (LEGIARTI000035611009, VIGUEUR, 2018-01-01→2999-01-01, rewrite_draft) | cch R342-30 (LEGIARTI000046112679, VIGUEUR, 2023-01-01→2999-01-01, retained_unchanged) | 1 | alerte écartée ×1 |

Lus en plus, hors paquet, pour qualifier : voir la méthode, point 3. Les fichiers de preuve correspondants sont listés dans `evidence_files` de chaque objection.

## 4. Constats

### P1 — effets probables, à corriger avant toute intégration

**RT-01 — DPAE électronique : la pénalité et l'obligation supprimées par la loi restent dans les décrets.** *Incohérence du projet, confirmée.*
- L1221-12-1 proposé supprime l'obligation de DPAE électronique au-delà d'un seuil et sa pénalité. Il décharge et restitue les pénalités non définitives.
- D1221-18 (plus de 50 DPAE) et D1221-19 (0,5 % du PMSS par salarié) sont retenus inchangés, avec des motifs qui affirment leur maintien.
- R1221-5 proposé écrit : « L'obligation de déclaration électronique prévue à l'article D. 1221-18 reste applicable ». R1221-13 proposé réserve la pénalité D1221-19.
- Les notes de L1221-12 et L1221-12-1 relèvent déjà la contradiction. Elle reste non résolue dans l'instantané.
- Conséquence : une pénalité sans base légale, contraire à la restitution prévue par la loi.

**RT-02 — Carte BTP : la carte est supprimée, mais pas ses obligations réglementaires.** *Incohérence du projet, confirmée.* Ces règlements restent en place :
- R8294-5 : présentation de la carte aux agents ;
- R8295-3 : mise à jour sous 24 heures ;
- R8295-3-1 : modification de la déclaration avant chaque mission ou détachement pour « activer » la carte ;
- R8295-1 : traitement SI-CIP « ayant pour finalité la délivrance de la carte », avec un motif qui dit que L8291-1 « conserve » la carte ;
- R8295-2 réécrit : catalogue de données maintenu.

Conséquences : une formalité maintenue et une collecte de données sans finalité restante, contraire aux principes du RGPD.

**RT-03 — Agences de mannequins : la licence est supprimée, mais pas son régime pénal et réglementaire.** *Incohérence du projet, confirmée.*
- L7123-26, retenu, punit toujours de six mois d'emprisonnement et de 75 000 € l'exercice « sans licence » ou « sans déclaration ». Son motif suppose la licence en vigueur.
- R7123-14, retenu, organise le refus et le retrait de la licence.
- R7123-11, réécrit, impose des notifications au « bénéficiaire de la licence ». Il renvoie à R*7123-9 et R7123-10-1, tous deux abrogés.
- R7123-12, réécrit, **maintient la déclaration préalable pour les seules agences d'autres États membres**. L7123-11 proposé la supprime pourtant. C'est une discrimination à rebours contre les prestataires européens (art. 56 TFUE).

**RT-04 — Dérogations dominicales : le circuit préfectoral reste dans les décrets.** *Coordination manquante, confirmée.* L3132-20, L3132-21 et L3132-23 proposés suppriment autorisation, avis et arrêtés. Pourtant R3132-16 (avis sous un mois, arrêté sous huit jours) et R3132-17 (autorisations d'extension) sont retenus. Le motif de R3132-16 défend même ce circuit.

**RT-05 — Congé de mobilité : le décret réécrit garde le rapport semestriel que la loi interdit.** *Incohérence du projet, confirmée.* D1237-5 réécrit commence par « Pour l'application de l'article L. 1237-18-5, l'employeur informe l'autorité administrative tous les six mois ». Or L1237-18-5 proposé interdit d'exiger toute information propre à ces ruptures. D1237-4 est retenu.

**RT-06 — SPSTI : une faveur de cotisation reste conditionnée à un document supprimé.** *Incohérence du projet, confirmée.* Pour déroger aux bornes de 80 % et 120 %, D4622-27-6 V exige toujours de présenter « le rapport comptable d'entreprise mentionné à l'article D. 4622-56 ». Or D4622-56 est abrogé. Soit la formalité revient par cette condition, soit la faveur devient inaccessible.

### P2 — alertes, coordinations à effet limité

- **RT-07** Revitalisation de la RCC. Les décrets D1233-38 à -48-3 ne sont pas bornés aux anciens accords. De plus, « deuxième alinéa de L1237-19-11 » vise désormais le paragraphe transitoire. Même mécanisme que les clusters L1237-19-9 et -10 du paquet P1-TRAVAIL-A : à dédupliquer.
- **RT-08** Conseil de perfectionnement des CFA. R6231-3 à R6231-5 restent rédigés comme obligatoires. La note de R6231-4 dit : « Le conseil prévu par L. 6231-3 subsiste ».
- **RT-09** Comité d'expertise des intermittents. D5424-68 est retenu, alors que le comité est supprimé.
- **RT-10** R3123-1 réécrit rattache le bilan du temps partiel et l'accès des délégués syndicaux à L3123-15, qui est abrogé. Il faut le rattacher à L2312-26.
- **RT-11** R6332-33 est abrogé, mais la transmission reste prévue pour les apprentis transfrontaliers (D6235-10) et D6331-70 dit ses obligations « applicables ».
- **RT-12** Certification des SPSTI supprimée, mais encore visée par L4624-8-2 (2e alinéa) et L4641-2-1 4°.
- **RT-13** Journée de solidarité supprimée. L3134-16 et L3422-1 sont retenus avec des motifs qui la disent subsistante. Même mécanisme que le cluster L3133-12 du paquet P1-TRAVAIL-A.
- **RT-14** Déclaration nominative des étudiants étrangers supprimée. La contravention R5224-1 la vise encore ; R5221-45 est obsolète. La faveur reste portée par L5221-8.
- **RT-15** R2523-12, dernier alinéa : le rapport de non-comparution est maintenu. Il est neutralisé par L2523-8.
- **RT-16** D1151-1 4° réécrit : il faut toujours afficher les coordonnées d'un référent harcèlement qui n'est plus obligatoire.
- **RT-17** L5134-25-1 dit que les conditions de L5134-23-2 (abrogé) « demeurent applicables ». Cela peut faire revivre l'évaluation préalable.
- **RT-18** *Risque juridique, à confirmer.* L1262-2 et L1251-32 gardent l'indemnité de fin de mission de 10 % pour les CDD étrangers de travail temporaire, y compris futurs. Aucun intérimaire employé en France n'y aura plus droit. Cela peut excéder ce que permet la directive 96/71/CE modifiée et constituer une restriction au sens de l'art. 56 TFUE. Il faut conserver la faveur en admettant une garantie équivalente.
- **RT-19** Renvois résiduels sans effet normatif, en un seul lot de nettoyage : R7122-16, R133-14 CSS, L3134-14, D5427-13, R1253-43, D133-21 CSS, L5427-1, L213-1 6° CSS, et R3132-22 (constat connexe).
- **RT-20** *Anomalie d'inventaire, à confirmer.* La version de L5427-1 qui entre en vigueur le 1er janvier 2028 (LEGIARTI000054468622, VIGUEUR_DIFF) n'a ni proposition ni ligne d'inventaire. La coordination du e) avec le contrat unique se perdrait donc à cette date. Les 89 versions VIGUEUR_DIFF du code du travail sont toutes sans brouillon : c'est peut-être un choix de périmètre non documenté.

### Alertes écartées et faux positifs (92)

- **Faux positifs (8, cluster L2).** « L. 2 » désigne une ligne comptable d'une annexe CSS ou un niveau vertébral L2 (annexe I à R434-32 CSS). L'annexe I à R434-32 relève d'un dossier documentaire ouvert (figure (7)) qui n'est pas affecté. Je l'ai classée faux positif plutôt que `couvert par dossier`, car l'alerte est sans rapport avec ce dossier.
- **Plages d'articles sans effet** : par exemple « L. 1225-1 à L. 1225-28 », « L. 6231-2 à L. 6231-7 », les exclusions de R342-30 CCH ou « L. 3334-1 à L. 3334-16 ».
- **Renvois expressément neutralisés ou bornés aux anciens contrats** : L1221-12, R1524-4, L5422-3, R3135-2, R4741-4/5, R6341-20, R3142-25, R6332-25, R6331-40.
- **Textes qui renvoient eux-mêmes abrogés avec la même transition** : L1251-37, L1251-37-1, L1255-8, L1255-9, L1242-11, L1243-4, L1248-3.
- **Régimes transitoires assumés** : L7313-17, L1243-12, D2261-4-5, L6222-18, L1233-68, L1233-72-1.
- **Adaptations outre-mer de mots d'articles abrogés, sans objet** : R7524-2, R5523-15-43.

## 5. Propositions de correction (présentées séparément, non appliquées)

Ce sont des projets de texte. Ils ne modifient ni l'instantané ni la production. Dépendance commune : ils doivent entrer en vigueur à la même date que les abrogations législatives correspondantes.

### 5.1 RT-01 — D1221-18, D1221-19, R1221-5, R1221-13

**D1221-18 (proposé)**
> Le présent article est abrogé à compter de l'entrée en vigueur de l'abrogation de l'article L. 1221-12-1. À compter de cette date, aucun employeur n'est tenu d'adresser la déclaration préalable à l'embauche par voie électronique en raison du nombre de déclarations accomplies au cours de l'année civile précédente. Les déclarations régulièrement effectuées par voie électronique conservent leurs effets.

**D1221-19 (proposé)**
> Le présent article est abrogé à compter de la même date. Aucune pénalité ne peut être appliquée sur son fondement aux manquements commis à compter de cette date ni aux manquements antérieurs pour lesquels elle n'est pas devenue définitive ; ces pénalités sont déchargées et les sommes versées à ce titre restituées dans les conditions de l'article L. 1221-12-1. Les pénalités devenues définitives avant cette date restent recouvrables selon les dispositions antérieures et les recours qui leur sont applicables.

**R1221-5, premier alinéa (proposé)**
> La déclaration préalable à l'embauche est effectuée, au choix de l'employeur, par voie électronique ou au moyen du formulaire mentionné à l'alinéa suivant.

Au deuxième alinéa, remplacer « Lorsqu'une autre voie est légalement ouverte, » par « Lorsque l'employeur ne recourt pas à la voie électronique, ».

**R1221-13** : remplacer la phrase « Les autres sanctions, notamment celles ayant un fondement distinct et la pénalité de déclaration dématérialisée de l'article D. 1221-19, ne sont pas supprimées par ce seul renvoi. » par :
> Les sanctions ayant un fondement distinct ne sont pas supprimées par ce seul renvoi. La pénalité de déclaration dématérialisée antérieurement prévue à l'article D. 1221-19 suit le régime transitoire de l'article L. 1221-12-1.

Justification : alignement sur la décharge et la restitution législatives ; aucune formalité de remplacement. Ce qui est préservé : la DPAE, R1227-1, le recouvrement du stock définitif.

### 5.2 RT-02 — Carte BTP

R8294-5, R8295-3 et R8295-3-1 : abrogation selon la formule
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune présentation, information, mise à jour ou modification de déclaration n'est exigée sur son fondement à compter de cette date, y compris pour une mission ou un détachement en cours. Les faits antérieurs restent soumis aux règles d'application dans le temps des dispositions répressives plus douces.

**R8295-1 (proposé)**
> À compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics, le traitement automatisé dénommé « Système d'information de la carte d'identification professionnelle » ne reçoit plus aucune donnée nouvelle. Les données antérieurement recueillies ne sont conservées que pour la gestion des opérations antérieures, de leurs créances, restitutions et recours, pendant la durée strictement nécessaire fixée par l'arrêté pris après avis de la Commission nationale de l'informatique et des libertés, puis effacées. Les droits des personnes concernées sur ces données demeurent applicables.

R8295-2 : ajouter un dernier alinéa :
> À compter de la même date, ces catégories ne désignent plus que les données antérieurement recueillies ; aucune n'est collectée ni mise à jour.

### 5.3 RT-03 — Agences de mannequins

**L7123-26 (proposé)**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique. L'exercice de l'activité d'exploitant d'agence de mannequins sans licence ou sans déclaration préalable n'est plus punissable à compter de cette date. Les faits antérieurs qui n'ont pas donné lieu à une condamnation passée en force de chose jugée bénéficient des dispositions pénales plus douces.

R7123-11, R7123-12 et R7123-14 : abrogation selon la formule de R7123-10-1 proposé (« Aucune licence ni pièce exclusivement destinée à sa délivrance ou à son maintien n'est exigible… »). Pour R7123-12, ajouter :
> Aucune déclaration préalable n'est exigée des agences légalement établies dans un autre État membre de l'Union européenne ou partie à l'accord sur l'Espace économique européen.

L8241-1 1° : remplacer « par une personne titulaire de la licence d'agence de mannequin » par « par une personne exerçant cette activité dans les conditions de l'article L. 7123-11 ».

Ce qui est préservé : l'agrément enfants (L7124-4, L7124-5), la garantie financière, la santé, les conflits d'intérêts.

### 5.4 RT-04 à RT-20

Les corrections minimales sont rédigées dans le champ `minimal_correction` de chaque objection du JSON. Les principales :
- RT-04 : abroger R3132-16 ; réduire R3132-17 aux conditions de fond.
- RT-05 : texte d'abrogation de D1237-4 et D1237-5 fourni.
- RT-06 : remplacer, dans D4622-27-6 V, le rapport D4622-56 par « les comptes annuels du dernier exercice clos ».
- RT-07 : clause de bornage temporel dans D1233-38 III bis.
- RT-18 : clause d'équivalence ajoutée à L1262-2.
- RT-20 : reporter la proposition de L5427-1 sur la version de 2028.

## 6. Incertitudes et éléments non examinés

- Pièces hors corpus non lues : code pénal, code rural (L725-3, R811-46), arrêtés (SI-CIP, formulaires DPAE, modèle D1237-5, arrêté sectoriel L1221-16), CESEDA, directives 96/71/CE, 2008/104/CE et 2006/123/CE, jurisprudence CJUE. Les points européens (RT-03, RT-18) restent à vérifier sur le texte consolidé.
- La revue est bornée aux alertes du paquet et aux textes que leurs notes désignent. D'autres règlements d'application peuvent présenter les mêmes défauts : D1233-37, -39, -40, -42, -45 à -48 ; composition du comité D5424 ; R6352-1 ; R3262-46 ; D4626-7 et -32.
- RT-20 : il n'a pas été vérifié si le pipeline reporte automatiquement les propositions sur les versions VIGUEUR_DIFF.
- Les propositions peuvent avoir changé depuis l'instantané. Les empreintes du JSON permettent de contrôler leur actualité.
