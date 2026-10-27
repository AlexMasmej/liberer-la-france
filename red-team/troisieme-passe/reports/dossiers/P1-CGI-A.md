# Dossier P1-CGI-A : qualification des alertes « renvoi vers une abrogation proposée » (cibles CGI, paquet A)

Red-team juridique indépendante, troisième passe. Instantané `snapshots/20261026T230545Z`, corpus de référence au **18 octobre 2026**. Rapport du 26 octobre 2026.

**Avertissement.** Cette revue est faite par une IA. Elle ne vaut pas validation par un juriste. La seconde passe continue : les propositions citées peuvent encore changer. Aucune source externe n'a été consultée : tout provient de l'instantané, lu par `tools/cite.py`, et de requêtes SQL en lecture seule.

## 1. Résumé

- **147 alertes, 38 clusters**, toutes classées :
  - 64 `faux positif` : le cluster CGI 199, entièrement dû à une erreur de résolution des numéros ;
  - 68 `alerte écartée` ;
  - 9 `coordination manquante` ;
  - 6 `incohérence du projet` ;
  - 0 `non examiné`.
- **9 objections** : 3 P1 (2 confirmées, 1 à confirmer), 6 P2 (5 confirmées, 1 faux positif documenté).
- **Point le plus important.** La suppression du *e-reporting* (290 et 290 A) est inachevée dans les annexes. Les objections concernées :
  - **RT-P1-CGI-A-01** (P1) : l'arrêté 41 septies G de l'annexe IV, *réécrit par le projet*, déclare encore « obligatoire » la transmission à l'administration du statut « encaissée », qui contient les données de paiement. Or 290 A et 242 nonies P suppriment cette transmission.
  - **RT-P1-CGI-A-02** (P1) : 242 nonies E de l'annexe II et 41 septies L et O de l'annexe IV, maintenus inchangés, organisent toujours ces flux.
  - **RT-P1-CGI-A-03** (P1, à confirmer) : la recodification de ces articles dans le CIBS au 1er janvier 2027 n'est pas coordonnée. La suppression pourrait rester sans effet après cette date.
- **Cluster 199.** Aucun des 64 renvois ne vise le CGI 199 : tous visent 199 novovicies, 199 terdecies-0 A, etc. Une recherche dans tout le corpus courant ne trouve aucun renvoi au CGI 199 nu. L'abrogation de la restriction de nationalité du quotient familial ne laisse donc aucun renvoi pendant.

## 2. Méthode

1. Pour chaque cluster, j'ai lu en entier la cible : source, NOTA, proposition, motif et notes de revue.
2. J'ai lu le texte courant de chaque article qui y renvoie : la proposition s'il est réécrit, la source s'il est inchangé. J'ai vérifié que chaque occurrence du numéro cité vise bien la cible (même code, absence de suffixe). Pour cela, j'ai extrait mécaniquement toutes les occurrences du numéro dans le texte courant intégral, puis je les ai contrôlées à la lecture.
3. Pour CGI 199, j'ai établi l'erreur de résolution par cette extraction exhaustive : les 64 occurrences sont toutes suffixées. Les 33 textes n'ont pas été lus intégralement, d'où `read_in_full=false`. J'ai ensuite vérifié que les articles réellement visés ne sont pas abrogés par une formule explicite, et cherché dans tout le corpus courant un renvoi au CGI 199 nu.
4. CGI 31 et 39 (55 000 et 46 600 signes) ont été lus sur le passage pertinent seulement, d'où `read_in_full=false`. La qualification repose sur des clauses d'exclusion autonomes.
5. Pour qualifier, j'ai lu au besoin d'autres textes, en version courante : 1519, 1588, 290 B, 289 E, 1788 D, 242 nonies J, M, N, O et P (annexe II), 41 septies M (annexe IV), 4 J, 4 K et 4 L et 50 (annexe IV). Les preuves sont dans `evidence/cited/20261026T230545Z/`.
6. Aucun cluster ne touche un dossier ouvert de l'addendum.
7. J'ai fait une seule objection par effet juridique. Les alertes neutralisées par une clause expresse de la cible (« Aucun renvoi au présent article ne peut... ») sont `alerte écartée`, sauf lorsqu'une proposition réécrite affirme le contraire (`incohérence du projet`).

## 3. Périmètre réellement lu

Toutes les cibles ont été lues intégralement (version citée ci-dessous). Les autres articles lus figurent au § 2, point 5.

