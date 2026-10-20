import json
from pathlib import Path


def paragraphs(*items):
    return "\n".join(f"<p>{item}</p>" for item in items)


drafts = {}


def add(number, text, reason, notes):
    drafts[number] = {
        "proposed_xml": text,
        "reason": reason,
        "review_notes": notes,
        "status": "rewrite_draft",
    }


add(
    "L213-5",
    paragraphs(
        "Lorsqu'une déclaration d'utilité publique a été prononcée et que le titulaire du droit de préemption en est également le bénéficiaire, l'exercice de ce droit éteint les droits réels et personnels dans les mêmes conditions qu'un accord amiable en matière d'expropriation.",
        "Lorsqu'une déclaration d'utilité publique a été prononcée, la cession d'un bien à son bénéficiaire échappe au droit de préemption.",
    ),
    "Réécriture à droit constant : la double condition tenant à la déclaration d'utilité publique et à l'identité de son bénéficiaire avec le titulaire du droit est placée avant l'effet extinctif. L'exclusion de la préemption lors d'une cession au bénéficiaire reste dans un alinéa distinct. Aucune réforme de fond.",
    "Les deux alinéas sont conservés. L'assimilation à l'accord amiable demeure limitée à l'extinction des droits réels et personnels ; elle n'est pas étendue aux autres effets de l'expropriation. Les mesures de policy.json n'affectent pas cet article.",
)

add(
    "L213-6",
    paragraphs(
        "Lorsqu'un bien soumis au droit de préemption est exproprié pour cause d'utilité publique, la date de référence mentionnée à l'article L. 322-2 du code de l'expropriation pour cause d'utilité publique est celle que prévoit le a de l'article L. 213-4.",
        "Lorsqu'un bien est exproprié pour cause d'utilité publique sur le fondement d'une déclaration d'utilité publique, la date de référence mentionnée à l'article L. 322-2 du code de l'expropriation pour cause d'utilité publique est celle que prévoit le a de l'article L. 213-4 du présent code si, à la date de cette déclaration, le bien était soumis, en application de l'article L. 212-2, au droit de préemption applicable dans le périmètre d'une zone d'aménagement différé. Si la déclaration d'utilité publique est prorogée, la date de référence est déterminée en application de l'article L. 322-2 du code de l'expropriation pour cause d'utilité publique.",
    ),
    "Réécriture à droit constant : la seconde règle est organisée autour de la date de la déclaration d'utilité publique, puis de la situation du bien à cette date. La règle particulière applicable à une prorogation reste explicite. Aucune réforme de fond.",
    "Renvois au a de L. 213-4, à L. 212-2 et à L. 322-2 conservés. Le a de L. 213-4 a été vérifié dans le corpus public : il distingue les dates selon la situation du bien et de la zone. Ces règles ne sont pas remplacées par une date unique. Deux alinéas conservés.",
)

add(
    "L213-7",
    paragraphs(
        "En l'absence d'accord sur le prix, le propriétaire d'un bien soumis au droit de préemption qui a manifesté son intention d'aliéner ce bien peut ensuite retirer son offre. Dans les mêmes circonstances, le titulaire du droit de préemption peut renoncer à exercer ce droit au cours de la procédure.",
        "Lorsque le prix est fixé par le juge, les parties disposent de deux mois à compter du jour où la décision juridictionnelle devient définitive pour accepter ce prix ou renoncer à la mutation. Leur silence pendant ce délai vaut acceptation du prix fixé par le juge et, à l'expiration du délai, transfert de propriété au titulaire du droit de préemption.",
    ),
    "Réécriture à droit constant : les facultés respectives du propriétaire et du titulaire sont formulées séparément ; le point de départ du délai de décision après fixation judiciaire du prix est explicité. Les effets du silence restent ceux de la source. Aucune réforme de fond.",
    "Délai de deux mois et condition d'absence d'accord sur le prix conservés. Difficulté préexistante : cet article rattache le transfert de propriété au silence à l'expiration des deux mois, tandis que L. 213-14 le situe à la plus tardive des dates du paiement et de l'acte authentique. Les deux formulations sont maintenues ; leur articulation nécessite une coordination expresse, non définie par policy.json.",
)

