import copy
import hashlib
import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REFERENCE_FINGERPRINT = 'aabe8db899607032094b2d520a441a45dd3fc48e80b2ea9dd2742571c626754d'

def read_json(name):
    return json.loads((ROOT / name).read_text())

def fingerprint(name):
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()

assert fingerprint('reference-targets.json') == REFERENCE_FINGERPRINT
sources = read_json('source.json')
references = read_json('reference-targets.json')
answer = copy.deepcopy(read_json('previous-answer.json'))
by_number = {row['number']: row for row in answer}
targets_by_number = {row['number']: (key, row) for key, row in references['targets'].items()}

# Analyses nouvelles des textes officiels et propositions contenus dans la vue actuelle.
# Ces analyses ne constituent pas une approbation du droit proposé.
checks = {
    'L2412-12': {
        'L1234-1': "La proposition de L. 1234-1 soumet le licenciement du nouvel emploi privé à quinze jours calendaires sans ancienneté minimale, avec maintien des autorisations. Ce délai court selon la notification de L. 1234-3, non selon la fin du mandat agricole. Les 2° et 3° historiques restent limités aux anciens contrats auxquels ils sont applicables ; ils ne deviennent pas une règle de terme du CDD.",
        'L1221-2': "L. 1221-2 proposé interdit de faire finir le nouvel emploi au retour d'un remplacé ou à l'achèvement d'une mission. La garantie rurale de L. 2412-12 est donc conservée pour le stock ancien et raccordée à L. 2411-20 pour l'emploi privé indéterminé ou converti. Ce raccordement ne transforme pas un agent public en salarié privé ni la fin de fonctions représentatives en terme d'emploi.",
        'L1234-9': "La proposition de L. 1234-9 prévoit, pour le contrat unique nouveau rompu par l'employeur hors faute grave, un an à la fin effective, préavis inclus, puis 0,20 mois brut par année totale et mois complets au prorata, avec plafond de six mois. Cette ancienneté indemnitaire ne conditionne pas la protection agricole ; les anciens services, indemnités spéciales et dommages d'illégalité restent dans leurs régimes propres.",
        'L2412-1': "Le 12° identifie le représentant des salariés d'une chambre d'agriculture. La vue actuelle conserve le contrôle du terme des anciens CDD et la continuité au chapitre Ier pour le contrat unique ou sa conversion. Son nouvel alinéa final interdit d'opposer un terme illicite pour retirer la protection ou l'autorisation préalable : L. 2412-12 l'explicite désormais, sans étendre le contrat privé aux agents publics ni exiger un an de service pour protéger le mandat.",
    },
    'L2412-14': {
        'L1234-1': "Les quinze jours calendaires de L. 1234-1 proposé sont le préavis individuel du contrat nouveau, pas le délai d'instruction de l'autorisation de rupture de l'assesseur maritime. Les six mois après cessation des fonctions et les conditions de candidature restent autonomes ; une notification ordinaire ne vaut pas autorisation. L'ancien CDD garde son régime de terme et ses protections.",
        'L1221-2': "Selon L. 1221-2 proposé, une activité maritime temporaire ou la durée des fonctions d'assesseur ne peuvent fixer le terme d'un nouvel emploi. L. 2412-14 ne conserve les mécanismes du CDD que pour les contrats conclus avant la réforme ; il raccorde l'emploi unique et les conversions consenties à L. 2411-23, sans perdre les protections des candidats et anciens assesseurs.",
        'L1234-9': "Le seuil d'un an en fin effective, préavis compris, de L. 1234-9 proposé ne remplace pas les six mois protecteurs suivant les fonctions d'assesseur. Le barème ordinaire patronal hors faute grave est de 0,20 mois brut par année totale, fractions en mois complets, plafond six mois ; il ne commande ni la procédure médicale spéciale, ni l'autorisation, ni les dommages d'une rupture illicite. Les contrats anciens ont leur transition.",
        'L2412-1': "L'assesseur maritime est le 14° de la liste ; les candidats et les six mois après fonctions sont précisés par L. 2412-14 et L. 2411-23. La vue actuelle ajoute expressément l'inopposabilité d'un terme contraire au contrat unique et le maintien de l'autorisation du chapitre Ier ; le texte final de L. 2412-14 reprend ce raccordement. Le renvoi au 17 décembre 1926 reste à confronter au 19 décembre cité par L. 2411-23, sans retirer la protection.",
    },
    'L2412-15': {
        'L1234-1': "L. 1234-1 proposé maintient les autorisations protectrices au-delà de son préavis individuel de quinze jours ; la faute grave conduit même au paiement du préavis si son exécution est impossible dans ce régime nouveau. Elle reste un cas de contrôle préalable de l'ancien CDD du défenseur syndical. Ni quinze jours après notification ni le terme d'une mission ne dispensent de l'inspecteur.",
        'L1221-2': "L. 1221-2 proposé ne permet aucun nouveau CDD au titre de la défense syndicale. La clause de renouvellement citée par L. 2412-15 conserve uniquement le contrôle d'un refus concernant un contrat antérieur, sans droit à renouveler à terme après la réforme. L'emploi futur ou converti est indéterminé et demeure protégé par L. 2411-24.",
        'L1234-9': "Le défenseur syndical ne perd pas sa protection avant un an d'ancienneté. L. 1234-9 proposé ne règle que l'indemnité ordinaire patronale : seuil en fin effective avec préavis, 0,20 mois brut sur toute l'ancienneté, mois complets au prorata et six mois au maximum, hors faute grave. L'autorisation préalable, les réparations d'illégalité et les composantes anciennes sont distinctes de ce calcul.",
        'L2412-1': "Le 15° de L. 2412-1 vise précisément le défenseur syndical de L. 1453-4. La vue actuelle ne se limite pas au stock de CDD : elle protège aussi l'emploi unique auquel un employeur aurait irrégulièrement attaché un terme, et conserve l'autorisation du chapitre Ier. L. 2412-15 explicite cette règle ; aucune ancienneté indemnitaire ou condition de notification ordinaire ne se substitue à la protection du mandat.",
    },
    'L2412-16': {
        'L1234-1': "Le préavis individuel de quinze jours du contrat nouveau prévu par L. 1234-1 proposé reste distinct de l'autorisation du membre de la commission régionale. Il ne réduit ni les six mois depuis la notification de L. 23-112-2 ni les six mois depuis l'expiration du mandat. Sa notification écrite ne remplace pas la notification syndicale identifiant les salariés protégés ; les anciens contrats gardent leur régime applicable.",
        'L1221-2': "La durée d'une désignation à la commission ou d'une propagande électorale ne met pas fin à l'emploi indéterminé de L. 1221-2 proposé. L. 2412-16 conserve les anciens contrôles de CDD, interdit leur renouvellement futur et raccorde le contrat unique à L. 2411-25. Une conversion consentie ne fait pas recommencer les deux périodes de six mois et ne remet pas l'ancienneté à zéro.",
        'L1234-9': "Les deux périodes de six mois protègent le mandat, elles ne sont ni le seuil d'indemnité ni son plafond. L. 1234-9 proposé fixe un an en fin effective préavis inclus pour l'indemnité ordinaire patronale, hors faute grave, puis 0,20 mois brut par année totale et mois complets au prorata, plafonné à six mois. Les dommages d'une atteinte au mandat, les indemnités spéciales et les droits anciens demeurent séparés.",
        'L2412-1': "Le 16° renvoie à la commission de L. 23-111-1 ; les deux périodes et la notification propre aux candidats sont précisées dans L. 2412-16 et L. 2411-25. Le dernier alinéa de la vue actuelle de L. 2412-1 protège aussi le salarié sous contrat unique présenté irrégulièrement comme un CDD. La proposition l'explicite sans nouvelle ancienneté d'accès à la protection et sans autorisation acquise par expiration d'un préavis.",
    },
    'L2421-7': {
        'L1234-1': "La proposition de L. 1234-1 réserve les procédures collectives et autorisations, malgré quinze jours de préavis individuel du contrat nouveau. L. 2421-7 maintient donc le renvoi à la sous-section de licenciement adaptée au mandat : consultation éventuelle, instruction et décision préalable ne sont pas réputées achevées quinze jours après notification. Le terme de l'ancien CDD garde ses propres contrôles.",
        'L1221-2': "L. 1221-2 proposé ferme les nouveaux recrutements déterminés sans annuler les demandes concernant le stock ancien. Pour ces anciens CDD, L. 2421-7 conserve le renvoi à la section 1 ; pour le contrat unique ou converti, cette section s'applique directement dans son champ. Aucun redépôt du dossier n'est requis du seul fait de la nouvelle rédaction, et aucune mission ne crée un terme d'emploi.",
        'L1234-9': "Le seuil d'un an à fin effective préavis inclus et le barème de 0,20 mois brut par année totale, mois complets au prorata, plafond six mois hors faute grave, de L. 1234-9 proposé ne sont pas des conditions de saisine de l'inspecteur. L. 2421-7 conserve la procédure protectrice dès lors que le mandat et sa période sont couverts ; les composantes anciennes et réparations d'illégalité restent autonomes.",
        'L2412-1': "L. 2412-1 énumère les mandats, avec ses 7° bis et ter, sans définir une consultation identique pour tous. Sa vue actuelle réserve les anciens CDD, poursuit la protection au chapitre Ier et exclut que le terme illicite d'un contrat unique dispense d'autorisation. L. 2421-7 maintient la section 1 selon le mandat même dans cette dernière situation ; la qualification erronée du contrat ne crée ni nouvelle procédure ni perte de protection.",
    },
    'L2421-8': {
        'L1234-1': "Les deux dates de L. 2421-8, saisine patronale et décision avant terme de l'ancien CDD, ne sont pas remplacées par les quinze jours de L. 1234-1 proposé. Le silence ou l'expiration du préavis ne constate pas l'absence de discrimination. Le contrat unique n'a pas de terme à contrôler ; sa rupture protégée suit les autorisations du chapitre Ier et les procédures distinctes réservées par la cible.",
        'L1221-2': "L. 1221-2 proposé rend sans terme les nouveaux emplois saisonniers ou temporaires, même si l'affectation cesse. Le contrôle de l'arrivée du terme de L. 2421-8 reste donc limité aux anciens CDD. Les droits de reconduction et prolongations de protection sont conservés dans leur champ, y compris les garanties futures du contrat unique, sans nouvelle embauche déterminée ni remise à zéro de l'ancienneté.",
        'L1234-9': "La constatation antidiscriminatoire de L. 2421-8 n'attend pas le seuil d'un an de L. 1234-9 proposé. Celui-ci règle l'indemnité ordinaire patronale nouvelle hors faute grave : ancienneté en fin effective préavis inclus, 0,20 mois brut par année totale et mois complets au prorata, plafond six mois. Les indemnités des anciens CDD et les dommages d'une discrimination ne sont ni absorbés ni plafonnés par cette règle.",
        'L2412-1': "La liste de L. 2412-1 identifie les bénéficiaires, non les modalités de saisine : L. 2421-8 rectifie explicitement cette attribution du texte source en conservant ses alinéas de saisine et de décision. La vue actuelle ajoute que le terme illicite du contrat unique est inopposable et n'écarte pas l'autorisation du chapitre Ier. Le texte final conserve cette garantie, sans traiter le terme illicite comme un terme valable auquel l'inspecteur pourrait mettre fin.",
        'L2412-13': "Le troisième alinéa officiel de L. 2412-13 porte les anciens CDD saisonniers ou d'usage du conseiller prud'homme, le refus contraire à une clause de reconduction et la prolongation pendant l'interruption habituelle. La proposition ajoute ensuite une prolongation pour les futurs contrats uniques : le renvoi matériel de L. 2421-8 remplace donc le dernier alinéa devenu mobile. Les références de périodes à L. 2411-5 et 8, relatives à d'autres mandats, restent une discordance à coordonner dans la cible.",
        'L2412-9': "L. 2412-9 vise la commission agricole d'hygiène et de sécurité ; le troisième alinéa officiel contient le régime saisonnier ou d'usage et la prolongation d'interruption. Ses alinéas proposés ultérieurs protègent les futurs contrats uniques, sans terme. L. 2421-8 vise la protection par son objet pour préserver le contrôle du seul terme ancien. Les renvois de périodes à L. 2411-8 et 10 concernent d'autres mandats et restent signalés, sans suppression des droits acquis.",
        'L2412-8': "Le premier alinéa de L. 2412-8 qualifie le représentant d'entreprise extérieure dans un établissement à risques selon l'environnement et le code minier. Son troisième alinéa officiel protège les anciens CDD saisonniers ou d'usage et prolonge les périodes d'interruption ; ce n'est plus le dernier alinéa du projet. L. 2421-8 garde ce champ matériel et réserve les protections futures sans terme. La discordance des renvois L. 2411-8 et 10 demeure à traiter dans la cible.",
        'L2412-5': "L. 2412-5 protège les élus du CSE interentreprises, les anciens membres et candidats selon L. 2411-10 et 10-1 : six mois après mandat ou disparition et six mois depuis dépôt de candidature, avec connaissance d'imminence dans son champ. Le troisième alinéa officiel ajoute les anciens CDD saisonniers ou d'usage ; les derniers alinéas du projet concernent l'emploi unique futur. L. 2421-8 n'applique son contrôle avant terme qu'au premier champ sans fermer les prolongations futures.",
        'L2412-4': "Pour le représentant de proximité, L. 2412-4 distingue les périodes de L. 2411-8 et 9, notamment six mois après mandat ou disparition, dépôt de candidature et connaissance de l'imminence avant entretien. Le troisième alinéa officiel ajoute les anciens contrats saisonniers ou d'usage et leur prolongation ; le projet ajoute ensuite l'emploi unique futur. Le renvoi par objet de L. 2421-8 préserve ces champs sans créer de contrôle à une fin de mission du contrat unique.",
        'L2412-3': "L. 2412-3 distingue élus du CSE, représentants syndicaux, anciens titulaires et candidats, avec les périodes de L. 2411-5 et 7, leurs six mois et conditions de candidature ou notification. Le troisième alinéa officiel protège les contrats saisonniers ou d'usage et prolonge les délais d'interruption ; les alinéas finaux proposés étendent cette garantie au contrat unique. L. 2421-8 identifie donc l'objet ancien du contrôle de terme plutôt qu'un dernier alinéa devenu inexact.",
        'L2412-2': "Le troisième alinéa officiel de L. 2412-2 protège le délégué syndical en CDD saisonnier ou d'usage et prolonge les périodes d'interruption. Son projet ajoute une garantie analogue aux futurs emplois uniques sans terme, distincte du contrôle de L. 2421-8. Le renvoi de périodes à L. 2411-5 concerne le CSE dans le corpus ; il ne peut être assimilé silencieusement à L. 2411-3 et ses douze mois après fonctions exercées au moins un an. Cette discordance reste à coordonner dans la cible.",
    },
    'L3122-14': {
        'L1234-1': "Les quinze jours de L. 1234-1 proposé restent soumis aux protections conditionnant la rupture. Le transfert médical du travailleur de nuit vers un poste de jour comparable et la justification écrite de l'impossibilité ou du refus gardent donc leur fonction propre. Le seul préavis et sa notification ne prouvent pas un reclassement ; les règles spéciales d'inaptitude et les anciens préavis demeurent distincts.",
        'L1221-2': "Le champ général de L. 3122-14 couvre déjà le contrat indéterminé qu'institue L. 1221-2 proposé. Une mission de nuit peut cesser sans mettre fin à l'emploi et sans retirer la garantie de transfert pour raison médicale. Les situations futures restent protégées ; une conversion consentie ne remet à zéro ni l'ancienneté ni les droits des anciens contrats, et aucun renvoi ne recrée de CDD.",
        'L1226-4-3': "La source de L. 1226-4-3 garantit l'indemnité spéciale du CDD pour inaptitude au moins égale à celle de L. 1234-9, avec les modalités de précarité. Sa proposition protège les anciens droits et maintient pour le contrat unique une indemnité spéciale au prorata sans seuil d'un an. La réserve sans préjudice de L. 3122-14 demeure cohérente : ni le transfert nuit/jour ni le zéro ordinaire ne neutralisent ce régime, distinct du doublement pour inaptitude professionnelle.",
        'L1234-9': "La proposition de L. 1234-9 maintient expressément salaires, congés, préavis, réparations et indemnités spéciales. Son seuil ordinaire d'un an en fin effective préavis inclus, puis 0,20 mois par année totale et mois complets, plafond six mois hors faute grave, ne plafonne donc pas par lui-même l'inaptitude spéciale réservée par L. 3122-14. Les anciennes composantes et le salaire de référence spécial restent dans leur champ.",
    },
    'L3123-5': {
        'L1234-1': "Le préavis de L. 1234-1 proposé est de quinze jours calendaires pour le contrat nouveau, sans prorata selon les jours travaillés à temps partiel. Les 2° et 3° anciens restent réservés aux contrats auxquels ils s'appliquent. L'ancienneté intégrale et la pondération du salaire de L. 3123-5 ne modifient ni le lendemain de notification servant au nouveau décompte ni les procédures spéciales de rupture.",
        'L1221-2': "L. 1221-2 proposé autorise un contrat unique à temps partiel, sans terme lié à la durée d'un besoin. Les cinq principes de L. 3123-5, dont l'ancienneté comptée comme à temps complet et la pondération salariale, restent applicables. Une conversion consentie d'un ancien contrat ne réinitialise ni l'essai ni les services ou créances ; la fin d'une mission ne crée pas une nouvelle embauche déterminée.",
        'L1221-23': "L'essai doit rester expressément stipulé selon L. 1221-23 : la limite calendaire de L. 3123-5 et son renvoi à trois mois ne créent pas un essai tacite. La proposition interdit le renouvellement de l'essai nouveau ; la possibilité expressément stipulée de renouveler ne subsiste que pour les anciens contrats où elle demeure licite. Aucun prorata d'horaire n'allonge le plafond.",
        'L1221-21': "L. 1221-21 proposé exclut tout renouvellement de l'essai du contrat nouveau, même si sa durée initiale est inférieure à trois mois. L. 3123-5 ne le rétablit pas au titre du temps partiel. Les plafonds anciens de quatre, six et huit mois, accord étendu, stipulation et consentement exprès au renouvellement restent réservés aux contrats antérieurs concernés, sans remise à zéro lors d'une conversion.",
        'L1221-20': "L. 1221-20 conserve la double finalité de l'essai, appréciation des compétences par l'employeur et des fonctions par le salarié ; son projet exclut la discrimination et rappelle le préavis du contrat unique. L. 3123-5 ne peut donc transformer le temps partiel ou la première année sans indemnité ordinaire en nouvel essai. Le préavis reste calendaire, sans allonger l'essai du fait de jours non travaillés.",
        'L1221-19': "La source de L. 1221-19 fixe deux mois pour ouvriers/employés, trois pour maîtrise/techniciens et quatre pour cadres ; son projet fixe trois mois non renouvelables à tous les nouveaux contrats. L. 3123-5 conserve seulement l'égalité de durée calendaire avec le temps complet et les durées plus courtes. Cette coordination n'est pas une baisse uniforme : le plafond initial des ouvriers et employés augmente dans la cible, tandis que les essais anciens gardent leur régime.",
        'L1234-9': "Le sixième alinéa suit la proposition de L. 1234-9 : seuil d'un an en fin effective préavis inclus, employeur seul hors faute grave, 0,20 mois brut sur toute l'ancienneté première année comprise, fractions en mois complets et plafond six mois. Le cinquième alinéa pondère le salaire par les périodes plein/partiel, sans réduire une seconde fois les services. Huit mois et composantes des anciens contrats, minima plus favorables et indemnités spéciales restent distincts.",
        'L1221-22': "L. 1221-22 proposé maintient pour les contrats nouveaux les essais plus courts des conventions ou accords quelle que soit leur date, ainsi que de la lettre ou du contrat, sans renouvellement. Cette réserve est expressément reprise au deuxième alinéa de L. 3123-5. La note de 2023 et les exceptions historiques des anciens contrats ne datent pas la nouvelle réforme et ne permettent pas d'allonger un essai à temps partiel au-delà du temps complet.",
    },
    'L3123-7': {
        'L1234-1': "Le besoin d'au plus sept jours du 1° de L. 3123-7 proposé dispense du minimum conventionnel mais ne fixe pas la durée d'emploi. Le contrat unique reste soumis aux quinze jours calendaires de L. 1234-1 dans son champ, selon la notification légalement requise. La dispense de durée horaire ne supprime ni préavis ni autorisation distincte ; les anciens CDD gardent leur seul régime transitoire.",
        'L1221-2': "Les 1° à 4° de L. 3123-7 sont des dispenses de minimum horaire, pas des cas de CDD. L. 1221-2 proposé exclut que la fin du besoin, du remplacement ou d'une aide d'insertion termine l'emploi nouveau. Les futures situations matérielles équivalentes restent donc éligibles aux dispenses dans le contrat indéterminé, sans priver les anciens contrats et conversions consenties de leurs droits et ancienneté.",
        'L1234-9': "Le temps partiel inférieur à l'ancien minimum n'abaisse pas l'ancienneté ouvrant l'indemnité de L. 1234-9 proposé. Pour le contrat unique nouveau, le seuil reste un an en fin effective préavis inclus, puis 0,20 mois brut par année totale, mois complets au prorata et plafond six mois, hors faute grave et à l'initiative de l'employeur. Le volume garanti, les composantes anciennes et les indemnités spéciales ne sont pas supprimés par la dispense horaire.",
        'L1251-6': "Le 3° ne reprend que le remplacement d'un salarié absent, soit le a) du 1° de L. 1251-6 ; il ne dispense pas pour l'ensemble des autres remplacements ou missions. La proposition de la cible régit l'affectation temporaire auprès de l'utilisateur, tandis que l'emploi nouveau est indéterminé. La dispense reste ouverte à cette affectation future sans création d'un contrat de mission à terme ni suppression des droits anciens.",
        'L1242-2': "Les cinq cas du 1° officiel de L. 1242-2 sont repris intégralement au 2° : absence, temps partiel provisoire par avenant ou échange écrit, suspension, départ avant suppression après consultation du CSE existant, et attente du remplaçant recruté en CDI. La proposition de la cible abroge prospectivement ses cas de CDD. Énoncer ces situations dans L. 3123-7 maintient la dispense pour les futurs remplacements sans ressusciter le fondement abrogé ni fixer un terme à l'emploi.",
        'L5132-15-1': "L. 5132-15-1 distingue les ateliers et chantiers d'insertion, le parcours initial de quatre mois et la limite de vingt-quatre mois, les prolongations et le minimum spécial de vingt heures avec ses dérogations. Sa proposition sépare parcours, aides et contrat sans terme. Le 4° de L. 3123-7 dispense l'autre emploi cumulé ; il ne retire pas les vingt heures spéciales. Le seuil de cumul encore renvoyé à L. 3123-27 dans la cible reste à coordonner dans celle-ci, sans le déclarer supprimé ici.",
        'L5132-11-1': "Les associations intermédiaires de L. 5132-11-1 conservent un minimum spécial de vingt heures et ses conditions de cumul, distinct du plancher général supprimé. Le projet sépare contrat indéterminé, parcours de quatre à vingt-quatre mois et prolongations jusqu'aux limites spéciales, sans promettre une aide inconditionnelle. Le 4° de L. 3123-7 allège l'autre emploi ; le renvoi de la cible à L. 3123-27 pour sa durée globale demeure une coordination non accomplie dans cet article.",
        'L5132-5': "La cible concerne l'entreprise d'insertion, son minimum spécial de vingt heures, les périodes de mise en situation, les suspensions et départs favorables. Le projet distingue l'emploi sans terme du parcours initial d'au moins quatre mois, de la limite de vingt-quatre mois et des prolongations de formation ou pour salariés âgés/handicapés. L. 3123-7 dispense seulement l'autre contrat cumulé ; le seuil global encore renvoyé à L. 3123-27 dans L. 5132-5 exige une coordination propre, sans suppression implicite des aides ou minima spéciaux.",
        'L161-22-1-5': "Le premier alinéa du I de L. 161-22-1-5 CSS renvoie à un âge fixé par décret, inférieur à l'âge légal ; aucun âge chiffré ni ancienneté d'entreprise n'est repris. L. 3123-7 utilise ce seul critère pour une demande de moindre durée. La durée d'assurance, les quotités, les activités agricoles, les majorations, la liquidation provisoire et les exclusions du II restent propres à la pension ; la dispense horaire ne vaut pas admission automatique à la retraite progressive ni extension du contrat privé aux autres assurés.",
    },
    'L3142-88': {
        'L1234-1': "Les 2° et 3° de L. 1234-1 proposé conservent les préavis historiques d'un et deux mois dans le seul champ des anciens contrats. Le troisième alinéa de L. 3142-88 réserve expressément son renvoi à ce champ. Les deux mandats assimilés ne modifient donc pas les quinze jours calendaires des nouveaux contrats ; la présentation ou réception de notification reste le point de départ de leur décompte selon L. 1234-3, et les procédures spéciales restent distinctes.",
        'L1221-2': "L. 1221-2 proposé régit l'emploi privé nouveau et n'en fait pas coïncider la fin avec celle du mandat ou de la suspension. Les futures suspensions d'élus éligibles gardent leurs assimilations et les conversions leur ancienneté. La réserve expresse de L. 3142-87 empêche d'attribuer le contrat unique aux fonctionnaires ou agents publics ; la liste des élus et les conditions CGCT ne sont pas remplacées par la cible privée.",
        'L1234-9': "Dans la limite inchangée de deux mandats consécutifs, l'assimilation compte pour l'ouverture et le calcul de l'indemnité selon L. 1234-9 proposé. Pour le contrat unique nouveau : un an en fin effective préavis inclus, 0,20 mois brut sur toute l'ancienneté y compris la première année, mois complets au prorata, plafond six mois et exception de faute grave. Les huit mois et composantes anciennes, indemnités plus favorables et spéciales sont préservés ; aucune indemnité de démission n'est créée.",
        'L3123-7': "La cible fournie est L. 3123-7 du code du travail, alors que le premier alinéa de L. 3142-88 désigne expressément L. 3123-7 du CGCT pour les élus départementaux. La source et le projet de la cible travail ne règlent que les minima de temps partiel : leur suppression n'a aucun effet sur les droits CGCT des élus, les deux mandats assimilés ou les agents publics. Le texte CGCT entier n'est pas fourni ; son contrôle demeure extérieur au lot, sans emprunter le contenu de son homonyme.",
    },
    'L3142-100': {
        'L1234-1': "Le préavis de quinze jours de L. 1234-1 proposé ne dispense d'aucune garantie du service national ni des restrictions de notification et de prise d'effet du paragraphe. L. 3142-100 répare leur méconnaissance par le juge, indépendamment d'un préavis nouveau ou ancien. Il n'impose pas une autorisation administrative supplémentaire et ne transforme pas un préavis respecté en immunité contre les dommages-intérêts.",
        'L1221-2': "L. 1221-2 proposé interdit la fin automatique d'un emploi nouveau par achèvement de son objet. La réparation de L. 3142-100 reste applicable aux bénéficiaires futurs, sans nouveau CDD. L'exception d'échéance de l'objet encore présente dans L. 3142-99, lu dans le corpus, doit être réservée dans son propre article aux anciens contrats ; sa coordination n'est pas accomplie en conservant seulement le présent droit autonome à réparation.",
        'L1234-9': "L. 1234-9 proposé réserve les réparations d'illégalité : ni son seuil d'un an en fin effective préavis inclus ni le plafond de six mois n'atteignent les dommages-intérêts de L. 3142-100. Le cumul s'opère avec l'indemnité ordinaire lorsqu'elle est due, selon 0,20 mois brut par année totale et mois complets, hors faute grave et avec transition des anciens services. La partie lésée n'a pas à justifier d'un an pour demander réparation et aucune indemnité ordinaire de démission n'est créée.",
    },
    'L3142-109': {
        'L1234-1': "L. 1234-1 proposé fixe le préavis du licenciement ; il ne retire pas la dispense spéciale de préavis à l'initiative du salarié après congé ou temps partiel de création/reprise. Celle-ci reste ouverte aux situations futures face aux quinze jours ordinaires du contrat unique. L'information de l'employeur prévue pour organiser la fin du congé garde son objet distinct, sans transformer ce délai d'information en préavis de rupture rétabli.",
        'L1221-2': "La durée du congé ou du temps partiel pour création/reprise n'est pas la durée d'emploi au sens de L. 1221-2 proposé. Le salarié conserve à son issue le choix de la rupture favorable de L. 3142-109 ou le droit au retour prévu par les articles voisins. Le maintien de l'absence de réemploi unilatéral avant terme ne crée pas un CDD ni n'interdit un retour convenu ; les anciens contrats et conversions gardent leurs droits.",
        'L1234-9': "L. 1234-9 proposé n'ouvre pas l'indemnité ordinaire à une rupture à l'initiative du salarié. La dispense, dans L. 3142-109, de payer lui-même une indemnité de rupture reste donc un avantage distinct. Le seuil patronal d'un an en fin effective préavis inclus, 0,20 mois brut par année totale et mois complets, et le plafond de six mois ne conditionnent pas cette dispense ; les créances anciennes et régimes spéciaux ne sont pas effacés.",
    },
}

