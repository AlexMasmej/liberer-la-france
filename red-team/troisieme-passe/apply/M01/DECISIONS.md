# M01 : cinquième balayage (CSS, pistes S16 et S17), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-M01.json`, soit 71 articles et 120 pistes. Qualification détaillée de chaque piste : `audit/sweeps/M01.json`.

Contrôle : `python3 -B apply/check_changes.py` donne `problems` vide pour M01 (5 lignes), W01ma (6), W02ma (9) et W04ma (1). Tous les diagnostics sont voulus : réductions et abrogations déclarées, renvois changés (L162-12-6 remplacé par L162-12-3 ; L200-2 et L222-2-1 ajoutés).

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 55 : 51 corrigées, 4 non corrigées (pièce manquante) |
| m | 52 |
| déjà réglé | 8 |
| faux positif | 5 |

Il y a 21 lignes de correction au total :
- M01 : 5 lignes ;
- W01ma : 6 ;
- W02ma : 9 ;
- W04ma : 1.

Aucune ligne n'est en mode `new`. Le groupe n'adresse aucune demande (`requests`) à un autre groupe.

Les dossiers de variante sont ceux des articles qui ont un `previous_owner` et que j'ai corrigés :
- `apply/W01ma/` ;
- `apply/W02ma/` ;
- `apply/W04ma/`.

Les articles des autres propriétaires (W03, W05, W06, W07, Y01 à Y04, J03) n'appellent aucune correction. Aucun dossier n'a donc été créé pour eux.

## Corrections (G)

### Articles du groupe M01

- **R481-7** (LEGIARTI000006750586), S16, F2 et F3 (`replace`).
  - Défaut : la proposition renvoie aux « pénalités prévues à l'article L. 471-3 ». Cet article a été abrogé le 20 décembre 2005.
  - Correction : le renvoi mort est retiré. La phrase devient « Sans préjudice des peines résultant d'autres lois s'il y échet ». Le remboursement des indus est conservé. Aucune sanction de remplacement n'est créée.
  - Les notes, qui disaient L471-3 absent du corpus, sont corrigées.