add(
    "L213-8",
    paragraphs(
        "Lorsque le titulaire du droit de préemption renonce à exercer son droit avant la fixation judiciaire du prix, le propriétaire peut vendre le bien au prix indiqué dans sa déclaration. Ce prix est révisé, s'il y a lieu, selon les variations du coût de la construction constatées par l'Institut national de la statistique et des études économiques depuis la date de la déclaration.",
        "Si le propriétaire n'a pas vendu le bien par acte authentique dans les trois ans suivant la renonciation au droit de préemption, il doit déposer une nouvelle déclaration préalable mentionnée à l'article L. 213-2.",
        "Lorsque le titulaire du droit de préemption a renoncé à exercer son droit sur un bien dont le prix a été fixé judiciairement, il ne peut plus l'exercer à l'égard du même propriétaire pendant les cinq ans suivant le jour où la décision juridictionnelle devient définitive, si le propriétaire vend le bien pendant ce délai au prix fixé par la juridiction. Ce prix est révisé, s'il y a lieu, selon les variations du coût de la construction constatées par l'Institut national de la statistique et des études économiques depuis cette décision.",
        "Pour l'application du deuxième alinéa du présent article, la vente est réalisée à la date de l'acte notarié ou de l'acte authentique en la forme administrative qui constate le transfert de propriété.",
        "Lorsque la juridiction administrative annule ou déclare illégale la décision d'exercer le droit de préemption et que la propriété n'a pas été transférée, le titulaire ne peut exercer à nouveau ce droit sur le bien pendant un an à compter du jour où la décision juridictionnelle devient définitive. Le propriétaire n'est alors pas tenu de respecter les prix et conditions indiqués dans sa déclaration d'intention d'aliéner.",
    ),
    "Réécriture à droit constant : les trois situations de renonciation ou d'illégalité sont énoncées par conditions, et les mécanismes de révision du prix sont détachés en phrases distinctes. La définition de la date de vente demeure au quatrième alinéa. Aucune réforme de fond.",
    "Cinq alinéas conservés, notamment le renvoi du quatrième au deuxième. Délais de trois ans, cinq ans et un an maintenus, avec leurs points de départ distincts. La protection de cinq ans reste attachée au même propriétaire et à la vente au prix judiciaire éventuellement révisé ; l'interdiction d'un an reste subordonnée à l'absence de transfert. Les deux bases temporelles de révision du prix sont conservées.",
)

add(
    "L213-9",
    paragraphs(
        "Lorsque le titulaire du droit de préemption lui notifie son intention d'acquérir le bien dans les conditions prévues à l'article L. 211-5 ou à l'article L. 212-3, le propriétaire doit en informer les locataires, les preneurs et les occupants de bonne foi du bien. Il doit également les faire connaître au titulaire du droit de préemption.",
        "L'exercice du droit de préemption sur ce bien exclut l'application des cinq premiers alinéas de l'article L. 145-46-1 du code de commerce.",
    ),
    "Réécriture à droit constant : les deux obligations d'information du propriétaire sont distinguées et leur déclencheur est conservé. L'exclusion des dispositions commerciales est formulée directement. Aucune réforme de fond.",
    "Les catégories de personnes informées et les renvois à L. 211-5 et L. 212-3 sont maintenus. L'exclusion reste limitée aux cinq premiers alinéas de L. 145-46-1 et à l'exercice de la préemption sur le bien concerné. Deux alinéas conservés.",
)

add(
    "L213-10",
    paragraphs(
        "Même si une disposition ou une stipulation prévoit le contraire, les preneurs de biens ruraux, les locataires ou occupants de bonne foi de locaux à usage d'habitation et les locataires de locaux à usage commercial, industriel ou artisanal ne peuvent s'opposer aux travaux de restauration ou de transformation intérieure ni à la démolition de ces locaux, lorsque ceux-ci se situent dans un bien acquis par voie de préemption ou en application de l'article L. 211-5 ou de l'article L. 212-3.",
        "Lorsque les travaux rendent nécessaire l'évacuation de tout ou partie des locaux, ces personnes doivent les évacuer. Le nouveau propriétaire du bien doit alors respecter les obligations prévues aux articles L. 314-1 et suivants.",
        "Même si une disposition ou une stipulation prévoit le contraire, ces personnes peuvent, à tout moment, déclarer au titulaire du droit de préemption leur intention de quitter les lieux et de résilier le bail. Le titulaire ne peut ni s'y opposer ni leur réclamer une indemnité à ce titre. Il doit leur verser les indemnités auxquelles elles peuvent prétendre, notamment celles qui peuvent leur être dues au titre des améliorations qu'elles ont apportées au fonds loué. En cas de litige, la juridiction compétente en matière d'expropriation fixe ces indemnités.",
    ),
    "Réécriture à droit constant : les personnes concernées, l'obligation d'évacuation et les obligations du nouveau propriétaire sont identifiées expressément. La résiliation à l'initiative des occupants et ses conséquences indemnitaires sont réparties en phrases courtes dans le même alinéa. Aucune réforme de fond.",
    "Trois alinéas conservés. Maintien des deux dérogations aux dispositions ou stipulations contraires, de la faculté de départ à tout moment et de la compétence du juge de l'expropriation. Le renvoi à L. 314-1 et suivants conserve les obligations envers les occupants ; il n'est pas remplacé par une simple indemnité. Cet article ne crée aucune faculté d'expulsion privée et ne transpose pas la voie de rénovation locative de vingt-quatre mois, qui appelle notamment la loi n° 89-462 hors de ce code.",
)

