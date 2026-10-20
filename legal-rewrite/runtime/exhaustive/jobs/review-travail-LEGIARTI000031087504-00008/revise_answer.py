import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent
sources = json.loads((ROOT / 'source.json').read_text())
refs_bytes = (ROOT / 'reference-targets.json').read_bytes()
refs = json.loads(refs_bytes)
answers = copy.deepcopy(json.loads((ROOT / 'previous-answer.json').read_text()))
by_number = {a['number']: a for a in answers}
target_by_key = refs['targets']

# Le texte intégral du précédent essai est le point de départ ; seules les
# corrections normatives ou de traçabilité identifiées sont apportées.
a = by_number['L1255-1']
a['proposed_xml'] = a['proposed_xml'].replace(
    "prévues à l'article L. 1251-2 est puni",
    "prévues au premier alinéa de l'article L. 1251-2 est puni",
).replace(
    "aux indemnités prévues aux articles L. 1235-2, L. 1235-3 ou L. 1235-5.",
    "aux indemnités prévues aux articles L. 1235-2 ou L. 1235-3. L'article L. 1235-5 demeure applicable aux exclusions du remboursement des indemnités de chômage ; il ne constitue pas un fondement autonome d'indemnisation du salarié.",
)
a['reason'] = (
    "La suppression déjà proposée des six mois d'emprisonnement en récidive est conservée après comparaison avec les trois alinéas officiels entiers. Les amendes de 3 750 et 7 500 euros et l'interdiction judiciaire de deux à dix ans restent nécessaires pour sanctionner les conditions sectorielles d'exercice ; les infractions autonomes protégeant salaires, santé et lutte contre la fraude subsistent. Le renvoi est limité au premier alinéa de L1251-2 : il ne transforme pas les ajouts proposés sur le contrat unique et les intermissions en une extension implicite de cette incrimination. Coordination explicite supplémentaire, alignée sur la cible actuelle L1251-47 : L1235-2 et L1235-3 fondent les indemnités supplémentaires, tandis que L1235-5 conserve sa seule fonction d'exclusion du remboursement des allocations. Cette rectification ne retire aucune indemnité existante."
)
a['review_notes'] = (
    "Source, note vide, previous_draft et article complet du précédent essai confrontés aux vues actuelles. Le premier alinéa de L1251-2 fourni porte la définition historique de l'entrepreneur, l'exclusivité de son activité et le recrutement et la rémunération selon une qualification convenue ; son second alinéa proposé ajoute les contrats uniques et les garanties d'intermission. La limitation pénale expresse au premier alinéa évite une extension automatique de l'incrimination par ce renvoi. La règle d'emploi sans terme garde ses autres fondements. Amendes de 3 750 et 7 500 euros, interdiction de deux à dix ans inchangées ; seule la prison de six mois est retirée, avec application de la loi pénale plus douce selon son champ, sans extinction générale des créances civiles ni des condamnations pécuniaires définitives. L1235-2 et L1235-5 ont été relus en entier, notes et propositions comprises, dans le corpus public ; les deux tableaux entiers de L1235-3 ont été lus dans reference-targets.json. Le renvoi source à L1235-5 comme fondement indemnitaire est une incohérence préexistante ici expressément rectifiée : ses exclusions (moins de deux ans d'ancienneté ou entreprise de moins de onze salariés) concernent le remboursement des allocations, non une créance salariale. La cible actuelle L1251-47 effectue la même rectification ; aucun numéro de renvoi absent de la source n'est ajouté. Préavis, indemnité ordinaire, réparations d'illégalité et procédures collectives ou autorisations de salariés protégés restent distincts. L'effectivité des sanctions restantes au regard de la directive 2008/104/CE est un point de coordination supérieur ; son texte entier n'est pas fourni et aucune conformité juridique indépendante n'est déclarée."
)
a['substantive_impact']['assessment'] = (
    "Par rapport à toute la source officielle, la prison de six mois en récidive est supprimée sans retirer les amendes ou l'interdiction. La rectification indemnitaire préserve les créances réellement fondées sur L1235-2 et L1235-3 et la dispense distincte de L1235-5. La limitation au premier alinéa de L1251-2 empêche une extension implicite de l'incrimination aux ajouts proposés dans cette cible. Aucune baisse fiscale ni économie nationale n'est démontrée."
)
a['substantive_impact']['new_burdens_review'] = (
    "Aucune charge nouvelle n'est identifiée : la prison n'est remplacée par aucune procédure et les amendes ne sont pas augmentées. Le renvoi limité au premier alinéa de L1251-2 exclut l'extension implicite de cette incrimination aux obligations nouvelles du contrat unique. La correction de L1235-5 n'ajoute ni indemnité ni condition de remboursement."
)
a['substantive_impact']['effects'].append({
    'kind': 'coordination',
    'measure_id': 'interim-coordination-indemnites-interdiction-fermeture',
    'description': "Rectification du renvoi indemnitaire ancien, dans la même mesure que le deuxième alinéa actuel proposé de L1251-47, sans suppression d'un droit ni création d'indemnité.",
    'before': "Le texte cite L1235-5 parmi les indemnités supplémentaires, alors que cet article exclut certains remboursements d'allocations et ne définit pas d'indemnité au salarié.",
    'after': "L1235-2 et L1235-3 restent les fondements indemnitaires ; L1235-5 demeure applicable aux exclusions de remboursement dans son champ propre.",
    'unit': 'legal_duty',
    'affected_population': "Personnel permanent licencié à la suite de l'interdiction judiciaire d'exercer et employeurs concernés",
    'conditions_and_transition': "La rectification ne remet pas en cause les créances civiles et droits antérieurs ; les autres garanties de rupture demeurent applicables.",
    'replacement_or_new_burdens': "Aucun paiement supplémentaire ni formalité nouvelle ; aucune seconde réduction comptée pour ce renvoi.",
    'source_quote': "Lorsque cette mesure entraîne le licenciement du personnel permanent, celui-ci a droit, en dehors de l'indemnité de préavis et de l'indemnité de licenciement, aux indemnités prévues aux articles L. 1235-2, L. 1235-3 ou L. 1235-5.",
    'proposed_quote': "L'article L. 1235-5 demeure applicable aux exclusions du remboursement des indemnités de chômage ; il ne constitue pas un fondement autonome d'indemnisation du salarié.",
})

