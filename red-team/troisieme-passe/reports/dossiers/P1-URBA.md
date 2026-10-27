# Dossier P1-URBA — qualification des alertes « renvoi vers une abrogation proposée » (code de l'urbanisme)

Red-team juridique indépendante, troisième passe. Revue du 26 octobre 2026 sur l'instantané `20261026T230545Z` (corpus au 18 octobre 2026). **Revue IA : elle ne vaut pas validation par un juriste.** Les conclusions sont provisoires : la seconde passe continue, et beaucoup d'articles réglementaires cités ici sont encore au statut d'inventaire `pending`.

## 1. Résumé

- Paquet : 72 clusters (72 cibles abrogées), **154 alertes**, 79 articles qui y renvoient (145 de l'urbanisme, 4 de l'annexe III du CGI, 3 du CGI, 2 du CCH). Toutes les alertes sont `live`.
- Classification des 154 alertes : **131 alertes écartées**, **12 incohérences du projet**, **7 coordinations manquantes**, **2 faux positifs**, **1 risque juridique**, **1 réserve documentaire**. Aucune alerte n'est classée `non examiné` ni `couvert par dossier` (aucun dossier ouvert de l'index ne touche ces articles).
- **12 objections** : 6 P1 (5 confirmées, 1 à confirmer) et 6 P2 (5 confirmées, 1 à confirmer). Aucune P0.
- Les plus importantes :
  1. **RT-P1-URBA-01** : L510-1 abroge entièrement l'agrément Île-de-France, mais les propositions du chapitre réglementaire R*510 le maintiennent. R*510-1 le rend obligatoire, R*510-5 organise ses conventions pour l'avenir et R*510-8 subordonne les fonds publics à la décision d'agrément.
  2. **RT-P1-URBA-05** : L153-16 proposé maintient les « pouvoirs de l'autorité administrative compétente de l'Etat fondés sur la méconnaissance des objectifs de fond » de L153-26, que le projet abroge. Cela touche le caractère exécutoire des PLU tenant lieu de PLH, donc des documents d'urbanisme en vigueur.
  3. **RT-P1-URBA-03** : L102-5 est maintenu inchangé et confère toujours, « en application de l'article L. 102-2 », le pouvoir de qualification PIG que L102-2 proposé abroge et interdit.
  4. **RT-P1-URBA-07** (à confirmer) : l'abrogation de L600-1-1 s'applique « aux instances en cours ». Elle rend recevables, contre des autorisations déjà délivrées, des recours d'associations qui ne l'étaient pas. C'est une protection favorable à la construction qui disparaît, avec un effet sur les titres existants.

## 2. Méthode

1. Pour chaque cluster, lecture intégrale de la proposition d'abrogation de la cible (`tools/cite.py` par identifiant LEGIARTI, ou SQL en lecture seule) : source, NOTA, bornes, proposition, motif et notes, avec relevé des clauses de transition et de neutralisation des renvois.
2. Pour chaque article qui renvoie, lecture intégrale du texte courant (la proposition si `rewrite_draft`, la source si `retained_unchanged`). Exceptions, signalées par `read_in_full=false` :
   - CGI 38 (82 Ko) et CGI 39 duodecies : homonymie établie par le contexte « du code des assurances » ;
   - annexe CCH à R172-4 (environ 500 Ko) : renvoi de plage descriptif.
3. Vérification du code et de la version visés : homonymes, versions historiques, versions différées.
4. Qualification selon l'addendum P1. J'ai appliqué la règle suivante :
   - **alerte écartée** lorsque le renvoi figure dans un article lui-même abrogé ou coordonné, ou dans un bloc transitoire assumé, ou lorsqu'il est neutralisé ou redirigé par la clause de la cible, ou lorsqu'il s'agit d'une plage restée opérante ;
   - **coordination manquante** ou **incohérence du projet** lorsque le texte maintenu ou réécrit peut encore être lu comme appliquant la règle abrogée.
5. Une objection par effet juridique distinct, avec les articles regroupés.
6. Contrôle des orientations (`preserved_benefits_2026_10_19`, `sru_abrogation`, `autorisations_urbanisme`, `cuts_and_reliefs_2026_10_19`, `editorial_direction_2026_10_19`, `logement`).
7. Une seule consultation externe, le 2026-10-26 : Conseil constitutionnel, décision n° 2011-138 QPC.

Les pièces lues sont exportées sous `evidence/cited/20261026T230545Z/`. Le fichier `reports/p1-work/P1-URBA-classification.jsonl` donne une ligne par `finding_id`, avec en plus `target` et `referrer` pour la lisibilité.

## 3. Orientations vérifiées (pas de constat défavorable)

