import html
import json
from pathlib import Path


drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": "\n".join("<p>" + html.escape(p, quote=False) + "</p>" for p in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
    }


add("L332-8", [
    "Les bénéficiaires d'une autorisation de construire peuvent être tenus de verser une participation spécifique lorsque l'autorisation porte sur une installation à caractère industriel, notamment relative aux communications électroniques, ou à caractère agricole, commercial ou artisanal, et que la nature, la situation ou l'importance de cette installation nécessite la réalisation d'équipements publics exceptionnels.",
    "Si la réalisation de ces équipements ne relève pas de sa compétence, l'autorité qui délivre le permis de construire fixe le montant de la contribution après avoir obtenu l'accord de la collectivité publique chargée de ces équipements ou de son concessionnaire.",
    "Lorsque l'autorisation de construire porte sur des installations de production d'électricité à partir de l'énergie mécanique du vent dont la situation ou l'importance nécessite des moyens de détection militaires supplémentaires, ces moyens constituent un équipement public exceptionnel au sens du premier alinéa. L'autorité militaire fixe le montant de la contribution par convention.",
],
    "Réécriture à droit constant : les bénéficiaires, les conditions justifiant une participation et les autorités qui en fixent le montant sont identifiés directement. Les trois alinéas et le régime particulier des moyens de détection militaires sont conservés. Aucune réforme de fond n'est appliquée à cette participation.",
    "Le caractère exceptionnel des équipements reste une condition de la participation. L'accord de la collectivité compétente ou de son concessionnaire et la fixation conventionnelle par l'autorité militaire sont maintenus. Les orientations de densification ne créent ici aucune contribution supplémentaire."
)

add("L332-11-3", [
    "I. – Dans les zones urbaines et les zones à urbaniser délimitées par un plan local d'urbanisme ou un document d'urbanisme en tenant lieu, une convention de projet urbain partenarial peut prévoir la prise en charge de tout ou partie du coût des équipements dont la réalisation est nécessaire à une ou plusieurs opérations d'aménagement, de construction ou de transformation de bâtiments de destination autre que l'habitation en bâtiments à destination principale d'habitation. Ces équipements doivent être distincts des équipements propres mentionnés à l'article L. 332-15. La convention peut être conclue entre les propriétaires, les aménageurs, les constructeurs, les maîtres d'ouvrage et :",
    "1° Le représentant de l'État, dans le périmètre d'une opération d'intérêt national au sens de l'article L. 102-12 ;",
    "2° La collectivité territoriale ou l'établissement public cocontractant mentionné à l'article L. 312-3, dans le périmètre d'une grande opération d'urbanisme au sens de l'article L. 312-3, sauf dans le cas prévu à l'article L. 312-5-1 ;",
    "3° La commune ou l'établissement public compétent en matière de plan local d'urbanisme, dans les autres cas.",
    "II. – Lorsque des équipements publics destinés à faire l'objet d'une première convention de projet urbain partenarial desservent aussi des terrains autres que ceux mentionnés dans le projet de cette convention, l'autorité compétente fixe les modalités de partage de leur coût et délimite un périmètre de participation. Cette décision est prise par l'organe délibérant de la commune ou de l'établissement public compétent en matière de plan local d'urbanisme, par celui de la collectivité territoriale ou de l'établissement public cocontractant mentionné à l'article L. 312-3 dans le périmètre des grandes opérations d'urbanisme, sauf dans le cas prévu à l'article L. 312-5-1, ou par arrêté du représentant de l'État dans le cadre des opérations d'intérêt national. À l'intérieur de ce périmètre, les propriétaires, les aménageurs, les constructeurs ou les maîtres d'ouvrage qui réalisent une opération mentionnée au premier alinéa du I participent, par convention, au financement de ces mêmes équipements publics. Cette participation porte sur les équipements restant à réaliser comme sur ceux déjà réalisés, dès lors qu'ils répondent aux besoins des futurs habitants ou usagers des opérations concernées. Les conventions successives peuvent prévoir des programmes d'équipements publics différents lorsque les opérations attendues dans le périmètre de chacune d'elles n'ont pas les mêmes besoins en équipements.",
    "Le conseil municipal ou l'organe délibérant de l'établissement public délimite le périmètre par délibération, pour une durée maximale de quinze ans. Dans les opérations d'intérêt national, ce périmètre est délimité par arrêté préfectoral pour la même durée maximale. Dans le périmètre des grandes opérations d'urbanisme, l'organe délibérant de la collectivité territoriale ou de l'établissement public cocontractant mentionné à l'article L. 312-3 délimite le périmètre par décision ; sa durée peut dépasser quinze ans, sans excéder celle fixée par l'acte décidant de la qualification de grande opération d'urbanisme.",
    "III. – Avant la conclusion de la convention, les personnes ayant qualité pour déposer une déclaration préalable ou une demande de permis de construire ou d'aménager peuvent demander l'étude de leur projet d'aménagement, de construction ou de transformation et sa mise en débat devant l'organe délibérant. Elles adressent cette demande à la commune ou à l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme, à la collectivité territoriale ou à l'établissement public mentionné à l'article L. 312-3 dans le périmètre des grandes opérations d'urbanisme, sauf dans le cas prévu à l'article L. 312-5-1, ou au représentant de l'État dans le cadre des opérations d'intérêt national. L'autorité compétente peut accepter cette demande.",
    "La demande est accompagnée d'un dossier qui délimite le périmètre du projet, définit le projet et énumère les équipements publics à réaliser pour répondre aux besoins des futurs habitants ou usagers des constructions ou des aménagements résultant des opérations conduites dans ce périmètre.",
    "La convention ne peut mettre à la charge des propriétaires, des aménageurs, des constructeurs ou des maîtres d'ouvrage que le coût des équipements publics à réaliser pour répondre aux besoins des futurs habitants ou usagers dans le périmètre qu'elle fixe. Si la capacité des équipements programmés dépasse ces besoins, seule la fraction de leur coût proportionnelle à ces besoins peut être mise à leur charge.",
    "La convention détermine les délais de paiement. La participation peut prendre la forme d'une contribution financière ou d'apports de terrains bâtis ou non bâtis.",
    "La convention peut prévoir le versement direct de la contribution financière mentionnée à l'avant-dernier alinéa du présent III à la personne publique qui assure la maîtrise d'ouvrage des équipements publics mentionnés au troisième alinéa du présent III.",
],
    "Réécriture à droit constant : les conditions du projet urbain partenarial, la répartition des compétences et le partage du coût des équipements sont exprimés en phrases plus courtes. Les I, II et III, les 1° à 3° et les onze alinéas sont conservés, notamment les cinq alinéas du III visés par les renvois internes. Aucune réforme de fond ne modifie les conventions ou leurs charges.",
    "Conserver les deux occurrences de quinze ans et la limite particulière liée à la durée de la grande opération d'urbanisme. L'exception de l'article L. 312-5-1, vérifiée dans le corpus public, reste présente au I, au II et au III. Le dernier alinéa continue de viser l'avant-dernier et le troisième alinéa du III. Deux difficultés de la source sont conservées et signalées : le III prévoit un débat devant un organe délibérant alors que la demande peut aussi être adressée au représentant de l'État ; le II vise des équipements déjà réalisés, tandis que le plafond du troisième alinéa du III demeure formulé pour des équipements à réaliser. Leur articulation appelle un contrôle explicite, sans modification silencieuse du régime."
)

