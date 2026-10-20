import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
    }


transition_2017 = (
    "La note source maintient le champ temporel défini au XVII de l'article 117 de la loi "
    "n° 2017-86 du 27 janvier 2017 : établissements publics de coopération intercommunale "
    "à fiscalité propre créés à compter du 1er janvier 2017 en application des I et III de "
    "l'article 35 de la loi n° 2015-991 du 7 août 2015, ou dont le périmètre a évolué à "
    "compter de cette date en application du II du même article 35. Cette disposition "
    "externe d'application n'est pas incorporée comme un nouvel alinéa de l'article. "
)
transition_2026 = (
    "La note source rappelle le VI de l'article 1 de la loi n° 2025-1129 du 26 novembre "
    "2025 : entrée en vigueur six mois après la promulgation, soit le 26 mai 2026, et "
    "exclusion des procédures d'évolution des schémas de cohérence territoriale ou des "
    "plans locaux d'urbanisme en cours à cette date. Cette règle transitoire externe "
    "reste à appliquer ; cette date historique n'est pas celle d'une réforme future. "
)
transition_2021 = (
    "La note source situe l'entrée en vigueur au 1er avril 2021, en application de "
    "l'article 7 de l'ordonnance n° 2020-744 du 17 juin 2020. "
)
transition_2023 = (
    "La note source situe l'entrée en vigueur au 1er janvier 2023, en application de "
    "l'article 40 de l'ordonnance n° 2021-1310 du 7 octobre 2021. "
)


add('L143-9', [
    "L'autorité administrative compétente de l'Etat est consultée lorsque le schéma de cohérence territoriale comprend une ou plusieurs communes littorales et que l'établissement public mentionné à l'article L. 143-16 décide d'élaborer un chapitre individualisé valant schéma de mise en valeur de la mer. La consultation porte sur la compatibilité du périmètre de ce schéma avec les enjeux d'aménagement, de protection et de mise en valeur du littoral."
],
    "Réécriture à droit constant : l'autorité consultée et les deux conditions cumulatives de la consultation sont exposées dans une première phrase ; l'objet de la consultation est détaché dans une seconde phrase du même alinéa. Aucune réforme de fond n'est introduite.",
    "Renvoi à L. 143-16 et trois enjeux littoraux conservés. La consultation reste subordonnée à la présence de communes littorales et à la décision d'élaborer le chapitre individualisé. L'expression source « périmètre de ce schéma » est conservée : son antécédent, entre le schéma de cohérence territoriale et le schéma de mise en valeur de la mer, n'est pas désigné expressément ; cette ambiguïté doit être examinée sans fixer silencieusement une portée différente. Aucune note source."
)

add('L143-10', [
    "I. - Lorsque le périmètre de l'établissement public prévu aux 1° et 2° de l'article L. 143-16 est étendu à une ou plusieurs communes ou à un ou plusieurs établissements publics de coopération intercommunale, la décision d'extension étend également le périmètre du schéma de cohérence territoriale. Cette règle s'applique aux extensions réalisées dans les conditions définies par le code général des collectivités territoriales, les articles 35 et 40 de la loi n° 2015-991 du 7 août 2015 portant nouvelle organisation territoriale de la République ou les articles L. 143-12 ou L. 143-13 du présent code.",
    "Dans le cas prévu au 3° de l'article L. 143-16, la décision d'adhésion au syndicat mixte d'une commune ou d'un établissement public de coopération intercommunale compétent en matière de schéma de cohérence territoriale étend également le périmètre du schéma, lorsque cette adhésion intervient dans les conditions définies par le code général des collectivités territoriales pour la compétence d'élaboration, de suivi et de révision du schéma. L'extension du périmètre du syndicat mixte en application des articles L. 143-12 ou L. 143-13 produit le même effet.",
    "II. - Dans les cas mentionnés au I, l'établissement public peut :",
    "1° Achever les procédures d'élaboration et d'évolution en cours sur le ou les périmètres antérieurs à l'extension, à condition que le débat prévu à l'article L. 143-18, lorsqu'il est requis, ait eu lieu avant l'extension du périmètre ;",
    "2° Engager les procédures de modification ou de mise en compatibilité des schémas approuvés dont il assure le suivi.",
    "Pour couvrir l'intégralité du périmètre étendu du schéma de cohérence territoriale, l'établissement public prescrit l'élaboration d'un schéma, ou la révision ou la modification de l'un des schémas en vigueur. Il le fait au plus tard lors de la délibération qui suit l'analyse des résultats de l'application du schéma en vigueur prévue à l'article L. 143-28."
],
    "Réécriture à droit constant : l'effet territorial de chaque décision est énoncé directement ; les pouvoirs transitoires et l'obligation de couvrir le périmètre étendu sont présentés en phrases distinctes. Les I, II, 1° et 2° et leurs alinéas sont maintenus. Aucune réforme de fond.",
    transition_2017 + "La note vise la rédaction issue du 1° du IV de l'article 117. Renvois aux 1°, 2° et 3° de L. 143-16, aux articles 35 et 40 de la loi de 2015 et à L. 143-12, L. 143-13, L. 143-18 et L. 143-28 conservés. Le débat préalable n'est exigé que s'il est requis ; la prescription reste due au plus tard à la délibération suivant l'analyse, sans nouveau délai."
)

