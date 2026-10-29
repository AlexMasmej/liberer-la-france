# Dossier P1-TRAVAIL-A : qualification des alertes « renvoi vers une abrogation proposée » (code du travail, paquet A)

Red-team juridique indépendante, troisième passe. Rapport établi le 26 octobre 2026 sur l'instantané `snapshots/20261026T230545Z` ; corpus daté du 18 octobre 2026. Objections préfixées `RT-P1-TRAVAIL-A-xx`.

**Avertissements.** Cette revue a été faite par une IA. Elle ne remplace pas la validation d'un juriste. La seconde passe continue en production (11 052 articles relus, 19 262 restants à la date de l'instantané) : toutes les conclusions sont provisoires et ne valent que pour les empreintes citées. Aucune source primaire n'a été consultée en ligne : toutes les pièces ont été lues dans l'instantané. Les quelques références au droit de l'Union sont citées de mémoire, sans conclusion de conformité.

Livrables :
- `reports/dossiers/P1-TRAVAIL-A.json` : 14 objections ;
- `reports/p1-work/P1-TRAVAIL-A-classification.jsonl` : 140 lignes, une par finding_id.

---

## 1. Résultat en bref

| Classification (140 alertes) | Nombre |
|---|---|
| alerte écartée | 94 |
| faux positif | 16 |
| coordination manquante | 18 |
| incohérence du projet | 12 |
| couvert par dossier | 0 |
| non examiné | 0 |

Les 30 alertes retenues forment **14 objections** : un effet juridique distinct par objection, sans double compte des renvois répétés.

| Priorité | Objections | Statut |
|---|---|---|
| P0 | aucune | — |
| P1 | 01 (R2312-21 / L2312-69), 02 (carte BTP), 03 (report du congé sabbatique) | confirmé |
| P2 | 04 à 14 | confirmé |

Les trois objections les plus importantes :

1. **RT-P1-TRAVAIL-A-02 (P1), carte d'identification professionnelle BTP.** L8291-1 proposé interdit d'exiger toute « demande, délivrance, présentation, mise à jour ». Or R8295-3-1, R8295-3, R8294-5, R8294-6 et R8295-1 sont maintenus inchangés et imposent encore une déclaration avant chaque mission, une mise à jour sous vingt-quatre heures et la présentation de la carte. Le traitement SI-CIP garde aussi une finalité de délivrance qui disparaît.
2. **RT-P1-TRAVAIL-A-03 (P1), report « combiné » du congé sabbatique.** Il repose uniquement sur L3142-114 et D3142-75, que le projet abroge sans distinguer les congés. L3142-29, D3142-21 et L3142-32 affirment pourtant le conserver.
3. **RT-P1-TRAVAIL-A-01 (P1), information trimestrielle du CSE.** R2312-21, réécrit et marqué « completed », maintient l'information trimestrielle « prévue au 3° de l'article L. 2312-69 », que le projet abroge.

**Contrat unique.** Aucune incohérence n'a été trouvée dans les textes du paquet qui le mettent en œuvre (voir § 4.3). Les abrogations du CDD examinées ici ne laissent aucun renvoi vivant dans les protections autonomes (voir § 4.4).

---

## 2. Périmètre réellement lu

Les 71 cibles et leurs 105 textes distincts qui y renvoient (126 couples cible–texte) (versions identifiées par code et identifiant LEGIARTI) ont été extraits avec `tools/cite.py`. Les sauvegardes sont dans `evidence/cited/20261026T230545Z/`. Pour chaque cible, la proposition d'abrogation a été lue en entier, avec ses clauses de transition et de neutralisation, son motif et ses notes. Pour chaque texte qui renvoie, le texte courant a été lu en entier : la proposition si `rewrite_draft`, la source si `retained_unchanged`, ainsi que le motif et les notes.

**Lecture non intégrale (14 alertes, `read_in_full=false`).** Deux pièces n'ont pas été lues en entier :
- l'annexe (1) à A931-11-17 CSS (LEGIARTI000006734907, 43 247 caractères) ;
- l'annexe I à R434-32 (5) CSS (LEGIARTI000028675245).

Pour ces deux pièces, chaque occurrence signalée a été lue dans son contexte. Il s'agit de numéros de lignes d'états comptables (« (L. 1) », « (L. 3) ») et de niveaux radiculaires (« D12 à L3 », « L1 - L3 »). Rien n'y renvoie aux articles L1 et L3 du code du travail. Ces alertes sont des faux positifs certains. Les tableaux de maladies professionnelles n° 97 et 98, eux, ont été lus en entier.

**Dépendances lues en plus** (sources, propositions, motifs, notes ; sauvegardes dans `evidence/cited/`) : L1251-58-6, L1234-1, L1234-9, L1221-26, L1237-19-11, L1237-19-12, L1237-19-13, L1237-19-14, D1233-41 (début), L3133-7, L3133-11, L3142-16, L3142-28, L3142-32, L3142-113, L3142-115, D3142-20, L6231-2, L6231-3, L6231-4, L6231-6, R5522-77, R5522-80, D1253-1, D1253-2, L8291-1, R8291-2, R8291-4, R8294-5, R8294-8, R8295-1, R8295-3, R3262-9 et ses voisins (statuts), L6323-17-5-1 (versions futures de 2027 et 2028), R3324-22 (version future de 2029), L2412-2, L1226-20, L1243-8, L1244-2-2 et L1242-2 (début des propositions, contrôle des protections autonomes).

Tableau complet par cluster :

