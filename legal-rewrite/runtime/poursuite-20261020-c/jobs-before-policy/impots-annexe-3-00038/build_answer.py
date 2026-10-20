import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def paras(*items):
    return '\n'.join('<p>' + item + '</p>' for item in items)


def tables(number):
    root = ET.fromstring('<root>' + by_number[number]['source_xml'] + '</root>')
    result = []
    for table in root.findall('table'):
        for elem in table.iter():
            for attr in list(elem.attrib):
                if attr not in ('rowspan', 'colspan'):
                    del elem.attrib[attr]
        result.append(ET.tostring(table, encoding='unicode').strip())
    return result


def add(number, xml, reason, notes, benefit=None, removed=None, repeal=None):
    source = by_number[number]
    result = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    if benefit is not None:
        result['benefit_review'] = benefit
    if removed:
        result.update(change_type='normative_reduction',
                      reform_policy_id='editorial_direction_2026_10_19',
                      removed_provisions=removed)
    if repeal:
        result.update(change_type='full_repeal',
                      repeal_policy_id='editorial_direction_2026_10_19',
                      repeal_scope=repeal)
    answers[number] = result


add('322 K', paras(
    "Lorsque, aux dates prévues à l'article 322 J, l'entreprise ne remplit pas encore les conditions requises, elle peut bénéficier provisoirement de l'exonération temporaire de cotisation foncière des entreprises. L'indication de ce bénéfice provisoire dans la déclaration prévue à l'article 1477 du code général des impôts vaut demande. Il n'est exigé ni demande distincte, ni état spécial des réalisations déjà effectuées, ni exposé prévisionnel des moyens d'atteindre les seuils réglementaires. L'exonération devient définitive si l'entreprise remplit les conditions requises au 31 décembre de la troisième année de l'opération. Si l'exercice ne coïncide pas avec l'année civile, cette date est remplacée, pour les seules immobilisations, par la date de clôture de l'exercice de douze mois clos au cours de cette troisième année. Cette échéance ne peut être reportée. La réalisation des conditions peut être établie par tout moyen dans le cadre des procédures de contrôle et de réclamation applicables ; elle n'est pas subordonnée au dépôt d'une justification spéciale à cette échéance. L'administration utilise les informations et pièces exactes déjà légalement à sa disposition, sans en exiger une nouvelle production.",
    "Ces simplifications s'appliquent aux demandes présentées et aux procédures en cours à compter de l'entrée en vigueur de la loi portant la présente réforme. Elles ne rouvrent pas une décision devenue définitive et ne modifient ni la période d'exonération ni la date à laquelle les conditions de fond doivent être remplies."
),
    "Réforme de fond : suppression du dossier prévisionnel accompagnant le bénéfice provisoire, de la demande séparée et de la justification spéciale à produire à l'échéance. L'indication dans la déclaration fiscale existante suffit ; les données déjà disponibles sont réutilisées. À droit constant, maintien du bénéfice provisoire, des seuils applicables, du contrôle de leur réalisation et des deux modalités de l'échéance de troisième année.",
    "Renvois vérifiés dans le corpus : 322 J fixe l'appréciation initiale et 322 G les seuils ; le CGI 1465 impose notamment l'indication lors de la première déclaration et conserve une durée maximale de cinq ans ainsi que les conditions de l'article 14 du règlement (UE) n° 651/2014. La présente simplification conserve cette indication et ne dispense pas des obligations législatives autonomes de 1465 ou 1477. Conserver le 31 décembre, la troisième année, les douze mois et l'exception limitée aux immobilisations. Le défaut de réalisation des conditions de fond demeure contrôlable ; aucune réouverture générale des anciennes décisions n'est créée.",
    benefit="L'avantage est l'accès provisoire à l'exonération de CFE malgré des seuils non encore atteints aux dates de 322 J, puis son acquisition définitive si les conditions sont remplies à l'échéance. Il demeure ouvert aux opérations futures éligibles ; le report propre aux immobilisations des exercices décalés et toute la durée légale sont conservés. Les formalités sont réduites sans retrancher l'exonération ni déplacer ses conditions de fond.",
    removed=[
        "Suppression de la demande distincte du bénéfice provisoire lorsque celui-ci est indiqué dans la déclaration fiscale existante.",
        "Suppression de l'état spécial des réalisations déjà effectuées et de l'exposé prévisionnel des moyens d'atteindre les seuils réglementaires.",
        "Suppression du dépôt d'une justification spéciale à l'échéance et de la nouvelle production de pièces exactes déjà légalement disponibles."
    ])