add('L143-11', [
    "Lorsqu'une commune ou un établissement public de coopération intercommunale se retire de l'établissement public prévu à l'article L. 143-16, dans les conditions définies par le code général des collectivités territoriales, les articles 35 et 40 de la loi n° 2015-991 du 7 août 2015 portant nouvelle organisation territoriale de la République ou les articles L. 143-12 ou L. 143-13 du présent code, la décision de retrait réduit le périmètre du schéma de cohérence territoriale. Elle abroge également les dispositions du schéma applicables à la commune ou à l'établissement public de coopération intercommunale qui s'est retiré.",
    "Toutefois, par dérogation aux articles L. 5215-22, L. 5216-7 et L. 5217-7 du code général des collectivités territoriales, lorsque le périmètre d'un établissement public de coopération intercommunale à fiscalité propre est entièrement compris dans celui d'un schéma de cohérence territoriale, cet établissement se substitue de plein droit à ses communes membres ou à l'établissement dont il est issu au sein de l'établissement public prévu à l'article L. 143-16. Cette substitution ne modifie ni les attributions de l'établissement public ni le périmètre dans lequel il exerce ses compétences."
],
    "Réécriture à droit constant : les deux effets du retrait sont énoncés séparément dans le premier alinéa ; le mécanisme dérogatoire de substitution et son absence d'effet sur les compétences et leur périmètre restent au second. Aucune réforme de fond.",
    transition_2017 + "La note vise la rédaction issue du 2° du IV de l'article 117. Les trois dérogations au code général des collectivités territoriales et les deux modalités de substitution sont conservées. Ne pas confondre la couverture intégrale requise ici avec la situation traitée à L. 143-12."
)

add('L143-12', [
    "Lorsque le périmètre d'un établissement public de coopération intercommunale à fiscalité propre n'est pas entièrement compris dans celui d'un schéma de cohérence territoriale, cet établissement devient, à l'expiration d'un délai de trois mois, membre de plein droit de l'établissement public prévu à l'article L. 143-16. Le périmètre du schéma est alors étendu en conséquence. Toutefois, si l'organe délibérant de l'établissement public de coopération intercommunale à fiscalité propre s'est prononcé, dans ce délai, contre l'appartenance à cet établissement public, sa délibération réduit le périmètre du schéma de cohérence territoriale.",
    "Avant l'expiration du délai de trois mois, l'établissement public de coopération intercommunale à fiscalité propre peut se prononcer en faveur de son appartenance à l'établissement public prévu à l'article L. 143-16. Sa délibération étend alors le périmètre du schéma de cohérence territoriale."
],
    "Réécriture à droit constant : l'adhésion de plein droit, son effet territorial et l'exception fondée sur l'opposition sont répartis en trois phrases au sein du premier alinéa. L'adhésion anticipée demeure au second alinéa. Aucune réforme de fond.",
    transition_2017 + "La note vise la rédaction issue du 4° du IV de l'article 117. Le délai de trois mois, l'opposition dans ce délai et l'effet immédiat de la délibération favorable anticipée sont maintenus. La source ne précise pas dans cet article le point de départ du délai ; il n'en est pas ajouté. Le libellé de la condition de couverture territoriale est conservé, sans l'étendre à d'autres situations."
)

add('L143-13', [
    "Lorsque le périmètre d'un établissement public de coopération intercommunale à fiscalité propre comprend des communes appartenant aux périmètres de plusieurs schémas de cohérence territoriale, cet établissement devient, à l'expiration d'un délai de trois mois, membre de plein droit de l'établissement public prévu à l'article L. 143-16 dont le territoire comprend la majeure partie de sa population. Cette adhésion de plein droit n'a pas lieu si, dans ce délai, son organe délibérant s'est prononcé contre l'appartenance à cet établissement public ou en faveur de l'appartenance à l'établissement public d'un des autres schémas. Les communes membres de l'établissement public de coopération intercommunale à fiscalité propre sont retirées des établissements publics prévus au même article L. 143-16 dont celui-ci n'est pas devenu membre. Ce retrait réduit le périmètre des schémas de cohérence territoriale correspondants.",
    "Avant l'expiration du délai de trois mois, l'établissement public de coopération intercommunale à fiscalité propre peut se prononcer en faveur de son appartenance à l'établissement public prévu à l'article L. 143-16 dont le territoire comprend la majeure partie de sa population. Sa délibération étend alors le périmètre du schéma de cohérence territoriale."
],
    "Réécriture à droit constant : l'adhésion de plein droit et ses deux exceptions sont formulées dans des phrases distinctes ; les retraits corrélatifs et la possibilité d'adhésion anticipée restent dans leurs alinéas d'origine. Aucune réforme de fond.",
    transition_2017 + "La note vise la rédaction issue du 5° du IV de l'article 117. Conservation de la majeure partie de la population comme critère, du délai de trois mois et des deux choix dérogatoires. La source ne fixe ici ni le point de départ du délai ni une solution d'égalité de population entre périmètres ; aucune règle supplétive n'est inventée."
)