add(
    "L213-11",
    paragraphs(
        "Les biens acquis par l'exercice du droit de préemption doivent être utilisés ou aliénés pour l'un des objets mentionnés au premier alinéa de l'article L. 210-1. Cet objet peut différer de celui indiqué dans la décision de préemption. L'utilisation ou l'aliénation d'un bien au profit d'une personne privée autre que le concessionnaire d'une opération d'aménagement ou une société d'habitations à loyer modéré exige une délibération motivée du conseil municipal ou, le cas échéant, une décision motivée du délégataire du droit de préemption.",
        "L'aliénation d'un bien en application du premier alinéa du présent article exclut l'application des cinq premiers alinéas de l'article L. 145-46-1 du code de commerce.",
        "Lorsque le titulaire du droit de préemption décide d'utiliser ou d'aliéner un bien acquis depuis moins de cinq ans par l'exercice de ce droit pour un objet autre que ceux mentionnés au premier alinéa de l'article L. 210-1, il doit informer les anciens propriétaires ou leurs ayants cause universels ou à titre universel de sa décision. Il doit leur proposer en priorité d'acquérir le bien.",
        "Tout changement d'affectation d'un bien acquis par l'exercice du droit de préemption, dans la limite des objets prévus à l'article L. 210-1, exige une décision de l'organe délibérant de la collectivité.",
        "En l'absence d'accord amiable, la juridiction compétente en matière d'expropriation fixe le prix selon les règles mentionnées à l'article L. 213-4.",
        "Si les anciens propriétaires ou leurs ayants cause universels ou à titre universel n'acceptent pas l'acquisition dans les trois mois suivant la notification de la décision juridictionnelle devenue définitive, ils sont réputés y avoir renoncé.",
        "Lorsque les anciens propriétaires ou leurs ayants cause universels ou à titre universel ont renoncé expressément ou tacitement à l'acquisition dans les conditions prévues aux alinéas précédents, le titulaire du droit de préemption doit aussi proposer l'acquisition à la personne qui avait l'intention d'acquérir le bien.",
        "Le titulaire du droit de préemption n'est obligé de suivre cette procédure que si le nom de l'acquéreur figurait dans la déclaration mentionnée à l'article L. 213-2.",
    ),
    "Réécriture à droit constant : les finalités de l'utilisation, la motivation de certaines décisions et l'ordre des offres d'acquisition sont rendus plus lisibles. Le régime du prix et celui de l'acceptation restent dans leurs alinéas respectifs. Aucune réforme de fond.",
    "Huit alinéas conservés : priorité des anciens propriétaires au troisième, délai d'acceptation au sixième et offre à l'acquéreur initial au septième. Les exceptions concernant le concessionnaire et les sociétés d'HLM, le délai inférieur à cinq ans et celui de trois mois sont maintenus. Les renvois de L. 213-12 aux deuxième et sixième alinéas ne correspondent pas aux obligations d'offre de cet article ; cette incohérence préexistante est signalée sans déplacer les alinéas. Le dernier alinéa conserve la condition d'inscription du nom et la désignation « cette procédure » de la source, sans en étendre ou réduire silencieusement la portée.",
)

