# Groupe B10 : décisions sur les objections P2

J'ai lu les textes en production (lecture seule, base `corpus.sqlite` en `mode=ro`) le 29 octobre 2026, et non l'instantané du registre. Les exports `cite.py` (CITE_PRODUCTION=1) sont dans `evidence/cited/production-20261029/`. Validation : `python3 -B apply/check_changes.py B10` donne 14 lignes construites et validées, `problems` vide. Aucun article d'un autre groupe n'est modifié et aucune variante n'a été nécessaire.

## Appliquées

### RT-TUT-06 : appliquée
- **Article touché :** CSS L224-10 (LEGIARTI000044404083).
- **Ce qui change :** le troisième alinéa (« Si la convention n'est pas signée […] le premier alinéa reste applicable ») est fondu dans le deuxième (« il en va de même lorsque la convention n'est pas signée… »). Il laissait croire à un régime de repli, alors que le premier alinéa prévoit déjà l'exécution dès l'adoption. Le fond ne change pas.
- **Pour l'auteur :** aucun point.

### RT-TUT-03 : appliquée (notes et motif seulement, objet même de l'objection)
- **Articles touchés :** CSS L151-1 (LEGIARTI000037064171), L224-10, R225-5 (LEGIARTI000006748702) et R226-4 (LEGIARTI000006748712).
- **Ce qui change :** les notes affirmaient que L226-4 était absent du corpus, ou que son renvoi était « non vérifiable ». Elles disent maintenant que L226-4 (LEGIARTI000006741828/829, transféré au 1er janvier 1995) a le même texte que L224-10 dans sa version de 1994 (LEGIARTI000006742291). Le renvoi s'entend donc de L224-10 dans sa rédaction antérieure.
- **Correction au passage :** les notes de L224-10 et de R226-4 sur D227-6 (« abrogation à la date du décret… à synchroniser ») ne valaient plus depuis RT-TUT-01. Elles sont mises à jour.
- **Corps :** aucun corps n'est modifié.
- **Pour l'auteur :** l'acte de transfert au JORF n'a pas été consulté (réserve documentaire).

### RT-TUT-08 : partiellement appliquée
- **Articles touchés :** CSS D635-5 (LEGIARTI000041967053) et R151-2 (LEGIARTI000021508238).
- **D635-5 :** le déclencheur non défini « l'entrée en vigueur de la réforme » est remplacé par celui de R226-4, « la loi supprimant le régime général d'opposition prévu à l'article L. 224-10 ».
- **R151-2 :** « l'entrée en vigueur du présent texte » devient « l'entrée en vigueur de la loi », comme dans R152-1, R152-2 et L151-1.
- **Non appliqué :** le passage, dans D635-5, du critère de la « demande d'approbation présentée » à celui de la « délibération adoptée ». Ce critère est plus restrictif pour les délibérations adoptées avant la loi mais présentées après, et les notes de D635-5 assument l'ancien critère.
- **Pour l'auteur :** l'article transitoire unique du décret d'application, s'il le souhaite.

### RT-DOMSUCC-06 : partiellement appliquée
- **Article touché :** CGI 750 ter (LEGIARTI000024453202), III.
- **Ce qui change :** après « applicables à la date du décès », j'ai inséré une réserve. Les demandes de crédit de paiement fractionné ou différé restent régies par leurs règles temporelles propres, y compris quand elles sont formées après l'entrée en vigueur. La contradiction avec 1722 bis et avec l'annexe III 397 proposés disparaît.
- **Non appliqué à un article :** la désignation unique de la loi et de la date d'effet. Elle relève d'une disposition non codifiée, rédigée sous `uncodified` avec la date laissée à l'auteur.
- **Pour l'auteur :**
  - le volet de l'absence et de la déclaration judiciaire de décès (code civil, hors corpus, à confirmer), qui n'est pas rédigé ;
  - les formules générales du même type dans 796-0, 851 et l'annexe III 281 O, articles non attribués et signalés « à vérifier », qui ne sont pas modifiées.

### RT-P1-CGI-A-05 : appliquée
- **Article touché :** CGI 170 (LEGIARTI000053543803), 1.
- **Ce qui change :** la mention des éléments du plafonnement global de 200-0 A ne vaut plus que pour les revenus des années antérieures à sa suppression. Le prélèvement de 204 A est maintenu.
- **Mises à jour liées :** `benefit_review` et `substantive_impact` (un effet de coordination ajouté).
- **Pour l'auteur :** aucun point.

