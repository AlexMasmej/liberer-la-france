# B07 : objections P2, décisions

Les textes ont été lus en production, en lecture seule, le 29 octobre 2026, avec `CITE_PRODUCTION=1 python3 -I tools/cite.py` et SQLite en `mode=ro`. Les exports sont dans `evidence/cited/production-20261029/`. Le registre (`reports/register.json`) n'a servi qu'à lire les objections ; chacune a été confrontée au texte actuel.

Contrôle :
- `python3 -B apply/check_changes.py B07` : 15 lignes construites, 15 validées, `problems` vide.
- `python3 -B apply/check_changes.py B02g` (variante pour B02) : 3 lignes construites, 3 validées, `problems` vide.
- Les diagnostics sont voulus :
  - réductions déjà déclarées ;
  - renvoi ajouté à R5221-20 dans R5221-22 ;
  - longueurs de L216-3, L281-6 et R213-5, déjà allongées par leurs transitions ;
  - mention documentaire de 1609 quinvicies.

Rien n'a été écrit en production. Cette revue a été faite par une IA. Elle ne vaut pas validation par un juriste.

## Bilan

| Décision | Objections |
|---|---|
| Appliquée | RT-INV-08, RT-INV-11, RT-DOMIS-08, RT-DOMIS-10, RT-DOMIS-11, RT-RXF03-03, RT-UNION-01 (variante B02g), RT-UNION-06 |
| Appliquée en partie | RT-INV-01 et RT-INV-07 (textes corrigés ; la sortie de l'inventaire revient au coordinateur), RT-UNION-07 (contenu aligné ; points de départ non unifiés) |
| Déjà réglée | Aucune entièrement. Le volet P0 de RT-INV-01 (réinstitution de la CSA) était déjà levé en production. Le texte de 302 J (RT-INV-10) ne rétablit déjà rien. |
| Non appliquée | RT-INV-10 (inventaire, CIBS hors corpus), RT-INV-14 (à confirmer), RT-DOMIS-09 (non aligné), RT-DOMIS-12 (arbitrage) |

## Objections appliquées

### RT-INV-01 : CGI 1609 quinvicies (LEGIARTI000042914206), appliquée en partie
- **Production.** Le corps commence déjà par « Le présent article est abrogé » et ne réinstitue plus la contribution. Il contient pourtant encore des règles de fond qui doublent L6242-1 VIII avec d'autres formulations : contrat unique, intérim, préavis.
- **Correction.** Le corps devient une mention documentaire, conforme à la correction révisée :
  - l'article est abrogé depuis le 1er janvier 2022 (ordonnance n° 2021-797, art. 6, lien LEGI ABROGE vérifié) ;
  - la rédaction des lois de finances pour 2020 et 2021 n'est jamais entrée en vigueur ;
  - le régime de la contribution relève de L6242-1.
- **Ce qui ne change pas.** Le type `full_repeal` est conservé. Le `repeal_scope` et l'évaluation d'impact sont mis à jour.
- **Rien n'est perdu.** L6242-1 proposé a été relu en entier. Il porte la créance, les décomptes du contrat unique, les exclusions intérimaires, les années antérieures et l'aide de L6243-1-2.
- **Laissé au coordinateur.** Sortir LEGIARTI000042914206 de la couverture courante (opération d'inventaire).
- **Laissé à l'auteur.** Mentionner expressément les rémunérations garanties entre missions dans L6242-1 VIII. L'objection laisse ce point au conditionnel, et ces garanties relèvent du droit du travail, pas d'une exclusion d'assiette.

### RT-INV-07 : versions fantômes de R611-2, R5221-22 et 382-0 C bis, appliquée en partie
- **R611-2 (LEGIARTI000036704272).** C'est la version historique de 2018, remplacée en 2019. Sa proposition normative est retirée : elle passe en `retained_unchanged`, sans proposition. Cette proposition étendait le régime de 2018 à 2019-2022 et créait une procédure concurrente. Aucune faveur n'est perdue : l'opposition d'un mois (IV de 2023) et le VI sur les déclarations à néant de LEGIARTI000043292679 couvrent les procédures en cours.
- **R5221-22 (LEGIARTI000043320687).** Ses notes signalent la version remplacée le 1er mai 2021 et le défaut de borne. Sa proposition reste identique à celle de la version en vigueur (voir RT-INV-08). Retirer une proposition identique n'apportait rien, et le maintien d'une source périmée l'aurait affichée comme maintenue.
- **382-0 C bis (LEGIARTI000034729420 et LEGIARTI000036256024).** Les notes sont corrigées : les liens LEGI montrent que 036256024, issue du décret n° 2017-1750, est la seule version en vigueur. La proposition, identique et conforme au texte en vigueur, est inchangée.
- **Laissé au coordinateur.** Sortir de l'inventaire courant LEGIARTI000036704272, LEGIARTI000043320687 et LEGIARTI000034729420.

### RT-INV-08 : R5221-22, deux versions, appliquée (à confirmer, correction sûre)
- **Ce qui change.** « La situation de l'emploi ne peut être opposée » devient « La condition prévue au 1° de l'article R. 5221-20 ne peut être opposée ».
- **Pourquoi la correction est sûre.** Le 1° de R5221-20 est une alternative : métier en tension ou offre publiée et non pourvue. Dispenser de la seule situation de l'emploi (le b) ou de tout le 1° produit donc le même effet. La coordination est neutre, quelle que soit la lecture du JORF, qui n'a pas été relu. Elle suit R5221-21.
- **Ce qui est conservé.** L'autorisation de droit, l'ouverture au contrat unique et la transition.

### RT-INV-11 : R4451-39, appliquée
- **Version actuelle (LEGIARTI000037024754).** La note qui disait les versions futures « non fournies » est corrigée.
- **Successeur du 1er juillet 2027 (LEGIARTI000047715485).** Il n'avait aucune décision. Une ligne `new` lui donne un maintien intégral, comme la version qu'il remplace, avec ses rubriques nouvelles 3° et 4°, que l'objection demande de préserver.
- **Laissé à l'auteur ou au coordinateur.** R4451-38 du 1er juillet 2027 (LEGIARTI000047715489) n'a ni décision ni groupe. Elle retire l'obligation propre aux entreprises de travail temporaire et relève de RT-INV-05.

### RT-DOMIS-08 : renvois à 216 dans 209 et 220, appliquée
- **209 (LEGIARTI000048847486).** Au XI, 1, « l'inscription prévue au II de l'article 216 » devient « au IV de l'article 216 ». Le motif est corrigé de même.
- **220 (LEGIARTI000028434377).** Au 4, « en application du II » et « ce même II » deviennent « IV ». Le motif, les notes (subdivisions de 216 actuelles) et la citation d'impact sont alignés.
- **Ce qui ne change pas.** Les crédits et les exclusions.

### RT-DOMIS-10 et RT-DOMIS-11 : 219 (LEGIARTI000053542939), appliquées (à confirmer, corrections sûres)
- **V, 3 (RT-DOMIS-10, `loophole_closure`).** Une phrase est ajoutée : la tranche de l'exercice de distribution, utilisée sur des bénéfices d'un autre exercice, s'impute sur le plafond de l'exercice d'origine.
  - Sans elle, les bénéfices d'un même exercice pouvaient recevoir deux fois 42 500 € à 15 %.
  - L'orientation `is_distribution` demande un plafond explicite qui conserve l'avantage du taux réduit.
  - Chaque exercice garde au moins l'avantage du droit actuel.
  - Si le texte n'autorisait pas le cumul, la phrase est neutre. S'il l'autorisait, elle retire seulement une extension non décidée.
- **V, 2 (RT-DOMIS-11).** L'assiette (bénéfice de la société avant impôt) est énoncée avant la formule 20/80, qui n'est exacte que sans déficit et pour une fraction entièrement taxable, comme le confirme le 4. La règle et le taux sont inchangés. La citation d'impact est mise à jour.
- **Laissé à l'auteur.** Le chiffrage. L'examen de l'impôt de distribution au regard de la directive 2011/96/UE, article 5.

### RT-RXF03-03 : annexe IV, 41 septies B (LEGIARTI000054606100), appliquée
- **Ce qui change.** L'article était maintenu ; il devient une coordination avec 290 B proposé, qui attribue l'immatriculation sans durée :
  - 2° du I : abrogé ;
  - 5° du II : abrogé ;
  - 6° du II : « renouvellement en cours, caduque » est retiré.
- **Nouveau III.** Publication sans date de fin de validité. Aucune demande de renouvellement ne peut être déduite de la publication. Le changement prend effet à l'entrée en vigueur de la réforme de 290 B.
- **Ce qui est conservé.** Les listes des agréments et des retraits (1788 E) et la mention de l'audit de 242 nonies B.
- **Lignes de lot.** `normative_reduction` avec trois dispositions retirées, et la même `measure_id` que 290 B, sans double comptage.
- **Non vérifiés.** L'arrêté du 7 octobre 2022 et la reprise dans le CIBS.

### RT-UNION-01 : L281-6 (LEGIARTI000006742239, groupe B02), appliquée dans la variante `apply/B02g/`
- **Ce qui change.** Seules les notes changent : la loi n° 2004-810 vise un « dernier alinéa du V » qui n'a jamais existé ; aucun V n'est créé.
- **Ce qui ne change pas.** Le corps sur ce point.

### RT-UNION-06 : L216-2, L216-3, L216-4, appliquée
- **Ce qui change.** Dans chaque article, la phrase des notes qui décrivait des renvois discordants de L281-6 est remplacée par : « L281-6 proposé traite les catégories historiques des groupements ; aucune coordination supplémentaire n'est requise dans le présent article. »
- **Pourquoi c'est exact.** RT-UNION-02 est déjà appliquée en production : L281-6 ancre ses catégories sur les rédactions antérieures au 25 avril 1996.
- **Ce qui ne change pas.** Les corps de L216-2 et L216-4.

### RT-UNION-07 : transitions de la fin de l'approbation des statuts, appliquée en partie
- **L216-3 (B07).** La transition est alignée sur L281-4, L752-1, R281-4 et R752-1 :
  - fin des procédures en cours sans nouveau dépôt ;
  - préservation des approbations données, des actes régulièrement adoptés, des droits et engagements valablement constitués et des recours ;
  - absence de régularisation des illégalités antérieures ;
  - conservation des statuts sans nouvelle adoption.
- **Variante B02g.**
  - L281-6 reçoit la réserve d'illégalité.
  - R216-2 reprend la formule de la correction révisée, tout en gardant « sans nouvelle adoption imposée ».
  - R213-5 préserve les droits « valablement constitués » et les recours.
- **Déjà alignés.** L281-4, L752-1 (deux versions), R281-4 et R752-1.
- **Non fait.** L'unification des points de départ. Chacun suit son propre fondement légal (dispense de L216-3, abrogation de L281-4) : les unifier relève d'un choix de véhicule, non d'une contradiction. L'option préférable, une disposition finale unique dans la loi et le décret, est laissée à l'auteur.
- **Hors de cette objection.** D227-6 (articulation avec RT-TUT-01).

## Objections non appliquées

- **RT-INV-10 (302 J), hors corpus et inventaire.**
  - Le texte ne rétablit déjà rien : maintien sans corps, et un motif qui exclut tout rétablissement.
  - Le classement hors couverture courante revient au coordinateur.
  - La coordination de l'annexe II, 289, 4°, avec le CIBS est hors corpus.
- **RT-INV-14, à confirmer.**
  - Il s'agit de documenter la règle de sélection de l'inventaire, puis de décider l'inclusion des versions orphelines (R4623-29, 302 B, 1695 ter et quater, R4214-28) après vérification sur Légifrance, inaccessible (403).
  - Aucune de ces versions n'a de brouillon en production. Le choix revient au coordinateur.
- **RT-DOMIS-09, non aligné.**
  - La correction crée des présomptions de distribution et une exigence nouvelle sur les conventions de prêt (échéance, intérêt de pleine concurrence). C'est une condition nouvelle qui avance l'imposition.
  - L'objection est à confirmer au regard de la liberté d'établissement, et elle propose elle-même de ne rien changer.
- **RT-DOMIS-12, arbitrage.**
  - Aucune correction de texte n'est demandée. La correction documentaire, un scénario de chiffrage, est hors codes.
  - L'option d'une imposition annuelle des revenus passifs suppose une décision expresse de l'auteur.

## Résumé

- **Appliquées :** 8 entièrement, 3 en partie. Cela fait 18 lignes : 15 pour B07, dont une nouvelle proposition sur une version future, et 3 dans la variante B02g.
- **Déjà réglées :** aucune entièrement. Le volet P0 de RT-INV-01 était déjà levé.
- **Non appliquées :** 4.
- **Garanties :** aucune taxe créée, aucune formalité nouvelle, aucune faveur retirée. Une seule fermeture est signalée à l'auteur (`loophole_closure`) : le plafond PME de 219 V 3.
- **Revue IA :** rien de ceci ne vaut validation par un juriste.