add("L332-11-4", [
    "Lorsque la taxe d'aménagement est instituée dans une commune, les constructions édifiées dans le périmètre délimité par une convention prévue à l'article L. 332-11-3 sont exclues du champ de cette taxe pendant la durée fixée par la convention. Cette durée ne peut dépasser dix ans.",
],
    "Réécriture à droit constant : la condition tenant à l'institution de la taxe est placée en tête et le plafond de dix ans fait l'objet d'une phrase distincte, dans le même alinéa. Le champ des constructions exclues demeure inchangé ; aucune baisse fiscale nouvelle n'est introduite.",
    "Maintenir la coordination avec le périmètre conventionnel de l'article L. 332-11-3. La note source, issue de l'article 28, III, H de la loi n° 2010-1658 du 29 décembre 2010, rend ces dispositions applicables aux demandes d'autorisations et déclarations préalables déposées à compter du 1er mars 2012, y compris aux modifications ultérieures au 1er mars 2012 d'une demande ou déclaration déposée avant cette date. Cette règle historique est conservée comme contexte d'application, sans être transformée en date d'une réforme future."
)

add("L332-12", [
    "Les articles L. 332-6 et L. 332-7 s'appliquent, dans les conditions suivantes, aux bénéficiaires de permis d'aménager, aux associations foncières urbaines de remembrement autorisées ou constituées d'office et aux associations foncières urbaines de projet.",
    "Les charges énumérées ci-après peuvent être imposées au bénéficiaire d'un permis d'aménager par ce permis, à une association foncière urbaine de remembrement par l'acte administratif approuvant le plan de remembrement, ou à une association foncière urbaine de projet par l'acte autorisant sa création :",
    "a) (Abrogé) ;",
    "b) La participation spécifique pour équipements publics exceptionnels, dans les conditions prévues à l'article L. 332-8 ;",
    "c) Une participation forfaitaire représentant la participation prévue à l'article L. 332-9 dans sa rédaction antérieure à l'entrée en vigueur de la loi n° 2010-1658 du 29 décembre 2010 de finances rectificative pour 2010, ainsi que les contributions énumérées au d du 2° et au 3° de l'article L. 332-6-1 dans leur rédaction antérieure à la loi n° 2014-1655 du 29 décembre 2014 de finances rectificative pour 2014. Cette participation forfaitaire ne peut être exigée dans les secteurs de la commune ou de l'établissement public de coopération intercommunale où l'article L. 331-15 est appliqué ;",
    "d) (Abrogé) ;",
    "e) La taxe d'aménagement prévue aux articles 1635 quater A et suivants du code général des impôts.",
    "Les bénéficiaires de permis d'aménager peuvent également être tenus de verser la participation instituée dans les périmètres fixés par les conventions mentionnées à l'article L. 332-11-3 du présent code.",
    "Aucune contribution ou participation mise à la charge du bénéficiaire du permis d'aménager, de l'association foncière urbaine de remembrement ou de l'association foncière urbaine de projet ne peut être perçue sur les constructeurs.",
],
    "Réécriture à droit constant : chaque catégorie de redevable est rattachée à l'acte qui peut lui imposer une charge, et l'interdiction d'une seconde perception sur les constructeurs est formulée directement. Les lettres a) à e), les mentions d'abrogation, les neuf alinéas et les versions historiques des renvois sont maintenus. Aucune réforme de fond n'est apportée au financement.",
    "Les articles L. 331-15 et L. 332-9 ne figurent pas dans le corpus urbanisme fourni ; le renvoi non daté à L. 331-15 appelle donc un contrôle de coordination avec le régime de taxe d'aménagement désormais visé au e), sans substitution inventée. Les renvois aux anciennes rédactions de L. 332-9 et L. 332-6-1 sont conservés pour les situations historiques. La note source rattache l'application de ce texte à l'article 16 de l'ordonnance n° 2022-883 du 14 juin 2022 et à la date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021 ; les conditions de l'article 1er du décret n° 2022-1102 du 1er août 2022 restent à prendre en compte. Aucune nouvelle date d'application n'est fixée."
)

