# Groupe B05 : décisions (troisième passe, objections P2)

Quinze objections P2 sont traitées : RT-P1-CGI-B-03 à 05 et 07 à 10, RT-P1-CGI-C-04, 08, 11 et 13, RT-P1-TRAVAIL-B-03, 18 et 19, RT-RXCGI-01.

**Méthode**
- Le registre date d'un instantané ancien. Tous les textes ont donc été relus en **production**, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py …`, exports dans `evidence/cited/production-20261029/`).
- Chaque nouveau texte part de la proposition, du motif et des notes de production. Il y applique des remplacements exacts : chaque passage modifié est vérifié comme unique. Tout le reste est repris à l'identique.
- Contrôle : `python3 -B apply/check_changes.py B05` donne 30 lignes construites, 30 validées et aucun problème (`problems` vide). La variante `B04f` donne 1 ligne validée et aucun problème.
- Les diagnostics `references_changed` et `length_change` portent sur des écarts déjà présents entre la source et la proposition. Seul nouveau renvoi : L. 5424-20 du code du travail, ajouté dans CSS L213-1, article présent au corpus.

Revue assistée par IA : rien de ceci ne vaut validation par un juriste.

## Appliquées

### RT-P1-CGI-B-03 : appliquée
- **Article touché :** annexe III 40 A (LEGIARTI000026348033).
- **Ce qui change :** au h, la donnée « recettes nettes soumises à la contribution de 234 nonies » ne vaut plus que pour les recettes perçues avant la suppression de la contribution sur les revenus locatifs (CRL). Les recettes nouvelles n'ont ni rubrique, ni déclaration à néant, ni justification propre à la CRL. La rédaction suit celle du e de 46 C, déjà bornée.
- **Lignes du lot :** une entrée `removed_provisions` et un effet `coordination` sont ajoutés.
- **Laissé à l'auteur :** rien.

