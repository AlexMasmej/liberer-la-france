import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
out = []

def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))

def paras(*items):
    return ''.join('<p>' + html.escape(x, quote=False) + '</p>' for x in items)

def effect(kind, measure, description, before, after, unit, population, transition, burdens, sq, pq):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=sq, proposed_quote=pq)

def add(index, proposal, reason, notes, classification, assessment, limits, burdens, effects=(), removed=(), repeal=None, benefit=None):
    s = sources[index]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposal, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposal is None else 'rewrite_draft',
             substantive_impact=dict(version=1, classification=classification, assessment=assessment,
                 scope_limitations=limits, new_burdens_review=burdens, effects=list(effects)))
    if removed:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=list(removed))
    if repeal:
        a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    if benefit:
        a['benefit_review'] = benefit
    out.append(a)
    return a

# R5221-44 : la dispense ne doit pas disparaître avec le contrat de mission.
p = paras(
    "Lorsqu'une entreprise de travail temporaire a vérifié l'existence de l'autorisation de travail dans les conditions prévues à l'article R. 5221-41, cette formalité est réputée remplie, pendant la durée de validité du titre de séjour, pour tous les contrats de mission conclus entre cette entreprise et le travailleur étranger ainsi que pour son emploi à durée indéterminée et ses affectations successives auprès d'entreprises utilisatrices.",
    "Aucune nouvelle vérification au titre de cette formalité n'est exigée du seul fait d'une nouvelle affectation ou d'une conversion convenue en contrat unique à durée indéterminée. Cette dispense ne prolonge ni la validité ni le champ de l'autorisation de travail.",
    "Ces dispositions s'appliquent aux vérifications restant à accomplir à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, y compris au titre d'un contrat antérieur. Les vérifications déjà effectuées conservent leurs effets pendant la durée de validité du titre de séjour. Les contrats de mission conclus avant cette entrée en vigueur conservent leur régime et leurs droits acquis ; aucune nouvelle embauche, aucun renouvellement ni aucune reconduction décidés à compter de cette entrée en vigueur ne peuvent créer un emploi à durée déterminée. La durée d'une affectation ne limite pas celle de l'emploi à durée indéterminée.")
add(0, p,
    "Coordination de fond de la dispense existante avec le contrat unique : elle couvre explicitement l'emploi à durée indéterminée et les affectations, sans nouveau contrôle à chaque mission. La seconde passe conserve la vérification initiale, nécessaire au respect de l'autorisation de travail, et sa limite de validité ; aucune taxe ni autre autorisation n'est supprimée ici. La répétition matérielle « s'est s'assurée » est corrigée.",
    "R. 5221-41, source et note lues dans le corpus : vérification initiale par saisine du préfet ; sa suppression dépasserait cette dispense et supposerait de coordonner L. 5221-8. La dispense reste propre à la même entreprise de travail temporaire et ne couvre pas une activité non autorisée. Le changement de mission ne rompt pas le contrat unique. Les régimes du séjour et du travail irrégulier restent distincts. Aucune coupe supplémentaire de la vérification initiale n'est retenue sans affaiblir le contrôle de régularité.",
    'coordination_only',
    "La source dispensait déjà de répétition pour tous les contrats de mission pendant la validité du titre. La proposition transpose cette même dispense aux affectations du contrat unique ; elle ne démontre pas une seconde suppression autonome de formalité.",
    "Ni la vérification initiale, ni le renouvellement du titre, ni les contrôles autonomes de l'emploi étranger ne sont supprimés. Aucun effet national de coût n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun dépôt, justificatif, registre ou contrôle de remplacement n'est créé, et la vérification existante conserve son champ.",
    [effect('coordination', 'contrat-unique-duree-indeterminee',
        "Maintien de la vérification unique lors du passage des contrats de mission aux affectations d'un emploi sans terme.",
        "Dispense pour tout contrat de mission avec la même entreprise pendant la validité du titre de séjour.",
        "Même dispense pour l'emploi à durée indéterminée, ses affectations et une conversion convenue, sans élargir le titre.",
        'legal_duty', 'Travailleurs étrangers employés par une entreprise de travail temporaire.',
        "Vérifications futures, y compris celles d'anciens contrats ; contrôles déjà accomplis conservés.",
        "Aucune formalité de remplacement ; contrôle initial maintenu.",
        "cette formalité est réputée remplie pour la durée de validité du titre de séjour",
        "Aucune nouvelle vérification au titre de cette formalité n'est exigée du seul fait d'une nouvelle affectation ou d'une conversion convenue en contrat unique à durée indéterminée.")])

# R5312-32 : pas de réécriture stylistique d'une base de traitement nécessaire.
add(1, None,
    "Maintien intégral nécessaire après examen de la source et du brouillon entier : cet article définit les responsables, les personnes concernées et trois finalités limitées d'un échange entre organismes. Il n'impose ni déclaration aux allocataires, ni agrément, ni délai minimal. Supprimer ce fondement sans supprimer les missions correspondantes compromettrait l'identification des droits et des aides ; la réécriture seulement stylistique du brouillon n'est pas reconduite comme simplification.",
    "Les renvois L. 5132-5, L. 5134-23-1 et L. 5134-25-1 servent à identifier des dispositifs, non à imposer des CDD. Les aides et prolongations favorables restent accessibles aux futurs emplois éligibles en contrat unique selon leurs conditions propres, sans transformer leur durée en terme d'emploi. L. 5134-23-1 a été lu intégralement dans le corpus. Les propositions des autres cibles sont distinguées de leur source officielle. R. 5312-33 et suivants restent le cadre distinct des données et garanties ; aucune nouvelle finalité n'est ouverte ici. La seconde occurrence « revenu de solidarité » dans la dénomination source diffère de « revenu de solidarité active » : anomalie préexistante signalée, non corrigée silencieusement. La note du 1er janvier 2025 demeure historique. Les articles L. 262-37 et L. 262-42 du code de l'action sociale et des familles, extérieurs au corpus fourni, ne sont pas réputés relus ou modifiés.",
    'retained_necessary',
    "L'article officiel entier est maintenu : les échanges servent l'identification des allocataires et l'application des missions et aides légales. Aucun doublon déclaratif imposé à l'usager ni prélèvement accessoire n'y est institué ; aucune réduction n'est revendiquée.",
    "Le maintien ne valide pas l'ensemble des traitements de France Travail ni les obligations du code de l'action sociale et des familles. Leurs bases légales et garanties restent à leur champ propre.",
    "Aucune charge nouvelle n'est identifiée puisque le texte source est intégralement conservé, sans extension des destinataires, catégories de personnes ou finalités.")

# D5422-3 : liberté de canal, avec maintien de ses trois alinéas.
p = paras(
    "Les organismes chargés du recouvrement des contributions d'assurance chômage mentionnés à l'article L. 5427-1 peuvent transmettre, à sa demande, à l'employeur ou à son tiers déclarant au sens de l'article L. 133-11 du code de la sécurité sociale, la liste des fins de contrats de travail et de contrats de mise à disposition mentionnés au 1° de l'article L. 1251-1 du présent code, concernant des personnes inscrites sur la liste des demandeurs d'emploi prévue à l'article L. 5411-1. Seules sont transmises les fins de contrat imputables à cet employeur dans les conditions fixées par les accords mentionnés à l'article L. 5422-20.",
    "Ces organismes mettent à disposition un téléservice permettant le dépôt et le traitement des demandes de communication de ces données. L'employeur ou son tiers déclarant choisit librement entre ce téléservice et tout autre moyen de demande.",
    "Le recours à un autre moyen n'est subordonné ni à l'impossibilité d'utiliser le téléservice, ni à une déclaration ou à un justificatif de cette impossibilité.",
    "Cette liberté de choix s'applique aux demandes présentées ou en cours à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, sans renouvellement des demandes déjà reçues. Pour un emploi relevant du contrat unique, la seule fin d'une affectation ou d'une période de formation ne constitue pas une fin de contrat de travail. Les contrats de mise à disposition mentionnés au 1° de l'article L. 1251-1 conservent leur nature distincte : leur fin reste prise en compte dans les seules conditions d'imputabilité qui leur sont applicables.")