add("L332-13", [
    "Lorsqu'une commune appartient à un établissement public de coopération intercommunale ou à un syndicat mixte compétent pour réaliser les équipements donnant lieu à participation au titre de la présente section, l'établissement public qui exerce cette compétence institue la participation dans les mêmes conditions, quel que soit le mode de gestion retenu. La participation lui est versée.",
],
    "Réécriture à droit constant : l'établissement public compétent devient le sujet de la règle d'institution de la participation, puis son rôle de destinataire du versement est explicité. Les conditions de compétence et l'indifférence du mode de gestion sont conservées ; aucune réforme de fond n'est introduite.",
    "Le transfert concerne la participation liée aux seuls équipements relevant de la compétence considérée. Le champ de la présente section et les conditions d'institution demeurent identiques."
)

add("L332-14", [
    "Lorsque cela est nécessaire, des décrets en Conseil d'État fixent les conditions d'application de la présente section.",
],
    "Réécriture à droit constant de la clause d'application : la nécessité d'un texte réglementaire est exprimée par une condition explicite. Le renvoi à des décrets en Conseil d'État et à la présente section est conservé, sans réforme de fond.",
    "Maintenir le pluriel des décrets et leur adoption en Conseil d'État ; le texte n'impose pas un décret lorsque l'application de la section n'en nécessite pas."
)

add("L332-15", [
    "L'autorité qui délivre l'autorisation de construire, d'aménager ou de lotir impose à son bénéficiaire, lorsque cela est nécessaire, de réaliser et de financer tous les travaux nécessaires à la viabilité et à l'équipement de la construction, du terrain aménagé ou du lotissement. Ces travaux concernent notamment la voirie, l'alimentation en eau et en gaz, les réseaux de communications électroniques, l'évacuation et le traitement des eaux et matières usées, l'éclairage, les aires de stationnement, les espaces collectifs, les aires de jeux et les espaces plantés.",
    "Les obligations prévues au premier alinéa comprennent le branchement des équipements propres à l'opération sur les équipements publics existant au droit du terrain sur lequel ces équipements propres sont implantés. Elles comprennent notamment les opérations réalisées à cette fin en empruntant des voies privées ou en utilisant des servitudes.",
    "L'autorisation peut aussi imposer au bénéficiaire de financer le raccordement au réseau d'eau qui emprunte, en tout ou partie, des voies ou des emprises publiques, dans les conditions définies par l'autorité organisatrice du service public de l'eau. Le financement ne peut être imposé que pour un raccordement n'excédant pas cent mètres. Il est en outre subordonné à la condition que le réseau soit dimensionné exclusivement pour les seuls besoins du projet et ne soit pas destiné à desservir d'autres constructions, existantes ou futures.",
    "Pour les réseaux de communications électroniques, les équipements propres mentionnés au deuxième alinéa doivent être établis, s'il y a lieu, en application d'un titre d'occupation. Leur propriété est transférée dans les conditions prévues aux articles L. 33-6-1 à L. 33-6-5 du code des postes et des communications électroniques.",
    "Si les équipements sont ultérieurement classés dans la voirie et les réseaux publics, les travaux exigés au titre des équipements propres ne donnent pas droit à l'action en répétition prévue à l'article L. 332-30.",
    "L'autorité qui approuve le plan de remembrement peut imposer ces mêmes obligations aux associations foncières urbaines de remembrement autorisées ou constituées d'office.",
],
    "Réécriture à droit constant : la liste complète des équipements est conservée et les conditions cumulatives du raccordement à l'eau sont séparées en phrases lisibles dans leur alinéa d'origine. Les six alinéas, les règles relatives aux communications électroniques et l'exclusion de l'action en répétition demeurent en place. Aucune réforme de fond n'étend les charges des bénéficiaires.",
    "La limite de cent mètres ne concerne que le raccordement à l'eau visé au troisième alinéa ; le réseau reste réservé aux seuls besoins du projet et ne peut être destiné à d'autres constructions, présentes ou futures. Le branchement au droit du terrain, les servitudes et voies privées, les renvois aux articles L. 33-6-1 à L. 33-6-5 du code des postes et des communications électroniques et à L. 332-30 sont maintenus. La densification ne permet pas de faire financer des équipements publics généraux sous la qualification d'équipements propres."
)