- **Dérogations littorales** : aucune cible du paquet n'est un article littoral protégé.
  - L121-28/29/30 et L104-2 sont `retained_unchanged`.
  - R121-7/8/36 et R151-52 sont réécrits sans abrogation.
  - Les abrogations de L111-3, L142-4, L142-5, R142-2 et R142-3 réservent expressément les possibilités de L121-28 à L121-30, pour les opérations futures comme pour les situations antérieures.
  - La pièce h de R431-16 (dérogation littorale R121-5) est conservée.
- **Franchise TASCOM** : hors code de l'urbanisme (loi 72-657, article 3). Aucune cible du paquet ne la touche. Les notes de L520-1 indiquent « Aucun effet sur la franchise TASCOM ».
- **SRU** :
  - les abrogations de L111-24 (quota de 30 ou 25 %), L153-26 (contrôle PLH), L213-2-1 (SRU21) et L115-4/L115-5 (SRU14) suivent l'orientation et préservent les permis délivrés, les contrats et les promesses antérieures ;
  - L152-6-3 conserve l'exemption défense pour les situations antérieures ;
  - seule divergence relevée : L510-1. L'orientation `sru_abrogation` prévoyait de ne retirer que le critère social SRU70. La proposition va plus loin, au titre de `editorial_direction_2026_10_19`, et le niveau réglementaire n'a pas suivi (RT-01).
- **Autorisations d'urbanisme** : la coordination L424-6 / A424-1 / R*424-8 / R*424-10 est conforme à `autorisations_urbanisme`. L'ancienne fenêtre de deux mois est conservée pour les titres antérieurs.
- **Autorisations délivrées, demandes en cours, documents en vigueur** : les clauses transitoires des cibles lues sont généralement complètes (demandes en cours sans nouveau dépôt, refus définitifs non rouverts, prescriptions non réécrites, loi répressive plus douce). Deux exceptions : RT-07 (L600-1-1, instances en cours) et RT-05 (PLU tenant lieu de PLH).

## 4. Constats (objections)

| ID | Prio | Nature | Statut | Objet |
|---|---|---|---|---|
| RT-P1-URBA-01 | P1 | incohérence du projet | confirmé | Chapitre R*510 maintenu (R*510-1, -2, -5, -8…) malgré l'abrogation intégrale de L510-1 |
| RT-P1-URBA-02 | P2 | incohérence du projet | confirmé | Clauses de réserve et pièce g maintenant l'agrément L510-1 (R*510-14, L111-12, R431-16 g, R*431-36) |
| RT-P1-URBA-03 | P1 | coordination manquante | confirmé | L102-5 maintenu, contraire à l'abrogation de L102-2 (PIG liés aux DTADD) |
| RT-P1-URBA-04 | P1 | incohérence du projet | confirmé | L102-13 1° : « Par dérogation à l'article L. 111-3 » orphelin, consultation CDPENAF en OIN incertaine ; 4° renvoi à L322-3-2 |
| RT-P1-URBA-05 | P1 | incohérence du projet | confirmé | L153-16 (et L153-44) maintiennent des pouvoirs de l'État fondés sur L153-26 abrogé |
| RT-P1-URBA-06 | P2 | incohérence du projet | confirmé | R*423-27 se fonde sur le délai de trois mois de R*423-61 abrogé |
| RT-P1-URBA-07 | P1 | risque juridique | à confirmer | Abrogation de L600-1-1 appliquée aux instances en cours |
| RT-P1-URBA-08 | P2 | coordination manquante | confirmé | Listes de pièces (R*431-4 c, R*434-2, R*431-36) non coordonnées avec la suppression du plan intérieur et de l'engagement EnR |
| RT-P1-URBA-09 | P2 | coordination manquante | confirmé | R*410-10 (certificat opérationnel) maintient les avis de R*423-52 abrogé |
| RT-P1-URBA-10 | P2 | incohérence du projet | confirmé | A520-1 maintenu (Cerfa 14600, renvoi à R520-10 à R520-13 abrogés) ; phrase de A520-2 sans borne temporelle |
| RT-P1-URBA-11 | P2 | anomalie d'inventaire | confirmé | L520-7 : version différée au 1er janvier 2027 (LEGIARTI000054567160) sans proposition |
| RT-P1-URBA-12 | P2 | réserve documentaire | à confirmer | Clause fiscale de L111-3 et successeur CIBS de CGI 257 (abrogé au 1er janvier 2027) |

Raisonnements, passages exacts, conséquences, options et réserves : voir `reports/dossiers/P1-URBA.json`. Points saillants :

