import copy
import hashlib
import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answer = copy.deepcopy(json.loads(Path('previous-answer.json').read_text()))
references = json.loads(Path('reference-targets.json').read_text())
by_number = {row['number']: row for row in answer}

assert len(sources) == len(answer) == 24
for source, row in zip(sources, answer):
    for field in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[field] == row[field], (source['number'], field)

# L2241-9 is now supplied in its complete current proposed version. Its
# removal of the separate salary report and general minimum delivery period
# must not be contradicted by the present lot.
row = by_number['L2241-3']
old = "D2241-1 maintient un rapport salarial quinze jours avant l'ouverture : ce délai de préparation n'est pas confondu avec le préavis individuel de rupture."
new = "Le D2241-1 officiel prévoit un rapport salarial remis au moins quinze jours avant l'ouverture. La proposition actuelle complète de L2241-9 retire le rapport distinct et le délai minimal général, tout en conservant les informations utiles et les dates librement convenues. D2241-1 doit être coordonné en ce sens ; le présent maintien de la loyauté ne rétablit ni ce support ni ce délai et ne concerne pas le préavis individuel de rupture."
assert old in row['review_notes']
row['review_notes'] = row['review_notes'].replace(old, new)
row['substantive_impact']['scope_limitations'] = row['substantive_impact']['scope_limitations'].replace(old, new)

row = by_number['L2241-8']
old_paragraph = "<p>Par dérogation au premier alinéa de l'article L. 2241-9, l'examen des données prévu par cet article a lieu à l'occasion de la négociation sur les salaires, sans examen annuel distinct imposé sur ce seul fondement. Toutes les catégories de données et les informations nécessaires prévues par cet article demeurent examinées et accessibles aux négociateurs.</p>"
new_paragraph = "<p>L'examen des données prévu à l'article L. 2241-9 a lieu à l'occasion de la négociation sur les salaires, sans examen annuel distinct imposé sur ce seul fondement. Toutes les catégories de données et les informations nécessaires prévues par cet article demeurent examinées et accessibles aux négociateurs. Aucun rapport distinct ni délai minimal général de remise de ces informations n'est requis pour cette négociation. Les dates de remise librement fixées par un accord organisant la négociation restent applicables ; les informations doivent permettre une négociation éclairée.</p>"
assert old_paragraph in row['proposed_xml']
row['proposed_xml'] = row['proposed_xml'].replace(old_paragraph, new_paragraph)
row['reason'] += " La rédaction est coordonnée avec la proposition actuelle complète de L2241-9 : elle ne rétablit ni rapport salarial distinct ni délai minimal général de remise ; cette coordination n'est pas comptée comme une seconde réduction propre à L2241-8."
row['review_notes'] = (
    "L2241-9 a été relu en entier dans reference-targets.json, source, notes et proposition actuelle : son premier alinéa proposé ne comporte plus d'annualité, et son avant-dernier alinéa retire le rapport distinct et le délai minimal général, avec réemploi des informations effectivement accessibles et maintien des dates librement convenues. La présente rédaction est alignée sur ces règles, sans compter une seconde suppression du rapport ou du délai. D2241-1 officiel impose encore un rapport et une remise quinze jours avant l'ouverture : le coordonner pour retirer ces deux contraintes, sans retirer l'information utile ni la loyauté de L2241-3 et sans confondre ce délai préparatoire avec le préavis individuel de rupture. L7113-4 a été lu : les salaires des journalistes professionnels permanents ou occasionnels restent inclus. Les articles L2241-11, L2241-17 et L2241-18 du lot cessent de rétablir l'annualité par leur formulation ; coordonner les intitulés de sous-sections. L'égalité de rémunération reste immédiatement opposable sans attendre quatre ans ; aucune conformité au droit supérieur n'est présumée. Le 1° proposé de L2241-9 ne vise les CDD que pour les contrats antérieurs ; les missions temporaires, y compris en CDI, ne constituent pas un terme de l'emploi. Aucun nouveau CDD ni renouvellement ne peut en résulter. Les cibles L1234-1, L1221-2 et L1234-9 ne fixent aucune périodicité de négociation salariale."
)
row['substantive_impact']['assessment'] += " Le rappel de la dispense de rapport distinct et de délai minimal général est une coordination de la proposition actuelle de L2241-9, non une réduction supplémentaire déduite de la seule source L2241-8."
row['substantive_impact']['scope_limitations'] = (
    "L'espacement diminue une fréquence de négociation, pas un taux fiscal, une cotisation ou un salaire. Il peut réduire la fréquence du dialogue en l'absence d'accord plus favorable ; aucun gain net de coût n'est chiffré. Les règles d'entreprise et les dispositifs sectoriels autonomes restent distincts. D2241-1 doit être coordonné avec L2241-9 pour ne plus imposer le rapport salarial distinct ni les quinze jours de remise ; ces suppressions ne sont pas comptées une seconde fois ici. Les dates de remise convenues, les informations nécessaires, le SMIC et le déclenchement de L2241-10 demeurent."
)
row['substantive_impact']['new_burdens_review'] = (
    "Aucune charge nouvelle n'est identifiée : aucun registre, donnée, dépôt ou condition d'aide supplémentaire n'est créé. L'information utile et les dates de remise librement convenues étaient déjà prévues ; leur maintien ne rétablit ni rapport distinct ni délai minimal général. L'espacement n'impose pas de négociation de remplacement. Le solde national de coûts n'est pas établi."
)

