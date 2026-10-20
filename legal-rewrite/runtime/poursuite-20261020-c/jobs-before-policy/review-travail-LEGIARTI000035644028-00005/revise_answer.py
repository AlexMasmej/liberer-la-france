import copy
import hashlib
import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
reference_bytes = Path('reference-targets.json').read_bytes()
references = json.loads(reference_bytes)
reference_digest = hashlib.sha256(reference_bytes).hexdigest()
assert reference_digest == '3fefceb74b63c5c6f7dcf0dfc43b04943b82f4ea87aa98769eed17a58cb4ca5b'
answer = copy.deepcopy(json.loads(Path('previous-answer.json').read_text()))
by_number = {a['number']: a for a in answer}

# Repartir des articles complets de l'essai précédent, sans ses certificats.
for article in answer:
    article['reference_checks'] = []

a = by_number['L1251-16']
old = "1° Les informations énumérées à l'article L. 1251-43. Elles peuvent être communiquées"
new = "1° Les informations exigibles en application de l'article L. 1251-43 dans son champ temporel. Pour les mises à disposition convenues à compter de l'entrée en vigueur de la loi portant la présente réforme, ce renvoi n'impose ni les justifications précises du motif, ni le nom et la qualification de la personne remplacée ou à remplacer, ni une clause spéciale de variation du terme ou sa répétition dans un avenant. Le motif du recours et les autres informations maintenues par cet article restent communiqués. Ces informations peuvent être communiquées"
assert old in a['proposed_xml']
a['proposed_xml'] = a['proposed_xml'].replace(old, new)
a['reason'] += " La cible actuelle L. 1251-43 est désormais reprise explicitement : le renvoi du 1° ne rétablit ni les précisions et identités de remplacement retirées, ni la clause spéciale de variation du terme. Ces suppressions propres à la cible constituent des coordinations, sans seconde réduction comptée dans le présent article."
a['review_notes'] = (
    "Source entière, notes, previous_draft et article complet de previous-answer.json confrontés ; les deux alinéas introductifs et les 1° à 7° restent dans leur ordre. Le 1° vise la cible actuelle L. 1251-43, et non sa rédaction antérieure : son 1° maintient le motif mais retire les justifications précises et l'identité/qualification du remplacé pour les nouvelles mises à disposition ; son 3° retire la clause spéciale de variation et sa répétition. Ces pièces ne sont pas exigées à nouveau dans la lettre de mission. Le terme, ou l'événement et la durée minimale lorsqu'ils sont applicables à la mission, les caractéristiques et risques du poste, les équipements et toute la rémunération de comparaison, primes et accessoires inclus, restent dans les rubriques maintenues. Une durée minimale d'affectation ne devient jamais une durée limitée d'emploi. Les mises à disposition et anciens contrats déjà convenus gardent leurs mentions et termes historiques ; les renouvellements valablement conclus avant la réforme ne sont pas assimilés à des décisions nouvelles. "
    "Les dispenses des 2° et 3° supposent une information effectivement remise, exacte et applicable : aucun justificatif nouveau ni dispense de payer. Le 5° garde le champ hors territoire métropolitain, la charge patronale et l'exception de rupture de l'emploi à l'initiative du salarié ; la fin d'une affectation ne suffit pas. L. 1251-32 conserve le complément de salaire de 10 % lorsqu'il est dû pour un ancien contrat, indépendamment du seuil d'un an de l'indemnité ordinaire. "
    "Le renvoi à L. 1251-44, absent des cibles fournies et ajouté par rapport à la source officielle, est conservé après lecture intégrale de sa source dans le corpus public : une interdiction d'embauche par l'utilisateur est réputée non écrite. L. 1221-5-1 et R. 1221-34 à R. 1221-38 ont été lus avec leurs notes : information initiale, modifications, départ à l'étranger et détachement restent dus selon leur champ et leurs échéances autonomes. L. 1255-2, R. 1255-1, R. 1263-8 et R. 6226-3 ont été lus dans le corpus. Leurs coordinations doivent reconnaître les dispenses, y compris pour les lettres futures des anciens CDI ; R. 1255-1 garde une rédaction insuffisamment coordonnée. Aucun de ces textes hors lot n'est modifié ici. Préserver les contrôles utiles, les recours et la loi répressive plus douce dans son champ ; aucune conformité européenne ou validation juridique globale n'est affirmée."
)
a['substantive_impact']['assessment'] += " Le renvoi à L. 1251-43 est également rectifié sur son texte actuel, sans compter comme une seconde coupe les mentions retirées dans cet autre article."
a['substantive_impact']['scope_limitations'] += " Les anciennes mises à disposition restent soumises à leurs mentions historiques ; les dispenses de la cible ne sont pas étendues rétroactivement."
a['substantive_impact']['effects'] += [
    {
        'kind': 'coordination',
        'measure_id': 'justifications-remplacement-supprimees',
        'description': "Le renvoi de la lettre de mission ne rétablit pas les précisions et identités de remplacement retirées par la cible L. 1251-43.",
        'before': "Le 1° exige la reproduction des clauses et mentions de L. 1251-43, dont la source officielle exige les justifications précises du motif et, dans les cas visés, le nom et la qualification de la personne remplacée.",
        'after': "Le motif reste communiqué, sans réintroduction par la lettre de mission des justifications précises ni de l'identité et de la qualification du remplacé supprimées dans les nouvelles mises à disposition.",
        'unit': 'legal_duty',
        'affected_population': "Agences, utilisateurs et salariés concernés par les nouvelles mises à disposition, y compris de remplacement.",
        'conditions_and_transition': "Dispenses dans le champ temporel de L. 1251-43 ; anciennes mises à disposition et anciens contrats de mission restent à leur régime de mentions. Les autres informations nécessaires et le contrôle de la réalité du motif subsistent.",
        'replacement_or_new_burdens': "Aucun dossier ni attestation de remplacement ; coordination de la suppression portée par la cible, sans gain autonome supplémentaire attribué ici.",
        'source_quote': "1° La reproduction des clauses et mentions du contrat de mise à disposition énumérées à l'article L. 1251-43 ;",
        'proposed_quote': "Pour les mises à disposition convenues à compter de l'entrée en vigueur de la loi portant la présente réforme, ce renvoi n'impose ni les justifications précises du motif, ni le nom et la qualification de la personne remplacée ou à remplacer, ni une clause spéciale de variation du terme ou sa répétition dans un avenant."
    },
    {
        'kind': 'coordination',
        'measure_id': 'assouplissement-terme-mission',
        'description': "Absence de rétablissement, dans la lettre de mission, de la clause spéciale de variation retirée au 3° de L. 1251-43.",
        'before': "Le 1° exige la reproduction des clauses de mise à disposition ; la source de L. 1251-43, 3°, impose le cas échéant une clause de variation du terme et l'étend à l'avenant de renouvellement.",
        'after': "Le renvoi n'exige plus cette clause ni sa répétition dans le nouveau champ ; l'information utile sur les dates, l'accord des entreprises et le consentement aux modifications essentielles de l'emploi restent applicables.",
        'unit': 'legal_duty',
        'affected_population': "Agences et salariés recevant la lettre des missions relevant de l'assouplissement de L. 1251-30.",
        'conditions_and_transition': "Nouvelles mises à disposition à compter de l'entrée en vigueur, dans le champ des dispositions coordonnées ; mentions et engagements historiques conservés, sans nouveau contrat de travail à terme.",
        'replacement_or_new_burdens': "Pas de clause ni pièce substituée ; simple coordination de la mesure d'assouplissement de la date de fin d'affectation, sans seconde suppression comptée.",
        'source_quote': "1° La reproduction des clauses et mentions du contrat de mise à disposition énumérées à l'article L. 1251-43 ;",
        'proposed_quote': "Pour les mises à disposition convenues à compter de l'entrée en vigueur de la loi portant la présente réforme, ce renvoi n'impose ni les justifications précises du motif, ni le nom et la qualification de la personne remplacée ou à remplacer, ni une clause spéciale de variation du terme ou sa répétition dans un avenant."
    }
]

