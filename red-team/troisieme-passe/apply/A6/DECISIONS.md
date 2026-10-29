# Groupe A6 : décisions de la troisième passe

Instantané lu : `20261029T034912Z`, avec `tools/cite.py` (sorties dans `evidence/cited/20261029T034912Z/`). Rien n'a été écrit en production.

Contrôle : `python3 -B apply/check_changes.py A6` donne 32 changements construits, 32 validés, `problems` vide.

Diagnostics restants, tous voulus :
- changements de renvois : L315-1 → L315-2 ; ajout de L281-5, L6231-2 et L6231-3 ;
- écarts de longueur déjà présents dans les propositions dont le corps est inchangé.

Pour l'annexe qualité, la ligne est une `normative_reduction`, donc le validateur ne contrôle pas le tableau. Le compte a été vérifié à la main : 1 tableau, 52 lignes et 224 cellules dans la source de 2026 comme dans la proposition (51 et 207 pour la version sortante).

**Méthode commune aux versions de remplacement.** Les versions qui cessent le 1er novembre 2026 gardent leur proposition. Pour les articles législatifs, elles conservent un champ résiduel : les victimes consolidées avant la date d'effet (V de l'article 90 de la loi n° 2025-199). Ces propositions ne sont corrigées que là où elles étaient fausses : clauses « date d'abrogation », clause inopérante, notes qui niaient l'existence du successeur.

Chaque version de remplacement reçoit une proposition `new`. Elle reprend le texte officiel entier et n'y reporte que la réforme propre au projet, avec le même `measure_id` : la mesure n'est pas comptée deux fois.

---

## RT-INV-02 (P0) : L434-1 et L461-1, réforme AT-MP du 1er novembre 2026 — **appliquée**

- **L434-1 LEGIARTI000051288500 (new).** Le texte de la loi de 2025 est repris, avec ses deux parts : la part professionnelle, due même au retraité, et la part fonctionnelle. Le projet y ajoute le versement dès la notification pour chacune des deux parts, le recours non suspensif et le respect de l'option entre rente et capital. Une transition couvre aussi le stock ancien, sans double versement. La rédaction fusionne C-02 (dossier INV) et P-RT-FUTCSS-02.
- **L434-1 LEGIARTI000031688413 (replace).** La clause inopérante « Les champs respectifs des versions successives […] sont conservés » est retirée. La note fausse est corrigée : L434-1 A (LEGIARTI000051288442) et le successeur figurent bien au corpus.
- **L461-1 LEGIARTI000053285183 et LEGIARTI000053285169 (new).** Le seul report est la coordination « au I de l'article L. 315-2 ». Sont conservés l'incapacité permanente professionnelle, le renvoi à L434-1 A et, pour 2027, la voie des deux médecins conseils et le renvoi « huitième et avant-dernier ».
- **L461-1 LEGIARTI000053281596 (replace).** Seules les notes changent : les successeurs existent.
- **Laissé à l'auteur ou aux propriétaires :**
  - le décret qui fixe la date d'effet n'a pas été lu au JORF ;
  - les successeurs de L434-2 (LEGIARTI000051288493), L434-1 A et D434-1 n'ont pas de proposition ;
  - R142-17-2, R461-8 et D461-27 doivent être renumérotés pour 2027 (RT-FUTCSS-20, hors A6).

## RT-INV-03 (P1) : sept autres articles AT-MP — **appliquée**

Pour chaque article, une proposition `new` est rédigée sur le successeur et, le cas échéant, l'ancienne est corrigée :