add("L332-16", [
    "Lorsque cela est nécessaire, un décret en Conseil d'État fixe les conditions d'application de la présente section.",
],
    "Réécriture à droit constant : la formule « en tant que de besoin » devient une condition explicite, sans modifier l'objet ni la forme du décret. Aucune réforme de fond n'est apportée.",
    "Le singulier du décret en Conseil d'État et le renvoi à la seule section relative aux équipements propres sont conservés."
)

add("L332-17", [
    "Le bénéficiaire du permis ou de la décision de non-opposition verse la contribution aux coûts de raccordement au réseau public d'électricité prévue à l'article L. 342-12 du code de l'énergie, dans les conditions fixées à l'article L. 342-21 du même code.",
],
    "Réécriture à droit constant : le bénéficiaire redevable est placé en sujet de l'obligation de versement. Les deux renvois au code de l'énergie et les deux catégories de décisions demeurent inchangés ; aucune réforme de fond n'est appliquée au raccordement électrique.",
    "La note source indique que, conformément au VIII de l'article 24 de la loi n° 2025-391 du 30 avril 2025, les dispositions du VII de cet article s'appliquent aux opérations dont le permis de construire, le permis d'aménager ou la décision de non-opposition à une déclaration préalable a été délivré à compter du 10 septembre 2023. Ce champ temporel historique est conservé ; la date du 30 avril 2025 n'est pas utilisée comme nouveau point de départ. Le code de l'énergie n'appartient pas au corpus fourni : ses articles L. 342-12 et L. 342-21 restent à contrôler lors de la coordination intercodes."
)

add("L332-28", [
    "Selon le cas, le permis de construire, le permis d'aménager, les prescriptions de l'autorité compétente prises à l'occasion d'une déclaration préalable ou l'acte approuvant un plan de remembrement prescrivent les contributions mentionnées ou prévues au c du 2° de l'article L. 332-6-1, au d du 2° du même article dans sa rédaction antérieure à la loi n° 2014-1655 du 29 décembre 2014 de finances rectificative pour 2014, et à l'article L. 332-9 dans sa rédaction antérieure à l'entrée en vigueur de la loi n° 2010-1658 du 29 décembre 2010 de finances rectificative pour 2010. Ces actes constituent le fait générateur des contributions. Ils en fixent le montant ou, en cas d'apport de terrains, la superficie. S'il s'agit des travaux mentionnés au premier alinéa de l'article L. 332-10 dans sa rédaction antérieure à l'entrée en vigueur de la loi n° 2010-1658 du 29 décembre 2010 précitée, ils en fixent les caractéristiques générales.",
],
    "Réécriture à droit constant : les actes prescripteurs sont placés en sujet, puis leurs effets et les éléments qu'ils déterminent sont distingués en phrases successives dans le même alinéa. Toutes les contributions et les références aux rédactions historiques restent présentes. Aucune réforme de fond ne crée de fait générateur supplémentaire.",
    "Le d du 2° de L. 332-6-1 est expressément visé dans sa rédaction antérieure à la loi de 2014 ; le c du 2° reste le renvoi courant. L. 332-9 et L. 332-10, absents du corpus urbanisme fourni, restent visés dans leurs rédactions antérieures à l'entrée en vigueur de la loi de 2010. Ne pas supprimer ces références historiques ni les convertir en contributions nouvelles. Les actes et le fait générateur doivent rester coordonnés avec le registre de L. 332-29 et l'action de L. 332-30."
)

add("L332-28-1", [
    "Pour l'application du titre III du livre III du présent code, les déclarations préalables produisent les mêmes effets que le permis de construire.",
],
    "Réécriture à droit constant : la limite du champ d'application est placée en tête de phrase et l'équivalence des effets est exprimée directement. Aucune réforme de fond ne modifie les formalités requises.",
    "L'équivalence reste limitée au titre III du livre III du code de l'urbanisme. Elle ne transforme pas la déclaration préalable en permis pour les autres dispositions du code."
)

