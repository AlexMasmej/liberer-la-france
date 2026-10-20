import json
from html import unescape
from html.parser import HTMLParser

sources = json.load(open('source.json'))
refs = json.load(open('reference-targets.json'))
by_number = {a['number']: a for a in sources}
targets = {a['number']: (k, a) for k, a in refs['targets'].items()}


def paras(*parts):
    return ''.join('<p>' + p + '</p>' for p in parts)


answers = []
for s in sources:
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(status='rewrite_draft', proposed_xml=s['previous_draft']['proposed_xml'])
    answers.append(a)
out = {a['number']: a for a in answers}


def revise(number, reason, notes, removed=None):
    a = out[number]
    a.update(reason=reason, review_notes=notes)
    if removed:
        a.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)


for n, reason, notes in [
    ('L1221-1',
     'Maintien intégral de la source après examen de sa fonction : le droit commun garantit le consentement, la capacité et la force obligatoire du contrat ; la liberté de forme dispense précisément les parties d’un écrit contractuel général. L’article ne prévoit ni taxe, cotisation accessoire, autorisation, déclaration, délai minimal ni justificatif à retirer. Le brouillon ne faisait que reformuler ces deux règles ; il n’est pas conservé comme une simplification.',
     'La liberté de forme ne rétablit pas la faculté de conclure de nouveaux CDD supprimée dans la proposition de L. 1221-2. Elle reste articulée avec les écrits spéciaux maintenus, notamment le temps partiel et les informations de L. 1221-5-1 avec leurs dispenses. Le présent maintien ne porte ni sur la durée de l’essai ni sur le préavis ou le barème d’indemnité. Le droit public des agents n’est pas assimilé au contrat privé.'),
    ('L1225-1',
     'Maintien intégral de la source après examen des charges et doublons : les interdictions de discrimination dans l’embauche, l’essai et la mutation, ainsi que de recherche patronale d’informations sur la grossesse, protègent l’égalité, la santé et la vie privée. Leur objet précis dépasse le seul principe général d’égalité. Les retirer supprimerait une protection essentielle, sans éliminer une formalité administrative. Les trois exceptions d’affectation temporaire favorables sont conservées pour les futures situations éligibles. Le brouillon était une reformulation sans réduction démontrée.',
     'L. 1225-7, L. 1225-9 et L. 1225-12, lus intégralement, maintiennent dans leurs champs la nécessité médicale, l’accord à un changement d’établissement et les garanties de rémunération ; la réserve du premier alinéa porte sur la mutation, non sur le refus d’embauche ou la rupture d’essai. L. 1225-2 et L. 1225-3 préservent la non-révélation et le régime de preuve favorable ; L. 1225-3-1 étend ces protections aux projets parentaux qu’il définit. Le contrat unique et son essai ne dérogent pas à ces règles. Les directives 92/85/CEE et 2006/54/CE nécessitent une coordination dans leur champ ; aucun texte européen n’est déclaré abrogé ou réécrit.')]:
    revise(n, reason, notes)
    out[n].update(status='retained_unchanged', proposed_xml=None)

revise('L1221-5-1',
       'La réforme déjà inscrite au brouillon supprime réellement la mise en demeure obligatoire avant le recours judiciaire et l’attente qui en dépend. La réutilisation d’un écrit complet déjà remis explicite une possibilité de la source, qui admet un ou plusieurs documents : elle n’est pas comptée comme une seconde obligation supprimée. Après lecture des modalités réglementaires, aucune autre coupe n’est justifiée dans cet article : l’information écrite rend les conditions d’emploi accessibles et participe à la transposition de la directive (UE) 2019/1152. Aucun formulaire ni déclaration de remplacement n’est créé.',
       'R. 1221-34 à R. 1221-41 et leurs notes ont été lus : retirer la mise en demeure et les sept jours calendaires de R. 1221-41, sans toucher aux délais de remise de sept jours et d’un mois de R. 1221-35 ni à l’information avant départ de R. 1221-37. Conserver les renvois permis, l’accessibilité et la preuve de transmission électronique de R. 1221-39 et la dispense de R. 1221-40 pour les seuls changements normatifs. Coordonner le 5° de R. 1221-34 avec l’absence de nouveau terme d’emploi. L. 1271-5 maintient la dispense CESU pour les emplois ne dépassant pas trois heures par semaine sur quatre semaines ; L. 7122-24, R. 7122-18 et R. 7122-21 maintiennent les équivalences du guichet du spectacle, sans nouveaux CDD. Le second alinéa du II de l’article 19 de la loi n° 2023-171, seulement cité dans la note source, reste à lire dans sa version intégrale hors corpus lors de l’intégration : son champ historique est réservé, sans en inventer les conditions. La procédure proposée vaut pour les actions nouvelles et les instances en cours, sans remettre en cause la chose définitivement jugée. La directive et les délais réglementaires ne sont pas réécrits dans ce lot.',
       ['Mise en demeure obligatoire de l’employeur comme préalable à la saisine du juge pour obtenir les informations manquantes ou incomplètes.'])

out['L1222-15']['proposed_xml'] = paras(
    'Lorsque le salarié choisit, au cours ou au terme de sa période de mobilité, de ne pas réintégrer son entreprise d’origine, le contrat de travail qui le lie à son employeur est rompu par démission. Aucun préavis autre que celui prévu par l’avenant mentionné à l’article L. 1222-13 ne lui est applicable.',
    'Pour le contrat de travail unique conclu à compter de l’entrée en vigueur de la loi instituant ce contrat, le préavis prévu par cet avenant ne peut excéder quinze jours calendaires. Le salarié notifie son choix par écrit ; le préavis se compte à partir du lendemain de la réception de cette notification par l’employeur, tout moyen établissant cette date de réception étant admis. Il expire à la fin du dernier jour, même non travaillé. L’absence de préavis ou un préavis plus court prévu par l’avenant, ainsi que les autres dispenses favorables applicables au salarié, sont conservés. Le délai d’information prévu par l’avenant pour ce même choix se confond avec ce préavis et ne peut imposer une notification plus précoce.',
    'Les contrats conclus avant cette entrée en vigueur et leurs avenants demeurent régis par les dispositions antérieures, sauf conversion convenue en contrat unique. Cette conversion conserve toute l’ancienneté et les créances acquises. La durée de la mobilité ne constitue pas un terme du contrat de travail.')
revise('L1222-15',
       'La réduction déjà acquise du préavis convenu à quinze jours calendaires au maximum est conservée pour le contrat unique ; l’information préalable ne peut s’y ajouter. Le point de départ imprécis du brouillon est rectifié : décompte dès le lendemain de la réception de la notification écrite, et non le jour même. Les dispenses et durées plus courtes restent ouvertes. La démission suppose toujours un choix du salarié ; la suspension et le droit de retour ne peuvent être supprimés sans détruire la mobilité sécurisée. Aucun délai supplémentaire, document spécial ou agrément n’est introduit.',
       'L. 1222-12 à L. 1222-14 ont été lus en entier : l’avenant de mobilité fixe un délai d’information écrite, sans définir un second préavis autonome. Coordonner L. 1222-13 avec la confusion expresse des deux délais pour le contrat unique. Le décompte est celui du L. 1234-3 proposé, lu intégralement dans reference-targets.json ; il est explicité ici sans ajouter un renvoi normatif. Cette cible n’est pas ajoutée aux reference_checks de cet article, dont les trois cibles requises sont exactement celles de requirements. L. 1237-1 doit conserver la dispense ou le préavis plus court de cet article. Le silence du salarié et l’absence d’un poste de retour conforme ne deviennent pas une démission. Le contrat de l’entreprise d’accueil reste distinct. Les anciens avenants conservent leur régime, sans remise à zéro d’ancienneté lors d’une conversion. Cette démission n’ouvre pas par elle-même l’indemnité ordinaire patronale.',
       ['Préavis conventionnel de non-retour excédant quinze jours calendaires pour le contrat unique et délai d’information supplémentaire imposant la notification plus tôt.'])

out['L1223-5']['proposed_xml'] = out['L1223-5']['proposed_xml'].replace(
    'Le préavis individuel est de quinze jours calendaires pour le contrat unique.',
    'Le préavis individuel est de quinze jours calendaires pour le contrat unique ; il se compte à partir du lendemain de la présentation ou, lorsque la loi autorise une autre forme de notification, de la réception de la notification écrite du licenciement, dans les conditions de l’article L. 1234-3.')
revise('L1223-5',
       'Suppression de fond conservée : l’accord collectif de branche ou d’entreprise cesse d’être un préalable à l’affectation en mission à l’exportation. La mission, accomplie en majeure partie hors du territoire national, devient une affectation du contrat unique indéterminé pour les nouvelles relations ; sa fin ne rompt pas l’emploi. L’exclusion du licenciement économique et la procédure de L. 1236-7 sont conservées dans leur champ. La seconde passe rectifie le décompte du préavis sans retirer les garanties de défense, le contrôle du motif ou les droits spéciaux : ces protections ont une fonction essentielle. Aucun écrit contractuel spécial, autorisation ou déclaration ne remplace l’accord préalable.',
       'Les renvois à L. 1223-6, L. 1223-7 et L. 1236-7 sont vérifiés sur les sources et propositions fournies. Les garanties de rémunération, d’indemnité sans seuil d’ancienneté, de formation, de reclassement et de protection sociale restent ouvertes aux futures missions, même sans accord spécial ; leur détermination directe est traitée à L. 1223-6. Le nouveau renvoi à L. 1234-3 vise son décompte proposé et figure parmi les cibles requises et fournies de reference-targets.json. L. 1232-1 à L. 1232-6 ont été lus dans le corpus : motif, entretien, assistance, notification et délais propres restent distincts des quinze jours de préavis. R. 1221-36 et R. 1221-37 gardent l’information avant départ. L’extension de la dérogation économique aux missions sans accord ne dispense jamais des procédures collectives distinctes imposées dans leur champ, notamment par la directive 98/59/CE, ni des protections spéciales ; la convention OIT n° 158 reste à articuler. Ces textes supérieurs ne sont pas réécrits ici et leur conformité n’est pas présumée. Les contrats anciens et stipulations plus favorables, y compris pour de futurs salariés éligibles, sont préservés.',
       ['Accord collectif préalable obligatoire de branche ou d’entreprise pour recourir au régime de mission à l’exportation, sans déclaration ni agrément de substitution.'])

