import json
import xml.etree.ElementTree as ET
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(index, paragraphs, reason, notes):
    if isinstance(paragraphs, list):
        xml = '\n'.join('<p>' + text + '</p>' for text in paragraphs)
    else:
        xml = paragraphs.strip()
    drafts[index] = dict(proposed_xml=xml, reason=reason, review_notes=notes,
                         status='rewrite_draft')


# Les intitulés professionnels sont une nomenclature exhaustive : ils sont
# conservés intégralement, dans leur alinéa, au sein de l'article réécrit.
ys_source = ET.fromstring('<root>' + sources[0]['source_xml'] + '</root>')
technicians = ys_source.findall('p')[3].text
add(0, [
    "Les dépenses retenues pour l'application du III de l'article 220 octies du code général des impôts sont énumérées ci-après :",
    "1. Pour les frais de production d'un enregistrement phonographique ou vidéographique musical, les dépenses retenues sont les suivantes :",
    "a. Pour le personnel autre que le personnel permanent de l'entreprise, sont retenus les salaires et charges sociales afférents aux artistes-interprètes de la musique signataires d'un contrat d'exclusivité avec le producteur phonographique, au chef d'orchestre, aux artistes-interprètes musiciens, aux artistes de chœurs, aux artistes choristes, aux diseurs, aux artistes-interprètes dramatiques, au réalisateur et à l'ingénieur du son. Sont également retenus les salaires et charges sociales afférents aux techniciens énumérés ci-après qui ont directement participé à la réalisation de la production :",
    technicians,
    "b. Pour les dépenses liées à l'utilisation des studios d'enregistrement ainsi qu'à la location et au transport de matériels et d'instruments, sont retenues : la location de studios pour les prises de son, la location de studios pour les mixages et la location du matériel et des instruments nécessaires à l'enregistrement de l'œuvre ;",
    "c. Pour la conception graphique d'un enregistrement phonographique, sont retenus les frais d'acquisition des droits des auteurs de photographies, d'illustrations, de créations graphiques et de biographies ;",
    "d. Pour le personnel permanent, sont retenus les salaires et charges sociales afférents aux personnels mentionnés au a bis du 1° du III de l'article 220 octies du code général des impôts. Ces dépenses ne sont retenues que pour la période pendant laquelle ces personnels ont été effectivement employés à la production d'une œuvre phonographique ou vidéographique musicale éligible au crédit d'impôt ;",
    "e. Pour la réalisation et la production d'images associées à l'enregistrement phonographique, sont retenus : les frais d'acquisition des droits des auteurs de photographies, d'illustrations et de créations graphiques ; les frais correspondant aux autorisations délivrées par des producteurs de spectacles, des exploitants de salles ou des organisateurs de festivals en cas d'utilisation d'extraits de captation ; les frais techniques nécessaires à la réalisation des images ; les frais de captation du son, de l'image et de la lumière ; les frais d'acquisition d'images préexistantes ; les cessions de droits facturées par l'ensemble des ayants droit d'auteurs et de droits voisins ; les dépenses d'utilisation des studios ou des lieux de tournage, à l'exclusion des lieux d'habitation ; les dépenses de décors, de costumes, de coiffures et de maquillage ; les frais de transport de matériels et d'instruments ; les dépenses de postproduction, comprenant la création et l'intégration d'effets spéciaux, le montage, l'étalonnage, le mixage, le codage et le matriçage ; les salaires et charges sociales afférents aux artistes, aux artistes-interprètes et aux personnels techniques ayant participé à ces opérations ;",
    "Pour un disque numérique polyvalent musical, sont retenus les frais de conception technique, tels que ceux liés à la création d'éléments d'interactivité ou d'une arborescence, ou au recours à des effets spéciaux.",
    "2. Pour le développement des productions phonographiques ou vidéographiques musicales mentionnées au 2° du III de l'article 220 octies du code général des impôts, les dépenses retenues sont les suivantes :",
    "a. Les dépenses engagées pour soutenir la production de concerts de l'artiste en France ou à l'étranger, dont le montant global est fixé par un contrat d'artiste ou de licence, sont retenues pour les postes suivants :",
    "la création d'affiches et de tracts, les prestations d'attaché de presse, les frais techniques indispensables à la réalisation de la tournée et les rémunérations versées aux artistes et aux techniciens, y compris pour les concerts promotionnels ;",
    "b. Pour la participation de l'artiste à des émissions de télévision ou de radio dans le cadre de la promotion de l'œuvre agréée, les dépenses suivantes sont retenues lorsqu'elles sont prévues par le contrat d'artiste ou de licence : les cachets versés aux artistes, les salaires et charges sociales afférents aux personnels et les frais de transport du matériel et des personnes nécessaires à ces opérations ;",
    "c. Pour la réalisation et la production d'images permettant le développement de la carrière de l'artiste, notamment de vidéogrammes, de documentaires musicaux ou de dossiers de presse en images, autres que celles mentionnées au f du 1° du III de l'article 220 octies du code général des impôts, sont retenus : les frais d'acquisition des droits des auteurs de photographies, d'illustrations et de créations graphiques, ainsi que les frais techniques nécessaires à ces créations ; les frais de captation du son, de l'image et de la lumière ; les frais d'acquisition d'images préexistantes ; les cessions de droits facturées par l'ensemble des ayants droit d'auteurs et de droits voisins ; les frais correspondant aux autorisations délivrées par des producteurs de spectacles, des exploitants de salles ou des organisateurs de festivals ; les dépenses de postproduction, comprenant le montage, l'étalonnage, le mixage, le codage et le matriçage ; les salaires et charges sociales afférents aux personnels techniques nécessaires à ces opérations ;",
    "Pour un disque numérique polyvalent musical, sont retenus les frais de conception technique, tels que ceux liés à la création d'éléments d'interactivité ou d'une arborescence, ou au recours à des effets spéciaux ;",
    "d. Pour la création d'un site internet dédié à l'artiste afin de développer sa carrière dans l'environnement numérique, sont retenus les frais de création liés à l'interactivité, à l'arborescence et au graphisme. Cette règle s'applique également à la création d'un site internet consacré à plusieurs artistes visés au b du II de l'article 220 octies du code général des impôts ;",
    "e. Pour le personnel permanent, les salaires et charges sociales ne sont retenus que pour la période pendant laquelle ces personnels ont été effectivement employés au développement d'une production phonographique ou vidéographique musicale éligible au crédit d'impôt."
],
    "Réécriture à droit constant des catégories de frais de production et de développement : les dépenses retenues et les périodes d'emploi effectif sont exprimées directement. Les longues énumérations sont conservées intégralement, notamment la nomenclature des techniciens, sans déplacement des subdivisions ni des alinéas. Aucune réforme de fond du crédit d'impôt n'est prévue par policy.json pour cet article.",
    "Conserver les 1 et 2, leurs lettres et les deux alinéas relatifs au disque numérique polyvalent à leur place. Les renvois aux III, II b, III 1° a bis et III 1° f de l'article 220 octies, l'exclusivité contractuelle des artistes-interprètes concernés, les concerts à l'étranger et l'exclusion des lieux d'habitation sont maintenus. Au 1 b, la source mentionne le transport dans l'intitulé de catégorie mais n'énumère que des locations : cette asymétrie est conservée, sans ajout de frais éligibles. Contrôler la concordance de cette énumération avec l'article 220 octies avant toute évolution de son assiette."
)

