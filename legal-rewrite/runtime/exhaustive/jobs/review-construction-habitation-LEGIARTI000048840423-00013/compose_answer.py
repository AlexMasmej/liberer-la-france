import html
import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())


def paragraphs(xml):
    return re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>', xml, re.S)


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml))


def identity(source):
    return {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


first, second = sources
p0 = paragraphs(first['previous_draft']['proposed_xml'])
old_b = next(p for p in p0 if p.startswith('b) Pour une société d\'économie mixte'))
old_c = next(p for p in p0 if p.startswith('c) Pour un organisme bénéficiant'))
p0[p0.index(old_b)] = 'b) Abrogé.'
p0[p0.index(old_c)] = 'c) Abrogé.'
transition0 = [
    "III. ― À compter de l'entrée en vigueur de la loi, aucune cession ne peut être imposée sur le fondement des b et c du 3° du I dans leur rédaction antérieure. Les décisions de nomination et les mandats des administrateurs désignés sur ces fondements cessent de produire effet, pour leur partie relative aux cessions qui n'ont pas été valablement conclues à cette date, même lorsque ces décisions sont devenues définitives.",
    "Les contrats de cession valablement conclus avant cette date, les transferts déjà réalisés, les créances nées et les obligations qui en découlent demeurent régis par les dispositions qui leur sont applicables. Les recours relatifs aux décisions et actes antérieurs ainsi que les restitutions et réparations qui peuvent en résulter sont préservés.",
    "La suppression de ces pouvoirs de cession ne modifie ni les baux et conventions en cours, ni les droits des locataires et occupants, ni les obligations attachées aux aides publiques et aux missions de service d'intérêt économique général. Elle ne fait pas obstacle aux cessions volontaires ni aux mesures fondées sur une disposition légale distincte. Les dispositions abrogées ne peuvent plus fonder une obligation de cession."
]
p0.extend(transition0)
xml0 = '\n'.join('<p>' + p + '</p>' for p in p0)

source0_paragraphs = paragraphs(first['source_xml'])
source0_b = next(p for p in source0_paragraphs if p.startswith("b) S'il s'agit d'une société d'économie mixte"))
source0_c = next(p for p in source0_paragraphs if p.startswith("c) S'il s'agit d'un organisme bénéficiant"))

a0 = identity(first)
a0.update({
    'proposed_xml': xml0,
    'reason': "Réforme de fond supplémentaire par rapport au brouillon : les b et c du 3° du I ne permettent plus de nommer un administrateur pour vendre de force les logements d'une SEM ou d'un organisme agréé de maîtrise d'ouvrage. Les autres instruments de rectification et de sanction subsistent : mise en demeure, sanctions pécuniaires, suspensions, révocations, retrait d'agrément, exclusions d'aides dans leur champ et remboursement des aides d'Etat. Le déplacement forcé de la propriété n'est donc plus un instrument additionnel de sanction ; les obligations conventionnelles et les droits des occupants continuent de peser sur leur titulaire. La suppression vise aussi les cessions non conclues résultant de décisions anciennes, sans défaire les contrats déjà valablement conclus. Ce choix est une réduction normative, distincte des concentrations forcées de L. 481-1-1 et L. 481-1-2 déjà supprimées dans le projet. Les autres dispositions du brouillon sont maintenues à droit constant, sans leur attribuer une réduction nouvelle. Le renvoi définitionnel au IV de L. 302-5 introduit dans le brouillon disparaît avec le pouvoir de cession du c ; il ne devient pas un renvoi aux quotas abrogés.",
    'review_notes': "Source et brouillon lus entièrement ; source_notes_xml vide ; aucune pièce source_companions ni aucun tableau. Vérification locale des sources de L. 342-2, L. 342-12 à L. 342-17, L. 411-2, L. 441-3, L. 441-11, L. 313-17-1, L. 313-19, L. 313-19-1, L. 313-19-2, L. 365-2, L. 831-1 et L. 302-5 : leurs champs autonomes ne sont pas supprimés. Les plafonds de deux millions d'euros, dix-huit mois de loyer et 1 % des participations de l'année civile précédente, l'imputation sur le fonds, les durées d'un an, deux ans, cinq ans et dix ans, les prolongations liées au procès pénal et l'exception des pouvoirs de l'assemblée demeurent. Les tirets du 3° a, les emplacements 6° et 8° déjà abrogés et le II de publicité sont conservés ; les lettres b et c du 3° restent en place comme abrogées. Les sanctions pécuniaires ne sont pas des impôts supprimés. Le contrôle de la fraude, les règles d'attribution, les plafonds de loyers, les restitutions d'aides et les garanties européennes de la décision 2012/21/UE mentionnée à L. 342-2 restent applicables ; leur effectivité n'est pas présentée comme auditée. L. 353-6, L. 481-1 et les deux articles de concentration ont été confrontés : ne pas confondre cette sanction patrimoniale avec les regroupements pour taille insuffisante, ni avec les protections du locataire lors d'une résiliation. La recherche dans le corpus CCH n'a trouvé cette formule de nomination pour cession qu'à L. 342-14 ; elle n'est pas un inventaire de tous les textes extérieurs et actes individuels. Mettre en cohérence les mandats et instructions d'exécution ; ne pas reconstituer ce pouvoir par règlement. Le retrait d'agrément demeure une sanction distincte : la suppression des cessions n'accorde pas un agrément implicite ni un droit de poursuivre une activité interdite. La disparition d'un outil patrimonial appelle une appréciation de l'efficacité des autres sanctions, sans obligation de remplacement proposée. Incohérences préexistantes signalées, sans correction hors lot : L. 342-15 et R. 313-23 visent encore des subdivisions 6° ou 8° abrogées ; leur réécriture autonome reste à faire. L. 313-29 et L. 423-12, lus, maintiennent leurs interdictions de dix ans et ne sont pas allégés ici. Le pouvoir de dissolution des HLM et l'administration provisoire de L. 422-8/8-1 restent distincts ; la suppression de leur suivi imposé déjà décidée n'est pas rétablie. Les textes initiaux SRU 149 et 162 fournis ont été lus intégralement : ils portent notamment sur l'ancien L. 422-7 et l'ancien L. 451-2-1, pas sur la totalité du catalogue actuel. La filiation exacte des cessions b/c n'est pas établie par ces seuls textes ; la coupe est fondée sur l'orientation actuelle, sans déclarer ces volets historiques ni les 209 articles achevés. Aucun chiffrage de recettes, de coût administratif ou d'efficacité n'est disponible dans ce lot.",
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Pouvoir de nommer, au b du 3° du I, un administrateur chargé de céder de force les logements locatifs et logements-foyers d'une société d'économie mixte, y compris le champ ultramarin défini par l'aide de l'Etat.",
        "Pouvoir de nommer, au c du 3° du I, un administrateur chargé de céder de force les logements locatifs sociaux d'un organisme agréé au titre de L. 365-2 ; fin des effets non contractualisés des anciennes décisions sur ce seul fondement."
    ],
    'benefit_review': "Le texte ne crée pas d'exonération fiscale propre. Ses plafonds et limites de sanction sont favorables aux personnes contrôlées : deux millions d'euros, dix-huit mois de loyer, limite de 1 %, durées maximales et contradictoire restent identiques. Les agréments et les aides auxquels ils donnent accès ne sont ni fermés pour l'avenir ni retirés par principe : le retrait pour manquement reste possible dans son champ antérieur. Les exemptions et aides des HLM, SEM et organismes Action Logement résultent des régimes autonomes lus, non d'un quota communal ; elles ne sont pas supprimées. Les droits conventionnels des locataires et les recours anciens sont expressément réservés.",
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à l'article officiel entier, deux pouvoirs de cession patrimoniale imposée comme sanction disparaissent au profit de la liberté de conserver les logements, sous les obligations et sanctions subsistantes. Il s'agit d'une réduction réelle du catalogue des sanctions, pas d'une suppression de taxe, d'une baisse des amendes ou d'une seconde abolition des concentrations de SEM. Le brouillon ne retirait pas ces pouvoirs.",
        'scope_limitations': "La réduction ne couvre que les cessions fondées sur les anciens b et c du 3° du I et non encore valablement conclues à l'entrée en vigueur. Les contrats conclus, droits des tiers, règles d'agrément, restitutions d'aides, dissolutions HLM, autres pouvoirs légaux autonomes et sanctions personnelles demeurent. L'efficacité comparée des sanctions et le solde net des coûts ne sont pas établis ; la filiation historique intégrale reste non démontrée.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée dans cette proposition : pas de déclaration, autorisation, registre, donnée, justificatif, délai ou condition remplaçant la vente forcée. La cessation des pouvoirs non exécutés et la réserve des contrats antérieurs organisent le retrait, sans imposer de dépôt aux organismes. Le coût du traitement administratif de cette transition et le solde de l'ensemble des codes ne sont pas chiffrés.",
        'effects': [{
            'kind': 'obligation_removed',
            'measure_id': 'logement-social-cessions-forcees-sanctions',
            'description': "Suppression des deux branches d'un pouvoir de cession forcée de logements par administrateur, comme sanction de SEM et d'organismes agréés de maîtrise d'ouvrage.",
            'before': "Après le contradictoire de L. 342-12, le ministre pouvait nommer un administrateur pour céder les logements locatifs et logements-foyers conventionnés des SEM, ou aidés par l'Etat outre-mer, et les logements locatifs sociaux des organismes agréés L. 365-2. Ni taux fiscal ni délai de paiement ne caractérisent cette contrainte patrimoniale.",
            'after': "Aucune cession ne peut être imposée sur ces deux fondements dès l'entrée en vigueur de la loi ; les mandats anciens cessent pour les cessions non valablement conclues. Les autres sanctions, contrats conclus et obligations conventionnelles sont conservés.",
            'unit': 'legal_duty',
            'affected_population': "Sociétés d'économie mixte exerçant la construction et la gestion de logements sociaux et organismes titulaires de l'agrément L. 365-2 concernés par ces sanctions.",
            'conditions_and_transition': "Application immédiate aux nouvelles décisions et aux effets de décisions anciennes, même définitives, pour les seules cessions non valablement conclues ; maintien des contrats conclus, transferts exécutés, créances, recours et droits des occupants.",
            'replacement_or_new_burdens': "Aucune procédure de remplacement ; conservation des instruments antérieurs de contrôle, de sanction et de récupération des aides, sans agrément implicite.",
            'source_quote': plain(source0_b + '\n' + source0_c),
            'proposed_quote': transition0[0]
        }]
    }
})

