# PFU : édition corrigée 002

Cette édition remplace la proposition 001, qui reste conservée. La contrelecture indépendante a établi que le crédit restituable sur un ancien prélèvement libératoire d’assurance-vie pouvait être amputé par le calcul U/F et par la borne finale de la première proposition. Les premiers tests ne reproduisaient pas cette borne finale : ils étaient insuffisants pour ce cas. L’édition 002 abandonne entièrement U/F et le nouveau crédit ; elle réduit directement l’IR forfaitaire **avant** les crédits et remboursements existants.

Un seul article 200 A est proposé intégralement, avec un C dans le 1. Tous les paragraphes du projet antérieur, dont la suppression du coefficient 1,25 et l’option globale rectifiable du 2, sont conservés exactement. Les cinq autres textes du circuit restent inchangés : leurs renvois au « 1 ou 2 » du 200 A couvrent déjà le nouveau C. Aucun actif, aucune base ni site n’est modifié.

## Formule complète

Pour chaque groupe homogène de revenus soumis au forfait du 200 A, 1 B :

- **A** : IR forfaitaire usuel, après exonérations, abattements et pertes imputables, avant crédits, réductions et avances. L’intégralité des pertes et reports recevables continue de s’appliquer à cet IR.
- **B** : revenus réellement soumis au forfait, après exonérations, abattements et pertes, avec seulement deux corrections de base : les pertes de prêts du 125-00 A et la moins-value du second alinéa du III de 150-0 B quinquies effectivement imputées en IR sont réintégrées **pour le plafond seulement** lorsque L136-6 exclut leur imputation sociale. Les moins-values déductibles dans les deux assiettes restent déduites de B.
- **T** : CSG, CRDS et solidarité effectivement dus sur les seuls revenus retenus dans B, nets des restitutions et sans double compte. Les prélèvements sociaux sur une fraction exonérée ou abattue en IR restent hors plafond. Les prélèvements antérieurement payés sur les mêmes produits d’assurance-vie ne sont pris qu’une fois.
- **G = min(A, max(0, A + T − 0,20 B))**, nul si B est nul.

R est le RFR des revenus de l’année N selon les composantes du IV de 1417, calculé pour N avant cette réduction ; le capital et les réintégrations légales y restent. Nparts est le nombre de parts de cette même année. S = Nparts × limite supérieure de la tranche à 11 % du 197 applicable à N. Aucun montant fixe n’est inscrit dans la loi proposée ; 29 579 € par part est une illustration du barème capturé.

La réduction du foyer est **D = max(0, ΣG − 0,50 × max(0, R − S))**. Elle est répartie entre les groupes proportionnellement à leurs G. L’IR de chaque groupe devient A′ = A − D × G / ΣG, ou A si ΣG = 0. Il reste positif ou nul. Il n’y a pas d’arrondi intermédiaire.

Ensuite viennent les réductions et crédits existants, dans leurs limites et droits à restitution habituels, puis les acomptes. Les crédits étrangers sont limités à l’impôt français recalculé légalement opposable ; aucune taxe étrangère n’est remboursée. Les crédits restituables remboursant un prélèvement libératoire distinct hors B, dont celui du 125-0 A, s’imputent ou sont restitués intégralement selon leur propre règle. Chaque avantage et chaque avance n’est appliqué qu’une fois. Une créance non remboursable ne devient pas remboursable du fait de D.

## Contre-exemple corrigé et solde payé

Couple sous 59 158 € de RFR illustratif : intérêts PFU 5 000 €, IR usuel 640 €, prélèvements sociaux 930 €, avance IR 640 €. Par ailleurs, ancien contrat d’assurance-vie de plus de huit ans, primes antérieures au 27 septembre 2017 : 7 200 € de produits avec ancien prélèvement libératoire de 540 €, intégralement couvert par l’abattement de 9 200 €, donc crédit autonome restituable de 540 €.

En 001, U = F = 100 €, G = 570 €, mais la borne finale limitait le nouveau crédit à 100 €. Restitution d’avances 640 €, ancien PFL de 540 € restant en trésorerie : charge française des deux impôts plus PS sur les intérêts = 1 470 €. Le plafond de 1 000 € sur les intérêts n’était pas atteint.