add(
    "L213-11-1",
    paragraphs(
        "Si, après le transfert de propriété, la juridiction administrative annule ou déclare illégale la décision de préemption, le titulaire du droit de préemption doit proposer en priorité aux anciens propriétaires ou à leurs ayants cause universels ou à titre universel d'acquérir le bien.",
        "Le prix proposé a pour objet de rétablir les conditions de la transaction empêchée par l'exercice du droit de préemption, sans enrichissement injustifié de l'une des parties. En l'absence d'accord amiable, la juridiction compétente en matière d'expropriation fixe ce prix selon les règles mentionnées à l'article L. 213-4.",
        "Si les anciens propriétaires ou leurs ayants cause universels ou à titre universel n'acceptent pas l'acquisition dans les trois mois suivant la notification de la décision juridictionnelle devenue définitive, ils sont réputés y avoir renoncé.",
        "Lorsque les anciens propriétaires ou leurs ayants cause universels ou à titre universel ont renoncé expressément ou tacitement à l'acquisition dans les conditions prévues aux trois premiers alinéas du présent article, le titulaire du droit de préemption doit aussi proposer l'acquisition à la personne qui avait l'intention d'acquérir le bien, si son nom figurait dans la déclaration mentionnée à l'article L. 213-2.",
    ),
    "Réécriture à droit constant : le transfert préalable est placé dans la condition d'ouverture et les sujets des obligations d'offre et de fixation du prix sont explicités. La priorité et l'offre subsidiaire sont maintenues dans quatre alinéas. Aucune réforme de fond.",
    "Maintien de l'annulation et de la déclaration d'illégalité, de l'absence d'enrichissement injustifié, du délai de trois mois et de son point de départ à la notification de la décision définitive. Le quatrième alinéa vise toujours les trois premiers et conditionne l'offre à l'acquéreur initial à son identification dans la déclaration de L. 213-2. Les renvois de L. 213-12 au premier et au dernier alinéa restent utilisables.",
)

add(
    "L213-12",
    paragraphs(
        "Lorsque les obligations prévues au deuxième alinéa de l'article L. 213-11 ou au premier alinéa de l'article L. 213-11-1 ne sont pas respectées, les anciens propriétaires ou leurs ayants cause universels ou à titre universel saisissent le tribunal de l'ordre judiciaire d'une action en dommages-intérêts contre le titulaire du droit de préemption.",
        "Lorsque les obligations prévues au sixième alinéa de l'article L. 213-11 ou au dernier alinéa de l'article L. 213-11-1 ne sont pas respectées, la personne qui avait l'intention d'acquérir le bien saisit le tribunal de l'ordre judiciaire d'une action en dommages-intérêts contre le titulaire du droit de préemption.",
        "Dans les cas prévus aux articles L. 213-11 et L. 213-11-1, une personne qui renonce à la rétrocession peut néanmoins saisir le tribunal de l'ordre judiciaire d'une action en dommages-intérêts contre le titulaire du droit de préemption.",
        "Le délai de prescription de l'action en dommages-intérêts est de cinq ans. Il court :",
        "1° Dans le cas prévu à l'article L. 213-11, à compter de la mention de l'affectation ou de l'aliénation du bien au registre mentionné à l'article L. 213-13 ;",
        "2° Dans le cas prévu à l'article L. 213-11-1, à compter du jour où la décision de la juridiction administrative devient définitive.",
    ),
    "Réécriture à droit constant : les titulaires des actions et les deux points de départ de la prescription sont énoncés directement. La possibilité d'agir malgré une renonciation à la rétrocession est formulée positivement. Aucune réforme de fond ; les renvois incohérents de la source ne sont pas corrigés tacitement.",
    "Incohérence préexistante à coordonner expressément : le premier alinéa vise le deuxième alinéa de L. 213-11, qui exclut cinq alinéas du code de commerce, alors que l'obligation d'offre prioritaire aux anciens propriétaires figure au troisième ; le deuxième alinéa vise le sixième alinéa de L. 213-11, qui traite de leur renonciation, alors que l'offre à l'acquéreur initial figure au septième. Les renvois source sont conservés dans proposed_xml. Les renvois à L. 213-11-1 sont cohérents avec ses quatre alinéas. Prescription de cinq ans, deux points de départ et subdivisions 1° et 2° conservés.",
)

add(
    "L213-13",
    paragraphs(
        "Dès qu'un droit de préemption est institué ou créé sur son territoire en application du présent titre, la commune doit ouvrir un registre. Elle y inscrit toutes les acquisitions réalisées par l'exercice de ce droit ou par sa délégation, ainsi que l'utilisation effective des biens acquis.",
        "Toute personne a le droit de consulter ce registre et d'en obtenir un extrait.",
    ),
    "Réécriture à droit constant : l'ouverture du registre et son contenu sont présentés en deux phrases dont la commune est le sujet. Le droit de consultation et d'extrait reste accessible à toute personne. Aucune réforme de fond.",
    "Deux alinéas conservés. Le registre couvre toutes les acquisitions par exercice ou délégation du droit et l'utilisation effective des biens. Renvoi de L. 213-12 à ce registre maintenu ; aucune nouvelle formalité ou restriction d'accès n'est introduite.",
)

