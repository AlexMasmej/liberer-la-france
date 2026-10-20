import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text())


sources = read('source.json')
previous = read('previous-answer.json')
references = read('reference-targets.json')
targets = references['targets']
target_by_number = {v['number']: (k, v) for k, v in targets.items()}
input_hashes = {
    n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest()
    for n in ['source.json', 'previous-answer.json', 'reference-targets.json', 'policy.json', 'coordination.json']
}

# Analyses renouvelées après lecture des sources et des vues actuelles.
# Les empreintes ne proviennent jamais des contrôles de l'ancien brouillon.
checks = {
    'L1225-66': {
        'L1234-1': "La source de L1234-1 règle le préavis patronal, avec durées selon l'ancienneté ; sa proposition fixe quinze jours pour les nouveaux contrats. Le départ parental de L1225-66 est à l'initiative du salarié et demeure spécialement dispensé de préavis : supprimer sa prévenance ne lui applique ni les quinze jours patronaux ni une condition d'ancienneté.",
        'L1221-2': "La proposition de L1221-2 réserve les embauches nouvelles au contrat sans terme et interdit les renouvellements CDD décidés après l'entrée en vigueur. La faculté parentale demeure ouverte dans ce contrat et dans les contrats antérieurs pour leurs départs futurs. La naissance et la fin du congé ouvrent une faculté de départ ; elles ne constituent pas un terme automatique de l'emploi.",
        'L1234-9': "L1234-9 proposé subordonne l'indemnité ordinaire patronale à un an au terme effectif, préavis inclus, puis retient toute l'ancienneté à 0,20 mois par année, fractions en mois complets, plafond six mois. L1225-66 dispense le parent d'une indemnité à sa charge ; cette dispense n'est pas l'indemnité patronale et ne dépend d'aucun seuil d'un an. Le départ volontaire ne crée pas de droit ordinaire à celle-ci.",
    },
    'L1226-4': {
        'L1234-1': "La proposition de L1234-1 distingue les nouveaux contrats à quinze jours des anciens contrats conservant leurs durées et exceptions. L1226-4 maintient une règle spéciale de non-exécution pour inaptitude non professionnelle ; le nouveau délai reporte la fin effective sans supprimer les conditions médicales et de reclassement. Pour les anciens CDD, le renvoi de L1226-4-2 ne crée pas un préavis CDI.",
        'L1234-3': "Le deuxième alinéa proposé de L1234-3 décompte quinze jours calendaires à partir du lendemain de la présentation de la lettre, ou de la réception/remise lorsque la loi admet cette autre notification ; l'expiration survient à la fin du quinzième jour, même non travaillé. L1226-4 reprend exactement ce mécanisme pour les contrats nouveaux, sans autoriser une forme de notification autrement irrégulière ni déplacer la fin à notification des anciens contrats.",
        'L1234-5': "L1234-5 proposé compense en principe les quinze jours patronaux non exécutés et distingue cette compensation de l'indemnité ordinaire. L1226-4 maintient expressément sa dérogation spéciale de non-compensation en inaptitude non professionnelle. Cette dérogation n'efface ni la reprise du salaire après un mois dans ses conditions propres, ni l'indemnité spéciale de L1226-4-3 ; elle ne s'étend pas à l'inaptitude professionnelle de L1226-14.",
        'L1221-2': "Le champ nouveau sans terme de L1221-2 proposé explique les quinze jours propres au contrat unique. Les contrats déjà conclus restent distingués : le CDI ancien conserve la fin à notification prévue ici, tandis que l'ancien CDD reste soumis aux causes et modalités de rupture de son régime, via L1226-4-2 et L1226-4-3. Une mission ou une formation limitée ne dispense pas d'une rupture régulière du contrat unique.",
        'L1226-4-3': "La source entière de L1226-4-3 ne vise que la rupture du CDD pour inaptitude, avec minimum renvoyant à L1234-9 et versement selon L1243-8. Sa proposition conserve ce champ ancien et ajoute une garantie spéciale pour le contrat unique nouveau, au prorata sans condition d'un an. La réserve ajoutée à L1226-4 assure que son explication du seuil ordinaire ne neutralise pas cette extension proposée ; elle ne présente pas l'extension comme le droit officiel.",
        'L1234-9': "Le seuil ordinaire d'un an se mesure, dans la proposition de L1234-9, à la fin effective avec préavis, puis le calcul porte sur toute l'ancienneté, fractions en mois complets, sans franchise d'année retranchée. Les quinze jours nouveaux de L1226-4 comptent donc pour le seuil et le montant. Les anciens contrats gardent l'ouverture à huit mois et leurs composantes transitoires ; la garantie spéciale sans seuil de L1226-4-3 reste indépendante.",
    },
    'L1226-4-1': {
        'L1234-1': "Le renvoi aux indemnités effectivement dues n'institue aucun préavis de fonds : la proposition L1234-1 fixe les durées générales par génération de contrats, tandis que L1226-4 conserve la fin particulière pour inaptitude non professionnelle. Le paiement direct ou par garantie souscrite ne modifie ni notification, ni date d'ancienneté, ni procédure de reclassement.",
        'L1221-2': "La mutualisation organisée par la source de L1226-4-1 n'est pas conditionnée au CDD. Elle peut donc couvrir les indemnités des futurs contrats uniques dans les limites des garanties souscrites, sans nouvelle adhésion imposée. L1221-2 proposé n'est ni une garantie de paiement automatique ni une autorisation de fixer la durée de l'emploi par celle de l'assurance.",
        'L1234-9': "Les indemnités financées restent celles légalement dues selon leurs textes ; la source maintenue ne fige donc pas l'ancien barème. Le seuil ordinaire d'un an, les mois complets, le plafond et les composantes des anciens contrats de L1234-9 proposé s'appliquent dans leur champ. Une garantie ne soumet pas au seuil ordinaire l'indemnité spéciale de L1226-4-3 et ne rend pas automatiquement l'AGS débitrice de sommes non couvertes.",
    },
    'L1226-4-2': {
        'L1234-1': "La proposition de L1234-1 concerne le préavis de licenciement, avec quinze jours pour les nouveaux contrats. Elle ne fournit pas à l'employeur un mode de rupture libre d'un ancien CDD. Le renvoi transitoire à L1226-4 conserve notamment la reprise du salaire ; ses formulations de licenciement restent articulées aux règles spéciales de l'ancien contrat, sans préavis CDI artificiellement importé.",
        'L1221-2': "L1221-2 proposé interdit les nouvelles embauches à terme et les renouvellements décidés après la réforme, mais préserve les contrats antérieurs. La limitation de L1226-4-2 à ces contrats est donc nécessaire, y compris pour leurs inaptitudes futures. L'application directe aux contrats uniques ne fait ni de la durée d'aide ou de formation un terme, ni de la conversion une remise à zéro de l'ancienneté.",
        'L1226-4-3': "La proposition actuelle distingue la garantie des anciens CDD, versée selon les modalités de L1243-8, d'une garantie spéciale étendue au contrat unique sans seuil d'un an. L1226-4-2 vise leurs règles propres et ne transforme pas son application directe de L1226-4 en exclusion de cette garantie future. Le minimum spécial n'est pas ramené à zéro pour une ancienneté inférieure à un an.",
        'L1226-4': "La source de L1226-4 reprend le salaire après un mois et termine le contrat à notification ; sa proposition distingue cette ancienne fin de la fin au quinzième jour des nouveaux contrats. Le renvoi de L1226-4-2 continue pour les anciens CDD sous leurs règles propres, sans leur attribuer un préavis CDI. Dans le présent lot, la réserve expresse de L1226-4-3 ajoutée au texte final de L1226-4 complète la vue fournie, dont l'empreinte reste celle contrôlée ici.",
        'L1234-9': "Le renvoi au contrat unique n'assujettit pas toute indemnité d'inaptitude au seuil ordinaire d'un an de L1234-9 proposé. La garantie spéciale de L1226-4-3 reste sans ce seuil ; les anciens droits de calcul sont préservés. Une conversion convenue conserve toute l'ancienneté sans doubler une période ; le taux de 0,20 mois et le plafond ne remplacent que les composantes que les textes leur attribuent.",
    },
    'L1226-14': {
        'L1234-1': "L1234-1 proposé réduit à quinze jours le préavis des nouveaux contrats, indépendamment de l'ancienneté, et réserve les anciens régimes. L1226-14 conserve sa compensation spéciale, avec non-exécution pour inaptitude professionnelle. Cette durée de référence ne supprime ni la procédure préalable ni une autorisation protectrice ; les anciens contrats ne perdent pas leur durée de compensation par application rétroactive des quinze jours.",
        'L1234-3': "Pour les contrats nouveaux, le décompte correspond au deuxième alinéa proposé de L1234-3 : lendemain de présentation ou, si légalement admise, réception ou remise, puis fin du quinzième jour même non travaillé. La proposition de L1226-14 en fait aussi la fin effective et inclut ces quinze jours dans l'ancienneté spéciale. La forme valable de notification et le régime des anciens contrats restent distincts.",
        'L1234-5': "Le premier alinéa source de L1226-14 renvoie au montant de la compensation de L1234-5 ; la proposition maintient ce renvoi, avec le salaire spécial de L1226-16. Elle ne crée pas une seconde compensation pour la même période. La non-compensation de L1226-4 reste étrangère à ce cas professionnel, et ni le seuil ordinaire d'un an ni son plafond de six mois ne limitent la compensation de préavis.",
        'L1221-2': "Le régime nouveau de L1221-2 proposé est sans terme, ce qui permet l'application de la procédure d'inaptitude des articles L1226-10 à L1226-16 sans attendre une fin de mission. Les anciens CDD gardent leur régime spécial de L1226-20 et non un licenciement sous quinze jours. La transition de L1226-14 réserve ainsi les anciens contrats sans permettre un CDD professionnel nouveau.",
        'L1234-9': "Le renvoi à L1234-9 porte ici sur le montant servant de base, pas sur sa condition ordinaire d'un an ni sur l'exclusion ordinaire pour faute grave. L1226-14 conserve son exception propre de refus abusif prouvé. Pour la composante nouvelle, 0,20 mois par année totale, prorata des mois complets et plafond six mois sont doublés, soit au plus douze mois ; les composantes anciennes et conventions plus favorables demeurent sans double compte.",
    },
    'L1226-15': {
        'L1226-14': "La vue proposée de L1226-14 conserve compensation, indemnité spéciale double sans seuil et leurs exceptions propres. Le cumul de L1226-15 porte sur ces sommes, sans créer une seconde indemnité ordinaire. Le texte final de L1226-14 précise les mois complets par rapport à la vue fournie ; cette précision ne réduit ni les dommages d'une illégalité ni le minimum de réparation appelé par L1235-3-1.",
        'L1234-1': "Le préavis nouveau de quinze jours proposé dans L1234-1 ne dispense ni du retour à l'emploi ni du reclassement médicalement adapté. Sa notification ne rend pas licite une rupture qui les méconnaît. Les dommages de L1226-15 restent à leur régime, y compris avant un an, et ne sont pas ramenés à quinze jours ; les anciens contrats gardent leur préavis dans son champ.",
        'L1221-2': "Le contrat unique sans terme de L1221-2 proposé reçoit les protections de retour et de reclassement. Une formation ou une mission achevée ne peut tenir lieu de rupture régulière. L1226-15 conserve la transition de l'ordonnance du 22 septembre 2017 pour les licenciements de son champ, sans prendre cette date historique pour la date de la future réforme et sans supprimer les recours anciens.",
        'L1234-9': "La proposition de L1234-9 sépare expressément l'indemnité ordinaire des réparations d'une illégalité et indemnités spéciales. Le seuil d'un an au terme effectif et le plafond de six mois de l'indemnité ordinaire n'entrent donc pas dans le calcul des dommages de L1226-15. Leurs cumuls propres et les droits correspondant aux services antérieurs restent protégés, sans double paiement d'une même créance.",
        'L1235-3-1': "La vue actuelle est official_source_only : aucun proposed_xml n'est fourni et aucune ancienne proposition ne lui est attribuée. Le premier alinéa officiel écarte le barème L1235-3 dans les nullités qu'il vise et garantit au moins les salaires des six derniers mois lorsque le salarié ne demande pas la poursuite ou que la réintégration est impossible. Les six catégories du deuxième alinéa concernent liberté fondamentale, harcèlement, discrimination, action en égalité professionnelle ou dénonciation de crimes et délits, mandat protégé et protections de maternité ou d'accident professionnel. Le dernier alinéa réserve les salaires dus sur les fondements indiqués et, s'il y a lieu, l'indemnité de licenciement. L1226-15 renvoie au montant de cette cible pour son propre cas de refus de réintégration par l'une ou l'autre partie ; il n'importe pas une condition d'ancienneté d'un an, ne transforme pas ce minimum de six mois en plafond et ne confond pas ce cas avec la seule irrégularité procédurale de L1235-2. La note de 2017 garde son champ historique.",
    },
    'L1226-18': {
        'L1234-1': "Le préavis de quinze jours de L1234-1 proposé règle la durée individuelle des nouveaux contrats, pas les motifs de rupture pendant un arrêt professionnel. Il ne permet donc ni de rompre un ancien CDD suspendu hors faute grave ou force majeure, ni d'écarter les protections de santé du nouveau contrat. Une autorisation ou une procédure spéciale éventuellement requise conserve son propre calendrier.",
        'L1221-2': "La proposition actuelle de L1221-2 supprime les embauches nouvelles à terme sans priver les contrats déjà conclus de leurs protections. L1226-18 réserve précisément à ces anciens CDD la faute grave ou la force majeure pendant la suspension, y compris future. Les contrats uniques nouveaux relèvent de L1226-9 et L1226-13 ; la durée d'une mission ne recrée pas de CDD spécial.",
        'L1234-9': "Le seuil d'un an et le plafond de six mois de l'indemnité ordinaire de L1234-9 proposé ne constituent pas des conditions de la protection pendant la suspension. La rupture contraire peut être nulle dès les faibles anciennetés, avec recours et réparations propres. La transition des anciens CDD n'est pas remplacée par le barème ordinaire du contrat unique.",
    },
    'L1226-19': {
        'L1234-1': "L'échéance d'un CDD antérieur, que sa suspension ne reporte pas d'elle-même, n'est pas un licenciement soumis au préavis de L1234-1 proposé. Les quinze jours ne purgent pas non plus un refus injustifié d'une clause antérieure de renouvellement pendant l'arrêt. Ce refus conserve le contrôle de son motif et son indemnité minimale de salaires et avantages, sans condition ordinaire d'un an.",
        'L1221-2': "La proposition de L1221-2 interdit un nouveau renouvellement décidé après l'entrée en vigueur même si une clause l'envisageait auparavant. L1226-19 préserve les périodes déjà valablement convenues et les droits réparateurs attachés aux clauses anciennes. Une poursuite convenue après la réforme est sans terme avec ancienneté conservée ; elle ne rétablit pas le CDD par une clause de renouvellement.",
        'L1234-9': "L'indemnité de L1226-19 répare le refus injustifié et possède un plancher égal aux salaires et avantages jusqu'au terme de renouvellement prévu, et non le taux de L1234-9. Ni son seuil d'un an ni son plafond de six mois ne lui sont applicables. Les conditions d'ouverture de la réparation restent à apprécier sur la clause et les faits, et une poursuite sans terme n'efface pas l'ancienneté.",
    },
    'L1226-21': {
        'L1234-1': "La proposition de L1234-1 ne régularise pas, par quinze jours de préavis, la méconnaissance du retour ou du reclassement dans un ancien CDD. L1226-21 garde le préjudice et le plancher jusqu'au terme en cours. Les nouveaux contrats uniques relèvent des protections générales de santé ; leurs délais individuels ne remplacent ni les motifs licites ni les procédures préalables.",
        'L1221-2': "La distinction temporelle de L1221-2 proposé laisse survivre les recours des anciens CDD même si la rupture ou l'action vient après la réforme. L1226-21 ne maintient donc pas une possibilité de nouvelle embauche ou de renouvellement à terme. Pour le contrat unique futur, la fin d'une mission ne remplace pas le licenciement et ses réparations dans leurs champs propres.",
        'L1226-20': "Le deuxième alinéa officiel de L1226-20 définit les cas de rupture pour inaptitude professionnelle du CDD ; sa proposition les place après un alinéa introductif et un alinéa d'exclusions. L1226-21 rectifie donc le renvoi en identifiant les dispositions qui déterminent les cas autorisant la rupture. Il ne vise pas à tort l'exclusion des règles CDI et ne soumet pas les dommages ou le minimum spécial au seuil ordinaire d'un an.",
        'L1226-15': "La proposition actuelle de L1226-15 maintient le retour, le reclassement, le montant de réparation renvoyant à L1235-3-1 et le cumul avec L1226-14, ainsi que la transition historique de 2017. Le renvoi de L1226-21 aux nouveaux contrats s'exerce dans ce seul champ. Le plancher des anciens CDD jusqu'au terme en cours ne devient ni le barème du contrat unique ni une réparation plafonnée à six mois.",
        'L1234-9': "Le montant fondé sur le préjudice et sur les salaires et avantages du terme en cours n'est pas l'indemnité ordinaire de L1234-9 proposé. La réserve expresse finale écarte donc le seuil d'un an et le plafond de six mois pour cette réparation. La prise en compte du préavis au seuil ordinaire ne devient pas une condition préalable au recours de l'ancien CDD inapte ou apte.",
    },
    'L1226-22': {
        'L1226-14': "La proposition de L1226-14 organise compensation et doublement spécial sans seuil pour les contrats de son champ ; le texte final du lot précise les mois complets. Les nouveaux contrats passent par la garantie de paiement de L1226-17, tandis que les anciens CDD relèvent de L1226-20 et L1226-22. Ce partage n'autorise ni deux versements d'une même créance ni l'application du seuil ordinaire d'un an au minimum spécial.",
        'L1234-1': "Le préavis individuel de quinze jours de L1234-1 proposé est distinct des délais de présentation des relevés et d'avance des fonds en procédure judiciaire. L1226-22 ne supprime aucun jugement d'ouverture ni contrôle des créances par son articulation des contrats anciens et nouveaux. Il ne promet pas la réalisation d'une procédure collective dans les quinze jours suivant une notification de rupture.",
        'L1221-2': "L1221-2 proposé réserve la durée déterminée aux contrats antérieurs. Leur garantie de paiement ne doit donc pas être fermée par la date ultérieure de naissance de la créance ou d'ouverture de la procédure. L1226-22 explicite cette continuité sans permettre de nouveau CDD ; les contrats uniques futurs bénéficient des dispositions de garantie correspondant à leurs indemnités propres.",
        'L1226-21': "Le texte proposé de L1226-21 maintient pour les anciens CDD le préjudice et le minimum jusqu'au terme en cours, y compris pour les ruptures postérieures à la réforme. Le paiement reste garanti selon les conditions des articles L3253 cités par la source de L1226-22 ; il ne devient pas automatique ou illimité. Le renvoi aux contrats nouveaux passe par L1226-15 et L1226-17 sans double règlement.",
        'L1226-20': "La proposition actuelle de L1226-20 garde les cas de rupture et l'indemnité spéciale double des anciens CDD, puis rattache les nouveaux contrats à L1226-10 à L1226-16. L1226-22 maintient la garantie de paiement du premier groupe et articule celle du second par L1226-17. Il n'importe ni terme d'emploi dans le contrat unique, ni seuil ordinaire d'un an dans le minimum spécial.",
        'L1226-15': "Les réparations des nouveaux contrats visées par L1226-15 proposé restent dans leur champ de santé et de retour/reclassement, avec cumul et minimum propres. L1226-22 rappelle leur couverture via L1226-17, sous les limites et contrôles de la garantie salariale. Le renvoi ne crée ni paiement de toute demande avant vérification ni plafonnement des dommages par les six mois de l'indemnité ordinaire.",
        'L1234-9': "La proposition de L1234-9 distingue l'indemnité ordinaire, ses composantes temporelles et les créances spéciales ou réparatrices. L1226-22 règle le paiement de ces dernières selon leurs textes propres et non un calcul uniforme par le fonds. Le seuil ordinaire d'un an au terme effectif n'éteint donc ni le minimum spécial des anciens CDD ni les dommages couverts, même si leur créance naît après la réforme.",
    },
    'L1231-2': {
        'L1234-1': "La proposition L1234-1 fixe quinze jours pour les nouveaux contrats et conserve les durées des contrats antérieurs. La réserve de L1231-2 maintient les protections spéciales et les autorisations ou procédures collectives distinctes sans rétablir pour les nouveaux contrats les anciens préavis ordinaires. Les dispenses favorables au salarié restent ouvertes dans leurs conditions et aucun calendrier collectif n'est réduit implicitement.",
        'L1221-2': "Le contrat unique de L1221-2 proposé est sans terme pour les nouvelles relations relevant du code ; une formation ou mission peut avoir une durée sans terminer l'emploi. L1231-2 conserve les protections de santé, maternité et représentation pour leurs bénéficiaires futurs aussi. Il ne transforme pas ce contrat privé en instrument de réforme des agents publics et réserve les droits des contrats antérieurs.",
        'L1234-9': "La source de L1234-9 ouvre l'indemnité à huit mois sauf faute grave ; sa proposition passe à un an au terme effectif pour les nouveaux contrats, puis calcule toute l'ancienneté à 0,20 mois, avec mois complets et plafond six mois. L1231-2 empêche que ces paramètres limitent salaires, congés, réparations ou indemnités spéciales et conserve la transition des services anciens. Il ne crée pas d'indemnité ordinaire pour une démission.",
    },
    'L1231-3': {
        'L1234-1': "La règle de champ source demeure applicable à chacune des relations avec plusieurs employeurs. La proposition L1234-1 conduit donc à quinze jours pour un contrat unique nouveau et à l'ancien régime pour un autre contrat antérieur. Aucun préavis collectif commun à tous les employeurs ni justification supplémentaire de multi-emploi ne découle du maintien de L1231-3.",
        'L1221-2': "La nouvelle relation de travail relevant de L1221-2 proposé est sans terme même lorsque le salarié a un autre employeur. La règle source conservée ne convertit pas ses contrats antérieurs ni les régimes publics et ne permet pas un nouveau CDD pour un second emploi. La fin d'une mission chez un employeur n'emporte pas automatiquement celle des autres contrats.",
        'L1234-9': "Le seuil d'un an de L1234-9 proposé est mesuré chez l'employeur concerné à la fin effective du contrat, préavis inclus ; L1231-3 n'additionne pas les anciennetés de relations distinctes. Chaque contrat garde ses composantes et droits temporels. Les indemnités spéciales sans seuil restent distinctes, et une solidarité ou un coemploi sur un autre fondement n'est ni créé ni supprimé par cette règle de champ.",
    },
}

