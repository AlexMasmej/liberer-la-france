import hashlib
import json
from pathlib import Path

root = Path(__file__).parent
source = json.loads((root / 'source.json').read_text())
refs_path = root / 'reference-targets.json'
refs_bytes = refs_path.read_bytes()
refs = json.loads(refs_bytes)
answer = json.loads((root / 'previous-answer.json').read_text())
by_number = {x['number']: x for x in answer}

# Reprendre les articles complets du précédent essai et corriger leur fond.
x = by_number['L6131-1']
old = "Pour les années nouvelles, aucune contribution supplémentaire, déclaration d'assiette ou transmission exclusivement justifiée par celle-ci n'est exigée"
new = ("Pour le calcul de la contribution des années anciennes et de la créance maintenue, les périodes d'apprentissage et de professionnalisation, l'année suivante et les exclusions d'effectif ou de rémunérations sont prises en compte dans les conditions de l'article L. 6242-1, y compris lorsque les missions ou formations sont exécutées dans un contrat unique. Le seul changement de support contractuel ne prive pas une entreprise d'une exonération ou d'une exclusion applicable. " + old)
assert old in x['proposed_xml']
x['proposed_xml'] = x['proposed_xml'].replace(old, new, 1)
x['reason'] = (
    "La suppression CPF-CDD du 4° reste acquise pour les périodes travaillées après l'entrée en vigueur, y compris sous un ancien CDD. Le 3° conserve la coordination déjà corrigée avec la suppression de la contribution supplémentaire à l'apprentissage pour les années civiles commençant le 1er janvier suivant l'entrée en vigueur de sa suppression. La nouvelle vue complète de L6242-1 précise les exclusions d'effectif et d'assiette des missions de même objet réalisées en contrat unique : le 3° en préserve expressément l'application aux anciennes années et au calcul de la créance maintenue. Les deux contributions et leurs calendriers ne sont pas confondus, et leur mention récapitulative n'est pas comptée comme une seconde suppression. Les financements des 1°, 2° et 5° restent nécessaires à la formation directement fournie, au financement principal de la formation et de l'alternance et aux engagements collectifs autonomes ; aucun doublon de versement n'est établi par cet article."
)
x['review_notes'] = (
    "L6242-1 est examiné dans la vue actuelle 1df4e817a6a12b9c9ca8d6aeb9eba32db43268abe383ec8ae723d7b2b84bdd58, et non dans la vue périmée du précédent essai. Son II maintient l'alternance et l'année suivante sans nouvelle embauche ni double compte ; son V maintient les exclusions d'effectif des missions de même objet sur contrat unique, sur les pièces déjà établies ; son VIII maintient aussi ces exclusions de rémunérations et les exonérations pour les anciennes années. Le 3° ne rétablit ni CSA annuelle, ni versement de mars, ni déclaration à zéro. Source CSA : au moins 250 salariés, quotient inférieur à 5 %, exonération à partir de 3 % et progression d'au moins 10 %, taux 0,4 %, 0,6 %, 0,2 %, 0,1 % et 0,05 %, taux territoriaux réduits à 52 % de leur montant ; ces paramètres ne subsistent que pour les anciennes années. L6331-6 fixe 1 % du revenu d'activité retenu pour les cotisations sociales des CDD : le 4° retient les mêmes périodes travaillées, non la date de paiement, et protège formation, alternance et saisonniers pour les périodes anciennes. L6131-2, L6131-3, L6131-4, L6332-1-2, L6241-2 et L6243-1-2 ont été lus dans le corpus. La créance reste imputable sur le solde, sans report ni restitution, dans la limite de deux points et avec montant ministériel entre 2,50 et 5,00 euros ; l'aide et le conseil au recrutement restent ouverts sans liste annuelle des redevables d'une taxe supprimée. Coordonner ces articles de recouvrement, d'affectation et d'avantages sans les prétendre réécrits dans ce lot. CSS L243-1-2, lu, organise un recouvrement unique, pas une exemption générale de cotisations. CSP L6133-1 et L6133-4 et CASF L312-7 ne sont pas fournis : leurs catégories exclues sont conservées, leur concordance extérieure demeure à contrôler. La note du 1er janvier 2024 ne date pas la réforme ; aucun rendement ou financement de remplacement n'est inventé."
)
x['benefit_review'] = (
    "Le II conserve toutes les catégories d'employeurs exclues du I. Pour le CPF-CDD, les exclusions des formations, de l'alternance et des emplois saisonniers restent applicables aux périodes anciennes ; les périodes futures sont entièrement déchargées, y compris dans un CDD antérieur, sans prélèvement de remplacement ni perte des droits CPF et abondements. La suppression de la CSA conserve ses exonérations, exclusions, taux territoriaux et restitutions pour les anciennes années. Le numérateur d'alternants comprend toujours l'année suivant la formation dans les conditions de L6242-1 ; les missions de même objet sur contrat unique conservent leurs exclusions d'effectif et de rémunérations. Pour les années nouvelles sans CSA, la créance favorable sur le solde de taxe d'apprentissage et l'aide au recrutement restent ouvertes aux entreprises futures éligibles. La créance n'est ni rendue remboursable ni subordonnée à une contribution supprimée. Les autres contributions conservent leurs exclusions et avantages propres, sans hausse compensatoire décidée ici."
)
x['substantive_impact']['assessment'] = (
    "La source officielle entière impose cinq voies de financement. La proposition coordonne le retrait de CSA et CPF-CDD aux échéances distinctes de leurs articles d'assiette, sans compter leurs renvois comme des taxes supplémentaires supprimées. La précision ajoutée sur les missions en contrat unique protège les exclusions et avantages de la vue actuelle de L6242-1 ; elle n'ajoute pas une troisième réduction."
)
x['substantive_impact']['scope_limitations'] = (
    "La contribution unique et les contributions conventionnelles conservent leurs régimes ; les pertes de recettes et le coût total de formation ne sont pas chiffrés. La CSA reste due pour les anciennes années, le CPF-CDD pour les périodes anciennes, avec avantages et recours ; les articles de recouvrement et les textes extérieurs restent à coordonner."
)
x['substantive_impact']['new_burdens_review'] = (
    "Aucune charge nouvelle n'est identifiée dans cet article : aucune recette de remplacement, déclaration à zéro, liste de redevables, attestation ni registre de missions n'est créé. Les calculs d'effectif pour la créance favorable utilisent le régime et les pièces existants de L6242-1 ; aucun solde net de l'ensemble des codes n'est chiffré."
)
x['substantive_impact']['effects'][1]['after'] = (
    "Aucune CSA ni assiette à déclarer pour les années civiles nouvelles ; anciennes assiettes, taux et exonérations conservés, y compris exclusions des missions de même objet en contrat unique ; créance favorable sur le solde et aide au recrutement maintenues pour les futurs cas éligibles."
)
x['substantive_impact']['effects'][1]['replacement_or_new_burdens'] = (
    "Ni complément de taxe ni liste exclusivement attachée à la contribution supprimée. Les calculs de la créance et des exclusions utilisent les données, contrats de mise à disposition et lettres de mission déjà établis, sans attestation ou registre nouveau."
)