add(
    "L213-14",
    paragraphs(
        "Lorsqu'un bien est acquis par voie de préemption ou dans les conditions prévues à l'article L. 211-5, la propriété est transférée à la plus tardive des deux dates suivantes : celle du paiement et celle de l'acte authentique.",
        "Le prix d'acquisition doit être payé ou, si un obstacle empêche le paiement, consigné dans les quatre mois suivant, selon le cas, la décision d'acquérir le bien au prix indiqué par le vendeur ou accepté par lui, la décision définitive de la juridiction compétente en matière d'expropriation, ou la date de l'acte ou du jugement d'adjudication.",
        "Si le délai prévu au deuxième alinéa du présent article n'est pas respecté, le vendeur peut aliéner librement son bien.",
        "Le propriétaire qui a repris son bien dans les conditions prévues au présent article peut ensuite l'aliéner librement.",
    ),
    "Réécriture à droit constant : la date du transfert est exprimée comme une comparaison entre deux dates ; les différentes origines du délai de paiement sont reliées par « selon le cas ». Les conséquences du dépassement du délai restent dans les troisième et quatrième alinéas. Aucune réforme de fond.",
    "Délai de quatre mois, consignation seulement en cas d'obstacle au paiement et trois faits de départ alternatifs conservés. Le quatrième alinéa est maintenu malgré son recoupement avec le troisième. Difficulté préexistante avec L. 213-7, qui rattache le transfert au silence après fixation judiciaire : aucune conciliation de fond n'est inventée. L. 212-3 renvoie également à cet article en cas d'acquisition ; ce renvoi du corpus reste intact.",
)

add(
    "L213-15",
    paragraphs(
        "Jusqu'au paiement intégral du prix, l'ancien propriétaire continue de jouir du bien acquis par voie de préemption.",
    ),
    "Réécriture à droit constant : la limite temporelle du maintien de la jouissance est placée en tête de phrase, sans modifier son titulaire ni son objet. Aucune réforme de fond.",
    "Le maintien de la jouissance demeure lié au paiement intégral du prix, sans substitution de la date de l'acte authentique ni ajout d'une indemnité. Alinéa unique conservé.",
)

add(
    "L213-16",
    paragraphs(
        "Les biens acquis par l'exercice du droit de préemption sont soumis aux dispositions de l'article L. 221-2.",
    ),
    "Réécriture à droit constant : les biens soumis au régime de L. 221-2 deviennent le sujet de la phrase. Le renvoi reste intégral. Aucune réforme de fond.",
    "L. 221-2 a été lu dans le corpus public : il traite notamment de la gestion des réserves foncières, des cessions, des concessions temporaires et des préavis agricoles. Le renvoi est conservé sans en réduire la portée ni importer ses subdivisions dans cet article à alinéa unique.",
)

add(
    "L213-17",
    paragraphs(
        "Lorsqu'un périmètre de zone d'aménagement différé ou un périmètre provisoire de zone d'aménagement différé est créé avant l'expiration du délai de deux mois prévu au quatrième alinéa de l'article L. 213-2, le maire doit transmettre la déclaration d'intention d'aliéner au représentant de l'État dans le département. Celui-ci instruit la déclaration selon les dispositions des articles L. 212-1 et suivants.",
        "Dans ce cas, le délai mentionné au premier alinéa du présent article commence à courir à la date de publication de l'acte créant la zone d'aménagement différé ou le périmètre provisoire de zone d'aménagement différé.",
    ),
    "Réécriture à droit constant : la transmission par le maire et l'instruction par le représentant de l'État sont réparties en deux phrases. Le nouveau point de départ du délai demeure dans le second alinéa. Aucune réforme de fond.",
    "Les deux types de périmètres et le délai de deux mois sont conservés. Vérification de L. 213-2 dans le corpus : son quatrième alinéa énonce bien le silence de deux mois ; ses règles de suspension ne sont pas réécrites ici. Le point de départ spécifique reste la publication, et non la transmission de la déclaration. Deux alinéas conservés.",
)

add(
    "L213-18",
    paragraphs(
        "Si nécessaire, un décret en Conseil d'État fixe les conditions d'application du présent chapitre.",
    ),
    "Réécriture à droit constant : « en tant que de besoin » est exprimé par une condition placée en tête de phrase. La compétence du décret en Conseil d'État est conservée. Aucune réforme de fond.",
    "L'habilitation reste limitée au présent chapitre et conserve son caractère conditionnel. Aucune date ni nouveau pouvoir réglementaire n'est ajouté.",
)

