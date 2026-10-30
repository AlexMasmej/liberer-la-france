# Z01 : sixième balayage (CSS, pistes S16b, S18, S19a, S19b), décisions

Texte lu : la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite `mode=ro`), le 30 octobre 2026. Exports : `evidence/cited/production-20261030/`. Paquet : `audit/sweeps/packet-Z01.json`, soit 52 articles du CSS et 66 pistes. Qualification détaillée de chaque piste : `audit/sweeps/Z01.json`.

Contrôle : `python3 -B apply/check_changes.py Z01` donne 9 lignes construites, 9 validées et `problems` vide. Les diagnostics sont voulus :
- renvois changés : D758-2 (R381-36 et L721-1 remplacés par R382-57) ; R731-20 et R731-21 (L731-2 et L731-3 cités dans la clause d'abrogation) ;
- réductions et abrogations déclarées : R731-20, R731-21 (`full_repeal`) ; R757-1, D752-2-5 et D752-2-6 (réductions antérieures inchangées) ;
- D752-2-6 : le retrait du renvoi à D752-2-3 date de la proposition antérieure.

Rien n'a été écrit en production. Revue faite par une IA, sans validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 11, toutes corrigées (9 lignes) |
| m | 13, non corrigées (articles non modifiés) |
| déjà réglé | 6 |
| faux positif | 36 |

- Corrections : 9 lignes en mode `replace`, toutes dans `apply/Z01/`. Il n'y a ni `new` ni `skipped`.
- Dossiers de variante : aucun. Les quatre articles qui ont un `previous_owner` sont des faux positifs ou des cas déjà réglés : L138-7 (B04), L443-1 et L434-16 (A6), R146-8 (B01).
- Demandes (`requests`) : 2, pour D752-2-3 (non attribué) et D752-2-1 (Z02).

## Corrections (G)

- **D758-2** (LEGIARTI000006739017, maintenu), S16b, F3.
  - Défaut : l'article rend applicable « L'article R. 381-36 » aux titulaires de la pension « instituée par l'article L. 721-1 ». R381-36 a été transféré au 1er novembre 2006 (CONCORDANCE vers R382-57) et L721-1 a pris fin le 20 décembre 2005.
  - Correction : le renvoi vise R. 382-57 et « les titulaires [...] mentionnés à cet article ». C'est une coordination à droit constant (`coordination_only`), sans extension. R382-57 couvre déjà les territoires de L111-2.
- **R731-20** (LEGIARTI000006753046) et **R731-21** (LEGIARTI000006753048), maintenus, S16b, F3.
  - Défaut : ces articles désignent les ministres compétents pour les arrêtés de L731-9 et L731-10. Ces deux articles ont été transférés le 2 janvier 1990 vers L731-2 et L731-3, eux-mêmes abrogés le 10 août 1994.
  - Pourquoi abroger plutôt que rediriger : L911-3 et L911-4 désignent aujourd'hui le seul ministre chargé de la sécurité sociale. Un renvoi redirigé y ajouterait une cosignature du budget, c'est-à-dire une contrainte.
  - Correction : `full_repeal`. Les arrêtés antérieurs sont conservés et aucune formalité de remplacement n'est créée.
- **R757-1** (LEGIARTI000027268435), S16b, F3 et F6.
  - Défaut : la proposition organise l'octroi de l'allocation supplémentaire pour les « demandes présentées à compter de l'entrée en vigueur du décret ». Or L757-2 est abrogé depuis le 1er janvier 2006, sous réserve de l'article 2 de l'ordonnance n° 2004-605 (NOTA de LEGIARTI000006744493). C'est le même défaut que R731-3 dans M01.
  - Correction : l'article ne s'applique plus qu'aux droits maintenus par cet article 2, sans attribution nouvelle.
  - Ce qui est conservé : la suppression de la décision préalable de la commission, les exclusions de ressources, les prestations acquises et les recours.
  - Les notes erronées sont corrigées : L757-2 était dit absent du corpus, et L751-1 dit sans successeur en 2028.
- **R412-6** (LEGIARTI000006750508, maintenu, sans version future), S19a, F3.
  - Défaut : l'article réserve « le quatrième alinéa de l'article L. 434-2 », qui vise les accidents successifs. Dans la version de L434-2 du 1er novembre 2026 (LEGIARTI000051288493), cette règle passe au III et le quatrième alinéa devient le II (tierce personne).
  - Correction : la réserve vise « les dispositions de l'article L. 434-2 relatives aux accidents successifs », formule exacte dans les deux rédactions.
- **D752-2-2**, **D752-2-4** (maintenus), **D752-2-5** et **D752-2-6** (proposés), S19a, F3.
  - Défaut : à compter du 1er janvier 2028 (L752-1, LEGIARTI000054466934, ordonnance n° 2026-647), le troisième alinéa de L752-1 vise Saint-Martin, le quatrième la caisse de MSA de Saint-Barthélemy et le cinquième le conseil de suivi. Les renvois au « troisième » et au « quatrième alinéa » deviennent donc faux.
  - Correction : la caisse et le conseil sont désignés par leur objet, sans numéro d'alinéa. C'est la correction suggérée par l'audit E08 (E148, G).
  - Les réductions déjà proposées (réunions, rapport annuel) sont inchangées.

## Demandes à d'autres groupes

- **D752-2-3** (LEGIARTI000034730990, non attribué) : même substitution dans la proposition, et correction de la note « Successeur de L752-1 au 1er janvier 2028 absent ».
- **D752-2-1** (LEGIARTI000041968338, Z02) : même substitution. À ignorer si Z02 l'a déjà faite.

## Pistes non corrigées

- **S18 (29 pistes) : 26 faux positifs, 3 déjà réglées.**
  - Faux positifs : D242-27, D413-9, L766-11, L711-2, L821-6, R262-10, R382-103, R711-25, R553-3-5, D521-4, A931-1-10, D848-5, L382-29, R162-30-1, R243-44, L380-3-1, L652-9 et R762-12. L'article abrogé n'y figure que dans une clause de transition ou de non-rétablissement.
  - Déjà réglées : L138-7 (correction RT-P1-CSS-A-02) et L243-2, deux pistes (renvois bornés par des alinéas exprès).
- **S16b, cas déjà réglés** : D821-4 et D821-3 (« dans sa rédaction demeurant applicable ») ; D634-11-3 (borné aux assurés régis par l'ancien L634-6).
- **S16b, défauts m** : renvois morts de la source, sans effet sur les droits, ou dont la cible de remplacement manque au corpus.
  - D412-11 : L432-5, dans une plage encore opérante.
  - D757-3 : L811-8, AVTS maintenue par l'ordonnance n° 2004-605 ; même qualification que D757-2 dans M01.
  - D712-46 : L361-3.
  - R251-5, R251-6, R251-7, R251-7-1 et R262-1 : L251-1. Les fonds subsistent, mais la base de l'arrêté de répartition manque au corpus.
  - R731-18 : L731-1. La désignation de l'autorité reste utile aux institutions autorisées avant 1994.
  - R256-9 : L256-2.
  - D643-9 : L622-7 et L811-1. Le montant de l'AVTS reste une référence, et D643-13 y renvoie.
  - Les notes de plusieurs de ces articles disent la cible « absente du corpus », ce qui est inexact (F10). Elles n'ont pas été corrigées, car les articles ne sont pas modifiés.
- **S19a, faux positifs** :
  - R434-1, R434-2, R434-3, R443-7 et D434-2 : leur version prend fin le 1er novembre 2026, et leurs versions suivantes (décrets n° 2026-354 et 2026-355) visent déjà le I, le II ou le III de L434-2.
  - L443-1 et L434-16 (A6) : leurs versions de remplacement portent déjà une proposition (RT-INV-03).
- **S19a, défaut m** : annexe I à R434-32 (17). Le renvoi au « premier alinéa de l'article L. 434-2 » reste exact pour les victimes consolidées avant le 1er novembre 2026. Après cette date, le barème relève d'un arrêté (L434-1 A), hors corpus.
- **S19b, faux positif** : R146-8, version future (B01). Elle étend R145-13 à R145-68 par renvoi, sans les réécrire, et son 3° correspond à la proposition de R145-48.

## Points pour l'auteur

- R731-18 : le chapitre R. 731 ne vit plus que pour les institutions autorisées avant 1994. Son abrogation d'ensemble est un choix à faire.
- R251-5 à R251-7-1 et R262-1 : il faut identifier le fondement actuel de l'arrêté de répartition des fonds nationaux pour corriger le renvoi à L251-1.
- Barèmes annexés à R434-32 : leur champ après le 1er novembre 2026 reste à fixer quand l'arrêté prévu par L434-1 A sera connu.

Revue IA : rien de ceci ne vaut validation par un juriste.