# Les décisions de renouvellement nouvelles et les renouvellements déjà conclus
# sont deux situations différentes dans les cibles actuelles L. 1251-35/35-1.
by_number['L1251-12-1']['review_notes'] += (
    " Relecture des cibles actuelles L. 1251-35 et L. 1251-35-1 : l'interdiction porte sur les renouvellements conclus ou décidés après l'entrée en vigueur. Un renouvellement valablement conclu avant cette date conserve ses effets, même s'il commence plus tard ; une faculté non exercée ne suffit pas. L'abrogation ne convertit pas cette faculté en droit à un nouveau CDD."
)
by_number['L1251-28']['review_notes'] += (
    " Les cibles actuelles L. 1251-35 et L. 1251-35-1 préservent les renouvellements valablement conclus avant la date d'entrée en vigueur, même à effet ultérieur ; elles interdisent une conclusion ou décision nouvelle après cette date, et non l'exécution différée d'un engagement déjà valable."
)
by_number['L1251-26']['review_notes'] += (
    " La cible radiologique L. 1251-34 n'est pas fournie dans le présent reference-targets.json : sa source et son projet ont été relus en entier dans le corpus, sans reprendre l'ancienne empreinte de vue. Son renvoi au deuxième alinéa reste opératoire ; le présent lot ne certifie ni ne modifie cet article extérieur au lot."
)
by_number['L1251-30']['review_notes'] += (
    " La cible actuelle entière de L. 1251-43 confirme le retrait de la clause préalable au 3° pour les nouvelles mises à disposition, sans exiger de document distinct. Le présent article ne la rétablit pas ; L. 1251-16 est coordonné dans le même sens."
)
by_number['L1251-31']['review_notes'] += (
    " La suppression actuelle du 3° de L. 1251-43 ne ferme pas le report favorable de L. 1251-31 ; aucune clause spéciale préalable ni répétition en avenant n'est réintroduite dans le nouveau champ."
)

