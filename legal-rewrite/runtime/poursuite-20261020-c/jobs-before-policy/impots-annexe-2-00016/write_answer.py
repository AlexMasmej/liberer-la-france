import json
from pathlib import Path


def paragraphs(*items):
    return "\n".join(f"<p>{item}</p>" for item in items)


def broken_paragraph(*items):
    return "<p>" + "<br /><br />".join(items) + "</p>"


drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml, reason, notes)


add(
    "253",
    broken_paragraph(
        "I. - Pour l'application du 3° du I de l'article 252 de la présente annexe et des III et IV de l'article 293 B ter du code général des impôts, les règles suivantes s'appliquent :",
        "1° Les montants à retenir sont ceux énumérés au B du I de l'article 293 D du code général des impôts ;",
        "2° L'assujetti exprime les montants en euros. Lorsqu'il a effectué des livraisons de biens ou des prestations de services dans une autre monnaie, il convertit ces montants en euros au taux de change en vigueur au premier jour de l'année civile. Il utilise le taux publié par la Banque centrale européenne pour ce jour ou, si aucun taux n'a été publié ce jour-là, celui du jour de publication suivant ;",
        "3° Lorsque l'Etat membre de l'Union européenne qui octroie la franchise applique des seuils différenciés en vertu du deuxième alinéa du paragraphe 1 de l'article 284 de la directive 2006/112/CE du Conseil du 28 novembre 2006 relative au système commun de la taxe sur la valeur ajoutée, l'assujetti déclare séparément, pour cet Etat membre et pour chaque seuil susceptible de s'appliquer, le montant total des livraisons de biens et des prestations de services correspondant à ce seuil.",
        "II. - L'assujetti communique par voie électronique les informations mentionnées à l'article 293 B ter du code général des impôts.",
    ),
    "Réécriture à droit constant : l'assujetti devient le sujet explicite des obligations d'expression, de conversion et de transmission des montants. La règle du taux de change et la déclaration distincte pour chaque seuil sont formulées en phrases plus directes. Aucune réforme de fond du projet ne vise ce dispositif de franchise de TVA.",
    "Maintien des I, II et 1° à 3°, des renvois à 252, 293 B ter, 293 D et à la directive, ainsi que du recours au jour de publication suivant, et non précédent. La note source fixe l'entrée en vigueur au 1er janvier 2025 par l'article 2 du décret n° 2024-1195 du 21 décembre 2024 ; elle ne fixe aucune date de réforme future. Le corpus de l'article 293 B ter annonce une reprise réglementaire liée aux articles L. 223-7, 1°, et L. 223-24 du code des impositions sur les biens et services, avec maintien transitoire : contrôler cette coordination lors de la reprise, sans anticiper ici un nouveau renvoi.",
)

add(
    "254",
    broken_paragraph(
        "L'assujetti non établi en France qui bénéficie de la franchise en base en application de l'article 293 B bis du code général des impôts est soumis aux obligations ci-après en cas de communication tardive à l'Etat membre d'établissement des informations prévues au paragraphe 1 de l'article 284 ter de la directive 2006/112/CE du Conseil du 28 novembre 2006 relative au système commun de la taxe sur la valeur ajoutée. Ces obligations s'appliquent si la communication intervient soit plus de trente jours après l'expiration du délai d'un mois suivant la fin du trimestre civil, soit après l'expiration de ce délai pour deux trimestres consécutifs :",
        "a) Il dépose une déclaration d'existence et fournit tous les renseignements relatifs à son activité professionnelle, conformément aux 1° et 2° du I de l'article 286 du code général des impôts ;",
        "b) Il est identifié par un numéro individuel, conformément au 7° de l'article 286 ter du code général des impôts ;",
        "c) Il dépose des déclarations de recettes, conformément au c du 6 de l'article 287 du code général des impôts.",
    ),
    "Réécriture à droit constant : les deux hypothèses alternatives de retard sont distinguées et les obligations des a à c ont chacune un sujet explicite. Le délai d'un mois, le retard de plus de trente jours et la répétition sur deux trimestres consécutifs sont conservés. Aucune réforme de fond n'est appliquée à la franchise de TVA.",
    "Les obligations des a à c restent cumulatives dès que l'une des deux hypothèses de retard est remplie ; le retard de plus de trente jours n'est pas exigé dans la seconde hypothèse. Renvois à 293 B bis, 286, 286 ter et 287 conservés. Entrée en vigueur historique au 1er janvier 2025 selon la note du décret n° 2024-1195 du 21 décembre 2024. Les notes des articles 293 B bis, 286 ter et 287 du corpus signalent une recodification au 1er janvier 2027 et des maintiens transitoires jusqu'à reprise réglementaire : contrôler ensemble les futurs textes de franchise, d'identification et de déclaration, sans substituer un renvoi supposé.",
)