- **RT-01** :
  - L510-1 proposé dispose « Aucun agrément fondé sur le présent article dans sa rédaction antérieure n'est exigé », que l'absence d'agrément ne peut empêcher « l'engagement de fonds publics, l'affectation des bâtiments », et que « Les conventions relatives à la mise en œuvre de l'agrément ne peuvent le rétablir ».
  - R*510-8 proposé dispose au contraire « Les fonds publics ne peuvent être engagés et l'affectation des bâtiments ne peut être prononcée que sur production de la décision d'agrément ».
  - R*510-5 vise les conventions « conclues ou renouvelées à compter de l'entrée en vigueur de la loi de réforme ».
  - Les décrets ont été rédigés sous l'hypothèse « le régime général est conservé » (notes de R*510-1).
- **RT-05** :
  - L153-16 dispose « Pour l'application de l'article L. 153-26 [...] Les pouvoirs de l'autorité administrative compétente de l'Etat fondés sur la méconnaissance des objectifs de fond mentionnés au même article demeurent applicables. »
  - L153-26 proposé dispose « aucune modification [...] ne peut être imposée sur le fondement du présent article ».
  - L153-25 6° est lui aussi abrogé : il ne reste aucun fondement autonome à ces « objectifs de fond ».
- **RT-07** : l'abrogation est présentée comme un allègement pour les associations, mais elle accroît le risque contentieux pesant sur les constructeurs. Appliquée aux instances en cours, elle touche les autorisations déjà délivrées. Le Conseil constitutionnel avait jugé L600-1-1 conforme (2011-138 QPC, 17 juin 2011, version antérieure à 2018 ; consulté le 2026-10-26). Supprimer cette condition relève de la politique des auteurs. La rétroactivité aux instances pendantes est le point à corriger.

## 5. Propositions de correction (présentées séparément)

Les textes ci-dessous sont des propositions de la red-team. Elles ne sont ni enregistrées ni appliquées. Elles dépendent de l'état courant des propositions, qui peut évoluer.

### RT-01 — R*510-5 (modèle pour l'abrogation du chapitre R*510)

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi abrogeant l'article L. 510-1. À compter de cette date, aucune convention ne peut être conclue, renouvelée ou exécutée pour définir les modalités locales de l'agrément supprimé, et le préfet ne peut ni suspendre ni dénoncer une convention sur ce fondement pour en tirer une obligation d'agrément. Les conventions en cours cessent de produire effet en tant qu'elles organisent la délivrance de l'agrément ou imposent des engagements exclusivement liés à celui-ci ; leurs autres stipulations, les engagements financiers valablement conclus et les droits des tiers demeurent régis par leurs propres termes. Les décisions prises avant cette date et les recours qui s'y rapportent restent régis par les dispositions antérieures, sous réserve des effets de l'abrogation de l'article L. 510-1.

- Même schéma pour R*510-1, -2, -4, -6, -7, -9, -10, -11 et -15.
- Pour R*510-8 : retirer le deuxième alinéa et la dérogation au g de R431-16.
- Justification : la loi proposée supprime la base légale (L510-1 IV) et interdit expressément ces effets.
- Dépendances : RT-02, R520-14 (remboursements adossés à la durée des anciens agréments).
- Autre option, à trancher par les auteurs : revenir au seul retrait du critère social (orientation `sru_abrogation`).

### RT-02 — Clauses de réserve

- R*510-14, dernier alinéa :
  > Les règles de planification, les autorisations d'urbanisme et les protections relatives à la sécurité, aux risques et à la pollution des sols qui reposent sur des fondements autonomes demeurent applicables. Cette réserve ne maintient ni ne rétablit l'agrément supprimé par l'abrogation de l'article L. 510-1.
- L111-12, dernière phrase :
  > Les obligations et sanctions fondées sur les articles L. 421-1 à L. 421-4 demeurent applicables dans leur champ propre. Les faits antérieurs à l'abrogation de l'article L. 510-1 restent soumis aux règles qui leur étaient applicables, sous réserve de l'application de la loi répressive plus douce.
- R431-16 : « g) Abrogé ; », avec une transition :
  > La suppression de la pièce prévue au g s'applique aux demandes nouvelles et en cours à compter de l'entrée en vigueur de l'abrogation de l'article L. 510-1, sans nouveau dépôt ni reprise des délais.
- R*431-36 : retirer « g ».

### RT-03 — L102-5

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi abrogeant l'article L. 102-2. À compter de cette date, aucun projet ni aucune mesure ne peut être qualifié de projet d'intérêt général sur le fondement du présent article ou de la seule nécessité de mettre en œuvre une directive territoriale d'aménagement et de développement durables, y compris pendant la fraction non écoulée du délai de douze ans qu'il prévoyait et pour les procédures de qualification en cours. Les qualifications régulièrement prononcées avant cette date conservent leurs effets pour la durée restant à courir, sans renouvellement sur ce fondement, dans les conditions de l'article L. 102-2. Les avis déjà recueillis des collectivités territoriales, de leurs groupements et des comités de massif demeurent au dossier. La qualification de projets d'intérêt général sur le fondement de l'article L. 102-1 n'est pas affectée.

