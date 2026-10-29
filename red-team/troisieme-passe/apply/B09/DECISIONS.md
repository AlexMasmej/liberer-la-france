# Groupe B09 : décisions (objections P2, troisième passe)

Lecture faite sur la production, en lecture seule (`CITE_PRODUCTION=1 python3 -I tools/cite.py …`, exports sous `evidence/cited/production-20261029/`), et non sur l'instantané du registre. Validation : `python3 -B apply/check_changes.py B09` et `python3 -B apply/check_changes.py W06c` donnent `problems: []` (8 lignes B09 et 1 ligne W06c construites et validées). Diagnostics restants, tous voulus : renvoi L272-2 retiré (L612-2), renvoi L512-2 préexistant (D545-8), écarts de longueur préexistants (178, L520-4), réductions normatives déjà déclarées.

## Appliquées

### RT-P1-CSS-B-01 : appliquée (correction révisée)
- Article : CSS L162-22-11-1 (LEGIARTI000048702188). Il passe de `retained_unchanged` à `rewrite_draft`, classé `coordination_only`, avec une mesure `forfait-journalier-hospitalier-suppression`.
- Ce qui change : le b) ne fait tenir compte du forfait journalier dans la facturation AME et soins urgents que « pour les seules journées antérieures à l'entrée en vigueur de la loi supprimant ce forfait ». Pour les journées postérieures, il ne permet ni de le facturer ni de le rétablir. Fractions de 80 % et 20 %, coefficient et a) inchangés.
- Déjà fait en production, conservé tel quel : D174-1, D325-1, D325-6, R381-80, R381-83, R821-8, R871-2, L871-1, L911-7.
- Point laissé à l'auteur : l'arrêté de calcul AME est hors corpus.

### RT-P1-CSS-B-05 : appliquée
- Article : CSS R652-31 (LEGIARTI000038770185).
- Ce qui change : l'alinéa de déduction des droits reversés tardivement visait les seules années « commençant à compter de l'entrée en vigueur de la réforme », que L652-6 proposé supprime. Il n'avait donc aucun champ. Il s'applique désormais à toute contribution équivalente non définitivement liquidée à cette date, y compris pour les années antérieures, avec régularisation dans les délais de réclamation et sans double déduction. Les contributions définitivement liquidées ne sont pas rouvertes.
- Effet : rend effective une faveur déjà décidée (moins de prélèvement). `removed_provisions`, motif, notes et `scope_limitations` ont été mis à jour, et la note périmée « peut laisser ce champ vide » retirée.
- Points laissés à l'auteur : la portée de « la réforme » (décret autonome ou loi de suppression) reste celle du texte existant. Le gain n'est pas chiffré.

### RT-P1-CSS-B-07 : appliquée (correction révisée, volet L272-2)
- Article : CSS L612-2 (LEGIARTI000036391005).
- Ce qui change : « L. 272-2, » est retiré de la liste du quatrième alinéa, puisque L272-2 est abrogé par le projet. L272-1, L281-1 et L281-3 restent applicables au CPSTI. La transition de L272-2 proposé régit les faits antérieurs. Une mesure de coordination `sanctions-caisses-fin-maxima-automatiques` est ajoutée.
- Déjà réglé : le volet L931-26 (L922-8) ; L641-1 et L766-11 neutralisent déjà le renvoi.
- Point d'attention pour le coordinateur : le champ `reference_coherence` de la ligne porte l'empreinte de l'ancienne proposition.

### RT-P1-CSS-B-09 : appliquée (correction révisée)
- Article : CSS D545-8 (LEGIARTI000045283844).
- Ce qui change : le 6° (allocation en cas de décès pendant la grossesse) exigeait un « document constatant la passation du premier examen prénatal mentionné au deuxième alinéa de l'article D. 532-1 », alors que ce deuxième alinéa n'en parle plus. Il vise désormais le document médical attestant la grossesse ou tout autre document médical l'établissant. Le document du premier examen en tient lieu, sans que l'examen puisse être exigé. Le 6° s'applique aux demandes en cours, sans nouveau dépôt.
- Conservés : le délai de quinze jours, la condition de D545-2 et les autres rubriques. La note périmée sur D532-1 (volet B-11) est corrigée dans les notes et dans `scope_limitations`.
- Déjà fait : D532-1 et D532-2.

### RT-P1-CSS-B-11 : partiellement appliquée (notes seules, objet même de l'objection)
- R163-2 (LEGIARTI000053212995), B09 : la note qui disait que R163-7 II 1°, R163-18 1° et R163-19 2° restaient à coordonner est remplacée. Les trois propositions sont coordonnées en production (vérifié). Les notes et `scope_limitations` sont mis à jour ; corps et motif inchangés.
- R163-7 (LEGIARTI000049737659) appartient à W06. La variante `apply/W06c/changes.json`, validée, remplace la note « R163-2 II conserve « du suffixe prévu à l'article L. 162-17-1 » ». Corps et motif inchangés.
- D545-8 : traité avec B-09.
- Déjà réglé : les notes de R543-6, R133-9 et R163-2 sur L162-17-1.
- Non traité ici : le volet L138-20 / L245-5-1. L'objection le renvoie à RT-P1-CSS-A-03, et l'article appartient au groupe B04.

