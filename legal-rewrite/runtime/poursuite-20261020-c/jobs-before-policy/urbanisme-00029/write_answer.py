import json
from html import escape
from pathlib import Path

drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + escape(p, quote=False) + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
    }


add('L328-4', [
    "I. – Pour l'exercice de la mission mentionnée à la seconde phrase du premier alinéa de l'article L. 328-3, le président du conseil d'administration de Paris La Défense exerce, à la place des maires des communes concernées et sur le territoire mentionné au même premier alinéa, les pouvoirs suivants :",
    "1° Par dérogation au 2° de l'article L. 2213-2 du code général des collectivités territoriales, le pouvoir de réglementer l'arrêt ou le stationnement des véhicules, ou de certaines catégories de véhicules, ainsi que la desserte des immeubles riverains. Les agents de l'établissement public Paris La Défense agréés à cette fin par le procureur de la République peuvent constater par procès-verbal les contraventions aux dispositions relatives à l'arrêt ou au stationnement des véhicules. Cette compétence ne porte pas atteinte à la compétence générale des officiers et agents de police judiciaire ;",
    "2° Par dérogation à l'article L. 2212-2 du même code, le pouvoir de réglementer la propreté des voies et espaces publics. Les agents de l'établissement public Paris La Défense habilités et assermentés dans les conditions prévues à l'article L. 1312-1 du code de la santé publique peuvent constater par procès-verbal les contraventions aux dispositions des règlements sanitaires relatives à la propreté des voies et espaces publics.",
    "Le président du conseil d'administration mentionné au premier alinéa du présent I transmet pour information aux maires des communes concernées, dans les meilleurs délais, tout arrêté de police qu'il prend dans les cas prévus aux 1° et 2° du même I.",
    "II. – Dans les six mois suivant la date du transfert au président du conseil d'administration des pouvoirs mentionnés aux 1° et 2° du I, un ou plusieurs maires peuvent s'opposer au transfert de chacun de ces pouvoirs. Ils notifient leur opposition au président. Le transfert prend alors fin pour les communes dont les maires ont notifié cette opposition.",
    "Lorsqu'un ou plusieurs maires des communes concernées se sont opposés au transfert de leurs pouvoirs de police, le président du conseil d'administration peut, dans chacun des domaines mentionnés aux mêmes 1° et 2°, renoncer au transfert de plein droit des pouvoirs de police des maires qui n'ont pas notifié leur opposition en application du premier alinéa du présent II. Il notifie sa renonciation à chacun de ces maires dans les six mois suivant la réception de la première notification d'opposition. Le transfert des pouvoirs de police prend alors fin à compter de cette notification de renonciation.",
],
    "Réécriture à droit constant : les deux pouvoirs de police, les compétences de constatation et les deux procédures mettant fin au transfert sont formulés séparément avec leurs titulaires. Les six alinéas et les subdivisions I, II, 1° et 2° sont conservés ; aucune réforme de fond n'est appliquée à ce régime spécial.",
    "Conserver les renvois à la seconde phrase du premier alinéa de L. 328-3, au 2° de L. 2213-2 et à L. 2212-2 du CGCT, ainsi qu'à L. 1312-1 du CSP. Les deux délais de six mois ont des points de départ distincts : transfert des pouvoirs et réception de la première opposition. La renonciation du président prend effet à sa notification ; agrément du procureur et habilitation avec assermentation demeurent distincts.")

add('L328-5', [
    "Paris La Défense peut exercer les missions définies aux articles L. 328-2 et L. 328-3 hors des périmètres mentionnés à ces articles, à condition que ses interventions s'inscrivent dans la continuité d'opérations en cours dans ces périmètres.",
    "Le ministre chargé de l'urbanisme autorise ces interventions après avis conforme de l'établissement public territorial et du conseil municipal de chacune des communes concernées par l'intervention hors périmètre.",
    "Lorsque Paris La Défense intervient dans les conditions du premier alinéa, un représentant de l'établissement public territorial et un représentant de chaque commune concernée qui n'est pas membre de Paris La Défense assistent, avec voix consultative, aux réunions du conseil d'administration chaque fois que celui-ci examine une décision relative à cette intervention.",
],
    "Réécriture à droit constant : la condition de continuité, l'autorité chargée de l'autorisation et la participation consultative aux décisions sont exprimées directement. Les trois alinéas sont maintenus ; aucune extension de compétence issue de la réforme n'est introduite.",
    "L'avis reste conforme, et non simplement consultatif. Le deuxième alinéa demeure la cible de L. 328-16, qui prévoit le délai de trois mois et l'avis réputé favorable. La participation des représentants reste limitée aux décisions relatives à l'intervention hors périmètre.")

add('L328-6', [
    "Paris La Défense peut réaliser les opérations suivantes, à condition que leur objet concoure directement à l'accomplissement de ses missions et sous réserve des compétences attribuées aux autres personnes publiques :",
    "1° Pour exercer la mission mentionnée au 2° de l'article L. 328-3, créer des filiales et acquérir ou céder des participations dans des sociétés publiques locales ;",
    "2° Pour exercer la mission mentionnée à l'article L. 328-2, acquérir ou céder des participations dans les sociétés publiques locales d'aménagement définies à l'article L. 327-1.",
    "Au moins un des représentants, au conseil d'administration de Paris La Défense, des communes sur le territoire desquelles une telle filiale ou société exerce son activité est membre du conseil d'administration ou de surveillance de cette filiale ou société.",
    "Pour l'application des dispositions régissant les sociétés mentionnées aux 1° et 2° du présent article, Paris La Défense est assimilé à un groupement de collectivités territoriales au sens de ces dispositions.",
],
    "Réécriture à droit constant : chaque catégorie d'opérations est rapprochée de la mission qui l'autorise ; la représentation communale et la règle d'assimilation sont explicitées. Les 1° et 2° conservent leur portée ; aucune réforme de fond ne concerne ces participations.",
    "Le pouvoir de créer des filiales reste au seul 1° ; le 2° ne prévoit que l'acquisition ou la cession de participations. Conserver la condition de concours direct aux missions, la réserve des compétences d'autres personnes publiques et la présence d'au moins un représentant des communes territorialement concernées.")

