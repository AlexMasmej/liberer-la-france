import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}

def add(number, text, reason, review_notes):
    paragraphs = [p.strip() for p in text.strip().split('\n\n')]
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }

add('L161-43', '''
Le président du collège représente la Haute Autorité en justice et dans tous les actes de la vie civile. Il peut mandater le directeur pour assurer cette représentation.

Les articles L. 412-1, L. 421-1, L. 431-1 et L. 236-1 du code du travail s'appliquent au personnel des services de la Haute Autorité. Un décret en Conseil d'Etat peut toutefois adapter ces dispositions lorsque les conditions de travail propres à la Haute Autorité et les différentes catégories de personnel qu'elle emploie le rendent nécessaire.
''', "Réécriture à droit constant : le mandat de représentation et la faculté d'adaptation réglementaire sont formulés avec un sujet explicite. Aucune réforme de fond de policy.json ne vise cet article.", "Les quatre renvois au code du travail sont conservés tels qu'ils figurent dans la source ; leur concordance avec la numérotation actuelle de ce code appelle un contrôle. La compétence du décret en Conseil d'Etat et les motifs d'adaptation sont maintenus.")

add('L161-45', '''
Les ressources de la Haute Autorité de santé comprennent notamment :

1° Les subventions de l'Etat ;

2° Une dotation des régimes obligatoires d'assurance maladie. La loi en fixe chaque année le montant ; un décret en fixe les conditions de versement et de répartition. Cette dotation comporte deux parts : l'une est versée au titre de la procédure prévue aux articles L. 6113-3, L. 6113-4 et L. 6322-1 du code de la santé publique ; l'autre au titre de la contribution de l'assurance maladie au fonctionnement de la Haute Autorité de santé ;

3° Le produit des redevances pour services rendus. Le collège en détermine les montants sur proposition du directeur ;

4° Les produits divers, ainsi que les dons et legs.
''', "Réécriture à droit constant : les compétences respectives de la loi, du décret, du collège et du directeur sont explicitées, sans modifier les quatre catégories de ressources ni les deux parts de la dotation. Aucune réforme de fond n'est applicable à cet article.", "Liste non exhaustive, périodicité annuelle du montant légal et renvois aux trois articles du code de la santé publique conservés. Aucun financement ni montant nouveau n'est créé.")

add('L161-46', '''
Un décret en Conseil d'Etat fixe les modalités d'application du présent chapitre, notamment :

1° Les conditions dans lesquelles la Haute Autorité de santé réalise les évaluations et rend les avis mentionnés à l'article L. 161-37 ;

2° Les critères selon lesquels sont évalués les produits, actes ou prestations de santé ;

3° Les modalités de mutualisation d'un ou de plusieurs services d'appui et de soutien de la Haute Autorité de santé avec un ou plusieurs services d'autres organismes, en application de l'article L. 1411-5-3 du code de la santé publique.
''', "Réécriture à droit constant : la compétence réglementaire est placée en tête et les trois objets du décret sont exprimés directement. Aucune réforme de fond n'est introduite.", "Caractère non exhaustif de l'énumération, possibilité de mutualiser un ou plusieurs services de part et d'autre et renvois aux articles L. 161-37 et L. 1411-5-3 conservés. Les sauts de ligne purement typographiques sont normalisés.")

add('L162-1', '''
Les soins sont dispensés aux assurés sociaux dans les conditions définies par les articles qui suivent, sous réserve des dispositions applicables aux assurés bénéficiaires de l'aide sociale.
''', "Réécriture à droit constant : la règle de dispensation des soins précède la réserve relative à l'aide sociale, dont la portée est conservée. Aucune réforme de fond n'est introduite.", "La réserve applicable aux bénéficiaires de l'aide sociale est maintenue ; aucun régime de prise en charge nouveau n'est créé.")

