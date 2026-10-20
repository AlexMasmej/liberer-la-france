import json
import re
import html
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
OUT = []
BY_NUMBER = {}

def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml or ''))

def paragraphs(*texts):
    return ''.join('<p>' + t + '</p>' for t in texts)

def add(index, proposed=None, reason='', notes='', retained=False):
    s = SOURCES[index]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if retained else 'rewrite_draft')
    OUT.append(a)
    BY_NUMBER[a['number']] = a
    return a

def reduction(a, *removed):
    a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
             removed_provisions=list(removed))

def repeal(a, scope):
    a.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=scope)

def impact(a, classification, assessment, limitations, burdens, effects):
    a['substantive_impact'] = dict(version=1, classification=classification, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens, effects=effects)

def effect(kind, measure, description, before, after, unit, population, transition, replacement, sq, pq):
    return dict(kind=kind, measure_id=measure, description=description, before=before, after=after,
        unit=unit, affected_population=population, conditions_and_transition=transition,
        replacement_or_new_burdens=replacement, source_quote=sq, proposed_quote=pq)

# R5221-44 : dispense déjà existante pour les contrats de mission, étendue au support unique.
a = add(0, SOURCES[0]['previous_draft']['proposed_xml'],
    "Réforme de fond conservée : la dispense de vérification répétée, déjà acquise pour les contrats de mission avec la même entreprise, couvre expressément le nouvel emploi à durée indéterminée et ses affectations. La correction de « s'est s'assurée » est seulement rédactionnelle. La seconde passe ne supprime pas la vérification initiale : elle contrôle un droit d'exercer et relève aussi de L. 5221-8, non d'une autorisation nouvelle créée par cet article.",
    "R. 5221-41 et L. 5221-8 ont été lus dans le corpus public : saisine initiale du préfet, avec la dispense légale propre à l'inscription comme demandeur d'emploi. Cette dispense n'est pas restreinte. La durée et le champ du titre ne sont pas élargis ; aucune vérification initiale nouvelle n'est créée lors d'une conversion déjà couverte. La validité du titre reste déterminante et les contrôles légalement distincts demeurent. Le passage au support unique exige les coordinations de L. 1251-1 et L. 1251-58-1 à L. 1251-58-6, sans perte des garanties mensuelles et d'intermission. Le présent article ne fixe ni préavis ni indemnité. Le brouillon est conservé après examen de sa fonction, sans revendiquer une seconde suppression de la vérification à chaque mission, déjà dispensée dans la source.")
reduction(a, "Vérifications répétées du seul fait des affectations d'un emploi à durée indéterminée ou de sa conversion convenue, dans le champ d'une vérification initiale toujours valable.")
impact(a, 'material_reduction',
    "La source dispense déjà toutes les missions avec la même entreprise ; le gain propre est l'extension expresse de cette dispense au support à durée indéterminée et à la conversion, non une nouvelle suppression pour chaque mission.",
    "La vérification initiale, les limites du titre et les autres employeurs restent hors de cette dispense. Aucun coût ni solde national n'est chiffré ; les règles législatives de l'intérim doivent être coordonnées.",
    "Aucune charge nouvelle n'est identifiée : ni formulaire, ni attestation, ni registre ou contrôle supplémentaire ne remplace la vérification répétée dispensée. Le contrôle initial préexiste.",
    [effect('relief_extended','interim-verification-travail-unique',
        "Étendre au support d'emploi unique la vérification valant pour les affectations successives.",
        "Dispense expressément formulée pour les contrats de mission entre l'étranger et la même entreprise, pendant la validité du titre de séjour.",
        "Même dispense pour l'emploi à durée indéterminée, les affectations et la conversion convenue, sans prolonger ni élargir le titre.",
        'legal_duty', 'Entreprises de travail temporaire et travailleurs étrangers déjà vérifiés par elles.',
        "Formalités à accomplir après l'entrée en vigueur ; vérifications antérieures toujours valables et anciens contrats préservés.",
        "Aucune démarche de remplacement ; vérification initiale et contrôles distincts maintenus.",
        "cette formalité est réputée remplie pour la durée de validité du titre de séjour et pour tout contrat de mission, conclu entre l'étranger et cette entreprise de travail temporaire.",
        "Aucune nouvelle vérification au titre de cette formalité n'est exigée du seul fait d'une nouvelle affectation ou de la conversion convenue d'un contrat en contrat unique à durée indéterminée.")])

# R5312-32 : les trois finalités sont nécessaires et ne dépendent pas du support CDD.
a = add(1, None,
    "Maintien intégral nécessaire après examen de la source et du brouillon stylistique. Le 1° permet l'identification des allocataires pour l'accompagnement ; le 2° assure l'articulation avec les procédures légales du RSA ; le 3° permet l'application des parcours d'insertion et prolongations favorables. Les organismes échangent des données existantes : l'article n'impose aux personnes aucune déclaration ou pièce supplémentaire. Aucune de ces finalités n'est démontrée redondante dans le contexte fourni. Changer seulement les mots du brouillon ne constituerait pas une réduction.",
    "Les trois finalités et les deux responsables sont conservés, ainsi que le périmètre exact des personnes, qui ne vise les proches que dans les cas énoncés. R. 5312-33 à R. 5312-36 ont été lus : nécessité des catégories, destinataires habilités, conservation et droits des personnes, avec références au RGPD. L'appui sur des données existantes évite une collecte nouvelle auprès des allocataires ; aucune extension de finalité n'est décidée. La dénomination comporte une seconde occurrence de « revenu de solidarité » sans « active » : discordance préexistante laissée visible. Le 1er janvier 2025 est la date historique du décret n° 2024-1268, non celle de la réforme. L. 5134-23-1 a été lu dans le corpus ; L. 5132-5 et L. 5134-25-1 dans les cibles fournies : les références entières restent opérantes avec leurs périodes d'aide distinctes de l'emploi, sans CDD nouveau. L. 262-37 et L. 262-42 du CASF restent des références extérieures dont le texte intégral n'est pas fourni ici ; aucune modification ni approbation de ces procédures n'est déduite de leur mention.", retained=True)
impact(a, 'retained_necessary',
    "La source officielle entière demeure applicable : pas de baisse revendiquée. Le traitement sert à identifier les droits et appliquer les parcours et dérogations d'aide sans imposer une déclaration d'allocataire dans cet article.",
    "Les modalités de sanction et les références au CASF ne sont pas réécrites. Le contrôle des garanties de données ne vaut pas audit indépendant du traitement ni bilan national de sa charge.",
    "Aucune charge nouvelle n'est identifiée puisque le texte source est reproduit intégralement sans ajout. Les finalités, responsables et garanties de données ne sont pas étendus.", [])

# D5422-3 : conserver l'accès pour contrôler l'imputation, supprimer l'exclusivité du canal.
a = add(2, SOURCES[2]['previous_draft']['proposed_xml'].replace("de ces données. L'employeur", "de ces données.</p><p>L'employeur"),
    "Réforme de fond conservée : le téléservice devient un canal au choix et l'indication préalable d'une impossibilité d'utilisation est supprimée. La seconde passe maintient l'accès à la liste, utile pour contrôler l'imputation des fins de contrat et contester une contribution ; supprimer cet accès ferait perdre une garantie. Le périmètre personnel et l'imputabilité sont conservés. La fin d'une affectation ou formation ne devient pas une fin de l'emploi unique.",
    "L. 1251-1 distingue le contrat commercial de mise à disposition du contrat de travail ; le premier demeure susceptible d'une fin autonome dans les accords de L. 5422-20, sans faire fictivement cesser le second. Le téléservice reste disponible : aucun compte ou dossier de remplacement n'est ajouté pour le canal alternatif. Aucune baisse de taux d'assurance chômage ni suppression de modulation n'est décidée par ce droit d'accès. La transition ancienne de l'article 2 du décret n° 2023-635 du 20 juillet 2023, mentionnée en note, reste à son champ ; elle ne date pas la réforme. Les accords d'imputabilité, L. 5422-20 et les dispositifs de collecte doivent être coordonnés sur les vraies fins d'emploi, sans requalifier une intermission en rupture.")
reduction(a, "Usage obligatoire du téléservice pour demander communication des données, et indication préalable de l'impossibilité de l'utiliser pour recourir à un autre moyen.")
impact(a, 'material_reduction',
    "La source oblige à utiliser le téléservice, sauf impossibilité indiquée ; la proposition donne immédiatement le choix du moyen. L'accès aux données et le contrôle de l'imputabilité sont conservés ; aucune contribution n'est réduite par cet article.",
    "Le gain est procédural, sans évaluation monétaire. Les fins de mise à disposition restent distinctes des fins du contrat de travail et soumises aux accords applicables.",
    "Aucune charge nouvelle n'est identifiée : la demande était déjà nécessaire à l'accès individuel, le téléservice subsiste et le moyen alternatif ne requiert ni justification d'impossibilité ni nouvelle pièce.",
    [effect('obligation_removed','chomage-acces-donnees-canal-libre',
        "Supprimer l'exclusivité du téléservice et sa condition d'exception.",
        "Demande électronique obligatoire, autre moyen seulement après indication de l'impossibilité d'utiliser le téléservice.",
        "Demande au choix par le téléservice ou tout autre moyen, sans justification d'impossibilité.",
        'legal_duty','Employeurs et tiers déclarants demandant leurs données de fins de contrats imputables.',
        "Demandes futures et en cours à l'entrée en vigueur, sans refaire celles déjà reçues.",
        "Aucun justificatif, registre ou déclaration de remplacement ; conservation du périmètre des données.",
        "L'employeur ou son tiers déclarant adresse, par voie dématérialisée, sa demande au moyen de ce téléservice.",
        "L'employeur ou son tiers déclarant peut utiliser ce téléservice ou adresser sa demande par tout autre moyen, sans avoir à justifier de son impossibilité d'utiliser le téléservice.")])

