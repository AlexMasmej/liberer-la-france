# R3 : demandes de correction du palier A (lecture de la production)

Il y a 12 demandes. 4 sont appliquées, aucune n'a été fusionnée par R3 et 8 ne sont pas appliquées : 7 étaient déjà réglées dans un changement en attente et 1 est un défaut mineur hors règle. Tous les textes visés ont été lus en production (`CITE_PRODUCTION=1`), avec leurs liens principaux.

## Appliquées

- **TA-T016-01 : a3 41 ZZ ter (LEGIARTI000054364166)**. Dossier `R3`. Correction **appliquée**.
  - Défaut : l'article maintenu limitait l'imputation aux « cinq années précédentes ». Or le b du 2 du I proposé de 163 quatervicies (LEGIARTI000053542827) permet d'utiliser les soldes « au cours des années suivantes sans limitation de durée ».
  - Changement : la limitation aux cinq ans est retirée. L'ordre d'imputation est conservé : le plafond de l'année d'abord, puis le solde le plus ancien. Les soldes expirés ne sont pas rétablis.
  - Ligne de lot : l'article passe en `rewrite_draft`, classé `coordination_only`. La mesure est `epargne-retraite-report-sans-expiration`, déjà comptée dans 163 quatervicies.
  - Rectification : le `benefit_review` disait « pendant cinq ans » ; il est corrigé.
  - Pour l'auteur : l'évaluation de `reference_checks` héritée du maintien parle encore de « cinq années suivantes ». Elle relève du recalcul de cohérence des renvois par le coordinateur.

- **TA-T108-01 : a4 50-0 BC (LEGIARTI000030625675)**. Dossier `R3`. Correction **appliquée**.
  - Défaut : l'arrêté maintenu exigeait le point b (identité de l'acquéreur) et le point d (destination) pour toute vente en comptoir. Or 111-0 HB proposé interdit à l'arrêté de les imposer pour les ventes en droits acquittés, et 111-0 HC proposé les écarte pour les ventes à bord.
  - Changement : le texte complet rédigé par T108 est appliqué tel quel. Un alinéa dispense des points b et d pour toute vente en droits acquittés, et une transition est ajoutée.
  - Ligne de lot : `normative_reduction`, classé `coordination_only`, mesure `accises-ventes-taxees-donnees-voyageur`.
  - Pour l'auteur : le point c (numéro de vol) reste exigé pour les ventes en comptoir en droits acquittés.

- **RT-T128-01 : a4 56 AI (LEGIARTI000006301473)**. Dossier `R3`. Correction **appliquée**.
  - Défaut : l'article vise « la caution agréée », alors que 56 AD proposé (LEGIARTI000006300766) supprime tout agrément de la caution.
  - Changement : « la caution agréée » devient « la caution solidaire mentionnée à l'article 56 AD ». La lettre recommandée, les destinataires, le délai de cinq jours francs et l'exigibilité restent inchangés.
  - Ligne de lot : `rewrite_draft`, classé `coordination_only`, mesure `tabacs-caution-fin-agrement-special`.

- **RT-T072-01 : cgi 242 septies (LEGIARTI000042912633)**. Propriétaire T036 ; dossier de variante `T036rc`. Correction **appliquée**.
  - Défaut : le douzième alinéa fixe le seuil de la mise en concurrence par référence à l'agrément ministériel. Or cet agrément est supprimé dans 199 undecies A, B et C, 217 undecies et 244 quater W, X et Y proposés. Ce seuil commande aussi le bénéfice de l'avantage et l'amende de 1740-00 AB.
  - Changement : le seuil est figé dans la rédaction en vigueur la veille de la loi. Aucun agrément n'est rétabli et le champ ne change pas. Le motif est inchangé ; les notes sont complétées.
  - Pour l'auteur (arbitrage, non appliqué) : supprimer la mise en concurrence et l'amende correspondante.

## Non appliquées : déjà réglées dans un changement en attente

- **TA-T013-02** (a3 41 duovicies J) : couverte par **T095**, changement TA-T095-01, qui cite TA-T013-02.
- **TA-T029-02** (a3 46 quater-0 ZE) : couverte par **J13tdx**, changement TA-T102-01, qui reprend TA-T029-02.
- **TA-T041-02** (a4 41 septies A) : couverte par **J16tet**, changement TIERA-T124-02, qui l'absorbe.
- **TA-T043-01** (a3 111 quater J) : couverte par **T107**, changement TIERA-T107-01.
- **TA-T052-01** (a4 121 KL bis) : couverte par **T130**, qui reprend le texte demandé mot pour mot.
  - Défaut mineur restant, pour le propriétaire : la première phrase du motif dit encore « sans changer […] la certification ».
- **TIERA-T082-02** (a4 41 septies D) : couverte par **T124**, changement TIERA-T124-03.
- **TIERA-T084-286M** (a4 50-00 G) : couverte par **M07tev**.

Aucun de ces dossiers n'a été modifié.

## Non appliquée : défaut mineur

- **TA-T110-02** (a4 121 KA, LEGIARTI000049826741) : article maintenu sans propriétaire.
  - Le défaut est mineur (m) : l'alinéa est illustratif (« Peuvent notamment ») et reste utile pour les délivrances antérieures à la gratuité de 953 et 954.
  - Les briefs ne corrigent un défaut m que sur un article déjà modifié, et la rédaction demandée ajoutait une règle.
  - Le point est laissé à l'auteur.

## Validation

`python3 -B apply/check_changes.py R3` et `python3 -B apply/check_changes.py T036rc` renvoient `problems: []`.

Revue IA : rien de ceci ne vaut validation par un juriste.