| # | Cible abrogée (code, n°, version, bornes, inventaire) | Textes qui renvoient (code, n°, version, statut, inventaire) | Alertes | Qualification |
|---|---|---|---|---|
| 0 | travail L3 LEGIARTI000042654542 (2021-06-01 → 2999-01-01, completed) | css Annexe (1) à l'art. A931-11-17 LEGIARTI000006734907 (rewrite_draft, pending)<br>css Annexe II : Tableau n° 97 LEGIARTI000006746422 (retained_unchanged, pending)<br>css Annexe II : Tableau n° 98 LEGIARTI000006746423 (retained_unchanged, pending)<br>css Annexe I à l'art. R434-32 (5) LEGIARTI000028675245 (retained_unchanged, pending) | 10 | faux positif ×10 |
| 1 | travail L3231-3 LEGIARTI000006902833 (2008-05-01 → 2999-01-01, pending) | travail L3232-3 LEGIARTI000006902847 (retained_unchanged, pending)<br>travail L3423-7 LEGIARTI000006903135 (retained_unchanged, pending)<br>travail R3233-1 LEGIARTI000018533820 (retained_unchanged, pending)<br>travail L1251-58-3 LEGIARTI000037379974 (rewrite_draft, completed)<br>travail D5122-15 LEGIARTI000044946857 (rewrite_draft, pending)<br>travail L8115-1 LEGIARTI000054335756 (retained_unchanged, pending)<br>css D531-9 LEGIARTI000041968391 (rewrite_draft, pending) | 7 | alerte écartée ×7 |
| 2 | travail L1 LEGIARTI000018764571 (2008-05-01 → 2999-01-01, completed) | css Annexe (1) à l'art. A931-11-17 LEGIARTI000006734907 (rewrite_draft, pending)<br>css Annexe I à l'art. R434-32 (5) LEGIARTI000028675245 (retained_unchanged, pending) | 6 | faux positif ×6 |
| 3 | travail L1251-12-1 LEGIARTI000035638866 (2017-09-24 → 2999-01-01, completed) | travail L1255-7 LEGIARTI000035644073 (rewrite_draft, completed)<br>travail L1251-34 LEGIARTI000035644080 (rewrite_draft, completed)<br>travail L1251-40 LEGIARTI000036262126 (rewrite_draft, completed)<br>travail L5213-13-3 LEGIARTI000048589910 (rewrite_draft, completed) | 5 | alerte écartée ×5 |
| 4 | travail L5424-17 LEGIARTI000006903896 (2008-05-01 → 2999-01-01, pending) | travail L1251-20 LEGIARTI000006901271 (rewrite_draft, completed)<br>travail D5424-17 LEGIARTI000018524908 (retained_unchanged, pending)<br>travail D5424-7 LEGIARTI000018524936 (retained_unchanged, pending)<br>travail L6331-35 LEGIARTI000041472880 (rewrite_draft, pending) | 4 | alerte écartée ×4 |
| 5 | travail L3141-29 LEGIARTI000033020678 (2016-08-10 → 2999-01-01, pending) | travail L3141-30 LEGIARTI000033020675 (rewrite_draft, pending)<br>travail R3143-1 LEGIARTI000033471401 (retained_unchanged, pending)<br>travail D7121-31 LEGIARTI000033516037 (rewrite_draft, pending)<br>travail L7221-2 LEGIARTI000047293314 (rewrite_draft, pending) | 4 | alerte écartée ×4 |
| 6 | travail L1237-19-9 LEGIARTI000036703157 (2018-01-01 → 2999-01-01, completed) | travail D1233-43 LEGIARTI000036248524 (rewrite_draft, pending)<br>travail D1233-37 LEGIARTI000036248563 (retained_unchanged, pending)<br>travail D1233-48-1 LEGIARTI000047777578 (rewrite_draft, pending)<br>travail D1233-38 LEGIARTI000047779099 (rewrite_draft, pending) | 4 | coordination manquante → RT-P1-TRAVAIL-A-04 ×4 |
| 7 | travail L1251-46 LEGIARTI000018766986 (2008-05-01 → 2999-01-01, completed) | travail L1251-58-4 LEGIARTI000037379976 (rewrite_draft, completed)<br>travail R1263-7 LEGIARTI000042168325 (rewrite_draft, pending)<br>travail R5312-42 LEGIARTI000050943179 (rewrite_draft, pending)<br>css R133-14 LEGIARTI000054167679 (rewrite_draft, pending) | 4 | alerte écartée ×3; incohérence du projet → RT-P1-TRAVAIL-A-08 ×1 |
| 8 | travail L6231-5 LEGIARTI000038951789 (2019-08-23 → 2999-01-01, pending) | travail R6232-1 LEGIARTI000039355507 (retained_unchanged, pending)<br>travail R6233-1 LEGIARTI000039355540 (rewrite_draft, pending)<br>travail L6356-1 LEGIARTI000054319153 (rewrite_draft, pending)<br>travail L6351-3 LEGIARTI000054336979 (rewrite_draft, pending) | 4 | alerte écartée ×3; incohérence du projet → RT-P1-TRAVAIL-A-06 ×1 |
| 9 | travail L6123-7-1 LEGIARTI000052437400 (2026-01-01 → 2999-01-01, pending) | travail L6323-17-5-1 LEGIARTI000052437402 (rewrite_draft, pending)<br>travail R6123-8 LEGIARTI000054107746 (rewrite_draft, pending)<br>travail R6123-21 LEGIARTI000054107762 (retained_unchanged, pending) | 4 | incohérence du projet → RT-P1-TRAVAIL-A-07 ×4 |
| 10 | travail L1225-53 LEGIARTI000006900938 (2008-05-01 → 2999-01-01, completed) | travail L1225-70 LEGIARTI000006900958 (retained_unchanged, completed)<br>travail L1225-72 LEGIARTI000006900964 (retained_unchanged, completed)<br>travail L1225-71 LEGIARTI000035643521 (retained_unchanged, completed) | 3 | alerte écartée ×3 |
| 11 | travail R5422-8 LEGIARTI000019562588 (2008-12-19 → 2999-01-01, pending) | travail R5429-1 LEGIARTI000018524656 (retained_unchanged, pending)<br>travail R5422-6 LEGIARTI000018525121 (rewrite_draft, pending)<br>travail D1272-2 LEGIARTI000038251781 (rewrite_draft, pending) | 3 | alerte écartée ×3 |
| 12 | travail L3121-40 LEGIARTI000035653037 (2018-01-01 → 2999-01-01, pending) | travail R3124-7 LEGIARTI000033471439 (rewrite_draft, pending)<br>travail R3124-2 LEGIARTI000033471465 (rewrite_draft, pending)<br>travail R3124-1 LEGIARTI000033471471 (rewrite_draft, pending) | 3 | alerte écartée ×3 |
| 13 | travail L1251-35-1 LEGIARTI000035638917 (2017-09-24 → 2999-01-01, completed) | travail L1255-8 LEGIARTI000035644066 (rewrite_draft, completed)<br>travail L1251-40 LEGIARTI000036262126 (rewrite_draft, completed) | 3 | alerte écartée ×3 |
| 14 | travail L1237-19-10 LEGIARTI000035623990 (2018-01-01 → 2999-01-01, completed) | travail D1233-44 LEGIARTI000036248518 (rewrite_draft, pending)<br>travail D1233-40 LEGIARTI000036248541 (retained_unchanged, pending)<br>travail D1233-37 LEGIARTI000036248563 (retained_unchanged, pending) | 3 | coordination manquante → RT-P1-TRAVAIL-A-04 ×3 |
| 15 | travail L6231-7 LEGIARTI000037372035 (2019-01-01 → 2999-01-01, pending) | travail R6232-1 LEGIARTI000039355507 (retained_unchanged, pending)<br>travail R6233-1 LEGIARTI000039355540 (rewrite_draft, pending)<br>travail L6356-1 LEGIARTI000054319153 (rewrite_draft, pending) | 3 | alerte écartée ×3 |
| 16 | travail L2312-79 LEGIARTI000035611313 (2018-01-01 → 2999-01-01, completed) | travail D1132-1 LEGIARTI000054323930 (retained_unchanged, pending)<br>cch R342-32 LEGIARTI000046112667 (retained_unchanged, pending)<br>cch R342-30 LEGIARTI000046112679 (retained_unchanged, pending) | 3 | alerte écartée ×3 |
| 17 | travail L1243-4 LEGIARTI000024026880 (2011-05-19 → 2999-01-01, completed) | travail L1242-11 LEGIARTI000006901205 (rewrite_draft, completed)<br>travail L6222-18 LEGIARTI000037386025 (rewrite_draft, pending) | 2 | alerte écartée ×2 |
| 18 | travail L321-4-2 LEGIARTI000018124959 (2012-01-01 → 2999-01-01, completed) | travail L143-11-7 LEGIARTI000018124885 (rewrite_draft, pending)<br>travail L351-5-1 LEGIARTI000038314413 (rewrite_draft, pending) | 2 | alerte écartée ×2 |
| 19 | travail R5522-82 LEGIARTI000018524404 (2008-05-01 → 2999-01-01, pending) | travail R5522-59 LEGIARTI000018524458 (retained_unchanged, pending)<br>travail R5522-60 LEGIARTI000049820903 (retained_unchanged, pending) | 2 | coordination manquante → RT-P1-TRAVAIL-A-10 ×2 |
| 20 | travail D1253-4 LEGIARTI000022356943 (2010-02-15 → 2999-01-01, pending) | travail R1253-44 LEGIARTI000018537184 (retained_unchanged, pending)<br>travail R1255-9 LEGIARTI000031814181 (rewrite_draft, pending) | 2 | coordination manquante → RT-P1-TRAVAIL-A-09 ×1; incohérence du projet → RT-P1-TRAVAIL-A-09 ×1 |
| 21 | travail L1254-15 LEGIARTI000030436220 (2015-04-04 → 2999-01-01, completed) | travail R1254-2 LEGIARTI000031818244 (rewrite_draft, completed)<br>travail L1254-9 LEGIARTI000033024484 (rewrite_draft, completed) | 2 | alerte écartée ×2 |
| 22 | travail L3133-12 LEGIARTI000035653012 (2018-01-01 → 2999-01-01, pending) | travail L3134-16 LEGIARTI000033008282 (retained_unchanged, pending)<br>travail L3422-1 LEGIARTI000033021064 (retained_unchanged, pending) | 2 | coordination manquante → RT-P1-TRAVAIL-A-11 ×1; alerte écartée ×1 |
| 23 | travail L1251-37 LEGIARTI000035644047 (2017-09-24 → 2999-01-01, completed) | travail L1251-37-1 LEGIARTI000035638998 (rewrite_draft, completed)<br>travail L1251-58-4 LEGIARTI000037379976 (rewrite_draft, completed) | 2 | alerte écartée ×2 |
| 24 | travail L2312-69 LEGIARTI000035611011 (2018-01-01 → 2999-01-01, completed) | travail R2312-21 LEGIARTI000036412642 (rewrite_draft, completed)<br>cch R342-30 LEGIARTI000046112679 (retained_unchanged, pending) | 2 | incohérence du projet → RT-P1-TRAVAIL-A-01 ×1; alerte écartée ×1 |
| 25 | travail R6313-6 LEGIARTI000038014111 (2019-01-01 → 2999-01-01, pending) | travail R1233-35 LEGIARTI000038033419 (retained_unchanged, pending)<br>travail D6323-6 LEGIARTI000053572443 (rewrite_draft, pending) | 2 | alerte écartée ×2 |
| 26 | travail L6331-69 LEGIARTI000048849229 (2023-12-31 → 2999-01-01, pending) | travail L6355-24 LEGIARTI000044981883 (rewrite_draft, pending)<br>travail L6332-1-2 LEGIARTI000048700917 (rewrite_draft, pending) | 2 | alerte écartée ×2 |
| 27 | travail L3142-17 LEGIARTI000033022071 (2016-08-10 → 2999-01-01, pending) | travail L7221-2 LEGIARTI000047293314 (rewrite_draft, pending)<br>travail R3324-22 LEGIARTI000049905590 (retained_unchanged, pending) | 2 | alerte écartée ×1; coordination manquante → RT-P1-TRAVAIL-A-13 ×1 |
| 28 | travail R8293-1 LEGIARTI000049153155 (2024-04-01 → 2999-01-01, pending) | travail R8295-2 LEGIARTI000049153210 (rewrite_draft, pending)<br>travail R8295-3-1 LEGIARTI000049153249 (retained_unchanged, pending) | 2 | coordination manquante → RT-P1-TRAVAIL-A-02 ×2 |
| 29 | travail R6223-1 LEGIARTI000041771443 (2020-04-01 → 2999-01-01, completed) | travail D6235-2 LEGIARTI000051400163 (rewrite_draft, pending) | 2 | alerte écartée ×2 |
| 30 | travail L2315-5 LEGIARTI000035651250 (2018-01-01 → 2999-01-01, completed) | travail L1221-14 LEGIARTI000006900853 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 31 | travail L1243-2 LEGIARTI000031087476 (2015-08-19 → 2999-01-01, completed) | travail L1242-11 LEGIARTI000006901205 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 32 | travail L1243-7 LEGIARTI000006901218 (2008-05-01 → 2999-01-01, completed) | travail L1242-11 LEGIARTI000006901205 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 33 | travail L2525-2 LEGIARTI000006902429 (2008-05-01 → 2999-01-01, pending) | travail L2523-9 LEGIARTI000006902411 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 34 | travail R7123-26 LEGIARTI000018521574 (2008-05-01 → 2999-01-01, pending) | travail R7123-29 LEGIARTI000018521568 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 35 | travail D6325-25 LEGIARTI000018522973 (2008-05-01 → 2999-01-01, pending) | travail D6325-25 LEGIARTI000018522973 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 36 | travail D5424-43 LEGIARTI000018524852 (2008-05-01 → 2999-01-01, pending) | travail R5429-3 LEGIARTI000018524652 (rewrite_draft, pending) | 1 | incohérence du projet → RT-P1-TRAVAIL-A-05 ×1 |
| 37 | travail R5423-13 LEGIARTI000018525058 (2008-05-01 → 2999-01-01, pending) | travail D5424-62 LEGIARTI000018524804 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 38 | travail R4152-22 LEGIARTI000018532761 (2008-05-01 → 2999-01-01, pending) | travail R4743-2 LEGIARTI000018527366 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 39 | travail R3262-8 LEGIARTI000028699416 (2014-04-02 → 2999-01-01, pending) | travail R3262-46 LEGIARTI000018533419 (rewrite_draft, pending) | 1 | incohérence du projet → RT-P1-TRAVAIL-A-12 ×1 |
| 40 | travail R3262-17 LEGIARTI000021926383 (2010-03-05 → 2999-01-01, pending) | travail R3262-46 LEGIARTI000018533419 (rewrite_draft, pending) | 1 | incohérence du projet → RT-P1-TRAVAIL-A-12 ×1 |
| 41 | travail L2525-1 LEGIARTI000006902428 (2008-05-01 → 2999-01-01, pending) | travail R2525-1 LEGIARTI000018534736 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 42 | travail D1253-6 LEGIARTI000022356995 (2010-02-15 → 2999-01-01, pending) | travail R1253-44 LEGIARTI000018537184 (retained_unchanged, pending) | 1 | coordination manquante → RT-P1-TRAVAIL-A-09 ×1 |
| 43 | travail R6352-24 LEGIARTI000039355601 (2019-11-09 → 2999-01-01, pending) | travail R6351-9 LEGIARTI000022257953 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 44 | travail L1242-10 LEGIARTI000006901204 (2008-05-01 → 2999-01-01, completed) | travail L1221-25 LEGIARTI000029144958 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 45 | travail L1243-10 LEGIARTI000006901221 (2008-05-01 → 2999-01-01, completed) | travail L1254-18 LEGIARTI000030436459 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 46 | travail L3133-8 LEGIARTI000033020862 (2016-08-10 → 2999-01-01, pending) | travail L3422-1 LEGIARTI000033021064 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 47 | travail L3142-114 LEGIARTI000033022269 (2016-08-10 → 2999-01-01, pending) | travail L3142-29 LEGIARTI000033022115 (retained_unchanged, pending) | 1 | coordination manquante → RT-P1-TRAVAIL-A-03 ×1 |
| 48 | travail L1255-9 LEGIARTI000035644059 (2017-09-24 → 2999-01-01, completed) | travail L5132-14 LEGIARTI000033024468 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 49 | travail D3142-75 LEGIARTI000033510247 (2017-01-01 → 2999-01-01, pending) | travail D3142-21 LEGIARTI000033509387 (retained_unchanged, pending) | 1 | coordination manquante → RT-P1-TRAVAIL-A-03 ×1 |
| 50 | travail R3142-44 LEGIARTI000033444399 (2017-01-01 → 2999-01-01, pending) | travail D3142-38 LEGIARTI000033510572 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 51 | travail L1242-8 LEGIARTI000035643967 (2017-09-24 → 2999-01-01, completed) | travail L1243-12 LEGIARTI000035644025 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 52 | travail L1251-36-1 LEGIARTI000035638964 (2017-09-24 → 2999-01-01, completed) | travail L1255-9 LEGIARTI000035644059 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 53 | travail L1243-13-1 LEGIARTI000035639380 (2017-09-24 → 2999-01-01, completed) | travail L1233-72-1 LEGIARTI000036261982 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 54 | travail R7111-4 LEGIARTI000018522034 (2008-05-01 → 2999-01-01, pending) | travail D7522-1 LEGIARTI000037584099 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 55 | travail L6331-5 LEGIARTI000038952124 (2019-08-23 → 2999-01-01, pending) | travail R6523-1 LEGIARTI000041611735 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 56 | travail L6331-40 LEGIARTI000042914271 (2022-01-01 → 2999-01-01, pending) | travail R6523-1 LEGIARTI000041611735 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 57 | travail L3344-3 LEGIARTI000035653250 (2018-01-01 → 2999-01-01, pending) | travail L3347-1 LEGIARTI000042009015 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 58 | travail R6331-37 LEGIARTI000044969980 (2022-01-01 → 2999-01-01, pending) | travail R6331-40 LEGIARTI000044969974 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 59 | travail R7343-101 LEGIARTI000046322266 (2022-09-24 → 2999-01-01, pending) | travail R7343-102 LEGIARTI000046322268 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 60 | travail L8256-5 LEGIARTI000006904872 (2008-05-01 → 2999-01-01, pending) | travail L8323-3 LEGIARTI000049050064 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 61 | travail R8292-1 LEGIARTI000049153176 (2024-04-01 → 2999-01-01, pending) | travail R8294-6 LEGIARTI000049153224 (retained_unchanged, pending) | 1 | coordination manquante → RT-P1-TRAVAIL-A-02 ×1 |
| 62 | travail D5132-18-1 LEGIARTI000049754347 (2024-07-01 → 2999-01-01, pending) | travail R5523-15-43 LEGIARTI000050742418 (rewrite_draft, pending) | 1 | incohérence du projet → RT-P1-TRAVAIL-A-14 ×1 |
| 63 | travail R6222-7 LEGIARTI000041771297 (2020-04-01 → 2999-01-01, completed) | travail D6235-3 LEGIARTI000051395697 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 64 | travail L6353-11 LEGIARTI000054319358 (2026-06-27 → 2999-01-01, pending) | travail L6356-1 LEGIARTI000054319153 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 65 | travail R7232-8 LEGIARTI000033747462 (2016-12-30 → 2999-01-01, pending) | css D133-21 LEGIARTI000050740376 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 66 | travail L3142-47 LEGIARTI000033022158 (2016-08-10 → 2999-01-01, pending) | css L412-8 LEGIARTI000053283575 (rewrite_draft, completed) | 1 | alerte écartée ×1 |
| 67 | travail L1221-18 LEGIARTI000037064963 (2018-06-14 → 2999-01-01, completed) | css R133-14 LEGIARTI000054167679 (rewrite_draft, pending) | 1 | alerte écartée ×1 |
| 68 | travail L2312-29 LEGIARTI000035609820 (2018-01-01 → 2999-01-01, completed) | cch R342-30 LEGIARTI000046112679 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 69 | travail L2312-32 LEGIARTI000035609826 (2018-01-01 → 2999-01-01, completed) | cch R342-30 LEGIARTI000046112679 (retained_unchanged, pending) | 1 | alerte écartée ×1 |
| 70 | travail R2312-61 LEGIARTI000036413365 (2018-01-01 → 2999-01-01, pending) | cch R342-30 LEGIARTI000046112679 (retained_unchanged, pending) | 1 | alerte écartée ×1 |