out['L1223-6']['proposed_xml'] = out['L1223-6']['proposed_xml'].replace(
    'les fractions d’année étant prises en compte au prorata,',
    'les fractions d’année étant prises en compte au prorata des mois complets,')
revise('L1223-6',
       'Les suppressions de fond du brouillon sont maintenues : retrait de la désignation collective préalable des catégories de salariés, du minimum légal de six mois de mission et des mentions de taille et de type d’entreprise. Le renvoi aux informations déjà remises évite un support spécial. Les contreparties de rémunération, la formation, le reclassement et le minimum indemnitaire sans condition d’ancienneté ni d’effectif sont conservés, aussi pour les futures missions sans accord. La présente passe corrige le prorata : les fractions se calculent sur les mois complets, conformément à la décision actuelle. Le minimum spécial utilise le barème coordonné de 0,20 mois, sans importer le seuil d’un an ; sa limite de six mois ne plafonne pas une garantie plus favorable. L’ouverture sans accord implique la détermination contractuelle des garanties en son absence : cette charge de mise en œuvre est identifiée, et non comptée comme supprimée.',
       'Les 1° à 5° gardent leur place. L. 1223-5 supprime le préalable collectif ; L. 1221-5-1 permet l’information dans les supports existants. R. 1234-4, fourni et lu, conserve le salaire le plus favorable : moyenne des douze mois ou de tout le service s’il est plus court, ou tiers des trois derniers mois avec primes à due proportion ; la fenêtre ne glisse pas à la fin du préavis. R. 1234-1 et R. 1234-2 ont été lus dans le corpus : mois complets, affectation des services entre composantes et absence de double compte. Contrairement aux anciennes notes du brouillon, leurs mois complets sont conformes à la décision actuelle. Pour la mission, l’absence de seuil d’ancienneté demeure une exception expresse à L. 1234-9, avant comme après réforme ; le seuil ordinaire d’un an ne s’applique pas. Les services antérieurs conservent leurs barèmes et minima ; la référence nouvelle ne limite ni les indemnités conventionnelles ou contractuelles plus favorables ni les réparations d’illégalité ou indemnités spéciales d’inaptitude. L. 6321-1 et L. 4141-2 ont été lus : adaptation et sécurité ne remplacent pas les garanties spécifiques de formation. La procédure de L. 1236-7 reste applicable. La coordination des règlements et des accords hors lot demeure à exécuter, sans prétendre ces textes modifiés ici.',
       ['Désignation collective obligatoire des catégories de salariés admissibles à la mission à l’exportation.',
        'Durée minimale légale de six mois de la mission à l’exportation et mention obligatoire d’une durée minimale.',
        'Fixation obligatoire de la taille et du type des entreprises concernées dans l’accord de branche.'])
out['L1223-6']['benefit_review'] = 'Le 3° protège les contreparties de rémunération et le minimum indemnitaire proportionnel sans condition d’ancienneté ni d’effectif : ils demeurent pour les futures missions, même sans accord préalable ; le seuil ordinaire d’un an est expressément écarté. Le salaire de référence le plus favorable et les garanties conventionnelles ou contractuelles supérieures restent applicables. Le 4° conserve les garanties de formation propres à la mission, distinctes de l’adaptation et de la sécurité légales ; le 5° conserve le reclassement. Les contrats anciens gardent leurs garanties et la composante antérieure de leurs indemnités, sans double compte. Les filtres des 1°, 2° et du dernier alinéa ne sont ni des exonérations ni des droits à indemnité : leur retrait ouvre l’affectation et supprime le minimum de six mois sans raccourcir l’emploi. La limite nouvelle concerne la référence légale coordonnée, pas les indemnités plus favorables ; aucune taxe ni cotisation autonome n’est créée ou supprimée par cet article.'

# La garantie spéciale ne doit pas être réduite par l'importation du barème ordinaire.
export_xml = out['L1223-6']['proposed_xml']
old_special = 'Pour le contrat unique conclu à compter de l’entrée en vigueur de la loi instituant ce contrat, ce minimum spécial est égal à 0,20 mois de salaire brut de référence par année totale d’ancienneté, les fractions d’année étant prises en compte au prorata des mois complets, dans la limite de six mois de ce salaire ; aucune condition d’un an n’est opposable. L’ancienneté est appréciée à la fin effective du contrat, préavis inclus. Ce minimum et sa limite ne plafonnent pas une indemnité conventionnelle ou contractuelle plus favorable.'
new_special = 'Pour cette garantie spéciale, le minimum est calculé sur toute l’ancienneté à raison d’un quart de mois de salaire par année pour les dix premières années et d’un tiers de mois par année au-delà de dix ans ; les fractions d’année sont prises en compte au prorata des mois complets. L’ancienneté est appréciée à la fin effective du contrat, préavis inclus. Ni la condition d’un an ni le plafond de six mois de l’indemnité ordinaire ne s’appliquent à ce minimum spécial. Les indemnités conventionnelles ou contractuelles plus favorables restent applicables.'
assert old_special in export_xml
out['L1223-6']['proposed_xml'] = export_xml.replace(old_special, new_special).replace(
    'Pour ces contrats, le minimum indemnitaire reste ouvert sans condition d’ancienneté et quel que soit l’effectif : la part correspondant aux services antérieurs à cette entrée en vigueur conserve son barème et ses minima ; la part correspondant aux services postérieurs relève du barème coordonné de l’indemnité légale, sans appliquer une condition d’un an à cette garantie spéciale. L’ancienneté n’est pas remise à zéro et une même période n’est pas comptée deux fois.',
    'Pour ces contrats, le minimum indemnitaire spécial reste ouvert sans condition d’ancienneté et quel que soit l’effectif, selon les taux et modalités conservés au 3°, sans application du seuil ou du plafond de l’indemnité ordinaire. L’ancienneté n’est pas remise à zéro et une même période n’est pas comptée deux fois ; l’indemnité ordinaire et ce minimum spécial ne se cumulent pas pour indemniser deux fois les mêmes services.')
out['L1223-6']['reason'] = 'Les suppressions de fond du brouillon sont maintenues : retrait de la désignation collective préalable des catégories de salariés, du minimum légal de six mois de mission et des mentions de taille et de type d’entreprise. Les informations existantes évitent un support spécial. Les contreparties de rémunération, la formation et le reclassement restent ouverts aux futures missions. Correction de fond du brouillon au titre de la préservation des indemnités spéciales : le minimum proportionnel sans ancienneté ni condition d’effectif conserve les taux officiels de référence, un quart puis un tiers de mois, sans importer le seuil d’un an, le taux de 0,20 ou le plafond ordinaire de six mois. Ce minimum spécial ne pouvait être traité comme la seule indemnité ordinaire. Les fractions sont calculées en mois complets. L’ouverture sans accord implique la détermination contractuelle des garanties en son absence : cette mise en œuvre est recensée parmi les obligations et non présentée comme supprimée.'
out['L1223-6']['review_notes'] = 'Les 1° à 5° gardent leur place. L. 1223-5 supprime le préalable collectif et L. 1221-5-1 permet les supports existants. R. 1234-1 et R. 1234-2 ont été lus en entier dans le corpus : les taux conservés sont un quart de mois par année jusqu’à dix ans et un tiers au-delà, fractions en mois complets ; ils ne sont pas des taux inventés. La nouvelle rédaction donne à ce minimum spécial un fondement autonome pour les missions futures et anciennes, au lieu de le laisser diminuer par le renvoi au barème ordinaire réformé. L’absence de seuil demeure ; le plafond ordinaire de six mois ne borne pas cette garantie spéciale. L. 1234-9 continue de régler l’indemnité ordinaire dans son champ et les créances acquises ; pas de cumul deux fois pour les mêmes services. R. 1234-4, cible fournie, maintient le salaire le plus favorable entre moyenne des douze mois ou de tout le service s’il est plus court et tiers des trois derniers mois, avec primes à due proportion ; les fenêtres précèdent la notification et ne glissent pas à la fin du préavis. Les contreparties conventionnelles ou contractuelles supérieures restent applicables aux futures situations éligibles. L. 6321-1 et L. 4141-2 lus : adaptation et sécurité ne remplacent pas la formation spécifique. L. 1236-7 garde sa procédure. Les modalités réglementaires doivent réserver expressément ce plancher spécial ; aucune modification hors lot n’est déclarée exécutée. Le renvoi à R. 1234-4 figurait déjà au brouillon mais pas dans la source ; il est fourni et vérifié dans reference-targets.json.'
out['L1223-6']['benefit_review'] = 'Les avantages du 3° sont les contreparties de rémunération et l’indemnité minimale proportionnelle sans condition d’ancienneté ni d’effectif. Ils demeurent pour les futures missions, même sans accord ; les taux officiels du plancher, un quart de mois pour les dix premières années et un tiers au-delà, sont conservés de façon autonome, sans seuil d’un an ni plafond ordinaire de six mois. Le brouillon réduisait ce minimum spécial par assimilation au nouveau barème ordinaire : cette restriction est retirée. Le salaire de référence le plus favorable, les indemnités supérieures et les droits antérieurs subsistent sans double compte. Le 4° conserve les garanties de formation propres à la mission, distinctes des devoirs légaux d’adaptation et de sécurité ; le 5° conserve le reclassement. Les catégories préalables, le minimum de six mois de mission et les mentions de taille ou de type d’entreprise ne constituent ni exonérations ni droits à indemnité : leur suppression ouvre la mission sans limiter la durée indéterminée de l’emploi. Aucun prélèvement autonome ne figure ici.'