| # | Cible (CGI) | Version cible | Renvois (code numéro LEGIARTI, statut, lecture) |
|---|---|---|---|
| 0 | 199 | LEGIARTI000027978108 VIGUEUR 2013-09-21→2999-01-01, 64 alertes | a2 74-0 F LEGIARTI000041590007 (réécrit ; extraction exhaustive des occurrences); a3 46 AI sexies LEGIARTI000020001091 (réécrit ; extraction exhaustive des occurrences); a3 46 AZA octies B LEGIARTI000026886281 (inchangé ; extraction exhaustive des occurrences); a3 46 AZA quaterdecies LEGIARTI000030553289 (réécrit ; extraction exhaustive des occurrences); a3 46 AZA terdecies LEGIARTI000030553298 (réécrit ; extraction exhaustive des occurrences); a3 46 AZA duodecies LEGIARTI000030553311 (réécrit ; extraction exhaustive des occurrences); a3 46 AZA undecies LEGIARTI000038316347 (réécrit ; extraction exhaustive des occurrences); a3 46 AI septies LEGIARTI000039436950 (réécrit ; extraction exhaustive des occurrences); a3 2 quindecies B LEGIARTI000041799260 (inchangé ; extraction exhaustive des occurrences); a3 46 AI quinquies A LEGIARTI000042223951 (inchangé ; extraction exhaustive des occurrences); a3 46 AZA octies-0 AA LEGIARTI000043841449 (réécrit ; extraction exhaustive des occurrences); a3 46 AZA octies-0 A LEGIARTI000043841461 (réécrit ; extraction exhaustive des occurrences); a3 46 AI bis A LEGIARTI000050736241 (inchangé ; extraction exhaustive des occurrences); a3 46 AI quinquies-0 A LEGIARTI000050736623 (réécrit ; extraction exhaustive des occurrences); a3 46 AI ter LEGIARTI000050743550 (réécrit ; extraction exhaustive des occurrences); a3 46 AI bis B LEGIARTI000051762578 (réécrit ; extraction exhaustive des occurrences); a3 46 AI bis LEGIARTI000051762587 (réécrit ; extraction exhaustive des occurrences); a3 46 AI quinquies-0 B LEGIARTI000053527526 (réécrit ; extraction exhaustive des occurrences); a3 2 terdecies F LEGIARTI000054364065 (réécrit ; extraction exhaustive des occurrences); a3 2 terdecies D LEGIARTI000054364082 (réécrit ; extraction exhaustive des occurrences); a4 18-0 bis C LEGIARTI000042147371 (inchangé ; extraction exhaustive des occurrences); cgi 726 LEGIARTI000048845731 (réécrit ; extraction exhaustive des occurrences); cgi 199 terdecies-0 C LEGIARTI000051217806 (réécrit ; extraction exhaustive des occurrences); cgi 199 terdecies-0 A LEGIARTI000053543691 (réécrit ; extraction exhaustive des occurrences); cgi 199 terdecies-0 AB LEGIARTI000053543929 (réécrit ; extraction exhaustive des occurrences); cgi 31 LEGIARTI000053544761 (réécrit ; extraction exhaustive des occurrences); cgi 279-0 bis A LEGIARTI000053561519 (réécrit ; extraction exhaustive des occurrences); urba L151-29 LEGIARTI000032860940 (réécrit ; extraction exhaustive des occurrences); cch R362-2 LEGIARTI000039636452 (réécrit ; extraction exhaustive des occurrences); cch L301-5-1-3 LEGIARTI000045201824 (réécrit ; extraction exhaustive des occurrences); cch L422-3 LEGIARTI000053546162 (réécrit ; extraction exhaustive des occurrences); cch L422-2 LEGIARTI000053546225 (réécrit ; extraction exhaustive des occurrences); cch L421-1 LEGIARTI000053546314 (réécrit ; extraction exhaustive des occurrences) |
| 1 | 290 | LEGIARTI000053546668 ABROGE_DIFF 2026-02-21→2222-02-22, 7 alertes | a2 242 nonies E LEGIARTI000054552509 (inchangé ; intégrale); a2 242 nonies K LEGIARTI000054552551 (réécrit ; intégrale); a4 41 septies O LEGIARTI000046386267 (inchangé ; intégrale); a4 41 septies L LEGIARTI000054606212 (inchangé ; intégrale); cgi 289 bis LEGIARTI000053546660 (réécrit ; intégrale); cgi 1788 E LEGIARTI000053546696 (réécrit ; intégrale) |
| 2 | 1641 | LEGIARTI000053546093 VIGUEUR 2026-02-21→2999-01-01, 7 alertes | a4 155 bis A LEGIARTI000053702677 (inchangé ; intégrale); cgi 1647-00 A LEGIARTI000006306861 (réécrit ; intégrale); cgi 1647 bis LEGIARTI000021640978 (réécrit ; intégrale); cgi 220 Z septies LEGIARTI000048826400 (réécrit ; intégrale); cgi 1647 B sexies LEGIARTI000048860555 (réécrit ; intégrale); cgi 1530 bis LEGIARTI000051219443 (inchangé ; intégrale); css L136-6 LEGIARTI000051218166 (réécrit ; intégrale) |
| 3 | 1587 | LEGIARTI000053546514 VIGUEUR 2026-02-21→2999-01-01, 5 alertes | a2 311 A LEGIARTI000006294877 (réécrit ; intégrale); a2 311 B LEGIARTI000006294878 (réécrit ; intégrale); a2 311 C LEGIARTI000025622306 (réécrit ; intégrale); a2 317 octies LEGIARTI000054363280 (réécrit ; intégrale); cgi 1589 LEGIARTI000027517638 (réécrit ; intégrale) |
| 4 | 290 A | LEGIARTI000053546674 ABROGE_DIFF 2026-02-21→2222-02-22, 5 alertes | a2 242 nonies E LEGIARTI000054552509 (inchangé ; intégrale); a2 242 nonies K LEGIARTI000054552551 (réécrit ; intégrale); a4 41 septies G LEGIARTI000054606169 (réécrit ; intégrale); cgi 1788 E LEGIARTI000053546696 (réécrit ; intégrale) |
| 5 | 200-0 A | LEGIARTI000053543258 VIGUEUR 2026-02-21→2999-01-01, 4 alertes | a3 46-0 B ter LEGIARTI000021981369 (réécrit ; intégrale); a3 46-0 B LEGIARTI000037100817 (réécrit ; intégrale); a3 46-0 B bis LEGIARTI000042161040 (réécrit ; intégrale); cgi 170 LEGIARTI000053543803 (réécrit ; intégrale) |
| 6 | 1530 | LEGIARTI000053544724 VIGUEUR 2026-02-21→2999-01-01, 4 alertes | cgi 1518 quater LEGIARTI000043157255 (inchangé ; intégrale); cgi 1382-0 LEGIARTI000048846391 (réécrit ; intégrale); cgi 1518 A quinquies LEGIARTI000053589332 (inchangé ; intégrale); cgi 1379 LEGIARTI000054356151 (inchangé ; intégrale) |
| 7 | 1407 ter | LEGIARTI000053546033 VIGUEUR 2026-02-21→2999-01-01, 4 alertes | cgi 1636 B octies LEGIARTI000051219300 (inchangé ; intégrale); cgi 1640 LEGIARTI000053546085 (réécrit ; intégrale); cgi 1758 bis LEGIARTI000053546938 (réécrit ; intégrale) |
| 8 | 1635 bis AE | LEGIARTI000037947963 VIGUEUR 2019-01-01→2999-01-01, 3 alertes | a2 326 quater LEGIARTI000054363276 (réécrit ; intégrale); cgi 1647 LEGIARTI000054373998 (réécrit ; intégrale); css L241-2 LEGIARTI000046805562 (réécrit ; intégrale) |
| 9 | 655 | LEGIARTI000006305199 VIGUEUR 2005-12-31→2999-01-01, 3 alertes | cgi 650 LEGIARTI000006305188 (réécrit ; intégrale); cgi 652 LEGIARTI000006305190 (réécrit ; intégrale); cgi 653 LEGIARTI000048838949 (réécrit ; intégrale) |
| 10 | 1519 B | LEGIARTI000054374020 ABROGE_DIFF 2026-07-01→2027-01-01, 3 alertes | cgi 1635 quinquies LEGIARTI000034596458 (inchangé ; intégrale); cgi 1379 LEGIARTI000054356151 (inchangé ; intégrale); cgi 1647 LEGIARTI000054373998 (réécrit ; intégrale) |
| 11 | 231 quater | LEGIARTI000054374077 ABROGE_DIFF 2026-07-01→2027-01-01, 3 alertes | cgi 1764 LEGIARTI000051219760 (réécrit ; intégrale); cgi 39 LEGIARTI000053542680 (réécrit ; passage pertinent); cgi 31 LEGIARTI000053544761 (réécrit ; passage pertinent) |
| 12 | 1499 A | LEGIARTI000006311727 VIGUEUR 1980-01-11→2999-01-01, 2 alertes | a2 310 K bis LEGIARTI000006294854 (réécrit ; intégrale); cgi 1518 LEGIARTI000037992547 (inchangé ; intégrale) |
| 13 | 234 quaterdecies | LEGIARTI000022171921 VIGUEUR 2010-05-01→2999-01-01, 2 alertes | a3 58 A LEGIARTI000006300110 (réécrit ; intégrale); a3 381 LEGIARTI000006300129 (réécrit ; intégrale) |
| 14 | 1609 untricies | LEGIARTI000030517151 ABROGE_DIFF 2015-04-25→2027-01-01, 2 alertes | a3 344 GD LEGIARTI000035302062 (réécrit ; intégrale) |
| 15 | 276 | LEGIARTI000006304328 ABROGE_DIFF 1979-07-01→2027-01-01, 2 alertes | a4 50 bis LEGIARTI000006300402 (réécrit ; intégrale); a4 49 LEGIARTI000043592523 (inchangé ; intégrale) |
| 16 | 742 | LEGIARTI000021642410 VIGUEUR 2011-01-01→2999-01-01, 2 alertes | cgi 689 LEGIARTI000006305248 (réécrit ; intégrale); cgi 743 bis LEGIARTI000006305329 (réécrit ; intégrale) |
| 17 | 209 quater | LEGIARTI000006303463 VIGUEUR 2005-01-01→2999-01-01, 2 alertes | cgi 208 septies LEGIARTI000031284026 (réécrit ; intégrale) |
| 18 | 1609 B | LEGIARTI000054373110 VIGUEUR 2026-07-01→2999-01-01, 2 alertes | cgi 220 Z septies LEGIARTI000048826400 (réécrit ; intégrale); cgi 1647 B sexies LEGIARTI000048860555 (réécrit ; intégrale) |
| 19 | 1519 A | LEGIARTI000054374023 ABROGE_DIFF 2026-07-01→2027-01-01, 2 alertes | cgi 1379-0 bis LEGIARTI000054356148 (réécrit ; intégrale); cgi 1379 LEGIARTI000054356151 (inchangé ; intégrale) |
| 20 | 1635 bis AG | LEGIARTI000037065058 VIGUEUR 2018-06-14→2999-01-01, 2 alertes | cgi 1647 LEGIARTI000054373998 (réécrit ; intégrale); css L241-2 LEGIARTI000046805562 (réécrit ; intégrale) |
| 21 | 54 quater | LEGIARTI000021657803 VIGUEUR 2011-01-01→2999-01-01, 1 alertes | a2 36 LEGIARTI000006293719 (réécrit ; intégrale) |
| 22 | 1635 bis N | LEGIARTI000041823043 VIGUEUR 2020-04-26→2999-01-01, 1 alertes | a2 326 bis LEGIARTI000006294933 (réécrit ; intégrale) |
| 23 | 1709 | LEGIARTI000020034005 VIGUEUR 2008-12-29→2999-01-01, 1 alertes | a2 171 quater LEGIARTI000054363238 (inchangé ; intégrale) |
| 24 | 1595 | LEGIARTI000006312235 VIGUEUR 2002-03-31→2999-01-01, 1 alertes | a3 267 LEGIARTI000006297169 (réécrit ; intégrale) |
| 25 | 1586 octies | LEGIARTI000042909509 ABROGE_DIFF 2021-01-01→2030-01-01, 1 alertes | a3 40 A LEGIARTI000026348033 (réécrit ; intégrale) |
| 26 | 805 | LEGIARTI000022174494 VIGUEUR 2010-05-01→2999-01-01, 1 alertes | a3 350 quindecies LEGIARTI000042987126 (réécrit ; intégrale) |
| 27 | 1722 bis | LEGIARTI000006313662 VIGUEUR 2007-01-01→2999-01-01, 1 alertes | a3 397 LEGIARTI000048852299 (réécrit ; intégrale) |
| 28 | 238 bis HY | LEGIARTI000006304034 VIGUEUR 2006-12-31→2999-01-01, 1 alertes | cgi 238 bis HZ bis LEGIARTI000006304036 (réécrit ; intégrale) |
| 29 | 958 | LEGIARTI000053547082 VIGUEUR 2026-05-01→2999-01-01, 1 alertes | cgi 959 LEGIARTI000024167481 (réécrit ; intégrale) |
| 30 | 796-0 ter | LEGIARTI000006305481 VIGUEUR 2007-08-22→2999-01-01, 1 alertes | cgi 990 I bis LEGIARTI000031781404 (réécrit ; intégrale) |
| 31 | 636 | LEGIARTI000042914141 VIGUEUR 2020-12-31→2999-01-01, 1 alertes | cgi 662 LEGIARTI000041466161 (réécrit ; intégrale) |
| 32 | 1609 C | LEGIARTI000048848666 VIGUEUR 2023-12-31→2999-01-01, 1 alertes | cgi 1396 LEGIARTI000048704443 (réécrit ; intégrale) |
| 33 | 1518 F | LEGIARTI000036356953 VIGUEUR 2018-01-01→2999-01-01, 1 alertes | cgi 1507 LEGIARTI000051219153 (inchangé ; intégrale) |
| 34 | 1135 bis | LEGIARTI000051149532 VIGUEUR 2025-02-09→2999-01-01, 1 alertes | cgi 1840 G ter LEGIARTI000053543390 (réécrit ; intégrale) |
| 35 | 242 quinquies | LEGIARTI000032701583 VIGUEUR 2016-06-13→2999-01-01, 1 alertes | cgi 1763 B LEGIARTI000053546921 (réécrit ; intégrale) |
| 36 | 1613 quater | LEGIARTI000051288275 ABROGE_DIFF 2026-01-01→2027-01-01, 1 alertes | cgi 302 decies LEGIARTI000054373376 (réécrit ; intégrale) |
| 37 | 168 | LEGIARTI000054373636 VIGUEUR 2026-07-01→2999-01-01, 1 alertes | css L136-6 LEGIARTI000051218166 (réécrit ; intégrale) |

