import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('371 ter D', [
    'Toute cession ou transmission de la convention est interdite.',
],
    'Réécriture à droit constant : les qualifications d’incessibilité et d’intransmissibilité sont formulées comme une interdiction expresse de toute cession ou transmission. Aucune réforme de fond.',
    'La portée de l’interdiction demeure celle de la convention entière ; aucune exception ni faculté de transfert n’est ajoutée.')

add('371 ter E', [
    "La convention est conclue pour trois ans. Le renouvellement par tacite reconduction est possible une seule fois, pour la même durée. Il est exclu si le directeur général des finances publiques, le professionnel ou l'organisme dénonce la convention au moins trois mois avant la date d'expiration de la convention en cours.",
    "La convention peut également être renouvelée pour trois ans selon la procédure initiale. La demande doit être présentée au moins trois mois avant la date d'expiration de la convention en cours.",
    "Le directeur général des finances publiques se prononce sur cette demande et informe le demandeur de sa décision selon les règles applicables à une demande initiale.",
    "En cas de non-renouvellement de sa convention, le certificateur à l'étranger informe ses clients ou adhérents dans le délai d'un mois à compter de la date de notification du non-renouvellement.",
],
    'Réécriture à droit constant : séparation de la durée, de la reconduction tacite et du renouvellement sur demande ; identification des personnes pouvant dénoncer la convention et du délai d’information des clients. Aucune réforme de fond.',
    'Sont maintenus : trois ans, une seule reconduction tacite de même durée, préavis et dépôt de la demande au moins trois mois avant expiration, information des clients dans le mois. La procédure initiale de l’article 371 ter B, consultée dans le corpus, comporte un délai de décision de quatre mois et une acceptation tacite ; le renvoi général à cette procédure est conservé sans inventer une prolongation de la convention pendant l’instruction.')

add('371 ter F', [
    'Par la convention, le demandeur prend les engagements suivants :',
    "1° Garantir une stricte indépendance dans l'examen des déclarations fiscales de son client ou adhérent. À cette fin, il confie cet examen à une personne qui n'a pas participé à la tenue de la comptabilité de ce dernier ;",
    "2° Contrôler la déclaration des revenus encaissés à l'étranger ainsi que la déclaration de résultats déposée à l'étranger, afférente aux revenus de source étrangère provenant d'un Etat membre de l'Union européenne ou d'un autre Etat partie à l'accord sur l'Espace économique européen ayant conclu avec la France une convention d'assistance administrative en vue de lutter contre la fraude et l'évasion fiscales ;",
    "3° Adresser un compte rendu de mission à son adhérent ou client dans les deux mois suivant la fin des opérations de contrôle et, au plus tard, dans les huit mois suivant la réception de la déclaration des revenus encaissés à l'étranger par un contribuable domicilié en France. Dans ce même délai, le certificateur transmet une copie du compte rendu par voie dématérialisée à la direction générale des finances publiques.",
],
    'Réécriture à droit constant : engagements présentés par actions, indépendance assortie de son moyen concret et échéances du compte rendu formulées sans incise. Les trois obligations et leur numérotation sont maintenues. Aucune réforme de fond.',
    'Le champ territorial UE/EEE avec la condition conventionnelle, les deux déclarations contrôlées, les deux mois après contrôle et le plafond de huit mois après réception de la déclaration sont conservés. La copie à l’administration reste obligatoire dans le même délai : elle a un destinataire distinct et ne constitue pas une demande administrative en double à supprimer.')

add('371 ter G', [
    "Le directeur général des finances publiques peut résilier la convention lorsqu'il constate des manquements du certificateur à l'étranger ou de la société dans laquelle celui-ci exerce sa profession à l'une des obligations de la convention individuelle.",
    "Avant de décider la résiliation, le directeur général des finances publiques doit mettre le certificateur à l'étranger en mesure de présenter ses observations sur les faits qui lui sont reprochés.",
    "La décision de résiliation est motivée. Elle est notifiée au certificateur à l'étranger par pli recommandé avec demande d'avis de réception.",
    "Le certificateur à l'étranger dont la convention est résiliée informe ses clients ou adhérents dans le délai d'un mois à compter de la date de notification du non-renouvellement.",
],
    'Réécriture à droit constant : les causes de résiliation, le contradictoire préalable et les exigences de motivation et de notification sont exprimés dans quatre alinéas distincts, comme dans la source. Aucune réforme de fond ; l’anomalie du dernier alinéa est maintenue et signalée.',
    'Incohérence préexistante : le dernier alinéa règle une résiliation mais fait courir le mois d’information à compter de la notification du « non-renouvellement ». Cette formulation est conservée ; sa substitution par la notification de la résiliation exige une correction normative explicite, coordonnée avec l’article 371 ter E. Ni le point de départ ni le délai ne sont corrigés silencieusement.')