# The complete new target confirms the precise information route: II, 2°.
row = by_number['L2242-3']
old = "dans les conditions de l'article L. 2312-26"
new = "dans les conditions du 2° du II de l'article L. 2312-26"
assert old in row['proposed_xml']
row['proposed_xml'] = row['proposed_xml'].replace(old, new)
row['review_notes'] += (
    " La cible actuelle L2312-26 a été relue intégralement avec sa note d'entrée en vigueur au 1er janvier 2026 et sa proposition : le 2° du II maintient exactement l'accord d'égalité ou, à défaut, le plan de L2242-3 parmi les informations du CSE ; le renvoi proposé est précisé à cette subdivision. Sa consultation annuelle, la disponibilité effective, les délais et les recours ne sont pas supprimés par la dispense de dépôt administratif du plan. La suppression proposée au d du 5° et celle de la justification spécifique des recours envisagés au 9° concernent d'autres informations et ne dispensent pas du plan annuel. Le réemploi prévu dans la cible n'exige pas un document nouveau ni une seconde remise du plan. Les mentions de contrats aidés, d'apprentissage et de missions y préservent les futures situations éligibles dans le contrat unique, sans nouveau CDD."
)

# Explicit provenance for new references whose full official text was checked
# in the read-only public corpus, rather than in the supplied target bundle.
by_number['L2241-2']['review_notes'] += (
    " Renvois nouveaux absents des cibles de reference-targets.json : L1225-47 et L3123-3, dont les textes officiels entiers et les notes ont été lus dans travail.json du corpus public fourni. Le 2° de L1225-47 porte les seize heures, avec l'ancienneté minimale d'un an et le champ suivant le congé de maternité ou d'adoption ; ce n'est pas le seuil d'indemnité de rupture. L3123-3 porte les priorités de passage entre emplois et l'information sur les postes disponibles. Son renvoi officiel au premier alinéa de L3123-7 doit rester coordonné à la suppression du plancher général sans réduire les priorités. Aucun de ces deux articles hors lot n'est déclaré réécrit ici."
)
by_number['L2241-5']['review_notes'] += (
    " Le renvoi nouveau à L2222-4 n'est pas fourni parmi les cibles de reference-targets.json ; son texte officiel entier et ses notes ont été lus dans travail.json du corpus public. Il permet les deux durées, fixe cinq ans en cas de silence et prévoit la cessation des effets à l'expiration ; aucune survie indéfinie d'un accord ancien n'en est déduite."
)
by_number['L2242-3']['review_notes'] += (
    " Renvois nouveaux non fournis parmi les cibles de reference-targets.json : L1142-8, L1142-9, L1142-9-1, L1142-13, L2242-8 et L2242-9 ; leurs textes officiels et notes ont été lus en entier dans travail.json du corpus public. Les publications et corrections ont leurs propres seuils et déclencheurs ; L1142-9 et L1142-13 renvoient aux modalités de dépôt du plan, ce qui justifie le maintien exprès de leurs dépôts de décisions. L2242-8 comporte une formulation préexistante grammaticalement défectueuse au premier alinéa (absence d'accord « ou, à défaut d'accord, par un plan d'action ») : elle est signalée sans réécriture silencieuse ni extension de la pénalité dans le présent lot."
)