## 4. Constats

### 4.1 Objections

| ID | Prio. | Nature | Statut | Objet | Alertes |
|---|---|---|---|---|---|
| RT-P1-CGI-A-01 | P1 | incohérence du projet | confirmé | 41 septies G (annexe IV), réécrit, maintient obligatoire la transmission du statut « encaissée » et des données de paiement, contre 290 A et 242 nonies P | 48e19f1ec4, 2253dff3e9 |
| RT-P1-CGI-A-02 | P1 | coordination manquante | confirmé | 242 nonies E 8° (annexe II), 41 septies L et O (annexe IV), inchangés, organisent encore les flux de 290 et 290 A | 35960b56f8, 6a3b8a7246, cc8cba74d4, 949db9d015, ec131f7042 |
| RT-P1-CGI-A-03 | P1 | risque juridique | à confirmer | Recodification CIBS au 1er janvier 2027 de 289 bis, 290 et 290 A non coordonnée avec leur abrogation | (cibles 290 et 290 A) |
| RT-P1-CGI-A-04 | P2 | coordination manquante | confirmé | CGI 1379, inchangé, liste encore 1519 A, 1519 B et 1530 (et 1519) parmi les ressources communales | cdb986f59b, b702b636ed, 5017c4a512 |
| RT-P1-CGI-A-05 | P2 | incohérence du projet | confirmé | 170, 1 proposé exige encore les éléments du plafonnement de 200-0 A abrogé | e13e25dcb2 |
| RT-P1-CGI-A-06 | P2 | incohérence du projet | confirmé | 1764 V proposé : « L'article 231 quater conserve son champ propre » | 801f01c2e4 |
| RT-P1-CGI-A-07 | P2 | incohérence du projet | confirmé | 50 bis (annexe IV) proposé maintient les conditions de 276 abrogé ; 49, inchangé, l'étend encore | e88dbb46c0, b419c0eefb |
| RT-P1-CGI-A-08 | P2 | incohérence du projet | confirmé | 36 (annexe II) proposé règle encore le relevé de 54 quater supprimé | 697c32fd09 |
| RT-P1-CGI-A-09 | P2 | faux positif | faux positif | Cluster CGI 199 : 64 renvois à des articles « 199 + suffixe » | 64 alertes du cluster 0 |