add("L332-29", [
    "Un registre tenu à la disposition du public en mairie recense les contributions prescrites par les actes mentionnés à l'article L. 332-28, ainsi que celles exigées pour la réalisation des zones d'aménagement concerté ou des projets urbains partenariaux. Lorsque cela est nécessaire, un décret en Conseil d'État fixe les modalités d'application du présent article.",
],
    "Réécriture à droit constant : le registre et son contenu sont décrits directement, et la condition du renvoi réglementaire est explicitée. L'accès en mairie et les trois origines des contributions sont conservés dans le même alinéa ; aucune réforme de fond n'est introduite.",
    "Le registre reste accessible au public en mairie. Coordonner ses inscriptions avec L. 332-30 : pour les acquéreurs successifs, le délai de répétition court à compter de l'inscription attestant le dernier versement ou l'obtention de la prestation, et non de la seule délivrance de l'autorisation."
)

add("L332-30", [
    "Les taxes et contributions de toute nature obtenues ou imposées en violation des articles L. 311-4 et L. 332-6 sont réputées sans cause. Les sommes versées et les sommes correspondant au coût des prestations fournies peuvent être réclamées par une action en répétition. Cette action se prescrit par cinq ans à compter du dernier versement ou de l'obtention des prestations indûment exigées.",
    "Les acquéreurs successifs de biens ayant fait l'objet des actes mentionnés à l'article L. 332-28, ou situés dans une zone d'aménagement concerté ou dans une zone couverte par une convention de projet urbain partenarial, peuvent aussi exercer l'action en répétition prévue au premier alinéa. Pour ces acquéreurs, le délai de prescription est de cinq ans à compter de l'inscription, sur le registre prévu à l'article L. 332-29, attestant le dernier versement ou l'obtention de la prestation.",
    "Les sommes remboursables en application des deux premiers alinéas produisent des intérêts au taux légal augmenté de cinq points.",
],
    "Réécriture à droit constant : la restitution des sommes et du coût des prestations est distinguée de la prescription, et le régime propre aux acquéreurs successifs est formulé séparément. Les trois alinéas, les deux délais de cinq ans et la majoration du taux légal de cinq points sont conservés. Aucune réforme de fond ne modifie le recours ou les intérêts.",
    "Les points de départ des deux prescriptions demeurent distincts : dernier versement ou obtention des prestations pour le premier alinéa ; inscription correspondante au registre pour les acquéreurs successifs. Le taux est le taux légal majoré de cinq points, et non un taux fixe de 5 %. Conserver l'articulation avec l'exclusion prévue au cinquième alinéa de L. 332-15 en cas de classement ultérieur des équipements propres."
)

add("L340-1", [
    "Pour permettre l'application, dans les départements d'outre-mer, des articles L. 311-1 à L. 311-7, L. 313-1 à L. 313-5 et L. 322-11, des décrets en Conseil d'État peuvent prévoir les adaptations et les dispositions transitoires éventuellement nécessaires.",
],
    "Réécriture à droit constant : l'objectif territorial du pouvoir d'adaptation est placé en tête de phrase et les deux types de mesures autorisées sont regroupés. Les trois ensembles de renvois et le caractère éventuel des mesures sont conservés ; aucune réforme de fond n'étend l'habilitation.",
    "Le champ reste celui des départements d'outre-mer, sans extension à d'autres collectivités ultramarines. Les intervalles L. 311-1 à L. 311-7 et L. 313-1 à L. 313-5 ainsi que l'article L. 322-11 restent les seuls textes visés par cette faculté d'adaptation réglementaire."
)

add("L340-2", [
    "Dans chacun des territoires de la Guadeloupe, de la Guyane, de la Martinique, de La Réunion et de Mayotte, un fonds régional d'aménagement foncier et urbain est créé. Il coordonne les interventions financières de l'État, des collectivités territoriales et de l'Union européenne pour constituer des réserves foncières et réaliser les équipements nécessaires à l'aménagement d'espaces déjà urbanisés ou destinés à l'être par les documents d'urbanisme applicables.",
    "Le fonds régional contribue également au financement des études préalables à ces opérations.",
    "Pour mettre en œuvre ce dispositif, une convention peut confier à une institution financière choisie par les contributeurs mentionnés au premier alinéa le regroupement des fonds et le versement des aides.",
    "Les représentants des maîtres d'ouvrage sociaux sont consultés sur la gestion et l'évaluation de ces fonds.",
    "La présidence de chaque fonds régional d'aménagement foncier et urbain est exercée alternativement, pour des périodes d'un an, par le président du conseil général et le président du conseil régional. À Mayotte, le président du conseil général assure la présidence du fonds.",
    "L'association des maires désigne deux représentants pour siéger au fonds régional d'aménagement foncier et urbain.",
    "Un décret fixe les autres modalités d'organisation et de fonctionnement des fonds régionaux.",
],
    "Réécriture à droit constant : la création territoriale des fonds, leurs missions financières et leurs règles de gestion sont exposées en phrases directes. Les sept alinéas, les cinq territoires, l'alternance annuelle de la présidence, la règle propre à Mayotte et les deux représentants des maires sont maintenus. Aucune réforme de fond n'attribue de ressource ou de compétence supplémentaire.",
    "Les appellations « conseil général » et « conseil régional » et leur alternance sont conservées telles qu'elles déterminent la gouvernance dans la source. Leur adéquation aux institutions des cinq territoires appelle un contrôle explicite, notamment pour les collectivités à assemblée unique ; aucune substitution institutionnelle n'est effectuée sans coordination. La correction grammaticale de « ces fonds régional » et « maîtres d'ouvrages » ne modifie pas les organes ni les personnes consultées. Les périodes d'un an et les deux représentants sont préservés. Aucun financement nouveau n'est présumé acquis."
)