- **L142-1 (051288452)** : 2°, 3° et alinéa final du projet sur le 5° de la loi. Ancienne version : notes seulement.
- **L351-3 (051288449)** : le 1° fusionne « professionnelle » (loi) et le retrait de l'occurrence erronée (projet), avec la transition. Ancienne version : notes seulement.
- **L434-16 (051288487)** : le renvoi au premier alinéa est corrigé. Sur 031688385, la phrase « date d'abrogation déjà fixée au 1er novembre 2026 » est retirée, ainsi que le membre de phrase correspondant du motif ; les notes sont corrigées.
- **L443-1 (051288476)** : la dispense d'intervalle et la transition sont reportées ; le renvoi au II de L434-2 est conservé. Ancienne version : notes seulement.
- **R351-12 (054060166 et 054425288, doublon DILA)** : le retrait de la mention préalable au compte est porté sur les deux versions, avec la transition. Le 5° « professionnelle » est conservé. L'ancienne version n'est pas modifiée.
- **R351-37 (054060160)** : circuit sans commission pluridisciplinaire, renvoi au cinquième alinéa et transition, selon la rédaction fusionnée P-RT-FUTCSS-03. L'ancienne version n'est pas modifiée.
- **R434-32 (054060111)** : accès au rapport sans délai ni formulaire et sans quinzaine. Les deux taux sont conservés et l'alinéa des barèmes annexés n'est pas rétabli. Sur 022073148, la phrase « date d'abrogation » est retirée et la réserve d'accès est réécrite sans parler d'abrogation ; le `substantive_impact` est mis à jour.
- **Laissé aux propriétaires :**
  - R443-1, dont l'intervalle annuel doit être coordonné ;
  - L351-1-4 (hors A6) ;
  - le choix, par la DILA, de la version de R351-12 qui subsistera.

## RT-INV-04 (P1) et RT-P1-TRAVAIL-B-08 (P1) : référentiel qualité (Qualiopi) et conseil de perfectionnement — **appliquées, un seul texte**

- **Annexe LEGIARTI000054612711 (new).** Le référentiel de 2026 est repris en entier : indicateurs 1 à 33, prévention des violences, du harcèlement et des discriminations, protection des mineurs, supervision renforcée. Les attributs de présentation sont retirés, toutes les cellules sont gardées. Trois mesures du projet y sont reportées :
  - le II, 2 : certification sans limitation de durée, ni expiration ni renouvellement, c) abrogé ;
  - l'indicateur 20 réécrit : appui à la mobilité sans personnel dédié ; référent handicap conservé ; pilotage et gouvernance « par tout moyen » ; conseil de perfectionnement facultatif ; la phrase de 2026 sur la supervision renforcée est conservée ;
  - trois transitions : renouvellement, mobilité, conseil. La dernière dispose que l'absence de conseil ne peut, à elle seule, fonder une non-conformité, un refus, une suspension ou un retrait de certification.
- **Annexe LEGIARTI000038591641 (replace).** Les mêmes retraits sont faits à l'indicateur 20 et dans la transition. La note qui disait le référentiel successeur absent du corpus est corrigée.
- **L6231-3, R6231-3, R6231-4, R6231-5 (replace).** Seules les notes changent : la coordination « hors lot encore nécessaire » est faite. Les corps, déjà des abrogations, sont inchangés.
- **Laissé à l'auteur :**
  - l'article 2 du décret n° 2026-728 (transition des certifications en cours) et les arrêtés d'application, qui ne sont pas au corpus ;
  - les exigences nouvelles du décret de 2026 (indicateur 33, supervision renforcée, référent pédagogique), conservées parce que le projet n'a pas décidé de les supprimer.

## RT-P1-TRAVAIL-A-01 (P1) : information trimestrielle du CSE — **appliquée**

- **R2312-21 (replace, `full_repeal`).** Abrogation transitoire alignée sur L2312-69 (rédaction du § 5.1 du dossier P1-TRAVAIL-A) : pas de rattrapage, rien n'est transféré dans la BDESE. Elle est classée `coordination_only`, avec la même mesure que L2312-69.
- **L2312-69 (replace).** Seules les notes changent.
- **Laissé au propriétaire :** le renvoi de R342-30 du CCH (ANCOLS) à R2312-21.

## RT-TR1-01 (P1) : participation de l'employeur à l'apprentissage — **appliquée (option désignée par l'objection)**