add(2, p,
    "Réforme de fond maintenue : suppression du canal électronique obligatoire et de la condition d'impossibilité pour utiliser un autre moyen. La seconde passe précise que cette dispense retire également la déclaration de cette impossibilité, sans supprimer le téléservice utile. Le périmètre des données demeure inchangé. La coordination distingue désormais expressément la fin de l'emploi et la fin du contrat commercial de mise à disposition : le contrat unique ne supprime pas ce second événement.",
    "L. 1251-1, 1°, vise le contrat entre l'entreprise de travail temporaire et l'utilisateur, non le contrat de travail du 2°. Son imputabilité ne peut être effacée au motif que l'emploi continue. L. 5422-20 et les accords de modulation doivent rester coordonnés avec ces deux catégories ; leur contenu n'est pas remplacé ici. Le tiers déclarant demeure celui de L. 133-11 CSS. La note relative à l'article 2 du décret n° 2023-635 reste une transition ancienne, non une date de la réforme. Aucune nouvelle donnée personnelle ni droit d'accès hors des fins imputables à l'employeur n'est créé.",
    'material_reduction',
    "Par rapport à la source entière, le demandeur n'a plus à utiliser obligatoirement le téléservice ni à indiquer qu'il ne peut l'utiliser pour choisir un autre canal. Le droit de communication et son périmètre ne sont pas supprimés ; aucune baisse des contributions chômage n'est déduite de cet allègement.",
    "La modulation des contributions et l'imputabilité des fins de mise à disposition restent régies par leurs accords et textes propres ; aucun gain de taux, de délai ou de recettes n'est établi.",
    "Aucune charge nouvelle n'est identifiée : le téléservice existe déjà et l'alternative devient libre, sans attestation supplémentaire ni nouveau fichier ou destinataire.",
    [effect('obligation_removed', 'assurance-chomage-acces-donnees-canal-libre',
        "Suppression de l'exclusivité du téléservice et de la déclaration préalable d'impossibilité.",
        "Demande dématérialisée obligatoire ; autre canal permis après indication d'une impossibilité d'utiliser le téléservice.",
        "Choix libre du téléservice ou de tout autre moyen, sans déclaration ni justificatif d'impossibilité.",
        'legal_duty', "Employeurs et tiers déclarants demandant les fins de contrat qui leur sont imputables.",
        "Demandes futures et en cours à l'entrée en vigueur, sans nouveau dépôt des demandes reçues.",
        "Téléservice existant conservé ; aucun canal ou justificatif imposé en remplacement.",
        "L'employeur ou son tiers déclarant adresse, par voie dématérialisée, sa demande au moyen de ce téléservice.",
        "Le recours à un autre moyen n'est subordonné ni à l'impossibilité d'utiliser le téléservice, ni à une déclaration ou à un justificatif de cette impossibilité.")],
    ["Exclusivité du téléservice pour les demandes de communication des fins de contrats imputables à l'employeur.",
     "Condition et indication préalable d'une impossibilité d'utiliser le téléservice pour choisir un autre canal."])

# D5424-22 : la protection contre le licenciement pendant l'inactivité subsiste.
add(3, None,
    "Maintien intégral nécessaire : l'interdiction protège le revenu et l'emploi pendant l'inactivité du chantier, sans imposer de déclaration ou d'autorisation nouvelle. Les exceptions de faute grave, d'arrêt par le maître d'œuvre en travaux publics et de préavis déjà donné évitent une interdiction absolue. Les retirer aggraverait la contrainte ; supprimer la protection transférerait le risque d'inactivité au salarié. Les précisions du brouillon découlent des règles générales du contrat unique et n'exigent pas de reformulation de cet article autonome.",
    "Le préavis individuel de quinze jours ne permet pas de notifier librement un licenciement interdit pendant cette période. Un préavis donné avant le début de l'inactivité peut expirer pendant celle-ci. Le champ particulier de l'arrêt décidé par le maître d'œuvre reste limité aux travaux publics. La fin d'un chantier ne termine pas automatiquement un nouvel emploi, par application de L. 1221-2 proposé. Les contrats antérieurs gardent leurs droits, et les autorisations de salariés protégés, procédures collectives et indemnisations d'intempéries ne sont pas supprimées. Aucune réduction additionnelle compatible avec cette protection essentielle n'est identifiée.",
    'retained_necessary',
    "L'article officiel entier est conservé, avec ses deux exceptions de fond et le préavis donné antérieurement. La protection pendant l'inactivité n'est ni un doublon déclaratif ni une taxe ; aucune baisse de charge n'est revendiquée.",
    "L'indemnisation des intempéries et les conditions générales du licenciement restent hors du changement ; l'effet global des réformes de rupture n'est pas chiffré ici.",
    "Aucune charge nouvelle n'est identifiée : maintien exact de la source, sans registre, déclaration, délai ou condition supplémentaire.")

# D5522-11 : abrogation de la reprise intégrale des aides pour les ruptures futures.
p = sources[4]['previous_draft']['proposed_xml']
add(4, p,
    "Abrogation de fond maintenue après seconde passe : le remboursement intégral d'une aide légalement versée pour des périodes réellement éligibles n'est plus déclenché par la seule rupture patronale anticipée. Il n'y a plus d'autre obligation autonome à supprimer dans cet article après cette abrogation. Les cinq dispenses restent protégées pour les ruptures anciennes ; pour les ruptures futures elles deviennent sans objet parce que la charge correspondante disparaît entièrement, sans récupération équivalente.",
    "D. 5522-7 a été lu intégralement : trois années consécutives d'aide et abattement de 50 % la troisième année ; ces paramètres ne sont pas modifiés. Les conditions d'accès et les aides restent ouvertes aux futurs emplois éligibles en contrat unique. La notification est retenue comme critère transitoire pour éviter de faire varier le régime avec la durée du préavis. Les conventions et décisions de récupération doivent être coordonnées : aucun simple rappel du présent article ne peut rétablir la reprise supprimée. La récupération d'un indu ou d'une fraude sur un fondement autonome demeure possible, sans aide nouvelle après cessation de l'emploi.",
    'material_reduction',
    "La source imposait le reversement de toute l'aide à certaines ruptures patronales avant la fin de la période aidée. Cette obligation disparaît pour toutes les ruptures nouvellement notifiées, y compris lorsque l'emploi a commencé avant la réforme ; les dettes issues de notifications anciennes restent possibles avec toutes leurs dispenses.",
    "Ce n'est ni une abolition des règles d'éligibilité, ni un droit à une aide après la fin de l'emploi, ni un remboursement général des reprises anciennes. L'effet budgétaire n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : aucun contrôle préalable ou formulaire ne remplace le reversement. Les contrôles autonomes des indus et de la fraude demeurent existants.",
    [effect('obligation_removed', 'aide-emploi-outre-mer-fin-reprise-integrale',
        "Suppression du reversement intégral déclenché par la seule rupture patronale avant la fin de la période aidée.",
        "Reversement de l'intégralité de l'aide en cas de rupture patronale avant la fin de la période D. 5522-7, hors cinq dispenses.",
        "Aucun reversement sur le seul fondement de D. 5522-11 pour les ruptures nouvellement notifiées ; indus autonomes réservés.",
        'legal_duty', "Employeurs bénéficiant de l'aide régie par D. 5522-7 et rompant un emploi aidé.",
        "Notifications à compter de l'entrée en vigueur ; notifications antérieures, dispenses, créances, restitutions et recours conservés.",
        "Aucune récupération équivalente ni déclaration nouvelle ; contrôle des indus sur un fondement distinct.",
        "le montant de l'aide est intégralement reversé par l'employeur à l'Etat.",
        "La rupture à l'initiative de l'employeur avant la fin de la période mentionnée à l'article D. 5522-7 n'entraîne plus, sur le fondement du présent article, le reversement intégral de l'aide à l'État.")],
    repeal="Suppression, pour les ruptures notifiées dès l'entrée en vigueur, de l'obligation de reverser intégralement l'aide à l'emploi du seul fait d'une rupture patronale avant la fin de la période aidée.")

# D6123-37 : catégories intégrales conservées, sauf les retraits explicitement décrits.
p = sources[5]['previous_draft']['proposed_xml'].replace('<br/>', '<br>')
p = p.replace("<br>- Nom commercial ;", '')
p = p.replace("À compter de cette entrée en vigueur, les transmissions", "À compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, les transmissions")
p = p.replace("Les données relatives aux rémunérations afférentes aux périodes d'emploi antérieures ne sont transmises que", "Les données relatives à cette contribution pour les rémunérations afférentes aux périodes d'emploi antérieures ne sont transmises que")
p = p.replace("de la contribution supplémentaire à l'apprentissage,", "de la contribution supplémentaire à l'apprentissage pour les seules années civiles antérieures au 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression,")
p = p.replace("Les déductions, exonérations et autres avantages relatifs aux contributions maintenues restent applicables.</p>",
    "Aucune assiette, aucun montant ni état néant de contribution supplémentaire à l'apprentissage n'est transmis pour les années civiles commençant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression. Les informations nécessaires aux liquidations, régularisations, exonérations, restitutions, contrôles et recours des années antérieures restent transmises selon leurs conditions propres. Les données nécessaires à la créance imputable sur le solde de la taxe d'apprentissage et à l'aide au recrutement maintenues à l'article L. 6242-1 restent transmises pour les situations éligibles, y compris futures ; elles ne rétablissent pas une déclaration de la contribution supprimée. Le nom commercial de l'établissement n'est plus transmis au titre du présent article. Les déductions, exonérations et autres avantages relatifs aux contributions maintenues restent applicables.</p>")