# Fresh, source-specific assessments against the current complete views.
assessments = {
    'L2241-2': {
        'L1234-1': "La cible officielle règle le préavis de licenciement, non le délai de prévenance d'un changement d'horaires visé par L2241-2. Sa proposition fixe quinze jours calendaires pour les contrats nouveaux sans condition d'ancienneté et conserve les anciennes durées et protections pour les contrats antérieurs. Aucun renvoi à cette cible n'est ajouté : le délai d'horaires reste négociable et n'est pas remplacé par le préavis de rupture. Le point de départ à la notification n'est pas défini par cette cible ; aucune règle de notification d'horaires n'en est déduite.",
        'L1221-2': "L2241-2 porte sur le temps partiel et non sur un cas de recours au CDD. Le second alinéa officiel de L1221-2 autorise encore certains termes ; la proposition actuelle de cette cible les exclut pour les contrats nouveaux, y compris en fin de mission ou de formation, et interdit les renouvellements contournant la bascule. Le volume garanti et les minima conventionnels du présent article restent compatibles avec cet emploi indéterminé ; les anciens contrats et les futures situations éligibles aux avantages restent à leur régime, sans autoriser de nouveau CDD.",
        'L1234-9': "La cible officielle ouvre l'indemnité de licenciement à huit mois, sauf faute grave ; sa proposition distingue les nouveaux contrats (un an atteint à la fin effective, préavis inclus sous réserve de l'essai, puis 0,20 mois par année totale et fractions en mois complets, six mois de plafond) et les composantes des anciens contrats. Elle ne fixe ni volume de travail ni rémunération des heures complémentaires. Aucun seuil indemnitaire n'est importé dans L2241-2 ; le minimum parental maintenu garde son ancienneté et son champ propres, sans nouvelle condition de notification ni limitation des salaires ou indemnités spéciales.",
    },
    'L2241-8': {
        'L1234-1': "Les quinze jours calendaires proposés dans L1234-1 concernent exclusivement le préavis individuel patronal des contrats nouveaux, indépendamment de l'ancienneté, avec paiement sans exécution si la faute grave rend le maintien impossible ; les anciens contrats conservent les durées et conditions antérieures. L2241-8 ne renvoie pas à ce dispositif. Ni la périodicité salariale de quatre ans ni le délai de remise des informations ne se calcule à partir d'une notification de rupture ; les procédures collectives et autorisations protectrices demeurent distinctes.",
        'L1221-2': "La source L2241-8 n'autorise aucune forme de contrat. La cible L1221-2 proposée supprime les nouveaux contrats à terme et leurs renouvellements après la bascule tout en préservant les anciens contrats. Le 1° actuel proposé de L2241-9, dont les données restent examinées ici, vise les CDD antérieurs et les missions temporaires, y compris dans un CDI : cet examen ne recrée donc aucun CDD. La fin d'une mission ne termine pas l'emploi ; salaires, aides et avantages futurs éligibles restent régis par leurs fondements propres.",
        'L2241-9': "Le premier alinéa officiel impose l'examen des données au moins annuel ; le premier alinéa proposé n'impose plus que l'examen lors de la négociation salariale. Le 1° proposé vise seulement les CDD antérieurs et les missions temporaires, y compris en CDI ; les 2° et 3° maintiennent prévention et salaires par catégorie et sexe. L'avant-dernier alinéa proposé retire le rapport distinct et le délai minimal général de remise, en conservant l'information utile, le réemploi et les dates convenues. L2241-8 est corrigé en conséquence : aucun maintien du rapport ou des quinze jours de D2241-1, dont la coordination demeure nécessaire. La transition de L2241-7 conserve échéances déjà dues, accords plus fréquents et droits antérieurs ; ce renvoi ne crée aucun droit de rupture ou nouveau CDD.",
        'L1234-9': "L1234-9 traite l'indemnité patronale ordinaire et non les salaires négociés par branche. Son texte proposé retient le seuil d'un an à la fin effective avec préavis inclus, sous la réserve de l'essai, puis 0,20 mois de salaire brut par année totale, fractions en mois complets, plafond de six mois ; il distingue anciens contrats, faute grave, indemnités plus favorables et réparations spéciales. L2241-8 n'en importe ni seuil ni plafond : l'espacement des négociations ne réduit pas les salaires dus, les minima, les congés ou l'égalité de rémunération, et ne change aucun fait de notification de rupture.",
    },
    'L2242-3': {
        'L1234-1': "L2242-3 maintient le plan annuel d'égalité et la programmation des corrections salariales ; il ne règle aucune rupture. Le préavis patronal de quinze jours de L1234-1 proposé ne dépend pas de l'ancienneté pour les contrats nouveaux, tandis que les anciens conservent les conditions et durées antérieures. Il n'abrège ni l'année du plan ni les délais de consultation du CSE ou de contrôle. Aucun renvoi à cette cible n'est créé et aucune notification individuelle de rupture ne remplace le dépôt volontaire ou la communication du plan lors d'un contrôle.",
        'L1221-2': "La proposition actuelle de L1221-2 impose un emploi indéterminé aux contrats nouveaux et exclut terme de mission, de formation et renouvellement contournant la réforme ; la source officielle permet encore des CDD. Le plan d'égalité de L2242-3 conserve son champ pour les salariés concernés, quelle que soit la durée d'une formation ou mission, et les avantages futurs ne sont pas réservés aux anciens contrats. La suppression du dépôt du plan n'est ni une dispense de plan ni une autorisation de nouveau CDD ; aucune règle de rupture individuelle n'est introduite ici.",
        'L1234-9': "La cible prévoit, pour les nouveaux contrats, le seuil d'un an à la fin effective avec préavis inclus sous réserve de l'essai, puis 0,20 mois de salaire brut par année totale et fractions en mois complets, plafond de six mois pour l'indemnité ordinaire patronale ; les anciennes composantes, indemnités plus favorables et réparations d'une illégalité restent distinctes. L2242-3 ne renvoie pas à ce calcul : son plan annuel et les corrections d'écarts s'appliquent sans attendre ce seuil. Une discrimination demeure réparable dès son fait générateur ; ni défaut de dépôt ni notification de rupture ne plafonne cette réparation.",
        'L2312-26': "Le renvoi nouveau est désormais contrôlé sur le texte officiel entier, sa note et la proposition actuelle, et précisé au 2° du II : ce numéro exige les indicateurs comparés ainsi que l'accord d'égalité ou, à défaut, le plan de L2242-3. Il ne subordonne pas l'accès du CSE à un dépôt administratif. Le I proposé conserve la consultation annuelle et le texte final conserve accès, délais, confidentialité et recours ; le réemploi dispense des remises répétées sans document supplémentaire. Les suppressions au d du 5° et au 9° visent le décompte des dérogations au plancher et certaines justifications prévisionnelles, pas le plan d'égalité. Les 1° et 9° coordonnent les anciens CDD, les missions et les futurs contrats uniques éligibles sans terme d'emploi. Aucun seuil d'ancienneté ou préavis de rupture n'est applicable à ce renvoi d'information du CSE.",
    },
}

for row in answer:
    source_key = row['code_id'] + '|' + row['source_id']
    required = references['requirements'][source_key]
    checks = []
    for target_key in required:
        target = references['targets'][target_key]
        assert hashlib.sha256(target['proposed_xml'].encode()).hexdigest() == target['view_sha256']
        assert hashlib.sha256(target['source_xml'].encode()).hexdigest() == target['source_xml_sha256']
        assert hashlib.sha256(target['source_notes_xml'].encode()).hexdigest() == target['source_notes_sha256']
        assessment = assessments[row['number']][target['number']]
        assert len(assessment) >= 80
        checks.append({'target_key': target_key, 'view_sha256': target['view_sha256'], 'assessment': assessment})
    # An explicit empty list prevents accidental inheritance of other sources'
    # targets, while keeping exactly the required list for each source.
    row['reference_checks'] = checks
    assert len(checks) == len(required)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(answer), 'reference_checks': sum(len(a['reference_checks']) for a in answer)}, ensure_ascii=False))
