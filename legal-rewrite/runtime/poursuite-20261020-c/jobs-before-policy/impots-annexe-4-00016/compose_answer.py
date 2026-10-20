import json
from html import escape
from pathlib import Path


source = json.loads(Path('source.json').read_text())
drafts = {}


def add(index, paragraphs, reason, review):
    drafts[index] = {
        'proposed_xml': '\n'.join('<p>' + escape(p, quote=False) + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review,
    }


add(0, [
    "Seuls les syndicats viticoles et les groupements professionnels peuvent être habilités à répartir les capsules collectives représentatives des droits destinées aux récoltants. Cette habilitation est subordonnée à l'agrément du directeur régional des douanes et droits indirects territorialement compétent.",
    "Les personnes habilitées à détenir des capsules représentatives de droits sont comptables des droits représentés par les marques fiscales qu'elles détiennent. Elles doivent fournir un cautionnement garantissant le paiement des droits correspondant aux capsules détenues ainsi que des droits sur les capsules expédiées aux récoltants sous le couvert du document mentionné au I de l'article 302 M du code général des impôts.",
    "Le directeur régional des douanes et droits indirects peut autoriser une personne habilitée à percevoir le droit de circulation lorsqu'elle répartit les capsules à ses seuls adhérents. La personne habilitée reverse ces droits chaque mois à la recette des douanes et droits indirects dont elle dépend.",
    "Les personnes habilitées doivent tenir une comptabilité matières comportant les indications suivantes :",
    "a) En entrée, le nombre de capsules reçues par catégorie, avec les références au document mentionné au I de l'article 302 M du code général des impôts. Les catégories sont distinguées notamment selon le volume net exprimé en centilitres, la couleur, le caractère tranquille ou mousseux pour les vins et, le cas échéant, le titre alcoométrique volumique ;",
    "b) En sortie, le nombre de capsules expédiées ou livrées, par destinataire et par catégorie, avec les références au document mentionné, selon le cas, au I ou au II de l'article 302 M du code général des impôts.",
    "Les personnes habilitées tiennent cette comptabilité matières et les capsules qu'elles détiennent à la disposition des agents des douanes et droits indirects pour leur contrôle.",
    "Chaque mois, la personne habilitée établit la balance des entrées et des sorties de la comptabilité matières. Elle la transmet au service des douanes et droits indirects dont elle dépend au plus tard le cinquième jour du mois suivant.",
], "Réécriture à droit constant : les organismes admissibles, l'autorité d'agrément, le cautionnement, la perception et le reversement des droits ainsi que les obligations de comptabilité et de contrôle sont exprimés avec un sujet explicite. Les huit alinéas utiles et les lettres a) et b) sont conservés. Aucune réforme de fond de policy.json ne vise ce régime.",
    "Le cinquième jour du mois suivant, le reversement mensuel et la limitation de la perception aux seuls adhérents sont conservés. Le renvoi à l'article 302 M, I et II, est maintenu ; cet article n'a pas été retrouvé dans le fichier public impots.json fourni : son actualisation nécessite un contrôle de coordination, sans substitution inventée. Les points de suspension de la liste des catégories sont rendus par « notamment », afin de conserver son caractère ouvert.")

add(1, [
    "Les capsules mentionnées à l'article 54-0 BW doivent présenter les caractéristiques fixées par les articles 54-0 B à 54-0 E. Toutefois, le numéro d'agrément de la personne responsable de l'embouteillage est remplacé par le numéro attribué à la personne habilitée.",
    "Le récoltant doit apposer sur les bouteilles et récipients portant ces capsules des étiquettes indiquant obligatoirement ses nom et adresse.",
], "Réécriture à droit constant : l'exception relative au numéro d'agrément est isolée dans une phrase et l'obligation d'étiquetage est directement attribuée au récoltant. Les deux alinéas et tous les renvois sont conservés ; aucune réforme de fond n'est appliquée.",
    "Les articles 54-0 B à 54-0 E du corpus public ont été lus pour vérifier les caractéristiques visées. Seul le numéro d'agrément est remplacé ; l'identification obligatoire du récoltant sur les étiquettes demeure distincte.")

add(2, [
    "Lorsqu'un professionnel transporte, ou fait transporter pour son compte, des alcools et boissons alcooliques dans des bouteilles et récipients revêtus de capsules représentatives de droits, les produits doivent circuler sous le couvert d'un document commercial. Ce document comporte l'identité de l'expéditeur, le nom et l'adresse du destinataire, le numéro de référence et la date d'établissement du document, la nature et la désignation des produits transportés avec leur dénomination et, le cas échéant, leur appellation d'origine, les quantités et, selon le cas, le titre alcoométrique volumique acquis des boissons. Le document commercial doit être présenté aux agents des douanes à première réquisition.",
    "Le document commercial prévu au premier alinéa ne s'applique pas aux livraisons destinées à des personnes situées hors du territoire fiscal de la France. Ces livraisons doivent être effectuées sous le couvert des documents d'accompagnement mentionnés à l'article 302 M du code général des impôts.",
], "Réécriture à droit constant : le champ du transport professionnel est placé en tête et la longue phrase est divisée sans déplacer les mentions obligatoires hors du premier alinéa. L'exclusion territoriale et le régime documentaire correspondant restent au second alinéa. Aucune réforme de fond n'est appliquée.",
    "Toutes les mentions documentaires, le titre alcoométrique volumique acquis « selon le cas », l'appellation d'origine « le cas échéant » et la présentation à première réquisition sont conservés. Le renvoi à l'article 302 M est maintenu, mais cet article n'a pas été retrouvé dans impots.json : coordination à contrôler sans créer de renvoi de remplacement.")

add(3, [
    "Les cidres et poirés bénéficient des dispositions du 5° de l'article 458 du code général des impôts lorsqu'ils sont libérés des droits indirects et livrés en récipients portant de manière apparente le nom et l'adresse du fabricant ou de l'embouteilleur.",
], "Réécriture à droit constant : le bénéfice du régime est directement rattaché aux cidres et poirés et à ses deux conditions cumulatives. Le renvoi et l'unique alinéa utile sont conservés ; aucune réforme de fond n'est appliquée.",
    "L'acquittement des droits indirects et la mention apparente du nom et de l'adresse du fabricant ou de l'embouteilleur restent requis. L'article 458 n'a pas été retrouvé dans le fichier public impots.json : le renvoi à son 5° est conservé et appelle un contrôle de coordination.")

add(4, [
    "Pour les vins doux naturels à appellation d'origine contrôlée, l'instance compétente ou les expéditeurs authentifient les mentions relatives à l'appellation d'origine figurant sur les documents d'accompagnement au vu d'une attestation établie par le comité interprofessionnel des vins doux naturels. Cette attestation constate que le produit a fait l'objet d'un agrément par l'Institut national de l'origine et de la qualité et précise, s'il y a lieu, les comptes d'âge.",
], "Réécriture à droit constant : l'auteur de l'authentification devient le sujet de la phrase et le contenu de l'attestation fait l'objet d'une seconde phrase, dans le même alinéa. Les deux auteurs possibles et les comptes d'âge conditionnels sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les erreurs rédactionnelles « instance compétence » et « au vue » sont corrigées en « instance compétente » et « au vu », sans changement de compétence. L'instance n'est pas identifiée plus précisément dans la source : aucune autorité nouvelle ne lui est substituée. L'agrément du produit par l'Institut national de l'origine et de la qualité est conservé.")

add(5, [
    "Les professionnels qui font déterminer par les bureaux de garantie le titre des lingots, apprêts ou composants entrant dans leurs fabrications doivent acquitter la rémunération prévue à l'article 191 de l'annexe III au code général des impôts. Cette rémunération est fixée, par opération, à 38 euros pour l'or et le platine et à 15 euros pour l'argent.",
    "Les bureaux de douane perçoivent cette rémunération. Les recettes correspondantes sont comptabilisées aux produits divers du budget.",
], "Réécriture à droit constant : les professionnels débiteurs, la prestation rémunérée et les bureaux chargés du recouvrement sont explicités. Les tarifs par opération et l'imputation budgétaire sont conservés dans les deux alinéas. Aucune réforme de fond n'est appliquée.",
    "Contrôle des montants : 38 euros pour l'or et le platine, 15 euros pour l'argent, par opération. Le renvoi à l'article 191 de l'annexe III a été vérifié dans le corpus public ; ce texte renvoie lui-même à l'article 56 J bis. Ces rémunérations ne sont pas modifiées par les orientations fiscales de policy.json.")

add(6, [
    "Toute personne physique ou morale qui souhaite exercer la profession de commissionnaire en garantie prévue à l'article L. 834-3 du code de commerce doit présenter une demande écrite d'agrément. Elle dépose cette demande auprès de la direction interrégionale des douanes et droits indirects territorialement compétente ou, en Guadeloupe, en Guyane, à La Réunion et à Mayotte, de la direction régionale des douanes et droits indirects. La demande indique les nom et adresse du demandeur ainsi que le ou les bureaux de garantie auprès desquels il souhaite exercer son activité.",
    "La personne physique joint à sa demande un extrait du casier judiciaire ou, à défaut, toute pièce en tenant lieu, ainsi qu'un justificatif d'identité. La personne morale joint un extrait du registre du commerce et des sociétés.",
], "Réécriture à droit constant : la demande, son destinataire et son contenu sont présentés en phrases distinctes au premier alinéa ; les pièces sont séparées selon la qualité du demandeur au deuxième alinéa. Aucune réforme de fond n'est appliquée et aucune dispense documentaire n'est créée.",
    "Le deuxième alinéa reste celui des justificatifs, car l'article 56 J septies le vise. Les quatre territoires, le choix d'un ou plusieurs bureaux et le caractère subsidiaire de la pièce tenant lieu d'extrait du casier judiciaire sont conservés. Le renvoi au code de commerce, hors du corpus fourni, est maintenu sans validation externe ni modification.")

add(7, [
    "La direction interrégionale ou régionale mentionnée à l'article 56 J quinquies accuse réception de la demande et ouvre sans délai une enquête.",
    "Cette direction peut demander la présentation de toute pièce complémentaire nécessaire à l'instruction. Elle statue dans les deux mois suivant la date de réception de la demande.",
], "Réécriture à droit constant : le pouvoir de demander des pièces et l'obligation de statuer sont formulés en deux phrases, en conservant les deux alinéas. L'enquête demeure immédiate et le délai part de la réception de la demande. Aucune réforme de fond n'est appliquée.",
    "Le délai de deux mois n'est pas reporté à la réception d'un dossier complet. La note source maintient, conformément au II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), l'instruction des demandes de décisions administratives individuelles présentées avant son entrée en vigueur selon les procédures applicables à la date de leur présentation. Cette transition reste applicable ; elle n'est pas une date d'entrée en vigueur d'une réforme future.")

add(8, [
    "L'agrément de commissionnaire en garantie est délivré à titre personnel.",
    "Une personne morale obtient l'agrément pour elle-même et pour les personnes physiques nommément désignées qui sont habilitées à la représenter. Ces personnes physiques doivent justifier qu'elles appartiennent à son personnel et présenter les documents mentionnés au deuxième alinéa de l'article 56 J quinquies qui concernent les personnes physiques.",
], "Réécriture à droit constant : la portée personnelle de l'agrément est maintenue et la représentation de la personne morale est décrite avec des sujets identifiés. Le rattachement des représentants au personnel et les justificatifs requis demeurent cumulatifs. Aucune réforme de fond n'est appliquée.",
    "Le renvoi au deuxième alinéa de l'article 56 J quinquies reste opérant dans la proposition correspondante. La désignation nominative des représentants et leur appartenance au personnel ne sont pas remplacées par une habilitation générale.")

add(9, [
    "Le directeur interrégional ou régional territorialement compétent au sens de l'article 56 J quinquies accorde l'agrément par décision, pour une durée indéterminée et pour un ou plusieurs bureaux de garantie.",
    "Chaque décision d'agrément est notifiée à son bénéficiaire.",
    "Toute décision rejetant une demande d'agrément doit être motivée et notifiée au requérant.",
], "Réécriture à droit constant : l'autorité devient le sujet de la décision et les obligations de notification sont formulées directement. Les trois alinéas, la durée indéterminée et la possibilité de plusieurs bureaux sont conservés. Aucune réforme de fond n'est appliquée.",
    "L'obligation de motivation reste attachée au rejet, sans être étendue dans cet article à toute décision favorable. La note source réserve, au titre du II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), les procédures applicables à la date de présentation des demandes de décisions administratives individuelles antérieures à l'entrée en vigueur de cet arrêté. Cette règle transitoire est conservée sans nouvelle date inventée.")

add(10, [
    "Le commissionnaire en garantie doit informer l'autorité administrative désignée à l'article 56 J quinquies de tout changement affectant les justificatifs mentionnés à ce même article. Il doit également l'informer de tout changement relatif aux personnes physiques habilitées à représenter les personnes morales agréées.",
], "Réécriture à droit constant : les deux catégories de changements à déclarer sont distinguées par deux phrases au sein du même alinéa. Le destinataire reste l'autorité désignée à l'article 56 J quinquies. Aucune réforme de fond n'est appliquée.",
    "Aucun délai chiffré ni nouvelle pièce n'est ajouté à l'obligation d'information. Selon la note source, le II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A) maintient les procédures applicables à la date de présentation pour les demandes de décisions administratives individuelles présentées avant son entrée en vigueur. Cette transition est conservée.")

add(11, [
    "Le commissionnaire en garantie exerce son activité dans le cadre des mandats écrits qui lui sont confiés. Il doit les présenter à toute réquisition du service des douanes et droits indirects.",
    "Le commissionnaire en garantie doit conserver tous les documents justificatifs de ses activités pendant trois ans à compter de la date à laquelle il accomplit les formalités pour le compte des fabricants ou des marchands mentionnés à l'article L. 832-4 du code de commerce. Il tient ces documents à la disposition du service des douanes et droits indirects.",
], "Réécriture à droit constant : l'exercice sous mandat écrit et sa présentation sont séparés ; la conservation et la mise à disposition des pièces ont un débiteur explicite. Les deux alinéas et le point de départ du délai sont conservés. Aucune réforme de fond n'est appliquée.",
    "Le délai reste de trois ans à compter de l'accomplissement des formalités, sans être remplacé par une durée courant à la clôture de l'exercice ou à la fin du mandat. Le renvoi à l'article L. 832-4 du code de commerce est conservé ; ce code n'est pas inclus dans le corpus public fourni.")

add(12, [
    "En cas de manquement aux dispositions légales ou réglementaires applicables à la garantie des métaux précieux, le directeur interrégional ou régional compétent au sens de l'article 56 J quinquies retire l'agrément par une décision motivée.",
    "Ce directeur peut suspendre sans délai, à titre conservatoire, l'agrément d'une personne morale ou physique qui ne respecte pas ses obligations.",
], "Réécriture à droit constant : le directeur est directement désigné comme auteur du retrait et de la suspension. Le retrait en cas de manquement, sa motivation et le caractère facultatif, conservatoire et immédiat de la suspension sont maintenus. Aucune réforme de fond n'est appliquée.",
    "Le pouvoir de suspension (« peut ») reste distinct du retrait prévu au premier alinéa. La note source conserve, en application du II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), les procédures de la date de présentation pour les demandes de décisions administratives individuelles antérieures à son entrée en vigueur. Cette règle n'est ni supprimée ni convertie en date d'une réforme future.")

add(13, [
    "Les professionnels habilités par une convention doivent décrire, dans le cahier des charges prévu à l'article 275 bis C de l'annexe II au code général des impôts, les moyens et les méthodes de contrôle et d'essai qu'ils mettent en œuvre, ainsi que leurs méthodes d'attestation de la garantie du titre.",
    "Le professionnel doit demander l'autorisation de procéder au marquage au laser pour attester la garantie du titre au directeur interrégional des douanes et droits indirects territorialement compétent ou, en Guadeloupe, en Guyane, à La Réunion et à Mayotte, au directeur régional des douanes et droits indirects. L'autorisation est accordée après que des organismes agréés mentionnés à l'article 275 bis F de l'annexe II au code général des impôts ont vérifié la conformité du protocole de sécurité.",
    "La direction régionale des douanes et droits indirects de rattachement doit approuver le cahier des charges avant l'habilitation du professionnel.",
    "Le cahier des charges mentionné au premier alinéa comprend notamment :",
    "1° Une documentation relative à l'entreprise, qui fournit :",
    "a) Une description des structures juridiques et des locaux de l'entreprise ;",
    "b) Une description de l'organisation et des responsabilités de la direction de l'entreprise ;",
    "2° Une documentation relative aux obligations de contrôle du titre des ouvrages, qui indique :",
    "a) Les sources d'approvisionnement des alliages et des apprêts pour les fabricants, ainsi que les méthodes de contrôle des métaux précieux appliquées depuis leur acquisition jusqu'aux produits finis ;",
    "b) Les méthodes d'analyse interne des produits lorsque le contractant habilité dispose d'un laboratoire dans son entreprise, ou les méthodes d'analyse externe dans les autres cas ;",
    "c) La méthode de gestion des échantillons lors des essais des ouvrages ;",
    "d) La méthode de gestion des produits non conformes au titre légal prévu ;",
    "e) Les modalités de mise en œuvre des actions correctives concernant les ouvrages aux titres non légaux ;",
    "3° Une documentation relative aux méthodes utilisées pour attester la garantie du titre et, en cas de marquage au laser, à la mise en place du protocole de sécurité informatique, qui indique :",
    "a) Les modalités d'installation et de configuration du poste informatique ;",
    "b) Les mesures de sécurisation des accès au poste de pilotage de la machine à graver au laser ;",
    "c) Les modalités de sauvegarde et d'archivage des données informatiques du journal de suivi des ouvertures de session et des modifications des comptes d'utilisateurs ;",
    "4° Les obligations en matière de marquage des ouvrages, avec les précisions suivantes :",
    "a) Les modalités de conservation de la documentation relative à la délégation de poinçons ;",
    "b) En cas de marquage au laser, la description du dessin de l'empreinte du poinçon à apposer sur l'ouvrage en or, argent et platine et le respect des profondeurs de gravure ;",
    "c) Le respect des règles de marque ;",
    "d) La tenue d'une comptabilité matières indiquant le nombre et le poids des ouvrages essayés, détaillant les ouvrages marqués par type de métal, précisant la modalité d'attestation de la garantie du titre parmi celles prévues à l'article L. 833-3 du code de commerce et recensant les ouvrages reconnus aux titres non légaux.",
], "Réécriture à droit constant : le contenu du cahier des charges est exprimé par des verbes directs et la procédure d'autorisation distingue le demandeur et les organismes vérificateurs. Les vingt-deux alinéas utiles, les quatre rubriques et toutes leurs lettres sont maintenus, avec l'intégralité des exigences techniques et comptables. Aucune réforme de fond n'est appliquée.",
    "Les renvois aux articles 275 bis C et 275 bis F de l'annexe II ont été vérifiés dans le corpus public ; le renvoi à L. 833-3 du code de commerce est maintenu sans contrôle externe. Écart préexistant conservé : le troisième alinéa confie l'approbation à la direction régionale de rattachement, tandis que le deuxième alinéa et l'article 275 bis C distinguent directeur interrégional et directeurs régionaux des quatre territoires cités. Une éventuelle harmonisation de compétence exige une coordination expresse ; elle n'est pas opérée silencieusement. Le 2° a) conserve les alliages, les apprêts pour les fabricants et le contrôle jusqu'aux produits finis.")

add(14, [
    "Les organismes de contrôle agréés doivent décrire, dans le cahier des charges prévu à l'article 275 ter B de l'annexe II au code général des impôts, les moyens et les méthodes de contrôle et d'essai qu'ils mettent en œuvre, ainsi que leurs méthodes d'attestation de la garantie du titre.",
    "L'organisme doit demander l'autorisation de procéder au marquage au laser pour attester la garantie du titre au directeur interrégional des douanes et droits indirects territorialement compétent ou, en Guadeloupe, en Guyane, à La Réunion et à Mayotte, au directeur régional des douanes et droits indirects. L'autorisation est accordée après que des organismes agréés mentionnés à l'article 275 ter G de l'annexe II au code général des impôts ont vérifié la conformité du protocole de sécurité.",
    "La direction interrégionale ou régionale compétente mentionnée au deuxième alinéa doit approuver le cahier des charges avant l'agrément de l'organisme de contrôle.",
    "Le cahier des charges mentionné au premier alinéa comprend notamment :",
    "1° Une documentation relative à l'organisme de contrôle agréé, qui fournit :",
    "a) Une description des structures juridiques et des locaux de l'organisme ;",
    "b) Une description de l'organisation et des responsabilités de la direction de l'entreprise, ainsi que de la compétence du personnel chargé de déterminer le titre des ouvrages ;",
    "2° Une documentation relative à la procédure d'analyse des ouvrages en métaux précieux, qui présente :",
    "a) Les normes utilisées pour les méthodes de dosage des métaux précieux ;",
    "b) Les moyens et les méthodes de contrôle et d'essai des ouvrages des professionnels habilités par une convention et des ouvrages des professionnels non habilités ;",
    "c) La méthode de gestion des échantillons lors des essais des ouvrages et la procédure appliquée en cas de découverte de produits non conformes au titre légal ;",
    "3° Une documentation relative aux méthodes utilisées pour attester la garantie du titre et, en cas de marquage au laser, à la mise en place du protocole de sécurité informatique, qui indique :",
    "a) Les modalités d'installation et de configuration du poste informatique ;",
    "b) Les mesures de sécurisation des accès au poste de pilotage de la machine à marquer au laser ;",
    "c) Les modalités de sauvegarde et d'archivage des données informatiques du journal de suivi des ouvertures de session et des modifications des comptes d'utilisateurs ;",
    "4° Une documentation relative aux obligations des organismes de contrôle agréés qui marquent éventuellement les ouvrages pour le compte des professionnels, précisant :",
    "a) En cas de marquage au laser, la description du dessin de l'empreinte du poinçon à apposer sur l'ouvrage en or, argent et platine et le respect des profondeurs de gravure ;",
    "b) Le respect des règles de marque ;",
    "c) La tenue d'une comptabilité matières indiquant le nombre et le poids des ouvrages essayés, détaillant les ouvrages marqués par type de métal, précisant la modalité d'attestation de la garantie du titre parmi celles prévues à l'article L. 833-3 du code de commerce et recensant les ouvrages reconnus aux titres non légaux.",
], "Réécriture à droit constant : la procédure d'autorisation et d'approbation est formulée directement ; le contenu documentaire est rédigé en propositions plus lisibles. Les dix-neuf alinéas utiles, les quatre rubriques et toutes leurs lettres sont conservés, sans retrancher les exigences d'analyse, de sécurité ou de traçabilité. Aucune réforme de fond n'est appliquée.",
    "Les renvois aux articles 275 ter B et 275 ter G de l'annexe II ont été vérifiés dans le corpus public. Le deuxième alinéa et le renvoi qui le vise au troisième restent en place. Le 1° b) de la source mentionne la « direction de l'entreprise » alors que la rubrique porte sur l'organisme de contrôle : cette variation de désignation est conservée et signalée, sans harmonisation silencieuse. Le renvoi à L. 833-3 du code de commerce reste inchangé et n'a pas été vérifié hors corpus.")

add(15, [
    "Pour obtenir l'agrément mentionné aux articles 275 bis F et 275 ter G de l'annexe II au code général des impôts, l'organisme doit déposer un dossier auprès de la direction interrégionale ou régionale compétente au sens de l'article 56 J terdecies. Ce dossier atteste de sa compétence, de son expérience et de son honorabilité. Il comprend l'engagement de respecter le cahier des charges mentionné à l'article 56 J terdecies B.",
    "L'organisme doit également justifier qu'il est à jour de ses obligations sociales et fiscales.",
    "La direction mentionnée au premier alinéa peut demander la présentation de toute pièce complémentaire nécessaire à l'instruction du dossier.",
    "Cette direction accorde l'agrément pour une durée de cinq ans.",
], "Réécriture à droit constant : la présentation du dossier, les qualités à établir et l'engagement au cahier des charges sont séparés en phrases courtes au premier alinéa. Les quatre alinéas, les obligations sociales et fiscales et la durée de cinq ans sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les articles 275 bis F et 275 ter G de l'annexe II ont été vérifiés dans le corpus public ; la durée de cinq ans reste propre à ces organismes et n'est pas étendue aux commissionnaires. La note source maintient, selon le II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), les procédures applicables à la date de présentation pour les demandes de décisions administratives individuelles antérieures à l'entrée en vigueur de cet arrêté. La casse du numéro « 56 j terdecies A » est recopiée à l'identique dans le champ number.")

add(16, [
    "Le cahier des charges mentionné aux articles 275 bis C, 275 bis F et 275 ter G de l'annexe II au code général des impôts comporte les éléments suivants :",
    "1° La définition des missions de l'organisme agréé par le directeur interrégional des douanes et droits indirects territorialement compétent ou, en Guadeloupe, en Guyane, à La Réunion et à Mayotte, par le directeur régional des douanes et droits indirects. Ces missions sont :",
    "a) Réaliser la version dématérialisée des poinçons attestant la garantie du titre ;",
    "b) Élaborer, vendre et transférer les fichiers contenant cette version dématérialisée aux professionnels habilités et aux organismes de contrôle agréés qui demandent l'autorisation d'attester la garantie du titre par le marquage au laser d'un poinçon ;",
    "c) Vérifier la mise en place et la conformité du protocole de sécurité informatique imposé aux professionnels habilités et aux organismes de contrôle agréés qui demandent l'autorisation d'attester la garantie du titre par le marquage au laser d'un poinçon ;",
    "2° Une documentation sur les conditions d'exercice des missions mentionnées au 1°, qui comporte :",
    "a) Les modalités d'élaboration de la version dématérialisée des poinçons attestant la garantie du titre, à partir des agrandissements photographiques des poinçons en acier détenus par la Monnaie de Paris et transmis par l'intermédiaire de l'administration des douanes et droits indirects ;",
    "b) Les modalités de conception et de gestion des fichiers contenant la version dématérialisée des poinçons attestant la garantie du titre par marquage au laser ;",
    "c) Les modalités de transfert des fichiers contenant la version dématérialisée des poinçons aux professionnels habilités et aux organismes de contrôle agréés qui demandent l'autorisation d'attester la garantie du titre par marquage au laser. Le transfert doit être effectué sur un support amovible au moyen d'un procédé de cryptage. L'organisme agréé fournit une clef de décryptage ;",
    "d) Une description des mesures de sécurisation du poste informatique qui garantissent l'inviolabilité des fichiers contenant la version dématérialisée des poinçons attestant la garantie du titre par le marquage au laser d'un poinçon. Cette description précise :",
    "Les modalités d'installation et de configuration du poste informatique ;",
    "Les mesures de sécurisation des accès au poste de travail. Pour les équipements dédiés à la gravure au laser, le local sécurisé de l'entreprise mentionné à l'article 275 bis C de l'annexe II au code général des impôts désigne le lieu sécurisé destiné à garantir l'inviolabilité des fichiers cryptés et de la clef de décryptage mentionnés au c du 2° ;",
    "Les modalités de sauvegarde et d'archivage des données ;",
    "e) Les modalités de vérification de la mise en place et de la conformité du protocole de sécurité informatique imposé aux professionnels habilités et aux organismes de contrôle agréés qui demandent l'autorisation d'attester la garantie du titre par le marquage au laser d'un poinçon, à savoir :",
    "La réalisation d'un audit des professionnels habilités et des organismes de contrôle agréés avant la délivrance de l'autorisation de marquage au laser, en présence d'un représentant de la direction régionale des douanes et droits indirects ;",
    "La transmission, par la direction régionale des douanes et droits indirects, du rapport d'audit signé conjointement par le représentant de cette direction et par l'organisme agréé.",
], "Réécriture à droit constant : les missions sont énoncées à l'infinitif et les obligations de cryptage, de sécurisation et d'audit sont formulées directement. Les seize alinéas, les deux rubriques, les lettres et les sous-alinéas non numérotés sont conservés ; aucune modalité technique n'est remplacée par un résumé. Aucune réforme de fond n'est appliquée.",
    "Renvois aux articles 275 bis C, 275 bis F et 275 ter G de l'annexe II vérifiés dans le corpus public. Le 1°, visé par les articles 56 J terdecies D et E, reste à sa place, ainsi que le c du 2°. Écart de désignation conservé : les deux derniers alinéas visent la direction régionale, tandis que le 1° distingue autorités interrégionale et régionales ; une harmonisation éventuelle exige un examen exprès. La note source maintient les procédures de la date de présentation pour les demandes de décisions administratives individuelles antérieures à l'entrée en vigueur de l'arrêté du 13 janvier 2020, conformément au II de son article 11 (NOR : CPAP1931008A). La casse du champ number est conservée.")

add(17, [
    "Chaque année, les services de la direction régionale des douanes et droits indirects de rattachement réalisent un audit de l'organisme agréé pour vérifier qu'il respecte les prescriptions du cahier des charges.",
    "L'organisme agréé doit conserver pendant trois ans toutes les pièces justifiant l'exercice de ses activités. Il les tient à la disposition de l'administration des douanes et droits indirects.",
], "Réécriture à droit constant : la périodicité de l'audit est placée en tête et les obligations de conservation et de mise à disposition sont attribuées à l'organisme. Les deux alinéas, la direction compétente désignée dans la source et la durée de trois ans sont conservés. Aucune réforme de fond n'est appliquée.",
    "La source ne précise pas le point de départ du délai de trois ans : aucun point de départ n'est ajouté. La désignation de la seule direction régionale de rattachement est maintenue, à coordonner expressément si les autorités du 1° de 56 J terdecies B sont harmonisées. Les notes mentionnent les modifications consécutives à l'article 4 du décret n° 2014-1048 du 15 septembre 2014 et la transition du II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A) : les demandes de décisions administratives individuelles antérieures à l'entrée en vigueur de cet arrêté restent instruites selon les procédures applicables à leur présentation. Ces indications historiques ne datent aucune réforme future. La casse de number est conservée.")

add(18, [
    "L'agrément est suspendu à titre conservatoire lorsqu'il est constaté que l'organisme agréé a manqué :",
    "1° Aux obligations résultant des articles 275 bis F et 275 ter G de l'annexe II au code général des impôts ;",
    "2° Aux dispositions législatives et réglementaires applicables à la garantie des métaux précieux.",
    "Cette suspension est prononcée à la diligence du directeur interrégional ou régional des douanes et droits indirects compétent mentionné au 1° de l'article 56 J terdecies B.",
], "Réécriture à droit constant : le lien entre le manquement constaté et la suspension conservatoire est formulé plus directement. Les quatre alinéas et les deux catégories de manquements sont maintenus ; la formule de compétence « à la diligence » est conservée pour ne pas en modifier la portée. Aucune réforme de fond n'est appliquée.",
    "Les renvois aux articles 275 bis F et 275 ter G ont été vérifiés dans l'annexe II du corpus ; le 1° de 56 J terdecies B reste en place. Les notes mentionnent l'article 4 du décret n° 2014-1048 du 15 septembre 2014 et maintiennent, selon le II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), les procédures de la date de présentation pour les demandes de décisions administratives individuelles présentées avant son entrée en vigueur. La suspension de ce régime reste distincte du pouvoir facultatif de l'article 56 J undecies. La casse de number est conservée.")

add(19, [
    "Le retrait de l'agrément intervient dans les cas suivants :",
    "1° À la demande de l'organisme agréé. L'organisme doit cesser sans délai ses activités lorsqu'il ne remplit plus les conditions prévues par les articles 275 bis F et 275 ter G de l'annexe II au code général des impôts ;",
    "2° D'office, par l'administration, lorsque l'organisme agréé a manqué :",
    "a) Aux obligations résultant des articles 275 bis F et 275 ter G de l'annexe II au code général des impôts ;",
    "b) Aux dispositions législatives et réglementaires applicables à la garantie des métaux précieux.",
    "Le directeur interrégional ou régional des douanes et droits indirects compétent mentionné au 1° de l'article 56 J terdecies B prononce le retrait de l'agrément. Ce retrait entraîne la cessation immédiate des activités exercées par l'organisme.",
], "Réécriture à droit constant : les deux voies de retrait sont présentées directement et le directeur est le sujet de la décision finale. Les six alinéas, les numéros et les lettres sont conservés, avec la cessation sans délai en cas de perte des conditions et l'effet immédiat du retrait. Aucune réforme de fond n'est appliquée.",
    "Les renvois aux articles 275 bis F et 275 ter G ont été vérifiés dans l'annexe II ; le 1° de 56 J terdecies B reste opérant. L'obligation de cesser sans délai demeure au 1°, sans déplacement d'alinéa. La note source maintient, selon le II de l'article 11 de l'arrêté du 13 janvier 2020 (NOR : CPAP1931008A), les procédures applicables à la date de présentation pour les demandes de décisions administratives individuelles antérieures à son entrée en vigueur. La casse du champ number est conservée.")

add(20, [
    "Les personnes physiques ou morales mentionnées à l'article L. 834-6 du code de commerce doivent tenir un registre de leurs achats, ventes, réceptions et livraisons de matières d'or, d'argent ou de platine ou d'ouvrages contenant ces matières. Elles doivent y inscrire les réceptions et les livraisons même lorsqu'elles ne font pas suite à un achat ou à une vente.",
    "Le registre doit être conservé sur le lieu de détention des ouvrages. Toutefois, l'établissement principal peut tenir un registre pour l'ensemble de ses magasins. Ce registre distingue alors les ouvrages détenus directement par l'établissement principal de ceux détenus par chacun des établissements secondaires dépourvus de personnalité juridique propre. Les ouvrages neufs livrés par l'établissement principal aux différents magasins doivent porter des étiquettes d'identification et être accompagnés d'une fiche de livraison ou de tout document en tenant lieu, portant la dénomination commerciale de l'établissement principal et permettant d'identifier les ouvrages. Ces documents doivent notamment préciser la référence, la désignation de l'ouvrage, la marque, le poids, la quantité et le prix hors taxes. Les magasins inscrivent leurs ventes sur des états de vente établis quotidiennement, qui indiquent au moins la référence des ouvrages et sont retournés à l'établissement principal en fin de journée. À la demande du service, les magasins doivent pouvoir communiquer à tout moment leur situation de stock par l'intermédiaire de l'établissement principal.",
    "Le I de l'article L. 102 B du livre des procédures fiscales s'applique.",
], "Réécriture à droit constant : le champ du registre est exprimé en deux phrases et la centralisation par l'établissement principal est détaillée sans déplacer les obligations hors du deuxième alinéa. Tous les mouvements, les mentions documentaires et les obligations quotidiennes sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les trois alinéas sont maintenus. La centralisation conserve la distinction des établissements secondaires sans personnalité juridique propre ; l'étiquetage et les documents concernent les ouvrages neufs livrés aux magasins. L'état de vente reste quotidien et retourné en fin de journée. Les renvois à L. 834-6 du code de commerce et au seul I de L. 102 B du livre des procédures fiscales sont conservés ; ces textes sont hors du corpus fourni et aucune durée de conservation supplémentaire n'est inventée.")

add(21, [
    "Sauf dans les cas prévus par la loi et sans préjudice des articles 56 J sexdecies à 56 J octodecies, le registre prévu à l'article 56 J quaterdecies doit indiquer les noms, prénoms et adresses des personnes qui ont vendu ou confié les matières ou ouvrages mentionnés à ce même article. Ces indications sont portées sur justification de l'identité de ces personnes.",
    "Pour permettre l'identification individuelle des matières ou ouvrages, le registre doit également indiquer leur nature, leur nombre, leur poids, leur titre, leurs dates d'entrée et de sortie et leur origine.",
], "Réécriture à droit constant : l'identification des personnes et celle des biens sont formulées en obligations distinctes, en conservant les deux alinéas. Les exceptions légales et la réserve des articles suivants restent en tête. Aucune réforme de fond n'est appliquée.",
    "Toutes les mentions sont maintenues, dont les prénoms, l'origine et les dates d'entrée et de sortie. L'article 56 J octodecies a été lu dans le corpus public : ses dispenses demeurent réservées par le premier alinéa. Les formes et adaptations prévues aux articles 56 J sexdecies et septdecies ne sont pas écartées par cette rédaction.")

add(22, [
    "L'opérateur peut choisir, pour le registre prévu à l'article 56 J quaterdecies, l'une des formes suivantes :",
    "1. Pour les ouvrages neufs :",
    "a. Un registre coté et paraphé par l'administration municipale territorialement compétente, qui peut :",
    "1° Comporter uniquement des renvois aux documents comptables, notamment aux factures et bordereaux d'expédition, relatifs aux matières ou ouvrages mentionnés à l'article 56 J quaterdecies. Dans ce cas, les indications prévues à l'article 56 J quindecies doivent y figurer. Toutefois, le poids et le titre des ouvrages peuvent ne pas être indiqués si les ouvrages sont identifiables par leur numéro de série individuel ou par leur référence commerciale mentionnée dans un catalogue ou dans tout document de nature comptable ;",
    "2° Renvoyer à des fiches de stock et d'inventaire numérotées en continu, appuyées de tout document probant comportant la désignation complète et détaillée des ouvrages et des matières confiées prévue à l'article 56 J quindecies ;",
    "3° Comporter une inscription globale pour les ouvrages strictement identiques, notamment quant à leur référence et à leur poids, à condition que la référence renvoie à une facture. La facture peut omettre le titre et le poids des objets si ceux-ci restent identifiables par leur numéro de série individuel ou par leur référence commerciale mentionnée dans un catalogue ou dans tout document de nature comptable ;",
    "b. Ou une comptabilité conforme, selon le cas, aux articles L. 123-12 à L. 123-23 du code de commerce ou aux spécifications du 3° du I de l'article 286 du code général des impôts, à condition que les documents prévus à cet article soient accompagnés de fiches de stock ou d'un inventaire permanent ;",
    "c. Ou un registre établi au moyen d'un logiciel qui assure une gestion permanente des stocks par référence de produits, permet d'identifier les ouvrages et offre toutes garanties en matière de preuve. Le logiciel doit comporter les indications prévues à l'article 56 J quindecies. Toutefois, le poids et le titre des ouvrages peuvent ne pas être indiqués si les ouvrages sont identifiables par leur numéro de série individuel ou par leur référence commerciale mentionnée dans un catalogue ou dans tout document de nature comptable.",
    "L'opérateur doit pouvoir prouver la fiabilité du système informatique utilisé et la chronologie des écritures présentées sous forme de listes. Les feuillets informatiques doivent être identifiés, numérotés et datés sans possibilité de modification, afin de garantir la chronologie des opérations enregistrées. Toute modification doit être justifiée par la création d'un nouvel enregistrement informatique qui en indique le motif.",
    "L'opérateur doit pouvoir éditer quotidiennement les informations relatives aux seuls ouvrages en métaux précieux. Il doit pouvoir présenter les enregistrements informatiques ou les listages à toute réquisition du service, dans les conditions prévues à l'article 56 J quaterdecies.",
    "2. Pour les ouvrages d'occasion :",
    "a. Un registre coté et paraphé par l'administration municipale territorialement compétente ;",
    "b. Ou le registre prévu à l'article 321-7 du code pénal. Les ouvrages contenant des métaux précieux doivent y être inscrits individuellement, quelle que soit leur valeur, avec une encre d'une couleur différente de celle utilisée pour les autres objets ;",
    "c. Ou le registre établi au moyen du logiciel de gestion permanente des stocks prévu au c du 1, à condition que les enregistrements informatiques créés pour les ouvrages d'occasion ne puissent être modifiés que par la création d'un nouvel enregistrement indiquant le motif de la modification. Le répertoire contenant ces informations doit être spécifique et comprendre un système d'identification des pages par chiffre de contrôle, contenant un algorithme ou un système fondé notamment sur la date de l'opération, reporté en fin et en tête des pages imprimées quotidiennement.",
    "L'opérateur doit pouvoir éditer quotidiennement les informations relatives aux seuls ouvrages en métaux précieux.",
], "Réécriture à droit constant : les formes de registre et les conditions de chaque option sont formulées plus directement ; les phrases sur les logiciels et la correction des écritures sont raccourcies. Les quinze alinéas, les subdivisions 1. et 2., a., b., c. et 1° à 3° sont maintenus avec toutes les alternatives, exceptions et garanties techniques. Aucune réforme de fond n'est appliquée.",
    "Le 3° du I de l'article 286 a été lu dans impots.json. Sa note annonce une abrogation à compter du 1er janvier 2027 avec maintien de certaines dispositions jusqu'à leur reprise par les mesures réglementaires visées à L. 215-26 du code des impositions sur les biens et services ; le renvoi actuel est conservé et sa coordination future nécessite un contrôle exprès. Les renvois au code de commerce et au code pénal, hors corpus, restent inchangés. L'ambiguïté préexistante de « y figurer » au 1. a. 1° est maintenue sans décider silencieusement si la mention vise le registre ou les documents auxquels il renvoie. La formule technique du chiffre de contrôle au 2. c. est conservée sans substitution d'un dispositif nouveau. L'exception de poids et de titre reste limitée aux cas prévus pour les ouvrages neufs ; aucune dispense générale n'est étendue aux ouvrages d'occasion.")

add(23, [
    "Les ouvrages neufs et d'occasion confiés à quelque titre que ce soit, notamment pour réparation, peuvent faire l'objet d'une inscription globale des entrées et des sorties en fin de journée sur le registre prévu à l'article 56 J quaterdecies. Cette faculté est subordonnée à la possibilité de justifier leur situation à tout moment par tout document probant, tel qu'une étiquette, un sachet individualisé ou un carnet à souche, indiquant le nom du client, la nature de l'objet et la date du dépôt.",
    "Pour ces mêmes ouvrages, il est également permis de présenter des documents comptables tenant lieu de registre, tels que les livres comptables, le livre d'inventaire permanent, les fiches de stocks et d'inventaire intégrées dans la comptabilité ou la comptabilité matières assortie de factures, de bons de livraison ou de bons, bordereaux ou fiches de confiés. Ces documents doivent alors comporter les indications prévues à l'article 56 J quindecies.",
    "Pour les ouvrages confiés pour réparation, le registre prévu à l'article 56 J quaterdecies peut être remplacé par un contrat de dépôt ou par des fiches « réparation-facture-horlogerie ». Le contrat et les fiches doivent indiquer le nom et l'adresse du déposant et du dépositaire, la date et le numéro du contrat ou de la fiche dans une série continue, ainsi que la désignation complète et détaillée des objets confiés, en particulier la nature, le poids, le métal et le titre des ouvrages. Le registre peut être établi au moyen d'un logiciel comportant la désignation complète et détaillée des ouvrages et des matières confiées prévue à l'article 56 J quindecies.",
], "Réécriture à droit constant : l'inscription globale et sa condition de justification sont séparées en deux phrases ; les documents tenant lieu de registre et les supports propres à la réparation sont explicités. Les trois alinéas, la liste complète des justificatifs et toutes les mentions d'identification sont conservés. Aucune réforme de fond n'est appliquée.",
    "L'inscription globale reste effectuée en fin de journée et subordonnée à une justification possible à tout moment. Le contrat de dépôt et les fiches restent réservés aux ouvrages confiés pour réparation, tandis que les deux premiers alinéas couvrent les ouvrages confiés à quelque titre que ce soit. La série continue, les deux parties au dépôt, le poids, le métal, le titre et les renvois à 56 J quaterdecies et quindecies sont conservés. Aucun délai de conservation ni remplacement obligatoire par un logiciel n'est ajouté.")


assert set(drafts) == set(range(len(source)))
answer = []
for index, article in enumerate(source):
    item = {key: article[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[index])
    item['status'] = 'rewrite_draft'
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'{len(answer)} articles rédigés dans answer.json')
