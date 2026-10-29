# Groupe B06 : décisions sur les objections P2

Revue IA, sans validation par un juriste.

## Méthode

- Production lue le 29 octobre 2026 en lecture seule : `CITE_PRODUCTION=1 python3 -I tools/cite.py …` (exports dans `evidence/cited/production-20261029/`), et `corpus.sqlite` ainsi que les fichiers de lots ouverts en mode `ro`.
- Chaque proposition est reprise mot pour mot depuis la production. Les remplacements sont faits par chaînes exactes, avec contrôle d'unicité ; le reste est inchangé.
- Contrôles passés sans problème :
  - `python3 -B apply/check_changes.py B06` : 10 lignes, 10 validées, `problems` vide ;
  - `B04x` : 3 lignes, `problems` vide ;
  - `A3x` : 1 ligne, `problems` vide.
- Pour lire les métadonnées des lignes de lot, `review_prior.batch_owners` a été importé une fois, en lecture, comme le fait `check_changes.py`. Aucun autre script de production n'a été lancé.

## Objections appliquées

### RT-DOMSRU-03 : appliquée

- **Article touché :** CCH L302-1 (LEGIARTI000053546338).
- **Ce qui change :** le dernier tiret du programme d'actions ne vise plus le 4° de l'article L. 151-41 du code de l'urbanisme, que la proposition de cet article abroge (« 4° Abrogé. »). Il garde les 2° et 4° de L. 151-28.
- **Pourquoi :** la correction supprime une contradiction. Le PLH ne peut plus fonder de réservations de mixité.
- **Ligne de lot :** une entrée est ajoutée à `removed_provisions`. Le diagnostic « renvoi L151-41 retiré » est voulu.

### RT-DOMSRU-04 : appliquée