add('L162-1-7', '''
I. - La prise en charge ou le remboursement par l'assurance maladie d'un acte ou d'une prestation exige son inscription sur une liste établie dans les conditions du présent article, à l'exception des prestations mentionnées à l'article L. 165-1. Cette exigence concerne les actes ou prestations réalisés par un professionnel de santé dans le cadre d'un exercice libéral, d'un exercice salarié auprès d'un autre professionnel de santé libéral, ou en centre de santé, en maison de santé, en maison de naissance, dans un établissement ou un service médico-social ou dans une société de téléconsultation définie à l'article L. 4081-1 du code de la santé publique. Elle concerne également, à compter du 1er janvier 2005, les actes ou prestations réalisés par un professionnel de santé dans le cadre d'un exercice salarié dans un établissement de santé. L'inscription peut être provisoire, dans des conditions fixées par décret, et faire l'objet d'une révision en respectant une durée de trois ans renouvelable une fois, dans la limite de dix-huit mois. Elle peut être subordonnée au respect d'indications thérapeutiques ou diagnostiques, à l'état du patient et à des conditions particulières de prescription, d'utilisation ou de réalisation de l'acte ou de la prestation. Pour les actes réalisés en série, les conditions de prescription peuvent fixer le nombre d'actes au-delà duquel un accord préalable du service du contrôle médical est nécessaire, en application de l'article L. 315-2, pour poursuivre exceptionnellement leur prise en charge. Cette poursuite de la prise en charge repose sur un référentiel élaboré par la Haute Autorité de santé ou validé par elle sur proposition de l'Union nationale des caisses d'assurance maladie.

II. - L'Union nationale des caisses d'assurance maladie ou les ministres chargés de la santé et de la sécurité sociale adressent la demande d'inscription de l'acte ou de la prestation à la Haute Autorité de santé pour avis. Celle-ci évalue le service attendu ou le service rendu par l'acte ou la prestation, ainsi que, le cas échéant, les actes existants dont l'évaluation pourrait en être modifiée. Son avis précise aussi, si nécessaire, les conditions liées aux indications thérapeutiques ou diagnostiques, à l'état du patient et aux modalités particulières de prescription, d'utilisation ou de réalisation de l'acte ou de la prestation. A la demande du collège, la commission spécialisée mentionnée à l'article L. 165-1 peut préparer cet avis. La Haute Autorité de santé le transmet à l'Union nationale des caisses d'assurance maladie dans les six mois suivant le dépôt de la demande.

Selon des modalités définies par voie réglementaire, les personnes et organismes suivants peuvent proposer à la Haute Autorité de santé de s'autosaisir de l'évaluation du service attendu ou du service rendu d'un acte ou d'une prestation :

1° Les conseils nationaux professionnels mentionnés à l'article L. 4021-3 du code de la santé publique ;

2° Les associations d'usagers agréées au titre de l'article L. 1114-1 du même code ;

3° L'exploitant, au sens du I de l'article L. 165-1-1-1 du présent code, d'un produit de santé mentionné aux articles L. 5211-1 ou L. 5221-1 du code de la santé publique, à condition que ce produit porte l'action thérapeutique ou diagnostique de l'acte à évaluer et soit à usage collectif.

III. - L'Union nationale des caisses d'assurance maladie saisit le Haut Conseil des nomenclatures institué au IV, chargé de décrire et de hiérarchiser les actes et les prestations. Elle lui transmet l'avis de la Haute Autorité de santé.

Le Haut Conseil des nomenclatures établit un rapport décrivant et hiérarchisant l'acte ou la prestation qui lui est soumis, en tenant compte des enjeux de pertinence médicale. Dans un délai de six mois, il remet ce rapport à l'Union nationale des caisses d'assurance maladie, après avis simple de la commission mentionnée au V compétente pour la profession de médecin.

IV. - Le Haut Conseil des nomenclatures est chargé :

1° De proposer à la commission mentionnée au V compétente pour la profession de médecin une méthodologie de description et de hiérarchisation des actes et prestations ;

2° D'étudier les actes et les prestations que lui soumet l'Union nationale des caisses d'assurance maladie, afin de les décrire et de les hiérarchiser selon la méthodologie mentionnée au 1°.

Le Haut Conseil des nomenclatures comprend un nombre égal de médecins libéraux et de praticiens hospitaliers, ainsi que des personnes qualifiées nommées dans des conditions fixées par décret. Un représentant de la Haute Autorité de santé, un représentant des patients et le président de la commission mentionnée au V compétente pour la profession de médecins assistent à ses travaux.

Chaque année, le Haut Conseil des nomenclatures remet un rapport d'activité, après avoir consulté l'ensemble des acteurs participant à la hiérarchisation. Ce rapport est rendu public.

L'Union nationale des caisses d'assurance maladie assure le secrétariat du Haut Conseil des nomenclatures.

V. - Des commissions assurent le suivi de l'activité de hiérarchisation pour chacune des professions dont les rapports avec les organismes d'assurance maladie sont régis par une convention mentionnée à l'article L. 162-14-1.

Chaque commission est présidée par une personnalité désignée d'un commun accord par ses membres. Elle comprend, à parité, des représentants des syndicats représentatifs des professionnels de santé et des représentants de l'Union nationale des caisses d'assurance maladie. Un représentant de l'Etat assiste à ses travaux.

Le Haut Conseil des nomenclatures tient la commission compétente pour la profession des médecins informée de ses travaux et lui adresse ses rapports. Cette commission valide la méthodologie de description et de hiérarchisation des actes et prestations proposée par le Haut Conseil. Elle rend aussi un avis sur les rapports du Haut Conseil relatifs à la description et à la hiérarchisation de l'acte ou de la prestation, dans un délai fixé par décret.

Pour les autres professions, les commissions fixent les règles de hiérarchisation des actes de leur profession.

VI. - Par dérogation au III, l'Union nationale des caisses d'assurance maladie inscrit les actes cliniques et les actes effectués par les biologistes-responsables et les biologistes coresponsables mentionnés aux articles L. 6213-7 et L. 6213-9 du code de la santé publique, après avis de la commission compétente pour leur profession.

VII. - L'Union nationale des caisses d'assurance maladie décide des conditions d'inscription, de l'inscription et de la radiation d'un acte ou d'une prestation, après avis de l'Union nationale des organismes d'assurance maladie complémentaire. Elle recueille aussi, le cas échéant, l'avis de la Haute Autorité de santé lorsque la décision porte sur l'évaluation du service attendu ou du service rendu par l'acte ou la prestation. Les décisions d'inscription de l'Union nationale des caisses d'assurance maladie sont réputées approuvées, sauf opposition motivée des ministres chargés de la santé et de la sécurité sociale.

VIII. - Chaque acte ou prestation inscrit est examiné en vue d'une nouvelle hiérarchisation, dans les conditions prévues aux alinéas précédents, au cours des cinq ans suivant l'entrée en vigueur de la décision de l'Union nationale des caisses d'assurance maladie.

VIII bis. - Par dérogation au VIII, la hiérarchisation peut être adaptée ou un acte, une prestation ou un groupe d'actes ou de prestations peut être radié à tout moment, si leurs conditions de production ou de réalisation ont évolué de manière significative.

Cette adaptation est engagée à la demande du directeur général de l'Union nationale des caisses d'assurance maladie, des ministres chargés de la santé et de la sécurité sociale ou des conseils nationaux professionnels et des commissions compétentes pour chaque profession. La procédure est définie par voie réglementaire.

VIII ter. - Avant le 31 décembre de chaque année, un avenant à la convention mentionnée à l'article L. 162-5 est négocié pour fixer les tarifs des actes et prestations qui ont fait l'objet d'une nouvelle hiérarchisation au cours de l'année.

IX. - Un décret en Conseil d'Etat précise les conditions d'application du présent article.

Si l'inscription ou la révision de l'inscription, sur la liste établie au présent article, d'un acte, d'une prestation, d'un ou de plusieurs groupes d'actes ou d'un ou de plusieurs groupes de prestations n'a pas été traduite dans la convention mentionnée à l'article L. 162-5 dans les six mois suivant la transmission à l'Union nationale des caisses d'assurance maladie de l'évaluation technique permettant leur hiérarchisation dans les conditions du présent article, leur prise en charge ou leur remboursement est défini par voie réglementaire, sur proposition du directeur général de cette Union.
''', "Réécriture à droit constant : les champs d'exercice, les autorités de saisine, les étapes d'évaluation et de hiérarchisation et les compétences de décision sont explicités. Les subdivisions I à IX, y compris VIII bis et VIII ter, et l'ordre des alinéas sont conservés. Les procédures dérogatoires et les délais sont intégralement repris ; aucune réforme de fond du programme ne vise ce dispositif.", "Ambiguïté préexistante maintenue au I : la source associe une durée de trois ans renouvelable une fois à une limite de dix-huit mois, sans préciser leur articulation. Une clarification législative est nécessaire avant adoption ; aucun choix n'est fait silencieusement. Les délais de six mois, cinq ans, la date historique du 1er janvier 2005 et l'échéance annuelle du 31 décembre sont conservés. La note source prévoit l'entrée en vigueur immédiate de la rédaction issue de la loi n° 2025-1403 du 30 décembre 2025 ; elle ne fixe aucune date de réforme future. Les renvois d'autres articles à cette structure, notamment L162-1-8, nécessitent une coordination signalée dans la fiche correspondante.")