add('322 L', paras(
    "Si, au cours d'une année, l'investissement net ou le nombre net d'emplois créés devient inférieur au seuil correspondant fixé à l'article 322 G, l'exonération cesse de s'appliquer à compter du 1er janvier de l'année suivante."
),
    "Réécriture à droit constant : la condition de cessation et sa prise d'effet sont exprimées directement. Cette disposition ne crée pas de déclaration supplémentaire. La cessation ne peut être supprimée isolément : elle met en œuvre les conditions de maintien de l'exonération prévues par le CGI 1465 et un régime d'aides européennes à coordonner.",
    "Lecture de 322 G et de 1465 effectuée : la baisse de l'un ou l'autre indicateur suffit selon le seuil applicable ; le texte ne transforme pas les voies alternatives de 322 G en conditions cumulatives. Le 1er janvier suivant est conservé, sans reprise rétroactive sur le seul fondement de cet article. Le CGI 1465 prévoit une cessation pour la période restant à courir et impose l'article 14 du règlement (UE) n° 651/2014 ; une suppression générale de ces conditions demanderait une coordination législative et européenne distincte.",
    benefit="Le présent article ne crée pas une taxe mais limite la durée d'une exonération de CFE lorsque les conditions d'éligibilité cessent d'être remplies. Le bénéfice antérieur à la cessation reste préservé par la prise d'effet au seul 1er janvier suivant. Les exonérations demeurent accessibles aux futures opérations éligibles, selon les seuils et les voies alternatives de 322 G, sans condition nouvelle.")

add('322 N', paras(
    "La demande d'exonération de cotisation foncière des entreprises est portée sur la déclaration prévue à l'article 1477 du code général des impôts, dans les conditions fixées par cet article. Cette indication vaut demande ; aucun formulaire de demande distinct n'est exigé. Les informations et pièces exactes déjà légalement détenues par l'administration ne sont pas produites une seconde fois.",
    "Ces simplifications s'appliquent, à compter de l'entrée en vigueur de la loi portant la présente réforme, aux demandes nouvelles et aux demandes en cours. Elles ne modifient pas les conditions de fond de l'exonération et ne rouvrent pas les délais de réclamation expirés."
),
    "Réforme de fond : la demande est intégrée à la déclaration de CFE existante, avec suppression du formulaire distinct et des pièces fournies en double. Le renvoi aux conditions de l'article 1477 est maintenu ; aucune nouvelle déclaration ni condition d'accès à l'exonération n'est créée.",
    "Le CGI 1477, lu dans le corpus, règle les déclarations annuelles et provisoires et leurs échéances ; le CGI 1465 exige l'indication de l'exonération au plus tard lors de la première déclaration comportant les éléments nouveaux et maintient la déclaration annuelle des éléments concernés. Ces obligations législatives ne sont pas supprimées par le présent texte. Coordonner les formulaires administratifs correspondants pour qu'aucun dépôt autonome ni pièce déjà disponible ne soit rétabli. Les prescriptions et décisions définitives ne sont pas rouvertes.",
    benefit="L'exonération de CFE demandée sur le fondement des dispositions auxquelles renvoie cet article est conservée pour tous les bénéficiaires futurs éligibles. L'intégration de la demande dans la déclaration existante facilite son accès, sans réduire le montant, la durée ou le champ de l'avantage et sans substituer une nouvelle obligation à la formalité supprimée.",
    removed=[
        "Suppression du formulaire autonome de demande d'exonération en plus de l'indication portée sur la déclaration de CFE existante.",
        "Suppression de la seconde production d'informations et de pièces exactes déjà légalement détenues par l'administration."
    ])

add('322 O', paras(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. À compter de cette date, l'exploitation, dans une même commune, d'établissements situés dans et hors d'une zone franche urbaine-territoire entrepreneur n'entraîne plus, sur le seul fondement du présent article, de déclaration séparée pour chacun des établissements situés dans cette zone. Aucun dépôt ni rattrapage de ces déclarations spéciales ne peut être exigé après cette date.",
    "Cette abrogation ne modifie ni le champ territorial, ni les conditions, ni la durée des exonérations et autres avantages légalement applicables aux établissements de la zone, y compris pour les situations futures éligibles. Les déclarations de droit commun légalement requises demeurent applicables ; aucune déclaration spéciale de remplacement n'est instituée. Les impositions afférentes aux années antérieures, leurs exonérations, restitutions, prescriptions et recours restent régis par les règles qui leur sont applicables, sous réserve de la suppression des dépôts spéciaux prévue au premier alinéa et des règles relatives à l'application des sanctions plus douces."
),
    "Abrogation de fond de l'obligation réglementaire de déclarer séparément les établissements situés en ZFU dans une commune où l'entreprise exploite aussi des établissements hors zone. La localisation et les bases restent traitées dans le circuit fiscal de droit commun ; aucun circuit spécial de remplacement n'est créé. Les exonérations territoriales sont expressément conservées, également pour l'avenir.",
    "La note source rattache la rédaction à la loi n° 2014-173 du 21 février 2014, articles 27-2° b et 30-II, et à la loi n° 2014-1655 du 29 décembre 2014, article 48-III ; elle ne fixe pas la date de cette réforme. Le CGI 1477 conserve ses déclarations de droit commun. Coordonner les formulaires et les dispositions d'application des exonérations ZFU du CGI 1466 A pour retirer le dépôt séparé de ce seul article sans étendre les bases exonérées aux établissements hors zone ni fermer les avantages futurs légalement ouverts. Aucune dette fiscale ancienne n'est effacée par la suppression d'une formalité.",
    benefit="La déclaration séparée n'est pas un avantage. Elle accompagne néanmoins les exonérations territoriales des établissements en ZFU : leur assiette, leur durée et leurs conditions légales restent applicables aux années anciennes et aux situations futures éligibles. Le seul regroupement du circuit déclaratif ne transfère pas l'exonération aux établissements hors zone et ne supprime aucun droit en zone.",
    repeal="Obligation spéciale de déposer séparément les éléments de CFE de chaque établissement en ZFU dans une commune comprenant aussi des établissements hors zone, sans suppression des exonérations territoriales.")