add(1, [
    "Pour l'application des articles 220 octies et 220 Q du code général des impôts, les entreprises doivent déposer une déclaration spéciale conforme au modèle établi par l'administration, avec le relevé de solde mentionné à l'article 360. Elles la déposent auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts.",
    "Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère doit joindre les déclarations spéciales des sociétés du groupe au relevé de solde relatif au résultat d'ensemble.",
    "Une copie de la déclaration spéciale doit être adressée au Centre national de la musique dans le même délai."
],
    "Réécriture à droit constant : la première phrase est scindée pour distinguer le document à déposer et son destinataire ; les obligations de la société mère et de transmission de la copie sont formulées expressément. Aucune modification de fond des formalités n'est introduite.",
    "Maintenir le dépôt avec le relevé de solde de l'article 360, le lieu d'imposition de l'article 218 A, le régime de l'article 223 A et le délai identique pour la copie au Centre national de la musique. L'orientation de réemploi des données appelle une disposition organisant la transmission unique par la direction générale des finances publiques au Centre national de la musique, les responsabilités de mise à jour et le droit de correction. La base légale d'une telle transmission au regard du secret fiscal doit être contrôlée dans le livre des procédures fiscales, hors des cinq codes ; si elle manque, une disposition législative y est nécessaire avant de supprimer l'envoi de la copie par l'entreprise. Aucun renvoi nouveau n'est créé."
)

add(2, [
    "Le crédit d'impôt prévu à l'article 220 octies du code général des impôts s'impute sur l'impôt qui reste dû après l'imputation des prélèvements non libératoires et des crédits d'impôt non restituables."
],
    "Réécriture à droit constant centrée sur l'ordre des imputations. Aucun taux, droit à restitution ou rang d'imputation n'est modifié ; aucune réforme de fond ne concerne cette règle dans policy.json.",
    "Le rang est conservé : prélèvements non libératoires et crédits d'impôt non restituables, puis crédit de l'article 220 octies. Ne pas remplacer cette catégorie par l'ensemble des autres crédits d'impôt, formulation propre à l'article 46 quater-0 YZC."
)

add(3, [
    "La rémunération du dirigeant retenue pour déterminer les dépenses mentionnées aux a du 1°, a du 2° et a du 3° du III de l'article 220 septdecies du code général des impôts est plafonnée à 45 000 € par an."
],
    "Réécriture à droit constant : le plafond annuel est rattaché directement à la rémunération du dirigeant prise en compte, avec maintien des trois postes de dépenses. Aucune réforme de fond ni suppression du dispositif n'est décidée.",
    "Plafond de 45 000 € par an maintenu. La note source indique une péremption liée à l'article 220 decies, alors que le dispositif renvoie à l'article 220 septdecies. Le corpus public contient un article 220 septdecies relatif à l'édition musicale ; l'article 220 decies y concerne les carburants d'aviation durables. Cette discordance est signalée, sans déduire l'abrogation du présent article. Le maximum légal de 50 000 € prévu au III de l'article 220 septdecies ne remplace pas le plafond réglementaire de 45 000 €."
)