add('L162-1-7-1', '''
Lorsque la prise en charge par l'assurance maladie d'un produit de santé et de ses prestations associées, d'un acte inscrit sur la liste prévue à l'article L. 162-1-7 ou d'un transport de patient est particulièrement coûteuse pour l'assurance maladie, ou en cas de risque de mésusage, elle peut être subordonnée à la présentation d'un document par le patient. Ce document est établi par le prescripteur. Il indique que le prescripteur a préalablement consulté le dossier médical partagé du patient ou que la prescription respecte les indications ouvrant droit au remboursement. Il ne contient aucune autre donnée médicale.

Pour établir le document mentionné au premier alinéa, le prescripteur communique des éléments permettant de vérifier s'il a préalablement consulté le dossier médical partagé du patient ou si sa prescription respecte le cadre des indications ouvrant droit au remboursement. Les conditions de cette communication sont précisées par voie réglementaire et permettent le recours à un téléservice spécifique. Ces renseignements sont transmis au service du contrôle médical.

Lorsque le document mentionné au premier alinéa est absent, ou indique que le prescripteur n'a pas préalablement consulté le dossier médical partagé du patient ou que la prescription ne respecte pas les indications ouvrant droit au remboursement, le professionnel chargé d'exécuter la prescription recueille l'accord du patient pour délivrer le produit ou réaliser les actes et prestations qui ne sont pas pris en charge par l'assurance maladie.

Après consultation des parties prenantes, dont les professionnels de santé et les associations de représentants d'usagers agréées mentionnées à l'article L. 1114-1 du code de la santé publique, les ministres chargés de la santé et de la sécurité sociale fixent par arrêté les produits, actes et prestations soumis au présent article. Ces arrêtés précisent les informations que le prescripteur doit renseigner en application du deuxième alinéa.
''', "Réécriture à droit constant : les motifs permettant d'exiger le document, son contenu médical limité, la transmission au contrôle médical et l'accord du patient sont exprimés en phrases distinctes. Les quatre alinéas et leurs renvois sont conservés ; aucune réforme de fond n'est introduite.", "Les alternatives relatives à la consultation préalable du dossier médical partagé et au respect des indications sont maintenues, y compris dans les cas de non-prise en charge. La note source fixe l'entrée en vigueur au 1er janvier 2026 en application du III de l'article 48 de la loi n° 2025-199 du 28 février 2025. Cette date historique est distincte de toute réforme future.")

add('L162-1-7-2', '''
Un acte ou une prestation réalisé par un salarié d'un établissement thermal ne peut être pris en charge ou remboursé par l'assurance maladie que s'il est inscrit sur une liste établie dans les conditions du présent article. Cette inscription peut être subordonnée au respect d'indications thérapeutiques ou diagnostiques, à l'état du patient et à des conditions particulières de prescription, d'utilisation ou de réalisation de l'acte ou de la prestation.

L'Union nationale des caisses d'assurance maladie décide des conditions d'inscription, de l'inscription et de la radiation d'un acte ou d'une prestation, après avis de la Haute Autorité de santé et de l'Union nationale des organismes d'assurance maladie complémentaire.

Les décisions de l'Union nationale des caisses d'assurance maladie sont réputées approuvées, sauf opposition motivée des ministres chargés de la santé et de la sécurité sociale. Pour des raisons de santé publique, le ministre chargé de la santé peut inscrire ou radier d'office un acte ou une prestation, par arrêté pris après avis de la Haute Autorité de santé. Les tarifs de ces actes et prestations sont publiés au Journal officiel.
''', "Réécriture à droit constant : la condition d'inscription est formulée directement et les autorités compétentes pour décider, s'opposer ou intervenir d'office sont identifiées. Les trois alinéas substantiels sont maintenus, sans réforme de fond.", "Le champ demeure limité aux actes et prestations des salariés d'établissements thermaux. Les deux avis, l'opposition ministérielle motivée, le motif de santé publique et la publication des tarifs sont conservés.")

add('L162-1-7-3', '''
Par dérogation à l'article L. 162-2 du présent code et à l'article L. 4113-5 du code de la santé publique, un établissement thermal qui emploie des médecins ayant choisi l'exercice salarié peut facturer la prise en charge de l'acte ou de la prestation réalisé en son sein. Cette facturation respecte les conditions prévues à l'article L. 162-1-7-2 du présent code et ne peut dépasser les tarifs fixés en application du même article L. 162-1-7-2.
''', "Réécriture à droit constant : l'établissement qui peut facturer est placé comme sujet et le plafond tarifaire fait l'objet d'une phrase distincte. La dérogation n'est pas étendue ; aucune réforme de fond n'est introduite.", "Les deux fondements dérogatoires et les conditions et tarifs de L. 162-1-7-2 sont conservés. L'attribut de présentation align de la source est supprimé conformément aux balises et attributs autorisés.")

add('L162-1-7-4', '''
Les actes ou prestations qu'une équipe de plusieurs professionnels de santé réalise dans une ou plusieurs des situations suivantes peuvent être inscrits de manière spécifique sur la liste mentionnée à l'article L. 162-1-7, à l'exception des prestations mentionnées à l'article L. 165-1 :

1° Dans le cadre d'un exercice libéral ou d'un exercice salarié auprès d'un professionnel de santé libéral ;

2° Dans un centre de santé ;

3° Dans le cadre d'un exercice salarié dans un établissement de santé.

L'Union nationale des caisses d'assurance maladie décide des conditions d'inscription spécifique de ces actes ou prestations, de leur inscription et de leur radiation, après avis de la Haute Autorité de santé et de l'Union nationale des organismes d'assurance maladie complémentaire.

Les décisions de l'Union nationale des caisses d'assurance maladie sont réputées approuvées, sauf opposition motivée des ministres chargés de la santé et de la sécurité sociale.

L'avis de la Haute Autorité de santé mentionné au cinquième alinéa n'est pas nécessaire si les actes ou prestations réalisés en équipe ont fait l'objet d'une proposition du comité national des coopérations interprofessionnelles prévue au deuxième alinéa du I de l'article L. 4011-3 du code de la santé publique.
''', "Réécriture à droit constant : la faculté d'inscription spécifique, les trois cadres d'exercice et la dispense d'avis sont formulés directement. L'exception de L. 165-1 et les sept alinéas sont maintenus ; aucune réforme de fond n'est appliquée.", "Le renvoi au cinquième alinéa reste dirigé vers l'alinéa qui impose les avis. La dispense porte seulement sur l'avis de la Haute Autorité de santé ; elle ne supprime ni l'autre avis ni la possibilité d'opposition ministérielle.")

