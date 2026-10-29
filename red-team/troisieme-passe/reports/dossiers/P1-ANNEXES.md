# Dossier P1-ANNEXES : renvois vers des abrogations proposées dans les annexes I à IV du CGI

Red-team juridique indépendante, troisième passe. Instantané `snapshots/20261026T230545Z`, corpus arrêté au **18 octobre 2026**. Rapport établi le 26 octobre 2026. Paquet `reports/p1-work/P1-ANNEXES.json` : 67 clusters, 137 alertes.

Ce rapport est une revue faite par une IA. Il ne vaut pas validation par un juriste. La seconde passe continue : les propositions citées peuvent encore changer, et les conclusions sont donc provisoires.

## 1. Résumé

- **137 alertes qualifiées**, toutes lues en entier : 67 `alerte écartée`, 2 `faux positif`, 45 `incohérence du projet`, 16 `coordination manquante`, 3 `simple alerte`, 4 `couvert par dossier`. Les dossiers concernés sont annexe I 165/185/186 (3 alertes) et RT-INUT pour annexe II 289 (1 alerte).
- **14 objections** : 5 en P1, toutes confirmées, et 9 en P2, dont 8 confirmées et 1 à confirmer. Une objection correspond à un effet juridique : les 64 alertes retenues (hors alertes écartées, faux positifs et `couvert par dossier`) se regroupent en 12 objections. Deux objections supplémentaires, 05 et 14, ne correspondent à aucune alerte du paquet.
- **Les plus importantes :**
  1. **RT-P1-ANNEXES-01 et 02 (P1), facturation électronique.** Le projet abroge les six articles d'exécution des flux fiscaux de données (annexe II 242 nonies J, L, M, N, O, P), en conséquence de l'abrogation proposée de CGI 289 E, 290 et 290 A. Mais 242 nonies E et G de l'annexe II ainsi que 41 septies J, K, L, N et O de l'annexe IV restent inchangés et imposent encore ces flux (coordination manquante). Les propositions réécrites 41 septies A, D, G, H, M et P, ainsi que 242 nonies B, organisent toujours délais, audits, statut transmis et données « transmises à l'administration » (incohérence du projet). Les cibles listent elles-mêmes ces coordinations comme « encore requises ».
  2. **RT-P1-ANNEXES-03 et 04 (P1), organismes de gestion agréés et viseurs fiscaux.** La convention de viseur (371 bis B, C, C bis) est abrogée, mais 371 bis F, H, K et M continuent de l'organiser. K renvoie même une nouvelle demande « à la procédure prévue aux articles 371 bis B et 371 bis C ». Les interdictions biennales (371 K bis, V bis, Z terdecies) sont abrogées, mais 371 F 11° affirme que « ces interdictions demeurent applicables » et 371 R et Z octies exigent encore une attestation sur K bis. Par ailleurs, la base légale de ces régimes (CGI 1649 quater C à M) est **abrogée depuis le 16 février 2025** dans l'instantané (loi n° 2025-127, art. 11). C'est une réserve : RT-P1-ANNEXES-05.
  3. **RT-P1-ANNEXES-06 (P1), fonds FCPR et FCPI.** 41 duovicies G (relevé annuel) et 41 sexdecies A (déclaration d'existence) sont abrogés, alors que 41 Y dispose que les renseignements « restent portés sur le relevé prévu à l'article 41 duovicies G » et que 46 AI ter soumet encore le gérant aux obligations de A et de G.

## 2. Périmètre réellement lu

Tous les articles du tableau ont été exportés par `tools/cite.py`, version par version : source entière, NOTA, bornes, état, proposition entière, motif, notes de revue, lot propriétaire et inventaire. Les fichiers sont dans `evidence/cited/20261026T230545Z/`. J'ai lu en entier la proposition de chaque cible, puis le texte courant de chaque article qui y renvoie : la proposition s'il est en `rewrite_draft`, la source s'il est en `retained_unchanged`.

| Rôle | Code | Article | Version (LEGIARTI) | Bornes | Statut proposition | Seconde passe | Source sha256 | Proposition sha256 |
|---|---|---|---|---|---|---|---|---|
| cible | a1 | 165 | LEGIARTI000032881253 | 2016-07-10 → 2999-01-01 | rewrite_draft | completed | 04708941f2… | 6d4be25d50… |
| cible | a1 | 181 | LEGIARTI000006293591 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | bd476b6053… | 72fc6d4943… |
| cible | a1 | 65 | LEGIARTI000006293307 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | d798a098c2… | 82931e9caf… |
| cible | a1 | 81 | LEGIARTI000006293553 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | 36a8ca9882… | 9225dde235… |
| cible | a1 | 85 | LEGIARTI000006293556 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | 46b0181b84… | 5b42ad563d… |
| cible | a2 | 142 | LEGIARTI000037094692 | 2018-06-23 → 2999-01-01 | rewrite_draft | completed | 43260fdda1… | ca1f473ac6… |
| cible | a2 | 143 | LEGIARTI000054363256 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | 6ed46b508f… | 2c4fa13274… |
| cible | a2 | 16 F | LEGIARTI000047658134 | 2023-06-10 → 2999-01-01 | rewrite_draft | completed | 4051567c2f… | 2c402cfb19… |
| cible | a2 | 242 nonies J | LEGIARTI000046385773 | 2022-10-10 → 2999-01-01 | rewrite_draft | completed | 13724f4d19… | fc748cdd6f… |
| cible | a2 | 242 nonies L | LEGIARTI000054552554 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | a77072b3bb… | e9ab2c80de… |
| cible | a2 | 242 nonies M | LEGIARTI000054552557 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 7cbf1d770f… | dddfb21bad… |
| cible | a2 | 242 nonies N | LEGIARTI000054552564 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 5d63afe29d… | 9f3abbbf1c… |
| cible | a2 | 242 nonies O | LEGIARTI000054552567 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | f0db9c507f… | 7cf0523760… |
| cible | a2 | 242 nonies P | LEGIARTI000054552572 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | f338b10cea… | ae441f9df4… |
| cible | a2 | 242-0 J | LEGIARTI000043663232 | 2021-06-12 → 2999-01-01 | rewrite_draft | completed | 99f514e5f4… | 861f0f2ea0… |
| cible | a2 | 286 O | LEGIARTI000030256212 | 2015-04-01 → 2999-01-01 | rewrite_draft | completed | cd01374db3… | 58edf9c16e… |
| cible | a2 | 297 | LEGIARTI000006294773 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 1cdec896aa… | 36a25d6c67… |
| cible | a2 | 311 A | LEGIARTI000006294877 | 1991-03-22 → 2999-01-01 | rewrite_draft | completed | 79d33a75eb… | 8c3fd5a17c… |
| cible | a2 | 311 C | LEGIARTI000025622306 | 2012-04-01 → 2999-01-01 | rewrite_draft | completed | fda2ab433b… | b438e871bc… |
| cible | a2 | 333 B | LEGIARTI000006294947 | 1987-08-10 → 2999-01-01 | rewrite_draft | completed | a761cdc4ba… | 6bc8fefb9a… |
| cible | a2 | 333 H | LEGIARTI000053387833 | 2026-01-01 → 2999-01-01 | rewrite_draft | completed | 4d90bf3dab… | 78cc8a7d9b… |
| cible | a2 | 371 B | LEGIARTI000033238661 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | 5adbe39fb0… | 5f7fd866b2… |
| cible | a2 | 371 K bis | LEGIARTI000033228679 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 86c2e6c51b… | 9ca3baaa71… |
| cible | a2 | 371 N | LEGIARTI000033238577 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | cd78dc164c… | 850df9cb60… |
| cible | a2 | 371 V bis | LEGIARTI000033228882 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 045e26a792… | 72bf8a2153… |
| cible | a2 | 371 Z terdecies | LEGIARTI000033238683 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | dd56dbb22b… | b2df0823ac… |
| cible | a2 | 371 bis B | LEGIARTI000033238757 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | d280195e18… | a9e68f215b… |
| cible | a2 | 371 bis C | LEGIARTI000022006332 | 2010-03-22 → 2999-01-01 | rewrite_draft | completed | 025c84cf1d… | 1f8b32b085… |
| cible | a2 | 371 bis C bis | LEGIARTI000033230802 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | edef57127e… | 9695a5dc99… |
| cible | a3 | 10 septies | LEGIARTI000006297595 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 1bc4dfff1c… | c2776ba912… |
| cible | a3 | 111 J | LEGIARTI000006298872 | 1999-03-31 → 2999-01-01 | rewrite_draft | completed | d7ea0ad975… | 3b21ae2197… |
| cible | a3 | 143 A | LEGIARTI000006299563 | 1987-08-01 → 2999-01-01 | rewrite_draft | completed | 57e3266713… | e80280db2b… |
| cible | a3 | 143 H | LEGIARTI000006298911 | 2002-03-31 → 2999-01-01 | rewrite_draft | completed | c5f744c166… | fb288e5314… |
| cible | a3 | 143 Z | LEGIARTI000006297028 | 1993-01-05 → 2999-01-01 | rewrite_draft | completed | b67c6be554… | 0fdbe79d09… |
| cible | a3 | 2 tervicies | LEGIARTI000037100856 | 2018-06-23 → 2999-01-01 | rewrite_draft | completed | c65c55ebdc… | 9ba1a6af76… |
| cible | a3 | 209-0 A | LEGIARTI000006299128 | 2006-07-23 → 2999-01-01 | rewrite_draft | completed | 07f6f37508… | 8df8333eba… |
| cible | a3 | 344 GA | LEGIARTI000006299501 | 1982-09-01 → 2999-01-01 | rewrite_draft | completed | e1c3cd8019… | 69cfed1063… |
| cible | a3 | 381 bis | LEGIARTI000025625204 | 2012-04-01 → 2999-01-01 | rewrite_draft | completed | b3e7e394df… | 4701c46e74… |
| cible | a3 | 385 | LEGIARTI000006299702 | 2006-01-01 → 2999-01-01 | rewrite_draft | completed | 7b80ef3af9… | 90c8ea620f… |
| cible | a3 | 387 | LEGIARTI000006299703 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | d8a4cbfde4… | ec76897e2c… |
| cible | a3 | 388 | LEGIARTI000006299706 | 2006-01-01 → 2999-01-01 | rewrite_draft | completed | dfcdec87ff… | 9b71acd668… |
| cible | a3 | 390 | LEGIARTI000006299711 | 2006-01-01 → 2999-01-01 | rewrite_draft | completed | 265266232b… | 768d83219c… |
| cible | a3 | 397 | LEGIARTI000048852299 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | 20fb9d240f… | 8bee94be1e… |
| cible | a3 | 404 A | LEGIARTI000048852254 | 2023-12-31 → 2999-01-01 | rewrite_draft | completed | 035e3e34d4… | 16e2766579… |
| cible | a3 | 41 J | LEGIARTI000047196869 | 2023-02-19 → 2999-01-01 | rewrite_draft | completed | c436111fc0… | 7b7d6c5356… |
| cible | a3 | 41 duodecies | LEGIARTI000006297787 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 18ffc1cd03… | a5454dd959… |
| cible | a3 | 41 duodecies P | LEGIARTI000006297803 | 1986-07-31 → 2999-01-01 | rewrite_draft | completed | 50b32a7ef1… | 4d64b01df4… |
| cible | a3 | 41 duovicies G | LEGIARTI000027799365 | 2013-07-31 → 2999-01-01 | rewrite_draft | completed | 5adbe6695a… | cec184363c… |
| cible | a3 | 41 sexdecies A | LEGIARTI000025624960 | 2012-04-01 → 2999-01-01 | rewrite_draft | completed | e9da223cef… | facc18a032… |
| cible | a3 | 46 B | LEGIARTI000006298161 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | b42b9aa284… | 92e88c1ef3… |
| cible | a3 | 46 quindecies Q | LEGIARTI000025625028 | 2012-04-01 → 2999-01-01 | rewrite_draft | completed | 544a009e89… | 71c0a230e3… |
| cible | a3 | 49 septies H | LEGIARTI000043682634 | 2021-06-21 → 2999-01-01 | rewrite_draft | completed | 43cadf68eb… | 716da4adb1… |
| cible | a3 | 49 septies ZZJ | LEGIARTI000029728940 | 2014-11-06 → 2999-01-01 | rewrite_draft | completed | 23b36f79f5… | 204b55a3ff… |
| cible | a3 | 53 bis | LEGIARTI000022343100 | 2010-05-08 → 2999-01-01 | rewrite_draft | completed | 1c885984ad… | 3b04e9c982… |
| cible | a3 | 53 ter | LEGIARTI000006298626 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | d6f51be280… | 8d50f0ccf2… |
| cible | a4 | 124 | LEGIARTI000006300874 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 7bf3625ff4… | 1db2ac8c5b… |
| cible | a4 | 137 | LEGIARTI000006301660 | 1996-05-12 → 2999-01-01 | rewrite_draft | completed | 18095885fa… | a420017331… |
| cible | a4 | 164 F octovicies | LEGIARTI000006301051 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 4b6a171583… | 5c24c02e4d… |
| cible | a4 | 164 F quatervicies | LEGIARTI000006301047 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | b4fe0ddc42… | 3bdae00489… |
| cible | a4 | 188 F | LEGIARTI000006301966 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 22172778da… | 7744a1776d… |
| cible | a4 | 23 A | LEGIARTI000006301277 | 1985-07-15 → 2999-01-01 | rewrite_draft | completed | a7344134a3… | 052b0cfed4… |
| cible | a4 | 23 B | LEGIARTI000006301279 | 1985-07-15 → 2999-01-01 | rewrite_draft | completed | 0af466101a… | 052b0cfed4… |
| cible | a4 | 4 J | LEGIARTI000051113363 | 2025-02-02 → 2999-01-01 | rewrite_draft | completed | 364cbd36ef… | 6fc1a00eec… |
| cible | a4 | 50 C | LEGIARTI000006300456 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 84c47ffe93… | 832fd0c3f7… |
| cible | a4 | 54-0 E | LEGIARTI000024378326 | 2011-07-21 → 2999-01-01 | rewrite_draft | completed | d664b6056a… | d3d5aee632… |
| cible | a4 | 56 AO | LEGIARTI000006300615 | 2000-03-31 → 2999-01-01 | rewrite_draft | completed | b8333a77f9… | e5e87cede9… |
| renvoi | a1 | 185 | LEGIARTI000006293344 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | d5c8b0401f… | 5d4a6c1957… |
| renvoi | a1 | 186 | LEGIARTI000032881225 | 2016-07-10 → 2999-01-01 | rewrite_draft | completed | 72ac8ce09a… | eef280bd11… |
| renvoi | a2 | 135 | LEGIARTI000006295285 | 1980-01-19 → 2999-01-01 | rewrite_draft | completed | 671c6055f5… | bfa771e91c… |
| renvoi | a2 | 208 | LEGIARTI000043663240 | 2021-06-12 → 2999-01-01 | retained_unchanged | completed | 96d0ce9820… | — |
| renvoi | a2 | 242 nonies E | LEGIARTI000054552509 | 2026-07-29 → 2999-01-01 | retained_unchanged | completed | 39dc07f05b… | — |
| renvoi | a2 | 242 nonies G | LEGIARTI000054552526 | 2026-07-29 → 2999-01-01 | retained_unchanged | completed | e82d8babbd… | — |
| renvoi | a2 | 286 J | LEGIARTI000038668387 | 2019-06-08 → 2999-01-01 | rewrite_draft | completed | 5b7608affa… | 28dae7e258… |
| renvoi | a2 | 286 W | LEGIARTI000030256234 | 2015-04-01 → 2999-01-01 | rewrite_draft | completed | 6551f4d723… | b1dfe2c633… |
| renvoi | a2 | 289 | LEGIARTI000054363092 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | 16e8bada90… | 6fac3dcbd3… |
| renvoi | a2 | 295 | LEGIARTI000006294771 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | cfe60e0720… | 36a25d6c67… |
| renvoi | a2 | 296 | LEGIARTI000006294772 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | d5a8a37008… | 36a25d6c67… |
| renvoi | a2 | 301 | LEGIARTI000020519371 | 2009-04-10 → 2999-01-01 | retained_unchanged | completed | dd5f93ecf0… | — |
| renvoi | a2 | 317 octies | LEGIARTI000054363280 | 2026-07-01 → 2999-01-01 | rewrite_draft | completed | 4a5061ae6c… | 5b927c2af9… |
| renvoi | a2 | 333 A | LEGIARTI000043663405 | 2021-06-12 → 2999-01-01 | retained_unchanged | completed | c295dd9b48… | — |
| renvoi | a2 | 371 D | LEGIARTI000033238650 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 7e44cb83dd… | 9cd7d39a19… |
| renvoi | a2 | 371 F | LEGIARTI000033238629 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | e7cba0f739… | 49a0b84190… |
| renvoi | a2 | 371 P | LEGIARTI000006295066 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 75655cd229… | d2892ce492… |
| renvoi | a2 | 371 R | LEGIARTI000033238552 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 8ee2e2b3d8… | 4113c20653… |
| renvoi | a2 | 371 Y | LEGIARTI000033238525 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 56a077bb3c… | 24c9fab91e… |
| renvoi | a2 | 371 Z octies | LEGIARTI000033238693 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | aeb1585e26… | 8ba972ad38… |
| renvoi | a2 | 371 Z quinquies | LEGIARTI000033238701 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 89767ab173… | 4c12fbbcd4… |
| renvoi | a2 | 371 Z ter | LEGIARTI000033238706 | 2019-01-01 → 2999-01-01 | rewrite_draft | completed | b95e92b774… | 0d909acc5b… |
| renvoi | a2 | 371 bis F | LEGIARTI000033238749 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | a17729e42a… | d1670a5ce4… |
| renvoi | a2 | 371 bis H | LEGIARTI000033238730 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | aa4c7185bb… | 9599b4d8b2… |
| renvoi | a2 | 371 bis I | LEGIARTI000022006313 | 2010-03-22 → 2999-01-01 | rewrite_draft | completed | fd6bb4dda7… | e8d1aa0a02… |
| renvoi | a2 | 371 bis K | LEGIARTI000033238721 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 84323c7718… | c049784e0c… |
| renvoi | a2 | 371 bis M | LEGIARTI000033230872 | 2016-10-14 → 2999-01-01 | rewrite_draft | completed | 28f1716da8… | e1a618ce41… |
| renvoi | a2 | 383 | LEGIARTI000022179520 | 2010-05-01 → 2999-01-01 | rewrite_draft | completed | c4159be3fb… | a758b7fd0d… |
| renvoi | a3 | 111 N | LEGIARTI000006298877 | 1999-03-31 → 2999-01-01 | rewrite_draft | completed | 544ce472fc… | 0028df2632… |
| renvoi | a3 | 143 A 1 | LEGIARTI000006298908 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | b960fd12d5… | 6a962d3299… |
| renvoi | a3 | 2 duovicies | LEGIARTI000006297564 | 2006-09-29 → 2999-01-01 | rewrite_draft | completed | 2d18e3ccd4… | 5966ea7f9b… |
| renvoi | a3 | 3 | LEGIARTI000006296502 | 1987-07-24 → 2999-01-01 | rewrite_draft | completed | 66c63f3fd2… | 750a6ca866… |
| renvoi | a3 | 324 K | LEGIARTI000037128030 | 2018-06-30 → 2999-01-01 | rewrite_draft | completed | 87a19db75f… | a7fc548643… |
| renvoi | a3 | 344 GB | LEGIARTI000006299502 | 1982-09-01 → 2999-01-01 | rewrite_draft | completed | 2a2438f1c2… | 4f25a3af9f… |
| renvoi | a3 | 381 K | LEGIARTI000038668514 | 2019-06-08 → 2999-01-01 | rewrite_draft | completed | aae7a9b491… | fe1a7fd923… |
| renvoi | a3 | 381 ter | LEGIARTI000006299637 | 2005-01-01 → 2999-01-01 | rewrite_draft | completed | 9cc8291201… | a2fb386ec5… |
| renvoi | a3 | 398 | LEGIARTI000048852294 | 2023-12-31 → 2999-01-01 | retained_unchanged | completed | d5ee45fc33… | — |
| renvoi | a3 | 402 | LEGIARTI000006299882 | 1997-04-11 → 2999-01-01 | retained_unchanged | completed | fbc343ed4c… | — |
| renvoi | a3 | 41 X | LEGIARTI000027799345 | 2013-07-31 → 2999-01-01 | rewrite_draft | completed | 93b622dc7b… | 27e547a6e2… |
| renvoi | a3 | 41 Y | LEGIARTI000006297987 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | 24b8054ed7… | 4ed8ff8222… |
| renvoi | a3 | 41 sexdecies G | LEGIARTI000027799387 | 2013-07-31 → 2999-01-01 | rewrite_draft | completed | e60d04bbbd… | 160f8bcb68… |
| renvoi | a3 | 46 AI ter | LEGIARTI000050743550 | 2024-12-06 → 2999-01-01 | rewrite_draft | completed | 5cc06fd66f… | 4b6c052058… |
| renvoi | a3 | 46 quater-0 A | LEGIARTI000006298179 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | e0396d0a17… | 93364f5c61… |
| renvoi | a3 | 46 quindecies O | LEGIARTI000052040030 | 2025-08-04 → 2999-01-01 | rewrite_draft | completed | a701b96c8a… | 09e0d39d87… |
| renvoi | a3 | 49 septies ZZK | LEGIARTI000029728931 | 2014-11-06 → 2999-01-01 | rewrite_draft | completed | 051d8696d0… | 152e822f96… |
| renvoi | a3 | 53 quater | LEGIARTI000006298627 | 1979-07-01 → 2999-01-01 | retained_unchanged | completed | 03d3d1d75c… | — |
| renvoi | a4 | 13 | LEGIARTI000006300256 | 2005-01-01 → 2999-01-01 | rewrite_draft | completed | 92285dc3f5… | 67daf97db8… |
| renvoi | a4 | 146 | LEGIARTI000006301676 | 1993-01-05 → 2999-01-01 | rewrite_draft | completed | 24583b9dd7… | f83b5e23df… |
| renvoi | a4 | 164 F quinvicies | LEGIARTI000006301048 | 1979-07-01 → 2999-01-01 | rewrite_draft | completed | 7d09435811… | e3d3c8154c… |
| renvoi | a4 | 23 L duodecies | LEGIARTI000043681810 | 2021-06-21 → 2999-01-01 | rewrite_draft | completed | 9cb47a3983… | 34bcfd8f7a… |
| renvoi | a4 | 4 L | LEGIARTI000006301198 | 1987-02-17 → 2999-01-01 | rewrite_draft | completed | 5874a64572… | 22262b384c… |
| renvoi | a4 | 41 septies A | LEGIARTI000054606058 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 4d4c52d504… | 2ba4c456e3… |
| renvoi | a4 | 41 septies D | LEGIARTI000054606114 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 2b0e399cfb… | f5176d7e02… |
| renvoi | a4 | 41 septies G | LEGIARTI000054606169 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 48d50498be… | 7cd9a96289… |
| renvoi | a4 | 41 septies H | LEGIARTI000054606182 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | d7f12de38d… | c97209ce28… |
| renvoi | a4 | 41 septies J | LEGIARTI000046386257 | 2022-10-10 → 2999-01-01 | retained_unchanged | completed | 005a424808… | — |
| renvoi | a4 | 41 septies K | LEGIARTI000054606200 | 2026-07-29 → 2999-01-01 | retained_unchanged | completed | cf5c5fdf9d… | — |
| renvoi | a4 | 41 septies L | LEGIARTI000054606212 | 2026-07-29 → 2999-01-01 | retained_unchanged | completed | d7b32a69ba… | — |
| renvoi | a4 | 41 septies M | LEGIARTI000054606222 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | 0edf03ffb9… | 71bfdb02fd… |
| renvoi | a4 | 41 septies N | LEGIARTI000046386265 | 2022-10-10 → 2999-01-01 | retained_unchanged | completed | 92fa6b10e6… | — |
| renvoi | a4 | 41 septies O | LEGIARTI000046386267 | 2022-10-10 → 2999-01-01 | retained_unchanged | completed | 2275573b55… | — |
| renvoi | a4 | 41 septies P | LEGIARTI000054606241 | 2026-07-29 → 2999-01-01 | rewrite_draft | completed | a293766a1a… | 4dc4598223… |
| renvoi | a4 | 50-0 BA | LEGIARTI000030625671 | 2015-05-25 → 2999-01-01 | rewrite_draft | completed | aeab93fd1a… | 90518f766b… |
| renvoi | a4 | 50-0 E | LEGIARTI000006300450 | 2001-03-31 → 2999-01-01 | rewrite_draft | completed | 0545ec4053… | 97df487ce4… |
| renvoi | a4 | 54-0 BX | LEGIARTI000006300563 | 2001-03-31 → 2999-01-01 | retained_unchanged | completed | 5844f33ac9… | — |
| renvoi | a4 | 56 AP | LEGIARTI000006300618 | 2007-08-09 → 2999-01-01 | retained_unchanged | completed | 627b1d6dab… | — |
| renvoi | a4 | 56 J vicies | LEGIARTI000006300595 | 2006-01-21 → 2999-01-01 | rewrite_draft | completed | 7246c206d4… | 101d20cd70… |
| renvoi | cch | R121-11 | LEGIARTI000043818381 | 2021-07-01 → 2999-01-01 | retained_unchanged | completed | 616b7c969f… | — |
| renvoi | cgi | 119 | LEGIARTI000006307270 | 1983-01-04 → 2999-01-01 | rewrite_draft | completed | 320d128487… | 4b9786ec9e… |
| renvoi | cgi | 124 E | LEGIARTI000006302672 | 1985-12-15 → 2999-01-01 | rewrite_draft | completed | edd7c5fcdb… | ea3d7d88a0… |
| renvoi | cgi | 1678 bis | LEGIARTI000026949201 | 2013-01-01 → 2999-01-01 | retained_unchanged | pending | 1219c14085… | — |
| renvoi | cgi | 172 bis | LEGIARTI000006308236 | 1984-07-25 → 2999-01-01 | retained_unchanged | completed | eda760767a… | — |
| renvoi | cgi | 39 quinquies GA | LEGIARTI000006302347 | 1991-06-24 → 2999-01-01 | rewrite_draft | completed | b524cbdb15… | f987cb9dd4… |
| renvoi | cgi | 90 | LEGIARTI000006314115 | 1987-08-10 → 2999-01-01 | rewrite_draft | completed | e02785ea95… | 3e35e05516… |
| renvoi | css | R931-1-29 | LEGIARTI000045387199 | 2022-03-20 → 2999-01-01 | rewrite_draft | pending | ccdb983c9e… | 1ba6ec57aa… |

Pièces complémentaires lues en entier (hors alertes), parce qu'elles conditionnent la qualification :

- CGI 244 quater B, LEGIARTI000053544409, proposition (II d bis, i, k 6°) ;
- annexe II 242 nonies B, LEGIARTI000054552495, proposition (I 6° et 7°) ;
- annexe III 41 duovicies F, LEGIARTI000027799370 (maintenu) ;
- CSS R931-3-59 et R931-3-60, propositions ;
- versions de CGI 1649 quater C, L et M (abrogées au 2025-02-16), CGI 1559 et 1565 (abrogés au 2025-01-01), CGI 527 (abrogé au 2019-01-01), CGI 306 (abrogé au 2025-07-01) et CGI 90 (versions de 1950 et de 1987) ;
- annexe III 369 et 374, toutes versions ;
- la recherche des numéros 370 à 373 de l'annexe III : 370 est abrogé depuis 2004, et 371, 372 et 373 n'existent pas.

Orientations consultées : `policy-coordinations.json` (fiscalite, editorial_direction_2026_10_19, formalites_accises_et_cidre, preserved_benefits_2026_10_19, cuts_and_reliefs_2026_10_19, is_distribution, successions, taxe_sur_les_salaires_removal et suivantes) et `notes-contradictions/INDEX.md`.

Sources publiques : une consultation de Légifrance (JORFARTI de la loi n° 2025-127) a été tentée le 2026-10-26 et a reçu une réponse HTTP 403. Elle n'a pas été contournée. Aucune autre source externe n'a été utilisée.

## 3. Méthode

1. Pour chaque cluster, j'ai lu la proposition d'abrogation de la cible et relevé ses clauses de transition et de neutralisation des renvois. Exemples : 371 V bis (« Aucun renvoi au présent article ne peut imposer une telle interdiction ni une attestation de son absence ») ; 242 nonies J à P (« Les calendriers et textes d'application du présent article ne peuvent rétablir ces obligations ») ; 39 quinquies GA (« l'article 16 F […] ne peut rétablir les transmissions supprimées »).
2. Pour chaque renvoi, j'ai vérifié l'identité de l'article visé (code, annexe, version). Deux erreurs de résolution ont été trouvées : CCH R121-11 vise le décret n° 2012-1246, et annexe II 135 vise l'annexe II, non l'annexe IV.
3. Chaque renvoi a ensuite reçu une seule qualification, selon la grille de l'addendum : contexte historique ou transitoire, plage neutre, renvoi neutralisé par la cible, article lui-même abrogé, maintien d'une règle vivante, ou appui actif d'une proposition.
4. Une seule objection a été rédigée par effet. Exemples : les sept textes maintenus de la facturation électronique forment RT-01 ; les six propositions réécrites forment RT-02.
5. Classement `couvert par dossier` : annexe I 165, 185 et 186 (ligne de l'INDEX, sans identifiant de dossier connu, d'où le libellé `ALCOOL-A1-165-185-186`) et annexe II 289 (RT-INUT, cité par le dossier MENS).
6. Fichier `reports/p1-work/P1-ANNEXES-classification.jsonl` : une ligne par `finding_id` (137 lignes), toutes avec `read_in_full: true`.

## 4. Constats

### 4.1 Objections

| ID | P | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-P1-ANNEXES-01 | P1 | coordination manquante | confirmé | Facturation électronique : 242 nonies E (1°, 6° c, 7°, 8°) et G de l'annexe II, 41 septies J, K, L, N et O de l'annexe IV, maintenus, appliquent encore les flux abrogés de J à P (16 alertes). |
| RT-P1-ANNEXES-02 | P1 | incohérence du projet | confirmé | Facturation électronique : 41 septies A (I 1° b, 4°, 5°, 7° c), D, G (I 4°, III), H, M et P proposés, ainsi que 242 nonies B I 7° c et d, s'appuient sur les flux abrogés. Les transitions se contredisent : « Les périodes antérieures conservent leurs échéances » contre la suppression des « transmissions restant à effectuer » (16 alertes). |
| RT-P1-ANNEXES-03 | P1 | incohérence du projet | confirmé | Viseurs fiscaux : 371 bis F, H, K et M organisent une convention abrogée par 371 bis B, C et C bis ; la base légale CGI 1649 quater L et M est abrogée depuis le 2025-02-16 (9 alertes). |
| RT-P1-ANNEXES-04 | P1 | incohérence du projet | confirmé | Interdictions biennales : 371 F 11° (« demeurent applicables »), 371 D, R 11°, Z octies 11° et Z quinquies contre l'abrogation de K bis et Z terdecies. Constat connexe : certificat de 371 D encore exigé par R 4° et Z octies 4° (6 alertes). |
| RT-P1-ANNEXES-05 | P2 | réserve documentaire | à confirmer | Base légale des régimes 371 A à 371 bis N : CGI 1649 quater C à M abrogés par la loi n° 2025-127, art. 11 ; portée de cet article non lue. |
| RT-P1-ANNEXES-06 | P1 | incohérence du projet | confirmé | Fonds : 41 X, 41 Y et 46 AI ter s'appuient sur 41 duovicies G et 41 sexdecies A, abrogés (6 alertes). |
| RT-P1-ANNEXES-07 | P2 | incohérence du projet | confirmé | 50-0 BA maintient le formulaire de la déclaration des comptoirs de vente, supprimée (286 O, 302 F ter 2°). |
| RT-P1-ANNEXES-08 | P2 | incohérence du projet | confirmé | 46 quater-0 A maintient pour les seuls organismes sans but lucratif la note de 41 J, abrogée. |
| RT-P1-ANNEXES-09 | P2 | incohérence du projet | confirmé | 23 L duodecies maintient les pièces d'un agrément CIR supprimé (49 septies H, 244 quater B d bis). |
| RT-P1-ANNEXES-10 | P2 | incohérence du projet | confirmé | 56 J vicies déroge à 209-0 A, abrogé, et vise la « déclaration de paiement » d'une contribution (CGI 527) abrogée depuis 2019. |
| RT-P1-ANNEXES-11 | P2 | incohérence du projet | confirmé | 146 exige « la déclaration visée à l'article 124 », abrogé ; CGI 1559 à 1566 sont abrogés depuis le 2025-01-01. |
| RT-P1-ANNEXES-12 | P2 | incohérence du projet | confirmé | 50-0 E identifie le bon de commande par 111 J, abrogé (imprécision rédactionnelle). |
| RT-P1-ANNEXES-13 | P2 | simple alerte | confirmé | CGI 90, note « Annexe III, art. 369 à 374 » : renvoi non nouveau, plage en partie inexistante et étrangère aux articles 79 à 89. |
| RT-P1-ANNEXES-14 | P2 | anomalie d'inventaire | confirmé | Sept notes de revue périmées ou inexactes (articles dits « absents du corpus » alors qu'ils y figurent, abrogés ; états antérieurs des cibles). |

