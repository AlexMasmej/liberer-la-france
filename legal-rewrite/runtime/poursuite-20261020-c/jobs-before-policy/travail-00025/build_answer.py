import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('L1454-3', [
    'Le conseiller prud’homme empêché de siéger à l’audience de départage est remplacé. Un décret fixe les limites et les modalités de ce remplacement.',
], 'Réécriture à droit constant : la règle de remplacement et le renvoi au décret sont exprimés dans deux phrases distinctes, avec un sujet explicite. Aucune réforme de fond.',
    'Le remplacement demeure obligatoire en cas d’empêchement ; ses limites et ses modalités restent réglementaires. Aucun délai ni pouvoir de remplacement supplémentaire n’est créé.')

add('L1454-4', [
    'Lorsque, à l’audience de départage, le bureau de jugement ou la formation de référé ne peut siéger au complet, le juge départiteur statue selon les conditions fixées par décret en Conseil d’État.',
], 'Réécriture à droit constant : la condition tenant à la composition incomplète de la formation est rattachée directement à l’intervention du juge départiteur. Aucune réforme de fond.',
    'Les deux formations, le contexte de l’audience de départage et le renvoi à un décret en Conseil d’État sont conservés.')

add('L1454-5', [
    'Lorsque le conseil de prud’hommes est saisi d’une demande de requalification en contrat de travail d’une convention de stage mentionnée à l’article L. 124-1 du code de l’éducation, l’affaire est portée directement devant le bureau de jugement. Celui-ci statue au fond dans le mois suivant sa saisine.',
], 'Réécriture à droit constant : la saisine directe du bureau de jugement et son délai pour statuer au fond sont distingués dans un même alinéa. Aucune réforme de fond.',
    'Le délai d’un mois suivant la saisine est conservé, sans nouveau point de départ. Le renvoi à l’article L. 124-1 du code de l’éducation et le champ limité aux conventions de stage concernées sont maintenus.')

add('L1456-1', [
    'La section ou la chambre saisie d’un litige portant sur des licenciements pour motif économique statue en urgence. Un décret en Conseil d’État fixe les modalités et les délais de cette procédure.',
], 'Réécriture à droit constant : la formation saisie est le sujet de l’obligation de statuer en urgence ; la compétence réglementaire fait l’objet d’une seconde phrase. Aucune réforme de fond.',
    'L’urgence reste applicable aux litiges relatifs aux licenciements économiques, y compris ceux relevant de la rédaction proposée de L. 1233-3. Aucun délai chiffré n’est ajouté ; les modalités et délais restent fixés par décret en Conseil d’État.')

add('L1457-1', [
    'La récusation d’un conseiller prud’homme peut être demandée dans les cas suivants :',
    '1° Il a un intérêt personnel au litige. Sa seule affiliation à une organisation syndicale ne constitue pas un tel intérêt ;',
    '2° Il est le conjoint, le partenaire lié par un pacte civil de solidarité ou le concubin de l’une des parties, ou un parent ou allié de celle-ci jusqu’au degré de cousin germain inclusivement ;',
    '3° Au cours de l’année précédant la récusation, une action judiciaire, criminelle ou civile, a opposé le conseiller à l’une des parties ou au conjoint, au partenaire lié par un pacte civil de solidarité, au concubin, aux parents ou aux alliés en ligne directe de cette partie ;',
    '4° Il a donné un avis écrit dans l’affaire ;',
    '5° L’une des parties en cause est son employeur ou son salarié.',
], 'Réécriture à droit constant : les cinq causes de récusation sont formulées avec le conseiller pour sujet ou avec une relation d’emploi explicite. L’exception relative à la seule affiliation syndicale est isolée dans une phrase. Aucune réforme de fond.',
    'Les 1° à 5° sont conservés. Contrôle particulier du degré de cousin germain inclus, de la période d’un an précédant la récusation et de la liste des proches au 3° : aucune de ces conditions n’est élargie. L’avis doit toujours être écrit.')