add(5, p,
    "Les subdivisions I, II, 1°, 2°, a) et b) et toutes les catégories utiles demeurent. Sont maintenus les retraits du circuit d'enquêtes de satisfaction et du reporting CPF-CDD sur les périodes futures. La seconde passe retire en plus le nom commercial, redondant avec les identifiants et la raison sociale, et coordonne le reporting agrégé de contribution supplémentaire à l'apprentissage avec sa suppression déjà proposée à L. 6131-1, 3°. Le réemploi de données accessibles n'est pas compté comme un nouveau gain CRPA. Ni la suppression de taxe ni les droits à aide ne résultent de ce seul article de transmission.",
    "L. 6131-1, I, 4°, cible le CPF-CDD : extinction pour périodes de travail à compter de l'entrée en vigueur, y compris les anciens CDD poursuivis. Son 3° vise une autre contribution, supprimée à partir du 1er janvier de l'année suivante ; ne pas aligner ces deux calendriers. La créance et l'aide autonomes de L. 6242-1 ne doivent perdre aucune donnée nécessaire à leurs futurs bénéficiaires. Son 5° vise des contributions conventionnelles distinctes, conservées. Les enquêtes de L. 6123-5, 14°, ne sont pas abrogées par le retrait de ce circuit ; elles ne doivent pas rétablir le même transfert par simple renvoi. R. 6123-34 lu, sans nouvelle collecte créée ici. Le renvoi préexistant à L. 6323-20-1 est incohérent en tant que source de cotisation : cet article, lu entier, règle le CPF de salariés de personnes publiques. Il demeure signalé, sans assiette nouvelle inventée ; une concordance législative expresse est nécessaire. Les rubriques DSN et textes de recouvrement restent à coordonner hors de cet article. Les données BOETH, alternants, intermittents, montants et déductions maintenus ne sont pas supprimés par la seule réduction des recettes.",
    'material_reduction',
    "La transmission obligatoire pour les enquêtes de satisfaction et la donnée de nom commercial sont réellement retirées par rapport à la source officielle entière. Les retraits de données CPF-CDD et de contribution supplémentaire à l'apprentissage sont des coordinations de suppressions décidées dans leurs articles d'assiette, sans compter ici une nouvelle baisse de prélèvement.",
    "Les autres catégories, les anciennes périodes et années, les données nécessaires aux crédits et aides futurs et les contributions distinctes restent couvertes. Les missions d'enquête légales subsistent. Le coût net des systèmes d'information n'est pas chiffré.",
    "Aucune charge nouvelle de déclaration ou de données n'est identifiée : catégories diminuées, circuit existant maintenu et pas d'accès nouveau. Les adaptations informatiques de transition restent à mesurer ; le réemploi prévu ne prouve pas un gain supplémentaire au CRPA.",
    [effect('obligation_removed', 'formation-transmissions-enquetes-satisfaction',
        "Retrait de la finalité obligatoire de transmission pour les enquêtes de satisfaction, sans abolir les enquêtes légales elles-mêmes.",
        "Le circuit de transmission I inclut la réalisation des enquêtes de satisfaction du 14° de L. 6123-5.",
        "Le 3° est abrogé ; les finalités 1°, 2°, 4° et 5° demeurent.",
        'legal_duty', "Organismes de recouvrement, France compétences et opérateurs de compétences.",
        "Transmissions à compter de l'entrée en vigueur ; aucun transfert de rattrapage sur le seul fondement abrogé.",
        "Pas d'enquête ou de déclaration nouvelle créée en remplacement de ce circuit.",
        "La réalisation des enquêtes de satisfaction mentionnées au 14° de l'article. L. 6123-5",
        "3° Abrogé à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail ;"),
     effect('obligation_removed', 'formation-transmissions-retrait-nom-commercial',
        "Suppression d'une donnée descriptive redondante dans les deux destinations du même circuit.",
        "Nom commercial de l'établissement transmis à France compétences et aux opérateurs, en plus des identifiants et de la raison sociale.",
        "Nom commercial retiré des deux listes ; identification par les données restantes inchangée.",
        'legal_duty', "Organismes transmetteurs et établissements identifiés dans ce circuit.",
        "Transmissions à compter de l'entrée en vigueur, sans effacer les droits fondés sur les anciennes données.",
        "Aucune donnée de remplacement et aucun formulaire nouveau.",
        "-Nom commercial ;", "Le nom commercial de l'établissement n'est plus transmis au titre du présent article."),
     effect('coordination', 'cpf-cdd-suppression-contribution',
        "Retrait des rubriques CPF-CDD futures en coordination de la suppression du prélèvement de 1 % à son fondement propre.",
        "Transmission de la masse salariale et du montant CPF-CDD sans limitation aux périodes anciennes.",
        "Transmission seulement pour les périodes d'emploi antérieures ; aucune donnée d'assiette, montant ou état néant pour les périodes nouvelles.",
        'legal_duty', "Employeurs auparavant redevables du CPF-CDD et organismes du circuit de formation.",
        "Date de la période de travail, y compris anciens CDD poursuivis ; régularisations et recours anciens conservés.",
        "Aucune contribution ou déclaration équivalente ; droits CPF et avantages distincts préservés.",
        "-Masse salariale assujettie à la contribution au compte personnel de formation des contrats à durée déterminée ;",
        "Aucune assiette, aucun montant ni état néant de contribution au compte personnel de formation des contrats à durée déterminée n'est demandé pour les rémunérations afférentes aux périodes d'emploi courant à compter de cette entrée en vigueur, y compris au titre d'un contrat antérieur."),
     effect('coordination', 'contribution-supplementaire-apprentissage-suppression',
        "Retrait prospectif de la donnée de contribution supplémentaire à l'apprentissage, distincte du CPF-CDD.",
        "Le montant déclaré des contributions inclut la contribution supplémentaire à l'apprentissage sans borne d'année.",
        "Ce montant est limité aux anciennes années ; les créances et aides favorables autonomes gardent leurs données nécessaires.",
        'legal_duty', "Organismes du circuit et employeurs concernés par la contribution supplémentaire à l'apprentissage.",
        "Années commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi de suppression ; années antérieures protégées.",
        "Aucun reporting de taxe supprimée ni recette de remplacement ; données des aides maintenues sans élargissement de catégorie.",
        "contribution supplémentaire à l'apprentissage",
        "Aucune assiette, aucun montant ni état néant de contribution supplémentaire à l'apprentissage n'est transmis pour les années civiles commençant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression.")],
    ["Transmission obligatoire de données dans ce circuit pour la réalisation des enquêtes de satisfaction du 14° de L. 6123-5.",
     "Transmission du nom commercial de chaque établissement à France compétences et aux opérateurs de compétences, sans donnée de remplacement.",
     "Transmission des assiettes, montants et états néants CPF-CDD relatifs aux périodes d'emploi nouvelles après suppression de la contribution.",
     "Transmission des montants ou états de contribution supplémentaire à l'apprentissage pour les années nouvelles où elle est supprimée, hors données utiles aux aides et créances autonomes maintenues."])

# D6222-1 : supprimer les deux barrières réglementaires, conserver les cas légaux.
p = paras(
    "Les dérogations à la limite d'âge supérieure prévues à l'article L. 6222-2 s'appliquent dans les conditions suivantes :",
    "1° Pour les dérogations prévues aux 1° et 2° de cet article, aucune limite d'âge supérieure supplémentaire n'est exigée ;",
    "2° Pour ces mêmes dérogations, aucun délai maximal entre le précédent apprentissage et le nouvel apprentissage n'est exigé ;",
    "3° Pour la dérogation prévue au 2° du même article, les causes de rupture indépendantes de la volonté de l'apprenti sont les suivantes :",
    "a) La cessation d'activité de l'employeur ;",
    "b) La faute de l'employeur ou ses manquements répétés à ses obligations ;",
    "c) La mise en œuvre de la procédure de suspension de l'exécution du contrat d'apprentissage prévue aux articles L. 6225-4 et suivants ;",
    "4° La dérogation prévue au 2° de l'article L. 6222-2 s'applique également en cas d'inaptitude physique et temporaire de l'apprenti constatée dans les conditions prévues à l'article L. 6222-18.",
    "La suppression de la limite de trente-cinq ans et du délai maximal d'un an s'applique aux admissions examinées à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, y compris à la suite d'un apprentissage antérieur et dans une relation d'emploi en cours. Les admissions déjà acquises et les droits des contrats antérieurs sont conservés, sans réouverture générale des refus devenus définitifs.",
    "Pour les emplois relevant du contrat unique à durée indéterminée, les dérogations portent sur l'accès à une nouvelle période d'apprentissage ; la durée de cette période ne limite pas celle de l'emploi. Les conditions de fond des 1° et 2° de l'article L. 6222-2 demeurent applicables. Les dérogations prévues aux 3°, 4° et 5° du même article restent ouvertes aux situations éligibles futures et antérieures sans condition d'âge supplémentaire ni de délai créée par le présent article.")
