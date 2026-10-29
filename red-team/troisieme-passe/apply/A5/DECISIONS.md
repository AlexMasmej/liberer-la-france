# Groupe A5 : décisions (troisième passe)

Instantané lu : `snapshots/20261029T034912Z`, avec `tools/cite.py` et la base en lecture seule. Rien n'a été écrit en production.

Contrôle : `python3 -B apply/check_changes.py A5` donne 79 changements construits et validés, `problems` vide. Le fichier comporte aussi 10 `requests` et 12 `skipped`. Il n'y a aucun `uncodified` : les dispositions non codifiées suggérées par les objections (L651-3, R711-9) sont remplacées par des propositions sur les versions futures. Aucune ligne ne porte `loophole_closure`.

Revue faite par une IA : elle ne vaut pas validation par un juriste.

## Notes de méthode pour le coordinateur

- **Retrait d'une réécriture.** Quand une proposition était purement rédactionnelle, le retrait passe par la ligne existante (`mode: replace`) avec :
  - `overrides.status = "retained_unchanged"` et `overrides.proposed_xml = null` ;
  - `classification` et `substantive_impact` en `retained_necessary`, `effects` vide.

  Le validateur du projet accepte ce schéma. Le `proposed_xml` placeholder de `changes.json` est écrasé par l'override. Articles concernés : L313-4, L1521-2-2, L1522-3, L1524-9, L2122-6-1 ; R711-8 et annexe II 279/280 (notes seulement, l'article était déjà maintenu).
- **Lignes `new`.** Elles portent un `substantive_impact` (citations exactes vérifiées par le validateur) mais pas de certificat : le coordinateur le calcule.
- **Certificats obsolètes.** Les champs `reference_checks` et `reference_coherence` des lignes existantes ne sont pas recalculés et peuvent viser l'ancienne empreinte.
- **Articles non attribués.** Plusieurs articles ne sont pas dans `assignment.json` mais relèvent de RT-FUTTL-02 : les instances fusionnées RT-FUTFISC-24 et RT-FUTFISC-25, ainsi que D353-145, R4451-61 et D1142-2-1 de la liste du coordinateur. A5 les a traités. Aucun article attribué à un autre groupe n'est modifié.

## RT-FUTTL-02 (absorbe RT-RXF01-01) : appliquée

Dans chaque proposition visée, la clause qui prenait l'état ABROGE_DIFF pour une abrogation est supprimée. Les motifs, les notes, les `substantive_impact` (et les `benefit_review` concernés) sont corrigés, y compris les notes qui disaient le successeur absent. La réforme est ensuite reportée sur la version suivante par une proposition `new`, sauf quand il n'y avait rien à reporter.

**Version en vigueur corrigée et version suivante créée :**
- L651-3 (2029) : plus de résiliation ni d'expulsion obligatoires, le délit étant maintenu. Cela remplace la disposition non codifiée envisagée.
- L452-5 (2027) : plus de déclaration ni d'autoliquidation CGLLS, plus de majoration de 0,2 %. Le recouvrement suit les « taxes sur les biens et services ».
- L302-16-2 (2027) : la coordination avec la suppression de la taxe sur les salaires est reportée.
- L112-16 (2027) : plus d'avis préalable de la commission consultative de l'environnement (CCE) dans le champ de l'ACNUSA ; les consultations deviennent simultanées.
- L861-2 (2028) : abrogation prospective liée à la suppression de la contribution de L813-4.
- L861-5 (2028) : le 1° est raccordé à CSS L755-35.
- D2135-7 (15 janvier 2027) : seule la réserve sur le rapport du commissaire aux comptes est reportée. La gratuité n'est pas comptée, le décret n° 2026-806 l'ayant déjà réalisée (correction reformulée de RT-FUTTL-13).
- D1142-4, D1142-5, D1142-6, D1142-6-2, D1142-8, D1142-2-1 et les annexes I et II de l'index (2029) : leurs versions suivantes ont un texte identique ; la proposition corrigée y est reprise mot pour mot.
- L5524-6 (2028) : la correction L131-1 → L131-2 est reportée (voir RT-FUTTL-09).
- D353-145 (2027) : le renvoi à L812-2 est conservé avec motivation, selon l'option de RT-FUTTL-14.