xml1 = second['previous_draft']['proposed_xml'].replace(
    "Le barème de l'aide personnalisée au logement n'a pas à être annexé au projet de bail.",
    "Le barème de l'aide personnalisée au logement et les éléments de ce barème n'ont pas à être annexés au projet de bail ni remis séparément à ce titre."
)
assert xml1 != second['previous_draft']['proposed_xml']
a1 = identity(second)
a1.update({
    'proposed_xml': xml1,
    'reason': "Réforme de fond déjà acquise, maintenue et rendue explicite pour les éléments du barème : suppression de l'annexion systématique du barème général APL et de la remise répétée d'une convention déjà reçue dans sa version applicable. L'interdiction de les rétablir par un document séparé au seul titre de cet article évite une substitution équivalente. Le barème ne fixe pas le droit individuel à l'aide et peut être périmé ; une nouvelle copie de la même convention n'apporte aucune information. L'examen supplémentaire ne justifie pas de supprimer l'offre de bail conforme, la première remise de la convention ou le délai de six mois : ils permettent un consentement informé et protègent le choix du locataire ou de l'occupant. Les quatre alinéas de fond, y compris la possibilité favorable de prise d'effet sans travaux, les conditions du refus, la réserve de L. 353-9 et l'occupation dans l'attente des travaux, conservent leur portée. Il ne s'agit ni d'une suppression de l'APL ni d'une nouvelle coupe chiffrée par rapport au brouillon ; la réduction se mesure par rapport à la source officielle.",
    'review_notes': "Source, notes vides, brouillon et texte initial entier de SRU 140 lus ; aucun tableau ni source_companions. Sources locales de L. 353-3, L. 353-6, L. 353-8, L. 353-9, L. 353-16, L. 441-3 et D. 353-46, D. 353-96, D. 353-140 et D. 353-197 relues. Les quatre règlements imposent encore des éléments du barème et la copie de la convention : les coordonner à la dispense législative, sans remplacer l'annexe par un envoi distinct ni exiger la preuve nouvelle de la remise passée. Leurs exigences autonomes de notification et de reproduction des droits d'option ne sont pas supprimées ici. Les clauses types des annexes à D. 353-32, D. 353-90, D. 353-127 et D. 353-190 identifiées dans le brouillon restent à confronter intégralement puis à coordonner : ce lot ne les donne pas pour réécrites. Le préalable autonome de publicité foncière de L. 353-3 reste applicable ; le V de SRU 140 visait explicitement cette publicité et ajoute seulement le cas sans travaux. La filiation des suppressions intermédiaires de mots sur la publicité dans l'article actuel reste à documenter et ne vaut pas abrogation de L. 353-3. Le délai de six mois est une faculté d'option, non une attente obligatoire : pas de délai minimal supprimable à cet endroit. La date de signature, qui peut mettre fin à l'application de la loi de 1948, n'est pas confondue avec la prise d'effet après travaux. La dérogation de L. 353-8 pour travaux de sécurité, salubrité ou habitabilité et les conditions de retour à la loi de 1948 de L. 353-9 (soixante-cinq ans ou soixante ans dans les cas prévus, ressources et applicabilité persistante), avec vocation à l'APL et loyer conventionnel, demeurent. Le refus protégé conserve le bail en cours sous la réserve de 1967 et les exceptions de L. 353-16 et L. 441-3 ; aucun nouveau loyer ni SLS n'est créé. Les renvois aux deuxième et troisième alinéas restent exacts ; seul l'alinéa transitoire est ajouté en cinquième position. Aucun des délais en cours, baux valables ou droits antérieurs n'est rouvert. Les lois n° 48-1360 et n° 67-561 ne figurent pas intégralement dans les sources locales assignées et ne sont pas réécrites : leurs réserves sont intégralement conservées. Le dispositif de rénovation locative de vingt-quatre mois n'est pas applicable par la seule réécriture de cet article ; il appelle la loi n° 89-462, notamment ses articles 6 et 20-1, hors lot. Aucun achèvement des autres composantes de SRU 140 ou de l'examen des 209 articles n'est affirmé. Pas de modification du calcul, des conditions de ressources ni des circuits autonomes de demande d'APL, et pas de chiffrage de coût national.",
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Obligation pour le propriétaire d'annexer au projet de bail le barème général de l'aide personnalisée au logement ou des éléments de ce barème ; aucun envoi séparé n'est imposé à ce titre.",
        "Obligation de remettre une nouvelle copie de la convention au locataire ou à l'occupant qui l'a déjà reçue dans sa version applicable, sans nouvelle attestation justificative."
    ],
    'benefit_review': "La prise d'effet du bail sans travaux dès son acceptation, avantage introduit par SRU 140 V, reste ouverte aux futures situations éligibles. Les deux délais de six mois, le maintien des stipulations du bail refusé sous réserve de la loi de 1967 et le droit d'occuper les lieux jusqu'à l'entrée en vigueur du bail accepté sont conservés. La réserve de L. 353-9 protège toujours le retour conditionnel à la loi de 1948 et la vocation à l'APL. La possibilité du propriétaire de demander révision ou report de ses engagements en cas de refus est maintenue. L'absence de droit à l'APL en cas de refus reste la condition du régime actuel, et non une exonération supprimée ; aucun barème ni avantage de calcul de l'aide n'est retranché. Les dispenses documentaires nouvelles bénéficient aux futurs projets de bail sans fermer les droits antérieurs.",
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à la source officielle entière, le propriétaire ne doit plus joindre le barème général APL et n'a plus à remettre une convention déjà reçue à jour. La dispense couvre expressément les éléments du barème et leur envoi séparé, sans remise en cause du premier accès à la convention. Le brouillon portait déjà ces deux coupes ; la présente passe en sécurise la coordination et ne les compte pas une deuxième fois.",
        'scope_limitations': "Seuls les documents joints aux projets de bail relevant de L. 353-7 sont visés pour les projets adressés dès l'entrée en vigueur. Aucun gain n'est affirmé sur le montant de l'aide, les loyers, la publicité foncière, la demande individuelle d'APL ou les notifications autonomes. Les clauses types et les quatre règlements doivent être coordonnés ; le volume de copies évitées et le solde des coûts restent inconnus.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée : aucun registre, formulaire, attestation de remise antérieure, agrément, donnée ou délai ne remplace les pièces retirées. La condition de version applicable limite seulement la dispense de nouvelle copie ; elle ne crée pas de dossier justificatif. La première remise de la convention et les délais protecteurs existaient déjà ; aucun solde global de complexité n'est chiffré.",
        'effects': [{
            'kind': 'obligation_removed',
            'measure_id': 'apl-conventionnement-annexes-allegement',
            'description': "Retrait du barème APL des pièces obligatoires et de la duplication d'une convention déjà remise dans sa version applicable.",
            'before': "Tout propriétaire proposant le bail de L. 353-7 devait annexer une copie de la convention et du barème APL, même si le destinataire possédait déjà la convention ; le droit individuel à l'aide ne se déduisait pas de cette seule annexe.",
            'after': "Le barème et ses éléments ne sont plus exigibles en annexe ni séparément à ce titre ; la convention n'est jointe que si sa version applicable n'a pas déjà été remise. Les deux délais d'option de six mois et les conditions d'accès à l'aide demeurent.",
            'unit': 'legal_duty',
            'affected_population': "Propriétaires de logements conventionnés occupés par un locataire avec bail en cours ou par un occupant de bonne foi relevant de la loi de 1948, et destinataires de leurs projets de bail.",
            'conditions_and_transition': "Projets adressés à compter de l'entrée en vigueur de la loi ; pas de nouvel envoi des projets antérieurs, de reprise des délais en cours ni de modification des baux valablement conclus et droits déjà nés.",
            'replacement_or_new_burdens': "Aucune pièce ni information séparée de remplacement au titre du barème ; première remise de la convention maintenue et aucune nouvelle attestation pour la dispense de duplication.",
            'source_quote': "Au projet de bail doit être annexée une copie de la convention et du barème de l'aide personnalisée dans des conditions définies par décret.",
            'proposed_quote': "Une copie de la convention est annexée au projet de bail, dans les conditions définies par décret, sauf si elle a déjà été remise au destinataire dans sa version applicable. Le barème de l'aide personnalisée au logement et les éléments de ce barème n'ont pas à être annexés au projet de bail ni remis séparément à ce titre."
        }]
    }
})

Path('answer.json').write_text(json.dumps([a0, a1], ensure_ascii=False, indent=2) + '\n')