x = by_number['L5521-2']
x['review_notes'] = (
    "Les deux sources et propositions complètes de L5132-11-1 et L5132-15-1 visent CSS L351-2 pour valider des trimestres, non pour déterminer la durée de l'emploi. Leurs minima spéciaux de vingt heures et dérogations restent distincts du plancher général de vingt-quatre heures. Leurs propositions conservent toutefois un seuil de cumul renvoyant à L3123-27 alors que la proposition de ce dernier, lue au corpus, ne fixe plus de minimum général : cette coordination reste à faire dans les cibles sans retirer la dérogation favorable. Leurs clauses réglementaires proposées désignent désormais le minimum du présent article sans reprendre l'ancien ordinal d'alinéa ; aucun défaut de cet ordinal n'est donc imputé aux propositions actuelles. CSS L351-2, lu intégralement, conserve les règles de cotisations minimales, la preuve aménagée et le congé de formation non rémunéré. L'article 7 de l'ordonnance mahoraise de 2002 et l'acte de raccordement de 2028 ne sont pas joints, restent à contrôler hors corpus et ne sont pas déclarés réécrits. La borne de 2028 vient de valid_until et ABROGE_DIFF ; elle n'est pas une date inventée pour la présente réforme."
)
by_number['L5132-11']['review_notes'] += (
    " Le renvoi rectifié à L2211-1 ne figure pas parmi les cibles fournies de reference-targets.json : son texte entier a été contrôlé dans le corpus public, avec L2212-1 et la note de transfert. Il n'est pas couvert par une empreinte de cible inventée."
)