add('L1462-1', [
    'Les jugements rendus par les conseils de prud’hommes peuvent faire l’objet d’un appel.',
    'En dessous du taux fixé par décret, les conseils de prud’hommes statuent toutefois en dernier ressort.',
], 'Réécriture à droit constant : le droit d’appel et son exception sont maintenus dans leurs deux alinéas ; le sujet de la décision en dernier ressort est explicité. Aucune réforme de fond.',
    'Le seuil demeure fixé par décret et la formulation « en dessous » est conservée. Incohérence de classement préexistante : le chemin fourni place cette règle d’appel dans le chapitre « Pourvoi en cassation ». Le texte et le classement ne sont pas corrigés sur ce seul constat.')

add('L1471-1', [
    'Le délai de prescription de toute action portant sur l’exécution du contrat de travail est de deux ans. Il court à compter du jour où la personne qui exerce l’action a connu ou aurait dû connaître les faits lui permettant d’exercer son droit.',
    'Le délai de prescription de toute action portant sur la rupture du contrat de travail est de douze mois à compter de la notification de cette rupture.',
    'Les délais prévus aux deux premiers alinéas ne s’appliquent pas aux actions en réparation d’un dommage corporel causé à l’occasion de l’exécution du contrat de travail, aux actions en paiement ou en répétition du salaire, ni aux actions exercées en application des articles L. 1132-1, L. 1152-1 et L. 1153-1. Ils ne font obstacle ni aux délais de prescription plus courts prévus par le présent code, notamment aux articles L. 1233-67, L. 1234-20, L. 1235-7, L. 1237-14 et L. 1237-19-8, ni à l’application du dernier alinéa de l’article L. 1134-5.',
], 'Réécriture à droit constant : chaque délai est assorti de son point de départ ; le troisième alinéa désigne expressément les délais auxquels il déroge et conserve l’ensemble des exceptions. Aucune réforme de fond.',
    'Trois alinéas conservés, notamment pour le renvoi aux deux premiers. Deux ans et douze mois restent distincts. Le pronom « Elles » de la source est explicité par une référence aux délais des deux premiers alinéas, sans étendre les exclusions. La note de l’article 40-II de l’ordonnance n° 2017-1387 du 22 septembre 2017 demeure à conserver avec le texte : application aux prescriptions en cours à compter de la publication de l’ordonnance, sans dépasser la durée totale prévue par la loi antérieure ; une instance introduite avant cette publication demeure poursuivie et jugée selon la loi ancienne, y compris en appel et en cassation. Cette transition historique n’est pas une date d’entrée en vigueur de la réforme proposée.')

add('L1511-1', [
    'Pour l’application de la présente partie, et sous réserve, le cas échéant, des dispositions du présent livre, les termes « national », « nationales », « nationaux », « France », « territoire français », « sol français », « ensemble du territoire » et « ensemble du territoire national » désignent les départements de métropole, la Guadeloupe, la Guyane, la Martinique, Mayotte, La Réunion, Saint-Barthélemy, Saint-Martin et Saint-Pierre-et-Miquelon.',
    'La sanction pénale d’interdiction du territoire français prévue par une disposition de la présente partie s’applique sur l’ensemble du territoire de la République française.',
], 'Réécriture à droit constant : le champ des expressions territoriales et celui de la sanction pénale sont formulés séparément, dans les deux alinéas existants. Aucune réforme de fond.',
    'Les huit expressions définies, les départements de métropole et les huit collectivités ultramarines sont conservés. L’interdiction pénale conserve le champ, distinct, de l’ensemble du territoire de la République française ; la réserve du présent livre demeure.')

add('L1521-1', [
    'En Guadeloupe, en Guyane, en Martinique, à Mayotte, à La Réunion, à Saint-Barthélemy, à Saint-Martin et à Saint-Pierre-et-Miquelon, la présente partie s’applique sous réserve des adaptations prévues par le présent titre.',
], 'Réécriture à droit constant : les territoires concernés sont placés en tête de la règle d’application, dont la réserve d’adaptation est conservée. Aucune réforme de fond.',
    'La liste des huit collectivités est intégrale. Cette règle générale ne dispense pas de respecter les adaptations territoriales et les transitions propres aux dispositions réformées, notamment celle proposée à L. 1524-1 pour Mayotte.')

