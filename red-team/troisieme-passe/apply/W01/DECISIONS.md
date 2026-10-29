# W01 : balayage par famille de défauts (CSS), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`), le 29 octobre 2026. Paquet : `audit/sweeps/packet-W01.json`, soit 54 articles et 75 pistes. Contrôle : `python3 -B apply/check_changes.py W01` donne 7 lignes construites, 7 validées et `problems` vide. Les diagnostics sont tous voulus (renvois changés, réductions déclarées, longueur de R253-2).

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 10, dont 8 corrigées et 2 non corrigées (pièce manquante) |
| m | 19 : 17 annexes A931 orphelines, R256-7 et R351-21 |
| déjà réglé | 16 |
| faux positif | 30 |

Corrections : 7 lignes au total. Cinq sont en mode `replace` : A932-5, D644-2, R246-2, R251-3 et R253-2. Deux sont en mode `new` : L355-2 (version 2029) et R382-72 (version future). Une demande est adressée au groupe W04 pour R226-1.

## Défauts confirmés et corrigés

- **A932-5** (LEGIARTI000006735117), piste S7/F3, G, corrigé (`replace`, maintenu → `rewrite_draft`, `coordination_only`).
  - Défaut : le renvoi « au dernier alinéa de l'article R. 932-5-6 » vise désormais l'alinéa de transition que la proposition de R932-5-6 a ajouté à la fin de l'article. Cet alinéa ne fixe aucun seuil.
  - Correction : le renvoi devient « au sixième alinéa ». Les seuils restent inchangés.
- **D644-2** (LEGIARTI000006738164), piste S8/F3, G, corrigé (`replace`).
  - Défaut : l'article renvoie à D641-6, abrogé au 1er juillet 2026 par le décret n° 2026-418.
  - Correction : le renvoi devient « en vue de l'approbation prévue à l'article L. 641-5 ». La note fausse, qui disait D641-6 absent du corpus, est corrigée. Ajout d'un effet de coordination.
- **L355-2, version 2029** (LEGIARTI000052850993), piste S5/F4, G, corrigé (`new`).
  - Défaut : cette version future, issue de l'ordonnance n° 2025-1091, rétablit la saisie des pensions jusqu'à 90 % pour frais d'hospitalisation, que le projet supprime.
  - Correction : la réforme et sa transition sont reportées sur cette version. Le renvoi à l'article L. 4326-18 du code de procédure pénale (CPP) est repris tel quel. Cet article est hors corpus.
  - Défaut mineur non corrigé : la note de la version en vigueur (« régime successeur non fourni ») est inexacte. Elle n'a pas été modifiée (m, F10).