add("L350-1", [
    "L'autorité administrative, d'une part, et les communes ainsi que les établissements publics de coopération intercommunale à fiscalité propre pour les objets relevant des compétences qui leur ont été transférées, d'autre part, peuvent conclure un contrat pour réaliser un projet d'intérêt majeur. Ce projet comprend des actions ou des opérations d'aménagement et, le cas échéant, des projets d'infrastructure.",
    "La région et les départements territorialement intéressés peuvent aussi signer le contrat à leur demande.",
    "À la demande de l'une des personnes publiques mentionnées aux deux premiers alinéas, tout établissement public de l'État, toute société publique locale ou toute société publique locale d'aménagement d'intérêt national susceptible de participer à la réalisation du projet d'intérêt majeur peut également signer le contrat.",
],
    "Réécriture à droit constant : l'objet du contrat est séparé de la désignation des cocontractants, puis les deux possibilités de participation complémentaire sont formulées directement. Les trois alinéas, les catégories de signataires et les conditions de compétence et de demande sont conservés. Aucune réforme de fond ne modifie les contrats existants ou les compétences transférées.",
    "La participation de la région et des départements dépend de leur propre demande ; celle des établissements publics de l'État et sociétés dépend de la demande d'une personne publique des deux premiers alinéas. Les sociétés publiques locales d'aménagement d'intérêt national restent une catégorie distincte. Coordonner les possibilités de réalisation avec L. 350-6, qui exige une prévision contractuelle et maintient les règles propres aux sociétés."
)

add("L350-2", [
    "Avant la signature du contrat, le projet d'intérêt majeur doit être soumis à l'avis du président du conseil régional, du président du conseil départemental et des présidents des établissements publics de coopération intercommunale compétents en matière de programme local de l'habitat ou de plan local d'urbanisme.",
    "L'avis de tout organisme ou de toute association ayant compétence en matière d'habitat, d'urbanisme, de déplacement, d'aménagement ou d'environnement peut également être recueilli.",
    "Le projet est soumis à une enquête publique conduite conformément au chapitre III du titre II du livre Ier du code de l'environnement.",
],
    "Réécriture à droit constant : la consultation préalable obligatoire est distinguée de la consultation facultative, sans ajouter de condition à l'enquête publique. Les trois alinéas, les autorités consultées et les cinq domaines de compétence des organismes ou associations sont conservés. Aucune réforme de fond n'allège les garanties de participation.",
    "Les avis du premier alinéa restent requis avant la signature, tandis que ceux du deuxième alinéa demeurent facultatifs. Conserver le renvoi au chapitre III du titre II du livre Ier du code de l'environnement et son articulation avec l'enquête de mise en compatibilité prévue à L. 350-5. Le code de l'environnement, hors du corpus fourni, n'a pas été modifié."
)

add("L350-3", [
    "Le contrat conclu en application de l'article L. 350-1 comporte les éléments suivants :",
    "1° Une présentation du projet d'intérêt majeur, de ses objectifs et de sa contribution au développement urbain durable du territoire dans lequel il s'insère ;",
    "2° Le nombre de logements et le pourcentage de logements sociaux à réaliser dans le cadre du projet. Ces objectifs quantitatifs sont fixés après consultation du comité régional de l'habitat ;",
    "3° La stratégie foncière nécessaire à la réalisation du projet et, le cas échéant, les modalités de mobilisation des terrains appartenant aux signataires du contrat et nécessaires à sa conduite ;",
    "4° La liste des actions et des opérations d'aménagement et, le cas échéant, des projets d'infrastructure mentionnés au premier alinéa de l'article L. 350-1, leurs conditions de mise en œuvre et l'échéancier prévisionnel de leur réalisation ;",
    "5° Les conditions générales de financement du projet.",
],
    "Réécriture à droit constant : les cinq éléments obligatoires du contrat sont formulés plus directement, sans modifier leur ordre ni leur numérotation. Le nombre de logements, le pourcentage de logements sociaux, la consultation préalable et le caractère prévisionnel de l'échéancier restent explicites. Aucune réforme de fond ne dispense d'obligations de logement social.",
    "L'introduction et les cinq subdivisions conservent leurs emplacements, notamment le 3° visé par L. 350-4 et le 4° visé par L. 350-5 et L. 350-6. La source mentionne le « comité régional de l'habitat » ; L. 364-1 du code de la construction et de l'habitation, lu dans le corpus public, emploie « comité régional de l'habitat et de l'hébergement » et prévoit des organismes territoriaux particuliers. Cette différence de désignation est signalée sans remplacement silencieux. Le contrat ne supprime pas les obligations légales de logement social."
)

