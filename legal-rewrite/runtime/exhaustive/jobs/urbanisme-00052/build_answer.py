import json
import re
from html import unescape


sources = json.load(open('source.json', encoding='utf-8'))
by_number = {a['number']: a for a in sources}
answers = {}


def retained(number, reason, review, assessment, limitations, burdens):
    source = by_number[number]
    answers[number] = {
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': None,
        'reason': reason,
        'review_notes': review,
        'status': 'retained_unchanged',
        'classification': 'retained_necessary',
        'substantive_impact': {
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': [],
        },
    }


def changed(number, xml, reason, review, classification, assessment,
            limitations, burdens, removed, effect):
    source = by_number[number]
    answers[number] = {
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': review,
        'status': 'rewrite_draft',
        'change_type': 'normative_reduction',
        'reform_policy_id': 'editorial_direction_2026_10_19',
        'removed_provisions': removed,
        'substantive_impact': {
            'version': 1,
            'classification': classification,
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': [effect],
        },
    }


retained(
    'L600-11',
    "Maintien intégral après examen des deux protections contentieuses. La première évite l'illégalité du document ou de l'opération pour des vices de concertation lorsque les modalités légalement définies ont été respectées ; la seconde protège les autorisations contre les seuls vices de la délibération de concertation ou de son exécution. Supprimer cette règle retirerait un avantage de sécurité juridique aux projets futurs sans supprimer aucune formalité. Aucun nouveau corps stylistique n'est proposé.",
    "Source entière lue, notes sources vides. L103-1 à L103-7 et L300-2 vérifiés dans le corpus public. Les allègements déjà proposés en L103-2, L103-3 et L103-5 ne privent pas ce texte de sa fonction : les modalités effectivement requises restent la référence. L'abrogation de L600-4-1 décidée dans sru_abrogation ne concerne pas cette protection distincte. La réduction du champ de R103-1 proposée dans ce lot ne rétablit pas une concertation supprimée par le présent renvoi. Ni quotas SRU ni fermeture des dérogations littorales. Aucune filiation SRU exhaustive déduite de la seule numérotation.",
    "La source officielle entière est conservée : les deux immunités relatives aux seuls vices de concertation restent ouvertes aux documents, opérations et autorisations futurs dans leur champ. Aucune nouvelle obligation retirée ni simplification comptée.",
    "Les autres causes d'illégalité et les exigences autonomes de participation subsistent. Le maintien ne valide aucune procédure particulière et ne chiffre aucun gain global de complexité.",
    "Aucune charge nouvelle identifiée : le maintien ne crée ni dossier, ni attestation de régularité, ni délai ; les modalités de concertation restent celles de leurs textes propres.",
)

retained(
    'L600-12',
    "Maintien de la règle supplétive qui identifie le document applicable après annulation ou déclaration d'illégalité. Elle prévient un vide de planification et ne commande ni nouvel agrément ni dépôt. Les réserves de L600-12-1 et L442-14 protègent les autorisations et les droits de lotissement ; leur suppression serait défavorable. Aucun retour général au droit antérieur à SRU n'est introduit.",
    "Lecture intégrale de la source et des deux articles réservés. La remise en vigueur vise le document immédiatement antérieur, non tous les documents successifs. L442-14 conserve ses deux périodes de cinq ans, leurs points de départ distincts et sa protection contre certains effets d'une annulation du document. Le présent maintien ne ressuscite pas les quotas, prélèvements ou dispositions législatives abrogés par la réforme : leur abrogation reste opposable aux documents remis en vigueur. Aucun renvoi à L600-4-1 supprimé.",
    "Aucun changement par rapport à la source : maintien de la continuité des règles de planification avec les deux réserves favorables existantes, sans compter cette continuité comme une suppression de charge.",
    "La légalité du document antérieur et les effets des abrogations législatives restent à apprécier dans chaque litige. Aucun bilan de coût national ne résulte de cette règle de conflit.",
    "Aucune charge nouvelle identifiée : aucune procédure de réapprobation, nouvelle demande de permis ou certification du document antérieur n'est ajoutée.",
)

retained(
    'L600-12-1',
    "Maintien intégral de la protection des décisions délivrées avant le prononcé juridictionnel lorsque le motif d'illégalité du document est étranger aux règles applicables au projet. Le second alinéa protège distinctement les demandeurs contre les refus de permis et oppositions fondés sur un document illégal. Retirer l'une de ces protections créerait une contrainte ou fermerait un recours favorable ; aucune formalité redondante n'est imposée ici.",
    "Les deux alinéas ont été relus : antériorité à la décision juridictionnelle, motif étranger au projet et exception impérative pour refus et oppositions sont conservés ensemble. L600-12 et L442-14 lus en entier : ne pas étendre l'immunité à un motif qui affecte les règles applicables au projet, ni à un refus ou une opposition. La protection continue de jouer pour les autorisations futures dès lors qu'elles précèdent le prononcé concerné, sans clause de stock fermant l'avantage.",
    "La source entière demeure applicable : stabilisation conditionnelle des autorisations favorables et maintien de l'annulation des refus ou oppositions dans le champ du second alinéa. Aucun allègement supplémentaire revendiqué.",
    "La qualification du motif étranger au projet reste juridictionnelle ; aucune immunité contre les illégalités propres du permis n'est créée. Le coût net des autres réformes n'est pas établi ici.",
    "Aucune charge nouvelle identifiée : le texte ne subordonne pas cette protection à une demande, à une pièce supplémentaire ou à une autorisation administrative.",
)

retained(
    'L600-12-2',
    "Maintien des deux alinéas : un mois pour introduire le recours administratif, rejet après plus de deux mois de silence, absence de prorogation du recours contentieux. Ces délais organisent la stabilité des autorisations sans rendre obligatoire un recours préalable. Les raccourcir davantage ou supprimer l'accès au recours administratif porterait sur des garanties de recours ; l'abrogation générale rétablirait au contraire une prorogation de l'incertitude sur le permis. Aucun changement de vocabulaire n'est présenté comme une coupe.",
    "Source intégralement lue, notes vides ; valid_from 2025-11-28 ne constitue pas une date de réforme future. R*600-1, R*600-2 et R*600-3 consultés : notifications, affichage et bornes contentieuses sont distincts du délai du recours gracieux. Un recours administratif ne dispense donc pas de saisir le juge dans le délai applicable. Le code de justice administrative et les règles générales du CRPA ne figurent pas dans les textes assignés ; aucune réécriture de ces codes ni validation de leur application à un cas concret n'est affirmée.",
    "Aucun changement normatif : le recours gracieux ou hiérarchique reste facultatif, avec les trois paramètres temporels de la source. Aucune nouvelle réduction de délai ou d'obligation n'est comptée.",
    "La règle ne fixe pas à elle seule tous les points de départ ni toutes les garanties du recours contentieux. Les autres codes procéduraux et les situations individuelles demeurent hors de cet examen borné.",
    "Aucune charge nouvelle identifiée : aucun recours préalable obligatoire, envoi, formulaire, frais ou délai additionnel n'est créé par le maintien.",
)