add('371 ter H', [
    "Lorsque sa convention est caduque ou a été résiliée en application du présent chapitre, le certificateur à l'étranger doit attendre l'expiration d'un délai de deux ans avant de déposer une nouvelle demande de convention.",
],
    'Réécriture à droit constant : la période pendant laquelle une nouvelle demande est interdite est formulée du point de vue du certificateur. Les deux situations déclenchant cette interdiction sont conservées. Aucune réforme de fond.',
    'Le délai reste de deux ans. La source ne précise pas expressément son point de départ ; cette précision n’est pas inventée, notamment au regard de l’anomalie de notification signalée à l’article 371 ter G.')

add('371 ter I', [
    "I. – À l'exception des parlementaires, les membres de la commission départementale des valeurs locatives mentionnée à l'article 1650 B du code général des impôts sont désignés selon les règles prévues aux II à V.",
    'II. – Dans les deux mois suivant son renouvellement, le conseil de Paris désigne ses membres appelés à siéger à la commission. Leur mandat a la même durée que celui des conseillers de Paris.',
    'Dans les deux mois suivant son renouvellement, le conseil départemental désigne ses membres appelés à siéger à la commission. Leur mandat a la même durée que celui des conseillers départementaux.',
    'Dans les deux mois suivant son renouvellement, le conseil de la Métropole de Lyon désigne ses membres appelés à siéger à la commission. Leur mandat a la même durée que celui des conseillers de la Métropole.',
    "L'association départementale des maires désigne les maires dans les deux mois suivant le renouvellement général des conseils municipaux. Leur mandat a la même durée que celui des conseillers municipaux.",
    "L'association départementale des maires désigne les représentants des établissements publics de coopération intercommunale à fiscalité propre dans les trois mois suivant le renouvellement général des conseils municipaux. Leur mandat a la même durée que celui des membres de l'organe délibérant de ces établissements.",
    "III. – Lorsque plusieurs associations de maires existent dans le département, le représentant de l'Etat dans le département désigne les maires et les représentants des établissements publics de coopération intercommunale à fiscalité propre après avoir consulté ces associations.",
    "Lorsqu'aucune association de maires n'existe dans le département, le représentant de l'Etat dans le département désigne les maires et les représentants des établissements publics de coopération intercommunale à fiscalité propre.",
    "À défaut de désignation dans les délais prévus au II, le représentant de l'Etat dans le département désigne les membres du conseil de Paris, les membres du conseil départemental, les membres du conseil de la Métropole de Lyon, les maires et les représentants des établissements publics de coopération intercommunale à fiscalité propre.",
    "IV. – Le représentant de l'Etat dans le département désigne les représentants des contribuables pour six ans, dans les trois mois suivant le renouvellement général des conseils municipaux. Ces représentants sont répartis comme suit :",
    "a) Trois personnes désignées après consultation des chambres de commerce et d'industrie territoriales ou, en Ile-de-France, des chambres de commerce et d'industrie départementales d'Ile-de-France ;",
    "b) Deux personnes désignées après consultation des chambres de métiers et de l'artisanat départementales ou, à défaut, de région ;",
    "c) Trois personnes désignées après consultation des organisations d'employeurs au niveau interprofessionnel les plus représentatives dans le département ;",
    'd) Une personne désignée après consultation des organisations représentatives des professions libérales dans le département.',
    "V. – Le directeur départemental ou, le cas échéant, régional des finances publiques désigne les représentants de l'administration fiscale.",
],
    'Réécriture à droit constant : chaque autorité de désignation devient le sujet de la règle ; délais, durées des mandats et mécanismes de substitution sont séparés en alinéas correspondant à ceux de la source. Les subdivisions I à V et les lettres a à d sont maintenues. Aucune réforme de fond.',
    'Délais de deux ou trois mois et mandat de six ans conservés ; les représentants des contribuables restent répartis en 3 + 2 + 3 + 1, soit les neuf prévus par l’article 1650 B consulté. Ce dernier mentionne aussi les conseillers à l’Assemblée de Corse, dont le présent article ne précise pas expressément la procédure de désignation : articulation à contrôler, sans ajout silencieux. La note source rattache la modification à l’article 146-IX H de la loi n° 2019-1479 du 28 décembre 2019 ; cette indication historique n’est pas une date de réforme future.')