add('L162-1-7-5', '''
Chaque année, le ministre chargé de la santé établit une liste de mesures prioritaires pour améliorer la pertinence des soins dispensés aux assurés. Il transmet ce document aux commissions compétentes de l'Assemblée nationale et du Sénat au plus tard le 15 septembre. Le document fixe des objectifs chiffrés, accompagnés d'indicateurs, pour améliorer la pertinence des soins et mettre fin au remboursement d'actes et de prestations réalisés en dehors des indications scientifiques ou des recommandations de bonne pratique de la Haute Autorité de santé. Il présente aussi le bilan des mesures d'amélioration de la pertinence des soins prises ou poursuivies l'année précédente.
''', "Réécriture à droit constant : la responsabilité du ministre, la transmission annuelle et le contenu obligatoire du document sont exprimés par des verbes directs. Aucune réforme de fond ni objectif chiffré nouveau n'est ajouté.", "Echéance du 15 septembre, destinataires parlementaires, objectifs assortis d'indicateurs et bilan de l'année précédente conservés. L'attribut de présentation align est retiré.")

add('L162-1-8', '''
Si la commission prévue au V de l'article L. 162-1-7 n'a pas procédé à la hiérarchisation dans un délai ne pouvant dépasser cinq mois à compter de la transmission à l'Union nationale des caisses d'assurance maladie de l'avis de la Haute Autorité de santé mentionné au troisième alinéa du même article et de l'évaluation mentionnée au deuxième alinéa du présent article, l'Union peut hiérarchiser un acte dont le service attendu est suffisant, à condition qu'il appartienne à l'une des catégories suivantes :

1° Les actes présentant un niveau déterminé d'amélioration du service attendu et dont l'inscription sur la liste prévue à l'article L. 162-1-7 est nécessaire à l'utilisation ou à la prise en charge par l'assurance maladie de l'un des produits de santé définis aux articles L. 5211-1 ou L. 5221-1 du code de la santé publique ;

2° Les actes pratiqués uniquement dans un établissement de santé et ayant, ou susceptibles d'avoir, un impact significatif sur l'organisation des soins et les dépenses de l'assurance maladie ;

3° Les actes ayant fait l'objet d'une tarification provisoire dans le cadre d'une expérimentation, notamment dans les conditions prévues à l'article L. 162-31-1 du présent code, et présentant un niveau déterminé d'amélioration du service attendu ou susceptibles d'avoir un impact significatif sur l'organisation des soins et les dépenses de l'assurance maladie ;

4° Les actes inscrits dans un protocole de coopération ayant fait l'objet d'une proposition du comité national des coopérations interprofessionnelles mentionnée au deuxième alinéa du I de l'article L. 4011-3 du code de la santé publique.

La Haute Autorité de santé évalue l'impact des actes mentionnés aux 2° et 3° sur l'organisation des soins et les dépenses de l'assurance maladie.

Lorsque l'Union nationale des caisses d'assurance maladie utilise la faculté prévue au premier alinéa, elle adresse la décision d'inscription de l'acte aux ministres chargés de la santé et de la sécurité sociale dans les trente jours suivant l'expiration du délai mentionné à ce premier alinéa.

Si l'Union nationale des caisses d'assurance maladie ne prend pas de décision dans le délai mentionné au septième alinéa, elle en informe les ministres chargés de la santé et de la sécurité sociale et leur en précise les motifs.

Dans le cas prévu au 3°, l'acte continue d'être pris en charge dans les conditions de l'expérimentation si une demande d'évaluation a été déposée auprès de la Haute Autorité de santé dans un délai maximal de six mois avant la fin de l'expérimentation. Cette prise en charge s'applique jusqu'à la décision de l'Union nationale des caisses d'assurance maladie, dans la limite d'un an à compter du dépôt de la demande.

Un décret en Conseil d'Etat détermine les modalités d'application du présent article, notamment les critères mentionnés aux 1° à 3°. Un décret fixe les modalités relatives aux délais.

Pour des raisons de santé publique, le ministre chargé de la santé peut inscrire ou radier d'office un acte ou une prestation, par arrêté pris après avis de la Haute Autorité de santé. Il en fixe alors la hiérarchisation dans le respect des règles ci-dessus. Les tarifs de ces actes et prestations sont publiés au Journal officiel.
''', "Réécriture à droit constant : les quatre catégories d'actes et les étapes de hiérarchisation subsidiaire sont distinguées, avec un sujet explicite pour les décisions et notifications. Les délais, la poursuite temporaire de l'expérimentation et le pouvoir ministériel d'office sont conservés. Aucune réforme de fond n'est introduite.", "Renvois préexistants à contrôler : le troisième alinéa de L. 162-1-7, dans la source assignée de cet article, ne contient plus l'avis de la Haute Autorité de santé ; le deuxième alinéa du présent article ne contient pas l'évaluation d'impact désormais énoncée après les 1° à 4°. Ces désignations sont conservées sans correction silencieuse ; leur remplacement exige une coordination explicite. Les quatre éléments numérotés, séparés par des br dans un même p de la source, sont matérialisés en quatre p sans changer leur ordre : le septième alinéa substantiel reste celui du délai de trente jours. La formulation source du délai maximal de six mois avant la fin de l'expérimentation, dont le point de départ appelle vérification, est maintenue. La note source fixe l'entrée en vigueur au 1er avril 2020, en application du IV de l'article 38 de la loi n° 2019-1446 du 24 décembre 2019.")

add('L162-1-9', '''
Une commission des équipements matériels lourds d'imagerie médicale est instituée auprès de l'Union nationale des caisses d'assurance maladie et présidée par son directeur général. Elle comprend des représentants des médecins libéraux et hospitaliers spécialistes en radiodiagnostic et en imagerie médicale, des représentants des médecins spécialistes en médecine nucléaire, des représentants des fédérations hospitalières représentatives et des représentants de l'Union nationale des caisses d'assurance maladie. Un représentant de l'Etat assiste à ses travaux.

La commission rend un avis motivé sur les propositions de l'Union nationale des caisses d'assurance maladie prévues à l'article L. 162-1-9-1.

Un arrêté fixe la composition et les règles de fonctionnement de la commission.
''', "Réécriture à droit constant : la présidence, les composantes de la commission et sa mission d'avis sont exposées en phrases plus courtes. Les trois alinéas et l'habilitation par arrêté sont conservés, sans réforme de fond.", "Toutes les catégories de représentants et la présence du représentant de l'Etat sont maintenues. L'avis reste motivé et porte sur les propositions de L. 162-1-9-1.")

