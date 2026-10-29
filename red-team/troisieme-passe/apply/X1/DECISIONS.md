# X1 : décisions sur les 9 défauts grossiers du second audit aléatoire

J'ai lu la production en lecture seule (`CITE_PRODUCTION=1 tools/cite.py` et sqlite en `mode=ro`). Les pièces citées sont sous `evidence/cited/production-20261029/`. J'ai consulté deux sources primaires sur Légifrance le 29 octobre 2026 : la loi n° 89-462 (articles 22 et 40, version en vigueur au 29/10/2026, donc postérieure au 18 octobre 2026) et le décret n° 2018-174 (JORF, articles 15 et 16).

## Bilan

- Les 9 défauts sont confirmés.
- 7 sont corrigés sur 17 articles : T123, T124, T065, T215, T236, T167, T169.
- T040 est corrigé dans `apply/W08b/changes.json` (groupe W08b, propriétaire des articles de W08).
- T081 est non appliqué (hors corpus) ; un texte non codifié est proposé sous `uncodified`.
- Le contrôle `python3 -B apply/check_changes.py X1` donne `problems: []` : 17 lignes construites et 17 validées.
- Diagnostics : tous voulus. Ce sont les renvois R. 231-24 → R. 231-4, l'ajout du renvoi à L. 200-8 dans L202-2, des changements de renvois hérités des brouillons dans les annexes, et un rapport de longueur de 2,51 pour l'abrogation motivée de l'article 138.
- Identifiant des objections : `AUDIT2-T<n>`.

## Par défaut

### T081 — CGI 283 (LEGIARTI000051214570) : non appliqué (hors corpus)

- **Défaut confirmé.** La NOTA annonce l'abrogation de l'article au 1er janvier 2027 par l'ordonnance n° 2025-1247. Seul le 2 septies est maintenu, jusqu'à sa reprise sous L. 215-9 du CIBS. La suppression des solidarités des 2 bis, 2 ter, 2 quater et 5 serait donc sans effet après cette date.
- **Pourquoi pas de correction codifiée.** Les articles de destination du CIBS ne sont pas au corpus, et aucune version future de 283 n'y figure. Une correction codifiée obligerait à inventer un numéro.
- **Ce qui est fait.** La proposition de 283 reste telle quelle : elle a un effet si la loi entre en vigueur avant 2027. Une disposition non codifiée est rédigée sous `uncodified` (I à III) :
  - les reprises CIBS de ces solidarités ne s'appliquent plus aux faits générateurs postérieurs ;
  - les 3, 4, 4 bis et 4 ter sont conservés ;
  - les opérations antérieures gardent leur régime ;
  - aucune formalité de remplacement.
- **Pour l'auteur.** Identifier les articles du CIBS par la table de l'article 15 de l'ordonnance. C'est la même famille que RT-INV-06.

### T123 — CSS D531-5 (LEGIARTI000030058462) : appliqué