Le raisonnement détaillé, les passages exacts et les empreintes figurent dans `reports/dossiers/P1-CGI-A.json`.

### 4.2 Le e-reporting (clusters 290 et 290 A)

Les abrogations de 290 et 290 A sont soignées. Elles visent les transmissions restant à effectuer, excluent tout rattrapage ou remplacement, appliquent la loi répressive plus douce et neutralisent la réserve de 289 bis. 289 bis a d'ailleurs été réécrit depuis l'audit : son texte courant dispose que 289 E, 290 et 290 A « ne peuvent fonder aucune obligation de transmission ». L'alerte de1ec3ecfc est donc résolue. Les notes de revue de 290 et 290 A décrivent encore une « contradiction effective » avec 289 bis qui n'existe plus : c'est une note périmée, sans objection.

Le démontage s'arrête pourtant aux textes réglementaires :
- **41 septies G** (annexe IV, completed) retire la remontée des statuts dépôt, rejet et refus, mais ajoute : « seule la transmission à l'administration des informations relatives au statut « encaissée », pour les opérations visées à l'article 290 A du même code, demeure obligatoire ». Son I, 4°, définit ce statut comme comprenant « les données de paiement mentionnées au I de l'article 242 nonies P », alors que 242 nonies P est abrogé. Ses notes (« Ne pas supprimer les données d’encaissement de 242 nonies P ») vont contre la réforme. La base formelle de cette obligation est le c du 6° de 242 nonies E, décret inchangé. La clause de 290 A, limitée au « fondement du présent article », ne l'atteint pas avec certitude. → RT-01.
- **242 nonies E** (annexe II, retained_unchanged) : le 8° maintient le recueil et la transmission des données de 290 et 290 A comme service obligatoire des plateformes agréées. Le 1° et le c du 6° visent encore 242 nonies J et P et la transmission des statuts à l'administration. **41 septies L et O** (annexe IV, inchangés) fixent encore le format et la globalisation des données de 290. → RT-02. Même mécanisme, hors paquet : le 7° de 242 nonies E (289 E) et 41 septies M (proposition qui fixe encore des délais pour les données de 242 nonies M).
- **Recodification.** D'après les NOTA LEGI, l'ordonnance n° 2025-1247 abroge 290 et 290 A au 1er janvier 2027, sauf maintien jusqu'à reprise par les mesures réglementaires de CIBS L. 215-39, L. 216-55 et L. 216-56. Le projet reconnaît dans ses notes que cette coordination n'est pas écrite. → RT-03, à confirmer : textes CIBS non lus.