---

## 3. Méthode

1. Pour chaque cluster, la proposition d'abrogation de la cible a été lue en entier. Ont été notés : la date de bascule (immédiate, par accord conclu, par période de travail ou par échéance), les transitions, les clauses de neutralisation (« ne peut fonder », « ne rétablit pas ») et les coordinations que les notes déclarent « hors lot ».
2. Pour chaque texte qui renvoie, le texte courant a été lu en entier. Il a d'abord été vérifié que le numéro cité vise bien la cible : même code, même article, pas un homonyme. C'est ce contrôle qui a écarté les 16 faux positifs des annexes CSS.
3. Chaque renvoi a ensuite été qualifié selon l'addendum. Un renvoi est **écarté** s'il est historique ou transitoire, neutralisé ou redirigé, ou s'il figure dans une plage ou une liste d'exclusion sans effet sur la règle abrogée, ou encore si le texte qui renvoie est lui-même abrogé. Un texte maintenu qui applique encore la règle comme vivante relève de la **coordination manquante**. Une proposition réécrite qui s'appuie activement sur la règle abrogée relève de l'**incohérence du projet**.
4. Les renvois qui ont le même effet ont été regroupés en une seule objection. Des articles du même mécanisme qui ne citent pas la cible par son numéro, et que l'audit ne pouvait donc pas repérer, ont été ajoutés comme dépendances : R8294-5, R8295-1 et R8295-3 (objection 02), L3142-32 (03), R3262-9 (12).
5. Recoupements avec d'autres dossiers ouverts :
   - aucun article de la liste des dossiers ouverts n'est touché ;
   - l'annexe I à R434-32 (5) n'est pas couverte par RESINT, qui ne vise que la figure du (7) : ses alertes sont classées faux positifs, sans renvoi à ce dossier ;
   - les versions futures (VIGUEUR_DIFF) de L6323-17-5-1 et de R3324-22 relèvent du paquet FUT-TRAV-LOG (`reports/p1-work/FUT-TRAV-LOG.json`). Elles sont signalées comme dépendances, sans objection en double.