- **Ce qui change.** Les deux conditions d'indemnités de la source sont rétablies. Le seul renvoi mort à l'article 204-0 bis du CGI (ABROGE au 2017-01-01) est remplacé par le 1° de l'article 81 du CGI. Ce 1° fixe désormais la fraction des indemnités de fonction des élus locaux affranchie au titre des frais d'emploi (17 % de l'indice brut terminal, 38,75 % pour les communes de moins de 3 500 habitants).
- **Transition.** Elle vaut pour les prestations dues à compter de la nouvelle rédaction. Les prestations versées et les droits ouverts sont maintenus. « Présent décret » devient « présente rédaction ».
- **Pourquoi.** Le 1 du I de L. 531-4 réserve le taux plein à la cessation d'activité et charge le décret d'assimiler le mandat à une activité. La suppression des plafonds étendait donc la PreParE, sans décision de réforme.
- **Lignes de lot.** `change_type`, `removed_provisions` et `reform_policy_id` sont retirés. Le bilan d'impact devient `coordination_only`.
- **Pour l'auteur.**
  - Le second alinéa (parlementaires) reprend la source. Son renvoi au 1° de l'article 81 vise aujourd'hui les frais de mandat de l'article 4 sexies de l'ordonnance n° 58-1100 : sa portée est à vérifier.
  - `reference_checks` et `reference_coherence` de la ligne décrivent encore la suppression du plafond et portent l'ancienne empreinte. Ils sont à rafraîchir par l'outil d'application.

### T124 — travail R364-2 (LEGIARTI000022123530) : appliqué (abrogation, `full_repeal`)

- **Constat.** Les articles R342-7, R342-8, R342-10 et R342-11 sont tous ABROGE depuis le 2008-05-01. R342-12 est abrogé depuis le 2010-04-22 : l'article 10 du décret 2008-244 ne maintenait R364-2 que pour lui, et l'article 15 du décret 2010-389 a abrogé ce reste.
- **Ce qui change.** L'article est abrogé, sans contravention ni obligation de remplacement. Aucun fait n'est encore poursuivable (prescription d'un an). Le contrôle moderne du détachement (R1263-1 et suivants) est intact.
- **Notes.** L'affirmation « pas présents dans le corpus » est corrigée. Aucun renvoi entrant vers R364-2.

### T065 — CCH, dépôt de garantie des logements conventionnés : appliqué (8 articles)

- **Constat.** L'article 22 de la loi n° 89-462 plafonne le dépôt à un mois de loyer en principal et en interdit la révision. Il s'applique aux logements sous convention L. 831-1 : le III de l'article 40 ne l'exclut pas.
- **Ce qui change.** Le plafond réglementaire de deux mois est ramené à un mois, avec renvoi à l'article 22. L'absence de révision est ajoutée là où la source prévoyait une révision.
- **Articles touchés.**
  - D353-43 (LEGIARTI000038978520) et D353-137 (LEGIARTI000038979257) : cautionnement révisable ;
  - D353-171 (LEGIARTI000038979443) et D353-207 (LEGIARTI000038979686) : dépôt de deux mois ;
  - article 20 des annexes V à D353-127 (LEGIARTI000039049069) et III à D353-32 (LEGIARTI000039049222) ;
  - article 17 des annexes III à D353-166 (LEGIARTI000039048967) et D353-200 (LEGIARTI000039048903).
- **Pourquoi aller au-delà de D353-137.** D353-43, D353-171 et D353-207 portent la même contradiction. Je les ai inclus pour ne pas laisser des articles voisins incohérents ; on ne compte qu'un seul défaut.
- **Transition.** Aucune formalité. Les garanties régulièrement versées au titre des baux en cours ne sont pas modifiées.
- **Qualification.** C'est une mise en conformité avec une loi qui prime déjà, pas une contrainte nouvelle. Les conventions types récentes du corpus retiennent déjà un mois. Les quatre articles maintenus passent en `rewrite_draft` / `coordination_only`. Dans les annexes, l'effet `coordination` s'ajoute à leur bilan.
- **Pour l'auteur.**
  - Les délais de restitution de trois mois (article 20 des annexes V à D353-127 et III à D353-32, article 21 de l'annexe III à D353-190) excèdent les délais de l'article 22, qui sont d'un ou deux mois. Ils ne sont pas modifiés.
  - L'annexe III à D353-190 garde « revisable » malgré son plafond d'un mois. Elle n'est pas modifiée, car elle ne reprend pas le plafond de deux mois.
  - La phrase de l'article 22 sur l'absence de révision est reprise de la lecture du second audit. Ma propre consultation n'a pas pu afficher ce passage.

### T215 — annexe III 47 A (LEGIARTI000034737284) : appliqué

- **Ce qui change.** Le choix du déclarant entre procédé informatique et support papier est rétabli, « dans les conditions de l'article 89 A ». C'est cohérent avec 89 A proposé (LEGIARTI000047622398 : « à son choix… », « aucune autorisation ni justification ») et avec 344 GE proposé.
- **Transition.** Elle renvoie à celle de 89 A. Le bilan reste `coordination_only`, sous la mesure `declarations-fiscales-choix-support`.
- **Notes.** L'affirmation « 89 A impose déjà le procédé informatique » est précisée.

### T236 — annexe IV 138 (LEGIARTI000006301663) : appliqué (abrogation, `full_repeal`)

- **Constat.** L'article 138 organise la perception d'un impôt sur les spectacles qui n'a plus de base légale. CGI 1565 bis est ABROGE au 2015-01-01. CGI 1559 était limité aux réunions sportives et aux cercles, puis aux seuls cercles ; il est ABROGE au 2025-01-01.
- **Ce qui change.** L'article est abrogé, sans impôt ni formalité de remplacement. Les impositions nées avant ces abrogations gardent leur régime.
- **Motif et notes.** La prémisse fausse du motif et l'affirmation « absents du corpus » des notes sont corrigées.
- **Pour l'auteur.** Les autres articles du bloc 124 à 154 de l'annexe IV (dont 145, 147, 153 et 154) n'ont pas été réexaminés.

### T167 — CCH L202-2 (LEGIARTI000031010344) : appliqué

- **Ce qui change.** Au 4°, « Ces opérations font l'objet d'une comptabilité séparée. » devient l'identification des opérations et de leur résultat dans la comptabilité de la société, « dans les conditions et selon la transition prévues à l'article L. 200-8, sans comptabilité séparée ». C'est la même formule que L201-3.
- **Motif et notes.** Ils sont corrigés : les notes disaient que « la comptabilité séparée n'est pas retirée ». L'effet `coordination` est ajouté sous la mesure de L200-8.
- **L200-8 n'est pas modifié.** Sa clause « nonobstant » reste exacte et inoffensive.

### T169 — CSS, renvoi R. 231-24 : appliqué (4 articles)

- **Constat.** Le JORF du décret n° 2018-174 le confirme :
  - article 15, 27° : « L'article D. 231-24 devient l'article R. 231-4 » ;
  - article 16, 4° : « A l'article D. 213-4, aux premiers alinéas des articles D. 224-3 et D. 224-6 et à l'article D. 752-1, la référence : « D. 231-24 » est remplacée par la référence : « R. 231-4 » ».
- **Ce qui change.** Le renvoi est rectifié à D213-4 (LEGIARTI000036704556), D752-1 (LEGIARTI000036704528), D224-3 (LEGIARTI000041968586) et D224-6 (LEGIARTI000046356337). Une phrase précise que les élections et délibérations antérieures restent valables.
- **Pourquoi quatre articles.** D752-1, D224-3 et D224-6 portent la même erreur, et le décret les vise expressément.
- **Pour l'auteur.** D224-3 et D224-6 sont des versions de 2020 et 2023. Si leurs décrets ont reproduit « R. 231-24 », la cible voulue reste R. 231-4.

### T040 — travail D6325-26 (LEGIARTI000020690617) : appliqué dans `apply/W08b/changes.json`

- **Pourquoi W08b.** L'article appartient à W08. À la demande du coordinateur, la correction est rédigée sous le groupe W08b et retirée des `requests` de X1. `check_changes W08b` donne `problems: []`.
- **Ce qui change.** Mode `replace`, passage de `retained_unchanged` à `rewrite_draft`, bilan `coordination_only` (unit `legal_duty`). Le renvoi aux articles L6325-16 et L6325-17 (ABROGE au 2019-01-01) est remplacé par la formule générale de la version officielle de 2008 (LEGIARTI000018522971), étendue aux réductions : « cumulable avec les exonérations et réductions de cotisations patronales de sécurité sociale dont bénéficient les groupements d'employeurs au titre de la conclusion de ces contrats ». Le cumul favorable est conservé.
- **Variante pour l'auteur.** Reprendre mot pour mot la phrase de 2008, sans « et réductions ».
- **Hors correction.** D6325-19 et D6325-19-1 ont le même renvoi mort ; ils ne sont pas modifiés (arbitrage de l'auteur).

## Points communs laissés au coordinateur

- Plusieurs lignes portent `reference_checks` ou `reference_coherence` calculés sur l'ancienne proposition : D531-5, 47 A, les annexes CCH et D213-4. `check_changes` ne les recalcule pas ; ils sont à rafraîchir si l'outil d'application l'exige. Le certificat d'impact, lui, est rafraîchi par l'outil.
- `apply/X1/changes.json` est produit par un script en lecture seule, gardé hors du projet : `/private/tmp/claude-501/-Users-alexandremasmejean-Coding-libererlafrance/b3c16b1d-1a74-44b1-ad92-751a94a7748e/scratchpad/x1/build.py`. Les remplacements y sont faits sur des passages exacts, chacun vérifié comme unique.

## Résumé

Les 9 défauts sont confirmés. 7 sont corrigés sur 17 articles dans X1, T040 est corrigé dans W08b et 1 n'est pas appliqué (T081, hors corpus, texte non codifié proposé). Le contrôle donne `problems` vide. Aucune formalité, sanction ni impôt de remplacement n'est créé, et les droits acquis et transitions sont conservés. Revue IA : rien de ceci ne vaut validation par un juriste.