add(6, p,
    "Réduction de fond renforcée : le délai maximal d'un an, déjà retiré dans le brouillon, et le plafond réglementaire de trente-cinq ans sont tous deux supprimés. Le plafond ajouté aux deux dérogations légales ne protège ni la qualité pédagogique ni la sécurité ; les conditions légales de qualification supérieure et de rupture indépendante de la volonté restent applicables. Les causes a), b), c), l'inaptitude temporaire et les dérogations distinctes sont conservées. L'emploi nouveau demeure sans terme.",
    "L. 6222-2 lu intégralement : le principe légal de vingt-neuf ans connaît notamment les cinq dérogations rappelées ; la suppression du plafond réglementaire de trente-cinq ans n'abolit pas le principe pour les personnes hors dérogation. Le 4° elliptique de D. 6222-1 est rattaché expressément au 2° légal, sans créer de constat médical supplémentaire. La référence L. 6222-18 vise la constatation dans son régime applicable, non un retour aux quarante-cinq jours pratiques pour les nouveaux emplois. Coordonner les formulaires et décisions d'admission pour retirer les contrôles des deux conditions supprimées ; aucune attestation de remplacement. La note du décret de 2020 demeure historique. Les âges et conditions des dispositifs de financement distincts ne sont pas implicitement supprimés par cet accès élargi à l'apprentissage ; leur coordination et leur coût restent à examiner.",
    'material_reduction',
    "Par rapport à la source entière, les personnes des deux premiers cas de L. 6222-2 ne perdent plus la dérogation à trente-six ans ou après une interruption de plus d'un an. L'accès est élargi sans nouveau seuil inventé ; les cas légaux et garanties médicales restent en place.",
    "La limite légale générale de vingt-neuf ans hors dérogation reste intacte. Les aides soumises à des conditions autonomes ne deviennent pas universelles. Aucun coût de formation ou solde budgétaire n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : deux conditions d'admission sont retirées sans déclaration, agrément ou justificatif substitutif ; les conditions légales existantes demeurent.",
    [effect('relief_extended', 'apprentissage-derogations-age-sans-plafond-reglementaire',
        "Suppression de la borne réglementaire de trente-cinq ans dans les deux premières dérogations légales.",
        "Apprenti âgé de trente-cinq ans au plus à la conclusion pour les cas 1° et 2° de L. 6222-2.",
        "Aucun plafond réglementaire supplémentaire dans ces deux cas ; les conditions légales de chaque cas subsistent.",
        'other', "Personnes poursuivant une qualification supérieure ou reprenant après rupture indépendante de leur volonté ou inaptitude temporaire.",
        "Admissions examinées dès l'entrée en vigueur, y compris en emploi et après apprentissage ancien ; droits acquis protégés.",
        "Aucune attestation ni limite d'âge de remplacement.",
        "l'âge de l'apprenti au moment de la conclusion du contrat est de trente-cinq ans au plus",
        "1° Pour les dérogations prévues aux 1° et 2° de cet article, aucune limite d'âge supérieure supplémentaire n'est exigée ;"),
     effect('relief_extended', 'apprentissage-reprise-sans-delai-maximal',
        "Suppression de la forclusion d'un an entre deux apprentissages dérogatoires.",
        "Nouvel apprentissage à souscrire au plus tard un an après l'expiration du précédent contrat pour les cas 1° et 2°.",
        "Aucun délai maximal d'interruption pour ces deux dérogations ; conditions légales propres conservées.",
        'other', "Bénéficiaires des 1° et 2° de L. 6222-2 reprenant un apprentissage.",
        "Admissions examinées dès l'entrée en vigueur, même après un apprentissage ancien ; pas de réouverture des refus définitifs.",
        "Aucun dossier de dérogation supplémentaire ni nouvel agrément.",
        "le contrat d'apprentissage doit être souscrit dans un délai maximum d'un an après l'expiration du précédent contrat",
        "2° Pour ces mêmes dérogations, aucun délai maximal entre le précédent apprentissage et le nouvel apprentissage n'est exigé ;")],
    ["Plafond réglementaire de trente-cinq ans applicable aux deux premières dérogations légales à la limite d'âge supérieure.",
     "Délai maximal d'un an après le précédent contrat pour accéder aux deux premières dérogations légales d'apprentissage."],
    benefit="Les deux avantages des 1° et 2° de L. 6222-2 demeurent ouverts aux futurs candidats et sont élargis par retrait du plafond de trente-cinq ans et de l'interruption maximale d'un an. La qualification supérieure, les causes a), b), c) de rupture subie et l'inaptitude physique temporaire conservent leur portée. Les avantages distincts du handicap, du projet de création ou reprise d'entreprise et du sport de haut niveau ne reçoivent aucun plafond nouveau. Les admissions acquises sont préservées ; la durée pédagogique ne termine pas l'emploi. Les aides et exonérations ayant leurs conditions autonomes ne sont ni supprimées ni réputées automatiquement étendues à tous les nouveaux âges.")

# R6222-6 : support commun, mais respect de l'annexe exigée par la loi cible.
p = paras(
    "La durée du contrat d'apprentissage conclu avant l'entrée en vigueur de la loi instituant le contrat de travail unique, ou celle de la période d'apprentissage, peut être réduite ou allongée par la convention prévue au troisième alinéa de l'article L. 6222-7-1, après évaluation par le centre de formation d'apprentis du niveau initial de compétences de l'apprenti ou de ses compétences acquises.",
    "Sous réserve des prolongations et dérogations prévues aux articles L. 6222-11, L. 6222-12-1, R. 6222-9 et R. 6222-23-1 ainsi que des aménagements visés au 2° de l'article L. 6222-37 et au 1° de l'article L. 6222-40, la durée ainsi fixée ne peut être inférieure à six mois ni supérieure à trois ans.",
    "Lorsque le centre de formation d'apprentis est interne à l'entreprise, la convention est signée par l'employeur et par l'apprenti ou son représentant légal.",
    "Pour les conventions conclues ou modifiées à compter de cette entrée en vigueur, l'accord sur l'aménagement peut figurer dans un document de formation commun, dès lors que le centre de formation, l'employeur et l'apprenti ou son représentant légal l'ont signé, sous réserve du troisième alinéa du présent article. La partie de ce document qui fixe l'aménagement constitue la convention et est annexée au contrat d'apprentissage conformément à l'article L. 6222-7-1. Aucun acte autonome ni aucune répétition des signatures déjà apposées pour cet accord ne sont exigés. Les conventions antérieures restent valables sans être refaites. Les évaluations déjà réalisées sont utilisées si elles permettent d'apprécier les compétences pertinentes à la date de l'aménagement ; une nouvelle évaluation n'est pas exigée du seul fait du changement de support.",
    "Pour les nouveaux emplois en contrat unique à durée indéterminée, seul l'aménagement de la période d'apprentissage peut être convenu. Ni son expiration ni la fin du document de formation ne rompent le contrat de travail.")
