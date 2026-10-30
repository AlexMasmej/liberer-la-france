# Groupe M02 : cinquième balayage, code du travail (pistes S16 et S17)

J'ai lu la production le 29 octobre 2026, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`). Rien n'a été écrit en production.

Le paquet contient 40 articles et 46 pistes :
- 10 G ;
- 17 m ;
- 16 faux positifs ;
- 3 déjà réglées.

Il y a 8 corrections : 1 dans `apply/M02`, 7 dans la variante `apply/W08mb`. Les deux dossiers sont validés par `check_changes.py`, avec `problems` vide. 15 demandes sont adressées au coordinateur.

## Règle de qualification

Pour la requalification S17, j'ai appliqué le critère de l'audit 5 (H091 D5134-1, A932-4-1, R5212-2-4).

**G** : le projet organise, réécrit ou présente comme vivant un régime dont la base légale est éteinte. L'article dépend alors entièrement d'un texte abrogé, ou son motif affirme qu'une faveur abolie est maintenue.

**m** : le renvoi mort est déclaratif, ou il figure dans une énumération à côté de cibles vivantes, sans effet sur la règle. Sont aussi m les défauts qui ne touchent que les notes (F10) et les dérogations simplement redondantes.

Les m ne sont pas corrigés, car je ne modifie pas ces articles.

## Corrections (G)

La correction est la même pour les huit articles : abrogation pour l'avenir. Les conventions, aides, exonérations, créances et recours antérieurs restent régis par les règles qui leur étaient applicables. Aucune aide, cotisation ni formalité de remplacement n'est créée. Chaque ligne porte `full_repeal` et un bilan `coordination_only`.

| Article | Dossier | Base légale éteinte | Ce qui change |
|---|---|---|---|
| D981-4 (LEGIARTI000037456714) | M02 | Ancien L981-6, applicable aux seuls contrats conclus avant le 1er janvier 2008, jusqu'à leur terme (NOTA de LEGIARTI000006651670, loi n° 2007-1822, art. 128 II) | Abrogation. Retrait de l'extension de l'exonération maritime aux contrats uniques futurs. Cette extension, ajoutée par le brouillon, relevait de la loi et n'avait pas été décidée. |
| D5134-8 (LEGIARTI000018526689) | W08mb | L5134-1, abrogé le 8 août 2015 | Abrogation de la durée de soixante mois de l'aide emplois-jeunes. |
| D5134-7 (LEGIARTI000018526693) | W08mb | L5134-11, abrogé le 8 août 2015 | Abrogation de la désignation du préfet. |
| D5134-6 (LEGIARTI000018526697) | W08mb | L5134-3, abrogé le 8 août 2015 | Abrogation. Le brouillon réglait les projets de convention « en cours » et « ultérieurs » d'un régime éteint. |
| D5134-2 (LEGIARTI000018526705) | W08mb | L5134-3, abrogé le 8 août 2015 | Abrogation du cahier des charges des conventions. |
| R5133-1 (LEGIARTI000020529422) | W08mb | L5133-1, abrogé le 1er janvier 2011 | Abrogation des conditions de la prime de retour à l'emploi. |
| D6325-19 (LEGIARTI000020690610) | W08mb | L6325-16 et L6325-17, abrogés le 1er janvier 2019 | Abrogation de la règle de calcul des heures exonérées. |
| D6325-19-1 (LEGIARTI000031088253) | W08mb | L6325-17, abrogé le 1er janvier 2019 | Abrogation du rattachement des GEIQ à l'exonération. L'aide de l'État et le cumul prévu par D6325-26 sont conservés. |

Dans chacun de ces articles, j'ai aussi corrigé les notes qui disaient les cibles « absentes du corpus » (F10).

## Demandes au coordinateur (`apply/W08mb/changes.json`, `requests`)

**Emplois-jeunes.** Abroger, dans les mêmes termes, D5134-1 et D5134-3 (propriétaire W08, hors paquet) ainsi que D5134-5 et D5134-9 à D5134-13 (sans propriétaire). D5134-4 proposé est déjà une abrogation. D5134-1 est le G H091 de l'audit 5.

**Prime de retour à l'emploi.** Abroger R5133-2 à R5133-8 (sans propriétaire). **Dépendance :** R5133-5 renvoie à R5133-1. Ces abrogations doivent donc être appliquées en même temps que celle de R5133-1. Sinon, R5133-5 renverrait à un article abrogé, dans un régime de toute façon éteint. L'aide personnalisée de retour à l'emploi (R5133-9 et suivants) n'est pas concernée.

## Pistes, une ligne chacune