retained(
    'L600-13',
    "Maintien de la règle d'articulation des contentieux du permis tenant lieu d'une autre autorisation. Elle permet d'appliquer un cadre commun sans imposer un second titre ni un second recours, tout en réservant les dispositions contraires de la législation sectorielle. La supprimer créerait une incertitude sur les garanties et procédures applicables ; l'article n'institue lui-même aucune taxe ou formalité à retirer.",
    "Article entier relu, notes vides. La réserve 'sauf disposition contraire de cette dernière' est essentielle : la règle ne neutralise ni évaluation environnementale, ni accord sectoriel, ni procédure de recours spéciale. Les coordinations de L425 dans coordination.json ne suppriment pas cette articulation et n'étendent pas fictivement les cas où un permis tient lieu d'une autre autorisation. Aucun renvoi nominatif à une norme abrogée dans la source.",
    "Maintien du champ contentieux commun et de la primauté des exceptions sectorielles. Aucune seconde fusion d'autorisations ni baisse de charge n'est attribuée à cet article conservé.",
    "La liste des législations sectorielles et leurs exceptions n'est pas auditée ici de manière exhaustive. L'article ne suffit pas à démontrer un solde national de simplification.",
    "Aucune charge nouvelle identifiée : ni saisine supplémentaire, ni dossier commun nouveau, ni extension du champ des permis tenant lieu n'est ajouté.",
)

source = by_number['L610-1']['source_xml']
old_first = "1° En cas d'exécution de travaux ou d'utilisation du sol en méconnaissance des obligations imposées par les articles L. 111-1 à L. 111-10, L. 111-15, L. 111-19-1, L. 111-23, L. 115-3 et L. 131-1 à L. 131-7 ainsi que par les règlements pris pour leur application ;"
new_first = "1° En cas d'exécution de travaux ou d'utilisation du sol en méconnaissance des obligations imposées par les articles L. 111-1 à L. 111-10, L. 111-15, L. 111-19-1, L. 111-23 et L. 115-3 ainsi que par les règlements pris pour leur application ;"
assert source.count(old_first) == 1
criminal_exclusion = "La seule méconnaissance des obligations prévues aux articles L. 131-1 à L. 131-7 ou par les règlements pris pour leur application ne constitue pas une infraction au titre du présent article."
xml = source.replace(old_first, new_first) + (
    '<p>' + criminal_exclusion + " Ces obligations et les recours contre les documents d'urbanisme demeurent applicables. Cette exclusion entre en vigueur à la date d'entrée en vigueur de la loi portant la présente rédaction et bénéficie aux faits antérieurs dans les conditions d'application de la loi pénale plus douce. Elle ne supprime ni les infractions fondées sur une autre disposition, ni les réparations civiles légalement dues.</p>"
)
changed(
    'L610-1', xml,
    "Réforme de fond ciblée : le 1° ne fait plus des rapports de hiérarchie entre documents de planification des fondements de l'incrimination des travaux ou de l'utilisation du sol. L131-1 à L131-7 s'adressent aux documents et à leurs auteurs, avec leurs analyses et délibérations ; leur renvoi pénal général ajoute une exposition distincte sans nécessité établie pour contrôler les travaux. Leur respect demeure contrôlable par le juge administratif. Sont intégralement maintenus les infractions au PLU, le reste du 1°, les 2° à 4°, l'étude de sécurité et sa réception requise, l'exception favorable d'autorisation définitive exécutée conformément à ses termes sauf fraude, et les droits de partie civile. Les passages non concernés restent ceux de la source ; la réduction n'est pas une dépénalisation générale de l'urbanisme.",
    "L131-1 à L131-7 et L480-1 à L480-9 lus en entier, ainsi que les autres articles législatifs nommés dans les 1° à 4° : la hiérarchie de planification, les protections littorales et de montagne, l'eau et les espaces protégés conservent leurs bases autonomes. Les sanctions directes du PLU et des autres dispositions retenues restent applicables aux mêmes personnes et dans leurs limites. Les facultés de reconstruction L111-15, de restauration L111-23, les exceptions de L111-4 et L111-7 à L111-10, les exemptions et le non-cumul de L111-19-1 ne sont pas supprimés ni resserrés. L114-1 à L114-3 et R114-1 à R114-3 vérifiés : aucun préavis ou procédure de travail ne leur est substitué. Subdivisions et neuf alinéas d'origine conservés, seul le renvoi hiérarchique est retiré du 1° ; un alinéa final explicite la limite et l'application de la loi pénale plus douce, sans amnistie générale ni effacement de droits civils. Le code pénal et le code de procédure pénale restent à coordonner si une mesure d'exécution supplémentaire est nécessaire ; ils ne sont pas déclarés réécrits. L'étendue pratique des poursuites antérieurement fondées sur ce seul renvoi n'est pas documentée, donc aucune économie de frais ni baisse de montant d'amende n'est chiffrée.",
    'material_reduction',
    "Réduction réelle mais étroite du champ pénal par rapport à la source entière : retrait du renvoi autonome aux sept articles de hiérarchie de planification. Les obligations de planification, les autres incriminations et toutes les protections favorables restent applicables. L'effet pratique sur le nombre de poursuites est inconnu.",
    "Aucune suppression générale des sanctions L480 ni des règles environnementales. Le retrait peut n'avoir qu'un effet limité lorsque les mêmes faits relèvent d'une autre infraction ; ni coût évité ni solde global des codes n'est établi.",
    "Aucune charge nouvelle identifiée : aucune déclaration, autorisation, registre ou preuve ne remplace le renvoi pénal retiré. Les obligations maintenues restent celles de leurs textes autonomes, sans nouveau contrôle de substitution.",
    ["L'extension des sanctions de L480-4 aux travaux et utilisations du sol sur le seul fondement des obligations de hiérarchie de planification de L131-1 à L131-7 est supprimée, y compris pour leurs règlements d'application au seul titre de ce renvoi."],
    {
        'kind': 'compliance_cost_reduced',
        'measure_id': 'urbanisme-fin-renvoi-penal-hierarchie-plans',
        'description': "Retrait d'un fondement d'exposition pénale attaché à la hiérarchie des documents, sans retrait des obligations administratives de planification ; aucun coût monétaire évité n'est présumé.",
        'before': "Les personnes auxquelles L480-4 est applicable peuvent relever du 1° de L610-1 pour les travaux ou utilisations du sol méconnaissant les obligations de L131-1 à L131-7 et leurs règlements ; aucun taux ou assiette fiscale en cause.",
        'after': "L610-1 ne sanctionne plus la seule méconnaissance de ces obligations de hiérarchie ; ses autres fondements et les infractions autonomes subsistent, sans réduction revendiquée du barème de L480-4.",
        'unit': 'legal_duty',
        'affected_population': "Personnes susceptibles de poursuites pour travaux ou utilisation du sol au titre du renvoi hiérarchique du 1° de L610-1.",
        'conditions_and_transition': "Entrée en vigueur de la loi portant la nouvelle rédaction ; faits antérieurs soumis à la loi pénale plus douce dans son champ, sans amnistie générale ni extinction des réparations civiles.",
        'replacement_or_new_burdens': "Aucune formalité de remplacement ; maintien du contrôle des documents et des autres infractions sur leurs bases propres.",
        'source_quote': old_first,
        'proposed_quote': criminal_exclusion,
    },
)

