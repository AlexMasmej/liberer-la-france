# Dossier INV : anomalies de version de l'inventaire et effets sur les propositions

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z`, date de référence du corpus : 18 octobre 2026. Rapport rédigé le 26 octobre 2026.
Préfixe des objections : RT-INV-xx. Livrable structuré : `reports/dossiers/INV.json`.

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste. La seconde passe continue en production : les conclusions sont provisoires et portent sur l'instantané.

## 1. Résumé

| Priorité | confirmé | à confirmer | faux positif | Total |
|---|---|---|---|---|
| P0 | 2 | 0 | 0 | 2 |
| P1 | 4 | 0 | 0 | 4 |
| P2 | 4 | 2 | 2 | 8 |
| **Total** | 10 | 2 | 2 | **14** |

Les trois constats les plus importants :

1. **RT-INV-01 (P0)** : CGI 1609 quinvicies. L'article est abrogé depuis le 1er janvier 2022 (ordonnance 2021-797). L'inventaire retient une version mort-née. Sa proposition rétablit « Il est institué une contribution supplémentaire à l'apprentissage », alors que le projet supprime cette même contribution à L6242-1 du code du travail.
2. **RT-INV-02 (P0)** et **RT-INV-03 (P1)** : réforme AT-MP au 1er novembre 2026. Neuf réécritures CSS partent des versions qui cessent ce jour-là et ignorent les remplacements publiés, présents dans le corpus. Le cas le plus grave est L434-1 : la proposition perd la part fonctionnelle de l'indemnité en capital. L461-1 perd la reconnaissance sur avis de deux médecins-conseils à compter du 1er janvier 2027.
3. **RT-INV-05 (P1)**, défaut de méthode : sur 650 entrées ABROGE_DIFF, 379 sont en réalité des **remplacements différés**, avec une version VIGUEUR_DIFF de même numéro qui commence à leur date de fin. Aucune des 519 versions VIGUEUR_DIFF du corpus n'est dans l'inventaire. 215 réécritures portent sur un texte dont le successeur est déjà publié, et au moins 60 notes de revue affirment à tort que ce successeur « n'est pas fourni ». S'y ajoute **RT-INV-06 (P1)** : la recodification de la TVA dans le CIBS au 1er janvier 2027 abroge 169 articles CGI de l'inventaire, dont 70 réécrits. Le CIBS n'est ni dans le corpus ni dans la liste des coordinations hors corpus.

Couverture réelle :

- Lus en entier par `cite.py`, toutes versions : les 3 numéros à versions concurrentes, les 3 annexes du code du travail, les 12 articles d'état anormal, les 10 réécritures dont l'abrogation tombe en 2026 et leurs successeurs, les 3 CCH sans lot, L6242-1 du code du travail et un échantillon de 17 entrées de janvier 2027.
- Lus par différences mot à mot entre source, successeur et proposition : les 45 entrées de 2026 dans leur ensemble.
- Traités seulement par requête : les 337 entrées de janvier 2027 et les 650 ABROGE_DIFF, en dehors de l'échantillon.

## 2. Périmètre réellement lu

Toutes les pièces ont été exportées par `tools/cite.py` dans `evidence/cited/20261026T230545Z/`. Liste des articles et versions :

- **Versions concurrentes.**
  - travail R5221-22 : 018525750, 024540531, 043320687, 042947235, 052536486. Lecture complémentaire de R5221-20 049999760.
  - css R611-2 : les 10 versions, dont 036704272, 039278160, 043292679.
  - a3 382-0 C bis : 034729420, 036256024, avec leurs documents XML LEGI (VERSIONS, LIENS).
- **Annexes du code du travail.**
  - « Annexe » : 018524217 (historique), 036483371 (modèles de convention D6122), 038591641 (référentiel qualité) et 054612711 (successeur au 1er novembre 2026).
  - « Annexe I » : 023018849, 040477365 (rayonnements optiques), 038137262 et 047548258 (index égalité).
  - « Annexe II » : 023018851 (rayonnements optiques), 038137266 et 047548249 (index égalité).
- **États anormaux.**
  - cgi 302 J : 006304989, 021664265.
  - cgi 1609 quinvicies : les 11 versions.
  - travail L6242-1 : 048839886.
  - travail R4451-39 : 022442755, 037024754, 047715485.
  - css (état vide) : L381-32 047452607, R381-5 047961931, R381-6 047961920, R381-7 047961910, R381-8 047961900, R381-9 047961889, D381-4 047961286, D381-5 047961281, D643-14 047634694, avec leurs versions antérieures.
- **Abrogations ou remplacements de 2026 réécrits**, source, successeur et proposition lus en entier : css L142-1, L351-3, L434-1, L434-16, L443-1, L461-1 (deux successeurs), R351-12 (deux successeurs identiques), R351-37, R434-32, et travail Annexe 038591641. Lectures complémentaires : css L434-2 et son successeur 051288493, L431-1, L452-2.
- **Échantillon de janvier 2027**, lu en entier (source, successeur, proposition, motif, notes) :
  - cgi : 1824, 256-0, 1407 bis, 39, 200, 244 quater C, 293 D. CGI 279, 283 bis et 296 ter ont été exportés mais seuls leur état et leur acte abrogatif ont été examinés ; CGI 1695 ter et 1695 quater sont hors inventaire.
  - travail : L3332-17-1, L6323-13, R4216-28. R4214-28 est hors inventaire.
  - css : L162-30-2, L137-26, L223-9.
  - urba : L112-16.
  - cch : L313-4, D824-15, R824-11.
- **CCH sans lot** : D304-1 038970859, D319-6 038972909 et 049356983, D319-7 038972915 et 049356981.
- **Hors inventaire** : cgi 302 B, 591, 1954, 322 ; travail R4623-29 ; css L161-24-1 (4 versions).

Rapports du coordinateur utilisés : `reports/consistency-20261026T230545Z.json` et `reports/concurrent-in-force-20261026T230545Z.json`. Orientations utilisées : `policy-coordinations.json` et `site-summaries.json`, recherche ciblée.

Consultations extérieures, toutes le 26 octobre 2026 :

- Légifrance, `legifrance.gouv.fr/codes/article_lc/LEGIARTI000036256024` : HTTP 403. Pas de contournement ; aucune autre consultation de Légifrance.
- BOFiP BOI 14901-PGP, publié le 07/10/2026 : doctrine administrative, source secondaire.
- Une recherche web pour identifier l'ordonnance 2025-1247.

## 3. Méthode

1. Pour chaque numéro, j'ai reconstitué la chaîne des versions à partir des documents XML LEGI de l'instantané : balises VERSIONS, ETAT, DATE_FIN et liens `sens="cible"` de type CREE, MODIFIE, ABROGE ou DEPLACE.
2. La version réellement en vigueur est déduite de l'acte modificatif le plus récent et de l'état LEGI. Une borne de fin 2999 sur une version MODIFIE est traitée comme un défaut de clôture de DILA.
3. Pour les versions concurrentes, j'ai comparé les empreintes des propositions (SHA-256 du `proposed_xml`), puis les textes.
4. Pour les entrées ABROGE_DIFF, j'ai recherché une version VIGUEUR_DIFF de même numéro qui commence à la date de fin. Lorsqu'elle existe, j'ai fait une comparaison mot à mot (difflib) entre source et successeur, puis entre source et proposition, et lu les motifs et notes.
5. Requêtes globales en lecture seule (`mode=ro`, `query_only`) : classement des 650 ABROGE_DIFF par date, code, statut, existence d'un successeur et acte abrogatif ; contrôle du périmètre (articles en vigueur par leurs dates mais absents de l'inventaire) ; rattachement aux sections (SECTION_TA).
6. Les nombres obtenus par expression régulière sont présentés comme des minima. Il s'agit des notes qui nient l'existence d'un successeur et des corps qui insèrent une clause d'abrogation.

## 4. Constats

### 4.1 Point 1 : numéros à deux versions ouvertes au 18 octobre 2026

| Numéro | Version réellement en vigueur | Version fantôme | Propositions | Conclusion |
|---|---|---|---|---|
| travail R5221-22 | **052536486** (VIGUEUR depuis le 1er mai 2021, consolidation DILA corrigée : 1er alinéa issu du décret 2021-360, renvoi L435-3 issu du décret 2020-1734) | 043320687 (MODIFIE, décret 2021-360, borne non close) ; 042947235 mort-née | identiques (empreinte 931f415e…) | Pas de divergence de fond. Double comptage (RT-INV-07). La rédaction « situation de l'emploi » est discutable (RT-INV-08). |
| css R611-2 | **043292679** (décret 2021-300, 1er janvier 2023) | 036704272 (décret 2018-174), remplacé dès le 26 octobre 2019 par 039278160 | deux retained_unchanged sans corps, **motifs incompatibles** : « quinze jours… puis du mois » contre « six mois, mois d'opposition » | Le lecteur affiche deux textes « maintenus », dont l'un est abrogé (RT-INV-07). |
| a3 382-0 C bis | **036256024** (modifié par le décret 2017-1750 avant l'entrée en vigueur du 1er janvier 2019) | 034729420 (créé par le décret 2017-975, avec l'exclusion de la CFE au II) | identiques (empreinte b8df2d50…) ; proposition conforme à 036256024 | Le « conflit préexistant non résolu » invoqué par les notes se résout par les liens LEGI (RT-INV-07). |

**Annexes du code du travail.** Ce ne sont pas de vrais doublons (RT-INV-09, faux positif) :

- « Annexe » désigne deux annexes distinctes : les modèles de convention de D6122-4 et D6122-5, et le référentiel national qualité du chapitre VI.
- « Annexe I » et « Annexe II » désignent chacune deux annexes : l'une sur les rayonnements optiques artificiels, l'autre sur l'index de l'égalité professionnelle. Les versions 2029 de l'index (décret 2023-370, DEPLACE) ont un texte identique aux versions actuelles.

Un vrai problème se cache toutefois derrière : le référentiel qualité est remplacé le 1er novembre 2026 (RT-INV-04).

### 4.2 Point 2 : articles d'état anormal

| Article | En vigueur au 18 octobre 2026 ? | Proposition | Objection |
|---|---|---|---|
| cgi 302 J 021664265 | Non : ETAT ABROGE (ordonnance 2021-1843, art. 10), mais borne 2222-02-22 incohérente | retained_unchanged ; le motif exclut expressément tout rétablissement | RT-INV-10 (P2) |
| cgi 1609 quinvicies 042914206 | **Non** : article abrogé le 1er janvier 2022 (ordonnance 2021-797, art. 6) ; la version retenue est mort-née | **rewrite_draft qui réinstitue la CSA** | **RT-INV-01 (P0)** |
| travail R4451-39 037024754 | Oui, jusqu'au 1er juillet 2027. MODIFIE est l'état LEGI ordinaire d'une version au remplacement programmé | retained_unchanged ; successeur 047715485 sans décision | RT-INV-11 (P2, alerte) |
| css L381-32, R381-5 à R381-9, D381-4, D381-5, D643-14 | Oui, en toute vraisemblance : articles créés en 2023 (loi 2023-270, décrets 2023-752, 2023-754, 2023-436), sans lien ABROGE, borne 2999, ETAT LEGI vide | 6 maintiens et 3 réécritures sur les bons textes | RT-INV-12 (faux positif) |

### 4.3 Point 3 : abrogations différées

**Répartition des 650 ABROGE_DIFF de l'inventaire** par mois de fin, avec existence d'un successeur VIGUEUR_DIFF de même numéro à la même date :

| Fin | Total | avec successeur | rewrite_draft | retained_unchanged |
|---|---|---|---|---|
| 2026-11 | 42 | 42 | 10 | 32 |
| 2026-12 | 3 | 3 | 0 | 3 |
| 2027-01 | 337 | 174 | 156 | 181 |
| 2027-02 à 2027-12 | 15 | 15 | 7 | 8 |
| 2028 | 51 | 42 | 26 | 25 |
| 2029 | 78 | 77 | 42 | 36 |
| 2030-2031 | 18 | 10 | 17 | 1 |
| 2222-02-22 (borne technique) | 106 | 16 | 69 | 37 |

**Les 45 entrées de 2026** sont toutes des remplacements, pas des abrogations sèches.

- **Bloc AT-MP, 42 entrées au 1er novembre 2026** (loi 2025-199, art. 90 ; décrets 2026-354 et 2026-355 du 7 mai 2026).
  - **Réécritures (9)** : L142-1, L351-3, L434-1, L434-16, L443-1, L461-1, R351-12, R351-37, R434-32.
  - **Maintiens (32)** : D242-34, D242-6-19, D242-6-5, D242-6-6, D242-6-7, D351-1-10, D351-1-9, D432-15, D434-1, D434-2, D434-3-1, L431-1, L434-15, L434-17, L434-2, L452-2, L452-3, R173-3-1, R434-1, R434-1-1, R434-1-2, R434-1-3, R434-2, R434-2-1, R434-21, R434-28, R434-3, R434-34, R434-4, R434-5, R443-7, R461-8.
  - Les successeurs introduisent l'« incapacité permanente professionnelle », la part fonctionnelle et les nouveaux renvois (L434-1 A, I à III de L434-2).
- **travail Annexe (référentiel qualité), 1er novembre 2026** : décret 2026-728 ; rewrite_draft.
- **Décembre 2026** : css L243-7-7 (25 décembre), travail L8222-2 et L8271-9 (26 décembre). Ces trois entrées viennent de la loi 2026-534 du 25 juin 2026, art. 95 ; ce sont des maintiens.

Examen des 10 réécritures de 2026 : aucune ne connaît la version de remplacement. Les notes de L142-1, L351-3, L443-1, L461-1 et L434-1 affirment que ce successeur n'est pas fourni, alors qu'il figure dans l'instantané. Les propositions **n'ignorent pas l'échéance**, puisqu'elles la citent, mais elles la prennent pour une abrogation. Elles **ressuscitent implicitement l'ancienne rédaction** si elles sont adoptées après le 1er novembre 2026, et entrent en **conflit avec le texte de remplacement publié**. Détails :

- **L434-1** : perte de la part fonctionnelle (RT-INV-02).
- **L461-1** : perte de la voie des deux médecins-conseils au 1er janvier 2027 et renvoi « septième » erroné (RT-INV-02).
- **L142-1, L351-3, L443-1, R351-12** : terminologie et renvois périmés (RT-INV-03).
- **L434-16** : la proposition déclare une « date d'abrogation » qui n'existe pas (RT-INV-03).
- **R434-32** : la proposition rétablit l'alinéa des barèmes supprimé et le taux unique (RT-INV-03).
- **R351-37** : compatible pour l'essentiel, car le renvoi au I de L351-1-4 neutralise le changement de L434-2 vers L434-1 A.
- **Annexe qualité** : les indicateurs 2026, dont le nouvel indicateur 33, sont perdus (RT-INV-04).

**Janvier 2027, 337 entrées.** Répartition par code et statut :

- cgi : 211 (109 réécritures, 102 maintiens) ;
- travail : 54 (14 réécritures) ;
- cch : 48 (17 réécritures) ;
- css : 22 (14 réécritures) ;
- urba : 2 (2 réécritures).

Les actes abrogatifs dominants sont :

- l'ordonnance 2025-1247, recodification de la TVA : 99 entrées ;
- le décret 2025-1100 : 37 entrées, toutes R4216-1 à R4216-34 du code du travail (sécurité incendie des lieux de travail), transférées vers le CCH selon les notes de R4216-28 ;
- le décret 2026-84, procédure d'impayés d'aides au logement : 20 entrées (CCH R824-17 à R824-33, D824-15, D824-34, D863-10) ;
- divers actes de 2025 et 2026 (LFI 2026, LFSS 2026, loi 2026-403).

172 entrées n'ont qu'un lien implicite, par remplacement.

Échantillon examiné : 17 entrées, voir § 2. Typologie observée :

- **Clause de bornage** (« s'applique jusqu'au 31 décembre 2026 », « ne proroge pas ») : CCH L313-4, R824-11, D824-15, CGI 256-0, travail R4216-28. Prudent, mais la réforme n'a d'effet que si la loi du projet entre en vigueur avant 2027.
- **Ignorance d'un successeur au contenu différent** :
  - travail L3332-17-1 (ESUS, loi 2026-403) ;
  - css L223-9 (7,75 % devient 7,93 %) ;
  - CGI 200 et 39, css L137-26, travail L6323-13 (renvois au CIBS) ;
  - CCH R824-11 (décret 2026-84).
- **Anticipation correcte** : urbanisme L112-16, déjà coordonné avec L6360-1 du code des transports ; CGI 293 D, dont les notes situent la reprise dans le CIBS.
- **Abrogation sèche sans successeur, avec suppression proposée cohérente** : CGI 1824, 1407 bis, 244 quater C ; css L162-30-2 (le CAQES devient volontaire, avec une demande expresse de coordination de l'article 79 de la LFSS 2026, hors corpus).

Non examiné dans les 337 : 320 entrées, dont environ 140 réécritures. En particulier :

- plus de 90 autres articles CGI abrogés par l'ordonnance 2025-1247 (279, 283 bis et 296 ter n'ont pas été lus sur le fond) ;
- les 36 autres articles du décret 2025-1100 ;
- les 18 autres articles du décret 2026-84 ;
- les entrées CSS de la LFSS 2026 autres que L162-30-2.

### 4.4 Point 4 : les 3 CCH sans lot

D304-1, D319-6 et D319-7 sont en vigueur, et leur proposition est liée à la bonne source : l'empreinte de source de `drafts` est égale à celle de l'article. Mais :

- aucun lot ni registre ne les possède ;
- elles n'ont ni `substantive_impact` ni `reference_checks` ;
- leur motif est purement stylistique (« Réécriture intégrale en formulation active »), ce qui contredit l'instruction du 19 octobre ;
- l'inventaire les marque `independent_second_pass_required`.

Conséquence documentaire : ces propositions sont publiées et comptées, mais elles échappent aux gardes et à la reprise. Leur provenance n'est pas traçable (RT-INV-13).

### 4.5 Constat complémentaire : périmètre de l'inventaire

44 versions sont en vigueur selon leurs dates au 18 octobre 2026 sans figurer dans l'inventaire :

- 9 fantômes DILA ;
- 7 articles orphelins ou situés dans des sections closes, dont CGI 1695 ter et 1695 quater, en vigueur jusqu'au 1er janvier 2027 ;
- 28 articles CGI à borne 2222.

La règle de sélection suit l'arborescence. Elle est défendable, mais elle n'est pas documentée, et les fantômes sont traités de façon inégale (RT-INV-14).

## 5. Propositions de correction (présentées séparément)

### C-01 : CGI 1609 quinvicies (RT-INV-01)

Retirer la proposition. Texte à afficher, non normatif :

> Article abrogé par l'article 6 de l'ordonnance n° 2021-797 du 23 juin 2021, à compter du 1er janvier 2022. La contribution supplémentaire à l'apprentissage est régie par l'article L. 6242-1 du code du travail.

Justification : la version LEGIARTI000042914206 n'a jamais été en vigueur. La coordination contrat unique est déjà dans L6242-1 proposé (II 1° et V).
Dépendance : L6242-1 (travail), L6241-2, L6131-1.

### C-02 : CSS L434-1, à rebaser sur LEGIARTI000051288500 (RT-INV-02)

> Une indemnité en capital est attribuée à la victime d'un accident du travail atteinte d'une incapacité permanente professionnelle inférieure à un pourcentage déterminé. Elle est constituée :
> 1° D'une part professionnelle correspondant à la perte de gains professionnels et à l'incidence professionnelle de l'incapacité. Son montant est déterminé, en fonction du taux d'incapacité permanente professionnelle de la victime, par un barème forfaitaire fixé par décret et revalorisé au 1er avril de chaque année par application du coefficient mentionné à l'article L. 161-25. Elle est révisée lorsque le taux d'incapacité permanente professionnelle de la victime augmente tout en restant inférieur à un pourcentage déterminé. Cette part est due même si la consolidation intervient alors que la victime est bénéficiaire d'une pension de retraite ;
> 2° D'une part fonctionnelle correspondant au déficit fonctionnel permanent de la victime. Son montant est égal au nombre de points d'incapacité permanente fonctionnelle multiplié par un pourcentage d'une valeur de point fixée par un référentiel prenant en compte l'âge de la victime. Ce pourcentage et ce référentiel sont définis par arrêté des ministres chargés du travail et de la santé. Cet arrêté définit également les conditions dans lesquelles ce référentiel est actualisé. Le montant de cette part est révisé lorsque le taux d'incapacité permanente fonctionnelle de la victime augmente.
> Cette indemnité est versée dès la notification de la décision qui l'attribue, sans attendre que cette décision soit devenue définitive. L'exercice d'un recours ne suspend pas ce versement. Lorsque la victime dispose d'un choix entre une rente et une indemnité en capital, le versement du capital intervient après qu'elle a choisi cette indemnité ou, à défaut de choix, à l'expiration du délai qui lui est ouvert pour exercer cette option ; l'attente du caractère définitif de la décision n'est pas exigée. Elle est incessible et insaisissable.
> La suppression de l'attente du caractère définitif de la décision s'applique aux deux parts de l'indemnité. Elle s'applique également aux indemnités en capital dues, en application de la rédaction antérieure du présent article, aux victimes dont l'état a été consolidé avant la date fixée en application du V de l'article 90 de la loi n° 2025-199 du 28 février 2025, lorsqu'elles n'ont pas encore été versées à l'entrée en vigueur de la loi portant la présente modification. Elle ne modifie ni le montant dû, ni la revalorisation ou la révision, ni les règles de prescription, de recours et de récupération des indus applicables. Aucun second versement n'est dû au titre d'une indemnité déjà payée.

Justification : ce texte conserve la réforme du projet (paiement à la notification) et la loi de 2025, y compris la part fonctionnelle et la part professionnelle due aux retraités. Le régime ancien reste celui du V de l'article 90.
Dépendances : L434-1 A, L434-2 (successeur 051288493, retained_unchanged à rebaser), R434-4 (option), D434-1 (successeur).

### C-03 : CSS L461-1, à rebaser sur LEGIARTI000053285169, version du 1er janvier 2027 (RT-INV-02)

Reprendre intégralement le texte du successeur au 1er janvier 2027 avec la seule coordination propre au projet. À l'avant-dernier alinéa, remplacer « dans les mêmes conditions que celles fixées à l'article L. 315-1 » par « dans les mêmes conditions que celles fixées au I de l'article L. 315-2 ». Le texte complet :

> Les dispositions du présent livre sont applicables aux maladies d'origine professionnelle sous réserve des dispositions du présent titre. En ce qui concerne les maladies professionnelles, est assimilée à la date de l'accident :
> 1° La date de la première constatation médicale de la maladie ;
> 2° Lorsqu'elle est postérieure, la date qui précède de deux années la déclaration de maladie professionnelle mentionnée au premier alinéa de l'article L. 461-5 ;
> 3° Pour l'application des règles de prescription de l'article L. 431-2, la date à laquelle la victime est informée par un certificat médical du lien possible entre sa maladie et une activité professionnelle.
> Est présumée d'origine professionnelle toute maladie désignée dans un tableau de maladies professionnelles et contractée dans les conditions mentionnées à ce tableau. Un décret en Conseil d'Etat, pris après avis des organisations syndicales de salariés et d'employeurs représentatives au niveau national, détermine les modalités générales d'établissement du diagnostic de ces maladies, qui tiennent compte des données acquises de la science.
> Si seule la condition tenant au délai de prise en charge n'est pas remplie, la maladie désignée dans un tableau de maladies professionnelles peut être reconnue d'origine professionnelle, après avis d'au moins deux médecins conseils recueilli dans des conditions fixées par décret, lorsqu'il est établi qu'elle est directement causée par le travail habituel de la victime. L'avis des médecins conseils s'impose à la caisse.
> Si une condition tenant à la durée d'exposition ou à la liste limitative des travaux ou plusieurs conditions tenant au délai de prise en charge, à la durée d'exposition ou à la liste limitative des travaux ne sont pas remplies, la maladie telle qu'elle est désignée dans un tableau de maladies professionnelles peut être reconnue d'origine professionnelle lorsqu'il est établi qu'elle est directement causée par le travail habituel de la victime.
> Peut être également reconnue d'origine professionnelle une maladie caractérisée non désignée dans un tableau de maladies professionnelles lorsqu'il est établi qu'elle est essentiellement et directement causée par le travail habituel de la victime et qu'elle entraîne le décès de celle-ci ou une incapacité permanente professionnelle d'un taux évalué dans les conditions mentionnées au deuxième alinéa de l'article L. 434-1 A et au moins égal à un pourcentage déterminé.
> Dans les cas mentionnés aux deux alinéas précédents, la caisse primaire reconnaît l'origine professionnelle de la maladie après avis motivé d'un comité régional de reconnaissance des maladies professionnelles. La composition, le fonctionnement et le ressort territorial de ce comité ainsi que les éléments du dossier au vu duquel il rend son avis sont fixés par décret. L'avis du comité s'impose à la caisse dans les mêmes conditions que celles fixées au I de l'article L. 315-2.
> Les pathologies psychiques peuvent être reconnues comme maladies d'origine professionnelle, dans les conditions prévues aux huitième et avant-dernier alinéas du présent article. Les modalités spécifiques de traitement de ces dossiers sont fixées par voie réglementaire.

Dépendances : R142-17-2, R461-8 et D461-27, qui visent les sixième, septième et huitième alinéas et dont la numérotation est à recaler après l'insertion. Décret relatif à l'avis des deux médecins-conseils. Pour la période intermédiaire (successeur 053285183, du 1er novembre au 31 décembre 2026), seuls « professionnelle » et le renvoi à L434-1 A changent.

### C-04 : autres articles AT-MP (RT-INV-03), passages corrigés

- **L142-1**, sur la base de 051288452 : 5° « A l'état d'incapacité permanente, notamment aux taux de cette incapacité, en cas d'accident du travail ou de maladie professionnelle ; ». Conserver les 2°, 3° et la clause finale du projet.
- **L351-3**, sur la base de 051288449 : 1° « …les travailleurs salariés ont perçu une rente d'accident du travail prenant effet antérieurement à la date susmentionnée, pour une incapacité permanente professionnelle au moins égale à un taux fixé par le même décret ; ». Conserver la clause finale du projet.
- **L434-16**, sur la base de 051288487 : 1er alinéa « …compte tenu du III de l'article L. 434-2. » ; 3e alinéa « …si son salaire annuel est supérieur au salaire minimum déterminé au premier alinéa du présent article… ». **Supprimer** la phrase « La présente rédaction ne modifie ni la date d'abrogation du présent article déjà fixée au 1er novembre 2026… ».
- **L443-1**, sur la base de 051288476 : 4e alinéa « …admise au bénéfice des dispositions du II de l'article L. 434-2… ». Conserver les deux ajouts du projet (dispense d'intervalle pour les demandes d'augmentation et transition).
- **R351-12**, sur la base de 054060166 : au 5°, « …une rente pour une incapacité permanente professionnelle au moins égale à 66 % ». Conserver la réforme du projet sur la mention préalable au compte.
- **R434-32**, sur la base de 054060111 :

> Au vu de tous les renseignements recueillis, la caisse primaire se prononce sur l'existence d'une incapacité permanente et, le cas échéant, sur les taux d'incapacité permanente professionnelle et fonctionnelle de celle-ci et sur le montant de la rente due à la victime ou à ses ayants droit.
> La décision motivée fixant les deux taux d'incapacité est immédiatement notifiée par la caisse primaire par tout moyen permettant de déterminer la date de réception, avec mention des voies et délais de recours, à la victime ou à ses ayants droit et à l'employeur au service duquel se trouvait la victime au moment où est survenu l'accident. Le double de cette décision est envoyé à la caisse d'assurance retraite et de la santé au travail.
> La notification adressée à la victime ou à ses ayants droit invite ceux-ci à faire connaître à la caisse, sans condition de délai ni de formulaire, s'ils demandent l'envoi, soit à eux-mêmes, soit au médecin que désignent à cet effet la victime ou ses ayants droit, d'une copie du rapport médical prévu au cinquième alinéa de l'article R. 434-31.
> La caisse procède à cet envoi dès réception de la demande, en indiquant que la victime, ses ayants droit ou le médecin désigné à cet effet peuvent, sans limitation à un délai de quinzaine suivant la réception du rapport, prendre connaissance au service du contrôle médical de la caisse des autres pièces médicales.
> Ces dispositions s'appliquent aux demandes d'accès au rapport et aux autres pièces médicales présentées à compter de l'entrée en vigueur du présent décret, y compris pour une décision antérieure. Elles ne rouvrent ni ne prolongent les délais de recours contre la décision. Les demandes déjà présentées restent valables sans renouvellement.

- **R351-37** : aucune correction de fond. Le renvoi proposé au I de L351-1-4 est compatible avec le successeur.

### C-05 : référentiel qualité, travail Annexe (RT-INV-04)

Base : texte intégral de LEGIARTI000054612711 (indicateurs 1 à 33, inchangés). Remplacer le seul II, 2 par :

> 2. Procédure et cycle de la certification
> La procédure de certification repose sur un audit initial et sur des audits de surveillance organisés selon des cycles de trois années, selon des modalités précisées par arrêté du ministre chargé de la formation professionnelle. La certification n'est soumise ni à expiration périodique ni à renouvellement. Elle comprend :
> a) Un audit initial, qui permet de vérifier que les actions de développement des compétences répondent aux exigences requises. En cas de résultats satisfaisants, la certification est délivrée sans limitation de durée ;
> b) Un audit de surveillance, qui permet de s'assurer de la bonne application du référentiel ;
> c) Abrogé.
> La durée de chacun des audits varie en fonction du chiffre d'affaires relatif à l'activité de prestataire d'action concourant au développement des compétences de l'organisme et du nombre de catégories d'actions de développement des compétences pour lesquelles l'organisme demande à être certifié, selon des modalités précisées par arrêté du ministre chargé de la formation professionnelle.

Ajouter en fin d'annexe la transition déjà rédigée par le projet (« La suppression du renouvellement périodique s'applique à compter de l'entrée en vigueur du présent décret… »).
Dépendances : R6316-2 proposé ; article 2 du décret 2026-728 (transition, non lu) ; arrêté du 6 juin 2019.

### C-06 : méthode de rebasage (RT-INV-05)

1. Inventaire : ajouter un champ `future_versions` (identifiant, date, acte, texte) pour chaque entrée dont la borne est finie, à partir des VIGUEUR_DIFF de même numéro, avec contrôle de la section pour les numéros recyclés.
2. Rédaction : fournir au rédacteur le successeur comme source principale lorsque sa date est antérieure à la date d'entrée en vigueur présumée du projet. Interdire dans les corps toute phrase sur une « date d'abrogation » lorsque LEGI prévoit un remplacement.
3. Lecteur : afficher pour chaque maintien la version future et sa date (par exemple L434-2 au 1er novembre 2026).
4. Priorités : le bloc AT-MP (42 entrées, échéance le 1er novembre 2026), puis la TVA et le CIBS, la loi 2026-403 (ESUS), le décret 2026-84 (APL) et le décret 2025-1100.

### C-07 : TVA et CIBS (RT-INV-06)

1. Ajouter « Code des impositions sur les biens et services, livre II (TVA) » à `outside_corpus_coordination_pending`, ou mieux au corpus, avec la table de concordance de l'ordonnance 2025-1247.
2. Pour chacune des 70 réécritures TVA, produire le texte cible dans l'article CIBS de reprise. Exemple : la mesure de 293 D III, suppression du prorata des plafonds nationaux pour l'assujetti qui débute son activité, est à porter sur l'article CIBS qui reprend 293 D. Ce numéro n'a pas été identifié et ne doit pas être inventé.
3. CGI 200 (successeur 053154489) : au 1 ter et dans la définition des soins de la proposition, remplacer le renvoi « au 1° du 4 de l'article 261 » par un renvoi à la définition autonome donnée par la proposition elle-même, ou par « au 3° de l'article L. 213-96, à l'article L. 213-98 ou à l'article L. 213-100 du code des impositions sur les biens et services ». Conserver le taux de 75 % et le champ des soins arrêtés par la proposition.

### C-08 : versions concurrentes et rédaction de R5221-22 (RT-INV-07, RT-INV-08)

- Retirer de l'inventaire courant 043320687, 036704272 et 034729420, et rattacher la proposition unique au seul identifiant en vigueur.
- R5221-22, second alinéa proposé :

> La condition prévue au 1° de l'article R. 5221-20 ne peut être opposée lorsque l'autorisation de travail est demandée par un étranger confié à l'aide sociale à l'enfance entre l'âge de seize ans et l'âge de dix-huit ans, dès lors qu'il satisfait les conditions fixées à l'article L. 435-3 du code de l'entrée et du séjour des étrangers et du droit d'asile pour obtenir une carte de séjour temporaire portant la mention “salarié” ou “travailleur temporaire”.

  Cette rédaction est à confirmer au JORF. Elle est en tout état de cause au moins aussi favorable que le texte actuel.

### C-09 à C-14 : corrections documentaires

- **Annexes** : les identifier par libellé ou section (RT-INV-09).
- **302 J** : le classer comme abrogé (RT-INV-10).
- **R4451-39** : donner une décision sur le successeur 047715485 (RT-INV-11).
- **Neuf articles CSS** : normaliser leur état en « VIGUEUR (état LEGI vide) » (RT-INV-12).
- **D304-1, D319-6, D319-7** : les rattacher au lot `automatic-construction-habitation/00115` (propriétaire de D319-5 et D319-8) et leur faire passer la seconde passe, ou les requalifier en maintien (RT-INV-13).
- **Exclusions** : publier la règle de sélection et la liste des 44 exclusions, et vérifier R4623-29, CGI 302 B, 1695 ter, 1695 quater et R4214-28 (RT-INV-14).

## 6. Orientations préservées

Aucune correction ne retire une faveur. Les corrections C-02 à C-05 ajoutent au contraire au texte du projet les faveurs nouvelles du droit positif :

- part fonctionnelle de l'indemnité en capital ;
- reconnaissance sur avis de deux médecins-conseils ;
- indicateurs de protection des apprenants.

Elles conservent aussi les allègements propres au projet : paiement à la notification, accès au rapport médical sans délai, révision à la demande de la victime, fin du renouvellement de la certification qualité.

La correction C-01 ne touche pas la suppression de la CSA décidée à L6242-1. Elle supprime seulement un doublon qui la contredit. Le contrat unique (préavis de 15 jours, indemnité de 0,20 mois par an plafonnée à 6 mois) n'est pas concerné par ce dossier. Les coordinations contrat unique présentes dans les propositions examinées sont conservées.

## 7. Incertitudes et éléments non examinés

**Sources inaccessibles.**

- Légifrance a répondu 403. Aucun texte JORF n'a été relu : les qualifications reposent sur les métadonnées LEGI (états, liens, NOTA) de l'instantané et, pour la date de la recodification TVA, sur le BOFiP du 7 octobre 2026.
- Ne sont pas dans le corpus : le CIBS, L434-1 A, l'article 2 du décret 2026-728, l'article 79 de la LFSS 2026 et les arrêtés d'application.

**Chiffres approximatifs.** Les 60 notes qui nient un successeur et les 26 corps qui insèrent une clause d'abrogation sont des minima obtenus par expression régulière. La correspondance successeur-source par numéro peut se tromper sur des numéros recyclés : elle se trompe sur les annexes du code du travail, ce qui a été vérifié.

**Non examiné.**

- 320 des 337 entrées de janvier 2027.
- Les ABROGE_DIFF de février 2027 à 2031.
- Les 106 entrées à borne 2222-02-22, hors constat global.
- Les 519 successeurs en eux-mêmes.
- Les annexes I et II (rayonnements optiques) sur le fond.
- Les maintiens AT-MP en dehors des différences mot à mot.

**Propositions en mouvement.** Plusieurs propositions examinées sont `pending` et peuvent changer. Pour L434-1 et L461-1, les empreintes de l'inventaire diffèrent déjà de l'instantané.

**Hypothèse de calendrier.** La date d'entrée en vigueur du projet n'est pas fixée. Si la loi du projet entrait en vigueur avant le 1er novembre 2026, ce qui n'est plus réaliste, RT-INV-02 à RT-INV-04 perdraient une partie de leur portée. Même dans ce cas, les remplacements déjà publiés écraseraient les réformes du projet aux dates prévues.