a = by_number['L1255-2']
a['review_notes'] = a['review_notes'].replace(
    "L1251-47 fourni retire déjà le motif déclaratif de fermeture ; son deuxième alinéa reste la cible indemnitaire, avec le renvoi historiquement incohérent à L1235-5 signalé.",
    "La vue actuelle fournie de L1251-47 retire le motif déclaratif de fermeture et conserve au deuxième alinéa les droits du personnel permanent : elle vise désormais les indemnités de L1235-2 ou L1235-3 et réserve L1235-5 aux exclusions de remboursement d'allocations. Le renvoi du présent article au deuxième alinéa reste donc exact, sans déplacement et sans maintenir l'ancienne présentation de L1235-5 comme indemnité. L1235-2 et L1235-5 ont été relus en entier dans le corpus, avec leurs notes et propositions ; aucune indemnité nouvelle n'est créée.",
)
a['substantive_impact']['effects'].append({
    'kind': 'coordination',
    'measure_id': 'interim-coordination-indemnites-interdiction-fermeture',
    'description': "Le renvoi au deuxième alinéa de L1251-47 suit la correction de sa fonction indemnitaire ; il ne constitue pas une nouvelle réduction de charge.",
    'before': "Le deuxième alinéa de L1251-47 auquel renvoie la source présentait L1235-5 comme un fondement indemnitaire.",
    'after': "Le renvoi conserve sa position et porte sur les indemnités de L1235-2 ou L1235-3 ; L1235-5 reste une exclusion du remboursement d'allocations.",
    'unit': 'legal_duty',
    'affected_population': "Personnel permanent licencié après interdiction judiciaire d'exercer l'activité de travail temporaire",
    'conditions_and_transition': "Droits antérieurs, créances civiles et recours conservés ; aucun déplacement de l'alinéa cible.",
    'replacement_or_new_burdens': "Aucune nouvelle indemnité ni formalité ; coordination de la même mesure que L1255-1 et L1251-47.",
    'source_quote': "Les dispositions du deuxième alinéa de l'article L. 1251-47 sont applicables.",
    'proposed_quote': "Le deuxième alinéa de l'article L. 1251-47 est applicable.",
})
a['review_notes'] += (
    " Écart documentaire local identifié après cette lecture : la source et les notes de L1251-47 concordent entre le corpus public travail.json et reference-targets.json, mais la proposition du corpus conserve l'ancienne vue 14a545761150c04917902fdc5c173fbd36ec96d21f47a01ee43c87d97149eccc. Le présent contrôle retient la vue actuelle expressément fournie dans reference-targets.json, 23107a6becef35bc76be6f05ec13ab3c01ba0e80bfbf014464bb9d33850a7923, avec la rectification de L1235-5. Le corpus extérieur n'est pas modifié et sa proposition ancienne n'est pas traitée comme le droit officiel ni comme la cible actuelle de ce lot."
)
a['substantive_impact']['scope_limitations'] += (
    " La proposition locale du corpus pour L1251-47 est antérieure à la vue actuelle fournie ; cette divergence est signalée sans modifier le corpus et sans substituer son ancienne empreinte à celle requise."
)
by_number['L1255-1']['review_notes'] += (
    " La coordination avec L1251-47 se fonde sur la vue actuelle de reference-targets.json, qui corrige L1235-5 ; la proposition plus ancienne du corpus public local ne contient pas encore cette correction. Les sources officielles concordent, mais ces deux propositions ne sont pas confondues et le corpus reste en lecture seule."
)