| Article (LEGIARTI) | Piste | Qualification | Suite |
|---|---|---|---|
| D5134-8 (…26689) | S17 (S8, L5134-1) | G | Corrigé (W08mb) |
| D5134-7 (…26693) | S17 (S8, L5134-11) | G | Corrigé (W08mb) |
| D5134-6 (…26697) | S16 (L5134-3) | G | Corrigé (W08mb) |
| D5134-6 (…26697) | S17 (S8, L5134-3) | G | Même défaut, corrigé |
| D5134-2 (…26705) | S17 (S8, L5134-3) | G | Corrigé (W08mb) |
| R4211-1 (…32577) | S17 (S8, L4211-1) | m | Base légale déclarative, abrogée en 2021 ; L4744-1 vise désormais CCH L112-2, L134-13 et L155-2. Non corrigé. |
| R5133-1 (…29422) | S17 (S8, L5133-1) | G | Corrigé (W08mb) |
| D6325-19 (…90610) | S17 (S8, L6325-16) | G | Corrigé (W08mb) |
| D6325-19 (…90610) | S17 (S8, L6325-17) | G | Même défaut, corrigé |
| D6325-26 (…90617) | S17 (S8, L6325-16) | déjà réglé | Renvoi corrigé au deuxième audit (AUDIT2-T040) |
| D6325-26 (…90617) | S17 (S8, L6325-17) | déjà réglé | Idem |
| R3332-21-1 (…76877) | S16 (L213-5) | faux positif | Code monétaire et financier |
| R3332-21-1 (…76877) | S17 (notes) | m | F10. Non corrigé. |
| L6325-1-1 (…87275) | S17 (S8, L6332-15) | m | Renvoi mort dans une énumération, sans effet. Non corrigé. |
| D6325-19-1 (…88253) | S17 (S8, L6325-17) | G | Corrigé (W08mb) |
| R8115-6 (…92078) | S16 (L124-8) | faux positif | Code de l'éducation |
| L3134-1 (…21075) | S17 (notes) | m | F10. Non corrigé. |
| D5213-93 (…30547) | S16 (L241-6) | faux positif | CASF |
| D5213-91 (…30551) | S16 (L351-7) | faux positif | CGFP |
| R7232-16 (…47562) | S17 (notes) | m | F10. Non corrigé. |
| L3422-5 (…02495) | S17 (S5, version 2028) | m | Imprécision héritée. Le a) tronqué ne peut être complété sans l'ordonnance n° 2026-647 (pièce manquante). Non corrigé. |
| D1233-4 (…83183) | S17 (notes) | m | F10. Non corrigé. |
| R1233-9 (…83247) | S17 (notes) | m | F10. Non corrigé. |
| D981-4 (…56714) | S16 (L981-6) | G | Corrigé (M02). Vrai positif : même code, ancien numéro. |
| R3341-5 (…95163) | S16 (L224-3) | faux positif | Code monétaire et financier |
| L3312-8 (…56571) | S17 (S10) | m | Dérogation redondante. Non corrigé. |
| R5221-3 (…25451) | S16 (L422-1) | faux positif | CESEDA |
| D5132-43-10 (…95210) | S17 (S9x) | m | Dérogation sans objet. Non corrigé. |
| D5213-63 (…50343) | S16 (L412-3) | faux positif | Code pénitentiaire |
| R5213-62 (…50355) | S16 (L412-3) | faux positif | Code pénitentiaire |
| D3142-8 (…86859) | S16 (L434-2) | faux positif | CSS |
| R6523-24 (…45520) | S17 (S8, R6123-3-4) | m | Exclusion sans objet. Non corrigé. |
| L7232-1-2 (…43974) | S17 (S8, L7233-3) | m | Renvoi mort dans une énumération. Non corrigé. |
| L7232-1-1 (…44005) | S17 (S5, version 2027) | déjà réglé | L7233-2 version 2027 proposé (LEGIARTI000053151858) déroge à la déclaration. |
| L7232-1-1 (…44005) | S17 (S8, L7233-3) | m | Renvoi mort hérité. Non corrigé. |
| R5141-25 (…09749) | S16 (L511-1) | faux positif | Code monétaire et financier |
| D5213-63-1 (…25075) | S16 (L412-3) | faux positif | Code pénitentiaire |
| R5213-76 (…27323) | S16 (L412-3) | faux positif | Code pénitentiaire |
| R5311-13 (…16791) | S16 (L351-7) | faux positif | CGFP |
| R5132-2 (…16185) | S16 (L412-3) | faux positif | Code pénitentiaire |
| D6353-1 (…19671) | S16 (L6331-54) | m | Renvoi mort repris par la source de 2025, sans effet. Non corrigé. |
| D6353-1 (…19671) | S17 (S8, L6331-54) | m | Idem |
| L1237-19-1 (…37244) | S17 (S7) | m | Dérogation redondante. Non corrigé. |
| R3252-3 (…93590) | S16 (L513-1) | faux positif | CSS |
| R6123-16 (…28211) | S17 (S5, version 2027) | m | Renvoi inexact hérité, sans effet sur l'aide. Non corrigé. |
| R5221-2 (…63834) | S16 (L233-5) | faux positif | CESEDA |

## Points laissés à l'auteur

- **R4211-1.** Le titre pourrait être rattaché à CCH L112-2, L134-13 et L155-2, les articles que vise désormais L4744-1. Je ne l'ai pas fait : la concordance n'est pas établie.
- **Renvois morts m sans effet.** Un toilettage reste possible si l'auteur le souhaite : L6325-1-1 (L6332-15), D6353-1 (L6331-54), L7232-1-1 et L7232-1-2 (L7233-3), R6523-24 (6°).
- **Dates d'abrogation.** Les dates des lois d'abrogation (2011, 2015, 2019) viennent du corpus LEGI. Les textes abrogeants eux-mêmes n'ont pas été consultés.

Revue IA, sans validation par un juriste.