### RT-P1-CGI-A-07 : appliquée
- **Articles touchés :** annexe IV 50 bis (LEGIARTI000006300402), 49 (LEGIARTI000043592523) et 50 (LEGIARTI000006300401) ; CGI 276 (LEGIARTI000006304328), notes seulement.
- **50 bis :** il ne renvoie plus aux conditions de 276 que pour les cautionnements des produits reçus avant l'abrogation.
- **49 et 50 :** maintenus jusqu'ici à l'identique, ils passent en `rewrite_draft`. Leur texte source est repris mot pour mot, avec une phrase qui les limite aux produits reçus avant l'abrogation de 276 et interdit toute caution pour les réceptions postérieures.
- **Ce qui est conservé :** les franchises de 275 et 277 A, les cautions existantes et les garanties douanières de l'Union.
- **Pour l'auteur :** la recodification de la TVA prévue au 1er janvier 2027 (276 est en ABROGE_DIFF) est à coordonner hors corpus.

### RT-P1-CGI-A-08 : appliquée
- **Article touché :** annexe II 36 (LEGIARTI000006293719).
- **Ce qui change :** l'article est abrogé intégralement (`full_repeal`), en coordination avec l'abrogation de 54 quater. Aucun relevé, renseignement ni report ne peut plus être exigé, même pour une échéance expirée. Les relevés déposés ne sont pas à refaire, et la loi répressive plus douce s'applique aux sanctions non définitives.
- **Motif et notes :** réécrits, car ils affirmaient que le relevé restait prescrit par la loi.
- **Pour l'auteur :** l'annexe IV 4 J dit encore que le relevé de 238 A « n'est pas supprimé par le présent article ». C'est exact pour 4 J, et je ne l'ai pas modifié.

### RT-RXFA03-02 : appliquée
- **Article touché :** CCH R863-4 (LEGIARTI000047985799).
- **Ce qui change :** la citation de R. 822-24 au 9° est fermée (« … renouvellement urbain. ” ; »). La clause de cessation des mois nouveaux devient le 10° du présent article, et « ce 8° » devient « au 8° ». Le fond ne change pas.
- **Mises à jour liées :** `substantive_impact` (citation proposée) et notes.
- **Pour l'auteur :** aucun point.

## Déjà réglées

### RT-TUT-02
La correction renvoyait à RT-TUT-01, appliquée depuis à D227-6 (groupe B07) : « Les délibérations adoptées avant cette date qui n'ont été ni approuvées ni refusées à cette date deviennent exécutoires à cette même date… ».

### RT-P1-TRAVAIL-A-13
La version de 2029 de R3324-22 (LEGIARTI000052845711) a déjà sa proposition (lot `third-pass-corrections/00013.json`) : « 10° […] tel que défini à l’article L. 3142-16 » ainsi que la clause de non-résidence.

## Non appliquées

### RT-TUT-05 (« à confirmer »)
Les deux options laissent un arbitrage ouvert : la correction minimale prolonge des suspensions, l'autre option rend caduques les infirmations nationales non définitives. Aucune n'est sûre quel que soit le point à confirmer. L'objection touche aussi R226-1 (W04), R226-2 (W01) et R752-24 (non attribué).

### RT-TUT-07 (« à confirmer »)
La correction minimale est une énumération de lisibilité sans effet normatif, donc une réécriture de style. L'option B rétablirait une opposition ministérielle supprimée par le projet : arbitrage contraire à l'orientation.

### RT-DOMSUCC-03
Aucune correction textuelle n'est demandée. Les motifs et le chiffrage sont hors corpus, et l'objection interdit toute déclaration de remplacement.

### RT-DOMSUCC-04
La correction ajoute une charge de la preuve sur le cédant, c'est-à-dire une condition nouvelle. L'objection juge elle-même défendable le statu quo. L'uniformisation des termes serait rédactionnelle.

### RT-DOMSUCC-05 (« à confirmer »)
- Le chiffrage et les motifs sont hors corpus, de même que la CRDS (ordonnance 96-50).
- L'inclusion du PEA est un arbitrage que l'objection laisse ouvert.
- L'option de repli supprimerait une exonération.

## Résumé

- **Appliquées (8) :**
  - entièrement (6) : RT-TUT-03, RT-TUT-06, RT-P1-CGI-A-05, RT-P1-CGI-A-07, RT-P1-CGI-A-08, RT-RXFA03-02 ;
  - partiellement (2) : RT-TUT-08 et RT-DOMSUCC-06.
- **Déjà réglées (2) :** RT-TUT-02 et RT-P1-TRAVAIL-A-13.
- **Non appliquées (5) :** RT-TUT-05, RT-TUT-07, RT-DOMSUCC-03, RT-DOMSUCC-04, RT-DOMSUCC-05.
- **Volume :** 14 articles modifiés, dont 4 par les notes ou le motif seulement (L151-1, R225-5, R226-4, CGI 276), et 1 disposition non codifiée proposée.

Ceci est une revue IA. Elle ne vaut pas validation par un juriste.