add('371 ter J', [
    "I. – Pour remplacer les membres de la commission en cas d'absence ou d'empêchement, des suppléants sont désignés en nombre égal à celui des titulaires mentionnés aux II à V de l'article 371 ter I et dans les mêmes conditions que ces titulaires.",
    "II. – Chaque représentant des collectivités territoriales et des établissements publics de coopération intercommunale à fiscalité propre peut se faire accompagner aux séances de la commission soit par son suppléant, soit par un fonctionnaire relevant de l'article L. 4 du code général de la fonction publique.",
    "Chaque représentant des contribuables peut se faire accompagner aux séances de la commission soit par son suppléant, soit, avec l'autorisation du président de la commission, par une personne choisie, selon le cas, dans l'une des catégories suivantes :",
    "a) Le personnel des chambres de commerce et d'industrie ;",
    "b) Le personnel des chambres de métiers et de l'artisanat ;",
    "c) Les membres ou le personnel des organisations d'employeurs au niveau interprofessionnel les plus représentatives dans le département ;",
    'd) Les membres ou le personnel des organisations représentatives des professions libérales dans le département.',
    "Aux séances de la commission, chaque représentant de l'administration fiscale peut se faire accompagner par son suppléant.",
    "Les fonctionnaires mentionnés au premier alinéa du présent II et les personnes choisies conformément à son deuxième alinéa ne participent pas aux débats de la commission. Les suppléants n'y participent pas non plus, sauf lorsqu'ils remplacent un titulaire dans les conditions prévues au I.",
    "III. – Toute personne désignée à plusieurs titres comme membre titulaire ou suppléant de la commission doit choisir, dans un délai d'une semaine, la qualité en laquelle elle siège.",
    "Toute personne désignée en application des II à IV de l'article 371 ter I comme membre titulaire ou suppléant de la commission départementale des valeurs locatives des locaux professionnels doit choisir, dans un délai d'une semaine, la commission dans laquelle elle siège si elle est déjà membre titulaire ou suppléant de la commission départementale des impôts directs locaux.",
],
    'Réécriture à droit constant : clarification du remplacement, des accompagnateurs autorisés et de leur exclusion des débats ; les deux choix à exercer en une semaine restent dans les deux alinéas du III. Les subdivisions et catégories de personnes sont conservées. Aucune réforme de fond.',
    'La note source indique expressément que « Le second alinéa du III devient sans objet », alors que cet alinéa figure toujours dans le source_xml et vise les anciennes commissions. Il est conservé intégralement quant à sa règle, dans l’attente d’une suppression ou coordination normative explicite. La note mentionne aussi l’article 146-IX I de la loi n° 2019-1479 du 28 décembre 2019 et l’entrée en vigueur au 1er mars 2022 prévue par l’article 11 de l’ordonnance n° 2021-1574 du 24 novembre 2021. Les renvois aux premier et deuxième alinéas sont explicités comme internes au II, sans déplacement de leurs cibles.')

add('371 ter K', [
    "Le préfet fixe par arrêté la liste des membres de la commission départementale des valeurs locatives, à l'exception des parlementaires et des représentants de l'administration fiscale. Il prend cet arrêté dès la désignation de ces membres dans les conditions prévues aux articles 371 ter I et 371 ter J.",
    'Cet arrêté est publié au recueil des actes administratifs du département.',
],
    'Réécriture à droit constant : l’autorité qui prend l’arrêté et les deux catégories exclues de la liste sont explicites. La publication demeure dans le second alinéa. Aucune réforme de fond.',
    'Les renvois aux articles 371 ter I et 371 ter J et la publication au recueil départemental sont maintenus. La note source mentionne une modification de conséquence de l’article 146-IX H de la loi n° 2019-1479 du 28 décembre 2019, sans disposition transitoire nouvelle.')

add('371 ter L', [
    "I. – Lorsqu'un membre de la commission ou son suppléant démissionne, perd la qualité au titre de laquelle il a été désigné ou n'est plus en état d'exercer ses fonctions, une nouvelle désignation a lieu. La personne désignée exerce ses fonctions jusqu'à l'expiration du mandat de celle qu'elle remplace. La désignation est effectuée par les personnes compétentes et selon les conditions prévues à l'article 371 ter I ; les délais courent à compter de l'événement qui rend cette nouvelle désignation nécessaire.",
    'La commission peut valablement siéger pendant le temps nécessaire au remplacement des membres dans les cas prévus au premier alinéa.',
    'II. – Une nouvelle désignation a également lieu pour :',
    'a) Les conseillers départementaux, en cas de renouvellement général des conseils départementaux ;',
    'b) Les conseillers métropolitains, en cas de renouvellement général du conseil de la Métropole de Lyon ;',
    'c) Les conseillers de Paris, les maires, les représentants des établissements publics de coopération intercommunale à fiscalité propre et les représentants des contribuables, en cas de renouvellement général des conseils municipaux.',
    'La commission interrompt ses travaux le vendredi qui précède le renouvellement général des conseils départementaux ou des conseils municipaux. Elle les reprend au plus tard une semaine après la désignation de ses nouveaux membres.',
],
    'Réécriture à droit constant : formulation directe des événements entraînant une nouvelle désignation, de la durée du remplacement et de la suspension des travaux. Les I et II, leurs alinéas et les lettres a à c sont conservés. Aucune réforme de fond.',
    'Le mandat du remplaçant reste limité au mandat restant ; les délais de l’article 371 ter I sont recalculés depuis l’événement déclencheur. Sont conservés le vendredi précédant le renouvellement et la reprise au plus tard une semaine après désignation. La source vise le renouvellement métropolitain au b mais ne le mentionne pas expressément dans la règle de suspension : cette asymétrie reste à contrôler, sans extension du texte.')