Les autres alertes de ces clusters sont écartées. 242 nonies K et 1788 E citent 290 et 290 A pour interdire tout rétablissement : ce sont des renvois neutralisants.

### 4.3 Fiscalité locale (1641, 1587, 1530, 1407 ter, 1519 A, 1519 B, 1499 A, 1609 B, 1609 C, 1518 F)

Les abrogations comportent presque toutes une clause du type « Aucun renvoi au présent article ne peut fonder cette perception ». Les renvois restants sont de trois sortes :
- des exclusions ou minorations qui deviennent sans objet sans effet défavorable : 1518 quater IV, 1382-0 IV, 1518 A quinquies V, 1647 B sexies II, 1635 quinquies, 1636 B octies, 1507 ;
- des assiettes de crédit calculées sur des sommes effectivement prélevées, nulles pour les années nouvelles : 220 Z septies II ;
- des renvois transitoires : 1647-00 A, 1589, 1396, annexe II 311 A à C, 317 octies et 310 K bis.

Seul **1379**, inchangé et encore pending, énumère comme vivantes la redevance des mines (1519), les pylônes (1519 A), l'éolien en mer (1519 B) et le pouvoir d'instituer la taxe sur les friches commerciales (1530) → RT-04, P2.

Deux renvois ont été écartés mais méritent un nettoyage, sans objection (la clause de 1641 les neutralise) : **1530 bis V**, inchangé (« après déduction du prélèvement prévu au A du I et au II de l'article 1641 »), et **a4 155 bis A** (tarifs 2025).

Une contradiction interne aux notes ne se retrouve pas dans les textes : les notes de 1587 demandent de ne pas « supprimer la redevance communale autonome », alors que 1519 est abrogé dans l'instantané. Les abrogations de 311 A à C (« redevances communale et départementale ») sont cohérentes avec cet état.

### 4.4 Impôt sur le revenu et sur les sociétés (200-0 A, 231 quater, 209 quater, 54 quater, 168, 242 quinquies)

- **170, 1** (RT-05) et **1764 V** (RT-06) : contradictions textuelles neutralisées par la cible, mais maintenues dans des propositions réécrites. Le projet les avait lui-même repérées dans ses notes ; elles subsistent dans l'instantané.
- **36 de l'annexe II** (RT-08) : il règle encore le contenu du relevé de 54 quater, que la loi proposée supprime même pour les échéances expirées.
- Écartés : 39, 1, 4° et 31, I, 1°, c (exclusions de déduction des taxes de 231 quater), 208 septies (coordonné avec 209 quater), 1763 B (abrogé) et L136-6 II a du CSS (sommes imposées en application de 168, aucune pour les années nouvelles).

### 4.5 TVA (276)

**50 bis** (annexe IV, réécrit) conserve « les conditions de solvabilité et de solidarité prévues à l'article 276 ». **49**, inchangé, étend toujours 276 à d'autres franchises. Les notes de 276 qualifient elles-mêmes cette situation de « contradiction effective hors lot » → RT-07, P2 : 276 neutralise ses textes d'application.

### 4.6 Successions et enregistrement (655, 636, 742, 805, 1709, 1722 bis, 796-0 ter, 1135 bis, 1595)

Tous les renvois sont transitoires (décès ou actes antérieurs) ou coordonnés : 650, 652, 653, 662, 689, 743 bis, 990 I bis, 1840 G ter, et annexe III 267, 350 quindecies et 397. 171 quater de l'annexe II renvoie à la plage « 1701 à 1712 » pour le prélèvement de 244 bis A ; 1709 (paiement des droits de succession) n'y joue aucun rôle. Toutes ces alertes sont écartées.

### 4.7 Droits et contributions divers (1635 bis AE, 1635 bis AG, 1635 bis N, 958, 1609 untricies, 1613 quater, 234 quaterdecies, 238 bis HY, 1586 octies)

Écartés : les annexes sont abrogées de manière coordonnée (326 bis, 326 quater, 58 A, 381, 344 GD, 40 A m), et les renvois de 1647 III bis, L241-2 du CSS, 959, 302 decies et 238 bis HZ bis sont transitoires ou neutralisants.

### 4.8 Cluster CGI 199 (64 alertes)

Les 33 articles qui y renvoient (annexes II, III et IV, CGI, CCH, urbanisme) citent tous des articles 199 suffixés :

| Article réellement visé | Alertes |
|---|---|
| 199 novovicies | 32 |
| 199 terdecies-0 A | 11 |
| 199 terdecies-0 C | 7 |
| 199 terdecies-0 A bis | 5 |
| 199 septvicies | 2 |
| 199 undecies A | 2 |
| 199 terdecies-0 B, 199 terdecies-0 AA, 199 terdecies-0 AB, 199 undecies B, 199 decies I | 1 chacun |

Ce décompte retient le premier article suffixé du contexte de chaque alerte. Aucun de ces articles n'est abrogé par une formule explicite.

Une recherche sur tout le corpus courant ne trouve que deux homonymes : l'article 199 de la loi n° 2021-1104, cité par urba L151-6-1, et les articles 199 à 204 de l'annexe IV, cités par a4 193. **L'abrogation de 199 n'a aucun renvoi pendant.** Elle préserve l'article 193 et les conventions, ce qui va dans le sens de la faveur.

Côté inventaire, il faut corriger le résolveur de l'audit, qui tronque les suffixes latins (RT-09).

## 5. Propositions de correction (présentées séparément)

Ces corrections sont des propositions de la red-team. Elles ne figurent pas dans le corpus. Elles préservent les orientations retenues : suppression des formalités sans aucune formalité de remplacement, droits acquis et échéances anciennes.

### 5.1 RT-P1-CGI-A-01 : annexe IV, article 41 septies G (texte complet proposé)

> I. - Pour l'application du 6° de l'article 242 nonies E de l'annexe II au code général des impôts, les plateformes agréées mettent à disposition de leurs utilisateurs, lorsqu'il y a lieu, les informations relatives aux statuts suivants :
> 1° « Dépôt » correspondant à l'acceptation de la facture par la plateforme de l'émetteur ;
> 2° « Rejet » par la plateforme de l'émetteur ou du destinataire si les formats définis au 1° du I de l'article 41 septies C ou les contrôles visés à l'article 41 septies F ne sont pas conformes ;
> 3° « Refus » par le destinataire ;
> 4° « Encaissée » de la facture, lorsque l'émetteur choisit de le renseigner.
> II. - Les plateformes agréées mettent à jour les informations relatives aux statuts « dépôt » et « rejet » de la facture visés aux 1° et 2° du I. Elles permettent aux destinataires de mettre à jour les informations relatives au statut de traitement « refus » et aux émetteurs qui le souhaitent de mettre à jour le statut « encaissée ».
> III. - Les informations relatives aux statuts de traitement mentionnées aux I et II sont transmises par les plateformes agréées à la plateforme agréée de l'autre partie à la transaction, selon un format précisé par les spécifications externes publiées sur le site internet de l'administration fiscale.
> Pour les transmissions effectuées à compter de l'entrée en vigueur de la loi supprimant les transmissions prévues aux articles 289 E, 290 et 290 A du code général des impôts, par dérogation au c du 6° de l'article 242 nonies E de l'annexe II à ce code, aucune information relative aux statuts de traitement, y compris le statut « encaissée » et les données de paiement, n'est transmise à l'administration, même lorsqu'elle concerne une facture, une opération ou un paiement antérieurs. Aucune transmission de rattrapage ou de remplacement n'est exigée. La date de dépôt demeure le point de départ du délai défini au II de l'article 41 septies H. Les informations déjà transmises n'ont pas à être transmises à nouveau du seul fait de la réforme et conservent leurs garanties légales.

*Justification.* Cette rédaction aligne l'arrêté sur 290 A, sur 242 nonies P et sur le troisième alinéa du I de 289 bis. Elle conserve l'utilité commerciale des statuts entre les parties. *Dépendances.* RT-02 (le c du 6° de 242 nonies E doit être modifié au niveau du décret) ; audit 41 septies A I 3° g et spécifications externes, que les notes de 41 septies G signalent déjà.

### 5.2 RT-P1-CGI-A-02 : annexe II, article 242 nonies E (texte complet proposé)

> Les plateformes agréées sont tenues de proposer les services suivants :
> 1° Permettre à leurs utilisateurs de saisir, déposer, émettre ou transmettre leurs factures électroniques dans des conditions de nature à en garantir l'authenticité de l'origine, l'intégrité du contenu et la lisibilité ;
> 2° Effectuer les contrôles mentionnés à l'article 242 nonies K et identifier les destinataires des factures électroniques au moyen de l'annuaire central ;
> 3° Fournir et mettre à jour les informations relatives à leurs utilisateurs nécessaires au fonctionnement de l'annuaire central dans le respect des conditions prévues par l'article 242 nonies E bis ;
> 4° Assurer la transmission des factures électroniques aux plateformes agréées choisies par leurs destinataires, selon les modalités d'interopérabilité définies à l'article 242 nonies I et dans des conditions de nature à en garantir l'authenticité de l'origine, l'intégrité du contenu et la lisibilité à compter de leur émission jusqu'à la fin de la période de conservation ;
> 5° Recevoir et mettre à disposition de leurs destinataires les factures électroniques adressées par les autres plateformes agréées ;
> 6° Assurer la gestion des statuts de traitement des factures électroniques en garantissant :
> a) La mise à disposition à leurs utilisateurs des informations relatives à ces statuts ;
> b) La possibilité pour leurs utilisateurs de mettre à jour les informations relatives aux statuts de traitement lorsqu'il y a lieu ;
> c) La transmission des informations relatives aux statuts de traitement aux plateformes agréées des parties aux transactions ;
> 7° (Abrogé) ;
> 8° (Abrogé).
> Les modalités d'application du présent article sont précisées par arrêté du ministre chargé du budget.
> Le retrait, au 1°, de la mention des données des articles 242 nonies J et 242 nonies P, la suppression, au c du 6°, de la transmission à l'administration et l'abrogation des 7° et 8° prennent effet, pour chaque flux, à l'entrée en vigueur de la loi supprimant la transmission prévue, selon le cas, à l'article 289 E, 290 ou 290 A du code général des impôts. Ils s'appliquent aux transmissions restant à effectuer à cette date, y compris pour des factures, opérations ou paiements antérieurs. Aucun service, contrôle ni condition d'immatriculation ne peut être fondé sur ces flux supprimés. Les données déjà transmises conservent leurs garanties légales de protection et d'accès.

