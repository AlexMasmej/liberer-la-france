import copy
import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
previous = json.loads(Path('previous-answer.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = copy.deepcopy(previous)
by_number = {a['number']: a for a in answers}

# These analyses are composed from the complete current target views. No old
# reference_checks object is carried into the new output.
contexts = {
    'L382-21-1': (
        "Le I de L382-21-1 indemnise l'incapacité d'exercer le ministère cultuel",
        "La qualité de ministre du culte et la durée d'un arrêt ne constituent pas une embauche privée",
        "Les IJ maladie et les prestations maternité, adoption et paternité des cultes ne sont pas des indemnités de rupture",
    ),
    'L382-25': (
        "L382-25 répartit le financement de l'assurance vieillesse des cultes",
        "Les cotisations forfaitaires et la répartition entre organismes cultuels ne définissent pas un contrat de travail",
        "Les bases forfaitaires et contributions vieillesse de L382-25 ne sont pas une indemnité patronale de licenciement",
    ),
    'L382-27': (
        "L382-27 ouvre la pension des cultes et protège les périodes antérieures à 1998",
        "L'application des règles de pension aux cultes ne transforme pas l'activité religieuse en emploi privé",
        "Les minima, majorations et réversions de L382-27 ne sont pas une indemnité ordinaire de rupture",
    ),
    'L382-29': (
        "L382-29 étend des règles de gestion, de recouvrement et de recours au régime des cultes",
        "Les conventions d'assistance au recouvrement et les périodes rachetables de L382-29 ne sont pas des embauches privées",
        "Une remise, un remboursement ou une prestation visés par L382-29 ne sont pas une indemnité ordinaire de rupture",
    ),
    'L382-29-1': (
        "L382-29-1 permet de prendre en compte des formations antérieures à l'affiliation cultuelle",
        "La formation religieuse précédant le statut d'affiliation n'est pas qualifiée de contrat de travail par L382-29-1",
        "Le rachat d'une période de formation de L382-29-1 ne rémunère pas une rupture à l'initiative d'un employeur",
    ),
    'L382-31': (
        "L382-31 règle l'affiliation des élus et l'assujettissement de leurs indemnités de fonction",
        "Le mandat électif et sa cessation ne sont pas des contrats de travail privés",
        "L'indemnité de fonction et l'option sociale de l'élu dans L382-31 ne sont pas une indemnité de licenciement",
    ),
    'L382-35': (
        "L382-35 protège l'accès aux soins et maintient certaines prestations pendant l'écrou",
        "La dispense d'avance, la pension liquidée, le capital-décès et les IJ maternité de L382-35 ne supposent pas un nouvel emploi privé",
        "Les prestations sanitaires, d'invalidité, de décès et de maternité de L382-35 ne sont pas une indemnité ordinaire de rupture",
    ),
    'L382-37': (
        "L382-37 applique des protections sanitaires aux personnes retenues en centre de sûreté",
        "La rétention de sûreté et sa durée ne sont pas un contrat privé d'emploi",
        "La couverture sanitaire étendue par L382-37 ne constitue pas une indemnité de rupture privée",
    ),
    'L382-39': (
        "L382-39 assujettit les rémunérations du contrat d'emploi pénitentiaire aux prélèvements sociaux spécifiés",
        "Le contrat d'emploi pénitentiaire relève de son régime propre, sans assimilation au contrat privé par L382-39",
        "La suppression sectorielle de CSA dans L382-39 ne crée aucun droit à une indemnité de licenciement privé",
    ),
    'L382-40': (
        "L382-40 détermine l'assiette des cotisations pénitentiaires et le minimum propre à la vieillesse de base",
        "Le renvoi à une assiette de revenus d'activité dans L382-40 ne qualifie pas le contrat pénitentiaire d'emploi privé",
        "La rémunération pénitentiaire et son plancher d'assiette vieillesse dans L382-40 ne sont pas des indemnités de rupture privées",
    ),
    'L382-41': (
        "L382-41 répartit les charges patronales du travail pénitentiaire entre donneurs d'ordre et Etat",
        "La désignation d'un donneur d'ordre dans L382-41 ne transforme pas le contrat pénitentiaire en contrat privé",
        "La prise en charge par l'Etat des cotisations patronales vieillesse de L382-41 n'est pas une indemnité ordinaire de licenciement",
    ),
    'L382-42': (
        "L382-42 garantit le calcul et la prise en charge des cotisations des personnes détenues en formation",
        "Le stage visé par L382-42 conserve une durée pédagogique distincte de tout emploi éventuellement associé",
        "Le financement social d'un stage dans L382-42 ne constitue pas une indemnité de rupture à l'initiative d'un employeur privé",
    ),
}


def labour_assessment(number, target_number):
    context = contexts[number]
    if target_number == 'L1234-1':
        return (
            context[0] + ". Le préavis de licenciement de L1234-1 ne régit pas cette règle sociale. "
            "Sa proposition de quinze jours calendaires sans ancienneté minimale concerne les contrats privés nouveaux ; "
            "la notification de rupture, les anciens contrats et les procédures collectives ou autorisations spéciales "
            "gardent leur champ. Aucun délai social ni droit à prestation n'est remplacé par ces quinze jours."
        )
    if target_number == 'L1221-2':
        return (
            context[1] + ". L1221-2 proposé impose la durée indéterminée aux nouvelles relations privées "
            "et interdit qu'une fin de mission ou de formation termine automatiquement l'emploi. "
            "Il ne modifie pas la population sociale ici visée. Les anciens contrats et leurs créances restent "
            "dans leur transition ; aucun nouveau CDD ni fermeture d'un avantage futur n'est déduit de ce renvoi."
        )
    if target_number == 'L1234-9':
        return (
            context[2] + ". La cible proposée réserve le barème ordinaire à la rupture patronale, hors faute grave : "
            "zéro avant un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, fractions au prorata "
            "des mois complets et plafond légal de six mois. Ce seuil et ce plafond ne conditionnent pas les droits "
            "sociaux ici visés ; anciens droits, indemnités spéciales et réparations restent distincts."
        )
    raise KeyError(target_number)


specific = {
    ('L382-21-1', 'L331-3'): "Le II de L382-21-1 vise l'indemnité de repos maternité. Le texte officiel de L331-3 conserve six semaines avant et dix après l'accouchement, au moins huit semaines de cessation, les périodes de douze ou vingt-quatre semaines avant et vingt-deux après en cas de naissances multiples, le déplacement possible de quatre semaines pour des jumeaux et la protection liée à la prématurité avec hospitalisation. Ce sont des conditions de prestation, sans ancienneté d'emploi ni notification de rupture ajoutée ; les futures naissances éligibles restent couvertes.",
    ('L382-21-1', 'L331-5'): "Le renvoi du II comprend le report après hospitalisation de l'enfant jusqu'à la fin de la sixième semaine suivant l'accouchement. L331-5 réserve d'abord la période supplémentaire de prématurité de L331-3 et permet aussi deux semaines supplémentaires sur prescription médicale. Le renvoi conservé ne retranche ni ce report ni cet avantage pour les futures situations ; ces délais ne sont ni une ancienneté d'emploi ni un préavis individuel.",
    ('L382-21-1', 'L323-7'): "Le dernier membre de la plage source imposait l'avis préalable du contrôle médical pour une nouvelle prescription rapprochée d'une suspension. La proposition entière de L323-7 l'abroge selon la date de prescription, sans annuler la suspension ancienne. Le corps de L382-21-1 distingue donc la plage active jusqu'à L323-6 et le seul champ transitoire de L323-7 ; aucun visa systématique ne renaît pour les prescriptions nouvelles, tandis que justification médicale, contrôles et recours demeurent.",
    ('L382-21-1', 'L331-6'): "Le II conserve le droit du père à l'indemnisation restant à courir après le décès maternel, avec cessation du travail, dispense expresse des conditions de L313-1, report dans le champ de L331-5 et droit subsidiaire du conjoint, partenaire ou concubin si le père ne le demande pas. Cette prestation n'est pas un prélèvement successoral. Aucun seuil d'ancienneté ni notification de licenciement n'est ajouté aux bénéficiaires futurs.",
    ('L382-21-1', 'L323-1'): "Le I renvoie à L323-1 pour les IJ maladie, leur carence et leur durée maximale. La cible distingue le calcul de date à date par affection relevant de L324-1 et le contingent pour les autres maladies ; elle prévoit des jours indemnisables ouvrables ou non. Retirer l'affiliation minimale ne retire ni ces limites ni la carence spéciale de trente jours documentée par D382-25-2. L'articulation de cette carence avec le renvoi législatif reste signalée, sans substitution du préavis privé.",
    ('L382-21-1', 'L313-1'): "Le dernier alinéa de la source de L313-1 exigeait une durée minimale d'affiliation au II ; sa proposition la supprime et ajoute un III transitoire. Conserver littéralement le renvoi ordinal de L382-21-1 serait donc incohérent. La proposition supprime expressément la condition spéciale cultuelle, y compris au début de l'indemnisation, pour les périodes nouvelles même si l'arrêt a commencé auparavant. Les autres conditions propres et avantages futurs demeurent ; le régime salarié n'est pas importé indistinctement.",
    ('L382-21-1', 'L331-8'): "Le II englobe la paternité et l'accueil de l'enfant : L331-8 fixe vingt-cinq jours au maximum, trente-deux pour naissances multiples, une cessation minimale de quatre jours et une dérogation pendant l'hospitalisation. Les non-cumuls et les règles distinctes selon poursuite ou interruption d'un mandat local demeurent dans leur champ. Ni les quinze jours de préavis ni le seuil d'un an de l'indemnité privée ne réduisent ces droits, ouverts aux futurs bénéficiaires éligibles.",
    ('L382-21-1', 'L331-7'): "Le II comprend l'adoption pour les parents adoptifs ou accueillants éligibles : seize semaines, vingt-deux pour adoptions multiples et dix-huit lorsque la charge atteint trois enfants, avec cessation d'activité, délai et fractionnement propres. L331-7 distingue aussi mandat local poursuivi ou interrompu. Le maintien du renvoi conserve ces droits futurs et leurs conditions sans les transformer en ancienneté, notification ou terme d'un contrat de travail.",
    ('L382-21-1', 'L162-4-1'): "La première phrase du I vise les règles de constatation par le médecin traitant. L162-4-1 source et proposé conservent motifs médicaux, durée, identification et authentification de la prescription, plafonds réglementaires au moins d'un mois initialement et de deux mois pour une prolongation, avec dépassement médicalement justifié. La dérogation favorable subsiste. Les mentions de transport du 2° ne deviennent pas une pièce supplémentaire d'arrêt, et aucune notification d'employeur ne remplace la prescription.",
    ('L382-21-1', 'L323-6'): "Le renvoi actif à L323-4-1 à L323-6 comprend les conditions de service des IJ, pas la rupture de l'emploi. La proposition entière de L323-6 abroge le 3° relatif aux heures de sortie, dispense d'autorisation préalable les activités non rémunérées compatibles et laisse à l'employeur seul l'information de reprise en cas de subrogation. Le renvoi maintient ces allègements selon leurs transitions, y compris pour un arrêt en cours, sans recréer une preuve équivalente. Prescriptions médicales, contrôles, adresse de contrôle, restitutions pour manquement volontaire, sanctions dans leur champ et faculté des élus demeurent ; aucune ancienneté privée d'un an n'est exigée.",
    ('L382-24', 'L351-1'): "La cible donne le cadre de liquidation vieillesse et de calcul selon âge et durée d'assurance ; L382-24 vise directement L351-1-5, lu séparément, pour l'âge abaissé d'inaptitude ou d'incapacité. La suppression du réexamen périodique ne change pas cet âge ni le passage à la vieillesse. Le dernier alinéa proposé de L351-1 limite le transfert de cotisations aux salariés d'employeurs privés sous conditions préalables : les assurés cultuels ne perdent pas des droits par ce seul renvoi.",
    ('L382-25', 'L222-2-1'): "Le 4° du I rattache la contribution de branche aux conditions de L222-2-1. La cible entière distingue allocations, périodes assimilées, volontariat, Mayotte, apprentissage au 7° et Saint-Pierre-et-Miquelon au 8°, avec bases forfaitaires des 2° et 5°. Sa proposition maintient les prises en charge des futures situations privées éligibles et distingue période pédagogique et durée d'emploi. Ce renvoi financier ne crée ni CDD ni indemnité de rupture, et ne transfère pas les cotisations des cultes à la capitalisation privée.",
    ('L382-27', 'L351-1'): "Le premier alinéa de L382-27 rend applicable le cadre de pension vieillesse de L351-1 : demande de liquidation, âge, durée d'assurance, salaire de base et garantie historique. La nouvelle fraction transférée de cotisations prévue dans la cible est réservée aux salariés du régime général employés par une personne privée, sous coordinations préalables. Le régime cultuel et les périodes antérieures à 1998 ne sont donc pas soumis automatiquement à une diminution de droits par répartition.",
    ('L382-27', 'L355-3'): "La plage L355-1 à L355-3 conserve la prescription de deux ans des indus vieillesse/invalidité hors fraude ou fausse déclaration, les protections de bonne foi liées aux ressources et l'examen amiable entre le plafond et son double. L355-3 conserve aussi l'accessoire de fraude de 10 %, l'option de remboursement et les garanties des retenues croisées. Son projet corrige seulement une expression de renvoi ; aucun de ces droits ou délais n'est remplacé par un préavis ou un plafond d'indemnité privée.",
    ('L382-27', 'L351-10'): "Le renvoi à L351-8 à L351-13 couvre le minimum contributif de L351-10, sa majoration selon les périodes cotisées et les périodes de solidarité éligibles, ainsi que les majorations qui s'y ajoutent. Le texte officiel prévoit sa revalorisation annuelle au 1er janvier au moins comme le SMIC. Le maintien intégral conserve ces avantages pour les liquidations futures, sans appliquer un seuil d'ancienneté privée, ni confondre le minimum avec le gel temporaire distinct de certaines pensions servies.",
    ('L382-27', 'L351-3'): "L382-27 ne vise que les 4°, 5° et 6° de cette cible : service national ou présence sous les drapeaux, situations de guerre postérieures au 1er septembre 1939 et détention provisoire non imputée sur la peine pour un assuré déjà affilié. Les 1°, 2°, 3° et 7° à 9° ne sont pas importés par ce renvoi, même si la cible entière les contient. Ces qualifications et justifications historiques sont conservées, sans ancienneté ou notification de contrat privé ajoutée.",
    ('L382-29', 'L231-12'): "La liste conserve L231-12 pour la gratuité du mandat d'administrateur, le remboursement des déplacements, le remboursement à l'employeur des salaires maintenus avec avantages et charges, et l'indemnisation possible de perte de gains des indépendants. Le projet cible conserve ces règles. Les allègements de publicité ou d'assistance de L382-29 ne retirent aucun de ces avantages présents ou futurs ; le temps de mandat n'est pas un préavis de rupture.",
    ('L382-29', 'L355-3'): "Le renvoi maintient les protections applicables aux indus vieillesse et invalidité des cultes : deux ans hors fraude/fausse déclaration, non-récupération de bonne foi sous plafond, examen amiable jusqu'au double et garanties de retenue sur d'autres prestations. La correction de renvoi rédactionnelle de la proposition de L355-3 n'en change pas la portée. Les abrogations coordonnées ici ne suppriment pas ces recours ni ne leur appliquent les quinze jours du contrat privé.",
    ('L382-29', 'L351-14-1'): "Le renvoi conserve le versement volontaire permettant de prendre en compte jusqu'à douze trimestres, sa neutralité actuarielle et les réductions des II à IV dans leurs champs. La proposition de L351-14-1 supprime la catégorie d'établissement définie par arrêté pour les demandes nouvelles et en cours, sans supprimer nature des études, diplôme ou scolarité assimilée et premier régime d'affiliation. La liste de L382-29 ne rétablit pas la condition retirée ni un CDD, et préserve les anciens versements.",
    ('L382-29', 'L243-5'): "La plage L243-4 à L243-6 conserve la remise des pénalités, majorations et frais dus à la date du jugement d'ouverture d'une sauvegarde, d'un redressement ou d'une liquidation. L243-5 exclut le passif issu du travail dissimulé visé à L8221-1, selon son entrée en vigueur documentée au 1er juillet 2026. L'avantage reste ouvert aux procédures futures éligibles ; aucun seuil d'ancienneté privée ou nouvelle notification ne conditionne la remise.",
    ('L382-29', 'L244-9'): "Le renvoi maintient la contrainte sociale et son opposition devant le tribunal compétent. La cible prévoit une exécution provisoire après deux jours calendaires pour les seuls redressements de travail illégal visés, avec demande d'arrêt au juge, et une prescription de trois ans pour l'exécution de la contrainte définitive. La note réserve l'application aux contraintes décernées à compter de la date réglementaire, au plus tard le 1er janvier 2027. Aucun délai de préavis privé n'est substitué à ces délais judiciaires.",
    ('L382-29-1', 'L351-14-1'): "L382-29-1 assimile expressément les formations précédant le statut cultuel aux périodes du 1° du I, et non aux quatre catégories indistinctement. La cible garde la limite globale de douze trimestres et les conditions du versement, avec réductions II à IV selon leurs critères. Son projet supprime la condition de catégorie d'établissement pour les demandes nouvelles ou en cours ; le renvoi ne la recrée pas. Le maintien ne réserve pas le droit aux formations déjà anciennes ni ne présume toutes les réductions applicables aux cultes.",
    ('L382-31', 'L3123-7'): "La cible fournie est L3123-7 du code du travail : son projet retire le minimum légal général du temps partiel et conserve minima conventionnels, dispenses et volume contractuel garanti. L382-31 vise explicitement L3123-7 du code général des collectivités territoriales, pour un élu ayant cessé son activité : c'est un homonyme d'un autre code. Aucune substitution n'est opérée et aucune concordance externe n'est affirmée sans ce texte ; les seuils sociaux des indemnités électives restent distincts des heures de travail privé.",
    ('L382-31', 'L241-3'): "Le premier alinéa de L382-31 ne vise que la valeur du plafond de sécurité sociale : la cible le fixe annuellement, le revalorise avec les salaires et interdit une baisse par rapport à l'année précédente. Les subdivisions nouvelles sur le compte investi ne sont pas importées par ce renvoi de valeur. Un mandat local n'est pas un emploi salarié privé ; fraction de seuil, exception des élus sans autre activité et option des indemnités non assujetties restent dans leur champ, sans nouveau transfert de cotisations.",
    ('L382-37', 'L382-35'): "Le texte entier de L382-35 comporte trois alinéas. Le premier garantit la dispense d'avance et la prise en charge des frais de santé ; le deuxième maintient pension d'invalidité liquidée et capital-décès ; le troisième maintient les IJ maternité. L382-37 exclut exactement les deuxième et troisième pour les personnes retenues et conserve le premier. L382-35 reste intégralement maintenu sans déplacement d'alinéas ; le renvoi demeure exact et les futures rétentions éligibles gardent la protection sanitaire.",
    ('L382-39', 'L241-3'): "L382-39 continue de viser les cotisations vieillesse plafonnées et déplafonnées de L241-3, indépendamment de la CSA supprimée. Le II proposé de la cible réserve le transfert aux salariés employés par une personne de droit privé, sous conditions de financement et de calcul préalable des droits. Le travail pénitentiaire et sa prise en charge patronale par l'Etat ne sont pas automatiquement inclus ; ni le renvoi réglementaire aux taux ni la suppression de CSA ne réduisent les droits vieillesse ou n'ajoutent une cotisation.",
    ('L382-39', 'L412-8'): "Le renvoi vise réellement le dernier alinéa de L412-8, qui détermine les obligations d'employeur et les bases spéciales de cotisations et d'indemnités lorsque la rémunération manque ou n'est pas normale. Le 5° inclut le travail sous contrat pénitentiaire avec son exception de séjour, tandis que le 2° c vise les stages. Ces champs ne sont ni effacés ni étendus par la suppression sectorielle de CSA. Le contrat pénitentiaire n'est pas attribué au contrat unique privé et aucune durée d'ancienneté de licenciement n'est ajoutée.",
    ('L382-40', 'L242-1'): "L382-40 utilise L242-1 pour déterminer la rémunération cotisable ; le I rattache les revenus aux périodes auxquelles ils sont attribués, et le II fixe les exclusions dans leurs champs. Le projet cible retire les assujettissements intégraux des indemnités dépassant cinq/dix PASS, tout en gardant la limite de deux PASS et sa transition. L382-40 ne rétablit pas ces assujettissements, n'invente pas une indemnité privée pénitentiaire et réserve son plancher aux seules cotisations vieillesse de base.",
    ('L382-41', 'L412-3'): "Le texte fourni est L412-3 du code de la sécurité sociale, relatif aux risques, mesures de prévention et recours entre entreprise de travail temporaire et entreprise utilisatrice. Le renvoi de L382-41 vise au contraire les 1° et 2° de L412-3 du code pénitentiaire, dont le texte entier n'est pas fourni. L'homonymie ne démontre aucune concordance : le renvoi source au code pénitentiaire est conservé, sans substitution de l'intérim ou du contrat privé et sans inventer une notification ou une condition d'ancienneté.",
}

for a in answers:
    source = next(s for s in sources if s['code_id'] == a['code_id'] and s['source_id'] == a['source_id'])
    for field in ['code_id', 'source_id', 'source_sha256', 'number']:
        a[field] = source[field]
    a.pop('reference_checks', None)
    source_key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in references['requirements'][source_key]:
        target = references['targets'][target_key]
        target_number = target['number']
        if target['code_id'] == 'LEGITEXT000006072050' and target_number in ['L1234-1', 'L1221-2', 'L1234-9']:
            assessment = labour_assessment(a['number'], target_number)
        else:
            assessment = specific[a['number'], target_number]
        checks.append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })
    if checks:
        a['reference_checks'] = checks