add(
    "L214-1",
    paragraphs(
        "Par une délibération motivée, le conseil municipal peut délimiter un périmètre de sauvegarde du commerce et de l'artisanat de proximité. Dans ce périmètre, les aliénations à titre onéreux de fonds artisanaux, de fonds de commerce et de baux commerciaux sont soumises au droit de préemption institué par le présent chapitre.",
        "Dans le même périmètre, le droit de préemption mentionné au premier alinéa s'applique aussi aux aliénations à titre onéreux de terrains portant ou destinés à porter des commerces dont la surface de vente est comprise entre 300 et 1 000 mètres carrés.",
        "Avant chaque aliénation à titre onéreux, le cédant doit adresser une déclaration à la commune, à peine de nullité de l'aliénation. La déclaration indique le prix, l'activité de l'acquéreur pressenti, le nombre de salariés du cédant, la nature de leur contrat de travail et les conditions de la cession. Elle comporte, le cas échéant, le bail commercial. Lorsque la cession porte sur un bail commercial ou un fonds artisanal ou commercial, elle indique aussi le chiffre d'affaires.",
        "Le titulaire exerce le droit de préemption selon les modalités prévues aux articles L. 213-4 à L. 213-7. S'il garde le silence pendant les deux mois suivant la réception de la déclaration, il est réputé renoncer à exercer ce droit. Le cédant peut alors vendre aux prix et conditions indiqués dans sa déclaration.",
    ),
    "Réécriture à droit constant : la délimitation du périmètre est distinguée de ses effets, les informations de la déclaration sont réparties en phrases et l'effet du silence a un sujet explicite. Aucune réforme de fond.",
    "Quatre alinéas conservés. Seuils de 300 et 1 000 mètres carrés de surface de vente, délai de deux mois à réception, nullité en l'absence de déclaration préalable et totalité des informations exigées maintenus. Le champ inclut les terrains seulement destinés à porter les commerces. Les adaptations propres à L. 214-2-1 demeurent distinctes ; aucune extension générale de ce régime n'est introduite.",
)

add(
    "L214-1-1",
    paragraphs(
        "Si la commune appartient à un établissement public de coopération intercommunale ayant vocation à exercer les compétences que le présent chapitre attribue à la commune, elle peut lui en déléguer tout ou partie avec son accord.",
        "La commune ou l'établissement public de coopération intercommunale délégataire mentionné au premier alinéa peut déléguer ce droit de préemption à un établissement public y ayant vocation, à une société d'économie mixte ou au concessionnaire d'une opération d'aménagement. La commune ou cet établissement peut aussi le déléguer au titulaire d'un contrat mentionné à l'article L. 300-9, si ce contrat prévoit les éléments mentionnés au deuxième alinéa du même article. La délégation peut concerner une ou plusieurs parties du périmètre de sauvegarde ou être accordée à l'occasion de l'aliénation d'un fonds de commerce, d'un fonds artisanal, d'un bail commercial ou de terrains. Les biens acquis dans ce cadre entrent dans le patrimoine du délégataire.",
        "Dans le périmètre d'une grande opération d'urbanisme au sens de l'article L. 312-3 du présent code, la collectivité territoriale ou l'établissement public cocontractant mentionné au même article exerce le droit de préemption prévu au présent chapitre. Cette collectivité ou cet établissement peut déléguer l'exercice de ce droit à un établissement public y ayant vocation ou au concessionnaire d'une opération d'aménagement.",
    ),
    "Réécriture à droit constant : les délégations communale, intercommunale et propre aux grandes opérations d'urbanisme sont distinguées. La condition relative au contrat de L. 300-9 est isolée sans changer la liste des délégataires. Aucune réforme de fond.",
    "Trois alinéas conservés. Accord de l'EPCI, délégation totale ou partielle, périmètres possibles et entrée des biens dans le patrimoine du délégataire maintenus. Le deuxième alinéa de L. 300-9 a été vérifié : le renvoi aux éléments du contrat reste intégral. La liste plus restreinte des délégataires du troisième alinéa n'est pas élargie à ceux du deuxième.",
)