add('L1521-2', [
    'En Guadeloupe, en Guyane, en Martinique et à La Réunion, pour l’application de la présente partie et sauf mention particulière propre à ces collectivités, les références à la caisse régionale d’assurance maladie désignent la caisse générale de sécurité sociale dans les départements d’outre-mer.',
], 'Réécriture à droit constant : la substitution de référence est énoncée comme une règle de lecture directement applicable, avec une réserve plus concise. Aucune réforme de fond.',
    'La règle demeure limitée aux quatre collectivités énumérées ; elle n’est pas étendue à Mayotte, à Saint-Barthélemy, à Saint-Martin ou à Saint-Pierre-et-Miquelon, qui font l’objet de dispositions propres.')

add('L1521-2-1', [
    'En Guyane et en Martinique, les règles suivantes s’appliquent à la présente partie, sauf mention particulière propre à ces collectivités :',
    '1° Le représentant de l’État dans la collectivité territoriale exerce les attributions du préfet dans la région ou dans le département ;',
    '2° Les attributions du conseil départemental, du conseil régional ou de leur président sont exercées, en Guyane, par l’assemblée de Guyane ou par son président. En Martinique, elles sont exercées par l’assemblée de Martinique ou par le président du conseil exécutif de Martinique ou, dans le cas prévu à l’article L. 7223-5 du code général des collectivités territoriales, par le président de l’assemblée de Martinique ;',
    '3° Les références au département, au département d’outre-mer, à la région, à la région d’outre-mer, au conseil départemental et au conseil régional s’entendent de références à la Guyane et à la Martinique.',
], 'Réécriture à droit constant : les autorités qui exercent les compétences sont identifiées directement ; le 2° distingue dans le même alinéa la Guyane et la Martinique. Aucune réforme de fond.',
    'Les 1° à 3° et l’exception de L. 7223-5 du code général des collectivités territoriales sont conservés. La coquille « où » dans « au conseil régional où à leur président » est rendue par la conjonction « ou », sans changement de compétence. Note historique à conserver : l’article 4 III de l’ordonnance n° 2015-1578 du 3 décembre 2015 fixe l’entrée en vigueur à la première réunion suivant la première élection des assemblées créées par la loi n° 2011-884 du 27 juillet 2011 ; cette règle n’est pas une transition de la réforme proposée.')