add('L328-7', [
    "Dans les cas et selon les conditions prévus par le présent code, Paris La Défense peut recourir à l'expropriation et exercer les droits de préemption et de priorité que ce code définit.",
    "Paris La Défense peut également constituer les réserves foncières définies par le présent code, dans les conditions qu'il prévoit.",
],
    "Réécriture à droit constant : les facultés d'intervention foncière sont rattachées expressément aux cas et conditions du code, avec un sujet explicite dans chacun des deux alinéas. Aucune réforme de fond ni procédure nouvelle n'est ajoutée.",
    "Les pouvoirs d'expropriation, de préemption, de priorité et de constitution de réserves foncières restent soumis au présent code ; aucune dérogation autonome n'est créée.")

add('L328-8', [
    "I. – Un conseil d'administration administre Paris La Défense. Les représentants du département des Hauts-de-Seine y sont majoritaires. Les communes de Courbevoie, Nanterre, Paris et Puteaux, la région d'Ile-de-France et la métropole du Grand Paris y sont également représentées.",
    "L'Etat nomme également au conseil d'administration des personnalités qualifiées pour leurs compétences en matière d'aménagement et de développement économique.",
    "Des représentants du personnel de l'établissement peuvent participer, avec voix consultative, aux réunions du conseil d'administration.",
    "Lorsque Paris La Défense intervient sur le territoire de La Garenne-Colombes dans le cadre des missions mentionnées à l'article L. 328-2, un représentant de cette commune assiste au conseil d'administration avec voix consultative chaque fois que celui-ci examine une décision relative à cette intervention.",
    "II. – Chaque représentant au conseil d'administration d'une collectivité territoriale ou d'un groupement mentionné au premier alinéa du I dispose d'au moins un droit de vote lorsque cette collectivité ou ce groupement a signé la convention mentionnée à l'article L. 328-10. Si cette collectivité ou ce groupement n'a pas signé la convention, ses représentants disposent d'une voix consultative.",
    "Les droits de vote des représentants des collectivités territoriales et de leurs groupements mentionnés au premier alinéa du I, dont la collectivité ou le groupement a signé la convention mentionnée à l'article L. 328-10, sont majorés en fonction de la part de la contribution de ces collectivités et groupements dans l'ensemble des contributions mentionnées à cet article. Cette majoration est définie par la convention ou, à défaut, dans les conditions fixées par décret en Conseil d'Etat.",
    "Toutefois, la majoration prévue à l'alinéa précédent ne peut retirer aux représentants du département des Hauts-de-Seine la majorité des droits de vote, à condition que ce département apporte au moins la moitié des contributions prévues par la convention mentionnée à l'article L. 328-10.",
    "Si cette convention n'a pas été notifiée au ministre chargé de l'urbanisme, tous les représentants au conseil d'administration des collectivités territoriales et de leurs groupements mentionnés au premier alinéa du I disposent d'un droit de vote. Aucune majoration ne peut alors leur être accordée en application du deuxième alinéa du présent II.",
    "III. – Le conseil d'administration élit son président parmi ses membres représentant les collectivités territoriales et leurs groupements mentionnés au premier alinéa du I.",
    "Le conseil d'administration règle les affaires de l'établissement par ses délibérations. Il approuve notamment le document d'engagement mentionné à l'article L. 328-12. Il nomme le directeur général et met fin à ses fonctions dans les conditions précisées à l'article L. 328-13.",
    "Le conseil d'administration désigne un comité d'audit et des finances composé de cinq membres, dont au moins deux personnalités qualifiées.",
    "IV. – Le préfet de la région d'Ile-de-France assiste de droit aux séances du conseil d'administration. Les procès-verbaux et les délibérations lui sont adressés. Le préfet des Hauts-de-Seine le supplée lorsque cela est nécessaire.",
],
    "Réécriture à droit constant : les règles de composition, de vote et de compétence du conseil sont décomposées en phrases plus courtes, sans modifier les douze alinéas ni les subdivisions I à IV. Les conditions de majorité et le régime applicable sans notification restent distincts. Aucune réforme de fond n'est introduite.",
    "Incohérence préexistante conservée au deuxième alinéa du III : le document d'engagement est renvoyé à L. 328-12, alors que L. 328-11 le définit et que L. 328-12 en organise la surveillance. Une éventuelle correction de renvoi doit être explicite. Conserver cinq membres, au moins deux personnalités qualifiées et la condition d'au moins la moitié des contributions pour garantir la majorité départementale des voix. La note source situe l'entrée en vigueur à l'exercice budgétaire et comptable 2023, conformément à l'article 4 de l'ordonnance n° 2022-1421 du 10 novembre 2022 ; ce n'est pas une date de réforme future.")

add('L328-9', [
    "Un conseil de développement représente les personnes physiques et morales qui utilisent régulièrement les équipements et espaces publics gérés par l'établissement. Il est consulté sur les orientations retenues par l'établissement public pour exercer ses compétences, selon une périodicité fixée par le conseil d'administration et au moins une fois par an.",
],
    "Réécriture à droit constant : la représentation des usagers est séparée, dans le même alinéa, de l'objet et de la fréquence de la consultation. Aucune réforme de fond ne modifie cette instance.",
    "Le conseil d'administration fixe la périodicité, sous réserve d'une consultation au moins annuelle. La représentation demeure celle des usagers réguliers, personnes physiques comme personnes morales, des équipements et espaces publics gérés par l'établissement.")