a = by_number['L382-21-1']
a['review_notes'] = (
    "Les textes officiels, notes et propositions des treize cibles requises ont été relus en entier dans reference-targets.json, "
    "notamment la cible L323-6 désormais fournie. Le renvoi actif jusqu'à L323-6 n'impose donc pas les anciennes heures de sortie "
    "ni l'autorisation de toute activité non rémunérée compatible, et ne rétablit pas la double information de reprise en cas de "
    "subrogation ; prescriptions, contrôles et adresse de contrôle demeurent selon les transitions propres à cette cible. "
    "Aucune réduction supplémentaire n'est comptée pour cette application du même dispositif. L313-1 proposé comporte un III : "
    "son dernier alinéa ne désigne plus la condition d'affiliation ; celle du régime des cultes est retirée expressément dans le I. "
    "L323-7 proposé supprime le visa pour les nouvelles prescriptions seulement, d'où sa réserve transitoire distincte. "
    "L323-4-1 et L323-5 ont aussi été lus intégralement dans le corpus : préparation de la reprise sans attente de trente jours "
    "dans la proposition, assistance choisie et limites de saisie restent dans leurs champs. L331-4 conserve huit semaines avant, "
    "dix-huit après et vingt-six semaines au total, avec sa faculté de déplacement de deux semaines. Les cibles L331-3/5/6/7/8 "
    "conservent les autres durées et exceptions. D382-25-1, D382-25-2, D382-25-3 et R382-104-1 lus en entier : "
    "préserver 1/30,42, 50 %, 79 % et les transitions du 15 octobre 2026 dans leur champ. La carence spéciale de trente jours "
    "de D382-25-2 n'est pas la durée d'affiliation supprimée ; son articulation avec le renvoi législatif à L323-1 reste à "
    "coordonner explicitement dans le règlement, sans réduction de carence implicite. La note du 1er juillet 2020 concerne le "
    "droit antérieur. Aucun nouveau renvoi normatif n'est ajouté par rapport au brouillon ; les propositions cibles ne sont pas "
    "présentées comme le droit en vigueur."
)

# Keep the normative bodies and other valid corrections of the previous draft.
# The missing target affects the documented reading of the existing range,
# without requiring a stylistic rewrite or a second reduction in the body.
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles': len(answers), 'reference_checks': sum(len(a.get('reference_checks', [])) for a in answers)}, ensure_ascii=False))