add(7, p,
    "Coordination du support commun avec la suppression du modèle obligatoire de R. 6222-7 : l'accord et l'évaluation pédagogiques restent requis, sans répétition des éléments acceptés du seul fait du support. La seconde passe rectifie la portée du brouillon : la loi cible exige toujours une convention annexée, donc la partie utile du support commun reste annexée. La source de R. 6222-6 n'impose pas elle-même un second acte en plus d'un support déjà signé ; aucune obligation autonome supplémentaire n'est donc comptée comme supprimée ici. La borne de six mois à trois ans et les exceptions favorables sont conservées. Le renvoi devenu inexact au dernier alinéa est remplacé par le troisième.",
    "L. 6222-7-1, source et proposition lues : son troisième alinéa, et non le dernier alinéa de sa proposition augmentée d'une transition, impose l'accord tripartite et l'annexe au contrat. Le support intégré respecte ces exigences ; supprimer aussi l'annexe demanderait une modification législative distincte qui n'est pas prétendue acquise ici. Aucun nouveau renvoi à L. 6353-1 n'est introduit. Les articles L. 6222-11 et L. 6222-12-1 ont été lus dans le corpus : prolongation d'un an au plus après échec et prise en compte des mois avant l'embauche conservent leur champ. R. 6222-23-1 préserve aussi les minima et la dispense après rupture. Les aménagements handicap et sport ne sont pas enfermés dans la borne générale. La fin pédagogique ne déclenche pas un nouvel essai ni une fin d'emploi. La dispense de R. 6222-9 prime l'exigence de convention. Aucune coupe supplémentaire des compétences évaluées ou des accords n'est retenue, car ils fondent la validité de l'aménagement.",
    'coordination_only',
    "La source prescrit une convention après évaluation, sans démontrer qu'un deuxième acte est toujours nécessaire. La proposition précise l'usage d'un support commun après suppression du modèle de R. 6222-7, tout en gardant l'annexe légale. Ce raccordement n'est pas compté comme une seconde réduction documentaire démontrée ; bornes et consentements demeurent.",
    "La disparition de l'annexe et du consentement tripartite n'est pas revendiquée. Les dispenses et prolongations spéciales restent applicables. Le nombre d'actes ou évaluations effectivement évités n'est pas établi ; aucun gain national n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : le support commun est facultatif, les signataires sont ceux déjà requis et l'annexe découle de la loi existante. Aucun nouveau registre, certificat ou agrément n'est ajouté.",
    [effect('coordination', 'apprentissage-modele-convention-facultatif',
        "Précision du support commun après retrait du modèle obligatoire, sans compter une deuxième suppression autonome.",
        "Convention d'aménagement signée et annexée selon L. 6222-7-1 ; pas de faculté expresse de support commun dans R. 6222-6.",
        "Support commun admis ; seule sa partie d'aménagement vaut convention annexée ; pas d'acte autonome ni de nouvelle signature des éléments acceptés.",
        'legal_duty', "Apprentis, représentants légaux, employeurs et centres de formation aménageant la durée pédagogique.",
        "Conventions nouvelles ou modifiées dès l'entrée en vigueur ; conventions antérieures valables sans reprise ; dispenses spéciales maintenues.",
        "Accord existant, évaluation pertinente et annexe conservés ; support intégré facultatif, sans nouveau modèle ni gain distinct démontré.",
        "La durée du contrat ou de la période d'apprentissage peut être réduite ou allongée par la convention prévue au dernier aliéna de l'article L. 6222-7-1",
        "Aucun acte autonome ni aucune répétition des signatures déjà apposées pour cet accord ne sont exigés.")])

# R6222-7 : modèle ministériel obligatoire abrogé.
p = sources[8]['previous_draft']['proposed_xml']
add(8, p,
    "Abrogation de fond maintenue : suppression de l'habilitation au modèle ministériel obligatoire. Après seconde passe, l'article ne comporte aucune autre norme autonome à retirer ; l'accord, l'évaluation, l'annexe légale et les conditions de financement restent à leurs textes propres. Le libre choix du support ne crée pas une déclaration équivalente et conserve les modèles comme outils volontaires.",
    "L. 6222-7-1 vise au troisième alinéa l'accord signé et l'annexe ; ce sont des exigences de fond et de preuve conservées, distinctes du modèle réglementaire supprimé. Son dernier alinéa proposé est transitoire, donc le renvoi ancien au dernier alinéa ne doit pas être reproduit. R. 6222-6 et R. 6222-9 sont coordonnés dans ce lot. L'arrêté d'application de R. 6222-7 et les circuits D. 6224-1 et D. 6275-1 doivent perdre toute exigence de modèle ; leur réécriture n'est pas réputée effectuée ici. Aucune absence de modèle ne peut fermer un dépôt ou financement si les conditions maintenues sont réunies, pour les situations futures aussi.",
    'material_reduction',
    "La norme officielle entière habilitait le ministre à déterminer le modèle de convention. La proposition retire son caractère obligatoire pour toutes les conventions nouvelles ou modifiées, sans refaire les anciennes. Aucun gain additionnel n'est attribué au seul renvoi de R. 6222-6.",
    "Le modèle externe n'est pas reproduit ni prétendu réécrit. L'accord pédagogique et l'annexe imposés par L. 6222-7-1 subsistent ; le coût net des circuits n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : aucun formulaire ou déclaration de remplacement, maintien volontaire du modèle existant et pas de reprise des conventions anciennes.",
    [effect('obligation_removed', 'apprentissage-modele-convention-facultatif',
        "Fin du modèle ministériel obligatoire de convention d'aménagement pédagogique.",
        "Modèle déterminé par arrêté pour la convention tripartite de L. 6222-7-1.",
        "Modèle facultatif ; son absence ne ferme pas dépôt ou prise en charge lorsque les conditions de fond et accords sont satisfaits.",
        'legal_duty', "Apprentis, employeurs, CFA et organismes de dépôt et de prise en charge.",
        "Conventions nouvelles ou modifiées dès l'entrée en vigueur ; conventions antérieures maintenues sans les refaire.",
        "Aucune déclaration équivalente ; convention de fond et annexe légale conservées.",
        "Un arrêté du ministre chargé de la formation professionnelle détermine le modèle de la convention tripartite",
        "Aucun modèle fixé par arrêté n'est obligatoire pour la convention d'aménagement de la période d'apprentissage prévue à l'article L. 6222-7-1.")],
    repeal="Suppression prospective de l'habilitation réglementaire imposant un modèle ministériel pour la convention d'aménagement, sans suppression des accords, garanties pédagogiques et annexes légales.")

# R6222-8 et 9 : corrections nécessaires de renvoi, pas de fausse coupe.
p = sources[9]['previous_draft']['proposed_xml']
add(9, p,
    "Coordination nécessaire, sans nouvelle réduction : le renvoi vise le troisième alinéa de L. 6222-7-1 et non son dernier alinéa devenu transitoire dans la proposition. La réserve d'inscription au diplôme est maintenue car elle assure que l'aménagement pédagogique conserve l'accès réel à la certification. Les obligations du certificateur ne sont ni étendues ni transformées en agrément de l'embauche. Aucune coupe supplémentaire justifiée n'est identifiée dans cette unique réserve.",
    "Le contenu officiel et la proposition de L. 6222-7-1 ont été confrontés : accord au troisième alinéa, transition ajoutée ensuite. Les contraintes d'inscription autonomes ne sont pas abolies par le modèle facultatif de R. 6222-7. Elles portent sur la qualification et non la durée de l'emploi. Les inscriptions anciennes et les futures situations recevables restent couvertes. Ni l'article ni son renvoi n'imposent de préavis ou d'indemnité ordinaire ; leurs régimes restent distincts.",
    'coordination_only',
    "La réserve officielle de respect des obligations d'inscription est conservée. Seuls le renvoi et l'articulation avec la phase d'apprentissage du contrat unique sont explicités ; aucune seconde suppression de formulaire ou de certification n'est comptée.",
    "Les obligations détaillées des certificateurs ne figurent pas dans cette source et ne sont pas réputées auditées. Les conditions de fond d'inscription ne sont pas retirées.",
    "Aucune charge nouvelle n'est identifiée : même réserve d'inscription et aucun document, contrôle, délai ou destinataire ajouté par la coordination.",
    [effect('coordination', 'contrat-unique-duree-indeterminee',
        "Rattachement de la réserve de certification à la phase pédagogique sans terme d'emploi.",
        "Réserve d'inscription visant la convention du dernier alinéa de L. 6222-7-1 officiel.",
        "Réserve visant le troisième alinéa pertinent et la qualification préparée, sans terme d'emploi.",
        'legal_duty', "Apprentis et parties à une convention d'aménagement pédagogique.",
        "Nouveaux contrats uniques dès l'entrée en vigueur ; conventions et inscriptions antérieures préservées.",
        "Aucune obligation de certification supplémentaire ni formalité remplaçant le modèle.",
        "sans préjudice du respect des obligations fixées par l'organisme certificateur",
        "ces obligations concernent la qualification préparée pendant la période d'apprentissage. Elles ne fixent pas la durée du contrat de travail.")])

