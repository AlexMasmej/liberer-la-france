# J07 : quatrième balayage (S9x, S12, S13), décisions

J'ai lu la production en lecture seule le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro`. Les exports sont dans `evidence/cited/production-20261029/`. Le paquet `audit/sweeps/packet-J07.json` compte 47 articles du CCH et 66 pistes : 56 S9x, 7 S12 et 3 S13.

Méthode :
- **S9x** : j'ai lu les `removed_provisions` de la loi visée et sa proposition entière, puis vérifié si le texte d'application organise encore ce qui a été retiré.
- **Grandes annexes** (annexe I à D353-1, annexes I et II à D353-90, annexe 1 au III de R353-159) : j'ai cherché les dispositions retirées dans le texte entier et lu les clauses trouvées. Je ne les ai pas relues ligne à ligne.
- **S12** : j'ai lu toutes les versions de l'article cité, y compris `VIGUEUR_DIFF`, avec leur NOTA.
- **S13** : j'ai lu la cible entière.

Contrôle : `python3 -B apply/check_changes.py J07` donne 1 ligne construite et validée, et `problems` est vide. Les diagnostics `length_change` (ratio 2,51 par rapport à la source) et `references_changed` (ajout de D302-35) viennent de la proposition existante. Ma correction ne les a pas créés.

Rien n'a été écrit en production. Cette revue est faite par une IA et ne vaut pas validation par un juriste.

## Bilan

| Qualification | S9x | S12 | S13 | Total |
|---|---|---|---|---|
| G | 0 | 1 | 0 | 1 |
| m | 0 | 5 | 0 | 5 |
| déjà réglé | 35 | 0 | 0 | 35 |
| faux positif | 21 | 1 | 3 | 25 |

Il y a une correction, sur D302-31. Aucune demande à un autre groupe (`requests` vide) et rien d'écarté (`skipped` vide).

Les articles détenus par un autre groupe sont les annexes I et II à D353-90 et l'annexe 1 au III de R353-159 (Y12), ainsi que R302-15 (B06). Aucun ne reçoit de correction : leurs pistes sont `m`, `déjà réglé` ou `faux positif`. Je n'ai donc créé aucun dossier de variante (`apply/Y12jg/` ou `apply/B06jg/`), puisqu'il n'y avait rien à y valider.

À noter : le paquet indique `previous_owner: null` pour l'annexe II à D353-90 (LEGIARTI000053356309), alors que `apply/assignment.json` l'attribue à Y12.

## Correction appliquée

**SWEEP-J07-D302-31 : D302-31 (LEGIARTI000044028256), piste S12/F4, G, appliquée (mode `replace`).**
- **Défaut.** Le troisième alinéa disait : « L'obligation de transmission prévue par la présente sous-section cesse au plus tard à l'abrogation de l'article L. 302-16-1 le 1er janvier 2027. Aucune transmission ni aucun dépôt de rattrapage ne sont exigés après cette date ». Or L302-16-1 LEGIARTI000054567276 (`VIGUEUR_DIFF` au 1er janvier 2027, ordonnance n° 2025-1247 modifiée par l'ordonnance n° 2026-671) maintient l'obligation d'information. La proposition de L302-16-1 a déjà retiré la même cessation au titre de RT-FUTTL-02.
- **Effet du défaut.** Le décret aurait éteint au 1er janvier 2027 l'exécution d'une obligation que la loi publiée maintient.
- **Changement.** Les phrases de cessation, de « rattrapage » et sur « cette cessation » sont remplacées par : « Les références à l'article L. 302-16-1 visent cet article dans sa rédaction en vigueur à la date de la transmission. » Les droits d'accès et de rectification sont conservés. Les deux premiers alinéas sont inchangés, ainsi que les allègements de D302-33 et D302-35.
- **Mise à jour du dossier.** Le motif, les notes et `overrides.substantive_impact` sont mis à jour. La citation `proposed_quote` est exacte et le certificat est recalculé par l'outil. Deux affirmations fausses des notes sont corrigées (F10) : « cette version est à abrogation différée » et « Cessation au 1er janvier 2027 ».
- **Alignement.** Il s'agit d'une coordination neutre. Elle ne crée aucune formalité nouvelle et ne recrée aucune étape supprimée ailleurs. Elle n'arbitre aucun choix politique : la réduction supprimée reposait sur une abrogation qui n'existe pas.
- **Point laissé à l'auteur.** À compter de 2027, le premier alinéa vise encore le 2° du I de CGI 279-0 bis A, alors que L302-16-1 renvoie au CIBS L. 231-74, hors corpus. C'est une réserve documentaire. Je n'ai inventé aucune équivalence.

## Défauts `m`, non corrigés

Ces articles appartiennent à Y12 et ne sont pas modifiés ici. Le brief ne permet de corriger un `m` que sur un article déjà modifié.