---

## 4. Constats

### 4.1 Objections

| ID | P | Nature | Objet | Articles principaux |
|---|---|---|---|---|
| 01 | P1 | incohérence du projet | Information trimestrielle du CSE maintenue par R2312-21 malgré l'abrogation de L2312-69 | L2312-69 (…35611011), R2312-21 (…36412642) |
| 02 | P1 | coordination manquante | Résidus réglementaires de la carte BTP : obligations de l'employeur et traitement SI-CIP | L8291-1, R8295-3-1, R8295-3, R8294-5, R8294-6, R8295-1, R8295-2 |
| 03 | P1 | coordination manquante | Report combiné du congé sabbatique privé de fondement | L3142-114, D3142-75, L3142-29, D3142-21, L3142-32 |
| 04 | P2 | coordination manquante | Volet RCC de la revitalisation non borné aux accords antérieurs | D1233-37, -38, -40, -43, -44, -48-1 |
| 05 | P2 | incohérence du projet | Contravention R5429-3 fondée sur la mise en demeure supprimée de D5424-43 | D5424-43, R5429-3 |
| 06 | P2 | incohérence du projet | Motif de refus d'enregistrement fondé sur la mention statutaire supprimée | L6231-5, L6351-3 3° |
| 07 | P2 | incohérence du projet | Commission CEP de France compétences sans ancrage après l'abrogation de L6123-7-1 | L6323-17-5-1 4°, R6123-8 20°, R6123-21 |
| 08 | P2 | incohérence du projet | Finalité de traitement DSN pour le relevé de mission supprimé | L1251-46, R5312-42 1° c) |
| 09 | P2 | incohérence du projet | Groupements d'employeurs : renvois aux déclarations supprimées | D1253-4, D1253-6, R1255-9, R1253-44 |
| 10 | P2 | coordination manquante | « Organisme agréé » maintenu après la suppression de l'agrément de mobilité outre-mer | R5522-80/82, R5522-59, R5522-60 |
| 11 | P2 | coordination manquante | Journée de solidarité : L3134-16 maintenu comme si elle existait | L3133-7 à L3133-12, L3134-16 |
| 12 | P2 | incohérence du projet | Liste pénale des titres-restaurant visant des articles abrogés | R3262-8, R3262-9, R3262-17, R3262-46 |
| 13 | P2 | coordination manquante | Déblocage anticipé pour proche aidant défini par renvoi à L3142-17 abrogé | L3142-17, R3324-22 10° |
| 14 | P2 | incohérence du projet | Renvoi nouveau vers la consultation abrogée de D5132-18-1 | D5132-18-1, R5523-15-43 |