### RT-CIBS-04 : appliquée (notes seules, objet même de l'objection)
- a3 178 (LEGIARTI000006298930) : la phrase « l'absence de CGI 435/438 dans le corpus » est remplacée, dans les notes et dans `scope_limitations`, par la mention de leurs versions abrogées au 1er janvier 2022, présentes au corpus (LEGIARTI000006309896, LEGIARTI000043662369). Corps et motif inchangés.
- Déjà réglé : a3 171, dont les notes et `scope_limitations` ont été corrigés par la correction RT-CIBS-01. CGI 435 et 438 sont des versions abrogées sans brouillon : aucune action.

### RT-P1-NEW-03 : appliquée
- Article : urba L520-4 (LEGIARTI000031816516).
- Ce qui change : seule la première phrase, « Le présent article est abrogé pour les faits générateurs intervenant à compter de… », est remplacée par « La suppression de la taxe […] à compter de la date d'entrée en vigueur de la loi qui la prévoit, est régie par les dispositions suivantes. » Les I, II, III et IV sont inchangés.
- Effet : l'article devient la disposition transitoire en vigueur sur laquelle reposent L520-11 (dispense du IV) et les 21 articles et textes réglementaires qui renvoient à son III.
- Ligne de lot : `change_type` passe de `full_repeal` à `normative_reduction` (`reform_policy_id`, `removed_provisions`), et `repeal_policy_id` et `repeal_scope` sont mis à null. Aucune hausse de taxe ni formalité nouvelle.

### RT-INUT-06 : partiellement appliquée (objection à confirmer)
- a3 111-0 E (LEGIARTI000006298854) : le motif précise que la justification du fournisseur (I 3°) résulte de ses documents commerciaux, sans attestation du client. Cette précision est sûre quel que soit le point à confirmer, et elle n'ajoute aucune formalité. La note sur le 15° de 289, désormais abrogé, est mise à jour. Corps inchangé.
- Non appliqué (pièce manquante) : la vérification de l'article 27 de la directive 92/83/CEE et de la directive 2020/262. L'exclusion temporaire après fraude relève d'un arbitrage législatif hors corpus.

## Déjà réglées (production)
- **RT-P1-CSS-B-04** : R652-26 version 2029 (LEGIARTI000052846149), déjà rédigée (lot third-pass-corrections/00009) : « Le présent article est abrogé, dans sa rédaction issue de l'ordonnance n° 2025-1091 du 19 novembre 2025 comme dans toute rédaction antérieure, à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi supprimant les droits de plaidoirie… ». Les textes courants sont coordonnés.
- **RT-CIBS-02** : 171 proposé ne dit plus « le droit auquel renvoyait le 2° » ; il vise « les droits régis par les articles 435 et 438 […] dans leur rédaction antérieure au 1er janvier 2022 dont l'exigibilité est intervenue avant cette date ».
- **RT-CIBS-03** : la phrase sur les « définitions directement applicables du droit de l'Union européenne » a disparu de 171 proposé.
- **RT-INUT-03** : 289 15° est déjà abrogé pour l'avenir (correction SWEEP-Y15-A2-289).
- **RT-INUT-07** : les transitions figurent déjà dans 50-0 H, 50-0 G, 111-0 F et 289 15° : numéros existants sans effet, déclarations pendantes sans objet, refus et retraits sans effet, opérations antérieures, loi répressive plus douce, L. 102 B. La différence « loi qui les prévoit » / « réforme » vise la même loi : elle n'est pas corrigée, pour éviter une réécriture de style. Reste hors corpus l'abrogation des modèles de l'arrêté du 4 juillet 2005.

## Non appliquées
- **RT-CIBS-05** : pièce manquante (CIBS au 18 octobre 2026, ordonnances n° 2026-671 et n° 2021-1843, directive). C'est une réserve documentaire.
- **RT-P1-NEW-04** : hors corpus et à confirmer. Le texte de CASF L344-2-6 n'a pas été lu et la correction proposée est conditionnelle. L2141-7-1 proposé réserve déjà les obligations d'information d'un fondement distinct.

## Résumé
- 8 objections appliquées en tout ou en partie : CSS-B-01, 05, 07, 09, 11 (notes), CIBS-04 (notes), NEW-03, INUT-06 (motif).
- 5 objections déjà réglées : CSS-B-04, CIBS-02, CIBS-03, INUT-03, INUT-07.
- 2 objections non appliquées : CIBS-05, NEW-04.
- 9 lignes en tout (8 B09 + 1 variante W06c), toutes validées. Aucune `request`. Aucune fermeture de faille (`loophole_closure`). Aucune disposition non codifiée.

Revue IA : rien de ceci ne vaut validation par un juriste.