p = sources[10]['previous_draft']['proposed_xml']
add(10, p,
    "Coordination de la dispense favorable avec le troisième alinéa de L. 6222-7-1 et avec le contrat unique. Les quatre champs et leurs conditions propres restent entièrement ouverts. Le second examen ne retire pas cette exonération de convention et ne fabrique pas une coupe supplémentaire : supprimer la dispense alourdirait les bénéficiaires, tandis que les cas généraux hors dispense reposent sur un accord pédagogique maintenu.",
    "L. 6222-11 et L. 6222-12-1 ont été lus intégralement dans le corpus : échec au diplôme avec prolongation d'un an au plus, et formation avant embauche de trois mois au plus avec réduction des mois écoulés. Les sources et propositions L. 6222-37, 2°, et L. 6222-40, 1°, visent les aménagements de durée pour handicap et sport de haut niveau. Ces renvois ne couvrent pas indistinctement toutes les obligations de ces régimes. La dispense s'applique au support autonome ou intégré, sans attestation substitutive. Le renvoi au dernier alinéa est rectifié car la proposition de L. 6222-7-1 ajoute un alinéa transitoire après son troisième alinéa de fond.",
    'coordination_only',
    "La source officielle dispensait déjà de convention dans les quatre situations visées. La proposition conserve ce bénéfice, corrige le rang de l'alinéa cible et le rend expressément applicable aux périodes pédagogiques des futurs contrats uniques ; aucune nouvelle obligation supprimée n'est revendiquée.",
    "Les durées spéciales, conditions de handicap ou de sport, et règles de formation avant embauche restent dans leurs textes propres. Aucun accès inconditionnel à toutes les aides n'est créé.",
    "Aucune charge nouvelle n'est identifiée : la dispense existante couvre les supports intégrés et aucun justificatif ou déclaration équivalente ne lui est substitué.",
    [effect('coordination', 'contrat-unique-duree-indeterminee',
        "Conservation de la dispense de convention malgré le changement de support contractuel.",
        "Dispense pour les cas L. 6222-11, L. 6222-12-1, L. 6222-37, 2°, et L. 6222-40, 1°.",
        "Même dispense et mêmes champs pour anciens contrats et futures périodes du contrat unique, sans déclaration équivalente.",
        'legal_duty', "Apprentis en prolongation après échec, formation avant embauche, handicap ou sport de haut niveau selon les textes visés.",
        "Situations antérieures préservées et futurs contrats uniques couverts dès l'entrée en vigueur.",
        "Aucun formulaire de remplacement ni nouveau contrôle.",
        "La conclusion de la convention tripartite prévue au dernier alinéa de l'article L. 6222-7-1 n'est pas requise",
        "Elle vaut que la convention soit établie séparément ou intégrée à un autre document ; aucune attestation ni déclaration équivalente n'est exigée à sa place.")])

# R6222-21 : un envoi par l'auteur, relais institutionnel et règles communes exactes.
p = paras(
    "La rupture du contrat d'apprentissage ou de la période d'apprentissage est constatée par écrit, dans les conditions des articles L. 6222-18 à L. 6222-19 applicables à la date de conclusion du contrat et sous réserve de leurs dispositions transitoires. Pour les contrats conclus avant l'entrée en vigueur de la loi instituant le contrat de travail unique, les règles de rupture et les droits antérieurement constitués sont conservés.",
    "Pour les communications restant à accomplir à compter de cette entrée en vigueur, l'auteur de la rupture adresse une seule fois l'écrit au directeur du centre de formation d'apprentis. Le centre le transmet à l'organisme chargé du dépôt du contrat, dans le respect des règles de protection et de transmission des données nécessaires à leurs missions. Aucune seconde notification de la même rupture n'est exigée de son auteur. Les communications déjà valablement accomplies ne sont pas renouvelées. Cette transmission n'est pas une autorisation de rupture et n'en diffère pas la date d'effet.",
    "Pour les relations de travail de droit privé relevant du contrat unique conclu à compter de cette entrée en vigueur, l'employeur comme le salarié disposent d'un préavis individuel de quinze jours calendaires. Il est calculé à partir du lendemain de la présentation de la notification écrite au destinataire ou, lorsqu'une autre forme de notification est légalement admise, du lendemain de sa réception ou de sa remise. Pour une rupture à l'initiative du salarié, il court à partir du lendemain de la réception par l'employeur de la notification écrite. Il expire à la fin du quinzième jour, même non travaillé. Les formes de notification et les dispenses de préavis plus favorables au salarié restent celles légalement applicables. La fin d'une formation ou l'obtention d'un diplôme ne rompt pas automatiquement l'emploi.",
    "Lorsqu'un essai est expressément stipulé pour le nouveau contrat, il est de trois mois sans renouvellement ; aucune nouvelle période d'essai ne résulte du changement ou de la fin d'une phase pédagogique ou d'une mission. Le préavis ne prolonge pas l'essai. Le reliquat du préavis patronal qui ne peut être exécuté avant son échéance est compensé selon les règles de l'essai ; cette compensation n'allonge pas l'ancienneté effective au-delà de ce terme.",
    "Lorsque l'employeur rompt le nouveau contrat, l'indemnité ordinaire est régie par l'article L. 1234-9, y compris son exception de faute grave. Aucune indemnité ordinaire n'est due avant un an d'ancienneté ; à partir d'un an, son montant légal est de 0,20 mois de salaire brut de référence par année totale d'ancienneté, les années incomplètes étant prises au prorata des mois complets, dans la limite de six mois de ce salaire. Le seuil s'apprécie à la fin effective du contrat, préavis exécuté ou non inclus, sous réserve de la fin d'essai. Une fois le seuil atteint, la première année n'est pas retranchée du calcul. La démission ordinaire n'ouvre pas cette indemnité. Les indemnités conventionnelles ou contractuelles plus favorables ne sont pas limitées par ce plafond légal.",
    "La conversion convenue d'un ancien contrat conserve l'ancienneté et les créances acquises. La composante d'indemnité acquise avant la réforme conserve son régime et ses minima, sans compter deux fois une même période. Les salaires et congés acquis, les indemnités de préavis, les indemnités spéciales, notamment celles liées à l'inaptitude professionnelle, et les réparations d'une rupture illégale restent à leur champ propre.",
    "La rupture patronale demeure soumise à un motif valable et contrôlable, aux procédures et à la défense du salarié, à la non-discrimination et au recours au juge. La procédure propre à la rupture de l'essai reste distincte de celle du licenciement. Les protections de santé, de maternité et de représentation, l'intervention du représentant légal lorsqu'elle est requise, les autorisations des salariés protégés, les procédures collectives et les mesures des articles L. 6225-4 et L. 6225-5 ne sont pas supprimées par le préavis individuel. Pour les nouveaux contrats relevant du régime de droit privé, les anciennes attentes de cinq puis sept jours liées à la médiation ne s'ajoutent pas à ce préavis ; la médiation reste accessible et les garanties propres aux mineurs demeurent. Les agents publics et les relations ne relevant pas de ce régime de droit privé ne sont pas placés dans le contrat unique par le présent article.")