add('L328-10', [
    "I. – Les collectivités territoriales et leurs groupements mentionnés au premier alinéa du I de l'article L. 328-8 peuvent contribuer aux charges et aux dépenses d'investissement liées à la mission mentionnée à la seconde phrase du premier alinéa de l'article L. 328-3.",
    "Une convention conclue pour dix ans entre ces collectivités territoriales et leurs groupements, puis notifiée au ministre chargé de l'urbanisme, établit ces contributions. Les contributions ainsi établies sont obligatoires.",
    "Les engagements pris dans cette convention garantissent le financement du document d'engagement et du programme pluriannuel d'investissement prévus à l'article L. 328-11. Ils peuvent être révisés pour garantir ce financement.",
    "La convention peut fixer la majoration des droits de vote prévue au II de l'article L. 328-8.",
    "II. – Si la convention n'a pas été notifiée au ministre chargé de l'urbanisme, les charges et les dépenses d'investissement résultant, pour les collectivités territoriales et leurs groupements, de l'exercice de la mission mentionnée à la seconde phrase du premier alinéa de l'article L. 328-3 sont réparties entre le département des Hauts-de-Seine et les communes de Courbevoie et Puteaux. Un décret en Conseil d'Etat fixe les conditions de cette répartition. Ces contributions sont obligatoires.",
],
    "Réécriture à droit constant : le mécanisme conventionnel et la répartition supplétive des contributions sont exposés avec leurs conditions et leurs débiteurs. Les cinq alinéas et les subdivisions I et II sont conservés ; aucune nouvelle ressource ni réforme de fond n'est créée.",
    "La convention dure dix ans ; sa notification commande le régime supplétif du II et se coordonne avec les votes prévus à L. 328-8. Le caractère obligatoire concerne tant les contributions conventionnelles que celles du II. Conserver le renvoi précis à la seconde phrase du premier alinéa de L. 328-3 ; aucune vente d'actif n'est assimilée à un financement permanent.")

add('L328-11', [
    "Paris La Défense élabore et approuve un document d'engagement. Ce document fixe les engagements de l'établissement public pour dix ans, notamment les investissements nécessaires à la mise aux normes. Il définit aussi les objectifs, la stratégie et les moyens que l'établissement, les collectivités territoriales et leurs groupements mettront en œuvre pour les atteindre.",
    "Ce document est élaboré en tenant compte des charges et contributions définies à l'article L. 328-10. Il prend en compte les priorités énoncées dans les documents d'urbanisme et les objectifs de réalisation de logements précisés par le programme local de l'habitat.",
    "Au terme de cinq ans, un bilan de la réalisation des opérations prévues par le document d'engagement est établi. Ce bilan est accompagné d'une nouvelle prévision portant sur cinq années supplémentaires, qui s'ajoutent aux cinq années restant à courir au titre du document.",
    "Le document d'engagement fixe une trajectoire financière pluriannuelle présentée de manière sincère. A son horizon et sur toute sa durée, cette trajectoire équilibre :",
    "1° L'ensemble des opérations d'aménagement, dont les prévisions à fin d'affaires sont annexées au document d'engagement ;",
    "2° Le plan de financement prévisionnel de l'établissement. Ce plan comprend, d'une part, la somme des ressources budgétaires, y compris les produits d'exploitation, les cessions d'actifs, les contributions des collectivités territoriales et de leurs groupements mentionnés au premier alinéa du I de l'article L. 328-8 et les ressources issues des emprunts. Il comprend, d'autre part, la somme des dépenses budgétaires, y compris les charges d'exploitation, les investissements conformes au programme pluriannuel d'investissement et les charges liées aux emprunts et à leur remboursement.",
    "Un compte de résultat prévisionnel accompagne la trajectoire financière pluriannuelle. Il est établi au même horizon, selon les normes de la comptabilité générale.",
    "Les orientations budgétaires prévues à l'article L. 2312-1 du code général des collectivités territoriales sont présentées dans les dix semaines précédant l'examen du budget. La trajectoire financière pluriannuelle est actualisée chaque année à cette occasion. Le rapport soumis au conseil d'administration comporte une proposition d'actualisation.",
    "Le conseil d'administration débat de ce rapport dans les conditions fixées par le règlement intérieur. Une délibération spécifique prend acte de ce débat. Cette délibération et le rapport sont transmis au représentant de l'Etat chargé du contrôle de légalité mentionné à l'article L. 328-14.",
],
    "Réécriture à droit constant : les engagements, le bilan à cinq ans, les deux composantes de l'équilibre financier et la procédure budgétaire annuelle sont explicités par des phrases courtes. Les neuf alinéas et les 1° et 2° sont maintenus ; aucune réforme de fond ni hypothèse de recettes n'est ajoutée.",
    "Conserver l'engagement à dix ans, le bilan après cinq ans, la projection complémentaire de cinq ans et les dix semaines précédant l'examen du budget. Le 2° conserve toutes les ressources et dépenses, notamment cessions d'actifs, emprunts et remboursements, sans leur donner une affectation nouvelle. La note source prévoit l'application à partir de l'exercice budgétaire et comptable 2023 (article 4 de l'ordonnance n° 2022-1421 du 10 novembre 2022). Le renvoi discordant de L. 328-8 au document d'engagement de L. 328-12 est signalé dans la notice de L. 328-8.")

add('L328-12', [
    "Le préfet de la région d'Ile-de-France veille à ce que le document d'engagement prévu à l'article L. 328-11 soit appliqué.",
    "Dans les quinze jours suivant la réception d'une décision du conseil d'administration de Paris La Défense, le préfet peut en suspendre le caractère exécutoire et demander une seconde délibération si cette décision porte manifestement atteinte aux intérêts nationaux, notamment aux intérêts patrimoniaux de l'Etat, ou au bon fonctionnement des services publics. La nouvelle délibération est adoptée à la majorité des deux tiers des suffrages exprimés, comprenant les représentants d'au moins deux des collectivités territoriales et de leurs groupements mentionnés au premier alinéa du I de l'article L. 328-8.",
],
    "Réécriture à droit constant : le point de départ du délai de contrôle et les motifs de suspension sont placés au début de la règle ; la seconde délibération reste soumise à sa majorité particulière. Les deux alinéas sont maintenus ; aucune réforme de fond n'est apportée.",
    "Le délai de quinze jours court à compter de la réception des décisions. Préserver l'atteinte manifeste, les deux tiers des suffrages exprimés et la représentation d'au moins deux collectivités ou groupements visés à L. 328-8, sans remplacer cette condition par un nombre de voix. Le renvoi à L. 328-11 pour le document est cohérent ici, contrairement à celui relevé dans L. 328-8.")

add('L328-13', [
    "Le directeur général administre l'établissement. Dans les conditions fixées par décret en Conseil d'Etat, il prépare les décisions du conseil d'administration et les exécute.",
    "Sur proposition du président et après avis motivé du préfet de région, le conseil d'administration nomme le directeur général pour un mandat de cinq ans. Ce mandat est renouvelable et révocable.",
],
    "Réécriture à droit constant : les missions du directeur et l'ordre des interventions dans sa nomination sont formulés directement ; la durée, le renouvellement et la révocabilité sont exprimés dans le même alinéa. Aucune réforme de fond n'est ajoutée.",
    "Maintenir le mandat de cinq ans, renouvelable et révocable, la proposition du président et l'avis motivé du préfet de région. L. 328-8 renvoie à cet article pour la nomination et la cessation des fonctions ; aucun régime autonome de révocation n'est créé.")