add(
    "260 A",
    paragraphs(
        "Les exploitants agricoles sont soumis à la taxe sur la valeur ajoutée, dans les conditions prévues aux articles 298 bis, 1693 bis et 1785 du code général des impôts, pour les opérations suivantes :",
        "a. Les ventes de produits agricoles réalisées dans l'une des conditions suivantes :",
        "Sur les marchés, à place fixe, avec l'aide d'un personnel exclusivement affecté à ces ventes ;",
        "Dans un magasin ou une installation ayant fait l'objet d'un agencement spécial pour la vente ;",
        "A l'aide de moyens publicitaires relevant des usages commerciaux ou avec le concours de représentants ou de placiers, lorsque les produits sont vendus sous un conditionnement et présentés sous une marque ;",
        "b. Les ventes de produits agricoles transformés, préparés ou conservés, lorsque l'exploitant utilise, pour leur transformation, leur préparation ou leur mise en conserve, des installations, des agencements ou des matériels importants de la nature de ceux utilisés par les industriels ou les commerçants pour des opérations semblables.",
    ),
    "Réécriture à droit constant : le texte désigne les exploitants comme redevables et présente les trois modalités alternatives de vente du a avant la condition propre aux produits transformés du b. Les critères de personnel exclusif, d'aménagement commercial, de conditionnement et de marque, ainsi que l'importance des équipements, sont conservés. Aucune réforme de fond ne vise ce régime agricole.",
    "Les a et b et leurs alinéas restent dans le même ordre. La condition de conditionnement et de marque du dernier alinéa du a est maintenue dans son emplacement et n'est pas étendue aux ventes sur marché ou en magasin. Renvois à 298 bis, 1693 bis et 1785 conservés. Le corpus annonce pour 298 bis et 1693 bis une recodification au 1er janvier 2027 avec maintiens transitoires : coordonner ces renvois lors de leur reprise. Aucun changement des sanctions ou de l'exception prévue par 1785 n'est opéré ici.",
)

add(
    "260 B",
    paragraphs(
        "Les opérations de vente mentionnées à l'article 260 A sont traitées, dans leur ensemble, comme une entreprise distincte de l'activité agricole non assujettie à la taxe sur la valeur ajoutée.",
    ),
    "Réécriture à droit constant : la règle de traitement global des ventes en entreprise distincte est exprimée directement, en conservant la distinction avec l'activité agricole non assujettie. Aucune réforme de fond n'est introduite.",
    "Le renvoi à l'article 260 A et le regroupement de toutes les ventes qu'il vise sont conservés. La disposition ne rend pas assujettie, par elle-même, l'activité agricole distincte.",
)

add(
    "260 D",
    paragraphs(
        "Les exploitants agricoles peuvent exercer l'option pour l'imposition selon le régime simplifié prévue à l'article 298 bis du code général des impôts, qu'ils soient propriétaires, fermiers ou métayers.",
        "En cas de métayage, si le propriétaire et le métayer n'exercent pas conjointement l'option, chacun peut l'exercer séparément pour la part de la récolte qui lui revient. Les droits à déduction de celui qui a exercé l'option sont alors calculés selon les règles applicables aux personnes dont les opérations n'ouvrent pas toutes droit à déduction. La totalité des recettes de la métairie figure au second terme du rapport défini au 1° du 3 du III de l'article 206.",
    ),
    "Réécriture à droit constant : les bénéficiaires de l'option sont placés en tête et l'option séparée en métayage est expliquée en distinguant la part de récolte, le calcul des droits à déduction et le dénominateur du rapport. Aucune réforme de fond ne modifie ce régime.",
    "Maintien des deux alinéas et des renvois à 298 bis du CGI et au 1° du 3 du III de l'article 206 de l'annexe. Le second terme est confirmé comme dénominateur par l'article 206 du corpus ; il comprend toujours la totalité des recettes de la métairie, et non la seule part de l'optant. Coordonner le renvoi à 298 bis lors de sa reprise réglementaire annoncée dans le corpus.",
)

add(
    "260 E",
    paragraphs(
        "L'exploitant agricole qui exerce l'option l'applique à toutes les opérations qu'il réalise.",
    ),
    "Réécriture à droit constant : l'exploitant est explicitement désigné comme responsable de l'application de l'option à la totalité de ses opérations. La portée générale de l'option est conservée ; aucune réforme de fond n'est introduite.",
    "Article à lire avec les articles 260 D, 260 G et 260 I relatifs à l'option agricole. Aucun choix opération par opération ni exception supplémentaire n'est créé.",
)

add(
    "260 G",
    paragraphs(
        "L'exercice de l'option soumet l'exploitant à la taxe sur la valeur ajoutée selon le régime simplifié pour trois ans. L'option est ensuite renouvelable par tacite reconduction pour des périodes de cinq ans.",
        "Si l'échéance de l'option ne correspond pas au dernier jour de la période annuelle d'imposition choisie par le redevable, l'option est prolongée jusqu'au dernier jour de cette période.",
    ),
    "Réécriture à droit constant : les durées initiale et de reconduction sont séparées en deux phrases, puis le terme de la prorogation est désigné expressément. La période de trois ans, les reconductions de cinq ans et l'alignement sur la période annuelle demeurent inchangés. Aucune réforme de fond n'est introduite.",
    "Maintien des deux alinéas. Contrôler conjointement les effets de l'échéance sur la renonciation prévue à 260 I et sur l'option comptable de 260 J ; aucune nouvelle date calendaire n'est fixée.",
)