add('L1521-2-2', [
    'À Mayotte, les règles suivantes s’appliquent à la présente partie, sauf mention particulière propre à cette collectivité :',
    '1° Le préfet de Mayotte exerce les attributions du préfet dans la région ou dans le département ;',
    '2° Le conseil départemental de Mayotte ou son président exerce les attributions du conseil régional ou de son président ;',
    '3° La direction des entreprises, de la concurrence, de la consommation, du travail et de l’emploi de Mayotte ou, respectivement, son directeur exerce les attributions de la direction régionale des entreprises, de la concurrence, de la consommation, du travail et de l’emploi ou de son directeur ;',
    '4° La direction compétente à Mayotte ou son directeur exerce les attributions d’une direction régionale ou de son directeur ;',
    '5° Les références au département ou à la région désignent, selon le cas, Mayotte ou le Département de Mayotte ;',
    '6° Les références à la chambre départementale d’agriculture désignent la chambre de l’agriculture, de la pêche et de l’aquaculture de Mayotte ;',
    '7° Les références à la caisse régionale d’assurance maladie, à la caisse d’assurance retraite et de la santé au travail ou aux unions de recouvrement des cotisations de sécurité sociale et d’allocations familiales désignent la caisse de sécurité sociale de Mayotte ;',
    '8° Lorsque le présent code renvoie au recouvrement dans les conditions prévues au chapitre VII du titre III du livre Ier du code de la sécurité sociale, ou à la section 1 de ce chapitre, ce renvoi s’entend du recouvrement par la caisse de sécurité sociale selon les règles applicables aux cotisations de sécurité sociale à la charge des employeurs, assises sur les gains et rémunérations de leurs salariés ;',
    '9° Les références au plafond de la sécurité sociale, y compris celui prévu à l’article L. 241-3 du code de la sécurité sociale, désignent le plafond de la sécurité sociale applicable à Mayotte ;',
    '10° Les références au régime général de sécurité sociale désignent le régime de sécurité sociale organisé par les textes suivants : l’ordonnance n° 96-1122 du 20 décembre 1996 relative à l’amélioration de la santé publique, à l’assurance maladie, maternité, invalidité et décès, au financement de la sécurité sociale à Mayotte et à la caisse de sécurité sociale de Mayotte ; l’ordonnance n° 2002-149 du 7 février 2002 relative à l’extension et à la généralisation des prestations familiales et à la protection sociale dans la collectivité départementale de Mayotte ; l’ordonnance n° 2002-411 du 27 mars 2002 relative à la protection sanitaire et sociale à Mayotte ; et l’ordonnance n° 2006-1588 du 13 décembre 2006 relative au régime de prévention, de réparation et de tarification des accidents du travail et des maladies professionnelles à Mayotte ;',
    '11° Les références aux exonérations de cotisations sociales mentionnées à l’article L. 241-13 du code de la sécurité sociale désignent les exonérations mentionnées à l’article 28-7 de l’ordonnance n° 96-1122 du 20 décembre 1996 relative à l’amélioration de la santé publique, à l’assurance maladie, maternité, invalidité et décès, au financement de la sécurité sociale à Mayotte et à la caisse de sécurité sociale de Mayotte ;',
    '12° Les références au code de la sécurité sociale s’entendent de références à la législation applicable à Mayotte en matière de sécurité sociale ;',
    '13° Tout document dont le présent code prévoit la transmission par lettre recommandée peut toujours être remis en main propre contre décharge ou transmis par tout autre moyen donnant date certaine à sa réception ;',
    '14° Lorsque le présent code prévoit que le public ou les salariés transmettent ou reçoivent des documents, organisent des réunions ou des scrutins, ou accomplissent toute autre formalité par voie électronique, ces opérations peuvent être accomplies par toute voie utile ;',
    '15° à 19° (Abrogés).',
], 'Réécriture à droit constant : les autorités compétentes sont placées en sujets et les substitutions de références deviennent des règles de lecture explicites. Les règles relatives aux transmissions et aux formalités sont formulées directement. Aucune réforme de fond.',
    'Les 1° à 14° restent à leur place et la mention des 15° à 19° abrogés est conservée. Les quatre ordonnances du 10°, leurs dates, le renvoi à L. 241-3 au 9°, ceux à L. 241-13 et à l’article 28-7 au 11°, ainsi que les conditions de réception du 13° sont maintenus. La ponctuation du titre de l’ordonnance n° 2006-1588 est clarifiée par des virgules. Les anciennes dénominations administratives du 3° sont conservées : une éventuelle actualisation appelle une coordination distincte. La source est signalée ABROGE_DIFF, valable du 1er janvier 2022 au 31 décembre 2027 ; ce calendrier source n’est ni supprimé ni prolongé. Les adaptations de sécurité sociale ne valent pas extension automatique à Mayotte de la nouvelle capitalisation du régime général définie dans coordination.json.')