add('L162-1-9-1', '''
I. - Au moins une fois tous les trois ans, avant le 1er mars de l'année concernée, le directeur général de l'Union nationale des caisses d'assurance maladie transmet à la commission prévue à l'article L. 162-1-9 :

1° Des éléments relatifs à l'évolution constatée, pendant la période concernée, des charges associées aux équipements matériels lourds d'imagerie médicale soumis à l'autorisation prévue à l'article L. 6122-1 du code de la santé publique et utilisés pour des actes et prestations délivrés par des professionnels de santé libéraux ou hospitaliers ;

2° S'il y a lieu, une analyse de l'évolution de l'organisation et du fonctionnement des différentes structures qui utilisent ces équipements ;

3° Des propositions d'évolution pluriannuelle des rémunérations liées à l'acquisition et au fonctionnement de ces équipements ;

4° Des propositions d'évolution de la classification de ces équipements ;

5° Un bilan de l'impact financier des propositions mentionnées aux 3° et 4°.

Les propositions mentionnées aux 3° et 4° sont aussi transmises aux organisations syndicales représentatives des médecins généralistes et des médecins spécialistes, ainsi qu'aux ministres chargés de la santé et de la sécurité sociale.

II. - Pour connaître les charges du secteur de l'imagerie médicale, l'Union nationale des caisses d'assurance maladie peut réaliser tous les trois ans une étude nationale de coût des charges de ce secteur. Avant le recueil des données, la commission prévue à l'article L. 162-1-9 est consultée sur la méthodologie et le calendrier de l'étude. Elle rend un avis sur ses résultats.

Cette étude comprend notamment le recueil, auprès d'un échantillon représentatif de personnes physiques ou morales, des informations ou documents nécessaires aux études et propositions mentionnées aux 1° à 3° du I.

Le recueil doit garantir que les informations protégées par le secret mentionné à l'article L. 151-1 du code de commerce ne sont pas divulguées.

L'échantillon représentatif est constitué tous les trois ans par appel à candidatures. Des désignations peuvent le compléter pour garantir la fiabilité et la représentativité des données.

Si une personne physique ou morale incluse dans l'échantillon refuse de transmettre les informations demandées, le directeur général de l'Union nationale des caisses d'assurance maladie peut lui infliger une pénalité financière après l'avoir mise en mesure de présenter ses observations. Cette pénalité ne peut dépasser 1 % du montant des remboursements liés à l'acquisition et au fonctionnement des équipements matériels lourds qu'elle exploite, versés par l'assurance maladie au cours des douze mois précédant le refus de transmission.

L'organisme d'assurance maladie compétent recouvre la pénalité selon les huitième et neuvième alinéas du IV de l'article L. 114-17-1. Le produit de cette pénalité est affecté à la Caisse nationale de l'assurance maladie.

Un décret en Conseil d'Etat fixe les modalités d'application du présent II.

III. - La commission mentionnée au I rend son avis sur les propositions mentionnées aux 3° et 4° du même I dans les trente jours suivant leur transmission. A l'expiration de ce délai, l'avis est réputé rendu. Le directeur général de l'Union transmet cet avis aux organisations nationales représentatives de médecins généralistes et de médecins spécialistes, ainsi qu'aux ministres chargés de la santé et de la sécurité sociale.

La convention mentionnée à l'article L. 162-5 définit l'évolution des rémunérations liées à l'acquisition et au fonctionnement de ces équipements matériels lourds d'imagerie médicale et la classification associée.
''', "Réécriture à droit constant : le calendrier de transmission, l'étude facultative de coûts, les garanties du recueil et les conditions de la pénalité sont clarifiés. Les subdivisions I à III, les cinq éléments transmis et l'ensemble des alinéas sont conservés. Aucune réforme de fond n'est appliquée.", "Contrôles ciblés : périodicités de trois ans, transmission avant le 1er mars, plafond de 1 % des remboursements des douze mois précédant le refus, délai d'avis de trente jours et avis réputé rendu conservés. La consultation préalable, le secret commercial, le contradictoire, l'affectation à la CNAM et les renvois aux huitième et neuvième alinéas du IV de L. 114-17-1 sont maintenus.")

add('L162-1-10', '''
Des conditions particulières d'exercice sont mises en œuvre pour permettre aux professionnels de santé libéraux ou salariés des centres de santé de délivrer des soins palliatifs à domicile. Elles peuvent prévoir des modes particuliers de rémunération autres que le paiement à l'acte. Elles peuvent aussi prévoir le paiement direct des professionnels par les organismes d'assurance maladie. L'accord conventionnel interprofessionnel prévu au II de l'article L. 162-14-1 détermine ces modes particuliers de rémunération et leur montant.

Un décret définit les modalités d'application du présent article.
''', "Réécriture à droit constant : le champ des professionnels et l'objet des conditions particulières sont explicités ; la fixation conventionnelle des rémunérations est exprimée directement. Aucune réforme de fond n'est introduite.", "Le champ reste celui des soins palliatifs à domicile délivrés par les libéraux ou les salariés des centres de santé. La formulation fautive de la source « accord au conventionnel interprofessionnel » est corrigée en « accord conventionnel interprofessionnel », sans modifier le renvoi au II de L. 162-14-1 ni la compétence de cet accord. Les deux alinéas sont conservés.")

