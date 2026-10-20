import json
import xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = []


def add(i, xml, reason, notes, removed=None, repeal=None, benefit=None):
    src = sources[i]
    for expression in ('la loi instituant le contrat unique à durée indéterminée',
                       'la loi instituant le contrat unique',
                       'la loi de simplification'):
        xml = xml.replace(expression, 'la loi portant la présente réforme')
    if i in (4, 5):
        notes += " Coordination européenne à vérifier au titre de l'exigence de sanctions effectives, proportionnées et dissuasives de la directive 2008/104/CE sur le travail intérimaire, notamment son article 10 : le retrait de cette seule contravention de relevé ne vaut pas suppression du contrôle ou des sanctions protégeant les droits substantiels. La conformité d'ensemble n'est pas présumée à partir de cette seule rédaction."
    if i == 10:
        notes += " Les exigences européennes d'information et de consultation effectives des travailleurs, notamment celles de la directive 2002/14/CE, et d'égalité professionnelle ne sont pas écartées : vérifier la coordination du contenu minimal et de l'accès utile aux informations, sans assimiler l'allègement de présentation à une dispense de consultation."
    obj = {k: src[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    obj.update(proposed_xml=xml.strip(), reason=reason, review_notes=notes, status='rewrite_draft')
    if removed:
        obj.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal:
        obj.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    if benefit:
        obj['benefit_review'] = benefit
    answers.append(obj)


add(0, '''
<p>L'entreprise de travail temporaire informe, par tout moyen, les salariés temporaires de chacun de ses établissements :</p>
<p>1° De la communication des informations nominatives figurant dans les relevés de contrats de mission à l'opérateur France Travail et au directeur régional des entreprises, de la concurrence, de la consommation, du travail et de l'emploi territorialement compétent ;</p>
<p>2° Des droits d'accès et de rectification prévus aux articles 39 et 40 de la loi du 6 janvier 1978 susvisée. Les salariés peuvent exercer ces droits auprès de l'opérateur France Travail et du directeur régional mentionné au 1°.</p>
<p>Pour les relations de travail conclues à compter de l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, l'information concerne les données des missions exécutées dans le cadre du contrat unique à durée indéterminée. La durée ou la fin d'une mission ne détermine pas la durée ou la fin de l'emploi. Les contrats conclus avant cette entrée en vigueur et les droits qui en résultent conservent leur régime antérieur.</p>
''',
    "Réécriture à droit constant des destinataires, de la liberté du moyen d'information et des droits des salariés, puis coordination prospective avec l'intérim à durée indéterminée. L'information sur l'usage de données nominatives remplit une fonction essentielle de protection des personnes et reste obligatoire ; sa suppression ne serait pas un simple retrait de doublon. Aucun nouveau relevé, justificatif ou envoi n'est créé.",
    "Sources R1251-7, R1251-8 et L1251-46 lues intégralement : le relevé sert notamment à la vérification des droits au revenu de remplacement, y compris lorsque l'emploi se poursuit entre deux missions. L1251-58-1 à L1251-58-5 distinguent emploi et missions ; la garantie mensuelle et les intermissions ne sont pas modifiées. Le renvoi source aux articles 39 et 40 de la loi du 6 janvier 1978 et la dénomination régionale sont anciens : leur concordance avec la loi modifiée, le RGPD et l'organisation administrative actuelle appelle une coordination explicite, non réalisée ici hors corpus ; ces références ne limitent pas les droits supérieurs applicables. La note d'entrée en vigueur au 1er juillet 2024 n'est pas la date de la réforme proposée. Aucun délai de rupture, droit à aide ou garantie financière n'est supprimé.")

add(1, '''
<p>Sans préjudice des mentions expressément prescrites par la loi, les documents de l'entreprise de travail temporaire, notamment les contrats de mise à disposition et les contrats de mission, ne sont soumis, au titre du présent article, à aucune obligation de mentionner le nom et l'adresse du garant ou la référence à l'article L. 1251-49.</p>
<p>Dans chaque établissement, l'entreprise affiche de manière visible le nom et l'adresse de son garant ainsi que les dates de prise d'effet et d'échéance de la garantie.</p>
<p>La suppression des mentions documentaires s'applique à compter de l'entrée en vigueur de la loi de simplification, y compris aux documents relatifs à des contrats antérieurs. Aucun document déjà établi n'a à être refait. La garantie financière, les créances qu'elle couvre et les droits de la mettre en œuvre demeurent régis par les dispositions qui leur sont applicables.</p>
''',
    "Réduction de fond : suppression de la répétition du nom et de l'adresse du garant et de la référence légale sur tous les documents de l'entreprise. L'affichage visible, qui permet au salarié d'identifier le garant, reste obligatoire avec ses deux dates ; la référence légale n'a plus à être affichée. La garantie protégeant salaires et cotisations est conservée, sans déclaration de remplacement.",
    "Coordination interne avec R1255-6 et R1254-2 du présent lot. L1251-49 et R1251-14 lus : couverture, attestation, montant, contrôle et mise en œuvre de la garantie ne sont pas abrogés. R1255-5 conserve son champ distinct. Pour le portage, les mentions législatives d'identité du garant de L1254-15, L1254-21 et L1254-23 subsistent : un règlement ne les supprime pas. Les contrats et missions antérieurs ne perdent aucune garantie ; la suppression de formalités documentaires profite aussi aux documents futurs. Les contrats de mission cités dans cet article ne constituent pas une autorisation de nouvelles embauches à durée déterminée.",
    removed=[
        "Obligation de répéter sur tous les documents de l'entreprise le nom et l'adresse du garant financier.",
        "Obligation de reproduire la référence à L1251-49 sur les documents et dans l'affichage relatif à la garantie."
    ])

add(2, '''
<p>Les règles de constitution et de mise en œuvre de la garantie financière fixées au paragraphe 2 de la sous-section unique de la section 3 du chapitre Ier du titre V du livre II de la première partie du présent code, dans sa partie réglementaire, s'appliquent aux entreprises de portage salarial, à l'exception des articles R. 1251-12, R. 1251-18 et R. 1251-25 à R. 1251-29. Elles sont appliquées avec les adaptations suivantes :</p>
<p>1° Les termes « entrepreneur de travail temporaire » et « entreprise de travail temporaire » désignent l'entreprise de portage salarial ;</p>
<p>2° La dispense de mentions documentaires prévue au premier alinéa de l'article R. 1251-15 s'applique aux contrats de travail de portage salarial et aux contrats commerciaux de prestation de portage salarial. Elle ne dispense pas des mentions d'identité du garant expressément exigées par les articles L. 1254-15, L. 1254-21 et L. 1254-23, dans leur champ respectif. Le nom et l'adresse du garant ainsi que les dates de prise d'effet et d'échéance de la garantie sont affichés de manière visible dans chaque établissement de l'entreprise de portage salarial, conformément au deuxième alinéa de l'article R. 1251-15 ;</p>
<p>3° Pour l'application de l'article R. 1251-13, la masse salariale remplace le chiffre d'affaires ;</p>
<p>4° Les références aux articles L. 1251-49, L. 1251-50, L. 1251-51 et L. 1251-52 désignent respectivement le I de l'article L. 1254-26, le II du même article, le III du même article et le I du même article.</p>
<p>La dispense prévue au 2° s'applique à compter de l'entrée en vigueur de la loi de simplification, y compris aux documents concernant des contrats antérieurs, sans réfection des documents déjà établis. Elle ne réduit ni la garantie ni les créances et recours antérieurs. Pour les relations de travail conclues à compter de l'entrée en vigueur de la loi instituant le contrat unique, l'emploi est à durée indéterminée ; la durée d'une prestation commerciale ne met pas fin à l'emploi. Les anciens contrats conservent leur régime jusqu'à leur terme, sans possibilité de conclure ou de renouveler un contrat de travail à durée déterminée après cette entrée en vigueur.</p>
''',
    "Réécriture des règles d'adaptation et réduction effective des mentions réglementaires répétées, en cohérence avec R1251-15. Les exceptions, les quatre adaptations, le calcul par masse salariale et les quatre correspondances législatives demeurent. Le 2° est remplacé par une règle opératoire, car l'ancienne substitution de mots deviendrait sans objet après la suppression des mentions générales. Les obligations législatives d'identification du garant et l'affichage utile sont conservés.",
    "R1251-11 à R1251-29 et L1254-26 lus pour vérifier l'assiette, les exclusions, la défaillance et la garantie : ne pas appliquer au portage le minimum de 8 % du chiffre d'affaires de R1251-12, expressément exclu. Les exceptions R1251-25 à R1251-29 sont intégralement conservées, sans étendre au client du portage la substitution de l'entreprise utilisatrice. L1251-50 à L1251-52 lus pour vérifier les quatre correspondances : le III de L1254-26 correspond à l'attestation de L1251-51 ; le I est conservé comme correspondance source de L1251-52 dans les dispositions importées, les règles de substitution restant exclues. L1254-15 1° i, L1254-21 I 8° et L1254-23 8° lus : leur mention d'identité du garant a une base législative autonome ; sa suppression éventuelle nécessiterait leur modification expresse, non réalisée dans ce lot. Aucun salaire général entre prestations n'est créé : L1254-21 II et L1254-8 restent à leur champ, contrairement aux garanties propres au CDI intérimaire. La déclaration en double exemplaire/recommandé encore prévue par R1254-4, lu, reste hors de ce lot : son articulation avec L1254-27 fourni, qui ne vise que l'obtention de la garantie, appelle un examen exprès ; elle n'est pas réputée supprimée ici.",
    removed=[
        "Mentions réglementaires générales répétées du garant et de la référence légale sur les documents de portage, hors exigences législatives autonomes.",
        "Reproduction obligatoire d'une référence légale dans l'affichage de garantie des établissements de portage."
    ])

add(3, '''
<p>La conclusion d'un contrat de mission dépourvu de l'une des mentions exigées aux 2°, 4° et 5° de l'article L. 1251-16 est punie de l'amende prévue pour les contraventions de la troisième classe.</p>
<p>Le présent article ne permet ni de conclure ni de renouveler un contrat de mission constituant un contrat de travail à durée déterminée à compter de l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée. Les contrats antérieurs et les faits relatifs à leur conclusion restent soumis aux règles antérieures, sous réserve de l'application de la loi pénale plus douce. La fin d'une mission exécutée dans le cadre d'un emploi à durée indéterminée ne met pas fin à cet emploi.</p>
''',
    "Réécriture de la contravention sans modifier sa classe ni les trois mentions visées. La qualification professionnelle, l'essai expressément stipulé et le rapatriement aux frais de l'employeur constituent des informations protectrices : l'amende n'est pas traitée comme une simple sanction de format. La transition interdit de lire le maintien du texte comme une faculté de conclure de nouveaux contrats de travail à terme.",
    "L1251-16 lu en entier : les 2°, 4° et 5° concernent respectivement la qualification, la durée de l'essai éventuel et le rapatriement hors du territoire métropolitain, avec caducité de cette dernière clause lors d'une rupture à l'initiative du salarié. Ces conditions restent dans l'article de fond. L1251-58-5 adapte déjà L1251-16 à la lettre de mission ; son articulation pénale avec R1255-1 doit être rendue explicite dans la coordination législative du contrat unique, sans étendre ici par analogie une incrimination à la lettre de mission. Les essais des contrats nouveaux relèvent du régime de trois mois sans renouvellement, sans nouvel essai à chaque mission. Ni montant d'amende nouveau ni suppression d'une réparation civile ne sont proposés.")

penal_transition = '''<p>Cette abrogation s'applique à compter de l'entrée en vigueur de la loi de simplification. Les faits antérieurs qui n'ont pas donné lieu à une condamnation passée en force de chose jugée bénéficient de la loi pénale plus douce dans les conditions de l'article 112-1 du code pénal. Lorsque ces faits perdent leur caractère d'infraction, la peine cesse de recevoir exécution dans les conditions de l'article 112-4 du même code.</p>'''

add(4, '''
<p>Le présent article est abrogé. L'absence de transmission à l'opérateur France Travail du relevé des contrats de mission dans le délai prévu à l'article R. 1251-7 ne donne plus lieu à la contravention de troisième classe instituée par le présent article.</p>
''' + penal_transition + '''
<p>Cette abrogation ne supprime ni l'obligation prévue à l'article L. 1251-46 ni les droits des salariés au revenu de remplacement, ni les obligations déclaratives et les infractions reposant sur un fondement distinct. Elle ne crée aucune déclaration ou sanction de remplacement.</p>
''',
    "Abrogation de fond de la contravention autonome réprimant le défaut ou le retard de remise du relevé. La collecte d'informations utile aux droits des salariés demeure ; la sanction pénale réglementaire supplémentaire n'a pas de fonction essentielle distincte démontrée. La réduction porte sur la coercition pénale et ne prétend pas supprimer, par cette seule abrogation, la déclaration législative.",
    "L1251-46 et R1251-7 lus : délai avant le 20 de chaque mois et relevé par établissement demeurent dans leurs textes, sans modification fictive. Leur simplification par réemploi de données sociales exigerait une coordination explicite de L1251-46 et R1251-7/R1251-8 et des règles de transmission de données ; elle n'est pas présentée comme réalisée. R1255-4 est également abrogé dans ce lot. Application des articles 112-1 et 112-4 du code pénal à coordonner dans le texte d'entrée en vigueur, sans maintien d'une répression abolie pour les dossiers en cours. Les fraudes et entraves ayant un fondement propre ne sont pas dépénalisées. La note source du 1er juillet 2024 reste historique.",
    repeal="Suppression de la contravention de troisième classe sanctionnant l'absence ou le retard du relevé des missions adressé à France Travail ; obligations de fond distinctes maintenues.")

add(5, '''
<p>Le présent article est abrogé. La transmission à l'opérateur France Travail d'un relevé des contrats de mission qui n'est pas conforme aux prescriptions de l'article R. 1251-8 ne donne plus lieu à la contravention de deuxième classe instituée par le présent article.</p>
''' + penal_transition + '''
<p>Cette abrogation ne supprime ni les obligations d'information résultant de l'article L. 1251-46 et de ses dispositions d'application ni les infractions ayant un fondement distinct. Elle ne crée aucune formalité ou sanction de remplacement.</p>
''',
    "Abrogation effective de la contravention autonome attachée à la non-conformité du relevé. Les données utiles à l'ouverture et au contrôle des droits demeurent exigibles dans leurs textes ; une amende pénale spécifique de présentation est retirée sans la transformer en pénalité équivalente.",
    "R1251-8 lu en entier : modèle fixé par arrêté, données sur l'utilisateur, identité et missions, rémunération brute, et caractère facultatif du Siret ou Siren. L'abrogation ne modifie pas silencieusement ces éléments ni n'invente un formulaire nouveau. Les éventuelles fausses déclarations relevant d'une infraction autonome gardent leur régime. Coordination avec R1255-3 du lot et avec les articles 112-1 et 112-4 du code pénal pour les faits anciens et les peines en cours. Ne pas attribuer à cette abrogation une suppression du relevé ou des règles de protection des données. La note source du 1er juillet 2024 n'est pas une entrée en vigueur de la réforme.",
    repeal="Suppression de la contravention de deuxième classe attachée à la non-conformité du relevé des missions aux prescriptions de R1251-8, sans nouvelle pénalité équivalente.")

add(6, '''
<p>L'absence, sur les documents de l'entreprise de travail temporaire, du nom et de l'adresse du garant ou de la référence à l'article L. 1251-49 n'est pas punie au titre du présent article.</p>
<p>La méconnaissance des obligations d'affichage des informations sur la garantie financière prévues au deuxième alinéa de l'article R. 1251-15 est punie de l'amende prévue pour les contraventions de la deuxième classe.</p>
<p>La suppression de l'incrimination des omissions documentaires s'applique à compter de l'entrée en vigueur de la loi de simplification. Les faits antérieurs non définitivement jugés bénéficient de la loi pénale plus douce conformément à l'article 112-1 du code pénal ; les peines relatives aux faits qui perdent leur caractère d'infraction cessent de recevoir exécution dans les conditions de l'article 112-4 du même code. Les obligations et infractions ayant un fondement distinct conservent leur champ.</p>
''',
    "Réduction de fond coordonnée : suppression de l'amende pour les mentions documentaires répétitives retirées de R1251-15. L'amende de deuxième classe protégeant l'accès visible au garant reste applicable, avec le contenu d'affichage allégé de cet article. Les deux alinéas sources gardent leur place et une transition pénale est ajoutée.",
    "Le deuxième alinéa de R1251-15 du présent lot conserve le nom et l'adresse du garant et les dates de prise d'effet et d'échéance ; la référence légale n'est plus à afficher. Le renvoi pénal ne la réintroduit donc pas. La garantie, l'attestation et les sanctions autonomes de R1255-5 subsistent. Pour le portage, les mentions législatives autonomes restent distinctes. Transition selon 112-1/112-4 du code pénal, sans prétendre annuler les condamnations définitives ou rembourser automatiquement les amendes acquittées.",
    removed=[
        "Contravention de deuxième classe pour omission du garant ou de la référence légale sur les documents, en coordination avec la suppression de cette obligation."
    ])

add(7, '''
<p>La déclaration d'identification du salarié prévue à l'article D. 133-13-1 du code de la sécurité sociale comporte les informations suivantes. Les données exactes et à jour dont l'organisme gestionnaire dispose légalement sont réutilisées ; l'employeur ne fournit que les informations manquantes ou modifiées. Aucune attestation supplémentaire n'est exigée pour ce réemploi.</p>
<p>1° Les informations relatives au salarié et à son embauche prévues aux 2° et 3° de l'article R. 1221-1, relatif à la déclaration préalable à l'embauche ;</p>
<p>2° Les informations relatives à l'emploi :</p>
<p>a) La nature du contrat de travail. Pour les contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat unique, il s'agit d'un contrat à durée indéterminée. Pour un contrat à durée déterminée conclu avant cette entrée en vigueur, sont indiqués son motif de recours et sa date de fin, sans que ces mentions permettent un nouveau contrat à durée déterminée ou son renouvellement après cette date ;</p>
<p>b) La durée du travail ;</p>
<p>c) La durée de la période d'essai, lorsqu'un essai est stipulé ;</p>
<p>d) La catégorie et la nature de l'emploi ainsi que, le cas échéant, son niveau hiérarchique et son coefficient ;</p>
<p>e) Le cas échéant, l'intitulé de la convention collective applicable ;</p>
<p>f) Le montant de la rémunération et de chacune de ses composantes, y compris les primes et accessoires de salaire lorsqu'il en existe ;</p>
<p>g) Le cas échéant, les particularités du contrat de travail ;</p>
<p>h) Le taux de la cotisation due au titre des accidents du travail et des maladies professionnelles, lorsque plusieurs taux s'appliquent dans l'établissement et que celui du salarié n'est pas déjà connu de l'organisme gestionnaire ;</p>
<p>i) Les abattements applicables à l'assiette ou au taux des cotisations. L'organisme gestionnaire applique ceux dont les conditions sont établies par les données légalement disponibles ; l'employeur complète, s'il y a lieu, les seuls éléments manquants permettant d'en bénéficier ;</p>
<p>j) Le taux de cotisation de prévoyance spécifique au salarié, lorsqu'il existe et n'est pas déjà connu de l'organisme gestionnaire ;</p>
<p>k) Le cas échéant, l'assujettissement au versement de transport, sans nouvelle indication lorsque cette information est déjà disponible auprès de l'organisme gestionnaire ;</p>
<p>l) Le cas échéant, le caractère de première embauche dans l'établissement, s'il ne ressort pas déjà des données de l'organisme gestionnaire ;</p>
<p>3° La signature de l'employeur et, lorsque la déclaration tient lieu de contrat de travail, celle du salarié. La signature par le salarié d'un contrat distinct dans les conditions de l'article D. 1272-4 dispense de signer à nouveau la déclaration d'identification.</p>
<p>L'employeur transmet au salarié une copie de la déclaration d'identification dans les délais prévus par le présent code. La remise par l'organisme gestionnaire, pour le compte de l'employeur et dans les mêmes délais, vaut transmission par celui-ci ; aucune seconde remise du même document n'est exigée.</p>
<p>Ces simplifications s'appliquent aux déclarations et remises effectuées à compter de l'entrée en vigueur de la loi de simplification, y compris pour les contrats antérieurs. Elles ne subordonnent à aucune démarche supplémentaire les abattements, exonérations, aides ou dispenses applicables. Les situations futures éligibles au sein du contrat unique demeurent admises aux avantages de même objet ; les droits antérieurs sont préservés. La durée d'une mission, d'une formation ou d'une aide ne constitue pas une date de fin d'emploi.</p>
''',
    "Réduction de fond des doubles saisies et remises : réemploi des données légalement disponibles, dispense de ressaisir les taux connus, une seule signature du salarié lorsque le contrat distinct est déjà signé, et remise par l'organisme pour le compte de l'employeur sans copie supplémentaire. Toutes les rubriques 1°, 2° a à l et 3° sont conservées dans leur ordre. La mention de CDD devient strictement transitoire ; les avantages ne sont pas cantonnés aux anciens contrats.",
    "D133-13-1 CSS, D1272-2 à D1272-4 et R1221-1 lus. La déclaration d'identification reste transmise avant la première déclaration de rémunération selon le CSS ; ni délai ni sanction de ce texte distinct ne sont effacés. Le réemploi n'est admis que pour des informations effectivement détenues légalement et à jour, avec possibilité de compléter/corriger. D1272-5 du lot coordonne le même volet et l'affiliation sans seconde déclaration. L'ancien doublon rédactionnel « d'identification du salarié » est retiré de l'introduction. Le terme source « versement de transport » est conservé : concordance avec le versement mobilité à vérifier expressément, sans créer un nouveau prélèvement ni étendre son champ. Le contrat unique et l'essai de trois mois sans renouvellement requièrent la coordination législative générale ; la durée de l'essai n'est pas rendue obligatoire en l'absence d'essai stipulé. Aucune modification des taux d'accidents du travail, de prévoyance ou des conditions de fond des allègements.",
    removed=[
        "Ressaisie obligatoire des données exactes et à jour, notamment des taux sociaux, déjà légalement disponibles pour l'organisme gestionnaire.",
        "Seconde signature du salarié sur le volet administratif lorsqu'un contrat distinct a déjà été régulièrement signé.",
        "Seconde remise du même volet au salarié lorsqu'il lui a déjà été remis dans les délais par l'organisme pour le compte de l'employeur."
    ],
    benefit="Le i) vise les abattements d'assiette ou de taux : ils sont conservés pour les situations présentes et futures et appliqués sur la base des données disponibles, avec complément des seuls faits manquants, sans attestation nouvelle. Le h) n'augmente aucun taux AT-MP et ne supprime aucune tarification favorable ; j) maintient la prévoyance spécifique, k) ne modifie ni champ ni dispenses du versement, et l) conserve l'information de première embauche utile aux aides. Le chèque-emploi associatif et le titre emploi-service entreprise restent des voies simplifiées ; le réemploi et la dispense de double signature ne ferment aucune de leurs facilités. Les aides et exonérations liées à une situation d'emploi, d'insertion ou de formation restent ouvertes aux futures situations de même objet dans le contrat unique. Salaires, primes, convention collective, droits acquis et garanties du salarié restent identifiés ; l'absence d'une double saisie n'est pas un motif de refus d'un avantage dont les conditions sont établies.")

add(8, '''
<p>Le volet d'identification du salarié est intégré à la déclaration prévue à l'article D. 1272-1. Il ne donne lieu ni à une seconde transmission ni à une nouvelle saisie des informations exactes et à jour déjà légalement disponibles. Il comporte les informations suivantes :</p>
<p>1° Informations relatives au salarié :</p>
<p>a) Les mentions prévues à l'article R. 1221-1, relatif à la déclaration préalable à l'embauche, sous réserve de la transition du 2° a) pour les mentions de durée déterminée ;</p>
<p>b) Son affiliation au régime général ou au régime agricole ;</p>
<p>2° Informations relatives à l'emploi :</p>
<p>a) La date de fin de l'emploi uniquement lorsqu'elle concerne un contrat de travail à durée déterminée conclu avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée. Pour les contrats conclus à compter de cette entrée en vigueur, l'emploi est à durée indéterminée ; la fin d'une mission, d'une formation ou d'une aide n'en constitue pas le terme. La présente mention ne permet aucun nouveau contrat à durée déterminée ni renouvellement d'un tel contrat après cette entrée en vigueur ;</p>
<p>b) La durée de la période d'essai, si un essai est stipulé ;</p>
<p>c) Le salaire prévu à l'embauche ;</p>
<p>d) La durée du travail ;</p>
<p>e) La nature et la catégorie de l'emploi ;</p>
<p>f) La convention collective applicable ;</p>
<p>g) Le taux de cotisation au titre des accidents du travail et, le cas échéant, celui de prévoyance, sans nouvelle indication des taux déjà connus de l'organisme gestionnaire ;</p>
<p>3° La signature de l'employeur et, lorsque la déclaration tient lieu de contrat de travail, celle du salarié. La signature d'un contrat distinct dans les conditions de l'article D. 1272-4 dispense le salarié d'une seconde signature.</p>
<p>Ces simplifications s'appliquent aux transmissions effectuées à compter de l'entrée en vigueur de la loi de simplification, y compris pour les contrats antérieurs, sans réfection des volets déjà établis. Les droits antérieurs et les avantages ouverts aux situations futures éligibles dans le contrat unique sont maintenus.</p>
''',
    "Réduction des doubles saisies et de la seconde signature lorsque l'accord du salarié figure déjà dans un contrat signé. La liste propre de D1272-5 est entièrement rédigée et son régime général ou agricole est conservé ; aucune assimilation des deux affiliations. Le renvoi introductif erroné au seul 2° de D1272-1 est remplacé explicitement par un rattachement à la déclaration unique. Le terme d'un CDD ne subsiste que pour les anciens contrats.",
    "Incohérence source identifiée : D1272-5 renvoie à un volet « prévu au 2° de D1272-1 », alors que le 2° actuel est la liste des mentions d'emploi. Correction expresse dans ce lot par intégration au document de D1272-1, et non création d'un volet supplémentaire. R1221-1 entier lu : le 1° a) importe aussi les données employeur et, pour l'agriculture, les données d'affiliation et de santé au travail ; elles demeurent exigibles lorsqu'elles manquent et ne sont pas supprimées par une formule de réemploi. Le renvoi à la nature/durée du contrat de R1221-1 ne doit pas rétablir de nouveaux CDD : la transition du 2° a) lui est expressément opposée. D133-13-1 CSS couvre les employeurs des 1°, 2° et 5° de L133-5-6 ; les exclusions des dispositifs et le guichet spectacle de D1272-3 ne sont pas élargis ici. Les taux sociaux et droits de prévoyance ne changent pas. Remise au salarié selon D1272-1/D133-13-1 maintenue.",
    removed=[
        "Nouvelle saisie ou nouvelle transmission du même ensemble d'informations d'identification déjà fourni et légalement disponible.",
        "Double signature administrative du salarié lorsqu'un contrat distinct a déjà constaté son consentement dans les formes requises."
    ])

add(9, '''
<p>À défaut de modalités différentes prévues par une convention ou un accord conclu en application de l'article L. 2262-5, l'employeur :</p>
<p>1° Informe le salarié des conventions et accords collectifs applicables dans l'entreprise ou l'établissement, dans les conditions prévues aux articles R. 1221-34 et R. 1221-35 ;</p>
<p>2° Met un exemplaire à jour de ces textes à la disposition des salariés sur le lieu de travail. Cet exemplaire peut être sur papier ou sur un support numérique effectivement accessible, gratuitement, à tous les salariés concernés sur leur lieu de travail ;</p>
<p>3° Lorsqu'il utilise l'intranet de l'entreprise pour cette mise à disposition, n'est pas tenu de conserver en plus un exemplaire sur un autre support si les conditions d'accès prévues au 2° sont remplies. Lorsque la mise à disposition est assurée sur un autre support conformément au 2°, aucune publication supplémentaire sur l'intranet n'est exigée.</p>
<p>Cette faculté s'applique à compter de l'entrée en vigueur de la loi de simplification. Elle ne dispense ni de l'information individuelle prévue au 1°, ni de l'actualisation des textes, ni des modalités conventionnelles autonomes applicables.</p>
''',
    "Réduction de fond du cumul automatique entre exemplaire sur le lieu de travail et exemplaire sur l'intranet. Un seul support suffit, à condition que tous les salariés aient un accès effectif ; l'information individuelle, les textes à jour et la primauté des modalités conventionnelles demeurent. Les trois subdivisions sont conservées.",
    "L2262-5 et R1221-34/R1221-35 lus : le 13° de R1221-34 inclut les accords applicables dans l'information du salarié, normalement communiquée au plus tard un mois après l'embauche selon R1221-35 ; cette obligation et son délai ne sont pas supprimés. Aucun renvoi à un simple site public ne remplace les accords propres à l'entreprise. Le support numérique suppose un accès réel sur le lieu de travail ; à défaut, le support papier reste nécessaire selon la modalité choisie. Ni dépôt des accords, ni transmission à la CPPNI, ni délai de négociation supprimé par negociation_collective ne sont recréés. Note source du 1er novembre 2023 : date historique uniquement.",
    removed=[
        "Cumul obligatoire de deux exemplaires à jour sur des supports différents lorsque l'entreprise dispose d'un intranet."
    ])


# La grille complète conserve ses 45 lignes et ses subdivisions ; chaque cellule
# substantielle est rédigée ci-dessous. Les suppressions sont désignées à part.
root = ET.fromstring('<root>' + sources[10]['source_xml'] + '</root>')
table = root.find('table')
for element in table.iter():
    element.attrib = {k: v for k, v in element.attrib.items() if k in ('rowspan', 'colspan')}
rows = table.findall('.//tr')


def cell(row, col, xml):
    target = rows[row][col]
    for child in list(target):
        target.remove(child)
    target.text = None
    fragment = ET.fromstring('<fragment>' + xml + '</fragment>')
    target.text = fragment.text
    for child in list(fragment):
        target.append(child)


cell(1, 1, '''<p>a) Évolution des effectifs par type de contrat, âge et ancienneté :</p>
<p>- évolution annuelle des effectifs, sans reconstitution obligatoire d'une série mois par mois ;</p>
<p>- nombre de salariés en contrat de travail à durée indéterminée ;</p>
<p>- nombre de salariés en contrat de travail à durée déterminée conclu avant l'entrée en vigueur de la loi instituant le contrat unique ;</p>
<p>- nombre de salariés temporaires ;</p>
<p>- nombre de salariés appartenant à une entreprise extérieure ;</p>
<p>- nombre de journées de travail accomplies par les salariés temporaires au cours des douze derniers mois ;</p>
<p>- nombre de contrats d'insertion et de formation en alternance ouverts aux jeunes de moins de vingt-six ans ;</p>
<p>- motifs du recours aux anciens contrats à durée déterminée, aux missions de travail temporaire et aux salariés d'entreprises extérieures. La justification particulière du recours au temps partiel n'est plus requise au titre de cette rubrique.</p>
<p>Pour les relations de travail conclues à compter de l'entrée en vigueur de la loi instituant le contrat unique, les emplois, y compris ceux d'intérim, de portage, d'insertion et d'alternance, sont à durée indéterminée. La durée d'une mission, d'une formation, d'une convention ou d'une aide n'est pas une durée d'emploi. Ces mentions ne permettent ni de conclure ni de renouveler un CDD après cette entrée en vigueur.</p>''')

cell(2, 0, '''<p>b) Évolution des emplois par catégorie professionnelle :</p>
<p>- répartition des effectifs par sexe et qualification ;</p>
<p>- actions de prévention et de formation envisagées par l'employeur, notamment pour les salariés âgés, peu qualifiés ou rencontrant des difficultés sociales particulières.</p>''')

cell(3, 0, '''<p>c) Évolution de l'emploi des personnes handicapées et mesures destinées à le développer :</p>
<p>- actions réalisées ou projetées en matière d'embauche, d'adaptation, de réadaptation ou de formation professionnelle ;</p>
<p>- informations de la déclaration annuelle prévue à l'article L. 5212-5, à l'exclusion de celles mentionnées à l'article D. 5212-4. Leur mise à disposition dans un document déjà accessible au comité dispense de les reproduire.</p>''')

cell(4, 0, '<p>d) Évolution du nombre de stagiaires âgés de plus de seize ans.</p>')

cell(5, 0, '''<p>e) Formation professionnelle : investissements en formation et publics concernés :</p>
<p>- orientations de la formation dans l'entreprise résultant de la consultation prévue à l'article L. 2312-24 ;</p>
<p>- résultats éventuels des négociations prévues à l'article L. 2241-6 ;</p>
<p>- conclusions éventuelles des services de contrôle après les vérifications effectuées en application des articles L. 6361-1, L. 6323-13 et L. 6362-4 ;</p>
<p>- pour l'année antérieure et l'année en cours, bilan agrégé des actions du plan de formation, des bilans de compétences et des validations des acquis de l'expérience réalisés, avec les effectifs concernés répartis par catégorie socioprofessionnelle et sexe. Une liste distincte action par action n'est pas exigée ;</p>
<p>- pour les mêmes années et pour chaque type de congé, nombre de congés accordés, durée totale et coût total des congés individuels de formation, de bilan de compétences, de validation des acquis de l'expérience et pour enseignement. Le détail de leur objet, des conditions de leur octroi ou de leur report et des résultats obtenus n'est pas exigé au titre de cette rubrique ;</p>
<p>- nombre de salariés bénéficiaires de l'abondement mentionné à l'avant-dernier alinéa du II de l'article L. 6315-1 et sommes versées à ce titre ;</p>
<p>- nombre de salariés ayant bénéficié de l'entretien professionnel mentionné au I de l'article L. 6315-1 ;</p>
<p>- pour l'année antérieure et l'année en cours, bilan des conditions de mise en œuvre de l'alternance : emplois occupés pendant et après l'action ou la période de professionnalisation ; effectifs par âge, sexe et niveau initial de formation ; résultats obtenus à la fin de l'action ou de la période, avec leurs modalités d'appréciation et de validation ; bilan de la mise en œuvre du compte personnel de formation.</p>''')

cell(6, 0, '''<p>f) Conditions de travail : durée et aménagement du temps de travail, y compris le temps partiel :</p>
<p>- nombre, sexe et qualification des salariés à temps partiel ;</p>
<p>- horaires à temps partiel pratiqués dans l'entreprise.</p>
<p>La base donne accès au programme annuel de prévention des risques professionnels et d'amélioration des conditions de travail prévu au 2° de l'article L. 2312-27. Établi à partir des analyses mentionnées à l'article L. 2312-9, ce programme énumère de façon détaillée les mesures prévues pour l'année à venir, notamment pour satisfaire :</p>
<p>i - aux principes généraux de prévention des articles L. 4121-1 à L. 4121-5 et L. 4221-1 ;</p>
<p>ii - aux obligations d'information et de formation des travailleurs des articles L. 4141-1 à L. 4143-1 ;</p>
<p>iii - à l'information et à la formation prévues aux articles L. 4154-2 et L. 4154-4 pour les salariés relevant de leur champ. La protection des titulaires d'anciens CDD est maintenue ; les salariés en contrat unique affectés aux mêmes postes ou missions bénéficient des protections de même objet ;</p>
<p>iv - à la coordination de la prévention des articles L. 4522-1 et L. 4522-2.</p>''')

cell(7, 1, '<p>a) Évolution des immobilisations, après déduction des amortissements et des dépréciations éventuelles.</p>')
cell(8, 0, '<p>b) Le cas échéant, montant des dépenses de recherche et développement.</p>')
cell(9, 0, "<p>c) Mesures envisagées pour améliorer, renouveler ou transformer les méthodes de production et d'exploitation, et leurs incidences sur les conditions de travail et l'emploi.</p>")

cell(11, 1, '''<p>L'analyse compare, pour chaque catégorie professionnelle, la situation chiffrée des femmes et des hommes en matière d'embauche, de formation, de promotion professionnelle, de qualification, de classification, de conditions de travail, de santé et de sécurité au travail, de rémunération effective et d'articulation entre activité professionnelle et responsabilité familiale.</p>
<p>Elle examine les écarts de salaire et de déroulement de carrière selon l'âge, la qualification et l'ancienneté, ainsi que l'évolution des taux de promotion respectifs des femmes et des hommes par métier dans l'entreprise.</p>''')

cell(12, 1, '''<p>La stratégie d'action est établie à partir de l'analyse prévue au A du 2°. Elle comprend :</p>
<p>- les mesures prises pendant l'année écoulée pour assurer l'égalité professionnelle ; le bilan des actions de cette année et, le cas échéant, de l'année précédente ; l'évaluation de la réalisation des objectifs au regard des indicateurs retenus ; les raisons pour lesquelles des actions prévues n'ont pas été réalisées ;</p>
<p>- les objectifs de progression pour l'année à venir et leurs indicateurs ; la définition qualitative et quantitative des mesures destinées à les atteindre conformément à l'article R. 2242-2 ; l'évaluation de leur coût et leur échéancier.</p>''')

cell(14, 1, "<p>a) Montant des capitaux propres de l'entreprise.</p>")
cell(15, 0, '<p>b) Emprunts et dettes financières, avec leurs échéances et charges financières.</p>')
cell(16, 0, "<p>c) Impôts et taxes, notamment, lorsque l'entreprise est concernée, les informations du rapport relatif à l'impôt sur les bénéfices prévu à l'article L. 232-6 du code de commerce. La mise à disposition de ce rapport dispense de reproduire ces informations dans un document distinct.</p>")

cell(18, 1, '''<p>a) Frais de personnel, cotisations sociales comprises ; évolution des salaires par catégorie et sexe ; salaire de base minimum et salaire moyen ou médian, par sexe et catégorie professionnelle.</p>''')
cell(19, 0, "<p>b) Pour les entreprises relevant de l'article L. 225-115 du code de commerce, montant global des rémunérations mentionnées au 4° de cet article.</p>")
cell(20, 0, "<p>c) Données relatives à l'épargne salariale : intéressement et participation.</p>")
cell(21, 0, '<p>5° Activités sociales et culturelles : montant de la contribution aux activités sociales et culturelles du comité social et économique ; mécénat.</p>')
cell(23, 0, '<p>A - Rémunération des actionnaires : revenus distribués.</p>')
cell(24, 0, "<p>B - Rémunération de l'actionnariat salarié : montant des actions détenues dans le cadre de l'épargne salariale, part du capital correspondante et dividendes reçus.</p>")

cell(26, 1, '''<p>Aides ou avantages financiers accordés à l'entreprise par l'Union européenne, l'État, une collectivité territoriale, l'un de leurs établissements publics ou un organisme privé chargé d'une mission de service public, et utilisation de ces concours.</p>
<p>Pour chaque aide sont indiqués sa nature, son objet, son montant, les conditions de versement et d'emploi éventuellement fixées par la personne publique qui l'accorde, ainsi que son emploi effectif.</p>''')
cell(27, 0, "<p>B - Réductions d'impôt dont bénéficie l'entreprise.</p>")
cell(28, 0, '<p>C - Exonérations et réductions de cotisations sociales dont bénéficie l’entreprise.</p>')
cell(29, 0, "<p>D - Crédits d'impôt dont bénéficie l'entreprise.</p>")
cell(30, 0, '<p>E - Concours reçus au titre du mécénat.</p>')
cell(31, 1, '''<p>a) Chiffre d'affaires et bénéfices ou pertes constatés ;</p>
<p>b) Résultats de l'activité en valeur et en volume ;</p>
<p>c) Affectation des bénéfices réalisés.</p>''')

cell(32, 0, '<p>8° Partenariats de sous-traitance :</p>')
cell(33, 0, "<p>A - Partenariats dans lesquels l'entreprise produit des services ou des produits pour une autre entreprise en qualité de sous-traitant.</p>")
cell(34, 0, "<p>B - Partenariats dans lesquels l'entreprise recourt à un sous-traitant pour bénéficier de services ou de produits. Les autres partenariats commerciaux ne font pas l'objet d'un recensement obligatoire au seul titre du présent 8°.</p>")

cell(35, 0, '<p>9° Dans les entreprises appartenant à un groupe, transferts commerciaux et financiers entre les entités du groupe :</p>')
cell(36, 0, "<p>A - Transferts de capitaux figurant dans les comptes individuels des sociétés du groupe lorsqu'ils sont significatifs, notamment les transferts importants entre la société mère et ses filiales.</p>")
cell(37, 0, '<p>B - Cessions, fusions et acquisitions réalisées.</p>')
cell(39, 1, "<p>Organisation mise en place par l'entreprise pour prendre en compte les questions environnementales et, le cas échéant, démarches d'évaluation ou de certification environnementale.</p>")
cell(40, 1, "<p>a) Prévention et gestion des déchets : évaluation de la quantité de déchets dangereux définis à l'article R. 541-8 du code de l'environnement et faisant l'objet du bordereau prévu à l'article R. 541-45 du même code.</p>")
cell(41, 0, "<p>b) Utilisation durable des ressources : consommations d'eau et d'énergie.</p>")
cell(42, 1, '''<p>a) Identification des postes d'émissions directes de gaz à effet de serre provenant des sources fixes et mobiles nécessaires à l'activité de l'entreprise, dites « émissions du scope 1 ». Le volume de ces émissions est évalué lorsque l'entreprise dispose de cette information.</p>''')
cell(43, 0, "<p>b) Bilan des émissions de gaz à effet de serre prévu à l'article L. 229-25 du code de l'environnement ou bilan simplifié prévu à l'article 244 de la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021, pour les entreprises tenues d'établir ces bilans.</p>")
cell(44, 0, "<p>Note (1) : lorsque les données environnementales de cette rubrique sont établies à un autre niveau que celui de l'entreprise, notamment au niveau du groupe ou d'établissements distincts, elles sont accompagnées des informations complémentaires pertinentes permettant de les mettre en perspective au niveau de l'entreprise.</p>")

table_xml = ET.tostring(table, encoding='unicode')
add(10, '''<p>En l'absence de l'accord prévu à l'article L. 2312-21, dans les entreprises de moins de trois cents salariés, la base de données prévue à l'article L. 2312-18 comporte les informations suivantes :</p>\n''' + table_xml + '''
<p>Les informations et analyses figurant déjà dans des documents exacts, à jour et légalement accessibles aux membres du comité sont mises à disposition par un accès direct et identifiable dans la base, sans transcription ni rapport distinct. Les conditions d'accès, d'actualisation, d'analyse et de confidentialité prévues aux articles L. 2312-18, L. 2312-36 et R. 2312-10 à R. 2312-14 demeurent applicables. Cette faculté ne dispense pas de fournir les informations manquantes nécessaires à l'exercice des compétences du comité.</p>
<p>Les allègements de contenu et de présentation prévus par le présent article s'appliquent aux mises à disposition effectuées à compter de l'entrée en vigueur de la loi de simplification, y compris lorsqu'elles portent sur des années antérieures. Les documents déjà établis n'ont pas à être refaits. Les obligations de consultation, les garanties de santé et de sécurité, l'égalité professionnelle et les recours ne sont pas supprimés.</p>
<p>Les informations relatives aux aides, réductions d'impôt, exonérations ou réductions de cotisations, crédits d'impôt, droits à formation, congés et épargne salariale n'instituent aucune condition supplémentaire pour en bénéficier. Ces avantages restent ouverts aux situations futures éligibles, y compris dans le contrat unique pour les dispositifs de même objet ; les droits antérieurs sont conservés.</p>
''',
    "Réécriture intégrale de la grille, avec conservation des dix rubriques, de leurs lettres, des quarante-cinq lignes et des conditions maintenues. Réductions de fond : retrait de la reconstitution mensuelle des effectifs, de la justification particulière du temps partiel, de la liste action par action, du détail des objets, octrois/reports et résultats des congés de formation, du recensement général des partenariats sans sous-traitance et des retranscriptions de documents déjà accessibles. Les bilans agrégés, la sous-traitance, les motifs requis pour l'intérim, les informations sur aides et avantages, les analyses d'égalité et les protections essentielles demeurent. Les CDD deviennent une catégorie historique, sans fermer l'insertion, l'alternance ou leurs aides futures dans le contrat unique.",
    "Relecture complète du tableau source et des notes internes, dont les conditions de la note (1). Seuil strictement inférieur à 300 salariés, douze derniers mois pour les journées d'intérim, moins de 26 ans pour l'insertion/alternance et plus de 16 ans pour les stagiaires conservés. L2312-18, L2312-21, L2312-26, L2312-27, L2312-36 et R2312-10/11/13/14 lus : ni périodicité légale, ni deux années précédentes/année en cours/perspectives sur trois ans, ni droit de consultation ne sont supprimés. La série mois par mois était réglementaire ; sa suppression n'écarte pas une information ponctuelle nécessaire à une consultation. Le 8° est recentré sur la sous-traitance expressément prévue par L2312-36, sans fermer les demandes utiles sur des partenariats relevant d'autres consultations. Les congés de formation sont désormais documentés par type, nombre, durée totale et coût total ; le détail de l'objet, des conditions d'octroi/report et des résultats n'est plus un relevé systématique, sans empêcher une information nécessaire à une consultation prévue par la loi. Les publics, les résultats de l'alternance, le bilan CPF et les contrôles restent documentés. Incohérences préexistantes à coordonner expressément : anciennes désignations « plan de formation », « congé individuel de formation », articles L6361-1/L6323-13/L6362-4 et position « avant-dernier alinéa » de L6315-1 ; la source R2312-8 de 2024 n'intègre pas toutes les évolutions du L2312-26 fourni, notamment les reconversions. Elles ne sont pas déclarées déjà réparées. La rubrique 1° A f iii préserve les formations de sécurité de même objet pour les nouveaux contrats ; la coordination de L4154-2/L4154-4 et du chapitre intérim demeure nécessaire. Le 3° c informe sur les impôts effectivement applicables et n'instaure aucun IS annuel, CVAE ou prélèvement de remplacement ; le rapport L232-6 du code de commerce garde son champ propre et sa coordination hors code reste distincte. Aucun chiffrage d'aide évitée ni suppression de crédit fiscal n'est déduit du cadre de chiffrage de l'IS.",
    removed=[
        "Reconstitution réglementaire obligatoire mois par mois des effectifs, remplacée par leur évolution annuelle sans suppression des horizons légaux de la BDESE.",
        "Justification particulière du motif de recours au temps partiel dans le 1° A a, sans retrait des données d'horaires, d'effectifs ou des garanties contractuelles.",
        "Liste obligatoire distincte action par action des formations, bilans de compétences et VAE ; bilan agrégé avec effectifs par catégorie et sexe maintenu.",
        "Relevé systématique du détail des objets, conditions d'octroi ou de report et résultats des congés de formation et assimilés, avec maintien du nombre, de la durée totale et du coût total par type.",
        "Recensement général des partenariats commerciaux qui ne relèvent pas de la sous-traitance, sans suppression des informations légalement nécessaires aux consultations.",
        "Transcription et rapports distincts pour des informations ou analyses déjà accessibles dans des documents exacts et à jour au moyen de la base."
    ],
    benefit="Les rubriques 7° A à D conservent les aides publiques de tous les financeurs énumérés, les réductions d'impôt, les exonérations et réductions de cotisations et les crédits d'impôt : leur information au CSE ne devient ni une autorisation ni une condition de leur bénéfice, pour les entreprises futures éligibles également. Les rubriques 4° A c et 6° B maintiennent intéressement, participation, épargne salariale et actionnariat salarié ; la rubrique 5° conserve l'information sur la contribution aux activités sociales et culturelles, sans diminution de celle-ci. Les droits et aides à l'emploi des personnes handicapées, à l'insertion et à l'alternance des moins de 26 ans, les abondements, le CPF, les congés de formation et les protections des salariés vulnérables restent applicables selon leur objet, y compris dans le contrat unique pour les situations futures éligibles. Le remplacement des listes par des bilans agrégés ne supprime aucun congé ni financement. La disponibilité préalable du volume d'émissions demeure une limite favorable à l'obligation d'évaluation ; les bilans climatiques ne sont exigés que des entreprises déjà tenues de les établir. La faculté de conclure un accord de BDESE reste ouverte. Aucun avantage n'est limité aux seuls contrats antérieurs et aucune taxe correspondante n'est prétendue abolie par ce tableau.")

assert len(answers) == len(sources) == 11
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