add('L1521-3', [
    'À Saint-Pierre-et-Miquelon, les règles suivantes s’appliquent à la présente partie, sauf mention particulière propre à cette collectivité :',
    '1° Le représentant de l’État exerce les attributions du préfet dans la région ou dans le département ;',
    '2° Le conseil général de Saint-Pierre-et-Miquelon ou son président exerce les attributions du conseil régional ou de son président ;',
    '3° Le tribunal de première instance, son président ou son greffe exerce les attributions du tribunal judiciaire, de son président ou de son greffe ;',
    '4° Le chef du service du travail, de l’emploi et de la formation professionnelle de Saint-Pierre-et-Miquelon exerce les attributions du directeur régional des entreprises, de la concurrence, de la consommation, du travail et de l’emploi ou du directeur du travail, de l’emploi et de la formation professionnelle des départements d’outre-mer ;',
    '5° Les références au code général des impôts désignent les dispositions équivalentes du code des impôts de Saint-Pierre-et-Miquelon ;',
    '6° Les références au département ou à la région désignent Saint-Pierre-et-Miquelon ;',
    '7° Les références à la caisse régionale d’assurance maladie désignent la caisse de prévoyance sociale.',
], 'Réécriture à droit constant : les titulaires locaux des compétences deviennent les sujets des 1° à 4° ; les 5° à 7° expriment directement la portée des références. Aucune réforme de fond.',
    'Les sept adaptations sont conservées, notamment les dispositions fiscales équivalentes du 5°, qui ne rendent pas le CGI directement applicable. La dénomination « conseil général » et les anciennes dénominations des services du travail proviennent de la source ; leur actualisation institutionnelle doit être contrôlée séparément, sans remplacement silencieux. La note de l’article 36 de l’ordonnance n° 2019-964 du 18 septembre 2019 fixe l’entrée en vigueur au 1er janvier 2020 et demeure à conserver comme note historique.')

add('L1521-4', [
    'À Saint-Barthélemy et à Saint-Martin, les règles suivantes s’appliquent à la présente partie, sauf mention particulière propre à l’une ou l’autre de ces collectivités :',
    '1° Le représentant de l’État dans chacune de ces collectivités exerce les attributions du préfet dans la région ou dans le département ;',
    '2° Le conseil territorial ou son président exerce les attributions du conseil régional ou de son président et du conseil général ou de son président ;',
    '3° Les références au département ou à la région désignent Saint-Barthélemy ou Saint-Martin, selon la collectivité concernée ;',
    '4° Les références à la caisse régionale d’assurance maladie désignent la caisse générale de sécurité sociale.',
], 'Réécriture à droit constant : les autorités locales compétentes sont nommées en tête de phrase et les références territoriales sont rattachées à la collectivité concernée. Aucune réforme de fond.',
    'Les 1° à 4° et la réserve de dispositions particulières sont conservés. La mention du conseil général demeure celle de la source ; toute actualisation des intitulés doit faire l’objet d’une coordination explicite.')

add('L1522-1', [
    'En Guadeloupe, en Guyane, en Martinique, à Mayotte, à La Réunion, à Saint-Barthélemy, à Saint-Martin et à Saint-Pierre-et-Miquelon, les règles relatives au chèque emploi-service universel prévues aux articles L. 1271-1 à L. 1271-16 et à la sous-section 2 de la section 1 du chapitre III bis du livre Ier du code de la sécurité sociale sont applicables.',
], 'Réécriture à droit constant : le champ territorial précède les deux ensembles de dispositions applicables au chèque emploi-service universel. Aucune réforme de fond.',
    'Les huit collectivités, la plage L. 1271-1 à L. 1271-16 et la subdivision du code de la sécurité sociale sont conservées. Ce texte maintient le dispositif existant ; il ne crée pas à lui seul le guichet unique envisagé par policy.json.')

add('L1522-2', [
    'En Guadeloupe, en Guyane, en Martinique, à Mayotte, à La Réunion, à Saint-Barthélemy, à Saint-Martin et à Saint-Pierre-et-Miquelon, sont applicables les dispositions relatives au chèque emploi associatif de la sous-section 2 de la section 1 du chapitre III bis du livre Ier du code de la sécurité sociale, ainsi que celles du chapitre II du titre VII du livre II de la première partie du présent code.',
], 'Réécriture à droit constant : les territoires sont présentés d’abord, puis les deux ensembles de règles applicables sont reliés sans ambiguïté entre les codes. Aucune réforme de fond.',
    'Les huit collectivités sont maintenues, y compris Mayotte et Saint-Pierre-et-Miquelon. Le chapitre II du titre VII du livre II relève bien de la première partie du code du travail, tandis que la sous-section citée relève du code de la sécurité sociale.')

