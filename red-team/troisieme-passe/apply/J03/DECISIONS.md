# Groupe J03 — décisions (quatrième balayage)

Lecture : production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py css …` et sqlite en `mode=ro`, `query_only`). Paquet : `audit/sweeps/packet-J03.json`, 59 articles et 65 pistes, tous du code de la sécurité sociale : 58 S9x, 4 S12, 1 S13 et 2 S15. Pour chaque piste S9x, j'ai lu les `removed_provisions` du lot de la loi visée, la proposition entière de cette loi, puis le texte d'application (proposition, ou source s'il est maintenu). Pour S12, j'ai vérifié si la phrase tient l'article cité pour abrogé et si sa version suivante le conserve. Pour S13, j'ai lu la rédaction de L161-22 à laquelle le renvoi est rattaché. Pour S15, j'ai vérifié que la loi visée fait bien, en production, la modification attendue. Toutes les citations de `audit/sweeps/J03.json` ont été contrôlées mot pour mot par script contre la production.

## Bilan

- 65 pistes : 44 déjà réglées, 20 faux positifs, 1 défaut mineur (m), aucun défaut grossier (G).
- Aucune correction : `apply/J03/changes.json` est vide (`changes`, `requests` et `skipped` vides). `python3 -B apply/check_changes.py J03` renvoie `problems: []`.
- Articles avec `previous_owner` : R147-9-2 (Y03), R351-37 (A6) et R133-14 (B03). Aucun ne demande de correction : R147-9-2 est un faux positif, R351-37 et R133-14 sont déjà réglés. Je n'ai donc créé aucun dossier de variante (`Y03jc`, `A6jc`, `B03jc`).

## Constats

- **S9x (58 pistes).** Les textes d'application qui portaient la formalité, la condition ou la majoration retirée de la loi ont déjà été alignés dans leur proposition, avec leur transition : par exemple R711-21, R142-8, D412-54, R160-17, R382-8-4 et R382-16-5 pour le recours préalable facultatif de L142-4 ; R166-1, R166-3 et R166-4 pour les remises sans versement provisionnel de L165-4. Les autres pistes ne partagent avec la loi que des mots courants. Le décret y garde une fonction utile et distincte : guichet unique, traitement de données, ventilation du forfait, garantie de non-révision de R353-13.
- **S12 (4 pistes).** Ce sont toutes des faux positifs : le mot « Abrogé » désigne un item voisin (4° de R147-9-2, 3° du II de L161-22-1-5, 1° a) du III de L136-1-1, 2° à 5° de L162-1-15). L'article cité reste visé et ses versions suivantes gardent les items visés (L412-8 de 2029, L431-1 du 1er novembre 2026).
- **S13 (1 piste).** D161-2-6 : le renvoi au 7° de L161-22 est déjà rattaché à la rédaction antérieure. Celle-ci (LEGIARTI000047453712) contient bien ce 7°. Il reste un défaut **m (F10)** : les notes affirment « La version historique intégrale de L161-22 n'est pas fournie dans le corpus consulté », alors qu'elle y figure. Je ne l'ai pas corrigé, faute de modifier l'article par ailleurs (BRIEF-SWEEP, point 4).
- **S15 (2 pistes).** Ce sont des faux positifs. La modification législative attendue existe en production : le récapitulatif du bulletin dans L133-5-8 (LEGIARTI000037947939) pour D133-13-3, et le caractère exécutoire des délibérations dès leur adoption dans L382-2 (LEGIARTI000053282099) pour R382-8-1.

## Points laissés à l'auteur (sans correction)

- R243-15, III : la contribution provisoire OETH reste majorée de 25 % (plus cinq points par échéance non déclarée). La proposition la tient expressément pour une contribution distincte, hors champ de L242-12-1. C'est un choix explicite du projet ; le rouvrir supposerait un arbitrage.
- R165-109 : le « 4° » est une interdiction rangée parmi les finalités du traitement. C'est une maladresse de forme sans effet, que je n'ai pas corrigée.
- L861-3 et L861-5 figurent en `ABROGE_DIFF` avec une borne au 22 février 2222. Cette anomalie de dates du corpus est hors du périmètre de ce balayage.

## Une ligne par piste

| # | Article | Piste | Cible | Qualification | Correction |
|---|---|---|---|---|---|
| 1 | R861-36 (LEGIARTI000045598338) | S9x/F1+F5 | css L861-5 (LEGIARTI000046806509) | déjà réglé | non |
| 2 | R861-16-5 (LEGIARTI000045601961) | S9x/F1+F5 | css L861-5 (LEGIARTI000046806509) | faux positif | non |
| 3 | R162-34-4 (LEGIARTI000045635658) | S9x/F1+F5 | css L162-23-8 (LEGIARTI000053283299) | faux positif | non |
| 4 | R200-1 (LEGIARTI000046021757) | S9x/F1+F5 | css L200-3 (LEGIARTI000045355354) | déjà réglé | non |
| 5 | D223-4 (LEGIARTI000046022014) | S9x/F1+F5 | css L162-31 (LEGIARTI000044404258) | faux positif | non |
| 6 | R711-21 (LEGIARTI000046086977) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 7 | R522-4 (LEGIARTI000046498997) | S9x/F1+F5 | css L522-3 (LEGIARTI000028394454) | déjà réglé | non |
| 8 | R531-1 (LEGIARTI000046499008) | S9x/F1+F5 | css L531-2 (LEGIARTI000042685543) | déjà réglé | non |
| 9 | R531-1 (LEGIARTI000046499008) | S9x/F1+F5 | css L531-3 (LEGIARTI000036393143) | déjà réglé | non |
| 10 | R522-2 (LEGIARTI000046499019) | S9x/F1+F5 | css L522-2 (LEGIARTI000036393166) | déjà réglé | non |
| 11 | D861-4 (LEGIARTI000046824497) | S9x/F1+F5 | css L861-3 (LEGIARTI000046812151) | faux positif | non |
| 12 | R162-118 (LEGIARTI000047382409) | S9x/F1+F5 | css L162-1-23 (LEGIARTI000048703007) | déjà réglé | non |
| 13 | R243-15 (LEGIARTI000047480899) | S9x/F1+F5 | css L242-12-1 (LEGIARTI000025009254) | déjà réglé | non |
| 14 | R147-9-2 (LEGIARTI000047502404) | S12/F4 | css L114-9 (LEGIARTI000054331835) | faux positif | non |
| 15 | R351-37 (LEGIARTI000047633235) | S9x/F1+F5 | css L351-1-4 (LEGIARTI000053281659) | déjà réglé | non |
| 16 | D221-50 (LEGIARTI000047959974) | S9x/F1+F5 | css L221-1-5 (LEGIARTI000047449926) | déjà réglé | non |
| 17 | D161-2-6 (LEGIARTI000047961757) | S13/F3 ; S13/F3 réglé ; F10 résiduel | css L161-22 (LEGIARTI000053279730) | m | non |
| 18 | R114-14 (LEGIARTI000048831074) | S9x/F1+F5 | css L114-17 (LEGIARTI000054331851) | déjà réglé | non |
| 19 | R165-86 (LEGIARTI000048831266) | S9x/F1+F5 | css L165-1-4 (LEGIARTI000054335726) | déjà réglé | non |
| 20 | D133-13-3 (LEGIARTI000048864525) | S15/F5 | — | faux positif | non |
| 21 | D133-7 (LEGIARTI000048864602) | S9x/F1+F5 | css L133-5-3 (LEGIARTI000051287164) | déjà réglé | non |
| 22 | R544-3 (LEGIARTI000049090510) | S9x/F1+F5 | css L544-3 (LEGIARTI000047864753) | déjà réglé | non |
| 23 | R162-128 (LEGIARTI000049351207) | S9x/F1+F5 | css L162-1-7 (LEGIARTI000053283421) | faux positif | non |
| 24 | R160-17 (LEGIARTI000049902786) | S9x/F1+F5 | css L160-14 (LEGIARTI000054711279) | faux positif | non |
| 25 | R160-17 (LEGIARTI000049902786) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 26 | R160-17 (LEGIARTI000049902786) | S9x/F1+F5 | css L162-13-2 (LEGIARTI000046812009) | faux positif | non |
| 27 | R162-113 (LEGIARTI000050942692) | S9x/F1+F5 | css L165-1-5 (LEGIARTI000046812781) | faux positif | non |
| 28 | R165-109 (LEGIARTI000051349128) | S9x/F1+F5 | css L165-1-8 (LEGIARTI000051285341) | déjà réglé | non |
| 29 | R165-105 (LEGIARTI000051349822) | S9x/F1+F5 | css L165-1-8 (LEGIARTI000051285341) | déjà réglé | non |
| 30 | D241-25 (LEGIARTI000051434553) | S9x/F1+F5 | css L241-18 (LEGIARTI000038610232) | déjà réglé | non |
| 31 | D241-25 (LEGIARTI000051434553) | S9x/F1+F5 | css L241-18-1 (LEGIARTI000053278678) | déjà réglé | non |
| 32 | R382-136 (LEGIARTI000051828247) | S9x/F1+F5 | css L382-44 (LEGIARTI000046448510) | déjà réglé | non |
| 33 | R142-8 (LEGIARTI000051829785) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 34 | D412-54 (LEGIARTI000051831566) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 35 | R613-1-2 (LEGIARTI000051999757) | S9x/F1+F5 | css L242-12-1 (LEGIARTI000025009254) | déjà réglé | non |
| 36 | R178-4 (LEGIARTI000052196489) | S9x/F1+F5 | css L223-13 (LEGIARTI000051285388) | déjà réglé | non |
| 37 | D613-4 (LEGIARTI000052218738) | S9x/F1+F5 | css L613-7 (LEGIARTI000048683570) | déjà réglé | non |
| 38 | D613-6 (LEGIARTI000052218747) | S9x/F1+F5 | css L613-7 (LEGIARTI000048683570) | déjà réglé | non |
| 39 | D613-6 (LEGIARTI000052218747) | S9x/F1+F5 | css L632-1 (LEGIARTI000037951125) | faux positif | non |
| 40 | L161-22-1-5 (LEGIARTI000052437156) | S12/F4 | css L311-3 (LEGIARTI000051284232) | faux positif | non |
| 41 | L136-1-1 (LEGIARTI000053282440) | S12/F4 | css L412-8 (LEGIARTI000053283575) | faux positif | non |
| 42 | R162-29-1 (LEGIARTI000053285612) | S9x/F1+F5 | css L162-22-8-2 (LEGIARTI000048725736) | déjà réglé | non |
| 43 | R161-69-1 (LEGIARTI000053335400) | S9x/F1+F5 | css L353-1 (LEGIARTI000047453693) | faux positif | non |
| 44 | R173-17-1 (LEGIARTI000053335521) | S9x/F1+F5 | css L353-6 (LEGIARTI000019959401) | faux positif | non |
| 45 | R353-13 (LEGIARTI000053335717) | S9x/F1+F5 | css L353-6 (LEGIARTI000019959401) | faux positif | non |
| 46 | D161-2-4-3 (LEGIARTI000053355879) | S9x/F1+F5 | css L161-21-1 (LEGIARTI000051289750) | déjà réglé | non |
| 47 | D351-1-12 (LEGIARTI000053355953) | S9x/F1+F5 | css L351-1-4 (LEGIARTI000053281659) | déjà réglé | non |
| 48 | D351-1-11 (LEGIARTI000053355959) | S9x/F1+F5 | css L351-1-4 (LEGIARTI000053281659) | déjà réglé | non |
| 49 | D353-1 (LEGIARTI000053356066) | S9x/F1+F5 | css L353-1 (LEGIARTI000047453693) | faux positif | non |
| 50 | R371-6 (LEGIARTI000053429344) | S9x/F1+F5 | css L371-6 (LEGIARTI000053611031) | déjà réglé | non |
| 51 | D131-6-1 (LEGIARTI000053451315) | S9x/F1+F5 | css L131-6-4 (LEGIARTI000053282569) | déjà réglé | non |
| 52 | R165-113 (LEGIARTI000053925024) | S9x/F1+F5 | css L165-1-8 (LEGIARTI000051285341) | déjà réglé | non |
| 53 | R166-4 (LEGIARTI000054130023) | S9x/F1+F5 | css L165-4 (LEGIARTI000053282805) | déjà réglé | non |
| 54 | R166-3 (LEGIARTI000054130026) | S9x/F1+F5 | css L165-4 (LEGIARTI000053282805) | déjà réglé | non |
| 55 | R166-1 (LEGIARTI000054130035) | S9x/F1+F5 | css L165-4 (LEGIARTI000053282805) | déjà réglé | non |
| 56 | R331-5-1 (LEGIARTI000054167652) | S9x/F1+F5 | css L331-8-1 (LEGIARTI000053270151) | déjà réglé | non |
| 57 | R133-14 (LEGIARTI000054167679) | S9x/F1+F5 | css L133-5-3 (LEGIARTI000051287164) | déjà réglé | non |
| 58 | D623-8 (LEGIARTI000054167887) | S9x/F1+F5 | css L622-3 (LEGIARTI000037951132) | déjà réglé | non |
| 59 | L162-1-15 (LEGIARTI000054335791) | S12/F4 | css L431-1 (LEGIARTI000035640835) | faux positif | non |
| 60 | R178-5 (LEGIARTI000054818797) | S9x/F1+F5 | css L223-15 (LEGIARTI000051285375) | déjà réglé | non |
| 61 | R178-5 (LEGIARTI000054818797) | S9x/F1+F5 | css L223-13 (LEGIARTI000051285388) | déjà réglé | non |
| 62 | R382-8-1 (LEGIARTI000054906308) | S15/F5 | — | faux positif | non |
| 63 | R382-8-4 (LEGIARTI000054906314) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 64 | R382-16-5 (LEGIARTI000054906320) | S9x/F1+F5 | css L142-4 (LEGIARTI000048700753) | déjà réglé | non |
| 65 | R382-28 (LEGIARTI000054907068) | S9x/F1+F5 | css L382-3 (LEGIARTI000032078751) | faux positif | non |

Revue IA : rien de ceci ne vaut validation par un juriste.
