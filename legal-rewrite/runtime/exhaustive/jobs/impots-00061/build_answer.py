import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
analyses = {}

def retain(number, reason, review, assessment, limitations, burdens, benefit):
    analyses[number] = dict(
        proposed_xml=None,
        reason=reason,
        review_notes=review,
        status='retained_unchanged',
        classification='retained_necessary',
        benefit_review=benefit,
        substantive_impact=dict(
            version=1,
            classification='retained_necessary',
            assessment=assessment,
            scope_limitations=limitations,
            new_burdens_review=burdens,
            effects=[],
        ),
    )

retain('223 WL',
    "Maintien intégral nécessaire, sans réécriture stylistique. Les deux formes de fusion et la scission définissent le périmètre des tests de chiffre d'affaires des trois articles suivants. Les retirer désorganiserait le seuil du minimum mondial, expressément conservé par is_distribution, sans supprimer une autorisation ou un dépôt autonome. L'examen n'identifie dans cet article ni prélèvement accessoire ni justificatif redondant détachable de cette fonction.",
    "Renvois contrôlés dans les sources : 223 WL bis vise le a du 1°, 223 WL ter le b du 1°, 223 WL quater les scissions. Les qualifications restent propres au chapitre II bis et ne qualifient pas par elles-mêmes une distribution pour l'IS ordinaire. Note source : exercices ouverts à compter du 31 décembre 2023, sans nouvelle date de réforme.",
    "Les définitions de fusion sous contrôle commun et de scission hors consolidation commune restent identiques à la source officielle entière ; aucune réduction de taxe ou de formalité n'est revendiquée.",
    "Maintien limité au minimum mondial et à ses restructurations ; aucun effet budgétaire ou solde de complexité des codes n'est établi par cet article de définition.",
    "Aucune charge nouvelle n'est identifiée : aucun dépôt, agrément, registre, donnée ou délai n'est ajouté aux définitions existantes.",
    "L'article n'accorde pas directement une exonération ; ses définitions bornent cependant les tests d'entrée dans le minimum mondial. Les deux cas de fusion et la scission restent intégralement applicables aux opérations futures, sans extension de leur champ.")

retain('223 WL bis',
    "Maintien nécessaire du test d'agrégation des chiffres d'affaires des groupes fusionnés. Le montant de 750 millions d'euros et la fenêtre des quatre exercices participent au champ du minimum mondial conservé, et non au taux de l'IS ordinaire. La règle utilise les états financiers existants ; elle n'institue aucun agrément de fusion, déclaration distincte ou minimum de durée que l'on puisse retirer séparément sans modifier ce champ.",
    "Contrôle de 223 WL 1° a et de 223 VL : seuil inclusif de 750 millions d'euros, règle générale d'au moins deux des quatre exercices et ajustement des exercices autres que douze mois dans l'article de champ. Le présent article ne taxe pas rétroactivement les exercices préalables : il indique le chiffre d'affaires à retenir pour le test. Note d'application au 31 décembre 2023 conservée.",
    "La somme des chiffres d'affaires antérieurs à la fusion reste utilisée pour apprécier le seuil ; aucun prélèvement ni dépôt n'est supprimé par rapport à la source officielle.",
    "L'article ne règle ni le calcul du taux effectif ni l'impôt des bénéfices conservés hors minimum mondial ; aucune économie nationale n'est déduite du maintien.",
    "Aucune charge nouvelle n'est identifiée : mêmes états financiers consolidés, même seuil et même fenêtre, sans état supplémentaire ni autorisation créée.",
    "Le seuil de 750 millions d'euros limite l'assujettissement ; il est conservé, ainsi que l'articulation au test général de 223 VL, pour les fusions futures. La règle d'agrégation n'est pas un avantage fiscal autonome à abroger.")

retain('223 WL ter',
    "Maintien intégral du test spécifique aux rapprochements impliquant une entité ou un groupe sans états financiers consolidés pour un exercice de référence. La somme des chiffres d'affaires financiers ou consolidés et le seuil de 750 millions d'euros évitent un trou de champ du minimum mondial. Il n'est pas exigé de reconstituer des comptes consolidés absents. Aucune autorisation, taxe accessoire ou pièce séparée sans fonction essentielle n'est identifiée.",
    "Renvoi au b du 1° de 223 WL vérifié ; ne pas lui substituer la fusion de plusieurs groupes du a. Conserver l'exercice considéré, les quatre exercices précédents, les deux types d'états et le seuil inclusif. Le test s'insère dans le champ de 223 VL, sans généraliser un impôt annuel ordinaire. Application historique : exercices ouverts à compter du 31 décembre 2023.",
    "Le mode de preuve du seuil par états financiers existants reste entier ; il ne constitue pas un nouvel allègement et ne subit aucune extension par la proposition.",
    "Maintien limité aux fusions visées au b du 1° et aux exercices sans comptes consolidés ; ni recette ni coût de conformité net n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : la règle conserve l'utilisation des comptes disponibles sans imposer de nouveaux comptes, attestations ou délais.",
    "L'emploi d'états financiers non consolidés lorsque la consolidation manque évite une exigence supplémentaire ; cette modalité et le seuil protecteur restent disponibles aux futures opérations satisfaisant les mêmes conditions.")

retain('223 WL quater',
    "Maintien nécessaire du dispositif de seuil après scission. Le premier exercice et les deuxième à quatrième exercices font l'objet de tests différents, qui déterminent la sortie ou l'entrée dans le minimum mondial préservé. Aucune autorisation de scission ni déclaration autonome n'est créée par cet article. Supprimer le mécanisme ou son seuil modifierait le champ international au lieu de retirer une formalité nationale détachable.",
    "Renvois à 223 VL, 223 VL bis et 223 VL ter contrôlés : champ, exclusions et option d'inclusion restent distincts. Conserver 750 millions d'euros pour le premier exercice ; aux deuxième, troisième et quatrième exercices, le test porte sur au moins deux des exercices suivant la scission, sans exclure le premier exercice suivant celle-ci ni fusionner les deux tests. La note du 31 décembre 2023 n'est pas une date de réforme proposée.",
    "Le texte source entier est maintenu : seuil annuel au premier exercice et test d'au moins deux exercices aux deuxième, troisième et quatrième exercices. Aucun allègement supplémentaire n'est compté.",
    "La règle concerne seulement les groupes issus d'une scission entrant dans le périmètre cité ; aucun effet sur les autres entreprises ou sur le solde public global n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : mêmes périodes et seuils, aucun nouveau dossier de scission, registre ou justificatif ajouté.",
    "Les seuils et le test pluriannuel sont des limites de l'assujettissement qui restent entiers pour les scissions futures. L'article ne contient pas une exonération SRU ni un droit de succession et n'est pas abrogé sur ces fondements.")