# D5424-22 : protection autonome, qui reste compatible avec le nouveau préavis.
a = add(3, None,
    "Maintien intégral nécessaire : l'interdiction de licencier pendant l'inactivité évite de transférer le risque de chantier au salarié. Les exceptions de faute grave et, dans les seuls travaux publics, d'arrêt par le maître d'œuvre sont déjà ciblées. Le préavis notifié avant l'inactivité peut expirer pendant celle-ci. Aucune formalité, autorisation, taxe ou attente sans fonction essentielle n'est isolée. La clarification du brouillon ne nécessite pas de réécrire la source, qui ne détermine elle-même aucune durée de préavis ni aucun terme d'emploi.",
    "La protection source couvre les nouveaux contrats sans renvoi à un CDD ni condition incompatible. Le préavis individuel nouveau de quinze jours ne permet pas de notifier un licenciement interdit pendant l'inactivité ; l'exception de faute grave autorise le licenciement, mais n'écarte pas le paiement du préavis nouveau prévu par la proposition de L. 1234-1. Les anciens contrats conservent leurs règles de préavis. Le mot « expiration » vise le préavis déjà donné, non le chantier : aucune fin automatique du contrat unique n'en résulte, au regard de L. 1221-2 proposé. L'indemnisation des intempéries, les autorisations de salariés protégés, les procédures collectives et les réparations demeurent distinctes. Le texte source ne comporte aucun renvoi à déplacer et n'a pas besoin du paragraphe général de rappel ajouté par le brouillon.", retained=True)
impact(a, 'retained_necessary',
    "La protection entière, ses deux exceptions et la règle du préavis antérieurement donné sont conservées ; aucune suppression de charge n'est revendiquée. L'article reste nécessaire pour la stabilité du revenu pendant l'inactivité du chantier.",
    "Le préavis et l'indemnisation demeurent définis ailleurs. Aucun gain de coût ou de complexité ni achèvement des coordinations du régime d'intempéries n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : le texte officiel reste intégralement inchangé, sans nouvelle procédure, donnée, pièce ou délai. L'interdiction et ses exceptions préexistent.", [])

# D5522-11 : une reprise intégrale d'aide pour emploi effectivement réalisé est retirée.
a = add(4, SOURCES[4]['previous_draft']['proposed_xml'],
    "Abrogation de fond conservée : le seul licenciement avant la fin de la période d'aide ne déclenche plus la restitution intégrale de l'aide pour des emplois effectivement éligibles. Une restitution générale sans rapport avec l'indû ne conserve pas une fonction essentielle démontrée ; la fraude et les indus ont des fondements distincts. La seconde passe ne laisse aucune fraction de cette reprise automatique. Les cinq dispenses demeurent pour les anciennes ruptures ; elles deviennent sans objet pour la charge entièrement retirée dans le nouveau champ.",
    "D. 5522-7 a été lu intégralement : trois années consécutives depuis l'embauche et abattement de 50 % la troisième année sont conservés. L'extinction prospective est déclenchée par la notification de la rupture, comme dans le brouillon, et non par une date de promulgation supposée. Les aides ne sont pas payables après cessation effective de l'emploi sur ce seul fondement. Coordonner les conventions et décisions de récupération : aucune clause rappelant seulement D. 5522-11 ne doit rétablir sa reprise intégrale pour les notifications nouvelles, y compris concernant un ancien contrat. Les récupérations fondées sur une condition autonome doivent être distinguées. Les aides pour situations futures éligibles restent ouvertes et leur durée ne borne pas l'emploi.")
repeal(a, "Suppression du reversement intégral de l'aide à l'État fondé sur la seule rupture patronale avant la fin de la période d'aide, pour les ruptures notifiées après l'entrée en vigueur ; créances et dispenses des ruptures antérieures conservées.")
impact(a, 'material_reduction',
    "La reprise intégrale de l'aide pour la seule rupture patronale anticipée disparaît dans le champ nouveau, et non seulement ses modalités rédactionnelles. Le texte retire toute cette charge, sans supprimer l'aide ni ses conditions propres.",
    "Les ruptures déjà notifiées, les indus et fraudes autonomes restent hors de la suppression. Le coût public de la moindre récupération n'est pas chiffré et n'est pas présenté comme une économie nationale.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration équivalente, ni taxe, ni justificatif de remplacement n'est institué. Les conditions d'aide et récupérations distinctes demeurent celles de leurs fondements.",
    [effect('obligation_removed','aide-emploi-fin-reprise-integrale',
        "Retirer la restitution intégrale déclenchée par la seule rupture patronale anticipée.",
        "Employeur tenu de reverser 100 % de l'aide à l'État si la rupture précède le terme de la période d'aide, sauf les cinq dispenses énumérées.",
        "Aucune reprise sur ce seul fondement pour une rupture nouvellement notifiée ; indus et fraudes autonomes toujours récupérables.",
        'legal_duty',"Employeurs bénéficiaires de l'aide régie par D. 5522-7.",
        "Notifications à compter de l'entrée en vigueur ; anciennes notifications soumises aux règles et cinq dispenses antérieures, sans restitution générale rétroactive.",
        "Aucune obligation de remplacement ; pas d'aide créée après la cessation de l'emploi.",
        "le montant de l'aide est intégralement reversé par l'employeur à l'Etat.",
        "La rupture à l'initiative de l'employeur avant la fin de la période mentionnée à l'article D. 5522-7 n'entraîne plus, sur le fondement du présent article, le reversement intégral de l'aide à l'État.")])

# D6123-37 : listes entières, sauf retraits explicitement identifiés.
p = SOURCES[5]['previous_draft']['proposed_xml']
p = p.replace("<br/>- Coordonnées du référent formation professionnelle ou, à défaut, de la personne chargée de la déclaration sociale nominative ;", '')
p = p.replace("<br/>- Coordonnées du référent chargé de la formation professionnelle ou, à défaut, du contact déclarant ;", '')
p = p.replace("de la contribution supplémentaire à l'apprentissage, de la contribution mentionnée", "de la contribution supplémentaire à l'apprentissage pour les seules années civiles antérieures à celles commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression, de la contribution mentionnée")
p = p.replace("Les données relatives aux rémunérations afférentes aux périodes d'emploi antérieures ne sont transmises", "Les données relatives à cette contribution pour les rémunérations afférentes aux périodes d'emploi antérieures ne sont transmises")
p += paragraphs(
    "Aucune transmission des coordonnées nominatives du référent chargé de la formation professionnelle ni, à défaut, de celles du déclarant n'est exigée au titre du présent article. L'absence de ces coordonnées dans ces transmissions ne peut conditionner l'accès aux financements et services auxquels l'entreprise et ses salariés sont éligibles. Cette suppression s'applique aux transmissions à accomplir à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, sans nouvelle transmission des fichiers antérieurs.",
    "Pour les années civiles commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant suppression de la contribution supplémentaire à l'apprentissage, aucune transmission d'assiette, de montant, de liste de redevables ni d'état néant exclusivement justifiée par cette contribution n'est exigée. Les données exclusivement justifiées par cette contribution pour les années antérieures ne sont transmises que pour leurs liquidations, régularisations, restitutions, contrôles et recours. Les données nécessaires à la créance imputable sur le solde de taxe d'apprentissage et à l'aide au recrutement maintenues dans le champ de l'article L. 6242-1 continuent d'être utilisées, à partir des données légalement disponibles, sans déclaration de la contribution supprimée. La période d'apprentissage ou de professionnalisation au sein d'un contrat unique, puis la poursuite de ce contrat dans les conditions propres à ces avantages, ne doivent pas en priver les futurs bénéficiaires éligibles.")
a = add(5, p,
    "Réformes conservées : retrait du circuit obligatoire de données destiné aux enquêtes de satisfaction, suppression de la redemande de données déjà disponibles et extinction du reporting CPF-CDD pour les périodes futures. La seconde passe supprime en plus les deux rubriques de coordonnées nominatives du référent ou du déclarant : elles ne sont pas nécessaires à identifier les entreprises et établissements, affecter les fonds ou calculer les assiettes ; leurs adresses et identifiants restent transmis. Elle coordonne aussi la suppression de la contribution supplémentaire à l'apprentissage déjà retenue dans L. 6131-1 et L. 6242-1 proposés, sans prétendre supprimer ces taxes une deuxième fois. Toutes les autres rubriques et subdivisions sont conservées, notamment BOETH, effectifs d'alternants, contributions conventionnelles, intermittents et déductions de taxe d'apprentissage.",
    "L. 6131-1 fourni a deux extinctions distinctes : CPF-CDD au jour d'entrée en vigueur pour les périodes de travail futures, même d'anciens CDD ; contribution supplémentaire à l'apprentissage au 1er janvier de l'année suivante. L. 6331-6 et L. 6242-1 ont aussi été lus dans le corpus public. La donnée de montant CSA reste utile pour les années anciennes ; sa suppression n'emporte ni celle de la taxe d'apprentissage de base, ni celle de la créance favorable sur son solde ou de l'aide au recrutement, même pour les futurs contrats uniques. Les effectifs d'alternants et BOETH sont conservés pour les missions et financements distincts, sans créer une déclaration individuelle. L. 6123-5 a été lu : son 14° garde une mission législative d'enquête ; seul son circuit de données au I, 3°, est retiré ici, pas la mission légale. Les contraintes de nécessité et de protection des données demeurent. R. 6123-34 a été lu et doit empêcher la redemande des informations déjà accessibles. Incohérence source signalée : L. 6323-20-1, lu intégralement, traite du CPF de salariés de personnes publiques, sans créer lui-même une contribution ; le renvoi est conservé, sans inventer une assiette, et appelle une concordance législative expresse. Nouveau renvoi opératoire à L. 6242-1 : cible absente de reference-targets.json, mais source et proposition lues dans le corpus public fourni ; aucune empreinte de vue fournie ne lui est attribuée. Les anciens dossiers ne sont ni détruits ni refaits. Les droits de contrôle sur les périodes antérieures demeurent.")
reduction(a,
    "Transmission obligatoire des informations d'entreprise par le circuit du présent article pour réaliser les enquêtes de satisfaction du 14° de L. 6123-5.",
    "Transmission systématique des coordonnées nominatives du référent formation ou du déclarant à France compétences et aux opérateurs de compétences.",
    "Rubriques, montants et états néant du CPF-CDD relatifs aux périodes de travail futures, y compris dans un ancien contrat qui se poursuit.",
    "Transmission d'assiette, montant et liste exclusivement motivée par la contribution supplémentaire à l'apprentissage pour les années où celle-ci est supprimée.",
    "Demandes complémentaires à l'entreprise ou remises répétées de données et justificatifs déjà légalement accessibles au destinataire dans ce circuit.")
