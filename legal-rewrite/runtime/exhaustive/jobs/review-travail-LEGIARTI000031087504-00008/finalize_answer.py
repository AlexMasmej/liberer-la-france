import copy
import hashlib
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
sources = json.loads((ROOT / 'source.json').read_text())
reference_bytes = (ROOT / 'reference-targets.json').read_bytes()
references = json.loads(reference_bytes)
answers = copy.deepcopy(json.loads((ROOT / 'previous-answer.json').read_text()))
by_number = {a['number']: a for a in answers}

# Partir des articles complets ; les anciens contrôles ne sont pas repris.
for a in answers:
    a.pop('reference_checks', None)
    a['review_notes'] = a['review_notes'].split(' Nouvelle passe de contrôle :')[0]

a = by_number['L1255-2']
old = a['proposed_xml'].split('<p>1°', 1)[1].split('</p>', 1)[0]
new = (
    " Recrute un salarié temporaire sans lui fournir les clauses, mentions et informations exigibles en application des 1° et 3° de l'article L. 1251-16, ou en les lui fournissant de manière volontairement inexacte, ou sans lui transmettre l'écrit prévu à l'article L. 1251-17. "
    "Pour les missions convenues à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique dans le cadre d'un emploi à durée indéterminée, y compris antérieur à cette date, ces obligations portent sur la lettre de mission et les informations qui l'accompagnent. Leur contenu et leur communication sont appréciés selon le champ temporel et les dispenses de reproduction et de répétition prévus par ces articles. "
    "Pour les mises à disposition convenues à compter de l'entrée en vigueur de la loi portant ces dispenses, l'absence de justifications précises du motif, du nom et de la qualification de la personne remplacée ou à remplacer, ou d'une clause spéciale de variation du terme et de sa répétition dans un avenant n'est pas sanctionnée sur le fondement du présent 1°. Le motif du recours et les autres informations maintenues restent exigibles. Aucun nouveau contrat de travail n'est exigé pour chaque affectation ;"
)
a['proposed_xml'] = a['proposed_xml'].replace('<p>1°' + old + '</p>', '<p>1°' + new + '</p>', 1)
a['reason'] = (
    "Réduction de fond conservée : retrait du délit déclaratif du 5°, de la sanction des seuls retards d'écrit aux 1° et 4°, et de la prison en récidive pour leurs manquements documentaires. Les amendes, l'interdiction judiciaire et la prison pour les seuls 2°, 3° et 6° demeurent pour protéger salaire, radioprotection et garantie financière. "
    "Correction du renvoi à la cible actuelle L1251-16 : les mentions qu'elle retire et les informations déjà régulièrement communiquées ne sont pas réintroduites par la sanction. Le 1° suit aussi L1251-17 pour les nouvelles missions d'un CDI antérieur. Ces coordinations ne constituent ni une seconde suppression des formalités déjà retirées dans les cibles, ni la suppression de leurs délais civils."
)
a['review_notes'] = (
    "Les six emplacements et les alinéas de peines sont conservés : amendes de 3 750 et 7 500 euros, interdiction judiciaire de deux à dix ans ; six mois de prison en récidive seulement aux 2°, 3° et 6°. "
    "Le 1° vise seulement les éléments des 1° et 3° de L1251-16 réellement exigibles, non leur recopie systématique. La cible actuelle exclut, pour les nouvelles mises à disposition, les justifications précises du motif, le nom et la qualification du remplacé et la clause spéciale de variation du terme ; elle admet des informations séparées conservables et déjà communiquées. Le motif lui-même et les informations maintenues restent dus. Les dispenses bénéficient aussi aux nouvelles lettres de mission d'un CDI intérimaire antérieur. Les anciens contrats de mission et mises à disposition déjà convenues gardent leurs mentions et leur terme en cours ; la loi pénale plus douce s'applique aux réductions de sanction selon son champ, sans effacer les droits civils. "
    "L1251-17 et L1251-42 conservent deux jours ouvrables ; leur seul dépassement n'est plus incriminé ici, mais aucune suppression de ces délais n'est revendiquée. L1251-18 est visé à son premier alinéa seulement. Le 3° conserve les trois jours ouvrables, le calcul d'exposition et les quatre garanties du deuxième alinéa de L1251-26, incorporées spécifiquement pour la radioprotection, sans importer sa rupture ordinaire dans le CDI intérimaire exclu de ce régime par L1251-58-4. "
    "L1251-45, lu en entier dans le corpus, conserve les déclarations d'activité, de siège, d'agences et de cessation ; seul leur délit est retiré ici. L1251-49 protège les salaires, indemnités, cotisations et remboursements. Le deuxième alinéa actuel proposé de L1251-47 reste bien le renvoi indemnitaire : L1235-2 ou L1235-3, avec L1235-5 réservé au remboursement d'allocations. L1235-2 et L1235-5 ont été lus intégralement dans le corpus ; leur ancienne présentation dans L1251-47 ne crée aucune indemnité. La proposition locale du corpus conserve cette ancienne présentation, contrairement à la vue actuelle fournie : la présente coordination retient cette dernière sans modifier le corpus. "
    "Les directives 2008/104/CE et 2019/1152 restent des contraintes supérieures à coordonner quant aux recours et sanctions effectifs ; leurs textes entiers ne sont pas joints, aucune conformité n'est présumée. Aucun nouveau renvoi à une cible non fournie n'est introduit. Les préavis, seuils indemnitaires et protections collectives ne sont pas déclenchés par la seule fin de mission."
)
impact = a['substantive_impact']
impact['assessment'] += (
    " Le renvoi documentaire est désormais borné aux informations réellement maintenues dans la cible actuelle L1251-16, avec ses dispenses et le champ des CDI antérieurs ; ce suivi ne constitue pas une nouvelle réduction à additionner à celle de la cible."
)
impact['new_burdens_review'] = (
    "Aucune charge nouvelle n'est identifiée : ni document ni déclaration de remplacement, ni attestation de réemploi. Le renvoi pénal suit exclusivement les informations maintenues, sans rétablir les justifications du motif, les données du remplacé, la clause spéciale de variation ou les recopies supprimées dans la cible. Les garanties de radioprotection et les délais civils demeurent préexistants ; aucun solde national n'est chiffré."
)
for e in impact['effects']:
    if e['measure_id'] == 'contrat-unique-duree-indeterminee':
        e['after'] = "Nouvelles missions d'un emploi à durée indéterminée, y compris antérieur : lettre et informations exigibles, sans nouveau contrat ni recopie dispensée."
        e['affected_population'] = "Entrepreneurs et salariés intérimaires en emploi à durée indéterminée, nouveau ou antérieur, pour les missions nouvelles"
        e['conditions_and_transition'] = "Nouvelles missions à compter de la réforme ; anciens contrats de mission et mises à disposition déjà convenues conservent leurs garanties de forme, sous réserve de la loi pénale plus douce."