retained(
    'L610-2',
    "Maintien du secret professionnel des personnes réalisant, à la demande et pour le compte d'une collectivité publique, les études préparatoires d'urbanisme. Il protège notamment les informations confidentielles recueillies à cette occasion et les intérêts des tiers ; il ne constitue ni une autorisation d'exercer ni un dossier déclaratif. Supprimer en bloc ce devoir de confidentialité ne serait pas une suppression justifiée de charge redondante.",
    "Source et absence de notes relues. Le champ exige la demande et le compte d'une collectivité publique, non toute étude d'urbanisme privée. Le renvoi pénal est exactement l'article 226-13 du code pénal ; son texte n'est pas dans le corpus des cinq codes fourni. Les exceptions légales de divulgation et les règles d'accès aux documents gardent leur champ propre ; aucune interdiction nouvelle de communiquer une information légalement accessible n'est ajoutée. Aucun secret réel ni fichier privé n'a été consulté pour ce travail.",
    "Aucun changement à la source entière : maintien d'un devoir de confidentialité circonscrit aux études pour une collectivité et du renvoi de sanction existant, sans nouvelle mesure d'allègement comptée.",
    "La coordination avec les exceptions du droit pénal et l'accès légal aux documents n'est pas une réécriture de ces régimes extérieurs. Aucun montant de coût de confidentialité n'est évalué.",
    "Aucune charge nouvelle identifiée : aucune habilitation, liste nominative, attestation de secret ou formation obligatoire n'est introduite par le maintien.",
)

retained(
    'L610-3',
    "Maintien de l'articulation pénale relative à l'ouverture, à l'extension et aux modifications d'exploitation des établissements dangereux, insalubres ou incommodes dans les territoires couverts par un PLU ou document équivalent. Le renvoi aux peines des installations classées porte une protection de santé et de sécurité ; son abrogation ne démontrerait pas la suppression d'une autorisation redondante. Aucune double sanction automatique n'est créée par une reformulation.",
    "Alinéa source entier lu, notes vides. Trois opérations restent visées : ouverture, extension et modification des conditions d'exploitation. Ne pas confondre ce renvoi aux sanctions sectorielles avec une taxe, ni avec le renvoi hiérarchique retiré du 1° de L610-1. La législation des installations classées est extérieure aux cinq codes fournis : son champ exact, les règles de concours et le non-cumul applicable ne sont pas présentés comme audités ou réécrits ici. Le maintien n'ajoute pas un agrément au régime environnemental.",
    "La source demeure entière : maintien du dispositif de sanctions pour des activités à risques, sans preuve locale permettant d'en retrancher un élément comme un doublon purement procédural.",
    "Le régime ICPE complet et les éventuels concours d'infractions ne sont pas contenus dans ce lot. Aucun gain de taxe, de délai ou de complexité n'est attribué à ce maintien.",
    "Aucune charge nouvelle identifiée : le texte maintenu ne crée ni étude, ni autorisation, ni déclaration supplémentaire et ne modifie aucun plafond de sanction.",
)

retained(
    'L610-4',
    "Maintien intégral des compétences de constatation, du commissionnement et de l'assermentation, ainsi que de la présomption probatoire simple des procès-verbaux. Ces conditions encadrent les pouvoirs de contrôle et les droits de défense ; les supprimer élargirait les pouvoirs sans garantie ou retirerait les moyens de protéger les boisements et espaces naturels. Il n'existe ici ni dépôt privé, ni agrément d'activité, ni prélèvement à retirer.",
    "Deux alinéas lus. L113-8 et L113-15 ont été vérifiés : compétences relatives aux espaces naturels sensibles et aux espaces agricoles et naturels périurbains, non quotas SRU. L480-1 vérifié : la proximité des règles de constatation ne les rend pas identiques quant aux infractions couvertes. Tous officiers et agents de police judiciaire, agents commissionnés et assermentés et compétence forestière restent à leurs champs exacts. 'Jusqu'à preuve du contraire' est conservé ; aucune présomption irréfragable ni nouveau document d'identification n'est proposé.",
    "Aucun changement normatif : compétences de police et garanties probatoires conservées intégralement. La similitude partielle avec L480-1 n'est pas comptée comme une procédure supprimée.",
    "Les règles générales de preuve et la procédure pénale restent distinctes. La conservation de cette compétence ne démontre aucun solde global de contrôle ou de coût public.",
    "Aucune charge nouvelle identifiée : aucun nouveau corps d'agents, commissionnement supplémentaire, registre privé ou délai de réponse n'est institué.",
)

