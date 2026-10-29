# Dossier P1-CCH — renvois vers des abrogations proposées dans le code de la construction et de l'habitation

Red-team juridique indépendante, troisième passe. Instantané `20261026T230545Z`, corpus au 18 octobre 2026. Rapport du 26 octobre 2026.

*Rapport rédigé par l'agent P1-CCH et enregistré par le coordinateur : l'outil d'écriture de l'agent a refusé le fichier .md. Le JSON et le fichier de classification ont été écrits par l'agent lui-même. Le tableau de périmètre est conservé dans `reports/p1-work/P1-CCH-perimeter.md`.*

C'est une revue IA, qui ne vaut pas validation par un juriste. Elle est provisoire, car la seconde passe continue.

## 1. Synthèse

- 104 alertes, en 54 clusters :
  - 76 écartées ;
  - 13 incohérences du projet ;
  - 12 coordinations manquantes ;
  - 3 faux positifs.
- 13 objections (`P1-CCH.json`) : 4 P1 confirmées (RT-P1-CCH-01 à 04) et 9 P2, dont RT-P1-CCH-11 à confirmer. Aucune P0.
- **SRU** : les renvois vers les articles abrogés (L302-7, L302-8, L302-9-1, L302-9-1-2, R302-16 à R302-19) sont tous bornés par des clauses de transition ou de non-rétablissement, qui renvoient au V proposé de L302-5. Aucun quota n'est réintroduit. TASCOM et dérogations littorales ne sont pas concernées.
- **Coopératives HLM** : les renvois de L422-3 et des statuts types (annexe à R422-6) sont des dispenses devenues sans objet, conservées. Les statuts types des SA HLM (annexe à R422-1) ne sont pas coordonnés (RT-06).
- **Locataires** : RT-04, 05, 07, 11. **Conventions en cours** : RT-03, 07, 13.

## 2. Méthode

- Brief et addendum lus en entier, ainsi que les orientations `logement`, `cooperatives_hlm`, `sru_abrogation`, `preserved_benefits`, `cuts_and_reliefs`, `editorial_direction`, `substantive_outcomes`, `autorisations_urbanisme` et `fiscalite`.
- Export par `tools/cite.py` de la proposition entière de chaque cible et de la version exacte de chaque texte qui y renvoie : la proposition s'il est `rewrite_draft`, la source s'il est `retained_unchanged`.
- Vérification du code et de l'absence d'homonymes. Trois faux positifs ont été trouvés :
  - urbanisme R213-3 vise ses propres R. 211-1 ;
  - dans CGI 150 VB, « dudit code » désigne le CASF ;
  - l'annexe IV à D353-1 vise l'ancien R441-19.
- Requêtes en lecture seule sur les versions en vigueur ou différées, les renvois à L813-5, et les propositions de L445-1 et R445-5-2.
- Chaque citation a été vérifiée par script.
- Lectures ciblées (`read_in_full: false`) : annexes I et II à R423-86, annexe à R422-1, annexe V à D353-127, annexe IV à D353-1, annexe I à D331-65, L422-2, L441-1.

## 3. Objections