add(
    "260 I",
    paragraphs(
        "L'exploitant agricole exerce l'option en accomplissant pour la première fois les obligations de déclaration et de liquidation qui en résultent.",
        "L'option produit effet au 1er janvier de la première année de la période qu'elle couvre. Si l'exploitation agricole commence après le 1er janvier, l'option produit effet à la date de début de l'exploitation. Pour le décompte des périodes prévues à l'article 260 G, elle est toutefois réputée exercée au 1er janvier.",
        "L'exploitant qui renonce à l'option adresse une lettre recommandée au service des impôts dont dépend l'exploitation, au moins deux mois avant l'expiration de la période fixée à l'article 260 G.",
    ),
    "Réécriture à droit constant : l'exercice de l'option est rattaché aux premières obligations déclaratives et liquidatives ; sa date d'effet réelle est distinguée de la date retenue pour décompter les périodes. L'auteur, le destinataire et le délai de la renonciation sont explicites. Aucune réforme de fond n'est introduite.",
    "Trois alinéas conservés. Maintien du 1er janvier, de l'effet au début d'exploitation lorsqu'il est postérieur et du délai minimal de deux mois avant l'échéance de 260 G. La source exige une lettre recommandée pour la renonciation, sans imposer ici un accusé de réception.",
)

add(
    "260 J",
    paragraphs(
        "L'exploitant agricole qui exerce l'option pour l'imposition selon l'exercice comptable prévue au I de l'article 298 bis du code général des impôts l'adresse, par lettre recommandée avec accusé de réception, au service des impôts dont dépend l'exploitation.",
        "L'option soumet l'exploitant à l'imposition selon l'exercice comptable pour cinq ans. Elle est ensuite renouvelable par tacite reconduction pour des périodes de cinq ans. Si son échéance ne correspond pas au dernier jour de la période annuelle d'imposition choisie par le redevable, elle est prolongée jusqu'au dernier jour de cette période.",
        "Toutefois, si l'exploitant agricole a opté pour l'imposition selon le régime simplifié, l'option pour l'imposition selon l'exercice comptable s'applique jusqu'à l'échéance fixée à l'article 260 G. Elle est ensuite renouvelable par tacite reconduction jusqu'à l'échéance suivante.",
        "Pour renoncer à l'option, l'exploitant adresse une lettre recommandée au service des impôts dont dépend l'exploitation, au moins deux mois avant l'expiration de l'option.",
    ),
    "Réécriture à droit constant : les formalités sont attribuées à l'exploitant ; les durées, la prorogation et l'articulation avec l'option de régime simplifié font l'objet de phrases distinctes dans leurs alinéas respectifs. Les formalités de renonciation sont explicitées sans les renforcer. Aucune réforme de fond n'est introduite.",
    "Quatre alinéas conservés ; deux durées de cinq ans, règle spéciale d'alignement sur 260 G et préavis minimal de deux mois maintenus. L'accusé de réception reste exigé pour l'exercice de l'option, mais n'est pas ajouté pour sa renonciation. Le renvoi au I de 298 bis est conservé ; coordonner sa reprise réglementaire annoncée dans le corpus, sans modifier les options déjà exercées.",
)

add(
    "260 K",
    paragraphs(
        "Le redevable calcule le rapport prévu au 1° du 3 du III de l'article 206 pour chaque période annuelle d'imposition. Lorsque la période d'imposition dure moins d'un an, les éléments de la période annuelle d'imposition précédente servent au calcul de ce rapport. Le redevable accomplit les obligations prévues au 2 du V de l'article 206 et au II de l'article 207 avant le cinquième jour du cinquième mois suivant la clôture de la période d'imposition.",
        "Le redevable peut exercer, par période d'imposition, les facultés prévues au 1 du V de l'article 206.",
    ),
    "Réécriture à droit constant : le calcul annuel, la période de référence en cas de période courte et l'échéance des obligations sont distingués ; le redevable devient le sujet explicite des obligations et facultés. Aucune réforme de fond n'est introduite.",
    "Deux alinéas conservés. Renvois au 1° du 3 du III, au 2 du V et au 1 du V de 206, ainsi qu'au II de 207, maintenus. L'échéance reste strictement avant le cinquième jour du cinquième mois. Les articles 206 et 207 comportent des échéances générales et des règles pour les assujettis uniques ; la règle spéciale du présent article est conservée sans les y substituer.",
)