add('371 ter M', [
    "I. – Dans les huit jours suivant la publication de l'arrêté prévu à l'article 371 ter K, le directeur départemental ou, le cas échéant, régional des finances publiques réunit les membres de la commission. Ceux-ci élisent, parmi les représentants des collectivités territoriales et des établissements publics de coopération intercommunale à fiscalité propre, le président de la commission et un vice-président chargé de le remplacer en cas d'absence ou d'empêchement.",
    "Le doyen d'âge préside la séance. Le vote a lieu au scrutin secret. Aux deux premiers tours, l'élection exige la majorité des suffrages exprimés. Si aucun candidat n'obtient cette majorité, un troisième tour est organisé : est alors élu le candidat ayant recueilli le plus de suffrages. En cas d'égalité, le candidat le plus âgé est élu.",
    "II. – Le président convoque la commission de sa propre initiative, à la demande de la moitié au moins de ses membres ou à la demande du directeur départemental ou, le cas échéant, régional des finances publiques. Les membres doivent être convoqués au moins huit jours francs avant la date de la réunion.",
    "Les séances se tiennent hors de la présence du public. Le président peut toutefois décider d'entendre toute personne susceptible d'apporter des informations utiles à la commission.",
    "III. – Pour délibérer, la commission doit compter au moins la moitié de ses membres présents. Si ce quorum n'est pas atteint, une nouvelle convocation est faite aussitôt. Après un délai d'au moins trois jours francs suivant cette nouvelle convocation, la commission peut délibérer quel que soit le nombre de membres présents.",
    'La commission adopte ses décisions à la majorité des suffrages exprimés.',
    "Les représentants de l'administration fiscale ne participent pas aux votes.",
    'En cas de partage égal des voix, celle du président est prépondérante.',
],
    'Réécriture à droit constant : décomposition de l’élection en étapes et clarification des initiatives de convocation, du quorum et de la seconde réunion. Les trois subdivisions et les huit alinéas sont conservés. Aucune réforme de fond.',
    'Contrôles : réunion initiale sous huit jours ; convocation ordinaire huit jours francs avant réunion ; seconde délibération au moins trois jours francs après la nouvelle convocation ; majorité des suffrages exprimés, départage par l’âge pour l’élection et voix du président pour les décisions. L’article 1650 B consulté exclut les parlementaires du calcul du quorum ; le présent article reste soumis à cette règle sans créer un calcul différent. La voix fiscale demeure consultative.')

add('371 ter S', [
    "I. – Les décisions que la commission départementale des valeurs locatives prend en application du 3 du I et du III de l'article 1504 du code général des impôts ou du II de l'article 1518 ter du même code doivent être notifiées :",
    "1° Au président du conseil départemental ou, le cas échéant, en Martinique ou en Guyane, au président de l'assemblée délibérante de la collectivité territoriale unique, au président du conseil de la Métropole de Lyon, ainsi qu'au maire de Paris ;",
    '2° Aux maires des communes et aux présidents des établissements publics de coopération intercommunale à fiscalité propre du département.',
    'Ces décisions sont transmises sans délai au directeur départemental ou, le cas échéant, régional des finances publiques.',
    "Les décisions que la commission départementale des valeurs locatives prend en application du IV de l'article 1504 du code général des impôts sont elles aussi notifiées dans les conditions prévues à l'alinéa précédent.",
    "II. – Les arrêtés pris en application du III ou du IV de l'article 1504 du code général des impôts doivent être notifiés :",
    "1° Au président du conseil départemental ou, le cas échéant, en Martinique ou en Guyane, au président de l'assemblée délibérante de la collectivité territoriale unique, au président du conseil de la Métropole de Lyon, ainsi qu'au maire de Paris ;",
    '2° Aux maires des communes et aux présidents des établissements publics de coopération intercommunale à fiscalité propre du département ;',
    '3° Au président de la commission départementale des valeurs locatives des locaux professionnels et au président de la commission départementale des impôts directs locaux.',
    "III. – Les tarifs établis en application du I de l'article 1518 ter du code général des impôts doivent être notifiés aux destinataires suivants :",
    "1° Au président du conseil départemental ou, le cas échéant, en Martinique ou en Guyane, au président de l'assemblée délibérante de la collectivité territoriale unique, au président du conseil de la Métropole de Lyon, ainsi qu'au maire de Paris ;",
    '2° Aux maires des communes et aux présidents des établissements publics de coopération intercommunale à fiscalité propre du département.',
    'IV. – Les décisions et arrêtés mentionnés aux I à III font l’objet d’une publication au recueil des actes administratifs de la préfecture du département.',
    "V. – Les notifications et transmissions prévues par le présent article sont faites par voie électronique. Si nécessaire, elles peuvent être effectuées par lettre recommandée avec demande d'avis de réception ou par voie administrative avec récépissé.",
],
    'Réécriture à droit constant : distinction des décisions, arrêtés et tarifs à notifier ; présentation de chaque destinataire dans sa subdivision et séparation du mode électronique et des modes subsidiaires. Les I à V et tous leurs destinataires sont conservés. Aucune réforme de fond.',
    'Deux difficultés préexistantes sont maintenues : au dernier alinéa du I, le renvoi à l’alinéa précédent vise une transmission au directeur des finances publiques alors que le texte parle de notification ; au 3° du II, les dénominations des deux anciennes commissions subsistent. Les articles 1504, 1518 ter et 1650 B du corpus ont été consultés ; aucune substitution implicite de destinataire ou de commission n’est faite. La note historique vise l’article 146-IX C de la loi n° 2019-1479 du 28 décembre 2019. Les alinéas logiques matérialisés par des br dans la source sont présentés en p, dans le même ordre, notamment pour conserver la cible du renvoi interne.')