add('L328-14', [
    "I. – Pour sa gestion financière et comptable, l'établissement applique les règles des entreprises de commerce.",
    "II. – Les dispositions financières, budgétaires et comptables du code général des collectivités territoriales s'appliquent à l'établissement, sous les conditions et réserves suivantes :",
    "1° Le chapitre II du titre Ier du livre VI de la première partie du code général des collectivités territoriales s'applique, à l'exception des articles L. 1612-1, L. 1612-3, L. 1612-4, L. 1612-6, L. 1612-7, L. 1612-10 à L. 1612-14 et L. 1612-19-1 ;",
    "2° Le budget de l'établissement comprend un compte de résultat et un tableau de financement, tous deux prévisionnels à fin d'exercice. Le compte de résultat prévisionnel est présenté selon les modalités définies à l'article L. 123-12 du code de commerce pour le compte de résultat. Le budget a un caractère évaluatif ;",
    "3° Le budget est adopté au plus tard le 15 avril de l'exercice concerné. Les délibérations qui le modifient peuvent être prises jusqu'à la fin de cet exercice. Le budget et les décisions modificatives sont transmis au représentant de l'Etat dans les quinze jours suivant leur adoption ;",
    "4° Si le budget n'est pas adopté avant le 1er janvier de l'exercice concerné, le directeur général peut, jusqu'à son adoption, mettre les recettes en recouvrement et exécuter les dépenses, dans les limites des recettes et des dépenses inscrites au budget de l'année précédente ;",
    "5° L'établissement suit l'exécution budgétaire et comptable au cours de l'année. Si ce suivi révèle un bouleversement significatif de l'économie générale du budget, un projet de décision modificative est présenté au conseil d'administration dans un délai d'un mois ;",
    "6° Pour l'application des articles L. 1612-2, L. 1612-5 et L. 1612-8 du code général des collectivités territoriales, les crédits ont un caractère limitatif lorsque le représentant de l'Etat règle le budget et le rend exécutoire ;",
    "7° Pour l'application de l'article L. 1612-5 du code général des collectivités territoriales, le budget n'est pas considéré comme voté en équilibre réel si, bien que ses recettes et ses dépenses aient été évaluées de façon sincère, il s'écarte significativement des prévisions de la trajectoire financière pluriannuelle pour l'année concernée. Cette trajectoire est établie conformément à l'article L. 328-11 ;",
    "8° Lorsque la chambre régionale des comptes a été saisie en application du 6°, le représentant de l'Etat lui transmet les délibérations qui modifient le budget de l'établissement pour le même exercice ;",
    "9° Le conseil d'administration adopte les comptes au plus tard le 30 juin de l'année suivant l'exercice. Les comptes sont transmis au représentant de l'Etat dans les quinze jours suivant leur adoption. A défaut, le représentant de l'Etat saisit la chambre régionale des comptes du plus proche budget voté par l'établissement, selon la procédure prévue à l'article L. 1612-5 du code général des collectivités territoriales ;",
    "10° Si les comptes de l'établissement, après vérification de leur sincérité, révèlent un écart significatif entre le budget exécuté et la trajectoire financière pluriannuelle établie conformément à l'article L. 328-11, la chambre régionale des comptes, saisie par le représentant de l'Etat, propose à l'établissement les mesures nécessaires à son rétablissement financier. Elle formule ces propositions dans le mois suivant sa saisine. Dans ce cas, le représentant de l'Etat transmet à la chambre le budget de l'exercice suivant ;",
    "11° Un commissaire aux comptes certifie les comptes de l'établissement. Il est désigné par délibération du conseil d'administration.",
    "III. – Le préfet du département des Hauts-de-Seine contrôle la légalité des actes et délibérations de l'établissement public dans les conditions prévues par le code général des collectivités territoriales. Il exerce aussi leur contrôle budgétaire dans les conditions prévues au II.",
],
    "Réécriture à droit constant : les onze règles budgétaires sont conservées dans leur ordre, avec des sujets explicites pour les transmissions et saisines et des phrases plus courtes. Les subdivisions I à III et chaque alinéa cible sont maintenus. Aucun changement de fond n'est apporté aux règles comptables ou aux contrôles.",
    "Vérifier toute coordination future avec le CGCT sans supprimer les exclusions du 1° : L. 1612-1, -3, -4, -6, -7, -10 à -14 et -19-1. Sont conservés le 15 avril, le 1er janvier, le 30 juin, les transmissions à quinze jours et les délais d'un mois des 5° et 10°. Le renvoi du 8° au 6° demeure celui de la source : le 6° mentionne plusieurs procédures du CGCT sans décrire lui-même une saisine ; cette articulation mérite contrôle, sans correction implicite. Les notes sources font entrer ces règles en vigueur à compter de l'exercice budgétaire et comptable 2023, en application de l'article 4 de l'ordonnance n° 2022-1421 du 10 novembre 2022.")

add('L328-15', [
    "L'établissement dispose des ressources suivantes :",
    "1° Les contributions de ses membres prévues à l'article L. 328-10 ;",
    "2° Les dotations, subventions, avances, fonds de concours ou participations que peuvent apporter l'Etat, l'Union européenne, les établissements publics, les collectivités territoriales ou leurs groupements ;",
    "3° Les produits des emprunts qu'il contracte ;",
    "4° La rémunération de ses prestations de services ;",
    "5° Les produits tirés de la gestion des biens entrés dans son patrimoine ;",
    "6° Les produits de la cession de biens et de droits mobiliers et immobiliers ;",
    "7° Les revenus des biens et des droits mobiliers et immobiliers ;",
    "8° Les dons et les legs ;",
    "9° Toute autre ressource autorisée par les lois et règlements.",
],
    "Réécriture à droit constant : le catalogue des ressources est rattaché directement à l'établissement et les apports extérieurs sont formulés avec leurs auteurs. Les neuf catégories et leur numérotation sont conservées, sans ajout de ressource ni réforme de fond.",
    "Maintenir séparément les produits de gestion, de cession et les revenus des biens, même s'ils peuvent se recouper dans la présentation comptable. Les contributions restent renvoyées à L. 328-10. Aucune recette ou économie nationale n'est chiffrée, et les cessions ne reçoivent aucune affectation nouvelle.")