add("L350-4", [
    "Pour mettre en œuvre la stratégie foncière prévue au 3° de l'article L. 350-3, le contrat peut prévoir la création de zones d'aménagement différé. Il en établit la liste, en délimite le périmètre et désigne les bénéficiaires des droits de préemption ainsi institués.",
    "Pour l'application de l'article L. 212-1, la délibération du conseil municipal ou de l'organe délibérant de l'établissement public de coopération intercommunale à fiscalité propre autorisant le maire ou le président de l'établissement à signer le contrat vaut avis favorable de la commune ou de l'établissement sur la création des zones d'aménagement différé prévues au contrat.",
    "Dans les zones d'aménagement différé prévues au contrat, la commune dispose d'un droit de préemption à titre subsidiaire lorsqu'elle ne bénéficie pas du droit de préemption à titre principal. Dans les deux mois suivant la déclaration préalable d'aliénation faite par le propriétaire dans les conditions de l'article L. 213-2, le bénéficiaire du droit principal informe la collectivité territoriale et le propriétaire de sa décision d'exercer ou non ce droit. S'il renonce à l'exercer, le délai fixé au même article L. 213-2, au terme duquel le silence vaut renonciation à l'exercice du droit de préemption, est porté à trois mois afin de permettre au titulaire du droit subsidiaire de l'exercer.",
],
    "Réécriture à droit constant : les mentions contractuelles, l'effet de la délibération et l'articulation des droits de préemption sont exprimés en phrases plus courtes dans leurs trois alinéas d'origine. Le délai de deux mois pour informer et celui porté à trois mois sont conservés. Aucune réforme de fond ne modifie la priorité des titulaires.",
    "Les articles L. 212-1 et L. 213-2 ont été consultés dans le corpus public. Le troisième alinéa conserve la formulation de la source rattachant l'information à la déclaration préalable d'aliénation ; L. 213-2 fait courir le délai ordinaire de silence à compter de la réception de cette déclaration et prévoit des suspensions. L'articulation de ces délais et suspensions appelle un contrôle, sans modification du point de départ dans cette réécriture. Le passage à trois mois reste conditionné à la renonciation du bénéficiaire principal et ne constitue pas l'octroi d'un nouveau délai autonome de trois mois au titulaire subsidiaire."
)

add("L350-5", [
    "Le contrat prévu au présent titre peut tenir lieu, pour l'application de l'article L. 300-6, de déclaration de projet pour les actions ou les opérations d'aménagement et les projets d'infrastructures mentionnés au 4° de l'article L. 350-3. Il désigne les actions, les opérations et les projets pour lesquels il vaut déclaration de l'intérêt général.",
    "Ces actions, opérations d'aménagement ou projets d'infrastructures doivent être compatibles, s'il y a lieu, avec le schéma directeur de la région d'Île-de-France, les schémas d'aménagement régional des collectivités de l'article 73 de la Constitution ou le plan d'aménagement et de développement durable de Corse.",
    "Lorsque ces actions, opérations d'aménagement ou projets d'infrastructure ne sont pas compatibles avec les schémas de cohérence territoriale, les schémas de secteurs et les plans locaux d'urbanisme, l'autorité administrative engage les procédures de mise en compatibilité prévues aux articles L. 143-44 et L. 153-54. L'enquête publique mentionnée à l'article L. 350-2 est alors organisée dans les conditions fixées par ces mêmes articles.",
],
    "Réécriture à droit constant : l'effet possible du contrat comme déclaration de projet, les obligations de compatibilité et le déclenchement des procédures correspondantes sont explicités dans les trois alinéas existants. Toutes les catégories de documents et les renvois sont conservés. Aucune réforme de fond ne dispense de l'enquête publique ni des protections de planification.",
    "Les renvois à L. 143-44 et L. 153-54 ont été vérifiés dans le corpus public ; ils portent notamment sur l'enquête et l'examen conjoint de la mise en compatibilité. La mention des schémas de secteurs est maintenue telle qu'elle figure dans la source et appelle un contrôle d'actualité de cette catégorie. La note source, fondée sur l'article 7 de l'ordonnance n° 2019-1170 du 13 novembre 2019, fixe l'entrée en vigueur au 1er mars 2020 mais exclut les procédures d'élaboration ou de révision de schémas d'aménagement régional en cours à cette date. Cette transition historique demeure applicable et n'est pas transformée en transition d'une réforme future."
)