# Chaque analyse est reconstruite à partir des vues entières du présent fichier.
# Les trois cibles communes sont appliquées à l'objet spécifique de chaque source.
local = {
    'L1251-12': "Le plafond conventionnel concerne l'affectation chez l'utilisateur ; il ne constitue pas une rupture de l'emploi chez l'agence.",
    'L1251-12-1': "Le barème supplétif des missions à terme est abrogé prospectivement ; les anciens termes, leurs dérogations et les durées pédagogiques autonomes restent distincts.",
    'L1251-13': "L'anticipation avant l'absence est une permission de commencer une affectation de remplacement, sans fin d'emploi ni démarche de rupture.",
    'L1251-14': "L'essai nouveau appartient au seul contrat de travail ; une nouvelle mission ou conversion ne peut ouvrir un nouvel essai.",
    'L1251-15': "Le salaire de l'essai reste dû, sans abattement ni condition d'ancienneté, dans les limites propres des garanties salariales applicables.",
    'L1251-16': "L'écrit de mission informe sur une affectation et réemploie les informations déjà remises ; il ne constitue pas un nouveau contrat d'emploi.",
    'L1251-17': "Les deux jours ouvrables concernent l'envoi de l'écrit d'affectation, sans constituer un préavis ni une condition d'ouverture de l'indemnité ordinaire.",
    'L1251-26': "La garantie jusqu'au terme de l'ancienne mission demeure ; la continuité du nouvel emploi entre missions et sa rupture patronale relèvent de règles différentes.",
    'L1251-28': "Le départ anticipé d'une ancienne mission reste distinct de la démission régulière du nouvel emploi ; seule cette dernière est dispensée de justifier un autre CDI.",
    'L1251-29': "La suspension n'empêche pas la fin de l'affectation, mais cette fin ne rompt pas l'emploi indéterminé et ne remplace pas les protections liées à la suspension.",
    'L1251-30': "L'accord sur la nouvelle date d'affectation retire trois calculs légaux ; il ne vaut ni notification de rupture de l'emploi ni réduction d'un salaire garanti.",
    'L1251-31': "Le report jusqu'au surlendemain de la reprise reste une faculté de passation, sans terme d'emploi et sans plafond nouveau sur les autres variations permises."
}