impact['effects'].append({
    'kind': 'coordination',
    'measure_id': 'interim-suppression-justifications-motif-variation',
    'description': "Le renvoi pénal ne rétablit pas les mentions que les cibles actuelles L1251-16 et L1251-43 retirent ; cette coordination n'est pas une seconde suppression documentaire.",
    'before': "Le 1° sanctionne l'absence des mentions des 1° et 3° de L1251-16, dont la reproduction des clauses de mise à disposition et leurs justifications de remplacement et de variation du terme.",
    'after': "Pour les mises à disposition nouvelles, absence des justifications précises, nom et qualification du remplacé, clause spéciale de variation et répétition dans un avenant non sanctionnée par le 1° ; motif et informations maintenues exigibles.",
    'unit': 'legal_duty',
    'affected_population': "Entreprises de travail temporaire et salariés concernés par les mises à disposition nouvelles",
    'conditions_and_transition': "Champ temporel de L1251-16 ; anciennes mises à disposition et contrats de mission gardent leurs mentions et droits civils, avec réserve pénale plus douce.",
    'replacement_or_new_burdens': "Aucun dossier ou justificatif substitué ; information maintenue et contrôle du motif préexistants. Pas de seconde réduction comptée pour le même renvoi.",
    'source_quote': "1° De recruter un salarié temporaire en ayant conclu un contrat ne comportant pas les mentions prévues aux 1° et 3° de l'article L. 1251-16 ou comportant ces mentions de manière volontairement inexacte ou sans lui avoir transmis dans le délai prévu à l'article L. 1251-17 un contrat de mission écrit ;",
    'proposed_quote': "Pour les mises à disposition convenues à compter de l'entrée en vigueur de la loi portant ces dispenses, l'absence de justifications précises du motif, du nom et de la qualification de la personne remplacée ou à remplacer, ou d'une clause spéciale de variation du terme et de sa répétition dans un avenant n'est pas sanctionnée sur le fondement du présent 1°.",
})

# L'essai commun ne représente pas un allègement uniforme.
a = by_number['L1254-21']
i = a['substantive_impact']
i['classification'] = 'mixed'
i['assessment'] += (
    " La coordination du plafond d'essai à trois mois n'est pas uniformément favorable : elle peut porter de deux à trois mois le plafond initial des ouvriers et employés, tout en réduisant celui des cadres de quatre à trois mois et en interdisant le renouvellement. Le solde net de ces effets et des coupes documentaires n'est pas établi."
)
i['scope_limitations'] += " Les plafonds initiaux et renouvelés ont été confrontés aux articles L1221-19 à L1221-23 du corpus ; les durées plus courtes applicables restent protégées."
i['new_burdens_review'] = (
    "Aucun registre, rapport, dépôt ou justificatif de remplacement n'est créé. Une contrainte potentiellement accrue pour les ouvriers et employés est identifiée : le plafond initial commun de trois mois peut dépasser leur ancien plafond légal de deux mois. Les durées plus courtes favorables et les anciens essais restent applicables ; le renouvellement est interdit pour les nouveaux contrats. Aucun solde global de coût ou de complexité n'est démontré."
)
i['effects'].append({
    'kind': 'coordination', 'measure_id': 'contrat-unique-essai-trois-mois',
    'description': "La mention d'essai suit le plafond commun et son non-renouvellement, avec effets différents selon la catégorie, sans compter une seconde réforme de l'essai.",
    'before': "Mention de la durée d'essai éventuellement prévue ; régime général du CDI : deux mois pour ouvriers et employés, trois pour maîtrise et techniciens, quatre pour cadres ; renouvellement possible selon ses conditions.",
    'after': "Nouveaux contrats : au plus trois mois sans renouvellement ni nouvel essai par prestation ; durées plus courtes et anciens essais préservés.",
    'unit': 'other', 'affected_population': "Salariés portés et entreprises de portage concluant de nouveaux contrats",
    'conditions_and_transition': "Nouveaux contrats à compter de la réforme ; anciens essais et garanties plus favorables restent applicables.",
    'replacement_or_new_burdens': "Allongement possible du plafond initial de deux à trois mois pour ouvriers et employés ; réduction pour cadres et retrait du renouvellement ; solde net non établi.",
    'source_quote': "5° La durée de la période d'essai éventuellement prévue ;",
    'proposed_quote': "Pour les contrats conclus à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, cette durée ne peut dépasser trois mois et l'essai n'est pas renouvelable.",
})
a['review_notes'] += (
    " Contrôle complémentaire dans le corpus : L1221-19 fixe actuellement les plafonds initiaux de deux, trois et quatre mois ; L1221-21 permet un renouvellement sous conditions, plafonné à quatre, six et huit mois au total. Les propositions L1221-19, L1221-21 et L1221-22 retiennent trois mois sans renouvellement et réservent les durées plus courtes et les anciens essais. L'effet potentiellement plus contraignant du plafond initial pour ouvriers et employés est recensé en mixed. L1221-25 et L1221-26, lus en entier, règlent les quinze jours pendant l'essai sans prolonger celui-ci ; ils ne sont pas de nouveaux renvois normatifs du présent article."
)