# Analyses nouvelles des vues actuelles, sans reprendre les certificats antérieurs.
common = {
'L5132-6-1': {
'L1234-1': "Le plafond de trente-six mois régit la mission, tandis que L1234-1 régit la rupture patronale de l'emploi. Sa proposition impose quinze jours calendaires aux contrats nouveaux, y compris un préavis payé si la faute grave interdit le maintien au travail. Notre abrogation n'abrège ni les procédures protectrices ni les préavis des contrats antérieurs.",
'L1221-2': "La source de L1221-2 admet encore un terme de CDD ; sa proposition le ferme aux recrutements et renouvellements nouveaux. L'abrogation de la permission de CDI à cinquante-sept ans n'est cohérente qu'avec l'ouverture simultanée du contrat unique à L5132-6 : l'âge reste un critère d'aide éventuel, pas d'accès à l'emploi indéterminé.",
'L1234-9': "La permission d'inclusion abrogée n'est pas une indemnité de rupture. La proposition de L1234-9 distingue nouveaux contrats et composantes des anciens : pour les nouveaux, un an au terme effectif préavis inclus, puis 0,20 mois par année totale et mois complets, plafond six mois, avec l'exception de faute grave qu'elle énonce. Aucun de ces paramètres ne ferme l'aide d'inclusion ou les garanties d'intermission."
},
'L5132-11': {
'L1234-1': "Les trois alinéas de rémunération ne visent aucun délai de licenciement. Le préavis de quinze jours proposé à L1234-1 ne constitue donc ni une attente pour l'égalité salariale ni une condition de paiement des jours fériés ; la période d'essai citée décrit seulement le salarié de comparaison. Les anciens préavis restent à leur champ.",
'L1221-2': "Le nombre d'heures forfaitaires hors L5132-9 est un mode de rémunération et ne fixe aucun terme à l'emploi. Il demeure compatible avec la proposition de L1221-2, qui sépare emploi indéterminé et affectation temporaire ; le salaire et les jours fériés des contrats antérieurs demeurent exigibles selon leurs conditions.",
'L1234-9': "Le seuil source de huit mois et le seuil proposé d'un an concernent l'indemnité de licenciement, pas le salaire dû par l'association intermédiaire. L'absence éventuelle d'indemnité ordinaire avant un an n'enlève ni l'égalité salariale, ni les heures garanties, ni les jours fériés du présent article, même après une conversion conservant l'ancienneté."
},
'L5134-29': {
'L1234-1': "La rupture sans préavis après mobilité est un avantage du salarié, tandis que L1234-1 encadre le préavis patronal. Les quinze jours proposés n'évincent pas cette dispense spéciale et ne permettent pas à l'employeur d'en déduire un licenciement sans motif, procédure ou autorisation ; les contrats anciens gardent leurs droits de mobilité.",
'L1221-2': "Le 2° proposé vise l'essai d'un emploi unique indéterminé, conformément à la séparation emploi/formation de L1221-2 proposé. L'offre de CDD d'au moins six mois ne subsiste que pour un contrat déjà conclu avant la réforme ; une offre non acceptée ne permet pas une nouvelle embauche à terme ni un renouvellement postérieur.",
'L1234-9': "La sortie sans préavis motivée par l'embauche du salarié n'est pas une rupture patronale ouvrant l'indemnité ordinaire. Le seuil d'un an apprécié au terme effectif et le barème de L1234-9 proposé ne conditionnent donc ni suspension ni dispense. Ils n'effacent pas les salaires, congés et droits anciens de l'emploi aidé."
},
'L5134-57': {
'L1234-1': "L'article historique traite du départ du salarié vers l'alternance ou la formation, non du préavis patronal de L1234-1. Les quinze jours du nouvel emploi ne peuvent être opposés à cette dispense résiduelle. La réserve légale de 2007 détermine les contrats encore bénéficiaires ; elle n'est pas une nouvelle condition d'ancienneté.",
'L1221-2': "Le contrat jeune source demeure fermé aux nouveaux contrats par la note de 2007. L1221-2 proposé intervient seulement pour le support du nouvel emploi d'alternance justifiant un départ encore recevable : une phase pédagogique dans un contrat unique conserve la destination favorable, sans rouvrir un CDD ou le soutien ancien.",
'L1234-9': "L'indemnité de L1234-9 proposé est ordinaire et patronale : elle ne rémunère pas le départ volontaire de L5134-57. Son seuil d'un an à la fin effective, préavis inclus, et son plafond de six mois ne sauraient réduire la dispense, les congés ou les créances d'un contrat jeune antérieur toujours couvert par la réserve de 2007."
},
'L5213-3-1': {
'L1234-1': "La convention de rééducation et son effet d'avenant ne notifient aucune rupture patronale. Le préavis de quinze jours de L1234-1 proposé reste distinct des dix-huit mois maximaux de la convention réglementaire et des autorisations de santé ou de représentation ; les délais des contrats antérieurs ne sont pas modifiés par la fusion documentaire.",
'L1221-2': "La durée de la rééducation n'est pas un terme du contrat de travail au sens de L1221-2 proposé. Donner à la convention l'effet d'avenant n'engendre ni nouvelle embauche, ni nouvel essai, ni remise à zéro d'ancienneté ; le régime antérieur de l'emploi reste distinct de la date de conclusion de la convention nouvelle.",
'L1234-9': "Les indemnités journalières de rééducation du I et du III sont des prestations sociales, pas l'indemnité ordinaire de L1234-9. Le zéro avant un an, le calcul à 0,20 mois par année totale et le plafond de six mois proposés ne les affectent pas ; les indemnités spéciales de santé et les composantes anciennes restent également réservées."
},
'L5213-13-3': {
'L1234-1': "L'entreprise adaptée reste employeur entre deux missions. Le préavis patronal de quinze jours de L1234-1 proposé porte sur la rupture de cet emploi, non sur l'échéance d'une lettre de mission ; il se calcule après notification selon L1234-3 lu au corpus, sans supprimer autorisations protectrices ou procédures collectives. Les anciens contrats gardent leur terme légal.",
'L1221-2': "La faculté source de contrats de mission de vingt-quatre mois est remplacée, pour les nouveaux recrutements, par la forme indéterminée imposée à L1221-2 proposé. L'accompagnement et l'aide peuvent expirer sans rompre l'emploi. La réserve des contrats déjà conclus conserve leurs dérogations, sans autoriser de nouveau renouvellement à terme.",
'L1234-9': "Pour l'emploi unique nouveau, les intermissions assimilées à du travail par L1251-58-2 entrent dans l'ancienneté reconnue : un an au terme effectif préavis inclus, puis 0,20 mois sur toutes les années et mois complets, plafond six mois selon L1234-9 proposé. Son exception de faute grave et les indemnités spéciales restent distinctes ; le seuil ne conditionne ni aide ni garantie mensuelle."
},
'L5422-12': {
'L1234-1': "Le délai patronal de L1234-1 proposé ne définit pas les fins de contrat à compter pour une minoration chômage. La suppression du malus ne vaut aucune suppression de préavis ou de procédure, et quinze jours de notification ne transforment pas une fin d'affectation sans fin d'emploi en rupture salariale.",
'L1221-2': "Le 2° conserve les critères favorables de nature, objet et durée, mais doit les apprécier sur la phase ou l'activité réelle dans le contrat unique de L1221-2 proposé. Cette coordination préserve les minorations futures sans rétablir une embauche à terme ; les fins d'anciens CDD restent régies par leur transition.",
'L1234-9': "L1234-9 fixe les conditions et le montant d'une indemnité patronale, et non un taux de contribution chômage. La suppression du pouvoir de majorer ne supprime aucune indemnité due ; le seuil d'un an au terme effectif, les mois complets et le plafond de six mois du projet ne deviennent pas de nouveaux critères de bonus ou d'exclusion au 1°."
},
'L5521-2': {
'L1234-1': "L5521-2 substitue une référence de validation de retraite à Mayotte et ne vise pas un licenciement. Le nouveau délai privé de quinze jours de L1234-1 n'a donc aucune incidence sur les trimestres ou la borne territoriale de 2028, pas davantage que ses anciens seuils de six mois et deux ans de préavis.",
'L1221-2': "L1221-2 proposé règle la forme des nouveaux emplois, sans modifier l'ordonnance sociale mahoraise. La substitution de L5521-2 continue de servir les périodes recevables avant 2028, y compris sous contrat unique si la réforme intervient avant cette borne ; elle ne rétablit pas de CDD et ne proroge pas le régime territorial après 2027.",
'L1234-9': "Les règles de huit mois de la source et d'un an préavis inclus du projet de L1234-9 concernent la rupture ordinaire privée. Aucune n'est une condition de validation de trimestre à Mayotte. Le présent article ne remplace pas un droit de retraite par l'indemnité plafonnée à six mois et ne ferme pas les recours relatifs aux périodes anciennes."
},
'L6131-1': {
'L1234-1': "La notification patronale et les quinze jours de L1234-1 proposé ne sont le fait générateur d'aucun des financements énumérés ici. Le 3° utilise des années civiles et le 4° des périodes travaillées : ni la date d'un licenciement ni le préavis ne décalent ces bornes, tandis que les salaires de préavis gardent leur régime d'assiette propre.",
'L1221-2': "L'interdiction des nouveaux CDD à L1221-2 proposé ne suffit pas à supprimer la contribution des périodes futures d'un CDD antérieur qui se poursuit. Le 4° et L6331-6 l'éteignent expressément ; le 3° conserve les exclusions et périodes d'alternance dans le contrat unique, sans attacher un terme à l'emploi ou créer une recette nouvelle.",
'L1234-9': "L'indemnité patronale de L1234-9 proposé ne définit ni les effectifs de CSA ni la période travaillée pour le CPF-CDD. Sa condition d'un an à la fin effective préavis inclus et son calcul de 0,20 mois par année totale ne sont pas des conditions supplémentaires d'exonération ou de droit CPF. Les financements supprimés n'effacent pas les indemnités ou créances anciennes."
},
'L6222-5': {
'L1234-1': "L'effet substitutif de la déclaration familiale ne dispense pas du préavis patronal applicable au nouvel emploi privé. Les quinze jours proposés à L1234-1 n'autorisent ni fin automatique après formation, ni suppression du salaire de suspension ou de l'indemnité spéciale de protection du mineur ; les procédures et autorisations distinctes demeurent.",
'L1221-2': "La déclaration vaut contrat et constate désormais la relation indéterminée exigée par L1221-2 proposé. Ses dates de formation et les neuf groupes d'articles matériels maintenus ne permettent pas de fixer un terme d'emploi. Le critère transitoire reste la conclusion de l'engagement, même si le travail commence après l'entrée en vigueur.",
'L1234-9': "Les droits repris par le 5° alimentent l'ancienneté de L1234-9, mais les sommes spéciales de L6225-4 et L6225-5 ne deviennent pas une indemnité ordinaire plafonnée. Pour cette dernière seulement : un an au terme effectif préavis inclus, 0,20 mois par année totale avec mois complets et plafond six mois, sous les réserves de la cible et sans double période."
},
'L6222-16': {
'L1234-1': "L'interdiction du nouvel essai n'est pas une dispense de préavis patronal. L1234-1 proposé fixe quinze jours pour le contrat unique nouveau et conserve les préavis des contrats antérieurs ; la fin de la phase pédagogique n'est ni la notification écrite requise par L1234-3 lu au corpus ni une rupture de l'emploi.",
'L1221-2': "La distinction formation/emploi de L1221-2 proposé justifie la poursuite du même contrat sans nouvel essai. Si un nouvel emploi est conclu dans la même entreprise après un ancien apprentissage, il est aussi indéterminé et sans essai selon L6222-16 proposé ; la transition n'autorise ni CDD nouveau ni remise à zéro de l'ancienneté.",
'L1234-9': "Toute la durée d'apprentissage reprise est retenue pour le seuil d'un an à la fin effective avec préavis inclus de L1234-9 proposé. Une fois ce seuil atteint, 0,20 mois s'applique à chaque année totale et aux mois complets, plafond six mois : la première année n'est pas déduite. Les anciennes composantes et indemnités spéciales demeurent réservées, ainsi que l'exception de faute grave de la cible."
},
'L6222-18-2': {
'L1234-1': "Les six mois de poursuite théorique sont postérieurs à une rupture et ne sont pas le préavis de L1234-1. Les quinze jours proposés doivent être notifiés et calculés dans leur régime propre ; l'obligation du centre ne dispense d'aucune procédure patronale, autorisation protectrice ou ancien délai applicable au contrat source.",
'L1221-2': "L1221-2 proposé interdit qu'une fin de cycle ou de phase pédagogique termine automatiquement l'emploi. Les six mois de L6222-18-2 ne commencent donc pas du seul fait de cette échéance : il faut une rupture entrant dans son champ. L'extension de coordination au contrat unique conserve les garanties anciennes et les exceptions territoriales.",
'L1234-9': "Le statut de stagiaire, la formation de six mois et l'aide à retrouver un employeur ne sont pas l'indemnité ordinaire de L1234-9. Ils restent ouverts avant un an d'ancienneté si leurs conditions sont réunies ; ni le calcul à 0,20 mois par année totale ni le plafond monétaire de six mois ne bornent cette prestation en nature ou les indemnités spéciales."
}
}