analyses = {}
for n in by_number:
    prefix = local[n] + ' '
    analyses[n] = {
        'L1234-1': prefix + (
            "La source de L. 1234-1 règle le licenciement hors faute grave selon les paliers de six mois et deux ans ; son projet fixe quinze jours calendaires pour les nouveaux emplois, sans ancienneté requise et avec préavis payé même si une faute grave interdit le travail. Ces règles ne se déduisent pas d'une date de mission ; les anciens contrats gardent leurs paliers et avantages, et les procédures collectives ou autorisations protectrices subsistent."
        ),
        'L1221-2': prefix + (
            "La source de L. 1221-2 autorise encore un terme dans les cas du titre IV ; la proposition actuelle impose l'emploi indéterminé pour les nouveaux recrutements et interdit la fin automatique par mission, remplacement, saison ou formation. La règle locale porte donc sur l'affectation, jamais sur un nouveau CDD ou un renouvellement à terme décidé après la réforme. Les engagements antérieurs et avantages futurs éligibles sont préservés ; aucun régime d'agent public n'est attribué au salarié privé de l'agence."
        ),
        'L1234-9': prefix + (
            "La source de L. 1234-9 ouvre l'indemnité du CDI à huit mois, hors faute grave. Le projet exige pour le nouvel emploi un an à sa fin effective, préavis inclus sauf fin d'essai de L. 1221-25 ; il retient 0,20 mois par année totale, première année comprise, prorata des mois complets et plafond légal de six mois, employeur seul. Ce seuil ne conditionne aucun salaire, document ou avantage d'affectation ; les anciens CDI gardent huit mois et leurs deux composantes, sans double compte, les indemnités spéciales et dommages restant distincts."
        )
    }

analyses['L1251-14']['L1234-1'] = (
    "Le préavis de licenciement de L. 1234-1 ne doit pas être transposé directement à une rupture d'essai. Sa source distingue les paliers de six mois et deux ans ; sa proposition impose quinze jours aux nouveaux emplois et conserve les anciens paliers. Ici, les renvois spéciaux à L. 1221-25 et L. 1221-26 fixent le départ du délai, le reliquat patronal indemnisé et la fraction salariée éventuellement exécutée après l'essai. Aucune condition d'ancienneté ni procédure de licenciement n'est ajoutée à l'essai sur ce fondement."
)
analyses['L1251-28']['L1234-1'] = (
    "L. 1234-1 traite une rupture décidée par l'employeur, alors que L. 1251-28 concerne le départ du salarié. Les paliers d'ancienneté de six mois et deux ans de la source et leur remplacement proposé par quinze jours ne calculent donc pas le préavis historique de départ vers un CDI. Le nouvel emploi relève ici de sa règle de démission et de la notification écrite de L. 1234-3, avec dispenses favorables ; les anciens contrats conservent un jour par semaine, de un jour à deux semaines."
)
analyses['L1251-26']['L1234-9'] = (
    "Le renvoi vise l'indemnité ordinaire de la rupture de l'emploi par l'agence, jamais la rémunération garantie jusqu'au terme d'une ancienne mission. La source ouvre le droit du CDI à huit mois hors faute grave ; le projet actuel applique aux nouveaux contrats un an à la fin effective, préavis exécuté ou non inclus sauf fin d'essai. Le texte proposé reprend 0,20 mois de salaire brut par année totale, première année comprise, fractions au prorata des mois complets et plafond légal de six mois, employeur seul, hors faute grave. Les anciens CDI gardent huit mois et leurs composantes transitoires ; indemnités spéciales et garanties plus favorables ne sont pas plafonnées ici."
)
analyses['L1251-28']['L1234-9'] = (
    "L. 1234-9, dans la source comme dans la proposition, vise une rupture patronale et ne rémunère pas la démission ordinaire traitée ici. Le seuil nouveau d'un an à la fin effective, préavis inclus sauf fin d'essai, puis 0,20 mois par année totale et mois complets dans la limite de six mois, ne mesure donc pas le préjudice d'une rupture ancienne ni la responsabilité pour abus. L'exclusion de l'indemnité ordinaire n'éteint aucun salaire, congé, dommage d'illégalité ou droit spécial, et les anciens CDI conservent leur transition."
)