**Version en vigueur corrigée seulement :**
- L302-16-1 : rien à reporter, la version de 2027 renvoie elle-même au CIBS.
- D2135-8 : la version de 2027 est plus favorable (RT-FUTTL-13).
- L5524-2 : la version de 2028 ne reprend pas l'adaptation coordonnée.
- L3422-5 : la clause « abrogé à compter du 1er janvier 2028 » est supprimée, mais rien n'est créé pour 2028, son a) étant tronqué (pièce manquante, `skipped`).
- R4451-61 : point 8 appliqué, la clause est remplacée par « s'applique jusqu'à l'entrée en vigueur de la rédaction issue du décret n° 2023-489 ». Rien n'est créé pour 2027 (RT-FUTTL-14).

**Retiré au profit de la version officielle :** L313-4, dont la réécriture était stylistique et se bornait elle-même au 31 décembre 2026.

**Volet fiscal :**
- Version en vigueur corrigée et version suivante créée :
  - 1840 P (2029) : plus d'emprisonnement en récidive.
  - 406 A 15 (annexe III, 2029) : plus de préalable administratif à la mainlevée.
  - 87 A (au plus tard 2030) : coordination du contrat unique.
  - 276 (annexe II, 1er août 2027) : plus de caution ni de sûreté de remplacement ; les cautionnements anciens sont limités aux dettes antérieures.
  - 1786 et 1788 D (2027) : abrogation équivalente.
  - 1788 E (2027) : 1° abrogé, plus de double information des clients, plus de délai de six mois.
- 279 et 280 (annexe II) : seules les notes sont corrigées.
- Non appliqué :
  - 1693 ter : faux positif, le successeur est une version mort-née.
  - 286 F : rien à créer.

**Fusion avec A8 (RT-P1-ANNEXES-01, facturation électronique, absorbe RT-FUTFISC-09)**, à la demande du coordinateur. 1788 D et 1788 E, versions en vigueur (LEGIARTI000053546693 et 053546696) et versions de 2027 (LEGIARTI000054567750 et 054567685), n'ont plus qu'un seul texte chacun, de champ `objection` « RT-FUTTL-02 / RT-P1-ANNEXES-01 » :
- **Textes et `overrides` :** ceux d'A8, fusionnés avec les `overrides` d'A5 (`policy_review_id`, `benefit_review`). Ils ne contiennent plus la clause ABROGE_DIFF erronée.
  - Pour les versions en vigueur, la clause est remplacée par une phrase qui vise expressément la rédaction de 2027.
  - Pour 1788 D en 2027, l'abrogation expresse vise les amendes de L. 216-47 et L. 216-48 du CIBS, avec application des montants plus doux.
  - Pour 1788 E en 2027, le 2° ne mentionne plus le renouvellement, supprimé par 290 B proposé.
- **Notes :** celles d'A8, complétées par la correction RT-FUTTL-02 et la mention que les successeurs retenus par le contrôle du coordinateur sont des versions mort-nées.

Le texte antérieur d'A5 est conservé hors livrable (sauvegarde dans le scratchpad).

**Transmis par `requests` aux groupes propriétaires :**
- A1 : 1754, 1750, 1751, 299 septies, 1613 ter et 1382-0 (fin du V). Le coordinateur les a transmises à A1.
- A2 : 287 et 1788 A (deux successeurs).
- A3 : 1789.
- A4 : CSS L531-8.

D'après le coordinateur, les demandes vers A2, A3 et A4 sont déjà satisfaites dans leurs textes.

**Laissé à l'auteur :**
- Le renvoi L812-2 ou L812-3 de D353-145 en 2027.
- La coordination CIBS des transmissions de L. 216-47 et L. 216-48 (1788 D et E).
- Un éventuel allègement du régime d'agrément des tabacs de 276 en 2027, qui supposerait de lire le code de la santé publique.
- Le niveau réglementaire des annexes II et III.

## RT-FUTTL-04 : partiellement appliquée (objection « à confirmer »)

Articles : L7233-2, versions de 2025 (notes) et de 2027 (`new`).

Ce qui est appliqué ne dépend pas du point à confirmer : la dispense de déclaration pour le crédit d'impôt de 199 sexdecies est reportée sur la version de 2027 (1° abrogé, renvoi CIBS conservé), et les notes sont rendues exactes.