### RT-P1-CGI-B-04 : appliquée
- **Articles touchés :** annexe IV 56 AJ (LEGIARTI000054359557) ; CGI 568 (LEGIARTI000054591219), notes seulement.
- **Ce qui change :** un alinéa final est ajouté à 56 AJ. Pour les tabacs mis à la consommation après l'abrogation de 568, aucune donnée, liquidation ni ligne de taux propre au droit de licence n'est transmise. Les mentions du droit de licence ne valent plus que pour les faits antérieurs : 1°, 4°, ligne « Droit de licence » du tableau, transmission unique.
- **Ce qui est conservé :** l'accise, la cotisation au régime d'allocation viagère des gérants de débits de tabac (RAVGDT), le 3° et les remises. Aucune cellule du tableau n'est retirée.
- **Notes corrigées :** dans 56 AJ, la note « aucun droit de licence n'est aboli » était fausse ; elle l'est aussi dans `scope_limitations`. Dans 568, la contradiction présentée comme restant à traiter est maintenant réglée.
- **Laissé à l'auteur :** l'utilité autonome du 3° (déclaration par débitant « mentionnée à l'article 568 ») n'a pas été tranchée. Le 3° est conservé.

### RT-P1-CGI-B-05 : appliquée (correction révisée)
- **Articles touchés :** annexe IV 121 sexies (LEGIARTI000054359512) ; CGI 1519 (LEGIARTI000053546523), notes seulement.
- **Ce qui change :** un alinéa est ajouté. Le relevé nominatif ne sert plus qu'aux répartitions des années de redevance antérieures à sa suppression. Aucun relevé n'est établi pour une année supprimée, même si son échéance précède cette année. Les relevés déjà arrêtés restent utilisables.
- **Motif rectifié :** il affirmait que le relevé restait « expressément exigé par 1519 ».
- **Laissé à l'auteur :** rien.

### RT-P1-CGI-B-07 : partiellement appliquée (le reste est déjà réglé)
- **Articles touchés :** CGI 1639 A quater (LEGIARTI000053546076) et 1640 (LEGIARTI000053546085) ; CSS L131-8 (LEGIARTI000053538201), placé en variante `apply/B04f/` car l'article appartient au groupe B04.
- **Ce qui change dans 1639 A quater et 1640 :** pour la seule taxe sur la vacance (1406 bis), un alinéa ajouté borne aux impositions des années antérieures à l'abrogation de 1406 bis :
  - la faculté de délibérer ;
  - le maintien des délibérations (b du 2 du II, ou b du 1° du II) ;
  - les dispositions issues de l'article 108 de la loi n° 2026-103.
- **Pourquoi cette rédaction :** elle est plus étroite que le texte du registre. Elle ne borne pas l'article 108 pour ses autres objets éventuels, car son contenu n'est pas au corpus.
- **Ce qui change dans L131-8 :** le 6° (affectation du droit de licence) est borné aux mises à la consommation antérieures à l'abrogation de 568. Les encaissements et régularisations ultérieurs restent couverts.
- **Déjà réglé :** 1379 (III), 1379-0 bis (XI), 1586 (I), 1647 (III bis et IX), 1599 bis, CSS L241-2. Pour 1649 quater B quater, le VII reste inchangé mais il est neutralisé par la garde générale : « ne peuvent rétablir une déclaration supprimée… ».

### RT-P1-CGI-B-08 : partiellement appliquée (le reste est déjà réglé)
- **Article touché :** CGI 1763 C (LEGIARTI000053543723).
- **Ce qui change :** la mention de 209-0 A devient « 209-0 A, dans sa rédaction applicable aux exercices ouverts avant son abrogation ». Le quota, l'amende, le plafond et l'abattement sont inchangés.
- **Déjà réglé :** 1788 C (IV et V) et 1729 B (6 a).

### RT-P1-CGI-B-10 : appliquée
- **Articles touchés :** CGI 234 duodecies (LEGIARTI000020013533) ; notes de 234 terdecies (LEGIARTI000022171914) et de l'annexe III 376 (LEGIARTI000006300119).
- **Ce qui change :** l'acompte « limité » maintenu pour l'exercice à cheval est remplacé par la règle de 234 terdecies et de 376. Aucun acompte n'est exigible si son échéance tombe après l'entrée en vigueur, même au titre de recettes antérieures ; la contribution ancienne est acquittée au solde.
- **Effet :** la contradiction entre la loi et son décret disparaît, ainsi que l'écart de traitement entre redevables à l'IS et sociétés de personnes.
- **Ce qui est conservé :** les acomptes déjà échus, les imputations, les restitutions et les dispenses.
- **Notes :** celles qui présentaient cette coordination comme restant à faire sont mises à jour.

### RT-P1-CGI-C-08 : appliquée (seul 1609 nonies C restait à corriger)
- **Article touché :** CGI 1609 nonies C (LEGIARTI000054356088).
- **Ce qui change :** un alinéa est ajouté à la fin du I bis, sur le modèle de 1379 III et de 1379-0 bis XI (texte révisé du réexamen). Il borne les 1 à 2 (composantes de l'imposition forfaitaire sur les entreprises de réseaux, IFER, et taxe de 1519 I) aux produits des années antérieures. Il interdit toute délibération sur le produit d'une année supprimée.
- **Ce qui ne change pas :** les attributions de compensation du V, les 3 et 4 (FNGIR et DCRTP) et la cotisation foncière des entreprises (CFE).
- **Note rectifiée :** elle disait que la suppression de 1519 I restait à écrire.
- **Déjà réglé :** 1379, 1379-0 bis, 1586 et 1609 quinquies C.

### RT-P1-CGI-C-11 : appliquée pour 281 N et 281 E ; 60 A non appliqué
- **Articles touchés :**
  - annexe III 281 N (LEGIARTI000048839986) et 281 E (LEGIARTI000041393548, sans groupe propriétaire) ;
  - CGI 650 (LEGIARTI000006305188) et 654 (LEGIARTI000006305195, sans groupe propriétaire), notes seulement.
- **Ce qui change dans 281 N :**
  - la réserve du 1 de 650, article abrogé, et le dépôt au seul service du domicile sont remplacés par le libre choix du service de 654 proposé (rédaction révisée du réexamen) ;
  - 650 ne reste applicable qu'aux présentations antérieures ;
  - le renvoi à « la déclaration prévue à l'article 790 G » est accordé à 790 G proposé, qui ne crée plus de formalité autonome : la déclaration est déposée « lorsqu'elle est souscrite ».
- **Ce qui change dans 281 E :** le dépôt au service du domicile est remplacé par un renvoi à 654. C'est la coordination que demandent la note de 654 et le réexamen.
- **Ce qui est conservé :** l'exonération de 31 865 € tous les quinze ans, l'exemplaire unique, le support libre et le téléservice.
- **Notes rectifiées :** celle de 281 N sur le délai d'un mois, retiré par 790 G proposé.
- **Non appliqué, laissé à l'auteur :** l'annexe IV 60 A. L'article est maintenu (retained_unchanged) et sa désignation de service est déjà rendue inopposable par 654.

### RT-P1-TRAVAIL-B-19 : partiellement appliquée (le reste est déjà réglé)
- **Articles touchés :** CSS L213-1 (LEGIARTI000048701101) ; code du travail L5427-1 (LEGIARTI000048600544), notes seulement.
- **Ce qui change :** une phrase est insérée au 6° du I, alignée mot pour mot sur L5427-1 proposé. Le recouvrement des contributions forfaitaires de L. 5422-11 ne porte plus que sur les fins de contrat antérieures à leur suppression. Celui des contributions spécifiques du spectacle (2° de L. 5422-9 et L. 5424-20) ne porte plus que sur les périodes d'emploi antérieures.
- **Ce qui est conservé :** les créances et recours anciens, et les autres recouvrements du 6°.
- **Déjà réglé :** R7122-16 (« c) Article L. 1221-10, … »), D5427-13, R1253-43, CSS D133-21, L5427-1, R3132-22, CSS R133-14 et L3134-14.

### RT-RXCGI-01 : appliquée (notes seulement, corps inchangés)
- **Articles touchés :** CGI 1519 D, 1519 E, 1519 F, 1519 G, 1519 H, 1519 HA, 1599 quater A, 1599 quater B, 1599 bis, 1379, 1379-0 bis et 1609 quinquies C.
- **Ce qui change :** les notes périmées sont remplacées.
  - Elles présentaient 1635-0 quinquies comme conservant sa liste ou gelant l'indexation, alors qu'il est abrogé à la même bascule.
  - Elles présentaient comme restant à faire des coordinations déjà faites : 1379 III, 1379-0 bis XI, 1586 I, 1609 quinquies C IV, et désormais la fin du I bis de 1609 nonies C.
- **Ce qui reste à faire :** plus aucune coordination ouverte dans cette chaîne d'affectation.

## Déjà réglées en production

- **RT-P1-CGI-C-04 :** 1673 bis est abrogé pour les exercices nouveaux. Annexe II 379 4 : « Aucune déclaration ni aucun versement de retenue à la source n'est exigé … au titre des exercices ouverts à compter de cette entrée en vigueur ». 380 IV et 381 sont bornés aux retenues des exercices ouverts avant l'abrogation de 115 quinquies. La correction AUDIT3-Q281 est déjà appliquée.
- **RT-P1-TRAVAIL-B-03 :** déjà corrigé par l'issue GitHub #13.
  - L8241-1 1° : « … lorsque celle-ci est exercée dans les conditions prévues à l'article L. 7123-11 ».
  - L7123-26, R7123-11, R7123-12 et R7123-14 sont abrogés.
  - Les notes de L7123-26, R7123-10-1, R7123-11, R7123-12 et R7123-14 indiquent « Coordinations faites ».

## Non appliquées

- **RT-P1-CGI-B-09 (à confirmer) : arbitrage.** Le fait générateur des plus-values en report n'est pas vérifié sur une source primaire, et aucune des deux options n'est sûre quel que soit ce point :
  - l'option A maintiendrait un impôt si la contribution exceptionnelle sur les hauts revenus (CEHR) naît à l'expiration du report ;
  - l'option B étendrait la suppression à des dettes d'années encore imposables, ce qui est une extension de faveur non décidée.

  Le choix revient à l'auteur.
- **RT-P1-CGI-C-13 (à confirmer) : pièce manquante.** La correction demandée est un chiffrage, par catégorie de collectivités, du ratio d'autonomie financière (art. 72-2 de la Constitution). Aucune donnée n'est au corpus et aucun article n'est à modifier. Les suppressions sont conservées et aucune ressource de remplacement n'est créée.
- **RT-P1-TRAVAIL-B-18 (à confirmer) : arbitrage.** La correction retirerait l'indemnité de fin de mission des détachés sous CDD étranger qui ont une garantie équivalente. Elle réduirait une faveur conservée par le projet, et elle n'est pas sûre si la mesure est justifiée (directive 96/71/CE et art. 56 TFUE non consultés).

## Résumé

| Résultat | Objections |
|---|---|
| Appliquées (5) | B-03, B-04, B-05, B-10, RXCGI-01 |
| Appliquées sur la partie qui restait, le reste déjà réglé (5) | B-07, B-08, C-08, C-11 (sauf 60 A), TRAVAIL-B-19 |
| Déjà réglées entièrement (2) | C-04, TRAVAIL-B-03 |
| Non appliquées (3) | B-09, C-13, TRAVAIL-B-18 |

- **Lignes :** 30 dans `apply/B05/changes.json`, dont 11 corrections de corps et 19 corrections de notes seules, et 1 dans `apply/B04f/changes.json` (CSS L131-8).
- **Aucune** taxe, formalité ni condition nouvelle. **Aucune** faveur, aucune exonération et aucune transition n'est retirée. **Aucune** fermeture de faille (`loophole_closure`).

Revue IA : rien de ceci ne vaut validation par un juriste.