add('L328-16', [
    "Pour l'application du premier alinéa des articles L. 328-2 et L. 328-3, les collectivités territoriales consultées sont réputées avoir rendu un avis favorable si elles ne se prononcent pas dans un délai de trois mois. Pour l'application du deuxième alinéa de l'article L. 328-5, l'établissement public territorial et le conseil municipal des communes concernées sont réputés avoir rendu un avis favorable s'ils ne se prononcent pas dans les trois mois suivant la réception, par l'établissement public ou par la commune, du projet d'autorisation du ministre chargé de l'urbanisme.",
],
    "Réécriture à droit constant : les deux règles d'avis tacitement favorable sont énoncées avec les personnes consultées et, pour la seconde, le point de départ prévu par la source. L'alinéa et les renvois ciblés sont maintenus ; aucune réforme de fond des délais n'est introduite.",
    "Les deux délais sont de trois mois. Le texte ne précise le point de départ par réception du projet ministériel que pour les avis du deuxième alinéa de L. 328-5 ; ne pas l'étendre tacitement à la première règle. Cet avis reste soumis au caractère conforme imposé par L. 328-5.")

add('L328-17', [
    "Les conditions d'application du présent chapitre sont fixées par un décret en Conseil d'Etat.",
],
    "Réécriture à droit constant de l'alinéa unique : la règle d'application est placée en tête et la forme du texte réglementaire est maintenue. Aucune réforme de fond n'est prévue pour ce renvoi.",
    "Le renvoi porte sur l'ensemble du présent chapitre et requiert toujours un décret en Conseil d'Etat.")

add('L329-1', [
    "Les organismes de foncier solidaire ont pour objet principal de gérer des terrains ou des biens immobiliers dont ils sont propriétaires, après les avoir acquis s'il y a lieu. Cette gestion vise à réaliser des logements destinés, sous conditions de plafond, à des personnes aux ressources modestes, ainsi que des équipements collectifs, conformément aux objectifs de l'article L. 301-1 du code de la construction et de l'habitation. Ces réalisations peuvent comprendre des travaux de réhabilitation ou de rénovation. Cet objet principal peut représenter tout ou partie de leur activité.",
    "A titre subsidiaire, ces organismes peuvent réaliser ou faire réaliser des locaux à usage commercial ou professionnel pour favoriser la mixité fonctionnelle. Ils interviennent alors sur des terrains préalablement acquis ou gérés au titre de leur activité principale.",
    "Le représentant de l'Etat dans la région agrée les organismes de foncier solidaire après avis de l'instance prévue à l'article L. 364-1 du même code. Les organismes sans but lucratif et les organismes mentionnés aux articles L. 411-2 et L. 481-1 de ce code peuvent être agréés pour exercer cette activité à titre principal ou accessoire.",
    "L'organisme de foncier solidaire conserve la propriété des terrains. Dans le cadre d'un bail de longue durée, il consent au preneur des droits réels pour permettre la location ou l'accession à la propriété des logements à usage d'habitation principale ou à usage mixte professionnel et d'habitation principale, ou des locaux à usage commercial ou professionnel. Le bail peut, s'il y a lieu, imposer de construire ou de réhabiliter, de rénover ou de gérer des constructions existantes. Les droits sont consentis sous conditions de prix de cession et, le cas échéant, de plafonds de ressources et de loyers.",
    "L'organisme de foncier solidaire peut bénéficier de la décote définie à l'article L. 3211-7 du code général de la propriété des personnes publiques.",
    "Les conditions d'application du présent article sont fixées par décret en Conseil d'Etat.",
],
    "Réécriture à droit constant : la finalité principale et l'activité subsidiaire sont distinguées ; l'agrément, la propriété du foncier et le contenu du bail sont explicités dans les six alinéas d'origine. Les clauses de prix et de plafonds sont maintenues. Aucune réforme de fond n'est appliquée à l'accession sociale ni au régime de ces organismes.",
    "Conserver les champs distincts : logement sous plafond pour l'activité principale ; locaux commerciaux ou professionnels seulement à titre subsidiaire sur les terrains préalablement acquis ou gérés au titre de l'activité principale. Le bail reste de longue durée, sans durée chiffrée nouvelle ; l'organisme reste propriétaire des terrains. Le double point final de la source est régularisé sans effet normatif. Le projet de rénovation locative de vingt-quatre mois ne modifie pas ce régime foncier : il appellerait notamment une disposition dans la loi n° 89-462 du 6 juillet 1989, en coordination avec le CCH, conformément à coordination.json.")