impact(a, 'material_reduction',
    "Par rapport à la source entière, le I, 3°, et les deux rubriques de contacts nominatives sont retirés ; les transmissions CPF-CDD et CSA sont bornées à leurs périodes anciennes. La source ne créait pas expressément une déclaration complémentaire de l'employeur : l'interdiction d'en exiger une sécurise le circuit, sans compter une abolition non démontrée.",
    "Le rôle d'enquête prévu par la loi et les autres financements subsistent. L'extinction des deux contributions relève de leurs articles législatifs, pas d'une seconde baisse ici. Les coûts des organismes et le solde public ne sont pas mesurés.",
    "Aucune charge nouvelle n'est identifiée : les listes restantes reprennent des données préexistantes, les transitions réutilisent les dossiers anciens et aucun état néant, registre ou donnée personnelle de remplacement n'est créé. Les transmissions utiles aux avantages maintenus ne constituent pas une nouvelle déclaration de contribution.",
    [effect('obligation_removed','formation-enquetes-sans-transmission-imposee',
        "Retirer la finalité d'enquête du circuit obligatoire d'informations.",
        "Informations communiquées notamment pour les enquêtes de satisfaction du 14° de L. 6123-5.",
        "I, 3°, abrogé ; autres finalités de répartition et missions maintenues, mission législative d'enquête distincte.",
        'legal_duty','Organismes de recouvrement, France compétences et opérateurs de compétences.',
        "Transmissions à compter de l'entrée en vigueur ; pas de remise à zéro des dossiers antérieurs.",
        "Aucune déclaration d'enquête de remplacement créée dans cet article.",
        "3° La réalisation des enquêtes de satisfaction mentionnées au 14° de l'article. L. 6123-5 ;",
        "3° Abrogé à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail ;"),
     effect('obligation_removed','formation-transmission-contacts-nominatifs',
        "Supprimer les deux rubriques de contacts personnels du circuit de données.",
        "Coordonnées du référent formation ou à défaut du déclarant transmises à France compétences puis aux opérateurs.",
        "Coordonnées nominatives retirées des deux listes sans condition nouvelle d'accès au service ou au financement.",
        'legal_duty','Organismes de recouvrement, France compétences, opérateurs et contacts des entreprises.',
        "Transmissions à accomplir après l'entrée en vigueur ; aucun fichier antérieur à refaire.",
        "Identifiants et adresses des entités conservés ; aucune donnée ou attestation de contact de remplacement.",
        "-Coordonnées du référent formation professionnelle, ou à défaut celles de la personne chargée de la déclaration sociale nominative ;",
        "Aucune transmission des coordonnées nominatives du référent chargé de la formation professionnelle ni, à défaut, de celles du déclarant n'est exigée au titre du présent article."),
     effect('coordination','suppression-cpf-cdd',
        "Adapter les rubriques à l'extinction législative du CPF-CDD, sans nouvelle réduction comptée.",
        "Masse salariale et montant CPF-CDD dans les catégories à transmettre sans borne temporelle dans cet article.",
        "Données CPF-CDD limitées aux périodes de travail antérieures ; aucun état néant pour les périodes nouvelles, même sur ancien CDD.",
        'legal_duty','Organismes de recouvrement et destinataires du circuit de formation professionnelle.',
        "Périodes de travail à compter de l'entrée en vigueur pour l'extinction ; anciennes liquidations, restitutions et recours conservés.",
        "Aucune nouvelle déclaration ni prélèvement équivalent ; droits et avantages de formation maintenus.",
        "-Masse salariale assujettie à la contribution au compte personnel de formation des contrats à durée déterminée ;",
        "Aucune assiette, aucun montant ni état néant de contribution au compte personnel de formation des contrats à durée déterminée n'est demandé pour les rémunérations afférentes aux périodes d'emploi courant à compter de cette entrée en vigueur, y compris au titre d'un contrat antérieur."),
     effect('coordination','suppression-contribution-supplementaire-apprentissage',
        "Empêcher le reporting de rétablir la CSA supprimée pour les années nouvelles.",
        "Montant déclaré de la contribution supplémentaire à l'apprentissage compris sans limite d'année dans le circuit.",
        "Données historiques maintenues ; plus de transmission exclusivement justifiée par la CSA pour les années supprimées, avec avantages autonomes préservés.",
        'legal_duty','Entreprises du champ CSA et organismes chargés de transmettre leurs données.',
        "Années civiles commençant le 1er janvier de l'année suivant l'entrée en vigueur de sa suppression ; dettes et remboursements anciens protégés.",
        "Pas de déclaration CSA de remplacement ; données utiles aux créances et aides maintenues réutilisées légalement.",
        "contribution supplémentaire à l'apprentissage",
        "Pour les années civiles commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant suppression de la contribution supplémentaire à l'apprentissage, aucune transmission d'assiette, de montant, de liste de redevables ni d'état néant exclusivement justifiée par cette contribution n'est exigée.")])

# D6222-1 : conserver les cas légaux, retirer deux obstacles réglementaires d'accès.
p = paragraphs(
    "Les dérogations à la limite d'âge supérieure prévues à l'article L. 6222-2 s'appliquent dans les conditions suivantes :",
    "1° Pour les dérogations prévues aux 1° et 2° de cet article, aucune limite d'âge supérieure n'est exigée ;",
    "2° Pour les dérogations prévues aux 1° et 2° du même article, aucun délai maximal entre le précédent apprentissage et le nouvel apprentissage n'est exigé ;",
    "3° Pour la dérogation prévue au 2° du même article, les causes indépendantes de la volonté de l'apprenti ayant entraîné la rupture du contrat d'apprentissage sont les suivantes :",
    "a) La cessation d'activité de l'employeur ;",
    "b) La faute de l'employeur ou les manquements répétés à ses obligations ;",
    "c) La mise en œuvre de la procédure de suspension de l'exécution du contrat d'apprentissage prévue aux articles L. 6225-4 et suivants ;",
    "4° La dérogation prévue au 2° de l'article L. 6222-2 s'applique également à l'inaptitude physique et temporaire de l'apprenti constatée dans les conditions prévues à l'article L. 6222-18.",
    "La suppression des conditions d'âge et de délai prévues aux 1° et 2° du présent article s'applique aux admissions restant à examiner et aux apprentissages commencés à compter de l'entrée en vigueur de la loi portant réforme du contrat de travail, y compris après un apprentissage antérieur à cette entrée en vigueur. Les admissions déjà accordées et les droits antérieurement constitués sont conservés ; aucune admission valable n'est remise en cause. Les dérogations distinctes prévues aux 3°, 4° et 5° de l'article L. 6222-2 demeurent applicables dans leurs conditions propres.",
    "Pour les nouveaux contrats uniques à durée indéterminée, ces règles concernent l'accès à une période d'apprentissage. Elles ne fixent aucun terme à l'emploi. Le seul achèvement d'une période pédagogique ne vaut pas rupture du contrat de travail pour l'application de la dérogation du 2° de l'article L. 6222-2. Aucun nouveau contrat à durée déterminée ni renouvellement à terme d'un ancien contrat n'est conclu sur le fondement du présent article.")
a = add(6, p,
    "La seconde passe retire le plafond réglementaire de trente-cinq ans pour les dérogations de progression de qualification et de rupture indépendante de la volonté ou d'inaptitude temporaire. Ces situations, légalement dispensées de la limite générale par L. 6222-2, ne justifient pas une seconde fermeture de l'accès à la formation à trente-cinq ans. La suppression antérieure du délai de reprise d'un an est conservée. Les cas légaux, les trois causes a) à c), la constatation médicale et les dérogations propres au handicap, à la création ou reprise d'entreprise et au sport de haut niveau restent applicables aux situations futures. Le 4° elliptique est explicité, sans nouvelle cause d'inaptitude.",
    "L. 6222-2 a été lu intégralement dans le corpus : ses 1° et 2° écartent la limite générale de vingt-neuf ans, sans imposer eux-mêmes trente-cinq ans ou un an d'interruption. La réforme ne supprime pas l'âge général hors de ces cas et n'assouplit pas les qualifications requises. Le 2° exige une vraie rupture indépendante de la volonté ou une inaptitude physique temporaire : une simple fin de formation dans un emploi poursuivi n'est pas assimilée à cette rupture. L. 6222-18 fourni distingue les régimes de rupture ancien et proposé ; le constat médical ne devient pas une faculté de licenciement discrétionnaire. L. 6225-4 et L. 6225-5 ont été lus : maintien du salaire et protection contre les risques graves subsistent, avec leurs indemnités spéciales. Les limites d'aide et leurs autres conditions restent propres à chaque dispositif ; aucun financement universel de l'apprentissage n'est inventé. La note du décret de 2020 conserve sa portée historique et ne fixe pas la date nouvelle. L. 6222-7 et L. 6222-7-1 nécessitent la coordination des périodes pédagogiques, sans CDD nouveau. Aucun nouveau renvoi normatif à une cible non fournie n'est ajouté.")
reduction(a,
    "Plafond supplémentaire de trente-cinq ans applicable aux deux dérogations légales de progression de qualification et de rupture indépendante de la volonté ou d'inaptitude temporaire.",
    "Délai maximal d'un an après le précédent contrat pour reprendre un apprentissage bénéficiant des dérogations des 1° et 2° de L. 6222-2.")
a['benefit_review'] = (
    "Les avantages sont les deux dérogations d'âge de L. 6222-2, 1° et 2°, pour une qualification supérieure ou une rupture subie/inaptitude temporaire, les causes admises a) cessation d'activité, b) faute ou manquements répétés de l'employeur, c) suspension protectrice, et la branche médicale du 4°. Ils demeurent ouverts aux futurs apprentissages recevables et sont élargis par le retrait du plafond de trente-cinq ans et du délai d'un an. Les dérogations distinctes pour handicap, projet de création ou reprise conditionné au diplôme et sportifs de haut niveau restent applicables sans ces anciennes restrictions ; les admissions valables et droits constitués sont conservés. Aucun taux d'aide, exonération ou droit social attaché à une situation par un autre texte n'est supprimé, et leur accès futur n'est pas conditionné à un ancien CDD. La durée pédagogique ne termine pas le nouvel emploi ; les autres critères d'aide restent propres à leurs textes.")