# Analyses nouvelles des trois cibles communes, chacune appliquée au référent.
common = {
 'L1234-1': "L1234-1 officiel prévoit, hors faute grave, un préavis selon la règle applicable avant six mois, un mois de six mois à moins de deux ans et deux mois ensuite, avec garanties plus favorables. La vue proposée impose quinze jours calendaires aux contrats nouveaux, même pour faute grave avec paiement si le travail est impossible, et réserve les anciens contrats et les procédures ou autorisations distinctes. ",
 'L1221-2': "L1221-2 officiel admet un terme dans les cas légaux ; la proposition impose l'emploi sans terme aux nouvelles embauches et ferme les renouvellements décidés après la réforme. Elle distingue les durées de mission, formation et chantier de la durée de l'emploi et conserve les contrats et droits antérieurs. ",
 'L1234-9': "L1234-9 officiel ouvre l'indemnité à huit mois hors faute grave. La proposition exige, pour le contrat nouveau rompu par l'employeur, un an au terme effectif préavis inclus, puis 0,20 mois de salaire brut par année totale, mois complets au prorata, plafond légal de six mois sans soustraire la première année. Faute grave, garanties plus favorables, indemnités spéciales et transition des anciens contrats gardent leur champ. ",
}
contexts = {
 'L1254-17': [
  "Le retrait du renouvellement du portage ne notifie aucune rupture : les quinze jours ne transforment pas une date de prestation en terme de l'emploi, et les renouvellements déjà convenus conservent leur exécution.",
  "La suppression de L1254-17 exécute cette règle : une simple faculté ancienne ne permet pas de décider un nouveau renouvellement à terme. Le report de prospection des anciens contrats reste une dérogation distincte, non un renouvellement ordinaire.",
  "Une poursuite convenue sans terme conserve toute l'ancienneté ; elle ne fait pas naître automatiquement une indemnité ordinaire ni une prime de fin de CDD. Les anciens droits et leurs faits générateurs restent distincts.",
 ],
 'L1254-21': [
  "Le II sans rémunération générale des intermissions de portage ne dispense pas du préavis payé lorsqu'une rupture de l'emploi est notifiée. L'allègement des mentions contractuelles ne transforme pas la fin d'une prestation en notification.",
  "Les mentions maintenues concernent l'emploi continu ; la durée de prestation ne le termine pas. Le 5° conserve l'essai expressément prévu, au plus trois mois sans renouvellement, sans nouvel essai à chaque prestation.",
  "Les frais professionnels, droits à congés et sommes dues au titre des prestations ne sont pas absorbés par le barème ordinaire. Le II ne dispense pas de l'indemnité lorsqu'une rupture patronale remplit réellement les conditions de la cible.",
 ],
 'L1255-1': [
  "L'interdiction judiciaire d'exercer n'efface pas le préavis du personnel permanent licencié : son régime dépend de la date du contrat et de la notification, sans dispense des procédures collectives et autorisations de salariés protégés.",
  "Le renvoi pénal est limité au premier alinéa de L1251-2, définition du secteur, pour ne pas étendre automatiquement le délit aux ajouts proposés sur l'emploi unique et l'intermission. Cette limitation n'autorise aucun nouveau CDD.",
  "Les indemnités ordinaires du personnel permanent licencié après interdiction restent distinctes des réparations de L1235-2 et L1235-3. Le seuil d'un an ne supprime pas ces réparations, ni les droits de l'ancien personnel.",
 ],
 'L1255-2': [
  "La fin d'affectation ou la proposition radiologique n'est pas une notification de rupture. Le renvoi au deuxième alinéa de L1251-47 conserve le préavis du personnel permanent licencié dans son régime temporel, même si une peine documentaire est retirée.",
  "L'écrit de chaque mission est une lettre, sans nouveau contrat ni nouvelle durée d'emploi. Le 1° respecte aussi les dispenses applicables aux CDI antérieurs ; le 3° propose des affectations de radioprotection, jamais de nouveaux CDD.",
  "La réduction pénale n'efface pas les créances de mission, l'intermission, la rémunération de radioprotection ou les dommages d'une illégalité. L'indemnité du personnel permanent visé via L1251-47 suit ses propres conditions d'ancienneté, distinctes de ces droits.",
 ],
 'L1255-4': [
  "Une affectation hors cas légaux ne permet pas de rompre automatiquement l'emploi. Le préavis nécessite la notification d'une rupture distincte ; la suppression de la prison ne dispense ni de cette notification ni des procédures spéciales.",
  "Le troisième alinéa maintient les cas de L1251-6 pour la seule affectation : même saisonnière, elle ne devient pas un CDD. Les anciens contrats de mission conservent leur champ historique, sans nouvelle embauche à terme.",
  "L'infraction de recours hors cas légaux n'est pas le fait générateur de l'indemnité ordinaire. Sa dépénalisation partielle ne ferme ni dommages civils ni garantie d'intermission, ni créances de terme des anciens contrats.",
 ],
 'L1255-6': [
  "L'abrogation du délit spécial du terme ne supprime pas le préavis dû à la rupture de l'emploi. Une date de fin de mission reste distincte de la notification qui fait courir ce préavis ; les procédures collectives gardent leur régime.",
  "Dépénaliser le terme de mission ne recrée ni CDD ni fin automatique de l'emploi. Les règles civiles de durée d'affectation de L1251-11 restent applicables dans leur champ et les anciens contrats conservent leurs droits.",
  "Le retrait du délit n'échange pas les créances civiles de terme des anciens contrats contre le barème ordinaire. Le zéro avant un an ne supprime ni ces créances ni la réparation des infractions ou illégalités distinctes.",
 ],
 'L1255-14': [
  "Le retrait des délits d'intitulé ou de transmission du contrat ne vaut pas dispense de préavis à la rupture du portage. Le régime sans rémunération générale des périodes sans prestation n'annule pas le préavis légal dû après notification.",
  "Le 2° suit L1254-7 et réserve le nouvel emploi sans terme ; les 4° et 6° limitent les règles de CDD au champ antérieur. Les reports favorables anciens ne permettent pas de décider un renouvellement ordinaire après réforme.",
  "Les sanctions documentaires et les créances civiles sont distinctes : supprimer une peine ne retire ni salaires, indemnité d'apport, congés ou droits de fin d'anciens CDD. L'indemnité ordinaire n'intervient qu'à la rupture patronale dans les conditions de la cible.",
 ],
 'L1262-2': [
  "Le renvoi d'accueil du détachement n'impose pas ce préavis privé français à tout contrat étranger par simple assimilation. La loi réellement applicable, les normes impératives et les règles spéciales de détachement doivent d'abord être déterminées.",
  "La règle française ne convertit pas automatiquement un CDD valablement régi par une loi étrangère, même conclu après réforme. Notre troisième et quatrième alinéas l'explicitent, sans autoriser un CDD relevant en réalité du droit français.",
  "Le barème ordinaire de rupture ne remplace pas les 10 % de fin de mission encore dus aux CDD étrangers éligibles. Le maintien explicite de l'ancienne rédaction de L1251-32 et L1251-33 protège ce bénéfice futur et ses exceptions propres.",
 ],
 'L1262-7': [
  "L'article maintenu exclut deux secteurs d'une dispense administrative de détachement ; il ne règle ni notification de rupture ni préavis. Aucun renvoi ne permet donc d'y appliquer quinze jours à un contrat étranger ou public sans examiner son droit propre.",
  "Le renvoi à L1251-2 identifie le secteur de l'intérim ; il ne convertit pas les contrats étrangers des entreprises exclues. Le maintien de la source n'autorise ni nouveau CDD français ni modification du régime autonome des agences de mannequins.",
  "L'exclusion d'une dispense documentaire ne fixe aucune indemnité de rupture et aucune ancienneté d'ouverture. Le barème nouveau ne peut être importé dans le détachement étranger ou l'agence de mannequins par cette seule définition sectorielle.",
 ],
 'L2143-2': [
  "Le retrait de l'ancienneté de désignation syndicale n'abroge pas les autorisations de licenciement du salarié protégé. Le préavis individuel n'est ni une autorisation ni une limite totale de procédure ; une notification régulière reste nécessaire.",
  "La dispense couvre les salariés temporaires en anciens contrats de mission, CDI intérimaires ou contrats uniques, avant la première affectation et pendant l'intermission. Elle ne fait pas de la durée du mandat ou de la mission un terme d'emploi.",
  "L'absence d'ancienneté pour être désigné n'abroge pas le seuil indemnitaire à la rupture. Elle n'efface pas non plus les réparations d'un licenciement illégal du salarié protégé, qui restent ouvertes dès le premier jour dans leur régime propre.",
 ],
 'L2241-9': [
  "Les calendriers de remise des informations salariales et la périodicité de négociation sont distincts du préavis de rupture. Supprimer le rapport séparé et son délai minimal ne dispense d'aucun préavis individuel ni notification.",
  "Les prévisions de CDD ne concernent que les contrats antérieurs ; les missions futures peuvent être limitées dans l'emploi sans terme. L'examen de données de branche ne constitue jamais une habilitation à créer ou renouveler un CDD.",
  "Les données de salaires moyens ne modifient ni salaire de référence de rupture ni ancienneté ni indemnités spéciales. L'allègement du support d'information n'enlève aucun droit indemnitaire ni conventionnel et ne vaut pas baisse de prélèvement.",
 ],
 'L2254-2': [
  "Le V conserve le régime spécifique après refus de l'accord. Les quinze jours se comptent dès le lendemain de la présentation, réception ou remise régulière selon L1234-3, et non dès l'information sur l'accord ou le refus ; les anciens contrats gardent leur préavis.",
  "Ni la durée de l'accord, ni une période d'aménagement, ni une formation ne fixe le terme du contrat unique. Le mois de refus et les deux mois pour engager le licenciement n'autorisent pas un CDD de remplacement ou une extinction automatique.",
  "L'alinéa d'application du V reprend le seuil au terme effectif, les mois complets et toute la première année, employeur seul. Il préserve l'ancienne condition de huit mois et les deux composantes, sans double compte, ainsi que le CPF spécial et les réparations d'illégalité.",
 ],
}