En 002, réduction D = 570 €, IR forfaitaire recalculé = 70 €. Crédit autonome 540 € et avance 640 € sont ensuite traités une fois : restitution totale 1 110 €. Solde payé = PFL 540 + avance 640 + PS 930 − restitution 1 110 = **1 000 €**. Les prélèvements sociaux propres aux anciens produits d’assurance-vie restent distincts et inchangés ; ils ne sont pas effacés par cet exemple.

## Bases divergentes : aucune fausse promesse

La source entière de L136-6 exclut explicitement l’imputation des pertes du 125-00 A et de la moins-value de clôture de compte PME innovation du second alinéa du III de 150-0 B quinquies. Ces deux sources actuelles, leurs notes et leurs propositions antérieures sont capturées et lues intégralement dans les deux fichiers `additional-reference*.json`. Le 125-00 A assigné est LEGIARTI000046860937, valide jusqu’au 1er janvier 2027 ; la proposition ne prolonge pas son applicabilité après son abrogation différée.

Exemple : intérêts 10 000 €, perte de prêt imputable 6 000 €. L’IR reste calculé sur 4 000 €, soit 512 €. Les prélèvements sociaux restent calculés sur 10 000 €, soit 1 860 €. La base du plafond est B = 10 000 € ; D = 372 €, IR final avant autres crédits = 140 €, total = **2 000 €**. Il serait faux de promettre 20 % de la base IR de 4 000 € : les seuls prélèvements sociaux la dépassent déjà et aucune restitution sociale n’est créée. Si les pertes éteignent tout l’IR, les prélèvements sociaux seuls restent dus : un résultat déjà inférieur à 20 % du revenu de référence ne se dégrade pas.

Les moins-values mobilières ordinaires imputables dans les deux assiettes sont maintenues au net : gain 10 000 €, perte commune 6 000 €, B = 4 000 €, total plafonné à 800 €. Les pertes non imputables et reports non utilisés ne sont pas ajoutés à B. Le traitement des deux pertes sociales exclues n’est pas étendu aux autres moins-values.

Les fractions exonérées ou abattues ne rentrent jamais dans B. Assurance-vie : 5 000 € de produits, abattement 4 600 €, B = 400 €, IR 30 €, PS sur la fraction retenue 68,80 €, D = 18,80 €. Les PS de 791,20 € portant sur la fraction abattue restent hors plafond et inchangés. Même règle de séparation pour un abattement fixe sur plus-value lorsqu’il est légalement applicable, sans présumer une éligibilité au plafond : pour un gain de 510 000 € avec abattement de 500 000 €, le RFR réintègre cet abattement selon 1417 IV. Dans le scénario annuel testé, RFR = 510 000 € pour une part, la réduction est nulle ; les 10 000 € imposables supportent 3 140 € et les prélèvements sociaux sur la fraction abattue restent 93 000 €. Le total de 96 140 € n’est pas présenté comme un plafonnement à 20 %. Aucun PEA exonéré n’est rendu imposable. Les taux et abattements plus favorables, l’option globale au barème et la déduction de CSG demeurent dans leurs champs propres.

La réduction de l’IR ne peut pas, à elle seule, garantir un plafond si T excédait 20 % de B : les tests incluent ce contre-exemple arithmétique pour ne pas confondre une borne d’IR avec une restitution sociale. Les divergences concrètes identifiées ont été traitées par les règles de base ci-dessus. La CSG de 25 % sur certaines sommes d’origine indéterminée de L136-8 IV bis n’est pas un taux PFU ordinaire au 200 A, 1 B ; aucun taux fictif n’est créé pour l’inclure. Le bilan ne prétend pas avoir certifié toutes les situations fiscales de tous les contribuables.

## Crédits étrangers, barème et régimes favorables

Pour 10 000 € de revenus ordinaires, A = 1 280 €, T = 1 860 €, D = 1 140 €, A′ = 140 €. Un crédit étranger de 1 000 € conserve sa règle habituelle de plafond français : il s’impute à hauteur de 140 €, IR français final nul. Si 1 280 € d’avances ont été versés, ces 1 280 € sont restitués une fois ; l’impôt étranger de 1 000 € demeure payé à l’étranger. La charge française est 1 860 €, la charge incluant cet impôt étranger est 2 860 €. Le nouveau dispositif ne rembourse pas ce dernier.