add('L162-1-11', '''
Les organismes gestionnaires des régimes obligatoires de base de l'assurance maladie assurent, par tous moyens adaptés, l'information générale des assurés sociaux. Cette mission vise notamment à faciliter leur accès aux soins et à la protection sociale et à leur faire connaître les conditions de prise en charge des actes de prévention, de diagnostic ou de soins qu'ils reçoivent.

Les assurés sociaux peuvent obtenir toutes informations utiles, notamment sur les tarifs applicables, les taux de remboursement, les conditions de prise en charge des services et des produits de santé et le bon usage des soins ou de ces produits.

Les caisses peuvent aussi proposer des services de conseils administratifs ou d'orientation. Ces services doivent donner aux assurés les informations nécessaires pour accéder à la prévention et aux soins dans les meilleures conditions. Ils peuvent notamment les informer sur les services des établissements de santé, sur la situation des professionnels de santé au regard des règles conventionnelles ou réglementaires qui les régissent, sur leur adhésion aux contrats prévus à l'article L. 162-12-21 du présent code et à l'article L. 1435-4 du code de la santé publique, sur leur participation à la coordination des soins et sur leur engagement dans la démarche de développement professionnel continu prévue à l'article L. 4021-1 du code de la santé publique. Ils fournissent aussi tous éléments d'information sur les tarifs d'honoraires habituellement demandés et toutes informations utiles pour bien orienter le patient dans le système de soins.

Les caisses nationales d'assurance maladie peuvent créer des programmes d'accompagnement des patients atteints de maladies chroniques, pour leur apporter des conseils d'orientation dans le système de soins et d'éducation à la santé.

Les caisses nationales d'assurance maladie peuvent créer des programmes d'aide au sevrage tabagique destinés aux personnes auxquelles un traitement de substitution nicotinique a été prescrit. Ces programmes visent à apporter des conseils et un soutien pour favoriser l'arrêt du tabac.

Les différents régimes d'assurance maladie coordonnent leurs actions pour assurer cette mission et veillent à mettre en commun les moyens nécessaires, le cas échéant par convention.

Les organismes qui gèrent un régime obligatoire pour le compte d'une caisse d'assurance maladie peuvent être associés à la mission du présent article dans le cadre d'une convention spécifique.

Les différents régimes d'assurance maladie coordonnent leurs actions pour assurer cette mission, veillent à mettre en commun les moyens nécessaires, le cas échéant par convention, et évaluent cette mission chaque année avec le concours de représentants des familles et des usagers.
''', "Réécriture à droit constant : les obligations d'information et les programmes facultatifs sont distingués par des phrases plus courtes. Les informations relatives aux professionnels, aux contrats, aux tarifs et à l'orientation sont intégralement reprises. Les huit alinéas sont conservés ; aucune réforme de fond n'est introduite.", "La source répète l'obligation de coordination et de mutualisation aux sixième et huitième alinéas, ce dernier ajoutant l'évaluation annuelle avec les représentants des familles et usagers. Ce doublon préexistant est maintenu afin de ne pas déplacer ou supprimer un alinéa cible ; sa suppression éventuelle exigerait une coordination explicite. Les renvois à L. 162-12-21, L. 1435-4 et L. 4021-1 sont conservés.")

add('L162-1-12', '''
Les bénéficiaires de l'examen bucco-dentaire de prévention mentionné à l'article L. 2132-2-1 du code de la santé publique et des soins dentaires réalisés dans les six mois suivant cet examen sont intégralement dispensés d'avancer les frais de ces actes, à l'exception des inlay-onlay, des soins prothétiques et des soins d'orthopédie dento-faciale. Cette dispense porte sur la part des dépenses prise en charge par l'assurance maladie et sur celle prise en charge, le cas échéant, par l'organisme d'assurance maladie complémentaire.
''', "Réécriture à droit constant : la dispense d'avance de frais et les deux parts de dépenses concernées sont exprimées en deux phrases au sein du même alinéa. Le délai et les trois exclusions sont maintenus ; aucune réforme de fond n'est introduite.", "La dispense n'est pas une prise en charge nouvelle : elle porte sur les parts effectivement couvertes par les organismes. La note source prévoit l'application au 1er avril 2025 au titre du III de l'article 63 de la loi n° 2025-199 du 28 février 2025, avec les mesures afférentes des articles 24.1 à 24.2.1.4 du sous-titre I du titre III et de l'article 28 du sous-titre II du titre III de la convention dentaire publiée au Journal officiel du 25 août 2023. Ces références historiques ne sont pas des paramètres de réforme future.")

add('L162-1-12-1 A', '''
Les régimes obligatoires de l'assurance maladie et maternité prennent intégralement en charge les examens de repérage des troubles du neuro-développement prévus à l'article L. 2132-2-2 du code de la santé publique. Les bénéficiaires de ces examens n'ont pas à avancer les frais.
''', "Réécriture à droit constant : les régimes débiteurs sont le sujet de l'obligation et la dispense d'avance de frais fait l'objet d'une phrase distincte, dans le même alinéa. Aucune réforme de fond n'est introduite.", "La prise en charge intégrale, la dispense d'avance et le seul champ des examens mentionnés à L. 2132-2-2 sont conservés. Le numéro d'article, y compris la lettre A, reste identique.")

add('L162-1-12-1', '''
Toute personne âgée de seize ans bénéficie, lors de sa sortie du statut d'ayant droit à l'assurance maladie puis à l'âge de vingt-trois ans, d'une information individualisée délivrée par les organismes gestionnaires des régimes obligatoires d'assurance maladie. Cette information porte sur ses droits à la couverture obligatoire et complémentaire du risque maladie, sur les dispositifs et programmes de prévention, sur les consultations accessibles aux jeunes consommateurs proposées par les centres de soins, d'accompagnement et de prévention en addictologie mentionnés au 9° de l'article L. 312-1 du code de l'action sociale et des familles, ainsi que sur les examens de santé gratuits dont elle peut bénéficier, notamment celui prévu à l'article L. 321-3 du code de la sécurité sociale. Elle comprend un volet consacré à l'éducation à la sexualité, à la contraception et à l'interruption volontaire de grossesse.

Les organismes gestionnaires des régimes obligatoires conduisent des actions de prévention et de pédagogie pour améliorer l'état de santé de leurs ressortissants âgés de seize à vingt-cinq ans. Ces actions sont prolongées jusqu'à vingt-huit ans pour les personnes encore étudiantes.

Les actions du deuxième alinéa destinées aux étudiants sont conduites conjointement avec les services communs mentionnés au chapitre IV du titre Ier du livre VII de la troisième partie du code de l'éducation.

Lorsqu'elles s'adressent aux étudiants, ces actions s'inscrivent dans un programme annuel de prévention. Ce programme est élaboré dans le cadre des orientations de la stratégie nationale de santé mentionnée à l'article L. 1411-1-1 du code de la santé publique, après concertation avec les représentants des associations d'étudiants mentionnées à l'article L. 811-3 du code de l'éducation.

Les actions mentionnées à l'article L. 841-5 du même code s'inscrivent également dans ce programme annuel lorsqu'elles visent la prévention, l'éducation ou la promotion des comportements favorables à la santé, ou le développement de l'accès des étudiants aux soins, au dépistage et à la vaccination.
''', "Réécriture à droit constant : l'information individualisée est séparée de son contenu, puis les actions de prévention et leur programmation sont formulées plus directement. Les cinq alinéas, les âges et les renvois sont conservés ; aucune réforme de fond n'est introduite.", "Les âges de seize ans et vingt-trois ans pour l'information, de seize à vingt-cinq ans pour les actions et de vingt-huit ans pour leur prolongation aux étudiants sont maintenus. La formulation source articulant l'âge de seize ans avec la sortie du statut d'ayant droit est conservée et appelle un contrôle de portée avant adoption ; aucun troisième fait générateur autonome n'est créé. Les consultations d'addictologie et l'ensemble du volet relatif à la sexualité sont maintenus.")