add('L143-14', [
    "En cas de fusion d'établissements publics prévus aux 1° et 2° de l'article L. 143-16, l'établissement public issu de la fusion exerce la compétence dans les conditions définies par le code général des collectivités territoriales. Son nouveau périmètre devient celui du schéma de cohérence territoriale. Il assure le suivi du ou des schémas antérieurement existants. Il peut achever les procédures d'élaboration et d'évolution en cours, à condition que le débat prévu à l'article L. 143-18, lorsqu'il est requis, ait eu lieu avant la fusion. Il peut également engager les procédures de modification ou de mise en compatibilité des schémas approuvés. Il prescrit l'élaboration d'un schéma couvrant l'intégralité de son périmètre au plus tard lors de la délibération qui suit l'analyse des résultats de l'application du premier schéma en vigueur, prévue à l'article L. 143-28."
],
    "Réécriture à droit constant : la compétence de l'établissement fusionné et la conséquence sur le périmètre sont distinguées ; les pouvoirs de poursuite des procédures et l'obligation d'un schéma intégral sont exprimés avec un sujet explicite. L'alinéa unique est conservé. Aucune réforme de fond.",
    transition_2017 + "La note vise la rédaction issue du 6° du IV de l'article 117. Les fusions restent limitées aux établissements des 1° et 2° de L. 143-16. Le débat antérieur à la fusion n'est exigé que s'il est requis. L'expression source « premier schéma en vigueur » et l'échéance liée à L. 143-28 sont maintenues ; l'article ne donne pas ici de règle supplémentaire pour identifier ce premier schéma."
)

add('L143-15', [
    "Lorsqu'une commune ou un établissement public de coopération intercommunale a utilisé la procédure prévue à l'article L. 143-21 sans obtenir les modifications demandées, malgré un avis favorable de l'autorité administrative compétente de l'Etat, son conseil municipal ou son organe délibérant peut décider de se retirer. Cette décision doit intervenir dans les deux mois suivant la notification qui lui est faite de la délibération approuvant le schéma.<br/>Par dérogation aux dispositions applicables du code général des collectivités territoriales, l'autorité administrative compétente de l'Etat prononce le retrait de la commune ou de l'établissement public de coopération intercommunale de l'établissement public prévu à l'article L. 143-16.<br/>Les dispositions du schéma concernant la commune ou l'établissement public de coopération intercommunale sont abrogées dès la publication de l'arrêté de l'autorité administrative compétente de l'Etat.<br/>Les alinéas précédents ne s'appliquent pas lorsque l'établissement public prévu à l'article L. 143-16 est une communauté urbaine, une métropole, une communauté d'agglomérations ou une communauté de communes."
],
    "Réécriture à droit constant : la condition ouvrant le retrait et le délai de décision sont séparés ; l'autorité qui prononce le retrait, la date d'abrogation et les exclusions sont formulées directement. Les quatre alinéas matérialisés par des sauts de ligne sont maintenus. Aucune réforme de fond.",
    "Le délai reste de deux mois à compter de la notification de l'approbation ; l'abrogation demeure attachée à la publication de l'arrêté de retrait. L'avis favorable de l'Etat et l'absence des modifications demandées restent cumulatifs. Les quatre catégories exclues sont conservées, y compris la dénomination source « communauté d'agglomérations », sans correction terminologique silencieuse. Aucune note source."
)

add('L143-16', [
    "L'élaboration du schéma de cohérence territoriale est assurée par l'un des établissements publics suivants :",
    "1° Un établissement public de coopération intercommunale ;",
    "2° Un syndicat mixte, un pôle métropolitain ou un pôle d'équilibre territorial et rural constitué exclusivement des communes et des établissements publics de coopération intercommunale compétents compris dans le périmètre du schéma ;",
    "3° Un syndicat mixte auquel toutes les communes et tous les établissements publics de coopération intercommunale compétents compris dans le périmètre du schéma de cohérence territoriale ont adhéré et transféré la compétence en matière de schéma de cohérence territoriale. Dans ce cas, seules les communes et seuls les établissements publics de coopération intercommunale compris dans le périmètre du schéma prennent part aux délibérations qui le concernent.",
    "L'établissement public mentionné aux 1°, 2° et 3° assure également l'approbation, le suivi et l'évolution du schéma ou des schémas de cohérence territoriale.",
    "La dissolution de l'établissement public, le retrait de sa compétence ou le transfert de celle-ci entraînent l'abrogation du ou des schémas, sauf lorsqu'un autre établissement public en assure le suivi.",
    "Lorsqu'une extension du périmètre d'un établissement public y intègre un ou plusieurs schémas de cohérence territoriale, cet établissement en assure le suivi."
],
    "Réécriture à droit constant : les catégories d'autorités et les conditions propres au syndicat mixte sont exprimées avec des sujets explicites ; les compétences de suivi et les effets de leur disparition sont clarifiés. Les 1°, 2°, 3° et les sept alinéas demeurent en place. Aucune réforme de fond.",
    transition_2021 + "La note demande aussi de se reporter aux conditions d'application du même article 7 : ce renvoi externe reste à respecter, sans reconstituer des conditions absentes de la source. Les catégories numérotées doivent rester stables pour L. 143-10, L. 143-14 et les autres renvois. La dissolution, le retrait ou transfert de compétence et l'exception de continuité du suivi sont tous conservés."
)