add(4, [
    "Les dépenses mentionnées au j du 3° du III de l'article 220 septdecies du code général des impôts sont constituées des dotations aux amortissements fiscalement déductibles afférentes aux immobilisations détenues par l'entreprise et directement affectées à la publication, à la diffusion et à l'exploitation commerciale d'œuvres ouvrant droit au crédit d'impôt."
],
    "Réécriture à droit constant : les dotations retenues sont définies directement, en conservant leur déductibilité fiscale, la détention des immobilisations et leur affectation directe. Aucune réforme de fond de l'assiette n'est introduite.",
    "La note source rattache une péremption à l'article 220 decies, mais le texte vise l'article 220 septdecies : même discordance que pour l'article 46 quater-0 YV, à contrôler sans suppression silencieuse. Le j du 3° du III de l'article 220 septdecies figurant dans le corpus exige une utilisation exclusive des immobilisations corporelles ou incorporelles ; le présent texte conserve la formulation réglementaire d'affectation directe et ne dispense pas des conditions légales."
)

add(5, """
<p>Pour les dépenses mentionnées au c du 1° du III de l'article 220 septdecies du code général des impôts, les frais d'hébergement retenus dans l'assiette du crédit d'impôt sont plafonnés à 270 € dans la ville de Paris et les départements des Hauts-de-Seine, de la Seine-Saint-Denis et du Val-de-Marne, et à 200 € dans les autres départements.<br /><br />Pour les dépenses mentionnées au d du 3° du III de l'article 220 septdecies du code général des impôts, les frais d'hébergement retenus dans cette assiette sont plafonnés à 270 €.</p>
""",
    "Réécriture à droit constant des deux plafonnements : chaque plafond est rattaché au poste de dépenses correspondant et les distinctions territoriales sont explicites. Aucune réforme de fond des montants ou du champ n'est introduite.",
    "Conserver 270 € pour Paris et les trois départements cités, 200 € pour les autres départements au premier alinéa, et 270 € sans distinction territoriale au second. Le c du 1° et le d du 3° du III de l'article 220 septdecies précisent, dans le corpus public, que le plafond est fixé par nuitée ; cette unité, absente du texte réglementaire fourni, reste déterminée par ces dispositions légales."
)

add(6, """
<p>Pour l'application des articles 220 septdecies et 220 Q bis du code général des impôts, les entreprises doivent déposer une déclaration spéciale conforme au modèle établi par l'administration, avec le relevé de solde mentionné à l'article 360. Elles la déposent auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts.<br /><br />Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère doit joindre les déclarations spéciales des sociétés du groupe au relevé de solde relatif au résultat d'ensemble.<br /><br />Une copie de la déclaration spéciale doit être adressée au Centre national de la musique dans le même délai.</p>
""",
    "Réécriture à droit constant : la phrase relative au dépôt est scindée et les obligations déclaratives de l'entreprise et de la société mère sont explicitées. Les trois alinéas sont conservés ; aucune réforme de fond des formalités n'est ajoutée.",
    "Conserver les articles 220 septdecies, 220 Q bis, 360, 218 A et 223 A, le dépôt avec le relevé de solde et la copie au Centre national de la musique dans le même délai. Le réemploi des données prévu par les orientations nécessite une organisation de la transmission avant toute suppression de la copie ; aucune dispense n'est présumée acquise."
)

add(7, [
    "Le crédit d'impôt prévu à l'article 220 septdecies du code général des impôts s'impute sur l'impôt qui reste dû après l'imputation des prélèvements non libératoires et des crédits d'impôt non restituables."
],
    "Réécriture à droit constant plaçant l'ordre des imputations au centre de la phrase. Aucune réforme de fond du crédit d'impôt pour l'édition musicale ni de son rang d'imputation n'est introduite.",
    "Maintenir le renvoi à l'article 220 septdecies et l'antériorité de l'imputation des prélèvements non libératoires et des seuls crédits d'impôt non restituables."
)

add(8, [
    "Pour calculer le crédit d'impôt prévu à l'article 220 nonies du code général des impôts, le montant d'impôt sur les sociétés à retenir est celui dû avant l'imputation des réductions et des crédits d'impôt."
],
    "Réécriture à droit constant : la base du calcul est exprimée directement comme l'impôt dû avant les imputations. Aucun nouveau taux ni changement de fond du crédit d'impôt n'est introduit.",
    "Le calcul reste fondé sur l'impôt dû avant réductions et crédits d'impôt. La réforme du taux normal relève de l'article 219 du CGI selon coordination.json ; son éventuel effet sur l'impôt dû ne justifie ni taux autonome ni correction forfaitaire dans le présent article."
)

add(9, [
    "Pour calculer le crédit d'impôt prévu à l'article 220 nonies du code général des impôts, seuls sont retenus les intérêts dus dont l'échéance intervient au cours de l'exercice au titre duquel ce crédit d'impôt est calculé."
],
    "Réécriture à droit constant : la condition d'échéance au cours de l'exercice est énoncée directement. Aucune réforme de fond des intérêts éligibles n'est prévue.",
    "Conserver l'exercice de calcul comme période de rattachement des intérêts dus. L'échéance est le critère de la source ; elle n'est pas remplacée par la date du paiement effectif ou par celle de la conclusion de l'emprunt."
)