revise('L1223-7',
       'Coordination nécessaire conservée : les dispositions de protection sociale de branche ou d’entreprise bénéficient au salarié en mission à l’exportation, même dans le contrat unique et sans accord spécial de mission. L’ancienne dénomination contractuelle ne peut fermer cet avantage. Après examen, aucune cotisation accessoire, déclaration ou contrôle autonome à supprimer ne figure ici ; le maintien de la couverture est une protection essentielle. Cette coordination ne démontre aucune baisse de prélèvement.',
       'La couverture reste ouverte aux contrats anciens et aux futures affectations relevant de L. 1223-5 et L. 1223-6. L’article n’établit pas une affiliation française universelle pour l’activité à l’étranger : territorialité, conventions internationales et règlements (CE) n° 883/2004 et n° 987/2009 gardent leur champ. Leurs textes entiers ne sont pas fournis dans ce lot et ne sont pas présentés comme réécrits. Le nouveau préavis et l’indemnité ordinaire ne réduisent pas cette protection ; aucune procédure de détachement ou cotisation d’un autre régime n’est supprimée par inférence.')

out['L1223-8']['proposed_xml'] = out['L1223-8']['proposed_xml'].replace(
    'le préavis individuel de quinze jours calendaires ne dispense pas',
    'le préavis individuel de quinze jours calendaires, décompté à partir du lendemain de la présentation ou, lorsque la loi autorise une autre forme de notification, de la réception de la notification écrite du licenciement dans les conditions de l’article L. 1234-3, ne dispense pas')
revise('L1223-8',
       'Les réductions de fond du brouillon sont conservées : suppression de l’accord de branche étendu comme préalable à l’affectation et du filtre d’usage sectoriel habituel au 1er janvier 2017. Aucun contrat de forme spéciale ou document distinct ne les remplace. La source qualifiait déjà l’emploi de CDI ; le passage au contrat unique et l’absence de rupture automatique ne sont donc pas comptés comme une seconde suppression de CDD. La présente passe précise le décompte du préavis. L’accord facultatif, les garanties de formation et de rémunération, la réalité du motif et le contrôle du juge restent nécessaires.',
       'L. 1223-9 conserve les garanties matérielles et supprime ses rubriques et circuits redondants ; la détermination des garanties sans accord y est recensée. L. 1236-8, lu en entier, rattache une cause réelle et sérieuse à la fin effective du chantier et renvoie à L. 1232-2 à L. 1232-6, au chapitre IV, à la section 1 du chapitre V et au chapitre VIII : ce n’est jamais une rupture automatique. Sa proposition dans le corpus nécessite encore une coordination avec l’ouverture sans accord. L. 1236-9 conserve la priorité de réembauche si l’accord la prévoit, y compris pour les futurs salariés éligibles. L. 2253-1, 8°, ne doit pas rétablir le préalable ou le filtre d’usage ; les garanties de branche gardent leur portée. Le renvoi ajouté à L. 1234-3 vise le décompte de sa proposition, intégralement fournie et requise dans reference-targets.json. L’ordonnance du 22 septembre 2017 conserve son champ historique pour les contrats antérieurs. Les obligations collectives européennes et la convention OIT n° 158 restent distinctes et à coordonner ; aucune autorisation spéciale n’est supprimée implicitement.',
       ['Convention ou accord collectif de branche étendu comme condition préalable de recours à l’affectation sur chantier ou opération.',
        'Restriction du recours sans accord aux secteurs où l’usage était habituel et conforme à l’exercice régulier de la profession au 1er janvier 2017.'])

out['L1223-9']['proposed_xml'] = out['L1223-9']['proposed_xml'].replace(
    'fractions d’année au prorata,', 'fractions d’année au prorata des mois complets,')
revise('L1223-9',
       'Les coupes déjà opérées sont maintenues : suppression des rubriques obligatoires de taille d’entreprise et d’activités, de la mesure d’information spécialisée en doublon des écrits ordinaires et de la négociation obligatoire de modalités de rupture pour l’impossibilité ou la fin anticipée du chantier. Le contrat unique et ses garanties de rupture s’appliquent directement. La présente passe corrige les fractions d’année en mois complets. Les contreparties de rémunération et d’indemnité, la formation et les modalités plus favorables restent applicables aux futures affectations ; leur suppression retirerait des avantages. La détermination par contrat en l’absence d’accord est une obligation de mise en œuvre pour ce champ nouvellement ouvert : elle est recensée avec les suppressions, sans affirmer un solde net chiffré.',
       'Les six subdivisions sont conservées. L’information du 3° est intégrée aux documents existants de L. 1221-5-1, sans nouveau formulaire. Le 4° renvoie au barème ordinaire de L. 1234-9 : employeur seul, seuil d’un an en fin effective préavis inclus, 0,20 mois sur toute l’ancienneté dès le seuil atteint, fractions selon les mois complets, plafond légal de six mois. Les anciennes notes du brouillon demandaient à tort d’écarter les mois complets de L. 1234-9 et R. 1234-1 : cette demande est retirée. L’exception de faute grave de L. 1234-9 reste à son champ ; les garanties conventionnelles, indemnités spéciales et dommages d’illégalité ne sont pas absorbés. L. 1236-8 et L. 1236-9 ont été lus : fin réelle et recours, aucune rupture automatique à l’abandon, priorité de réembauche conventionnelle maintenue. L. 2253-1, 8°, doit préserver les garanties sans reconstituer un filtre d’accès. Le champ historique de l’ordonnance de 2017 et les composantes anciennes d’indemnité restent protégés. Les nouvelles modalités de préavis n’abrègent ni consultation collective ni autorisation spéciale. Les textes hors lot sont signalés et non modifiés dans le présent fichier.',
       ['Rubriques obligatoires fixant la taille des entreprises et les activités admises au régime de chantier ou d’opération.',
        'Mesures particulières d’information sur la nature du contrat en doublon de l’information écrite ordinaire déjà remise au salarié.',
        'Obligation de négocier des modalités particulières de rupture pour chantier irréalisable ou terminé de façon anticipée, sans retirer les garanties plus favorables.'])

revise('L1225-6',
       'Abrogation prospective de coordination conservée : l’exception permettant l’échéance d’un CDD malgré les protections visées n’a plus de champ pour les nouvelles relations soumises au contrat unique. Cet article ne créait pas un cas de recours au CDD : son abrogation n’est donc pas comptée comme une seconde suppression de ce régime. La règle reste opératoire jusqu’au terme valablement défini des anciens CDD, avec leurs droits et recours ; aucune rupture anticipée discriminatoire n’est autorisée. Les protections et les deux notes temporelles de la source sont conservées dans leur champ. Aucune autre charge autonome n’existe ici à retirer.',
       'L. 1225-4, L. 1225-4-3, L. 1225-4-5 et L. 1225-5 ont été lus en entier. L’absence de L. 1225-4-2 et L. 1225-4-4 dans la liste est préexistante ; aucun ajout par analogie n’est opéré. Les notes distinguent l’entrée en vigueur immédiate de la rédaction issue de la loi n° 2025-1403 et le champ des enfants nés ou adoptés à compter du 1er janvier 2026 ou nés avant avec naissance attendue après. Cette date n’est pas celle de la réforme proposée. L’article 99 de cette loi, extérieur au corpus fourni, reste à confronter en entier pour sa portée exacte ; aucune restriction supplémentaire n’est déduite de la seule note. La transition couvre aussi les anciens termes imprécis fixés par un événement, sans renouvellement décidé après la réforme. Coordonner L. 1221-2, le titre IV et L. 1225-38 ; ne pas traiter une formation, une mission ou un congé comme un terme d’emploi. Les protections de maternité, de santé, de naissance et leurs réparations restent distinctes du préavis et du seuil d’indemnité ordinaire.')
out['L1225-6'].update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope='Suppression pour les nouvelles relations de l’exception d’échéance du CDD aux protections de maternité, d’interruption de grossesse et de naissance visées ; maintien transitoire pour les seuls termes des CDD valablement conclus avant la réforme.')

revise('L1225-34',
       'La suppression de fond du brouillon est conservée : la salariée enceinte n’a plus à faire constater médicalement sa grossesse pour exercer cette seule liberté de départ sans préavis ni indemnité à sa charge. La grossesse réelle demeure la condition du droit et peut être prouvée librement ; aucun certificat, formulaire ou déclaration ne remplace le constat. La dispense spéciale prime aussi le préavis de quinze jours du futur contrat unique. La seconde passe ne retire pas la condition de grossesse, qui définit le champ de cette protection, ni les preuves médicales ayant un autre objet de santé ou de prestation.',
       'L. 1142-3, 4°, R. 1225-1 et R. 1225-3 ont été lus : coordonner la mention de grossesse médicalement constatée et empêcher le rétablissement du certificat ou d’un mode imposé de transmission pour la seule dispense de L. 1225-34. Leurs autres objets de protection et de preuve demeurent distincts. L. 1237-1 doit préserver expressément cette dispense dans le contrat unique. L’indemnité écartée est celle que la salariée devrait à l’employeur ; cette démission n’ouvre pas en elle-même l’indemnité ordinaire de L. 1234-9 et ne supprime ni salaires, congés acquis ni réparations d’une illégalité. La nouvelle preuve libre vaut pour les ruptures notifiées après l’entrée en vigueur, y compris sous un contrat ancien ; aucune réouverture ou restitution générale des ruptures antérieures n’est décidée.',
       ['Constat médical obligatoire de la grossesse comme condition spécifique de la rupture à l’initiative de la salariée sans préavis ni indemnité à sa charge.'])