retain('223 WM',
    "Maintien intégral des sept règles d'entrée et de sortie du groupe, nécessaires au minimum mondial. Les comptes consolidés bornent les résultats et impôts de l'exercice d'acquisition ; les valeurs antérieures, les déductions de substance et les impôts différés sont suivis sans rupture artificielle. Le cinquième exercice et l'exception propre à la perte qualifiée font partie du mécanisme conservé. L'article ne prévoit ni autorisation d'acquisition, ni déclaration séparée, ni pièce redondante détachable.",
    "Lecture complète des sept points et de la note 2026 : rédaction issue de la loi n° 2026-103, applicable aux exercices ouverts à compter du 31 décembre 2023. Vérifiés : 223 WA et suivants pour la substance, 223 VV à 223 VV quinquies pour la perte qualifiée nette, et III de 223 VU sexies dans sa rédaction 2026 pour la régularisation. Le point 6 déroge expressément au calendrier de ce III ; conserver la reprise chez le cédant, la naissance chez l'acquéreur et le cinquième exercice suivant l'acquisition. Le minimum reste distinct de l'IS à la distribution ; pas de crédit fictif ni de report estonien automatique.",
    "Le rattachement à la seule période consolidée, la continuité des valeurs et le traitement des impôts différés restent identiques à la source officielle entière ; aucune baisse ou suppression nouvelle n'est revendiquée.",
    "Les effets dépendent des comptes, impôts couverts et opérations réels des groupes dans le champ du minimum mondial. Le maintien ne prouve ni neutralité globale avec l'IS réformé ni absence de minimum sur bénéfices conservés.",
    "Aucune charge nouvelle n'est identifiée : le suivi comptable, les proratas et la régularisation au cinquième exercice sont ceux de la source ; aucun registre, dépôt ou agrément supplémentaire n'est introduit.",
    "Sont conservés pour les acquisitions futures : limitation des résultats et impôts à ceux intégrés aux comptes consolidés au point 1 ; continuité des valeurs au point 2 ; déductions de personnel et d'actifs avec leur prorata aux points 3 et 4 ; continuité des actifs et passifs d'impôts différés au point 5, avec l'exception propre à la perte qualifiée nette ; délai particulier de régularisation du point 6. Le point 7 répartit l'inclusion entre groupes et n'est pas une exonération autonome. Aucun de ces mécanismes n'est réservé aux opérations anciennes ni transformé en double crédit.")

retain('223 WN',
    "Maintien intégral des cinq définitions qui rendent opératoires les transferts d'actifs et de passifs du minimum mondial. Les conditions cumulatives du 1° permettent notamment la neutralité des réorganisations ; son exception au a évite d'exiger une émission sans importance économique. Le plafond du 2° borne la plus ou moins-value non éligible. Aucun agrément de réorganisation ni déclaration supplémentaire n'est prescrit ; supprimer ces limites risquerait de retirer un avantage ou de rompre les règles conservées.",
    "Vérifiés dans le lot : 223 WN bis, ter, quater et quinquies pour la règle générale, la continuité, la fraction imposable et l'option de juste valeur. L'article 223 WM bis nécessite une coordination expresse : sa référence au seul 1° est remplacée dans sa propre proposition par le champ de la sous-section, sans modifier les présentes définitions. Conserver les lettres a à c, l'exception du a, le minimum de deux montants au 2° et les 3° à 5°. Note historique du 31 décembre 2023 maintenue.",
    "Les définitions et conditions de neutralité restent intégralement celles de la source ; aucune suppression de régime, taxe ou formalité n'est attribuée à ce maintien.",
    "Ces définitions ne dispensent pas d'une taxation étrangère et ne règlent pas l'IS ordinaire de la société ; aucun rendement ni coût net global n'est établi.",
    "Aucune charge nouvelle n'est identifiée : les qualifications, leurs conditions cumulatives et les valeurs comparées sont conservées sans agrément, attestation ou déclaration de remplacement.",
    "La réorganisation éligible ouvre les règles de neutralité de 223 WN ter ; l'exception à l'émission économiquement inutile et la limitation de la plus ou moins-value non éligible au plus faible des deux montants sont conservées pour les opérations futures aussi. Les définitions de l'événement et des parties restent leurs supports.")

retain('223 WN bis',
    "Maintien de la règle générale de calcul du résultat qualifié lors d'un transfert. La prise en compte symétrique d'une plus ou moins-value chez le cédant et de la valeur d'acquisition chez le cessionnaire est nécessaire au minimum mondial conservé. Les dérogations favorables de 223 WN ter et quater restent applicables. Le texte ne comporte pas de dépôt, agrément ou minimum de délai que l'on puisse supprimer séparément.",
    "Contrôle des articles 223 WN, 223 WN ter et quater : la règle générale n'écarte pas la neutralité des réorganisations ni sa limitation aux fractions non éligibles. Ne pas assimiler toute cession ou sortie de trésorerie à une distribution au titre de l'IS ordinaire. La norme comptable reste celle des états consolidés de l'entité mère ultime ; application source au 31 décembre 2023.",
    "La règle de réalisation chez le cédant et de valeur d'acquisition chez le cessionnaire reste inchangée par rapport à la source entière ; aucun gain fiscal nouveau n'est annoncé.",
    "Le maintien ne calcule pas le taux effectif de chaque groupe ni les effets de ses valeurs comptables ; la fiscalité étrangère et l'IS ordinaire restent distincts.",
    "Aucune charge nouvelle n'est identifiée : mêmes écritures et même norme de consolidation, sans nouvelle déclaration ni condition d'accès à une dérogation.",
    "La prise en compte des moins-values et de la valeur d'acquisition n'est pas supprimée. Les dérogations explicites de 223 WN ter et quater demeurent ouvertes aux réorganisations futures ; le présent maintien ne les neutralise pas.")