special = {
 'L1254-17': {
  'L1254-12': "Le texte officiel plafonne à dix-huit mois, renouvellements compris ; sa note vise les contrats en cours de la réforme de 2015. La proposition retire ce plafond pour le nouvel emploi et maintient les anciens contrats, renouvellements déjà convenus et report de prospection. Notre transition conserve exactement deux renouvellements et dix-huit mois, sous réserve du report de trois mois, sans limiter la durée de l'emploi unique.",
 },
 'L1255-1': {
  'L1251-2': "L'alinéa officiel unique définit l'activité exclusive, la mise à disposition temporaire, la qualification convenue, le recrutement et la rémunération. La proposition scinde cette définition dans son premier paragraphe et ajoute un second paragraphe sur le contrat unique et ses garanties. Le renvoi pénal est expressément borné au premier alinéa pour ne pas étendre le délit à ces ajouts ; il ne supprime pas leurs fondements civils.",
  'L1235-3': "La cible n'a aucune proposition substitutive : ses deux tableaux officiels demeurent la référence. Le premier couvre de zéro à trente ans et au-delà, plafond d'un mois à zéro an jusqu'à vingt mois dès vingt-neuf ans ; le second réduit certains minima pour moins de onze salariés, de 0,5 à 2,5 mois entre un et dix ans. La réintégration, le maintien des avantages et les cumuls restent dans leur champ. Notre correction de L1235-5 ne réduit aucune de ces réparations et le seuil ordinaire d'un an ne s'y substitue pas.",
 },
 'L1255-2': {
  'L1251-16': "Lecture de la vue actuelle entière : le 1° ne demande plus les justifications précises du motif, le nom et la qualification du remplacé, ni la clause spéciale de variation ou sa répétition ; il maintient motif et autres informations, avec remise séparée ou réemploi de l'écrit conservable accessible. Le 3° maintient la rémunération et l'indemnité de fin de mission seulement lorsqu'elle est due. Notre 1° vise ces deux subdivisions réellement exigibles, exclut expressément les mentions supprimées et les recopies dispensées, y compris pour nouvelles lettres de mission d'un CDI antérieur. Les anciens contrats et mises à disposition gardent leur champ historique ; aucun nouvel essai ou terme d'emploi n'en découle.",
  'L1251-17': "Le texte officiel exige la transmission sous deux jours ouvrables après mise à disposition. La proposition maintient ce délai et prévoit, pour les missions nouvelles d'un CDI même antérieur, la lettre de mission et les informations non encore communiquées ; aucun second envoi de l'écrit déjà transmis n'est dû. Notre 1° suit ce champ élargi aux CDI antérieurs et ne rétablit ni contrat nouveau ni double envoi ; le dernier alinéa retire seulement la sanction du retard, non l'obligation civile ou le délai.",
  'L1251-26': "Le deuxième alinéa officiel protège quatre éléments essentiels : qualification professionnelle, rémunération, horaire et temps de transport. La proposition conserve ces garanties ; pour un ancien contrat rompu, elle garde les trois jours ouvrables, la rémunération jusqu'au terme et, au-delà de quatre semaines, au plus trois affectations, sans nouveau CDD. Notre 3° incorpore seulement les quatre garanties pour la proposition radiologique, même lorsque L1251-58-4 exclut la rupture ordinaire de mission ; il n'applique ni son indemnité de terme ni son délai général au nouvel emploi par erreur.",
  'L1251-34': "La source déroge aux maxima de mission pour l'exposition dépassant la limite annuelle rapportée à la durée et prescrit une proposition dans trois jours ouvrables, avec les garanties du deuxième alinéa de L1251-26. La proposition raisonne en affectations, conserve les quatre garanties, le calcul sur la durée totale et les limites de radioprotection, et réserve les anciens contrats. Notre 3° sanctionne cette protection réelle, sans imposer nouveau CDD, durée minimale d'emploi ou fin automatique du contrat unique.",
  'L1251-47': "La vue actuelle retire le seul motif déclaratif de fermeture, maintient garantie financière, risque sérieux, mise en demeure et maximum de deux mois. Son deuxième alinéa reste celui des indemnités du personnel permanent, avec L1235-2 ou L1235-3 et L1235-5 limité au remboursement d'allocations. Le renvoi conservé porte exactement sur cet alinéa ; la proposition plus ancienne du corpus n'est pas substituée à cette vue. Les droits civils et anciens recours demeurent, indépendamment du retrait pénal des déclarations.",
 },
 'L1255-4': {
  'L1251-6': "Le premier alinéa vise une tâche précise et temporaire sous réserve de L1251-7 ; les cinq cas et les a à e du remplacement sont entiers dans les deux vues. La proposition définit directement le saisonnier au 3° et précise que les cas concernent l'affectation. Notre infraction conserve les deux branches, objet ou cas illicites, avec les mêmes amendes ; sa prison seule est retirée. Aucun remplacement ni saison ne justifie un nouveau CDD, et les anciens droits de mission restent distincts.",
 },
 'L1255-6': {
  'L1251-11': "La source impose un terme précis, avec cinq exceptions permettant un événement de fin et une durée minimale. La proposition conserve ces règles, remplace au 4° le renvoi CDD par les critères de mission saisonnière de L1251-6 et les applique à la lettre de mission du contrat nouveau, sans fin d'emploi. L'abrogation de L1255-6 retire seulement son incrimination : ni ces règles civiles, ni la garantie d'intermission, ni les droits de terme des anciens contrats, ni les sanctions autonomes de durée maximale ne sont supprimés.",
 },
 'L1255-14': {
  'L1254-15': "Les listes officielles sont complètes : 1° a à i pour l'emploi et 2° a à h pour la prestation. La proposition les abroge prospectivement et les réserve aux CDD déjà valablement conclus avec leurs droits, sans réédition. Notre 6° suit ce champ historique ; il ne transporte pas ces mentions, notamment terme ou renouvellement, dans le nouvel emploi. Les droits autonomes de salaire, congés, protection sociale et santé ne disparaissent pas avec cette liste spéciale.",
  'L1254-20': "La source exige l'écrit et l'intitulé du CDI de portage ; la proposition impose l'intitulé du contrat unique pour les recrutements nouveaux et conserve les contrats antérieurs sans formalité. Le 5° abrogé retire le délit de mention exacte, sans abroger l'écrit ni les informations civiles. La nouvelle mention n'est pas étendue aux anciens contrats et le 6° ne réintroduit pas le délit retiré du 5°.",
  'L1254-21': "La cible fournie fusionne les frais au 1°, retire les 3° et 7° et dispense de répéter les données sociales du 6° ; ses huit numéros et le II sans rémunération générale des intermissions sont conservés. Notre article L1254-21 maintient ces coupes et ajoute au 8° la dispense du garant déjà communiqué et exact. Le 6° pénal suit les mentions et dispenses réellement applicables, y compris cette correction dans le lot, sans recréer le descriptif ou les comptes rendus ; les anciens essais et clauses favorables restent réservés.",
  'L1254-7': "Le texte officiel autorise durée déterminée ou indéterminée ; la proposition impose le contrat unique pour les nouveaux recrutements et conserve les droits et ancienneté des contrats antérieurs. Le 2° coordonne cette restriction : le CDD auparavant permis devient sanctionnable pour les recrutements nouveaux. Cette portée plus contraignante est explicitement recensée en mixed, avec les mêmes 3 750 euros puis 7 500 euros et six mois en récidive, sans présenter l'ajout comme une seconde réduction.",
  'L1254-12': "Le plafond officiel est dix-huit mois au total, renouvellements compris ; la note historique d'application aux contrats en cours ne date pas la réforme future. La proposition retire le plafond pour les nouveaux emplois sans terme et le maintient pour les anciens CDD, renouvellements déjà convenus et report de prospection compris selon son régime. Le 4° n'incrimine que ce champ ancien ; ni la prestation commerciale ni ce plafond ne limite la durée du contrat unique.",
  'L1254-17': "La source permet deux renouvellements et exige clause ou avenant avant le terme initialement prévu. La vue fournie, conservée dans le lot, ferme tout renouvellement décidé après réforme même sur simple faculté ancienne, mais conserve ceux déjà convenus et le report de prospection de trois mois, distinct du renouvellement ordinaire. Le 4° suit exactement ce champ sans retirer le report favorable ni recréer un nouveau CDD ; les créances et ancienneté ne sont pas remises à zéro.",
 },
 'L1262-2': {
  'L1251-32': "La source garantit, sauf CDI immédiat chez l'utilisateur, 10 % de la rémunération totale brute en supplément, versés à chaque mission avec le dernier salaire et inscrits au bulletin. La proposition de la cible réserve ce régime aux anciens contrats français et ne paie pas une prime à la seule fin de mission du contrat unique. Notre quatrième alinéa conserve explicitement l'ancienne règle pour les CDD réellement régis par une loi étrangère, y compris futurs ; ni le seuil d'un an ni le barème de 0,20 mois ne remplace cet avantage.",
  'L1251-33': "Les exceptions officielles sont le saisonnier sous accord au 1°, le régime de L1251-57 au 2° et rupture par le salarié, faute grave ou force majeure au 4° ; le 3° est déjà abrogé. La proposition les réserve aux anciens contrats et précise qu'elles ne dispensent pas du préavis du contrat unique. Notre maintien de l'ancienne rédaction pour les futurs CDD étrangers préserve ensemble indemnité et exceptions ; l'exclusion des CDI dans le pays d'origine demeure, sans extension au nouveau CDD français interdit.",
 },
 'L1262-7': {
  'L1251-2': "La source définit l'entrepreneur par l'activité exclusive de mise à disposition, le recrutement et la rémunération selon qualification convenue ; la proposition conserve cette définition et ajoute le contrat unique et l'intermission. Le renvoi de L1262-7 demeure une identification du secteur exclu de la dispense, non une importation du régime français de rupture dans les contrats étrangers. Les agences de mannequins restent visées séparément par L7123-12, lu au corpus ; aucun élargissement de l'exclusion n'est créé.",
 },
 'L2254-2': {
  'L1232-2': "La source exige un entretien et cinq jours ouvrables avant celui-ci avec convocation par recommandé ou décharge. La proposition conserve l'entretien, ouvre les écrits datés et retire le minimum chiffré en imposant le temps effectif de défense et d'assistance, avec report nécessaire. Le V applique cette transition selon la date de convocation, y compris à une rupture d'ancien contrat ; les quinze jours de préavis ne commencent pas à la convocation et ne remplacent pas ces garanties.",
  'L1232-3': "La cible n'a pas de texte substitutif : l'employeur doit toujours, à l'entretien, exposer les motifs envisagés et recueillir les explications du salarié. Le renvoi du V reste applicable au licenciement après refus de l'accord. Le motif spécifique ne supprime ni cet échange réel ni le contrôle judiciaire ; le délai de quinze jours de préavis n'autorise pas une décision prise sans entretien effectif selon les règles applicables.",
  'L1232-4': "La source garantit l'assistance par un membre du personnel ou, faute d'institutions représentatives, par un conseiller inscrit ; la convocation indique alors les services tenant la liste. La proposition dispense seulement des adresses si la liste officielle à jour ou une référence effectivement accessible est fournie, avec accès gratuit de secours. Le V conserve ce droit, la transition selon convocation et le temps nécessaire de préparation, sans le remplacer par le mois de refus de l'accord.",
  'L1232-5': "L'habilitation officielle à un décret en Conseil d'État devient dans la proposition une habilitation bornée : pas de moyen exclusif de convocation, pas de minimum général chiffré avant entretien, pas de retour des adresses si la dispense s'applique. Le renvoi du V ne rétablit aucune de ces contraintes retirées, mais conserve les garanties d'assistance et de défense. Il ne transforme pas l'habilitation en autorisation de rupture ni en préavis supplémentaire.",
  'L1232-6': "La source impose recommandé motivé et deux jours ouvrables après entretien. La proposition ouvre les écrits à réception certaine, conserve motifs et examen des explications, retire les minima d'attente y compris disciplinaire tout en gardant son maximum d'un mois, et réserve autorisations et procédures spéciales. Le V suit la transition selon convocation ; le préavis court ensuite du lendemain de la présentation ou réception/remise régulière selon L1234-3. Aucun modèle facultatif ne devient obligatoire par le renvoi.",
  'L1234-2': "La source annule les clauses de préavis moins favorable au salarié. La proposition distingue les anciens contrats et répute non écrite, pour les nouveaux, toute durée unilatérale différente de quinze jours ; une dispense d'exécution ne modifie pas seule le terme ou les sommes dues. Notre alinéa d'application du V ne permet donc pas à l'accord de performance de réduire ce délai nouveau ni de rétablir les anciens préavis conventionnels dans son nouveau champ.",
  'L1234-3': "La source fait partir le préavis à la présentation du recommandé ; la proposition compte les quinze jours du contrat nouveau à partir du lendemain, jusqu'à la fin du quinzième jour même non travaillé. Réception ou remise ne se substitue à la présentation que pour un autre mode légalement autorisé. Notre formule reprend expressément ces conditions : ni date d'information de l'accord, ni refus, ni convocation ne déclenche ce délai ; le salarié notifie sa propre rupture par écrit reçu par l'employeur.",
  'L1234-4': "La source dit que l'inexécution du préavis n'avance pas la fin du contrat ; la proposition l'étend explicitement aux quinze jours et réserve la fin d'essai et les reports de protection ou de dispositif collectif. Le V et son alinéa d'application apprécient donc l'ancienneté au terme effectif préavis inclus, sans retrancher une période dispensée. Cette règle n'impose pas de prolonger un essai : son reliquat compensé conserve son régime distinct.",
  'L1234-5': "La source protège salaires, avantages et congés du préavis non exécuté et les cumuls. La proposition garantit la compensation des quinze jours patronaux, même pour faute grave, la distingue du seuil d'un an et du plafond de six mois de l'indemnité ordinaire, et ne paie pas automatiquement un travail refusé par le salarié. Dans le licenciement du V, le refus de l'accord ne vaut pas faute grave ; les sommes de préavis restent dues dans leur champ même avant un an.",
  'L1234-6': "La source calcule le préavis empêché par fermeture ou réduction d'horaire sur la durée légale ou conventionnelle du temps plein, ou sur la durée contractuelle du temps partiel. La proposition conserve les deux assiettes et les applique aux quinze jours sans baisse contractuelle de salaire. Le renvoi du V et le passage à quarante heures hebdomadaires ne permettent donc pas de diminuer cette compensation ni d'inventer une rémunération uniforme indépendante du contrat.",
  'L1234-7': "La cessation d'entreprise ne libère pas du préavis dans la source. La proposition précise respect ou paiement et quinze jours dans le nouveau champ, en réservant la véritable force majeure à L1234-12 et L1234-13. Notre renvoi conserve cette obligation : un accord de performance et son refus ne constituent pas une force majeure ; ni cessation ni arrêt de mission ne suffit à écarter la notification et la compensation requises.",
  'L1234-8': "La source maintient la continuité d'ancienneté pendant les suspensions mais en exclut la durée pour l'ouverture des anciens préavis gradués, sauf suspension des élus locaux. La proposition réserve intégralement ce champ ancien et n'exige plus aucune ancienneté pour les quinze jours nouveaux. Le V ne transpose donc pas l'ancien calcul d'ancienneté au préavis unique ; les suspensions ne le réduisent pas, sans effacer leurs régimes protecteurs autonomes.",
  'L1234-10': "La source maintient l'indemnité de licenciement malgré cessation d'entreprise, s'il y a lieu. La proposition renvoie expressément aux conditions d'ouverture, composantes et plafonds de L1234-9 et distingue force majeure et sinistre. Le V ne crée donc pas d'indemnité ordinaire avant le seuil applicable, mais ne retire aucune composante ancienne acquise ni salaire, congé ou réparation spéciale du seul fait d'une cessation.",
  'L1234-11': "La source ne rompt pas l'ancienneté lors des suspensions mais en exclut la durée, sauf suspension des élus locaux ; la proposition réserve aussi les assimilations d'autres dispositions. Elle mesure le seuil du contrat unique au terme effectif préavis inclus, retient toute l'ancienneté reconnue une fois l'an atteint et interdit le double compte ancien/nouveau. Notre alinéa applique ces règles : aucune année de franchise retranchée ni assimilation générale de toutes les suspensions n'est inventée.",
  'L1234-14': "La source étend certains articles aux agents et salariés de L5424-1 autres que fonctionnaires et militaires, ainsi qu'aux salariés sous statut légal d'entreprise publique, si leurs conditions sont réunies. La proposition respecte le champ et la transition propres de chaque cible sans convertir un contrat public. Notre régime de l'accord de performance privé ne prétend donc pas imposer le contrat unique ou son barème à tous ces agents par ce seul renvoi.",
  'L1234-18': "L'habilitation source couvre L1234-1 à L1234-14. La proposition précise calcul du préavis, compensation, référence salariale et deux composantes des anciens contrats, sans pouvoir changer un an, 0,20 mois ou six mois, ni réduire la part ancienne. Le renvoi du V respecte ces bornes et les mois complets de L1234-9 ; il n'autorise ni prorata journalier substitué ni nouvelle pièce de calcul obligatoire à fournir au salarié sur ce seul fondement.",
  'L2253-1': "La source et la proposition placent les salaires minima hiérarchiques au 1°, sans subdivision I. Le I de notre article corrige donc expressément le renvoi erroné au « 1° du I », sans changer les minima ni l'équivalence de garanties par matière. La proposition de la cible réserve au champ transitoire ses références aux anciens CDD, chantiers et renouvellements d'essai ; notre accord ne les rouvre pas et conserve les minima de rémunération du portage et autres garanties autonomes.",
  'L6323-11': "La source fixe l'alimentation annuelle, la moitié de durée, la majoration handicap, les accords favorables, le plafond d'au plus dix alimentations annuelles et les droits majorés saisonniers. La proposition conserve ces règles en définissant directement le saisonnier, y compris en contrat unique. Le VI maintient hors calcul annuel et plafond l'abondement spécial après refus de l'accord, encore ouvert aux futurs salariés éligibles ; le minimum réglementaire de 3 000 euros de R6323-3-2, lu au corpus, n'est ni absorbé ni supprimé par le barème ordinaire.",
 },
}