add('371 AI', [
    "La direction générale des finances publiques valide les inscriptions d'informations et les dépôts de pièces au Registre national des entreprises prévu à l'article L. 123-36 du code de commerce lorsque les entreprises étrangères concernées réunissent les trois conditions suivantes :",
    "1° Elles exercent en France une activité de nature commerciale, artisanale, agricole ou indépendante, sans y disposer d'un établissement stable ;",
    "2° Aucune des personnes qu'elles emploient n'est affiliée à un régime de sécurité sociale en France ;",
    '3° Elles sont tenues de remplir une obligation fiscale en France.',
],
    'Réécriture à droit constant : la direction générale des finances publiques devient le sujet de la validation et le caractère cumulatif des trois critères est explicite. Le champ des entreprises et la numérotation demeurent identiques. Aucune réforme de fond.',
    'Maintien du renvoi à L. 123-36 du code de commerce et des quatre natures d’activité, de l’absence d’établissement stable et de salarié affilié en France, ainsi que de l’obligation fiscale. La note source fixe l’entrée en vigueur au 1er janvier 2023 par l’article 45 du décret n° 2022-1014 du 19 juillet 2022 ; cette date demeure une donnée historique.')

add('371 AJ', [
    "L'organisme unique mentionné à l'article R. 123-1 du code de commerce transmet les informations et pièces à la direction générale des finances publiques selon les modalités prévues à l'article R. 123-7 du même code.",
    "Pour cette transmission, l'organisme unique réutilise les informations et pièces à jour déjà détenues légalement par l'administration, lorsque leur réutilisation est autorisée. Il ne les demande pas à nouveau à l'entreprise. Cette réutilisation respecte les secrets protégés par la loi et le droit de l'entreprise de faire rectifier à la source les données inexactes.",
],
    'À droit constant, la transmission est reformulée avec l’organisme unique comme sujet. Réforme de fond issue du volet entreprise de policy.json : obligation de réutiliser les données et pièces déjà disponibles légalement et à jour, suppression de leur nouvelle demande, maintien des secrets et du droit de rectification. Le guichet existant est conservé.',
    'Coordination nécessaire avec les articles R. 123-1 et R. 123-7 du code de commerce, hors des cinq codes traités, pour organiser le réemploi dans le circuit de transmission existant et les corrections à la source. La rédaction ne crée pas d’autorisation d’accès à des données couvertes par un secret et reste limitée aux réutilisations autorisées. Le premier alinéa et ses renvois sont maintenus à leur place ; l’obligation nouvelle est ajoutée après lui. La note d’entrée en vigueur au 1er janvier 2023 (article 45 du décret n° 2022-1014 du 19 juillet 2022) ne date que le dispositif source, pas l’ajout proposé.')

add('371 AK', [
    "Sur demande de la direction générale des finances publiques, le teneur du Registre national des entreprises radie toute entreprise inscrite à ce registre qui ne respecte pas son obligation de faire accréditer un représentant assujetti établi en France dans les conditions de l'article 289 A du code général des impôts.",
    "La procédure de radiation passe par l'organisme unique mentionné à l'article R. 123-1 du code de commerce, selon les modalités prévues à l'article R. 123-7 du même code.",
],
    'Réécriture à droit constant : formulation active de la radiation, en conservant la demande préalable de la direction générale des finances publiques et le passage par l’organisme unique. Aucune réforme de fond ni nouvelle cause de radiation.',
    'Le représentant demeure assujetti et établi en France, dans le champ de l’article 289 A ; les renvois à R. 123-1 et R. 123-7 du code de commerce sont conservés. Le réemploi proposé à l’article 371 AJ ne supprime pas cette obligation d’accréditation. La note source vise l’entrée en vigueur le 1er janvier 2023 prévue par l’article 3 du décret n° 2022-1620 du 23 décembre 2022.')