retain('223 WN ter',
    "Maintien intégral nécessaire de la neutralité des réorganisations. Exclure la plus ou moins-value chez le cédant et poursuivre les valeurs comptables chez le cessionnaire évite d'imposer un gain purement lié à une restructuration éligible. Cette dérogation favorable ne doit pas disparaître tant que le minimum mondial subsiste. Aucun agrément ou dépôt séparé n'est imposé ici ; la suppression des conditions de définition n'est pas nécessaire à son fonctionnement.",
    "Renvoi à 223 WN bis vérifié, ainsi que conditions cumulatives de 223 WN 1° et dérogation particulière de 223 WN quater. Conserver l'exclusion des moins-values autant que des plus-values et la valeur comptable du cédant, sans substituer une valeur fiscale ou une juste valeur. Les opérations futures éligibles restent couvertes ; note historique au 31 décembre 2023.",
    "L'exclusion du résultat du cédant et la continuité de valeur chez le cessionnaire sont préservées intégralement ; il s'agit d'une neutralité existante, sans réduction nouvelle comptée.",
    "Maintien limité aux réorganisations définies et sous réserve des fractions non éligibles ; aucune exonération de tous impôts ni économie nationale chiffrée n'est établie.",
    "Aucune charge nouvelle n'est identifiée : mêmes conditions de réorganisation, aucun agrément, justificatif périodique ou suivi distinct ajouté par la proposition.",
    "L'avantage possible est l'exclusion de la plus-value de réorganisation du résultat qualifié du cédant, avec continuité des valeurs comptables chez le cessionnaire. Il reste entier pour les opérations futures répondant à 223 WN ; l'exclusion corrélative des pertes et la règle spéciale de 223 WN quater conservent leur champ, sans réserver la neutralité aux dossiers déjà engagés.")

retain('223 WN quater',
    "Maintien intégral de la neutralité partielle des réorganisations comportant une plus ou moins-value non éligible. L'inclusion chez le cédant reste plafonnée à cette fraction et la valeur chez le cessionnaire reçoit l'ajustement correspondant. Retirer l'article pourrait imposer le gain intégral ou perdre l'ajustement protecteur. Il ne contient pas de formalité autonome ou d'autorisation inutile ; son calcul sert le minimum mondial conservé.",
    "Renvois à 223 WN bis et ter vérifiés. La définition du 2° de 223 WN retient le plus faible des deux montants ; ne pas lui substituer la totalité du gain comptable ni supprimer les moins-values. L'ajustement suit les règles fiscales nationales du cessionnaire, sans exiger une autorisation française. Application source aux exercices ouverts à compter du 31 décembre 2023.",
    "La limitation à la fraction non éligible et l'ajustement des valeurs acquis restent identiques à la source officielle entière ; aucun allègement nouveau n'est revendiqué.",
    "La règle ne supprime pas l'imposition de la fraction non éligible et dépend des règles locales du cessionnaire ; ni effet budgétaire agrégé ni neutralité fiscale universelle n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : les deux calculs et leurs conditions sont maintenus, sans nouvel agrément, registre ou justificatif obligatoire.",
    "L'avantage est la neutralité conservée sur la fraction éligible du transfert, l'inclusion du résultat du cédant étant limitée à la plus ou moins-value non éligible. La reprise des valeurs ajustées chez le cessionnaire évite une discordance de bases. Ces deux protections restent applicables à toute future réorganisation recevable et ne sont pas limitées aux droits acquis avant réforme.")

retain('223 WN quinquies',
    "Maintien intégral de l'option d'alignement sur la juste valeur fiscale et de ses deux modalités de prise en compte. L'option est une faculté du déclarant, non un agrément français à supprimer ; l'imposition immédiate et l'étalement sur cinq exercices doivent tous deux rester ouverts. Les trois points, l'ajustement des fractions non éligibles et la reprise du reliquat à la sortie assurent la cohérence du minimum mondial sans déclaration séparée prévue ici.",
    "Vérifiés : définitions d'événement déclencheur et de fraction non éligible dans 223 WN, ainsi que la place de l'option à la suite des règles de transfert. Conserver au 3° b un cinquième dans l'exercice de l'événement et chacun des quatre suivants, puis tout le reliquat à l'exercice de sortie. Ce calendrier existant ne reporte pas l'IS ordinaire réformé et n'est pas une baisse de taux. Note du 31 décembre 2023 maintenue.",
    "L'option de juste valeur et l'étalement déjà présents dans la source restent entiers ; aucune nouvelle baisse ni nouvelle amélioration de calendrier n'est comptée.",
    "L'étalement ne s'applique qu'aux ajustements fiscaux visés et ne supprime pas la dette finale ; aucune économie nationale ni incidence chiffrée sur chaque groupe n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : la faculté et ses calculs sont ceux de la source, sans nouveau dossier, visa ou délai imposé en remplacement.",
    "L'option peut préserver l'alignement des bases et l'étalement en cinq fractions offre un avantage de trésorerie existant. Les deux voies, l'ajustement des fractions non éligibles et leur accès pour les événements futurs restent intégralement maintenus ; la sortie du groupe conserve la taxation du reliquat, sans nouveau taux ni remboursement fictif.")