Justification : aligner L102-5 sur L102-2, R102-1, L102-4 et L172-7, déjà coordonnés. Les qualifications anciennes sont préservées.

### RT-04 — L102-13, 1° et 4° (passages complets)

> 1° Les constructions et installations nécessaires à la réalisation de l'opération peuvent être autorisées en dehors des parties urbanisées de la commune, dans les conditions des règles applicables sur un fondement distinct ; aucune consultation n'est exigée au seul titre de cette localisation ;

> 4° Les associations foncières urbaines sont créées dans les conditions prévues au chapitre II du titre II du livre III, sans l'accord ou l'avis supprimé par l'abrogation de l'article L. 322-3-2.

Ajouter à l'alinéa transitoire final :

> La présente rédaction des 1° et 4° s'applique aux décisions prises à compter de l'entrée en vigueur de la loi abrogeant les articles L. 111-3, L. 111-5 et L. 322-3-2, y compris sur les demandes en cours, sans nouveau dépôt ni reprise des délais ; les consultations déjà accomplies restent au dossier et les autorisations antérieures conservent leur régime.

- Justification : la consultation CDPENAF de droit commun est supprimée par L111-5. La conserver en OIN rendrait ce régime de faveur plus contraignant que le droit commun.
- Option inverse, conforme à la note de L111-3 (« son avis autonome ») : rédiger le 1° comme une consultation autonome expresse, limitée aux communes sans document d'urbanisme. Ce choix revient aux auteurs.

### RT-05 — L153-16 et L153-44

- L153-16, remplacer l'alinéa « Pour l'application de l'article L. 153-26 […] demeurent applicables. » par :
  > L'absence d'avis du comité mentionné au 3°, son avis défavorable ou ses réserves ne peuvent justifier une demande de modification du plan ni faire obstacle à son caractère exécutoire. Aucun pouvoir de l'autorité administrative compétente de l'État fondé sur l'article L. 153-26 dans sa rédaction antérieure à son abrogation ne peut être exercé à l'égard des plans transmis à compter de cette abrogation ; les pouvoirs prévus à l'article L. 153-25, le contrôle de légalité et les recours demeurent applicables dans leur champ propre.
- L153-44, deuxième phrase du deuxième alinéa :
  > Les pouvoirs de notification prévus à l'article L. 153-25, leurs conditions et délais d'exercice ainsi que l'obligation d'apporter les modifications légalement demandées sur ce fondement demeurent applicables ; aucune notification ne peut être fondée sur l'article L. 153-26 abrogé.
- Coupe facultative, non revendiquée : supprimer, dans L153-23 II 2°, l'attente d'un mois propre aux PLU tenant lieu de PLH couverts par un SCoT. Elle n'avait d'autre fonction que le contrôle de L153-26.

### RT-06 — R*423-27, avant-dernier alinéa

> La réduction prévue au a ne modifie ni l'obligation de consulter la commission nationale, ni le délai au terme duquel son avis est réputé émis en application de l'article R*423-59, ni les autres accords, évaluations et participations du public légalement requis. Les délais plus longs résultant d'un autre cas légalement applicable au projet demeurent applicables.

Corriger aussi les notes de R*423-59, qui décrivent R*423-27 a comme maintenant cinq mois.

### RT-07 — L600-1-1, deuxième alinéa de la proposition

> La condition d'une ancienneté minimale d'un an du dépôt des statuts d'une association cesse de s'appliquer aux recours dirigés contre les décisions relatives à des demandes dont l'affichage ou la publication prévus à l'article R. 423-6 interviennent à compter de cette entrée en vigueur. Les recours dirigés contre les décisions relatives à des demandes affichées ou publiées avant cette date, y compris les instances en cours, restent soumis à cette condition. Aucun justificatif de cette ancienneté ne peut être exigé sur ce seul fondement pour les recours relevant de la présente rédaction.

Autre option : maintenir L600-1-1, garantie favorable aux constructeurs.

### RT-08 — Listes réglementaires de pièces

- R*431-4 :
  - supprimer le c ;
  - au dernier alinéa, remplacer la phrase « Elle ne retire pas le plan intérieur légalement demandé… » par : « Le plan intérieur supprimé avec l'article R. 431-34-1 ne fait plus partie de la demande, y compris pour les demandes en cours. »