add('L1522-3', [
    'I. – En Guadeloupe, en Guyane, en Martinique, à La Réunion, à Saint-Barthélemy, à Saint-Martin et à Saint-Pierre-et-Miquelon, sont applicables les dispositions relatives au titre emploi-service entreprise de la sous-section 2 de la section 1 du chapitre III bis du livre Ier du code de la sécurité sociale, ainsi que celles du chapitre III du titre VII du livre II de la première partie du présent code.',
    'II. – À Mayotte, le titre emploi-service entreprises prévu par les dispositions de la sous-section 2 de la section 1 du chapitre III bis du livre Ier du code de la sécurité sociale s’applique dans les conditions définies à l’article 28-11 de l’ordonnance n° 96-1122 du 20 décembre 1996 relative à l’amélioration de la santé publique, à l’assurance maladie, maternité, invalidité et décès, au financement de la sécurité sociale à Mayotte et à la caisse de sécurité sociale de Mayotte.',
], 'Réécriture à droit constant : le I énonce d’abord son champ territorial ; le II expose directement le régime propre à Mayotte. Les deux subdivisions et leurs champs de renvoi restent distincts. Aucune réforme de fond.',
    'Le I conserve les sept collectivités et le renvoi au chapitre III du code du travail ; le II ne reprend pas ce dernier renvoi et reste soumis à l’article 28-11 de l’ordonnance n° 96-1122. La variation de dénomination « entreprise » au I et « entreprises » au II est préexistante et conservée pour contrôle. La source est signalée ABROGE_DIFF avec une fin de validité au 1er janvier 2028 ; la proposition ne prolonge pas ce régime.')

add('L1522-4', [
    'En Guadeloupe, en Guyane, en Martinique, à Mayotte, à La Réunion, à Saint-Barthélemy et à Saint-Martin, sont applicables les dispositions de la sous-section 2 de la section 1 du chapitre III bis du livre Ier du code de la sécurité sociale relatives aux particuliers qui emploient des salariés exerçant une activité de garde d’enfants, mentionnés au 4° de l’article L. 133-5-6 de ce code, ainsi que les dispositions du chapitre Ier du titre III du livre cinquième du même code.',
], 'Réécriture à droit constant : la liste territoriale ouvre la phrase et les deux ensembles de dispositions du code de la sécurité sociale sont distingués. Aucune réforme de fond.',
    'Sept collectivités sont visées : Saint-Pierre-et-Miquelon n’est pas ajouté. Le 4° de L. 133-5-6 a été vérifié dans le corpus public : il concerne les particuliers employant des salariés pour la garde d’enfants. La note historique demeure à conserver : l’article 34 de l’ordonnance n° 2017-1491 du 25 octobre 2017 prévoyait le 1er janvier 2022 ; le 1° de l’article 3 de l’ordonnance n° 2021-1553 du 1er décembre 2021 a reporté cette entrée en vigueur à une date fixée par décret, au plus tard le 31 décembre 2023. La métadonnée source retient le 31 décembre 2023 ; aucune date de décret non fournie n’est inventée.')

add('L1523-1', [
    'Pour les conseils de prud’hommes de Guadeloupe, les suffrages des organisations syndicales de salariés retenus en application de l’article L. 1441-4 sont ceux obtenus en Guadeloupe, à Saint-Barthélemy et à Saint-Martin. Ces territoires constituent le niveau départemental de référence pour cette application.',
], 'Réécriture à droit constant : l’adaptation territoriale est exprimée comme la règle de prise en compte des suffrages, au lieu d’une substitution de mots. Aucune réforme de fond.',
    'L. 1441-4 a été vérifié dans le corpus public : le niveau départemental concerne les suffrages des organisations syndicales de salariés ; l’audience patronale reste déterminée au niveau national. L’adaptation concerne les conseils de prud’hommes de Guadeloupe et les trois territoires énumérés, sans modifier la répartition proportionnelle ni les autres critères de cet article.')