retain('223 WO',
    "Maintien intégral de la définition des coentreprises, de ses cinq exclusions et de la définition de leurs filiales. Le seuil d'au moins 50 %, la mise en équivalence et la consolidation des filiales distinguent le sous-groupe soumis au minimum mondial. Ces limites et exclusions évitent des extensions indues ; les supprimer sous couvert de simplification retirerait des protections. Aucun agrément, dépôt distinct ou justificatif périodique n'est prévu dans cette définition.",
    "Vérifiés : 223 VL bis pour les entités exclues, 223 VO bis 2° et 3° pour dividendes et participations exclus, et 223 WO bis à quater pour calcul et attribution. Conserver les trois branches alternatives du c, les exclusions a à e, les deux branches du 2° et les établissements stables. Maladresse source du d ('une entité d'un groupe d'entreprises multinationales ou un groupe national') signalée sans tirer d'extension de champ de cette syntaxe. Note du 31 décembre 2023 conservée.",
    "Les exclusions, le seuil de participation et la définition des filiales restent entiers ; aucune réduction nouvelle de taxe ou d'obligation n'est attribuée à cette définition maintenue.",
    "La portée exacte de la maladresse syntaxique du d n'est pas tranchée par une modification silencieuse ; le maintien ne prétend pas établir une économie ni un audit global du minimum mondial.",
    "Aucune charge nouvelle n'est identifiée : aucune consolidation, certification, déclaration ou donnée supplémentaire n'est exigée au-delà de la définition source.",
    "Restent exclus les mères ultimes soumises à l'inclusion qualifiée, les entités exclues, les entités détenues directement par ces dernières remplissant l'une des trois conditions du c, les entités de groupes exclusivement exclus et les filiales déjà traitées comme telles. Le seuil de 50 % et les critères de filiale restent inchangés. Toutes ces limites et exclusions bénéficient aussi aux situations futures éligibles.")

retain('223 WO bis',
    "Maintien nécessaire de l'attribution à l'entité mère de sa part d'impôt complémentaire au titre d'une coentreprise ou de sa filiale. L'impôt relève du minimum mondial expressément conservé et non d'une contribution additionnelle à l'IS ordinaire. L'article ne crée aucun agrément, dépôt ni justificatif autonome. Sa suppression isolée désarticulerait l'inclusion du revenu et la déduction anti-cumul de 223 WO quater.",
    "Sous-section 2 de la section V contrôlée, notamment 223 WG, 223 WH, 223 WH ter et 223 WI : redevable, part attribuable et réductions anti-cascade. Articuler avec les définitions de 223 WO et le calcul séparé de 223 WO ter ; la coordination expresse de 223 WO quater ne modifie pas la part due ici. Le maintien ne rétablit pas un IS annuel ordinaire. Note historique du 31 décembre 2023 conservée.",
    "L'inclusion de la seule part attribuable à la mère reste celle de la source entière ; aucun prélèvement supprimé ou nouveau ne résulte de ce maintien.",
    "Le montant effectif dépend des participations et des règles du minimum mondial ; aucune baisse de charge fiscale nationale ou internationale n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : même part d'impôt et mêmes règles d'inclusion, sans dépôt ou formalité supplémentaire ajouté.",
    "La limitation à la part de la coentreprise ou de sa filiale et les mécanismes anti-cascade de la sous-section visée restent applicables. Ils ne constituent pas une exonération totale ; aucun droit favorable futur n'est fermé.")

retain('223 WO ter',
    "Maintien intégral du calcul de la coentreprise et de ses filiales comme sous-groupe distinct. Cette séparation fournit la base nécessaire au minimum mondial et évite de mélanger les résultats et impôts de plusieurs ensembles. Les sections citées conservent leurs déductions et régimes favorables. Aucun nouvel état distinct ni agrément n'est exigé par cet article, qui ne peut être supprimé sans rendre le calcul et ses neutralités incohérents.",
    "Les sections III, IV et VII portent respectivement le taux effectif, la liquidation et les dispositions particulières ; la section VI contient les restructurations. 223 WO définit les membres, 223 WO bis attribue la part et 223 WO quater déduit les parts déjà attribuées. Le renvoi erroné de ce dernier à 223 VO ter est corrigé dans sa proposition au profit du présent calcul. Note d'application au 31 décembre 2023 maintenue.",
    "Le calcul séparé, les quatre ensembles de règles et la coentreprise comme mère ultime restent inchangés ; aucune fusion de régimes ni économie nouvelle n'est annoncée.",
    "Le calcul reste annuel au seul titre du minimum mondial ; ni conformité globale de l'IS français nouveau ni effet financier agrégé n'est démontré par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : mêmes règles de calcul et de sous-groupe, sans nouveau relevé, registre ou attestation imposé.",
    "La séparation du sous-groupe conserve l'application des déductions, neutralités et régimes particuliers des sections citées aux coentreprises et filiales futures. Aucun avantage n'est limité au seul stock ancien ; le texte ne crée pas d'exonération générale nouvelle.")

retain('223 WP',
    "Maintien intégral des définitions du groupe à mères multiples, du jumelage et de la double cotation. Les conditions de titres, de convention et de comptes consolidés identifient une unité économique pour le minimum mondial conservé. La certification n'est pas un nouvel agrément fiscal : elle qualifie les comptes consolidés servant au régime. Aucune déclaration supplémentaire ou délai minimal détachable n'est identifié ; modifier les définitions seules risquerait de modifier le champ plutôt que d'alléger une démarche.",
    "Contrôlés 223 WP bis à septies, ainsi que 223 VK 22°, 26° et 28°. Préserver le seuil d'au moins 50 % des titres au 2° a et les cinq conditions cumulatives du 3°. Incohérence préexistante signalée : le 1° nomme les groupes nationaux tout en exigeant un élément situé dans un autre Etat ou territoire, alors que 223 VK 28° situe toutes leurs entités constitutives en France. Aucune extension aux ensembles purement domestiques n'est inventée pour résoudre cette tension de champ ; elle appelle une confrontation spécifique à la transposition européenne. Note historique du 31 décembre 2023 maintenue.",
    "Les définitions et conditions source restent intégrales, y compris la condition internationale ; aucune réduction de formalités, taux ou base n'est revendiquée.",
    "La tension entre groupe national et condition internationale du 1° reste explicitement signalée, sans élargissement silencieux de l'impôt. Le texte européen intégral n'est pas joint au lot ; aucune concordance exhaustive n'est prétendue.",
    "Aucune charge nouvelle n'est identifiée : les conventions et états certifiés sont les critères existants, sans nouveau visa fiscal, registre ni délai ajouté.",
    "Le rattachement commun peut éviter des traitements discordants, mais n'est pas une exonération autonome. Les critères bornant ce rattachement, dont 50 % au moins pour les titres jumelés et la négociation indépendante des titres en double cotation, restent entiers pour les structures futures répondant à la source.")