revise('L1225-38',
       'Coordination de fond conservée : l’exception d’échéance est réservée aux CDD valablement conclus avant la réforme ; elle ne peut servir à un nouveau contrat ni à un renouvellement ultérieur. La suppression du régime nouveau de CDD se situe à L. 1221-2 et au titre IV, sans double comptage ici. La suspension de l’emploi pendant le congé et l’application des protections aux parents adoptants restent intégrales et ouvertes aux futures adoptions éligibles. Elles ont une fonction essentielle et ne constituent pas des formalités redondantes à supprimer. Aucun document ni délai nouveau n’est ajouté.',
       'L. 1225-4 et L. 1225-5, puis L. 1225-39, ont été lus : les exceptions et modalités d’annulation restent à leur champ, avec les adaptations propres à l’adoption. Le préavis de quinze jours ne permet ni notification ni prise d’effet d’une rupture pendant une période légalement protégée. L. 1225-6 conserve l’échéance transitoire des anciens CDD, y compris un événement valablement défini avant réforme, sans nouveau renouvellement. L. 1225-70, L. 1225-71, L. 1225-72 et R. 1227-5, lus, continuent d’assurer nullité, réparation et sanctions des protections maintenues ; leurs renvois ne doivent ni ressusciter les nouveaux CDD ni désarmer les droits des parents. Les règles européennes de congés familiaux et l’article 16 de la directive 2006/54/CE restent à articuler dans leur champ sans conformité globale présumée. Les deux alinéas matériels gardent leur place ; les droits des contrats anciens et des futures adoptions sont préservés.',
       ['Application pour l’avenir de l’exception d’échéance du CDD pendant le congé d’adoption, réservée désormais aux seuls contrats antérieurs valablement conclus.'])