- R*434-2 :
  > Les arrêtés prévus à l'article R. 434-1 ne peuvent imposer ni le plan intérieur supprimé avec l'article R. 431-34-1, ni les informations statistiques complémentaires supprimées avec l'article R. 431-34, ni un état, une attestation ou une déclaration de remplacement sur ces fondements. Les obligations statistiques pourvues d'un fondement légal autonome et les règles relatives aux secrets protégés et aux données personnelles restent applicables dans leur champ.
- R*431-36, deuxième alinéa :
  > Il est complété, s'il y a lieu, par les documents mentionnés aux a et b de l'article R. 431-10, à l'article R. 431-14, aux a, b, c, h, q, r et t de l'article R. 431-16 et aux articles R. 431-18, R. 431-21, R. 431-23-2 et R. 431-31 à R. 431-33.

### RT-09 — R*410-10, deuxième alinéa

> L'autorité compétente recueille l'avis des collectivités, établissements publics et services gestionnaires des réseaux mentionnés à l'article L. 111-11 ainsi que l'avis prévu par l'article R. 423-53.

Ajouter :

> La suppression de la consultation prévue par l'ancien article R. 423-52 s'applique aux demandes de certificat en cours, sans reprise du délai d'instruction ; les avis déjà émis restent au dossier.

### RT-10 — A520-1 (et A520-2)

> Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant la taxe sur la création de locaux à usage de bureaux, de locaux commerciaux et de locaux de stockage en Île-de-France. Aucune déclaration établie conformément au formulaire Cerfa 14600, ni aucune autre déclaration exclusivement destinée à l'ancienne redevance ou à cette taxe, ne peut être exigée sur son fondement dans le dossier d'une demande de permis de construire ou d'une déclaration préalable lorsque le fait générateur n'est pas antérieur à cette date ; son absence ne rend pas la demande incomplète. Pour les opérations dont le fait générateur est antérieur à cette date, les déclarations déjà déposées conservent leurs effets et les articles R. 520-10 à R. 520-13, dans leur rédaction applicable à ces faits, régissent les déclarations encore dues, en un seul exemplaire. Les exonérations, décharges, réductions, restitutions, prescriptions et voies de recours applicables à ces opérations demeurent préservées.

A520-2 : ajouter, après « demeurent applicables », les mots « pour les seuls faits générateurs antérieurs à la suppression de cette taxe, dans les conditions de l'article L. 520-1 ».

### RT-11 — L520-7

Rattacher la proposition d'abrogation à la version LEGIARTI000054567160 (en vigueur différée au 1er janvier 2027) et l'inscrire à l'inventaire. Le texte reste identique, avec la référence CIBS L. 231-12 pour les seuls faits anciens.

### RT-12 — L111-3, clause fiscale

Après identification du texte CIBS qui succède à CGI 257 I 2 1°, compléter si nécessaire : « Pour les seuls renvois fiscaux au présent article, y compris ceux des dispositions qui leur succèdent dans le code des impositions sur les biens et services, […] ».

## 6. Alertes écartées : regroupements

- **Taxe sur les bureaux en Île-de-France** (L520-1 à L520-23, R520-8 à R520-13) : 42 alertes A520-2 et A520-6, et 17 alertes R520-x.
  - A520-2 et A520-6 sont eux-mêmes abrogés ; la plage « L. 520-1 à L. 520-23 » n'y figure que dans des clauses de non-modification ou de réserve.
  - Tous les R520-x référents sont abrogés ; leurs renvois figurent dans le bloc « Pour les seuls faits générateurs intervenus avant cette date ».
  - Le portefeuille ancien est cohérent : exonérations, plafond de 30 %, imputations, remboursements, prescriptions et loi plus douce.
- **Renvois de plage restés opérants** : L153-36/37 à L153-44 (L123-24-2, L121-22-3, L131-7, L131-8, L153-36), L153-11 à L153-26 (L154-3), R431-13 à R431-33 (R*431-4, R*441-6), R152-4 à R152-9 (R*431-31-2), R421-26 à R421-28 (A451-1), R322-7 à R322-22 (R*322-24), R112-4 à R112-17 (annexe CCH à R172-4).
- **Mécanismes coordonnés** : L111-6 à L111-10, L424-6 / A424-1 / R*424-8 / R*424-10, L102-4 / L102-7 / L172-6 / L172-7 / R102-1, L142-4 / L142-5 / L143-7, R423-75 / R423-78 / R423-79, R*423-29 / R*423-43, L113-12 / L113-14 / L113-25, L213-2-1 / L213-4, L115-4 / L115-5, R111-17 / R152-4, L111-24 / L152-6-3, bordereaux (A431-2/5, A441-2/5, A451-2 ; A434-1, A444-1, A453-4), A213-1 / A142-1, R*442-7 / R*442-8, L111-5 / L122-7, annexe III 331 K ter (abrogé pour les cessions nouvelles).
- **Renvois inertes dans des textes maintenus** (neutralisés par la clause de la cible ; toilettage facultatif) : L111-1 (vers L111-3 à L111-5), R111-20 (vers L111-5), L102-10 et R102-2 (vers L102-7), L153-59 et L153-23 II 2° (vers L153-26), L113-25 1° (vers L113-14), L102-13 4° (vers L322-3-2, correction intégrée à RT-04), L122-20 et L122-21 (dérogation expirée en 2019), CCH R318-11 (vers L113-10).
  - Les motifs de maintien de R111-20 et R431-16 g supposent encore la survie des articles abrogés. C'est sans effet normatif, mais à corriger pour la traçabilité.