retain('223 WP bis',
    "Maintien intégral du rattachement à un groupe unique des ensembles à mères multiples et de la qualification de leurs entités constitutives. L'exclusion expresse de 223 VL bis protège les catégories favorables ; la consolidation ligne par ligne et la détention du contrôle évitent des trous de champ du minimum mondial. Aucun agrément ni dépôt autonome n'est exigé. Une suppression isolée ferait perdre l'unité de calcul sans démontrer une baisse nette de contrainte.",
    "Vérifiés 223 WP pour le champ des accords et 223 VL bis pour les exclusions ; 223 WP ter et quater identifient les comptes et mères, quinquies et sexies l'impôt. La tension de champ national/international relevée à 223 WP n'est pas élargie ici. Garder les deux voies alternatives du second alinéa et l'exception des entités exclues. Application historique au 31 décembre 2023 maintenue.",
    "Le groupe unique et l'exclusion des entités protégées restent identiques à la source officielle ; aucune nouvelle fusion normative ou réduction d'obligation n'est comptée.",
    "Maintien limité aux structures répondant à 223 WP, avec sa difficulté de champ signalée ; ni solde national de complexité ni baisse fiscale n'est établi.",
    "Aucune charge nouvelle n'est identifiée : mêmes critères de consolidation ou de contrôle, sans nouveau dépôt ou justificatif ajouté.",
    "L'exception pour toute entité exclue par 223 VL bis est conservée sans restriction, y compris dans les structures futures. L'unité de groupe existante est maintenue et ne devient pas une nouvelle condition d'accès aux exclusions.")

retain('223 WP ter',
    "Maintien nécessaire de la règle identifiant les comptes du groupe à mères multiples et la norme réputée être celle de la mère ultime. Les comptes sont ceux des accords déjà définis, sans seconde série obligatoire instituée ici. Cette articulation sert le calcul du minimum mondial et évite une indétermination comptable ; aucun agrément, déclaration ou délai autonome à supprimer n'est relevé.",
    "Renvois contrôlés aux 2° et 3° de 223 WP : états de jumelage et de double cotation. La qualification de la norme est propre au chapitre, dans le cadre des définitions de 223 VK. Ne pas imposer des comptes consolidés additionnels à ceux désignés. La difficulté de champ du 1° de 223 WP reste signalée dans sa notice ; note d'application au 31 décembre 2023 maintenue.",
    "La référence aux comptes existants et la norme de la mère ultime restent celles de la source entière ; aucune obligation de comptes supprimée ou fusionnée n'est revendiquée.",
    "Le maintien ne tranche pas toutes les situations comptables étrangères et ne démontre ni coût net de conformité ni effet de recette.",
    "Aucune charge nouvelle n'est identifiée : pas de seconde consolidation, nouvelle certification, donnée ou déclaration ajoutée au texte source.",
    "La désignation d'une même référence comptable évite une divergence de normes mais ne constitue pas une exonération directe. Cette règle demeure entière pour les futurs groupes éligibles et ne ferme aucun des régimes particuliers du chapitre.")

retain('223 WP quater',
    "Maintien intégral nécessaire de l'identification des entités mères du groupe à mères multiples. Le texte distribue une qualité juridique entre les mères ultimes existantes ; il ne prescrit aucune autorisation ni transmission. Sa suppression rendrait incertains les redevables et la faculté déclarative commune des articles suivants, sans retirer une charge autonome.",
    "Vérifiés 223 WP, 223 WP quinquies, sexies et septies : distinguer les mères redevables au titre de l'inclusion, les entités constitutives et la déclaration d'informations. Ne pas transformer l'identification en responsabilité solidaire générale ni en nouveau groupe d'IS ordinaire. Note d'application au 31 décembre 2023 conservée.",
    "L'identité des mères reste celle de la source officielle entière ; aucun transfert d'impôt, fusion de formalités ou nouvel allègement ne résulte du maintien.",
    "La disposition ne fixe ni montant ni clé de partage de l'impôt ; les difficultés de champ relevées à 223 WP et le calcul réel des groupes restent distincts.",
    "Aucune charge nouvelle n'est identifiée : même qualification des mères ultimes, sans registre, désignation administrative ou délai supplémentaire.",
    "Aucun avantage fiscal autonome n'est supprimé : l'identification des mères préserve l'articulation des règles de partage et de déclaration unique pour les groupes éligibles futurs, sans ajouter de solidarité fiscale.")

retain('223 WP quinquies',
    "Maintien nécessaire de la qualité de redevable des mères multiples au titre de la règle d'inclusion du revenu. Ce prélèvement relève du minimum mondial maintenu, non des contributions additionnelles à l'IS ordinaire dont la suppression est décidée. Le texte limite l'impôt à la part due au titre des entités faiblement imposées et renvoie au régime comportant ses mécanismes anti-cascade. Aucune formalité autonome détachable n'est prévue.",
    "Sous-section 2 de la section V contrôlée : 223 WG, WH, WH bis, WH ter et WI pour redevables, part attribuable et réductions. Vérifier les qualités de mère dans 223 WP quater et la définition de 223 WP sans extension implicite. Le maintien de l'inclusion annuelle du minimum ne rétablit pas l'annualité de l'IS ordinaire. Note source du 31 décembre 2023 maintenue.",
    "La même part d'impôt complémentaire reste due selon l'inclusion du revenu ; aucune taxe retirée ou nouvelle réduction de taux n'est attribuée à ce maintien.",
    "La dette dépend du calcul du minimum et des parts attribuables ; le maintien ne démontre ni zéro impôt sur les réserves des grands groupes ni rendement budgétaire.",
    "Aucune charge nouvelle n'est identifiée : même redevable, même part et mêmes règles, sans nouvelle déclaration ou garantie ajoutée.",
    "La limitation à la part d'impôt et les réductions anti-cascade de la sous-section visée demeurent applicables aux situations futures. Il ne s'agit pas d'un droit successoral ou d'une surtaxe de l'IS ordinaire supprimable sur ces seuls fondements.")

