# Y07 : troisième balayage (S9, S10), Code du travail, décisions

J'ai lu la production en lecture seule, le 29 octobre 2026, avec `CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`. Les copies des pièces sont dans `evidence/cited/production-20261029/`.

Le paquet `audit/sweeps/packet-Y07.json` contient 56 articles et 64 pistes : 59 S9 et 5 S10. Pour chaque piste, j'ai lu en entier la source, la proposition, le motif et les notes de l'article. J'ai lu aussi la proposition de la loi visée et sa ligne `removed_provisions`. Pour S10, j'ai lu l'article auquel la proposition déroge.

Le contrôle `python3 -B apply/check_changes.py Y07` donne 0 changement et `problems` vide.

Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Qualification | Pistes |
|---|---|
| G | 0 |
| m | 1 (L3312-8, S10) |
| déjà réglé | 47 |
| faux positif | 16 |

Aucune correction n'a été faite et aucune demande n'a été adressée à un autre groupe. Le fichier `changes.json` est vide.

## Défaut mineur, non corrigé

- **L3312-8** (LEGIARTI000042656571), piste S10/F5, qualifiée m.
  - L'article commence par « Par dérogation à l'article L. 3345-4 ». Or L3345-4 (LEGIARTI000046194018) proposé ne contient plus d'agrément.
  - Les deux textes disent la même chose : pas d'agrément. L3312-8 rappelle aussi la garantie du dernier alinéa de L3345-4. La formule est redondante et reste sans effet.
  - L3322-9 (LEGIARTI000042656568), hors paquet, emploie la même formule.
  - Correction possible si l'auteur le souhaite : supprimer les mots « Par dérogation à l'article L. 3345-4, ». Ce serait une retouche de forme, non faite ici.

## Pistes S9 : décret visant une loi réduite

Pour 47 pistes, le cas est **déjà réglé** : la proposition du décret retire déjà, ou rend facultative, la formalité supprimée par la loi. Elle prévoit une transition et aucune formalité de remplacement. Les pistes sont les suivantes :

- **Égalité professionnelle** : R2242-7 (L2242-3) et R2242-2-1.
- **Accords handicap** : R5212-18, R5212-15, R5212-12 et D5212-4.
- **Spectacles vivants** : R7122-11 (L7122-4 et L7122-7), R7122-7 (L7122-5 et L7122-4), R7122-6 et R7122-3.
- **Santé, embauche et licenciement** : R4163-36, R1221-3, R1233-3-5, R4822-1 et R6523-1.
- **Plateformes** : D7342-8 et D7342-7.
- **Formation et chantiers** : D6523-2-1, R4532-3, R5221-45, R1225-11, D1225-8 et R6351-13.
- **Épargne salariale** : D2231-8, D3323-4, D3323-1 (deux pistes), D3345-4 (deux pistes) et D3345-7.
- **Rupture conventionnelle et titres-mobilité** : D1237-3-1, R3261-13-3 et R3261-13-5.
- **Prévention et santé au travail** : R4641-8, R4641-4, R3132-5, D1142-6, R4121-4, R5424-72-2, R4623-39, D4622-44 et D4622-49-1 (deux pistes).
- **Dernières pistes d'épargne salariale** : D3345-5 et D3345-3 (L3323-4).

Pour 12 pistes, c'est un **faux positif** : la formalité détectée reste légale, ou le décret ne l'organise pas.

- **R2242-7 (L1142-9)** : la pénalité court jusqu'à la réception, par l'inspection, de la décision après mise en demeure. Ce n'est pas un dépôt autonome.
- **D5212-9 (maintenu)** : la déclaration de L5212-5 est maintenue.
- **R6224-8** : la déclaration de L6222-5 est maintenue. Le décret retire lui-même le visa du CFA.
- **R5122-9 et R5122-2** : l'autorisation d'activité partielle est maintenue. Les engagements nouveaux sont déjà retirés.
- **R7342-17 (maintenu)** : le décompte des alinéas a été vérifié. Le treizième alinéa de L7342-9 proposé reste celui de l'homologation.
- **R6523-2-14 (maintenu)** : l'agrément de L6332-1-1 est maintenu.
- **R7122-20 et R7122-17** : la DPAE unique de L1221-10 est maintenue.
- **R5424-71 (CGI 64 bis et 93)** : ce sont des renvois aux régimes d'imposition, sans formalité organisée.
- **D3345-3 (L3312-5)** : le procès-verbal de carence n'est pas une formalité retirée, et le dépôt d'intéressement reste prévu par L3313-3.

## Pistes S10 : dérogations entre propositions

| Article | Cible | Qualification | Motif |
|---|---|---|---|
| R6233-1 | L6231-2 et L6231-4 | faux positif | Les missions et la comptabilité visées existent encore. Les articles abrogés sont retirés du renvoi. |
| L3312-8 | L3345-4 | m | Voir plus haut. |
| D4625-22 | R4624-23 | faux positif | R4624-23 définit toujours les postes à risques particuliers. La réserve « sauf » est propre à D4625-22. |
| R6332-63 | R6332-33 | faux positif | Le texte rappelle l'abrogation de R6332-33 et ne déroge à aucune règle maintenue. |
| R6523-24 | R6523-19 | faux positif | R6523-19 contient toujours la composition du comité, et l'exception vise une règle existante. |

## Points pour l'auteur

Six notes de revue sont devenues inexactes (m, F10). Elles portent sur des articles que je n'ai pas modifiés, donc elles ne sont pas corrigées. Chacune décrit comme « hors lot, à coordonner » un texte qui est déjà coordonné en production :

- **R4641-8** dit que R4641-4 n'est pas coordonné, et **R4641-4** dit la même chose de R4641-8. Les deux le sont déjà.
- **D7342-7** dit que D7342-11 n'est pas coordonné. Il l'est.
- **R5221-45** dit que R5224-1 n'est pas coordonné. Il l'est.
- **R6351-13** dit que R6352-22 et R6352-23 ne sont pas coordonnés. Ils le sont.
- **R4623-39** dit que R4644-2 à R4644-5 et D4644-6 à D4644-9 ne sont pas coordonnés. Ils le sont.

Une correction groupée des notes pourrait les reprendre.

Une piste hors paquet, non examinée à fond, est laissée à l'auteur. **L3312-5** II (LEGIARTI000046194090) réserve la décision unilatérale aux entreprises « non couvertes par un accord de branche agréé ». Après la suppression générale de l'agrément par L3345-4, cette condition peut se lire de deux façons :

- toujours remplie, puisque plus aucun accord n'est agréé ;
- remplie seulement sans accord de branche du tout, si l'on applique la règle de L3345-4 qui supprime la condition d'agrément.

Ce choix touche à la portée d'une faveur. Il relève de l'auteur.

## Non traité

Néant : les 64 pistes sont qualifiées.