retained(
    'R101-1',
    "Maintien des quatre parties et des classifications favorables du III : photovoltaïque remplissant les critères et sols végétalisés des parcs ou jardins publics peuvent demeurer non artificialisés. Le classement fondé sur l'occupation effective et les seuils de nomenclature assure une mesure comparable sans créer un relevé individuel obligatoire. Une suppression de la méthode seule laisserait les objectifs législatifs en vigueur avec davantage d'incertitude et pourrait retirer ces avantages futurs.",
    "Source entière relue. Annexe à R101-1 consultée intégralement dans le corpus, y compris ses dix catégories, tableau à cellules fusionnées, seuils 50 m² et 2 500 m², largeur de cinq mètres et couvert arboré de moins de 25 %. Cette annexe est une source distincte non assignée ; elle n'est ni résumée dans une proposition ni modifiée. L101-2-1, L111-27, L111-29 et L123-1 vérifiés. Les catégories 6°, 7°, 10° pour le photovoltaïque et 9° ou 10° pour parcs et jardins restent à leur objet exact et aux mêmes seuils. Les trois renvois CGCT et le décret prévu par l'article 194 III 6° de la loi 2021-1104 sont hors corpus assigné : aucune vérification intégrale de ces textes extérieurs ni abolition générale de l'objectif d'artificialisation n'est affirmée.",
    "La règle entière reste inchangée, notamment les exceptions favorables du III et le classement effectif. Aucune baisse de prélèvement ou nouvelle dispense déclarative n'est inventée à partir d'une méthode de mesure.",
    "Les objectifs législatifs d'artificialisation ne sont pas supprimés par cette décision ; leurs coûts et les textes régionaux extérieurs restent à leur champ propre. Aucun solde national de complexité n'est établi.",
    "Aucune charge nouvelle identifiée : le maintien n'impose ni déclaration parcellaire privée, ni levé supplémentaire, ni nouvelle donnée à transmettre et ne modifie aucun seuil de la nomenclature.",
)

retained(
    'R101-2',
    "Maintien de la plateforme nationale de données d'artificialisation. La mise à disposition par l'État permet l'accès partagé aux données et évite de supprimer un outil commun au profit de collectes séparées. La source n'oblige pas les particuliers ou collectivités à transmettre un état supplémentaire à cet observatoire ; aucune suppression d'un reporting inexistant n'est revendiquée.",
    "Alinéa entier relu, notes vides. L'accès dématérialisé porte à la fois sur consommation des espaces naturels, agricoles et forestiers et artificialisation ; ces deux objets sont maintenus. La mention de fixation et de suivi des objectifs n'est ni un quota de logements sociaux ni une habilitation à exiger une attestation individuelle nouvelle. R101-1 et son annexe ont été lus ; leur maintien laisse cette plateforme utile. Pas de réemploi CRPA présenté comme un nouveau gain.",
    "Aucune modification : la mise à disposition nationale de données est conservée comme infrastructure commune, sans la comptabiliser comme une nouvelle fusion de déclarations.",
    "Les coûts publics de fonctionnement et les obligations de collecte fondées sur d'autres textes ne sont pas évalués par cet alinéa. Aucun solde consolidé des codes n'en est déduit.",
    "Aucune charge nouvelle identifiée : aucune remontée périodique, nouvelle inscription à la plateforme ou donnée personnelle n'est demandée par le texte maintenu.",
)

pig_xml = """<p>Les projets mentionnés à l'article L. 102-1 sont qualifiés de projet d'intérêt général par arrêté préfectoral.</p>
<p>Lorsqu'un document d'urbanisme doit permettre la réalisation d'un projet d'intérêt général, l'arrêté est notifié à la personne publique qui élabore ce document.</p>
<p>Le préfet précise les incidences du projet sur le plan local d'urbanisme dans le cas prévu par l'article L. 153-49.</p>
<p>L'arrêté préfectoral devient caduc à l'expiration d'un délai de trois ans à compter de la notification prévue au deuxième alinéa. Il peut être renouvelé lorsque le projet satisfait aux conditions de l'article L. 102-1.</p>
<p>La présente rédaction s'applique à compter de l'entrée en vigueur de la loi abrogeant l'article L. 102-2, y compris aux procédures de qualification ou de renouvellement en cours à cette date. Une directive territoriale d'aménagement et de développement durables ne peut, à elle seule, fonder une qualification ou un renouvellement ; les conditions de l'article L. 102-1 doivent être remplies de manière autonome.</p>
<p>Les arrêtés régulièrement pris avant cette date sur le seul fondement de l'article L. 102-2 conservent leurs effets pour la durée restant à courir, sans renouvellement sur ce fondement. Les actes pris, les contrats valablement conclus et les droits acquis sur leur fondement restent régis par les dispositions qui leur étaient applicables, sous réserve des voies de recours.</p>"""
changed(
    'R102-1', pig_xml,
    "Coordination nécessaire de la suppression déjà proposée en L102-2 : retrait, pour l'avenir, de la référence aux mesures d'exécution des DTADD comme fondement spécial de qualification en PIG. Ce n'est pas une seconde suppression de procédure à additionner à L102-2. La qualification de droit commun de L102-1, l'arrêté, sa notification, la précision des incidences sur le PLU et la caducité de trois ans restent à droit constant. Le renouvellement est réservé aux projets remplissant de façon autonome les conditions conservées, sans pérenniser la voie spéciale par renvoi.",
    "L102-1 à L102-12 et L153-49 lus ; proposition complète de L102-2 consultée. Son abrogation prospective et sa transition imposent cette coordination, même si le renvoi figure encore dans la source réglementaire officielle. L102-5 conserve dans le corpus un brouillon à droit constant incompatible : son pouvoir spécial pendant douze ans et ses consultations ne sont pas coordonnés par le présent lot ; sa réécriture demeure nécessaire et n'est pas déclarée accomplie. Les quatre alinéas matériels de R102-1 sont maintenus dans leur ordre, avec le renvoi au deuxième alinéa conservé ; deux alinéas transitoires sont ajoutés. Les anciens PIG spéciaux ne sont ni annulés ni prorogés ; les contrats et droits acquis sont protégés. L102-3 conserve son exclusion des initiatives communales. Aucune suppression de dérogation littorale ni de finalité de logement des personnes modestes de L102-1. La filiation historique SRU des règles PIG ne résulte pas de cette coordination et reste non soldée. Une même clé de mesure doit être reprise lors du bilan ultérieur de L102-2 et L102-5 ; aucun impact antérieur consolidé validé n'a été trouvé pour L102-2.",
    'coordination_only',
    "La source officielle permet encore la qualification spéciale renvoyant à L102-2 ; la proposition en retire l'exécution réglementaire et protège les arrêtés anciens. Effet coordonné de la même suppression de voie DTADD, sans deuxième allègement autonome compté.",
    "La cohérence législative exige encore la reprise de L102-5, dont le brouillon public reste incompatible. Les PIG de droit commun et les anciens effets protégés subsistent ; aucun coût net national n'est établi.",
    "Aucune charge nouvelle identifiée : les conditions L102-1 étaient déjà celles de la voie de droit commun. Aucun dossier, avis, déclaration ou preuve autonome ne remplace la qualification spéciale retirée.",
    ["La voie réglementaire de qualification et de renouvellement des seules mesures de mise en œuvre des DTADD par renvoi à L102-2 est retirée pour les décisions nouvelles ; le régime des PIG fondés sur L102-1 reste ouvert."],
    {
        'kind': 'coordination',
        'measure_id': 'urbanisme-pig-dtadd-suppression',
        'description': "Retrait du renvoi réglementaire qui rétablirait la voie spéciale DTADD supprimée en L102-2 ; aucune seconde autorisation supprimée n'est comptée.",
        'before': "Qualification par arrêté préfectoral des projets de L102-1 et des mesures de L102-2 ; caducité trois ans après notification et possibilité générale de renouvellement.",
        'after': "Seuls les projets remplissant les conditions autonomes de L102-1 peuvent recevoir une qualification ou un renouvellement nouveau ; même caducité de trois ans, anciens arrêtés spéciaux préservés jusqu'à leur terme.",
        'unit': 'regime',
        'affected_population': "État, collectivités élaborant les documents et personnes concernées par les qualifications PIG fondées seulement sur une DTADD.",
        'conditions_and_transition': "Entrée en vigueur alignée sur l'abrogation législative de L102-2 ; procédures en cours couvertes ; durée résiduelle et droits anciens protégés, sans renouvellement spécial.",
        'replacement_or_new_burdens': "Pas de procédure spéciale de remplacement ; la voie L102-1 préexistante demeure soumise à ses propres conditions.",
        'source_quote': "Les projets et mesures mentionnés respectivement aux articles L. 102-1 et L. 102-2 sont qualifiés de projet d'intérêt général par arrêté préfectoral.",
        'proposed_quote': "Les projets mentionnés à l'article L. 102-1 sont qualifiés de projet d'intérêt général par arrêté préfectoral.",
    },
)