assert len(sources) == len(previous) == 12
answer = []
for source, old in zip(sources, previous):
    for key in ['code_id', 'source_id', 'number', 'source_sha256']:
        assert source[key] == old[key], (source['number'], key)
    item = dict(old)
    item['reference_checks'] = []
    source_key = source['code_id'] + '|' + source['source_id']
    required = references['requirements'][source_key]
    expected_numbers = {targets[k]['number'] for k in required}
    assert set(checks[source['number']]) == expected_numbers
    for target_key in required:
        target = targets[target_key]
        text = target['proposed_xml'] if target['view_kind'] == 'proposal' else target['source_xml']
        assert hashlib.sha256(text.encode()).hexdigest() == target['view_sha256']
        assessment = checks[source['number']][target['number']]
        assert len(assessment) >= 80
        item['reference_checks'].append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })
    answer.append(item)

by_number = {a['number']: a for a in answer}

a = by_number['L1226-4']
a['reason'] = a['reason'].replace(
    "La présente passe ajoute la réserve expresse de l'indemnité spéciale de L. 1226-4-3 proposée, pour éviter que le seuil ordinaire d'un an la ferme.",
    "La réserve expresse de l'indemnité spéciale de L. 1226-4-3 proposée est conservée, afin que le seuil ordinaire d'un an ne la ferme pas.",
)
a['substantive_impact']['new_burdens_review'] += " La garantie spéciale que la proposition cible de L1226-4-3 étend aux contrats uniques est expressément réservée : elle peut accroître la charge indemnitaire pour les futurs salariés qui auraient relevé d'un CDI sans indemnité à faible ancienneté. Il s'agit d'une coordination de l'extension portée par cette cible, non d'une seconde indemnité créée ici ; son coût et son solde avec le barème ordinaire ne sont pas établis."