impact(a, 'material_reduction',
    "Deux restrictions réglementaires d'accès sont effectivement retirées par rapport à la source entière : trente-cinq ans et l'interruption maximale d'un an. Le premier retrait est supplémentaire au brouillon. Les autres cas et garanties restent entiers.",
    "La limite générale de vingt-neuf ans hors dérogation et les conditions légales des cinq cas restent applicables. L'éligibilité à une aide particulière n'est pas automatiquement démontrée par cette seule ouverture ; aucun coût public n'est estimé.",
    "Aucune charge nouvelle n'est identifiée : aucune demande ou preuve de remplacement n'est créée, le régime de constatation médicale et les causes préexistantes sont maintenus. Le rattachement à une période pédagogique évite une nouvelle règle d'âge liée à une simple continuation d'emploi.",
    [effect('relief_extended','apprentissage-derogations-sans-age-additionnel',
        "Ouvrir sans plafond réglementaire supplémentaire les deux dérogations légales.",
        "Pour les cas de L. 6222-2, 1° et 2°, âge de trente-cinq ans au plus à la conclusion du contrat.",
        "Aucun âge supérieur maximal dans ces deux cas, avec maintien de leurs conditions légales ; âge général et autres dérogations hors de cette suppression ciblée.",
        'other',"Personnes en progression de qualification ou reprenant après rupture subie ou inaptitude temporaire, dont celles de plus de trente-cinq ans.",
        "Admissions restant à examiner et apprentissages commencés après l'entrée en vigueur ; admissions valables et droits antérieurs conservés.",
        "Aucune autorisation, déclaration ou condition de financement de remplacement.",
        "1° Pour les dérogations prévues aux 1° et 2°, l'âge de l'apprenti au moment de la conclusion du contrat est de trente-cinq ans au plus ;",
        "1° Pour les dérogations prévues aux 1° et 2° de cet article, aucune limite d'âge supérieure n'est exigée ;"),
     effect('relief_extended','apprentissage-reprise-sans-delai-maximal',
        "Maintenir l'accès dérogatoire après une interruption supérieure à un an.",
        "Nouveau contrat souscrit au plus tard un an après l'expiration du précédent pour les dérogations de L. 6222-2, 1° et 2°.",
        "Aucun délai maximal de reprise dans ces deux cas ; conditions légales de progression ou de rupture subie et d'inaptitude maintenues.",
        'other',"Personnes relevant des deux dérogations légales après une interruption d'apprentissage.",
        "Même application aux nouvelles admissions et admissions restant à examiner, y compris après un ancien apprentissage ; droits déjà accordés conservés.",
        "Aucun justificatif d'interruption d'une durée autorisée ni procédure équivalente créée.",
        "2° Pour les dérogations prévues aux 1° et 2°, le contrat d'apprentissage doit être souscrit dans un délai maximum d'un an après l'expiration du précédent contrat ;",
        "2° Pour les dérogations prévues aux 1° et 2° du même article, aucun délai maximal entre le précédent apprentissage et le nouvel apprentissage n'est exigé ;")])

# R6222-6 : convention intégrable, consentement et bornes pédagogiques conservés.
p = SOURCES[7]['previous_draft']['proposed_xml']
p += paragraphs("L'aménagement de la période pédagogique ne permet aucun nouveau contrat à durée déterminée ni renouvellement à terme après cette entrée en vigueur. Les dispenses de convention mentionnées au deuxième alinéa ne sont subordonnées à aucune convention intégrée ni à une déclaration de remplacement.")
a = add(7, p,
    "Réforme de fond conservée : la convention d'aménagement peut être intégrée au document de formation, sans annexe, modèle ou signature répétée ; les évaluations pertinentes déjà réalisées sont réutilisées. Le consentement des parties reste requis et les centres internes conservent la signature de l'employeur et de l'apprenti ou de son représentant légal. La seconde passe ne retire pas les bornes de six mois et trois ans, fixées par la loi et liées à la formation certifiante, ni l'évaluation utile ; leurs exceptions et dispenses sont expressément sauvegardées. La période pédagogique ne fixe pas la durée du contrat unique.",
    "L. 6222-7-1 fourni place la convention au troisième alinéa, même dans sa proposition à laquelle un paragraphe transitoire est ajouté ; « dernier alinéa » deviendrait inexact. Sa proposition conserve néanmoins les mots exigeant une convention signée et annexée. Coordination législative indispensable, non effectuée sur ce fichier en lecture seule : au troisième alinéa, dernière phrase, autoriser l'intégration dans la convention de formation et supprimer l'exigence d'annexe matériellement distincte, en maintenant l'accord du CFA, de l'employeur et de l'apprenti ou représentant légal. L'intégration proposée ici ne peut prévaloir réglementairement sur la loi non coordonnée. Nouveaux renvois non fournis comme cibles : L. 6222-11, L. 6222-12-1 et L. 6353-1 ont été lus intégralement dans le corpus ; le premier conserve sa prolongation d'un an au plus pour échec, le deuxième sa phase initiale de trois mois avant employeur, le dernier sa convention acheteur-organisme. Les cibles fournies R. 6222-9 et R. 6222-23-1 dispensent de convention dans leurs champs respectifs et ce dernier autorise des minima réduits pour la reprise après rupture. Les dérogations handicap et sport de haut niveau ne sont pas enfermées dans le plafond ordinaire. D. 6224-1 et D. 6275-1 ont été lus : coordonner leurs dossiers privés et publics, sans attribution automatique du statut privé à un agent public. L'arrêté de modèle doit perdre son caractère obligatoire avec R. 6222-7 ; son annexe externe n'est pas présentée comme lue ou réécrite.")
reduction(a,
    "Document d'aménagement matériellement séparé et réitération de signatures déjà recueillies lorsque les parties ont accepté par écrit l'intégration à la convention de formation.",
    "Nouvelle évaluation répétant une évaluation déjà réalisée et toujours pertinente pour apprécier les mêmes compétences de l'apprenti.")
impact(a, 'material_reduction',
    "La proposition permet un document conventionnel commun au lieu de la convention séparée et réutilise les évaluations pertinentes ; les protections pédagogiques et accords ne sont pas supprimés. Ce gain reste subordonné à une coordination législative expressément identifiée, dont la cible fournie contient encore l'exigence d'annexe.",
    "Le texte réglementaire ne suffit pas à écarter la dernière phrase du troisième alinéa de L. 6222-7-1. Les six mois et trois ans restent la règle, avec toutes les dérogations citées ; aucun coût évité n'est mesuré.",
    "Aucune charge nouvelle n'est identifiée : l'accord écrit et l'évaluation existent déjà, les documents communs sont facultatifs, les signatures et pièces pertinentes sont réutilisées et les dispenses ne reçoivent aucune attestation de remplacement.",
    [effect('obligation_merged','apprentissage-convention-sans-doublon',
        "Réunir l'aménagement et la convention de formation sans refaire les éléments acceptés.",
        "Convention d'aménagement spécifique après évaluation ; L. 6222-7-1 exige sa signature et son annexion au contrat.",
        "Intégration possible à la convention de formation avec les accords écrits requis ; pas de document séparé ni de signature ou évaluation répétée lorsque les éléments restent pertinents.",
        'legal_duty','Employeurs, apprentis ou représentants légaux et centres de formation.',
        "Conventions nouvelles à l'entrée en vigueur ; anciennes valides sans les refaire ; coordination législative de l'annexe requise pour rendre l'intégration pleinement opérante.",
        "Accords et contenu nécessaires conservés, aucune déclaration équivalente ; dispenses spéciales maintenues.",
        "La durée du contrat ou de la période d'apprentissage peut être réduite ou allongée par la convention prévue au dernier aliéna de l'article L. 6222-7-1, après évaluation par le centre de formation d'apprentis du niveau initial de compétence de l'apprenti ou de ses compétences acquises.",
        "Aucun document séparé, modèle imposé ni nouvelle signature des éléments déjà acceptés n'est exigé.")])

# R6222-7 : le modèle obligatoire disparaît, la convention de fond reste.
a = add(8, SOURCES[8]['previous_draft']['proposed_xml'],
    "Abrogation de fond conservée : suppression complète de l'habilitation à imposer un modèle ministériel de convention. La durée adaptée, son évaluation et l'accord des parties demeurent établis selon leurs textes ; le format obligatoire ne porte pas de protection autonome démontrée. Toute la norme de format est déjà supprimée par le brouillon, de sorte qu'une coupe supplémentaire dans cet article retirerait des garanties transitoires ou favorables, non une obligation subsistante.",
    "Le troisième alinéa de L. 6222-7-1 fourni reste celui de la convention ; sa proposition conserve l'annexion, dont la coordination requise est identifiée dans R. 6222-6 du lot. La suppression du modèle ne dispense pas du consentement requis. L'arrêté pris pour R. 6222-7 est un texte extérieur au lot : retirer sa portée obligatoire et les refus automatiques fondés sur son seul format ; son numéro et son annexe ne sont pas inventés. D. 6224-1 et D. 6275-1 ont été lus dans le corpus pour les dossiers privés et publics ; leurs pièces ne doivent pas rétablir le modèle. Les conventions antérieures sont valides et le financement des futures situations recevables reste ouvert. Aucun nouveau renvoi opératoire à une cible non fournie n'est créé.")
repeal(a, "Suppression de l'obligation de recourir au modèle ministériel pour la convention d'aménagement de l'apprentissage, avec maintien des conventions antérieures, du consentement et des conditions de fond pour les financements futurs.")
impact(a, 'material_reduction',
    "Le format ministériel imposé par la source disparaît entièrement pour l'avenir ; il reste utilisable volontairement. La convention et ses conditions de fond subsistent, avec absence de refus de dépôt ou de prise en charge fondé sur le seul défaut de modèle.",
    "L'arrêté d'application et les dossiers doivent être coordonnés, sans prétendre son annexe déjà réécrite. La contrainte législative d'annexion reste à traiter dans L. 6222-7-1 ; aucun gain chiffré n'est affirmé.",
    "Aucune charge nouvelle n'est identifiée : aucun modèle nouveau, déclaration, confirmation ou signature supplémentaire ne remplace le modèle obligatoire ; les conventions valides restent utilisables.",
    [effect('obligation_removed','apprentissage-convention-sans-doublon',
        "Supprimer le format ministériel obligatoire dans la même simplification des conventions.",
        "Modèle de convention tripartite déterminé par arrêté ministériel sur le fondement de cet article.",
        "Aucun modèle obligatoire ; choix volontaire du modèle antérieur sans motif de refus tiré du seul format.",
        'legal_duty','Employeurs, apprentis ou représentants légaux, CFA et organismes de dépôt ou de financement.',
        "À l'entrée en vigueur ; conventions antérieures valides et conventions nouvelles ou modifiées couvertes.",
        "Convention de fond maintenue, aucune déclaration équivalente ni nouveau formulaire.",
        "Un arrêté du ministre chargé de la formation professionnelle détermine le modèle de la convention tripartite prévue au dernier alinéa de l'article L. 6222-7-1.",
        "Aucun modèle fixé par arrêté n'est obligatoire pour la convention d'aménagement de la période d'apprentissage prévue à l'article L. 6222-7-1.")])