retained(
    'R102-3',
    "Maintien intégral de la liste des vingt-neuf opérations d'intérêt national. Elle délimite des régimes territoriaux et ouvre notamment des possibilités de construction dérogatoire ; en retrancher arbitrairement des opérations supprimerait ces avantages et modifierait les compétences. La liste n'ajoute pas elle-même un agrément ou une déclaration à chaque projet. Le millésime olympique ne démontre pas à lui seul l'extinction de tous les travaux ou effets de l'opération.",
    "Les vingt-neuf rubriques et la note du 5° ont été lues en entier : noms, communes, périmètres, dates et décrets restent ceux de la source. L102-12 et L102-13 vérifiés : les avantages de construction et exclusions de certains droits restent distincts du pouvoir de sursis dont coordination.json prévoit déjà l'allègement. La note renvoie au plan annexé au décret 2025-774 pour Euroméditerranée ; ce plan et les autres décrets territoriaux ne sont pas joints à la source ni présents comme compagnons assignés, leurs tracés ne sont donc pas prétendus vérifiés. Les 26° à 29° proviennent des décrets de décembre 2025, sans être transformés en dates de réforme future. Le renvoi source de L102-13 9° à L331-7, extérieur au lot, appelle sa propre vérification dans la recodification fiscale ; le maintien de la liste n'en prétend pas achever la coordination.",
    "Aucune modification à la liste officielle entière : les vingt-neuf qualifications et leurs possibilités favorables futures sont conservées. Aucune nouvelle fusion territoriale ou suppression de procédure n'est revendiquée.",
    "Les périmètres graphiques et textes extérieurs des opérations ne sont pas audités ici. La conservation de la liste ne démontre ni nécessité de toute contrainte dérivée ni solde national de complexité.",
    "Aucune charge nouvelle identifiée : aucune nouvelle opération, commune, compétence, déclaration ou pièce de périmètre à produire n'est ajoutée à la source.",
)