add(
    "263",
    paragraphs(
        "Sous réserve des dispositions de l'article 264 (1), le remboursement forfaitaire est calculé sur les encaissements nets correspondant aux ventes ou aux livraisons qui y ouvrent droit.",
    ),
    "Réécriture à droit constant : la base du remboursement est exprimée directement comme les encaissements nets des seules opérations éligibles. Le renvoi historique est conservé et son anomalie est signalée séparément ; aucune réforme de fond n'est introduite.",
    "Incohérence préexistante : la note source (1) déclare sans objet les mots « Sous réserve des dispositions de l'article 264 » et mentionne l'article 1er (L) du décret n° 2010-1075 du 10 septembre 2010. L'article 264 est absent du corpus fourni. La réserve et son appel de note sont conservés pour ne pas supprimer silencieusement un renvoi ; leur suppression formelle appelle une coordination explicite. La date historique de la note n'est pas une date de réforme future.",
)

add(
    "265",
    paragraphs(
        "L'entreprise redevable de la taxe sur la valeur ajoutée au titre de la revente des produits achetés doit, pour tout paiement d'un achat auprès d'un agriculteur non redevable de cette taxe, délivrer un bulletin d'achat ou un bon de livraison. Ce document indique la date, la nature et la valeur de l'achat. L'administration fixe la structure du bulletin d'achat ou du bon de livraison.",
        "Lorsque le paiement est effectué par acomptes, l'acheteur délivre un bulletin d'achat ou un bon de livraison à chaque versement d'acompte et lors du versement du solde.",
    ),
    "Réécriture à droit constant : l'acheteur est désigné comme débiteur de l'obligation documentaire et les mentions obligatoires sont séparées de la règle fixant la structure du document. La délivrance à chaque acompte et au solde est rendue explicite. Aucune réforme de fond n'est introduite.",
    "Maintien des deux alinéas, du choix entre bulletin d'achat et bon de livraison et des trois mentions : date, nature et valeur de l'achat. Le champ reste limité à l'acheteur redevable de TVA au titre de la revente et au fournisseur agriculteur non redevable. L'orientation générale de réemploi des données ne permet pas de supprimer ici les documents que l'acheteur remet au fournisseur sans dispositif coordonné.",
)

add(
    "266",
    paragraphs(
        "I. - L'exploitant agricole qui demande le remboursement forfaitaire établit une déclaration annuelle des encaissements définis à l'article 263 et perçus au cours de l'année écoulée.",
        "La déclaration distingue les livraisons en France, les livraisons donnant lieu à une expédition ou à un transport dans un autre Etat membre de la Communauté européenne à destination d'assujettis ou de personnes morales non assujetties réalisant des acquisitions intracommunautaires imposables dans cet Etat, et les exportations.",
        "Selon le cas, l'exploitant joint en outre à la déclaration les pièces suivantes :",
        "Les attestations de ses clients indiquant les versements effectués pendant l'année considérée (1). Ces attestations respectent les modèles indiqués par l'administration ;",
        "La copie des déclarations en douane ;",
        "Les doubles des factures relatives aux livraisons de produits agricoles expédiés ou transportés dans un autre Etat membre de la Communauté.",
        "II. - L'exploitant établit la déclaration prévue au I sur les imprimés de l'administration. Il l'adresse au service des impôts dont il relève pour l'application du I et des articles 263 et 265.",
        "(1) Voir toutefois l'article 98 bis de l'annexe III.",
    ),
    "Réécriture à droit constant : la demande annuelle, les catégories de livraisons à distinguer, les justificatifs selon les cas et le dépôt au service compétent sont formulés avec l'exploitant comme sujet. L'exception signalée par l'article 98 bis de l'annexe III est conservée. Aucune réforme de fond n'est introduite.",
    "Maintien des I et II, des alinéas et du renvoi (1) à l'article 98 bis de l'annexe III. Ce dernier confirme le mandat particulier pour les ventes de fruits et légumes ; la réécriture ne généralise pas cette dérogation. Les trois catégories de livraisons et les trois catégories de pièces restent distinctes, sans transformer « selon le cas » en cumul obligatoire. La terminologie historique « Communauté européenne » est conservée. La note source vise l'article 1er (L) du décret n° 2010-1075 du 10 septembre 2010. Le renvoi à 263 demeure soumis à l'anomalie signalée pour cet article ; aucune suppression de justificatifs n'est déduite de la seule orientation de réemploi des données.",
)

add(
    "267 bis",
    paragraphs(
        "1. à 4. (Abrogés)",
        "5. Les ventes ou les livraisons d'animaux ayant été importés n'ouvrent pas droit au remboursement forfaitaire.",
        "6. (Abrogé)",
        "7. Lorsque le prix de cession d'animaux vivants de boucherie et de charcuterie dépasse leur valeur normale en poids de viande, le ministre de l'économie et des finances fixe chaque année, forfaitairement, la base de calcul du remboursement en se référant au prix de vente sur les marchés d'abattage. Le prix porté sur le bulletin d'achat et sur l'attestation est alors réduit à due concurrence.",
        "8. (Abrogé).",
    ),
    "Réécriture à droit constant : l'exclusion des animaux importés est exprimée comme une absence de droit au remboursement ; le ministre compétent devient le sujet de la fixation annuelle de l'assiette forfaitaire. La réduction corrélative des prix figurant sur les deux documents est conservée. Aucune réforme de fond n'est introduite.",
    "Conservation des positions 1 à 8, y compris les subdivisions abrogées, sans renumérotation. Le caractère annuel et forfaitaire, la référence aux marchés d'abattage et la condition de dépassement de la valeur normale sont maintenus. Le II de l'article 298 quinquies du CGI cite le 7 du présent article ; ses notes annoncent une abrogation au 1er septembre 2026, sous réserve de deux alinéas maintenus jusqu'à reprise réglementaire. Contrôler la base légale et la coordination de ce mécanisme dans ce contexte, sans substituer ici un renvoi nouveau ni écarter les situations historiques.",
)