def set_check(source_number, target_number, text):
    analyses[source_number][target_number] = text

for n in ['L1251-12', 'L1251-12-1', 'L1251-30']:
    set_check(n, 'L1251-58-6', local[n] + ' ' +
        "La source de L. 1251-58-6 dispense déjà le salarié en CDI avec l'agence de la durée totale de L. 1251-12-1 ; le projet étend expressément cette continuité au contrat unique. Le renvoi conserve cette dispense pour les anciens et futurs emplois indéterminés, sans rétablir dix-huit mois par lettre de mission ni compter un second allègement. Les limites conventionnelles autonomes et la prévention des affectations permanentes chez l'utilisateur restent distinctes ; aucune ancienneté ou notification de rupture ne conditionne la dispense.")

set_check('L1251-12-1', 'L1251-35-1',
    "La source permet deux renouvellements supplétifs, avec durée cumulée limitée et clause ou avenant soumis avant le terme. La proposition actuelle abroge ce circuit pour les futures missions d'un emploi indéterminé. Elle conserve les renouvellements valablement conclus avant l'entrée en vigueur, même à effet ultérieur ; une faculté non exercée n'est pas un renouvellement déjà conclu. L'abrogation de L. 1251-12-1 ne permet donc aucun renouvellement nouvellement conclu ou décidé après cette date, sans faire perdre les créances des anciens termes ni leurs dérogations.")
set_check('L1251-12-1', 'L1251-35',
    "L. 1251-35 habilite actuellement la branche à fixer le maximum de renouvellements et impose clause ou avenant avant le terme. Son projet actuel abroge ce fondement tout en conservant les limites conventionnelles autonomes de durée et l'interdiction des affectations permanentes. Les renouvellements déjà valablement conclus conservent leurs effets, et non les seules facultés restées inexercées. Le retrait du barème de L. 1251-12-1 ne les invalide pas et n'ouvre aucun nouveau CDD après la réforme ; ni durée d'emploi, ni ancienneté, ni notification de rupture ne sont déduites du nombre d'affectations.")
for n in ['L1251-12-1', 'L1251-30']:
    set_check(n, 'L1251-12', local[n] + ' ' +
        "La source de L. 1251-12 donne compétence à la branche étendue de l'utilisateur pour la durée totale, avec interdiction d'occuper durablement un emploi permanent. La proposition fournie, conservée dans ce lot, cantonne cette compétence à la mission du nouvel emploi indéterminé. Le renvoi garde les plafonds conventionnels encore applicables et leur champ historique, sans les transformer en terme d'emploi ni recréer le barème légal abrogé. La dispense favorable des CDI demeure ; le changement d'affectation n'est pas une notification de rupture.")