# L'interdiction des nouveaux CDD de portage n'est pas présentée comme une
# dépénalisation : la portée nouvelle du 2° est recensée distinctement.
a = by_number['L1255-14']
a['substantive_impact']['classification'] = 'mixed'
a['substantive_impact']['assessment'] += (
    " En sens inverse, le 2° coordonne l'incrimination avec L1254-7 proposé : un nouveau CDD de portage, auparavant une forme d'emploi admise, relève désormais de l'interdiction du contrat à terme et de ses sanctions. Cette portée nouvelle est recensée, sans compter une seconde fusion du contrat unique. Le solde net des coupes et de cette contrainte nouvelle n'est pas établi."
)
a['substantive_impact']['new_burdens_review'] = (
    "Aucun nouveau document, registre, agrément ou dépôt de remplacement n'est créé. Une contrainte de fond nouvelle est toutefois identifiée au 2° : l'interdiction commune des nouveaux CDD de portage entre dans le champ pénal du renvoi à L1254-7, avec 3 750 euros d'amende et, en récidive, 7 500 euros et six mois de prison maintenus pour ce 2°. Les anciens contrats restent valables. Ce changement n'est pas compté comme un allègement ; son solde avec les dépénalisations n'est pas chiffré."
)
a['substantive_impact']['effects'].append({
    'kind': 'coordination',
    'measure_id': 'contrat-unique-duree-indeterminee',
    'description': "Coordination pénale de l'interdiction commune des nouveaux contrats à terme ; portée contraignante expressément recensée, sans nouvelle fusion comptée.",
    'before': "L1254-7 officiel permet le CDD ou le CDI de portage ; le 2° sanctionne le non-respect de ces formes autorisées.",
    'after': "Pour les nouveaux recrutements, seul le contrat unique sans terme est admis ; le 2° sanctionne sa méconnaissance : 3 750 euros, puis 7 500 euros et six mois de prison en récidive.",
    'unit': 'regime',
    'affected_population': "Entrepreneurs de portage et salariés recrutés après la réforme du contrat unique",
    'conditions_and_transition': "Nouveaux contrats à compter de l'entrée en vigueur ; anciens contrats et droits valables conservés, loi pénale plus douce pour les réductions distinctes.",
    'replacement_or_new_burdens': "Extension de la portée de la sanction à une forme d'emploi auparavant admise ; aucune nouvelle déclaration ; solde net non établi.",
    'source_quote': "2° De conclure un contrat de travail en portage salarial sans respecter les dispositions prévues à l'article L. 1254-7 ;",
    'proposed_quote': "2° Il conclut un contrat de travail en portage salarial sans respecter l'article L. 1254-7. Pour les recrutements effectués à compter de l'entrée en vigueur de la loi instituant le contrat de travail unique, le contrat est à durée indéterminée ; la durée d'une prestation commerciale ne fixe pas le terme de l'emploi ;",
})
a['review_notes'] += (
    " Comparaison de fond avec la source entière : la nouvelle portée pénale du 2° liée à L1254-7 n'est pas une coupe et figure dans le bilan mixed. La conservation des sanctions du nouveau contrat unique ne peut être confondue avec l'abrogation des délits documentaires."
)