guard = ("Pour le contrat unique, même présenté à tort comme un contrat à durée déterminée, "
         "la stipulation illicite d'un terme ne peut priver le salarié des protections de son emploi "
         "ou de son mandat et ne dispense pas l'employeur de l'autorisation préalable de rupture "
         "requise au titre du chapitre Ier du titre Ier du présent livre.")

protected = ['L2412-12', 'L2412-14', 'L2412-15', 'L2412-16', 'L2421-7', 'L2421-8']
for number in protected:
    row = by_number[number]
    assert row['proposed_xml'].endswith('</p>')
    row['proposed_xml'] = row['proposed_xml'][:-4] + ' ' + guard + '</p>'
    row['reason'] += (" La correction ciblée de cette reprise explicite la garantie désormais portée par "
                      "le dernier alinéa de L. 2412-1 : un terme illicite ne retire ni protection "
                      "ni autorisation préalable au contrat unique. Cette coordination ne constitue "
                      "pas une coupe supplémentaire de la procédure protectrice.")
    row['review_notes'] += (" Nouvelle confrontation à la vue actuelle de L. 2412-1, y compris son dernier "
                            "alinéa sur le terme illicite : le texte proposé en assure expressément "
                            "l'application. Un terme contraire au contrat unique ne devient pas un "
                            "terme valable soumis au seul contrôle de son arrivée ; la rupture relève "
                            "des garanties du contrat indéterminé et du mandat. L'empreinte actuelle "
                            "de cette vue est reprise dans reference_checks après lecture de la "
                            "source officielle et de la proposition entières ; celles-ci restent "
                            "deux textes de nature différente.")
    row['substantive_impact']['assessment'] += (" La précision sur le terme illicite coordonne la "
                                               "protection du contrat unique ; elle ne supprime "
                                               "ni ne recrée une autorisation.")
    row['substantive_impact']['new_burdens_review'] += (" La précision sur la qualification illicite "
                                                      "du terme maintient l'autorisation déjà "
                                                      "requise pour ce mandat et n'ajoute ni "
                                                      "dossier, donnée ou délai.")
    effect = row['substantive_impact']['effects'][0]
    effect['after'] += (" Le terme illicite d'un contrat unique est inopposable pour retirer "
                       "la protection ; l'autorisation de rupture requise demeure préalable.")