add(10, [
    "Pour calculer le crédit d'impôt prévu à l'article 220 nonies du code général des impôts, la proportion des droits sociaux détenus indirectement par les salariés dans le capital de la société rachetée est celle des droits détenus de manière continue pendant l'exercice au titre duquel le crédit d'impôt est calculé. Pour le premier exercice de calcul du crédit d'impôt, cette proportion est toutefois appréciée au dernier jour de l'exercice."
],
    "Réécriture à droit constant : le critère de détention continue est formulé directement et la règle particulière du premier exercice est distinguée par une seconde phrase. Aucune réforme de fond du calcul n'est introduite.",
    "Conserver la détention indirecte par les salariés, la continuité sur l'exercice et l'appréciation au dernier jour pour le seul premier exercice. Aucun prorata, moyenne annuelle ou seuil supplémentaire n'est créé."
)

add(11, [
    "Pour l'application de l'article 220 nonies du code général des impôts, sont considérées comme salariés les personnes que l'entreprise rémunère directement et qui sont titulaires d'un contrat de travail. Cette définition s'applique que le contrat soit à durée déterminée ou non, quelles que soient sa nature ainsi que la situation ou l'affectation de la personne."
],
    "Réécriture à droit constant : les deux conditions cumulatives, rémunération directe et contrat de travail, sont séparées des précisions qui rendent indifférentes la durée, la nature du contrat, la situation et l'affectation. Aucune réforme de fond de la qualité de salarié n'est introduite.",
    "Le champ reste propre à l'article 220 nonies. Les orientations relatives au CDI ou aux nouveaux contrats ne retirent pas les titulaires de CDD ni les contrats antérieurs de cette définition fiscale."
)

add(12, [
    "Pour l'application des articles 220 nonies et 220 R du code général des impôts, les entreprises doivent déclarer les réductions et crédits d'impôt selon le format établi par l'administration. Elles respectent les mêmes délais que pour la déclaration annuelle de résultat qu'elles doivent souscrire en application de l'article 223 du même code.",
    "La société mère d'un groupe au sens de l'article 223 A du code général des impôts déclare les réductions et crédits d'impôt pour le compte des sociétés du groupe, y compris les siens, lors du dépôt de la déclaration relative au résultat d'ensemble du groupe."
],
    "Réécriture à droit constant : l'obligation de déclaration et son délai sont distingués, puis le dépôt centralisé par la société mère est formulé directement. Aucune réforme de fond des réductions, crédits ou délais n'est introduite.",
    "Maintenir les renvois aux articles 220 nonies, 220 R, 223 et 223 A, l'inclusion des réductions et crédits propres à la société mère et le dépôt lors de la déclaration du résultat d'ensemble. Le réemploi des informations ne crée ici aucune dispense de déclaration sans modalités coordonnées."
)

add(13, [
    "Le crédit d'impôt prévu à l'article 220 nonies du code général des impôts s'impute sur l'impôt qui reste dû après l'imputation des prélèvements non libératoires et de tous les autres crédits d'impôt."
],
    "Réécriture à droit constant rendant explicite le rang du crédit d'impôt après les autres imputations citées. Aucune réforme de fond de cet ordre n'est introduite.",
    "Conserver la priorité de tous les autres crédits d'impôt, sans limiter cette priorité aux crédits non restituables comme dans les articles 46 quater-0 YU, 46 quater-0 YW quater et 46 quater-0 YZI."
)

add(14, """
<p>I. - Pour l'application de l'article 220 undecies du code général des impôts, les entreprises doivent déclarer les réductions d'impôt selon le format établi par l'administration. Elles respectent les mêmes délais que pour la déclaration annuelle de résultat qu'elles doivent souscrire en application de l'article 223 du même code.<br /><br />La société mère d'un groupe au sens de l'article 223 A du code général des impôts déclare les réductions d'impôt pour le compte des sociétés du groupe, y compris les siennes, lors du dépôt de la déclaration relative au résultat d'ensemble du groupe.<br /><br />II. - Lorsqu'une entreprise souscrit au capital d'une société de presse remplissant les conditions du I de l'article 220 undecies du code général des impôts, la société de presse doit lui délivrer un état individuel comportant les mentions suivantes :<br /><br />a) L'objet pour lequel l'état est établi ;<br /><br />b) La raison sociale, l'objet social, le siège social et le régime fiscal de la société ;<br /><br />c) L'identité et l'adresse de l'entreprise souscriptrice ;<br /><br />d) Le nombre de titres souscrits ainsi que le montant et la date de leur souscription ;<br /><br />e) La date et le montant des versements effectués.<br /><br />Sur cet état, la société de presse doit attester qu'elle remplit les conditions prévues aux I et VII de l'article 220 undecies du code général des impôts.</p>
""",
    "Réécriture à droit constant : les délais déclaratifs sont isolés dans une phrase, l'obligation de la société de presse de délivrer l'état puis d'y attester son éligibilité est explicite. Les I et II et toutes les mentions a à e restent dans leur ordre. Aucune réforme de fond n'est introduite.",
    "Conserver le rattachement des délais à l'article 223, la centralisation par la société mère selon l'article 223 A et l'attestation des conditions cumulées des I et VII de l'article 220 undecies. Le montant et la date de souscription au d ne se confondent pas avec la date et le montant des versements au e."
)