add('322 R', paras(
    "Pour le dispositif prévu au 3° du III de l'article 1466 F du code général des impôts, le champ des activités éligibles est celui défini à l'article 49 ZC."
),
    "Réécriture à droit constant du rattachement des activités éligibles. Cette règle ouvre le champ d'un abattement favorable et n'impose aucune formalité propre ; sa suppression pourrait retirer l'accès à l'avantage et n'est pas retenue.",
    "Lecture du CGI 1466 F et de l'article 49 ZC dans le corpus : le 3° du III de 1466 F vise l'activité principale dans les secteurs du 3° du III de 44 quaterdecies ; 49 ZC en précise les activités. Le renvoi demeure dynamique, sans figer les listes ni leurs restrictions. Le présent article ne modifie ni l'abattement de 80 %, ni sa majoration à 100 %, ni le plafond de 150 000 € de 1466 F. Il ne rétablit aucune CVAE.")

add('323', paras(
    "Pour établir l'assiette de la cotisation foncière des entreprises due par les entreprises hydrauliques concédées ou d'une puissance supérieure à 500 kilowatts, la valeur locative de la force motrice des chutes d'eau et de leurs aménagements utilisés par ces entreprises est répartie entre les communes sur le territoire desquelles se trouvent les ouvrages définitifs de génie civil et celles sur le territoire desquelles coulent les cours d'eau utilisés. Cette répartition suit les règles des articles 316 à 321 B."
),
    "Réécriture à droit constant : séparation de la règle de répartition et de son renvoi technique. Il s'agit de répartir une valeur locative, sans prélèvement accessoire ni dossier nouveau ; supprimer ce mécanisme laisserait sans règle la répartition entre les communes intéressées.",
    "Articles 316, 317, 318, 319, 320, 321 et 321 B lus dans le corpus : ouvrages, retenues et puissance indisponible participent à la répartition, avec la formule p = 0,5 (a + b) de 319. Le renvoi d'ensemble est conservé sans modifier ces calculs, leurs notifications ou les dispositions de retard. Maintien de l'alternative entre concession et puissance strictement supérieure à 500 kilowatts ; aucune extension à tous les producteurs hydrauliques.")

add('324 A', paras(
    "Pour l'application de l'article 1494 du code général des impôts, les termes suivants ont le sens ci-dessous :",
    "1° Une propriété normalement destinée à une utilisation distincte est :",
    "a. Pour les biens autres que les établissements industriels, l'ensemble des sols, terrains et bâtiments appartenant au même groupement topographique et normalement destinés, en raison de leur agencement, à être utilisés par un même occupant ;",
    "b. Pour les établissements industriels, l'ensemble des sols, terrains, bâtiments et installations qui concourent à une même exploitation et appartiennent au même groupement topographique.",
    "2° Une fraction de propriété normalement destinée à une utilisation distincte est, dans un immeuble collectif ou un ensemble immobilier :",
    "a. Le local normalement destiné, en raison de son agencement, à être utilisé par un même occupant ;",
    "b. L'établissement industriel dont les éléments concourent à une même exploitation.",
    "L'ensemble des sols, terrains, bâtiments et parties de bâtiment réservés à l'usage commun des occupants constitue également une fraction de propriété. Un immeuble collectif est une propriété bâtie normalement aménagée pour recevoir au moins deux occupants."
),
    "Réécriture à droit constant des définitions de l'unité d'évaluation, avec ponctuation des énumérations et distinction des deux catégories de biens. Ces définitions délimitent l'assiette des impôts maintenus ; elles ne constituent ni une autorisation ni une déclaration retirable isolément.",
    "Renvoi au CGI 1494 vérifié : l'évaluation s'opère pour chaque propriété ou fraction destinée à une utilisation distincte. Maintien des 1° et 2°, des a et b, du groupement topographique, de l'unicité d'occupant ou d'exploitation, des parties communes et du minimum de deux occupants. L'unité normalement destinée à un occupant ne dépend pas d'une occupation effective unique.")