# R6222-8 : renvoi déplacé par la proposition législative, pas de coupe de la certification.
a = add(9, SOURCES[9]['previous_draft']['proposed_xml'],
    "Coordination nécessaire, sans réduction autonome revendiquée : le renvoi vise le troisième alinéa, où figure réellement la convention dans L. 6222-7-1 proposé. La réserve relative aux obligations d'inscription protège l'accès au diplôme ; l'aménagement de durée et la suppression du formulaire n'y suppléent pas. Après seconde passe, supprimer cette réserve pourrait faire croire qu'un accord de durée suffit à être inscrit ; aucune pièce ou procédure distincte n'est exigée par l'article lui-même. La qualification reste préparée dans une période pédagogique sans terme d'emploi.",
    "L. 6222-7-1 source comprend trois alinéas textuels ; sa proposition en ajoute un quatrième. « Dernier alinéa » ne viserait donc plus la convention : le troisième est expressément retenu. L'identité du diplôme ou titre reste celle mentionnée au contrat, avec les mises à jour valablement convenues ; aucune autorisation d'embauche par le certificateur n'est créée. R. 6222-6 et R. 6222-7 sont coordonnés dans ce lot, sous réserve de la correction législative d'annexion identifiée. Les inscriptions antérieures demeurent valables et les nouvelles situations recevables restent ouvertes. Aucun nouveau renvoi à une cible non fournie n'est ajouté.")
impact(a, 'coordination_only',
    "La réserve de certification est maintenue intégralement dans son champ ; seul le renvoi à l'alinéa et l'articulation avec la période d'apprentissage sont rendus opérants. Il n'est revendiqué aucune disparition d'obligation d'inscription.",
    "Les règles de l'organisme certificateur ne sont pas réécrites ou chiffrées. La suppression du modèle de convention est une mesure distincte coordonnée, pas une seconde réduction ici.",
    "Aucune charge nouvelle n'est identifiée : les obligations d'inscription sont celles déjà réservées par la source, sans agrément de l'emploi, nouveau dossier ou exigence de preuve.",
    [effect('coordination','apprentissage-convention-sans-doublon',
        "Conserver la réserve d'inscription malgré la simplification de la convention et rectifier l'alinéa.",
        "Convention du dernier alinéa conclue sans préjudice des obligations d'inscription au diplôme ou titre du contrat.",
        "Aménagement du troisième alinéa soumis aux mêmes obligations d'inscription, sans leur donner un effet de terme sur l'emploi unique.",
        'regime','Apprentis, CFA et organismes certificateurs.',
        "Nouveaux contrats uniques à compter de l'entrée en vigueur ; conventions et inscriptions antérieures valables.",
        "Aucune obligation autonome nouvelle ; pas d'autorisation d'embauche par le certificateur.",
        "La convention tripartite prévue au dernier alinéa de l'article L. 6222-7-1 est conclue sans préjudice du respect des obligations fixées par l'organisme certificateur pour l'inscription au diplôme ou titre à finalité professionnelle mentionné dans le contrat d'apprentissage.",
        "L'aménagement convenu dans les conditions prévues au troisième alinéa de l'article L. 6222-7-1 ne dispense pas du respect des obligations fixées par l'organisme certificateur pour l'inscription au diplôme ou au titre à finalité professionnelle mentionné dans le contrat d'apprentissage.")])

# R6222-9 : la dispense reste pour tous les cas, futurs aussi.
a = add(10, SOURCES[10]['previous_draft']['proposed_xml'],
    "Coordination et maintien de la dispense favorable entière : les quatre renvois couvrent l'échec au diplôme, la formation débutée avant employeur, le handicap et le sport de haut niveau. Aucune convention intégrée ne doit contourner la dispense existante. La seconde passe ne supprime pas cette exonération de formalité, ne la réserve pas aux anciens contrats et ne la présente pas comme une formalité abolie une seconde fois. Le troisième alinéa est celui réellement visé dans la proposition législative fournie.",
    "L. 6222-11 et L. 6222-12-1 ont été lus dans le corpus : prolongation pédagogique d'un an au plus après échec et réduction liée aux mois déjà écoulés d'une formation commencée avant employeur. Le 2° de L. 6222-37 et le 1° de L. 6222-40 fournis concernent seulement leurs aménagements de durée, non toutes leurs autres dispositions. Les bornes générales de R. 6222-6 ne doivent pas neutraliser ces cas et la dispense supplémentaire de R. 6222-23-1 reste distincte. Les modifications des articles législatifs de durée doivent exclure tout nouveau CDD ; leur terme pédagogique ne rompt pas l'emploi. L. 6222-7-1 proposé conserve une exigence d'annexe à coordonner, mais cela ne restreint pas les dispenses. Aucun nouveau renvoi normatif à une cible non fournie n'est ajouté : les deux articles non fournis mentionnés au début de ces notes sont déjà des renvois source.")
impact(a, 'coordination_only',
    "La source contient déjà une dispense dans quatre cas et la proposition la conserve, y compris pour les futurs apprentissages sous contrat unique. La correction du renvoi et l'interdiction du document de remplacement ne sont pas comptées comme quatre suppressions nouvelles.",
    "Les conditions des quatre régimes demeurent propres à leurs textes, dont toutes les coordinations de durée ne sont pas réalisées dans ce lot. Aucune baisse de prélèvement ni économie chiffrée n'est démontrée ici.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation, convention intégrée ou déclaration ne remplace la convention dispensée ; les anciens cas et les futurs bénéficiaires restent couverts.",
    [effect('relief_preserved','apprentissage-convention-sans-doublon',
        "Préserver la dispense de convention sans la fermer aux futures situations.",
        "Dispense pour L. 6222-11, L. 6222-12-1, L. 6222-37, 2°, et L. 6222-40, 1°.",
        "Mêmes quatre cas et subdivisions, avec dispense de document séparé ou intégré et de déclaration équivalente dans les apprentissages futurs éligibles.",
        'legal_duty','Apprentis et employeurs relevant des quatre cas de dispense.',
        "Anciens contrats et nouveaux contrats uniques à compter de l'entrée en vigueur ; prolongation ou réduction limitée à la période de formation.",
        "Aucune formalité de remplacement ; pas d'extension générale de tous les autres régimes spéciaux.",
        "La conclusion de la convention tripartite prévue au dernier alinéa de l'article L. 6222-7-1 n'est pas requise dans les cas prévus aux articles L. 6222-11 et L. 6222-12-1, au 2° de l'article L. 6222-37 et au 1° de l'article L. 6222-40.",
        "La convention prévue au troisième alinéa de l'article L. 6222-7-1 n'est pas exigée dans les cas prévus aux articles L. 6222-11 et L. 6222-12-1, au 2° de l'article L. 6222-37 et au 1° de l'article L. 6222-40.")])

# R6222-21 : deux premiers alinéas conservent leurs fonctions ; suite transitoire complète.
p = paragraphs(
    "La rupture du contrat d'apprentissage ou de la période d'apprentissage est constatée par écrit dans les conditions des articles L. 6222-18 à L. 6222-19. Pour les contrats conclus avant l'entrée en vigueur de la loi portant réforme du contrat de travail, ces conditions et les droits antérieurement constitués demeurent ceux qui leur étaient applicables.",
    "À compter de cette entrée en vigueur, l'écrit de rupture est communiqué une seule fois au directeur du centre de formation d'apprentis. Celui-ci transmet l'information et l'écrit nécessaires à l'organisme chargé du dépôt du contrat dans les conditions légales de protection des données. Aucune seconde notification de la même rupture n'est exigée de son auteur. Cette règle s'applique également aux notifications restant à accomplir pour un contrat antérieur ; les notifications déjà valablement effectuées ne sont pas refaites.",
    "Pour les nouveaux contrats uniques à durée indéterminée, une rupture de la seule période d'apprentissage, la fin de la formation ou l'obtention du diplôme ne rompent pas, par elles-mêmes, l'emploi. La rupture de l'emploi est distinctement notifiée par écrit à l'autre partie. Lorsqu'elle intervient à l'initiative de l'employeur ou du salarié, le préavis individuel est de quinze jours calendaires, sous réserve des dispenses favorables légalement ouvertes au salarié. Il se compte à partir du lendemain de la présentation de la notification patronale ou, lorsqu'une autre forme de notification est légalement admise, de sa réception ou remise au salarié ; pour une notification du salarié, il se compte à partir du lendemain de sa réception par l'employeur. Il expire à la fin du quinzième jour, même non travaillé, dans les conditions de l'article L. 1234-3. La communication au centre de formation ne remplace pas cette notification à l'autre partie.",
    "Lorsqu'un essai est expressément stipulé dans le nouveau contrat, sa durée ne peut dépasser trois mois, sous réserve des durées plus courtes applicables ; il ne peut être renouvelé. La fin ou le changement d'une phase pédagogique ou d'une mission ne crée pas un nouvel essai. Le préavis ne prolonge pas l'essai ; le reliquat patronal qui ne peut être exécuté avant son échéance est compensé, sans allonger l'ancienneté effective au-delà de ce terme. La première année de l'emploi ne constitue pas une période d'essai.",
    "L'indemnité ordinaire de rupture du nouveau contrat n'est due qu'en cas de rupture à l'initiative de l'employeur dans les conditions de l'article L. 1234-9, notamment sous réserve de l'exception de faute grave. Aucune indemnité ordinaire n'est due avant un an d'ancienneté. Lorsque ce seuil est atteint, elle est égale à 0,20 mois de salaire brut de référence par année d'ancienneté totale, les fractions d'année étant calculées au prorata des mois complets, dans la limite de six mois de ce salaire. Le seuil et l'ancienneté sont appréciés à la fin effective du contrat, préavis exécuté ou non inclus, sous la réserve relative à la fin de l'essai prévue à l'alinéa précédent. La première année n'est pas soustraite du calcul. La démission ordinaire n'ouvre pas cette indemnité.",
    "Les anciens contrats et leurs droits acquis conservent leurs dispositions transitoires. Une conversion convenue conserve l'ancienneté et les créances acquises. La composante d'indemnité correspondant aux services antérieurs à la réforme conserve son régime et ses minima selon l'article L. 1234-9 ; une même période n'est pas comptée deux fois. Les indemnités conventionnelles ou contractuelles plus favorables ne sont pas réduites par le plafond de l'indemnité légale ordinaire.",
    "Ces règles ne suppriment ni les salaires et congés acquis, ni l'indemnité de préavis, ni les réparations d'une rupture illégale, ni les indemnités spéciales. L'inaptitude professionnelle conserve notamment son indemnité spéciale sans condition minimale d'ancienneté, son salaire de référence propre et le doublement du montant qui lui sert de base, y compris le doublement du plafond lorsqu'il est applicable à cette base. La rupture patronale demeure soumise aux conditions de motif, de défense et de contrôle qui lui sont applicables. Les protections de santé, de maternité et de représentation, la non-discrimination et le recours au juge demeurent. La signature et l'intervention du représentant légal du mineur lorsqu'elles sont requises, les autorisations de salariés protégés, les procédures collectives ainsi que la suspension, le maintien de rémunération et les réparations propres aux mesures de sécurité des articles L. 6225-4 et L. 6225-5 ne sont pas supprimés par le préavis individuel.",
    "Le présent article n'étend pas le régime du contrat unique aux fonctionnaires ou agents publics. Les contrats d'apprentissage de droit privé conclus par une personne publique relèvent de leurs dispositions spéciales coordonnées ; la simplification de communication prévue au deuxième alinéa ne modifie pas, à elle seule, leur régime de durée ou de rupture.")
