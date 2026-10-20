import json
from pathlib import Path


drafts = {
    'L1441-1': (
        """<p>Tous les quatre ans, le garde des sceaux, ministre de la justice, et le ministre chargé du travail nomment conjointement les conseillers prud'hommes, pour chaque conseil de prud'hommes, collège et section. Ces nominations interviennent sur proposition des organisations syndicales et professionnelles, selon les modalités prévues au présent chapitre.</p>""",
        "Réécriture à droit constant : la périodicité et les autorités de nomination sont placées en tête ; une seconde phrase distingue la proposition des organisations de la décision conjointe des ministres. Aucune réforme de fond n'est applicable à cet article dans policy.json.",
        "Périodicité de quatre ans, compétence conjointe des deux ministres et répartition par conseil, collège et section conservées. Articulation avec le calendrier de L. 1441-2 maintenue."
    ),
    'L1441-2': (
        """<p>Pour le collège des salariés, les conseillers prud'hommes sont nommés au cours de l'année suivant chaque cycle de mesure de l'audience syndicale définie au 5° de l'article L. 2121-1. Pour le collège des employeurs, ils sont nommés au cours de l'année suivant chaque cycle de mesure de l'audience patronale définie au 6° de l'article L. 2151-1.</p>""",
        "Réécriture à droit constant : deux phrases identifient le cycle de mesure applicable à chacun des collèges, dans le même alinéa. Aucune modification de fond du calendrier n'est prévue par policy.json.",
        "Renvois au 5° de L. 2121-1 et au 6° de L. 2151-1 vérifiés dans le corpus public fourni. Le délai reste l'année suivant chaque cycle ; il n'est pas transformé en délai de douze mois."
    ),
    'L1441-3': (
        """<p>Les conditions d'application du présent chapitre sont fixées par un décret en Conseil d'État.</p>""",
        "Reformulation à droit constant de la phrase unique : les conditions d'application sont placées en sujet, en conservant la nature du décret requis. Aucune réforme de fond n'est apportée.",
        "Le recours à un décret en Conseil d'État et son champ, l'ensemble du présent chapitre, sont conservés."
    ),
    'L1441-4': (
        """<p>Le garde des sceaux, ministre de la justice, et le ministre chargé du travail fixent, pour la durée du mandat, le nombre de sièges attribués aux organisations syndicales et professionnelles par conseil de prud'hommes, collège et section. Ils tiennent compte du nombre de conseillers défini à l'article L. 1423-2. Pour les organisations syndicales de salariés, ils retiennent les suffrages obtenus par chaque organisation au niveau départemental dans le cadre de la mesure de l'audience définie au 5° de l'article L. 2121-1. Pour les organisations professionnelles d'employeurs, ils retiennent l'audience patronale prévue au 6° de l'article L. 2151-1, déterminée au niveau national.</p>
<p>Pour apprécier l'audience patronale, le nombre d'entreprises qui emploient au moins un salarié et qui adhèrent à des organisations professionnelles d'employeurs, ainsi que le nombre de salariés employés par ces mêmes entreprises, sont chacun pris en compte à hauteur de 50 %.</p>
<p>L'attribution des sièges s'effectue à la représentation proportionnelle, selon la règle de la plus forte moyenne.</p>""",
        "Réécriture à droit constant : le premier alinéa distingue le nombre de conseillers, les suffrages départementaux des salariés et l'audience nationale des employeurs. La pondération patronale et la méthode de répartition demeurent dans leurs alinéas respectifs. Aucune réforme de fond n'est introduite.",
        "Trois alinéas conservés. Pondération de 50 % pour chacun des deux critères, condition d'au moins un salarié et règle de la plus forte moyenne maintenues. Renvois à L. 1423-2, au 5° de L. 2121-1 et au 6° de L. 2151-1 vérifiés dans le corpus fourni."
    ),
    'L1441-5': (
        """<p>Une organisation syndicale ou professionnelle qui conteste la répartition du nombre de sièges effectuée en application de l'article L. 1441-4 doit saisir le Conseil d'État dans un délai de quinze jours à compter de la publication de cette répartition. À défaut, sa contestation est irrecevable.</p>""",
        "Réécriture à droit constant : l'auteur du recours, la juridiction et le point de départ du délai sont explicités ; la sanction du dépassement est énoncée dans une seconde phrase du même alinéa. Aucune réforme de fond n'est apportée.",
        "Délai de quinze jours à compter de la publication de la répartition, qualité d'organisation syndicale ou professionnelle, compétence du Conseil d'État et irrecevabilité conservés. Renvoi à L. 1441-4 maintenu."
    ),
    'L1441-6': (
        """<p>Sous réserve des conditions prévues à l'article L. 1441-7, les personnes suivantes peuvent présenter leur candidature :</p>
<p>1° Les salariés et les employeurs ;</p>
<p>2° Les personnes inscrites sur la liste des demandeurs d'emploi qui sont à la recherche d'un emploi ;</p>
<p>3° Les personnes qui ont cessé d'exercer toute activité professionnelle.</p>""",
        "Réécriture à droit constant : l'introduction exprime directement la faculté de candidature sous condition, et les catégories des 2° et 3° sont formulées avec des propositions explicites. Aucune réforme de fond n'est introduite.",
        "Les trois catégories et leurs numéros sont conservés. Au 2°, la recherche d'emploi et l'inscription sur la liste restent cumulatives. Renvoi aux conditions de L. 1441-7 maintenu."
    ),
    'L1441-7': (
        """<p>Pour être candidate, une personne doit remplir les conditions suivantes :</p>
<p>1° Posséder la nationalité française ;</p>
<p>2° N'avoir, au bulletin n° 2 du casier judiciaire, aucune mention incompatible avec l'exercice des fonctions prud'homales et ne faire l'objet d'aucune interdiction, déchéance ou incapacité relative à ses droits civiques ;</p>
<p>3° Avoir au moins vingt et un ans ;</p>
<p>4° Avoir exercé une activité professionnelle pendant deux ans ou justifier d'un mandat prud'homal dans les dix ans précédant la candidature.</p>""",
        "Réécriture à droit constant : les conditions sont rattachées à une personne candidate ; les deux exigences du 2° et le seuil d'âge sont exprimés plus directement. Les quatre subdivisions sont maintenues. Aucune réforme de fond n'est appliquée.",
        "Bulletin n° 2, âge minimal de vingt et un ans, durée de deux ans et période de dix ans conservés. Ambiguïté préexistante : le 4° place les dix ans après le mandat prud'homal, tandis que L. 1441-12 évoque expressément une activité professionnelle de deux ans dans les dix ans précédant la candidature. La rédaction ne déplace pas ce complément temporel et ne tranche pas silencieusement son champ. Les dates d'appréciation restent régies par L. 1441-8."
    ),
    'L1441-8': (
        """<p>Les conditions de candidature prévues aux 1° et 2° de l'article L. 1441-7 sont appréciées à la date de nomination.</p>
<p>Les conditions de candidature prévues aux 3° et 4° de l'article L. 1441-7, ainsi que celles qui concernent le conseil de prud'hommes, le collège et la section de candidature, sont appréciées à la date d'ouverture du dépôt des candidatures. Cette date est fixée par voie réglementaire.</p>""",
        "Réécriture à droit constant : les deux dates d'appréciation sont distinguées ; la fixation réglementaire de la date d'ouverture est énoncée dans une phrase autonome du second alinéa. Aucune réforme de fond n'est apportée.",
        "Deux alinéas et renvois aux 1° et 2°, puis aux 3° et 4° de L. 1441-7 conservés. Aucune condition n'est transférée de la date de nomination à celle d'ouverture du dépôt, ou inversement."
    ),
    'L1441-9': (
        """<p>Une personne ne peut présenter sa candidature :</p>
<p>1° Sur plus d'une des listes mentionnées à l'article L. 1441-18 ;</p>
<p>2° Dans plus d'une section ;</p>
<p>3° Dans un conseil de prud'hommes, un collège ou une section pour lesquels elle ne remplit pas les conditions de candidature ;</p>
<p>4° Dans un conseil de prud'hommes au sein duquel elle a déjà exercé cinq mandats.</p>""",
        "Réécriture à droit constant : l'interdiction est rattachée à la personne candidate et le 3° est exprimé directement par l'absence des conditions requises. Les quatre cas d'interdiction demeurent distincts. Aucune réforme de fond n'est introduite.",
        "Limites d'une liste, d'une section et de cinq mandats dans un même conseil conservées ; aucun caractère consécutif des mandats n'est ajouté. La note source prévoit, conformément au VIII de l'article 60 de la loi n° 2023-1059 du 20 novembre 2023, l'application à compter du premier renouvellement des conseillers prud'hommes suivant la promulgation de cette loi. Cette transition historique demeure applicable ; elle n'est pas une date de réforme future."
    ),
    'L1441-10': (
        """<p>Un conseiller prud'homme déclaré déchu en application de l'article L. 1442-14 ne peut présenter sa candidature.</p>
<p>Lorsqu'un conseiller prud'homme nommé refuse de se faire installer, est déclaré démissionnaire ou est réputé démissionnaire en application de l'article L. 1442-1, il ne peut présenter sa candidature pendant quatre ans. Ce délai court, selon le cas, à compter de son refus, de la décision du tribunal qui le déclare démissionnaire ou de l'expiration du délai prévu au troisième alinéa de l'article L. 1442-1.</p>""",
        "Réécriture à droit constant : les trois événements ouvrant l'interdiction de quatre ans sont séparés des points de départ correspondants, dans le même alinéa. L'interdiction liée à la déchéance reste dans le premier alinéa. Aucune réforme de fond n'est introduite.",
        "Durée de quatre ans et trois points de départ conservés. Le corpus de L. 1442-1 présente la règle de démission réputée après des sauts de ligne internes au second élément p : le renvoi textuel au troisième alinéa est maintenu sans renumérotation fondée sur les balises. Point préexistant à contrôler : L. 1442-14 distingue une déchéance assortie d'une interdiction temporaire, de dix ans au maximum, et une déchéance assortie d'une interdiction définitive ; L. 1441-10 n'explicite pas ici cette distinction. Aucune durée nouvelle n'est ajoutée pour résoudre cette articulation."
    ),
    'L1441-11': (
        """<p>Les salariés et les employeurs mentionnés au 1° de l'article L. 1441-6, à l'exception des employés de maison et de leurs employeurs, présentent leur candidature dans la section du conseil de prud'hommes dans le ressort duquel ils exercent leur activité principale ou dans la section de même nature de l'un des conseils de prud'hommes limitrophes. Les voyageurs, représentants ou placiers, ainsi que les salariés qui exercent leur activité à domicile ou en dehors de toute entreprise ou de tout établissement, peuvent également être candidats dans le conseil de prud'hommes dans le ressort duquel se trouve leur domicile ou dans l'un des conseils de prud'hommes limitrophes.</p>
<p>Les personnes mentionnées aux 2° et 3° de l'article L. 1441-6 présentent leur candidature dans la section du conseil de prud'hommes dans le ressort duquel elles exerçaient leur dernière activité professionnelle ou dans le ressort duquel se trouve leur domicile, ou dans la section de même nature de l'un des conseils de prud'hommes limitrophes.</p>
<p>Pour les employés de maison et leurs employeurs, la candidature est présentée dans la section du conseil de prud'hommes dans le ressort duquel se trouve leur domicile ou dans la section de même nature de l'un des conseils de prud'hommes limitrophes.</p>""",
        "Réécriture à droit constant : chaque alinéa identifie la catégorie de candidats et ses possibilités territoriales ; l'option supplémentaire des voyageurs, représentants, placiers et salariés travaillant à domicile ou hors entreprise demeure au premier alinéa. Aucune réforme de fond n'est prévue pour ce régime.",
        "Trois alinéas, activité principale, dernière activité professionnelle, domicile et sections de même nature conservés. Ambiguïté préexistante signalée : au deuxième alinéa, la source juxtapose par une virgule la section d'un conseil limitrophe aux conseils de la dernière activité ou du domicile, sans conjonction. La proposition explicite cette possibilité par « ou », suivant la logique des autres alinéas ; le rattachement exact des conseils limitrophes appelle un contrôle, sans ajout de ressort. La note source fixe l'entrée en vigueur de la rédaction issue du décret n° 2025-1356 du 26 décembre 2025 au 1er janvier 2026, conformément à son article 9 ; cette date historique est conservée dans le suivi, sans servir de date à une réforme future."
    ),
    'L1441-12': (
        """<p>Les personnes suivantes peuvent présenter leur candidature dans le collège des employeurs :</p>
<p>1° Les personnes qui emploient un ou plusieurs salariés pour leur propre compte ou pour le compte d'autrui ;</p>
<p>2° Le cas échéant, les conjoints collaborateurs mentionnés à l'article L. 121-4 du code de commerce pour les artisans, commerçants et professionnels libéraux et à l'article L. 321-5 du code rural et de la pêche maritime pour les agriculteurs, à condition qu'ils aient reçu un mandat exprès des personnes mentionnées au 1° et que ces personnes ne soient pas elles-mêmes candidates ;</p>
<p>3° Les associés en nom collectif, les présidents des conseils d'administration, les directeurs généraux et les directeurs, ainsi que les cadres qui détiennent, sur un service, un département ou un établissement de l'entreprise, une délégation particulière d'autorité établie par écrit et permettant de les assimiler à un employeur ;</p>
<p>4° Les personnes qui ont cessé d'exercer toute activité et dont la dernière activité professionnelle relevait des catégories mentionnées au 1° ou au 3°.</p>
<p>Pour les candidatures mentionnées au 2°, les conditions prévues à l'article L. 1441-7 doivent être remplies à la fois par l'artisan, le commerçant, le professionnel libéral ou le chef d'exploitation ou de l'entreprise agricole mandant et par son conjoint collaborateur mandataire. Pour ce conjoint, la condition d'exercice d'une activité professionnelle pendant deux ans dans les dix ans précédant la candidature, mentionnée à cet article, est toutefois remplacée par une durée équivalente d'appartenance au statut de conjoint collaborateur. Cette durée est appréciée à la date d'ouverture du dépôt des candidatures, fixée par voie réglementaire.</p>""",
        "Réécriture à droit constant : les quatre catégories restent numérotées ; le 2° identifie expressément les mandants qui ne doivent pas être candidats. Le dernier alinéa distingue les conditions communes au couple et la condition substituée pour le conjoint collaborateur. Aucune réforme de fond n'est apportée.",
        "Mandat exprès, absence de candidature du mandant, délégation particulière écrite des cadres, deux ans dans les dix ans et date réglementaire d'ouverture conservés. Au 2°, l'expression « ces personnes » est explicitée par le renvoi interne au 1°, sans ajout de catégorie. Renvois à L. 121-4 du code de commerce et L. 321-5 du code rural et de la pêche maritime maintenus, sans modification de ces codes hors lot. L'articulation temporelle avec le 4° de L. 1441-7, dont la formulation est moins explicite, reste à contrôler ; aucune harmonisation de fond n'est présumée. Les quatre catégories de mandants et les conditions applicables aux deux personnes sont toutes reprises."
    ),
    'L1441-13': (
        """<p>Les personnes suivantes peuvent présenter leur candidature dans le collège des salariés :</p>
<p>1° Les salariés qui ne sont pas cadres ;</p>
<p>2° Les cadres qui ne détiennent pas la délégation particulière d'autorité mentionnée au 3° de l'article L. 1441-12 ;</p>
<p>3° Les salariés liés par un contrat d'apprentissage ou de formation en alternance ;</p>
<p>4° Les personnes inscrites sur la liste des demandeurs d'emploi qui sont à la recherche d'un emploi ;</p>
<p>5° Les personnes mentionnées aux 1°, 2°, 3° et 4° qui ont cessé d'exercer toute activité professionnelle.</p>""",
        "Réécriture à droit constant : les catégories sont exprimées par des propositions précisant le statut des candidats, en conservant leur numérotation et la catégorie des personnes ayant cessé toute activité professionnelle. Aucune réforme de fond n'est appliquée.",
        "Cinq catégories conservées, avec exclusion des cadres détenant la délégation du 3° de L. 1441-12. Le 4° exige toujours la recherche d'un emploi et l'inscription sur la liste des demandeurs d'emploi. Aucun élargissement des contrats visés au 3° n'est effectué."
    ),
    'L1441-14': (
        """<p>Les personnes appartenant aux catégories mentionnées aux 1°, 2°, 3° et 4° de l'article L. 1423-1-2 relèvent de la section de l'encadrement du collège des salariés, sauf si elles détiennent une délégation particulière d'autorité.</p>""",
        "Réécriture à droit constant : les personnes concernées sont placées en sujet et l'exception liée à la délégation d'autorité est exprimée en fin de phrase. Aucune réforme de fond n'est introduite.",
        "Renvoi aux quatre catégories de L. 1423-1-2 vérifié dans le corpus public fourni. L'exception reste la délégation particulière d'autorité ; elle n'est pas confondue avec toute délégation de commandement figurant dans les catégories de cet article."
    ),
    'L1441-15': (
        """<p>Les employeurs et assimilés définis à l'article L. 1441-12, y compris les cadres qui détiennent une délégation particulière d'autorité, relèvent de la section de l'encadrement du collège des employeurs lorsqu'ils emploient exclusivement des salariés appartenant aux catégories définies à l'article L. 1423-1-2.</p>
<p>Les employeurs et assimilés définis à l'article L. 1441-12, y compris les cadres qui détiennent une délégation particulière d'autorité, peuvent relever de la section de l'encadrement du collège des employeurs lorsqu'ils emploient au moins un salarié appartenant aux catégories définies à l'article L. 1423-1-2.</p>""",
        "Réécriture à droit constant : les deux alinéas distinguent clairement le rattachement obligatoire en cas d'emploi exclusif des catégories visées et le rattachement facultatif en présence d'au moins un salarié de ces catégories. Aucune réforme de fond n'est apportée.",
        "Deux alinéas conservés. Les termes « relèvent » puis « peuvent relever », le champ des employeurs et assimilés incluant les cadres délégataires, et les renvois à L. 1441-12 et L. 1423-1-2 sont maintenus."
    ),
    'L1441-16': (
        """<p>La section à laquelle appartient un salarié candidat est déterminée en fonction du champ d'application de la convention ou de l'accord collectif de travail dont il relève, selon le tableau de répartition mentionné à l'article L. 1423-1-1. Cette règle ne s'applique ni aux personnes mentionnées à l'article L. 1441-14 ni aux cadres mentionnés au 3° de l'article L. 1441-12.</p>""",
        "Réécriture à droit constant : une première phrase énonce le critère conventionnel et le tableau applicable ; une seconde rend explicites les deux exceptions, dans le même alinéa. Aucune réforme de fond n'est introduite.",
        "Renvoi au tableau de L. 1423-1-1 vérifié dans le corpus fourni. Les deux exclusions, L. 1441-14 et les seuls cadres du 3° de L. 1441-12, restent distinctes et ne sont pas étendues aux autres personnes de ce 3°."
    ),
    'L1441-17': (
        """<p>Pour le collège des employeurs, les employeurs et assimilés définis à l'article L. 1441-12 choisissent une section dont relève au moins l'un de leurs salariés. Ce choix s'exerce sous réserve des dispositions de l'article L. 1441-15 relatives à la section de l'encadrement.</p>""",
        "Réécriture à droit constant : la faculté de choix est formulée par un verbe explicite, puis encadrée par la réserve relative à l'encadrement dans la même unité d'alinéa. Aucune réforme de fond n'est apportée.",
        "Le choix reste limité à une section dont relève au moins un salarié. La réserve de L. 1441-15 et la définition des employeurs et assimilés par L. 1441-12 sont conservées ; aucun libre choix d'une section sans salarié rattaché n'est créé."
    ),
    'L1441-18': (
        """<p>Les mandataires des organisations auxquelles des sièges ont été attribués en application de l'article L. 1441-4 déclarent les candidatures en déposant une liste de candidats pour chaque conseil de prud'hommes.</p>
<p>Le dépôt de cette liste s'effectue par voie dématérialisée, dans les conditions fixées par décret.</p>""",
        "Réécriture à droit constant : le mandataire devient le sujet de la déclaration effectuée par dépôt ; le second alinéa conserve séparément la modalité dématérialisée. Aucune réforme de fond n'est introduite.",
        "Deux alinéas conservés. Seuls les mandataires des organisations attributaires de sièges selon L. 1441-4 effectuent ce dépôt ; liste par conseil et renvoi à un décret maintenus."
    ),
    'L1441-19': (
        """<p>La liste de candidats présente alternativement un candidat de chaque sexe.</p>
<p>Lorsqu'une liste de candidats est incomplète, les organisations syndicales et professionnelles peuvent déroger à la règle du premier alinéa en proposant des candidats du même sexe dans la limite de 50 % du nombre de sièges qui leur sont attribués. Si ce nombre est impair, la limite est de 50 % plus un siège.</p>""",
        "Réécriture à droit constant : le principe d'alternance reste au premier alinéa ; le second relie explicitement la dérogation au caractère incomplet de la liste et énonce séparément le cas d'un nombre impair de sièges. Aucune réforme de fond n'est apportée.",
        "Deux alinéas conservés. Seuil de 50 % et formule « 50 % plus un siège » pour un nombre impair repris sans modification. Cette dernière formule laisse, pour un nombre impair, une fraction de siège dans le résultat arithmétique ; la source ne précise pas de règle d'arrondi. Ce point préexistant est signalé sans remplacer la formule par un plafond arrondi ni étendre la dérogation aux listes complètes."
    ),
    'L1441-20': (
        """<p>Le nombre de candidats figurant sur une liste ne peut dépasser le nombre de postes attribués par section et par conseil de prud'hommes.</p>""",
        "Réécriture à droit constant : l'interdiction est exprimée comme un plafond directement applicable au nombre de candidats. Aucune réforme de fond n'est introduite.",
        "Plafond apprécié par section et par conseil de prud'hommes conservé. Aucune exigence de liste complète ou de candidat supplémentaire n'est ajoutée."
    ),
    'L1441-21': (
        """<p>L'autorité administrative ne peut enregistrer les déclarations de candidatures qui, à la date de clôture du dépôt des candidatures, ne respectent pas les conditions fixées aux articles L. 1441-18 à L. 1441-20.</p>""",
        "Réécriture à droit constant : l'autorité administrative est placée en sujet et la date d'appréciation est rapprochée du respect des conditions. Aucune réforme de fond n'est apportée.",
        "Renvoi inclusif à L. 1441-18, L. 1441-19 et L. 1441-20 maintenu. Le contrôle reste apprécié à la clôture du dépôt, sans déplacement à l'ouverture ou à la nomination."
    ),
    'L1441-22': (
        """<p>Le mandataire de la liste notifie à l'employeur de chaque salarié candidat le nom du salarié qu'il entend présenter sur cette liste. Il procède à cette notification à compter de la date d'ouverture du dépôt des candidatures.</p>""",
        "Réécriture à droit constant : l'obligation de notification et son calendrier sont formulés autour du mandataire et de chaque salarié concerné. Les deux phrases restent dans le même alinéa. Aucune réforme de fond n'est introduite.",
        "Destinataire employeur du salarié candidat et point de départ à l'ouverture du dépôt conservés. Aucun délai final, mode de notification ou contenu supplémentaire n'est inventé."
    ),
    'L1441-23': (
        """<p>Lorsqu'un salarié de l'entreprise est désigné mandataire de liste dans le cadre du renouvellement prud'homal, l'employeur lui accorde le temps nécessaire à l'exercice de ces fonctions. Ce temps est assimilé à du temps de travail effectif conformément à l'article L. 1442-6.</p>
<p>L'employeur ne peut sanctionner un salarié ni rompre son contrat de travail en raison de l'exercice des fonctions de mandataire de liste. Les délégués syndicaux qui exercent ces fonctions peuvent utiliser à cette fin le crédit d'heures dont ils disposent au titre de leur mandat.</p>""",
        "Réécriture à droit constant : l'obligation d'accorder le temps nécessaire et l'interdiction de sanctionner ou de rompre sont énoncées avec l'employeur pour sujet. La faculté d'utiliser le crédit d'heures syndical reste au second alinéa. Aucune réforme de fond n'est apportée.",
        "Deux alinéas conservés. Renvoi à L. 1442-6 vérifié dans le corpus fourni : assimilation au travail effectif et garanties attachées à ce renvoi maintenues. Le temps nécessaire n'est pas transformé en quota ; aucun crédit d'heures nouveau ni régime d'autorisation de rupture n'est ajouté."
    ),
    'L1441-24': (
        """<p>Tout candidat ou mandataire de liste qui conteste une nomination effectuée dans les conditions fixées à l'article L. 1441-1 doit saisir le tribunal administratif dans un délai de dix jours à compter de cette nomination. À défaut, sa contestation est irrecevable. Le tribunal statue en premier et dernier ressort.</p>""",
        "Réécriture à droit constant : l'auteur du recours, le délai, la sanction et le degré de juridiction sont exprimés dans trois phrases du même alinéa. Aucune réforme de fond n'est introduite.",
        "Délai de dix jours à compter de la nomination, et non de sa notification ou de sa publication, conservé. Qualité de candidat ou de mandataire de liste, renvoi à L. 1441-1, compétence du tribunal administratif et jugement en premier et dernier ressort maintenus."
    ),
}


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    proposed, reason, notes = drafts[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': proposed,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