add('L143-17', [
    "L'établissement public mentionné à l'article L. 143-16 prescrit l'élaboration du schéma. Il précise, conformément à l'article L. 103-3, les objectifs poursuivis et les modalités de concertation.<br/>La délibération prévue au premier alinéa est notifiée aux personnes publiques associées mentionnées aux articles L. 132-7 et L. 132-8, ainsi qu'à la commission départementale de la préservation des espaces naturels, agricoles et forestiers prévue à l'article L. 112-1-1 du code rural et de la pêche maritime."
],
    "Réécriture à droit constant : la prescription de l'élaboration est distinguée de la définition des objectifs et de la concertation. Les destinataires de la notification et le renvoi au premier alinéa sont maintenus au second alinéa, matérialisé par un saut de ligne. Aucune réforme de fond.",
    "Conservation de tous les destinataires et des renvois à L. 143-16, L. 103-3, L. 132-7, L. 132-8 et L. 112-1-1 du code rural et de la pêche maritime. La notification n'est pas remplacée par une simple publicité. Aucune note source."
)

add('L143-18', [
    "L'organe délibérant de l'établissement public prévu à l'article L. 143-16 débat des orientations du projet d'aménagement stratégique. Ce débat a lieu au plus tard quatre mois avant l'examen du projet de schéma."
],
    "Réécriture à droit constant : l'obligation de débattre est attribuée directement à l'organe délibérant ; une seconde phrase fixe son échéance. L'alinéa unique et le délai restent identiques. Aucune réforme de fond.",
    transition_2021 + "Le délai minimal de quatre mois avant l'examen du projet est conservé ; l'anticipation permise en cas de révision par L. 143-30 reste distincte. L'intitulé de la sous-section fourni dans les métadonnées emploie encore « projet d'aménagement et de développement durables », tandis que le texte source vise le « projet d'aménagement stratégique » : discordance préexistante à coordonner dans l'intitulé, sans modifier ces métadonnées."
)

add('L143-20', [
    "L'organe délibérant de l'établissement public prévu à l'article L. 143-16 arrête le projet de schéma, puis le soumet pour avis aux personnes et organismes suivants :",
    "1° Les personnes publiques associées mentionnées aux articles L. 132-7 et L. 132-8 ;",
    "2° Les communes et les groupements de communes membres de l'établissement public ;",
    "3° Les établissements publics de coopération intercommunale directement intéressés et les communes limitrophes, à leur demande ;",
    "4° La commission prévue à l'article L. 112-1-1 du code rural et de la pêche maritime, lorsque le projet entraîne une réduction des surfaces des espaces agricoles, naturels ou forestiers ;",
    "5° Le comité de massif, lorsque le schéma est situé en tout ou partie en zone de montagne, ainsi que la commission spécialisée compétente de ce comité, lorsque le schéma prévoit la création d'une ou plusieurs unités touristiques nouvelles structurantes ;",
    "6° Le représentant de l'ensemble des organismes mentionnés à l'article L. 411-2 du code de la construction et de l'habitation propriétaires ou gestionnaires de logements situés sur le territoire de l'établissement public de coopération intercommunale compétent ou de la commune, si ces organismes ont désigné un représentant et si celui-ci en fait la demande ;",
    "7° En outre, lorsque le schéma de cohérence territoriale tient lieu de plan climat-air-énergie territorial, les organismes mentionnés au III de l'article L. 229-26 du code de l'environnement, dans les conditions prévues à ce III."
],
    "Réécriture à droit constant : l'introduction et les sept entrées forment une liste grammaticale homogène. Les demandes préalables, les conditions territoriales et les consultations supplémentaires sont rattachées expressément à chaque destinataire. Les numéros et les alinéas sont conservés. Aucune réforme de fond.",
    transition_2021 + "Les consultations sur demande des 3° et 6°, la désignation préalable du représentant au 6° et les qualifications des unités touristiques nouvelles structurantes au 5° sont conservées. Incohérence préexistante : L. 143-33 vise le 6° du présent article pour les unités touristiques nouvelles, alors que leur consultation est au 5°. Les deux numéros restent inchangés dans les propositions ; une coordination expresse de ce renvoi est à examiner."
)