add(11, p,
    "Réduction de fond de la double communication : l'auteur ne notifie plus séparément au CFA et à l'organisme de dépôt ; le CFA assure le relais. Les règles communes nouvelles sont coordonnées sans convertir la durée d'apprentissage en terme d'emploi. La seconde passe corrige le départ au lendemain, le prorata par mois complets, le caractère expressément stipulé de l'essai et la distinction du secteur public. Elle évite de prétendre que le préavis supprime les procédures collectives ou les protections spéciales. Le relais crée une tâche institutionnelle, explicitement recensée, et les quinze jours ne sont pas présentés comme une baisse universelle par rapport à la source officielle.",
    "La source L. 6222-18 contient les quarante-cinq premiers jours pratiques, la médiation, la signature du représentant légal et des ruptures spéciales, avec note excluant les contrats antérieurs au 1er janvier 2019. Sa proposition conserve cette transition : les anciens contrats gardent leur version réellement applicable, pas automatiquement celle de 2018. Le nouveau contrat suit son régime commun proposé, y compris l'exception de faute grave à l'indemnité L. 1234-9 ; le préavis patronal nouveau reste payé même si la faute empêche son exécution. L. 1234-3 et L. 1221-25, lus source et proposition dans le corpus, précisent lendemain, essai et compensation ; aucun nouveau renvoi normatif à ces cibles non fournies n'est ajouté. R. 1234-1 lu confirme le prorata des mois complets. D. 6222-21-1 lu, proposition comprise, retire pour les contrats nouveaux les attentes de cinq puis sept jours, sans retirer les garanties du mineur. L. 6222-19 lu dans le corpus garde sa faculté de départ sur diplôme, non une fin automatique ; son raccordement aux dispenses favorables doit rester exprès. L. 6225-4 et L. 6225-5 lus protègent santé, rémunération et indemnité spéciale : leur rupture de sécurité est distincte et n'est pas remplacée par le barème ordinaire. Le caractère public de l'employeur ne suffit pas à exclure un contrat d'apprentissage de droit privé ; le critère est la nature juridique de la relation, avec médiation sectorielle adaptée, sans assimilation des agents publics. La tâche de relais CFA et ses coûts de traitement doivent être organisés sans dossier nouveau de l'apprenti. Aucune approbation juridique ni solde net de complexité n'est affirmé.",
    'mixed',
    "Par rapport à la source officielle entière, la double notification externe est fusionnée en un envoi de l'auteur et un relais du CFA. Cette tâche est transférée au centre. Le raccordement au contrat unique ajoute le préavis commun, notamment là où la source législative autorisait une rupture pendant les quarante-cinq premiers jours sans ce préavis ; il n'est donc pas une réduction générale de délai. Le solde net de coûts n'est pas établi.",
    "Les contrats antérieurs et leurs versions applicables, les garanties des mineurs, les ruptures de sécurité, les indemnités spéciales et les régimes publics distincts demeurent. Le nouveau barème n'efface ni salaires ni réparations ; aucun bilan national n'est chiffré.",
    "Charge institutionnelle nouvelle identifiée : le CFA doit relayer l'écrit au dépositaire. Le contrat unique impose aussi quinze jours de préavis commun dans des situations anciennement sans ce délai, et un régime ordinaire d'indemnité à partir d'un an. Aucun nouveau registre, formulaire, agrément ou condition d'aide n'est créé ; le solde net de ces changements reste inconnu.",
    [effect('obligation_merged', 'apprentissage-rupture-notification-unique',
        "Un seul envoi de l'auteur au CFA remplace ses deux notifications aux destinataires légaux.",
        "L'écrit de rupture est notifié au directeur du CFA et à l'organisme chargé du dépôt du contrat.",
        "Un envoi au CFA par l'auteur ; transmission au dépositaire par le centre, sans seconde notification de l'auteur.",
        'legal_duty', "Auteurs d'une rupture d'apprentissage et CFA destinataires.",
        "Communications restant à accomplir dès l'entrée en vigueur, y compris anciens contrats ; pas de reprise des envois valables.",
        "Relais obligatoire du CFA : transfert de tâche, sans bilan net chiffré ni nouveau dossier.",
        "Elle est notifiée au directeur du centre de formation d'apprentis ainsi qu'à l'organisme chargé du dépôt du contrat.",
        "Aucune seconde notification de la même rupture n'est exigée de son auteur."),
     effect('obligation_added', 'apprentissage-rupture-notification-unique',
        "Le CFA est désormais chargé d'assurer le relais au dépositaire à la place de l'auteur.",
        "Deux destinataires reçoivent notification, sans obligation expresse de relais du CFA dans cet article.",
        "Le CFA transmet l'écrit au dépositaire dans le cadre légal de protection des données.",
        'legal_duty', "Centres de formation d'apprentis recevant les écrits de rupture.",
        "Communications nouvelles ou restant à accomplir dès l'entrée en vigueur.",
        "Tâche institutionnelle de remplacement, coût non chiffré ; aucune autorisation de rupture.",
        "Elle est notifiée au directeur du centre de formation d'apprentis ainsi qu'à l'organisme chargé du dépôt du contrat.",
        "Le centre le transmet à l'organisme chargé du dépôt du contrat, dans le respect des règles de protection et de transmission des données nécessaires à leurs missions."),
     effect('coordination', 'contrat-unique-preavis-quinze-jours',
        "Raccordement au préavis commun nouveau, sans le compter comme une baisse uniforme du délai d'apprentissage.",
        "Renvoi à L. 6222-18 et L. 6222-19 : quarante-cinq jours pratiques de rupture initiale libre, puis voies et délais spéciaux.",
        "Quinze jours calendaires des deux côtés dans le nouveau régime privé, départ au lendemain ; dispenses favorables et procédures spéciales conservées.",
        'calendar_days', "Parties aux nouveaux emplois d'apprentis relevant du contrat unique de droit privé.",
        "Nouveaux contrats dès l'entrée en vigueur ; anciens contrats, mineurs et régimes publics à leur champ exact.",
        "Le préavis peut être une contrainte supplémentaire au début de l'emploi ; aucune baisse universelle ni suppression de procédure collective revendiquée.",
        "dans les conditions prévues aux articles L. 6222-18 à L. 6222-19.",
        "l'employeur comme le salarié disposent d'un préavis individuel de quinze jours calendaires."),
     effect('coordination', 'contrat-unique-indemnite-ordinaire-rupture',
        "Raccordement au barème ordinaire sans neutraliser les indemnités spéciales ou les anciens droits.",
        "Article réglementaire renvoyant aux ruptures spéciales d'apprentissage, sans barème ordinaire propre.",
        "Employeur seul : zéro avant un an, puis 0,20 mois brut de référence par année totale, prorata mois complets et plafond légal six mois ; exception de faute grave et indemnités plus favorables réservées.",
        'other', "Salariés dont le nouvel emploi privé en contrat unique est rompu par l'employeur.",
        "Seuil au terme effectif préavis inclus, sous réserve de l'essai ; droits anciens et indemnités spéciales distincts.",
        "Obligation ordinaire nouvelle possible dans certains cas auparavant régis autrement ; aucune économie nette globale revendiquée.",
        "dans les conditions prévues aux articles L. 6222-18 à L. 6222-19.",
        "Aucune indemnité ordinaire n'est due avant un an d'ancienneté ; à partir d'un an, son montant légal est de 0,20 mois de salaire brut de référence par année totale d'ancienneté, les années incomplètes étant prises au prorata des mois complets, dans la limite de six mois de ce salaire.")],
    ["Seconde notification séparée de la même rupture à l'organisme chargé du dépôt par l'auteur, remplacée par le relais du CFA sans nouveau dossier.",
     "Cumul des anciennes attentes de cinq puis sept jours de médiation avec le préavis commun pour les nouveaux contrats privés, sans suppression des garanties des mineurs."])

# Analyses de renvoi : chaque cible requise exactement une fois, empreinte fournie intacte.
contexts = {
 'R5221-44': "La vérification du titre et les affectations d'intérim",
 'R5312-32': "Le traitement de données des allocataires et des aides d'insertion",
 'D5422-3': "L'accès aux données de fins d'emploi et de mise à disposition",
 'D5424-22': "L'interdiction de licencier pendant l'inactivité du chantier",
 'D5522-11': "L'extinction de la reprise intégrale de l'aide après rupture",
 'D6123-37': "Le circuit d'information sur les contributions et aides de formation",
 'D6222-1': "Les conditions d'accès aux dérogations d'âge de l'apprentissage",
 'R6222-6': "L'aménagement conventionnel de la durée pédagogique",
 'R6222-7': "L'abrogation du modèle ministériel de convention",
 'R6222-8': "La réserve des conditions d'inscription à la certification",
 'R6222-9': "La dispense de convention dans les quatre situations spéciales",
 'R6222-21': "La rupture de l'apprentissage et son circuit de notification",
}