- **Articles touchés :**
  - CCH L302-5 (LEGIARTI000045214963) : suppression de la dernière phrase du dernier alinéa du IV (« Pour la détermination des résidences principales à l'article L. 444-2, … onzième alinéa du présent IV. »). Le motif et les notes sont actualisés.
  - CCH L444-2 (LEGIARTI000031019854) : notes seules. Le « point résiduel hors lot » est déclaré réglé ; le corps et le motif sont inchangés.
- **Ce qui change :** L444-2 proposé ne comporte plus de condition de taux ni de renvoi à L302-5. La phrase n'avait donc plus d'objet et pouvait faire croire à une condition de taux communal.

### RT-INTEG-01 : appliquée (notes seules)

- **Articles touchés :** urbanisme L121-32 (LEGIARTI000042655490) et L121-34 (LEGIARTI000042655487) ; annexe III 385 (LEGIARTI000006299702) et 38 (LEGIARTI000026348040).
- **Ce qui change :** les notes qui décrivaient comme ouvertes des incohérences déjà corrigées renvoient maintenant aux corps courants :
  - R121-23 vise le « délai d'observations d'au moins quinze jours prévu à l'article R. 121-22 » ;
  - 196 A de l'annexe IV exclut les faits générateurs nouveaux ;
  - le XV de 1649 quater B quater est borné au stock TSCA ancien dans ses trois versions.
- **Ligne de lot :** aucun corps ni motif n'est modifié. Le diagnostic de longueur sur 385 existait déjà : c'est une abrogation avec transition.

### RT-RXCSS-02 : appliquée

- **Article touché :** CSS R155-4 (LEGIARTI000035656783).
- **Ce qui change :** le troisième alinéa ne désigne plus le seul ministre chargé du budget pour l'arrêté du stock. Il dispose : « Le prélèvement pour frais de perception afférent aux cotisations recouvrées avant l'entrée en vigueur de l'abrogation de l'article L. 133-4-10 demeure régi par l'article R. 133-9-4. » L'interdiction de tout prélèvement sur les recouvrements nouveaux est maintenue.
- **Pourquoi :** la contradiction de compétence avec R133-9-4 disparaît.
- **Ligne de lot :** la `proposed_quote` de l'effet concerné est mise à jour dans `substantive_impact`.

### RT-RXFISC-01 : appliquée

- **Article touché :** CGI 879 (LEGIARTI000022335681).
- **Ce qui change :** l'alinéa liminaire « Le présent article est abrogé pour les réquisitions et demandes présentées à compter de … » est supprimé. Les I à III sont inchangés : ils restent la base de la suppression de la CSI pour les demandes nouvelles, de l'interdiction du refus de dépôt et de la sauvegarde du III, et les renvois de 880 à 881 M s'y rattachent toujours.
- **Ligne de lot :**
  - le corps ne commence plus par « Le présent article est abrogé », donc la ligne passe de `full_repeal` à `normative_reduction` (`reform_policy_id` et deux `removed_provisions`) ;
  - `repeal_policy_id` et `repeal_scope` sont mis à `null`.
- **Point laissé à l'auteur :** si une convention commune « Le présent article est abrogé pour… » est voulue dans tout le projet, l'autre option est de reporter la suppression dans une disposition non codifiée.

### RT-RXFISC-02 : appliquée (objection « à confirmer »)

- **Article touché :** CGI 1391 E, version en vigueur (LEGIARTI000048826210).
- **Ce qui change :** « dans sa rédaction en vigueur le 26 octobre 2026 » devient « dans sa rédaction en vigueur au 31 décembre 2026 ».
- **Pourquoi c'est sûr quel que soit le point à confirmer :**
  - cette date est couverte par la version de 278 sexies présente au corpus (LEGIARTI000053545600, en vigueur du 21 février 2026 au 1er janvier 2027) ;
  - elle est identique à celle que A1 a retenue pour la version 2027 (LEGIARTI000054567264) ;
  - la dispense d'agrément et le reste de la faveur sont inchangés.
- **Point non vérifié :** aucune consolidation postérieure au 18 octobre 2026 n'a été consultée.

### RT-RXFISC-03 : appliquée, par des variantes pour les propriétaires

- **Articles touchés :** CGI 1600, II 1, appartenant à d'autres groupes :
  - dossier `apply/B04x/` (propriétaire B04) : LEGIARTI000053562172 (version en vigueur, seule visée par l'objection), LEGIARTI000049534935 (2027) et LEGIARTI000051242816 (2028) ;
  - dossier `apply/A3x/` (propriétaire A3) : LEGIARTI000051249045 (2029).
- **Ce qui change :** la formule est la même dans les quatre versions. « après la suppression de la taxe sur le chiffre d'affaires » devient « après la suppression, prévue à l'article 1600 A, de la taxe pour frais de chambres de commerce et d'industrie assise sur leur chiffre d'affaires ».
- **Pourquoi :** c'est une simple précision, qui évite une lecture comme renvoi à la TVA. Les versions futures sont corrigées pour éviter une divergence entre versions.
- **Ligne de lot :** la `proposed_quote` de la version en vigueur est mise à jour.
- **Point pour le coordinateur :** ces lignes ont pu être retouchées par B04 ou A3. Il faut fusionner avant d'appliquer.

## Objections non appliquées

### RT-DOMSRU-05 : non appliquée (« à confirmer », arbitrage)

- **État :** le défaut subsiste. Aucune source de décompte n'est désignée pour le numérateur des 50 % de 1384 B, 1384 C et 1384 G.
- **Pourquoi pas :** la correction choisit une méthode (répertoire L411-10 et conventions L831-1 seuls) qui fait baisser la proportion. Elle étend donc en pratique les exonérations sans décision de l'auteur, et l'objection laisse ouvertes deux autres options.
- **À l'auteur :** choisir entre trois méthodes :
  - données légalement disponibles seules ;
  - dernier décompte notifié, figé ;
  - critère tiré du seul répertoire.

### RT-DOMSRU-06 : non appliquée (hors corpus)

- **Pourquoi pas :** les compagnons CGCT L2252-2, L3231-4-1 et L4253-2 sont absents de `corpus.sqlite`. Modifier seul L302-5 V créerait une contradiction avec ces compagnons, qui figent la liste « la veille ».
- **À l'auteur :** ouvrir la dérogation aux plafonds de garanties aux communes futures éligibles, dans le manifeste coordinations/sru-quotas.

### RT-DOMSRU-07 : non appliquée (hors corpus, « à confirmer »)

- **Pourquoi pas :** tous les articles à changer relèvent du CGCT : L1523-5, L1523-6, L1525-3, L5216-5, L5215-20 et L5214-16. L302-7 garde déjà l'affectation des anciennes sommes.
- **À l'auteur :** maintenir les habilitations de financement, ou motiver leur abrogation comme une restriction distincte.

### RT-DOMSRU-08 : non appliquée (hors corpus : inventaire, non un article)

- **État :** `runtime/sru-integral/status.json` de production indique toujours `exhaustive_repeal_complete: false`. L'instantané 20261029T034912Z ne contient pas `sru-integral`.
- **Au coordinateur :** copier l'inventaire dans l'instantané suivant, et corriger les synthèses publiques pour dire que seul le volet quotas, carence et prélèvement est traité.

### RT-DOC-01 : déjà réglé

- **Texte actuel :** l'annexe I à R434-32 (7) n'a pas de brouillon, son inventaire est en documentary_hold, et sa source garde « [cliché non reproduit] » après « assignant à chaque quadrant une valeur de : ».
- **Reste ouvert :** le fac-similé JO est une pièce manquante.

### RT-DOC-02 : non appliquée (pièce manquante)

- **Texte rédigé et refusé :** le 1° suivant de l'annexe IV, article 15 a été soumis en mode `new`. Le validateur du projet l'a refusé : « Normative graphic source is unresolved ». Seule une abrogation est admise sur une source marquée « non reproduits » tant que les modèles CERFA ne sont pas récupérés. Aucun compagnon n'a été fabriqué.
- **Texte tenu prêt :** le reste de l'article serait inchangé, avec le 1° suivant.

  > 1° Les relevés encore exigés par le 1 de l'article 57 de l'annexe II au code général des impôts sont établis sous forme de fiches individuelles, sur tout support, y compris mécanographique ou électronique, comportant les renseignements mentionnés aux 2° et 4°. L'usage des modèles administratifs Cerfa n° 30-0812 et n° 30-0813 est facultatif. Aucun relevé n'est établi pour les paiements relevant de l'article 242 ter du code général des impôts, y compris lorsque cet article dispense de déclaration, conformément au 1 de l'article 57 de l'annexe II. Ces dispositions s'appliquent aux relevés établis à compter de l'entrée en vigueur de la loi ; les relevés antérieurement établis selon les modèles restent valables et ne sont pas à refaire ;

- **À vérifier avant usage :** le renvoi du 4° a au « troisième alinéa du 3 de l'article 158 » et le « crédit d'impôt » du 4° d.

### RT-DOC-03 : non appliquée (pièce manquante ; volet « motif » déjà réglé)

- **Pièce manquante :** la confrontation au JO authentifié est impossible avec les pièces disponibles.
- **Déjà réglé :** le motif et les notes de l'annexe II du travail énumèrent déjà chaque correction et sa source européenne, avec la réserve « confrontation au JO du 4 juillet 2010, texte 11, restant à effectuer ».

### RT-DOC-04 : non appliquée (pièce manquante)

La réserve reste ouverte. Aucun acte extérieur n'est reconstitué.

## Résumé

- **Appliquées (7) :** RT-DOMSRU-03, RT-DOMSRU-04, RT-INTEG-01, RT-RXCSS-02, RT-RXFISC-01, RT-RXFISC-02 et RT-RXFISC-03 (cette dernière par les variantes B04x et A3x).
- **Déjà réglée (1) :** RT-DOC-01.
- **Non appliquées (7) :**
  - arbitrage : RT-DOMSRU-05 ;
  - hors corpus : RT-DOMSRU-06, 07 et 08 ;
  - pièce manquante : RT-DOC-02, 03 et 04.

Revue IA : rien de ceci ne vaut validation par un juriste.