add(15, [
    "Les frais retenus pour l'application du I de l'article 220 undecies A du code général des impôts sont les suivants :",
    "a) Les dotations aux amortissements fiscalement déductibles relatives à l'acquisition de vélos ;",
    "b) Les dotations aux amortissements ou les charges déductibles relatives à l'achat ou à la location d'équipements nécessaires à la sécurité, notamment les casques, protections, gilets réfléchissants et antivols ;",
    "c) Les frais d'assurance contre le vol et couvrant les déplacements à vélo des salariés entre leur domicile et leur lieu de travail ;",
    "d) Les frais d'entretien des vélos ;",
    "e) Les dotations aux amortissements fiscalement déductibles relatives à la construction ou à l'aménagement d'une aire de stationnement ou d'un local destiné aux vélos ;",
    "f) Les frais afférents à la location d'une aire de stationnement ou d'un local destiné aux vélos.",
    "Les cycles et les cycles à pédalage assisté définis aux 6.10 et 6.11 de l'article R. 311-1 du code de la route ouvrent droit à la réduction d'impôt prévue à l'article 220 undecies A du code général des impôts."
],
    "Réécriture à droit constant de l'introduction, des postes de dépenses et du champ des cycles, en gardant les lettres a à f et les conditions de déductibilité. La dénomination du code de la route est rétablie grammaticalement. Aucune réforme de fond de la réduction d'impôt n'est introduite.",
    "Les amortissements des vélos et des locaux, les équipements de sécurité, les assurances, l'entretien et les locations restent distingués. Le cumul de l'assurance contre le vol et de la couverture des déplacements domicile-travail est conservé. Les renvois aux 6.10 et 6.11 de l'article R. 311-1 du code de la route sont maintenus ; ce code n'est pas dans le corpus fourni pour vérification. La source écrit « code la route » : seule la préposition manquante est rétablie."
)

add(16, [
    "Pour l'application de l'article 220 undecies A du code général des impôts, les entreprises doivent déclarer les réductions d'impôt selon le format établi par l'administration. Elles respectent les mêmes délais que pour la déclaration annuelle de résultat qu'elles doivent souscrire en application de l'article 223 du même code.",
    "La société mère d'un groupe au sens de l'article 223 A du code général des impôts déclare les réductions d'impôt pour le compte des sociétés du groupe, y compris les siennes, lors du dépôt de la déclaration relative au résultat d'ensemble du groupe."
],
    "Réécriture à droit constant : la déclaration et son délai sont exprimés séparément, et l'inclusion des réductions de la société mère est formulée avec un accord grammatical cohérent. Aucune réforme de fond des formalités n'est introduite.",
    "Les articles 220 undecies A, 223 et 223 A, le format administratif et le dépôt avec la déclaration du résultat d'ensemble sont conservés. La source utilise « ceux » pour des réductions d'impôt : la proposition emploie « les siennes » sans changement de champ. Le réemploi des données nécessite des modalités coordonnées avant toute dispense de déclaration."
)

add(17, [
    "Les dépenses retenues pour l'application du IV de l'article 220 terdecies du code général des impôts sont définies ci-après :",
    "1. Pour les dotations aux amortissements mentionnées au 1° du 1, seules sont retenues les dotations fiscalement déductibles correspondant à la période pendant laquelle l'immobilisation a été effectivement utilisée pour créer le jeu vidéo éligible au crédit d'impôt ;",
    "2. Pour les dépenses mentionnées au 2° du 1, sont retenues les rémunérations versées par l'entreprise et les charges sociales qui s'y rapportent, ces charges n'étant retenues que dans la mesure où elles correspondent à des cotisations sociales obligatoires ;",
    "3. Pour les dépenses mentionnées au 3° du 1, sont retenus les rémunérations et leurs accessoires ainsi que les charges sociales qui s'y rapportent, ces charges n'étant retenues que dans la mesure où elles correspondent à des cotisations sociales obligatoires. Pour les salariés employés à titre permanent par l'entreprise de création, seuls sont retenus les salaires et charges sociales correspondant à la période pendant laquelle ces personnels ont été effectivement employés à la création du jeu vidéo éligible au crédit d'impôt ;"
],
    "Réécriture à droit constant : les conditions de déductibilité et d'utilisation effective sont regroupées au 1, et la restriction aux cotisations sociales obligatoires est explicitement rattachée aux charges sociales aux 2 et 3. La limitation propre aux salariés permanents est conservée. Aucune réforme de fond de l'assiette n'est introduite.",
    "Conserver les renvois au IV, puis aux 1° du 1, 2° du 1 et 3° du 1 de l'article 220 terdecies. Les accessoires de rémunération ne figurent qu'au 3. Les durées d'utilisation effective de l'immobilisation et d'emploi effectif du personnel permanent restent les périodes de rattachement. Aucun allègement salarial ou patronal du projet n'est assimilé à une nouvelle dépense éligible."
)

