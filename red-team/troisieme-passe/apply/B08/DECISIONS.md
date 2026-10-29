# Groupe B08 : décisions sur les objections P2

Tous les textes ont été lus en production, en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et SQLite `mode=ro`). Le registre date d'un instantané plus ancien.

Contrôle : `python3 -B apply/check_changes.py B08` donne 8 lignes construites et validées, `problems` vide. La variante `B03h` (articles du groupe B03) donne 2 lignes validées, `problems` vide.

Diagnostics vérifiés et voulus :
- L200-9-1 : le renvoi à L202-9-1, abrogé, est retiré.
- L421-7 : le renvoi à L421-6 figurait déjà dans le brouillon.
- 508 et 374 : la longueur change.

## Objections appliquées

### RT-P1-CCH-06 : appliquée (annexe à R422-1, LEGIARTI000039049603)

- **Ce qui change.** Les 17°, 20°, 22° et 23° de la clause 3 perdaient leur base. Ils exigeaient l'accord du maire, et pour le 17° celui du préfet selon R442-23. Le 23° exigeait aussi une vacance « depuis plus d'un an ». Or L422-2 proposé supprime ces accords et cette durée, et R442-23 est abrogé. Ces rubriques sont donc réécrites sur le modèle de l'annexe à R422-6.
- **Vacance.** Au 23°, la condition est remplacée par « sans durée minimale de vacance ». Les conditions de L442-11 s'appliquent aussi aux logements vacants depuis un an ou moins, comme le prévoit L422-2.
- **Transition finale.** Elle couvre désormais ces dispenses : les demandes pendantes deviennent sans objet et les mandats en cours sont préservés, sans nouveau dépôt.
- **Ligne de lot.** Trois `removed_provisions` et un effet de `coordination` sont ajoutés.
- **Laissé à l'auteur :**
  - le 22° ne reçoit pas l'extension aux opérations de requalification de copropriétés dégradées (ORCOD) que prévoit L422-2 ;
  - la note de R442-23 (« Coordination hors lot à effectuer ») est désormais périmée. Elle n'est pas modifiée, car elle n'est pas l'objet de l'objection.

### RT-P1-CCH-07 : appliquée (annexe V à D353-127, LEGIARTI000039049069)

- **Statut.** L'objection est « à confirmer », mais la correction est neutre et favorable au locataire.
- **Ce qui change.** Une phrase est ajoutée à la transition finale. Dans les conventions conclues avant la réforme, la référence à l'autorisation de R631-4, abrogé, s'entend de l'autorisation de changement d'usage lorsqu'elle est légalement requise, sous réserve des dispenses et dérogations. La tolérance d'usage professionnel partiel est ainsi préservée dans les conventions en cours.
- **Laissé à l'auteur.** La note de R631-4 (« Cette annexe n'est pas modifiée ici ») est périmée ; elle n'est pas corrigée.

### RT-P1-CCH-09 : appliquée (L200-9-1, LEGIARTI000030989277, de `retained_unchanged` à `rewrite_draft`)

- **Ce qui change.** Le 2° du I renvoyait à la durée de L202-9-1, que le projet abroge. Il reprend désormais directement le délai de deux ans « à compter de l'acceptation de la succession ou de la donation », pour les sociétés d'attribution et d'autopromotion.
- **Choix retenu.** C'est l'option « deux ans sans renouvellement » de l'objection : elle conserve la faveur sans l'étendre. La formule atypique « ou de la donation » est conservée, par cohérence avec L201-9.
- **Laissé à l'auteur :**
  - un renouvellement statutaire ;
  - ou une durée illimitée, à concilier avec L202-2.

### RT-P1-CCH-10 : appliquée (L831-1, LEGIARTI000038814882, de `retained_unchanged` à `rewrite_draft`)

- **Ce qui change.** Aux 1° et 6°, les réserves de L831-2 sont limitées « aux seules aides dues au titre des mois commençant avant l'entrée en vigueur de la loi portant abrogation de cet article ». La réouverture de l'APL accession, décidée par L831-2 proposé, devient ainsi effective.
- **Motif et notes.** Ils sont corrigés : l'ancienne formule « ce maintien ne rouvre pas les régimes fermés » est remplacée.
- **Déjà réglé.** L'annexe I à D331-65 était déjà coordonnée.

### RT-P1-CCH-12 : partiellement appliquée