add('L32-10-1', [
    "I. – L'Etat ou l'un de ses établissements publics mentionnés aux sections 2 et 3 du chapitre Ier du présent titre peut créer une société d'économie mixte d'aménagement à opération unique avec une ou plusieurs collectivités territoriales ou un groupement de collectivités territoriales compétent et avec au moins un actionnaire opérateur économique. Cet actionnaire est sélectionné après mise en concurrence dans les conditions définies à l'article L. 1541-2 du code général des collectivités territoriales.",
    "II. – La société d'économie mixte d'aménagement à opération unique est constituée pour une durée limitée, exclusivement pour conclure et exécuter un contrat avec l'Etat ou l'un de ses établissements publics mentionnés au I et la collectivité territoriale ou le groupement de collectivités territoriales compétent. Ce contrat a pour objet unique la réalisation d'une opération de construction, de développement du logement ou d'aménagement.",
    "L'objet unique du contrat ne peut être modifié pendant sa durée.",
    "III. – La société d'économie mixte d'aménagement à opération unique est une société anonyme régie par le livre II du code de commerce et par le titre II du livre V de la première partie du code général des collectivités territoriales. Par dérogation à l'article L. 225-1 du code de commerce, elle compte au moins trois actionnaires. Elle ne peut prendre aucune participation dans des sociétés commerciales.",
    "IV. – Les statuts fixent le nombre de sièges d'administrateur ou de membre du conseil de surveillance attribués à chaque actionnaire. Ce nombre est proportionnel au capital détenu et, le cas échéant, arrondi à l'unité supérieure.",
    "V. – La présidence du conseil d'administration ou du conseil de surveillance est exercée par un représentant de l'Etat, de l'un de ses établissements publics mentionnés aux sections 2 et 3 du chapitre Ier du présent titre, de la collectivité territoriale ou du groupement de collectivités territoriales compétent.",
    "VI. – L'Etat ou l'un de ses établissements publics mentionnés aux mêmes sections 2 et 3 détient, avec la collectivité territoriale ou le groupement de collectivités territoriales, entre 34 % et 85 % du capital de la société et au moins 34 % des voix dans ses organes délibérants. L'ensemble des actionnaires opérateurs économiques détient au moins 15 % du capital.",
    "VII. – La société d'économie mixte d'aménagement à opération unique est dissoute de plein droit au terme du contrat conclu avec l'Etat ou l'un de ses établissements publics mentionnés auxdites sections 2 et 3 et la collectivité territoriale ou le groupement de collectivités territoriales compétent, ou dès que l'objet de ce contrat est réalisé ou a expiré.",
    "VIII. – Pour l'application du présent article, les dispositions de l'article L. 1541-2 du code général des collectivités territoriales qui visent la collectivité territoriale ou le groupement de collectivités territoriales s'appliquent aussi à l'Etat ou à l'un de ses établissements publics mentionnés aux mêmes sections 2 et 3.",
    "IX. – L'article L. 1541-3 du code général des collectivités territoriales s'applique à chaque collectivité territoriale ou groupement de collectivités territoriales compétent actionnaire d'une société d'économie mixte d'aménagement à opération unique.",
],
    "Réécriture à droit constant : la constitution de la société et le contrat sont décrits en phrases distinctes, les seuils sont rattachés explicitement aux catégories d'actionnaires et les neuf subdivisions sont conservées. Les dix alinéas, l'objet unique et les cas de dissolution demeurent ; aucune réforme de fond ni transition nouvelle n'est introduite.",
    "Le numéro source atypique L32-10-1 est reproduit exactement, sans le normaliser. Conserver au moins trois actionnaires, la part publique entre 34 % et 85 %, au moins 34 % des voix et au moins 15 % du capital pour l'ensemble des opérateurs économiques. Les sections 2 et 3, les articles L. 1541-2 et L. 1541-3 du CGCT et L. 225-1 du code de commerce restent les renvois applicables. L'expression source du VII selon laquelle l'objet du contrat peut avoir expiré est conservée ; son articulation avec le terme du contrat mérite clarification explicite, sans modification silencieuse des causes de dissolution.")

add('L331-1', [
    "Les communes ou établissements publics de coopération intercommunale, la métropole de Lyon, les départements, la collectivité de Corse et la région d'Ile-de-France perçoivent la taxe d'aménagement prévue aux articles 1635 quater A et suivants du code général des impôts. Cette taxe finance les actions et opérations qui contribuent à la réalisation des objectifs définis à l'article L. 101-2.",
    "Pour l'application de l'article 302 septies B du code général des impôts, la taxe d'aménagement entre dans le prix de revient de l'ensemble immobilier.",
],
    "Réécriture à droit constant : les bénéficiaires de la taxe et sa finalité sont énoncés avant le traitement du prix de revient, dans les deux alinéas d'origine. Aucune réforme de fond n'est introduite ; la baisse projetée des droits de mutation n'est pas étendue à la taxe d'aménagement.",
    "Conserver tous les bénéficiaires et les renvois à L. 101-2, aux articles 1635 quater A et suivants et à l'article 302 septies B du CGI. Les notes sources rattachent l'application à l'article 16 de l'ordonnance n° 2022-883 du 14 juin 2022, à la date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021, et aux conditions de l'article 1er du décret n° 2022-1102 du 1er août 2022. Ces règles temporelles ne sont ni remplacées ni utilisées pour dater une réforme future.")

add('L331-2', [
    "La commune ou l'établissement public de coopération intercommunale inscrit le produit de la part communale ou intercommunale de la taxe d'aménagement prévue aux articles 1635 quater A et suivants du code général des impôts dans la section d'investissement de son budget. La métropole de Lyon et la Ville de Paris inscrivent le produit de la taxe dans la section d'investissement de leur budget principal, à l'exception des produits mentionnés aux troisième et quatrième alinéas du II de l'article 1586 du même code.",
],
    "Réécriture à droit constant : les personnes publiques chargées de l'affectation budgétaire sont les sujets des deux phrases et l'exception reste attachée à la métropole de Lyon et à Paris. L'alinéa unique est conservé ; aucune réforme de fond ni affectation nouvelle n'est introduite.",
    "L'exception vise exactement les troisième et quatrième alinéas du II de l'article 1586 du CGI ; elle ne s'étend pas à la règle générale des communes et EPCI. Application selon l'article 16 de l'ordonnance n° 2022-883 du 14 juin 2022, à la date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021, sous les conditions de l'article 1er du décret n° 2022-1102 du 1er août 2022, conformément aux notes sources.")