a = add(11, p,
    "Réforme de fond conservée et précisée : une seule communication par l'auteur de la rupture remplace les deux notifications aux organismes ; le CFA assure le relais. Ce relais est une tâche nouvelle pour le CFA, explicitement recensée. Le régime des nouveaux apprentissages est coordonné au contrat unique, sans fin automatique liée au diplôme, et le préavis part désormais explicitement du lendemain de la notification, contrairement à la formule imprécise du brouillon. Le prorata est celui des mois complets, non un prorata journalier. Les conditions et avantages des anciens contrats, les protections des mineurs et les indemnités spéciales sont conservés. La seconde passe évite une nouvelle démarche de rupture de l'emploi lors de la seule fin de formation, mais ne retire ni la preuve écrite ni l'information des organismes, nécessaires à la continuité de formation et au financement.",
    "L. 6222-18 fourni oppose l'ancien régime des quarante-cinq jours pratiques, puis accord ou cas légaux et médiation préalable, au régime nouveau. La médiation du majeur ne doit pas redevenir préalable obligatoire et les délais de cinq puis sept jours de D. 6222-21-1 ne s'ajoutent pas au nouveau préavis. Cet article a été lu dans le corpus, ainsi que L. 6222-19 et L. 6222-18-2 : coordination des départs favorables après diplôme et maintien de six mois de formation théorique avec statut de stagiaire après rupture. Le relais d'information par le CFA doit aussi coordonner la copie prévue dans L. 6222-18 pour éviter un second envoi de la même pièce. L. 1234-9 fourni conserve l'exception de faute grave pour l'indemnité ordinaire ; la faute grave n'écarte pas le préavis nouveau selon L. 1234-1 proposé. Le salaire de référence et les mois complets ont été vérifiés avec R. 1234-1, R. 1234-2 et R. 1234-4 du corpus : fenêtres de salaire avant notification, non décalées à la fin du préavis ; seuil d'un an apprécié au terme effectif ; composantes anciennes sans double compte. L. 1226-14 et L. 1226-16 ont été lus pour l'inaptitude professionnelle : pas de seuil d'un an, salaire propre, doublement et absence de plafond ordinaire de six mois appliqué directement à l'indemnité spéciale. Les mesures de L. 6225-4 et L. 6225-5 restent autonomes, même si la proposition de L. 6222-18 supprime en liquidation l'indemnité automatique égale à la formation restant à courir : ne pas étendre cette suppression au refus de reprise pour risque grave. Nouveaux renvois opératoires non fournis comme cibles : L. 1234-3, L. 6225-4 et L. 6225-5 ont été lus dans le corpus ; aucune empreinte de vue fournie ne leur est inventée. L. 1221-19, L. 1221-21, L. 1221-23, L. 1221-25 et L. 1221-26 ont été lus : essai stipulé, plafond trois mois sans renouvellement, reliquat patronal payé et ancienneté non prolongée après l'essai. L. 6227-1 et L. 6227-2 ont été lus : l'apprentissage de droit privé auprès d'un employeur public ne doit pas être confondu avec le statut des agents publics ; sa durée relève de la coordination législative distincte déjà proposée. Les délais collectifs et les autorisations ne sont pas absorbés par les quinze jours.")
reduction(a,
    "Seconde notification de la même rupture à l'organisme chargé du dépôt, remplacée pour son auteur par une communication unique au CFA qui assure le relais institutionnel.",
    "Application aux nouveaux emplois d'apprentis d'un terme automatique ou d'un régime autonome de rupture à durée déterminée lié à la fin de la formation, sous réserve de la coordination législative du contrat unique.")
impact(a, 'mixed',
    "La double notification de la source est fusionnée pour son auteur, avec transfert d'une tâche au CFA. Les règles nouvelles de rupture sont coordonnées aux cibles législatives, et non comptées comme une seconde baisse d'indemnité. Le préavis uniforme peut accroître la durée à respecter par certains apprentis : le solde net de charges n'est pas établi.",
    "L. 6222-18 et les autres dispositions législatives doivent recevoir leurs coordinations effectives ; le règlement seul ne supprime pas leurs anciennes procédures. La continuité de formation, les mineurs, l'inaptitude professionnelle et les agents publics gardent leurs champs. Aucun bilan global de coût n'est calculé.",
    "Charge nouvelle identifiée : le CFA doit relayer l'information et l'écrit au dépositaire, ce que les deux notifications de la source ne lui imposaient pas. La notification écrite entre les parties et le préavis uniforme procèdent des cibles coordonnées ; quinze jours peuvent allonger le préavis du salarié par rapport aux anciennes ruptures libres pendant quarante-cinq jours pratiques ou au délai de sept jours après information. Aucun registre, attestation ou délai supplémentaire de dépôt n'est créé. Le solde net n'est pas démontré.",
    [effect('obligation_merged','apprentissage-notification-rupture-unique',
        "Faire communiquer l'écrit une seule fois par son auteur, puis relayer par le CFA.",
        "Rupture notifiée au directeur du CFA et à l'organisme de dépôt, soit deux destinataires à desservir par son auteur.",
        "Une communication de l'auteur au CFA ; le CFA transmet au dépositaire, sans seconde notification à la charge de l'auteur.",
        'legal_duty',"Auteurs de ruptures d'apprentissage, CFA et organismes de dépôt.",
        "Notifications restant à accomplir après l'entrée en vigueur, même pour ancien contrat, sans refaire les envois valables.",
        "Relais nouveau à la charge du CFA, recensé séparément ; écrit de rupture et protection des données conservés.",
        "Elle est notifiée au directeur du centre de formation d'apprentis ainsi qu'à l'organisme chargé du dépôt du contrat.",
        "Aucune seconde notification de la même rupture n'est exigée de son auteur."),
     effect('obligation_added','apprentissage-notification-rupture-unique',
        "Assigner au CFA la transmission au dépositaire, contrepartie de la communication unique.",
        "Le CFA et l'organisme de dépôt sont tous deux destinataires, sans obligation de relais confiée au CFA dans l'article source.",
        "Le directeur du CFA reçoit puis transmet l'information et l'écrit nécessaires à l'organisme de dépôt.",
        'legal_duty',"Centres de formation d'apprentis recevant les écrits de rupture.",
        "Même transition que la communication unique ; données nécessaires seulement et aucun envoi déjà valable à refaire.",
        "Tâche de transmission nouvelle pour le CFA ; aucune nouvelle collecte ou durée de conservation n'est instituée ici. Gain net non chiffré.",
        "Elle est notifiée au directeur du centre de formation d'apprentis ainsi qu'à l'organisme chargé du dépôt du contrat.",
        "Celui-ci transmet l'information et l'écrit nécessaires à l'organisme chargé du dépôt du contrat dans les conditions légales de protection des données."),
     effect('coordination','contrat-unique-preavis-quinze-jours',
        "Coordonner le régime nouveau de rupture et son point de départ, avec ses charges possibles pour le salarié.",
        "Renvoi au régime spécial de L. 6222-18 à L. 6222-19 : notamment quarante-cinq jours pratiques de rupture libre puis procédures particulières ; pas de préavis uniforme de quinze jours dans l'article source.",
        "Emploi nouveau sans terme, préavis individuel de quinze jours des deux côtés à compter du lendemain de la notification légalement reçue ou présentée ; dispenses favorables, procédures collectives et protections spéciales préservées.",
        'calendar_days','Nouveaux apprentis de droit privé en contrat unique et leurs employeurs.',
        "Nouveaux contrats après l'entrée en vigueur ; anciens régimes et droits conservés ; fin d'essai non prolongée par le reliquat patronal payé.",
        "Quinze jours peuvent être plus longs que le régime antérieur de certains départs d'apprentis ; aucune baisse universelle de délai n'est revendiquée. Motif, défense, sécurité et recours préservés.",
        "La rupture anticipée du contrat d'apprentissage ou de la période d'apprentissage fait l'objet d'un document écrit, dans les conditions prévues aux articles L. 6222-18 à L. 6222-19.",
        "Lorsqu'elle intervient à l'initiative de l'employeur ou du salarié, le préavis individuel est de quinze jours calendaires, sous réserve des dispenses favorables légalement ouvertes au salarié."),
     effect('coordination','contrat-unique-indemnite-ordinaire',
        "Appliquer le barème légal coordonné sans créer une seconde suppression ni plafonner les indemnités spéciales.",
        "Régime spécial de rupture renvoyé à L. 6222-18 à L. 6222-19 ; article réglementaire source sans barème ordinaire propre.",
        "Dans les conditions de L. 1234-9 : employeur seul et exception de faute grave, zéro avant un an au terme effectif, puis 0,20 mois de salaire brut de référence par année totale, fractions selon mois complets, plafond légal six mois ; indemnités spéciales et plus favorables préservées.",
        'other',"Salariés et employeurs relevant du nouveau contrat unique d'apprentissage ; anciens contrats pour leur seule transition.",
        "Préavis inclus dans l'ancienneté sauf fin d'essai ; aucune première année soustraite après seuil ; composante antérieure et minima conservés sans double compte.",
        "Pas de nouveau taux ou prélèvement ; une simple démission ne crée pas d'indemnité ordinaire. Salaires, congés, illégalité et doublement sans seuil de l'inaptitude professionnelle restent distincts.",
        "dans les conditions prévues aux articles L. 6222-18 à L. 6222-19.",
        "Lorsque ce seuil est atteint, elle est égale à 0,20 mois de salaire brut de référence par année d'ancienneté totale, les fractions d'année étant calculées au prorata des mois complets, dans la limite de six mois de ce salaire.")])