add('324 B', paras(
    "I. - Pour l'application de l'article 1495 du code général des impôts, la date de l'évaluation est le jour de clôture du procès-verbal des opérations de révision dans la commune.",
    "II. - La consistance est appréciée en tenant compte de tous les travaux, équipements et éléments d'équipement existant au jour de l'évaluation.",
    "III. - Lorsqu'une propriété ou un local comporte plusieurs affectations principales, chaque fraction est évaluée selon son affectation particulière.",
    "Toutefois, les règles de l'article 1498 du code général des impôts s'appliquent à un même élément utilisé à la fois pour une activité commerciale ou artisanale et pour un autre usage, ou à la fois pour une profession sans caractère agricole, commercial, artisanal ou industriel et pour l'habitation.",
    "IV. - Lorsqu'une propriété ou un local n'a qu'une affectation principale, un même élément utilisé à plusieurs usages est évalué selon les règles applicables à la partie principale de cette propriété ou de ce local."
),
    "Réécriture à droit constant : les dates, la consistance et les cas d'affectation mixte sont exprimés en phrases directes dans leurs subdivisions. Le classement des usages demeure nécessaire au choix de la méthode d'évaluation et ne crée pas de formalité autonome à supprimer.",
    "CGI 1495 et 1498 lus : le second alinéa de 1495 écarte son premier alinéa pour les propriétés du I de 1498. Le présent renvoi réglementaire ne neutralise pas cette exclusion législative. Les deux hypothèses précises du III et la règle différente d'affectation principale du IV sont conservées ; aucune application générale du régime professionnel à tous les logements mixtes n'est ajoutée.")

add('324 C', paras(
    "I. - Sous réserve du 1 du III de l'article 1496 du code général des impôts, les actes de location retenus pour évaluer les propriétés ou fractions de propriétés mentionnées au I de l'article 1498 du même code et aux articles 324 D à 324 Y sont les baux écrits ou locations verbales en cours à la date de référence, librement conclus à des conditions de prix normales.",
    "II. - Le loyer prévu par le bail écrit ou la location verbale est corrigé, s'il y a lieu, selon les règles suivantes :",
    "Il est diminué de la fraction de valeur locative correspondant aux éléments compris dans la location qui ne sont pas imposables à la taxe foncière sur les propriétés bâties, des charges normalement supportées par le locataire mais payées par le propriétaire et des dépenses diverses payées par ce dernier en contrepartie de prestations fournies aux occupants ;",
    "Il est augmenté des dépenses normalement supportées par le propriétaire mais payées par le locataire. La plus-value résultant des travaux d'amélioration effectués par le locataire ne donne pas lieu à une majoration du loyer retenu pour l'évaluation.",
    "La suppression de cette dernière majoration s'applique aux évaluations servant à établir les impositions dont le fait générateur intervient à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque le bail ou les travaux lui sont antérieurs. Les impositions dont le fait générateur est antérieur, leurs dégrèvements, restitutions, prescriptions et recours restent soumis aux règles antérieures. Cette suppression ne modifie pas les autres règles d'appréciation de la consistance ou de classement des locaux et n'autorise aucune majoration compensatrice."
),
    "Réforme de fond : retrait de la majoration du loyer de référence correspondant à la plus-value des améliorations effectuées par le locataire, afin de ne plus ajouter cette charge d'évaluation à ses travaux. Maintien des trois diminutions favorables et de l'ajustement pour les charges du propriétaire payées par le locataire, qui empêche de minorer artificiellement le loyer en transférant des charges. Réécriture à droit constant du reste, dont la réserve du régime des loyers réglementés.",
    "CGI 1496 et 1498 lus ; le 1 du III de 1496 conserve notamment son régime historique spécifique. La coupe porte sur le loyer de comparaison, sans prétendre effacer l'effet des travaux dans la consistance du bien ou dans toutes les autres méthodes d'évaluation. Coordonner l'établissement et la mise à jour des tarifs de 1496, 1517 et 1518 et les instructions de calcul afin de retirer cette majoration pour les faits générateurs nouveaux, sans hausse compensatrice. Ces coordinations hors lot ne sont pas présentées comme rédigées. La transition ne crée pas de restitution générale des anciennes impositions. Les baux verbaux et la date de référence sont conservés.",
    benefit="Les diminutions pour éléments non imposables, charges locatives payées par le propriétaire et prestations aux occupants restent intégralement applicables aux évaluations futures. La réserve du régime favorable de l'article 1496 III 1 subsiste. La seule majoration retirée est celle des améliorations du locataire ; aucune réduction préexistante n'est supprimée en contrepartie.",
    removed=[
        "Suppression, pour les impositions nouvelles, de la majoration du loyer de référence correspondant à la plus-value des travaux d'amélioration effectués par le locataire."
    ])

add('324 D', paras(
    "I. - Une propriété affectée à l'habitation et normalement destinée à une utilisation distincte comprend, pour son évaluation :",
    "La maison ;",
    "Les dépendances bâties ;",
    "Les dépendances non bâties.",
    "II. - La maison constitue la partie principale. Elle comprend tous les éléments situés à l'intérieur des gros murs du corps de bâtiment principal ou reliés à celui-ci par une communication intérieure.",
    "III. - Les dépendances bâties sont les constructions accessoires au bâtiment principal qui ne communiquent pas intérieurement avec lui.",
    "IV. - Les dépendances non bâties comprennent les cours, passages et, plus généralement, tous les terrains qui constituent une dépendance indispensable et immédiate des constructions et leur servent de voies d'accès ou de dégagement."
),
    "Réécriture à droit constant : définition de la maison en deux phrases et clarification des liens physiques distinguant les dépendances. Cette décomposition commande les pondérations favorables et ne peut être supprimée sans perturber leur application ; aucune démarche autonome n'est imposée.",
    "Maintien des subdivisions I à IV et des trois alinéas de l'énumération. La communication intérieure demeure le critère des dépendances bâties ; les terrains du IV doivent être à la fois indispensables, immédiats et utilisés pour l'accès ou le dégagement. Aucun ensemble de terrains supplémentaire n'est incorporé à l'assiette par la réécriture.",
    benefit="La distinction entre maison, dépendances bâties et dépendances non bâties n'est pas, en elle-même, une exonération. Elle permet néanmoins d'appliquer les traitements distincts et pondérations des dépendances, dont les coefficients réduits de 324 N et la prise en compte de la situation de 324 R. Toutes ces qualifications restent disponibles pour les biens futurs comme pour les biens existants ; aucun terrain supplémentaire n'est assimilé à une dépendance imposable.")