add('L331-3', [
    "La part départementale de la taxe d'aménagement prévue aux articles 1635 quater A et suivants du code général des impôts est instituée pour financer :",
    "1° La politique de protection des espaces naturels sensibles prévue à l'article L. 113-8 du présent code, ainsi que les dépenses suivantes :",
    "a) L'acquisition de terrains ou d'ensembles de droits sociaux donnant vocation à l'attribution de terrains en propriété ou en jouissance, par voie amiable, par expropriation ou par exercice du droit de préemption mentionné à l'article L. 215-4 ; l'aménagement et l'entretien de tout espace naturel, boisé ou non, appartenant au département, à condition qu'il soit ouvert au public dans les conditions prévues à l'article L. 215-21 ;",
    "b) La participation du département à l'acquisition, à l'aménagement et à la gestion des terrains du Conservatoire de l'espace littoral et des rivages lacustres ; sa participation à l'acquisition de terrains par une commune ou un établissement public de coopération intercommunale compétent, ainsi qu'à l'entretien des terrains acquis par l'une ou l'autre de ces personnes publiques ou par l'agence des espaces verts de la région d'Ile-de-France dans l'exercice du droit de préemption, par délégation ou par substitution, prévu aux articles L. 215-4 à L. 215-8 ;",
    "c) L'aménagement et l'entretien des espaces naturels, boisés ou non, qui appartiennent à des collectivités publiques ou à leurs établissements publics et sont ouverts au public, ainsi que de ceux qui appartiennent à des propriétaires privés et ont fait l'objet d'une convention passée en application de l'article L. 113-6 ;",
    "d) L'aménagement et la gestion des parties naturelles de la zone dite des cinquante pas géométriques définie à l'article L. 121-45 ;",
    "e) L'acquisition, l'aménagement et la gestion des sentiers inscrits sur un plan départemental des itinéraires de promenade et de randonnée établi dans les conditions prévues à l'article L. 361-1 du code de l'environnement, ainsi que des chemins et servitudes de halage et de marchepied des voies d'eau domaniales concédées qui ne sont pas ouvertes à la circulation générale ; l'acquisition, par voie amiable ou par exercice du droit de préemption mentionné à l'article L. 215-4, l'aménagement et la gestion des chemins longeant les autres cours d'eau et plans d'eau ;",
    "f) L'acquisition de bois et forêts ou de droits sociaux donnant vocation à leur attribution en propriété ou en jouissance, par un département, une commune, un établissement public de coopération intercommunale ou le Conservatoire de l'espace littoral et des rivages lacustres, sous réserve de leur ouverture au public dans les conditions prévues à l'article L. 215-21 ;",
    "g) L'acquisition, l'aménagement et la gestion des espaces, sites et itinéraires inscrits au plan départemental des espaces, sites et itinéraires relatifs aux sports de nature établi en application de l'article L. 311-3 du code du sport, à condition que l'aménagement ou la gestion envisagés maintiennent ou améliorent la qualité des sites, des paysages et des milieux naturels ;",
    "h) L'acquisition, la gestion et l'entretien des sites Natura 2000 désignés à l'article L. 414-1 du code de l'environnement et des territoires classés en réserve naturelle au sens de l'article L. 332-1 du même code ;",
    "i) Les études et inventaires du patrimoine naturel nécessaires à l'élaboration et à la mise en œuvre de la politique de protection et de gestion des espaces naturels sensibles destinés à être ouverts au public ;",
    "j) L'acquisition de sites destinés à préserver la ressource en eau, ainsi que leur aménagement et leur gestion ;",
    "k) Les travaux qui contribuent à préserver ou à remettre en bon état les continuités écologiques identifiées dans les schémas prévus à l'article L. 371-3 du code de l'environnement ;",
    "l) L'acquisition, par un département, une commune, un établissement public de coopération intercommunale ou un opérateur public, de terrains nus, bâtis ou aménagés et de gisements artificialisés pour y réaliser des travaux de transformation et, le cas échéant, de dépollution, d'entretien et d'aménagement, afin de les convertir en espaces naturels. Les opérateurs publics concernés comprennent notamment le Conservatoire de l'espace littoral et des rivages lacustres, les établissements publics fonciers et l'agence des espaces verts de la région d'Île-de-France ;",
    "2° Les dépenses des conseils d'architecture, d'urbanisme et de l'environnement prévues en application de l'article 8 de la loi n° 77-2 du 3 janvier 1977 sur l'architecture.",
    "Le produit de cette part départementale constitue une recette de fonctionnement.",
],
    "Réécriture à droit constant : le catalogue des dépenses est formulé par objets de financement, avec des phrases ou segments plus courts pour les acquisitions et participations complexes. Tous les seize alinéas, les 1° et 2° et les lettres a) à l) sont conservés. Aucune dépense éligible ni condition environnementale n'est supprimée ; aucune réforme de fond n'est introduite.",
    "Les conditions d'ouverture au public des a), c) et f), la convention des propriétés privées au c), la condition qualitative du g) et les deux catégories de voies d'eau du e) restent distinctes. Le l) conserve terrains nus, bâtis ou aménagés, gisements artificialisés, travaux de transformation et travaux éventuels complémentaires ; la liste des opérateurs demeure non exhaustive. La désignation historique de l'agence des espaces verts est conservée sans modernisation implicite. Les notes sources renvoient à l'article 16 de l'ordonnance n° 2022-883 du 14 juin 2022, à la date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021 et à l'article 1er du décret n° 2022-1102 du 1er août 2022 pour l'application. La qualification de recette de fonctionnement est maintenue.")

add('L331-4', [
    "La part de la taxe d'aménagement prévue aux articles 1635 quater A et suivants du code général des impôts qui est versée à la région d'Ile-de-France finance les équipements collectifs rendus nécessaires par l'urbanisation, principalement les infrastructures de transport.",
    "La région d'Ile-de-France inscrit le produit de cette taxe dans la section d'investissement de son budget.",
],
    "Réécriture à droit constant : la finalité de la part régionale et son affectation budgétaire sont énoncées directement dans les deux alinéas d'origine. Aucune réforme de fond ni priorité nouvelle d'investissement n'est ajoutée.",
    "Les infrastructures de transport demeurent la destination principale, sans exclure les autres équipements collectifs nécessaires à l'urbanisation. Conserver l'affectation en investissement. Application selon les notes sources : article 16 de l'ordonnance n° 2022-883 du 14 juin 2022, date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021 et conditions de l'article 1er du décret n° 2022-1102 du 1er août 2022.")

add('L331-17', [
    "La délibération prise en application du II de l'article 1635 quater L du code général des impôts fixe les taux de répartition de la part départementale de la taxe d'aménagement prévue aux articles 1635 quater A et suivants du même code entre la politique de protection des espaces naturels sensibles et les conseils d'architecture, d'urbanisme et de l'environnement. A défaut, ces taux sont fixés au plus tard lors de l'établissement du budget annuel.",
],
    "Réécriture à droit constant : la décision qui fixe la répartition est placée en sujet, puis l'échéance ultime est formulée dans une seconde phrase du même alinéa. Aucune réforme de fond, aucun taux chiffré ni changement de bénéficiaire n'est introduit.",
    "Il s'agit de taux de répartition du produit entre deux destinations, et non de taux d'imposition nouveaux. L'échéance reste au plus tard l'établissement du budget annuel. Les notes sources prévoient l'application par l'article 16 de l'ordonnance n° 2022-883 du 14 juin 2022, à la date résultant du B du VI de l'article 155 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021 et selon l'article 1er du décret n° 2022-1102 du 1er août 2022.")