add(
    "267 ter",
    paragraphs(
        "1. Le contrôle des animaux prévu au II de l'article 298 quinquies du code général des impôts peut être effectué par identification ou par marquage.",
        "Pour l'application du présent article, ces deux procédés sont définis comme suit :",
        "L'identification permet de déterminer à tout moment l'identité propre de l'animal ;",
        "Le marquage consiste à apposer sur l'animal une marque désignant son propriétaire ou la personne qui en a la garde.",
        "2. Pour les animaux relevant de la loi n° 66-1005 du 28 décembre 1966 sur l'élevage, l'identification prévue au présent article est celle réalisée en application de cette loi.",
        "3. Pour les équidés, les systèmes d'identification suivants sont admis :",
        "L'identification par les livres généalogiques ou zootechniques ;",
        "L'identification effectuée sous l'égide du ministre de l'agriculture pour le contrôle sanitaire des animaux. Dans ce cas, le certificat sanitaire porte le nom et l'adresse du propriétaire de l'animal ;",
        "L'identification effectuée sous l'égide du ministre de l'économie et des finances pour les animaux des zones franches ;",
        "L'identification effectuée, avec l'accord du service des impôts, sous le contrôle de groupements de producteurs constitués pour réaliser les objectifs définis par la loi d'orientation agricole n° 60-808 du 5 août 1960.",
        "4. A titre transitoire, par dérogation aux 2 et 3, l'identification ou, le cas échéant, le marquage peut être effectué pour tous les animaux :",
        "a. Soit selon l'un des systèmes prévus au 3 ;",
        "b. Soit par le propriétaire de l'animal ou par la personne qui en a la garde, dans les conditions prévues au 5.",
        "5. a. La personne tenue de faire marquer ses animaux qui souhaite bénéficier du b du 4 en fait la demande au service des impôts. Ce service lui attribue un indicatif personnel de marque comprenant notamment le numéro de code INSEE de son département.",
        "Le service des impôts fixe les conditions dans lesquelles cet indicatif est, le cas échéant, complété par un numéro individuel pour chaque animal.",
        "b. L'identification ou le marquage est effectué par tatouage ou par des procédés que le service des impôts agrée après avis des organisations professionnelles intéressées.",
        "c. L'identification ou le marquage doit être effectué :",
        "Dans les trente jours à compter de la naissance, pour les animaux nés sur l'exploitation ;",
        "Dès l'achat ou la prise en garde, pour les autres animaux.",
        "Dans tous les cas, l'opération doit précéder toute commercialisation. Toutefois, le service des impôts peut en différer la réalisation pour les catégories d'animaux qu'il désigne.",
    ),
    "Réécriture à droit constant : les définitions, les systèmes admis et la procédure de marque personnelle sont présentés avec des acteurs et des actions explicites. Les phrases longues relatives au certificat sanitaire, à l'indicatif et à la commercialisation sont scindées dans leurs alinéas. Les régimes historiques et transitoires sont conservés ; aucune réforme de fond n'est introduite.",
    "Maintien des 1 à 5, des a et b du 4 et des a à c du 5, ainsi que de chaque alinéa dans son ordre. Conservation des lois n° 66-1005 du 28 décembre 1966 et n° 60-808 du 5 août 1960, des quatre systèmes pour les équidés, de l'accord fiscal et de l'avis professionnel, du code départemental INSEE, des trente jours et du pouvoir de report avant commercialisation. Le régime transitoire du 4 n'a pas de terme explicite dans la source : aucun n'est inventé. Point de coordination préexistant : les notes du CGI 298 quinquies annoncent son abrogation au 1er septembre 2026, sauf les deux derniers alinéas du II maintenus jusqu'à reprise réglementaire ; vérifier le maintien de la base du contrôle ici visée au II. Aucune référence de remplacement non établie n'est introduite.",
)