add(18, [
    "Pour l'application des articles 220 terdecies et 220 X du code général des impôts, les entreprises doivent déposer auprès du service des impôts une déclaration spéciale conforme au modèle établi par l'administration, avec le relevé de solde mentionné à l'article 360.",
    "Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère doit joindre les déclarations spéciales des sociétés du groupe au relevé de solde relatif au résultat d'ensemble.",
    "Une copie de la déclaration spéciale doit être adressée au Centre national du cinéma et de l'image animée dans le même délai."
],
    "Réécriture à droit constant : le service destinataire est placé auprès de l'obligation de dépôt et les obligations de la société mère et d'envoi de la copie sont explicites. Aucune réforme de fond des modalités déclaratives n'est introduite.",
    "Conserver le dépôt avec le relevé de solde de l'article 360, les articles 220 terdecies, 220 X et 223 A et le même délai pour la copie au Centre national du cinéma et de l'image animée. La note relative à l'article 3, premier alinéa, de l'ordonnance n° 2009-901 du 24 juillet 2009 est historique et ne fixe aucune entrée en vigueur future. Une suppression de la copie au titre du réemploi des données exigerait une transmission coordonnée au Centre."
)

add(19, [
    "Le crédit d'impôt prévu à l'article 220 terdecies du code général des impôts s'impute sur l'impôt qui reste dû après l'imputation des prélèvements non libératoires et des crédits d'impôt non restituables."
],
    "Réécriture à droit constant centrée sur l'ordre des imputations. Aucune réforme de fond du crédit d'impôt pour la création de jeux vidéo ou de son rang n'est introduite.",
    "Conserver le renvoi à l'article 220 terdecies et le rang postérieur aux prélèvements non libératoires et aux crédits d'impôt non restituables, sans étendre cette priorité à tous les autres crédits."
)

add(20, [
    "L'imposition des plus-values ou moins-values réalisées par les caisses de crédit mutuel agricole et rural lors de la cession d'éléments d'actif immobilisés ou de titres de placement ne porte que sur leur fraction acquise à compter du 1er janvier 1985.",
    "Pour les titres cotés, cette fraction est calculée en prenant pour prix de revient leur cours moyen du mois de décembre 1984.",
    "Pour les titres de participation non cotés, les autres éléments d'actif immobilisés et les titres de placement non cotés, la fraction acquise à compter du 1er janvier 1985 est calculée en appliquant à la plus-value ou moins-value le rapport entre la durée de détention du bien depuis cette date et sa durée totale de détention. Pour les biens amortissables détenus depuis plus de deux ans, la partie de la plus-value ou moins-value réputée à court terme est, en outre, plafonnée au montant des amortissements déduits à compter du 1er janvier 1985 pour le calcul de l'impôt."
],
    "Réécriture à droit constant : le champ historique de l'imposition et les deux méthodes de calcul sont formulés directement ; le rapport des durées et le plafond applicable au court terme sont explicités. Aucune réforme de fond n'est apportée au régime des caisses.",
    "Conserver le 1er janvier 1985 à chaque occurrence, le cours moyen de décembre 1984, les trois catégories non cotées et la condition de détention de plus de deux ans. Les dates anciennes définissent des fractions encore susceptibles d'être pertinentes ; elles ne sont ni actualisées ni prises pour des dates d'entrée en vigueur du projet. La réforme du taux normal de l'IS ne modifie pas ces règles de détermination du bénéfice."
)

add(21, [
    "Les provisions figurant au bilan de clôture de l'exercice 1984, à l'exception des provisions pour risques sur crédit à moyen ou à long terme mentionnées à l'article 46 quater-0 ZB, sont considérées comme des réserves exonérées de l'impôt lorsqu'elles ne remplissent pas les conditions du 5° du 1 de l'article 39 du code général des impôts ou lorsqu'elles deviennent sans objet."
],
    "Réécriture à droit constant : le rattachement au bilan de clôture de 1984 est placé immédiatement après les provisions concernées, puis l'exception et les deux conditions alternatives sont formulées explicitement. Aucune réforme de fond du régime historique n'est introduite.",
    "Maintenir l'exercice 1984, l'exclusion des provisions pour risques sur crédit à moyen ou à long terme et le renvoi au 5° du 1 de l'article 39. L'article 46 quater-0 ZB n'est pas retrouvé dans le fichier public impots-annexe-3.json fourni ; son renvoi est conservé, sans création d'un article de remplacement ni supposition sur son abrogation. La source ne ferme pas nettement l'incise d'exception avant « existant au bilan de clôture de l'exercice 1984 » : la proposition rattache cette précision à l'ensemble des provisions visées ; ce rattachement appelle un contrôle de la ponctuation source. Vérifier la portée historique du renvoi avant toute coordination."
)