add('L143-21', [
    "Une commune ou un groupement de communes membre de l'établissement public prévu à l'article L. 143-16 peut saisir l'autorité administrative compétente de l'Etat lorsque cette commune ou ce groupement estime que les dispositions du projet de schéma compromettent l'un de ses intérêts essentiels en lui imposant, notamment, des nuisances ou des contraintes excessives. La saisine intervient au plus tard trois mois à compter de la transmission du projet de schéma, par une délibération motivée précisant les modifications demandées à ce projet.<br/>L'autorité administrative compétente de l'Etat consulte la commission de conciliation prévue à l'article L. 132-14, puis rend un avis motivé."
],
    "Réécriture à droit constant : la faculté de saisine, sa condition et ses modalités sont exprimées en deux phrases ; la consultation de la commission et l'avis de l'Etat sont placés dans leur ordre procédural. Les deux alinéas sont maintenus. Aucune réforme de fond.",
    "Le délai de trois mois reste calculé à compter de la transmission du projet. La délibération et l'avis demeurent tous deux motivés ; la délibération doit préciser les modifications demandées. Les nuisances et contraintes restent des exemples, et non une liste fermée. Coordonner avec la faculté de retrait de L. 143-15 sans modifier ses exclusions. Aucune note source."
)

add('L143-22', [
    "Le président de l'établissement public prévu à l'article L. 143-16 soumet le projet arrêté de schéma de cohérence territoriale à une enquête publique conduite conformément au chapitre III du titre II du livre Ier du code de l'environnement.",
    "Par décision motivée, le président peut remplacer l'enquête publique par la participation du public par voie électronique prévue à l'article L. 123-19 du code de l'environnement. Le dossier soumis à cette participation est également consultable sur support papier, aux horaires d'ouverture, dans les mairies concernées."
],
    "Réécriture à droit constant : le président est placé comme sujet de la mise à l'enquête ; la substitution facultative et son exigence de motivation sont formulées directement. La consultation sur papier reste au second alinéa. Aucune réforme de fond.",
    transition_2026 + "Les deux modalités de participation et le support papier en mairie sont intégralement maintenus. Le second alinéa n'est pas déplacé : L. 143-23 y renvoie expressément. La décision motivée reste nécessaire pour substituer la voie électronique à l'enquête."
)

add('L143-23', [
    "A l'issue de l'enquête publique ou de la participation du public par voie électronique organisée en application du second alinéa de l'article L. 143-22, l'organe délibérant de l'établissement public prévu à l'article L. 143-16 approuve le schéma de cohérence territoriale. Avant cette approbation, le schéma peut être modifié pour tenir compte des avis joints au dossier, des observations du public et, le cas échéant, du rapport du commissaire ou de la commission d'enquête.",
    "L'établissement public tient le schéma de cohérence territoriale approuvé à la disposition du public."
],
    "Réécriture à droit constant : l'autorité d'approbation est nommée en sujet et les modifications possibles sont exposées dans une phrase distincte du même alinéa. La mise à disposition du schéma approuvé demeure au second alinéa. Aucune réforme de fond.",
    transition_2026 + "Renvoi au second alinéa de L. 143-22 conservé. Les trois catégories d'éléments susceptibles de justifier une modification sont maintenues, avec le rapport seulement le cas échéant. L'approbation reste distincte des conditions du caractère exécutoire fixées à L. 143-24 et L. 143-25."
)

add('L143-24', [
    "I. - Par dérogation à l'article L. 2131-1 du code général des collectivités territoriales :",
    "1° Le schéma de cohérence territoriale et la délibération qui l'approuve font l'objet d'une publication sur le portail national de l'urbanisme prévu à l'article L. 133-1 du présent code ;",
    "2° Dès lors que cette publication a eu lieu, le schéma et la délibération deviennent exécutoires deux mois après leur transmission à l'autorité administrative compétente de l'Etat, sauf si celle-ci a décidé, dans ce délai, de mettre en œuvre l'article L. 143-25.",
    "II. - Si la publication prévue au 1° du I est empêchée par le fonctionnement du portail national de l'urbanisme ou par des difficultés techniques avérées, le schéma et la délibération peuvent être rendus publics dans les conditions prévues au III ou au IV de l'article L. 2131-1 du code général des collectivités territoriales.",
    "Le schéma et la délibération deviennent alors exécutoires dans les conditions prévues au 2° du I du présent article.",
    "L'établissement public mentionné à l'article L. 143-16 informe l'autorité administrative compétente de l'Etat des difficultés rencontrées. Le schéma et la délibération doivent être publiés sur le portail national de l'urbanisme dans les six mois suivant la date à laquelle ils sont devenus exécutoires.",
    "III. - Le présent article s'applique également aux évolutions du schéma de cohérence territoriale et aux délibérations qui les approuvent."
],
    "Réécriture à droit constant : les deux actes à publier sont désignés explicitement, et le régime de secours technique est exprimé sous une condition directe. Les I, II, III, les 1° et 2° ainsi que les alinéas sont conservés. Aucune réforme de fond.",
    transition_2023 + "Délai de deux mois après transmission, réserve d'intervention de l'Etat et délai de six mois après l'acquisition du caractère exécutoire conservés. La publicité de secours demeure limitée aux obstacles de fonctionnement du portail ou aux difficultés techniques avérées ; elle ne dispense ni d'informer l'Etat ni de publier ensuite sur le portail. Renvois internes inchangés, notamment ceux utilisés par L. 143-25."
)