add('324 E', paras(
    "I. - Dans une fraction de propriété affectée à l'habitation et normalement destinée à une utilisation distincte, l'évaluation distingue :",
    "La partie principale ;",
    "Les éléments bâtis formant dépendances ;",
    "Une quote-part des dépendances non bâties.",
    "II. - Dans un immeuble collectif, la partie principale est l'ensemble des éléments d'un seul tenant qui forment, à l'intérieur des gros murs d'un même bâtiment, une unité d'habitation, telle qu'un logement ou un appartement.",
    "III. - Dans ces immeubles, les éléments bâtis formant dépendances comprennent :",
    "D'une part, les éléments situés hors du bâtiment qui abrite la partie principale ;",
    "D'autre part, les éléments situés dans le même bâtiment que la partie principale à laquelle ils se rattachent, mais qui ne sont pas d'un seul tenant avec elle."
),
    "Réécriture à droit constant : présentation directe de l'unité d'habitation et des deux catégories d'éléments formant dépendances. La distinction évite d'assimiler automatiquement toutes les annexes à la partie principale ; aucune obligation déclarative ou autorisation n'est créée par cet article.",
    "Les trois éléments du I et les deux branches du III sont conservés. La quote-part des dépendances non bâties n'est pas transformée en prise en compte de leur totalité. L'expression source « d'une seule tenue » est explicitée par « d'un seul tenant », en cohérence avec le II, sans déplacer les éléments d'évaluation.")

add('324 F', paras(
    "Une construction accessoire isolée est toujours classée parmi les dépendances bâties lorsqu'aucune partie principale à laquelle elle puisse être rattachée ne se trouve sur la même propriété."
),
    "Réécriture à droit constant de la qualification applicable aux constructions accessoires isolées. Cette règle permet l'accès au traitement propre aux dépendances même en l'absence de partie principale ; la retirer pourrait rendre leur évaluation moins favorable.",
    "Le caractère accessoire et isolé, l'absence de partie principale de rattachement et l'exigence de même propriété sont tous conservés. La qualification ne dépend pas de l'existence d'un logement sur une autre propriété et ne constitue pas une nouvelle autorisation de construire.")

add('324 G', paras(
    "I. - La classification communale identifie et définit les catégories de locaux d'habitation existant dans la commune pour chaque nature de construction : maisons individuelles, immeubles collectifs et dépendances bâties isolées.",
    "II. - Pour cette classification, sont assimilés aux dépendances bâties isolées les dépendances bâties et les éléments bâtis formant dépendances qui, en raison de leur nature particulière, doivent être évalués distinctement. Sont notamment concernés les éléments de pur agrément ainsi que, dans les immeubles collectifs, les garages et les emplacements individuels aménagés pour le stationnement des véhicules automobiles."
),
    "Réécriture à droit constant : explicitation de la classification par nature de construction et scission de la règle d'assimilation. Cette règle détermine le barème applicable sans exiger de dossier propre ; sa conservation protège notamment le traitement séparé des dépendances.",
    "Maintien du I et du II, de la condition de nature particulière et de la liste non exhaustive introduite par « notamment ». La précision relative aux immeubles collectifs reste attachée aux garages et emplacements de stationnement, sans être étendue à tous les éléments de pur agrément. Coordination maintenue avec 324 H II, 324 I II, 324 N et 324 V II.")

add('324 H', paras(
    "I. – Les maisons individuelles et les locaux situés dans un immeuble collectif sont classés, dans la commune, selon une nomenclature type de huit catégories. Les critères généraux du premier tableau ci-dessous sont adaptés aux normes locales de construction.",
    "II. – Les dépendances bâties isolées et les éléments mentionnés au II de l'article 324 G sont classés selon une nomenclature type spéciale de quatre catégories. Les critères généraux du second tableau ci-dessous sont adaptés aux normes locales de construction.",
    "III. – Dans les deux cas prévus aux I et II, des catégories intermédiaires peuvent être créées en combinant, dans des proportions simples, deux catégories types.",
    "IV. – Les caractéristiques physiques de chaque nature et catégorie de locaux retenues pour la classification communale sont inscrites au procès-verbal des opérations de révision."
) + '\n' + '\n'.join(tables('324 H')),
    "Réécriture à droit constant des quatre règles de classement, avec désignation explicite des deux tableaux et correction de la répétition « cas deux cas ». Les deux nomenclatures et tous leurs critères sont intégralement conservés. Leur conservation assure une évaluation comparable et les catégories moins élevées ; l'inscription au procès-verbal conserve une fonction de preuve et de contrôle de l'assiette.",
    "Deux tableaux intégralement repris, avec huit catégories d'habitation et quatre catégories A à D, toutes cellules et fusions conservées. La faculté de catégories intermédiaires n'est pas supprimée. Les libellés sources atypiques « Absence de fréquence » pour l'ascenseur en cinquième catégorie et « Habillement, couverture en matériaux courants » pour la toiture sont conservés : leur sens requiert vérification documentaire, sans correction normative silencieuse. Les critères d'habitabilité décrivent ici une classification fiscale et ne dispensent pas des règles autonomes de sécurité ou de salubrité. Seuls les attributs de présentation non autorisés sont retirés.")