add(
    "267 quater",
    paragraphs(
        "I. - Les redevables de la taxe sur la valeur ajoutée qui réalisent des achats, des importations, des acquisitions intracommunautaires, des ventes, des opérations de commission ou de courtage portant sur des animaux vivants de boucherie et de charcuterie sont tenus aux obligations suivantes :",
        "a. Ils ne peuvent avoir la propriété ou la garde que d'animaux identifiés ou marqués selon les modalités fixées à l'article 267 ter ;",
        "b. Ils tiennent une comptabilité matières qui retrace chaque jour les mouvements de ces animaux. L'administration en fixe les caractéristiques ;",
        "c. Ils font figurer sur les factures de vente la dénomination précise de l'animal, comprenant notamment son numéro d'identification ou sa marque ;",
        "d. (Abrogé).",
        "II. - Lorsqu'une personne mentionnée au I vend des animaux à un acheteur non assujetti à la taxe sur la valeur ajoutée au titre d'activités portant sur ces animaux, elle mentionne expressément cette qualité de l'acheteur sur la facture.",
    ),
    "Réécriture à droit constant : les redevables sont explicitement sujets de chacune des obligations d'identification, de comptabilité matières et de facturation. La qualité particulière de l'acheteur doit toujours figurer expressément sur la facture dans le cas prévu au II. Aucune réforme de fond n'est introduite.",
    "Conservation des I, II et a à d, y compris le d abrogé, des six catégories d'opérations, de la propriété comme de la garde et du suivi quotidien. Le II vise l'absence d'assujettissement au titre des activités portant sur ces animaux, sans l'étendre à toute personne dispensée de payer la taxe. Renvoi à 267 ter maintenu ; sa base de contrôle liée au II de 298 quinquies appelle la coordination signalée dans la note de cet article.",
)

add(
    "267 quater F",
    paragraphs(
        "I. - Le poids des produits auquel se réfère le II de l'article 302 bis WA du code général des impôts est leur poids net, exprimé en kilogrammes.",
        "II. - Le 3 du V de l'article 302 bis WA du code général des impôts vise les espèces suivantes :",
        "a. Les harengs de l'espèce Clupea harengus ;",
        "b. Les sardines de l'espèce Sardina pilchardus ;",
        "c. Les maquereaux de l'espèce Scomber scombrus ;",
        "d. Les maquereaux de l'espèce Scomber japonicus ;",
        "e. Les chinchards de l'espèce Trachurus spp ;",
        "f. Les anchois de l'espèce Engraulis spp ;",
        "g. Les picarels de l'espèce Maena smaris ;",
        "h. Les sprats de l'espèce Sprattus sprattus.",
        "Pour l'application de ces dispositions, un lot est la quantité de poissons d'une ou de plusieurs des espèces énumérées ci-dessus qui est déchargée d'un même navire et achetée ou réceptionnée par une même personne.",
        "III. - Les redevables déclarent et acquittent la redevance sanitaire de première mise sur le marché des produits de la pêche ou de l'aquaculture lors du dépôt des déclarations suivantes :",
        "1° Chaque déclaration mensuelle de taxe sur la valeur ajoutée, pour les redevables qui acquittent cette taxe selon le premier alinéa du 2 de l'article 287 du code général des impôts ;",
        "2° Chaque déclaration trimestrielle de taxe sur la valeur ajoutée, pour les redevables qui acquittent cette taxe selon le dernier alinéa du 2 du même article 287 ;",
        "3° La déclaration mentionnée au 3 du même article 287, pour les redevables qui relèvent du régime simplifié d'imposition prévu à l'article 302 septies A du même code.",
        "IV. - La redevance n'est pas remboursée en cas de saisie par les services d'inspection sanitaire, d'exportation ou d'expédition vers les Etats membres de l'Union européenne.",
        "V. - La perception de la redevance de première mise sur le marché n'exclut pas celle de la redevance sanitaire de transformation prévue à l'article 302 bis WB du code général des impôts lorsque les produits font ensuite l'objet d'opérations de préparation ou de transformation.",
    ),
    "Réécriture à droit constant : les définitions du poids et du lot sont directes ; les obligations de déclaration et de paiement sont reliées clairement à chaque périodicité de TVA. Le non-remboursement et le cumul possible des deux redevances sont formulés en phrases plus courtes. Aucune réforme de fond ni modification de tarif n'est introduite.",
    "Maintien des I à V, des huit espèces a à h avec leurs dénominations scientifiques, des trois échéances 1° à 3° et du poids net en kilogrammes. La notion de lot exige à la fois un même navire et une même personne acheteuse ou réceptionnaire ; elle peut réunir plusieurs espèces. Les III et IV restent à leur emplacement, car 267 quater G y renvoie. La note du décret n° 2014-1686 du 29 décembre 2014, article 2, vise les déclarations portant sur une période d'imposition postérieure au 1er janvier 2015 ; ce critère n'est pas remplacé par la seule date de dépôt. Les renvois à 287 et 302 septies A sont maintenus : 302 septies A renvoie désormais à L. 162-1 du code des impositions sur les biens et services et les notes de 287 annoncent sa reprise réglementaire ; contrôler la coordination sans appliquer ici un régime déclaratif nouveau.",
)