- **L6332-14 (replace).**
  - Au I 1°, les deux phrases sur la participation de niveau 6 et sur la minoration de la prise en charge par l'OPCO sont supprimées.
  - Le III devient une transition : le régime ancien (750 €, réduction de 50 %, 200 €, créances et recours) est réservé aux contrats conclus avant la loi.
  - Pour les contrats nouveaux, aucune participation ni charge équivalente n'est due.
  - Le `substantive_impact` est classé `financing_transfer`. Ce n'est pas une baisse de prélèvement comptée.
- **R6332-25, R6332-25-1, R6332-25-2 (replace).** Seules les notes changent. Leur formule « la loi supprimant la participation patronale prévue à l'article L. 6332-14 » désigne désormais cette loi, avec une entrée en vigueur commune. Aucune formalité n'est rétablie : la copie de facture, le délai de quatre mois et l'attestation préalable restent supprimés.
- **Laissé à l'auteur :** le coût du transfert vers l'OPCO, non chiffré, et sa couverture budgétaire.

## RT-INV-06 (P1) : TVA recodifiée dans le CIBS — **non appliquée (hors corpus)**

Le CIBS n'est pas au corpus. Ses articles de reprise ne peuvent pas être rédigés sans invention. Les articles CGI attribués au groupe (293 D, 256-0, 279, 1824) ne sont pas modifiés. Les renvois des successeurs (CGI 200 et 39, CSS L137-26, urbanisme L112-16) appartiennent aux groupes A1, A3, A4 et A5.

**Laissé à l'auteur :** ajouter le livre II du CIBS au corpus, ou à `outside_corpus_coordination_pending`, avec la table de concordance de l'ordonnance n° 2025-1247 ; puis porter sur les articles de reprise les mesures TVA du projet, comme la franchise sans prorata.

## RT-XCUT-01 (P1) : 408 paires de versions futures — **statut seulement, sauf le cas démontré**

**Couverture partielle.** Les groupes FUT-* traitent les paires de leurs dossiers : A1 à A3 pour FUT-FISC, A4 pour FUT-CSS, A5 pour FUT-TRAV-LOG. Ce groupe A6 couvre les 11 successeurs AT-MP et le référentiel qualité du 1er novembre 2026 (RT-INV-02 à 04).

**Reste à faire.**
- Il n'existe ni lecture ni décision pour toutes les paires.
- Les 108 nouveaux numéros futurs ne sont pas inventoriés.
- Les 16 bornes techniques 2222-02-22 ne sont pas traitées.
- Les notes qui affirment qu'un successeur « n'est pas fourni » subsistent hors périmètre (RT-FUTTL-19, RT-FUTCSS-38).

**Seul cas traité article par article : L752-1** (cas démontré, RT-UNION-05). Il est attribué à A6 et aucun groupe FUT ne le porte.
- LEGIARTI000054466934 (2028, new) : renvois limités à L281-5 et L281-6, caisse de Saint-Barthélemy visée « au quatrième alinéa », transition sur l'approbation des statuts.
- LEGIARTI000042684012 (replace) : notes seulement.

À l'auteur de dire s'il préfère retirer ce cas pour s'en tenir au statut.

---

## Résumé

- **Objections appliquées** : 6 sur 8 (RT-INV-02, RT-INV-03, RT-INV-04, RT-P1-TRAVAIL-B-08, RT-P1-TRAVAIL-A-01, RT-TR1-01).
- **Non appliquée** : RT-INV-06, hors corpus.
- **Statut seulement** : RT-XCUT-01, sauf le cas L752-1.
- **Lignes produites** : 32, dont 13 nouvelles propositions sur des versions futures et 19 remplacements. Parmi ces remplacements, 13 ne changent que les notes et le motif, ou ajoutent la phrase de troisième passe ; 6 changent le corps (L434-1, L434-16, R434-32, annexe qualité sortante, R2312-21, L6332-14).
- **Aucune** taxe créée ni formalité nouvelle ; aucune faveur retirée. Les apports favorables des lois de 2025 et 2026 sont conservés : part fonctionnelle, deux médecins conseils, indicateur 33.
- Revue IA : rien de ceci ne vaut validation par un juriste.