# Les trois cibles communes sont examinées dans le champ de chaque article.
contexts = {
    'L1254-17': (
        "L'abrogation du renouvellement de portage ne notifie aucune rupture ; une poursuite convenue sans terme conserve l'ancienneté et ne rétablit pas un essai.",
        "Les deux renouvellements ne restent exécutables que s'ils étaient déjà convenus avant la réforme ; une simple clause facultative ne permet pas d'en décider un nouveau ensuite. Le report favorable de prospection des anciens contrats est distinct.",
        "La conversion ou le renouvellement ancien ne fait pas naître automatiquement l'indemnité ordinaire : les primes de fin des anciens CDD conservent leurs propres faits générateurs.",
    ),
    'L1254-21': (
        "Le II, qui ne rémunère pas en général les périodes sans prestation, ne vaut pas dispense de préavis lorsqu'une rupture de l'emploi est effectivement notifiée par l'employeur.",
        "Les mentions allégées s'appliquent à l'emploi continu ; une prestation limitée ne termine pas ce contrat et n'autorise ni nouvel essai ni nouveau CDD.",
        "Les frais, congés et informations contractuelles de portage ne sont pas absorbés par l'indemnité ordinaire, et le II ne supprime pas cette indemnité à la rupture effective de l'emploi.",
    ),
    'L1255-1': (
        "Les salariés permanents licenciés après une interdiction judiciaire restent créanciers du préavis dans leur régime temporel ; l'interdiction n'est pas une dispense d'autorisation ou de procédure collective.",
        "La réduction de peine ne permet pas un nouveau CDD. Le renvoi pénal est désormais expressément limité à la définition du premier alinéa de L1251-2 pour ne pas incriminer implicitement ses ajouts sur le contrat unique.",
        "L'indemnité ordinaire du personnel permanent licencié se distingue des réparations supplémentaires de L1235-2 et L1235-3 ; le zéro avant un an ne ferme pas ces réparations.",
    ),
    'L1255-2': (
        "Ni une fin de mission ni une proposition de radioprotection ne notifie la rupture de l'emploi. Le renvoi indemnitaire du deuxième alinéa de L1251-47 conserve le préavis dû au personnel permanent licencié.",
        "La lettre de mission n'est pas un nouveau contrat de travail et les affectations proposées pour radioprotection ne rouvrent pas de CDD ; les anciens contrats gardent leurs droits civils sous la réserve pénale plus douce.",
        "Le seuil indemnitaire ne ferme ni la rémunération d'intermission ni la protection radiologique ni les réparations du personnel permanent visées par L1251-47.",
    ),
    'L1255-4': (
        "L'affectation irrégulière n'autorise pas une fin automatique de l'emploi : le préavis n'est déclenché que par une notification régulière de rupture, distincte de la fin de mission.",
        "Le troisième alinéa limite le renvoi à L1251-6 aux cas d'affectation auprès de l'utilisateur ; la suppression de la prison ne crée aucun nouveau cas de CDD ou renouvellement.",
        "L'infraction de recours irrégulier n'est pas le fait générateur de l'indemnité ordinaire ; les réparations civiles d'une illégalité et les anciens droits de mission gardent leur régime.",
    ),
    'L1255-6': (
        "L'abrogation du délit du terme ne supprime pas le préavis dû à une rupture de l'emploi ; la fin de l'affectation reste distincte de cette rupture notifiée.",
        "La dépénalisation des règles de terme de mission ne rétablit aucun terme d'emploi ni CDD nouveau. Les règles civiles d'affectation et droits des anciens contrats restent applicables.",
        "Le retrait de l'incrimination n'échange pas les créances civiles de terme des anciens CDD contre le barème ordinaire de rupture du nouvel emploi.",
    ),
    'L1255-14': (
        "Les coupes pénales du portage ne constituent ni une rupture de l'emploi ni une dispense de préavis. Les garanties financières et sanitaires demeurent indépendantes des quinze jours.",
        "Le 2° sanctionne le contrat unique exigé par L1254-7 proposé ; le 4° ne couvre que les plafonds des anciens contrats. Le bilan recense cette portée pénale nouvelle et ne la présente pas comme une réduction.",
        "Les primes de fin des anciens CDD et les droits de salaire ou de congés restent distincts du barème ordinaire ; la dépénalisation documentaire ne les éteint pas.",
    ),
    'L1262-2': (
        "Le renvoi au travail temporaire ne rend pas le préavis français automatiquement applicable au contrat étranger : la loi réellement applicable et les règles impératives de détachement doivent être déterminées.",
        "Le nouveau régime français ne convertit pas un contrat régulièrement soumis à une loi étrangère ; cette réserve ne valide pas un CDD fictivement étranger relevant en réalité du droit français.",
        "Les 10 % de fin de mission du CDD étranger éligible ne sont pas remplacés par l'indemnité ordinaire française ; son champ dépend de la loi réellement applicable à la relation.",
    ),
    'L1262-7': (
        "L'exclusion maintenue d'une dispense administrative ne règle aucune rupture du contrat étranger et ne lui impose pas un préavis français par simple définition sectorielle.",
        "Le maintien des deux exclusions de la section ne crée aucun CDD nouveau dans le champ français et ne convertit aucun contrat étranger : ce sont des limites de dispense de détachement.",
        "Aucun renvoi indemnitaire n'existe dans cet article maintenu : les indemnités étrangères et les anciens droits ne sont pas absorbés par une définition de la dispense de contrôle.",
    ),
    'L2143-2': (
        "La dispense d'ancienneté pour le mandat ne dispense jamais de l'autorisation de licenciement du représentant ; la notification régulière de rupture vient après les protections applicables.",
        "Les salariés employés sans terme sont éligibles dès l'embauche, avant la première mission et pendant les intermissions ; les anciens contrats de mission bénéficient aussi de la dispense sans prolongation de leur terme.",
        "La suppression de l'ancienneté de désignation ne supprime pas le seuil distinct de l'indemnité ordinaire. Dès la désignation, même avant un an, réparations d'illégalité et protection du mandat restent ouvertes.",
    ),
    'L2241-9': (
        "L'examen de prévisions salariales et d'emploi n'est pas une notification de licenciement ; le délai de remise d'informations supprimé ne se confond pas avec le préavis individuel ou les procédures collectives.",
        "Le 1° ne suit que les CDD antérieurs et les affectations temporaires, y compris en CDI ; il n'autorise aucun recrutement ou renouvellement à terme sous couvert de prévisions de branche.",
        "La remise simplifiée des données salariales ne modifie aucun fait générateur d'indemnité de rupture ni les anciennes composantes, congés et réparations autonomes.",
    ),
    'L2254-2': (
        "Le V reprend les quinze jours pour les seuls nouveaux contrats ; le refus de l'accord n'est pas une faute grave. Ni le mois de refus ni les deux mois d'engagement de procédure ne sont des préavis.",
        "Seules les relations nouvelles du champ privé relèvent du contrat unique ; la durée de l'accord, d'un forfait ou de la formation CPF n'est jamais un terme de l'emploi.",
        "La proposition retient explicitement les mois complets, toute la première année dès le seuil atteint et le terme effectif préavis inclus. Le CPF spécial et les réparations d'illégalité ne sont ni plafonnés ni absorbés.",
    ),
}