def impact(n, classification, assessment, limitations, burdens):
    out[n]['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=[])


def effect(n, kind, measure, description, before, after, unit, population, transition, burdens, sq, pq):
    out[n]['substantive_impact']['effects'].append(dict(
        kind=kind, measure_id=measure, description=description, before=before, after=after,
        unit=unit, affected_population=population, conditions_and_transition=transition,
        replacement_or_new_burdens=burdens, source_quote=sq, proposed_quote=pq))


impact('L1221-1', 'retained_necessary',
       'La source entière reste applicable : droit commun et liberté de forme. Aucune réduction réelle n’est revendiquée ; le brouillon stylistique n’apportait aucune coupe.',
       'Cet article ne détermine ni la durée de l’emploi ni les écrits spéciaux. Le maintien ne valide pas la coordination des autres articles du code.',
       'Aucune charge nouvelle identifiée : la source est maintenue intégralement et n’exige ni écrit général, dépôt, registre ou autorisation. Aucun solde de l’ensemble des codes n’est chiffré.')
impact('L1221-5-1', 'material_reduction',
       'Par rapport à la source officielle entière, le salarié peut obtenir les informations du juge sans mise en demeure préalable. L’information écrite et ses dispenses restent ; le réemploi d’écrits n’est pas compté comme une seconde réduction.',
       'La suppression du délai réglementaire de sept jours dépend de la coordination de R. 1221-41. Les délais utiles de remise, les règles européennes et le champ historique de la loi de 2023 ne sont pas supprimés.',
       'Aucune charge nouvelle identifiée : aucun écrit supplémentaire, registre ou procédure de remplacement ; le juge peut être saisi directement. Le coût contentieux éventuel et le solde de tous les codes ne sont pas chiffrés.')
effect('L1221-5-1', 'obligation_removed', 'information-emploi-recours-direct',
       'Retrait du préalable de mise en demeure pour obtenir judiciairement les informations d’emploi.',
       'Le salarié doit mettre l’employeur en demeure avant saisine ; R. 1221-41 prévoit ensuite sept jours calendaires sans réponse.',
       'Saisine directe, sans mise en demeure ni attente liée à ce préalable ; délais ordinaires de remise maintenus.',
       'legal_duty', 'Salariés privés qui demandent la communication ou le complément des informations obligatoires.',
       'Actions introduites après entrée en vigueur et instances en cours ; décisions définitives préservées, champ historique de l’information réservé.',
       'Aucun préalable de remplacement ; coordination réglementaire de R. 1221-41 nécessaire.',
       "Un salarié qui n'a pas reçu les informations mentionnées au premier alinéa ne peut saisir le juge compétent afin de les obtenir qu'après avoir mis en demeure son employeur de lui communiquer les documents requis ou, le cas échéant, de compléter les documents remis.",
       'Le salarié peut saisir directement le juge compétent pour obtenir les informations manquantes ou le complément des informations incomplètes, sans mise en demeure préalable ni délai d’attente lié à une telle mise en demeure.')

impact('L1222-15', 'material_reduction',
       'La source laisse la durée du préavis au seul avenant. Pour le contrat unique, sa durée est plafonnée à quinze jours calendaires et aucun délai d’information plus précoce ne s’ajoute ; les dispenses et durées plus courtes demeurent.',
       'La réduction concerne les avenants dont le préavis excède quinze jours ou impose une information plus précoce. Les contrats anciens, la mobilité et le droit de retour restent à leur champ ; aucune économie chiffrée n’est établie.',
       'Aucune charge nouvelle identifiée : la notification écrite reprend celle déjà prévue par l’avenant de L. 1222-13 ; sa réception peut se prouver par tout moyen, sans formulaire ni registre supplémentaire. Aucun solde global n’est établi.')
effect('L1222-15', 'deadline_reduced', 'preavis-contrat-unique',
       'Plafonnement du délai de non-retour et suppression de son cumul avec une information plus précoce.',
       'Préavis du seul avenant, sans plafond légal chiffré dans cet article ; délai d’information fixé dans L. 1222-13.',
       'Au maximum quinze jours calendaires à partir du lendemain de la réception de la notification écrite ; zéro ou moins si l’avenant le prévoit.',
       'calendar_days', 'Salariés en mobilité qui choisissent de ne pas revenir sous un nouveau contrat unique ou après conversion convenue.',
       'Nouveaux contrats à compter de l’entrée en vigueur ; anciens contrats et avenants maintenus sauf conversion préservant ancienneté et créances.',
       'Pas de nouveau support ; la notification écrite préexistante sert au décompte et aucun délai d’information ne s’ajoute.',
       "Cette rupture constitue une démission qui n'est soumise à aucun préavis autre que celui prévu par l'avenant mentionné à l'article L. 1222-13.",
       'Pour le contrat de travail unique conclu à compter de l’entrée en vigueur de la loi instituant ce contrat, le préavis prévu par cet avenant ne peut excéder quinze jours calendaires.')

impact('L1223-5', 'material_reduction',
       'La source subordonne le régime d’exportation à un accord collectif. Ce préalable est supprimé pour les nouveaux contrats, avec garanties maintenues. La dérogation économique existait déjà et n’est pas comptée comme une nouvelle procédure supprimée.',
       'Le champ reste la mission accomplie en majeure partie à l’étranger. Les protections collectives supérieures ne sont pas effacées ; la mise en œuvre des garanties sans accord est recensée à L. 1223-6, sans double compte.',
       'Aucun agrément, dépôt ou déclaration de remplacement n’est identifié dans cet article. L’information sur la mission utilise les écrits existants ; les garanties directement exigibles sans accord sont explicitées et recensées à L. 1223-6. Solde net non chiffré.')
effect('L1223-5', 'obligation_removed', 'mission-export-acces-sans-accord',
       'Suppression de l’accord collectif comme préalable au recours au régime de mission à l’exportation.',
       'Accord collectif de branche ou d’entreprise déterminant les contrats éligibles au régime dérogatoire.',
       'Mission possible sans accord préalable ; garanties des L. 1223-6 et L. 1223-7 et procédure de L. 1236-7 conservées.',
       'legal_duty', 'Employeurs et salariés des nouvelles missions à l’exportation accomplies majoritairement hors du territoire national.',
       'Suppression du préalable pour les contrats nouveaux ; conditions et garanties des contrats antérieurs préservées.',
       'Aucune autorisation ni déclaration équivalente ; détermination des garanties en l’absence d’accord traitée à L. 1223-6.',
       "Un accord collectif de branche ou d'entreprise détermine les contrats de travail conclus pour la réalisation d'une mission à l'exportation accomplie en majeure partie hors du territoire national, dont la rupture à l'initiative de l'employeur à la fin de la mission n'est pas soumise aux dispositions relatives au licenciement économique.",
       'Une mission à l’exportation accomplie en majeure partie hors du territoire national peut être confiée à un salarié sans accord collectif préalable de branche ou d’entreprise.')

impact('L1223-6', 'mixed',
       'Retrait effectif des filtres de catégories, de durée minimale de mission et de taille/type d’entreprise. Les avantages matériels restent, avec maintien autonome du plancher indemnitaire spécial officiel. Leur détermination contractuelle sans accord collectif est une obligation de mise en œuvre dans le champ nouvellement ouvert.',
       'Le minimum spécial ne devient pas l’indemnité ordinaire à 0,20 mois : les taux de référence officiels un quart puis un tiers sont conservés, sans seuil ni plafond ordinaire. L’effet des garanties à fixer sans accord ne permet pas de chiffrer un solde net de charges.',
       'Une détermination contractuelle des contreparties et garanties est exigée à défaut d’accord pour les missions nouvellement accessibles ; elle remplace leur détermination collective, sans document distinct ni registre. Aucun prélèvement, agrément ou donnée supplémentaire n’est créé. Le solde net des codes reste non établi.')
effect('L1223-6', 'obligation_removed', 'mission-export-filtres-conventionnels',
       'Retrait des rubriques imposant des catégories préalables de salariés et la taille et le type des entreprises.',
       'L’accord désigne les catégories de salariés ; un accord de branche fixe aussi la taille et le type des entreprises.',
       'Aucune désignation collective préalable des catégories ni mention obligatoire de taille et de type d’entreprise.',
       'legal_duty', 'Employeurs, salariés et négociateurs des futures missions à l’exportation.',
       'Nouveaux contrats après entrée en vigueur ; garanties des contrats antérieurs et stipulations plus favorables maintenues.',
       'Aucune liste, déclaration ou autorisation de remplacement ; garanties matérielles toujours applicables.',
       "S'il s'agit d'un accord collectif de branche, il fixe également la taille et le type d'entreprises concernées.",
       'Un accord de branche n’est pas tenu de fixer la taille et le type des entreprises concernées.')
effect('L1223-6', 'deadline_reduced', 'mission-export-duree-minimale',
       'Suppression du minimum légal de durée de la mission à l’exportation.',
       'La durée minimale de la mission fixée par accord ne peut être inférieure à six mois ; ce n’est pas un préavis.',
       'Aucune durée minimale légale de mission ni mention distincte d’un minimum ; emploi indéterminé maintenu.',
       'other', 'Salariés et employeurs des nouvelles missions à l’exportation, même plus courtes que six mois.',
       'Contrats nouveaux à compter de l’entrée en vigueur ; anciennes conditions convenues conservées.',
       'Aucune durée minimale de remplacement et aucun terme d’emploi créé par la durée de mission.',
       "2° La nature des missions à l'exportation concernées ainsi que leur durée minimale, qui ne peut pas être inférieure à six mois ;",
       'Aucune durée minimale légale de mission ni mention distincte d’une telle durée minimale n’est exigée.')
effect('L1223-6', 'relief_preserved', 'mission-export-minimum-special',
       'Conservation du plancher indemnitaire spécial sans seuil ni condition d’effectif, distinct de l’indemnité ordinaire réformée.',
       'Indemnité au moins égale à l’indemnité légale proportionnelle sans condition d’ancienneté ni d’effectif ; référence officielle un quart de mois jusqu’à dix ans, un tiers au-delà.',
       'Même plancher spécial autonome : un quart puis un tiers de mois de salaire de référence par année, mois complets, sans seuil d’un an ni plafond ordinaire de six mois.',
       'other', 'Salariés en mission à l’exportation remplissant les conditions du régime, y compris les futurs salariés et les anciens contrats.',
       'Garantie maintenue pour les missions futures et les contrats anciens ; ancienneté totale en fin effective préavis inclus, pas de double indemnisation des mêmes services.',
       'Aucune pièce supplémentaire ; calcul spécial conservé au lieu d’importer le barème ordinaire réduit.',
       "3° Les contreparties en termes de rémunération et d'indemnité de licenciement accordées aux salariés, sans que cette indemnité puisse être inférieure au montant de l'indemnité légale de licenciement attribué à due proportion du temps sans condition d'ancienneté et quel que soit l'effectif de l'entreprise ;",
       'Ni la condition d’un an ni le plafond de six mois de l’indemnité ordinaire ne s’appliquent à ce minimum spécial.')
effect('L1223-6', 'obligation_added', 'mission-export-garanties-sans-accord',
       'Détermination contractuelle des garanties dans le champ désormais ouvert sans accord collectif.',
       'L’accord collectif de mission fixe notamment les contreparties et garanties ; le régime n’est pas ouvert sans ce préalable.',
       'À défaut d’accord, le contrat précise les garanties de mission, y compris rémunération et formation, dans les supports existants.',
       'legal_duty', 'Employeurs recourant désormais à une mission à l’exportation sans accord spécial applicable.',
       'Contrats nouveaux après entrée en vigueur ; pas de redépôt pour les contrats antérieurs.',
       'Détermination contractuelle à la place de la détermination collective ; aucun document distinct ni nouvelle attestation.',
       "L'accord collectif de branche ou d'entreprise prévoyant la mise en place du contrat de mission à l'exportation fixe notamment :",
       'Elles sont précisées par l’accord collectif applicable ou, à défaut, par le contrat de travail, sans que la conclusion d’un accord collectif soit un préalable à l’embauche :')

impact('L1223-7', 'coordination_only',
       'La protection sociale de branche ou d’entreprise est conservée et explicitement applicable dans le contrat unique sans accord spécial de mission. Aucune taxe ni formalité distincte n’est supprimée par rapport à la source entière.',
       'La garantie ne détermine pas la territorialité de l’affiliation, les cotisations ou les formalités de détachement. Ces régimes et contraintes internationales ne sont pas évalués ou réécrits ici.',
       'Aucune charge nouvelle identifiée : aucune pièce, registre, déclaration, délai ni cotisation autonome ; la garantie existante suit l’affectation même sans accord spécial. Aucun solde national de charges n’est chiffré.')
effect('L1223-7', 'coordination', 'mission-export-acces-sans-accord',
       'Maintien de la protection sociale de branche ou d’entreprise lorsque le préalable collectif est supprimé.',
       'Protection sociale de branche ou d’entreprise applicable au bénéficiaire du contrat de mission à l’exportation.',
       'Même protection pour le salarié affecté à la mission, y compris sous contrat unique sans accord spécial.',
       'regime', 'Salariés en mission à l’exportation dans le champ du régime de protection sociale applicable.',
       'Contrats antérieurs et futures missions ; aucune affiliation française universelle déduite du texte.',
       'Pas de nouvelle cotisation ou pièce ; simple coordination de la garantie existante.',
       "Les dispositions en matière de protection sociale de la branche ou de l'entreprise sont applicables au bénéficiaire du contrat de mission à l'exportation.",
       'Le salarié affecté à une mission à l’exportation bénéficie des dispositions de protection sociale applicables dans sa branche ou son entreprise, y compris lorsque son emploi relève du contrat de travail unique et qu’aucun accord collectif spécial de mission n’a été conclu.')

impact('L1223-8', 'material_reduction',
       'Par rapport à la source entière, retrait du préalable d’accord étendu et du filtre d’usage sectoriel de 2017. La source prévoyait déjà un CDI : l’affectation au contrat unique ne représente pas ici la suppression d’un ancien CDD.',
       'Les anciens contrats conservent leur champ de recours et leurs garanties. L. 1236-8, L. 1236-9 et L. 2253-1 doivent être coordonnés sans fermer les priorités ni prétendre toutes les procédures terminées en quinze jours.',
       'Aucun agrément, registre ou déclaration de remplacement ; les informations d’affectation utilisent les écrits existants. La détermination contractuelle des garanties sans accord est recensée à L. 1223-9. Le coût net de cette ouverture n’est pas chiffré.')
effect('L1223-8', 'obligation_removed', 'chantier-acces-sans-accord',
       'Retrait des préalables alternatifs d’accord étendu ou d’usage sectoriel antérieur au recours au régime de chantier.',
       'Accord collectif de branche étendu ou, à défaut, usage habituel et régulier dans le secteur au 1er janvier 2017.',
       'Affectation possible sans accord préalable et sans filtre d’usage sectoriel antérieur, sous garanties maintenues.',
       'legal_duty', 'Employeurs et salariés des nouvelles affectations sur chantier ou opération.',
       'Nouveaux contrats après entrée en vigueur ; anciens contrats selon leur régime, dont champ historique de l’ordonnance de 2017.',
       'Aucun contrat de forme spéciale, agrément ou déclaration de remplacement ; garanties précisées à L. 1223-9.',
       "A défaut d'un tel accord, ce contrat peut être conclu dans les secteurs où son usage est habituel et conforme à l'exercice régulier de la profession qui y recourt au 1er janvier 2017.",
       'En l’absence d’une telle convention ou d’un tel accord, un salarié peut également être recruté pour être affecté à un chantier ou à une opération, sans condition d’usage sectoriel antérieur.')

impact('L1223-9', 'mixed',
       'Les rubriques de taille et d’activités, le circuit d’information spécialisé et la négociation obligatoire de modalités de fin anticipée disparaissent. Les garanties matérielles demeurent et doivent être précisées par contrat à défaut d’accord : cette obligation accompagne l’ouverture et empêche d’affirmer un solde net démontré.',
       'Le barème ordinaire est coordonné par renvoi à L. 1234-9, sans deuxième réduction comptée. Les anciens droits, indemnités spéciales et garanties plus favorables demeurent. Les modalités des autres articles de rupture restent à coordonner.',
       'Détermination contractuelle des contreparties et garanties de formation dans le champ nouvellement accessible sans accord, avec réemploi des stipulations déjà remises ; aucun registre ni formulaire nouveau. Les coupes coexistent avec cette mise en œuvre ; le solde net n’est pas établi.')
effect('L1223-9', 'coordination', 'chantier-acces-sans-accord',
       'Suppression des rubriques de taille et d’activités en exécution de l’ouverture sans accord préalable.',
       'L’accord de L. 1223-8 fixe la taille des entreprises et les activités concernées.',
       'Ces mentions ne sont plus obligatoires ; l’accès ne dépend plus de ces filtres collectifs.',
       'legal_duty', 'Employeurs, salariés et négociateurs du régime de chantier ou opération.',
       'Contrats nouveaux après réforme ; garanties et champ des anciens contrats préservés.',
       'Aucune liste ou déclaration de remplacement ; coordination de la même mesure portée par L. 1223-8.',
       '1° La taille des entreprises concernées ;',
       '1° Aucune mention obligatoire de la taille des entreprises concernées n’est exigée ;')
effect('L1223-9', 'obligation_merged', 'chantier-information-emploi',
       'Intégration de l’information spécialisée sur le contrat aux documents ordinaires déjà remis.',
       'L’accord fixe des mesures propres d’information sur la nature du contrat, en plus du régime général d’information.',
       'Information dans les documents de L. 1221-5-1 ; aucune mesure particulière ni document supplémentaire à cette seule fin.',
       'legal_duty', 'Employeurs et salariés des nouvelles affectations de chantier ou opération.',
       'Contrats nouveaux après entrée en vigueur ; droits d’information et anciens contrats conservés.',
       'Information maintenue sur supports existants, pas de formulaire supplémentaire.',
       "3° Les mesures d'information du salarié sur la nature de son contrat ;",
       'Aucune mesure particulière d’information ni document supplémentaire n’est imposé à cette seule fin ;')
effect('L1223-9', 'obligation_removed', 'chantier-rupture-sans-modalites-doublees',
       'Suppression de la négociation obligatoire de modalités spécifiques de rupture pour chantier irréalisable ou terminé plus tôt.',
       'L’accord doit fixer des modalités adaptées de rupture en cas d’impossibilité du chantier ou de fin anticipée.',
       'Application directe des règles légales et garanties plus favorables, sans négociation ni répétition contractuelle imposées.',
       'legal_duty', 'Employeurs et négociateurs du régime de chantier ou opération pour les nouvelles affectations.',
       'Réforme applicable aux contrats nouveaux ; clauses plus favorables et garanties anciennes maintenues.',
       'Aucune rupture automatique ni nouvelle autorisation ; procédures légales distinctes conservées.',
       "6° Les modalités adaptées de rupture de ce contrat dans l'hypothèse où le chantier ou l'opération pour lequel ce contrat a été conclu ne peut pas se réaliser ou se termine de manière anticipée.",
       'Aucune négociation de modalités particulières de rupture ni leur répétition dans le contrat n’est exigée ;')
effect('L1223-9', 'obligation_added', 'chantier-garanties-sans-accord',
       'Détermination contractuelle des garanties matérielles dans le champ nouvellement ouvert sans accord collectif.',
       'L’accord fixe les contreparties de rémunération et d’indemnité et les garanties de formation.',
       'À défaut d’accord, le contrat détermine ces contreparties et garanties, avec possibilité de renvoi aux écrits remis.',
       'legal_duty', 'Employeurs d’affectations de chantier ou opération désormais accessibles sans accord applicable.',
       'Contrats nouveaux après réforme ; garanties plus favorables conservées pour les futurs bénéficiaires et les anciens contrats.',
       'Détermination contractuelle à défaut de collective, sans document distinct ni répétition obligatoire des stipulations.',
       '4° Les contreparties en termes de rémunération et d’indemnité de licenciement accordées aux salariés ;'.replace('’', "'"),
       'Les salariés bénéficient de contreparties en matière de rémunération et d’indemnité de licenciement, fixées par la convention ou l’accord collectif ou, à défaut, par le contrat.')
effect('L1223-9', 'coordination', 'indemnite-ordinaire-contrat-unique',
       'Coordination du seul barème ordinaire, sans retirer les contreparties et indemnités plus favorables.',
       'Contreparties conventionnelles ; droit commun lu à L. 1234-9 et R. 1234-2 : seuil de huit mois, un quart puis un tiers de mois par année sans plafond légal de six mois.',
       'Pour le contrat unique nouveau : employeur seul, zéro avant un an en fin effective préavis inclus ; ensuite 0,20 mois de salaire de référence par année totale, mois complets au prorata, plafond légal six mois.',
       'other', 'Salariés des nouveaux contrats uniques affectés à un chantier, pour la seule indemnité ordinaire.',
       'Anciennes composantes et droits spéciaux préservés ; première année non retranchée une fois le seuil atteint ; pas de plafond imposé aux garanties plus favorables.',
       'Calcul coordonné au barème principal de L. 1234-9 ; coexistence de composantes transitoires sans double compte, aucune baisse nationale de prélèvement revendiquée.',
       "4° Les contreparties en termes de rémunération et d'indemnité de licenciement accordées aux salariés ;",
       'Lorsque ce seuil est atteint, le montant est calculé à raison de 0,20 mois de salaire brut de référence par année totale d’ancienneté, fractions d’année au prorata des mois complets, dans la limite de six mois de ce salaire, sans soustraire la première année.')

impact('L1225-1', 'retained_necessary',
       'Maintien intégral de la source : non-discrimination dans l’embauche, l’essai et la mutation, interdiction d’enquête sur la grossesse, exceptions de santé. Aucune réduction réelle n’est attribuée à ce maintien.',
       'Le maintien ne modifie ni les modalités médicales des affectations temporaires ni les règles de preuve et l’extension aux projets parentaux définies dans les articles distincts lus.',
       'Aucune charge nouvelle identifiée : le texte source est conservé sans document, registre, délai ou contrôle supplémentaire. Ses interdictions patronales protègent des droits essentiels ; aucun solde global de complexité n’est chiffré.')

impact('L1225-6', 'coordination_only',
       'L’exception d’échéance du CDD est abrogée pour les nouvelles relations, en coordination de la suppression des nouveaux CDD. Elle survit aux seuls anciens termes valables ; cet article n’ouvrait pas lui-même un cas de recours et ne démontre donc pas une seconde suppression de régime.',
       'Les CDD anciens, même à terme imprécis, restent concernés jusqu’au terme antérieurement défini ; protections et recours restent applicables. La portée externe de l’article 99 de la loi de 2025 reste à confronter au-delà des notes jointes.',
       'Aucune charge nouvelle identifiée : pas de conversion forcée, de déclaration ou pièce de remplacement ; seule l’application future de l’exception est fermée avec les nouveaux CDD. Aucun gain national ou solde de tous les codes n’est chiffré.')
effect('L1225-6', 'coordination', 'suppression-nouveaux-cdd',
       'Retrait prospectif de l’exception de terme aux protections visées, sans modifier les anciens termes valables.',
       'Les protections des quatre articles visés ne font pas obstacle à l’échéance d’un CDD, sans distinction selon sa date de conclusion.',
       'Article abrogé pour l’avenir ; maintien exprès uniquement pour les CDD valablement conclus avant réforme et leurs termes prévus.',
       'regime', 'Salariés bénéficiant des protections visées et titulaires d’un ancien CDD ; nouvelles relations soumises au contrat unique.',
       'Ancien terme fixé par date ou événement avant réforme conservé ; aucun renouvellement décidé après réforme, ni rupture anticipée discriminatoire.',
       'Aucune déclaration ou taxe de remplacement ; coordination de la suppression portée par L. 1221-2 et le titre IV.',
       "Les dispositions des articles L. 1225-4, L. 1225-4-3, L. 1225-4-5 et L. 1225-5 ne font pas obstacle à l'échéance du contrat de travail à durée déterminée.",
       'Le présent article est abrogé à compter de l’entrée en vigueur de la loi instituant le contrat de travail unique.')

impact('L1225-34', 'material_reduction',
       'La source exige une grossesse médicalement constatée pour partir sans préavis ni indemnité à la charge de la salariée. La proposition supprime ce constat imposé pour cette seule dispense et ouvre la preuve libre, tout en conservant la condition de grossesse réelle.',
       'Cette suppression ne dispense pas des preuves médicales utiles aux soins, aux prestations ou à d’autres protections. Les ruptures notifiées avant réforme conservent leur régime ; pas de restitution générale décidée.',
       'Aucune charge nouvelle identifiée : aucun certificat, formulaire ou déclaration ne remplace le constat supprimé. La possibilité de prouver la grossesse par tout moyen n’impose aucun nouveau support ; le solde de tous les codes n’est pas chiffré.')
effect('L1225-34', 'obligation_removed', 'grossesse-demission-sans-constat-impose',
       'Suppression du constat médical comme condition spécifique de la dispense de préavis et d’indemnité à la charge de la salariée.',
       'Grossesse médicalement constatée exigée pour bénéficier de cette liberté de départ sans préavis ni indemnité due par la salariée.',
       'Grossesse réelle prouvable par tout moyen ; aucun certificat médical exigible à cette seule fin, dispense conservée dans le contrat unique.',
       'legal_duty', 'Salariées enceintes qui rompent leur contrat, ancien ou nouveau, après entrée en vigueur.',
       'Ruptures notifiées après réforme, même pour contrats anciens ; ruptures antérieures sous leur droit, autres protections et preuves médicales distinctes.',
       'Aucune attestation ni déclaration équivalente ; coordonner R. 1225-1 et la mention de L. 1142-3, 4°.',
       "La salariée en état de grossesse médicalement constaté peut rompre son contrat de travail sans préavis et sans devoir d'indemnité de rupture.",
       'Sa grossesse peut être établie par tout moyen ; aucun certificat médical ne peut être exigé à cette seule fin.')

impact('L1225-38', 'coordination_only',
       'La suspension et les protections du congé d’adoption restent entières. L’exception de terme est réservée aux CDD antérieurs : coordination de la suppression des nouveaux CDD et non seconde réduction autonome.',
       'Les anciens CDD conservent leurs termes valables par date ou événement, sans renouvellement nouveau. Les modalités propres d’annulation de L. 1225-39 et les règles européennes de congés familiaux gardent leur champ.',
       'Aucune charge nouvelle identifiée : pas de document, registre ou délai supplémentaire ; les protections existantes suivent le contrat unique et l’exception devient transitoire. Aucun solde global de complexité ou de prélèvements n’est établi.')
effect('L1225-38', 'coordination', 'suppression-nouveaux-cdd',
       'Réserve de l’exception de terme aux seuls anciens CDD pendant le congé d’adoption.',
       'Les protections du congé d’adoption ne font pas obstacle au terme de tout CDD.',
       'Exception uniquement pour le terme antérieurement convenu d’un ancien CDD ; futur emploi indéterminé et protection maintenue.',
       'regime', 'Parents salariés prenant un congé d’adoption, titulaires d’un ancien CDD ou d’un nouveau contrat unique.',
       'Ancien terme valable par date ou événement conservé ; aucun renouvellement décidé après entrée en vigueur, droits des futures adoptions maintenus.',
       'Aucun document ou déclaration de remplacement ; coordination de la même suppression que L. 1225-6.',
       "L'application de ces articles ne fait pas obstacle à l'échéance du contrat de travail à durée déterminée.",
       'Pour les seuls contrats de travail à durée déterminée valablement conclus avant l’entrée en vigueur de la loi instituant le contrat de travail unique, cette protection ne fait pas obstacle à l’échéance, même postérieure, du terme prévu par le contrat antérieur, qu’il soit fixé par une date ou par un événement valablement déterminé avant cette entrée en vigueur, sans autoriser un renouvellement décidé après cette entrée en vigueur.')


# Analyses propres à chaque article et à chacune des trois cibles communes.
# Les empreintes désignent les vues fournies, pas une approbation de leur contenu.
common_checks = {
    'L1221-1': {
        'L1234-1': 'La liberté de forme ne fixe aucun préavis. La cible proposée substitue quinze jours au préavis de licenciement des contrats nouveaux et conserve l’ancien régime pour les contrats antérieurs ; elle ne permet pas de déduire de la source une rupture sans notification ou sans protections.',
        'L1221-2': 'La source de la cible autorise encore des termes dans le titre IV ; seule sa proposition les supprime pour les nouvelles relations. La liberté de forme maintenue ici ne constitue pas une exception à ce contrat unique et ne rétablit ni CDD nouveau ni renouvellement après réforme.',
        'L1234-9': 'L’article maintenu ne régit pas l’indemnité. La cible proposée mesure l’année à la fin effective préavis inclus, puis calcule 0,20 mois sur toute l’ancienneté en mois complets, plafond six mois ; l’ancien seuil de huit mois et la composante acquise restent distincts.'},
    'L1221-5-1': {
        'L1234-1': 'L’information écrite sur la cessation de la relation doit décrire le régime applicable : quinze jours pour le contrat unique dans la proposition, anciens préavis pour les contrats antérieurs. Supprimer la mise en demeure judiciaire ne supprime ni cette information ni la notification du licenciement.',
        'L1221-2': 'Les documents ne peuvent annoncer un terme d’emploi nouveau là où la proposition de L. 1221-2 impose l’indétermination. Une durée de mission ou de formation reste distincte. Les anciennes informations de terme concernent les CDD antérieurs ; les dispenses d’information restent applicables.',
        'L1234-9': 'Les informations de rupture doivent distinguer l’indemnité ordinaire proposée, employeur seul, seuil d’un an en fin effective avec préavis et 0,20 mois sur l’ancienneté totale en mois complets plafonnés à six mois, des anciens droits et des indemnités spéciales ; aucune nouvelle attestation n’est créée ici.'},
    'L1222-15': {
        'L1234-1': 'Cette cible porte sur la rupture patronale, non sur le choix de non-retour qui est une démission. Le plafonnement du préavis de l’avenant ici conserve zéro ou moins de quinze jours s’ils sont favorables ; son calcul commence au lendemain de la réception écrite et non au terme de la mobilité.',
        'L1221-2': 'La mobilité est une suspension du contrat d’origine, pas un terme de l’emploi. La proposition de la cible interdit tout nouveau CDD ; le non-retour reste un choix exprès de démission. La transition préserve les anciens avenants et l’ancienneté d’une conversion convenue.',
        'L1234-9': 'Le non-retour volontaire n’est pas une rupture à l’initiative de l’employeur : aucune indemnité ordinaire n’est ouverte par cet article, même après un an. Les salaires, congés et recours distincts demeurent ; le seuil en fin effective et le barème patronal ne sont pas transposés à la démission.'},
    'L1223-5': {
        'L1234-1': 'Pour les nouveaux emplois à l’exportation, le préavis individuel suit les quinze jours proposés, après notification patronale, sans faire disparaître procédure personnelle ou autorisation spéciale. La cible maintient les anciens préavis ; la fin de mission ne vaut jamais notification ni rupture automatique.',
        'L1221-2': 'La cible proposée impose l’emploi indéterminé aux nouvelles relations. La mission majoritairement à l’étranger peut être limitée sans limiter l’emploi ; le texte le dit expressément. L’ouverture sans accord n’autorise donc ni CDD de mission ni renouvellement nouveau d’un ancien CDD.',
        'L1234-9': 'Le seuil ordinaire d’un an et son plafond de six mois ne doivent pas neutraliser la garantie spéciale sans ancienneté de L. 1223-6. Le présent lot conserve de façon autonome son plancher spécial ; la cible proposée règle l’ordinaire et les composantes anciennes, sans double compte des mêmes services.'},
    'L1223-6': {
        'L1234-1': 'La durée de service pour le minimum spécial se mesure à la fin effective avec préavis ; la notification et les quinze jours individuels proposés ne remplacent pas la procédure de rupture. Les anciens contrats conservent leur préavis propre, sans créer de condition d’ancienneté à la garantie spéciale.',
        'L1221-2': 'La suppression des six mois minimaux concerne la mission et non l’emploi : celui-ci reste indéterminé pour les nouveaux contrats selon la proposition de la cible. Les anciens contrats et garanties subsistent ; aucune mission brève ne devient un nouveau CDD.',
        'L1234-9': 'La cible propose zéro indemnité ordinaire avant un an puis 0,20 mois par année totale en mois complets, plafond six mois. Ces paramètres ordinaires ne sont pas importés dans le plancher spécial de mission : son absence de seuil et ses taux officiels de référence sont conservés, aussi pour les futures missions.'},
    'L1223-7': {
        'L1234-1': 'Le maintien de la protection sociale de mission ne dépend ni de la notification du licenciement ni de la durée de son préavis. Les quinze jours proposés pour les nouveaux contrats et les anciens préavis restent à la cible ; ils ne constituent pas une dispense de couverture ou d’affiliation.',
        'L1221-2': 'La couverture doit suivre les futures missions affectées au contrat unique indéterminé, même sans accord spécial ; l’ancienne dénomination contractuelle ne peut fermer le droit. Les contrats antérieurs restent couverts selon leur champ ; aucune affiliation française universelle n’en résulte.',
        'L1234-9': 'Le seuil d’un an de l’indemnité ordinaire ne conditionne pas la protection sociale de branche ou d’entreprise. Celle-ci garde ses propres règles, indépendamment du barème 0,20 mois et du plafond de six mois ; aucun seuil de rupture n’est ajouté à la couverture.'},
    'L1223-8': {
        'L1234-1': 'La fin effective du chantier n’est ni une rupture automatique ni une dispense de notification. Le préavis individuel des nouveaux contrats suit les quinze jours proposés, avec procédures collectives et autorisations distinctes ; les anciens contrats gardent leur régime de préavis.',
        'L1221-2': 'La source de L. 1223-8 prévoyait déjà un CDI. La cible proposée généralise le contrat unique pour les relations nouvelles ; supprimer l’accord préalable et le filtre sectoriel ouvre l’affectation sans autoriser un terme d’emploi au chantier. Anciennes conditions de recours préservées.',
        'L1234-9': 'L’indemnité ordinaire de chantier suit le barème proposé : seuil d’un an à la fin effective préavis inclus, puis 0,20 mois sur toute l’ancienneté en mois complets et plafond six mois. Les contreparties conventionnelles et les composantes antérieures ne sont pas supprimées par ce renvoi.'},
    'L1223-9': {
        'L1234-1': 'Les modalités particulières de fin anticipée ne sont plus obligatoirement négociées, mais la rupture doit être notifiée et le préavis de quinze jours de la proposition n’écarte ni procédure collective ni autorisation spéciale. Les anciens contrats conservent leurs règles et garanties.',
        'L1221-2': 'Les six subdivisions sont coordonnées à une affectation dans l’emploi indéterminé : impossibilité ou fin anticipée du chantier ne termine pas le contrat. La proposition de la cible n’autorise aucun nouveau CDD ni renouvellement ; les anciens contrats restent dans leur transition.',
        'L1234-9': 'Le 4° respecte la cible proposée : employeur seul, seuil d’un an en fin effective préavis inclus, 0,20 mois par année totale sans retrancher la première, fractions en mois complets et plafond six mois. Les anciennes notes contraires aux mois complets sont corrigées ; garanties plus favorables et spéciales restent distinctes.'},
    'L1225-1': {
        'L1234-1': 'L’interdiction de discrimination pendant l’essai ou la mutation reste entière : le préavis de licenciement proposé ne permet pas de justifier une rupture par la grossesse. La cible traite la durée, non la licéité du motif ; notification et protections spéciales restent nécessaires.',
        'L1221-2': 'Le contrat unique proposé n’écarte aucune interdiction d’enquête sur la grossesse ou de discrimination à l’embauche et à l’essai. Le maintien de la source couvre aussi les nouvelles relations ; il n’autorise aucun régime de CDD par exception implicite.',
        'L1234-9': 'Le zéro ordinaire avant un an ne neutralise pas la réparation d’une discrimination ou d’une rupture illicite dès le premier jour. La cible proposée distingue ces droits de l’indemnité 0,20 mois plafonnée ; aucune condition d’ancienneté n’est ajoutée aux interdictions maintenues.'},
    'L1225-6': {
        'L1234-1': 'L’échéance transitoire d’un ancien CDD ne devient pas un licenciement soumis au préavis ordinaire de cette cible. Pour les emplois nouveaux indéterminés, les quinze jours proposés n’écartent pas les périodes protégées ni les interdictions de notification et de prise d’effet applicables.',
        'L1221-2': 'La source de la cible autorise encore des CDD ; sa proposition interdit les nouveaux termes et renouvellements. L’abrogation est coordonnée avec cette proposition et conserve les seuls anciens termes valables, par date ou événement, sans attribuer à L. 1225-6 un ancien pouvoir de créer des CDD.',
        'L1234-9': 'Le terme valable d’un ancien CDD n’entre pas par lui-même dans l’indemnité de licenciement du CDI visée par la cible. Pour le nouveau contrat unique, le zéro ordinaire avant un an ne supprime ni garanties de maternité ni dommages d’illégalité ; les droits de fin des anciens contrats restent distincts.'},
    'L1225-34': {
        'L1234-1': 'La cible vise le préavis patronal ; la démission de la salariée enceinte relève ici d’une dispense spéciale, conservée même avec les quinze jours du contrat unique. L’article n’exige pas de notification de licenciement et n’abolit pas le préavis que l’employeur devrait de son côté.',
        'L1221-2': 'La liberté de départ de la salariée enceinte reste ouverte pour les futures relations indéterminées imposées par la proposition de la cible. Elle n’introduit aucun terme d’emploi, aucun CDD spécial et aucune restriction des droits ou de l’ancienneté des contrats antérieurs.',
        'L1234-9': 'L’indemnité écartée ici est celle due par la salariée à l’employeur ; ce n’est pas l’indemnité patronale de la cible. Une démission ordinaire n’ouvre pas le barème 0,20 mois après un an ; congés, salaires et réparations d’illégalité restent hors de cette exclusion.'},
    'L1225-38': {
        'L1234-1': 'Pendant le congé d’adoption, le préavis individuel de quinze jours proposé ne lève pas l’interdiction d’une rupture ou notification protégée. L’ancien terme de CDD conservé est distinct du licenciement et de son préavis ; aucune procédure complète en quinze jours n’est promise.',
        'L1221-2': 'L’exception de terme du deuxième alinéa est limitée aux CDD antérieurs pour respecter la proposition de contrat unique. Ni la durée du congé ni celle d’une mission ne termine l’emploi nouveau ; aucun renouvellement décidé après réforme ne reconstitue un CDD.',
        'L1234-9': 'Les protections d’adoption ne sont pas conditionnées à l’année d’ancienneté de l’indemnité ordinaire. Le barème proposé, fin effective avec préavis puis 0,20 mois par année totale en mois complets plafonné à six mois, ne supprime pas salaires, congés ou réparations du licenciement illicite.'}
}

extra_checks = {
    ('L1223-5', 'L1234-3'): 'Le renvoi nouveau vise le deuxième alinéa proposé : quinze jours calendaires à partir du lendemain de la présentation de la lettre, ou de la réception si une autre forme est légalement admise. Le premier alinéa conserve le départ historique pour les anciens contrats. La fin de mission ne vaut pas notification ; le troisième alinéa sur le départ volontaire ne régit pas ce licenciement.',
    ('L1223-8', 'L1234-3'): 'Le renvoi nouveau reprend le deuxième alinéa proposé, soit le lendemain de la présentation ou de la réception légalement admise, jusqu’à la fin du quinzième jour même non travaillé. L’achèvement du chantier n’est ni une notification ni un terme automatique. Le premier alinéa historique et les anciens préavis sont réservés aux contrats antérieurs ; les procédures collectives restent distinctes.',
    ('L1223-5', 'L1223-6'): 'Le renvoi vise les cinq garanties de mission, dont le minimum sans ancienneté ni condition d’effectif, et non un terme d’emploi. La vue fournie importe encore 0,20 mois et six mois dans ce minimum spécial ; la présente réponse la rectifie pour préserver les taux officiels un quart puis un tiers sans plafond ordinaire, avec mois complets.',
    ('L1223-5', 'L1223-7'): 'Ce renvoi protège la couverture de branche ou d’entreprise pour les missions nouvelles sans accord spécial aussi bien que pour les anciennes. La vue proposée le dit explicitement ; elle ne règle pas la territorialité de l’affiliation et ne crée pas une affiliation française générale.',
    ('L1223-5', 'L1236-7'): 'La source renvoie au chapitre II du titre III, donc au licenciement pour motif personnel, non à la procédure économique. Sa proposition maintient motif, contrôle, garanties de mission et anciens droits ; la fin de mission ne remplace jamais une notification et les quinze jours ne valent pas autorisation spéciale.',
    ('L1223-6', 'L1223-5'): 'La mission doit rester accomplie en majeure partie hors du territoire national. L’ouverture sans accord de la vue proposée appelle des garanties directement opposables, sans terme automatique ; le minimum spécial sans ancienneté n’est pas une autorisation de rompre à la seule expiration d’une durée.',
    ('L1223-6', 'R1234-4'): 'Le renvoi vise le salaire de référence le plus favorable : douze mois ou tout le service plus court, ou tiers des trois derniers mois avec primes proportionnées. La proposition conserve ces fenêtres avant notification, distinctes de l’ancienneté mesurée en fin effective ; aucun seuil d’un an ne s’applique à cette base spéciale.',
    ('L1223-6', 'L1221-5-1'): 'La nature de la mission utilise les documents d’information existants, complets et à jour, sans second dépôt ni document contractuel spécial. La suppression proposée de la mise en demeure judiciaire ne supprime pas ces informations ou leurs dispenses, ni celles requises avant le départ à l’étranger.',
    ('L1223-8', 'L1223-9'): 'Les six rubriques de la vue proposée maintiennent les contreparties et la formation tout en retirant les filtres et circuits redondants. Le présent texte conserve ces garanties et corrige le prorata en mois complets ; la détermination contractuelle à défaut d’accord est recensée comme mise en œuvre nouvelle dans le champ ouvert.',
    ('L1223-8', 'L1221-5-1'): 'L’identification du chantier utilise l’information écrite sur l’emploi et l’affectation, pas un contrat de forme spéciale. Le réemploi d’écrits doit rester complet et à jour ; les dispenses légales sont conservées, sans faire d’une durée de chantier la date de fin d’un emploi nouveau.',
    ('L1223-9', 'L1223-8'): 'La vue proposée ouvre l’affectation sans accord étendu ni usage sectoriel ancien ; ce n’est pas la création d’un CDD, la source étant déjà un CDI. Les garanties des 4° et 5° restent applicables sans accord et les anciens contrats conservent leur régime, dont le champ historique de 2017.',
    ('L1223-9', 'L1221-5-1'): 'Le 3° fusionne l’information particulière avec les documents généraux sans supprimer son contenu. La vue proposée permet de réemployer les informations remises et de saisir directement le juge ; elle ne justifie ni formulaire nouveau ni perte d’une dispense, et les garanties contractuelles peuvent être précisées par renvoi.'
}

for a in answers:
    source_key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][source_key]:
        t = refs['targets'][target_key]
        number = t['number']
        assessment = common_checks[a['number']].get(number)
        if assessment is None:
            assessment = extra_checks[(a['number'], number)]
        checks.append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
    def handle_data(self, s):
        self.parts.append(s)