- **Annexe I à D353-90 (LEGIARTI000051283462), pistes R824-1 et R824-4.** Le texte dit : « ne prorogent pas leur application au-delà de leur abrogation prévue le 1er janvier 2027 ».
  - Les versions 2027 (LEGIARTI000053470474 et LEGIARTI000053470467, NOTA du décret n° 2026-84) donnent à ces numéros un autre contenu : il ne s'agit pas d'une abrogation. Le mot est donc inexact.
  - L'effet reste juste : l'annexe renvoie, à compter de cette date, aux « dispositions réglementaires applicables prises pour l'exécution de l'article L. 824-1 ».
  - C'est le même défaut que RT-FUTTL-11 (P2).
- **Annexe II à D353-90 (LEGIARTI000053356309), piste R824-4.** Le texte dit : « elle ne proroge pas cet article au-delà de son abrogation ». Même remarque.
- **Annexe 1 au III de R353-159 (LEGIARTI000053561433), pistes R824-4 et R824-7.** Le texte dit : « ne proroge pas les dispositions des articles R. 824-4 et R. 824-7 au-delà de leur abrogation ».
  - R824-7 en 2027 (LEGIARTI000053470483) pose une règle plus favorable, le maintien de l'aide en cas d'impossibilité manifeste. Elle s'applique par le renvoi déjà présent aux « dispositions réglementaires applicables dans le temps ».
- **Correction possible, si l'auteur le souhaite.** Remplacer « au-delà de leur abrogation [prévue le 1er janvier 2027] » par « au-delà du 1er janvier 2027, date à laquelle ces articles reçoivent la rédaction issue du décret n° 2026-84 du 12 février 2026 ».

## Constats connexes, hors pistes, non corrigés

- **F10, notes devenues fausses.** Ces articles sont déjà coordonnés par leur proposition ou par celle de la cible, mais leurs notes disent encore le contraire :
  - R165-21 (LEGIARTI000043819365) : « R165-3 proposé n'est pas encore aligné » ;
  - D319-38 (LEGIARTI000050042800) et D319-48 (LEGIARTI000049356928) : « D319-28 et D319-55 [...] restent à coordonner » ;
  - annexe I à D353-1 (LEGIARTI000053537885) : les textes successeurs de R824-1 et R824-4 « ne sont pas fournis », alors qu'ils sont au corpus.
- **Défaut déjà connu.** L441-1-5 proposé (LEGIARTI000045136844), 1° ter, vise encore « un taux supérieur au taux minimal des attributions annuelles de logements situés dans les quartiers prioritaires [...] prévu au même article L. 441-1 », alors que L441-1 proposé n'en prévoit plus aucun. Le défaut est déjà relevé (S11pilot-P5, qualifié `m`). Je n'ai fait aucune demande.
- **Défaut signalé par D353-61, non vérifié.** Les notes de D353-61 (LEGIARTI000053537918) disent que les articles 3 et 7, 4°, de l'annexe I à D353-59 gardent la notification solennelle et le bilan. Ce point est hors paquet et je ne l'ai pas vérifié.

## Une ligne par piste

| Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|
| R812-6 (LEGIARTI000039502553) | S9x/F1+F5 | L812-1 | déjà réglé | non |
| R441-2-16 (LEGIARTI000039636411) | S9x/F1+F5 | L441-1 | faux positif | non |
| R441-2-15 (LEGIARTI000039636874) | S9x/F1+F5 | L441-1 | déjà réglé | non |
| R441-2-15 (LEGIARTI000039636874) | S9x/F1+F5 | L441-1-5 | déjà réglé | non |
| R441-2-15 (LEGIARTI000039636874) | S9x/F1+F5 | L441-1-6 | déjà réglé | non |
| R441-2-15 (LEGIARTI000039636874) | S9x/F1+F5 | L441-1-1 | déjà réglé | non |
| R441-2-15 (LEGIARTI000039636874) | S9x/F1+F5 | L441-2-7 | faux positif | non |
| R442-2 (LEGIARTI000039652821) | S9x/F1+F5 | L442-1 | déjà réglé | non |
| D832-2 (LEGIARTI000041477269) | S9x/F1+F5 | L822-4 | déjà réglé | non |
| R441-5-1 (LEGIARTI000041612753) | S9x/F1+F5 | L441-1 | déjà réglé | non |
| R445-6 (LEGIARTI000041615522) | S9x/F1+F5 | L441-1 | déjà réglé | non |
| R445-6 (LEGIARTI000041615522) | S9x/F1+F5 | L441-1-6 | déjà réglé | non |
| R113-9 (LEGIARTI000043818335) | S9x/F1+F5 | L113-17 | déjà réglé | non |
| R131-4 (LEGIARTI000043818689) | S9x/F1+F5 | L131-3 | déjà réglé | non |
| R134-12 (LEGIARTI000043818749) | S9x/F1+F5 | L134-4 | déjà réglé | non |
| R165-2 (LEGIARTI000043819313) | S9x/F1+F5 | L164-2 | déjà réglé | non |
| R165-3 (LEGIARTI000043819317) | S9x/F1+F5 | L164-2 | déjà réglé | non |
| R165-18 (LEGIARTI000043819359) | S9x/F1+F5 | L164-2 | déjà réglé | non |
| R165-21 (LEGIARTI000043819365) | S9x/F1+F5 | L164-2 | déjà réglé | non |
| R174-24 (LEGIARTI000043819507) | S9x/F1+F5 | L174-1 | faux positif | non |
| R174-31 (LEGIARTI000043819527) | S9x/F1+F5 | L174-1 | déjà réglé | non |
| R186-1 (LEGIARTI000043819591) | S9x/F1+F5 | L134-4 | déjà réglé | non |
| R186-1 (LEGIARTI000043819591) | S13/F3 | R134-8 | faux positif | non |
| D302-31 (LEGIARTI000044028256) | S12/F4 | L302-16-1 | G | oui (SWEEP-J07-D302-31) |
| R174-27 (LEGIARTI000044133897) | S9x/F1+F5 | L174-1 | faux positif | non |
| R863-2 (LEGIARTI000044636777) | S9x/F1+F5 | L812-3 | faux positif | non |
| R481-12 (LEGIARTI000044636898) | S9x/F1+F5 | L442-3 | déjà réglé | non |
| R411-3 (LEGIARTI000044636960) | S9x/F1+F5 | L443-11 | faux positif | non |
| R313-7 (LEGIARTI000044636969) | S13/F3 | R313-20-2 | faux positif | non |
| D353-59 (LEGIARTI000044636997) | S9x/F1+F5 | 278 sexies | faux positif | non |
| R353-163 (LEGIARTI000044845840) | S9x/F1+F5 | L441-1 | faux positif | non |
| R481-6 (LEGIARTI000045646946) | S9x/F1+F5 | L481-6 | déjà réglé | non |
| R302-1-4 (LEGIARTI000046415198) | S9x/F1+F5 | L302-1 | déjà réglé | non |
| R441-1-3 (LEGIARTI000047372336) | S9x/F1+F5 | L302-1 | faux positif | non |
| R441-1-3 (LEGIARTI000047372336) | S9x/F1+F5 | L441-1-6 | faux positif | non |
| R171-35 (LEGIARTI000048597085) | S9x/F1+F5 | L171-4 | déjà réglé | non |
| L31-10-3 (LEGIARTI000048826429) | S12/F4 | L31-10-2 | faux positif | non |
| D319-48 (LEGIARTI000049356928) | S9x/F1+F5 | 244 quater U | déjà réglé | non |
| R442-13 (LEGIARTI000049794981) | S9x/F1+F5 | L442-5 | déjà réglé | non |
| D319-55 (LEGIARTI000050040314) | S9x/F1+F5 | 244 quater U | déjà réglé | non |
| D319-38 (LEGIARTI000050042800) | S9x/F1+F5 | 244 quater U | déjà réglé | non |
| Annexe III à l'article D353-1 (LEGIARTI000051283362) | S9x/F1+F5 | L631-12 | faux positif | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S12/F4 | R824-1 | m | non |
| Annexe I à l'article D353-90 (LEGIARTI000051283462) | S12/F4 | R824-4 | m | non |
| R126-43-3 (LEGIARTI000052098089) | S9x/F1+F5 | L126-6-1 | déjà réglé | non |
| R126-43-9 (LEGIARTI000052098101) | S9x/F1+F5 | L126-6-1 | faux positif | non |
| R321-5 (LEGIARTI000052830191) | S9x/F1+F5 | L303-1 | faux positif | non |
| Annexe II à l'article D353-90 (LEGIARTI000053356309) | S12/F4 | R824-4 | m | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L442-5 | déjà réglé | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L441-9 | déjà réglé | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | 284 | déjà réglé | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L342-14 | faux positif | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L301-5-1 | faux positif | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L353-15 | faux positif | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L631-12 | faux positif | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L443-10 | faux positif | non |
| Annexe I à l'article D353-1 (LEGIARTI000053537885) | S9x/F1+F5 | L442-8-1 | faux positif | non |
| D353-61 (LEGIARTI000053537918) | S9x/F1+F5 | L442-5 | déjà réglé | non |
| D353-4 (LEGIARTI000053537920) | S9x/F1+F5 | L442-5 | déjà réglé | non |
| D353-4 (LEGIARTI000053537920) | S9x/F1+F5 | L441-9 | déjà réglé | non |
| Annexe 1 au III art R353-159 (LEGIARTI000053561433) | S12/F4 | R824-4 | m | non |
| Annexe 1 au III art R353-159 (LEGIARTI000053561433) | S12/F4 | R824-7 | m | non |
| R134-7 (LEGIARTI000053629120) | S13/F3 | R134-8 | faux positif | non |
| R302-15 (LEGIARTI000054551209) | S9x/F1+F5 | L302-5 | déjà réglé | non |
| D443-34 (LEGIARTI000054756955) | S9x/F1+F5 | L421-1 | faux positif | non |
| D443-34 (LEGIARTI000054756955) | S9x/F1+F5 | L422-2 | faux positif | non |