Le raisonnement, les passages exacts, les conséquences et les options figurent dans le JSON. Points saillants :

- **01.** La cible neutralise expressément « les dispositions réglementaires prises pour son application ». Le risque juridique en est réduit, mais R2312-21 reste rédigé comme autonome (six rubriques, motifs de recours) et son motif invoque une obligation législative abrogée. Il est marqué « completed » : il ne sera pas repris d'office. La priorité P1 tient à ce point.
- **02.** Les propositions abrogatives (R8292-1, R8293-1, R8291-2) signalent elles-mêmes que « R8294-5 et R8295-1 à R8295-3 […] doivent cesser d'imposer présentation, collecte et mises à jour ». Ces articles sont pourtant classés `retained_unchanged`, avec des motifs qui supposent la carte maintenue : « la carte que L8291-1 conserve ». Doivent être préservés R8291-4 (limitation de finalité), R8294-8 (document d'information des travailleurs détachés) et les contrôles autonomes.
- **03.** Les clauses d'abrogation de L3142-114 et de D3142-75 sont générales : « aucun report ne peut être décidé […] sur le seul fondement du présent article ». Le motif de L3142-114 affirme que le sabbatique reste distinct, ce qui est inexact : son report combiné n'existe que par le renvoi du deuxième alinéa de L3142-29 et par D3142-21. Deux voies cohérentes existent. L'option A suit l'intention exprimée par L3142-28, L3142-29, L3142-32 et D3142-21 : un fondement autonome limité au sabbatique. L'option B étend la suppression au sabbatique. C'est un choix de fond, à ne pas trancher par simple coordination.

### 4.2 Alertes écartées : motifs types

- **Plages de renvoi encore opérantes** (environ 45) : par exemple L3231-2 à L3231-12 pour le SMIC, L5424-6 à L5424-19 pour les intempéries, L3141-1 à L3141-33 pour les congés payés, L1225-1 à L1225-69 pour la maternité, L2312-78 à L2312-84 pour les activités sociales, L6331-1 à L6331-68 pour les contributions formation. Dans chaque cas, l'article abrogé inclus dans la plage ne porte pas la règle visée, ou il s'agit d'une plage pénale ou de dispense devenue sans objet.
- **Renvois historiques ou transitoires assumés** (environ 30) : tout le bloc CDD, intérim et portage (L1242-11, L1243-12, L1251-34, L1251-40, L1255-7, L5213-13-3, L1254-9, L1254-18, R1254-2, L1233-72-1, L6222-18, L1221-25) ainsi que L143-11-7 et L351-5-1 (ancienne CRP).
- **Neutralisations expresses** (environ 12) : R1263-7, L1251-58-4, R5422-6, R3124-7, R4743-2, L6356-1 (pour L6353-11), L6332-1-2, D6235-2, R7343-102, D3142-38 et L3141-30.
- **Listes d'exclusion sans effet** : R342-30 CCH (ANCOLS), L3347-1, L5132-14, D6235-3, L3422-1.
- **Dispenses devenues sans objet** dans R133-14 CSS (IV 2° vers L1251-46, IV 3° vers L1221-18) : sans effet normatif, à nettoyer lors de la consolidation.

### 4.3 Contrat unique : vérifications faites dans le paquet

Les propositions suivantes ont été confrontées aux orientations (préavis de quinze jours calendaires de chaque côté, aucune indemnité ordinaire avant un an, 0,20 mois par année d'ancienneté totale avec prorata des mois complets, plafond de six mois, due seulement en cas de rupture par l'employeur) : L7221-2 6° (particulier employeur), D6235-2 (apprentissage transfrontalier), L6222-18 (apprentissage), L1221-25 et L1221-26 (essai), L1234-1 et L1234-9.