retain('223 WP sexies',
    "Maintien de la règle de redevabilité au titre des bénéfices insuffisamment imposés, composante distincte du minimum mondial expressément conservé. Elle ne peut être retirée comme une contribution additionnelle au nouvel IS. La sous-section visée contient déjà les calculs de répartition et exclusions de cumul. L'article n'ajoute ni déclaration particulière, ni agrément, ni condition documentaire inutile.",
    "Contrôlé 223 WK, spécialement le II qui annule ou réduit le complément lorsque l'inclusion qualifiée s'applique déjà, et identification des entités par 223 WP bis. Les notes des règles de collecte distinguent l'application ordinaire aux exercices ouverts à compter du 31 décembre 2024 et le cas anticipé prévu par la loi ; la note générale du présent article au 31 décembre 2023 ne suffit pas à avancer indistinctement ces règles. Aucun nouveau calendrier n'est créé.",
    "La redevabilité au titre du minimum sur bénéfices insuffisamment imposés reste entière, avec les règles visées ; aucune suppression ni augmentation d'impôt nouvelle n'est comptée.",
    "Le maintien ne chiffre pas les parts françaises ou étrangères, et ne préjuge pas l'application des exceptions de collecte ni le solde budgétaire de l'IS à la distribution.",
    "Aucune charge nouvelle n'est identifiée : aucune nouvelle donnée, sûreté, déclaration ou échéance n'est ajoutée à la redevabilité source.",
    "Les limitations anti-cumul et les exceptions de la sous-section de collecte restent entières, notamment le II de 223 WK. Elles continuent à s'appliquer aux exercices futurs éligibles ; le maintien ne crée pas un complément sur une part déjà exclue par ces règles.")

retain('223 WP septies',
    "Maintien nécessaire de la déclaration d'informations du groupe à mères multiples avec la faculté existante de déclarant unique. L'examen des doublons conduit à conserver cette dispense, déjà prévue par la source, plutôt qu'à présenter son simple rappel comme une nouvelle fusion. Le dépôt fournit les données du minimum mondial conservé ; il n'est ni un agrément préalable ni une déclaration d'IS ordinaire sur les bénéfices conservés. Aucun second rapport spécifique n'est ajouté.",
    "Lecture de 223 WW II et de 223 WW bis : déclaration d'informations, délai de quinze mois ou dix-huit mois au premier exercice ; dispense si dépôt par entité française désignée par toutes les entités françaises avec information de l'administration, ou par mère/déclarante dans un Etat ou territoire doté de l'accord d'échange requis. Le relevé de liquidation de 223 WW III est distinct et n'est pas abrogé indirectement. Supprimer sans remplacement la déclaration du minimum n'est pas décidé par is_distribution. Les conditions de la dispense ne sont ni renforcées ni réputées remplies.",
    "Le dépôt des informations de tous les groupes et la dispense par déclarant unique sont déjà dans la source entière et restent inchangés ; aucun doublon nouvellement supprimé n'est revendiqué.",
    "Le maintien ne règle pas les formulaires ou les échanges internationaux et ne démontre pas que toutes les mères sont dispensées dans chaque Etat ; aucune économie globale n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucune déclaration de remplacement, désignation obligatoire, échéance ou nouvelle catégorie de données n'est introduite.",
    "L'option de déclarant unique constitue une dispense de dépôts multiples déjà acquise. Elle reste ouverte aux futurs groupes satisfaisant 223 WW bis, avec les dépôts français ou étrangers éligibles et sans attestation nouvelle ; elle n'est pas confinée aux groupes existant avant réforme.")

retain('223 WQ',
    "Maintien intégral nécessaire du champ des neutralités des mères ultimes interposées. Les trois catégories incluent la mère, son établissement stable et celui d'une entité transparente détenue directement ou par une chaîne transparente. Supprimer ce support ferait perdre les réductions de bénéfice qualifié de 223 WQ bis, alors que le minimum mondial subsiste. Il n'existe ici ni autorisation ni dépôt supplémentaire détachable.",
    "Vérifiés 223 VK 14° pour l'entité interposée et la transparence, et 223 WQ bis pour les réductions. Ne pas assimiler toute société soumise au nouvel IS à une entité interposée ; le régime de distribution éligible du 39° de 223 VK impose notamment l'antériorité au 1er juillet 2021. Les établissements et chaînes visés restent couverts pour l'avenir. Note source du 31 décembre 2023 maintenue.",
    "Les trois catégories de bénéficiaires restent intégralement celles de la source ; aucune nouvelle exonération ni réduction de formalité n'est comptée.",
    "Le maintien concerne les seules entités interposées et établissements définis, et ne prouve pas que le nouvel IS français entre dans une dérogation internationale de distribution.",
    "Aucune charge nouvelle n'est identifiée : les mêmes critères de participation et de transparence subsistent sans nouvel agrément, justificatif ou délai.",
    "Cet article est le fondement du champ favorable de 223 WQ bis. Les trois voies d'accès, dont la détention indirecte par une chaîne d'entités transparentes, sont intégralement maintenues pour les situations futures recevables, sans fermeture ni condition supplémentaire.")