source = by_number['R103-1']['source_xml']
pedestrian_old = "3° La transformation d'une voie existante en aire piétonne d'une superficie supérieure à 3 000 mètres carrés ou la suppression d'une aire piétonne d'une même superficie ;"
assert source.count(pedestrian_old) == 1
pedestrian_rule = "La transformation d'une voie existante en aire piétonne ou la suppression d'une aire piétonne n'est pas soumise à une concertation sur le seul fondement de sa superficie."
pedestrian_xml = source.replace(pedestrian_old, '3° Abrogé ;') + (
    '<p>' + pedestrian_rule + " Les opérations relevant d'une autre catégorie de l'article L. 103-2 restent soumises à la concertation correspondante. Les obligations de participation du public prévues par d'autres dispositions demeurent applicables.</p>"
    "<p>La suppression de la concertation fondée sur la seule superficie de l'aire piétonne s'applique à compter de l'entrée en vigueur du décret portant la présente rédaction, y compris aux opérations en cours. Les observations déjà recueillies sont conservées et le temps de participation déjà annoncé au public ne peut être réduit sur ce seul fondement. Les actes régulièrement accomplis et les décisions devenues définitives ne sont pas remis en cause.</p>"
)
changed(
    'R103-1', pedestrian_xml,
    "Réforme de fond : retrait de la concertation obligatoire du seul fait qu'une voie transformée en aire piétonne, ou une aire supprimée, dépasse 3 000 m². La surface de cet aménagement, isolément, ne démontre pas la nécessité d'une procédure d'urbanisme distincte ; les autres catégories et les obligations de participation sur fondement environnemental ou sectoriel restent applicables selon leurs conditions propres. Aucune déclaration ne remplace le 3°. Les sept autres rubriques sont conservées intégralement avec leurs seuils, qualifications et territoires, sans retoucher les protections des cours d'eau, ports, rivages ou grandes opérations de construction.",
    "L103-1 à L103-7, L300-2, L313-4-1 et R103-2/R103-3 lus. Le retrait du 3° n'exonère pas une opération relevant aussi d'un autre cas de L103-2 ou des sept rubriques conservées ; R103-2 continue à agréger les tranches sur moins de cinq ans pour ces seuils. La participation imposée par d'autres dispositions, notamment environnementales, et les recours restent réservés ; le code de l'environnement et le CGCT ne sont pas fournis en entier dans ce corpus, leur coordination procédurale n'est pas prétendue réalisée. Le dispositif n'est donc pas une dispense générale de consultation ni une autorisation de supprimer une aire piétonne sans ses autres conditions légales. Les dispenses favorables L103-7 et R103-3 restent ouvertes aux situations futures. Le 3° reste à son emplacement comme abrogé ; les 1°, 2° et 4° à 8° sont reproduits sans aucune omission, y compris 5 000 m², 1 900 000 euros, 150 places, plus de 10 % et plus de 2 000 m². La note de prise d'effet au 1er juin 2021 du décret 2021-618 reste historique, sans devenir la date de la réforme. Concertations engagées : observations et durée annoncée protégées, sans recommencer les actes ni remettre en cause les décisions définitives. La filiation exhaustive de SRU25 demeure distincte de cette coupe actuelle et n'est pas déclarée achevée.",
    'material_reduction',
    "Par rapport aux huit rubriques de la source officielle, une obligation de concertation fondée seulement sur la superficie d'une aire piétonne est effectivement supprimée. Les sept autres cas et les procédures légalement autonomes demeurent ; aucune suppression de toutes les participations d'un projet n'est revendiquée.",
    "Le gain ne couvre que les opérations dont l'obligation reposait sur ce seul critère ; il peut être nul lorsqu'une autre procédure reste due. Les procédures engagées conservent le temps annoncé, et le coût net de l'ensemble des codes n'est pas établi.",
    "Aucune charge nouvelle identifiée : ni déclaration, ni étude ni procédure de remplacement du 3° n'est créée. La réserve des participations déjà dues et la conservation des observations existantes n'exigent aucun nouveau dépôt.",
    ["La concertation obligatoire attachée à la seule transformation d'une voie en aire piétonne de plus de 3 000 m² ou à la suppression d'une aire piétonne de cette superficie est supprimée, sous réserve des autres fondements de participation déjà applicables."],
    {
        'kind': 'obligation_removed',
        'measure_id': 'urbanisme-aires-pietonnes-fin-concertation-surface',
        'description': "Suppression du déclenchement automatique d'une concertation d'urbanisme par le seul seuil de superficie de l'aire piétonne.",
        'before': "Transformation d'une voie en aire piétonne de superficie supérieure à 3 000 m² ou suppression d'une aire piétonne de même superficie : concertation obligatoire en application du 3° de R103-1 et de L103-2.",
        'after': "La seule superficie ne déclenche plus cette concertation, sans formulaire de remplacement ; les obligations fondées sur une autre catégorie ou une autre législation restent dues.",
        'unit': 'legal_duty',
        'affected_population': "Autorités et maîtres d'ouvrage transformant une voie existante en aire piétonne ou supprimant une aire piétonne dans le champ de l'ancien 3°.",
        'conditions_and_transition': "Entrée en vigueur du décret portant la nouvelle rédaction ; opérations en cours incluses, observations acquises et temps de participation déjà annoncé préservés, décisions définitives non remises en cause.",
        'replacement_or_new_burdens': "Aucune procédure de remplacement ; les autres obligations de concertation, de participation et de recours restent à leur champ propre.",
        'source_quote': pedestrian_old,
        'proposed_quote': pedestrian_rule,
    },
)

retained(
    'R103-2',
    "Maintien de l'agrégation des tranches réalisées dans un intervalle de moins de cinq ans pour apprécier les seuils de R103-1. Ce calcul empêche qu'une opération importante échappe à la participation du public par son seul fractionnement ; il ne crée ni transmission périodique ni dossier distinct. La coupe du 3° de R103-1 ne justifie pas de supprimer cette garantie pour les sept catégories restantes.",
    "Source entière et R103-1/R103-3 lus. 'Moins de cinq ans' est conservé exactement : aucun passage à cinq ans inclus, aucun délai minimal d'attente entre tranches. Le renvoi aux seuils de R103-1 ne recrée pas celui de l'aire piétonne supprimé dans la proposition du présent lot. Il reste utile pour les autres seuils de construction, montant, capacité, surface ou pourcentage. Le maintien n'exige aucun registre des opérations ni déclaration globale nouvelle et ne ferme pas les dispenses d'entretien ou d'opération sensible.",
    "Aucun changement par rapport à la source : maintien de la règle antifractionnement pour les seuils encore applicables, sans réintroduction du seuil supprimé pour les aires piétonnes.",
    "Le texte n'établit ni délai d'autorisation ni durée maximale des travaux. L'identification concrète d'une même opération et les coûts de participation ne sont pas chiffrés ici.",
    "Aucune charge nouvelle identifiée : aucun dépôt agrégé autonome ou calendrier déclaratif n'est ajouté ; seul le mode de calcul déjà prévu reste applicable.",
)

retained(
    'R103-3',
    "Maintien intégral de la dispense favorable de concertation pour les travaux d'entretien et de grosses réparations, quels que soient les ouvrages et aménagements concernés. Elle bénéficie aux opérations futures aussi bien qu'aux travaux déjà envisagés. L'abroger au nom de la simplification imposerait potentiellement une nouvelle concertation ; aucune contrepartie déclarative n'est ajoutée.",
    "Source et notes vides relues. Le renvoi porte sur l'ensemble de L103-2, non le seul 3°. La qualification d'entretien ou de grosses réparations reste nécessaire, mais aucune restriction de surface, de coût ou de catégorie d'ouvrage n'est introduite. La suppression ciblée du 3° de R103-1 n'absorbe pas cette dispense générale ; les participations ou autorisations légalement autonomes demeurent distinctes.",
    "La dispense officielle entière est conservée, sans restriction aux situations antérieures ni revendication d'une nouvelle exemption créée par ce lot.",
    "Les qualifications des travaux et les procédures d'autres législations gardent leur champ propre. Aucune réduction supplémentaire de prélèvement ou de complexité globale n'est démontrée.",
    "Aucune charge nouvelle identifiée : ni déclaration d'exemption, ni attestation d'entretien ni autorisation spécifique n'est exigée pour bénéficier de la règle maintenue.",
)