special = {
    'L1254-17': {
        'L1254-12': "Le texte officiel plafonne à dix-huit mois la durée totale, renouvellements compris, et sa note vise historiquement les contrats en cours. La vue proposée abroge ce plafond pour l'avenir : notre renvoi vise donc sa rédaction antérieure pour les renouvellements déjà convenus, avec le report de prospection distinct, sans limiter la durée du nouvel emploi.",
    },
    'L1255-1': {
        'L1251-2': "La définition officielle réunit activité exclusive de mise à disposition, recrutement et rémunération selon une qualification convenue. La vue proposée ajoute un second alinéa sur les nouveaux contrats uniques et leurs intermissions. Notre premier alinéa pénal vise désormais le seul premier alinéa de la cible : maintien des conditions historiques sanctionnées, sans extension pénale implicite aux ajouts de la proposition.",
        'L1235-3': "La cible est une source officielle sans proposition. Ses deux tableaux entiers distinguent minima et maxima selon ancienneté, avec minima particuliers sous onze salariés et maxima jusqu'à vingt mois ; le juge peut proposer la réintégration. Ces réparations d'une absence de cause réelle et sérieuse restent distinctes du barème ordinaire de six mois. Le renvoi correctif ne crée aucun minimum absent de ces tableaux.",
    },
    'L1255-2': {
        'L1251-16': "Le 1° pénal vise seulement les mentions des 1° et 3° de la cible, non toute sa liste. La proposition y admet la lettre de mission et la communication d'informations déjà accessibles, exactes et conservables. Notre texte respecte ces dispenses : une mention légalement supprimée ou régulièrement communiquée ailleurs ne redevient pas une omission pénale ; aucun nouveau contrat n'est requis à chaque affectation.",
        'L1251-17': "Source et proposition conservent le maximum de deux jours ouvrables suivant la mise à disposition ; la proposition porte sur la lettre et les informations non déjà remises, sans double transmission. Notre suppression vise la sanction du seul retard, non cette obligation civile ni ce délai. L'absence totale d'écrit transmis demeure distincte du retard dépénalisé.",
        'L1251-26': "Le deuxième alinéa, dans la source et la vue proposée, interdit les modifications essentielles de qualification, rémunération, horaire et transport. Le 3° incorpore seulement ces quatre garanties pour la proposition radiologique. Il n'importe ni le mécanisme général de rupture de mission exclu pour le CDI intérimaire ni un nouveau contrat à terme ; les trois jours sont ceux de L1251-34.",
        'L1251-34': "La vue actuelle est déjà coordonnée en affectations : proposition sous trois jours ouvrables, quatre garanties essentielles et calcul de la limite annuelle d'exposition rapportée à la durée totale des missions. Notre 3° conserve sa sanction et ces conditions, sans donner de terme à l'emploi ni effacer une exposition déjà subie. La note de l'ordonnance de 2017 garde son champ historique.",
        'L1251-47': "La vue actuelle, distincte de celle du précédent essai, retire le défaut déclaratif du fondement de fermeture et maintient défaut de garantie, risque sérieux, mise en demeure et maximum de deux mois. Son deuxième alinéa vise désormais les indemnités de L1235-2 ou L1235-3 et réserve L1235-5 à l'exclusion de remboursement d'allocations. Notre renvoi au deuxième alinéa reste exact et ne rétablit pas l'ancienne indemnité inexistante ; ses droits antérieurs restent protégés.",
    },
    'L1255-4': {
        'L1251-6': "Le renvoi conserve les deux branches exactes de l'infraction : l'objet précis et temporaire du premier alinéa, puis les cinq cas de recours sous la réserve de L1251-7. La proposition conserve remplacements, accroissement et activités saisonnières comme cas d'affectation ; notre troisième alinéa ne les convertit pas en terme du contrat unique et ne supprime aucune de leurs exceptions.",
    },
    'L1255-6': {
        'L1251-11': "La source prévoit terme précis, cinq cas sans terme précis et durée minimale. La proposition conserve ces règles comme durée d'affectation dans une lettre de mission pour les nouveaux emplois, sans fin automatique de l'emploi. Notre abrogation porte sur leur seul délit autonome : ces conditions civiles et les droits de terme des anciens contrats ne sont pas abrogés, ni assimilés aux quinze jours de préavis.",
    },
    'L1255-14': {
        'L1254-15': "Les listes officielles 1° a à i et 2° a à h distinguent les clauses d'emploi et de prestation du CDD de portage. La vue proposée les abroge pour l'avenir mais les réserve aux contrats déjà valablement conclus. Le 6° pénal suit ce seul champ historique, sans les imposer aux nouveaux contrats uniques ni faire refaire les anciens écrits ; les garanties autonomes restent applicables.",
        'L1254-20': "La source exige écrit et intitulé du CDI de portage ; la vue proposée les coordonne avec le nouveau contrat unique et dispense de refaire les anciens contrats. L'abrogation du 5° pénal supprime le délit d'intitulé, sans abroger l'exigence civile d'écrit ni fermer un droit d'information ou introduire une forme exclusive supplémentaire.",
        'L1254-21': "La vue fournie fusionne les frais au 1°, retire les 3° et 7° et dispense de répéter les données sociales du 6°. Le texte complet de notre lot conserve ces coupes et étend au 8° la dispense de recopier le garant déjà communiqué et exact. Le 6° pénal respecte les mentions et dispenses réellement applicables, y compris cette extension, sans rétablir le reporting ; le II non rémunéré du portage demeure distinct de l'intérim.",
        'L1254-7': "Le texte officiel admet contrat déterminé ou indéterminé ; la proposition impose le contrat unique aux nouveaux recrutements et réserve les anciens contrats avec leurs droits. Notre 2° coordonne effectivement cette interdiction, sans prendre la durée commerciale pour un terme d'emploi. Sa portée pénale plus large sur une forme auparavant autorisée est recensée dans substantive_impact mixed, non qualifiée d'allègement.",
        'L1254-12': "Le plafond officiel de dix-huit mois, renouvellements compris, et la note historique sont distingués de la réforme future. La proposition abroge le plafond pour les nouveaux emplois et le conserve, avec les renouvellements déjà convenus et le report de prospection, pour les anciens CDD. Notre 4° sanctionne seulement ce champ antérieur et ne limite pas la durée du contrat unique.",
        'L1254-17': "La source autorise deux renouvellements, clause ou avenant soumis avant le terme initialement prévu. La vue proposée, conservée dans notre lot, interdit tout nouveau renouvellement après réforme, même fondé sur une simple faculté ancienne, mais protège ceux déjà convenus et le report favorable de prospection distinct. Le 4° suit cette transition et ne recrée aucune autorisation de CDD nouveau.",
    },
    'L1262-2': {
        'L1251-32': "Le texte officiel ouvre, sauf CDI immédiat chez l'utilisateur, un complément de salaire de 10 % de toute la rémunération brute, payé à chaque fin de mission avec le dernier salaire et inscrit au bulletin. La proposition de la cible réserve ce régime aux anciens contrats. Notre quatrième alinéa conserve expressément l'ancienne rédaction pour les futurs CDD valablement soumis à une loi étrangère ; il ne ferme pas leur avantage au nom de la transition française.",
        'L1251-33': "Les exceptions officielles des 1°, 2° et 4°, ainsi que le 3° déjà abrogé, ont été confrontées à l'abrogation prospective proposée avec réserve des anciens contrats. Notre maintien de l'ancienne rédaction pour les CDD étrangers futurs conserve ensemble l'indemnité et ces exceptions ; la dispense générale des CDI dans leur pays d'origine est aussi maintenue. Aucune dispense ancienne ne devient une dispense de préavis du contrat unique.",
    },
    'L1262-7': {
        'L1251-2': "Ce renvoi définit les entreprises exclues de la section de dispense : mise à disposition exclusive de salariés recrutés et rémunérés selon une qualification convenue. Le second alinéa ajouté dans la proposition sur le contrat unique et les intermissions ne convertit pas à lui seul les contrats étrangers des entreprises ainsi identifiées. L'article est maintenu sans nouvelle rédaction ni renvoi de rupture.",
    },
    'L2254-2': {
        'L1232-2': "Le texte officiel exige cinq jours ouvrables et certains modes de convocation. La proposition supprime ce minimum chiffré et ouvre les moyens écrits à date certaine, mais maintient le temps effectif de préparation et le report nécessaire à la défense. Le V suit la transition de la cible selon la date de convocation, non celle de l'accord ; les quinze jours ne résument pas la procédure entière.",
        'L1232-3': "Cette cible n'a que sa source officielle : pendant l'entretien l'employeur expose les motifs envisagés et recueille les explications du salarié. Le V préserve cet échange, qui reste nécessaire après le refus de l'accord ; ni le motif spécifique ni la suppression d'un délai minimal dans les autres cibles ne permet de s'en dispenser.",
        'L1232-4': "Source et proposition maintiennent l'assistance par un membre du personnel et, sans représentants, par un conseiller inscrit sur liste. La dispense proposée d'adresses suppose une liste officielle ou un accès effectif gratuit, avec accès fourni si nécessaire. Le V conserve ces droits selon la transition de convocation, sans nouveau protocole ni condition à l'assistance.",
        'L1232-5': "L'habilitation au décret demeure dans la proposition, mais ne permet plus de rétablir modes exclusifs de convocation, minimum général chiffré ou adresses dispensées. Le renvoi de notre V respecte ces limites et ne reconstitue pas les formalités par le régime de refus d'un accord ; entretien et défense restent effectifs.",
        'L1234-2': "La proposition répute non écrite, pour les nouveaux contrats, une clause de préavis unilatéral différente des quinze jours et précise qu'une dispense d'exécution ne change pas à elle seule terme et sommes dues. Le V suit cette règle, la compensation de L1234-5 et l'ancien régime des contrats antérieurs, sans étendre cette interdiction aux dispenses favorables relevant d'un champ distinct.",
        'L1234-3': "La source fait partir l'ancien préavis à la présentation du recommandé. Pour le nouveau contrat, la proposition compte les quinze jours depuis le lendemain de la présentation, ou de la réception/remise d'une autre notification légalement admise, jusqu'à la fin du quinzième jour même non travaillé. Notre texte reprend cette règle exacte, distincte du mois de refus et des deux mois pour engager le licenciement.",
        'L1234-4': "Source et proposition maintiennent que l'inexécution du préavis n'avance pas le terme ; la proposition réserve la fin d'essai et les reports protecteurs ou collectifs. Notre seuil d'ancienneté est donc apprécié à la fin effective préavis inclus et non à la notification ou au dernier jour travaillé ; aucune dispense d'exécution ne retranche automatiquement une période du calcul.",
        'L1234-5': "La proposition garantit la compensation des salaires, avantages et congés si l'employeur dispense d'exécution ou ne respecte pas les quinze jours. Elle distingue l'indemnité ordinaire et réserve l'inexécution propre au salarié ainsi que l'ancien régime. Notre zéro avant un an et notre plafond légal de six mois ne s'appliquent pas à la compensation du préavis ; le refus de l'accord n'est pas qualifié de faute grave.",
        'L1234-6': "La cible conserve pour la fermeture ou la baisse d'horaire la base du salaire de préavis : durée légale ou conventionnelle applicable au salarié à temps plein, durée contractuelle pour le temps partiel. Le V ne permet pas de réduire ce salaire par le seul passage à quinze jours, ni de relever implicitement les seuils annuels ou plurihebdomadaires maintenus au II.",
        'L1234-7': "La cessation d'activité ne libère pas l'employeur du préavis ; la proposition rappelle les quinze jours pour les nouveaux contrats et distingue force majeure et sinistre. Le renvoi du V préserve cette obligation et ces champs spéciaux : une cessation liée à l'accord ne devient pas une dispense générale de notification, de paiement ou d'autorisation.",
        'L1234-10': "La cessation de l'entreprise ne supprime pas l'indemnité de L1234-9 lorsqu'elle est due. La proposition renvoie à ses conditions, composantes et plafond et réserve force majeure et sinistre. Le V conserve donc cette ouverture conditionnelle et les droits anciens, sans transformer la fermeture en extinction des créances ou en indemnité automatique indépendante du barème.",
        'L1234-14': "Les 1° et 2° étendent certaines règles aux agents non fonctionnaires ou militaires et aux salariés sous statut légal comparable à celui d'entreprises publiques, sous leurs conditions propres. La proposition précise que ce renvoi ne convertit pas un contrat public distinct. Notre V vise le nouveau contrat privé dans son champ, sans lui attribuer artificiellement tous les agents visés par cette cible.",
        'L1234-18': "Le décret demeure chargé d'application, salaire de référence et répartition des périodes ; la proposition lui interdit de changer le seuil d'un an, 0,20 mois ou le plafond de six mois, ou de réduire la composante acquise. Notre V respecte cette hiérarchie : pas de prorata journalier substitué aux mois complets, pas d'année soustraite dès le seuil atteint, pas de double compte des anciennes périodes.",
        'L2253-1': "La source et la proposition fournies comportent un 1° sur les minima hiérarchiques, sans subdivision I. Notre renvoi corrige donc expressément le « 1° du I » de la source vers le 1°, sans réduire ces minima. Les garanties de branche et les restrictions temporelles proposées aux 7°, 8° et 10° ne permettent pas de rétablir CDD, terme de chantier automatique ou renouvellement d'essai dans l'accord.",
        'L1232-6': "La proposition exige toujours notification écrite motivée à date certaine, mais retire l'exclusivité du recommandé et le minimum général d'attente après entretien, tout en préservant explications, délais disciplinaires maximaux et autorisations spéciales. Le V suit sa transition par la date de convocation. Le préavis est ensuite décompté selon L1234-3 et ne se confond pas avec une attente préalable supprimée.",
        'L6323-11': "La source et la proposition conservent alimentation annuelle, seuil de moitié du temps, prorata, plafonds, majorations et dispositions plus favorables, dont l'avantage saisonnier coordonné au contrat unique. Notre VI maintient l'abondement spécial hors alimentation annuelle et plafond pour les futurs licenciements éligibles. Le minimum de 3 000 euros et les quinze jours d'information ont été lus séparément dans R6323-3-2, sans les prétendre contenus dans cette cible.",
        'L1234-11': "Les suspensions n'interrompent pas l'ancienneté, mais leur durée ne compte pas toujours, sauf exceptions et assimilations applicables, dont celle des élus locaux mentionnés au premier alinéa de L3142-88. La proposition apprécie l'ancienneté reconnue au terme effectif préavis inclus et interdit le double compte des anciennes composantes. Le V conserve ces distinctions et ne retranche aucune première année après le seuil.",
        'L1234-8': "La proposition n'impose aucune ancienneté pour le préavis des nouveaux contrats et interdit sa réduction du fait des suspensions ; les règles historiques d'ancienneté et de suspension des anciens préavis demeurent. Notre V n'importe donc pas le seuil indemnitaire d'un an dans le droit aux quinze jours et ne retire pas l'exception historique des élus locaux dans le champ ancien.",
    },
}