Non appliqué (hors corpus) : supprimer la déclaration et l'exclusivité pour la TVA suppose de modifier les articles L. 213-187 et L. 213-188 du CIBS. Cette coordination extérieure est indispensable ; sans elle, l'allègement de TVA ne peut être compté à partir du 1er janvier 2027.

## RT-FUTTL-05 : appliquée

Articles : CCH R144-19 et R144-20 (`new`), notes de R4216-33 et R4216-34.

La réforme est reportée sur le nouveau support du code de la construction et de l'habitation : l'enquête de l'inspection devient facultative et le rejet implicite naît après deux mois, avec la transition. Les propositions R4216-33 et R4216-34 restent bornées à la période antérieure au 1er janvier 2027.

R144-16 (registre de sécurité) n'est pas modifié, l'objection n'en demandant pas la suppression.

## RT-FUTTL-06 : appliquée, avec un choix laissé à l'auteur

Articles : L3332-17-1, version de 2025 (notes) et version de 2027 (`new`).

La qualité ESUS de plein droit et la suppression de l'agrément sont reportées sur la version de 2027. Le II rédigé « pour l'obtention de l'agrément » est remplacé.

Les seize catégories de plein droit, faveur que la proposition conservait, sont maintenues. La présomption de la loi n° 2026-403 pour les catégories fixées par décret y est ajoutée, sans agrément.

Laissé à l'auteur : le maintien de la liste contre le retrait voulu par la loi de 2026. Ce choix est motivé par la conservation des faveurs et l'effet est déclaré `relief_extended`. L'auteur peut l'abandonner au profit de la seule présomption.

## RT-FUTTL-07 : appliquée, sauf R1142-23

Articles : L1142-11 (2026, avec le palier de 40 % au 1er mars 2029 ; version de 2029 créée, quota de 40 %), L1142-12, D1142-18 et D1142-19 (2029, `new`).

La publication propre à l'entreprise est remplacée, aussi pour les objectifs de progression, par la transmission existante au ministère, qui rend les informations publiques. Les quotas, le délai, la pénalité et l'information du CSE sont maintenus.

Non appliqué (arbitrage) : l'alignement du forfait de deux PMSS de R1142-23 sur D1142-14.

## RT-FUTTL-08 : appliquée

Articles : R711-9 (2020 : le V vise « le II dans sa rédaction antérieure à la présente réforme » ; version de 2027 créée), R711-8 (2016 : notes ; version de 2027 créée).

Les II et III étendus par le décret n° 2025-831 sont abrogés sur la version de 2027. L'obligation de vérification des syndics devient une faculté de signalement.

Laissé à l'auteur : maintenir cette vérification s'il juge la fiabilité du registre essentielle.

## RT-FUTTL-09 : appliquée

**Retirés au profit des versions officielles successives (2027 à 2036) :** L1521-2-2, L1522-3, L1524-9 et L2122-6-1. Leurs réécritures étaient purement rédactionnelles (`editorial_only`).

**Reportés sur 2028 :**
- L5524-6 : les articles L. 131-2, L. 241-2, L. 242-13 et L. 711-2 du CSS s'entendent dans leurs versions applicables à Mayotte.
- L861-5 : le 1° est raccordé à CSS L755-35.

**Version en vigueur seulement :** L5524-2, la version de 2028 étant exacte.

**Partiellement traité :** L3422-5 (voir RT-FUTTL-02). Le renvoi tronqué de la version de 2028 n'est pas complété (pièce manquante : ordonnance n° 2026-647, article 18, 7°).

## RT-FUTTL-10 : appliquée

Articles : L6353-12 (`new`) et notes de L6353-11.

Le champ de L6353-12 est défini sans renvoi à L6353-11, que le projet abroge. Un lien vers la publication de l'État suffit désormais. L'information des apprenants avant toute inscription et tout paiement est conservée. L6113-8-1 n'est pas modifié.

Laissé à l'auteur : abroger L6353-12, option plus conforme à l'orientation mais qui retire une information anti-fraude.

## Réserves générales

- Aucun texte modificatif n'a été lu au JORF : ordonnances n° 2025-1247, 2025-1091 et 2026-647 ; décrets n° 2025-1100, 2025-831, 2026-806, 2026-84 et 2023-489 ; lois n° 2026-403 et 2026-534. Leur contenu est déduit de la consolidation LEGI et des NOTA.
- Le CIBS, le code de la santé publique et les ordonnances mahoraises sont hors corpus.
