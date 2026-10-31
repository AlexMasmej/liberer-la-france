# T107 — décisions (lecture systématique, palier A)

Paquet : annexe III du CGI, de 95 ter à 111-00 D (22 articles). Le texte a été lu en production, en lecture seule, le 30 octobre 2026.

## TIERA-T107-01 (= TA-T043-01) — annexe III 111 quater J : appliquée

- **Article touché :** 111 quater J (LEGIARTI000026484581). Il est dans le paquet T107 et n'a pas de `previous_owner`.
- **Défaut (G, F1 + F5) :** la proposition maintenait, sans limite dans le temps, les deux phrases « est modulée à la hausse » (catégories D ou E de D. 233-15, catégories C ou D de D. 233-16 et D. 233-17). Or 302 bis O proposé ne permet plus qu'une modulation « uniquement à la baisse » et déclare ces branches inapplicables aux opérations nouvelles. 302 bis R proposé interdit de les rétablir. Le motif disait en outre que la suppression n'était « pas étayée ».
- **Changement :** les deux hausses sont retirées pour les abattages et traitements réalisés à partir de l'entrée en vigueur de la loi. Un dernier alinéa les maintient pour les opérations antérieures (liquidation, paiement, contrôle, restitutions, prescriptions, recours). Les baisses A et B, le classement au 31 décembre, le renvoi au règlement (UE) 2017/625 et le taux fixé par arrêté conjoint sont inchangés.
- **Critère d'alignement :** la correction rend effective une réforme déjà décidée (302 bis O) et supprime une contradiction. Elle ne crée ni taxe ni formalité.
- **Champs du lot :** `change_type: normative_reduction`, `reform_policy_id: editorial_direction_2026_10_19`, deux `removed_provisions`. Le `substantive_impact` reste `coordination_only` : la réduction est déjà comptée en 302 bis O, sous la mesure `redevance-abattage-fin-majoration`. Le motif et les notes ont été corrigés.
- **Contrôle :** `python3 -B apply/check_changes.py T107` renvoie `problems: []`. Le seul diagnostic est `explicit_normative_reduction`, ce qui est voulu.
- **Point pour l'auteur ou le coordinateur :** les notes de 302 bis O (« leurs suppressions rédactionnelles dans J restent à faire ») et de 302 bis R (« Contradiction effective localisée en 111 quater J ») deviendront périmées une fois la correction appliquée. C'est un défaut mineur de notes, sans demande formelle.

## Défauts mineurs non corrigés

- **111 quater U (m, F10) :** le corps est correct (abrogation du doublon). Mais le motif et les notes affirment que 302 bis WD « impose déjà la déclaration et le paiement » et que « le niveau législatif maintient la charge fiscale ». Or 302 bis WD proposé, dans ses deux versions, abroge la redevance d'agrément de l'alimentation animale pour les événements nouveaux. À corriger si l'article est retouché.
- **111-0 D (m, F5, article de Y16) :** au V, le nouvel entrepositaire « communique » encore son estimation à l'administration. Le I du même article et 111-0 B (I et II, même seuil, même dispense du 3° de 302 G V) écartent toute transmission préalable. Il n'y a pas de contradiction normative. Aligner le V sur 111-0 B serait un allègement supplémentaire : c'est un **arbitrage pour l'auteur**. Aucun dossier de variante Y16tec n'a donc été créé.

## Défaut déjà traité ailleurs

- **96 G / annexe IV 41 septies :** l'arrêté organise encore la liste récapitulative que 96 G proposé supprime. Ce défaut a déjà été relevé G et corrigé par T124 (TIERA-T124-01), et la correction attend d'être appliquée. Il n'est pas compté une seconde fois. Aucune demande n'a été faite.

## Résumé

Sur 22 articles : 1 G, 2 m et 19 « 0 ». Il y a une correction (111 quater J), dans `apply/T107/`. Aucun dossier de variante n'a été créé et aucune demande n'a été adressée à un autre groupe.

Revue IA : ce n'est pas une validation par un juriste.
