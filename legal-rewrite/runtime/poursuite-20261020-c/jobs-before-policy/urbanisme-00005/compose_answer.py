import json
from pathlib import Path


DRAFTS = {
    "L131-10": (
        """<p>Les documents d'urbanisme qui s'appliquent aux territoires frontaliers doivent prendre en compte l'occupation des sols dans les territoires des États limitrophes.</p>""",
        "Réécriture à droit constant : l'obligation de prise en compte est formulée expressément et rattachée aux documents applicables aux territoires frontaliers. Aucune obligation de compatibilité avec un document étranger n'est ajoutée.",
        "Le champ des territoires frontaliers et la référence à l'occupation des sols des États limitrophes sont conservés. Aucune réforme de fond de policy.json ne modifie cette obligation."
    ),
    "L132-1": (
        """<p>L'État veille, dans les conditions précisées par le présent titre, à ce que les principes définis à l'article L. 101-2 soient respectés et que les projets d'intérêt général ainsi que les opérations d'intérêt national soient pris en compte.</p>""",
        "Réécriture à droit constant : les deux objets du contrôle de l'État sont formulés distinctement, en maintenant la différence entre respect des principes et prise en compte des projets et opérations.",
        "Renvoi à L. 101-2 et encadrement par le présent titre conservés. Les orientations de densification ne dispensent pas de ces principes ni de la prise en compte des projets d'intérêt général et des opérations d'intérêt national."
    ),
    "L132-2": (
        """<p>L'autorité administrative compétente de l'État porte à la connaissance des communes ou de leurs groupements compétents les éléments suivants :</p>
<p>1° Le cadre législatif et réglementaire qu'ils doivent respecter ;</p>
<p>2° Les projets des collectivités territoriales et de l'État, qu'ils soient en cours d'élaboration ou existants.</p>
<p>Elle leur transmet également, à titre d'information, toutes les études techniques dont elle dispose et qui sont nécessaires à l'exercice de leur compétence en matière d'urbanisme.</p>
<p>Un retard ou une omission dans la transmission de ces informations n'a aucun effet sur les procédures engagées par les communes ou leurs groupements.</p>""",
        "Réécriture à droit constant : l'autorité qui informe les collectivités est identifiée, les deux catégories d'éléments restent numérotées et la transmission des études est distinguée de leur portée informative. L'absence d'effet procédural d'une transmission tardive ou omise est maintenue.",
        "Les 1° et 2° et les alinéas relatifs aux études et à l'absence d'effet sur les procédures restent dans le même ordre. L'obligation porte sur toutes les études à la fois disponibles et nécessaires. Coordination avec L. 132-3 et L. 133-3 : le porter à connaissance demeure distinct de la diffusion publique des servitudes protégées."
    ),
    "L132-3": (
        """<p>Les communes ou leurs groupements compétents mettent à la disposition du public les informations qui leur ont été portées à connaissance. Ils peuvent également annexer au dossier d'enquête publique tout ou partie des pièces correspondantes.</p>""",
        "Réécriture à droit constant : les communes et leurs groupements deviennent les sujets explicites de l'obligation d'accès public et de la faculté d'annexer les pièces au dossier d'enquête.",
        "L'accès public reste obligatoire ; l'annexion au dossier d'enquête publique reste facultative et peut porter sur une partie seulement des pièces. La coordination avec L. 133-3 doit préserver les restrictions de diffusion des informations protégées sans supprimer leur transmission aux autorités compétentes."
    ),
    "L132-4": (
        """<p>Les maires et les présidents d'établissements publics de coopération intercommunale compétents en matière de politique locale de l'habitat peuvent demander à l'autorité administrative compétente de l'État la liste des immeubles appartenant à l'État et à ses établissements publics qui sont situés sur le territoire des communes où ils exercent leur compétence. Cette autorité leur transmet la liste demandée.</p>""",
        "Réécriture à droit constant : la demande des élus et l'obligation de transmission de l'État sont exprimées en deux phrases. Les immeubles concernés restent définis par leur propriétaire et leur localisation.",
        "Conserver les deux catégories de destinataires, la compétence en matière de politique locale de l'habitat, le périmètre communal de leur compétence et les immeubles de l'État comme ceux de ses établissements publics. Aucun transfert de propriété ni financement par cession n'est créé."
    ),
    "L132-4-1": (
        """<p>Lorsqu'un groupement de communes compétent le demande, l'autorité administrative compétente de l'État lui transmet une note d'enjeux exposant les politiques à mettre en œuvre sur le territoire concerné par le document d'urbanisme dont ce groupement est l'auteur. La note présente notamment une synthèse des enjeux à traduire dans ce document pour assurer sa compatibilité avec les documents mentionnés aux articles L. 131-1, L. 131-4, L. 131-5 et L. 131-8 et la prise en compte des documents mentionnés à l'article L. 131-2.</p>
<p>L'établissement mentionné à l'article L. 143-16 présente la demande prévue au premier alinéa à l'occasion de la notification prévue à l'article L. 143-17. En l'absence de schéma de cohérence territoriale, l'établissement public de coopération intercommunale compétent présente cette demande à l'occasion de la notification prévue à l'article L. 153-11.</p>
<p>Un retard ou une omission dans la transmission de cette note n'a aucun effet sur les procédures engagées par le groupement compétent.</p>""",
        "Réécriture à droit constant : la note, son contenu et ses deux niveaux d'exigence sont explicités ; les deux autorités et les notifications correspondant à leur demande sont réparties en deux phrases au sein du deuxième alinéa. Les trois alinéas et l'absence d'effet d'un retard ou d'une omission sont conservés.",
        "Renvois à L. 131-1, L. 131-4, L. 131-5, L. 131-8 pour la compatibilité et à L. 131-2 pour la prise en compte maintenus ; les notifications de L. 143-17 et L. 153-11 ne sont pas interverties. La note source relative à l'article 7 de l'ordonnance n° 2020-745 du 17 juin 2020 reste applicable : ces dispositions concernent les SCoT, PLU, documents en tenant lieu et cartes communales dont l'élaboration ou la révision est engagée à compter du 1er avril 2021. L'établissement de L. 143-16 ayant prescrit une élaboration ou une révision avant cette date peut opter pour la rédaction issue de cette ordonnance tant que le projet prévu à L. 143-20 n'est pas arrêté, à condition que le schéma entre en vigueur à compter du 1er avril 2021. Il s'agit d'une transition historique, non d'une date d'entrée en vigueur de la réforme proposée."
    ),
    "L132-4-2": (
        """<p>Lorsque les bois et forêts d'un territoire sont classés à risque d'incendie au sens de l'article L. 132-1 du code forestier, ou réputés particulièrement exposés aux risques d'incendie au sens de l'article L. 133-1 du même code, l'autorité administrative compétente de l'État adresse aux communes ou à leurs groupements compétents de ce territoire des recommandations techniques pour réduire la vulnérabilité des constructions aux incendies de forêt, de surfaces agricoles et de végétation.</p>""",
        "Réécriture à droit constant : les deux qualifications forestières sont présentées comme les conditions alternatives de l'envoi des recommandations, dont l'auteur, les destinataires et l'objet sont explicités.",
        "Les renvois L. 132-1 et L. 133-1 visent le code forestier, et non les articles homonymes du code de l'urbanisme. Les trois origines d'incendie sont maintenues. Ces recommandations ne sont pas transformées en prescriptions opposables par la réforme du certificat parcellaire."
    ),
    "L132-5": (
        """<p>Selon les besoins, les services déconcentrés de l'État peuvent être mis gratuitement à la disposition des communes ou des groupements de communes compétents pour l'élaboration, la modification ou la révision des schémas de cohérence territoriale, des plans locaux d'urbanisme ou de tout autre document d'urbanisme.</p>""",
        "Réécriture à droit constant : la condition tenant aux besoins et la gratuité sont rapprochées de la faculté de mise à disposition. Les trois opérations sur les documents et leur champ complet sont conservés.",
        "La mise à disposition demeure facultative et gratuite, pour les communes ou groupements compétents. Coordination avec L. 132-15 : la prise en charge des études n'écarte pas cette faculté ; aucune ressource budgétaire nouvelle n'est présumée."
    ),
    "L132-6": (
        """<p>Les communes, les établissements publics de coopération intercommunale et les collectivités territoriales peuvent créer des agences d'urbanisme avec l'État et les établissements publics ou d'autres organismes qui contribuent à l'aménagement et au développement de leur territoire. Ces agences sont des organismes de réflexion, d'études et d'accompagnement des politiques publiques.</p>
<p>Ces agences d'ingénierie partenariale exercent notamment les missions suivantes :</p>
<p>1° Suivre les évolutions urbaines et développer l'observation territoriale ;</p>
<p>2° Participer à la définition des politiques d'aménagement et de développement ainsi qu'à l'élaboration des documents d'urbanisme et de planification qui leur sont liés, notamment les schémas de cohérence territoriale et les plans locaux d'urbanisme intercommunaux ;</p>
<p>3° Préparer les projets d'agglomération métropolitains et territoriaux, dans un souci d'approche intégrée et d'harmonisation des politiques publiques ;</p>
<p>4° Contribuer à diffuser l'innovation, les démarches et les outils du développement territorial durable et la qualité paysagère et urbaine ;</p>
<p>5° Accompagner les coopérations transfrontalières et les coopérations décentralisées liées aux stratégies urbaines ;</p>
<p>6° Contribuer à la mise en place des observatoires de l'habitat et du foncier prévus au III de l'article L. 302-1 du code de la construction et de l'habitation ;</p>
<p>7° Apporter ponctuellement une ingénierie dans les territoires situés à proximité de leur périmètre d'action, dans le cadre d'un contrat de projet partenarial d'aménagement ou d'une convention d'opération de revitalisation de territoire.</p>
<p>Les agences peuvent être constituées sous la forme d'une association ou d'un groupement d'intérêt public. Les groupements d'intérêt public sont soumis au chapitre II de la loi n° 2011-525 du 17 mai 2011 de simplification et d'amélioration de la qualité du droit.</p>
<p>Un commissaire du Gouvernement est nommé auprès du groupement lorsque la part de la participation de l'État dépasse un montant fixé par décret en Conseil d'État.</p>""",
        "Réécriture à droit constant : la création et la nature des agences sont séparées dans le premier alinéa ; les sept missions restent énumérées intégralement. Le pronom désignant les groupements d'intérêt public est remplacé par leur nom et la condition de nomination du commissaire est reformulée directement.",
        "Les 1° à 7° restent dans leur ordre. L'intervention du 7° demeure ponctuelle, proche du périmètre d'action et liée à l'un des deux instruments cités. Renvoi au III de L. 302-1 du CCH et au chapitre II de la loi n° 2011-525 du 17 mai 2011 conservés. Le montant déclenchant la nomination du commissaire reste renvoyé au décret en Conseil d'État ; aucun seuil n'est inventé. Le 4° conserve l'association, peu explicite dans la source, entre diffusion des outils et contribution à la qualité paysagère et urbaine."
    ),
    "L132-7": (
        """<p>Dans les conditions définies aux titres IV et V, sont associés à l'élaboration des schémas de cohérence territoriale et des plans locaux d'urbanisme : l'État ; les régions ; les départements ; les autorités organisatrices prévues à l'article L. 1231-1 du code des transports ; les établissements publics de coopération intercommunale compétents en matière de programme local de l'habitat ; les collectivités territoriales ou les établissements publics mentionnés à l'article L. 312-3 du présent code ; les établissements publics chargés d'une opération d'intérêt national ; les organismes de gestion des parcs naturels régionaux et des parcs nationaux.</p>
<p>Sont également associés les chambres de commerce et d'industrie territoriales ou, en Corse, l'établissement public du commerce et de l'industrie de Corse, les chambres de métiers, les chambres d'agriculture et, dans les communes littorales au sens de l'article L. 321-2 du code de l'environnement, les sections régionales de la conchyliculture. Les organismes mentionnés au présent alinéa assurent les liaisons avec les organisations professionnelles intéressées.</p>
<p>Est également associé le gestionnaire d'infrastructure ferroviaire qui dispose d'au moins un passage à niveau ouvert au public dans l'emprise du schéma de cohérence territoriale ou du plan local d'urbanisme.</p>""",
        "Réécriture à droit constant : les personnes associées du premier alinéa sont distinguées par des points-virgules ; l'association des organismes professionnels et du gestionnaire ferroviaire est formulée directement. Les trois alinéas conservent leurs catégories respectives.",
        "Maintenir tous les participants, l'alternative propre à la Corse, la condition littorale de L. 321-2 et le seuil d'au moins un passage à niveau ouvert au public dans l'emprise du document. Les dénominations chambres de métiers et sections régionales de la conchyliculture sont celles de la source et ne sont pas actualisées sans vérification. Les droits de ces personnes restent précisés à L. 132-11 ; la coordination du dossier de permis à L. 423-1 ne supprime pas leur association à la planification."
    ),
    "L132-8": (
        """<p>Lors de l'élaboration des schémas de cohérence territoriale, les personnes suivantes sont également associées dans les mêmes conditions :</p>
<p>1° Les syndicats mixtes de transports créés en application de l'article L. 1231-10 du code des transports, si l'établissement public qui élabore le schéma n'exerce pas les compétences définies aux articles L. 1231-10 et L. 1231-11 du même code ;</p>
<p>2° Les établissements publics chargés de l'élaboration, de la gestion et de l'approbation des schémas de cohérence territoriale limitrophes ;</p>
<p>3° Les groupements de collectivités territoriales mentionnés aux I et II de l'article L. 213-12 du code de l'environnement.</p>""",
        "Réécriture à droit constant : l'énumération est annoncée plus directement et, au 1°, le défaut de compétence est rattaché explicitement à l'établissement qui élabore le schéma. Les trois catégories et leurs renvois sont maintenus.",
        "Le 1° reste conditionné par les compétences des articles L. 1231-10 et L. 1231-11 du code des transports ; les établissements limitrophes du 2° et les groupements des I et II de L. 213-12 du code de l'environnement restent associés. Les conditions communes de L. 132-7 et les droits de L. 132-11 ne sont pas modifiés."
    ),
    "L132-9": (
        """<p>Lors de l'élaboration des plans locaux d'urbanisme, les personnes suivantes sont également associées dans les mêmes conditions :</p>
<p>1° Les syndicats d'agglomération nouvelle ;</p>
<p>2° Si le territoire concerné par le plan est situé dans le périmètre d'un schéma de cohérence territoriale, l'établissement public chargé de l'élaboration, de la gestion et de l'approbation de ce schéma ;</p>
<p>3° Si le territoire concerné par le plan n'est pas couvert par un schéma de cohérence territoriale, les établissements publics chargés de l'élaboration, de la gestion et de l'approbation des schémas de cohérence territoriale limitrophes de ce territoire.</p>""",
        "Réécriture à droit constant : les conditions territoriales des 2° et 3° précèdent les établissements à associer, afin de rendre lisible l'alternative entre un territoire couvert par un schéma et un territoire qui ne l'est pas.",
        "Les trois entrées restent à leur place, y compris la mention source des syndicats d'agglomération nouvelle, sans présumer une actualisation institutionnelle. Le 3° n'est pas étendu aux territoires déjà couverts par un SCoT. Les renvois à cet article dans L. 153-11 et les droits prévus à L. 132-11 restent cohérents."
    ),
    "L132-10": (
        """<p>Les services de l'État sont associés à l'élaboration du schéma de cohérence territoriale ou du plan local d'urbanisme à l'initiative de l'autorité chargée de cette élaboration ou à la demande de l'autorité administrative compétente de l'État.</p>""",
        "Réécriture à droit constant : les services associés deviennent le sujet de la phrase ; les deux voies de déclenchement de leur association restent expressément prévues.",
        "L'initiative de l'autorité chargée du document et la demande de l'autorité administrative compétente de l'État demeurent alternatives. La coordination des services autour d'un dossier de permis ne remplace pas cette association à l'élaboration des SCoT et des PLU."
    ),
    "L132-11": (
        """<p>Les personnes publiques associées participent à l'élaboration dans les conditions suivantes :</p>
<p>1° Elles reçoivent notification de la délibération qui prescrit l'élaboration du schéma de cohérence territoriale ou du plan local d'urbanisme ;</p>
<p>2° Pendant toute la durée de cette élaboration, elles peuvent demander à être consultées sur le projet de schéma de cohérence territoriale ou de plan local d'urbanisme ;</p>
<p>3° Elles émettent un avis sur le projet de schéma ou de plan arrêté. Cet avis est joint au dossier d'enquête publique.</p>""",
        "Réécriture à droit constant : chaque entrée comporte un sujet explicite. Au 3°, l'émission de l'avis et son annexion au dossier d'enquête sont exprimées en deux phrases sans changer le stade auquel intervient l'avis.",
        "Les 1°, 2° et 3° restent dans le même ordre : prescription, consultation pendant l'élaboration, puis avis sur le projet arrêté. L'avis n'est ni rendu conforme ni remplacé par une consultation facultative. Les catégories de personnes associées de L. 132-7 à L. 132-9 sont conservées."
    ),
    "L132-12": (
        """<p>Lorsqu'elles en font la demande, les personnes suivantes sont consultées pour l'élaboration des schémas de cohérence territoriale :</p>
<p>1° Les associations locales d'usagers agréées selon les conditions fixées par décret en Conseil d'État ;</p>
<p>2° Les associations de protection de l'environnement agréées mentionnées à l'article L. 141-1 du code de l'environnement ;</p>
<p>3° La commission départementale des espaces naturels agricoles et forestiers mentionnée à l'article L. 112-1-1 du code rural et de la pêche maritime.</p>""",
        "Réécriture à droit constant : la demande préalable est placée en tête pour rendre explicite la condition commune aux trois consultations. Les agréments, la commission et les renvois restent dans leur ordre.",
        "La note source fixe l'entrée en vigueur au 1er avril 2021 en application de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020 ; cette date historique n'est pas celle de la réforme proposée. Incohérence de dénomination préexistante à contrôler : le 3° nomme la commission départementale des espaces naturels agricoles et forestiers, alors que L. 143-17 du corpus désigne, pour le même renvoi à L. 112-1-1 du code rural et de la pêche maritime, la commission départementale de la préservation des espaces naturels, agricoles et forestiers. La dénomination de la source assignée est maintenue sans correction silencieuse."
    ),
    "L132-12-1": (
        """<p>L'établissement public mentionné à l'article L. 143-16 peut désigner des représentants d'organismes publics ou privés qui, en raison de leur activité ou de leur taille, ont vocation à contribuer à l'élaboration ou à la mise en œuvre du schéma de cohérence territoriale. Il procède à cette désignation sous réserve de l'accord des organismes concernés ou à leur demande.</p>""",
        "Réécriture à droit constant : la faculté de désignation et les critères tenant aux organismes sont exposés avant la condition d'accord ou de demande, reprise dans une seconde phrase du même alinéa.",
        "Le renvoi à L. 143-16, le caractère facultatif, les organismes publics comme privés et les critères alternatifs d'activité ou de taille sont maintenus. La contribution peut concerner l'élaboration ou la mise en œuvre. La note source conserve l'entrée en vigueur du 1er avril 2021 prévue à l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020, sans nouvelle date de réforme."
    ),
    "L132-13": (
        """<p>Lorsqu'elles en font la demande, les personnes suivantes sont consultées pour l'élaboration des plans locaux d'urbanisme :</p>
<p>1° Les associations locales d'usagers agréées selon les conditions fixées par décret en Conseil d'État ;</p>
<p>2° Les associations de protection de l'environnement agréées mentionnées à l'article L. 141-1 du code de l'environnement ;</p>
<p>3° L'établissement public de coopération intercommunale à fiscalité propre dont est membre la commune chargée de l'élaboration du plan, si cet établissement n'est pas compétent en matière de plan local d'urbanisme ;</p>
<p>4° Les établissements publics de coopération intercommunale voisins compétents en matière d'élaboration du plan d'urbanisme ;</p>
<p>5° Le représentant de l'ensemble des organismes mentionnés à l'article L. 411-2 du code de la construction et de l'habitation qui sont propriétaires ou gestionnaires de logements situés sur le territoire de la commune ou de l'établissement public de coopération intercommunale compétent ;</p>
<p>6° Lorsque le plan local d'urbanisme tient lieu de plan de mobilité, les représentants des professions et des usagers des voies et modes de transport ainsi que les associations de personnes handicapées ou dont la mobilité est réduite ;</p>
<p>7° Les communes limitrophes.</p>""",
        "Réécriture à droit constant : la condition commune de demande est annoncée en tête ; le lien d'appartenance de la commune à l'établissement du 3° et la qualité des organismes du 5° sont explicités. Au 6°, la condition tenant au plan de mobilité précède les personnes consultées.",
        "Les sept entrées gardent leur numéro et leur ordre. Le 3° vise un EPCI à fiscalité propre non compétent pour le PLU ; le 5° porte sur un représentant de l'ensemble des organismes de L. 411-2 du CCH, non sur un représentant par organisme ; le 6° reste limité au PLU tenant lieu de plan de mobilité. Le 4° conserve l'expression source plan d'urbanisme. La note source maintient le 1er avril 2021 comme entrée en vigueur historique au titre de l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020."
    ),
    "L132-14": (
        """<p>Une commission de conciliation est instituée dans chaque département. Elle a pour mission principale de rechercher un accord entre l'autorité compétente pour élaborer les schémas de cohérence territoriale, les plans locaux d'urbanisme ou les cartes communales et les autres personnes associées à cette élaboration, ou de formuler, en tant que de besoin, des propositions alternatives.</p>""",
        "Réécriture à droit constant : l'institution de la commission et sa mission principale sont exprimées en deux phrases. Le champ des trois documents, les parties à la conciliation et la possibilité de propositions alternatives sont conservés.",
        "Une commission reste instituée par département. La recherche d'accord n'est pas transformée en pouvoir de décision ou en préalable obligatoire à l'adoption des documents. Les propositions alternatives demeurent possibles en tant que de besoin."
    ),
    "L132-15": (
        """<p>Les communes ou les groupements de communes compétents pour élaborer les documents d'urbanisme prennent en charge les dépenses d'études et d'établissement de ces documents, sans préjudice de l'application de l'article L. 132-5.</p>
<p>L'État compense ces dépenses dans les conditions définies aux articles L. 1614-1 et L. 1614-3 du code général des collectivités territoriales.</p>""",
        "Réécriture à droit constant : les collectivités qui supportent les dépenses et l'État qui les compense sont les sujets explicites des deux alinéas. Le renvoi à la mise à disposition des services de l'État est maintenu.",
        "Les renvois à L. 132-5 et à L. 1614-1 et L. 1614-3 du CGCT restent intacts. La compensation demeure soumise aux conditions de ces textes, sans promesse de remboursement intégral ni montant nouveau. Les charges de la fiche parcellaire et de l'adaptation du portail devront être évaluées séparément ; elles ne sont pas réputées déjà financées par cet article."
    ),
    "L132-16": (
        """<p>Les communes et les établissements publics de coopération intercommunale inscrivent dans la section d'investissement de leur budget les dépenses qu'ils exposent pour les études, l'élaboration, la modification et la révision de leurs documents d'urbanisme, ainsi que pour la numérisation du cadastre.</p>
<p>Ces dépenses ouvrent droit aux attributions du Fonds de compensation pour la taxe sur la valeur ajoutée.</p>""",
        "Réécriture à droit constant : les communes et les établissements deviennent les sujets de l'obligation d'imputation budgétaire. L'ensemble des opérations éligibles et le droit aux attributions du fonds sont conservés dans leurs alinéas respectifs.",
        "Le champ reste limité aux dépenses citées des communes et EPCI, y compris la numérisation du cadastre, avec imputation en investissement et droit au FCTVA. Aucun taux de compensation, délai de versement ou élargissement aux charges de fonctionnement du portail n'est ajouté."
    ),
    "L133-1": (
        """<p>Le portail national de l'urbanisme est le site national qui permet, pour l'ensemble du territoire et depuis un point d'entrée unique, d'accéder par voie dématérialisée aux documents d'urbanisme, aux servitudes d'utilité publique et aux cartes de préfiguration définies aux articles L. 121-22-3 et L. 121-22-7. Ces documents, servitudes et cartes sont transmis à l'État selon les modalités prévues aux articles L. 133-2 et L. 133-3.</p>
<p>À compter de l'entrée en vigueur de la délivrance du certificat d'urbanisme sous forme de fiche parcellaire prévue à l'article L. 410-1, le portail donne également accès gratuitement à cette fiche et aux documents fondant ses indications. Cet accès respecte les restrictions de diffusion prévues à l'article L. 133-3. La consultation du portail ne vaut délivrance d'un certificat d'urbanisme que si les conditions de délivrance de la fiche parcellaire prévues à l'article L. 410-1 sont remplies ; la fiche produit alors les effets du certificat prévus au même article.</p>""",
        "Le premier alinéa est réécrit à droit constant en distinguant le rôle du portail et les transmissions qui l'alimentent. Réforme de fond par coordination avec L. 410-1 déjà retenu : le portail fournit un accès gratuit à la fiche parcellaire et à ses documents de fondement. Sa valeur de certificat reste subordonnée à sa délivrance régulière, et les restrictions de diffusion des servitudes sont préservées.",
        "Le premier alinéa reste en place ; le second est ajouté. Le renvoi à la fiche parcellaire de L. 410-1 vise la rédaction proposée déjà présente dans le corpus et coordination.json, non une modalité réputée exister dans la source en vigueur. L'application du second alinéa est alignée sur l'entrée en vigueur de cette modalité : le projet de L. 410-1 prévoit six mois suivant la publication de la loi créant son nouvel alinéa, sans date de promulgation inventée. Coordonner le décret d'enregistrement et de délivrance de L. 410-1 avec l'accès par le portail ; vérifier la datation, l'authentification, la délivrance par l'autorité compétente et l'accès en mairie. Le délai de dix-huit mois, les certificats antérieurs, les exceptions de sécurité et de salubrité et l'absence d'effet d'une simple consultation cartographique restent régis par L. 410-1. Les pièces protégées au titre de L. 133-3 ne deviennent pas publiques du seul fait de la fiche. Les charges de fonctionnement et d'interopérabilité doivent être évaluées et financées sans les présumer couvertes par le FCTVA."
    ),
    "L133-2": (
        """<p>Les communes ou leurs groupements compétents transmettent à l'État, sous format électronique et au fur et à mesure de la modification de leurs dispositions, les documents applicables sur leur territoire : schémas de cohérence territoriale, plans locaux d'urbanisme, documents en tenant lieu, cartes communales et cartes de préfiguration définies aux articles L. 121-22-3 et L. 121-22-7. Ils joignent à cette transmission les délibérations qui ont approuvé ces documents.</p>""",
        "Réécriture à droit constant : le rythme et le format de transmission précèdent l'énumération des documents, puis une seconde phrase explicite la transmission des délibérations d'approbation. Aucun document ni acte d'approbation n'est retranché.",
        "Le format électronique, la transmission au fur et à mesure des modifications, le champ territorial et les délibérations d'approbation sont maintenus. Les cartes de L. 121-22-3 et L. 121-22-7 restent distinctes des cartes communales. Ces documents alimentent le portail de L. 133-1 ; leur transmission ne vaut pas délivrance de la fiche-certificat de L. 410-1. La numérisation reste encadrée par L. 133-4."
    ),
    "L133-3": (
        """<p>Le gestionnaire de toute servitude d'utilité publique qui affecte l'utilisation du sol et figure sur une liste établie par décret en Conseil d'État transmet à l'État, sous format électronique, la servitude dont il assure la gestion, en vue de son insertion dans le portail national de l'urbanisme.</p>
<p>L'insertion de ces servitudes dans le portail ne doit porter atteinte ni à la conduite de la politique extérieure de la France, ni à la sécurité publique, ni à la défense nationale.</p>
<p>Ces dispositions ne font pas obstacle à la transmission à l'État de l'ensemble des servitudes, puis à leur porter à connaissance des communes et de leurs groupements pour l'exercice de leurs compétences en matière d'urbanisme, conformément à l'article L. 132-2.</p>""",
        "Réécriture à droit constant : le gestionnaire responsable de la transmission et les deux conditions tenant à la servitude sont explicités. Les trois intérêts protégés sont énumérés distinctement et la transmission complète aux autorités reste distinguée de la diffusion sur le portail.",
        "Les trois alinéas restent dans leur ordre : transmission électronique, limites à la publication, puis maintien du porter à connaissance de l'ensemble des servitudes. Le décret en Conseil d'État et le renvoi à L. 132-2 sont conservés. Coordination de fond portée par L. 133-1 : l'accès à la fiche parcellaire doit respecter ces mêmes restrictions ; la transmission aux autorités ne constitue pas une autorisation de publication des données protégées."
    ),
    "L133-4": (
        """<p>Un décret en Conseil d'État définit le format de numérisation à utiliser pour transmettre, en application des articles L. 133-2 et L. 133-3, les documents d'urbanisme, les servitudes d'utilité publique et les cartes de préfiguration définies aux articles L. 121-22-3 et L. 121-22-7.</p>""",
        "Réécriture à droit constant : le décret qui définit le format devient le sujet de la phrase. La finalité de transmission et les trois catégories d'objets numérisés sont intégralement maintenues.",
        "Le niveau du décret en Conseil d'État et les quatre renvois sont conservés. Le format de transmission de L. 133-2 et L. 133-3 doit être articulé avec les modalités réglementaires de la fiche parcellaire prévue dans le projet de L. 410-1 ; le présent article ne lui confère pas, à lui seul, la valeur d'un certificat."
    ),
}


def write_answer():
    sources = json.loads(Path('source.json').read_text())
    assert len(sources) == 24
    assert set(DRAFTS) == {s['number'] for s in sources}
    answer = []
    for source in sources:
        xml, reason, notes = DRAFTS[source['number']]
        item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
        item.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
        answer.append(item)
    Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    write_answer()