add('L143-25', [
    "Dans le délai de deux mois prévu à l'article L. 143-24, l'autorité administrative compétente de l'Etat notifie à l'établissement public prévu à l'article L. 143-16, par lettre motivée, les modifications qu'elle estime nécessaires lorsque les dispositions du schéma :",
    "1° Sont incompatibles avec les prescriptions particulières prévues à l'article L. 122-26 ou, en l'absence de telles prescriptions, avec les dispositions particulières aux zones de montagne et au littoral mentionnées à l'article L. 131-1 ;",
    "2° Compromettent gravement les principes énoncés à l'article L. 101-2, sont contraires à un projet d'intérêt général, autorisent une consommation excessive de l'espace, notamment faute de prévoir la densification des secteurs desservis par les transports ou les équipements collectifs, ou prennent insuffisamment en compte les enjeux de préservation ou de remise en bon état des continuités écologiques.",
    "Le schéma devient exécutoire seulement après la publication des modifications demandées et de la délibération qui les approuve, dans les conditions prévues au 1° du I ou au II de l'article L. 143-24, et après leur transmission à l'autorité administrative compétente de l'Etat."
],
    "Réécriture à droit constant : le délai est rattaché explicitement à L. 143-24 et les conditions de l'intervention de l'Etat sont reformulées sans modifier leur portée. La publication et la transmission sont présentées comme deux conditions cumulatives du caractère exécutoire. Aucune réforme de fond : le motif existant relatif à la densification est conservé, sans lui ajouter les mesures destinées à L. 151-4 et L. 151-26.",
    transition_2023 + "Conservation des prescriptions particulières prioritaires et du régime applicable à défaut, des quatre motifs alternatifs du 2°, de la gravité requise pour l'atteinte aux principes de L. 101-2 et du caractère illustratif du défaut de densification. Les renvois au 1° du I et au II de L. 143-24 restent exacts. Les réformes d'enveloppes de densification prévues par coordination.json relèvent des articles qui y sont désignés, hors de ce lot."
)

add('L143-27', [
    "Une fois le schéma de cohérence territoriale exécutoire, l'établissement public prévu à l'article L. 143-16 le transmet aux personnes publiques associées, ainsi qu'aux établissements publics de coopération intercommunale compétents en matière de plan local d'urbanisme et aux communes compris dans son périmètre."
],
    "Réécriture à droit constant : le caractère exécutoire est placé en tête de phrase comme préalable à la transmission. L'obligation de transmission et tous ses destinataires sont maintenus dans l'alinéa unique. Aucune réforme de fond.",
    "Les personnes publiques associées restent destinataires, de même que les établissements publics compétents en matière de plan local d'urbanisme et les communes compris dans le périmètre. Le possessif source « son périmètre » est conservé : l'article n'en désigne pas expressément l'antécédent ; cette ambiguïté doit être examinée notamment pour le syndicat mixte du 3° de L. 143-16, sans élargir ou restreindre silencieusement les destinataires. Aucun délai de transmission nouveau n'est ajouté. Aucune note source."
)

add('L143-28', [
    "L'établissement public prévu à l'article L. 143-16 analyse les résultats de l'application du schéma de cohérence territoriale au plus tard dix ans après la délibération qui approuve le schéma, la dernière délibération portant révision complète de celui-ci ou la délibération qui a décidé son maintien en vigueur en application du présent article. Cette analyse porte notamment sur l'environnement, les transports et les déplacements, la maîtrise de la consommation de l'espace, la réduction du rythme de l'artificialisation des sols, les implantations commerciales et, en zone de montagne, la réhabilitation de l'immobilier de loisir et les unités touristiques nouvelles structurantes. En matière de logement, elle porte également, dans le périmètre du schéma, sur le nombre de logements livrés, l'évolution des loyers, les délais d'instruction des autorisations d'urbanisme et de livraison des logements ainsi que sur les charges supportées par leurs occupants.",
    "L'établissement public communique cette analyse au public, à l'autorité administrative compétente de l'Etat et à l'autorité administrative compétente en matière d'environnement mentionnée à l'article L. 104-6. Sur la base de cette analyse et, le cas échéant, du débat mentionné au troisième alinéa, l'établissement public prévu à l'article L. 143-16 délibère sur le maintien en vigueur du schéma de cohérence territoriale ou sur sa révision.",
    "Lorsque le périmètre du schéma de cohérence territoriale est identique à celui d'un plan local d'urbanisme intercommunal, l'analyse examine également l'opportunité d'élargir le périmètre du schéma, en lien avec les territoires limitrophes. Dans ce cas, avant de décider du maintien en vigueur du schéma ou de sa révision, l'organe délibérant de l'établissement public prévu à l'article L. 143-16 débat spécifiquement de l'évolution du périmètre du schéma."
],
    "A droit constant, l'auteur de l'analyse est explicité et les thèmes examinés sont détachés de la phrase fixant l'échéance ; la communication, la décision et le débat territorial particulier restent dans leurs trois alinéas d'origine. Réforme de fond : conformément au suivi des résultats prévu par le volet logement de policy.json, l'analyse doit aussi examiner les logements livrés, les loyers, les délais et les charges des occupants. Cette obligation est rattachée à l'article qui organise l'évaluation du schéma.",
    "Conservation du délai maximal de dix ans, des trois événements de référence, de la qualification de révision complète et de tous les thèmes d'analyse existants. Les indicateurs de logement ajoutés demandent une coordination du recueil et des méthodes de mesure avec les communes et les services d'instruction ainsi qu'avec le diagnostic de L. 151-4 mentionné dans coordination.json ; aucun objectif chiffré, budget ou effet automatique sur les loyers n'est fixé. Le troisième alinéa reste le troisième pour le renvoi du deuxième ; l'identité des périmètres demeure la condition du débat spécifique. La source ne prévoit ici ni caducité automatique ni sanction du dépassement du délai : aucune n'est ajoutée. Aucune note source."
)