- **Préavis.** Quinze jours calendaires pour l'employeur comme pour le salarié. Le délai court du lendemain de la présentation ou de la réception de la notification et expire à la fin du quinzième jour, même non travaillé (L1234-3). Les dispenses favorables au salarié sont conservées. Pendant l'essai, le préavis ne prolonge pas l'essai : le reliquat patronal est compensé (L1221-25) et la poursuite du préavis du salarié au-delà de l'essai vaut démission sans second préavis (L1221-26). La faute grave ne supprime pas le préavis patronal, qui est alors payé sans exécution (L1234-1 et D6235-2, concordants).
- **Indemnité ordinaire.** Aucune avant un an d'ancienneté, apprécié à la fin effective du contrat, préavis inclus. Au-delà : 0,20 mois de salaire brut de référence par année d'ancienneté totale, fractions au prorata des mois complets, plafond de six mois. Elle n'est due qu'en cas de rupture patronale et n'est pas due en cas de faute grave (L1234-9). La première année n'est pas retranchée. Pour les anciens contrats, la part antérieure garde son régime, sans double compte. L7221-2 et D6235-2 reprennent exactement ce barème. Aucun écart n'a été constaté.
- **Protections autonomes.** L1226-20 (inaptitude, anciens CDD) garde le doublement sans condition d'ancienneté. L1225-70 à L1225-72 (maternité) et L412-8 CSS (accidents du travail, 7°) sont conservés. L2412-2 (salariés protégés) réserve les renvois au CDD aux contrats antérieurs.

### 4.4 Abrogations du CDD et protections autonomes

Les cibles CDD du paquet (L1242-8, L1242-10, L1243-2, L1243-4, L1243-7, L1243-10, L1243-13-1) ne sont citées que par des textes eux-mêmes abrogés ou bornés aux contrats antérieurs. Un balayage complémentaire, hors alertes du paquet, de L2411 à L2413, L2421, L1225 et L1226 a relevé des renvois à L1241-1, L1242-2, L1243-8 et L1244-2-2 dans L2412-2 à L2412-13, L2421-8-1, L1226-4-3 et L1226-20. Pour L2412-2 et L1226-20, la lecture confirme un bornage exprès aux contrats antérieurs. Le cas de L1243-8 relève du paquet P1-TRAVAIL-B, qui le contient. Les autres renvois n'ont pas été lus en entier ici (voir § 6).

---

## 5. Propositions de correction (présentées séparément)

Ces textes sont des propositions de la red-team. Ils ne sont pas intégrés et doivent être confrontés à la version courante avant tout usage. Aucun ne crée de formalité, de taxe ou d'agrément de remplacement.

### 5.1 R2312-21 (objection 01) : article complet proposé

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi abrogeant l'article L. 2312-69.
>
> À compter de cette date, aucune information trimestrielle sur l'évolution des effectifs et de la qualification des salariés par sexe, aucune présentation des motifs de recours aux contrats à durée déterminée, au travail temporaire ou aux salariés d'entreprises extérieures et aucun décompte ne sont exigés sur le fondement du présent article, y compris pour un trimestre antérieur dont la mise à disposition n'a pas encore été effectuée. Aucun relevé, aucune transmission ni aucun rattrapage n'est exigé à ce titre.
>
> Les informations régulièrement communiquées avant cette date n'ont pas à être refaites ; elles demeurent accessibles dans la forme où elles ont été communiquées. Les obligations d'information et de consultation ayant un fondement autonome, notamment la base de données économiques, sociales et environnementales, les consultations récurrentes et les indicateurs relatifs à l'égalité professionnelle, demeurent applicables dans leur champ propre.
>
> Les droits et recours relatifs aux manquements antérieurs demeurent, sous réserve de l'application de la loi répressive plus douce.

*Justification :* alignement exact sur la bascule et sur la neutralisation de L2312-69. *Dépendances :* adoption de L2312-69 ; motif de R2312-21 à remplacer ; renvoi résiduel de R342-30 CCH à vérifier.

### 5.2 Carte BTP (objection 02) : textes proposés

**R8294-5**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune présentation de la carte ou de l'attestation provisoire ne peut être exigée après cette date, y compris pour une carte en cours de validité. Les pouvoirs de contrôle que les agents mentionnés à l'article L. 8271-1-2 tiennent d'autres dispositions demeurent applicables. Les faits antérieurs restent soumis aux règles d'application dans le temps de la loi répressive plus douce.

**R8294-6**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune vérification de déclaration ou de carte auprès de l'association "CIBTP France" n'est organisée après cette date. Les obligations de vigilance des maîtres d'ouvrage et des donneurs d'ordre fondées sur d'autres dispositions demeurent applicables.

**R8295-1**
> Le traitement automatisé d'informations à caractère personnel dénommé "Système d'information de la carte d'identification professionnelle" (SI-CIP), créé au sein de l'association "CIBTP France", ne reçoit plus aucune donnée nouvelle à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. À compter de cette date, sa seule finalité est la gestion des opérations antérieures et de leurs suites, notamment les créances, restitutions et recours mentionnés à l'article R. 8291-2, ainsi que l'exercice des droits des personnes concernées. Les données sont effacées au terme de la durée strictement nécessaire à ces finalités, selon les modalités fixées par l'arrêté du ministre chargé du travail pris après avis de la Commission nationale de l'informatique et des libertés. Cet arrêté ne peut prévoir aucune collecte, mise à jour ni utilisation nouvelle.

**R8295-2** : remplacer l'alinéa « Les renseignements énumérés aux 1° à 3° sont mentionnés par les employeurs sur les déclarations mentionnées aux articles R. 8293-1 et R. 8293-2. » par :
> Les renseignements énumérés aux 1° à 3° sont ceux qui ont été mentionnés par les employeurs sur les déclarations effectuées en application des articles R. 8293-1 et R. 8293-2 dans leur rédaction antérieure à l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune donnée n'est collectée ni mise à jour après cette date.

**R8295-3**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune information de l'association "CIBTP France" sur la modification des renseignements relatifs à l'employeur ou aux salariés n'est exigée après cette date. Les faits antérieurs restent soumis aux règles d'application dans le temps de la loi répressive plus douce.

**R8295-3-1**
> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la carte d'identification professionnelle des salariés du bâtiment et des travaux publics. Aucune modification de déclaration ni activation de carte n'est exigée avant une mission ou un détachement. La déclaration de détachement prévue à l'article L. 1262-2-1 et les obligations de l'entreprise de travail temporaire fondées sur d'autres dispositions demeurent applicables.

*Justification :* exécuter la suppression déjà décidée dans L8291-1, sans formalité de remplacement, et donner au traitement résiduel une finalité licite. *Dépendances :* arrêté SI-CIP (non fourni) ; motifs de R8294-5, R8294-6, R8295-1, R8295-3 et R8295-3-1 à réécrire ; R8291-4 et R8294-8 à maintenir.

### 5.3 Congé sabbatique (objection 03)