set_check('L1251-12-1', 'L6222-7-1',
    "Les six mois à trois ans de la source concernent le contrat d'apprentissage à durée limitée ou sa phase pédagogique en CDI, sous réserve des prolongations de L. 6222-11. Le projet conserve ces bornes pour la seule phase, l'égalité avec le cycle et les adaptations liées aux compétences, à la mobilité et aux engagements énumérés, avec convention tripartite. Abroger le plafond de trente-six mois de L. 1251-12-1 ne retire aucune de ces adaptations ni les aides futures éligibles et ne fixe aucun terme d'emploi. Le minimum autonome de mission de L. 6226-1 reste hors de cette abrogation ; ni préavis ni ancienneté d'un an ne remplacent la durée pédagogique.")

for n in ['L1251-13', 'L1251-31']:
    set_check(n, 'L1251-6', local[n] + ' ' +
        "Les 4° et 5° visés comprennent les dirigeants, professionnels libéraux, conjoints participants et associés non salariés énumérés, puis les exploitants, aides familiaux, associés d'exploitation et conjoints agricoles dans les conditions des renvois ruraux. La proposition actuelle conserve ces personnes comme remplacés : elle ne les transforme pas en salariés de l'agence. La faculté locale reste ouverte aux futurs remplacements de ces catégories, sans condition d'ancienneté de l'intérimaire ni notification de rupture ; seul l'emploi du remplaçant nouveau est indéterminé.")

for n in ['L1251-14', 'L1251-26', 'L1251-28']:
    set_check(n, 'L1234-3', local[n] + ' ' +
        "La source de L. 1234-3 prend la présentation du recommandé de licenciement comme point de départ. La proposition actuelle compte les quinze jours du nouveau régime dès le lendemain de la présentation, ou de la réception/remise si une autre forme est légalement permise ; pour le salarié, dès le lendemain de la réception de son écrit par l'employeur, preuve par tout moyen. Le délai expire au quinzième jour même non travaillé. Pour l'essai patronal, L. 1221-25 règle spécialement la réception sans recommandé imposé et la fin effective ; les notifications anciennes gardent leur régime.")
set_check('L1251-14', 'L1221-26',
    "La source fixe quarante-huit heures à l'initiative du salarié, ou vingt-quatre heures sous huit jours de présence. Le projet actuel impose quinze jours calendaires écrits au nouveau contrat, sans prolonger l'essai : si le préavis dépasse son terme, la fraction suivante s'exécute en emploi ordinaire et vaut démission, sans second délai. L. 1251-14 conserve cette correction du précédent essai et les dispenses favorables. L'allongement possible est recensé comme charge, sans l'appliquer aux anciens essais ni créer une indemnité ordinaire de démission.")
set_check('L1251-14', 'L1221-23',
    "La source exige une stipulation expresse de l'essai et de son renouvellement éventuel ; le projet ne permet plus le renouvellement des nouveaux contrats et conserve l'exigence expresse des anciennes possibilités licites. L. 1251-14 renvoie à la stipulation initiale de l'emploi, non à une faculté d'essai attachée à chaque lettre de mission. La dispense de répétition de cet écrit ne vaut pas consentement à un essai non convenu. Une conversion ne remet ni ancienneté ni essai à zéro ; la notification de rupture reste un acte distinct.")
for n in ['L1251-14', 'L1251-26']:
    set_check(n, 'L1221-25', local[n] + ' ' +
        "La source de L. 1221-25 comporte les prévenances patronales de vingt-quatre heures, quarante-huit heures, deux semaines et un mois, ainsi qu'une compensation sauf faute grave. Son projet actuel fixe quinze jours dès le lendemain de la réception établie, sans recommandé obligatoire pour l'essai. Le travail s'arrête au terme de l'essai et le reliquat est indemnisé, congés compris, même en cas de faute grave ; il n'ajoute pas d'ancienneté effective. Le renvoi conserve cette exception au préavis ordinaire, sans exiger un an pour payer les salaires ou la compensation et sans modifier les anciens essais.")