add('324 I', paras(
    "I. - Les maisons individuelles et les locaux situés dans un immeuble collectif sont classés dans la commune selon les caractéristiques générales de leur partie principale. II. - Les dépendances bâties et les éléments bâtis formant dépendances, autres que ceux mentionnés au II de l'article 324 G, sont classés dans la catégorie de leur partie principale lorsqu'ils se trouvent sur la même propriété et en constituent l'accessoire. S'ils sont à usage commun, ils sont classés dans la catégorie de la majorité des parties principales des locaux qu'ils desservent."
),
    "Réécriture à droit constant : explicitation du rattachement des dépendances à leur partie principale et de la règle de majorité pour l'usage commun. L'exception des dépendances évaluées distinctement est maintenue ; aucun contrôle préalable ni déclaration autonome ne figure dans cette règle de calcul.",
    "Le I et le II demeurent dans le même alinéa, comme dans la source, afin de ne pas modifier sans coordination les cibles d'alinéas. Le renvoi « 324 G. II » est clarifié en « II de l'article 324 G ». La majorité porte sur les parties principales desservies, non sur la surface, les voix des copropriétaires ou les occupants. Aucune solution nouvelle n'est inventée en cas d'absence de majorité.")

add('324 J', paras(
    "Pour chaque nature de construction, un ou plusieurs locaux de référence sont choisis dans chaque catégorie de la classification communale afin de l'illustrer et de servir de termes de comparaison. Ces locaux doivent être particulièrement représentatifs de leur catégorie. Ils comprennent, le cas échéant, des dépendances bâties et non bâties d'une importance moyenne par rapport à la généralité des locaux de même nature appartenant à cette catégorie.",
    "La liste des locaux de référence figure au procès-verbal des opérations de révision."
),
    "Réécriture à droit constant des critères de choix des locaux de référence en trois phrases. Leur identification documentée est nécessaire à la méthode comparative du CGI 1496 et à la contestation d'une évaluation ; elle n'est pas une formalité supplémentaire imposée aux contribuables.",
    "Maintien de la pluralité possible des références, du classement par nature et catégorie, de la représentativité particulière et de l'importance moyenne des dépendances lorsqu'elles existent. Le procès-verbal est conservé pour rendre la comparaison vérifiable. Aucun choix d'une catégorie supérieure par défaut n'est introduit.")

add('324 K', paras(
    "I. - Sous réserve des travaux d'homogénéité prévus au premier alinéa du II de l'article 1496 du code général des impôts, le tarif d'évaluation est déterminé, pour chaque nature et catégorie de locaux d'habitation, en tenant compte des loyers annuels des locaux loués librement à des conditions de prix normales et de leurs surfaces pondérées. Ces surfaces sont calculées selon les articles 324 L à 324 V.",
    "II. - Si une catégorie ne comprend pas assez de locations répondant aux conditions du I, son tarif est déterminé par comparaison avec les tarifs des catégories voisines de la même commune ou avec ceux des catégories identiques ou voisines d'autres communes présentant des conditions économiques analogues."
),
    "Réécriture à droit constant : séparation de la règle de tarif et du calcul des surfaces, puis formulation directe de la méthode subsidiaire. Le mécanisme évite une assiette arbitraire en l'absence de locations suffisantes et conserve les correctifs favorables ; aucune formalité autonome ne peut être retranchée ici.",
    "Le renvoi au premier alinéa du II de 1496 et à tous les articles 324 L à 324 V est maintenu. Les loyers sont annuels, libres et normaux ; la comparaison subsidiaire reste conditionnée à l'insuffisance de locations admissibles et à l'analogie économique pour les communes extérieures. Aucun taux ni moyenne nouvelle n'est ajouté.")