add("L350-6", [
    "Si le contrat prévu au présent titre l'autorise, un établissement public de l'État qui en est signataire peut réaliser certaines actions ou opérations d'aménagement ou certains projets d'infrastructure prévus par ce contrat en application du 4° de l'article L. 350-3.",
    "Si le contrat prévu au présent titre l'autorise, une société publique locale mentionnée à l'article L. 327-2 du présent code ou à l'article L. 1531-1 du code général des collectivités territoriales, ou une société publique locale d'aménagement d'intérêt national mentionnée à l'article L. 327-3 du présent code, peut réaliser certaines actions ou opérations d'aménagement ou certains projets d'infrastructure prévus par ce contrat en application du 4° de l'article L. 350-3, à condition d'en être signataire. La société agit dans les conditions fixées par les dispositions qui la régissent.",
],
    "Réécriture à droit constant : les deux alinéas rendent explicites la prévision contractuelle et la qualité de signataire exigées pour réaliser les actions, opérations ou infrastructures. Tous les types de personnes et les règles propres aux sociétés sont conservés. Aucune réforme de fond ne transfère de compétence ou n'affranchit les sociétés de leur régime.",
    "Le renvoi au 4° de L. 350-3 demeure dans chacun des deux alinéas. L. 327-2, consulté dans le corpus public, régit les sociétés publiques locales d'aménagement ; la source les désigne ici par la formule plus générale « société publique locale ». Cette différence de désignation est signalée sans supprimer le renvoi. L'article L. 1531-1 du code général des collectivités territoriales est hors du corpus fourni et reste à contrôler dans la coordination intercodes."
)

add("L350-7", [
    "Les contrats prévus au présent titre sont soumis aux règles de publicité et de communication fixées par les articles L. 2121-24 et L. 2121-26 du code général des collectivités territoriales.",
],
    "Réécriture à droit constant : les contrats sont placés en sujet de la règle qui les soumet à publicité et à communication. Les deux renvois et le périmètre du présent titre sont conservés, sans réforme de fond.",
    "Les obligations de publicité et de communication demeurent distinctes et cumulatives selon les textes visés. Les articles L. 2121-24 et L. 2121-26 du code général des collectivités territoriales sont hors du corpus fourni ; aucun contenu nouveau ne leur est attribué."
)

add("L421-1", [
    "Un permis de construire doit être délivré avant la réalisation d'une construction, même si celle-ci ne comporte pas de fondations.",
    "Un décret en Conseil d'État fixe la liste des travaux sur des constructions existantes et des changements de destination qui doivent également être précédés de la délivrance d'un permis de construire en raison de leur nature ou de leur localisation.",
],
    "Réécriture à droit constant : la délivrance préalable du permis est formulée comme une condition explicite de réalisation de la construction. Le second alinéa conserve le renvoi réglementaire pour les travaux sur l'existant et les changements de destination. Aucune réforme de fond ne dispense les transformations de bureaux d'une autorisation exigible.",
    "Les deux alinéas et les critères de nature ou de localisation sont conservés. Le principe du permis reste à lire avec les régimes de déclaration préalable et d'exemption du même chapitre. Le dossier coordonné, le réemploi des pièces et les délais ordinaires de deux et trois mois relèvent de la coordination déjà retenue à L. 423-1 et de ses textes d'application ; ils ne sont pas ajoutés à ce champ d'application. Les solutions techniques équivalentes pour la transformation en logements nécessitent, dans le code de la construction et de l'habitation, le contrôle des dispositifs de solutions d'effet équivalent des articles L. 112-4 à L. 112-12 et leur coordination réglementaire, sans création ici d'une dérogation générale de sécurité, d'accessibilité ou de salubrité."
)

add("L421-2", [
    "Un permis d'aménager doit être délivré avant la réalisation des travaux, installations et aménagements qui affectent l'utilisation des sols et figurent sur une liste fixée par décret en Conseil d'État.",
],
    "Réécriture à droit constant : l'exigence de délivrance préalable du permis est placée en tête et les deux conditions du champ d'application sont réunies clairement. Aucune réforme de fond ne modifie la liste réglementaire des opérations soumises à permis d'aménager.",
    "L'affectation de l'utilisation des sols et l'inscription sur la liste réglementaire restent des conditions cumulatives. Le décret doit rester un décret en Conseil d'État. La coordination d'un dossier d'autorisation prévue à L. 423-1 ne supprime pas la distinction entre permis d'aménager et permis de construire."
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {s["number"] for s in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(drafts[source["number"]])
    item["status"] = "rewrite_draft"
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