| ID | P | Nature | Objet | Alertes |
|---|---|---|---|---|
| 01 | P1 | incohérence | D241-7 III et D711-8 II : Tmin et Tdelta sont choisis selon la qualité de redevable FNAL ou la catégorie de L813-5, toutes deux supprimées pour les périodes nouvelles | 4 |
| 02 | P1 | incohérence | Urbanisme R425-15-2 et R423-70-1 : un accord est maintenu au titre de L126-19, abrogé | 3 |
| 03 | P1 | incohérence | R445-2-8 : évaluation et pénalité de L445-1 portant sur les engagements de R445-5-1, supprimés, conventions en cours comprises | 1 |
| 04 | P1 | anomalie d'inventaire | Versions différées non rédigées : L621-6 (2029, expulsion), L861-2 (2028), CSS L241-13 (2028). 62 cas au CCH et 178 au CSS restent non qualifiés | 0 (3 liées) |
| 05 | P2 | incohérence | L342-14 I 1° b : sanction du SLS sans borne, avec un plafond qui renvoie à L441-11, abrogé | 2 |
| 06 | P2 | incohérence | Annexe à R422-1 (SA HLM) : les 16°, 17°, 20°, 22° et 23° gardent des accords, un agrément spécial et une condition de vacance d'un an supprimés par L422-2 | 1 |
| 07 | P2 | incohérence | Annexe V à D353-127 : l'usage professionnel reste subordonné à une autorisation de R631-4, abrogé | 1 |
| 08 | P2 | incohérence | R432-2 : les contrats doivent mentionner R431-14, abrogé | 1 |
| 09 | P2 | coordination | L200-9-1 I 2° : la durée d'occupation des héritiers renvoie à L202-9-1, abrogé | 1 |
| 10 | P2 | coordination | L831-1 (maintenu) et annexe I à D331-65 : réserves de L831-2 et motifs contraires à la réouverture de l'APL accession | 3 |
| 11 | P2 (à confirmer) | coordination | CSS D133-2 : la réserve de L823-7 est vide, ce qui permet de différer les petits rappels d'APL | 1 |
| 12 | P2 | coordination | Toilettage sans effet normatif : R*442-3-3, R481-11, R362-2 14°, R441-12 I, L441-1, R213-2, L421-7 | 7 |
| 13 | P2 | conflit de source | Annexe IV à D353-1 : la réservation aux agents de l'État renvoie à l'ancien R441-19 (l'alerte elle-même est un faux positif) | 1 |

Le raisonnement, les citations, les empreintes et les preuves sont dans le JSON.

**Recoupements notés par le coordinateur (`reports/dedupe.json`) :**
- RT-04 est une instance de RT-XCUT-01 / RT-INV-05 (versions futures sans proposition) ;
- RT-01 est présenté avec RT-P1-CSS-A-05 (réduction générale après suppression de la CSA et du FNAL).

## 4. Propositions de correction (non validées, aucun chiffre nouveau)

**RT-01 — CSS D241-7, remplacement intégral du III :**

> III. - Pour les revenus d'activité afférents aux périodes d'activité antérieures à l'entrée en vigueur de la loi supprimant la contribution relative à l'allocation de logement sociale prévue à l'article L. 813-4 du code de la construction et de l'habitation, y compris lorsque la réduction est calculée, régularisée ou imputée ultérieurement :
> - pour les employeurs redevables de cette contribution au taux prévu au 1° de l'article L. 813-5 du même code dans sa rédaction applicable à ces périodes : Tmin = 0,0200 ; Tdelta = 0,3781 ;
> - pour les employeurs redevables de cette contribution au taux prévu au 2° du même article dans la même rédaction : Tmin = 0,0200 ; Tdelta = 0,3821.
>
> Pour les revenus d'activité afférents aux périodes d'activité courant à compter de cette entrée en vigueur, les valeurs Tmin = 0,0200 et Tdelta = 0,3781 s'appliquent à tous les employeurs, quel que soit leur effectif, sous réserve de l'alinéa suivant. Pour l'année civile comprenant cette date, les revenus d'activité et le salaire minimum de croissance sont répartis entre les deux périodes à proportion de leur durée, sans double compte, et la réduction est calculée pour chacune d'elles selon les valeurs qui lui sont applicables.
>
> Lorsque la somme des taux des cotisations et contributions effectivement à la charge de l'employeur est inférieure à la somme des valeurs Tmin et Tdelta, la valeur Tdelta est réduite jusqu'à ce que ces deux sommes soient égales. Pour l'application de cette règle, il n'est pas tenu compte de l'application des deuxième à dernier alinéas de l'article L. 5422-12 du code du travail. La suppression de la contribution relative à l'allocation de logement sociale ne peut, à elle seule, réduire la fraction de la réduction imputable sur les cotisations et contributions maintenues, ni donner lieu à imputation sur cette contribution pour les périodes où elle n'est plus due.

**RT-01 — CSS D711-8 II.** En tête :

> Les A et B ci-dessous s'appliquent aux revenus d'activité afférents aux périodes d'activité antérieures à l'entrée en vigueur de la loi supprimant la contribution relative à l'allocation de logement sociale prévue à l'article L. 813-4 du code de la construction et de l'habitation ; les catégories mentionnées au 1° et au 2° de l'article L. 813-5 du même code s'entendent dans leur rédaction applicable à ces périodes.

Puis ajouter un C :

> C. – Pour les revenus d'activité afférents aux périodes d'activité courant à compter de cette entrée en vigueur, le tableau du A s'applique à tous les employeurs. Dans chaque régime, lorsque la somme des taux des cotisations et contributions effectivement à la charge de l'employeur et mentionnées dans une ligne du tableau est inférieure à la somme des valeurs Tmin et Tdelta de cette ligne, la valeur Tdelta est réduite jusqu'à ce que ces deux sommes soient égales. L'année civile comprenant cette date est traitée comme au III de l'article D. 241-7.

Justification : l'écart de 0,0040 entre les deux branches correspond à l'écart des taux FNAL (0,5 % − 0,1 %). Dépendances : L813-4 et L813-5 proposés, version 2028 de L241-13, paramètres annuels. À préserver : la réduction intégrale sur les prélèvements maintenus et le calcul distinct du contrat unique.

**RT-02 — Urbanisme R425-15-2 :**

> Lorsque le projet porte sur des travaux conduisant à la création de plusieurs locaux à usage d'habitation dans un immeuble existant, dans une zone où a été instituée l'autorisation préalable prévue par l'article L. 126-18 du code de la construction et de l'habitation, le permis de construire ou la décision prise sur la déclaration préalable tient lieu de cette autorisation, sous réserve de l'accord du président de l'établissement public de coopération intercommunale compétent en matière d'habitat, recueilli dans les conditions prévues au dernier alinéa de cet article lorsque cet accord est requis.
>
> Pour les décisions prises à compter de l'entrée en vigueur de la loi abrogeant l'article L. 126-19 du même code, y compris sur des demandes déposées auparavant, aucun accord ni consultation ne peut être exigé au titre de cet article, même dans une zone délimitée par une délibération antérieure. Les demandes relevant également de l'article L. 126-18 sont poursuivies sur ce seul fondement, sans nouveau dépôt ni reprise des délais.
>
> Les décisions déjà prises et les accords déjà recueillis conservent leurs effets.

**RT-02 — Urbanisme R423-70-1** : supprimer « ou l'article L. 126-19 », puis ajouter :

> Pour les demandes et déclarations en cours à l'entrée en vigueur de la loi abrogeant l'article L. 126-19 du même code, aucun accord n'est sollicité au titre de cet article.

**RT-03 — R445-2-8, deuxième alinéa :**

> Cette évaluation porte notamment sur les indicateurs chiffrés territorialisés mentionnés à l'article R. 445-5 ainsi que sur les éléments qualitatifs mentionnés aux articles R. 445-5 et R. 445-5-2 à R. 445-5-5. À compter de l'entrée en vigueur de la réforme abrogeant l'article R. 445-5-1, les engagements chiffrés et les développements fixés sur son fondement, y compris dans les conventions en cours, ne sont plus évalués ; leur non-respect ne peut fonder ni mise en demeure ni proposition de pénalité au titre de l'article L. 445-1, y compris pour une période antérieure. Les pénalités devenues définitives avant cette date conservent leur régime.

**RT-04 — Versions différées.**

L621-6, ajouter :

> La rédaction du présent article issue de l'ordonnance n° 2025-1091 du 19 novembre 2025, prévue pour entrer en vigueur le 1er janvier 2029, n'entre pas en vigueur ; à compter de cette date, le présent article demeure régi par la rédaction issue de la loi portant son abrogation.

L861-2, ajouter :

> La rédaction du présent article issue de l'ordonnance n° 2026-647 du 22 juillet 2026 ne s'applique qu'aux revenus d'activité afférents aux périodes d'activité antérieures à l'entrée en vigueur de la loi supprimant la contribution relative à l'allocation de logement sociale.

CSS L241-13 : reporter la proposition sur la version LEGIARTI000054466849.

**RT-05 — L342-14 I 1° b :**

> b) Lorsque les règles d'application du supplément de loyer de solidarité prévues à l'article L. 441-3, dans sa rédaction antérieure à son abrogation, n'ont pas été respectées au titre de périodes d'occupation antérieures à cette abrogation, la sanction est prononcée dans les limites prévues par la convention conclue avec l'Etat et des montants mentionnés à l'article L. 441-11 dans sa rédaction applicable à ces périodes, sous réserve de l'application de la loi répressive plus douce. Aucun manquement postérieur à cette abrogation ne peut être sanctionné sur le fondement du présent b ;