add('372', [
    "I. – Relèvent de l'article 1655 ter du code général des impôts les sociétés suivantes :",
    "1° Les sociétés qui justifient qu'à la date de publication de la loi n° 63-254 du 15 mars 1963, elles n'exerçaient en fait que des activités concourant à la réalisation de l'objet défini à l'article 1655 ter et qui ont, depuis cette date, respecté sans interruption les dispositions de cet article ;",
    "2° Les sociétés constituées après la date de publication de la même loi dont l'activité est restée, depuis leur création, conforme à celle prévue au 1°.",
    "Le régime prévu à l'article 1655 ter du code général des impôts s'applique aux sociétés visées aux premier, deuxième et troisième alinéas ainsi qu'à leurs membres. Il cesse de s'appliquer à la date à laquelle ces sociétés cessent, le cas échéant, de remplir les conditions prévues à ces mêmes alinéas.",
    "II. – Pour les sociétés autres que celles visées au I et pour leurs membres, le régime fiscal prévu à l'article 1655 ter du code général des impôts ne s'applique, le cas échéant, dans les conditions énoncées au 2 bis de l'article 221 du même code, qu'à compter de la date à laquelle ces sociétés modifient leurs statuts et leur activité réelle pour se conformer à l'article 1655 ter.",
    "III. – Par dérogation au II, les nouvelles règles d'assiette de la taxe foncière et des taxes assimilées qui s'y rapportent ne s'appliquent, le cas échéant, qu'à partir du 1er janvier de l'année suivant celle au cours de laquelle sont intervenues les modifications entraînant le changement de régime d'imposition.",
],
    'Réécriture à droit constant : distinction des deux catégories historiques de sociétés, de la fin du régime et des dates d’effet propres aux autres sociétés et à la taxe foncière. Les six alinéas, les I à III et les 1° et 2° sont conservés. Aucune réforme de fond.',
    'La date du 15 mars 1963 reste celle de la loi citée ; le critère demeure sa date de publication, sans les confondre. Le renvoi aux trois premiers alinéas conserve ses cibles. Le report au 1er janvier de l’année suivante ne concerne que la taxe foncière et les taxes assimilées, non tout le régime. Renvois maintenus à 1655 ter et au 2 bis de 221 ; le régime des sociétés de copropriété n’est pas remplacé par la réforme générale du taux normal d’IS.')

add('373', [
    "Dans les trois mois suivant la date à laquelle l'article 1655 ter du code général des impôts leur devient applicable, les sociétés visées à l'article 372 remettent au service des impôts du lieu de leur principal établissement une déclaration souscrite en un seul exemplaire, sur un imprimé conforme au modèle annexé au décret n° 63-679 du 9 juillet 1963 (1).",
    'Elles joignent à cette déclaration un seul exemplaire de leurs statuts en vigueur à cette même date, sauf lorsque le service des impôts les réutilise conformément au quatrième alinéa.',
    "La société renouvelle sa déclaration dans les trois mois du changement lorsque les indications déclarées cessent d'être exactes.",
    "Pour l'application du présent article, le service des impôts réutilise les informations et pièces déjà détenues légalement par l'administration et correspondant à la situation à déclarer, lorsque leur réutilisation est autorisée. Il ne les demande pas à nouveau à la société. Cette réutilisation respecte les secrets protégés par la loi et le droit de la société de faire rectifier à la source les données inexactes. Elle ne dispense pas la société de déclarer, dans les délais prévus au présent article, les informations nouvelles ou modifiées.",
    '(1) Voir le Journal officiel du 12 juillet 1963, p. 6319.',
],
    'À droit constant, les obligations de la société, les deux délais de trois mois et le service destinataire sont formulés directement. Réforme de fond de simplification prévue par policy.json : la déclaration en triple exemplaire et les deux exemplaires des statuts sont remplacés par un seul exemplaire de chaque document ; un alinéa impose le réemploi autorisé des informations et pièces déjà détenues, avec secrets protégés et rectification.',
    'Les réductions de trois à un et de deux à un exemplaire sont des modifications de fond explicites, limitées aux copies administratives : elles ne changent ni les renseignements requis ni les événements à déclarer. Coordonner le formulaire annexé au décret n° 63-679 du 9 juillet 1963 et les modalités de réception du service ; aucun téléservice nouveau ni échange non autorisé n’est créé. Les trois alinéas normatifs d’origine restent dans leur ordre ; le réemploi est ajouté au quatrième, auquel renvoie désormais le deuxième alinéa pour les statuts. Les pièces réutilisées doivent correspondre à la situation à déclarer, notamment les statuts à la date pertinente ; les données nouvelles ou modifiées restent à déclarer dans les délais. La référence intégrale au Journal officiel du 12 juillet 1963, page 6319, est conservée ; il ne s’agit pas d’une date d’entrée en vigueur de la réforme proposée.')

add('374', [
    "Outre les renseignements dont la production est déjà prévue par le code général des impôts, les sociétés visées à l'article 372 font parvenir au service des impôts du lieu de leur principal établissement, au plus tard le deuxième jour ouvré suivant le 1er mai, une déclaration en un seul exemplaire. Pour l'année précédente, cette déclaration indique la part revenant ou incombant à chaque associé dans chacun des éléments suivants :",
    'a. Les revenus bruts de la société ;',
    "b. Le montant des dépenses de réparation et d'entretien, des frais de gérance et des rémunérations des gardes et concierges effectivement supportés par la société ;",
    "c. Le montant des impositions perçues à raison des immeubles sociaux au profit des collectivités locales ou de certains établissements publics et d'organismes divers, à l'exclusion de celles qui incombent normalement à l'occupant ;",
    "d. Le montant des intérêts des dettes contractées pour la conservation, l'acquisition, la construction, la réparation ou l'amélioration des immeubles sociaux ;",
    "e. Les frais de gestion et d'assurance payés par la société ;",
    'f. Le cas échéant, toutes les autres charges non énumérées ci-dessus mais effectivement supportées par la société.',
    "Le contrôle de cette déclaration s'effectue dans les conditions prévues à l'article L. 53 du livre des procédures fiscales.",
],
    'À droit constant, présentation directe de l’obligation annuelle et des six postes répartis entre associés, en maintenant leur lettrage et leurs qualifications. Réforme de fond de simplification prévue par policy.json : suppression de la seconde copie de la déclaration, désormais produite en un seul exemplaire. Aucun poste, délai ou pouvoir de contrôle n’est supprimé.',
    'Le passage de deux à un exemplaire concerne uniquement la multiplicité des copies. Sont conservés le deuxième jour ouvré suivant le 1er mai, l’année précédente, les parts revenant ou incombant aux associés, les exclusions des impositions de l’occupant, les cinq objets d’emprunt et les charges effectivement supportées. Coordonner le formulaire déclaratif pour supprimer l’exigence de double exemplaire ; le contrôle de L. 53 du livre des procédures fiscales demeure applicable. Les huit alinéas logiques et les lettres a à f conservent leur ordre.')