**Option A (recommandée pour suivre l'intention exprimée par les textes du sabbatique).**

**L3142-29**, article complet proposé :
> L'employeur peut différer le départ en congé dans la limite de six mois à compter de la demande, en fonction de la proportion de salariés absents dans l'entreprise au titre du congé ou en fonction du nombre de jours d'absence prévus au titre du même congé. Dans les entreprises de moins de trois cents salariés, cette limite est portée à neuf mois.
>
> L'employeur peut également différer ce congé lorsque ce départ aurait pour effet de porter l'effectif des salariés simultanément absents ou le nombre de jours d'absence au titre de ce congé et au titre du congé pour création ou reprise d'entreprise à un niveau excessif au regard, respectivement, de l'effectif total et du nombre de jours travaillés dans l'entreprise. Dans les entreprises de moins de trois cents salariés, il peut le refuser sur le fondement du 1° de l'article L. 3142-113, selon les modalités prévues aux deux derniers alinéas du même article.
>
> L'abrogation de l'article L. 3142-114 ne prive pas l'employeur de la faculté de report prévue au deuxième alinéa pour le seul congé sabbatique. Elle ne permet aucun report du congé ou de la période de travail à temps partiel pour création ou reprise d'entreprise.

**L3142-32, 4°**
> 4° Les plafonds mentionnés aux deux premiers alinéas de l'article L. 3142-29 ;

**D3142-21**, article complet proposé :
> A défaut de convention ou d'accord mentionné à l'article L. 3142-32, le départ en congé sabbatique peut être différé par l'employeur dans les conditions mentionnées au deuxième alinéa de l'article L. 3142-29, de telle sorte que le pourcentage des salariés simultanément absents de l'entreprise au titre du congé sabbatique et du congé pour la création d'entreprise ou pour l'exercice de responsabilités de direction au sein d'une entreprise répondant aux critères de jeune entreprise innovante ne dépasse pas 2 % de l'effectif de cette entreprise, jusqu'à la date à laquelle cette condition de taux est remplie, ou que le nombre de jours d'absence prévu au titre de ces congés ne dépasse pas 2 % du nombre total des jours de travail effectués dans les douze mois précédant le départ en congé. Pour permettre le départ en congé d'un salarié, cette période de douze mois est prolongée dans la limite de quarante-huit mois.
>
> Ces seuils ne permettent de différer que le congé sabbatique. Ils ne peuvent fonder aucun report du congé ou de la période de travail à temps partiel pour création ou reprise d'entreprise. Les reports décidés avant l'entrée en vigueur de la loi abrogeant l'article L. 3142-114 restent régis par les dispositions alors applicables.

*Justification :* reprendre à droit constant, pour le seul sabbatique, le mécanisme existant que les motifs de L3142-28, L3142-29, L3142-32 et D3142-21 entendent conserver. Le congé pour création reste libéré de tout report, comme le veulent L3142-114, L3142-115 et D3142-75. Aucune contrainte nouvelle par rapport au droit actuel. *Dépendances :* motif de L3142-114 à corriger (« sans effacer les règles distinctes du sabbatique » devient vrai) ; L3142-117 (« report imposé sur les fondements abrogés ») reste compatible.

**Option B.** Étendre la suppression au sabbatique : le deuxième alinéa de L3142-29 se limite au refus du 1° de L3142-113 ; le 4° de L3142-32 vise « les plafonds mentionnés au premier alinéa de l'article L. 3142-29 » ; D3142-21 est abrogé avec transition pour les reports déjà décidés ; les motifs contraires de L3142-28, L3142-29, L3142-32 et D3142-21 sont corrigés.

### 5.4 Revitalisation et RCC (objection 04) : alinéa à ajouter à D1233-37

> Pour les accords collectifs portant rupture conventionnelle collective conclus à compter de l'entrée en vigueur de la loi abrogeant les articles L. 1237-19-9 à L. 1237-19-12 et L. 1237-19-14, les dispositions de la présente sous-section ne s'appliquent pas en tant qu'elles concernent la rupture conventionnelle collective. Aucune indication d'assujettissement, aucune convention, étude d'impact, contribution, aucun titre de perception, aucune convention-cadre ni mesure de suivi ne peut être fondée sur elles. Elles demeurent applicables aux accords conclus avant cette date, y compris pour leur exécution, leurs conventions et le recouvrement des contributions dues. Les obligations de revitalisation propres aux licenciements collectifs pour motif économique et la participation volontaire prévue à l'article L. 1237-19-13 ne sont pas modifiées.

*Dépendances :* D1233-38 II, qui vise « les deux procédures », reste compatible pour les licenciements et les RCC antérieures ; il faut vérifier que la sous-section couvre bien D1233-37 à D1233-48-3.

### 5.5 R5429-3 (objection 05) : alinéa à ajouter (option b)

> Le premier alinéa ne s'applique qu'aux mises en demeure adressées en application de l'article D. 5424-43 au titre d'échéances de paiement ou de déclaration antérieures à l'entrée en vigueur de la loi abrogeant l'article L. 5424-17. Aucune contravention ne peut être fondée sur le présent article au titre des échéances postérieures. Les cotisations et les intérêts légalement dus restent exigibles.

*Option a, à choisir par l'auteur :* rédiger dans R5429-3 un élément constitutif autonome (mise en demeure de la caisse d'effectuer le versement ou la déclaration, sans majoration).

### 5.6 L6351-3 (objection 06)

- Remplacer le 3° par : « 3° Abrogé ; » (sans renumérotation).
- Ajouter au dernier alinéa : « L'absence de mention de l'activité de formation en apprentissage dans l'objet des statuts ne peut fonder un refus à compter de l'entrée en vigueur de la loi abrogeant l'article L. 6231-5, y compris pour les déclarations en cours d'examen. »

### 5.7 Commission CEP (objection 07) : option « maintien facultatif »

- **L6323-17-5-1, 4°** : « 4° Participer, le cas échéant, à l'animation de la commission chargée du conseil en évolution professionnelle lorsque France compétences la maintient en qualité de commission spécialisée. »
- **R6123-8, I, 20°** : « 20° Le règlement du conseil d'administration, les règlements intérieurs de la commission en charge de la certification professionnelle prévue à l'article L. 6113-6 et, lorsqu'elle est maintenue en application du 21° du présent I, de la commission chargée du conseil en évolution professionnelle, et la charte déontologique applicable aux membres du conseil d'administration, de ces commissions et des commissions spécialisées mentionnées au 21° du présent I, ainsi qu'au personnel de l'établissement ; »
- **R6123-21, premier alinéa** : « Les membres du conseil d'administration, de la commission mentionnée à l'article L. 6113-6, de la commission chargée du conseil en évolution professionnelle lorsqu'elle est maintenue et des commissions spécialisées créées au sein de France compétences, ainsi que les agents de France compétences exercent leurs fonctions dans le respect de principes fixés dans une charte déontologique, préparée par le directeur général et adoptée par le conseil d'administration. »