Le détail de chaque objection figure dans `reports/dossiers/P1-ANNEXES.json` : passages, références, raisonnement, conséquences, corrections, éléments à préserver et incertitudes.

### 4.2 Qualification des alertes, cluster par cluster

| Cible (abrogée) | Renvoi | Type | Classification | Objection |
|---|---|---|---|---|
| 242 nonies P | 242 nonies E (a2) ×2 | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies P | 242 nonies G (a2) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies P | 41 septies N (a4) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies P | 41 septies O (a4) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies P | 41 septies A (a4) ×4 | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies P | 41 septies G (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies P | 41 septies P (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies M | 242 nonies E (a2) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies M | 242 nonies G (a2) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies M | 41 septies J (a4) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies M | 41 septies A (a4) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies M | 41 septies K (a4) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies M | 41 septies L (a4) ×2 | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies M | 41 septies M (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 371 bis B | 371 bis I (a2) | proposal | alerte écartée | — |
| 371 bis B | 371 bis C (a2) | proposal | alerte écartée | — |
| 371 bis B | 371 bis M (a2) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 371 bis B | 371 bis K (a2) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 371 bis B | 371 bis H (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 371 bis B | 371 bis F (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 371 K bis | 371 R (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| 371 K bis | 371 F (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| 371 K bis | 371 D (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| 371 K bis | 371 B (a2) | proposal | alerte écartée | — |
| 371 K bis | 371 Z octies (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| 371 K bis | 371 Z quinquies (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| (aucune : renvoi introduit) | 90 (cgi) ×3 | reference | simple alerte | RT-P1-ANNEXES-13 |
| (aucune : renvoi introduit) | R931-1-29 (css) ×2 | reference | alerte écartée | — |
| 371 V bis | 371 P (a2) | proposal | alerte écartée | — |
| 371 V bis | 371 F (a2) | proposal | alerte écartée | — |
| 371 V bis | 371 D (a2) | proposal | alerte écartée | — |
| 371 V bis | 371 Z octies (a2) | proposal | alerte écartée | — |
| 371 V bis | 371 Z quinquies (a2) | proposal | alerte écartée | — |
| 242 nonies J | 242 nonies E (a2) ×2 | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies J | 242 nonies G (a2) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies J | 41 septies A (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies J | 41 septies D (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 297 | 295 (a2) | proposal | alerte écartée | — |
| 297 | 296 (a2) | proposal | alerte écartée | — |
| 297 | 297 (a2) | proposal | alerte écartée | — |
| 297 | 301 (a2) | unrewritten | alerte écartée | — |
| 41 duovicies G | 41 Y (a3) | proposal | incohérence du projet | RT-P1-ANNEXES-06 |
| 41 duovicies G | 41 X (a3) | proposal | incohérence du projet | RT-P1-ANNEXES-06 |
| 41 duovicies G | 46 AI ter (a3) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-06 |
| 165 | 185 (a1) ×2 | proposal | couvert par dossier ALCOOL-A1-165-185-186 | — |
| 165 | 186 (a1) | proposal | couvert par dossier ALCOOL-A1-165-185-186 | — |
| 371 Z terdecies | 371 R (a2) | proposal | alerte écartée | — |
| 371 Z terdecies | 371 F (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-04 |
| 371 Z terdecies | 371 Z octies (a2) | proposal | alerte écartée | — |
| 242 nonies N | 41 septies A (a4) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies N | 41 septies K (a4) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 385 | 387 (a3) ×2 | proposal | alerte écartée | — |
| 385 | 390 (a3) | proposal | alerte écartée | — |
| 41 sexdecies A | 41 sexdecies G (a3) | proposal | alerte écartée | — |
| 41 sexdecies A | 46 AI ter (a3) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-06 |
| 143 | 383 (a2) | proposal | alerte écartée | — |
| 143 | 142 (a2) | proposal | alerte écartée | — |
| 286 O | 286 W (a2) | proposal | alerte écartée | — |
| 286 O | 50-0 BA (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-07 |
| 371 bis C bis | 371 bis H (a2) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 333 B | 333 A (a2) | unrewritten | alerte écartée | — |
| 333 B | 324 K (a3) | proposal | alerte écartée | — |
| 242 nonies L | 242 nonies E (a2) | unrewritten | coordination manquante | RT-P1-ANNEXES-01 |
| 242 nonies L | 41 septies H (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 242 nonies O | 41 septies M (a4) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-02 |
| 2 tervicies | 2 duovicies (a3) ×2 | proposal | alerte écartée | — |
| 41 J | 46 quater-0 A (a3) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-08 |
| 111 J | 111 N (a3) | proposal | alerte écartée | — |
| 111 J | 50-0 E (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-12 |
| 388 | 390 (a3) ×2 | proposal | alerte écartée | — |
| 41 duodecies | 381 K (a3) | proposal | alerte écartée | — |
| 41 duodecies | 119 (cgi) | proposal | alerte écartée | — |
| 209-0 A | 56 J vicies (a4) ×2 | proposal | incohérence du projet | RT-P1-ANNEXES-10 |
| 65 | 286 J (a2) | proposal | alerte écartée | — |
| 81 | 286 J (a2) | proposal | alerte écartée | — |
| 85 | 286 J (a2) | proposal | alerte écartée | — |
| 181 | R121-11 (cch) | unrewritten | faux positif | — |
| 142 | 383 (a2) | proposal | alerte écartée | — |
| 371 B | 371 Z ter (a2) | proposal | alerte écartée | — |
| 371 N | 371 Z ter (a2) | proposal | alerte écartée | — |
| 371 bis C | 371 bis K (a2) | proposal | incohérence du projet | RT-P1-ANNEXES-03 |
| 242-0 J | 208 (a2) | unrewritten | alerte écartée | — |
| 333 H | 333 A (a2) | unrewritten | alerte écartée | — |
| 311 A | 317 octies (a2) | proposal | alerte écartée | — |
| 311 C | 317 octies (a2) | proposal | alerte écartée | — |
| 16 F | 39 quinquies GA (cgi) | proposal | alerte écartée | — |
| 10 septies | 3 (a3) | proposal | alerte écartée | — |
| 143 H | 143 Z (a3) | proposal | alerte écartée | — |
| 53 bis | 53 quater (a3) | unrewritten | alerte écartée | — |
| 53 ter | 53 quater (a3) | unrewritten | alerte écartée | — |
| 143 A | 143 A 1 (a3) | proposal | alerte écartée | — |
| 143 Z | 143 H (a3) | proposal | alerte écartée | — |
| 344 GA | 344 GB (a3) | proposal | alerte écartée | — |
| 381 bis | 381 ter (a3) | proposal | alerte écartée | — |
| 390 | 388 (a3) | proposal | alerte écartée | — |
| 387 | 390 (a3) | proposal | alerte écartée | — |
| 404 A | 402 (a3) | unrewritten | alerte écartée | — |
| 49 septies ZZJ | 49 septies ZZK (a3) | proposal | alerte écartée | — |
| 397 | 398 (a3) | unrewritten | alerte écartée | — |
| 46 quindecies Q | 46 quindecies O (a3) | proposal | alerte écartée | — |
| 49 septies H | 23 L duodecies (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-09 |
| 41 duodecies P | 124 E (cgi) | proposal | alerte écartée | — |
| 46 B | 172 bis (cgi) | unrewritten | alerte écartée | — |
| 137 | 135 (a2) | proposal | faux positif | — |
| 164 F octovicies | 371 Y (a2) | proposal | alerte écartée | — |
| 50 C | 289 (a2) | proposal | couvert par dossier INUT | — |
| 23 A | 13 (a4) | proposal | alerte écartée | — |
| 23 B | 13 (a4) | proposal | alerte écartée | — |
| 54-0 E | 54-0 BX (a4) | unrewritten | alerte écartée | — |
| 56 AO | 56 AP (a4) | unrewritten | alerte écartée | — |
| 164 F quatervicies | 164 F quinvicies (a4) | proposal | alerte écartée | — |
| 4 J | 4 L (a4) | proposal | alerte écartée | — |
| 124 | 146 (a4) | proposal | incohérence du projet | RT-P1-ANNEXES-11 |
| 188 F | 1678 bis (cgi) | unrewritten | alerte écartée | — |

### 4.3 Alertes écartées : motifs principaux

- **Contexte transitoire assumé** : TSCA 385, 387, 388, 390 (taxe née de faits antérieurs) ; taxe sur les salaires 142, 143, 383, 53 bis, 53 ter et 53 quater ; successions 397, 398, 402 et 404 A ; 2 tervicies et 2 duovicies ; 371 bis I ; 344 GA et 344 GB ; 10 septies et 3 (exercices clos avant 1997).
- **Article qui renvoie, lui-même abrogé dans le même mouvement** : 295, 296, 297 ; 4 J et 4 L ; 143 H, 143 Z, 143 A et 143 A 1 ; 317 octies (311 A et 311 C) ; 371 bis C.
- **Renvoi neutralisé par une clause de la cible ou de l'article qui renvoie** : 371 V bis (cinq renvois) ; attestations relatives à 371 Z terdecies dans R et Z octies ; 41 sexdecies G ; 111 N ; 381 ter ; 39 quinquies GA (16 F) ; 49 septies ZZK ; 164 F quinvicies (la clause de 164 F quatervicies dispose que quinvicies et sexvicies « ne peuvent imposer cette information »).
- **Plages ou notes de plage neutres** : 286 J (« 57 à 87 de l'annexe I ») ; 286 W ; 333 A ; 324 K III ; 208 ; 381 K et CGI 119 ; 124 E ; 172 bis ; 371 Y ; 46 quindecies O ; 54-0 BX ; 56 AP ; 1678 bis ; 371 Z ter.
- **Faux positifs** : CCH R121-11, qui vise les « articles 178 à 185 » du décret n° 2012-1246 ; annexe II 135, qui vise « 136 à 140 » de l'annexe II.
- **Renvoi introduit valide** : CSS R931-1-29 vers R931-3-59 et R931-3-60. Ces articles existent, sont en vigueur et figurent déjà dans la plage R931-3-52 à R931-3-64.
- **Annexe IV 13 II 3°** (récépissés de 23 A et 23 B) : mode de preuve facultatif, qui ne rétablit aucune déclaration. Amélioration rédactionnelle facultative : « récépissé délivré avant l'abrogation des articles 23 A et 23 B ».

## 5. Propositions de correction (présentées séparément)

Toutes les propositions ci-dessous préservent les orientations : suppression des formalités sans formalité de remplacement, maintien des exonérations et dérogations favorables, droits acquis et échéances anciennes, et loi répressive plus douce. Elles dépendent de l'entrée en vigueur simultanée des abrogations législatives visées (289 E, 290 et 290 A ; 302 F ter 2° ; 244 quater B d bis).

### 5.1 RT-P1-ANNEXES-01 : textes maintenus de la facturation électronique

**Annexe II, article 242 nonies E (proposition complète) :**

> Les plateformes agréées sont tenues de proposer les services suivants :
>
> 1° Permettre à leurs utilisateurs de saisir, déposer, émettre ou transmettre leurs factures électroniques dans des conditions de nature à en garantir l'authenticité de l'origine, l'intégrité du contenu et la lisibilité ;
>
> 2° Effectuer les contrôles mentionnés à l'article 242 nonies K et identifier les destinataires des factures électroniques au moyen de l'annuaire central ;
>
> 3° Fournir et mettre à jour les informations relatives à leurs utilisateurs nécessaires au fonctionnement de l'annuaire central dans le respect des conditions prévues par l'article 242 nonies E bis ;
>
> 4° Assurer la transmission des factures électroniques aux plateformes agréées choisies par leurs destinataires, selon les modalités d'interopérabilité définies à l'article 242 nonies I et dans des conditions de nature à en garantir l'authenticité de l'origine, l'intégrité du contenu et la lisibilité à compter de leur émission jusqu'à la fin de la période de conservation ;
>
> 5° Recevoir et mettre à disposition de leurs destinataires les factures électroniques adressées par les autres plateformes agréées ;
>
> 6° Assurer la gestion des statuts de traitement des factures électroniques en garantissant :
>
> a) La mise à disposition à leurs utilisateurs des informations relatives à ces statuts ;
>
> b) La possibilité pour leurs utilisateurs de mettre à jour les informations relatives aux statuts de traitement lorsqu'il y a lieu ;
>
> c) La transmission des informations relatives aux statuts de traitement aux plateformes agréées des parties aux transactions ;
>
> 7° (Abrogé) ;
>
> 8° (Abrogé).
>
> Les modalités d'application du présent article sont précisées par arrêté du ministre chargé du budget.
>
> À compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues aux articles 289 E, 290 et 290 A du code général des impôts, aucune extraction, aucun recueil ni aucune transmission à l'administration de données de facturation, de transaction ou de paiement, ni d'informations relatives aux statuts de traitement, ne peut être exigé des plateformes agréées ou de leurs utilisateurs sur le fondement du présent article, y compris pour des opérations, factures ou paiements antérieurs. L'absence de ces services ne peut fonder un refus, une suspension ou un retrait d'immatriculation. Les services mentionnés aux 1° à 6° demeurent. Les données déjà transmises restent soumises aux garanties de confidentialité, de conservation et d'accès qui leur sont applicables. Les manquements antérieurs aux seules obligations supprimées relèvent, dans leur champ, de la loi répressive plus douce.

*Justification* : l'article retire ce que les cibles abrogent et conserve ce que leurs notes demandent de ne pas abolir (« Les contrôles de factures et l'annuaire ne doivent pas être abolis avec les flux fiscaux »). *Dépendances* : 242 nonies B I 7° c et d (RT-02), 41 septies A I 1° b (RT-02), propositions législatives 289 E, 290 et 290 A.

**Annexe II, article 242 nonies G :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues aux articles 289 E, 290 et 290 A du code général des impôts. À compter de cette date, aucun recueil de données de facturation, de transaction ou de paiement, ni d'informations relatives aux statuts de traitement, ne peut être organisé ou exigé sur son fondement, y compris pour des opérations antérieures. L'annuaire central prévu au III de l'article 289 bis du code général des impôts et les échanges entre plateformes agréées ne sont pas affectés. Les données déjà recueillies demeurent soumises aux garanties de confidentialité, de conservation et d'accès qui leur sont applicables.

**Annexe IV, articles 41 septies J, L, N et O (rédaction commune, en adaptant l'objet) :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues à l'article 290 [J et L] / 290 A [N et O] du code général des impôts. Aucune norme sémantique, aucun format, aucune globalisation ni aucune modalité de transmission des données de transaction [J et L] / de paiement [N et O] ne peut être exigé sur son fondement à compter de cette date, y compris pour des opérations antérieures. Les données déjà transmises demeurent soumises aux garanties qui leur sont applicables. Les manquements antérieurs aux seules obligations supprimées relèvent, dans leur champ, de la loi répressive plus douce.

**Annexe IV, article 41 septies K (proposition complète, qui conserve les identifiants favorables utilisés par 41 septies D) :**

> En l'absence du numéro d'identification de l'assujetti mentionné au 1° du I de l'article 242 nonies A de l'annexe II au code général des impôts, la facture électronique comporte l'un des identifiants suivants, sans que la plateforme agréée ait à en contrôler la validité :
>
> a) Pour les assujettis dont le siège social est domicilié dans un État membre de l'Union européenne autre que la France, le numéro d'identification à la taxe sur la valeur ajoutée ;
>
> b) Pour les assujettis dont le siège social est domicilié dans un État non membre de l'Union européenne, le code pays défini par la norme ISO 3166 et les seize premiers caractères de la dénomination sociale ;
>
> c) Pour les entreprises immatriculées dans le traitement automatique hiérarchisé des institutions de Tahiti et des îles de Polynésie française, le numéro TAHITI attribué en application de l'arrêté n° 1025 CM du 27 août 1986 ;
>
> d) Pour les entreprises immatriculées dans le répertoire d'identification des entreprises et des établissements de Nouvelle-Calédonie, le numéro du répertoire RIDET attribué en application de l'arrêté n° 83-661/ CG du 20 décembre 1983 ;
>
> e) Pour les entreprises dont le siège social est situé dans la collectivité de Wallis-et-Futuna, le code « FRWF » suivi des quatorze premiers caractères de la raison sociale.
>
> À compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues à l'article 290 du code général des impôts, les contrôles de présence et de cohérence des données de transaction antérieurement prévus pour l'application de l'article 242 nonies N de l'annexe II ne sont plus exigés, y compris pour des opérations antérieures.

*Dépendance* : 41 septies D renvoie au « 2° de l'article 41 septies K ». Il faut remplacer ce renvoi par « à l'article 41 septies K ».

### 5.2 RT-P1-ANNEXES-02 : propositions réécrites de la facturation électronique

- **41 septies H, M et P** : abrogation, avec la rédaction de 5.1 (« Aucun délai, aucune échéance ni aucune transmission […] n'est exigé sur son fondement, y compris pour les périodes antérieures »). Il faut supprimer « Les périodes antérieures conservent leurs échéances », qui contredit les cibles O et P.
- **41 septies A** : en I 1° b, supprimer « à la solution de l'administration mentionnée à l'article 242 nonies G de l'annexe II à ce même code et ». Les I 4° et I 5° deviennent « (Abrogé) ». Le I 7° c devient « c) Les processus de traitement des factures ; ». Ajouter au IV : « Les points d'audit relatifs au recueil des données et à leur transmission à l'administration ne sont pas examinés dans les rapports remis à compter de l'entrée en vigueur de la loi supprimant les transmissions prévues aux articles 289 E, 290 et 290 A du code général des impôts ; aucune non-conformité ne peut être relevée à ce titre. »
- **41 septies G** : le I 4° devient « 4° “ Encaissée ” de la facture. ». Au II, conserver la faculté de mise à jour du statut « encaissée » par l'émetteur, mais remplacer le renvoi à l'article 290 A, abrogé, par la désignation directe des opérations concernées, à vérifier dans la proposition de 290 A, sans étendre ni restreindre ce champ. Au III, le second alinéa devient : « À compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues aux articles 289 E, 290 et 290 A du code général des impôts, aucune information relative aux statuts de traitement n'est transmise à l'administration sur le fondement du présent article ou du 6° de l'article 242 nonies E de l'annexe II, y compris pour une facture antérieure. Les informations déjà transmises n'ont pas à l'être de nouveau. »
- **41 septies D** : en I, remplacer « mentionnées à l'article 242 nonies J de l'annexe II » par « mentionnées à l'article 289 bis du code général des impôts ». Ajouter : « Ces données ne sont pas transmises à l'administration sur le fondement du présent article. » Autre option : abroger D en entier si ce socle n'a pas d'autre fonction que fiscale.
- **242 nonies B (annexe II)** : supprimer I 7° c et, au I 7° d, « avec la solution de l'administration mentionnée à l'article 242 nonies G ».

### 5.3 RT-P1-ANNEXES-03 : 371 bis F, H, K et M

**371 bis F :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la présente réforme, en conséquence de la suppression du conventionnement prévu à l'article 371 bis B. Aucune obligation, notamment de transmission, d'examen ou de traçabilité des missions de contrôle, ne peut être exigée sur son fondement à compter de cette date, y compris au titre d'une convention antérieure. Le client ou l'adhérent demeure mis en mesure de présenter ses observations dans un examen engagé avant cette date. Les pièces déjà recueillies restent soumises aux règles de conservation et de confidentialité. Cette abrogation ne peut, par elle-même, entraîner la perte d'un avantage fiscal du client ou de l'adhérent. Les obligations professionnelles, déontologiques et contractuelles autonomes demeurent.

**371 bis H :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la présente réforme. Aucune résiliation de convention ne peut être prononcée sur son fondement après cette date. Les décisions de résiliation notifiées avant cette date, leur motivation, leur notification et les recours qui les concernent conservent leur régime, sous réserve des dispositions répressives plus douces. Les sanctions disciplinaires, fiscales et pénales fondées sur d'autres dispositions ne sont pas affectées.

**371 bis K :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la présente réforme. Aucune demande d'autorisation ou de convention ne peut être présentée ni instruite sur son fondement ; les demandes en cours deviennent sans objet, sans nouvelle démarche. L'absence de convention ne peut être opposée au professionnel ou à son client pour une situation future. Les conditions d'exercice de la profession d'expert-comptable, l'inscription au tableau et les suspensions prononcées sur un autre fondement ne sont pas modifiées.

**371 bis M :**

> Le présent article est abrogé à compter de l'entrée en vigueur de la présente réforme. Les clients ou adhérents d'un professionnel ayant signé la convention prévue à l'ancien article 371 bis B ne sont plus tenus d'apposer ni de diffuser une information relative à cette convention, et le professionnel n'a plus à porter cette obligation à leur connaissance. Aucun affichage ou information de remplacement n'est exigé. Les obligations légales autonomes d'acceptation des moyens de paiement et d'information du consommateur demeurent applicables.

*Justification* : chaque texte retire une procédure attachée à la convention abrogée, ainsi que des renvois actifs à 371 bis B, C et C bis. *Dépendances* : RT-05 (base légale), modèles ministériels de convention, 371 bis G (non examiné).

### 5.4 RT-P1-ANNEXES-04 : interdictions biennales et pièces des dossiers d'agrément

- **371 F 11°** : « 11° Aucune attestation n'est jointe au titre des interdictions des articles 371 K bis, 371 V bis et 371 Z terdecies, abrogés ; ces interdictions ne produisent plus effet ; ».
- **371 R** : « 4° Aucun certificat prévu à l'article 371 D n'est joint ; » et « 11° Abrogé ; » (alignement sur 371 F et 371 D proposés).
- **371 Z octies** : « 4° Aucun certificat prévu à l'article 371 D n'est joint ; » et « 11° Aucune attestation n'est jointe au titre des interdictions des articles 371 K bis, 371 V bis et 371 Z terdecies, abrogés ; ». Supprimer la phrase « Cette attestation vaut également celle requise par l'article 371 D dans les conditions de l'article 371 Z quinquies. »
- **371 D** : remplacer l'alinéa « Les centres veillent à ce que les personnes qui les administrent ne soient pas frappées par les interdictions prévues aux articles 371 K bis et 371 V bis. » par « À compter de l'entrée en vigueur de la présente réforme, les interdictions des articles 371 K bis, 371 V bis et 371 Z terdecies, abrogés, ne constituent plus une condition d'agrément ni de maintien de l'agrément. »
- **371 Z quinquies (proposition complète)** : « Les organismes mixtes sont soumis aux conditions prévues à l'article 371 D, sans production de certificat ni d'attestation. Cette règle s'applique dès l'entrée en vigueur de la réforme aux demandes en cours et futures ; les pièces déjà produites n'ont pas à être renouvelées. »

### 5.5 RT-P1-ANNEXES-06 : fonds

- **41 Y** : « 2° (Supprimé) ; ». Ajouter en fin d'article : « Le relevé prévu à l'article 41 duovicies G, abrogé, n'est plus exigé. »
- **41 X** : remplacer « désignée à l'article 41 duovicies G » par « auprès de laquelle il souscrit sa déclaration de résultats », et « Les obligations prévues aux articles 41 Y et 41 duovicies G demeurent applicables dans leur champ propre » par « Les obligations prévues à l'article 41 Y demeurent applicables dans leur champ propre ».
- **46 AI ter** : au I, la dernière phrase devient « Aucune déclaration n'est exigée au titre de l'article 41 sexdecies A, abrogé. ». Au II, remplacer « 41 sexdecies A à 41 sexdecies F » par « 41 sexdecies C à 41 sexdecies F ». Au III, remplacer « aux articles 41 duovicies F et 41 duovicies G » par « à l'article 41 duovicies F ». Au VIII, remplacer « au titre des articles 41 duovicies F et 41 duovicies G » par « au titre de l'article 41 duovicies F ».

### 5.6 Objections P2

Les corrections de RT-07 à RT-13 sont rédigées en entier dans le champ `minimal_correction` du JSON. RT-05 et RT-14 demandent une vérification documentaire avant toute rédaction.

## 6. Incertitudes et éléments non examinés

- **Base légale des régimes OGA et viseurs (RT-05)** : l'article 11 de la loi n° 2025-127 n'a pas pu être lu (Légifrance HTTP 403). On ne sait donc pas s'il supprime ou transfère le régime. 1649 quater E et H présentent une version VIGUEUR_DIFF au 2030-01-01 qui reste inexpliquée.
- **Facturation électronique** : les propositions législatives 289 E, 290, 290 A, 289 bis et 290 B n'ont pas été relues en entier ici. Leur abrogation est tirée des motifs des cibles. Les notes annoncent une reprise dans le CIBS au 1er janvier 2027 (ordonnance n° 2025-1247, non lue). Le droit de l'Union n'a pas été vérifié pour ce paquet : directive TVA, décision d'exécution autorisant l'obligation française, directive « ViDA » sur la déclaration numérique des opérations intracommunautaires. Une suppression totale du flux de 290 (opérations internationales) devra être confrontée à ces textes.
- **Annexe I 165, 185 et 186, et annexe II 289** : non examinés au fond, car couverts par d'autres dossiers.
- **Articles non alertés mais touchés par les corrections** : 371 bis G, 371 bis J, 54-0 AB, 54-0 S, 54-0 V, 41 septies C, F et I, 242 nonies E bis et E ter, 242 nonies C. Seuls leurs passages liés ont été vus.
- **Classement `couvert par dossier ALCOOL-A1-165-185-186`** : je n'ai pas trouvé d'identifiant officiel de dossier pour cette ligne de l'INDEX. Le libellé est descriptif.
- La seconde passe continue : une proposition modifiée après l'instantané peut rendre caduque une objection, ou en créer une nouvelle.