add('375', [
    "I. – Lorsqu'une entreprise soumise à l'impôt sur le revenu dans la catégorie des bénéfices industriels et commerciaux ou à l'impôt sur les sociétés détient à son actif des actions ou parts d'une société visée à l'article 372, elle doit pratiquer dans sa comptabilité l'amortissement de la fraction des immeubles sociaux correspondant à ses droits. Cet amortissement sert à déterminer le revenu net afférent à ces actions ou parts.",
    "Sous réserve du II, l'amortissement est calculé sur le prix de revient des actions ou parts ou, en cas de révision des bilans, sur leur valeur nette de réévaluation.",
    "II. – Pour l'application du I, à la date d'ouverture du premier exercice arrêté après le 31 août 1963 par la société immobilière, la fraction des immeubles sociaux correspondant aux actions ou parts figurant à cette date à l'actif de l'entreprise est réputée déjà amortie du montant des amortissements que cette entreprise a précédemment retenus pour déterminer les revenus imposables de ces actions ou parts. Cette règle s'applique que les amortissements aient été pratiqués par la société immobilière ou par l'entreprise actionnaire ou associée. Ces amortissements doivent être inscrits ou maintenus, selon le cas, au passif du bilan de l'entreprise actionnaire ou associée.",
    "Pour les immeubles définis au premier alinéa du présent II, l'amortissement est calculé sur la valeur d'actif des actions ou parts correspondantes, diminuée du montant des amortissements mentionnés ci-dessus, et en fonction du nombre d'années restant à courir jusqu'au terme de la période normale d'utilisation de ces immeubles.",
],
    'Réécriture à droit constant : explicitation de l’entreprise qui comptabilise l’amortissement et décomposition de la règle historique de reprise des amortissements antérieurs. La base de calcul et la durée résiduelle restent dans leurs alinéas respectifs. Aucune réforme de fond ni nouveau régime d’amortissement.',
    'Le 31 août 1963, la date d’ouverture du premier exercice arrêté après cette date, l’inscription des titres à l’actif à cette ouverture, les amortissements précédemment retenus, leur maintien au passif, la diminution de la base et la durée normale restante sont conservés. Le dernier renvoi au premier alinéa est explicité comme visant celui du II. Les orientations générales d’investissement de policy.json ne définissent aucun nouveau taux ou durée d’amortissement applicable à ce régime historique.')

add('376-0 bis', [
    "Le grade d'administrateur des finances publiques adjoint constitue le grade minimal prévu au second alinéa de l'article 1658 du code général des impôts.",
],
    'Réécriture à droit constant : l’intitulé du grade est placé en tête et son caractère minimal, résultant du second alinéa de l’article 1658, est explicité. Aucune réforme de fond.',
    'L’intitulé du grade est conservé exactement. Le second alinéa de l’article 1658 du corpus a été consulté : il prévoit le grade minimal fixé par décret en Conseil d’Etat pour la délégation des pouvoirs de recouvrement par voie de rôle ; la réécriture n’en change ni les bénéficiaires ni la portée.')

add('379', [
    "1. Les sociétés étrangères qui réalisent des bénéfices en France sans y avoir leur siège social doivent déposer une déclaration destinée à la liquidation de la retenue à la source exigible en application de l'article 115 quinquies du code général des impôts.",
    "2. Elles adressent cette déclaration au service des impôts dont dépend le lieu d'établissement de l'impôt sur les sociétés, dans le même délai que la déclaration des résultats.",
    "La déclaration est établie sur les imprimés fournis par l'administration. Elle indique séparément, en euros :",
    "– les bénéfices et plus-values à retenir pour l'assiette de l'impôt sur les sociétés ;",
    "– l'impôt correspondant ;",
    '– les bénéfices et plus-values réalisés en France et exonérés de cet impôt.',
    '3. La société accompagne sa déclaration du versement de la retenue exigible.',
],
    'Réécriture à droit constant : les sociétés deviennent le sujet du dépôt, de l’envoi et du versement ; les trois montants à distinguer sont conservés en alinéas. Les subdivisions 1 à 3 restent en place. Aucune réforme de fond.',
    'Conservation du champ des sociétés étrangères sans siège en France, du renvoi à 115 quinquies, du délai de la déclaration de résultats et des montants exprimés en euros. La réforme du taux national normal de l’IS relève de l’article 219 ; elle ne crée ici ni un taux de retenue nouveau ni une exonération des bénéfices réinvestis. Le montant de l’IS correspondant reste celui résultant des règles applicables.')