special = {
('L5132-6-1','L1251-58-1'): "La source autorise déjà un CDI intérimaire avec contrat de mise à disposition au 1° et lettre de mission au 2°. Sa proposition rend ce support obligatoire pour les futurs recrutements et conserve ancienneté et garanties des CDI existants. L'abrogation de la permission spéciale de L5132-6-1 ne supprime ni ces instruments ni l'accès favorable de son public au CDI d'inclusion.",
('L5132-6-1','L5132-6'): "L5132-6 officiel exclut la section 4 bis et prévoit des contrats de mission pouvant atteindre vingt-quatre mois. Sa proposition réintègre le régime CDI, ses garanties mensuelles et d'intermission, sans plafond légal de mission, et maintient les aides futures. Cette substitution doit prendre effet avec l'abrogation de L5132-6-1 ; ses limites conventionnelles d'affectation restent distinctes du plafond spécial retiré.",
('L5134-57','L1237-1'): "L1237-1 proposé réserve les dispenses légales particulières tout en imposant une notification calculée selon L1234-3 pour la démission ordinaire du nouveau contrat. L5134-57 constitue précisément une dispense historique toujours favorable : aucune formalité de notification ne peut lui substituer quinze jours d'activité, et le départ n'ouvre pas l'indemnité patronale ordinaire.",
('L5213-3-1','L1237-1'): "Le III renvoie réellement à la démission de L1237-1 : sa proposition impose quinze jours calendaires au contrat unique, calculés selon L1234-3 après réception écrite ; les contrats antérieurs gardent leurs règles. Le maintien éventuel d'indemnité journalière n'institue ici aucune dispense de préavis ni condition d'ancienneté d'indemnité patronale.",
('L5213-3-1','L323-3-1'): "Cette cible du code de la sécurité sociale est fournie en droit officiel seulement, sans proposition. Son premier alinéa exige accord du médecin traitant, avis du médecin-conseil et accord de la caisse avec compatibilité de l'action et de l'arrêt ; son 2° vise la convention de rééducation. Donner à cette convention l'effet d'avenant ne supprime aucune de ces conditions de prestation et ne les attribue pas au seul contrat privé.",
('L5213-13-3','L1251-12-1'): "Les plafonds source sont dix-huit mois, neuf mois dans certains cas, vingt-quatre mois dans trois cas et trente-six mois en apprentissage, avec un minimum initial de six mois pour la commande export exceptionnelle. La proposition les abroge pour les nouveaux contrats et conserve les anciens. Les vingt-quatre mois spéciaux de L5213-13-3 restent donc transitoires ; la dispense déjà applicable au CDI n'est pas une seconde coupe.",
('L5213-13-3','L1251-12'): "L1251-12 source vise la durée conventionnelle du contrat de mission ; sa proposition ne conserve cette faculté que pour l'affectation chez l'utilisateur, avec interdiction de pourvoir durablement un poste permanent. La suppression du plafond légal ne retire pas cette compétence conventionnelle ni cette protection ; aucune durée d'affectation ne devient un terme au contrat unique.",
('L5213-13-3','L1251-36'): "La carence officielle se mesure en jours d'ouverture de l'utilisateur, suivant la durée du contrat et ses renouvellements. Sa proposition supprime la carence pour les embauches et affectations nouvelles et arrête les délais en cours, tout en réservant les actions anciennes et les sanctions plus douces. L5213-13-3 garde ses dispenses sans renvoi prospectif à un fondement abrogé et sans compter une deuxième réduction.",
('L5213-13-3','L1251-58-1'): "La faculté de CDI de la source devient, dans la proposition, l'unique support des recrutements futurs. La mission conserve sa lettre et son contrat commercial distincts ; ni sa fin ni la fin du parcours n'interrompt l'emploi et l'ancienneté. L'application de cette règle aux entreprises adaptées est recensée avec ses coûts d'intermission, et non présentée comme une économie certaine.",
('L5213-13-3','L1251-58-2'): "Le deuxième alinéa source assimile les intermissions à du travail effectif pour congés payés et ancienneté. La proposition conserve cet avantage et les huit rubriques de l'écrit, dont mobilité respectant la vie familiale, joignabilité, qualifications et garantie mensuelle. Le renvoi de L5213-13-3 préserve tout cet ensemble, sans nouvelle ancienneté ou essai à chaque mission.",
('L5213-13-3','L1251-58-3'): "La rémunération garantie source est au moins le SMIC multiplié par les heures de la durée légale du mois, compte tenu des rémunérations de missions. La proposition la maintient explicitement sans mission et selon la durée légale applicable au contrat. Le volume de travail adapté de L5213-13-3 ne permet aucune réduction implicite de cette garantie ; son extension aux nouveaux emplois est une obligation recensée.",
('L5213-13-3','L1251-58-6'): "La dispense officielle du plafond légal profite déjà au CDI intérimaire, avant toute réforme. Sa proposition la confirme pour le contrat unique et protège les garanties entre missions. Le renvoi nouveau de L5213-13-3 conserve cette faveur sans appliquer vingt-quatre mois au CDI ; le propre renvoi de la cible à L1251-12-1 abrogé dans le projet nécessite une coordination, sans rétablissement du plafond.",
('L5422-12','L1251-1'): "Le 1° source vise le contrat commercial de mise à disposition, le 2° le contrat salarial de mission ; la proposition remplace seulement le second par une lettre d'affectation au sein du contrat unique. L5422-12 conserve l'exclusion des anciens contrats de mission et ne compte pas la fin d'une lettre comme rupture de l'emploi. Les fins commerciales du 1° restent dans leur champ distinct, y compris avec utilisateur public sous la section 6.",
('L5521-2','L5132-15-1'): "Le renvoi à CSS L351-2 figure dans la règle de durée du travail et sert à valider la retraite des salariés d'atelier ou chantier, sans condition de rupture. La proposition conserve vingt heures et leurs dérogations, mais son renvoi de seuil de cumul à L3123-27 ne fournit plus de nombre dans le projet : rectification nécessaire dans cette cible. L'adaptation mahoraise n'efface ni cette faveur ni les droits constitués avant 2028.",
('L5521-2','L5132-11-1'): "Le renvoi social de cette cible assure la validation des trimestres des salariés d'association intermédiaire. La proposition en maintient le principe, le minimum spécial de vingt heures et l'exception de cumul, tout en séparant parcours et emploi. Le seuil de cumul visant L3123-27 doit encore être coordonné ; la clause réglementaire proposée ne reprend plus l'ordinal ancien. La substitution mahoraise demeure limitée aux périodes antérieures à 2028.",
('L6131-1','L6331-6'): "La source fixe 1 % du revenu d'activité retenu pour les cotisations sociales des titulaires de CDD, hors formations/alternance listées par décret et emplois saisonniers. Sa proposition supprime ce prélèvement pour les périodes travaillées après la réforme, même dans un ancien CDD. Le 4° utilise la même borne, conserve exclusions et restitutions anciennes et protège droits CPF et abondements sans taxe de remplacement.",
('L6131-1','L6242-1'): "La vue actuelle supprime la CSA dès le 1er janvier suivant l'entrée en vigueur, mais son II garde l'alternance et l'année suivante sans double compte pour la créance ; son V conserve les exclusions d'effectif des missions de même objet en contrat unique à partir des lettres et mises à disposition existantes. Son VIII maintient aussi ces exclusions d'assiette et exonérations pour les anciennes années. Le 3° reprend ces garanties, garde la créance et l'aide futures, et ne rétablit ni versement de mars ni déclaration ou liste annuelle de redevables supprimés.",
('L6222-5','L6222-16'): "Le 5° vise effectivement absence de nouvel essai, rémunération et ancienneté après apprentissage. La source de L6222-16 réserve une convention contraire ; sa vue proposée ferme cette réserve aux contrats nouveaux, sans limiter la reprise de durée à l'après-réforme. L'article complet du présent lot explicite la date de cette règle ; la déclaration familiale applique ces droits sans nouvel engagement formel et sans double compte de l'ancienneté.",
('L6222-18-2','L6222-18'): "La cible officielle distingue quarante-cinq jours de pratique, accord écrit, motifs spéciaux, départ avec médiation et liquidation ; sa note exclut les contrats conclus avant le 1er janvier 2019. La proposition coordonne le nouveau contrat unique avec quinze jours de préavis et conserve les régimes anciens. Le renvoi déclenche toujours la continuité de formation après une rupture réelle, même sans indemnité ordinaire avant un an. La transition pré-2019 et les indemnités spéciales doivent rester expressément réservées, sans assimiler le secteur public à un statut privé ordinaire."
}

