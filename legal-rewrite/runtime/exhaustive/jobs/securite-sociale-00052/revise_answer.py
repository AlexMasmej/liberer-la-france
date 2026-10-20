import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('previous-answer.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in answers}

# Les corps normatifs du brouillon sont repris après comparaison avec les sources.
# Les analyses de renvois sont établies à nouveau sur les vues intégrales actuelles.
contexts = {
    'L341-14-1': (
        "Le service de l'invalidité est ici articulé avec la retraite progressive, les départs anticipés et l'amiante ; ses accessoires restent maintenus.",
        "La poursuite ou la réduction d'activité permettant la retraite progressive demeure possible avec un nouvel emploi à durée indéterminée ; la durée de cette phase ne termine pas l'emploi.",
        "La suspension de l'invalidité dépend de la prestation de retraite servie, sans attendre un an d'emploi ni le versement d'une indemnité de licenciement."
    ),
    'L341-16': (
        "Le choix exprès de liquider la vieillesse pour inaptitude et le maintien de l'invalidité pendant l'activité relèvent des cinq alinéas de L341-16.",
        "L'activité professionnelle qui ouvre cette dérogation reste recevable sous contrat unique futur ; ni son début ni sa poursuite ne nécessitent un ancien CDD.",
        "La demande expresse de retraite n'est pas une rupture patronale : le maintien de l'invalidité et le minimum comparatif ne dépendent donc pas du premier anniversaire de l'emploi."
    ),
    'L341-17': (
        "Le maintien temporaire de l'invalidité au chômage indemnisé et son relais en cas de reprise d'activité sont les objets de L341-17.",
        "La reprise d'activité permet toujours le bénéfice du deuxième alinéa de L341-16 avec un contrat unique nouveau ; aucune durée de chômage ne constitue un terme de cet emploi.",
        "Le revenu de remplacement visé est distinct de l'indemnité ordinaire patronale : les conditions de maintien de l'invalidité ne sont pas remplacées par une ancienneté d'un an."
    ),
    'L342-3': (
        "La référence de L342-3 est la pension principale réelle ou théorique du défunt pour calculer la pension du conjoint survivant invalide.",
        "Les carrières du défunt accomplies sous anciens contrats comme sous nouveaux contrats uniques alimentent les droits selon les règles de pension ; aucun ancien CDD n'est exigé du conjoint.",
        "Le pourcentage de la pension principale n'est pas une indemnité de licenciement : aucun seuil d'un an chez un employeur, plafond de six mois ou notification de rupture ne lui est applicable."
    ),
    'L351-1': (
        "Les cinq premiers alinéas de L351-1 règlent l'âge de liquidation, le salaire, le taux, la durée et la garantie historique de pension.",
        "Les périodes d'emploi futures sous contrat unique restent des périodes d'assurance dans leurs conditions propres ; une fin de formation ou de mission n'en devient pas le terme contractuel.",
        "Le salaire de base et la durée d'assurance ne sont pas le salaire de référence et l'ancienneté de l'indemnité de rupture : aucun droit à retraite n'est fermé avant un an d'emploi."
    ),
    'L351-1-1 A': (
        "Les durées d'au moins un an, jusqu'à neuf ans et au plus deux ans de L351-1-1 A abaissent des âges d'accès à la retraite.",
        "Les futures activités sous contrat unique peuvent toujours ouvrir les départs et la retraite progressive visés ; l'abaissement d'âge ne fixe aucune durée de l'emploi.",
        "Les abaissements d'âge ne sont pas une indemnité de rupture : ni le seuil d'un an chez l'employeur ni le plafond de six mois ne réduisent ces dérogations de pension."
    ),
    'L351-1-1': (
        "La carrière longue repose sur quatre âges de début d'activité et sur la durée d'assurance, avec les périodes réputées cotisées des 1°, 2° et 3°.",
        "Les périodes acquises sous contrat unique futur restent éligibles et les anciens contrats restent pris en compte ; les équivalences des fonctionnaires, magistrats et militaires conservent leur régime public.",
        "La durée totale d'assurance tous régimes n'est pas l'ancienneté chez un même employeur : le seuil d'un an de rupture ordinaire ne conditionne aucune période admise pour carrière longue."
    ),
    'L351-1-2': (
        "La surcote de L351-1-2 dépend de l'assurance cotisée après l'âge et la durée requis, avec les exceptions pour enfants et handicap.",
        "La continuation d'activité sous contrat unique futur permet toujours d'acquérir la surcote dans ses conditions propres ; ni une mission ni une phase de formation ne termine cet emploi.",
        "La surcote majore la pension et non une créance patronale : les 0,20 mois par année et le seuil d'un an ne remplacent pas les conditions d'âge et d'assurance."
    ),
}

def work_check(article, target):
    context, employment, severance = contexts[article]
    if target == 'L1234-1':
        return (
            context + " La source de L1234-1 gradue le préavis de licenciement selon l'ancienneté ; sa proposition prévoit quinze jours calendaires pour les contrats nouveaux et conserve le régime ancien pour les contrats antérieurs. "
            "Ce préavis et sa notification de rupture ne règlent aucun âge, délai de service ou demande de pension ici ; les procédures collectives et protections distinctes ne sont pas effacées."
        )
    if target == 'L1221-2':
        return (
            employment + " La proposition de L1221-2, distincte de sa source officielle autorisant encore les CDD, impose la durée indéterminée aux emplois privés nouveaux et protège les contrats antérieurs sans nouveau renouvellement à durée déterminée. "
            "Elle n'institue ni ancienneté minimale de pension ni notification de rupture dans cet article social et ne transforme pas les agents publics en salariés privés."
        )
    if target == 'L1234-9':
        return (
            severance + " La proposition de L1234-9 réserve l'indemnité ordinaire à la rupture patronale : zéro avant un an mesuré au terme effectif, préavis inclus, puis 0,20 mois par année totale, fractions en mois complets, plafond de six mois, avec exception de faute grave et transition des anciens contrats. "
            "Ces règles ne retranchent ni pension, ni congés, ni réparation d'une illégalité, ni indemnité spéciale dans le présent champ."
        )
    raise ValueError(target)

specific = {
    ('L341-14-1', 'L161-22-1-5'): "Le renvoi vise le bénéfice effectif de la retraite progressive : le I de la cible comprend salariés à temps partiel ou réduit, activités sans durée définie et activité agricole, avec âge, assurance, quotités et fraction commune ; le II maintient ses trois exclusions. La proposition de la cible conserve ces conditions. L341-14-1 écarte la suspension de l'invalidité quand la retraite progressive est elle-même suspendue et garde les accessoires ; aucun seuil d'ancienneté ni notification de licenciement ne s'y substitue.",
    ('L341-14-1', 'L351-1-4'): "La cible officielle seule distingue le I, retraite à soixante ans pour l'incapacité professionnelle au taux requis, le II, taux plein sans durée complète, et le III, âge abaissé de deux ans avec conditions d'exposition et de lien. Sa dispense finale des 2° et 3° et de commission pour certaines maladies reste applicable. Le renvoi suspend le service de l'invalidité lorsque cette retraite est perçue, sans supprimer ses accessoires ; il n'est pas une condition de rupture ou d'ancienneté privée.",
    ('L341-15', 'L351-1'): "Le premier alinéa de la cible officielle soumet la pension ordinaire à une demande à l'âge de L161-17-2 ; L341-15 conserve sa substitution spéciale à l'âge d'inaptitude de L351-1-5 et ses deux garanties de montant, dont celle des invalidités liquidées avant le 31 mai 1983. Le corps proposé dans ce lot laisse les cinq alinéas de L351-1 à leur place et ajoute seulement la coordination du transfert conditionnel. Il ne substitue ni l'âge ordinaire ni une notification de licenciement à la règle spéciale.",
    ('L341-16', 'L351-1'): "Le troisième alinéa de L341-16 exclut le seul premier alinéa de L351-1 : le calcul du taux, du salaire, de la durée et la garantie de 1983 restent visés. La vue fournie de L351-1 est sa source officielle, tandis que ce lot lui ajoute un sixième alinéa coordonnant la fraction transférée sous conditions. Cet ajout demeure dans le renvoi sans déplacer les cinq règles sources ni supprimer le choix exprès ou le minimum comparatif de L341-16 ; il n'ajoute aucune ancienneté d'emploi.",
    ('L341-17', 'L351-1'): "Le renvoi indirect au calcul de L351-1 résulte du troisième alinéa de L341-16, applicable par le premier alinéa de L341-17, et laisse de côté le premier alinéa de L351-1. Les alinéas de calcul restent aux mêmes positions dans le projet du lot ; son ajout final sur le transfert ne supprime ni le maintien temporaire d'invalidité au chômage ni la garantie comparative. La demande de retraite et la reprise d'activité ne deviennent pas une notification de licenciement soumise à ancienneté.",
    ('L342-3', 'L351-1'): "L351-1 fournit les règles de calcul de la pension principale dont bénéficiait ou aurait bénéficié le défunt : salaire de base, taux et durée, avec sa garantie historique. La vue cible est la source officielle entière ; le sixième alinéa proposé ici coordonne seulement la fraction effectivement transférée et protège les droits antérieurs. L342-3 demeure applicable aux droits non encore liquidés comme aux pensions servies ; il ne règle ni le capital au décès ni une indemnité de rupture privée.",
    ('L351-1', 'L241-3'): "La source officielle de L241-3 finance l'assurance vieillesse et veuvage par les cotisations et autres ressources énumérées ; sa proposition conserve ce financement au I et prévoit au II le transfert de cotisations existantes pour les seuls salariés du régime général employés par une personne privée. Les III et VI exigent avant tout transfert des règles de réduction exacte des droits futurs, de protection des droits antérieurs et de gouvernance ; le II exige le financement voté de chaque palier. Le nouvel alinéa de L351-1 répond à ces conditions sans présumer leur réalisation, sans étendre le transfert au public ou à l'agricole et sans promettre deux fois les mêmes droits. Il ne s'agit ni d'une baisse de cotisation ni de la condition d'ancienneté d'une indemnité de rupture.",
    ('L351-1', 'L330-1'): "Le quatrième alinéa de L351-1 inclut exactement les indemnités journalières du 2° de L330-1 dans le salaire de base : le 1° des frais et le 3° d'autres indemnités ne sont pas inclus par ce renvoi. La proposition fournie de L330-1 conserve le 2° et son objet, en coordonnant ses proportions de remboursement, et rectifie séparément un renvoi du 3°. Aucun déplacement n'affecte donc cette inclusion. Les transitions maternité 2011/2012 propres à L351-1 sont conservées, sans nouvelle condition d'ancienneté ou de notification de rupture.",
    ('L351-1-1 A', 'L351-1'): "La cible est l'âge mentionné au seul premier alinéa de L351-1 ; l'article L351-1-1 A conserve toutes ses bornes d'abaissement d'âge. La vue fournie est la source officielle de L351-1, et sa proposition dans ce lot conserve cet alinéa et les quatre suivants à leur place. Le sixième alinéa de financement n'élève aucun âge et ne retire aucune voie de retraite anticipée ; l'ancienneté de rupture et son délai de notification n'entrent pas dans ce renvoi.",
    ('L351-1-1 A', 'L351-6-1'): "Le I de L351-6-1 ouvre la majoration d'assurance au titre du compte professionnel de prévention ; son II la retient pour le taux et la durée et répute les trimestres cotisés pour les carrières longues et les régimes cités. L351-1-1 A conserve pour ces assurés l'abaissement d'âge ne pouvant excéder deux ans. La note d'application aux pensions prenant effet en 2026 garde son champ. Cette durée n'est ni un préavis ni une ancienneté d'emploi, et l'avantage reste ouvert sous contrat unique futur.",
    ('L351-1-1 A', 'L161-22-1-5'): "Le renvoi désigne les assurés de la retraite progressive du I, y compris indépendants et exploitants agricoles, avec ses conditions d'âge, d'assurance et de quotité ainsi que les exclusions du II. La proposition de la cible conserve ces subdivisions et l'article L351-1-1 A maintient l'abaissement d'au moins un an. Ni une activité réduite ni la durée de versement d'une fraction de pension ne fixe le terme d'un emploi ; aucun préavis ou seuil d'indemnité de rupture ne remplace les conditions de retraite.",
    ('L351-1-1', 'L351-5'): "Le 3° de L351-1-1 vise la majoration pour congé parental de L351-5, égale à la durée effective du congé et accordée aux personnes de L351-4 quand elle est plus favorable. La cible n'a qu'une source officielle ; son ancien renvoi à L122-28-1 et sa référence au congé public de 1978 demandent une concordance dans ce texte hors lot, sans fermer ici les périodes parentales futures éligibles. Un congé dans un contrat unique ne termine pas l'emploi et le seuil d'un an de l'indemnité ordinaire ne conditionne pas cette majoration.",
    ('L351-1-1', 'L351-1'): "Le premier alinéa de L351-1-1 vise l'âge du premier alinéa de L351-1 et plafonne la durée exigible par celle de son deuxième alinéa. Les quatre âges de début d'activité, dont le plus élevé ne peut dépasser vingt et un ans, restent intacts. La proposition de L351-1 dans ce lot conserve ces deux positions et ajoute sa coordination en dernier alinéa seulement. Les périodes réputées cotisées ne disparaissent pas avec le transfert ; elles ne deviennent pas une ancienneté de licenciement chez un seul employeur.",
    ('L351-1-1', 'L381-1'): "Le 2° vise les périodes d'assurance vieillesse des parents au foyer de L381-1 et les situations publiques équivalentes expressément mentionnées. La cible officielle distingue inactivité et temps partiel, ressources, enfants et prestations, et fait financer les cotisations par les organismes débiteurs de prestations familiales ; sa dernière règle évite une double affiliation pour un même enfant et une même période. Le renvoi conserve ces avantages pour les situations futures, sans les assujettir à une ancienneté de rupture ni convertir les fonctionnaires en salariés privés.",
    ('L351-1-1', 'L381-2'): "Le 2° vise les périodes d'assurance des aidants de L381-2 et les périodes publiques équivalentes de son propre texte. La cible officielle inclut présence parentale, proche aidant, non-salariés et aide aux personnes handicapées, avec demandes résiduelles, exclusions publiques et limite totale d'un an pour les deuxième et troisième alinéas. Cette limite d'affiliation n'est pas le seuil d'indemnité ordinaire de rupture. Les dispenses de déclaration de cessation et de radiation demeurent ; aucune condition de CDD ancien ni notification de licenciement n'est ajoutée.",
    ('L351-1-1', 'L351-3'): "Le 1° autorise le décret à réputer cotisées certaines périodes validées sous L351-3, dont les neuf catégories restent distinctes : prestations de santé et naissance, chômage, service et guerre, détention, sport et stages. La répétition du congé supplémentaire de naissance dans le membre de phrase sur les rentes antérieures à juillet 1930 est une incohérence préexistante de la cible officielle, non une condition ajoutée ou corrigée ici. Ses transitions de naissance de 2026 et les droits futurs éligibles sont conservés ; aucun délai de notification ou seuil d'ancienneté de rupture n'est transposé.",
    ('L351-1-2', 'L351-1'): "La surcote vise l'âge du premier alinéa et la limite de durée du deuxième alinéa de L351-1, tous deux maintenus à leur place dans le corps proposé de ce lot. Le sixième alinéa ajouté coordonne les droits futurs sur la seule fraction transférée sous conditions ; il n'élève ni l'âge ni la durée et ne supprime pas les exceptions pour enfants ou handicap. La note protège les assurés qui remplissaient les conditions avant le 1er janvier 2013 ; aucune ancienneté chez un employeur ou notification de licenciement ne remplace ces règles.",
}

for source, answer in zip(sources, answers):
    assert all(source[k] == answer[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
    key = source['code_id'] + '|' + source['source_id']
    checks = []
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        number = target['number']
        assessment = (work_check(source['number'], number) if target['code_id'] == 'LEGITEXT000006072050'
                      else specific[(source['number'], number)])
        checks.append({'target_key': target_key, 'view_sha256': target['view_sha256'], 'assessment': assessment})
    answer['reference_checks'] = checks

by_number['L351-1']['review_notes'] = (
    "Les cinq positions d'alinéas sont préservées pour L341-16, L351-1-1 A, L351-1-1 et L351-1-2. "
    "Le renvoi nouveau à L241-3 dispose désormais de sa cible complète dans reference-targets.json, source, notes et proposition lues ; son contrôle figure dans reference_checks avec l'empreinte actuelle. "
    "Le I de cette proposition conserve les ressources existantes ; le II borne le transfert aux salariés du régime général employés par une personne privée et subordonne chaque palier à un financement voté ; les III et VI interdisent tout démarrage avant les règles de droits et de gouvernance. "
    "Les paliers de 0,5 %, 1 %, 2 %, 3 % et 4 %, les deux points salariaux et deux points patronaux à terme et le plafond de frais de 0,35 % restent à cette cible : le présent article ne crée aucun taux supplémentaire. "
    "L111-2-1, L161-17, L161-17-2, L161-23-1, L161-25, L357-4 et R351-27 ont également été lus en entier dans le corpus public fourni, sources, notes et propositions disponibles. "
    "R351-27 et les autres règles de salaire de référence, durée et proratisation doivent recevoir une formule coordonnée avant le premier transfert ; aucun coefficient arbitraire ni application immédiate n'est présumé. "
    "L357-4 conserve son application locale ; ni les employeurs publics ni les salariés agricoles ne sont intégrés automatiquement au transfert. "
    "Les dates du 1er juillet 2011 et du 1er janvier 2012 de la note source demeurent à leur objet. L330-1 2° reste la cible des indemnités intégrées au salaire de base, sans extension au 3°. "
    "Les modalités de liquidation du capital, de propriété et de décès nécessitent les dispositions distinctes identifiées au VI de L241-3 ; aucun impôt de décès n'est créé. "
    "Le gel de revalorisation proposé à L161-23-1 conserve sa transition propre, sans baisse nominale liée au transfert. Aucun autre renvoi nouveau n'est introduit dans le corps de cet article ; les textes cités seulement dans ces notes ne sont pas présentés comme réécrits."
)

by_number['L341-13']['review_notes'] = (
    "Incohérence préexistante : L341-14 n'est pas présent dans le corpus actif fourni, contrairement à L341-14-1 et L341-14-2 lus dans ce lot. "
    "La réserve proposée porte sur les règles particulières applicables du chapitre, sans attribuer à l'une de ces deux dispositions une filiation historique non documentée. "
    "Elle respecte notamment le maintien des accessoires et le cumul autorisé avec une pension publique, sans rétablir un texte disparu ni élargir leurs conditions. "
    "La date et le contenu historique de l'ancienne cible demeurent non établis ; cette coordination ne vaut donc pas concordance historique exhaustive. "
    "Aucun nouveau renvoi numéroté à une cible absente de reference-targets.json n'est introduit ; la condition de capacité de gain et ses deux conséquences sont conservées, sans taux numérique inventé."
)

by_number['L341-17']['review_notes'] = (
    "Dans L341-16 maintenu intégralement, le premier alinéa vise la demande expresse, le troisième le calcul vieillesse et l'avant-dernier le minimum comparatif : les trois renvois gardent leur cible. "
    "L5421-2 est le renvoi source au revenu de remplacement et non une règle de préavis ; il n'est pas ajouté par ce lot et ne figure pas dans les cibles obligatoires fournies. "
    "La poursuite de l'invalidité au chômage, sa limite réglementaire et la reprise d'activité restent à leur champ, sans importation des quinze jours ni du seuil d'un an. "
    "Les deux notes du 1er septembre 2023 restent attachées à leurs réformes historiques."
)

# Les analyses facultatives mentionnent la proposition du présent lot comme telle,
# et non comme une modification déjà en vigueur dans la vue officielle de la cible.
by_number['L341-16']['review_notes'] = (
    "Les cinq alinéas restent à leur place : les premier, troisième et avant-dernier visés par L341-17 demeurent la demande, le calcul et la garantie de montant. "
    "Le renvoi à L351-1 exclut seulement son premier alinéa ; le sixième alinéa proposé dans ce lot reste donc inclus, dans son seul champ de transfert conditionnel, sans réduire la garantie comparative. "
    "La vue fournie de L351-1 est encore sa source officielle : la présente proposition n'est pas traitée comme du droit en vigueur. "
    "L351-8 1° et L351-1-5 ont été lus dans le corpus. Les deux notes de septembre 2023 restent historiques ; aucune notification de rupture ni ancienneté chez un employeur ne conditionne cette dérogation."
)

Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answers)} articles ; {sum(len(a["reference_checks"]) for a in answers)} analyses de renvois établies sur les vues actuelles.')