Annexe IV, articles 41 septies L et 41 septies O : abrogation selon la formule de 242 nonies M et P proposés (« Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les transmissions fiscales prévues à l'article 290 [290 A] du code général des impôts [...] Cette suppression s'applique également aux transmissions restant à effectuer à cette date [...] »).

*Justification.* Le décret garde intacts tous les services d'échange de factures et retire seulement les flux que la loi supprime. Les dates restent liées à chaque loi de suppression, comme pour 242 nonies J, M à P. *Dépendances.* 41 septies M (annexe IV), même mécanisme, à abroger ; 242 nonies A et B (conditions d'immatriculation), non lus ici.

### 5.3 RT-P1-CGI-A-03 : coordination CIBS (disposition de la loi de réforme, hors des cinq codes)

Principe : une disposition expresse supprime, dans le CIBS et dans le tableau de l'article 15 de l'ordonnance n° 2025-1247, les obligations de transmission correspondant à 289 E, 290 et 290 A, ainsi que leurs mesures réglementaires de reprise. Elle reprend la transition des propositions : transmissions restant à effectuer comprises, ni rattrapage ni remplacement, loi répressive plus douce. Je ne propose pas de rédaction, faute d'avoir lu les articles L. 215-39, L. 216-55 et L. 216-56 du CIBS dans leur version au 18 octobre 2026 : en écrire une reviendrait à inventer leur contenu.