add('L143-29', [
    "L'établissement public chargé de l'élaboration du schéma de cohérence territoriale, mentionné à l'article L. 143-16, doit réviser ce schéma lorsqu'il envisage de modifier les orientations définies par le projet d'aménagement stratégique. Cette obligation ne s'applique pas dans les cas prévus au second alinéa de l'article L. 143-32 ni dans les autres cas prévus par la loi."
],
    "Réécriture à droit constant : l'établissement responsable de la révision est nommé en sujet ; l'obligation et ses exceptions sont distinguées dans deux phrases du même alinéa. Aucune réforme de fond.",
    transition_2026 + "Le renvoi vise toujours le second alinéa de L. 143-32, qui conserve sa place, ainsi que les autres exceptions légales sans en dresser une liste prétendument exhaustive. Le critère de révision reste le changement des orientations du projet d'aménagement stratégique."
)

add('L143-30', [
    "L'organe délibérant de l'établissement public prescrit la révision par délibération. La procédure suit les règles d'élaboration du schéma définies aux articles L. 143-17 à L. 143-27.",
    "Toutefois, dès la mise en révision du schéma, l'organe délibérant peut tenir le débat sur les orientations du projet d'aménagement stratégique prévu à l'article L. 143-18."
],
    "Réécriture à droit constant : la compétence de prescription est exprimée à la voix active, et l'anticipation du débat est formulée comme une faculté. La règle générale et la dérogation restent dans deux alinéas distincts. Aucune réforme de fond.",
    transition_2021 + "La plage L. 143-17 à L. 143-27 est conservée telle que dans la source, sans la renuméroter en fonction des articles présents au lot. La possibilité d'organiser le débat dès la mise en révision reste facultative et se coordonne avec L. 143-18."
)

add('L143-31', [
    "Pendant la période comprise entre la mise en révision d'un schéma de cohérence territoriale et l'approbation de cette révision, les autorités compétentes peuvent décider une ou plusieurs modifications ou mises en compatibilité du schéma."
],
    "Réécriture à droit constant : une construction active remplace la tournure impersonnelle et délimite explicitement la période pendant laquelle des procédures parallèles peuvent être décidées. La pluralité des modifications ou mises en compatibilité est conservée. Aucune réforme de fond.",
    "Les deux bornes restent la mise en révision et l'approbation de cette révision. La désignation générale des autorités compétentes ne transfère pas de compétence : leurs attributions respectives demeurent déterminées par les procédures concernées, notamment L. 143-33. Aucune note source."
)

add('L143-32', [
    "Le schéma de cohérence territoriale relève de la procédure de modification définie aux articles L. 143-33 à L. 143-36, sauf lorsqu'une révision est requise par l'article L. 143-29.",
    "Par dérogation à l'article L. 143-29, les changements des orientations du projet d'aménagement stratégique relèvent également de cette procédure de modification lorsqu'ils ont pour objet de soutenir le développement de la production d'énergie renouvelable au sens de l'article L. 211-2 du code de l'énergie, de la production d'hydrogène renouvelable ou bas-carbone ou du stockage d'électricité, ou de définir des zones d'accélération pour l'implantation d'installations terrestres de production d'énergies renouvelables mentionnées à l'article L. 141-5-3 du même code."
],
    "Réécriture à droit constant : l'articulation entre modification et révision est énoncée directement ; les objets énergétiques ouvrant la dérogation sont rattachés à une condition commune. Les deux alinéas restent en place pour préserver le renvoi de L. 143-29. Aucune réforme de fond.",
    "Conservation de L. 143-33 à L. 143-36 et des renvois au code de l'énergie. Les productions d'énergie renouvelable, d'hydrogène renouvelable ou bas-carbone, le stockage d'électricité et les zones d'accélération restent des objets distincts ; les installations visées pour les zones demeurent terrestres. Aucune note source n'accompagne cet article, dont les métadonnées donnent le 26 mai 2026 comme début de validité : pour les procédures en cours, vérifier son articulation avec le VI de l'article 1 de la loi n° 2025-1129, rappelé aux articles voisins, sans déduire une transition nouvelle de la seule date des métadonnées."
)