base_preavis = (
    "La source de L1234-1 distingue moins de six mois, un mois de six mois à moins de deux ans et deux mois ensuite, sauf règles plus favorables. La vue proposée fixe quinze jours calendaires pour les contrats nouveaux, conserve l'ancien régime et réserve procédures et protections distinctes. "
)
base_unique = (
    "L1221-2 officiel permet les contrats à terme dans les cas prévus ; la proposition les ferme aux relations nouvelles et aux renouvellements après réforme, tout en distinguant durée de mission ou de formation et durée de l'emploi. "
)
base_indemnite = (
    "La source de L1234-9 ouvre à huit mois hors faute grave et renvoie au calcul réglementaire. La proposition exige, pour les nouveaux contrats rompus par l'employeur, un an au terme effectif préavis inclus, puis 0,20 mois sur toute l'ancienneté, mois complets au prorata et plafond légal de six mois ; faute grave, minima plus favorables et composante acquise des anciens contrats gardent leur champ. "
)

for source, answer in zip(sources, answers):
    assert all(source[k] == answer[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
    number = source['number']
    key = source['code_id'] + '|' + source['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = target_by_key[target_key]
        tn = target['number']
        if tn == 'L1234-1':
            assessment = base_preavis + contexts[number][0]
        elif tn == 'L1221-2':
            assessment = base_unique + contexts[number][1]
        elif tn == 'L1234-9':
            assessment = base_indemnite + contexts[number][2]
        else:
            assessment = special[number][tn]
        checks.append({
            'target_key': target_key,
            'view_sha256': target['view_sha256'],
            'assessment': assessment,
        })
    answer['reference_checks'] = checks

    # Traçabilité nouvelle de cette passe : les anciennes analyses et
    # empreintes ne sont jamais utilisées comme autorité de vérification.
    answer['review_notes'] += (
        " Nouvelle passe de contrôle : la source officielle entière, ses notes, previous_draft et le texte complet de previous-answer.json ont été confrontés aux sources, notes et propositions actuelles de reference-targets.json. Les reference_checks ci-joints portent sur ces vues actuelles, distinguées du droit en vigueur ; les anciennes empreintes et analyses ne valent pas certificat. Les suppressions de sanctions ne sont pas assimilées à une suppression des obligations civiles maintenues."
    )

assert hashlib.sha256((ROOT / 'reference-targets.json').read_bytes()).digest() == hashlib.sha256(refs_bytes).digest()
(ROOT / 'answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({
    'output_file': 'answer.json',
    'article_count': len(answers),
    'reference_checks': sum(len(a['reference_checks']) for a in answers),
    'reference_file_sha256': hashlib.sha256(refs_bytes).hexdigest(),
}, ensure_ascii=False))