add('L162-1-13', '''
Un accord-cadre conclu entre l'Union nationale des caisses d'assurance maladie et l'Union nationale des professionnels de santé définit les rapports entre les organismes d'assurance maladie et les professions mentionnées aux articles L. 162-5, L. 162-9, L. 162-12-2, L. 162-12-9, L. 162-14, L. 162-16-1 et L. 322-5-2.

L'accord-cadre ne s'applique à l'une de ces professions que si au moins une organisation syndicale représentative de cette profession l'a signé.

Conclu pour une durée maximale de cinq ans, l'accord-cadre fixe des dispositions communes à l'ensemble des professions relevant des conventions prévues aux sections 1, 2 et 3 du présent chapitre, à l'article L. 162-16-1 et à l'article L. 322-5-2. Il peut notamment fixer les obligations respectives des organismes d'assurance maladie et des professionnels de santé exerçant en ville. Il peut aussi définir les mesures que les partenaires conventionnels jugent appropriées pour garantir la qualité des soins et une meilleure coordination des soins, ou pour promouvoir des actions de santé publique.
''', "Réécriture à droit constant : les parties à l'accord-cadre, sa condition d'application par profession et ses objets sont exposés directement. Les trois alinéas et l'ensemble des professions visées sont conservés, sans réforme de fond.", "Durée maximale de cinq ans et signature d'au moins une organisation représentative de chaque profession concernée maintenues. Les sept renvois du premier alinéa et le périmètre conventionnel du troisième sont conservés.")

add('L162-1-14-1', '''
Le directeur de l'organisme local d'assurance maladie peut sanctionner les professionnels de santé qui :

1° Pratiquent une discrimination dans l'accès à la prévention ou aux soins, au sens de l'article L. 1110-3 du code de la santé publique, y compris dans l'accès à un moyen de contraception en urgence ;

2° Exposent les assurés à des dépassements d'honoraires excédant le tact et la mesure ;

3° Exposent les assurés à des dépassements d'honoraires non conformes à la convention applicable au professionnel de santé, au I de l'article L. 162-5-13, au dernier alinéa de l'article L. 162-9 ou aux deuxième et troisième alinéas du I de l'article L. 165-6 ;

4° Omettent de délivrer l'information écrite préalable prévue à l'article L. 1111-3-2 du code de la santé publique.

La sanction est prononcée après avis de la commission et selon la procédure prévus à l'article L. 114-17-1 du présent code. Elle peut consister en :

- une pénalité financière forfaitaire ne dépassant pas deux fois le plafond mensuel de la sécurité sociale, dans les cas mentionnés au 1° ;

- une pénalité financière proportionnelle aux dépassements facturés, ne dépassant pas deux fois le montant des dépassements en cause, dans les cas mentionnés aux 2°, 3° et 4° ;

- en cas de récidive dans un délai fixé par voie réglementaire, un retrait temporaire du droit à dépassement ou une suspension de la participation des caisses au financement des cotisations sociales prévue au 5° du I de l'article L. 162-14-1.

Les sanctions prononcées en application du présent article sont notifiées après avis conforme du directeur de l'Union nationale des caisses d'assurance maladie ou de son représentant désigné à cet effet. Cet avis est réputé conforme dans un délai précisé par voie réglementaire.

Ces sanctions peuvent être affichées dans les locaux de l'organisme local d'assurance maladie. En cas de récidive, elles peuvent aussi être rendues publiques par voie de presse, après épuisement des voies de recours.

Les décisions de sanction peuvent être contestées devant le tribunal judiciaire spécialement désigné en application de l'article L. 211-16 du code de l'organisation judiciaire. Les pénalités financières sont recouvrées selon les modalités prévues aux huitième et avant-dernier alinéas du IV de l'article L. 114-17-1.

L'organisme local d'assurance maladie ne peut recourir concurremment aux pénalités du présent article et aux procédures conventionnelles pour sanctionner le même comportement d'un professionnel de santé.

Les modalités d'application du présent article, notamment celles de l'affichage et le barème des sanctions, sont fixées par voie réglementaire.
''', "Réécriture à droit constant : les quatre manquements, les trois formes de sanction et les garanties procédurales sont formulés plus directement. Les plafonds, la récidive, la publicité, les recours et l'interdiction du recours concurrent aux deux procédures sont intégralement conservés. Aucune réforme de fond n'est introduite.", "Les plafonds restent de deux fois le plafond mensuel de la sécurité sociale pour le 1° et de deux fois les dépassements pour les 2° à 4°. La publicité par voie de presse reste soumise à la récidive et à l'épuisement des recours. Les renvois aux subdivisions de L. 114-17-1, L. 162-5-13, L. 162-9, L. 165-6 et L. 162-14-1 sont conservés sans modifier leurs cibles. Aucun délai réglementaire n'est inventé.")