add(
    "267 quater G",
    paragraphs(
        "I. - Pour l'application du I de l'article 302 bis WB du code général des impôts, les opérations de préparation consistent à modifier l'intégrité anatomique, par exemple par l'éviscération, l'étêtage, le filetage ou le hachage. Les opérations de transformation consistent à appliquer un procédé physique ou chimique, tel que le chauffage, le salage, la dessiccation ou le marinage.",
        "II. - Le poids des produits auquel se réfère le II de l'article 302 bis WB du code général des impôts est leur poids net, exprimé en kilogrammes.",
        "III. - La redevance sanitaire de transformation des produits de la pêche ou de l'aquaculture est soumise aux dispositions des III et IV de l'article 267 quater F.",
    ),
    "Réécriture à droit constant : les deux catégories d'opérations sont définies par leur effet ou leur procédé, avec l'ensemble des exemples de la source. La définition du poids et l'application par renvoi des règles déclaratives et de non-remboursement sont formulées directement. Aucune réforme de fond n'est introduite.",
    "Maintien des I à III, des quatre exemples de préparation et des quatre exemples de transformation, qui demeurent illustratifs. Le poids reste net et exprimé en kilogrammes. Renvoi limité aux III et IV de 267 quater F, à l'exclusion de ses autres subdivisions. L'application temporelle de ces règles doit rester cohérente avec la note historique du décret n° 2014-1686 du 29 décembre 2014 figurant à 267 quater F.",
)

add(
    "267 quater H",
    paragraphs(
        "I. - Les redevables déclarent et acquittent la redevance sanitaire pour le contrôle de certaines substances et de leurs résidus prévue à l'article 302 bis WC du code général des impôts lors du dépôt des déclarations suivantes :",
        "1° Chaque déclaration mensuelle de taxe sur la valeur ajoutée, pour les redevables qui acquittent cette taxe selon le premier alinéa du 2 de l'article 287 du code général des impôts ;",
        "2° Chaque déclaration trimestrielle de taxe sur la valeur ajoutée, pour les redevables qui acquittent cette taxe selon le dernier alinéa du 2 du même article 287 ;",
        "3° La déclaration mentionnée au 3 du même article 287, pour les redevables qui relèvent du régime simplifié d'imposition prévu à l'article 302 septies A du même code.",
        "II. - (sans objet)",
        "III. - (sans objet)",
        "IV. - La redevance n'est pas remboursée en cas de saisie par les services d'inspection sanitaire, d'exportation ou d'expédition vers les Etats membres de l'Union européenne.",
    ),
    "Réécriture à droit constant : l'obligation de déclarer et de payer est reliée au dépôt de chacune des déclarations concernées ; les événements exclus du remboursement sont énoncés directement. Aucune réforme de fond ni modification de la redevance n'est introduite.",
    "Conservation des I à IV, y compris les II et III sans objet, et des 1° à 3° du I. Les rythmes mensuel, trimestriel et du régime simplifié, ainsi que tous les cas de non-remboursement, sont maintenus. La note de l'article 2 du décret n° 2014-1686 du 29 décembre 2014 concerne les périodes d'imposition postérieures au 1er janvier 2015. Renvois à 302 bis WC, 287 et 302 septies A conservés ; contrôler la coordination avec L. 162-1 du code des impositions sur les biens et services et la reprise réglementaire de 287 annoncée par ses notes, sans préjuger d'une nouvelle périodicité.",
)

add(
    "267 quinquies",
    paragraphs(
        "I. - Les redevables de la taxe sur la valeur ajoutée dont le chiffre d'affaires ne dépasse pas les limites fixées au I de l'article 302 septies A du code général des impôts relèvent, pour les taxes sur le chiffre d'affaires, du régime simplifié dans les conditions définies ci-après (1).",
        "Ces redevables peuvent toutefois choisir, sur option, l'imposition d'après leur chiffre d'affaires réel.",
        "II. - (Dispositions abrogées).",
        "III. - 1. Le redevable notifie à l'administration l'option mentionnée au I avant le 1er février de la première année pour laquelle il souhaite être imposé d'après son chiffre d'affaires réel. L'option vaut pour cette année et pour l'année suivante ; elle est irrévocable pendant ces deux années.",
        "L'entreprise nouvelle qui choisit l'imposition d'après son chiffre d'affaires réel exerce l'option dans les trois mois suivant le début de son activité. L'option vaut jusqu'au 31 décembre de l'année suivante.",
        "2. L'option mentionnée au I est reconduite tacitement pour des périodes de deux ans, pendant lesquelles elle est irrévocable.",
        "Le redevable qui souhaite renoncer à l'option notifie sa renonciation à l'administration avant le 1er février de l'année suivant la période pour laquelle l'option a été exercée ou tacitement reconduite.",
        "(1) Il convient également de se reporter à l'article 204 quater de la présente annexe.",
    ),
    "Réécriture à droit constant : le rattachement au régime simplifié, le choix du réel, la durée de l'option et les formalités de renonciation sont exprimés avec le redevable comme sujet. Les règles propres aux entreprises nouvelles et l'irrévocabilité sont conservées. Aucune réforme de fond ni modification des seuils n'est introduite.",
    "Maintien des I à III, des 1 et 2 du III et de tous les alinéas, du 1er février, des trois mois, du 31 décembre de l'année suivante et des reconductions de deux ans. Deux points préexistants nécessitent une coordination explicite : le I de 302 septies A cité comme support des limites n'existe plus dans le texte de cet article fourni par le corpus, qui renvoie globalement à L. 162-1 du code des impositions sur les biens et services ; l'article 204 quater cité en note est absent du corpus fourni. Renvois conservés, sans suppression silencieuse ni nouvelle référence de seuil supposée.",
)