**RT-06 — Annexe à R422-1, clause 3 :**

> 16° … pour la réalisation d'opérations d'aménagement, sans agrément spécial ;
> 17° De gérer, en qualité d'administrateur de biens, des logements situés dans des copropriétés connaissant des difficultés importantes de fonctionnement ou être syndic de ces copropriétés, sans accord préalable du maire ou du préfet, sans demande ni délai d'opposition ;
> 20°, 22° … sans accord préalable du maire ;
> 23° … des logements appartenant à des personnes privées et vacants, sans accord préalable du maire ni durée minimale de vacance ;

Ajouter la transition prévue par l'annexe à R422-6 : les demandes pendantes deviennent sans objet, les actes et mandats antérieurs sont préservés. Réserve : R422-4, visé par le 16°, n'a pas été lu.

**RT-07 — Annexe V à D353-127 :**

> Sous réserve, le cas échéant, de l'autorisation de changement d'usage requise par les articles L. 631-7 et suivants, le bailleur s'engage à ne pas faire obstacle à une utilisation des logements en partie à usage professionnel, dans la mesure où le locataire satisfait aux conditions d'occupation et de peuplement. Dans les conventions conclues avant l'entrée en vigueur de la présente réforme, la référence à l'article R. 631-4 s'entend de cette autorisation, lorsqu'elle est requise.