for item in answer:
    number = item['number']
    source_item = next(s for s in source if s['number'] == number)
    for field in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert item[field] == source_item[field]
    required = refs['requirements'][item['code_id'] + '|' + item['source_id']]
    fresh_checks = []
    for key in required:
        target = refs['targets'][key]
        target_number = target['number']
        assessment = common[number].get(target_number)
        if assessment is None:
            assessment = special[(number, target_number)]
        assert len(assessment) >= 80
        fresh_checks.append({'target_key': key, 'view_sha256': target['view_sha256'], 'assessment': assessment})
    item['reference_checks'] = fresh_checks

# Aucune nouvelle référence ni modification d'une cible en cours de rédaction.
assert refs_path.read_bytes() == refs_bytes
(root / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
(root / 'input-snapshot.json').write_text(json.dumps({
    'reference_targets_file_sha256': hashlib.sha256(refs_bytes).hexdigest(),
    'files': {name: hashlib.sha256((root / name).read_bytes()).hexdigest()
              for name in ('source.json', 'policy.json', 'coordination.json', 'previous-answer.json')},
    'reference_views': {k: v['view_sha256'] for k, v in refs['targets'].items()}
}, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles, {sum(len(x["reference_checks"]) for x in answer)} analyses de renvoi actuelles.')