add(22, [
    "Les options prévues aux premier, deuxième, quatrième et cinquième alinéas du I de l'article 223 A du code général des impôts doivent être notifiées au service des impôts auprès duquel la déclaration du résultat d'ensemble est souscrite.",
    "La société mère doit transmettre à ce même service les documents suivants :",
    "1. Lors de la notification de l'option :",
    "a) La liste des personnes morales et des établissements stables qui seront membres du groupe. Pour chaque société mentionnée au b, cette liste précise sa désignation, l'adresse de son siège social et la répartition de son capital. Pour chaque autre personne morale, elle précise sa désignation, l'adresse de son siège social et, le cas échéant, celle de son établissement stable, ainsi que la nature du lien qui l'unit à l'entité tête du groupe formé en application du quatrième ou du cinquième alinéa du I de l'article 223 A du code général des impôts ;",
    "a bis) La liste des personnes morales et des établissements stables qui seront qualifiés de sociétés intermédiaires. Pour chaque société mentionnée au b bis, cette liste précise sa désignation, l'adresse de son siège social, l'impôt étranger équivalent à l'impôt sur les sociétés auquel elle est soumise et la répartition de son capital. Pour chaque autre personne morale, elle précise sa désignation, l'adresse de son siège social et, le cas échéant, celle de son établissement stable, l'impôt étranger équivalent à l'impôt sur les sociétés auquel elle ou son établissement stable est soumis, ainsi que la nature du lien qui l'unit à l'entité tête du groupe formé en application du quatrième ou du cinquième alinéa du I de l'article 223 A du code général des impôts ;",
    "a ter) La liste des personnes morales et des établissements stables qui seront qualifiés de sociétés étrangères, avec la désignation de l'entité mère non résidente. Pour chaque société étrangère et pour l'entité mère non résidente, cette liste précise sa désignation, l'adresse de son siège social, l'impôt étranger équivalent à l'impôt sur les sociétés auquel elle est soumise et la répartition de son capital. Pour chaque autre personne morale, elle précise sa désignation, l'adresse de son siège social et, le cas échéant, celle de son établissement stable, ainsi que l'impôt étranger équivalent à l'impôt sur les sociétés auquel elle ou son établissement stable est soumis ;",
    "b) Les attestations par lesquelles les sociétés filiales donnent leur accord à la prise en compte de leurs propres résultats par la société mère pour déterminer le résultat d'ensemble ;",
    "b bis) Les attestations par lesquelles les sociétés filiales donnent leur accord pour être qualifiées de sociétés intermédiaires ;",
    "b ter) Les attestations par lesquelles l'entité mère non résidente et les sociétés étrangères donnent leur accord à l'option de la société mère dans les conditions du deuxième alinéa du I de l'article 223 A du code général des impôts.",
    "Les sociétés membres d'un groupe constitué en application du deuxième alinéa du I de l'article 223 A du code général des impôts, autres que la société mère, doivent joindre à leurs attestations mentionnées au b les attestations par lesquelles l'entité mère non résidente et, s'il y a lieu, les sociétés étrangères donnent leur accord à la prise en compte des résultats de ces sociétés membres pour déterminer le résultat d'ensemble ;",
    "c) Le cas échéant, le document mentionné au premier alinéa du c du 6 de l'article 223 L du code général des impôts ou au deuxième alinéa du g du 6 du même article. Ce document comporte la liste et les attestations précédemment mentionnées.",
    "2. Au plus tard à l'expiration du délai de dépôt de la déclaration de résultat de chacun des exercices arrêtés pendant la période de validité de l'option :",
    "a) La liste des sociétés qui seront membres du groupe défini à l'article 223 A du code général des impôts pour l'exercice suivant ;",
    "a bis) La liste des sociétés intermédiaires définies à l'article 223 A du code général des impôts, ainsi que celle des sociétés qui cessent d'être qualifiées de sociétés intermédiaires au titre de l'exercice suivant ;",
    "a ter) La liste des sociétés qui seront qualifiées de sociétés étrangères au sens de l'article 223 A du code général des impôts pour l'exercice suivant, ainsi que celle des sociétés qui cessent d'avoir cette qualification au titre de ce même exercice ;",
    "b) Les attestations mentionnées au b du 1, produites par les sociétés qui seront membres du groupe à compter de cet exercice suivant ;",
    "b bis) Les attestations mentionnées au b bis du 1, produites par les sociétés qui seront qualifiées de sociétés intermédiaires à compter de cet exercice suivant ;",
    "b ter) Les attestations mentionnées au b ter du 1, par lesquelles l'entité mère non résidente et les sociétés étrangères donnent les accords prévus au même b ter du 1 et applicables à compter de cet exercice suivant ;",
    "c) Le cas échéant, l'extrait de l'annexe comptable qui indique, pour les comptes combinés, le nom de l'entreprise combinante, la liste des entreprises du périmètre de combinaison et une description de la nature des liens fondant les critères de sélection des entreprises dont les comptes sont combinés. Cet extrait indique aussi les motifs justifiant la non-combinaison de certaines entreprises ;",
    "d) Le cas échéant, la référence de l'agrément collectif délivré par l'Autorité de contrôle prudentiel et de résolution pour la société mère elle-même et pour les caisses locales qui la détiennent.",
    "2 bis. Dans les trois mois de l'acquisition des titres d'une société du groupe, d'une autre société intermédiaire ou d'une société étrangère, la société mère transmet l'attestation mentionnée au b bis du 1, produite par la société qui sera qualifiée de société intermédiaire à compter de l'exercice au cours duquel l'acquisition est intervenue, ou l'attestation mentionnée, selon le cas, au premier ou au second alinéa du b ter du 1, produite par la société qui sera qualifiée de société étrangère à compter de ce même exercice.",
    "3. Lorsque le capital de la société mère vient à être détenu à hauteur de 95 % au moins, directement ou indirectement, par une personne morale passible de l'impôt sur les sociétés dans les conditions du premier alinéa du d du 6 de l'article 223 L du code général des impôts, la société mère transmet une lettre en même temps que la déclaration du résultat d'ensemble de l'exercice concerné. Cette lettre est signée des représentants dûment mandatés de la société mère et de la société détentrice des titres. Elle précise la nature, les circonstances et les justifications juridiques, économiques ou sociales de l'opération à l'origine de cette détention.",
    "Les dispositions du premier alinéa s'appliquent aussi lorsque le capital de l'entité mère non résidente vient à être détenu à hauteur de 95 % au moins, directement ou indirectement, par une autre personne morale passible de l'impôt sur les sociétés, ou par une autre société ou un autre établissement stable remplissant les conditions du deuxième alinéa du I de l'article 223 A du code général des impôts, dans les conditions du premier alinéa du d du 6 de l'article 223 L du même code. Dans ce cas, les représentants dûment mandatés de l'entité mère non résidente et de la personne morale détentrice des titres signent la lettre mentionnée au premier alinéa.",
    "4. L'accord donné par une société étrangère pour se substituer à l'entité mère non résidente, mentionné au deuxième alinéa du k du 6 de l'article 223 L du code général des impôts, doit être transmis lorsque l'Etat dans lequel cette entité est soumise à un impôt équivalent à l'impôt sur les sociétés se retire de l'Union européenne ou de l'accord sur l'Espace économique européen. Cet accord est transmis au plus tard à l'expiration du délai de dépôt de la déclaration de résultat de l'exercice au cours duquel le retrait intervient."
],
    "Réécriture à droit constant des notifications du groupe : les longues phrases décrivant les listes sont scindées selon les personnes concernées, et les obligations de transmission, leurs échéances et les signataires sont exprimés directement. Les 24 alinéas, les subdivisions 1, 2, 2 bis, 3 et 4 et toutes leurs lettres sont maintenus dans le même ordre, notamment les deux alinéas du b ter du 1. Aucune réforme de fond du régime des groupes n'est introduite.",
    "Conserver le délai de trois mois du 2 bis, les deux seuils de 95 % au moins, les déclarations initiales et annuelles, les accords distincts et les renvois aux subdivisions de 223 A et de 223 L. Les alinéas visés par le b ter du 1 ne sont pas déplacés. Au second alinéa du 3, la source emploie « premier alinéa » sans préciser « du 3 » ; ce renvoi ambigu est maintenu et doit être clarifié par coordination expresse si nécessaire. Au 2 d, « elle-même » est explicité comme désignant la société mère, conformément au cinquième alinéa du I de l'article 223 A du corpus. La note relative à l'article 24-I de la loi n° 2013-672 du 26 juillet 2013 est historique. Le réemploi des listes et attestations appelle des modalités de mise à jour et de transmission ; il ne permet pas de supprimer les accords exigés par l'article 223 A."
)