**RT-08 à RT-13** : textes complets ou substitutions exactes dans le champ `minimal_correction` du JSON. Pour RT-09, le choix de la durée relève de l'auteur.

## 5. Incertitudes et éléments non examinés

- **Hors paquet, non qualifiés :**
  - divergence entre L421-7 proposé, qui supprime les autorisations préfectorales des OPH, et R421-1 proposé, qui les conserve ;
  - avis des finances publiques au 18° de l'annexe à R422-6.
- **Textes non relus :** L183-14, R441-28, R422-4, L201-9, L202-2, L631-7-2 et L631-7-3, D823-16, R441-5, R445-5-3 à R445-5-5.
- **Calibrage :** la valeur de Tdelta hors FNAL et le traitement de l'année de bascule relèvent d'une décision réglementaire.
- **Ordonnances 2025-1091 et 2026-647 :** seuls leurs NOTA ont été lus.
- **Versions différées :** les décomptes (62 au CCH, 178 au CSS) ne sont pas qualifiés un à un. Les paquets FUT-* les traitent.
- **Lectures ciblées :** elles ne certifient pas l'absence d'autres défauts.
- **Portée :** aucune cohérence exhaustive des neuf recueils n'est affirmée.

## 6. Périmètre réellement lu

Le tableau des 54 clusters est dans `reports/p1-work/P1-CCH-perimeter.md`. Chaque ligne de `P1-CCH-classification.jsonl` donne aussi le texte qui renvoie et la cible, avec leurs identifiants LEGIARTI.

Versions lues en plus :
- CCH L621-6 LEGIARTI000052846041 (2029) ;
- CCH L861-2 LEGIARTI000054475016 (2028) ;
- CSS L241-13 LEGIARTI000054466849 (2028) ;
- CCH L445-1 LEGIARTI000045211763 ;
- CCH R445-5-2 LEGIARTI000034684907 ;
- CCH R441-19 LEGIARTI000006900283 (1978-1986).