a = by_number['L1226-14']
a['reason'] = a['reason'].replace(
    "La présente passe précise que les fractions d'année sont calculées en mois complets, conformément à la décision actuelle ;",
    "Le texte final conserve la précision du calcul des fractions d'année en mois complets, conformément à la décision actuelle ;",
)
for effect in a['substantive_impact']['effects']:
    if effect['measure_id'] == 'inaptitude-professionnelle-maintien-quinze-jours':
        effect['measure_id'] = 'contrat-unique-preavis-quinze-jours'

# Enlever une ambiguïté temporelle, sans modifier le régime des renouvellements
# déjà valablement convenus avant l'entrée en vigueur.
a = by_number['L1226-19']
a['proposed_xml'] = a['proposed_xml'].replace(
    'Une poursuite convenue de l’emploi après la réforme prend la forme du contrat unique à durée indéterminée',
    'Une poursuite de l’emploi convenue à compter de cette entrée en vigueur prend la forme du contrat unique à durée indéterminée',
)
a['reason'] = "Coordination de fond de la suppression prospective des nouveaux CDD et de leurs renouvellements, sans réduction des garanties de santé : le terme ancien, le contrôle du motif de refus et le plancher comprenant salaires et avantages sont conservés. La rédaction finale précise que seule la poursuite convenue à compter de l'entrée en vigueur prend la forme du contrat unique ; les périodes de renouvellement valablement convenues auparavant conservent leur régime. Aucune taxe, autorisation, déclaration ou pièce redondante n'est imposée par la source entière. Une coupe du motif étranger à l'accident ou du plancher réparateur retirerait une protection essentielle ; aucune coupe supplémentaire du brouillon n'est donc retenue."