# L. 2421-8 ne vise pas le dernier alinéa des propositions désormais complétées.
# La rectification matérielle déjà faite dans previous-answer est conservée.
by_number['L2421-8']['review_notes'] = by_number['L2421-8']['review_notes'].replace(
    "Aucun nouveau renvoi à une cible non fournie n'est ajouté.",
    "Aucun nouveau renvoi numéroté à une cible non fournie n'est ajouté ; le chapitre Ier "
    "reste celui de la protection du contrat indéterminé, sans créer de contrôle à un terme inexistant."
)

for row, source in zip(answer, sources):
    for field in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert row[field] == source[field], (row['number'], field)
    key = source['code_id'] + '|' + source['source_id']
    required = references['requirements'][key]
    assert set(checks[row['number']]) == {
        references['targets'][target]['number'] for target in required
    }
    row['reference_checks'] = []
    for target_key in required:
        target = references['targets'][target_key]
        row['reference_checks'].append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': checks[row['number']][target['number']],
        })

# Citations exactes à l'intérieur d'un même alinéa de la source, sans concaténation
# dépendant de la façon dont un lecteur HTML traite les retours à la ligne.
by_number['L2412-14']['substantive_impact']['effects'][0]['source_quote'] = (
    "Cette procédure est applicable durant les six premiers mois suivant la fin des fonctions d'assesseur maritime."
)
by_number['L2412-16']['substantive_impact']['effects'][0]['source_quote'] = (
    "Cette procédure s'applique également pendant une durée de six mois à compter de la notification "
    "prévue à l'article L. 23-112-2 et de six mois à compter de l'expiration du mandat du salarié "
    "ayant siégé dans cette commission."
)
by_number['L2421-8']['substantive_impact']['effects'][0]['source_quote'] = (
    "Pour l'application de la protection prévue au dernier alinéa des articles L. 2412-2, "
    "L. 2412-3, L. 2412-4, L. 2412-5, L. 2412-8, L. 2412-9 et L. 2412-13, l'arrivée du terme "
    "du contrat de travail à durée déterminée n'entraîne sa rupture qu'après constatation par "
    "l'inspecteur du travail, saisi en application de l'article L. 2412-1, que le salarié "
    "ne fait pas l'objet d'une mesure discriminatoire."
)
for effect in by_number['L3142-88']['substantive_impact']['effects']:
    effect['source_quote'] = (
        "Elle entre en compte, dans la même limite, dans le calcul de l'ancienneté exigée pour "
        "la détermination de la durée du préavis de licenciement prévue aux 2° et 3° de l'article "
        "L. 1234-1 et pour le bénéfice de l'indemnité de licenciement mentionnée à l'article L. 1234-9."
    )

assert fingerprint('reference-targets.json') == REFERENCE_FINGERPRINT
(ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(answer)}, ensure_ascii=False))