add(23, [
    "Les sociétés filiales qui acceptent d'entrer dans le groupe défini à l'article 223 A du code général des impôts doivent adresser au service dont elles relèvent l'attestation mentionnée à l'article 46 quater-0 ZD. Elles la transmettent au plus tard à l'expiration du délai de dépôt de la déclaration de résultat de l'exercice précédant celui au titre duquel le régime défini à l'article 223 A s'applique. Leur accord reste valable jusqu'à leur sortie du groupe. Il peut être dénoncé au plus tard à l'expiration du délai de dépôt de la déclaration de résultat du dernier exercice précédant la période couverte par le renouvellement de l'option prévu au deuxième alinéa du III de l'article 223 A.",
    "Lorsque, sur décision de la société mère, les résultats d'un exercice d'une société filiale cesseront d'être pris en compte dans le résultat d'ensemble, cette filiale doit en informer le service des impôts dont elle relève. Elle le fait au plus tard à l'expiration du délai de dépôt de la déclaration de résultat de l'exercice précédent.",
    "Pour satisfaire aux obligations du présent article et de l'article 46 quater-0 ZD, la société doit utiliser des documents conformes aux modèles établis par l'administration."
],
    "Réécriture à droit constant : les obligations d'attestation, leur délai, la durée de l'accord et sa dénonciation sont répartis en phrases distinctes ; l'obligation d'informer en cas de sortie décidée par la société mère est rattachée expressément à la filiale. Les trois alinéas et leurs règles sont conservés. Aucune réforme de fond n'est introduite.",
    "Conserver les deux délais fondés sur l'exercice précédent, la validité de l'accord jusqu'à la sortie du groupe, le délai propre à sa dénonciation avant renouvellement et les modèles administratifs. Les renvois à 46 quater-0 ZD et au deuxième alinéa du III de l'article 223 A sont maintenus ; ce dernier porte, dans le corpus public, les règles de durée et de reconduction des options et accords. Aucune dispense de modèle ou d'accord n'est déduite de l'orientation de réemploi des données."
)


assert len(sources) == 24
assert set(drafts) == set(range(24))
answer = []
for i, source in enumerate(sources):
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[i])
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