add('380', [
    "I. – La société peut demander une nouvelle liquidation de la retenue à la source acquittée dans les conditions prévues à l'article 379, sur la base de ses distributions effectives.",
    "Sont prises en compte les distributions au sens des articles 109 et suivants du code général des impôts effectuées pendant les douze mois suivant la clôture de l'exercice ou de la période dont les résultats ont servi au calcul de la retenue à la source. Elles sont retenues quel que soit l'exercice auquel elles se rapportent.",
    'II. – La société présente sa demande de révision dans les trois mois suivant l’expiration de la période de douze mois définie au I.',
    'Pour chaque distribution, la demande indique :',
    '– sa date ;',
    '– son montant en euros, calculé au cours des changes du jour de la mise en paiement.',
    "III. – La société joint à sa demande de révision les copies des décisions ou délibérations relatives aux distributions mentionnées, ainsi que celles des procès-verbaux ou comptes rendus des assemblées générales d'actionnaires ou d'associés ayant approuvé les comptes de l'exercice. Ces copies sont accompagnées, le cas échéant, de traductions en langue française.",
],
    'Réécriture à droit constant : définition des distributions en deux phrases, identification de la société qui demande la révision et séparation des pièces justificatives et de leur traduction. Les I à III et les deux mentions par distribution sont maintenus. Aucune réforme de fond.',
    'Les douze mois courent depuis la clôture de l’exercice ou de la période retenue pour la retenue ; les trois mois de demande courent depuis l’expiration de ces douze mois. Maintien des distributions quel que soit leur exercice de rattachement, du cours des changes au jour de mise en paiement, des deux familles de justificatifs et des traductions si nécessaires. La limite au principal demeure celle de l’article 382, sans modification des pénalités.')

add('381', [
    "La société peut également obtenir la restitution de la retenue à la source opérée en application de l'article 379 dans la mesure où elle justifie que les bénéficiaires des distributions définies à l'article 380 ont leur domicile réel ou leur siège social en France.",
    'Pour étayer sa demande de révision, la société produit une liste détaillée indiquant, pour chacun de ces bénéficiaires :',
    '– ses nom et prénoms ou sa raison sociale ;',
    "– l'adresse de son domicile réel ou de son siège ;",
    '– le montant des sommes versées et la date de leur mise en paiement.',
    "La société peut présenter sa demande de révision jusqu'au 31 décembre de l'année suivant celle de la mise en paiement des produits.",
    'Pour obtenir la restitution, la société doit justifier du transfert des sommes correspondantes aux bénéficiaires des distributions.',
],
    'Réécriture à droit constant : formulation directe de la faculté de restitution, du contenu de la liste nominative et de la preuve du transfert. Les sept alinéas logiques de la source sont conservés. Aucune réforme de fond.',
    'Le domicile reste réel et l’alternative avec le siège social en France est conservée. Maintien des trois groupes d’informations par bénéficiaire, du 31 décembre de l’année suivant la mise en paiement et de la preuve effective du transfert. Le délai distinct de l’article 380 n’est pas substitué à celui du présent article ; les deux voies restent coordonnées avec la limitation au principal de l’article 382.')

add('382', [
    "Les révisions prévues aux articles 380 et 381 portent exclusivement sur le montant principal de la retenue à la source. Elles ne s'appliquent à aucune majoration ni pénalité.",
],
    'Réécriture à droit constant : la limite au principal et l’exclusion des majorations et pénalités sont énoncées en deux phrases directes. Aucune réforme de fond.',
    'Les deux renvois, 380 et 381, sont conservés ; aucune remise, restitution ou révision des accessoires n’est créée.')

add('382 bis', [
    "Le demandeur adresse sa demande en décharge de responsabilité prévue au II de l'article 1691 bis du code général des impôts au directeur départemental des finances publiques du lieu d'établissement des impositions concernées. Lorsque les impositions et pénalités sont recouvrées par un service à compétence nationale, il adresse sa demande au directeur chargé de ce service. Il joint toutes les justifications nécessaires à l'appréciation de sa situation financière et patrimoniale, nette de charges.",
],
    'Réécriture à droit constant : scission de la règle de compétence et de son cas particulier, puis identification du demandeur comme responsable des justificatifs. Le seul alinéa normatif et le renvoi au II de 1691 bis sont conservés. Aucune réforme de fond.',
    'Le directeur du lieu d’établissement des impositions demeure compétent, sous réserve du service à compétence nationale qui recouvre les impositions et pénalités. La justification porte toujours sur la situation financière et patrimoniale nette de charges ; aucune nouvelle condition de décharge ni pièce supplémentaire déterminée n’est ajoutée.')


assert len(sources) == 24
assert len(drafts) == 24
answer = []
for source in sources:
    identifiers = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.append({**identifiers, **drafts[source['number']]})
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