retain('223 WQ bis',
    "Maintien intégral des quatre paragraphes du régime de neutralité des mères ultimes interposées. Les deux voies du I et les deux catégories du II réduisent le bénéfice qualifié pour éviter ou limiter une double imposition ; le III coordonne les pertes utilisables par le détenteur et le IV les impôts couverts. Les conditions de période, de résidence et de participation sont constitutives du régime du minimum mondial préservé, non des formalités redondantes. Les supprimer indistinctement pourrait retirer l'avantage ou produire un double emploi.",
    "Contrôlés le champ de 223 WQ, le taux minimum de 15 % du 45° de 223 VK et 223 VV quinquies qui vise expressément le III pour l'actif de perte qualifiée. Conserver douze mois après clôture, les alternatives de taux nominal ou d'impôts cumulés, 5 % au plus sur les droits aux bénéfices ET aux actifs, les deux conditions de résidence/établissement, l'imputabilité locale de la perte et la réduction proportionnelle du IV. La preuve prévue au I 2° n'est pas transformée en agrément ou attestation périodique. Note du 31 décembre 2023 conservée.",
    "Toutes les réductions de bénéfice, la coordination des pertes et des impôts couverts restent exactement celles de la source entière ; le maintien d'avantages existants n'est pas présenté comme une baisse nouvelle.",
    "Les conditions du régime doivent être vérifiées pour chaque détenteur ; le maintien ne garantit ni absence de double impôt de tous régimes ni accès automatique du nouvel IS français à une dérogation internationale.",
    "Aucune charge nouvelle n'est identifiée : aucune donnée, attestation, déclaration, condition de taux ou durée supplémentaire n'est ajoutée aux conditions source.",
    "Les avantages possibles sont conservés pour les futures situations éligibles : réduction de bénéfice du I en cas d'imposition du détenteur dans les douze mois et de taux nominal suffisant ou d'impôts cumulés suffisants ; réduction du II pour personnes physiques résidentes et pour entités publiques, organisations internationales, organismes sans but lucratif ou fonds de pension établis localement, avec au plus 5 % des deux catégories de droits. Le III retire corrélativement la perte seulement si elle est imputable localement ; le IV ajuste les impôts couverts pour éviter le double emploi du bénéfice exclu. Ces deux coordinations ne sont pas des exonérations autonomes à détacher ou à supprimer.")

source_by_number = {a['number']: a for a in sources}

def coordinate(number, old, new, reason, review, assessment, limitations, burdens,
               benefit, measure_id, description, before, after):
    source = source_by_number[number]['source_xml']
    assert source.count(old) == 1
    proposed = source.replace(old, new)
    analyses[number] = dict(
        proposed_xml=proposed,
        reason=reason,
        review_notes=review,
        status='rewrite_draft',
        benefit_review=benefit,
        substantive_impact=dict(
            version=1,
            classification='coordination_only',
            assessment=assessment,
            scope_limitations=limitations,
            new_burdens_review=burdens,
            effects=[dict(
                kind='coordination',
                measure_id=measure_id,
                description=description,
                before=before,
                after=after,
                unit='legal_duty',
                affected_population=(
                    "Entités faisant l'objet d'une cession de contrôle dans le champ du minimum mondial."
                    if number == '223 WM bis' else
                    "Coentreprises, leurs filiales et entités mères dans le champ du minimum mondial."
                ),
                conditions_and_transition=(
                    "Coordination applicable à compter de l'entrée en vigueur de la loi proposée ; aucune nouvelle date calendaire, modification rétroactive des impositions ou extinction des recours antérieurs n'est instituée."
                ),
                replacement_or_new_burdens="Aucune formalité, donnée, garantie ou taxe de remplacement ; les conditions et calculs maintenus restent ceux du minimum mondial.",
                source_quote=old,
                proposed_quote=new,
            )],
        ),
    )

coordinate('223 WM bis',
    "est considérée comme un transfert d'actifs et de passifs au sens du 1° de l'article 223 WN",
    "est considérée comme un transfert d'actifs et de passifs pour l'application de la sous-section 3 de la présente section",
    "Coordination nécessaire, sans baisse de taux ni suppression de prélèvement. La source renvoie au seul 1° de 223 WN, qui définit la réorganisation avec conditions de contrepartie et de non-imposition totale ou partielle, alors que l'article assimile une cession de contrôle fiscalement imposée à un transfert d'actifs et passifs. Le renvoi est rattaché à la sous-section des transferts, qui contient la règle générale et ses neutralités. Le reste du corps est intégralement conservé : contrôle, territoire pertinent, impôt couvert du cédant et différence de valeurs. Aucun agrément ni déclaration inutile n'est identifié dans ce mécanisme du minimum mondial maintenu.",
    "Incohérence préexistante expressément corrigée après lecture de 223 WN 1° a à c et de 223 WN bis à quinquies. La correction ne qualifie pas automatiquement la cession de réorganisation : les conditions de 223 WN restent à satisfaire pour appliquer 223 WN ter ou quater. Elle ne rend imposable ni un prêt professionnel ni toute cession au titre de l'IS ordinaire et ne crée aucun impôt couvert fictif lorsque le régime local n'impose pas le cédant. La note d'application historique au 31 décembre 2023 demeure ; la coordination nouvelle est prospective. Le texte intégral de la directive n'étant pas joint au lot, aucune concordance européenne exhaustive ni neutralité chiffrée de la correction n'est certifiée.",
    "Le corps intégral reste une assimilation pour le minimum mondial ; seul le renvoi ambigu à la définition d'une réorganisation est remplacé par le champ des transferts. Aucun allègement matériel n'est démontré par cette correction.",
    "L'incidence de l'ancien renvoi ambigu dans chaque dossier n'est pas chiffrée. La coordination ne dispense pas des conditions de neutralité et ne prétend pas modifier la directive ni les impôts étrangers.",
    "Aucune charge nouvelle n'est identifiée : le critère d'impôt couvert, le territoire et l'assiette décrite sont conservés, sans nouveau dépôt, calcul autonome ou agrément. L'effet d'interprétation de l'ancien renvoi reste signalé.",
    "L'assimilation au transfert peut permettre le traitement cohérent des valeurs d'actifs déjà fiscalement taxées. Elle reste ouverte pour les futures cessions répondant à la même condition d'impôt couvert. Les neutralités de 223 WN ter et quater ne sont ni supprimées ni accordées sans leurs conditions ; aucun impôt supplémentaire n'est déclaré économisé par le changement de renvoi.",
    'minimum-mondial-transferts-renvoi',
    "Rattachement de l'assimilation des cessions de contrôle à la sous-section complète des transferts, au lieu de la seule définition d'une réorganisation.",
    "Pour les acquisitions ou cessions de contrôle visées, assimilation à un transfert par renvoi au 1° de 223 WN ; aucun taux autonome fixé dans l'article.",
    "Pour les mêmes opérations et sous la même condition d'impôt couvert, assimilation pour la sous-section 3, avec conditions de réorganisation distinctement conservées ; aucun taux autonome ajouté.")