- **R246-2** (LEGIARTI000006748898), piste S8/F3, G, corrigé (`replace`, maintenu → `rewrite_draft`).
  - Défaut : l'article renvoie à R243-36, abrogé au 1er janvier 2024 par le décret n° 2023-1384.
  - Correction : le renvoi est remplacé par la désignation exacte des avantages que visait R243-36 (revenus de remplacement de L131-2 versés par une personne autre que l'employeur). Le champ ne change pas. Les notes fausses sont corrigées.
- **R251-3** (LEGIARTI000006749094), piste S8/F3, G, corrigé (`replace`).
  - Défaut : au 1° des recettes, les renvois à L241-1 (abrogé en 2016) et à L251-1 (abrogé en 2001) sont morts.
  - Correction : ces deux renvois sont retirés et seul L. 241-2 est conservé. Les notes fausses sont corrigées.
- **R382-72, version future** (LEGIARTI000025690160), piste S5/F4, G, corrigé (`new`).
  - Défaut : cette version (décret n° 2012-477, applicable « au prochain renouvellement général ») maintient l'exclusion des personnes condamnées à une peine contraventionnelle dans les cinq ans, que le projet supprime.
  - Correction : la suppression est reportée sur cette version. Le quota de nationalité en est déjà absent ; il n'est pas réécrit.
  - Point laissé à l'auteur : le corpus n'établit pas la date du renouvellement général.
- **R253-2** (LEGIARTI000022073019), pistes S8/F3 et AUDIT, G, corrigé (`replace`, `full_repeal`, `coordination_only`).
  - Défaut : l'article est vide de contenu. Ses deux renvois sont abrogés : R215-2 le 1er avril 2010, jour même de la création de R253-2, et L256-2 en 2001. Son motif et ses notes sont inexacts.
  - Correction : abrogation. Les règles comptables communes de L114-5 continuent de s'appliquer.
  - **Demande au groupe W04** : au 3° de R226-1 (LEGIARTI000038789394), supprimer « et R. 253-2 ».

## Défauts confirmés non corrigés

- **R752-19 et R752-20** (LEGIARTI000021647709 et LEGIARTI000021647722), pistes S8/F3, G, `skipped` (pièce manquante).
  - Défaut : les deux articles renvoient à L752-3-1, que l'ordonnance n° 2026-648 a transféré au 23 juillet 2026 vers L760-15.
  - Pourquoi rien n'est corrigé : L760-15 et l'ordonnance sont hors corpus. On ne peut pas vérifier que les subdivisions (I, 1° et 2°) se correspondent.
  - À faire par l'auteur : remplacer le numéro après avoir lu la cible.
- **17 pistes sur les annexes A931 du paquet**, m (conflit de source et anomalie d'inventaire), `skipped` (arbitrage). Annexes concernées : A931-11-16, annexe 1 de A931-11-17, A931-10-14, annexe 1 de A931-11-11, annexe 2 de A931-11-20 et A931-11-19.
  - Défaut : les articles que ces annexes complètent, et leurs cibles, sont abrogés au 1er janvier 2016 (régime antérieur à Solvabilité II). LEGI laisse pourtant les annexes en vigueur.
  - Ampleur : 21 annexes orphelines dans le CSS, dont 6 dans ce paquet. Les autres sont celles de A951-1, A931-10-10, A931-11-9 (I et II), A931-11-11 (2 et 3), A931-11-15, A931-11-17 (2 et 3), A931-11-20 (1), A931-11-21, A931-11-22 et A941-1-1, ainsi que les annexes de R611-21 et R611-31.
  - Pourquoi rien n'est corrigé : l'effet juridique est nul. Une abrogation systémique est proposée à l'auteur, mais elle n'est pas appliquée. L'arrêté du 30 décembre 2015 est hors corpus.
- **R256-7** (LEGIARTI000006748990), m (F3 et F10).
  - Défaut : R256-3 à R256-6 sont tous abrogés. La règle d'affectation des produits du patrimoine reste opérante.
  - Pourquoi rien n'est corrigé : retirer ou remplacer le renvoi modifierait les ressources affectées. C'est un arbitrage pour l'auteur.
- **R351-21** (LEGIARTI000006749360), m (F3 et F10).
  - Défaut : l'article renvoie à R351-31 (majoration pour conjoint), abrogé en 2011.
  - Pourquoi rien n'est corrigé : des majorations anciennes peuvent encore en dépendre (droits acquis possibles).

## Déjà réglé (16 pistes)

D174-1, D374-1, D374-2, D645-5, L244-4 (2 pistes), R213-5, R245-4 (3 pistes), R711-14, R752-1, R815-48, R815-52, R815-53 et R153-2. Pour chacun, la proposition borne déjà le renvoi aux situations antérieures à l'abrogation, ou retire le renvoi.

## Faux positifs (30 pistes)

- **Renvois à un autre code de même numéro** : L245-1, L245-3 et L245-12 du code de l'action sociale et des familles (CASF), dans L351-4-1, R541-10, D541-3 et R351-24-2 ; L723-1 et L723-5 du code rural, dans L153-3 et L152-1.
- **Alinéa visé resté à sa place** : L161-21, premier alinéa (5 pistes) ; L441-2, L441-4 et L441-5, premiers alinéas (5 pistes) ; L151-1, troisième alinéa (3 pistes) ; L241-10 ; L471-1 ; R731-3 ; L815-7 (2 pistes).
- **Renvois maintenus seulement pour le régime antérieur** : L245-2 dans R245-6 et L245-5-3 dans R245-16-2.
- **Renvoi transitoire utile** : L821-1-1 dans R821-5-2. Les notes sont inexactes (F10), sans effet.
- **Plage dont seule la borne est abrogée** : D242-6-21 dans D242-41. Les notes sont inexactes (F10), sans effet.

## Points pour l'auteur

1. Décider de l'abrogation systémique des 21 annexes orphelines du CSS.
2. Faire coordonner R752-19 et R752-20 vers L760-15 après lecture de la cible.
3. Faire appliquer par le groupe W04 la coordination de R226-1 3°.
4. Arbitrer le renvoi mort de R256-7.
5. Corriger les notes erronées de L355-2 (version en vigueur), R351-21, R821-5-2 et D242-41, qui disent absents du corpus des articles qui y figurent à l'état abrogé ou transféré.