- **Faux positifs** : CGI 38 et 39 duodecies visent L. 142-5 du code des assurances.

## 7. Incertitudes et éléments non examinés

- La seconde passe est en cours : la plupart des articles réglementaires cités (chapitre R*510, R*423-27, R*423-59, R*423-61, R*431-4, R*431-36, R*434-2, R*410-10, A520-1) sont au statut d'inventaire `pending` et peuvent encore changer.
- Lus seulement en partie ou par leur statut : R*510-4, -6, -7, -9, -10, -11, -15 ; A520-3, A520-4, A520-5 ; R153-7 (signalé par les notes de L153-18 et L153-39 comme à coordonner, hors paquet) ; R112-14 et L112-16 (réserve relative à R112-11, hors paquet).
- CGI 38 et 39 duodecies, ainsi que l'annexe CCH à R172-4, n'ont pas été lus en entier (`read_in_full=false`).
- Textes hors corpus non consultés : CIBS (successeur de CGI 257), ordonnance 2025-1247, directive 2006/112/CE, code rural L112-1-1, code du commerce et code du cinéma, CGCT, loi 2000-1208. Ce sont des réserves documentaires.
- Le paquet ne couvre que les renvois que l'audit a détectés par une formule d'abrogation explicite. Des renvois non textuels ou extérieurs aux cinq codes ont pu lui échapper.
- Aucune vérification juridictionnelle ni avis de juriste. Les priorités sont des appréciations de la red-team.

## 8. Périmètre réellement lu (code, numéro, identifiant de version, état, bornes, statut de la proposition, statut de seconde passe)