add(
    "267 septies",
    paragraphs(
        "Les entreprises relevant du régime simplifié d'imposition appliquent, pour toutes les règles qui ne sont pas propres à ce régime, les dispositions applicables aux entreprises imposées d'après leur chiffre d'affaires réel.",
    ),
    "Réécriture à droit constant : les entreprises deviennent le sujet de l'application des règles communes, tout en conservant la priorité des règles propres au régime simplifié. Aucune réforme de fond n'est introduite.",
    "La disposition reste limitée aux règles non spécifiques au régime simplifié et n'efface aucune de ses règles particulières. Aucun seuil, délai ou renvoi nouveau n'est ajouté.",
)

add(
    "267 septies A",
    paragraphs(
        "Les entreprises relevant de plein droit du régime simplifié de bénéfice réel défini à l'article 302 septies A bis du code général des impôts peuvent opter pour le régime de bénéfice réel. Elles notifient cette option à l'administration dans les délais de dépôt de la déclaration des résultats de la période précédant celle pour laquelle l'option s'applique.",
        "L'entreprise nouvellement créée qui choisit ce régime exerce l'option dans les délais de dépôt de la déclaration souscrite au titre de l'année de sa première période d'activité.",
        "L'option prévue au premier alinéa vaut pour un an. Elle est reconduite tacitement chaque année pour une nouvelle période d'un an.",
        "Le redevable peut renoncer à l'option en le notifiant à l'administration dans les délais de dépôt de la déclaration des résultats de la période précédant celle pour laquelle la renonciation s'applique.",
    ),
    "Réécriture à droit constant : les entreprises sont explicitement chargées de notifier l'option ; les délais sont exprimés par rapport à la période de résultats pertinente et la reconduction annuelle est isolée dans une phrase. Les règles de création et de renonciation sont maintenues. Aucune réforme de fond n'est introduite.",
    "Quatre alinéas conservés, notamment le premier auquel renvoie le troisième. Maintien de la durée d'un an, de la reconduction annuelle et des délais rattachés aux déclarations des résultats. La source désigne le régime de destination comme « régime de bénéfice réel », sans le qualifier de « normal » ; cette formulation est conservée, sans précision de fond ajoutée. Renvoi à 302 septies A bis maintenu.",
)

add(
    "267 nonies",
    paragraphs(
        "Pour les opérations fiscales, il n'est pas exigé de certificat de jaugeage des récipients destinés à produire ou à stocker des vins, des cidres, des bières ou d'autres produits fermentés soumis à l'accise sur les alcools mentionnée à l'article L. 313-15 du code des impositions sur les biens et services.",
    ),
    "Réécriture à droit constant : le champ des opérations fiscales est placé en tête et la destination des récipients est exprimée par des verbes. La dispense et toutes les catégories de produits restent identiques. Aucune réforme de fond n'est introduite.",
    "Renvoi à L. 313-15 du code des impositions sur les biens et services conservé. La dispense vise les opérations fiscales et les récipients destinés à la production ou au stockage des produits indiqués ; aucune dispense générale de contrôle n'est créée. La note source de l'article 4 du décret n° 2025-591 du 26 juin 2025 fixe l'entrée en vigueur au 1er juillet 2025, sans constituer une date de réforme future.",
)

add(
    "268",
    paragraphs(
        "La distillation de toute matière première importée est interdite, sauf celle des fruits frais autres que les pommes, les poires ou les raisins. Cette interdiction ne s'applique pas aux matières premières originaires et en provenance des Etats membres de la Communauté européenne, ni à celles qui sont originaires de pays tiers et mises en libre pratique dans l'un de ces Etats membres.",
    ),
    "Réécriture à droit constant : l'interdiction est formulée avec la distillation comme sujet et les deux exclusions fondées sur l'origine et la circulation des matières premières sont distinguées. L'exception des fruits frais conserve ses propres exclusions. Aucune réforme de fond n'est introduite.",
    "Conservation de l'unique alinéa, des pommes, poires et raisins exclus de l'exception des fruits frais, du cumul origine et provenance communautaires et de la mise en libre pratique requise pour les matières originaires de pays tiers. La dénomination historique « Communauté européenne » est maintenue ; aucune extension territoriale ni restriction nouvelle n'est déduite de sa reformulation.",
)

sources = json.loads(Path("source.json").read_text())
assert len(sources) == 24
assert set(drafts) == {r["number"] for r in sources}
answer = []
for source in sources:
    xml, reason, notes = drafts[source["number"]]
    answer.append({
        "code_id": source["code_id"],
        "source_id": source["source_id"],
        "source_sha256": source["source_sha256"],
        "number": source["number"],
        "proposed_xml": xml,
        "reason": reason,
        "review_notes": notes,
        "status": "rewrite_draft",
    })
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
print(f"answer.json : {len(answer)} articles")