add('L143-33', [
    "Le président de l'établissement public prévu à l'article L. 143-16 prend l'initiative de la procédure de modification et établit le projet de modification.",
    "Avant la mise du dossier à la disposition du public, l'ouverture de l'enquête publique ou celle de la participation du public par voie électronique, le président de l'établissement public notifie le projet de modification à l'autorité administrative compétente de l'Etat et aux personnes publiques associées mentionnées aux articles L. 132-7 et L. 132-8. Si le projet prévoit la création d'une ou plusieurs unités touristiques nouvelles, il est également soumis aux avis prévus au 6° de l'article L. 143-20."
],
    "Réécriture à droit constant : le président est désigné comme auteur de l'initiative et du projet ; les trois événements avant lesquels la notification doit intervenir sont présentés de manière parallèle. Les deux alinéas restent en place. Aucune réforme de fond ni correction silencieuse du renvoi source.",
    transition_2026 + "Incohérence préexistante confirmée par la lecture intégrale de L. 143-20 : le 6° vise le représentant des organismes de logement social, tandis que la consultation du comité de massif et de sa commission spécialisée pour les unités touristiques nouvelles structurantes figure au 5°. Le renvoi au 6° est conservé dans le texte proposé ; sa correction vers le 5° et l'articulation entre « unités touristiques nouvelles » et « structurantes » nécessitent une coordination expresse. L'antériorité de la notification et tous ses destinataires sont maintenus."
)

add('L143-34', [
    "I. - Le président de l'établissement public mentionné à l'article L. 143-16 met le projet de modification à la disposition du public. Il peut remplacer cette mise à disposition par une procédure de participation du public au sens de l'article L. 123-19 du code de l'environnement ou par une enquête publique.",
    "Si le projet de modification est soumis à une évaluation environnementale en application de l'article L. 104-1 du présent code, le président doit recourir à la participation du public par voie électronique ou à l'enquête publique.",
    "Si la modification ne concerne que certaines communes, l'enquête publique, la participation du public par voie électronique ou la mise à disposition du public peut être organisée uniquement sur le territoire de ces communes.",
    "II. - Le public dispose, pendant un mois, du projet de modification, de l'exposé de ses motifs et, le cas échéant, des avis émis par les personnes publiques associées mentionnées aux articles L. 132-7 et L. 132-8. Les conditions de cette mise à disposition doivent lui permettre de formuler des observations. Celles-ci sont enregistrées et conservées.",
    "L'organe délibérant de l'établissement public mentionné à l'article L. 143-16 précise les modalités de la mise à disposition. Ces modalités sont portées à la connaissance du public au moins huit jours avant le début de la mise à disposition.",
    "A l'issue de la mise à disposition, le président de l'établissement public présente à l'organe délibérant le bilan des observations formulées. L'organe délibérant adopte le projet, après l'avoir, le cas échéant, modifié pour tenir compte des avis émis et des observations formulées lors de la mise à disposition.",
    "III. - L'enquête publique prévue au I est conduite conformément au chapitre III du titre II du livre Ier du code de l'environnement.",
    "Les avis des personnes publiques associées mentionnées aux articles L. 132-7 et L. 132-8 du présent code sont joints au dossier d'enquête publique ou, le cas échéant, soumis à la procédure de participation du public par voie électronique.",
    "En cas de participation du public par voie électronique, le dossier est également consultable sur support papier, aux horaires d'ouverture, dans les mairies concernées."
],
    "Réécriture à droit constant : les responsabilités du président et de l'organe délibérant sont explicites ; les obligations, les choix de procédure et la limitation territoriale facultative sont distingués. Les I, II, III et les neuf alinéas sont conservés, avec tous les documents, délais et supports de consultation. Aucune réforme de fond.",
    transition_2026 + "Le mois de mise à disposition, l'annonce au moins huit jours avant son début, l'enregistrement et la conservation des observations, l'évaluation environnementale imposant une participation électronique ou une enquête et la consultation papier en mairie sont tous maintenus. La lecture du corpus confirme que L. 143-35 prévoit aussi une approbation par délibération à l'issue de chacune des trois procédures ; cette articulation avec l'adoption prévue au dernier alinéa du II doit être contrôlée, sans supprimer ni fusionner silencieusement ces dispositions."
)


assert len(sources) == 24
assert set(drafts) == {source['number'] for source in sources}
answer = []
for source in sources:
    draft = drafts[source['number']]
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': source['number'],
        **draft,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