def plain(xml):
    parser = Plain()
    parser.feed(xml)
    return ''.join(parser.parts)


def verify():
    assert len(answers) == 12
    for s, a in zip(sources, answers):
        assert all(s[k] == a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number'))
        assert len(a['reason']) >= 40 and len(a['review_notes']) >= 40
        imp = a['substantive_impact']
        assert imp['version'] == 1
        for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(imp[k]) >= 40, (a['number'], k)
        if s['benefit_check_required']:
            assert len(a['benefit_review']) >= 100
        for e in imp['effects']:
            assert len(e['source_quote']) >= 12 and len(e['proposed_quote']) >= 12
            assert e['source_quote'] in plain(s['source_xml']), (a['number'], 'source_quote', e['source_quote'])
            assert e['proposed_quote'] in plain(a['proposed_xml']), (a['number'], 'proposed_quote', e['proposed_quote'])
        checks = a['reference_checks']
        key = a['code_id'] + '|' + a['source_id']
        assert [c['target_key'] for c in checks] == refs['requirements'][key]
        for c in checks:
            assert len(c['assessment']) >= 80
            assert c['view_sha256'] == refs['targets'][c['target_key']]['view_sha256']
        if a['status'] == 'retained_unchanged':
            assert a['proposed_xml'] is None
            assert imp['classification'] == 'retained_necessary' and not imp['effects']
        else:
            assert a['proposed_xml']
        if a.get('change_type') == 'full_repeal':
            assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
            assert len(a['repeal_scope']) >= 30
        if a.get('change_type') == 'normative_reduction':
            assert all(len(s) >= 30 for s in a['removed_provisions'])


verify()
with open('answer.json', 'w') as f:
    json.dump(answers, f, ensure_ascii=False, indent=2)
    f.write('\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(answers)}, ensure_ascii=False))