- **L441-1 (LEGIARTI000054354341).** Le texte vise désormais « des comptes rendus déjà établis en application de l'article L. 441-2-5 avant son abrogation ».
- **L421-7 (LEGIARTI000006825599).** Les deux renvois à L423-1, abrogé, sont limités aux dissolutions prononcées et aux liquidations antérieures que L423-1 préserve : premier alinéa et réserve du cinquième alinéa. Le motif, qui disait L423-1 maintenu, est corrigé.
- **Déjà réglé** (texte de production cité dans `skipped`) : R*442-3-3, R481-11, R362-2, R441-12 et R213-2.
- **Laissé à l'auteur.** R421-1 garde le même renvoi à L423-1. Il est hors du périmètre de l'objection.

### RT-DOMTS-02 : appliquée (annexe II, article 143, LEGIARTI000054363256)

- **Ce qui change.** Le troisième alinéa précise que l'année de la suppression n'est pas une « période d'application partielle de la majoration ». La majoration se calcule aux taux de 4,25 % et 9,35 %, sur la seule rémunération versée avant la suppression, avec les limites annuelles entières du 2 bis de l'article 231 ancien. Il n'y a ni prorata ni ajustement à l'année, conformément à CGI 231 II proposé.
- **Exemple.** Pour un salaire de 3 000 € par mois et une suppression au 1er juillet, la majoration est de 372,77 €, contre environ 1 017 € avec l'ancien prorata.

### RT-A1-03 : appliquée (CGI 508, LEGIARTI000006309958, mode `new`)

- **Statut.** L'objection est « à confirmer », mais la correction est sûre dans les deux hypothèses :
  - si 508 s'applique encore, elle retire une formalité ;
  - s'il ne s'applique plus, elle est sans objet.
- **Ce qui change.** L'« établissement désigné à l'administration » devient un établissement « connu de l'administration », ce qu'établissent les pièces ordinaires, l'autorisation du procédé spécial ou un statut d'accise existant. Aucune démarche propre n'est exigée et les désignations antérieures restent valables. Le texte est celui du § 5.4 du dossier A1, complété d'une phrase : la proposition ne retarde pas l'abrogation différée prévue par l'ordonnance 2021-1843.
- **Laissé à l'auteur :**
  - l'applicabilité résiduelle de 508 et la concordance avec le CIBS, hors corpus ;
  - l'article était absent de l'inventaire.

### RT-DOMTS-03 : appliquée dans la variante B03h (annexe III, articles 369 et 374)

- **Pourquoi une variante.** Les articles appartiennent au groupe B03. Les changements sont dans `apply/B03h/changes.json` et ont été validés.
- **Ce qui change.** Dans ces annexes réglementaires, « la présente loi » ne désignait aucun texte. L'expression est remplacée par « le texte qui introduit la présente rédaction du présent article ». Aucune date n'est fixée et les modalités ne changent pas.
- **Laissé à l'auteur :**
  - le véhicule et la date de ce texte ;
  - l'éventuelle anticipation du versement annuel sur la suppression de la taxe (option de l'objection).

## Déjà réglées en production (citations dans `skipped`)

- **RT-P1-CCH-05.** L342-14 I 1° b est déjà limité aux manquements antérieurs à l'abrogation du supplément de loyer de solidarité, sous réserve de la loi répressive plus douce (balayage W12).
- **RT-A1-02.** La phrase de 165 sur la déclaration de 302 D bis a été remplacée par la preuve par pièces ordinaires, avec la correction de RT-A1-01.
- **RT-A1-04.** L'objection ne demande aucune correction propre. L'autorisation du procédé spécial (186) et le pouvoir de retrait (192) sont conservés.
- **RT-MENS-02.** La transition de 50-0 I III et de 111-0 H est déjà écrite : anciens mois et mois à cheval, numéro « le cas échéant », loi répressive plus douce, même déclencheur.
- **RT-MENS-05.** La fiche d'impact de 50-0 I a déjà été corrigée (champ `after` et population visée).

## Non appliquées

- **RT-A1-06.** Simple alerte : l'objection dit elle-même qu'aucune correction n'est nécessaire, et l'option proposée serait une réécriture de style.
- **RT-DOMTS-04.** Alerte sans effet normatif, qui reviendrait sur un choix explicite des auteurs : L3332-22, L5123-5 et L5428-1 sont maintenus inchangés. Ce serait aussi une réécriture de style.

## Résumé

- **Appliquées (8 objections, 10 lignes) :**
  - en totalité : CCH-06, CCH-07, CCH-09, CCH-10, DOMTS-02, A1-03 ;
  - en partie : CCH-12 (2 articles ; les 5 autres déjà réglés) ;
  - dans la variante B03h : DOMTS-03 (2 articles).
- **Déjà réglées (5) :** CCH-05, A1-02, A1-04, MENS-02, MENS-05.
- **Non appliquées (2) :** A1-06, DOMTS-04.
- **Fermeture de faille, extension de faveur non décidée, nouvelle formalité :** aucune.

Revue IA : rien de ceci ne vaut validation par un juriste.