set_check('L1251-14', 'L1221-22',
    "La source réserve les durées d'essai plus courtes d'accords postérieurs à la loi de 2008 ou de l'écrit individuel. Le projet garde, pour le nouveau contrat, toute durée collective applicable plus courte quelle que soit sa date, ainsi que les durées individuelles plus courtes, sans renouvellement. Trois mois est donc un maximum, jamais une durée imposée par L. 1251-14. Ces avantages restent ouverts aux situations futures ; la note de 2023 et ses six mois d'entrée en vigueur concernent seulement le régime historique, sans fixer la date de cette réforme ni une ancienneté minimale.")

for n in ['L1251-14', 'L1251-15', 'L1251-26', 'L1251-28']:
    set_check(n, 'L1251-58-4', local[n] + ' ' +
        "La source et le projet fourni de L. 1251-58-4 excluent encore des missions en CDI les articles L. 1251-14, L. 1251-15 et L. 1251-26 à L. 1251-28, notamment. Le dernier alinéa local maintenu du précédent essai rend expressément les nouvelles dispositions d'emploi applicables nonobstant cette exclusion des règles de mission. La cible hors lot doit être harmonisée : il ne s'agit ni d'importer la garantie de terme dans toute intermission ni d'écarter le préavis ou les salaires de l'emploi. Les anciens CDI conservent leurs garanties ; les seuils d'indemnité restent distincts.")
for n in ['L1251-15', 'L1251-26', 'L1251-29', 'L1251-30']:
    set_check(n, 'L1251-58-3', local[n] + ' ' +
        "La source impose un minimum mensuel au moins égal au SMIC multiplié par les heures de la durée légale hebdomadaire du mois, en tenant compte des rémunérations de mission. Le projet précise la durée légale applicable au contrat et protège les intermissions et droits plus favorables. Le renvoi ne cumule pas deux fois le même salaire et n'en conditionne pas le versement à un an d'ancienneté ; il n'instaure pas un salaire intégral pendant toute suspension. La fin ou la variation de mission ne supprime pas cette garantie ; les droits antérieurs restent à leur champ.")
for n in ['L1251-26', 'L1251-29', 'L1251-30']:
    set_check(n, 'L1251-58-2', local[n] + ' ' +
        "La source et le projet de L. 1251-58-2 assimilent les périodes sans mission au travail effectif pour les congés et l'ancienneté ; l'écrit d'emploi comporte huit rubriques, dont mobilité, essai, minimum mensuel et lettre par mission. Cette assimilation est conservée pour ces objets précis, sans nouveau CDD ou remise à zéro au changement d'utilisateur et sans maintien intégral inventé pour toute suspension. Les informations de mission restent dues ; ni leur transmission sous deux jours ouvrables ni la notification d'une rupture ne résultent d'un seuil d'un an.")

set_check('L1251-16', 'L1251-14',
    "Le 4° de L. 1251-16 vise la durée d'un essai valablement stipulé, non sa création dans chaque lettre. La source de la cible fixe à défaut d'accord deux, trois ou cinq jours selon les seuils d'un et deux mois ; sa vue fournie prévoit un seul essai du nouvel emploi, trois mois au plus, avec durées plus courtes et sans renouvellement. Le présent lot conserve en outre les corrections du précédent essai : fraction du préavis salarié après l'essai en emploi ordinaire, et priorité explicite sur l'exclusion de L. 1251-58-4. L'empreinte est celle de la vue fournie, distincte de la proposition finale de ce lot ; aucun essai ni ancienneté ne recommence à une mission.")