add('L1524-1', [
    'À Mayotte, pour les contrats à durée indéterminée conclus avant l’entrée en vigueur de la nouvelle rédaction de l’article L. 1221-19, les règles relatives à la période d’essai applicables lors de leur conclusion demeurent applicables. Elles comprennent, dans son champ temporel propre, la dérogation à l’article L. 1221-22 concernant les durées plus longues fixées par les accords collectifs de branche conclus avant le 1er janvier 2018, dans la limite d’une durée de cinq ans. Ce maintien ne prolonge ni ne rétablit une dérogation arrivée à expiration.',
    'Pour les contrats à durée indéterminée conclus à compter de cette entrée en vigueur, la période d’essai ne peut excéder trois mois et ne peut être renouvelée, conformément aux articles L. 1221-19 et L. 1221-21. Les durées plus courtes admises par l’article L. 1221-22 restent applicables dans les conditions qu’il prévoit.',
], 'Réécriture et coordination de fond avec la réforme de l’essai : l’adaptation de Mayotte est désormais formulée directement. Les nouveaux CDI relèvent du plafond de trois mois sans renouvellement ; les contrats antérieurs restent régis par leurs règles de conclusion, sans réactivation d’une dérogation expirée. Le 1er janvier 2018 et la limite historique de cinq ans sont conservés dans ce seul champ antérieur.',
    'Coordination requise avec les rédactions déjà retenues de L. 1221-19, L. 1221-21, L. 1221-22, L. 1221-23 et L. 1221-25 : même entrée en vigueur pour les nouveaux CDI, durées plus courtes admises et prévenance maintenues. Incohérence préexistante constatée dans le corpus : L. 1524-1 vise le deuxième alinéa de L. 1221-22 comme une exception pour des durées plus longues, alors que, depuis sa rédaction applicable le 9 septembre 2023, cet alinéa traite des durées plus courtes. La proposition abandonne cette substitution d’alinéa au profit d’une règle territoriale autonome et expose expressément la transition. La portée temporelle exacte de la formule source « dans la limite d’une durée de cinq ans » doit être contrôlée avec les textes transitoires d’extension à Mayotte ; elle n’est interprétée ni comme une nouvelle période d’essai de cinq ans ni comme un délai recommençant avec la réforme. Aucune date future de promulgation n’est fixée.')

add('L1524-2', [
    'À Mayotte, pour les garanties de rémunération prévues aux articles L. 1225-10 et L. 1225-14, l’indemnité journalière de maternité prévue à l’article 20-6 de l’ordonnance n° 96-1122 du 20 décembre 1996 relative à l’amélioration de la santé publique, à l’assurance maladie, maternité, invalidité et décès, au financement de la sécurité sociale à Mayotte et à la caisse de sécurité sociale de Mayotte tient lieu de l’allocation journalière mentionnée à l’article L. 333-1 du code de la sécurité sociale.',
], 'Réécriture à droit constant : la prestation mahoraise entrant dans les garanties de rémunération est désignée directement, sans citation de mots à remplacer. Aucune réforme de fond.',
    'Les renvois aux deux articles du code du travail, à L. 333-1 du code de la sécurité sociale et à l’article 20-6 de l’ordonnance n° 96-1122 sont conservés. La substitution porte sur la prestation journalière et ne modifie pas les conditions de suspension ni l’indemnité complémentaire à la charge de l’employeur. La source est signalée ABROGE_DIFF avec une fin de validité au 1er janvier 2028 ; ce calendrier n’est pas prolongé.')