retained(
    'R104-1',
    "Maintien de la règle de champ de l'évaluation environnementale. Elle renvoie aux cas et conditions du chapitre au lieu d'exiger une étude identique pour chaque document ou évolution. Les obligations relèvent notamment de la directive 2001/42/CE et de la prévention des incidences notables ; leur abrogation générale ne serait pas un allègement national juridiquement coordonné. Les dispenses et procédures proportionnées restent applicables.",
    "Source et note du Conseil d'État n° 400420 du 19 juillet 2017 lues intégralement. L104-1 à L104-8 et R104-2 à R104-8 vérifiés : le champ comprend les catégories légales récentes sans exiger une nouvelle liste réglementaire. La note signale l'annulation partielle de l'ancien dispositif pour les évolutions susceptibles d'incidences notables, pas l'abrogation totale de R104-1. L104-2 3° et L121-28 ont été lus : les schémas de plage et leurs évaluations ne sont ni fermés ni supprimés. La rubrique environnement I 50° n'est pas réécrite ici. Aucun changement aux dates d'application des textes historiques.",
    "Aucune modification de la source entière : maintien du champ nécessaire d'évaluation, dans ses cas et conditions, sans compter une obligation environnementale conservée comme une simplification.",
    "Le respect du droit de l'Union et de la décision de 2017 doit être apprécié dans chaque procédure ; aucune conformité européenne générale ni évaluation de coût net n'est affirmée.",
    "Aucune charge nouvelle identifiée : aucune catégorie, étude supplémentaire, pièce ou autorisation n'est ajoutée aux renvois existants et les exclusions légales restent applicables.",
)

retained(
    'R104-2',
    "Maintien de l'alternative entre nouvelle évaluation et actualisation d'une évaluation déjà réalisée. L'actualisation est un allègement existant à conserver pour les évolutions futures ; la présenter comme une fusion nouvelle serait inexact. L104-3 et L104-5 ainsi que R104-19 et R104-20 encadrent déjà le champ et la proportionnalité : aucune étude entièrement nouvelle obligatoire ne résulte de cet article à supprimer.",
    "Alinéa entier et note CE 400420 lus. L104-3, L104-5, R104-18 à R104-20 vérifiés : informations raisonnablement exigibles, références aux études existantes et compléments lors des évolutions sont déjà possibles. Ne pas déclarer comme nouveau gain le simple réemploi ou la possibilité d'actualiser. La note de 2017 sanctionne l'insuffisante couverture des incidences notables, non l'option d'actualisation. Les exceptions légales et leurs transitions restent celles de L104-3 ; aucune dispense ne se substitue à l'analyse des incidences.",
    "Aucun changement : la voie favorable d'actualisation et l'alternative de la source sont conservées intégralement. Zéro nouvelle fusion ou dispense de dépôt comptée.",
    "La suffisance d'une actualisation dépend du document et des incidences ; le texte ne permet pas de garantir l'absence de compléments. Les gains existants ne sont pas chiffrés comme nouveaux.",
    "Aucune charge nouvelle identifiée : aucun formulaire d'actualisation, certification de réemploi, délai ou étude systématique n'est créé par le maintien.",
)

retained(
    'R104-3',
    "Maintien des évaluations d'élaboration et de révision des DTADD et du filtre plus favorable pour leurs modifications : Natura 2000 ou incidences notables établies après examen au cas par cas. La suppression de la voie spéciale PIG de L102-2 ne supprime pas les directives elles-mêmes ni leurs effets de planification ; elle ne rend donc pas cette évaluation sans objet. Retirer les filtres favorables rendrait au contraire l'évaluation systématique.",
    "Source, subdivisions 1° à 3° et a/b et note de l'article 26 du décret 2021-1345 lues en entier. L102-4 à L102-11 et R104-28 à R104-32 vérifiés. Le contrôle Natura 2000 et les critères de l'annexe II de la directive 2001/42/CE sont conservés ; aucune dispense générale ne résulte du caractère modificatif. La note source distingue les procédures déjà couvertes par une décision de dispense et les autres procédures ayant une décision antérieure : aucune date future n'en est déduite. Anomalie extérieure au lot repérée : R104-30 vise R104-32 pour la décision implicite, alors que R104-31 en fixe le régime dans le corpus ; ce renvoi appelle une vérification et coordination propres, non une suppression de la plage correcte R104-28 à R104-32 du présent article.",
    "Maintien intégral du mécanisme officiel, avec évaluation des élaborations/révisions et sélection des modifications selon leurs incidences. Aucune suppression de la voie PIG n'est comptée une seconde fois ici.",
    "La directive européenne et les décisions d'examen gardent leur champ ; les coordinations extérieures identifiées ne sont pas exécutées dans cet article. Aucun bilan net national n'est démontré.",
    "Aucune charge nouvelle identifiée : mêmes événements déclencheurs, même filtre au cas par cas, aucun avis ou dossier de remplacement ajouté après suppression du PIG spécial.",
)

retained(
    'R104-4',
    "Maintien complet des cinq cas concernant le schéma directeur d'Île-de-France. L'évaluation n'est systématique pour les modifications ou mises en compatibilité que dans les cas définis ; le cas par cas et l'analyse déjà incluse dans l'étude d'impact de la procédure intégrée évitent les évaluations sans objet ou redondantes. Ces allègements existants restent ouverts pour l'avenir ; les supprimer ou retirer les protections Natura 2000 ne serait pas une simplification justifiée.",
    "Les 1° à 5°, lettres a/b du 3° et a/b/c du 4°, et la note d'application du décret 2021-1345 ont été relus intégralement. L104-1 à L104-5, R104-28 à R104-32 et L300-6-1 entier vérifiés : son V conditionne l'évaluation distincte à l'absence d'analyse incluse dans l'étude d'impact. Les trois voies du 4° restent distinctes : Natura 2000, mêmes effets qu'une révision, incidences notables après examen. L123-1 confirme le rôle du schéma. Pas de fusion nouvelle revendiquée pour l'étude d'impact déjà suffisante, ni modification de la transition historique de 2021. Les règles CGCT et du code de l'environnement extérieures ne sont pas déclarées réécrites.",
    "Aucun changement à la source entière : les déclencheurs nécessaires et les filtres favorables sont conservés, notamment l'absence de seconde analyse quand le V de L300-6-1 est satisfait.",
    "La suffisance de l'étude d'impact et les incidences du schéma doivent être établies dans chaque opération. Aucun coût de double étude supposé supprimé ni solde global n'est chiffré.",
    "Aucune charge nouvelle identifiée : aucune étude additionnelle, nouvelle condition de dispense, saisine ou nouvelle échéance n'est créée.",
)