# Analyses des cibles : les textes proposés sont distingués des sources officielles.
BASE_CHECKS = {
 'R5221-44': {
  'L1234-1': "La cible propose quinze jours pour les ruptures patronales des nouveaux contrats, sans ancienneté minimale et avec paiement même en faute grave ; R. 5221-44 ne traite que de la réutilisation d'une vérification du titre. La validité du titre n'est donc ni un préavis ni une dispense de protection ; les anciens contrats gardent leur préavis propre.",
  'L1221-2': "La source autorise encore les CDD, tandis que la proposition interdit tout nouveau terme ou renouvellement à terme. La dispense couvre donc les affectations du contrat unique de la même entreprise de travail temporaire ; seuls les contrats antérieurs conservent leur régime jusqu'à leur terme, sans nouvelle vérification causée par la conversion seule.",
  'L1234-9': "Le titre de séjour et sa vérification ne conditionnent pas le barème ordinaire. Le seuil proposé d'un an au terme effectif, préavis inclus, le calcul sur l'ancienneté totale à 0,20 mois par année et le plafond de six mois ne sont ni modifiés ni étendus par R. 5221-44 ; les créances antérieures restent distinctes."
 },
 'R5312-32': {
  'L1234-1': "Les transmissions d'allocations ne constatent pas une notification de licenciement et ne fixent aucun point de départ du préavis. Les quinze jours proposés pour les nouveaux contrats et les règles des anciens contrats n'imposent aucune donnée ou transmission supplémentaire dans R. 5312-32.",
  'L1221-2': "Les trois finalités de R. 5312-32 ne reposent pas sur l'existence d'un CDD. Les renvois entiers aux aides et parcours continuent donc pour le contrat unique futur ; une durée d'aide ou d'accompagnement ne vaut ni terme d'emploi ni motif de collecte additionnelle. Les contrats anciens gardent leur transition.",
  'L1234-9': "Le traitement d'allocations n'est pas un calcul d'indemnité de licenciement : les conditions de huit mois pour les anciens contrats et d'un an au terme effectif pour les nouveaux ne sont pas importées dans l'éligibilité aux aides. Aucun barème de rupture ni droit acquis n'est supprimé par le maintien du traitement."
 },
 'D5422-3': {
  'L1234-1': "La liste porte sur des fins effectives imputables selon les accords, non sur la seule notification qui commence un préavis. Les quinze jours du régime nouveau n'autorisent pas à enregistrer une fin d'emploi lors d'une intermission ; les anciens préavis et les procédures distinctes restent à leur champ.",
  'L1221-2': "La proposition de L. 1221-2 exclut qu'une mission ou formation termine automatiquement l'emploi nouveau. D. 5422-3 le traduit pour les données : aucune fin fictive du contrat unique lors de la seule fin d'affectation. Les fins réelles des anciens contrats restent traitées selon leurs règles et leur imputabilité.",
  'L1234-9': "La communication permet de contrôler l'imputabilité pour l'assurance chômage, pas de liquider l'indemnité ordinaire. Le seuil d'un an au terme effectif et les composantes anciennes de L. 1234-9 proposé ne définissent pas les fins de contrat à communiquer ; l'existence ou non d'une indemnité ne remplace pas cette fin effective."
 },
 'D5424-22': {
  'L1234-1': "L'interdiction de licencier pendant l'inactivité reste une protection autonome. L'exception source de faute grave ne dispense pas du préavis nouveau payé de quinze jours prévu dans la cible proposée. Un préavis déjà notifié avant l'inactivité peut expirer pendant celle-ci ; les anciens contrats gardent leurs durées antérieures.",
  'L1221-2': "Le chantier ou son inactivité ne constitue pas un terme du contrat unique dans la proposition de L. 1221-2. Le texte source conservé de D. 5424-22 ne vise que le licenciement et l'expiration d'un préavis déjà donné, sans créer de fin automatique de chantier ni de nouveau CDD ; aucune correction de renvoi n'y est nécessaire.",
  'L1234-9': "La protection pendant l'inactivité n'est pas subordonnée à l'ancienneté ouvrant l'indemnité : elle vaut aussi avant un an pour les nouveaux contrats. Le zéro d'indemnité ordinaire avant ce seuil n'autorise aucun licenciement autrement interdit ; barème, faute grave et anciennes composantes restent régis par la cible."
 },
 'D5522-11': {
  'L1234-1': "Le déclencheur transitoire de l'abrogation est la notification de rupture, pas l'expiration du préavis. Que celui-ci soit de quinze jours pour un nouvel emploi ou reste ancien ne rétablit pas la reprise intégrale supprimée ; les notifications antérieures restent dans l'ancien régime avec leurs dispenses.",
  'L1221-2': "La durée d'aide de D. 5522-7 demeure distincte de la durée indéterminée des nouveaux emplois de L. 1221-2 proposé. L'abrogation protège aussi les futures aides éligibles et ne réserve pas l'avantage à un CDD ancien ; elle ne permet ni nouveau terme ni renouvellement à durée déterminée.",
  'L1234-9': "L'indemnité due au salarié et le reversement de l'aide à l'État sont deux dettes distinctes. Le seuil d'un an, les mois complets et le plafond du barème nouveau n'ont aucun effet sur la suppression de reprise de l'aide ; cette suppression ne supprime ni les créances salariales ni les minima antérieurs."
 },
 'D6123-37': {
  'L1234-1': "Les dates de transmission de fonds ou les périodes de rémunération ne sont pas des notifications de rupture. Le préavis individuel nouveau de quinze jours ne déclenche aucun état supplémentaire dans D. 6123-37 ; les règles de préavis des anciens contrats restent étrangères à ces catégories de données.",
  'L1221-2': "Les périodes d'apprentissage et de professionnalisation peuvent subsister au sein de l'emploi unique ; leurs effectifs restent utilisables pour les droits favorables sans fin fictive du contrat. L'extinction CPF-CDD s'applique aussi aux rémunérations futures d'anciens CDD, non aux seules nouvelles embauches ; aucune mission ne recrée un CDD.",
  'L1234-9': "Les masses salariales servent aux contributions et financements de formation, non au seuil ni au salaire de référence de l'indemnité ordinaire. Le seuil proposé d'un an au terme effectif et les anciennes composantes n'autorisent ni données nouvelles de rupture ni perte d'un avantage de formation dans D. 6123-37."
 },
 'D6222-1': {
  'L1234-1': "Le délai d'un an supprimé est un délai maximal de reprise d'apprentissage, sans rapport avec le préavis de licenciement. Le plafond de trente-cinq ans supprimé ne change pas les quinze jours proposés pour le nouvel emploi ; les règles de notification et les anciens préavis demeurent à leur champ propre.",
  'L1221-2': "L'accès dérogatoire doit rester possible pour une nouvelle période pédagogique au sein d'un contrat unique sans terme. Le seul achèvement d'une formation n'est pas la rupture involontaire exigée par L. 6222-2, 2° ; l'élargissement d'âge et de délai ne rétablit aucun CDD ni renouvellement à terme après la réforme.",
  'L1234-9': "Le retrait du délai maximal d'un an d'interruption ne supprime ni ne modifie le seuil distinct d'un an d'ancienneté pour l'indemnité ordinaire. Les âges d'accès à la formation, le terme effectif incluant préavis et les composantes d'indemnité des anciens contrats sont des règles différentes ; aucune assimilation n'est faite."
 },
 'R6222-6': {
  'L1234-1': "Les six mois et trois ans sont des bornes de période pédagogique, pas de préavis ou d'emploi. L'accord d'aménagement ne vaut pas notification de rupture et ne dispense pas du préavis individuel de quinze jours pour le nouvel emploi ; les anciens contrats et leurs notifications restent soumis à leur transition.",
  'L1221-2': "La source permet l'aménagement de la durée d'un contrat limité ; la proposition ne l'admet pour le nouveau support que sur la période d'apprentissage. Le dernier paragraphe exclut expressément tout nouveau CDD ou renouvellement à terme, tout en sauvegardant les conventions antérieures et leurs droits.",
  'L1234-9': "L'accord de durée pédagogique ne remet aucune ancienneté à zéro et n'ouvre pas d'indemnité à sa fin si l'emploi continue. Le seuil d'un an et le calcul intégral à 0,20 mois, avec mois complets et plafond de six mois, ne concernent que les ruptures patronales éligibles ; l'ancien acquis reste régi par sa composante."
 },
 'R6222-7': {
  'L1234-1': "L'abrogation retire seulement le modèle de convention pédagogique, sans notification de rupture ni changement de préavis. Le nouveau délai individuel de quinze jours et le régime des anciens contrats restent définis par leurs textes ; un défaut de modèle ne devient pas un motif de rupture ou de privation de financement.",
  'L1221-2': "La convention sans modèle peut aménager une période d'apprentissage, jamais rétablir un terme d'emploi nouveau. La source de L. 1221-2 autorisait les CDD, sa proposition les exclut pour les nouvelles relations ; l'abrogation du format conserve les conventions antérieures sans en faire un support de renouvellement à terme.",
  'L1234-9': "Aucun droit à indemnité ni condition d'ancienneté n'est attaché au modèle supprimé. Les huit mois de l'ancien régime, l'année au terme effectif du nouveau et ses mois complets restent dans L. 1234-9 proposé et ses règlements ; le défaut de format ne peut effacer une composante d'indemnité acquise."
 },
 'R6222-8': {
  'L1234-1': "Les obligations d'inscription du certificateur n'organisent aucune rupture et ne fixent pas un préavis. Ni l'obtention du diplôme ni l'aménagement de formation ne font courir les quinze jours proposés ; une notification valable reste nécessaire pour le nouvel emploi, avec le régime distinct des anciens contrats.",
  'L1221-2': "La certification reste un objet de la période d'apprentissage au sein du contrat unique, pas une condition de terme de l'emploi. Le paragraphe nouveau de R. 6222-8 évite d'attribuer au certificateur un pouvoir de durée déterminée, en cohérence avec l'interdiction de nouveaux CDD et de renouvellements à terme.",
  'L1234-9': "L'inscription au diplôme n'est pas un fait générateur de l'indemnité ordinaire. Le seuil d'un an apprécié à la fin effective du contrat et le calcul de l'ancienneté totale ne sont pas remplacés par la durée du cycle ; les droits des anciens contrats et les indemnités spéciales ne sont pas réduits par cette réserve pédagogique."
 },
 'R6222-9': {
  'L1234-1': "La dispense porte sur une convention de durée d'apprentissage, pas sur la notification d'une rupture ou son préavis. Les quinze jours de L. 1234-1 proposé continuent à s'appliquer aux nouveaux emplois dans leur champ ; aucune fin automatique ni dispense patronale de préavis n'est déduite de R. 6222-9.",
  'L1221-2': "Les quatre dispenses doivent rester accessibles aux futurs apprentis sous contrat unique, et non être gelées aux anciens CDD. Les prolongations et réductions portent sur la phase pédagogique ; elles ne permettent ni nouveau terme de l'emploi ni renouvellement à terme, conformément à la cible proposée.",
  'L1234-9': "La dispense de convention ne dépend pas de l'ancienneté du salarié et ne vaut pas rupture indemnisable. L'année ouvrant l'indemnité ordinaire au terme effectif, l'ancienneté totale après seuil et la composante antérieure restent distinctes ; aucune réduction d'indemnité n'est produite ou revendiquée par la dispense."
 },
 'R6222-21': {
  'L1234-1': "La cible proposée fixe quinze jours indépendamment de l'ancienneté et conserve un préavis payé même en faute grave, contrairement à la source légale. Le texte de R. 6222-21 coordonne le lendemain de la notification selon L. 1234-3 et n'efface ni autorisations ni procédures collectives. Les anciens contrats gardent leur régime, sans nouveau délai ajouté à leur rupture.",
  'L1221-2': "L'emploi nouveau d'apprenti est sans terme : la rupture de la seule phase pédagogique, la fin de formation ou le diplôme ne le rompent pas automatiquement. L'écrit communiqué au CFA ne dispense donc pas d'une notification de rupture de l'emploi à l'autre partie ; les anciens contrats et conversions conservent ancienneté et créances.",
  'L1234-9': "La proposition fournie réserve l'indemnité ordinaire à la rupture patronale, avec exception de faute grave : cette exception est explicitée pour éviter une extension involontaire. Un an se mesure au terme effectif, préavis inclus sauf fin d'essai ; ensuite 0,20 mois par année totale, mois complets au prorata, six mois au maximum. Les anciennes composantes, minima plus favorables et indemnités spéciales restent distincts."
 }
}