special = {
 ('R5312-32','L5134-25-1'): "Le 3° du règlement vise ce dispositif pour appliquer les règles particulières aux allocataires identifiés. La source permet des prolongations de CDD à vingt-quatre mois, cinq ans, fin de formation ou retraite à partir de cinquante-huit ans. La proposition les rattache au parcours et à l'aide sans terme d'emploi ; le traitement est conservé sans fermer l'accès des futurs bénéficiaires éligibles et sans garantir une aide hors de ses conditions.",
 ('R5312-32','L5132-5'): "Le renvoi du 3° identifie les personnes en insertion, non une obligation de conclure un CDD. La source et la proposition ont été distinguées : quatre mois et vingt-quatre mois portent désormais sur le parcours, les prolongations favorables restent ouvertes, le départ sans préavis en cas d'embauche demeure. Le partage de données n'ajoute ni nouveau terme d'emploi, ni plafond général de vingt-quatre heures à ce régime spécial.",
 ('D5422-3','L1251-1'): "Le 1° réellement visé concerne le contrat commercial de mise à disposition entre l'ETT et l'utilisateur ; il reste à durée limitée même quand l'emploi est sans terme. La fin d'une mission n'est pas la rupture du contrat de travail du 2°, mais elle peut rester une fin de mise à disposition imputable selon les accords chômage. La proposition est rectifiée pour préserver cette distinction et les anciens contrats de mission.",
 ('D6123-37','L6131-1'): "Le 5° conservé vise des contributions conventionnelles et non le CPF-CDD du 4°. La proposition cible supprime le CPF-CDD pour les périodes de travail nouvelles, et la contribution supplémentaire du 3° pour les années commençant au 1er janvier suivant la loi de suppression. Le présent circuit distingue ces calendriers, protège anciennes dettes et avantages, et garde les données nécessaires à la créance et à l'aide futures de L. 6242-1 ; il n'institue pas une seconde suppression de taxe.",
 ('D6222-1','L6222-18'): "Le 4° renvoie à la constatation d'inaptitude physique temporaire, non à une reprise générale du régime de rupture en quarante-cinq jours pratiques. Les deux versions de L. 6222-18 sont distinguées : anciens contrats selon leurs dates, nouveau régime de rupture du contrat unique selon sa proposition. Le retrait des conditions de trente-cinq ans et d'un an ne retire aucune garantie médicale ou signature requise du représentant légal ; les mesures de sécurité demeurent autonomes.",
 ('R6222-21','L6222-18'): "Renvoi direct de fond : la source prévoit quarante-cinq jours de pratique, accord écrit, cas de rupture patronale, médiation, signature du représentant légal et liquidation. La proposition cible réserve ces règles aux anciens contrats, dont la note exclut déjà ceux d'avant 2019, et applique le contrat unique aux nouveaux. L'écrit et le relais CFA ne rétablissent ni délai spécial cumulé, ni fin automatique de formation ; garanties des mineurs, santé, recours et créances anciennes sont préservés, sans généraliser le régime privé aux agents publics.",
 ('R6222-6','L6222-37'): "Le renvoi exact est le 2°, aménagement des durées pour les personnes handicapées ; les autres 1°, 3° à 6° ont des objets distincts. La proposition cible applique cette adaptation à la période pédagogique sans terme d'emploi et maintient les avantages futurs et droits anciens. R. 6222-6 réserve cette adaptation et la dispense de convention de R. 6222-9 : la borne générale six mois/trois ans ne neutralise pas le régime favorable.",
 ('R6222-9','L6222-37'): "La dispense vise exactement le 2° relatif aux durées pour handicap, non toute la liste des aménagements. La source et la proposition cible conservent ce champ favorable pour les futurs apprentis en contrat unique et les anciens contrats ; aucune convention ou attestation équivalente n'est rétablie, et l'aménagement de formation ne termine pas l'emploi.",
 ('R6222-6','L6222-40'): "Le 1° visé concerne l'aménagement des durées pour sportifs de haut niveau, distinct du temps de travail du 2°. La proposition cible maintient cet avantage dans la période pédagogique et pour les futurs éligibles, avec transition des anciens contrats. La réserve de R. 6222-6 empêche les bornes générales de faire perdre cet aménagement ; l'emploi reste sans terme.",
 ('R6222-9','L6222-40'): "Le 1° seul fonde ici la dispense de convention pour l'adaptation des durées des sportifs de haut niveau. Le 2° sur le temps de travail n'est pas transformé en dispense générale. Les deux versions sont distinguées : période de formation pour les contrats uniques nouveaux, avantages et droits maintenus pour anciens et futurs éligibles, sans fin automatique d'emploi.",
 ('R6222-6','R6222-23-1'): "Cette cible permet après rupture, dans le cadre de L. 6222-18-2, de déroger à la durée minimale d'apprentissage et à celle de formation en CFA, sans convention de réduction. La proposition conserve la dispense pour les futurs apprentissages du contrat unique et les droits anciens. La réserve expresse de R. 6222-6 empêche de réimposer six mois ou une convention intégrée dans ce cas ; aucune ancienneté ni nouvelle notification de rupture n'en découle.",
 ('R6222-6','R6222-9'): "La cible dispense déjà de convention dans quatre cas précis : échec, formation avant embauche, handicap et sport de haut niveau par les subdivisions visées. Sa proposition corrige le renvoi au troisième alinéa et conserve la dispense pour les futurs contrats uniques. R. 6222-6 la réserve explicitement : le support commun ne devient pas obligatoire pour ceux qui étaient dispensés, sans attestation substitutive ni nouvel essai.",
}

for a in out:
    if a['number'] == 'D6123-37':
        a['review_notes'] += " Le renvoi ajouté à L. 6242-1 n'est pas une cible fournie dans reference-targets.json : sa source entière, sa note et sa proposition ont été lues dans le corpus public. Sa source institue la contribution ; sa proposition maintient la créance via L. 6241-2 et l'aide via L. 6243-1-2. Ce sont des dispositions proposées distinctes du droit en vigueur, sans bénéfice ni données supplémentaires inventés ici."
    elif a['number'] == 'R6222-6':
        a['review_notes'] += " Les renvois ajoutés à L. 6222-11 et L. 6222-12-1 sont hors des cibles fournies dans reference-targets.json ; leurs sources entières et notes ont été lues dans le corpus public. Les autres cibles requises seules figurent dans reference_checks."
    elif a['number'] == 'R6222-21':
        a['review_notes'] += " Les renvois ajoutés à L. 6225-4 et L. 6225-5 ne sont pas des cibles fournies dans reference-targets.json ; leurs sources entières et notes ont été lues dans le corpus public, sans contenu normatif supposé. L. 6227-1 a aussi été lu sur le champ des employeurs publics, sans introduire de renvoi supplémentaire dans le texte proposé."
    if a['proposed_xml'] is not None:
        a['proposed_xml'] = a['proposed_xml'].replace('<br>', '<br />')
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for tk in refs['requirements'][key]:
        t = refs['targets'][tk]
        n = t['number']
        an = a['number']
        if (an,n) in special:
            assessment = special[(an,n)]
        elif n == 'L1221-2':
            assessment = contexts[an] + " : le présent article ne crée pas un nouveau contrat à terme. La source de L. 1221-2 autorise encore les CDD ; sa proposition, distincte du droit en vigueur, impose la durée indéterminée aux nouvelles embauches et exclut tout terme de mission, chantier ou formation. Les anciens contrats et leurs créances demeurent selon leur transition ; conversion sans remise à zéro d'ancienneté, sans nouveau renouvellement à durée déterminée."
        elif n == 'L1234-1':
            if an == 'D5424-22':
                assessment = "Le préavis proposé de quinze jours pour les nouveaux contrats ne lève pas l'interdiction de licencier pendant l'inactivité. Le second membre de D. 5424-22 autorise seulement l'expiration d'un préavis donné avant cette période ; les anciens contrats gardent notamment les préavis d'un ou deux mois selon ancienneté. Les procédures collectives et autorisations distinctes restent opposables ; ce maintien n'impose pas un nouveau préavis."
            elif an == 'R6222-21':
                assessment = "La source de L. 1234-1 porte les préavis de licenciement selon ancienneté ; sa proposition substitue quinze jours calendaires pour le nouveau contrat, y compris une faute grave qui impose un préavis payé sans exécution. R. 6222-21 coordonne le régime privé et le départ au lendemain, sans déduire une durée de procédure collective de ce seul préavis. Les anciens contrats, les notifications soumises à leur forme légale et les protections spéciales restent distincts."
            else:
                assessment = contexts[an] + " : le présent article ne fixe pas le préavis de licenciement et n'y déroge pas. La cible proposée prévoit quinze jours calendaires pour les seuls nouveaux contrats, sans condition d'ancienneté ; sa source conserve les durées antérieures d'un ou deux mois selon les cas. Ni cette règle ni la notification de rupture n'est remplacée par la formalité traitée ici ; les anciens contrats et procédures collectives demeurent distincts."
        elif n == 'L1234-9':
            if an == 'R6222-21':
                assessment = "Le renvoi est désormais exprès à la proposition L. 1234-9 : employeur seul, exception de faute grave, seuil d'un an au terme effectif préavis inclus sous réserve de l'essai, puis 0,20 mois brut de référence par année totale, mois complets au prorata et plafond légal six mois. La première année n'est pas soustraite. L'ancienne condition de huit mois demeure pour les anciens contrats selon la cible ; minima acquis, indemnités plus favorables et spéciales ne sont ni effacés ni plafonnés deux fois."
            else:
                assessment = contexts[an] + " : le présent article ne fixe pas l'indemnité ordinaire et n'abaisse pas ses conditions par un renvoi indirect. La cible proposée ouvre au salarié le droit à indemnité pour une rupture patronale à un an au terme effectif, préavis inclus, puis 0,20 mois par année totale avec mois complets et plafond six mois, hors faute grave. L'ancienne condition de huit mois, les composantes antérieures et les indemnités spéciales restent à leur champ ; aucun remboursement d'aide ou échange de données ne se substitue à ces droits."
        elif n == 'L6222-7-1':
            extra = {
                'R6222-6': "Le support commun signé est admis mais sa partie d'aménagement demeure annexée ; la proposition législative fournie n'a pas supprimé l'annexe. Les six mois/trois ans et dispenses spéciales sont réservés.",
                'R6222-7': "L'abrogation ne porte que sur le modèle ministériel, non la convention de fond, ses signatures ou son annexe légale. L'usage volontaire d'un modèle ne ferme pas le financement des futures situations recevables.",
                'R6222-8': "La réserve de certification demeure applicable à l'aménagement, même sans modèle obligatoire. Elle ne devient ni un agrément d'embauche ni une durée d'emploi.",
                'R6222-9': "La dispense des quatre cas est maintenue malgré l'usage éventuel d'un support commun, sans formulaire substitutif. Les apprentissages futurs éligibles restent couverts.",
            }[an]
            assessment = "La convention est au troisième alinéa de la source officielle. La proposition cible ajoute ensuite un alinéa transitoire : renvoyer encore au dernier alinéa serait erroné, d'où la rectification au troisième. " + extra + " La période pédagogique ne termine pas le contrat unique et les anciens contrats conservent leurs droits."
        else:
            raise ValueError((an,n))
        checks.append(dict(target_key=tk, view_sha256=t['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(out)} articles')