add('L162-1-15', '''
I. - Après avoir mis le professionnel de santé en mesure de présenter ses observations, le directeur de l'organisme local d'assurance maladie peut subordonner à l'accord préalable du service du contrôle médical, pour une durée maximale de six mois, la couverture des actes, produits ou prestations figurant sur les listes mentionnées aux articles L. 162-1-7, L. 162-17 et L. 165-1, la couverture des frais de transport ou le versement des indemnités journalières mentionnés, respectivement, au 2° de l'article L. 160-8 et à l'article L. 321-1 et aux 1° et 2° de l'article L. 431-1 du présent code ainsi qu'aux 1° et 2° de l'article L. 752-3 du code rural et de la pêche maritime. Cette décision peut être prise si le service du contrôle médical constate l'une des situations suivantes :

1° Le professionnel de santé ne respecte pas les conditions prévues, respectivement, au 2° de l'article L. 160-8 et à l'article L. 321-1 et au 1° ou au 2° de l'article L. 431-1 du présent code ainsi qu'aux 1° et 2° de l'article L. 752-3 du code rural et de la pêche maritime ;

2° Le nombre ou la durée des arrêts de travail prescrits par le professionnel de santé et donnant lieu au versement d'indemnités journalières est significativement supérieur aux données moyennes constatées, pour une activité comparable, chez les professionnels de santé exerçant la même profession dans le ressort de la même agence régionale de santé ou du même organisme local d'assurance maladie. Pour le nombre d'arrêts, cette comparaison peut porter sur le nombre absolu ou sur le nombre rapporté au nombre de patients pour lesquels au moins un acte ou une consultation a été facturé au cours de la période considérée ;

3° Le nombre de prescriptions de transports ou le montant des remboursements de transports résultant de ces prescriptions est significativement supérieur à la moyenne des prescriptions de transport constatée, pour une activité comparable, chez les médecins exerçant dans le ressort de la même agence régionale de santé ou du même organisme local d'assurance maladie. Cette comparaison peut porter sur ce nombre ou ce montant en valeur absolue, ou rapporté au nombre de patients pour lesquels au moins un acte ou une consultation a été facturé au cours de la période considérée ;

4° Le taux de prescription de transports en ambulance, rapporté à l'ensemble des transports prescrits, est significativement supérieur aux données moyennes constatées, pour une activité comparable, chez les médecins installés dans le ressort de la même agence régionale de santé ou du même organisme local d'assurance maladie ;

5° Le nombre de réalisations ou de prescriptions d'un acte, d'un produit ou d'une prestation figurant sur les listes mentionnées au premier alinéa, ou d'un groupe de ces actes, produits ou prestations, est significativement supérieur à la moyenne des réalisations ou des prescriptions constatée, pour une activité comparable, chez les professionnels de santé exerçant la même profession dans le ressort de la même agence régionale de santé ou du même organisme local d'assurance maladie. Cette comparaison peut porter sur ce nombre en valeur absolue ou rapporté au nombre de patients pour lesquels au moins un acte ou une consultation a été facturé au cours de la période considérée. Pour dénombrer les réalisations d'actes, sont exclus ceux réalisés en application et dans le respect d'une prescription médicale qui en précise expressément le nombre. Un décret définit les modalités de constitution éventuelle de groupes d'actes, de produits ou de prestations pour l'application du présent alinéa.

Toutefois, si le professionnel de santé prescripteur atteste l'urgence, l'accord préalable de l'organisme débiteur des prestations n'est pas requis pour prendre en charge les frais de transport et les actes, produits ou prestations figurant sur les listes mentionnées au premier alinéa.

I bis. - Après avoir mis le centre de santé ou la société de téléconsultation mentionnée à l'article L. 4081-1 du code de la santé publique en mesure de présenter ses observations, le directeur de l'organisme local d'assurance maladie peut subordonner à l'accord préalable du service du contrôle médical, pour une durée maximale de six mois, la couverture des actes, produits ou prestations figurant sur les listes mentionnées aux articles L. 162-1-7, L. 162-17 et L. 165-1 du présent code, la couverture des frais de transport ou le versement des indemnités journalières mentionnés au 2° de l'article L. 160-8, à l'article L. 321-1 et aux 1° et 2° de l'article L. 431-1 du présent code ainsi qu'aux 1° et 2° de l'article L. 752-3 du code rural et de la pêche maritime. Cette décision peut être prise si le service du contrôle médical constate l'une des situations définies aux 1° à 5° du I du présent article, sous réserve du dernier alinéa du même I.

Pour les centres de santé et les sociétés de téléconsultation, la condition d'activité comparable s'apprécie dans le ressort de la même agence régionale de santé ou au niveau national.

II. - Conjointement avec le service du contrôle médical, le directeur peut aussi proposer au professionnel de santé, au centre de santé ou à la société de téléconsultation de s'engager à atteindre, dans un certain délai, un objectif de réduction des prescriptions ou réalisations en cause, en alternative à la procédure de mise sous accord préalable prévue au I. En cas de refus, il poursuit la procédure prévue au I ou au I bis.

II bis. - La décision mentionnée au premier alinéa du I est notifiée après avis conforme du directeur de l'Union nationale des caisses d'assurance maladie ou de son représentant désigné à cet effet. Cet avis est réputé conforme dans un délai précisé par voie réglementaire.

III. - Un décret en Conseil d'Etat fixe les modalités d'application du présent article.
''', "Réécriture à droit constant : les conditions de mise sous accord préalable sont formulées comme cinq constats distincts ; les indicateurs absolus et rapportés aux patients sont explicités à l'intérieur des mêmes alinéas. Les subdivisions I, I bis, II, II bis et III, l'urgence, l'exclusion des actes médicalement prescrits en nombre, le contradictoire et l'alternative d'engagement sont conservés. Aucune réforme de fond n'est introduite.", "Les deux durées maximales de six mois, les quatre familles d'indicateurs comparatifs des 2° à 5°, les professions comparées et les périmètres territoriaux sont maintenus. L'urgence ne dispense pas ici d'accord préalable pour les indemnités journalières. Le I bis conserve le champ national de comparaison et le renvoi au dernier alinéa du I. Deux particularités préexistantes sont maintenues : le II désigne la procédure du I comme alternative même pour les structures, avant de viser I ou I bis en cas de refus ; le II bis ne vise expressément que la décision du premier alinéa du I. Une extension de ces renvois au I bis nécessiterait une coordination explicite. Les renvois au code rural ne sont pas modifiés.")

add('L162-1-16', '''
I. - Les actes ou prestations inscrits sur la liste prévue à l'article L. 162-1-7, réalisés pendant son affectation par un réserviste mentionné à l'article L. 3132-1 du code de la santé publique, donnent lieu :

- sous réserve du II du présent article, lorsqu'il remplace des professionnels de santé libéraux ou leur apporte son concours, au reversement à l'Agence nationale de santé publique du montant des honoraires qu'il perçoit. Le réserviste doit respecter les tarifs mentionnés aux articles L. 162-14-1 et L. 162-1-7. Le cas échéant, la part reversée au cabinet libéral ou à la structure d'affectation est déduite de ce reversement, selon des modalités fixées par arrêté du ministre chargé de la sécurité sociale ;

- lorsqu'il est mis à disposition d'une personne morale, au remboursement par celle-ci à l'Agence nationale de santé publique des indemnités ou rémunérations qu'il perçoit pendant la période de cette mise à disposition.

II. - Un décret en Conseil d'Etat détermine les conditions dans lesquelles un arrêté de l'autorité compétente de l'Etat peut fixer les modalités particulières de rémunération des professionnels de santé libéraux exerçant dans le cadre des mesures d'urgence prises en application de l'article L. 3131-1 du code de la santé publique.
''', "Réécriture à droit constant : les deux situations d'affectation du réserviste et les débiteurs des reversements ou remboursements sont explicités. Les subdivisions I et II, les deux tirets et le régime de rémunération d'urgence sont conservés. Aucune réforme de fond n'est introduite.", "La source comporte deux fois la tournure défectueuse « Agence nationale de santé publique du code de la santé publique ». Seul ce raccord grammatical est retiré ; le bénéficiaire reste l'Agence nationale de santé publique. La réserve du II, les tarifs, la déduction éventuelle et les compétences respectives de l'arrêté et du décret en Conseil d'Etat sont maintenus. Les renvois à L. 3132-1 et L. 3131-1 sont conservés sans substitution.")

assert len(sources) == 22
assert len(drafts) == len(sources)
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[source['number']])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