EXTRA_CHECKS = {
 ('R5312-32','L5134-25-1'): "La source légale règle la prolongation du CDD d'accompagnement ; la proposition transfère les vingt-quatre mois, cinq ans et exceptions de formation ou d'âge cinquante-huit ans vers la période d'accompagnement et d'aide, sans terme d'emploi. Le renvoi entier du 3° de R. 5312-32 reste approprié : il ne doit pas exclure les futurs bénéficiaires en contrat unique ni garantir une aide dont les autres conditions manquent.",
 ('R5312-32','L5132-5'): "Le 3° de R. 5312-32 vise les dispositions d'insertion, non un alinéa particulier de CDD. La proposition de L. 5132-5 garde les parcours, mises en situation, prolongations favorables, retraite et départs sans préavis dans leur champ, en emploi sans terme ; son minimum spécial de vingt heures n'est pas le plancher général supprimé de vingt-quatre heures. Aucun nouveau filtre contractuel n'est ajouté au traitement de données.",
 ('D5422-3','L1251-1'): "Le 1° réellement visé demeure le contrat commercial entre l'entreprise de travail temporaire et l'utilisateur, y compris utilisateur public sous réserve de sa section spéciale. Le 2° proposé devient la lettre de mission d'un emploi unique ; sa fin n'est pas une fin d'emploi. D. 5422-3 maintient donc les fins de mise à disposition imputables selon les accords sans inventer une rupture du CDI à chaque mission.",
 ('D6123-37','L6131-1'): "La cible distingue le I, 3° (CSA : années à compter du 1er janvier suivant l'entrée en vigueur de sa suppression) du I, 4° (CPF-CDD : périodes de travail futures au jour d'entrée en vigueur, même sur ancien contrat), et du I, 5° conventionnel maintenu. Les rubriques et transitions de D. 6123-37 suivent ces deux calendriers sans couper les déductions, la créance ou les aides futures ni rétablir une contribution par état néant ; le II conserve les exclusions d'employeurs publics.",
 ('D6222-1','L6222-18'): "Le 4° source renvoie à la constatation d'inaptitude et non au délai d'essai. La cible officielle distingue les quarante-cinq jours pratiques, puis les cas et procédures de rupture ; sa proposition applique le contrat unique, conserve les mineurs et les anciens contrats. D. 6222-1 ne transforme ni l'inaptitude temporaire en rupture libre, ni la fin d'une phase pédagogique en rupture involontaire ; ses causes a) à c) et les protections de suspension restent nécessaires.",
 ('R6222-6','L6222-37'): "Le 2° vise les aménagements de durée pour les personnes handicapées, distincts des 1°, 3° à 6° sur accès, succession, départ, formation et temps de travail. La cible proposée conserve leur ouverture future dans la période pédagogique du contrat unique. Les bornes ordinaires de R. 6222-6 s'entendent sous réserve de ces aménagements, avec la dispense de convention de R. 6222-9, sans terme d'emploi ni remise à zéro d'ancienneté.",
 ('R6222-6','L6222-40'): "Seul le 1° de la cible concerne la durée de l'apprentissage des sportifs de haut niveau ; le 2° concerne leur temps de travail. La proposition fait porter l'aménagement sur la période pédagogique et garde les futurs bénéficiaires. R. 6222-6 ne rétablit pas sa borne générale contre l'exception et R. 6222-9 dispense toujours de la convention, indépendamment de son intégration matérielle.",
 ('R6222-6','L6222-7-1'): "La convention est au troisième alinéa dans la source ; elle y reste dans la proposition, dont le dernier alinéa devient transitoire. Le renvoi est rectifié. Les bornes de six mois et trois ans et leurs exceptions restent pédagogiques. La proposition fournie exige encore une convention signée et annexée : l'intégration et la suppression de l'annexe séparée proposées par R. 6222-6 nécessitent donc une modification expresse de cette dernière phrase législative, non réputée réalisée.",
 ('R6222-6','R6222-23-1'): "Cette cible dispense de convention et permet la dérogation au minimum de période d'apprentissage et au minimum de formation CFA pour une reprise après rupture dans L. 6222-18-2. Sa proposition conserve les futurs bénéficiaires et l'emploi sans terme. R. 6222-6 la cite expressément pour ne pas imposer six mois ou une convention intégrée là où la reprise en est dispensée ; ce n'est pas une dispense générale de certification.",
 ('R6222-6','R6222-9'): "La cible dispense de convention dans quatre régimes précis : échec, début avant employeur, durée adaptée pour handicap et sport de haut niveau. Sa proposition vise le troisième alinéa et préserve la dispense pour l'avenir sans attestation. R. 6222-6 maintient ces exceptions et précise que l'intégration de la convention ne peut les rétablir ; la proposition de R. 6222-9 retenue dans ce lot conserve cette analyse.",
 ('R6222-7','L6222-7-1'): "L'article législatif fixe une convention tripartite au troisième alinéa, avec compétences et accords nécessaires ; il n'impose pas lui-même un modèle ministériel. L'abrogation de R. 6222-7 ne retire donc que le format, pas l'accord. La proposition législative fournie conserve une annexe obligatoire, à coordonner pour l'intégration envisagée dans R. 6222-6 ; les périodes nouvelles restent sans effet de terme sur l'emploi.",
 ('R6222-8','L6222-7-1'): "La source vise le dernier alinéa de L. 6222-7-1, alors troisième ; la proposition ajoute un alinéa transitoire après la convention. R. 6222-8 vise donc expressément le troisième pour préserver la réserve de certification sans renvoi à la transition. Les compétences, accords de durée et exceptions demeurent ; aucune règle d'inscription n'est réputée remplacée par le seul aménagement ni par l'emploi sans terme.",
 ('R6222-9','L6222-37'): "Le renvoi est précisément au 2° sur la durée aménagée pour les personnes handicapées, pas à l'ensemble de leurs obligations. La source de dispense et la cible proposée continuent pour les futurs apprentissages du contrat unique ; la convention, séparée ou intégrée, ne peut être exigée à la place d'une dispense. Les droits antérieurs, autres aménagements et dérogations de départ restent à leur champ.",
 ('R6222-9','L6222-40'): "Le renvoi au 1° concerne la durée aménagée des sportifs de haut niveau, tandis que le 2° vise le temps de travail. La dispense de convention reste donc limitée à l'aménagement de durée, ouverte aux situations futures comme anciennes. La cible proposée distingue déjà période pédagogique et emploi ; R. 6222-9 ne tire aucun terme d'emploi de cet aménagement.",
 ('R6222-9','L6222-7-1'): "Le troisième alinéa contient la convention dans la source et la proposition, mais n'est plus le dernier dans celle-ci. Le renvoi est corrigé sans réduire les quatre cas dispensés. L'annexe encore mentionnée dans la cible doit être coordonnée avec l'intégration de R. 6222-6 ; aucune forme d'annexe ou de convention intégrée ne peut réintroduire la formalité expressément dispensée, y compris pour les futurs contrats uniques.",
 ('R6222-21','L6222-18'): "La source comporte une liberté de rupture durant quarante-cinq jours pratiques, puis accord, cas légaux, médiation préalable et liquidation avec renvoi à L. 1243-4. La proposition introduit le contrat unique, la médiation facultative du majeur et le maintien des signatures et de l'intervention du médiateur pour le mineur, plus la transition des anciens contrats dont la note distingue ceux d'avant 2019. R. 6222-21 suit cette séparation sans rétablir le délai de cinq puis sept jours, conserve la copie utile via le CFA et n'étend pas la suppression d'indemnité de liquidation aux réparations de sécurité de L. 6225-5."
}

for a in OUT:
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in REFS['requirements'][key]:
        target = REFS['targets'][target_key]
        num = target['number']
        assessment = BASE_CHECKS[a['number']].get(num) or EXTRA_CHECKS.get((a['number'], num))
        assert assessment and len(assessment) >= 80, (a['number'], num)
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

assert len(OUT) == len(SOURCES) == 12
Path('answer.json').write_text(json.dumps(OUT, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(OUT), 'articles,', sum(len(a['reference_checks']) for a in OUT), 'analyses de cibles')