### Cibles abrogées (72)
- urba A213-1 (LEGIARTI000006813832, VIGUEUR, 1987-06-02→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A431-2 (LEGIARTI000006814119, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A431-5 (LEGIARTI000006814122, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A441-2 (LEGIARTI000006814057, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A441-5 (LEGIARTI000006814139, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A451-2 (LEGIARTI000006814150, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba L102-2 (LEGIARTI000031210080, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L102-7 (LEGIARTI000031210098, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-10 (LEGIARTI000031210195, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-24 (LEGIARTI000045211103, VIGUEUR, 2022-02-23→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-3 (LEGIARTI000031210179, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-5 (LEGIARTI000047303696, VIGUEUR, 2023-03-12→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-6 (LEGIARTI000047300284, VIGUEUR, 2023-03-12→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-8 (LEGIARTI000031210191, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-9 (LEGIARTI000031210193, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L113-10 (LEGIARTI000031210329, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L113-14 (LEGIARTI000031210337, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L115-4 (LEGIARTI000031210397, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L142-4 (LEGIARTI000042013180, VIGUEUR, 2021-04-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L142-5 (LEGIARTI000031210995, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-18 (LEGIARTI000031211360, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-26 (LEGIARTI000044190571, VIGUEUR, 2023-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-39 (LEGIARTI000031211414, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L172-6 (LEGIARTI000031211546, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L213-2-1 (LEGIARTI000006814978, VIGUEUR, 2000-12-14→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L322-3-2 (LEGIARTI000037667133, VIGUEUR, 2018-11-25→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L424-6 (LEGIARTI000006815954, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L510-1 (LEGIARTI000053544648, VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L510-4 (LEGIARTI000031217078, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-1 (LEGIARTI000031816543, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-10 (LEGIARTI000031816455, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-11 (LEGIARTI000031816449, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-12 (LEGIARTI000031816444, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-13 (LEGIARTI000031816441, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-13-1 (LEGIARTI000045917226, VIGUEUR, 2022-09-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-14 (LEGIARTI000031764338, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-15 (LEGIARTI000031764340, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-16 (LEGIARTI000031764342, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-17 (LEGIARTI000031764346, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-18 (LEGIARTI000042914585, VIGUEUR, 2022-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-19 (LEGIARTI000031764350, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-2 (LEGIARTI000031816534, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-21 (LEGIARTI000031764356, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-22 (LEGIARTI000031764358, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-23 (LEGIARTI000031764362, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-3 (LEGIARTI000031816522, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-5 (LEGIARTI000031816504, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-6 (LEGIARTI000053544635, VIGUEUR, 2026-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-7 (LEGIARTI000045917236, ABROGE_DIFF, 2022-09-01→2027-01-01, rewrite_draft, 2e passe : completed)
- urba L520-8 (LEGIARTI000031816477, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-9 (LEGIARTI000045917231, VIGUEUR, 2022-09-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L600-1-1 (LEGIARTI000037668002, VIGUEUR, 2019-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R*322-13 (LEGIARTI000006818114, VIGUEUR, 1986-04-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R*421-27 (LEGIARTI000006819100, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*423-29 (LEGIARTI000030864501, VIGUEUR, 2015-07-11→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*423-52 (LEGIARTI000028678360, VIGUEUR, 2014-04-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*423-61 (LEGIARTI000006819971, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-13 (LEGIARTI000006820090, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-18-1 (LEGIARTI000033498226, VIGUEUR, 2016-11-28→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-34 (LEGIARTI000038494420, VIGUEUR, 2019-05-22→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-34-1 (LEGIARTI000030536171, VIGUEUR, 2015-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*442-7 (LEGIARTI000006819522, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R111-17 (LEGIARTI000031721286, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R112-11 (LEGIARTI000031721145, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R152-4 (LEGIARTI000031720499, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R152-9 (LEGIARTI000032722284, VIGUEUR, 2016-06-18→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R423-78 (LEGIARTI000038493286, VIGUEUR, 2019-05-22→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-10 (LEGIARTI000035710588, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-11 (LEGIARTI000035710579, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-12 (LEGIARTI000035710563, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-13 (LEGIARTI000035709105, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-8 (LEGIARTI000035710606, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)

### Articles qui y renvoient (79)
- a3 331 K ter (LEGIARTI000033498355, VIGUEUR, 2016-11-28→2999-01-01, rewrite_draft, 2e passe : completed)
- cch Annexe à l'article R172-4 (LEGIARTI000054024988, VIGUEUR, 2026-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- cch R318-11 (LEGIARTI000033498420, VIGUEUR, 2016-11-28→2999-01-01, rewrite_draft, 2e passe : pending)
- cgi 257 (LEGIARTI000046196126, ABROGE_DIFF, 2022-08-18→2222-02-22, retained_unchanged, 2e passe : completed)
- cgi 38 (LEGIARTI000051203585, VIGUEUR, 2025-02-16→2999-01-01, rewrite_draft, 2e passe : completed)
- cgi 39 duodecies (LEGIARTI000051203546, VIGUEUR, 2025-02-16→2999-01-01, rewrite_draft, 2e passe : completed)
- urba A142-1 (LEGIARTI000006813818, VIGUEUR, 1987-06-02→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A424-1 (LEGIARTI000006814020, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A434-1 (LEGIARTI000047518319, VIGUEUR, 2023-05-04→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A444-1 (LEGIARTI000047518298, VIGUEUR, 2023-05-04→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A451-1 (LEGIARTI000031200655, VIGUEUR, 2015-09-23→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A453-4 (LEGIARTI000025378981, VIGUEUR, 2012-02-19→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A520-1 (LEGIARTI000031650475, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A520-2 (LEGIARTI000031650470, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba A520-6 (LEGIARTI000006814209, VIGUEUR, 1977-01-18→2999-01-01, rewrite_draft, 2e passe : pending)
- urba L102-10 (LEGIARTI000031210104, VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, 2e passe : completed)
- urba L102-13 (LEGIARTI000049399405, VIGUEUR, 2024-04-11→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L102-4 (LEGIARTI000031210088, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L102-5 (LEGIARTI000033745638, VIGUEUR, 2016-12-30→2999-01-01, retained_unchanged, 2e passe : completed)
- urba L111-1 (LEGIARTI000031210169, VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, 2e passe : completed)
- urba L111-10 (LEGIARTI000031210195, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-12 (LEGIARTI000031210201, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-6 (LEGIARTI000047300284, VIGUEUR, 2023-03-12→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-7 (LEGIARTI000047300277, VIGUEUR, 2023-03-12→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-8 (LEGIARTI000031210191, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L111-9 (LEGIARTI000031210193, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L113-12 (LEGIARTI000031210333, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L113-25 (LEGIARTI000031210369, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L115-5 (LEGIARTI000031210399, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L121-22-3 (LEGIARTI000052866143, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L122-20 (LEGIARTI000042013170, VIGUEUR, 2021-04-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L122-21 (LEGIARTI000033746300, VIGUEUR, 2017-08-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L122-7 (LEGIARTI000047300186, VIGUEUR, 2023-03-12→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L123-24-2 (LEGIARTI000052865175, VIGUEUR, 2025-11-28→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L131-7 (LEGIARTI000052866170, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L131-8 (LEGIARTI000052866162, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L142-4 (LEGIARTI000042013180, VIGUEUR, 2021-04-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L142-5 (LEGIARTI000031210995, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L143-7 (LEGIARTI000031211015, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L152-6-3 (LEGIARTI000045201309, VIGUEUR, 2022-02-23→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-16 (LEGIARTI000033746220, VIGUEUR, 2017-08-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-23 (LEGIARTI000044190577, VIGUEUR, 2023-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-36 (LEGIARTI000052866306, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-44 (LEGIARTI000052866363, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L153-59 (LEGIARTI000031211464, VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, 2e passe : completed)
- urba L154-3 (LEGIARTI000052866371, VIGUEUR, 2026-05-26→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L172-7 (LEGIARTI000031211548, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L213-4 (LEGIARTI000029738526, VIGUEUR, 2015-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R*322-24 (LEGIARTI000006818126, VIGUEUR, 1986-04-01→2999-01-01, retained_unchanged, 2e passe : completed)
- urba R*410-10 (LEGIARTI000031764615, VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, 2e passe : pending)
- urba R*423-27 (LEGIARTI000030864525, VIGUEUR, 2015-07-11→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*423-43 (LEGIARTI000006819948, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*423-6 (LEGIARTI000054550543, VIGUEUR, 2026-07-29→2999-01-01, retained_unchanged, 2e passe : pending)
- urba R*424-10 (LEGIARTI000043857111, VIGUEUR, 2021-07-26→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*424-8 (LEGIARTI000006819993, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-31-2 (LEGIARTI000046817190, VIGUEUR, 2022-12-28→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-36 (LEGIARTI000054481641, VIGUEUR, 2026-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*431-4 (LEGIARTI000030539010, VIGUEUR, 2015-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*434-2 (LEGIARTI000030538987, VIGUEUR, 2015-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*441-6 (LEGIARTI000028678508, VIGUEUR, 2014-04-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*442-8 (LEGIARTI000006819512, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*510-14 (LEGIARTI000026736154, VIGUEUR, 2013-01-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*510-5 (LEGIARTI000006820274, VIGUEUR, 2001-03-28→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R102-1 (LEGIARTI000031721460, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R102-2 (LEGIARTI000031721455, VIGUEUR, 2016-01-01→2999-01-01, retained_unchanged, 2e passe : completed)
- urba R111-20 (LEGIARTI000038495943, VIGUEUR, 2019-05-23→2999-01-01, retained_unchanged, 2e passe : completed)
- urba R152-4 (LEGIARTI000031720499, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R423-75 (LEGIARTI000038493280, VIGUEUR, 2019-05-22→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R423-79 (LEGIARTI000038493288, VIGUEUR, 2019-05-22→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R431-16 (LEGIARTI000053903389, VIGUEUR, 2026-04-17→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-10 (LEGIARTI000035710588, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-11 (LEGIARTI000035710579, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-12 (LEGIARTI000035710563, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-13 (LEGIARTI000035709105, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-15 (LEGIARTI000035709153, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-15-1 (LEGIARTI000047280427, VIGUEUR, 2023-03-10→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-16 (LEGIARTI000035709238, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-18 (LEGIARTI000035709298, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R520-9 (LEGIARTI000035710598, VIGUEUR, 2017-10-05→2999-01-01, rewrite_draft, 2e passe : pending)

### Pièces complémentaires lues pour qualifier
- urba L153-25 (LEGIARTI000044190574, VIGUEUR, 2023-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L421-3 (LEGIARTI000006815694, VIGUEUR, 2007-10-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L423-1 (LEGIARTI000039784126, VIGUEUR, 2019-12-27→2999-01-01, rewrite_draft, 2e passe : completed)
- urba L520-7 (LEGIARTI000054567160, VIGUEUR_DIFF, 2027-01-01→2999-01-01, None, 2e passe : not_in_inventory)
- urba R*423-59 (LEGIARTI000033052369, VIGUEUR, 2016-08-15→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*510-1 (LEGIARTI000006820261, VIGUEUR, 2007-11-14→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*510-2 (LEGIARTI000022406053, VIGUEUR, 2010-07-01→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R*510-8 (LEGIARTI000006820330, VIGUEUR, 1973-11-13→2999-01-01, rewrite_draft, 2e passe : pending)
- urba R142-2 (LEGIARTI000031720717, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)
- urba R142-3 (LEGIARTI000031720715, VIGUEUR, 2016-01-01→2999-01-01, rewrite_draft, 2e passe : completed)