add('L332-6', [
    "Les seules obligations qui peuvent être imposées aux bénéficiaires d'autorisations de construire sont les suivantes :",
    "1° Verser la taxe d'aménagement prévue à l'article 1635 quater A du code général des impôts ou la participation instituée dans les secteurs d'aménagement définis à l'article L. 332-9 du présent code, dans sa rédaction antérieure à l'entrée en vigueur de la loi n° 2010-1658 du 29 décembre 2010 de finances rectificative pour 2010, ou dans les périmètres fixés par les conventions visées à l'article L. 332-11-3 ;",
    "2° Verser les contributions aux dépenses d'équipements publics mentionnées au c du 2° de l'article L. 332-6-1, ainsi que la participation pour voirie et réseaux et la participation des riverains des départements du Bas-Rhin, du Haut-Rhin et de la Moselle définies au d du 2° et au 3° du même article L. 332-6-1, dans leur rédaction antérieure à l'entrée en vigueur de la loi n° 2014-1655 du 29 décembre 2014 de finances rectificative pour 2014. Toutefois, les contributions définies au d du 2° et au 3° de l'article L. 332-6-1, dans leur rédaction antérieure à cette même loi, ne peuvent concerner les équipements publics qui donnent lieu à la participation instituée dans les secteurs d'aménagement définis à l'article L. 332-9, dans sa rédaction antérieure à la loi n° 2010-1658 du 29 décembre 2010 précitée, ou dans les périmètres fixés par les conventions mentionnées à l'article L. 332-11-3 ;",
    "3° Réaliser les équipements propres mentionnés à l'article L. 332-15 ;",
    "5° Verser la redevance d'archéologie préventive prévue aux articles L. 524-2 à L. 524-13 du code du patrimoine ;",
    "6° Verser la contribution mentionnée à l'article L. 332-17 du présent code.",
],
    "Réécriture à droit constant : la liste limitative est rédigée en obligations verbales, avec maintien des régimes historiques et de l'interdiction de cumul concernant certains équipements. Les six alinéas et la numérotation 1°, 2°, 3°, 5°, 6° restent inchangés. Aucune réforme de fond des prélèvements n'est ajoutée.",
    "L'absence de 4° est celle de la source et n'est pas comblée. Les renvois au d du 2° et au 3° de L. 332-6-1 visent expressément leur rédaction antérieure à la loi n° 2014-1655 : ils ne doivent pas être remplacés par le texte actuel, qui ne les contient plus. Les deux références à L. 332-9 conservent leur qualification historique, dont la première vise expressément l'entrée en vigueur de la loi de 2010. La note source précise que le VII de l'article 24 de la loi n° 2025-391 du 30 avril 2025 s'applique aux opérations dont le permis de construire, le permis d'aménager ou la décision de non-opposition à déclaration préalable ont été délivrés à compter du 10 septembre 2023 (VIII du même article) : ne pas confondre cette date d'application avec une réforme future. L'accord grammatical de « mentionnés » au 3° est régularisé sans effet de fond.")

add('L332-6-1', [
    "La liste des contributions aux dépenses d'équipements publics visées au 2° de l'article L. 332-6 est la suivante :",
    "1° a) (Abrogé) ;",
    "b) (Abrogé) ;",
    "c) (Abrogé) ;",
    "d) (Abrogé) ;",
    "e) (Abrogé) ;",
    "2° a) (Abrogé) ;",
    "b) (Abrogé) ;",
    "c) La participation spécifique prévue à l'article L. 332-8 pour réaliser des équipements publics exceptionnels.",
],
    "Réécriture à droit constant : l'introduction identifie directement la liste et le c) du 2° place le renvoi auprès de la participation. Les neuf alinéas et toutes les subdivisions abrogées sont conservés pour la lecture des renvois historiques ; aucune réforme de fond ni réactivation d'une contribution n'est opérée.",
    "Les mentions « Abrogé » ne sont pas des emplacements « Réservé. » et sont maintenues dans le texte intégral. Le 2° de L. 332-6 conserve des renvois à la rédaction antérieure de cet article pour les régimes anciens ; ne pas réintroduire d) ou 3° dans le texte actuel. La note source fixe l'entrée en vigueur au 1er janvier 2015 par le X de l'article 44 de la loi n° 2014-1655 du 29 décembre 2014, et applique l'abrogation du b du 2° de L. 332-6-1 aux demandes d'autorisation et déclarations préalables effectuées à compter de cette même date.")

add('L332-7', [
    "Lorsqu'une prescription exigeant une taxe ou une contribution aux dépenses d'équipements publics est illégale, cette illégalité n'affecte pas la légalité des autres dispositions de l'autorisation de construire.",
    "Si une telle prescription est annulée pour illégalité, l'autorité qui a délivré l'autorisation prend un nouvel arrêté prescrivant une taxe ou une contribution aux dépenses d'équipements publics. Elle tient compte de la décision juridictionnelle devenue définitive.",
],
    "Réécriture à droit constant : l'effet limité de l'illégalité est formulé sous condition, puis l'obligation de prendre un nouvel arrêté est attribuée explicitement à l'autorité compétente. Les deux alinéas sont conservés ; aucune réforme de fond ni nouveau pouvoir de prélèvement n'est créé.",
    "La nouvelle prescription doit tenir compte de la décision juridictionnelle devenue définitive. La règle n'autorise pas un prélèvement dépourvu de base légale et ne supprime pas la liste limitative de L. 332-6 ; aucune procédure ou échéance supplémentaire n'est ajoutée.")


def main():
    sources = json.loads(Path('source.json').read_text())
    assert len(sources) == len(drafts) == 24
    assert set(drafts) == {a['number'] for a in sources}
    answers = []
    for source in sources:
        draft = drafts[source['number']]
        assert draft['proposed_xml'] != source['source_xml']
        answers.append({
            **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
            **draft,
            'status': 'rewrite_draft',
        })
    Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
    print(f"answer.json : {len(answers)} articles")


if __name__ == '__main__':
    main()