*Dépendance :* même correction à porter dans les versions futures de L6323-17-5-1 (2027 et 2028), via le paquet FUT-TRAV-LOG. *Option de disparition :* supprimer ces trois mentions.

### 5.8 R5312-42 (objection 08) : 1° c) proposé

> c) Les données de la déclaration sociale nominative nécessaires à l'édition de l'attestation d'employeur mentionnée à l'article R. 1234-9, au recouvrement des contributions des employeurs, à la proposition du contrat de sécurisation professionnelle, au développement d'une expertise sur l'évolution des emplois, des parcours professionnels et des compétences et à l'évaluation des résultats des actions d'accompagnement. Les données antérieurement enregistrées pour l'édition du relevé de mission de travail temporaire prévu par l'article L. 1251-46 dans sa rédaction antérieure à son abrogation ne sont conservées que pour l'examen des droits, réclamations et contentieux relatifs aux périodes antérieures, dans la limite des durées de conservation applicables ; aucune donnée nouvelle n'est enregistrée à cette fin ;

### 5.9 Groupements d'employeurs (objection 09)

- **R1255-9, premier alinéa** : « Le fait, pour la personne mentionnée à l'article D. 1253-2, de transmettre des informations inexactes est puni de l'amende prévue pour les contraventions de la deuxième classe. La suppression du renvoi au dernier alinéa de l'article D. 1253-4 s'applique à compter de l'abrogation de cet article, sous réserve de l'application de la loi pénale plus douce aux faits antérieurs. » Le reste de la proposition est inchangé.
- **R1253-44** : « La compétence de l'autorité administrative pour l'information prévue à l'article D. 1253-1 est appréciée en fonction des activités des seuls adhérents de droit privé. Il en va de même pour les déclarations adressées en application des articles D. 1253-4 et D. 1253-6 avant leur abrogation. »

### 5.10 Mobilité outre-mer (objection 10)

- **R5522-59** : « Pour l'élaboration de son projet en vue de réaliser une formation en mobilité, le demandeur bénéficie du concours, le cas échéant, d'un organisme public ou privé remplissant les conditions de capacité prévues à l'article R. 5522-80. »
- **R5522-60, 2°** : « 2° Pour la formation en mobilité, par le délégué régional de l'Agence nationale pour l'insertion et la promotion des travailleurs d'outre-mer ou par le directeur régional de l'opérateur France Travail ou son représentant ou par le responsable d'un organisme intervenant au titre de l'aide à la formation en mobilité dans les conditions prévues à l'article R. 5522-80. »

*Réserve :* l'instruction d'un dossier d'aide est une mission publique déléguée. Le rattachement à la convention de gestion de R5522-77, qui existe déjà, est une variante prudente à arbitrer.

### 5.11 L3134-16 (objection 11) : alinéa à ajouter

> Le présent article ne s'applique qu'aux journées de solidarité fixées et accomplies au titre de périodes antérieures à l'entrée en vigueur de la loi supprimant la journée supplémentaire de travail non rémunérée au titre de la solidarité. Il ne permet de fixer aucune journée nouvelle.

Le motif doit être corrigé : la journée est supprimée par L3133-7 proposé. Le nettoyage de L3422-1 est facultatif.

### 5.12 R3262-46 (objection 12) : article complet proposé

> Le fait de méconnaître les dispositions du premier et du troisième alinéa de l'article L. 3262-2, de l'article L. 3262-3 et du second alinéa de l'article L. 3262-5, est puni de l'amende prévue pour les contraventions de la quatrième classe.
>
> Il en est de même des infractions aux dispositions des articles R. 3262-1, R. 3262-2, R. 3262-4 à R. 3262-7, R. 3262-10, R. 3262-11, R. 3262-16, R. 3262-21 à R. 3262-25, R. 3262-33 à R. 3262-35 et R. 3262-37 à R. 3262-39, ainsi que des entraves mises à l'exercice de la mission de contrôle impartie à la commission prévue à l'article R. 3262-36.
>
> La suppression des renvois aux articles R. 3262-8, R. 3262-9, R. 3262-17 et R. 3262-20 s'applique à compter de l'entrée en vigueur du présent texte, sous réserve de l'application de la loi pénale plus douce aux faits antérieurs.

### 5.13 R3324-22, 10° (objection 13)

> 10° L'activité de proche aidant exercée par l'intéressé, son conjoint ou son partenaire lié par un pacte civil de solidarité auprès d'un proche tel que défini à l'article L. 3142-16 du code du travail ; la condition de résidence de la personne aidée antérieurement prévue à l'article L. 3142-17 du même code n'est pas exigée pour les demandes présentées à compter de l'abrogation de cet article ;

Même correction à porter dans la version applicable à partir du 1er janvier 2029 (LEGIARTI000052845711), via le paquet FUT-TRAV-LOG.

### 5.14 R5523-15-43 (objection 14) : introduction proposée

> Pour l'application des articles R. 5132-2, R. 5132-10-6, R. 5132-11, R. 5132-27, D. 5132-30, D. 5132-34, R. 5132-47, D. 6211-3 et R. 6223-7, ainsi que, pour les seules dérogations accordées avant son abrogation, de l'article D. 5132-18-1 :

---

## 6. Incertitudes et éléments non examinés

- **Choix de fond à arbitrer par l'auteur** : objection 03 (options A ou B), objection 05 (option a ou b), objection 07 (maintien ou disparition de la commission CEP).
- **Versions futures.** L6323-17-5-1 (2027, 2028), R3324-22 (2029) et L412-8 CSS (version ABROGE_DIFF jusqu'en 2029) ont des versions futures hors inventaire. Celles du code du travail relèvent du paquet FUT-TRAV-LOG. L412-8 CSS n'y figure pas : point à signaler au coordinateur, non instruit ici.
- **Non lus en entier** : l'annexe (1) à A931-11-17 et l'annexe I à R434-32 (5) CSS (occurrences seulement), D1233-41, D1233-42 et D1233-45 à D1233-48-3, D3142-68 et D3142-76, D1253-3 et D1253-5, R6351-5, R2523-17, L2412-3 à L2412-13, L2421-8-1, L1226-4-3, ainsi que les articles visés par R5523-15-43 autres que D5132-18-1.
- **Pièces externes non fournies** : arrêtés SI-CIP, arrêté du modèle de R1251-8, accords de branche sur L3142-32 et L6331-69, conventions internationales de L6235-2. Aucune consultation de Légifrance, d'EUR-Lex ou de la CNIL n'a été faite ; les références au RGPD et à la directive 2014/67/UE sont citées de mémoire.
- **Observations hors du paquet, non qualifiées.** L1 (concertation préalable) et L3 (présentations annuelles) sont abrogés. Leurs alertes sont des faux positifs, mais l'articulation avec les conventions OIT n° 122 et n° 144, que les notes de L1 signalent elles-mêmes, n'a pas été examinée.
- **Instantané figé** : les propositions peuvent avoir changé en production depuis le 26 octobre 2026 ; vérifier les empreintes du JSON avant toute correction.