# La seule cible modifiée lors du précédent essai est maintenant une vue de
# source officielle, et non une proposition de remplacement de L1235-3-1.
a = by_number['L1226-15']
a['review_notes'] += " Contrôle repris sur la vue actuelle de L. 1235-3-1, uniquement officielle, avec proposed_xml nul : le renvoi de montant conserve le minimum des salaires des six derniers mois, sans plafond ordinaire et sans ajouter au cas de refus de réintégration de L. 1226-15 une condition propre à une autre hypothèse. La liste officielle des nullités et les réserves de salaires et d'indemnité du dernier alinéa ne sont pas abrogées. La note de 2017 conserve son champ. Aucun contenu ni aucune empreinte d'une ancienne proposition de cette cible n'est utilisé."

# Analyse de chaque obligation maintenue : les formulations de brouillon
# ci-dessous sont conservées pour les corrections de fond, pas pour le style.
for item in answer:
    item['review_notes'] += " Les reference_checks sont établis sur les textes officiels, notes et propositions des vues actuelles de reference-targets.json ; une proposition est distinguée du droit en vigueur. Les cibles hors de ce fichier déjà signalées dans ces notes ont été consultées dans le seul corpus public local, sans modification. Ce contrôle rédactionnel et technique ne constitue pas une approbation juridique indépendante."

for name, digest in input_hashes.items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name

(ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'input-review-fingerprints.json').write_text(json.dumps(input_hashes, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(answer)}, ensure_ascii=False))