add('324 L', paras(
    "I. - Dans une maison ou dans la partie principale des locaux d'un immeuble collectif, les éléments suivants sont distingués, lorsqu'ils existent :",
    "a. Les pièces, telles que salles à manger, pièces de réception diverses, chambres, pièces à usage professionnel et cuisines, ainsi que leurs annexes, notamment les salles d'eau (salles de bains, de douches ou cabinets de toilette avec eau courante), les cabinets d'aisance, l'entrée, les couloirs et l'antichambre. Les éléments énumérés au b en sont exclus ;",
    "b. Les garages, buanderies, caves, greniers, celliers, bûchers et autres éléments de même nature, ainsi que les terrasses et toitures-terrasses accessibles.",
    "Les pièces à usage professionnel sont évaluées selon l'article 1498 du code général des impôts et les articles 324 A, 324 B et 324 X. Leur surface pondérée est calculée selon l'article 324 Z.",
    "II. - Parmi les dépendances bâties et les éléments bâtis formant dépendances, outre les éléments de même nature que ceux énumérés au I, sont distingués :",
    "Les éléments de pur agrément, tels que les piscines privées et les terrains de jeux ;",
    "Dans les immeubles collectifs, les emplacements individuels aménagés pour le stationnement des véhicules automobiles."
),
    "Réécriture à droit constant des listes et séparation, dans son alinéa d'origine, de la règle d'évaluation des pièces professionnelles et du calcul de leur surface. Le classement conditionne les coefficients propres aux annexes ; le supprimer pourrait accroître leur base, sans alléger une formalité.",
    "Conservation des I et II, des a et b, de tous les exemples, de l'accessibilité des terrasses et toitures-terrasses et des quatre renvois réglementaires. Le quatrième alinéa du I reste consacré aux pièces professionnelles, car 324 M le vise expressément. Le renvoi préexistant à 324 X, consacré au classement comparatif des logements, est conservé mais appelle une coordination avec le champ du CGI 1498 ; il n'est ni effacé ni présenté comme corrigé.")

add('324 M', paras(
    "Pour calculer la surface pondérée d'un local de référence, les correctifs des articles 324 N à 324 S sont appliqués à sa surface réelle. Celle-ci est mesurée au sol entre les murs ou séparations et arrondie au mètre carré inférieur.",
    "Lorsqu'un local est affecté à la fois à l'habitation et à un usage professionnel, les surfaces sont calculées séparément pour chaque affectation.",
    "La surface affectée à l'usage professionnel est calculée selon les règles mentionnées au quatrième alinéa du I de l'article 324 L."
),
    "Réécriture à droit constant : distinction claire entre mesure réelle, correctifs et séparation des usages. L'arrondi inférieur est maintenu, ainsi que la méthode particulière aux pièces professionnelles ; ces règles de calcul n'imposent aucune déclaration autonome.",
    "Maintien du renvoi complet à 324 N à 324 S et de l'arrondi au mètre carré inférieur, sans arrondissement au plus proche. Le quatrième alinéa du I de 324 L demeure au même emplacement dans la proposition et vise notamment 324 Z, lu dans le corpus ; les surfaces professionnelles restent distinctes.")

add('324 N', paras(
    "Les surfaces des éléments de la maison mentionnés au b du I de l'article 324 L et des éléments, autres que les pièces et leurs annexes, mentionnés au II du même article sont pondérées par un coefficient compris entre 0,2 et 0,6. Ce coefficient tient compte du service rendu par chaque élément dans la valeur d'usage du local.",
    "La surface pondérée brute qui en résulte est arrondie au mètre carré inférieur.",
    "Cette pondération ne s'applique toutefois pas aux éléments qui relèvent de la classification spéciale prévue au II de l'article 324 H."
),
    "Réécriture à droit constant d'une pondération favorable des surfaces annexes, avec séparation du coefficient et de sa justification. Supprimer ce mécanisme pendant que la taxe foncière subsiste pourrait augmenter les bases ; la fourchette et l'arrondi inférieur sont donc conservés.",
    "Coefficients de 0,2 à 0,6 intégralement maintenus ; aucun coefficient intermédiaire nouveau n'est fixé. L'exclusion des pièces et de leurs annexes reste limitée au renvoi au II de 324 L. L'exception de classification spéciale du II de 324 H demeure pour éviter un double traitement inadapté des dépendances isolées.")

add('324 O', paras(
    "La surface totale des pièces et annexes mentionnées au I de l'article 324 L, dans une maison ou dans la partie principale des locaux d'un immeuble collectif, à l'exclusion des pièces à usage professionnel, est pondérée selon son importance. Les coefficients et les limites de tranche applicables à chaque catégorie mentionnée aux articles 324 G et 324 H sont fixés par le tableau suivant :"
) + '\n' + tables('324 O')[0] + '\n' + paras(
    "Le résultat, arrondi au mètre carré inférieur, constitue la surface pondérée comparative de la partie principale."
),
    "Réécriture à droit constant de la règle de pondération par importance et de la dénomination du résultat. Le tableau reste entier : les coefficients inférieurs à l'unité, les seuils par catégorie et l'arrondi favorable ne sont pas supprimés. Une réduction isolée de ce barème comparatif demanderait de coordonner les tarifs plutôt que de présumer une baisse d'impôt uniforme.",
    "Tableau intégral conservé : huit catégories, deux natures de locaux et trois tranches ; première tranche de 20 m², seuils maisons 400/320/240/160/110/80/60/40 et collectifs 350/260/200/140/90/70/50/30. Coefficients de première tranche maisons 3,00/2,50/2,10/1,70/1,45/1,30/1,20/1,10 et collectifs 2,60/2,20/1,90/1,60/1,35/1,25/1,15/1,05 ; 0,90 et 0,75 pour les tranches suivantes. L'exclusion des pièces professionnelles et l'arrondi inférieur subsistent. Ces coefficients d'assiette ne sont pas des taux d'impôt.")

