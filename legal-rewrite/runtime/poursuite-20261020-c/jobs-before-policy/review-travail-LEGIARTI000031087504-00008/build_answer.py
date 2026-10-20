import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
out = []

def text_only(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()

def replace_once(text, before, after):
    assert text.count(before) == 1, before
    return text.replace(before, after, 1)

def article(number, reason, notes, classification, assessment, limitations, burdens):
    source = by_number[number]
    item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(proposed_xml=source['previous_draft']['proposed_xml'], reason=reason,
                review_notes=notes, status='rewrite_draft')
    item['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=[])
    out.append(item)
    return item

def reduction(item, *removed):
    item.update(change_type='normative_reduction',
                reform_policy_id='editorial_direction_2026_10_19',
                removed_provisions=list(removed))

def repeal(item, scope):
    item.update(change_type='full_repeal',
                repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)

def effect(item, kind, measure, description, before, after, unit, population,
           conditions, replacement, source_quote, proposed_quote):
    assert len(source_quote) >= 12 and source_quote in text_only(by_number[item['number']]['source_xml']), (item['number'], source_quote)
    assert len(proposed_quote) >= 12 and proposed_quote in text_only(item['proposed_xml']), (item['number'], proposed_quote)
    item['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before,
        after=after, unit=unit, affected_population=population,
        conditions_and_transition=conditions, replacement_or_new_burdens=replacement,
        source_quote=source_quote, proposed_quote=proposed_quote))

a = article('L1254-17',
    "Abrogation prospective du régime de renouvellement du CDD de portage, en coordination avec le contrat unique. La seconde passe conserve cette suppression déjà acquise : la limite de deux renouvellements et les avenants de renouvellement ne doivent pas devenir un régime d'affectation dans le nouvel emploi sans terme. Les règles anciennes ne subsistent que pour les renouvellements déjà convenus. Le report favorable de prospection reste ouvert aux anciens contrats ; le supprimer davantage retirerait un avantage sans supprimer une charge générale correspondante.",
    "Lecture des deux alinéas, de la note historique et du brouillon entier. Deux renouvellements, plafond de dix-huit mois par L1254-12 et report conventionnel maximal de trois mois par L1254-13 distingués. La note « applicables aux contrats en cours » concerne la réforme de 2015. L1254-13, absent des cibles fournies, a été lu intégralement dans le corpus travail.json : son report par accord pour prospection est conservé pour les anciens contrats, même décidé après la réforme, sans être un renouvellement ordinaire nouveau. Sa proposition actuelle reste à coordonner hors lot. Une clause offrant une faculté de renouvellement n'est pas un renouvellement déjà convenu. La conversion ne remet pas l'ancienneté à zéro et ne fait pas naître automatiquement une prime de fin de contrat. Les sanctions sont coordonnées dans L1255-14 ; les textes réglementaires propres au portage restent à coordonner. Aucun nouveau renvoi n'est introduit dans cette proposition.",
    'coordination_only',
    "Par rapport à la source officielle entière, le régime futur de renouvellement à terme disparaît, avec ses formalités ; cette conséquence appartient à la mesure commune du contrat unique et ne constitue pas une seconde fusion de régimes. Aucun prélèvement n'est supprimé par cet article. Le brouillon opératoire est conservé après nouvel examen de chacune de ses garanties transitoires.",
    "Les renouvellements déjà valablement convenus et le report de prospection des anciens contrats restent couverts par leur droit antérieur. Les contrats étrangers et le régime public ne sont pas convertis ici. Aucun gain net de coût ou de complexité de l'ensemble des codes n'est chiffré.",
    "Aucun dossier, déclaration, registre ou justificatif nouveau n'est identifié : la poursuite convenue relève du contrat unique déjà décidé par la réforme commune. L'interdiction de nouveaux renouvellements réduit toutefois une faculté de recours au CDD ; elle ne doit pas être présentée comme un gain universel pour les parties.")
repeal(a, "Régime futur des deux renouvellements de CDD de portage, de leur durée cumulée et de leurs clauses ou avenants ; maintien des renouvellements déjà convenus et du report favorable des anciens contrats.")
a['benefit_review'] = "La source permet deux renouvellements et réserve la dérogation de L1254-13 : la poursuite en CDD n'est plus ouverte après la réforme, conformément à la décision expresse de contrat unique, mais les renouvellements valablement convenus restent exécutables. Le report par accord pour prospecter de nouveaux clients, limité à trois mois, demeure accessible aux anciens contrats même si l'accord intervient ensuite. Les limites de durée et les conditions d'avenant de ces anciens contrats restent protectrices. Les indemnités, congés, créances, garanties et recours ne sont pas éteints. Les aides et exonérations de même objet restent ouvertes aux futurs emplois éligibles sous contrat unique, sans inventer un avantage chiffré absent de la source."
effect(a, 'coordination', 'contrat-unique-duree-indeterminee',
    "Retrait du mécanisme de renouvellement à terme en exécution du régime commun, sans compter une fusion supplémentaire.",
    "CDD de portage renouvelable deux fois dans la durée maximale visée, avec clause ou avenant avant le terme initial.",
    "Aucun nouveau renouvellement à terme ; poursuite convenue sans terme et avec ancienneté et créances conservées.",
    'regime', 'Entreprises de portage et salariés portés',
    "À l'entrée en vigueur de la loi instituant le contrat unique ; renouvellements déjà convenus et report de prospection des anciens contrats préservés.",
    "Le contrat unique remplace le renouvellement ; aucune déclaration de remplacement ni nouvel essai.",
    "Les conditions de renouvellement sont stipulées dans le contrat ou font l'objet d'un avenant soumis au salarié avant le terme initialement prévu.",
    "À compter de cette date, aucun nouveau renouvellement à durée déterminée d'un contrat de portage salarial ne peut être convenu, même si une clause du contrat antérieur en prévoyait la possibilité.")

a = article('L1254-21',
    "Réduction de fond : maintien des suppressions du descriptif détaillé et des comptes rendus périodiques du salarié, de la fusion des frais professionnels et de la dispense de répéter les organismes sociaux. Coupe supplémentaire : l'identité du garant déjà remise par écrit n'est plus obligatoirement recopiée dans le contrat. Les modalités financières et de congés restent nécessaires pour rendre les droits vérifiables ; elles ne sont pas remplacées par un reporting. Le régime sans rémunération générale des intermissions du portage est conservé, ainsi que les garanties plus favorables. L'essai est coordonné avec les trois mois sans renouvellement des nouveaux contrats.",
    "I et ses huit emplacements, II et transition III préservés. Le 2° est fusionné au 1°, non une suppression de frais ou de remboursement. L1254-23, lu en entier dans le corpus, conserve au 2° le descriptif dans le contrat commercial, au 5° le prix et au 8° l'identité du garant ; L1254-22 conserve la remise au salarié d'une copie du contrat commercial. Cette copie peut satisfaire à la communication du garant si elle est déjà remise et exacte ; aucune remise supplémentaire n'est créée. L1254-25, lu en entier, maintient le compte d'activité et les six postes d'information mensuelle fournis par l'employeur. L1254-2 maintient expertise, qualification, autonomie, rémunération minimale et absence d'obligation de fournir du travail. Les obligations autonomes d'information, notamment celles à coordonner avec la directive 2019/1152, le temps de travail, la santé et les congés subsistent. Leur contenu supérieur n'est pas réputé abrogé. L1255-14, 6°, est coordonné avec les dispenses nouvelles. Aucun taux fiscal ni transfert de retraite n'est décidé ici.",
    'material_reduction',
    "La comparaison avec toute la source démontre deux obligations retirées (descriptif détaillé et comptes rendus du salarié), une fusion des mentions de frais et des dispenses de recopie de données sociales et du garant. L'extension au garant est supplémentaire par rapport au brouillon. Les montants de salaire, frais et prélèvements ne sont pas abaissés par ces coupes documentaires.",
    "Les obligations autonomes de communication et de décompte restent dues. La dispense de recopie ne vaut que pour des informations écrites déjà accessibles et exactes. Les clauses plus favorables et les anciens essais sont réservés ; l'effet du plafond commun d'essai sur chaque catégorie n'est pas chiffré ici.",
    "Aucune charge administrative nouvelle n'est identifiée : pas de registre, de nouvelle attestation ni de rapport de remplacement. La communication exacte et conservable était déjà nécessaire à l'information du salarié. Le plafond de trois mois sans renouvellement relève de la réforme commune de l'essai ; les anciens essais ne sont pas refaits.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "sous réserve de la dispense de répétition prévue au 6°", "sous réserve des dispenses de répétition prévues aux 6° et 8°")
a['proposed_xml'] = replace_once(a['proposed_xml'], "8° L'identité du garant financier de l'entreprise de portage salarial.</p>", "8° L'identité du garant financier de l'entreprise de portage salarial. Cette identité n'a pas à être reproduite dans le contrat si elle a déjà été communiquée par écrit au salarié, sur un support qu'il peut conserver, et demeure exacte. Une simple référence à un document auquel il n'a pas accès ne vaut pas communication.</p>")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Les suppressions et la dispense de répétition prévues au I", "Les suppressions et les dispenses de répétition prévues au I")
reduction(a,
    "Suppression du descriptif contractuel détaillé des compétences, qualifications et domaines d'expertise du salarié porté.",
    "Suppression des comptes rendus périodiques d'activité obligatoirement établis par le salarié sur le fondement du 7°.",
    "Fusion de la mention séparée des modalités de déduction des frais professionnels dans les modalités financières du 1°.",
    "Suppression de la recopie des coordonnées sociales et de l'identité du garant lorsque ces données ont déjà été remises par écrit et restent exactes.")
effect(a, 'obligation_removed', 'portage-suppression-descriptif-contractuel',
    "Retrait du descriptif détaillé propre au contrat de travail, sans supprimer qualifications ou information de base sur les fonctions.",
    "Descriptif détaillé obligatoire dans chaque contrat de travail de portage à durée indéterminée.",
    "Le 3° est abrogé ; les autres informations légalement dues et le descriptif commercial autonome subsistent.",
    'legal_duty', 'Entreprises de portage et salariés portés',
    "Dès l'entrée en vigueur ; aucun contrat antérieur à refaire ; garanties plus favorables conservées.",
    "Aucun descriptif ni déclaration de remplacement.",
    "3° Le descriptif des compétences, des qualifications et des domaines d'expertise du salarié porté ;",
    "Le présent article n'impose plus de descriptif contractuel des compétences, qualifications et domaines d'expertise ni de comptes rendus périodiques d'activité établis par le salarié porté.")
effect(a, 'obligation_removed', 'portage-suppression-comptes-rendus-salarie',
    "Suppression du reporting périodique du salarié, distinct de son compte d'activité tenu par l'employeur.",
    "Le contrat impose une périodicité des comptes rendus d'activité établis par le salarié.",
    "Le 7° est abrogé ; aucun compte rendu périodique n'est dû sur ce fondement.",
    'legal_duty', 'Salariés portés',
    "À l'entrée en vigueur, sans supprimer les décomptes autonomes de temps et les garanties conventionnelles.",
    "Le compte d'activité déjà obligatoire demeure ; aucune création d'un rapport équivalent.",
    "7° La périodicité de l'établissement par le salarié porté de comptes rendus d'activité ;",
    "Le présent article n'impose plus de descriptif contractuel des compétences, qualifications et domaines d'expertise ni de comptes rendus périodiques d'activité établis par le salarié porté.")
effect(a, 'obligation_merged', 'portage-fusion-mentions-frais-professionnels',
    "Réunion des règles de déduction et de versement des frais dans la même mention financière.",
    "Frais mentionnés au 1° et modalités de déduction exigées séparément au 2° s'il y a lieu.",
    "Une mention financière au 1° comprenant la déduction ; 2° abrogé ; droits aux frais maintenus.",
    'legal_duty', 'Entreprises de portage établissant le contrat',
    "À l'entrée en vigueur, sans réédition des contrats existants.",
    "Aucune donnée financière nouvelle ; suppression d'une présentation séparée.",
    "2° S'il y a lieu, les modalités de déduction des frais professionnels ;",
    "1° Les modalités de calcul et de versement de la rémunération due pour la réalisation de la prestation, de l'indemnité d'apport d'affaire, des prélèvements sociaux et fiscaux, des frais de gestion et, le cas échéant, des frais professionnels, y compris les modalités de leur déduction.")
effect(a, 'compliance_cost_reduced', 'portage-dispense-recopie-information-sociale',
    "Fin de la recopie contractuelle des organismes sociaux déjà communiqués par écrit.",
    "Nom et adresse des organismes sociaux obligatoirement dans le contrat, même déjà communiqués.",
    "Pas de recopie si les mêmes données écrites conservables sont déjà communiquées et exactes.",
    'legal_duty', 'Entreprises de portage et salariés déjà informés',
    "À l'entrée en vigueur ; accès effectif et exactitude requis ; information autonome maintenue.",
    "Aucune attestation de remise nouvelle n'est requise.",
    "6° Les nom et adresse de la caisse de retraite complémentaire ainsi que, le cas échéant, ceux de l'organisme de prévoyance dont relève l'entreprise de portage salarial ;",
    "Ces informations n'ont pas à être reproduites dans le contrat si elles ont déjà été communiquées par écrit au salarié, sur un support qu'il peut conserver, et demeurent exactes.")
effect(a, 'compliance_cost_reduced', 'portage-dispense-recopie-garant-financier',
    "Dispense supplémentaire de recopier l'identité du garant déjà communiquée au salarié.",
    "Identité du garant à inscrire au contrat même lorsque le salarié en dispose déjà par écrit.",
    "Recopie dispensée pour une identité déjà communiquée sur support conservable et toujours exacte.",
    'legal_duty', 'Entreprises de portage et salariés déjà informés du garant',
    "À l'entrée en vigueur ; les contrats existants ne sont pas refaits et la garantie financière reste obligatoire.",
    "Ni nouvelle déclaration ni suppression de l'information ou de la garantie.",
    "8° L'identité du garant financier de l'entreprise de portage salarial.",
    "Cette identité n'a pas à être reproduite dans le contrat si elle a déjà été communiquée par écrit au salarié, sur un support qu'il peut conserver, et demeure exacte.")

a = article('L1255-1',
    "Réduction de fond conservée après seconde passe : retrait des six mois d'emprisonnement en récidive du manquement sectoriel à L1251-2. Les amendes et l'interdiction judiciaire protègent encore l'identification de l'employeur qui recrute et rémunère ; les supprimer aussi priverait ce régime d'une sanction propre sans examen de l'effectivité des protections restantes. Les deux amendes, la durée de l'interdiction et les droits indemnitaires du personnel permanent restent à droit constant. Aucun allègement de déclaration ni de salaire n'est revendiqué.",
    "Trois alinéas source et transition relus : 3 750 euros, 7 500 euros, suppression des seuls six mois de prison, interdiction de deux à dix ans. L1251-2 fourni maintient la définition et coordonne les nouveaux recrutements sans terme avec les garanties d'intermission. L1235-2 et L1235-5 ont été lus en entier dans le corpus ; L1235-3 et ses deux tableaux sont fournis et ont été lus. Incohérence préexistante conservée et signalée : L1235-5 ne fixe plus d'indemnité au salarié mais une dispense de remboursement d'allocations ; son renvoi ne crée donc pas de créance nouvelle. Les indemnités visées ne sont pas le barème ordinaire de L1234-9 et ne disparaissent pas avant un an. Les procédures collectives et autorisations de salariés protégés restent distinctes. La loi pénale plus douce règle les faits antérieurs ; les condamnations pécuniaires définitives et les créances civiles ne sont pas effacées. L'effectivité des sanctions au regard de la directive 2008/104/CE reste à coordonner ; ce texte européen n'est pas joint et aucune conformité n'est certifiée.",
    'material_reduction',
    "La source entière expose le récidiviste à six mois d'emprisonnement et 7 500 euros : la proposition retire effectivement la prison, déjà retirée par le brouillon. Il s'agit d'une réduction de l'exposition pénale, sans suppression des conditions d'activité, des amendes, des droits du personnel ni d'un impôt.",
    "Seule l'infraction sectorielle de cet article est concernée ; fraude, rémunération, santé et autres délits autonomes subsistent. L'efficacité globale des sanctions maintenues et leur coût ne sont pas établis par ce lot.",
    "Aucune charge nouvelle n'est identifiée : la peine supprimée n'est remplacée ni par une déclaration ni par une autorisation. Amendes et interdiction existaient déjà ; elles ne sont ni augmentées ni rendues automatiques.")
reduction(a, "Suppression de la peine de six mois d'emprisonnement pour récidive du manquement aux conditions d'exercice de L1251-2, sans retirer les amendes ni l'interdiction judiciaire.")
effect(a, 'compliance_cost_reduced', 'interim-retrait-prison-manquement-sectoriel',
    "Réduction de l'exposition pénale sectorielle, sans économie monétaire de conformité présumée.",
    "Récidive du manquement à L1251-2 : six mois de prison et 7 500 euros d'amende.",
    "Récidive : 7 500 euros d'amende ; interdiction judiciaire de deux à dix ans inchangée.",
    'other', 'Entrepreneurs de travail temporaire poursuivis sur L1255-1',
    "À l'entrée en vigueur et pour les faits antérieurs selon la loi pénale plus douce ; droits civils maintenus.",
    "Aucune peine ou formalité de remplacement ; obligation de fond toujours sanctionnée.",
    "La récidive est punie d'un emprisonnement de six mois et d'une amende de 7 500 euros.",
    "La récidive est punie de 7 500 euros d'amende.")

a = article('L1255-2',
    "Maintien des coupes pénales du brouillon : abrogation du 5° et retrait de la seule sanction pénale des retards d'écrit aux 1° et 4°. Coupe supplémentaire : la récidive des seuls manquements documentaires des 1° et 4° ne comporte plus de peine de prison, l'amende de 7 500 euros et l'interdiction judiciaire demeurant. La prison reste prévue pour la récidive des atteintes à la rémunération, à la protection radiologique ou à la garantie financière. Les obligations et délais civils ne sont pas supprimés. Les lettres de mission et les affectations de radioprotection sont coordonnées avec le contrat unique sans nouveau CDD.",
    "Maintien des six numéros et des alinéas de peine ; 3 750 euros, 7 500 euros et interdiction de deux à dix ans inchangés. Le caractère volontaire reste limité à l'inexactitude des mentions du 1°. L1251-17 et L1251-42 conservent deux jours ouvrables ; seules les sanctions indiquées sont réduites. L1251-18 est limité à son premier alinéa. La vue actuelle de L1251-34 est déjà coordonnée en affectations, contrairement à la réserve périmée du brouillon : trois jours ouvrables, calcul de la limite annuelle rapportée à la durée totale et quatre garanties du deuxième alinéa de L1251-26 restent applicables. L1251-58-4 exclut L1251-26 pour le CDI intérimaire, d'où l'incorporation ciblée de ses garanties de proposition radiologique, non du régime général de rupture de mission. L1251-45, lu en entier hors lot, impose toujours les déclarations d'activité, siège, agences et cessation : le 5° retire le délit, pas ces obligations. Leur suppression administrative nécessite sa propre réécriture. L1251-47 fourni retire déjà le motif déclaratif de fermeture ; son deuxième alinéa reste la cible indemnitaire, avec le renvoi historiquement incohérent à L1235-5 signalé. Les directives 2008/104/CE et 2019/1152 nécessitent des recours et sanctions effectifs, proportionnés et dissuasifs : leur coordination n'est pas réputée acquise par la dépénalisation. Le renvoi ciblé à L1251-26 est fourni, non inventé.",
    'material_reduction',
    "La comparaison complète avec la source montre le retrait d'un délit déclaratif, de l'exposition pénale pour le seul retard de deux écrits et, en supplément du brouillon, de la prison en récidive pour leurs manquements documentaires restants. Les délais et démarches administratives sources subsistent dans leurs articles ; ils ne sont pas comptés comme supprimés. Les protections salariales, radiologiques et financières restent sanctionnées.",
    "Les sanctions restantes et les autres fondements d'information ou de contrôle ne sont pas abrogés. L'absence de chiffrage des coûts et de contrôle complet de l'effectivité européenne empêche toute conclusion de réduction nette sur l'ensemble du régime de l'intérim.",
    "Aucune déclaration ou pièce de remplacement n'est créée. Les lettres de mission et les propositions de radioprotection existaient dans les cibles coordonnées ; elles ne sont pas de nouveaux contrats. Les quatre garanties de proposition sont conservées, sans nouvel essai ni nouveau terme d'emploi.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "La récidive est punie de six mois d'emprisonnement et de 7 500 euros d'amende.", "La récidive est punie de 7 500 euros d'amende. Pour les seuls manquements prévus aux 2°, 3° et 6°, elle est également punie de six mois d'emprisonnement.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Ces réductions pénales s'appliquent aux faits antérieurs", "La suppression de l'emprisonnement en récidive pour les manquements des 1° et 4° s'applique à compter de la même date. Ces réductions pénales s'appliquent aux faits antérieurs")
reduction(a,
    "Abrogation du délit spécial de défaut des déclarations administratives de l'entrepreneur de travail temporaire visé au 5°.",
    "Suppression de la sanction pénale du seul dépassement des délais de transmission de l'écrit de mission et de conclusion du contrat de mise à disposition.",
    "Suppression de six mois d'emprisonnement en récidive pour les seuls manquements documentaires subsistant aux 1° et 4°, sans retirer l'amende ni l'interdiction judiciaire.")
effect(a, 'compliance_cost_reduced', 'interim-depenalisation-formalites-documentaires',
    "Retrait de délits ou peines documentaires ; aucune suppression fictive des démarches administratives elles-mêmes.",
    "Défaut des déclarations et retard des écrits incriminés ; récidive de tous les manquements punie de six mois et 7 500 euros.",
    "Déclarations et seuls retards écartés du délit ; récidive documentaire des 1° et 4° punie d'amende sans prison ; sanctions des 2°, 3° et 6° conservées.",
    'other', 'Entrepreneurs de travail temporaire soumis aux infractions documentaires de L1255-2',
    "À l'entrée en vigueur et faits antérieurs selon loi pénale plus douce ; obligations civiles, délais et créances conservés.",
    "Aucune déclaration de remplacement, amendes restantes non augmentées.",
    "La récidive est punie d'un emprisonnement de six mois et d'une amende de 7 500 euros.",
    "La récidive est punie de 7 500 euros d'amende. Pour les seuls manquements prévus aux 2°, 3° et 6°, elle est également punie de six mois d'emprisonnement.")
effect(a, 'coordination', 'contrat-unique-duree-indeterminee',
    "L'infraction de forme suit la lettre de mission au lieu d'imposer un nouveau contrat de travail.",
    "Le 1° vise le contrat de mission écrit et ses mentions par renvoi à L1251-16 et L1251-17.",
    "Dans les nouveaux emplois, écrit et informations de mission sans nouveau contrat ni répétition dispensée.",
    'regime', 'Entrepreneurs et salariés intérimaires sous contrat unique',
    "Nouveaux contrats à compter de la réforme ; anciens droits de forme réservés sous la loi pénale plus douce.",
    "Aucune formalité supplémentaire par rapport aux lettres de mission des cibles.",
    "1° De recruter un salarié temporaire en ayant conclu un contrat ne comportant pas les mentions prévues aux 1° et 3° de l'article L. 1251-16 ou comportant ces mentions de manière volontairement inexacte ou sans lui avoir transmis dans le délai prévu à l'article L. 1251-17 un contrat de mission écrit ;",
    "Aucun nouveau contrat de travail n'est exigé pour chaque affectation ;")

a = article('L1255-4',
    "Coupe supplémentaire au brouillon : suppression des six mois d'emprisonnement en récidive du recours hors cas légaux, en conservant les amendes de 3 750 et 7 500 euros. La restriction des affectations temporaires et sa sanction pécuniaire gardent une fonction de prévention du contournement de l'emploi direct ; elles ne sont pas assimilées à une autorisation ou à une déclaration. Le nouvel alinéa distingue l'affectation limitée du contrat unique sans terme et maintient les droits des anciens contrats.",
    "Les deux alinéas de source et la coordination finale sont relus. L1251-6 fourni conserve le premier alinéa sur la tâche précise et temporaire et ses cinq cas, sous réserve de L1251-7 ; le présent article ne retire aucun de ces cas ni leurs exceptions. Il n'autorise pas un nouveau CDD, même saisonnier, et la fin de mission n'est pas un motif automatique de rupture. Amendes inchangées ; prison de six mois supprimée, avec transition expresse de loi pénale plus douce. Les droits civils, les salaires et garanties d'intermission subsistent. Une coordination des sanctions effectives et proportionnées exigées par la directive 2008/104/CE reste nécessaire ; aucune conformité européenne n'est présumée et aucune abrogation de ce cadre supérieur n'est annoncée.",
    'material_reduction',
    "La source prévoit six mois de prison en récidive : ils sont réellement retirés, contrairement au brouillon. Les cas légaux d'affectation et les deux amendes demeurent. Cette réduction de peine n'est ni une disparition des conditions de recours ni une économie fiscale ou nationale chiffrée.",
    "La suppression porte uniquement sur cette peine ; les infractions de santé, de salaire, de fraude et les recours autonomes sont hors de cette coupe. Le nouveau régime ne modifie pas les anciens contrats de mission ni les garanties d'intermission.",
    "Aucune charge nouvelle n'est identifiée : pas de formulaire, justificatif ou permission substitué à la prison. Les règles d'affectation restent celles de L1251-6, et le contrat unique relève de la coordination commune.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "La récidive est punie de six mois d'emprisonnement et de 7 500 euros d'amende.", "La récidive est punie de 7 500 euros d'amende.")
a['proposed_xml'] += "\n<p>La suppression de la peine d'emprisonnement s'applique à compter de l'entrée en vigueur de la loi la portant et aux faits antérieurs dans les conditions d'application de la loi pénale plus douce. Elle ne supprime ni les droits et recours civils des salariés ni les infractions distinctes.</p>"
reduction(a, "Suppression de la peine de six mois d'emprisonnement en récidive du recours à un salarié temporaire hors objet ou cas de L1251-6 ; maintien des amendes et des droits civils.")
effect(a, 'compliance_cost_reduced', 'interim-retrait-prison-recours-irregulier',
    "Réduction de l'exposition pénale de l'utilisateur, sans abrogation des cas de recours.",
    "Récidive : six mois de prison et 7 500 euros d'amende, en plus du maintien de l'incrimination initiale.",
    "Récidive : 7 500 euros d'amende ; l'amende initiale de 3 750 euros reste due dans les conditions du délit.",
    'other', 'Utilisateurs de salariés temporaires',
    "À l'entrée en vigueur et faits antérieurs selon la loi pénale plus douce ; anciens droits civils préservés.",
    "Ni taxe ni formalité de remplacement ; contraintes d'affectation maintenues.",
    "La récidive est punie d'un emprisonnement de six mois et d'une amende de 7 500 euros.",
    "La récidive est punie de 7 500 euros d'amende.")

a = article('L1255-6',
    "Abrogation intégrale de l'incrimination spéciale du terme de la mission, déjà acquise dans le brouillon et conservée après seconde passe. Elle retire 3 750 euros d'amende, puis six mois d'emprisonnement et 7 500 euros en récidive, sans remplacer ces sanctions. Les règles civiles de fixation de l'affectation et les anciens droits de terme ne sont pas abrogés. La suppression ne transforme pas les durées de mission en durée de l'emploi unique et ne retire pas les infractions distinctes de santé, rémunération ou durée maximale.",
    "Source entière de deux alinéas et proposition entière relues. L1251-11 fourni conserve terme précis, cinq exceptions et durée minimale ; dans sa proposition ces règles visent la lettre de mission, pas le terme de l'emploi. Le présent article retire son incrimination seule et non ces règles ni L1255-7. Les dispositions de loi pénale plus douce et de cessation d'exécution d'une peine pour un fait devenu non pénal sont expressément réservées, distinctement des réparations civiles. La coordination du régime collectif de sanctions avec les exigences effectives, proportionnées et dissuasives de la directive 2008/104/CE reste à faire ; ce texte entier n'est pas fourni et aucune conformité ne découle de cette relecture. Aucun nouveau renvoi normatif n'est ajouté.",
    'material_reduction',
    "L'article officiel est entièrement une incrimination et ses peines : cette incrimination disparaît effectivement. Les sanctions supprimées ne sont pas un prélèvement fiscal. Le brouillon conserve déjà toute la coupe possible sur cet article ; retirer les réserves civiles ou transitoires supprimerait des protections au-delà de son objet.",
    "L1251-11 et les délits autonomes restent applicables dans leur champ ; les anciens contrats gardent leurs créances et recours. Aucun coût national, montant d'amende effectivement recouvré ou solde global n'est évalué.",
    "Aucune charge nouvelle n'est identifiée : il n'est créé ni amende de remplacement, ni registre, ni déclaration. Les obligations de preuve et de durée d'affectation demeurent préexistantes dans leur texte propre.")
repeal(a, "Incrimination spéciale du manquement de l'utilisateur aux règles de terme de L1251-11 et totalité de ses peines de première infraction et de récidive ; maintien des règles civiles et droits anciens.")
effect(a, 'compliance_cost_reduced', 'interim-abrogation-delit-terme-mission',
    "Suppression complète du délit spécial du terme, sans présenter le maintien civil de la règle comme supprimé.",
    "Manquement au terme : 3 750 euros ; récidive : six mois de prison et 7 500 euros.",
    "Aucune peine fondée sur L1255-6 ; règles civiles de mission et infractions distinctes maintenues.",
    'other', 'Utilisateurs de salariés temporaires',
    "À l'entrée en vigueur ; effets pénaux antérieurs selon loi plus douce et cessation d'exécution ; droits civils anciens conservés.",
    "Aucune peine ni formalité de remplacement.",
    "Le fait pour l'utilisateur de méconnaître les dispositions relatives au terme du contrat, prévues à l'article L. 1251-11, est puni d'une amende de 3 750 euros.",
    "Le manquement aux règles de fixation du terme prévues à l'article L. 1251-11 n'est plus puni sur le fondement du présent article.")

a = article('L1255-14',
    "Réduction de fond conservant le retrait des délits du terme, de l'intitulé exact et de transmission du contrat aux 3°, 5° et 7°, ainsi que la dépénalisation du seul retard au 8°. Coupe supplémentaire : la prison en récidive est retirée pour les manquements des 4°, 6°, 8°, 9° et 10°, dont les amendes et l'interdiction judiciaire demeurent. Elle subsiste aux 1°, 2°, 11°, 12° et 14° pour les interdictions sectorielles protectrices, le contrat unique, la traçabilité des fonds, la garantie financière et la santé. Le 6° suit les dispenses de mentions de L1254-21, y compris la nouvelle dispense de recopie du garant ; il ne recrée pas ces formalités.",
    "Quatorze emplacements conservés ; le 13° était déjà abrogé. Peines des infractions subsistantes : 3 750 euros et 7 500 euros en récidive ; six mois de prison seulement pour les 1°, 2°, 11°, 12° et 14° ; interdiction de deux à dix ans inchangée. Au 4°, dix-huit mois, deux renouvellements antérieurement convenus et report favorable de trois mois restent exclusivement dans le champ ancien. L1254-13 lu hors cibles conserve le report de prospection, non un nouveau CDD. L1254-15 et L1254-17 fournis prévoient une abrogation prospective avec droits anciens ; L1254-21 est effectivement modifié dans le présent lot et commande le 6°. L1254-11, L1254-14 et L1254-16 restent à coordonner dans leur lot propre : les dispositions de durée déterminée qui y figurent ne rouvrent pas de nouveaux CDD ici. L1254-16 et L1254-22, lus en entier, gardent leurs délais civils de deux jours ouvrables ; le 7° retire le délit de transmission, pas son obligation ; le 8° garde contrat commercial et copie au salarié. Au 5°, l'écrit et l'intitulé de L1254-20 restent dus malgré l'absence de délit spécial. Deux incohérences préexistantes sont signalées sans extension pénale : au 1° le renvoi L1254-5 ne vise que les services à la personne ; au 14° L1254-28 traite de médecine du travail alors que L4121-1 à L4121-5 traitent de santé et sécurité générales. Leur coordination pénale précise reste nécessaire. Les exigences supérieures d'information et de sanctions effectives de la directive 2019/1152 ne sont pas effacées par ces coupes, et leur conformité n'est pas certifiée.",
    'material_reduction',
    "La source officielle entière contient quatorze rubriques et des peines uniformes. Trois incriminations actives sont retirées, le seul retard commercial n'est plus pénalement sanctionné et la prison en récidive est désormais ciblée. Ce dernier ciblage et la dispense relative au garant vont au-delà du brouillon. Les obligations écrites, les prélèvements cités dans les comptes et les garanties financières ne sont pas abolis.",
    "Les sanctions documentaires restantes demeurent des amendes. Les anciens contrats gardent leur régime de durée et leurs droits. L'effectivité des sanctions maintenues et les deux incohérences de renvoi demandent coordination, sans résultat financier net démontré.",
    "Aucune charge nouvelle n'est identifiée : les sanctions restantes sont préexistantes et non augmentées. La référence au contrat unique applique la mesure commune ; aucun document, registre ou agrément de substitution n'est créé. Le compte d'activité et la garantie financière étaient déjà obligatoires.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "La récidive est punie de six mois d'emprisonnement et de 7 500 euros d'amende.", "La récidive est punie de 7 500 euros d'amende. Pour les seuls manquements prévus aux 1°, 2°, 11°, 12° et 14°, elle est également punie de six mois d'emprisonnement.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Les suppressions d'incriminations et l'exclusion de la sanction du seul retard prévues par le présent article", "Les suppressions d'incriminations, l'exclusion de la sanction du seul retard et la suppression de l'emprisonnement en récidive pour les manquements des 4°, 6°, 8°, 9° et 10° prévues par le présent article")
reduction(a,
    "Abrogation de l'incrimination spéciale du terme ou de la durée minimale du CDD de portage au 3°.",
    "Abrogation du délit d'absence d'intitulé exact au 5° et du délit de défaut de transmission du contrat au salarié au 7°.",
    "Suppression de la sanction pénale du seul retard de conclusion du contrat commercial et de remise de sa copie au 8°.",
    "Suppression de six mois d'emprisonnement en récidive pour les manquements des 4°, 6°, 8°, 9° et 10°, avec maintien des amendes et de l'interdiction judiciaire.")
effect(a, 'compliance_cost_reduced', 'portage-depenalisation-formalites-contractuelles',
    "Retrait ciblé des délits de forme et de peines de prison ; les obligations civiles ne sont pas comptées comme abrogées.",
    "Délits autonomes aux 3°, 5° et 7°, retard au 8° et prison de six mois pour la récidive de toutes les infractions actives.",
    "3°, 5° et 7° abrogés ; seul retard au 8° non pénal ; prison conservée seulement aux 1°, 2°, 11°, 12° et 14°.",
    'other', 'Entrepreneurs de portage salarial',
    "À l'entrée en vigueur et pour les faits antérieurs selon la loi pénale plus douce ; droits et recours civils conservés.",
    "Aucune nouvelle amende ou démarche substituée ; les amendes et l'interdiction restantes ne sont pas augmentées.",
    "La récidive est punie de six mois d'emprisonnement et de 7 500 € d'amende.",
    "La récidive est punie de 7 500 euros d'amende. Pour les seuls manquements prévus aux 1°, 2°, 11°, 12° et 14°, elle est également punie de six mois d'emprisonnement.")
for measure, source_quote, description in [
    ('portage-suppression-descriptif-contractuel', "6° De conclure un contrat de travail en portage salarial ne comportant pas l'ensemble des clauses et mentions prévues aux articles L. 1254-15 ou L. 1254-21 ;", "La sanction ne rétablit pas le descriptif contractuel supprimé dans L1254-21."),
    ('portage-suppression-comptes-rendus-salarie', "6° De conclure un contrat de travail en portage salarial ne comportant pas l'ensemble des clauses et mentions prévues aux articles L. 1254-15 ou L. 1254-21 ;", "La sanction ne rétablit pas les comptes rendus périodiques supprimés dans L1254-21."),
    ('portage-dispense-recopie-garant-financier', "6° De conclure un contrat de travail en portage salarial ne comportant pas l'ensemble des clauses et mentions prévues aux articles L. 1254-15 ou L. 1254-21 ;", "La sanction respecte la dispense nouvelle de recopier le garant déjà communiqué.")]:
    effect(a, 'coordination', measure, description,
        "Le 6° sanctionne l'absence de l'ensemble des mentions de L1254-21, sans dispense source de recopie.",
        "Le 6° exclut expressément les mentions supprimées et les informations dispensées de répétition.",
        'legal_duty', 'Entrepreneurs de portage soumis au 6°',
        "Suivant l'entrée en vigueur et les dispenses de L1254-21 ; application de la loi pénale plus douce.",
        "Coordination de la même mesure, sans seconde suppression indépendante ni obligation nouvelle.",
        source_quote, "Les mentions supprimées et les informations dispensées de répétition ne peuvent donner lieu à sanction ;")

a = article('L1262-2',
    "Coordination de fond conservée après examen intégral : la relation d'emploi pendant le détachement et les deux cas de mise à disposition identifient l'employeur responsable et ne constituent pas une formalité redondante. Le bénéfice de l'indemnité de fin de mission reste ouvert aux futurs CDD valablement régis par une loi étrangère ; la réforme française ne les convertit pas automatiquement. L'exception existante des CDI étrangers est conservée. Il n'existe ici ni taxe, agrément, déclaration, délai minimal ou justificatif autonome à retirer sans atteindre ces fonctions et le cadre supérieur du détachement.",
    "Source, deux cas, exception et note de 2019 lus entièrement. L1251-32 conserve pour son champ ancien 10 % de la rémunération totale brute, versement à chaque mission avec le dernier salaire et mention au bulletin ; L1251-33 comprend les dispenses des 1°, 2° et 4° et un 3° déjà abrogé. Leurs propositions limitent le champ français aux anciens contrats ; une base explicite maintient ici les mêmes droits et exceptions pour les futurs CDD étrangers, sans leur appliquer le zéro avant un an ou 0,20 mois. Le renvoi n'écarte pas la détermination de la loi réellement applicable et ne valide pas un montage fictivement étranger. La note historique vise le 30 juillet 2020 et réserve les salariés roulants visés à L1321-1 du code des transports selon les I et II de l'article 7 de l'ordonnance 2019-116 : maintien exact de cette réserve, pas une date d'entrée en vigueur de la réforme future. Ces deux textes extérieurs ne sont pas joints ; leur contenu n'est pas inventé ni réputé réécrit. Le règlement Rome I et les directives détachement/intérim gardent leur champ et restent à coordonner. Aucun nouveau renvoi numéroté n'est introduit.",
    'coordination_only',
    "La proposition maintient les deux possibilités de détachement et les garanties de la source entière. Elle empêche qu'une restriction temporelle des cibles françaises ferme l'indemnité aux futurs CDD étrangers éligibles. Ce maintien et la distinction de loi applicable sont une coordination, sans réduction autonome de prélèvement ou de démarche. Aucune coupe supplémentaire au brouillon n'est justifiée par la fonction des conditions restantes.",
    "Les contrats réellement soumis au droit français ne peuvent devenir des CDD sous couvert de détachement. Les transporteurs roulants conservent leur réserve propre et les règles supérieures ne sont pas purgées. Les cibles extérieures non jointes et l'effectivité européenne ne sont pas certifiées.",
    "Aucune charge nouvelle n'est identifiée : la relation de travail préexistante, les garanties d'accueil et l'indemnité éventuelle existaient dans la source par renvoi. Il n'est ajouté ni déclaration, ni attestation, ni conversion obligatoire du contrat étranger.")
effect(a, 'coordination', 'detachement-maintien-indemnite-mission-etrangere',
    "Maintien du bénéfice et des exceptions actuels de l'indemnité pour les futurs contrats étrangers, face à la transition nationale des cibles.",
    "Application de L1251-32 et L1251-33 aux salariés détachés, sauf CDI dans le pays d'origine.",
    "Même indemnité et mêmes exceptions pour les CDD valablement soumis à une loi étrangère, même conclus après la réforme.",
    'legal_duty', 'Salariés intérimaires détachés en France sous CDD régi par une loi étrangère',
    "La loi étrangère doit être réellement applicable ; l'exception CDI d'origine et les droits anciens restent maintenus.",
    "Aucun nouveau dépôt ou contrôle documentaire créé ; pas de conversion automatique.",
    "Les dispositions du chapitre Ier du titre V du présent livre relatives au travail temporaire sont applicables aux salariés détachés dans le cadre d'une mise à disposition au titre du travail temporaire, à l'exception des articles L. 1251-32 et L. 1251-33 pour les salariés titulaires d'un contrat de travail à durée indéterminée dans leur pays d'origine.",
    "Pour un salarié détaché titulaire d'un contrat de travail à durée déterminée régulièrement régi par une loi étrangère, les droits à l'indemnité de fin de mission, son calcul et son versement restent déterminés par les articles L. 1251-32 et L. 1251-33 dans leur rédaction antérieure à l'entrée en vigueur de la loi instituant le contrat de travail unique, y compris pour les contrats étrangers conclus après cette entrée en vigueur.")

a = article('L1262-7',
    "Maintien intégral de la source, sans nouvelle reformulation. L'exclusion des entreprises de travail temporaire et agences de mannequins de la dispense sectorielle de courte durée conserve le contrôle de l'employeur et de la mise à disposition dans ces relations triangulaires. L'article ne crée aucun dossier propre. Son abrogation isolée ne rendrait pas l'intérim éligible à L1262-6, dont le champ demeure limité à certains détachements de L1262-1 : aucun allègement fictif n'est revendiqué. La phrase stylistique du brouillon n'apportait pas de réduction réelle ; elle est écartée au profit de la source nécessaire.",
    "Alinéa unique et ses deux définitions relus. L1262-6 lu en entier dans travail.json : dispense des I et II de L1262-2-1, activités et durées listées par arrêté, réserves antifraude et règles de protection, adaptations documentaires possibles par décret. L7123-12 lu en entier : agence qui embauche et rémunère des mannequins mis provisoirement à disposition à titre onéreux. L'arrêté d'activités et de durées n'est pas joint, aucune liste n'est extrapolée. L1251-2 fourni reste une définition du secteur ; son projet de contrat unique ne convertit pas les contrats étrangers. Aucun renvoi de rupture n'est ajouté. Le maintien de cette exclusion ne crée ni n'élargit une taxe et ne supprime aucun avantage existant dans le champ actuellement éligible de L1262-6.",
    'retained_necessary',
    "Après examen de la source entière et du brouillon, maintien sans changement : la règle sectorielle empêche une dispense administrative inadaptée à ces mises à disposition et conserve la traçabilité de l'employeur. Aucune obligation autonome, aucun doublon ni prélèvement susceptible d'être retiré dans cet alinéa n'est identifié. L'article ne compte pas comme réécrit ou simplifié.",
    "Les obligations et dispenses générales de détachement ne sont pas toutes examinées dans cet article. L'arrêté extérieur de L1262-6 manque ; aucun achèvement de sa révision ni gain global n'est allégué. Les lois étrangères et régimes publics ne sont pas convertis.",
    "Aucune charge nouvelle n'est identifiée, puisque le texte officiel reste intégralement applicable et n'est pas modifié. Aucun formulaire, délai, registre, justificatif ou condition de remplacement n'est institué.")
a.update(status='retained_unchanged', proposed_xml=None)

a = article('L2143-2',
    "Réduction de fond déjà acquise et conservée après seconde passe : suppression des six mois d'ancienneté et des fenêtres de totalisation de dix-huit ou six mois pour la désignation syndicale des salariés temporaires. Aucun seuil résiduel ni justificatif de substitution n'est nécessaire au libre choix du syndicat. Le champ couvre les anciens contrats de mission, les CDI intérimaires, le nouvel emploi unique et les intermissions, sans étendre la dispense au personnel permanent interne. Les autres conditions, contestations et protections restent nécessaires à leur objet.",
    "Alinéa entier relu. L2143-1, lu dans le corpus, conserve âge de dix-huit ans, droits civiques, condition générale d'un an et réduction à quatre mois : le texte spécial dispense les seuls salariés temporaires de toute ancienneté, sans retour de ces seuils généraux. L2142-1-2, lu entier, rend cette règle applicable aux représentants de section syndicale ; aucune nouvelle procédure n'est ajoutée. L'ancien « Ce délai » relatif aux six mois n'a plus à être interprété défavorablement pour les désignations futures puisque toutes les fenêtres sont supprimées. Mandats, régularité et recours concernant les désignations antérieures gardent leur droit. Les autorisations de licenciement des salariés protégés ne sont pas remplacées par le préavis individuel de quinze jours. Aucun renvoi normatif nouveau n'est ajouté.",
    'material_reduction',
    "Par rapport à la source officielle entière, l'accès des salariés temporaires à la désignation syndicale n'exige plus six mois d'ancienneté ni un décompte des contrats dans une fenêtre. La réduction concerne une condition d'accès au mandat, pas un prélèvement ni une suppression de protection. Le brouillon contient déjà toute cette coupe ; aucune autre condition de cet article ne reste à retirer.",
    "Le personnel permanent interne demeure hors dispense. Représentativité, âge, droits civiques, publicité, contestation et protections sont maintenus ailleurs. Les conséquences financières et le nombre de désignations supplémentaires ne sont pas établis.",
    "Aucune charge documentaire nouvelle n'est identifiée : pas de registre ni preuve de remplacement de l'ancienneté. Davantage de salariés peuvent devenir protégés par leur désignation ; les autorisations et recours correspondants restent ceux du mandat préexistant, sans chiffrage d'un solde net pour les employeurs.")
reduction(a,
    "Suppression de la condition spéciale de six mois d'ancienneté pour la désignation syndicale des salariés temporaires.",
    "Suppression de la totalisation des contrats de mission dans les dix-huit mois et de la fenêtre spéciale de six mois des entreprises ou établissements nouveaux.")
effect(a, 'obligation_removed', 'interim-suppression-anciennete-designation-syndicale',
    "Retrait du seuil et du calcul d'ancienneté pour accéder à la désignation syndicale.",
    "Six mois de liens par contrats de mission, totalisés sur dix-huit mois ; fenêtre réduite à six mois lors de la création ou ouverture.",
    "Aucune ancienneté pour les salariés temporaires, y compris sous CDI et avant première mission ; autres conditions maintenues.",
    'legal_duty', 'Salariés temporaires, syndicats et entreprises de travail temporaire',
    "Désignations à compter de l'entrée en vigueur ; mandats et recours antérieurs gardent leurs règles ; personnel permanent interne exclu.",
    "Aucun seuil ou justificatif substitué ; protections du mandat inchangées pour les nouveaux titulaires.",
    "Dans les entreprises de travail temporaire, la condition d'ancienneté pour être désigné délégué syndical est fixée à six mois pour les salariés temporaires.",
    "Dans les entreprises de travail temporaire, aucune condition d'ancienneté n'est exigée des salariés temporaires pour être désignés délégués syndicaux.")

a = article('L2241-9',
    "Réduction de fond : le brouillon supprimait déjà l'examen annuel autonome et la nouvelle remise d'informations accessibles. La coupe est prolongée par la suppression expresse du rapport distinct et du délai minimal général de remise pour cette négociation, dont les quinze jours de D2241-1. Les trois thèmes, notamment les salaires par sexe, restent nécessaires à une négociation éclairée et à l'égalité. Les périodicités légales supplétives et les engagements conventionnels autonomes sont conservés. Les prévisions de CDD portent sur les anciens contrats sans autoriser de nouveaux termes.",
    "Cinq alinéas source et trois numéros relus. L2241-1 et L2241-5 prévoient notamment les périodicités négociées de quatre ans, L2241-7 l'application supplétive, et L2241-8 la négociation annuelle salariale : tous ont été lus intégralement dans le corpus, sans être supprimés ici. D2241-1 lu entier impose un rapport au moins quinze jours avant la négociation de L2241-8, puis les informations utiles. La règle législative nouvelle retire expressément cette forme distincte et ce minimum général ; D2241-1 doit être réécrit en coordination hors du lot pour ne pas les rétablir. Les dates librement convenues en application du 4° de L2241-5 restent autonomes. Les données accessibles doivent être exactes, à jour et effectivement utilisables ; aucun rapport reconstitué ou attestation de réemploi n'est requis. Aucun chiffre de salaire ni écart par sexe n'est supprimé. L'article ne crée aucun CDD, ni ne ferme une aide future du contrat unique.",
    'material_reduction',
    "La source entière impose un examen au moins annuel et habilite le règlement pour l'information. L'examen suit désormais la négociation selon sa périodicité propre, les données exactes accessibles ne sont plus remises en double et aucun rapport distinct ni minimum général de remise n'est exigé. Ces deux dernières précisions complètent le brouillon pour neutraliser effectivement la contrainte réglementaire identifiée. Les thèmes utiles restent entiers.",
    "La négociation annuelle supplétive et les calendriers conventionnels autonomes peuvent continuer d'imposer une cadence annuelle ou une remise anticipée. D2241-1 est identifié à coordonner, non déclaré déjà réécrit. La source législative ne chiffre pas elle-même les quinze jours : ce délai a été vérifié dans le règlement public, et n'est pas compté comme une seconde coupe autonome.",
    "Aucune charge nouvelle n'est identifiée : aucun portail, document, registre ni attestation de réemploi. L'exigence d'une présentation permettant une négociation éclairée reprend la finalité des informations préexistantes ; elle n'ajoute ni thème, ni délai fixe ni donnée obligatoire.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Leur présentation doit permettre une négociation éclairée.</p>", "Leur présentation doit permettre une négociation éclairée. Pour la négociation salariale visée au présent article, aucun rapport distinct ni délai minimal général de remise des informations n'est requis. Les dates de remise librement fixées par un accord organisant la négociation restent applicables.</p>")
reduction(a,
    "Suppression de l'examen annuel d'information autonome lorsque la négociation salariale suit une autre périodicité légalement admise.",
    "Suppression de la remise répétée des informations exactes et à jour déjà effectivement accessibles et du document supplémentaire de même contenu.",
    "Suppression du rapport distinct et du délai minimal général de remise pour la négociation salariale, en coordination expresse avec les quinze jours de D2241-1.")
effect(a, 'obligation_merged', 'branche-information-salariale-integree-negociation',
    "Examen intégré à la négociation et réemploi des données ; la contrainte réglementaire de rapport distinct est expressément écartée.",
    "Examen au moins annuel des trois thèmes, avec information précisée par règlement ; D2241-1 impose un rapport distinct remis au moins quinze jours avant la négociation.",
    "Examen lors de la négociation selon sa périodicité propre ; données accessibles réutilisées, pas de rapport distinct ni minimum général de remise ; calendriers conventionnels conservés.",
    'legal_duty', 'Négociateurs de branche et organisations fournissant les informations salariales',
    "Dès l'entrée en vigueur ; droits antérieurs conservés ; négociation supplétive annuelle et engagements autonomes subsistent.",
    "Seuls éléments manquants ou modifiés à fournir ; aucune attestation ni reporting de remplacement. Le délai réglementaire n'est pas une seconde mesure comptée.",
    "La négociation sur les salaires est l'occasion, pour les parties, d'examiner au moins une fois par an au niveau de la branche les données suivantes :",
    "Pour la négociation salariale visée au présent article, aucun rapport distinct ni délai minimal général de remise des informations n'est requis.")

a = article('L2254-2',
    "Réduction de fond supplémentaire : l'accord doit toujours définir ses objectifs contrôlables mais n'est plus tenu de leur consacrer un préambule distinct. Cette coupe coordonne la suppression générale du préambule déjà proposée dans L2222-3-3. Les six subdivisions, les clauses facultatives, le mois de refus, la fenêtre patronale de deux mois, les règles de forfait, le chômage et l'abondement CPF sont conservés pour leur fonction de consentement, de santé et de sécurisation du salarié. Les ruptures du contrat unique suivent exactement les quinze jours décomptés le lendemain de la notification et le barème ordinaire en mois complets, sans retrancher la première année une fois le seuil atteint.",
    "Relecture des dix-neuf alinéas sources et de tout le brouillon. Le renvoi source au « 1° du I de L2253-1 » était inexact : la cible fournie n'a pas de I ; la proposition vise expressément son 1°, sans changer les minima. Un et deux mois maintenus au IV et V ; ils ne sont pas le préavis. L1234-3 fourni impose de compter les quinze jours depuis le lendemain de présentation, réception ou remise régulière ; la formule imprécise du brouillon est rectifiée. L1234-9 fourni impose le prorata des mois complets, non journalier ; la note antérieure demandant son alignement sur un autre prorata est écartée. Seuil d'un an au terme effectif, préavis inclus, calcul sur toute l'ancienneté, 0,20 mois par année et plafond légal de six mois ; faute grave et indemnités plus favorables gardent le champ de la cible. Pour les anciens contrats, seuil de huit mois et part acquise selon taux antérieurs avec salaire de référence à la rupture, sans double compte. L1232-2 à L1232-6 fournis conservent entretien, défense, assistance et motivation avec leurs transitions de convocation ; ils ne promettent pas une procédure totale en quinze jours. Les procédures collectives distinctes et autorisations de salariés protégés restent réservées. L3121-41, 42, 44, 47, 55 et 64 ont aussi été lus entièrement dans le corpus : 1 607 heures et trente-cinq heures en moyenne, périodes d'un ou trois ans, neuf semaines, prévenance et garanties de forfait restent propres ; les dérogations à L3121-55 et au 5° du I de L3121-64 demeurent limitées à la simple modification. L6323-11 fourni et R6323-3-2 lu entier conservent l'abondement spécial, dont minimum réglementaire de 3 000 euros et information sous quinze jours dans ce dernier texte ; aucune suppression de cet avantage futur n'est décidée. L2222-3-3, absent des cibles, a été lu entier source et proposition : sa suppression générale du préambule ne suffisait pas à retirer l'exigence spéciale ici supprimée. Ce n'est pas un nouveau renvoi normatif. Les renvois nouveaux à L1234-3 sont fournis ; aucun renvoi numéroté inédit à une cible non fournie n'est introduit.",
    'mixed',
    "Par rapport à la source entière, le préambule distinct cesse d'être obligatoire, tandis que tous les objectifs, garanties et avantages de l'accord sont conservés. Le préavis et l'indemnité relèvent de mesures communes coordonnées, pas de réductions supplémentaires à additionner ici. Le préavis nouveau peut aussi allonger le préavis dû avant six mois d'ancienneté lorsque le régime antérieur aurait prévu moins de quinze jours. Le solde net de ces coupes et coordinations n'est pas établi.",
    "Le mois de refus, les deux mois pour engager la procédure, les majorités, le contrôle du juge et les autorisations spéciales demeurent. Les minima acquis, les garanties plus favorables, le CPF, les congés et les réparations d'illégalité subsistent. Le décret CPF et les textes réglementaires de rupture nécessitent leur coordination propre sans être déclarés réécrits ici.",
    "Aucun nouveau registre, dépôt, déclaration ou justificatif n'est créé. Le préavis garanti dès l'embauche peut néanmoins dépasser une durée antérieure inférieure à quinze jours ; le calcul de deux composantes pour les anciens contrats est aussi une opération de coordination à recenser. Le refus de l'accord n'est pas une faute grave : l'extension générale du préavis à cette faute dans la cible n'est pas comptée ici comme une charge de ce licenciement spécifique. Aucun solde global des codes n'est chiffré.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "mentionnés au 1° du I de l'article L. 2253-1", "mentionnés au 1° de l'article L. 2253-1")
a['proposed_xml'] = replace_once(a['proposed_xml'], "II. – L'accord énonce ses objectifs dans son préambule. Il peut préciser :", "II. – L'accord définit ses objectifs, sans qu'un préambule distinct soit obligatoire. Il peut préciser :")
a['proposed_xml'] = replace_once(a['proposed_xml'], "le préavis individuel est de quinze jours calendaires à compter de sa notification régulière.", "le préavis individuel est de quinze jours calendaires, décomptés à partir du lendemain de la présentation, de la réception ou de la remise de la notification écrite dans les conditions de l'article L. 1234-3.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "les fractions d'année étant retenues au prorata,", "les fractions d'année étant retenues au prorata des mois complets,")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Il est soumis aux modalités et conditions des articles L. 1232-2", "Il est soumis aux seules modalités et conditions des articles L. 1232-2")
a['proposed_xml'] = replace_once(a['proposed_xml'], "Les modalités de salaire de référence relèvent de l'article L. 1234-9 et de ses textes d'application.", "Les autres conditions d'ouverture, le salaire de référence et les garanties conventionnelles ou contractuelles plus favorables relèvent de l'article L. 1234-9 et de ses textes d'application.")
a['proposed_xml'] = replace_once(a['proposed_xml'], "La présente rédaction ne remet pas en cause les créances et recours nés avant son entrée en vigueur.", "La suppression de l'obligation de préambule distinct s'applique aux accords conclus à compter de l'entrée en vigueur de la loi la portant. Les préambules des accords antérieurs conservent leur portée et aucun accord déjà conclu n'est à refaire. La présente rédaction ne remet pas en cause les créances et recours nés avant son entrée en vigueur.")
reduction(a, "Suppression de l'obligation spéciale de définir les objectifs de l'accord de performance collective dans un préambule distinct, sans retirer les objectifs ni leur contrôle.")
effect(a, 'obligation_removed', 'accords-suppression-preambule-obligatoire',
    "Retrait de l'exigence spéciale de préambule dans l'accord de performance collective, coordonné avec la mesure générale.",
    "Objectifs de l'accord obligatoirement dans son préambule.",
    "Objectifs toujours définis dans l'accord, sans préambule distinct obligatoire.",
    'legal_duty', "Signataires d'accords de performance collective",
    "Accords conclus à compter de l'entrée en vigueur de la suppression ; anciens préambules et accords conservés sans réédition.",
    "Aucun exposé, annexe ou déclaration de remplacement ; contenu des objectifs maintenu.",
    "II. – L'accord définit dans son préambule ses objectifs et peut préciser :",
    "II. – L'accord définit ses objectifs, sans qu'un préambule distinct soit obligatoire.")
effect(a, 'coordination', 'contrat-unique-preavis-quinze-jours',
    "Application du préavis commun à la rupture après refus de l'accord, sans compter une seconde réduction.",
    "Renvoi aux durées de L1234-1 pour ce licenciement spécifique : moins de six mois selon régime applicable, un mois entre six mois et deux ans, deux mois ensuite, sauf dispositions plus favorables.",
    "Nouveaux contrats uniques : quinze jours calendaires dès le lendemain de la notification régulière, selon L1234-3 et les garanties communes ; anciens contrats gardent leur champ.",
    'calendar_days', "Salariés licenciés après refus d'un accord de performance collective et leurs employeurs",
    "Nouveaux contrats à compter de la réforme ; procédures et autorisations distinctes maintenues, transitions de notification des cibles respectées.",
    "Le nouveau plancher de quinze jours peut dépasser le préavis antérieur applicable avant six mois d'ancienneté ; solde net non établi. Le refus de l'accord ne constitue pas une faute grave.",
    "Ce licenciement est soumis aux seules modalités et conditions définies aux articles L. 1232-2 à L. 1232-14 ainsi qu'aux articles L. 1234-1 à L. 1234-11, L. 1234-14, L. 1234-18, L. 1234-19 et L. 1234-20.",
    "Pour l'application du V à un contrat de travail unique conclu à compter de l'entrée en vigueur de la loi qui l'institue, le préavis individuel est de quinze jours calendaires, décomptés à partir du lendemain de la présentation, de la réception ou de la remise de la notification écrite dans les conditions de l'article L. 1234-3.")
effect(a, 'coordination', 'contrat-unique-indemnite-ordinaire',
    "Application du barème commun et de sa transition, distinct du CPF et des réparations d'illégalité.",
    "Indemnité de licenciement par renvoi à L1234-9 : droit à huit mois hors faute grave, taux réglementaires ; avantages conventionnels et créances distinctes.",
    "Nouveau contrat : aucune indemnité ordinaire avant un an au terme effectif préavis inclus ; ensuite 0,20 mois de salaire brut de référence par année totale, mois complets au prorata, plafond légal six mois ; employeur seul.",
    'other', "Employeurs et salariés dont le contrat unique est rompu après refus de l'accord",
    "Anciens droits et composante acquise préservés selon L1234-9 ; première année incluse dès seuil atteint ; indemnités plus favorables et spéciales distinctes.",
    "Calcul transitoire de deux composantes pour les anciens contrats, sans nouvel enregistrement obligatoire ni double compte.",
    "Ce licenciement est soumis aux seules modalités et conditions définies aux articles L. 1232-2 à L. 1232-14 ainsi qu'aux articles L. 1234-1 à L. 1234-11, L. 1234-14, L. 1234-18, L. 1234-19 et L. 1234-20.",
    "L'indemnité ordinaire due à l'initiative de l'employeur est nulle avant un an d'ancienneté et, à compter d'un an, égale à 0,20 mois de salaire de référence par année d'ancienneté totale, les fractions d'année étant retenues au prorata des mois complets, dans la limite légale de six mois de ce salaire.")

# Chaque analyse vise la source officielle et la proposition fournie, sans
# attribuer à cette dernière la valeur du droit en vigueur.
checks = {
 'L1254-17': {
  'L1234-1': "La cible proposée règle le préavis patronal de quinze jours pour les nouveaux contrats, non le renouvellement du portage. L'abrogation du renouvellement ne rompt pas automatiquement un CDI ni ne raccourcit le préavis des anciens contrats ; notification et protections suivent leurs règles propres.",
  'L1221-2': "La cible proposée interdit tout nouveau terme et renouvellement après la réforme. L1254-17 applique cette interdiction même à une faculté inscrite dans une clause ancienne, tout en préservant les renouvellements déjà convenus, sans nouvel essai ni remise à zéro d'ancienneté.",
  'L1254-12': "Source : plafond total de dix-huit mois, renouvellements compris ; note historique sur les contrats en cours. Proposition : abrogation future avec maintien du plafond pour les anciens contrats et report de prospection. La transition de L1254-17 vise expressément cette ancienne rédaction et ne rétablit pas de plafond du nouvel emploi.",
  'L1234-9': "L'indemnité ordinaire proposée s'ouvre à un an au terme effectif préavis inclus, puis 0,20 mois par année totale, fractions en mois complets et plafond six mois. Elle n'est pas une indemnité de renouvellement : les primes et créances des anciens CDD restent à leurs faits générateurs, sans versement automatique du seul fait d'une conversion."
 },
 'L1254-21': {
  'L1234-1': "L'information contractuelle du portage ne modifie pas le préavis : la cible proposée prévoit quinze jours pour les nouveaux contrats et conserve l'ancien régime. L'absence de prestation au II n'est ni une notification patronale ni une dispense de préavis payé en cas de rupture effective.",
  'L1221-2': "La cible proposée impose l'emploi sans terme aux nouvelles embauches, même si la prestation est limitée. Les mentions maintenues portent sur ce lien continu ; la fin d'une prestation ne crée ni nouvel essai ni fin automatique du contrat. Les dispenses de recopie ne rouvrent pas de CDD.",
  'L1234-9': "Le II propre au portage ne supprime pas l'indemnité ordinaire lors d'une rupture patronale effective : cible proposée à un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, mois complets et plafond six mois. Les mentions financières ne remplacent ni les anciens minima acquis ni les congés ou indemnités spéciales."
 },
 'L1255-1': {
  'L1234-1': "Les indemnités de préavis du personnel permanent licencié après interdiction suivent la cible : quinze jours pour les nouveaux contrats, ancien régime pour les autres. La réduction de peine ne dispense pas de notification, de préavis ou des procédures collectives et autorisations distinctes.",
  'L1251-2': "La source définit l'entrepreneur qui recrute et rémunère les salariés selon une qualification convenue. La proposition ajoute le contrat unique et les garanties d'intermission. L1255-1 conserve l'incrimination de ces conditions, sans transformer une affectation temporaire en emploi à terme ; seule la prison en récidive est retirée.",
  'L1221-2': "La définition du nouvel emploi sans terme ne doit pas disparaître avec une peine de prison. L1255-1 conserve amendes et interdiction pour le manquement sectoriel, sans autoriser de nouveaux CDD ou renouvellements ; les créances des contrats antérieurs demeurent distinctes.",
  'L1234-9': "L'indemnité de licenciement du personnel permanent relève du barème commun et de sa transition : un an au terme effectif pour le nouveau contrat, 0,20 mois par année totale et mois complets, six mois de plafond légal. Les réparations de L1235 visées en supplément ne sont pas soumises au zéro avant un an.",
  'L1235-3': "La cible n'a pas de proposition et demeure une source officielle : réintégration possible, puis indemnité selon les deux tableaux lus intégralement, avec minima spécifiques des entreprises de moins de onze salariés et maxima allant jusqu'à vingt mois. Ces réparations d'une absence de cause réelle et sérieuse ne sont ni le barème ordinaire de L1234-9 ni plafonnées à six mois par ce renvoi."
 },
 'L1255-2': {
  'L1234-1': "Les infractions documentaires et radiologiques ne règlent pas le préavis de rupture de l'emploi. La cible proposée de quinze jours n'est déclenchée que par une rupture régulièrement notifiée du nouveau contrat ; elle ne dispense pas des affectations de santé ni des autorisations de salariés protégés.",
  'L1251-16': "Le 1° pénal reste limité aux mentions des 1° et 3° de cette cible. La proposition y substitue une lettre de mission et dispense de recopier des informations déjà accessibles et exactes. L1255-2 respecte ces dispenses, ne sanctionne pas la disparition d'une mention légalement supprimée et n'exige aucun nouveau contrat pour chaque mission.",
  'L1251-17': "La source et la proposition maintiennent deux jours ouvrables suivant la mise à disposition. La proposition autorise l'envoi de la lettre et des seules informations non déjà communiquées. L1255-2 retire la peine du seul retard mais pas l'obligation civile ni les recours, et ne transforme pas la dépénalisation en délai supplémentaire.",
  'L1251-26': "Le 3° incorpore seulement les garanties du deuxième alinéa : qualification, rémunération, horaire et transport sans modification essentielle. Le délai radiologique est celui de L1251-34. L'exclusion de L1251-26 pour le CDI intérimaire ne neutralise pas cette incorporation ciblée ; le barème de rupture de l'emploi n'est pas appliqué à une simple proposition de mission.",
  'L1221-2': "La cible proposée interdit les nouveaux CDD, y compris par renouvellement. Les propositions exigées au 3° de L1255-2 sont donc des affectations dans un emploi continu, sans terme d'emploi ; les anciens contrats conservent leurs droits civils et les effets de la loi pénale plus douce demeurent distincts.",
  'L1251-34': "La vue actuelle est déjà rédigée en affectations : délai maximal de trois jours ouvrables, quatre garanties essentielles et exposition appréciée par rapport à la durée totale des missions. Le 3° conserve ces conditions et la dérogation de durée sans créer un nouveau CDD ; l'ancienne réserve du brouillon prétendant cette cible non coordonnée est retirée.",
  'L1234-9': "Le seuil d'un an au terme effectif et le barème proposé de 0,20 mois par année totale, prorata des mois complets et plafond six mois concernent la rupture patronale de l'emploi. Ils ne suppriment ni les rémunérations garanties d'intermission ni les droits de santé ou réparations civiles que protège L1255-2.",
  'L1251-47': "La proposition de cette cible retire la fermeture pour seul défaut déclaratif et conserve la fermeture pour défaut de garantie avec risque sérieux, mise en demeure et plafond de deux mois. Le renvoi pénal reste son deuxième alinéa indemnitaire, inchangé en position ; le renvoi historique à L1235-5 ne doit pas être interprété comme une indemnité inexistante."
 },
 'L1255-4': {
  'L1234-1': "Le préavis proposé de quinze jours règle la rupture d'un nouvel emploi, pas l'achèvement d'une affectation irrégulière. L1255-4 n'autorise aucune rupture automatique ni dispense de notification ou de protections spéciales ; l'ancien régime de préavis demeure pour les anciens contrats.",
  'L1221-2': "La cible proposée interdit tout nouveau contrat à terme. Le troisième alinéa de L1255-4 limite donc le renvoi à L1251-6 aux cas d'affectation chez l'utilisateur, sans redonner un terme au contrat unique ni modifier les droits des contrats de mission antérieurs.",
  'L1234-9': "L'infraction de recours irrégulier n'est pas un fait générateur d'indemnité ordinaire. La cible proposée exige, pour la rupture patronale du contrat nouveau, un an au terme effectif préavis inclus, puis 0,20 mois par année totale avec mois complets et plafond six mois ; elle laisse les recours et réparations d'illégalité autonomes.",
  'L1251-6': "Source et proposition distinguent la tâche précise et temporaire du premier alinéa et les cinq cas de recours, avec les réserves de L1251-7. Le renvoi de L1255-4 conserve exactement ces deux branches de l'infraction ; aucune exception favorable n'est supprimée et aucune durée de mission n'est transformée en durée de l'emploi."
 },
 'L1255-6': {
  'L1234-1': "Le retrait du délit de terme n'écarte pas le préavis patronal de la cible proposée : quinze jours pour les nouveaux contrats et droits antérieurs préservés. La fin d'affectation reste distincte de la notification de rupture de l'emploi, et les autorisations spéciales ne sont pas dépénalisées ici.",
  'L1221-2': "L'abrogation de la sanction du terme ne rétablit pas un contrat à terme. La cible proposée impose le nouveau contrat unique et interdit ses renouvellements en CDD ; les anciens contrats de mission conservent leurs droits de terme sous réserve des seuls effets pénaux plus doux.",
  'L1251-11': "La source et la proposition ont été lues entièrement : terme précis, cinq exceptions et durée minimale restent des règles d'affectation dans le nouveau champ. L1255-6 retire leur seul délit autonome, sans abroger ces conditions ni confondre leur durée avec le préavis de rupture de l'emploi.",
  'L1234-9': "L'abrogation d'une incrimination de terme ne substitue pas le barème ordinaire aux indemnités ou salaires des anciens CDD. La cible proposée concerne la rupture patronale effective du nouveau contrat avec un an préavis inclus, 0,20 mois par année totale, mois complets et plafond six mois ; les créances civiles antérieures restent distinctes."
 },
 'L1255-14': {
  'L1234-1': "Le nouveau préavis patronal de quinze jours ne supprime pas les protections pénales financières ou de santé du portage. La réduction des sanctions de forme n'est ni une notification de rupture ni une dispense de préavis ; anciens préavis et procédures spéciales restent dans leur champ.",
  'L1221-2': "La cible proposée ferme tout nouveau CDD et renouvellement, même sous régime spécial. Le 2° de L1255-14 suit cette règle ; le 4° ne maintient que les durées des anciens contrats et le report favorable légalement applicable, sans recréer un terme automatique du nouvel emploi.",
  'L1254-15': "La source contient les clauses du CDD, y compris les subdivisions 1° a à i et 2° a à h ; la proposition abroge cette liste pour l'avenir et la conserve pour les anciens contrats. Le 6° pénal de L1255-14 ne peut la rétablir pour les nouveaux CDI ni exiger la réédition des anciens écrits.",
  'L1254-20': "La source exige l'écrit et un intitulé précis ; la proposition garde l'écrit et prévoit l'intitulé du nouveau contrat sans refaire les anciens CDI. Le 5° de L1255-14 supprime l'incrimination de l'intitulé, pas cette obligation civile ni les droits à l'information ; aucune nouvelle forme pénalement exclusive n'est créée.",
  'L1254-21': "La vue fournie retirait déjà les 3° et 7°, fusionnait le 2° et dispensait de recopier le 6°. La proposition finale du présent lot ajoute au 8° la dispense de recopier le garant déjà communiqué. Le 6° pénal respecte l'ensemble de ces dispenses selon leur champ temporel ; il ne recrée ni descriptif ni reporting du salarié.",
  'L1254-7': "La source admettait CDD ou CDI ; la proposition impose le contrat unique pour les nouveaux recrutements et distingue la durée commerciale. Le 2° conserve une sanction du non-respect de cette règle, et le maintien des anciens contrats ne donne pas droit à un nouveau CDD après la réforme.",
  'L1254-12': "La source limite la durée totale à dix-huit mois et vise L1254-17. La proposition abroge le plafond pour les nouveaux emplois et réserve anciens contrats, renouvellements déjà convenus et report de prospection. Le 4° pénal n'est maintenu que dans ce champ historique ; il ne limite pas la durée du nouvel emploi.",
  'L1254-17': "La source ouvre deux renouvellements et impose clause ou avenant avant terme ; la vue proposée abroge pour l'avenir et réserve les renouvellements déjà convenus. L1255-14, 4°, suit la proposition finale de ce lot et n'autorise ni faculté ancienne activée après réforme ni nouveau renouvellement, tout en conservant le report de prospection distinct.",
  'L1234-9': "Les sanctions de forme du portage ne modifient pas l'indemnité ordinaire : cible proposée à un an au terme effectif préavis inclus, 0,20 mois par année totale en mois complets et plafond légal six mois. Les primes des anciens CDD, salaires et congés ne sont pas effacés ni transformés en cette indemnité par la dépénalisation."
 },
 'L1262-2': {
  'L1234-1': "Le renvoi aux règles françaises de travail temporaire ne rend pas automatiquement applicable le préavis du contrat privé français à tout contrat étranger. Le projet de quinze jours doit respecter la loi réellement applicable et les règles impératives de détachement ; la seule fin du détachement ne rompt pas un CDI étranger.",
  'L1251-32': "La source prévoit 10 % de la rémunération totale brute, versés à chaque mission avec le dernier salaire et indiqués au bulletin, sauf embauche immédiate en CDI par l'utilisateur. La proposition limite ce droit aux anciens contrats français. L1262-2 conserve explicitement l'ancienne rédaction pour les futurs CDD étrangers éligibles, sans leur appliquer le barème ordinaire ou une extinction temporelle indue.",
  'L1221-2': "Le champ international est expressément distingué : la proposition française de contrat unique ne convertit pas un CDD réellement régi par une loi étrangère. Cette réserve ne valide pas un contrat fictivement étranger ni un nouveau CDD relevant effectivement du droit français ; l'emploi subsiste durant le détachement.",
  'L1251-33': "Les dispenses sources des 1°, 2° et 4° et l'emplacement 3° déjà abrogé ont été lus ; la proposition les réserve aux anciens contrats. L1262-2 maintient ces exceptions avec l'indemnité dans les futurs CDD étrangers éligibles, tandis que l'exception générale des CDI du pays d'origine demeure. Aucun avantage n'est fermé par la transition nationale.",
  'L1234-9': "La proposition d'indemnité ordinaire d'un an, 0,20 mois par année totale et six mois de plafond ne remplace pas l'indemnité de mission des détachés en CDD étranger. Son application dépend de la loi et du champ propres du contrat ; ancienneté préavis inclus et prorata de mois complets ne sont pas étendus artificiellement aux 10 % de fin de mission."
 },
 'L1262-7': {
  'L1234-1': "L'article maintenu délimite une dispense de détachement, non un régime de rupture. Le préavis proposé de quinze jours ne découle pas de cette exclusion pour les contrats étrangers ; sa loi applicable et la notification restent à déterminer selon leur champ propre, sans conversion par définition sectorielle.",
  'L1251-2': "Le renvoi sert uniquement à identifier les entreprises exclues de cette section de dispense. La source définit l'entrepreneur recruteur et payeur ; la proposition y ajoute le nouvel emploi sans terme et les intermissions. Le maintien de L1262-7 n'incorpore pas artificiellement ces règles françaises à tous les contrats étrangers.",
  'L1221-2': "L'exclusion de la dispense ne constitue pas un cas de recours au CDD. La cible proposée de contrat unique s'applique à son champ de droit français, avec anciens contrats préservés ; L1262-7 n'y déroge pas et ne convertit pas davantage un contrat étranger régulier.",
  'L1234-9': "Aucun renvoi indemnitaire n'existe dans l'alinéa maintenu. Le barème proposé à un an au terme effectif, préavis inclus, puis 0,20 mois par année totale et plafond six mois, reste étranger à la définition d'une dispense de contrôle du détachement ; ni les droits étrangers ni les anciens minima ne sont absorbés par cet article."
 },
 'L2143-2': {
  'L1234-1': "La dispense d'ancienneté pour la désignation syndicale n'est pas une dispense d'autorisation de licenciement. Le préavis proposé de quinze jours pour le nouveau contrat ne commence qu'à sa notification régulière après les protections applicables ; les anciens contrats gardent leur préavis propre.",
  'L1221-2': "La désignation est ouverte aux salariés mis à disposition sous nouvel emploi sans terme, avant leur première mission et pendant les intermissions. La cible proposée n'autorise aucun CDD nouveau ; le maintien des anciens contrats permet de leur appliquer aussi la dispense d'ancienneté sans prolonger leur terme.",
  'L1234-9': "La suppression des six mois pour un mandat ne supprime pas la condition indemnitaire distincte : cible proposée à un an au terme effectif préavis inclus, puis 0,20 mois par année totale, mois complets et plafond six mois. Un délégué protégé avant un an conserve les réparations d'une illégalité et les garanties spéciales, indépendantes de cette indemnité ordinaire."
 },
 'L2241-9': {
  'L1234-1': "L'information salariale de branche n'est pas une notification de licenciement. Les prévisions d'emploi ne déclenchent pas les quinze jours proposés et n'abolissent ni les anciens préavis ni les autorisations ou procédures collectives ; la suppression d'un délai de remise d'information a un objet distinct.",
  'L1221-2': "Le 1° distingue les seuls CDD conclus avant la réforme et les missions qui peuvent être accomplies dans un CDI. Cette référence statistique ne peut autoriser ni nouvelle embauche à terme ni renouvellement ; les futurs emplois éligibles aux aides restent possibles sous contrat unique.",
  'L1234-9': "L'examen des salaires et des prévisions ne constitue pas un motif de suppression d'indemnités. Le barème proposé reste celui d'une rupture patronale effective, seuil d'un an préavis inclus et calcul de 0,20 mois par année totale en mois complets, plafond six mois, avec les anciennes composantes et les réparations spéciales conservées."
 },
 'L2254-2': {
  'L1232-2': "La source impose entretien, modes de convocation et cinq jours ouvrables ; la proposition supprime le minimum chiffré mais conserve le temps effectif de préparation et le report nécessaire. Le renvoi du V suit sa transition selon la date de convocation, non la date de signature de l'accord, sans promettre une procédure totale de quinze jours.",
  'L1232-3': "La cible fournie est seulement le droit officiel : l'employeur indique les motifs et recueille les explications lors de l'entretien. Le renvoi du V conserve cette défense effective après refus de l'accord ; ni le motif spécifique ni le préavis nouveau ne permettent de la supprimer.",
  'L1232-4': "La source et la proposition conservent l'assistance interne ou par conseiller en l'absence de représentants. La dispense proposée d'indiquer les adresses ne vaut qu'avec accès effectif et gratuit à la liste. Le V n'ajoute aucun protocole ni nouvelle liste et suit la transition de convocation de la cible.",
  'L1232-5': "L'habilitation proposée au décret exclut le retour du mode exclusif, du délai minimal général ou des adresses lorsque dispensées. Le V conserve ce renvoi d'exécution sans réintroduire ces contraintes à travers la procédure spéciale de refus d'accord ; le droit effectif à l'entretien demeure.",
  'L1234-1': "Le renvoi du V applique la cible proposée aux nouveaux contrats : quinze jours calendaires sans condition d'ancienneté ; les anciens contrats gardent leurs durées et conditions plus favorables. La règle générale de la cible sur la faute grave ne requalifie pas le refus de l'accord en faute. Procédures collectives distinctes et autorisations ne sont pas absorbées dans ce délai individuel.",
  'L1234-2': "La proposition écarte pour le nouveau contrat les clauses de préavis unilatéral différentes de quinze jours et précise qu'une dispense d'exécution n'avance pas, à elle seule, le terme. Le V doit lire cette règle avec les conditions de compensation et la transition des anciens contrats, sans annuler les dispenses favorables de champ distinct.",
  'L1234-3': "Le brouillon comptait imprécisément depuis la notification ; la proposition finale compte depuis le lendemain de la présentation recommandée ou de la réception/remise régulière admise. Fin au quinzième jour calendaire même non travaillé ; cette précision concerne le préavis, non le mois de refus ou la fenêtre patronale de deux mois.",
  'L1234-4': "La cible précise que l'inexécution n'avance pas la fin du contrat, y compris pour les quinze jours, avec réserve de fin d'essai et reports protecteurs. Le seuil indemnitaire du V se mesure donc au terme effectif préavis inclus, pas au dernier jour travaillé ou à la seule notification.",
  'L1234-5': "La proposition sépare compensation du préavis et indemnité ordinaire : salaires, avantages et congés du préavis restent dus si l'employeur dispense ou ne respecte pas les quinze jours. Le zéro avant un an et le plafond six mois du V ne limitent pas cette compensation. La règle générale de la cible sur la faute grave ne transforme pas en faute le refus de cet accord ; l'inexécution volontaire du salarié garde son champ propre.",
  'L1234-6': "La cible conserve le salaire de référence de préavis en cas de fermeture ou baisse d'horaire : durée légale ou conventionnelle du temps plein, durée contractuelle du temps partiel. Le renvoi du V ne réduit pas ce salaire par le seul passage à quinze jours et ne confond pas les seuils hebdomadaires avec les seuils d'aménagement.",
  'L1234-7': "La cessation de l'entreprise ne dispense pas du préavis, conservé ou payé ; la proposition réserve séparément force majeure et sinistre. Le licenciement après refus de l'accord ne transforme pas cette cessation en dispense générale de quinze jours ni en extinction de salaire.",
  'L1234-10': "La cessation ne libère pas de l'indemnité due selon L1234-9 ; la proposition renvoie à ses conditions et composantes, non à une indemnité automatique. Le V conserve ce champ avec seuil et plafond applicables, sans utiliser la fermeture pour retirer les anciens droits ou les indemnités distinctes.",
  'L1234-14': "La cible étend certaines règles à des agents non fonctionnaires et à des salariés sous statut public comparable, selon leurs conditions propres. Le V ne convertit pas un contrat public en contrat unique privé et ne peut attribuer les quinze jours ou le nouveau barème à tout agent par ce seul renvoi.",
  'L1234-18': "Le décret proposé ne peut changer un an, 0,20 mois et six mois ni réduire la composante acquise. Le V suit cette hiérarchie, laisse le salaire de référence et l'affectation des périodes à leurs textes et ne traite pas le décret comme une autorisation de réintroduire la première année en franchise déduite.",
  'L1221-2': "La référence au nouveau contrat vise seulement les relations nouvelles dans le champ privé de la réforme. La durée de l'accord, de la formation financée ou d'un forfait ne devient pas un terme de l'emploi ; le refus suit une procédure de rupture et ne permet pas de recruter ou renouveler un CDD.",
  'L1234-9': "La cible proposée exige un an d'ancienneté ininterrompue à la fin effective préavis inclus, hors faute grave ; 0,20 mois sur toute l'ancienneté, prorata des mois complets et plafond légal six mois, employeur seul. Le V reprend exactement ces paramètres. Pour les anciens contrats, huit mois et composante acquise restent protégés ; indemnités plus favorables, CPF et réparations ne sont pas plafonnés par assimilation.",
  'L2253-1': "Le texte fourni n'a pas de subdivision I : le renvoi source au « 1° du I » est rectifié explicitement vers son 1° sur les minima hiérarchiques. Les garanties de branche, dont égalité et rémunération du portage, demeurent ; les coordinations des 7°, 8° et 10° ne rétablissent pas CDD ou renouvellement d'essai dans l'accord de performance.",
  'L1232-6': "La proposition impose un écrit motivé à date certaine et retire l'attente minimale générale après entretien, avec ses réserves disciplinaires et de protection ; sa transition dépend de la convocation. Le V garde entretien, défense et autorisations. L1234-3 décompte ensuite depuis le lendemain de la présentation ou réception régulière, sans compter une attente supprimée comme préavis.",
  'L6323-11': "La source et la proposition conservent alimentation annuelle, prorata, majorations et plafonds du CPF, dont la faveur saisonnière coordonnée dans les emplois uniques. Le VI maintient l'abondement spécial après refus de l'accord hors alimentation annuelle et plafond, pour les futurs licenciements éligibles aussi ; le barème de rupture ne l'absorbe pas.",
  'L1234-11': "La cible maintient la continuité d'ancienneté en suspension, distingue les périodes comptables et les assimilations, puis confirme le terme effectif préavis inclus. Le V retient cette ancienneté reconnue et, au seuil d'un an, toute la période sans soustraire la première année ; les anciennes et nouvelles composantes ne prennent pas deux fois la même période.",
  'L1234-8': "La proposition écarte toute condition d'ancienneté pour le nouveau préavis de quinze jours et préserve les règles de suspension des anciens préavis. Le V ne doit donc pas importer le seuil indemnitaire d'un an dans le droit au préavis ; les suspensions ne ramènent pas ce nouveau délai au-dessous de quinze jours."
 }
}

for item in out:
    required = refs['requirements'][item['code_id'] + '|' + item['source_id']]
    analyses = checks[item['number']]
    assert {refs['targets'][k]['number'] for k in required} == set(analyses), item['number']
    item['reference_checks'] = []
    for key in required:
        target = refs['targets'][key]
        assessment = analyses[target['number']]
        assert len(assessment) >= 80
        item['reference_checks'].append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))

Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles': len(out), 'reference_checks': sum(len(a['reference_checks']) for a in out), 'effects': sum(len(a['substantive_impact']['effects']) for a in out)}, ensure_ascii=False))