add('L1524-3', [
    'À Mayotte, l’exception concernant les accords collectifs de branche ou d’entreprise, prévue au dernier alinéa de l’article L. 1225-26 et au dernier alinéa de l’article L. 1225-44, s’applique aux accords conclus avant le 1er janvier 2018. Cette date est la référence territoriale pour l’exception attachée, dans ces articles, à l’entrée en vigueur de la loi n° 2006-340 du 23 mars 2006 relative à l’égalité salariale entre les femmes et les hommes.',
], 'Réécriture à droit constant : la date déterminant les accords couverts par l’exception territoriale est énoncée dans une règle complète, sans instruction de remplacement de mots. Aucune réforme de fond.',
    'Le seuil historique du 1er janvier 2018 demeure applicable aux accords antérieurs, tant pour le congé de maternité que pour le congé d’adoption. Les renvois aux derniers alinéas de L. 1225-26 et L. 1225-44 restent valables dans les propositions consultées ; ne pas déplacer ces exceptions lors de leur assemblage. La date de la loi n° 2006-340 reste une référence historique, sans effet sur l’entrée en vigueur de la réforme proposée.')

add('L1524-4', [
    'À Mayotte, pour l’application de l’article L. 1225-28, le décès de la mère doit survenir, selon le cas, entre la naissance de l’enfant et la fin de l’indemnisation au titre du régime d’assurance maternité, ou entre la naissance de l’enfant et la fin du maintien de traitement lié à la maternité. Le père peut suspendre son contrat de travail pendant une période au plus égale à la durée d’indemnisation restant à courir. Les renvois figurant à l’article L. 1225-28 à la définition prévue au premier alinéa de l’article L. 331-6 du code de la sécurité sociale et au report prévu au deuxième alinéa de ce même article ne s’appliquent pas pour déterminer cette période et cette durée à Mayotte.',
], 'Réécriture à droit constant : les deux périodes alternatives et la durée maximale de suspension sont formulées directement. L’exclusion territoriale des renvois de L. 1225-28 à L. 331-6 est énoncée sans fragments cités à supprimer. Aucune réforme de fond.',
    'Les deux branches, indemnisation maternité ou maintien de traitement, sont conservées. La règle demeure une adaptation de L. 1225-28 : les obligations d’information de l’employeur, les protections contre le licenciement et le droit du conjoint salarié ou de la personne salariée liée par un PACS ou vivant maritalement avec la mère lorsque le père n’exerce pas son droit restent ceux de cet article. Le report du deuxième alinéa de L. 331-6 n’est pas réintroduit par la réécriture. Aucun régime d’indemnisation autonome n’est créé.')

add('L1524-5', [
    'À Mayotte, pour le congé prévu au premier alinéa de l’article L. 1225-61, la référence à la charge de l’enfant au sens de l’article L. 513-1 du code de la sécurité sociale s’entend de la charge de l’enfant au sens du premier alinéa de l’article 6 de l’ordonnance n° 2002-149 du 7 février 2002 relative à l’extension et à la généralisation des prestations familiales et à la protection sociale dans la collectivité départementale de Mayotte.',
], 'Réécriture à droit constant : le critère territorial de charge de l’enfant est exprimé comme une règle de lecture du congé concerné, sans citation ni instruction d’amendement. Aucune réforme de fond.',
    'Les renvois au premier alinéa de L. 1225-61, à L. 513-1 et au premier alinéa de l’article 6 de l’ordonnance n° 2002-149 sont maintenus. L’adaptation concerne seulement la définition de la charge : elle ne modifie ni l’âge de moins de seize ans, ni le certificat médical, ni l’absence de rémunération, ni les durées et majorations du congé prévues à L. 1225-61. Le texte de l’ordonnance n’est pas fourni dans le corpus indiqué et n’a pas été reconstitué.')


assert len(sources) == len(drafts) == 24
assert {a['number'] for a in sources} == set(drafts)
answer = []
for source in sources:
    record = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    record.update(drafts[source['number']])
    answer.append(record)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