Un crédit étranger de 50 € s’impute à hauteur de 50 € : IR final 90 €, charge française 1 950 €, charge incluant la taxe étrangère 2 000 €. Les autres crédits remboursables conservent leur excédent restituable ; les crédits non remboursables gardent leur borne et leur report éventuel selon leurs règles. La baisse du montant de crédit imputable peut provenir d’un impôt français plus faible ; elle ne crée aucune hausse de cet impôt ni modification de la règle de l’avantage.

L’option au barème reste explicite, globale, annuelle et rectifiable. Les dividendes au forfait n’obtiennent pas l’abattement de 40 % réservé au barème. Un foyer avec IR nul au barème peut conserver une charge sociale ordinaire de 18,6 %, inférieure au plafond de 20 %. Les cas d’assurance-vie à 7,5 %, les abattements de 4 600 / 9 200 €, les exonérations et les anciennes options libératoires restent disponibles pour les situations futures recevables.

## Lissage, collecte et limites

Le retrait de 0,50 € par euro de RFR remplace le saut d’un seuil sec. À base constante, perte maximale de réduction : 0,50 € par euro de RFR. Pour un euro de capital ordinaire entrant pour un euro dans le RFR, la charge croît de 0,70 € pendant la sortie puis de 0,314 € après extinction, toutes autres règles constantes. Les deux raccordements sont continus. Un retrait de 1 € produirait au contraire une pente de 1,20 € dans ce cas ; un seuil sec ferait perdre 1 140 € pour un euro supplémentaire de RFR sur B = 10 000 €.

Ces limites concernent le dispositif proposé, pas tous les impôts, prestations, changements de parts ou relations entre revenu brut et RFR. Aucun simulateur exhaustif de ménage, rendement comportemental ou garantie universelle de taux marginal inférieur à 100 % n’est revendiqué. Les tests isolés couvrent les soldes effectivement payés et plusieurs milliers de valeurs de lissage, sans appel réseau.

117 quater, 125 A, 125 D et 125-0 A gardent leurs avances, taux et dispenses fondées sur N−2. Il s’agit d’une régularisation annuelle, pas d’un débit immédiat promis à 20 %. 154 quinquies et L136-8 ne sont pas modifiés : aucune CSG n’est remboursée par cette réduction d’IR. Le PFU ordinaire 2026 est 31,4 % lorsque les assiettes coïncident ; l’assurance-vie garde notamment ses exceptions de CSG à 9,2 % et sa charge sociale de 17,2 %. Les exonérations sociales et autres particularités restent celles de leurs sources.

Le dispositif reste classé `mixed` : baisse effective d’IR, calcul de groupes et lissage supplémentaires. Aucun formulaire autonome ni inscription nouvelle n’est créé, mais l’adéquation opérationnelle de toutes les informations disponibles n’est pas certifiée, notamment pour les PS antérieurs d’assurance-vie. Coût budgétaire et coût administratif inconnus ; aucune économie nationale, compensation automatique de CFE ou promesse d’autofinancement. Une seule mesure est dédupliquée dans le bilan.

## Provenance et attribution

Les quinze sources/notes/propositions complètes sont des captures du corpus officiel DILA et de ses propositions gardées. Le taux CRDS de 0,5 % est corroboré par le résultat primaire de [l’article 19 de l’ordonnance 96-50](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000041466982/2026-05-23) ; l’ouverture distante du corps entier a renvoyé 403, réserve inchangée et sans contournement. Ce taux n’est pas recréé par le texte proposé.

[La proposition officielle de David Lisnard du 16 avril 2026](https://www.unenouvelleenergie.fr/changer-de-logiciel-fiscal/) soutient un PFU allégé et stable, mais ne donne pas le présent taux de 20 % ni ce seuil pour les petits revenus. Son taux de 20 % concerne l’IS. Taux, seuil et lissage de cette édition sont propres au projet. Le résumé public proposé est : « PFU à 20 % sur les revenus soumis au forfait pour les petits revenus, avec assiettes, exceptions et lissage détaillés », sans garantie tous placements ni tous prélèvements confondus.