add(
    "L214-2",
    paragraphs(
        "Dans les deux ans suivant la prise d'effet de l'aliénation à titre onéreux, le titulaire du droit de préemption doit rétrocéder le fonds artisanal, le fonds de commerce, le bail commercial ou le terrain à une entreprise immatriculée au registre du commerce et des sociétés ou au registre national des entreprises en tant qu'entreprise du secteur des métiers et de l'artisanat. Cette rétrocession a pour objet une exploitation destinée à préserver la diversité et à promouvoir le développement de l'activité commerciale et artisanale dans le périmètre concerné. En cas de mise en location-gérance du fonds de commerce ou du fonds artisanal, le délai peut être porté à trois ans. L'acte de rétrocession précise les conditions dans lesquelles il peut être résilié si le cessionnaire n'exécute pas le cahier des charges.",
        "L'acte de rétrocession d'un fonds de commerce doit respecter les conditions fixées au chapitre Ier du titre IV du livre Ier du code de commerce.",
        "La rétrocession d'un bail commercial exige, à peine de nullité, l'accord préalable du bailleur. Cet accord doit figurer dans l'acte de rétrocession.",
        "Pendant le délai mentionné au premier alinéa du présent article, le titulaire du droit de préemption peut mettre le fonds en location-gérance selon les conditions prévues aux articles L. 144-1 à L. 144-13 du code de commerce.",
        "Pour l'application de l'article L. 214-1 et du présent article, la désignation « titulaire du droit de préemption » comprend aussi, s'il y a lieu, le délégataire prévu à l'article L. 214-1-1.",
    ),
    "Réécriture à droit constant : l'obligation de rétrocession, son objectif d'exploitation et l'allongement éventuel du délai sont énoncés dans des phrases distinctes. L'accord du bailleur et l'inclusion du délégataire restent explicites. Aucune réforme de fond.",
    "Cinq alinéas conservés. Délais de deux ans et de trois ans, double objectif de diversité et de développement, registres d'immatriculation, cahier des charges et nullité sont maintenus. La note source renvoie à l'article 47 de l'ordonnance n° 2021-1189 du 15 septembre 2021 et fixe l'entrée en vigueur au 1er janvier 2023 : cette date historique reste un élément de contrôle et n'est pas présentée comme l'entrée en vigueur d'une réforme future. Les délais particuliers de L. 214-2-1 restent distincts.",
)

add(
    "L214-2-1",
    paragraphs(
        "Une délibération motivée peut instaurer le droit de préemption institué au présent chapitre dans le périmètre d'une grande opération d'urbanisme mentionnée à l'article L. 312-3, lorsque cette opération est mise en œuvre dans tout ou partie d'une zone d'activité économique au sens de l'article L. 318-8-1 et prévoit la transformation de cette zone, notamment pour en favoriser la mixité fonctionnelle.",
        "Les secteurs de la grande opération d'urbanisme dans lesquels ce droit est instauré peuvent être délimités par l'acte décidant de la qualification de grande opération d'urbanisme mentionné à l'article L. 312-4 ou par un acte ultérieur pris dans les mêmes formes. Cette délimitation intervient après l'avis de la commune prévu à l'article L. 312-7.",
        "Par dérogation aux articles L. 214-1 et L. 214-2, dans les secteurs où ce droit est instauré :",
        "1° Le droit de préemption s'applique aussi aux aliénations à titre onéreux de terrains accueillant ou destinés à accueillir des commerces dont la surface de vente est comprise entre 1 000 et 4 000 mètres carrés ;",
        "2° Le délai de rétrocession peut être porté à six ans ou, en cas de mise en location-gérance du fonds de commerce ou du fonds artisanal, à sept ans.",
    ),
    "Réécriture à droit constant : les conditions cumulatives liées à la grande opération d'urbanisme et à la transformation de la zone économique sont regroupées ; la consultation communale fait l'objet d'une phrase propre. Les deux dérogations restent numérotées. Aucune réforme de fond.",
    "Cinq alinéas et subdivisions 1° et 2° conservés. Maintien de la délibération motivée, des formes des actes, de l'avis communal et des quatre renvois L. 312-3, L. 318-8-1, L. 312-4 et L. 312-7. Seuils de 1 000 et 4 000 mètres carrés et possibilités de porter le délai à six ou sept ans conservés, sans les transformer en délais automatiques ni les étendre hors des secteurs concernés.",
)

add(
    "L214-3",
    paragraphs(
        "Les conditions d'application du présent chapitre sont précisées par un décret en Conseil d'État.",
    ),
    "Réécriture à droit constant : les conditions d'application deviennent le sujet de la phrase ; la nature du décret et le périmètre de l'habilitation restent identiques. Aucune réforme de fond.",
    "Alinéa unique conservé. Contrairement à L. 213-18, la source ne subordonne pas ce décret à une nécessité particulière ; aucune telle condition n'est ajoutée.",
)