retained(
    'R104-5',
    "Maintien des règles des schémas d'aménagement régionaux et du plan de Corse. L'élaboration et la révision, les modifications ciblées et la procédure intégrée conservent leurs champs distincts. Le 4° évite déjà une évaluation séparée si l'étude d'impact couvre les incidences ; le 5° ne concerne que le schéma régional, sans extension au plan de Corse. Aucune formalité supplémentaire sans fonction identifiée n'est retirée au prix d'une réduction des protections ou des dispenses existantes.",
    "Source intégrale et note de l'article 26 du décret 2021-1345 lues ; les deux paragraphes et les 1° à 5° sont conservés. L300-6-1 et R104-28 à R104-32 vérifiés en entier. Le 3° a Natura 2000, le 3° b examen d'incidences, le 4° analyse déjà incluse et le 5° a/b gardent leurs critères exacts. Les articles CGCT L4433-7 et L4424-9 sont cités par la source mais leurs textes complets ne figurent pas dans les cinq codes fournis : aucune réécriture de leurs compétences n'est affirmée. Différence préexistante à signaler, sans correction silencieuse : le 5° a/b ne reproduit pas une branche Natura 2000 autonome comme le 4° a de R104-4 ; la protection européenne et l'examen des incidences restent à respecter, sans prétendre résoudre cette différence dans un maintien à droit constant.",
    "Aucun changement normatif : maintien intégral des champs différenciés du schéma régional et du plan de Corse, avec les cas par cas et l'absence de doublon d'analyse déjà prévue au 4°.",
    "Les régimes CGCT extérieurs, l'asymétrie rédactionnelle Natura 2000 et l'application du droit de l'Union demandent leur propre contrôle. Aucun solde net des obligations des codes n'est établi.",
    "Aucune charge nouvelle identifiée : le 5° n'est pas étendu au plan de Corse, aucun dossier séparé n'est imposé lorsque l'étude d'impact remplit déjà la condition du 4°.",
)

retained(
    'R104-6',
    "Maintien des deux déclencheurs d'évaluation des prescriptions particulières de massif : élaboration et révision. Ces prescriptions peuvent adapter des seuils d'études, protéger les espaces remarquables et préciser les règles de montagne ; leur évaluation a une fonction environnementale essentielle. Le texte ne crée ni rapport périodique ni justification privée répétée ; l'actualisation proportionnée demeure possible selon R104-2.",
    "Source entière, les 1°/2° et la note CE 400420 lus. L104-1 4°, L104-3 à L104-5 et L122-26 vérifiés. La note d'annulation partielle de 2017 porte sur les évolutions de PLU et mises en compatibilité exposées, non sur une abrogation générale des prescriptions de massif. Les trois fonctions de L122-26 et sa note de 2017 restent autonomes ; l'évaluation des prescriptions ne supprime pas les possibilités de dérogation prévues par la législation de montagne ni les dérogations littorales. Aucune transition nouvelle ni extension aux simples actes d'exécution.",
    "Aucun changement à la source : maintien de l'évaluation de deux procédures de prescriptions de massif, avec les règles générales de proportionnalité et d'actualisation déjà existantes.",
    "La nécessité d'études concrètes dépend des prescriptions et de leurs incidences ; les textes de montagne extérieurs ne sont pas tous réécrits. Aucun coût évité nouveau n'est démontré.",
    "Aucune charge nouvelle identifiée : aucun troisième déclencheur, étude annuelle, registre de massif ou dossier privé supplémentaire n'est ajouté.",
)

retained(
    'R104-7',
    "Maintien de l'évaluation des élaborations et révisions des SCoT. Ces procédures fixent ou refondent les orientations territoriales ; l'analyse environnementale ne se confond pas avec une autorisation administrative redondante. Les évolutions plus limitées relèvent de R104-8 ou des autres dispositions du chapitre et l'actualisation demeure possible ; aucune obligation d'évaluation annuelle ne figure dans cette source.",
    "Deux rubriques et note de l'article 26 du décret 2021-1345 lues intégralement. L104-1 3°, L104-3 à L104-5, R104-2 et R104-8 vérifiés : ne pas étendre la systématicité des élaborations/révisions aux modifications relevant du filtre distinct. La note conserve ses règles transitoires pour les décisions environnementales antérieures au décret de 2021 ; elle n'est pas transformée en date de réforme future. Les exemptions légales et l'évaluation proportionnée ne sont ni fermées ni réécrites comme nouveaux avantages.",
    "La source entière est maintenue sans nouveau corps : deux événements structurants demeurent évalués, sans nouvelle simplification ou fusion fictive avec les modifications du SCoT.",
    "Le contenu de chaque révision et les exigences européennes restent à apprécier selon le chapitre ; le maintien de cet article ne mesure pas les coûts de planification ni leur solde national.",
    "Aucune charge nouvelle identifiée : aucun calendrier périodique, nouveau justificatif, avis complémentaire ou condition d'accès à une dispense n'est ajouté.",
)

retained(
    'R104-8',
    "Maintien intégral des deux cas d'évaluation des modifications de SCoT et de la dispense pour la seule rectification d'une erreur matérielle. Les incidences Natura 2000 et les incidences notables contrôlées au cas par cas justifient la protection ; les modifications sans tels effets ne subissent pas une étude systématique. La dispense finale est conservée pour toutes les futures procédures recevables, et non seulement pour le stock antérieur.",
    "Source entière relue, notes vides, version applicable depuis le 5 août 2026. R104-33 à R104-37 et L104-3 ont été lus en entier : personne publique responsable, avis conforme quand requis, quinze jours pour demander les compléments, deux mois depuis la réception initiale et régime tacite relèvent de ces textes propres, non du préavis de travail. Le renvoi R104-33 à R104-37 reste exact et ne doit pas être substitué par la voie R104-28 à R104-32 des autres catégories. L'exemption d'erreur matérielle ne couvre pas un changement de fond dissimulé. Aucun tableau ni compagnon documentaire dans cette source.",
    "Aucune modification : maintien des filtres d'incidences et de la dispense expresse pour erreur matérielle. Cette exemption déjà présente ne compte pas comme une nouvelle obligation supprimée.",
    "La qualification d'erreur matérielle et les incidences notables doivent être appréciées dans chaque procédure. Les autres évolutions et les obligations européennes ne sont pas abolies ni leur coût net chiffré.",
    "Aucune charge nouvelle identifiée : aucun formulaire de dispense, avis préalable pour les seules erreurs matérielles, registre ou délai additionnel n'est créé.",
)


ordered = [answers[a['number']] for a in sources]
assert len(ordered) == len(sources) == 24
with open('answer.json', 'w', encoding='utf-8') as output:
    json.dump(ordered, output, ensure_ascii=False, indent=2)
    output.write('\n')