### 5.4 RT-P1-CGI-A-04 : CGI 1379 (alinéa à ajouter à la fin)

> III. – Les mentions, aux 6° à 8° du I et au 3° du II, des impositions prévues aux articles 1519, 1519 A, 1519 B et 1530 ne valent que pour les impositions établies au titre des années antérieures à leur suppression. Elles ne permettent ni l'institution ni la perception de ces impositions pour les années auxquelles cette suppression s'applique.

Nettoyage connexe recommandé, sans objection : dans 1530 bis V, après « après déduction du prélèvement prévu au A du I et au II de l'article 1641 du présent code », ajouter « au titre des années pour lesquelles ce prélèvement demeure dû ».

### 5.5 RT-P1-CGI-A-05 : CGI 170, 1 (premier alinéa)

> 1. En vue de l'établissement de l'impôt sur le revenu, toute personne imposable audit impôt est tenue de souscrire et de faire parvenir à l'administration une déclaration détaillée de ses revenus et bénéfices, de ses charges de famille et des autres éléments nécessaires au calcul de l'impôt sur le revenu, dont notamment ceux qui servent à la détermination du prélèvement prévu à l'article 204 A. Pour l'imposition des revenus des années antérieures à la suppression du plafonnement global prévu à l'article 200-0 A, la déclaration comporte en outre les éléments nécessaires à ce plafonnement.