- **R315-1** (LEGIARTI000022073076), S16, F3 (`replace`, bilan d'impact mis à jour).
  - Défaut : la proposition renvoie à L. 162-12-6. Cet article a été transféré le 30 décembre 1999 (loi n° 99-1140, article 24). LEGI le met en concordance avec L. 162-12-3, qui prévoit la même mise à la charge des infirmiers.
  - Correction : le renvoi est redirigé vers L. 162-12-3. La procédure visée reste la même, sans extension.
- **R162-1-8** (LEGIARTI000038790484), S16, F3 (`replace`, `normative_reduction`).
  - Défaut : un alinéa impose une cosignature de la MSA « lorsqu'il est fait application de l'article L. 162-7 ». Cet article a été abrogé le 25 avril 1996, si bien que la condition ne peut plus se réaliser.
  - Correction : l'alinéa est retiré. Le retrait est ajouté à `removed_provisions`, et le bilan d'impact ainsi que les notes sont corrigés.
- **R731-3-1** (LEGIARTI000006752488) et **R731-3** (LEGIARTI000006753005), S16, F3 (`replace`).
  - Défaut : le projet réforme l'octroi de l'autorisation prévue par L. 731-1 et ses « demandes en cours ». Or L. 731-1 a été abrogé le 10 août 1994 (loi n° 94-678, article 16).
  - Correction : un alinéa final interdit toute autorisation ou approbation initiale nouvelle et limite l'article, le cas échéant, aux institutions autorisées avant 1994.
  - Ce qui est conservé : les allègements du projet (seuil d'affiliés, approbation des modifications) restent acquis à ces institutions. Aucune formalité de remplacement n'est créée. Les renvois de R731-4, R731-5, R731-31 et R731-32 restent valides.

### Variante W01ma (articles du groupe W01)

Six annexes orphelines sont abrogées en `full_repeal` (`coordination_only`) :
- l'annexe à A931-11-16 ;
- l'annexe (1) à A931-11-17 ;
- l'annexe à A931-10-14 ;
- l'annexe (1) à A931-11-11 ;
- l'annexe 2 à A931-11-20 ;
- l'annexe à A931-11-19.

Ces annexes couvrent 17 pistes S17, que je requalifie de m en G. Les articles qu'elles complètent ont été abrogés au 1er janvier 2016 par l'arrêté du 30 décembre 2015, article 1er (LIEN ABROGE LEGIARTI000031791801). Le projet réduisait encore ces états ou les déclarait « nécessaires ». Aucun article en vigueur ne renvoie à ces annexes. Les documents des exercices antérieurs sont conservés, et aucune formalité de remplacement n'est créée.

### Variante W02ma (articles du groupe W02)

- **Sept annexes orphelines** sont abrogées sur le même motif, ce qui couvre 25 pistes :
  - l'annexe II à A931-11-9 ;
  - l'annexe (3) à A931-11-11 ;
  - l'annexe à A931-11-15 ;
  - les annexes (2) et (3) à A931-11-17 ;
  - l'annexe à A931-11-21 ;
  - l'annexe à A941-1-1.
- **R135-2** (LEGIARTI000031285233), S16 et S17, G.
  - Défaut : le projet réforme la nomination du conseil du fonds de solidarité vieillesse (FSV). Or le fonds a été supprimé : L. 135-1 a été abrogé au 1er janvier 2026 (loi n° 2025-199, article 24) et L. 222-2-1 transfère ses dépenses à la branche vieillesse.
  - Correction : la transition « nominations et renouvellements » est remplacée par une limitation aux opérations de dissolution et de liquidation. Les indemnités acquises sont conservées.
- **R135-14** (LEGIARTI000031285187), S17, G.
  - Défaut : l'article organise la trésorerie du fonds supprimé.
  - Correction (`replace`, l'article passe de maintenu à `rewrite_draft`, `coordination_only`) : il est limité aux placements et dépôts antérieurs, jusqu'à leur dénouement ou leur transfert.

### Variante W04ma (article du groupe W04)

- **R135-6** (LEGIARTI000038789272), S17, G.
  - Défaut : l'article maintient le comité de surveillance du fonds supprimé, avec une réunion annuelle et un avis sur le rapport d'activité.
  - Correction (`replace`, `coordination_only`) : le comité n'est plus réuni pour l'avenir. Le remboursement des frais des réunions antérieures est conservé.

## G non corrigés (pièce manquante)

- **R932-5-11** (W02, 2 pistes) : la notification transfrontalière repose sur L. 932-48 et L. 932-43, abrogés au 1er janvier 2023. LEGI marque L. 932-48 comme déplacé (DEPLACE) par l'ordonnance n° 2019-697, mais sa cible n'est pas au corpus.
- **A932-3-4** (W02) : le 4° renvoie au II de A. 932-3-14, abrogé au 5 décembre 2020. Le régime de remplacement relève du code des assurances, hors corpus.
- **D752-6** (W03) : l'article renvoie à L. 752-3-1, transféré le 23 juillet 2026. Sa cible (L760-15) est hors corpus. Même cas que R752-19 et R752-20 chez W01.

## Déjà réglé

Huit pistes S16 portent sur L643-6, L634-6 et L653-7, abrogés au 31 décembre 2025 par la loi n° 2025-1403, article 102. Les articles concernés sont D643-10, D643-10-1, D643-10-2, D634-11-1, D634-11-2, D634-11-5, D634-11-7 et R653-10. Leurs propositions limitent déjà l'article au régime ancien et réservent L. 161-22.

## Faux positifs

Cinq renvois visent en réalité un autre code :
- R932-4-2-4 : L. 144-2 du code des assurances ;
- D932-4-17 : L. 225-5 du code monétaire et financier ;
- R175-1 : L. 312-1 du code de l'action sociale et des familles ;
- D241-7 : L. 813-5 du code de la construction et de l'habitation ;
- D311-1 : L. 214-1 du code de l'environnement.

## Défauts m, non corrigés

- **D757-2 et D757-5**.
  - Défaut : ces articles relèvent de l'AVTS, régime fermé en 2006.
  - Pourquoi ils restent m : leurs propositions se bornent déjà aux droits maintenus par l'article 2 de l'ordonnance 2004-605.
- **R256-7**.
  - Défaut : il renvoie à R256-3 à R256-6, tous abrogés.
  - Pourquoi il reste m : la règle d'affectation reste opérante, et retirer la liste modifierait les ressources affectées.
- **Éléments de liste ou rubriques inertes**, sans effet normatif propre :
  - R351-21 ;
  - L160-7 ;
  - A931-11-10 ;
  - R243-59-9 ;
  - D412-79 ;
  - L311-3 ;
  - R753-2 ;
  - D221-1-1 ;
  - L114-16-3 ;
  - L315-1 ;
  - D311-1 (R141-1, R141-7 et D162-31).
- **Renvois à L162-1-17**, abrogé au 1er janvier 2026 : D162-11, R147-3, R147-9 et R147-9-2.
  - Ces renvois restent utiles aux mises sous accord préalable antérieures.
  - D162-10, version officielle du 31 décembre 2025, vise encore L. 162-1-17.
- **Versements forfaitaires du FSV**.
  - Articles : R135-15-1, R135-16 et R135-16-1 à R135-16-6.
  - Défaut : ils renvoient à L. 135-2 (conflit de source), alors que le décret officiel du 30 décembre 2025 a encore réécrit R135-16-2 en visant L. 135-2.
  - Pourquoi ils restent m : ces règles de calcul gardent une fonction pour L. 222-2-1, qui renvoie à un décret. Les rediriger demanderait le décret de 2025, hors corpus, et un choix sur le régime général, que L. 222-2-1 ne vise plus.
- **Autres articles** : D162-1-11, R931-12-7, R147-8, L162-22-3-2, R162-54-10, R762-36, R243-45-1, et R252-29 et D161-2-6 (F10).
  - Pour R162-54-10, la correction vers L165-6 étendrait un pouvoir de suspension : elle n'est pas alignée.

## Points pour l'auteur

- **Annexes orphelines.** Les autres annexes orphelines du CSS, hors de ce paquet, appellent la même abrogation. Ce sont celles de A951-1, A931-10-10, A931-11-9 (I), A931-11-11 (2), A931-11-20 (1) et A931-11-22, ainsi que les annexes de R611-21 et R611-31.
- **Fonds de solidarité vieillesse.**
  - Les articles d'organisation R135-1, R135-3 à R135-5 et R135-7 à R135-13, hors paquet, appellent la même limitation que R135-2, R135-6 et R135-14.
  - Les textes de dissolution et de liquidation du fonds, hors corpus, sont réservés sans être reconstitués.
- **Chapitre R731.** Les autres articles du chapitre (hors R731-3 et R731-3-1) organisent eux aussi le régime de L. 731-1, abrogé en 1994. Ils appellent la même limitation.