add('324 P', paras(
    "Un correctif d'ensemble est appliqué à la surface pondérée comparative de la partie principale, augmentée, pour une maison et s'il y a lieu, de la surface pondérée brute des éléments mentionnés au b du I de l'article 324 L. Il tient compte de l'état d'entretien et de la situation de la partie principale. Il est égal à la somme algébrique des coefficients définis aux articles 324 Q et 324 R.",
    "La surface pondérée nette ainsi calculée est arrondie au mètre carré inférieur."
),
    "Réécriture à droit constant : identification de la surface corrigée, de l'objet du correctif et de sa formule dans des phrases distinctes. Le mécanisme conserve les réductions pour mauvais entretien et mauvaise situation ; il ne constitue pas une formalité redondante.",
    "Le correctif reste une somme algébrique, jamais un produit de coefficients. L'ajout de surface des éléments du b du I de 324 L demeure limité aux maisons. Maintien de l'arrondi inférieur et des renvois Q et R ; le correctif d'ascenseur de 324 S, lu dans le corpus, garde son champ distinct dans les immeubles collectifs.")

add('324 Q', paras(
    "Le coefficient applicable à l'état d'entretien de la construction est fixé par le tableau suivant :"
) + '\n' + tables('324 Q')[0],
    "Réécriture à droit constant de la règle d'application du coefficient d'entretien ; le tableau demeure intégral. Les réductions à 0,90 et 0,80 sont protégées pour les situations futures comme présentes. Le barème décrit une variable nécessaire à la méthode d'évaluation, sans dossier particulier susceptible d'être supprimé.",
    "Cinq états et cinq coefficients conservés : bon 1,20 ; assez bon 1,10 ; passable 1 ; médiocre 0,90 ; mauvais 0,80. Toutes les qualifications relatives aux réparations, à la vétusté et à l'habitabilité figurent dans le tableau. Aucun classement automatique d'un logement vétuste dans une catégorie supérieure n'est ajouté. Attributs de présentation retirés, contenu des cellules conservé.")

add('324 R', paras(
    "Le coefficient de situation est la somme algébrique du coefficient de situation générale dans la commune et du coefficient d'emplacement particulier. Chacun est déterminé selon le tableau suivant :"
) + '\n' + tables('324 R')[0] + '\n' + paras(
    "Pour déterminer le coefficient de situation particulière, il est notamment tenu compte de la présence ou de l'absence de dépendances non bâties."
),
    "Réécriture à droit constant de la composition du coefficient et de la prise en compte des dépendances non bâties. Le tableau conserve toutes les corrections, dont les valeurs négatives favorables ; supprimer ce calcul sans supprimer l'impôt ferait perdre les minorations pour situations défavorables.",
    "Tableau complet à cinq lignes de situation et deux colonnes de coefficients : + 0,10, + 0,05, 0, - 0,05 et - 0,10 dans chaque colonne. Maintien des avantages et inconvénients qualifiant chaque situation et de l'addition algébrique des deux coefficients, puis du renvoi de 324 P. La présence ou l'absence de dépendances reste un critère non exclusif, sans minoration ou majoration automatique nouvelle.")


if set(answers) != set(by_number):
    raise ValueError(('Coverage mismatch', set(by_number) - set(answers)))

allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
for s in sources:
    a = answers[s['number']]
    root = ET.fromstring('<root>' + a['proposed_xml'] + '</root>')
    for e in root.iter():
        if e.tag == 'root':
            continue
        assert e.tag in allowed_tags, (s['number'], e.tag)
        for k, v in e.attrib.items():
            assert k in ('rowspan', 'colspan') and re.fullmatch('[0-9]+', v)
    if s.get('benefit_check_required'):
        assert len(a.get('benefit_review', '')) >= 100
    for k in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[k] == s[k]
    assert a['status'] == 'rewrite_draft'
    if a.get('change_type') == 'normative_reduction':
        assert all(len(x) >= 30 for x in a['removed_provisions'])
    if a.get('change_type') == 'full_repeal':
        assert len(a['repeal_scope']) >= 30
        assert ''.join(root.itertext()).startswith(('Le présent article est abrogé', 'Abrogé'))
    if a.get('change_type') != 'full_repeal':
        st = ET.fromstring('<root>' + s['source_xml'] + '</root>').findall('table')
        at = root.findall('table')
        assert len(st) == len(at), s['number']
        for orig, new in zip(st, at):
            assert list(orig.itertext()) == list(new.itertext()), s['number']
            assert [(e.tag, {k: v for k, v in e.attrib.items() if k in ('rowspan', 'colspan')}) for e in orig.iter()] == [(e.tag, e.attrib) for e in new.iter()], s['number']

Path('answer.json').write_text(json.dumps([answers[s['number']] for s in sources], ensure_ascii=False, indent=2) + '\n')
print(f"answer.json : {len(answers)} articles ; identifiants, XML, bénéfices signalés et tableaux vérifiés.")