set_check('L1251-16', 'L1251-32',
    "La source ouvre l'indemnité de fin de mission en l'absence de CDI immédiat chez l'utilisateur : 10 % de la rémunération totale brute, ajoutés au salaire, payés avec le dernier salaire de mission et inscrits au bulletin. Le projet conserve ce régime historique mais ne fait pas de la seule fin de mission un fait générateur du nouvel emploi indéterminé, qui garde les garanties d'intermission. Le 3° de L. 1251-16 communique toujours les modalités de cette indemnité quand elle est due, sans les répéter si déjà remises et inchangées ; le seuil d'un an et le plafond de l'indemnité ordinaire ne réduisent aucune créance ancienne ni garantie plus favorable.")
set_check('L1251-16', 'L1251-43',
    "La source comporte les six rubriques : motif et précisions de remplacement, terme, clause de variation, poste/risques/qualification/lieu/horaire, équipements, rémunération de comparaison avec primes et accessoires. La proposition actuelle maintient le motif au 1° mais supprime les justifications précises et le nom/qualification du remplacé ; elle abroge le 3° pour les nouvelles mises à disposition et permet le réemploi d'écrits accessibles. Son 2° conserve l'événement et la durée minimale lorsque la mission peut être sans terme précis, jamais un terme d'emploi. Le 1° local est expressément rectifié pour ne rétablir aucune mention retirée ni pièce de remplacement. Les autres informations utiles sont communiquées au salarié ; anciennes mentions et termes en cours gardent leur transition, sans seuil d'ancienneté ni préavis de rupture pour cette information.")
set_check('L1251-17', 'L1251-16',
    "La source de L. 1251-16 exige l'écrit et sept rubriques ; sa vue fournie supprime plusieurs répétitions et donne un fondement légal direct au rapatriement et à la liberté d'embauche. La proposition de ce lot conserve les dispenses supplémentaires déjà acquises pour qualification et rémunération inchangées, y compris dans les lettres futures des anciens CDI, et coordonne la nouvelle cible L. 1251-43. L'envoi sous deux jours ouvrables de L. 1251-17 porte sur la lettre et les seules informations restant à communiquer, sans nouveau contrat ni second envoi. Le droit d'accès effectif et le recours pour défaut de transmission ne dépendent pas d'un an d'ancienneté.")
set_check('L1251-30', 'L1251-12-1',
    "Le deuxième alinéa de L. 1251-30 ne renvoie au barème de L. 1251-12-1 que dans son champ historique : dix-huit mois, neuf mois dans les deux cas, vingt-quatre mois aux trois cas avec six mois initiaux au seul cas d'exportation, trente-six mois pour l'apprentissage. La proposition fournie abroge ce barème prospectivement en protégeant les anciens termes et dérogations. Les futures missions d'un emploi indéterminé ne reçoivent donc aucun de ces plafonds par ce renvoi ; L. 1251-58-6 les en dispensait déjà. Les durées pédagogiques autonomes, les avantages futurs et le préavis de rupture restent distincts.")
set_check('L1251-31', 'L1251-30',
    "La source de L. 1251-30 encadre les variations par un jour pour cinq jours de travail, deux jours sous dix jours de mission et dix jours de réduction au plus. Sa proposition fournie, conservée dans ce lot, retire ces trois calculs pour les futures missions dans un emploi indéterminé, sans effacer limites conventionnelles, salaire garanti ou consentement aux modifications essentielles. Le surlendemain de L. 1251-31 reste une faculté autonome de passation pour les remplacements concernés ; il ne devient ni un plafond général ni une obligation de clause spéciale. Les anciennes missions gardent leurs règles, sans notification de rupture ou ancienneté minimale à ajouter au report.")

for article in answer:
    source_key = article['code_id'] + '|' + article['source_id']
    for target_key in references['requirements'][source_key]:
        target = references['targets'][target_key]
        assessment = analyses[article['number']][target['number']]
        article['reference_checks'].append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })

assert hashlib.sha256(Path('reference-targets.json').read_bytes()).hexdigest() == reference_digest
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f"answer.json : {len(answer)} articles ; {sum(len(a['reference_checks']) for a in answer)} analyses de renvoi actuelles.")