coordinate('223 WO quater',
    "pour chaque membre du groupe imposable conformément à l'article 223 VO ter",
    "pour chaque membre du groupe dont l'impôt complémentaire est calculé conformément à l'article 223 WO ter",
    "Coordination nécessaire du mécanisme anti-cumul, sans taxe supprimée ou réduction nouvelle. Le renvoi source à 223 VO ter est matériellement incohérent : cette cible traite de pleine concurrence, non du calcul de l'impôt d'un membre du groupe de coentreprise. Le nouveau corps entier rattache ce calcul à 223 WO ter, situé dans la même sous-section, et conserve la déduction des parts attribuées aux mères par 223 WO bis ainsi que l'affectation du seul reliquat à la règle des bénéfices insuffisamment imposés. Aucun dépôt ou agrément supplémentaire n'est prescrit.",
    "Erreur de renvoi préexistante signalée, non corrigée silencieusement : lecture de 223 VO ter (transactions et pleine concurrence), 223 WO ter (calcul séparé de la coentreprise et de ses filiales), 223 WO bis (part de la mère) et du II de 223 WK (complément résiduel). Tous les autres termes des deux alinéas sont conservés. La portée anti-cumul est maintenue pour les situations futures, sans crédit remboursable ni double déduction. La note d'application historique au 31 décembre 2023 reste distincte de l'entrée en vigueur prospective de la coordination ; les règles temporelles autonomes de collecte ne sont pas avancées.",
    "La correction rend le renvoi opérant pour le calcul des coentreprises ; le même mécanisme de déduction et de reliquat subsiste. Aucun nouvel allègement chiffré ni seconde suppression de taxe n'est revendiqué.",
    "L'incidence contentieuse de l'ancien renvoi erroné n'est pas tranchée rétroactivement et aucun montant de double imposition effectivement subi n'est établi ; le solde global de complexité reste inconnu.",
    "Aucune charge nouvelle n'est identifiée : seul le renvoi de calcul est corrigé, sans nouvelle déclaration, condition, donnée ou délai et sans modification des parts déduites ou du reliquat.",
    "L'avantage anti-cumul demeure : les parts attribuables aux mères au titre de 223 WO bis sont déduites du complément du groupe, seule la différence restant dans la règle des bénéfices insuffisamment imposés. Le renvoi au calcul de 223 WO ter rend cette articulation opérante pour les coentreprises futures également ; aucune nouvelle imputation ou restitution n'est créée.",
    'minimum-mondial-coentreprises-renvoi',
    "Correction du renvoi de pleine concurrence en renvoi au calcul de l'impôt complémentaire du sous-groupe de coentreprises.",
    "Pour chaque membre du groupe de coentreprise, la déduction des parts attribuées aux mères renvoie à tort à 223 VO ter ; le reliquat relève du II de 223 WK, sans taux autonome dans l'article.",
    "Pour les mêmes membres et parts, le calcul est identifié par 223 WO ter ; la déduction et le seul reliquat relevant du II de 223 WK sont conservés, sans taux ni assiette nouveaux.")

# The entry-into-force clauses are part of the full normative bodies.
analyses['223 WM bis']['proposed_xml'] = analyses['223 WM bis']['proposed_xml'].rstrip() + (
    "\n<p>Les dispositions du présent article, dans leur rédaction issue de la loi prévoyant le renvoi à la sous-section 3 de la présente section, s'appliquent aux acquisitions ou cessions réalisées à compter de l'entrée en vigueur de cette loi. Les acquisitions ou cessions antérieures demeurent régies par les dispositions antérieurement applicables, y compris pour la liquidation, le contrôle, le recouvrement, les restitutions, les prescriptions et les voies de recours.</p>\n"
)
analyses['223 WO quater']['proposed_xml'] = analyses['223 WO quater']['proposed_xml'].rstrip() + (
    "\n<p>Les dispositions du présent article, dans leur rédaction issue de la loi prévoyant le renvoi à l'article 223 WO ter, s'appliquent aux exercices ouverts à compter de l'entrée en vigueur de cette loi. Les exercices ouverts avant cette date demeurent régis par les dispositions antérieurement applicables, y compris pour la liquidation, le contrôle, le recouvrement, les restitutions, les prescriptions et les voies de recours.</p>\n"
)
analyses['223 WM bis']['substantive_impact']['effects'][0]['conditions_and_transition'] = (
    "Coordination pour les acquisitions ou cessions réalisées à compter de l'entrée en vigueur de la loi prévoyant cette rédaction ; opérations antérieures et leurs liquidations, contrôles, recouvrements, restitutions, prescriptions et recours régis par les dispositions antérieurement applicables. Aucun taux ni date calendaire nouvelle."
)
analyses['223 WO quater']['substantive_impact']['effects'][0]['conditions_and_transition'] = (
    "Coordination pour les exercices ouverts à compter de l'entrée en vigueur de la loi prévoyant cette rédaction ; exercices ouverts avant cette date et leurs liquidations, contrôles, recouvrements, restitutions, prescriptions et recours régis par les dispositions antérieurement applicables. Les calendriers propres à la collecte du minimum demeurent."
)

assert set(analyses) == {a['number'] for a in sources}
answer = []
for source in sources:
    row = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    row.update(analyses[source['number']])
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