### 5.6 RT-P1-CGI-A-06 : CGI 1764 V (second alinéa)

> Le V ne s'applique, en ce qui concerne l'article 231 ter, qu'aux engagements se rapportant à une exonération d'une taxe légalement due au titre d'une période antérieure à la suppression de cette taxe. Il en va de même, en ce qui concerne l'article 231 quater, pour les engagements se rapportant à une exonération de la taxe légalement due au titre d'une année antérieure à la suppression de cette taxe. Aucun manquement à un engagement relatif à une période pour laquelle l'une de ces taxes est supprimée ne peut donner lieu à la majoration. Les exonérations et autres avantages applicables aux périodes antérieures, ainsi que les créances, restitutions, prescriptions et recours, demeurent régis par leurs règles propres, sous réserve des dispositions répressives plus douces.

### 5.7 RT-P1-CGI-A-07 : annexe IV, articles 49, 50 et 50 bis

- 50 bis, dernière phrase : « Les conditions de solvabilité et de solidarité prévues à l'article 276 du code général des impôts, dans sa rédaction antérieure à son abrogation, ne demeurent applicables qu'aux cautionnements garantissant des produits reçus avant cette abrogation. »
- 49 et 50, alinéa ajouté : « Le présent article ne s'applique qu'aux produits reçus avant l'entrée en vigueur de la loi abrogeant l'article 276 du code général des impôts. Aucune caution ne peut être exigée sur son fondement pour les réceptions postérieures. »

### 5.8 RT-P1-CGI-A-08 : annexe II, article 36 (texte complet proposé)

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant le relevé prévu à l'article 54 quater du code général des impôts. Aucun relevé, renseignement ni report ne peut être exigé sur son fondement à compter de cette date, y compris pour un exercice antérieur ou une échéance expirée. Les relevés déjà déposés n'ont pas à être refaits. Les manquements antérieurs restent régis par les règles applicables à leur date, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives.

### 5.9 RT-P1-CGI-A-09 : outil d'audit

Le résolveur doit conserver les suffixes (« novovicies », « terdecies-0 A bis », « septvicies », etc.) avant la correspondance avec un article cible. Il faut ensuite relancer le contrôle des renvois vers 199 novovicies et les articles voisins, qui n'ont pas été rapprochés de leur propre statut.

## 6. Incertitudes restantes et éléments non examinés

- **Textes extérieurs non lus** (réserves documentaires) : CIBS L. 215-39, L. 216-55 et L. 216-56 ; ordonnance n° 2025-1247 (articles 9, 15 et 49) ; ordonnance n° 2022-306 (affectation de 231 quater). Aucune consultation de Légifrance n'a été faite.
- **Versions à fin programmée.** Les sources de 231 quater, 1519 A et 1519 B prennent fin au 1er janvier 2027, et celle de 1613 quater aussi (ABROGE_DIFF). 290, 290 A et 289 bis courent jusqu'au 2222-02-22. Leurs successeurs ne sont pas identifiés dans le paquet ; la question des versions concurrentes reste hors périmètre.
- **Seconde passe.** Plusieurs articles qui renvoient sont encore `pending`, dont 1379, 1530 bis, 1764, 170 (completed), 1640 et 1647 : la seconde passe peut y apporter les coordinations proposées. Mes conclusions sont provisoires.
- **Non lus intégralement :** CGI 31 et CGI 39 (passages pertinents seulement) et les 33 textes du cluster 199 (extraction exhaustive des occurrences seulement).
- **Hors paquet mais signalés :**
  - 242 nonies E 7° (289 E) et 41 septies M (annexe IV), même mécanisme que RT-02 ;
  - annexe III 40 A h, qui mentionne encore les recettes soumises à la contribution de 234 nonies ;
  - annexe III 267, qui renvoie encore à 1595 bis « dans le champ propre » ;
  - 4 J (annexe IV), sur le relevé de 238 A.
  Je ne les ai pas qualifiés.
- **Non examinés au fond :** l'opportunité des abrogations elles-mêmes, la conformité au droit de l'Union (directive TVA 2006/112/CE, notamment ses éventuelles exigences futures de déclaration numérique) et les pertes de recettes. Les notes du projet les signalent comme non chiffrées.