add(
    "L215-1",
    paragraphs(
        "Le département peut créer des zones de préemption pour mettre en œuvre la politique prévue à l'article L. 113-8, dans les conditions fixées au présent article.",
        "Dans une commune dotée d'un plan local d'urbanisme approuvé, la création de ces zones nécessite l'accord de la commune ou de l'établissement public de coopération intercommunale compétent en matière de plan local d'urbanisme. En l'absence d'un tel document et à défaut d'accord des communes ou des établissements publics de coopération intercommunale concernés et compétents en matière de plan local d'urbanisme, le département ne peut créer ces zones qu'avec l'accord de l'autorité administrative compétente de l'État.",
    ),
    "Réécriture à droit constant : la faculté du département et les accords nécessaires sont exprimés directement. La condition tenant à l'absence de plan approuvé reste distincte de celle tenant à l'absence d'accord local. Aucune réforme de fond.",
    "Deux alinéas conservés. L'absence de document et le défaut d'accord restent cumulés pour le recours à l'accord de l'État ; la rédaction ne généralise pas ce mécanisme aux communes dotées d'un PLU approuvé. La finalité de L. 113-8 et les protections des espaces naturels sensibles sont maintenues, sans application à ce régime distinct des mesures de densification de policy.json.",
)

add(
    "L215-2",
    paragraphs(
        "Dans les limites de sa compétence territoriale, le Conservatoire de l'espace littoral et des rivages lacustres peut prendre l'initiative de créer des zones de préemption hors des zones délimitées par le département en application de l'article L. 215-1, hors des zones urbaines ou à urbaniser délimitées par un plan local d'urbanisme et hors des secteurs où les constructions sont autorisées délimités par une carte communale.",
        "Le projet de périmètre est soumis pour avis au département et à la commune ou à l'établissement public de coopération intercommunale compétent.",
        "L'autorité administrative compétente de l'État délimite le périmètre. Si la commune ou l'établissement public de coopération intercommunale compétent émet un avis défavorable, seul un décret en Conseil d'État peut le délimiter.",
        "Par dérogation, l'autorité administrative compétente de l'État délimite les zones de préemption prévues au premier alinéa du présent article dans les espaces, sites et paysages définis à l'article L. 121-23 et identifiés par une directive territoriale d'aménagement mentionnée à l'article L. 172-1, par une directive territoriale d'aménagement et de développement durables mentionnée à l'article L. 102-4 du présent code ou par un schéma d'aménagement régional mentionné à l'article L. 4433-7 du code général des collectivités territoriales.",
        "Dans les périmètres ainsi délimités, le conservatoire exerce les compétences que le présent chapitre attribue au département.",
    ),
    "Réécriture à droit constant : les trois catégories de zones exclues sont rendues explicites par la répétition de « hors ». L'autorité de délimitation, la conséquence de l'avis défavorable et la dérogation relative aux espaces protégés demeurent dans leurs alinéas respectifs. Aucune réforme de fond.",
    "Cinq alinéas conservés. Compétence territoriale du conservatoire, avis du département et de la commune ou de l'EPCI, décret en Conseil d'État en cas d'avis local défavorable et dérogation du quatrième alinéa maintenus. Les espaces doivent rester à la fois définis à L. 121-23 et identifiés par l'un des trois documents cités. Aucun élargissement aux zones urbaines ou à urbaniser ni aux secteurs constructibles des cartes communales n'est introduit.",
)

add(
    "L215-3",
    paragraphs(
        "La délimitation des zones de préemption en application des articles L. 215-1 et L. 215-2 donne lieu à la consultation des organisations professionnelles agricoles et forestières.",
    ),
    "Réécriture à droit constant : la délimitation devient le sujet de la phrase et l'obligation de consultation reste exprimée. Aucune réforme de fond.",
    "Alinéa unique et deux renvois conservés. Les organisations agricoles comme forestières restent consultées ; leur consultation n'est transformée ni en simple faculté ni en accord conforme.",
)

add(
    "L215-4",
    paragraphs(
        "Le département est titulaire d'un droit de préemption dans les zones délimitées en application de l'article L. 215-1.",
    ),
    "Réécriture à droit constant : le département, titulaire du droit, est placé en tête de phrase ; la délimitation de son champ territorial reste inchangée. Aucune réforme de fond.",
    "Alinéa unique conservé. Le champ reste celui des zones de L. 215-1. Les compétences particulières du conservatoire dans les périmètres de L. 215-2 ne sont pas attribuées au département par cette réécriture.",
)


sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert {a["number"] for a in sources} == set(drafts)
answer = []
for source in sources:
    item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    item.update(drafts[source["number"]])
    answer.append(item)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