for a in answers:
    source_key = a['code_id'] + '|' + a['source_id']
    a['reference_checks'] = []
    for key in references['requirements'].get(source_key, []):
        target = references['targets'][key]
        number = target['number']
        if number in common:
            index = ['L1234-1', 'L1221-2', 'L1234-9'].index(number)
            assessment = common[number] + contexts[a['number']][index]
        else:
            assessment = special[a['number']][number]
        a['reference_checks'].append({
            'target_key': key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })

# Les notes rendent compte des lectures, sans certificat ancien ni validation juridique.
for a in answers:
    a['review_notes'] += (
        " Les contrôles de renvois ci-joints ont été rédigés à partir des textes officiels, notes et propositions entiers de la version actuelle de reference-targets.json ; les empreintes sont celles de ces vues. Une proposition cible n'est pas le droit en vigueur et ce contrôle n'est pas une validation juridique indépendante."
    )

def text_only(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml or ''))).strip()

def validate():
    assert len(answers) == len(sources) == 12
    assert len({(a['code_id'], a['source_id']) for a in answers}) == 12
    allowed_tags = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
    classifications = set('material_reduction coordination_only retained_necessary financing_transfer payment_timing_relief mixed reserved editorial_only'.split())
    kinds = set('tax_removed tax_reduced obligation_removed obligation_merged authorization_removed regime_merged deadline_reduced compliance_cost_reduced tax_increased obligation_added deadline_increased complexity_added financing_transfer payment_deferred relief_extended relief_preserved coordination'.split())
    units = set('percent euro legal_duty regime calendar_days working_days financing other'.split())
    from html.parser import HTMLParser
    class CheckMarkup(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed_tags, tag
            for k, v in attrs:
                assert k in ['rowspan', 'colspan'] and v.isdigit(), (tag, k, v)
        def handle_startendtag(self, tag, attrs):
            self.handle_starttag(tag, attrs)
        def handle_endtag(self, tag):
            assert tag in allowed_tags, tag
    for a, s in zip(answers, sources):
        for k in ('code_id', 'source_id', 'source_sha256', 'number'):
            assert a[k] == s[k], (s['number'], k)
        key = a['code_id'] + '|' + a['source_id']
        required = references['requirements'].get(key, [])
        assert [x['target_key'] for x in a['reference_checks']] == required
        for c in a['reference_checks']:
            assert c['view_sha256'] == references['targets'][c['target_key']]['view_sha256']
            assert len(c['assessment']) >= 80
        i = a['substantive_impact']
        assert i['version'] == 1 and i['classification'] in classifications
        for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(i[k]) >= 40
        if a['status'] == 'retained_unchanged':
            assert a['proposed_xml'] is None and i['classification'] == 'retained_necessary' and i['effects'] == []
        else:
            assert a['status'] == 'rewrite_draft' and a['proposed_xml']
            CheckMarkup().feed(a['proposed_xml'])
        if s.get('benefit_check_required'):
            assert len(a['benefit_review']) >= 100
        if a.get('change_type') == 'full_repeal':
            assert a['repeal_policy_id'] == 'editorial_direction_2026_10_19'
            assert len(a['repeal_scope']) >= 30
            assert text_only(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        if a.get('change_type') == 'normative_reduction':
            assert a['reform_policy_id'] == 'editorial_direction_2026_10_19'
            assert all(len(x) >= 30 for x in a['removed_provisions'])
        for e in i['effects']:
            assert e['kind'] in kinds and e['unit'] in units
            assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)+', e['measure_id']) and 6 <= len(e['measure_id']) <= 96
            for k in ('description', 'before', 'after', 'affected_population', 'conditions_and_transition', 'replacement_or_new_burdens'):
                assert e[k]
            assert len(e['source_quote']) >= 12 and e['source_quote'] in text_only(s['source_xml']), (a['number'], 'source', e['source_quote'])
            assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in text_only(a['proposed_xml']), (a['number'], 'proposed', e['proposed_quote'])
    assert (ROOT / 'reference-targets.json').read_bytes() == reference_bytes, 'Reference targets changed during drafting'

validate()
(ROOT / 'answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'verification.json').write_text(json.dumps({
    'article_count': len(answers),
    'rewrite_draft_count': sum(a['status'] == 'rewrite_draft' for a in answers),
    'retained_necessary_count': sum(a['status'] == 'retained_unchanged' for a in answers),
    'reference_check_count': sum(len(a['reference_checks']) for a in answers),
    'reference_targets_sha256': hashlib.sha256(reference_bytes).hexdigest(),
    'answer_sha256': hashlib.sha256((ROOT / 'answer.json').read_bytes()).hexdigest(),
    'legal_validation': False,
}, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answers), 'articles ;', sum(len(a['reference_checks']) for a in answers), 'renvois actuels contrôlés structurellement.')
