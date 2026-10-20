import json
import re
import html
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
A = []


def plain(x):
    return html.unescape(re.sub(r'<[^>]*>', '', x or ''))


def paras(x):
    return re.findall(r'<p>.*?</p>', x, flags=re.S)


def p(x):
    return '<p>' + html.escape(x, quote=False) + '</p>'


def effect(kind, measure, description, before, after, unit, population, transition,
           burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens, source_quote=source_quote,
                proposed_quote=proposed_quote)


def add(i, proposed, reason, notes, classification, assessment, scope, burdens,
        effects=None, benefit=None, removed=None):
    s = S[i]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if s.get('benefit_check_required'):
        assert benefit and len(benefit) >= 100
        a['benefit_review'] = benefit
    a['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=scope,
        new_burdens_review=burdens, effects=effects or [])
    A.append(a)
    return a


IS = 'is-distribution'
OM = 'outre-mer-investissement-fin-agrement-national'

# 217 undecies : les alinéas du I et du II, et leurs renvois ordinaux, restent en place.
q = paras(S[0]['source_xml'])
assert len(q) == 63
q[33] = p('II quater. – Les programmes d’investissement ouvrent droit aux déductions mentionnées aux I, II et II ter sans agrément préalable national, quel que soit leur montant, sous les conditions de fond du présent article et sous réserve des exigences du droit de l’Union européenne mentionnées au VI. Les conditions de fond définies au 1 du III demeurent applicables aux programmes dont le montant total est supérieur à 1 000 000 €.')
q[34] = p('Cette dispense s’applique également lorsque l’investissement est réalisé par une société ou un groupement mentionnés à l’avant-dernière phrase du premier alinéa du I. Pour les investissements mentionnés au I réalisés par cette société ou ce groupement, les conditions de fond définies au 1 du III demeurent applicables lorsque le montant total par programme est supérieur à 250 000 €. Aucune déclaration ou demande particulière ne remplace l’agrément supprimé.')
q[36] = p('III. – 1. Pour ouvrir droit à déduction, les investissements mentionnés au I réalisés dans les secteurs des transports, de la navigation de plaisance, de l’agriculture, de la pêche maritime et de l’aquaculture, de l’industrie charbonnière et de la sidérurgie, de la construction navale, des fibres synthétiques, de l’industrie automobile, ou concernant la rénovation et la réhabilitation d’hôtel, de résidence de tourisme et de village de vacances classés ou des entreprises en difficultés, ou qui sont nécessaires à l’exploitation d’une concession de service public local à caractère industriel et commercial satisfont aux conditions suivantes, sans agrément national préalable ni avis ministériel préalable :')
q[37] = p('L’investissement :')
q[42] = p('Les bénéficiaires directs ou indirects respectent leurs obligations fiscales et sociales, sous réserve des précisions favorables du IV ter. L’obligation de dépôt des comptes annuels reste limitée aux personnes désignées au même IV ter. Les contrôles légalement applicables à la réalisation et à l’exploitation de l’investissement aidé demeurent possibles, sans engagement préalable distinct de les accepter.')
q[43] = p('2. La procédure nationale d’agrément préalable est supprimée. Les délais d’instruction, leur interruption ou suspension et la saisine de la commission consultative attachés à cette seule procédure cessent de s’appliquer, sans faire obstacle aux recours de droit commun relatifs à l’avantage fiscal.')
q[44] = p('Aucun refus de déduction ne peut être fondé sur la seule absence d’une demande, d’un avis ou d’un agrément national supprimé. Les conditions de fond et les contrôles fiscaux demeurent applicables.')
q[45] = p('Les obligations de notification et de suspension de l’octroi d’une aide résultant du droit de l’Union européenne restent applicables dans leur champ propre. Leur accomplissement incombe aux autorités compétentes ; le présent article ne vaut pas décision de compatibilité de la Commission européenne.')
q[46] = p('3. Aucun état récapitulatif distinct des investissements n’est joint à la déclaration de résultat au titre du présent article. Les montants nécessaires à la déduction sont portés dans la déclaration fiscale de droit commun ; les pièces comptables et les données déjà légalement disponibles servent à en contrôler les conditions, sans déclaration de remplacement.')
q[47] = p('La dispense d’agrément national et d’état récapitulatif distinct vaut pour tous les secteurs relevant du présent article, y compris les transports, sans retirer aucune dispense ni dérogation favorable et sous réserve du VI.')
# L'habilitation réglementaire ne doit pas recréer la formalité supprimée.
q[61] = p('Un décret en Conseil d’Etat précise, en tant que de besoin, les modalités d’application du présent article, sans rétablir un agrément national, un avis ministériel préalable ou un état récapitulatif distinct supprimés aux II quater et III.')
q.append(p('VII. – Pour les entreprises relevant du régime d’imposition à la distribution de l’article 219, les déductions et les reprises prévues au présent article sont constatées aux dates et pour les montants définis aux I à VI dans le résultat fiscal de référence prévu à l’article 209. Une reprise ne rend pas exigible, à elle seule, un impôt sur un bénéfice conservé dans l’entreprise. Les déductions réduisent une seule fois les bases de bénéfices dont l’imposition est différée ou alimentent, pour leur fraction non utilisée, les déficits reportables dans les conditions de l’article 209 ; une fraction déjà déduite d’une base ne peut être à nouveau imputée comme déficit lors de sa distribution. Elles ne réduisent pas le compte des bénéfices déjà taxés ou définitivement exonérés. Aucune distribution ni aucun investissement supplémentaire n’est exigé pour conserver une déduction régulièrement acquise. Les rétrocessions de 77 % prévues au 5° du I et aux dispositions qui y renvoient et celle des trois quarts prévue au 3° du I bis demeurent calculées sur l’avantage en impôt effectivement procuré, sans double emploi ; leur bénéfice reste dû aux exploitants et aux accédants éligibles. Le suivi utilise les éléments comptables et fiscaux de droit commun, sans état distinct supplémentaire.'))
q.append(p('VIII. – Les suppressions de procédure prévues aux II quater et III s’appliquent dès l’entrée en vigueur de la loi qui les institue aux démarches restant à accomplir, y compris pour un investissement ou une souscription antérieurs, sans retirer un agrément, une déduction, une dispense ou un droit valablement acquis. Une demande pendante n’a pas à être renouvelée et les données déjà remises restent utilisables dans les conditions légales. Les opérations nouvelles ou encore éligibles restent soumises aux conditions matérielles et aux limites temporelles du présent article. Les modifications du régime d’aide ne sont mises en œuvre que dans le respect des règles européennes de notification, d’exemption et de compatibilité applicables. Les dettes, créances, reprises, restitutions, prescriptions et recours afférents aux périodes antérieures conservent leur régime ; aucune reprise n’est fondée sur une formalité supprimée dont l’échéance est postérieure à l’entrée en vigueur. Le VII s’applique aux exercices relevant du régime de distribution ; il n’annule aucune dette d’impôt antérieure ni les obligations distinctes de l’impôt minimum international.'))
x = '\n'.join(q)
add(0, x,
    'Réforme de fond : suppression des agréments nationaux liés aux seuils de 1 000 000 € et 250 000 €, du circuit sectoriel ministériel, de son avis et de sa commission, de l’engagement distinct d’accepter les contrôles et de l’état récapitulatif distinct. Les conditions économiques, sociales, environnementales, antifraude et de protection des tiers subsistent directement. Coordination nécessaire de toutes les déductions et reprises avec les résultats de référence et l’IS à la distribution, sans double déduction ni annualité rétablie. Les autres alinéas sont maintenus intégralement, sans prétendre les avoir réécrits.',
    'Lecture des 63 paragraphes et de la note d’entrée en vigueur au 1er janvier 2026. Les 22 alinéas du I restent dans leur ordre : les renvois aux 7e/8e, 9e, 14e à 19e, 15e à 20e et 19e alinéas ne sont pas déplacés. Le IV et ses transmissions 210 A/210 B restent entiers. Les délais matériels de 5, 7, 10 et 15 ans, les deux ans d’achèvement et les douze mois ne sont pas supprimés : ils définissent l’investissement aidé et ses rétrocessions, distinctement de l’agrément. Le VI, l’exclusion européenne des entreprises en difficulté, les plafonds d’intensité applicables, notifications et effet incitatif européens restent à coordonner avant mise en œuvre ; l’abolition du visa national ne prouve pas cette compatibilité. La mention des entreprises en difficultés au III et leur exclusion au VI préexistent ; le VI limite ce champ sans rétablir le visa. Les plafonds de 20 millions d’euros, par watt, par véhicule 30 000 €, par mètre carré, les fractions moitié/quart/20 %, 77 % et trois quarts sont conservés. Coordination des annexes II/III et des règles d’agrément de l’article 1649 nonies à prévoir dans leur champ exact ; ces textes ne sont pas déclarés réécrits ici. Les articles 199 undecies A/B, 244 quater W/X, 39, 210 A/B et 44 quaterdecies gardent leurs conditions autonomes. Les renvois nouveaux aux règles de distribution des articles 209 et 219, absents des cibles fournies comme telles, ont été confrontés à leurs propositions du corpus public local, notamment 209 XI à XIII et 219 V/VI ; ce sont des projets, non le droit officiel. Le renvoi CCH D331-76-5-1 porte sur le prêt de location-accession, sans lien avec un contrat de travail. Aucun rendement budgétaire, aucune compensation et aucune suppression supplémentaire du crédit outre-mer ne sont allégués.',
    'material_reduction',
    'La comparaison avec toute la source démontre le retrait de deux circuits d’agrément nationaux et d’un état récapitulatif, sans déclaration équivalente. Le mécanisme fiscal avantageux demeure ; la coordination avec l’IS à la distribution n’est pas une seconde suppression d’impôt.',
    'L’allègement n’abolit ni les conditions de l’aide, ni les contrôles fiscaux, ni les exigences européennes et les délais d’exploitation. Le coût net du dispositif et les coordinations réglementaires ne sont pas chiffrés ni achevés par ce seul article.',
    'Aucune charge nouvelle autonome n’est identifiée : les critères du III existaient déjà, le calcul et la preuve passent par la comptabilité et la déclaration communes, sans dossier distinct. Le traitement des aides par l’administration demeure ; aucun solde global de complexité n’est établi.',
    effects=[
        effect('authorization_removed', OM,
            'Fin des agréments nationaux de montant et sectoriels, sans déclaration de substitution.',
            'Agrément obligatoire au-delà de 1 000 000 €, ou 250 000 € via certaines sociétés ; agrément sectoriel avec avis ministériel et instruction, sous dispenses existantes.',
            'Aucun agrément national, quel que soit le montant ou le secteur ; conditions de fond et droit européen maintenus.',
            'legal_duty', 'Entreprises et associés éligibles aux I, II et II ter, y compris opérations futures dans les dates légales.',
            'Démarches restant à accomplir dès entrée en vigueur ; droits acquis et règles européennes réservés.',
            'Aucun dossier déclaratif équivalent ; pouvoirs fiscaux de droit commun maintenus.',
            'Les programmes d\'investissement dont le montant total est supérieur à 1 000 000 € ne peuvent ouvrir droit à la déduction mentionnée aux I, II et II ter que s\'ils ont reçu un agrément préalable du ministre chargé du budget dans les conditions prévues au III.',
            'Les programmes d’investissement ouvrent droit aux déductions mentionnées aux I, II et II ter sans agrément préalable national, quel que soit leur montant, sous les conditions de fond du présent article et sous réserve des exigences du droit de l’Union européenne mentionnées au VI.'),
        effect('obligation_removed', 'outre-mer-investissements-fin-etat-recapitulatif',
            'Suppression de l’état récapitulatif spécial joint par les propriétaires ou crédit-preneurs dispensés d’agrément.',
            'État récapitulatif des investissements joint à chaque déclaration de résultat concernée par le III, 3.',
            'Aucun état distinct, sans déclaration de remplacement ; montants utiles dans la déclaration commune.',
            'legal_duty', 'Entreprises propriétaires ou crédit-preneuses relevant du III, 3.',
            'Dépôts restant à accomplir dès entrée en vigueur, même concernant un investissement antérieur.',
            'Pas de nouvelle transmission ; les justificatifs de l’avantage restent contrôlables.',
            "L'entreprise propriétaire des biens ou qui les a acquis en crédit-bail joint à sa déclaration de résultat un état récapitulatif des investissements réalisés au cours de l'exercice et au titre desquels la déduction fiscale est pratiquée.",
            'Aucun état récapitulatif distinct des investissements n’est joint à la déclaration de résultat au titre du présent article.'),
        effect('coordination', IS,
            'Articulation des déductions, déficits et reprises avec les bases différées sans double utilisation.',
            'Déduction et reprise rattachées au résultat imposable d’un exercice, dans le système annuel officiel.',
            'Même fait générateur de l’avantage, ajustement du résultat de référence sans IS ordinaire avant distribution.',
            'other', 'Entreprises bénéficiaires de la déduction relevant du nouvel IS ordinaire.',
            'Exercices relevant du régime de distribution ; dettes anciennes et minimum international distincts.',
            'Suivi par les données communes, sans état supplémentaire ; pas de gain fiscal chiffré.',
            "La déduction est opérée sur le résultat de l'exercice au cours duquel l'investissement est mis en service, le déficit éventuel de l'exercice étant reporté dans les conditions prévues au I de l'article 209.",
            'Une reprise ne rend pas exigible, à elle seule, un impôt sur un bénéfice conservé dans l’entreprise.')],
    benefit='Sont conservés pour les opérations encore ou nouvellement éligibles jusqu’aux échéances légales : déduction des investissements productifs, déduction par les associés et groupements, rénovation hôtelière et réhabilitation lourde, concessions, câbles (moitié puis quart), navigation de croisière (20 %), transports et autres investissements des I bis, I quinquies et I sexies de 199 undecies B, logement locatif et location-accession, et déductions des souscriptions des II et II ter. Restent les exceptions en faveur de véhicules éligibles, les plafonds et frais de transport/installation admis, les déficits reportables et l’exclusion de la déduction du calcul de 44 quaterdecies. Les rétrocessions de 77 % aux exploitants et des trois quarts aux accédants ne sont pas retirées. Les exceptions de reprise pour transmission 210 A/210 B, changement de locataire défaillant, durée normale d’utilisation plus courte, limite du prix de cession et titres substitués restent intégrales. Le plan d’apurement social vaut toujours régularité au IV ter et les adaptations locales demeurent. Les anciennes dispenses d’agrément, le tacite et les délais favorables ne sont pas remplacés par une autorisation plus dure : l’agrément national lui-même disparaît. Aucun plafond ni exclusion fiscale n’est ajouté ; les critères préexistants a à d et le VI européen subsistent. La coordination permet de consommer une seule fois déductions et déficits dans les bases différées, sans perte des droits anciens et sans transformer l’avantage en crédit nouveau. La date du 31 décembre 2029 n’est ni raccourcie ni artificiellement renouvelée.',
    removed=[
        'Agrément national préalable imposé en raison des seuils de 1 000 000 € et 250 000 € aux programmes des II quater et III.',
        'Agrément sectoriel du ministre du budget, avis préalable du ministre de l’outre-mer et information exécutive liée à ce circuit national.',
        'Instruction, délais, interruptions, commission consultative et engagement distinct d’accepter les contrôles attachés au seul agrément national.',
        'État récapitulatif des investissements obligatoirement joint à la déclaration de résultat au titre du III, 3, sans dépôt spécial de remplacement.'
    ])

# 217 duodecies : tous les champs territoriaux et transitions historiques subsistent.
q = paras(S[1]['source_xml'])
old = "L'option est formulée sur un document conforme à un modèle établi par l'administration, auprès du service des impôts du lieu de dépôt de la déclaration de résultat, avec la déclaration de résultat de l'exercice au titre duquel la déduction prévue au présent article est pratiquée."
new = 'L’option est formulée par une mention dans la déclaration de résultat de l’exercice au titre duquel la déduction prévue au présent article est pratiquée, auprès du service des impôts du lieu de dépôt de cette déclaration. Aucun document distinct ni modèle administratif particulier n’est exigé.'
assert old in q[5]
q[5] = q[5].replace(old, new)
q.append(p('Pour les options restant à exercer à compter de l’entrée en vigueur de la loi supprimant le document distinct, cette suppression s’applique également aux opérations antérieures encore recevables dans les conditions du présent article. Les options, agréments et droits valablement acquis demeurent. Les règles de constatation et d’utilisation sans double emploi des déductions et de leurs reprises dans le régime de distribution prévues au VII de l’article 217 undecies s’appliquent aussi aux opérations relevant du présent article, y compris en cas d’option pour la rédaction antérieure à la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021. Les suppressions de procédure nationale prévues aux II quater, III et VIII de l’article 217 undecies s’appliquent aux démarches restant à accomplir pour ces opérations, même sous cette option, sans remettre en cause les conditions historiques d’éligibilité. Aucune disposition du présent alinéa ne rouvre le délai des commandes, versements, demandes ou ouvertures de chantier fixé au 31 décembre 2021. Les exigences européennes demeurent applicables dans leur champ propre, sans remettre en cause l’exclusion du VI de l’article 217 undecies dans les collectivités énumérées à l’alinéa précédent. Les règles d’entrée en vigueur propres à Saint-Martin demeurent applicables.'))
x = '\n'.join(q)
add(1, x,
    'Réduction normative ciblée : l’option historique en faveur de la rédaction antérieure à la loi de finances pour 2021 est exprimée dans la déclaration de résultat existante, sans document séparé imposé par modèle. Coordination des déductions outre-mer survivantes avec le VII nouveau de 217 undecies ; les périmètres territoriaux et les quatre voies transitoires ne sont pas reformulés.',
    'Les sept paragraphes, la note 2022 et la condition européenne de mise en œuvre à Saint-Martin sont lus intégralement. Le texte officiel ferme le régime général au 31 décembre 2021 mais laisse une option pour certains engagements antérieurs dont le fait générateur peut être ultérieur : ne pas présenter cette option comme un nouveau dispositif général 2026. Sont maintenus les acomptes d’au moins 50 %, la commande ou déclaration d’ouverture de chantier et les demandes parvenues au 31 décembre 2021. Le renvoi aux b et c du 1 du I de 244 quater X, la non-application du seuil de chiffre d’affaires et l’exclusion du VI dans les six territoires énumérés restent entiers ; Saint-Martin n’est pas ajouté à cette dernière liste. Le VII nouveau de 217 undecies est dans le présent lot, pas dans les cibles obligatoires de reference-targets ; coordination facultative signalée ici. Les dispositions réglementaires imposant le modèle de l’option devront être mises en accord, sans nouveau dépôt. Le renvoi ancien au cinquième alinéa de 217 undecies est conservé : il vise sa dernière phrase sur la navigation de croisière, dont la position n’a pas changé.',
    'material_reduction',
    'Le seul allègement propre est le retrait du document d’option distinct ; le choix fiscal demeure dans la déclaration existante. La coordination de l’IS ne supprime pas une nouvelle taxe et les droits matériels de 217 duodecies ne sont pas fermés aux opérations futures encore recevables.',
    'Aucune réouverture générale après 2021 n’est décidée. Les aides locales, exceptions de croisière, conditions locatives et exigences européennes restent dans leur champ ; le gain de coût administratif et les effets budgétaires ne sont pas chiffrés.',
    'Aucune charge nouvelle n’est identifiée : la même option est portée sur la déclaration existante, avec suppression du modèle et du dépôt séparé. Les conditions et preuves préexistantes subsistent sans nouveau formulaire ni registre.',
    effects=[effect('obligation_merged', 'outre-mer-option-fin-document-distinct',
        'Intégration de l’option transitoire dans la déclaration de résultat déjà due.',
        'Option sur un document conforme à un modèle administratif, déposé avec la déclaration de résultat.',
        'Une mention dans cette déclaration, sans document séparé ni modèle imposé.',
        'legal_duty', 'Entreprises ayant une opération encore recevable au titre des quatre transitions de 217 duodecies.',
        'Options restant à exercer dès entrée en vigueur, sans rouvrir les engagements clos au 31 décembre 2021.',
        'Aucune option nouvelle ni déclaration équivalente créée ; la déclaration commune existait déjà.',
        old, 'Aucun document distinct ni modèle administratif particulier n’est exigé.')],
    removed=['Document séparé conforme à un modèle administratif pour exercer l’option historique jointe à la déclaration de résultat.'])

# 217 quindecies : ni abrogation de l'amortissement ni création d'un crédit.
x = S[2]['source_xml'] + p('Pour les exercices relevant du régime d’imposition à la distribution de l’article 219, cet amortissement est constaté dès l’année de réalisation de l’investissement dans le résultat fiscal de référence établi selon l’article 209. Il réduit une seule fois les bases de bénéfices dont l’imposition est différée ; sa fraction non utilisée relève des règles de déficit reportable de ce même article, sans qu’une fraction déjà déduite d’une base puisse être imputée une seconde fois lors d’une distribution. Sa constatation n’exige aucune distribution. Les conditions propres aux sociétés et aux souscriptions visées à l’article 238 bis HV et le respect du règlement mentionné au deuxième alinéa demeurent applicables. Les amortissements et déficits antérieurs non consommés conservent leurs droits, sans double déduction ni imposition annuelle des seuls bénéfices conservés. Les règles antérieures continuent de régir les exercices précédant ce régime, leurs dettes, créances et recours.')
add(2, x,
    'Coordination nécessaire, sans retrait de l’amortissement exceptionnel de 50 % : l’année de l’investissement continue d’ouvrir le droit, mais sa déduction affecte les bases différées et les déficits du nouveau régime, pas un IS annuel fictif. Les deux alinéas officiels sont maintenus.',
    'Le règlement 2023/2831 et la note relative aux aides octroyées depuis le 1er janvier 2024 subsistent. L’article 238 bis HV officiel du corpus local a été lu : souscriptions en numéraire du 1er janvier 2023 au 31 décembre 2028, sociétés de capitaux agréées, activité d’acquisition de contrats d’approvisionnement à long terme d’électricité et capital agréé. L’agrément propre à 238 bis HV ne peut être présenté comme supprimé par cet article ; son champ, lié à un dispositif d’aide et à un volume de capital, appelle un examen distinct. Renvois nouveaux aux mécanismes des articles 209 et 219 non fournis comme cibles dans reference-targets : leurs propositions locales 209 XI/XIII et 219 V/VI ont été lues, sans les assimiler au droit en vigueur. Le taux de 50 % est un montant d’amortissement, pas un taux d’IS ni un remboursement de 50 % de la souscription. Aucun chiffrage national ou crédit nouveau.',
    'coordination_only',
    'Le bénéfice de l’amortissement de 50 % est conservé en entier et articulé avec les bases différées. Cet article ne démontre aucune suppression autonome de taxe, d’agrément de 238 bis HV ni de formalité.',
    'Les périodes d’éligibilité, l’agrément du capital et le plafond de minimis gardent leur champ ; le montant économique effectivement imputable dépend des bases et des pertes, sans rendement garanti.',
    'Aucune charge nouvelle propre n’est identifiée : le calcul comptable de l’amortissement reste nécessaire et le suivi utilise le résultat de référence de droit commun. Aucun état, registre ou justificatif distinct n’est ajouté.',
    effects=[effect('coordination', IS, 'Conservation de l’amortissement dans le régime de distribution.',
        'Amortissement exceptionnel de 50 % dès l’année de réalisation, utilisé dans le système annuel d’IS.',
        'Même amortissement de 50 %, constaté à la même date dans les bases différées et déficits, une seule fois.',
        'other', 'Entreprises réalisant les souscriptions éligibles de 238 bis HV.',
        'Exercices du régime de distribution, avec droits antérieurs préservés et contrôle de minimis.',
        'Aucune formalité de remplacement ; agrément distinct de 238 bis HV non aboli.',
        'un amortissement exceptionnel égal à 50 % du montant des sommes effectivement versées pour la souscription au capital des sociétés définies à l’article 238 bis HV.'.replace('l’article', "l'article"),
        'Sa constatation n’exige aucune distribution.')])

# 217 septdecies : réserve historique, les périodes favorables ne sont pas renouvelées.
x = S[3]['source_xml'] + p('3. Pour les exercices relevant du régime d’imposition à la distribution de l’article 219, le rapport prévu au 2 est effectué dans le résultat fiscal de référence établi selon l’article 209 et affecte les bases différées correspondantes, sans rendre exigible un impôt ordinaire avant leur distribution. Les sommes n’ayant pas encore été rapportées à l’entrée dans ce régime ne sont pas considérées comme des bénéfices déjà taxés. Une même somme ne peut être soumise deux fois à l’impôt du fait de ce rapport et de sa distribution. Les dotations admises au titre des exercices ouverts en 2012 et en 2013, les reprises et dettes antérieures et les recours conservent leur régime ; le présent 3 n’ouvre pas de nouvelle période de dotation déductible et ne modifie pas les obligations prudentielles distinctes ni le minimum international.')
add(3, x,
    'Coordination nécessaire de la reprise d’une réserve fiscale historique avec l’IS à la distribution. Les taux de dotation de 60 % en 2012 et 40 % en 2013, le champ mutualiste/prévoyance et le fait de reprise au prélèvement restent intacts ; aucune réouverture ni reprise annuelle sur bénéfice conservé n’est créée.',
    'Le 2 officiel prévoit une reprise encore susceptible de produire des effets sur une réserve ancienne : son abrogation totale créerait une exonération définitive d’une base seulement différée et n’est pas justifiée comme doublon. Les nouveaux renvois aux articles 209 et 219, non cibles fournies, sont fondés sur la lecture des propositions publiques locales 209 XI/XIII et 219 V/VI. Le stock non taxé ne rejoint pas le compte protégé de 209 XI, 1. Les règles prudentielles du code de la mutualité et du titre III du livre IX CSS restent distinctes et ne sont pas réécrites ; le présent article ne crée ni capitalisation salariale ni nouvelle solvabilité déclarative.',
    'coordination_only',
    'Seule l’articulation de la reprise historique avec le fait générateur de distribution change. La réserve, ses périodes et ses deux taux ne sont pas une nouvelle réduction et aucune charge prudentielle n’est abolie.',
    'Le texte couvre les soldes des seules dotations de 2012/2013 et ne chiffre pas leur montant. Les régimes prudentiels et le minimum international conservent leur champ propre.',
    'Aucune charge nouvelle n’est identifiée : la réserve devait déjà être suivie jusqu’au prélèvement ; la même base est suivie dans les comptes fiscaux communs sans nouvel état ou agrément.',
    effects=[effect('coordination', IS, 'La reprise d’une réserve non encore taxée alimente les bases différées.',
        'Sommes prélevées rapportées au résultat imposable de l’exercice du prélèvement.',
        'Même reprise au résultat fiscal de référence, avec IS ordinaire exigible seulement à la distribution.',
        'other', 'Mutuelles, unions et institutions de prévoyance disposant encore de réserves éligibles 2012/2013.',
        'Exercices relevant du nouveau régime ; anciens impôts et recours conservés.',
        'Suivi préexistant de la réserve, aucune nouvelle dotation requise.',
        "Les sommes prélevées sur la réserve mentionnée au 1 sont rapportées au résultat imposable de l'exercice en cours à la date de ce prélèvement.",
        'Les sommes n’ayant pas encore été rapportées à l’entrée dans ce régime ne sont pas considérées comme des bénéfices déjà taxés.')])

add(4, None,
    'Maintien nécessaire après examen : la cote unique évite la multiplication d’impositions par activité et identifie le débiteur dans les sociétés de 206, 4. L’article ne fixe ni assiette annuelle, ni acompte, ni autorisation ; il est compatible avec les nouvelles liquidations à la distribution sans changer ses mots.',
    'Le renvoi aux a à f du I de 219 reste utile aux catégories et taux particuliers conservés par le VI proposé de cet article ; il ne commande pas une cotisation sur un bénéfice non distribué. Le 4 de 206 vise les droits des commanditaires et associés non indéfiniment responsables ou non identifiés, non une règle de contrat de travail. La proposition de 206 distingue expressément régime ordinaire de distribution et revenus patrimoniaux du 5. Il n’y a pas de lieu ni de date de paiement nouveau dans 218. Aucun allègement autonome supplémentaire n’est compté.',
    'retained_necessary',
    'La cote unique et l’identification légale du redevable sont des garanties utiles contre la fragmentation d’un même IS ; aucune obligation distincte supprimable n’est établie dans cet article bref.',
    'Le maintien ne valide pas à lui seul les liquidations des articles 219 et 1668 ni tous leurs renvois. Le régime des activités spéciales reste à son champ.',
    'Aucune charge nouvelle n’est identifiée puisque le texte est conservé intégralement ; aucun dépôt, délai, registre ou donnée supplémentaire ne résulte de cet article.')

add(5, None,
    'Maintien nécessaire : l’article détermine un lieu unique d’imposition et les rattachements des personnes morales sans siège français. Cette règle évite des conflits de compétence et ne constitue ni un agrément préalable d’activité ni une obligation déclarative distincte.',
    'La faculté de désignation administrative est une compétence de localisation fiscale, non une autorisation d’exploiter. Le 2 et la note renvoient à l’article 23 ter de l’annexe IV pour les personnes étrangères ; aucun contenu de cet arrêté n’est inventé ni modifié. Le principal établissement, la direction effective et le siège ne sont pas confondus avec la résidence d’un associé. Le texte ne fixe aucune annualité d’assiette ; il reste utile pour les créances anciennes et les distributions nouvelles.',
    'retained_necessary',
    'La source entière répartit seulement la compétence territoriale des services fiscaux. Sa suppression laisserait indéterminé le service compétent sans retirer un prélèvement ou une démarche propre.',
    'Aucune économie de procédure ou modification du régime des personnes non résidentes n’est démontrée. Le détail réglementaire de 23 ter n’est pas réécrit dans ce lot.',
    'Aucune charge nouvelle n’est identifiée : maintien intégral de la localisation existante, sans obligation pour le contribuable de demander une nouvelle désignation.')

x = S[6]['source_xml'] + p('Pour les exercices au cours desquels la société ou la personne morale associée relève du régime d’imposition à la distribution de l’article 219, sa part de bénéfices est déterminée dans le résultat fiscal de référence prévu à l’article 209. L’attribution de cette part ou son versement par la société ou le groupement relevant des articles 8, 8 quater, 8 quinquies ou 1655 ter ne déclenche pas, à lui seul, l’impôt ordinaire tant que ce bénéfice demeure dans l’activité, les réserves, le report ou la trésorerie de la personne morale associée. L’impôt devient exigible lors d’une distribution par cette dernière dans les conditions de l’article 219. Les pertes, exonérations et fractions déjà taxées conservent leurs règles et ne sont prises en compte qu’une fois. Les revenus relevant du 5 de l’article 206 demeurent exclus du présent article. Les exercices antérieurs au régime de distribution, leurs dettes, créances, contrôles et recours restent soumis aux règles qui leur étaient applicables ; le minimum international et les régimes annuels distincts conservent leur champ.')
add(6, x,
    'Coordination de fond nécessaire pour éviter que la transparence d’une société de personnes ne recrée un IS annuel chez son associé personne morale. La part reste personnellement attribuée à cet associé ; son encaissement ne vaut pas distribution de cet associé à ses propres membres.',
    'Le premier alinéa officiel est conservé entier, notamment l’exception de 206, 5 et les quatre régimes 8, 8 quater, 8 quinquies et 1655 ter. L’allocation de bénéfice n’est pas supprimée : elle alimente les résultats de référence. Ne pas appliquer automatiquement les exonérations mère-fille à une simple part transparente ni taxer deux fois la réalisation et l’encaissement. La protection des réserves déjà taxées et l’utilisation unique des pertes relèvent de 209 XI. Les nouveaux renvois 209/219, non cibles fournies de cet article, ont été confrontés aux propositions du corpus public, non au droit officiel prétendument réformé. Les obligations comptables et la détermination des parts restent nécessaires à la répartition entre redevables ; pas de registre séparé créé.',
    'coordination_only',
    'L’article conserve le redevable et la quotité de bénéfice, mais coordonne son imposition avec la distribution effective par l’associé soumis à l’IS. Ce renvoi ne compte pas comme une nouvelle taxe supprimée en plus de la réforme générale.',
    'L’exclusion des revenus patrimoniaux de 206, 5 demeure ; les régimes distincts, conventions et minimum international ne sont pas neutralisés. Aucun taux propre ni gain chiffré n’est avancé.',
    'Aucune charge nouvelle propre n’est identifiée : attribution des parts et résultat de référence utilisent les informations préexistantes et les comptes communs, sans nouvel agrément ni dépôt.',
    effects=[effect('coordination', IS, 'La part de société transparente reste attribuée sans annualité implicite de l’IS ordinaire.',
        'Assujettissement personnel à l’IS sur la part des bénéfices des sociétés et groupements visés.',
        'Attribution inchangée dans le résultat de référence ; la conservation de la part ne déclenche pas l’IS avant distribution par l’associé.',
        'other', 'Personnes morales associées soumises à l’IS, hors 206, 5.',
        'Exercices du régime de distribution ; situations anciennes et régimes distincts préservés.',
        'Même calcul des droits sociaux, sans formalité distincte nouvelle.',
        'sont personnellement soumises audit impôt à raison de la part des bénéfices correspondant aux droits qu’elles détiennent'.replace('qu’elles', "qu'elles"),
        'L’impôt devient exigible lors d’une distribution par cette dernière dans les conditions de l’article 219.')])

add(7, None,
    'Maintien intégral d’un régime distinct expressément réservé par 206, 12 et 219 VI proposés : revenus patrimoniaux des organismes non lucratifs. Les taux favorables de 10 % sur certains titres de créance et de 15 % sur les dividendes restent ouverts ; le taux propre de 24 % n’est pas transformé en régime de distribution.',
    'Le taux de 24 % de ce régime non lucratif n’est pas le taux normal du nouvel IS ordinaire de 20 %. Les organismes et revenus de 206, 5 restent dans leur champ, avec leurs exonérations personnelles. Les produits de 124 B et les titres émis depuis le 1er janvier 1987 des articles 118, 119 et 238 septies A/B/E conservent leur qualification. Ce régime ne comporte ni agrément, ni déclaration distincte, ni contribution accessoire à supprimer ici ; son principe a expressément été conservé dans les coordinations IS. Ne pas relever 10 % ou 15 % à 20 % au nom d’une fusion.',
    'retained_necessary',
    'Le maintien préserve les deux taux réduits d’un régime patrimonial autonome et n’apporte aucune baisse nouvelle. Le calendrier de distribution des sociétés ordinaires ne lui est pas attribué.',
    'Aucune baisse du taux de 24 % ni extension aux activités lucratives n’est décidée dans ce lot ; le produit budgétaire et le nombre de bénéficiaires ne sont pas établis.',
    'Aucune charge nouvelle n’est identifiée : source conservée intégralement, sans condition, option, agrément ou déclaration supplémentaire.',
    benefit='Les taux de 10 % pour les produits de titres de créances de 124 B et les revenus des titres émis à compter du 1er janvier 1987, et de 15 % pour les dividendes, sont conservés intégralement pour toutes perceptions futures éligibles. Le taux de 24 % est celui du régime patrimonial distinct de 206, 5 ; les exemptions de ses organismes ne sont pas effacées par le renvoi à 219. Le taux normal proposé de 20 % des sociétés ordinaires ne remplace donc ni ces taux réduits ni leur champ.')

x = p('Par dérogation aux dispositions de l’article 219, les indemnités perçues par les entreprises sinistrées par faits de guerre au titre de la réparation des éléments d’actif immobilisés ou en remplacement de stocks détruits sont soumises à l’impôt sur les sociétés au plus faible des deux taux suivants : le taux qui serait normalement applicable à ces indemnités, ou le taux de l’impôt sur les bénéfices industriels et commerciaux ou de l’impôt sur les sociétés en vigueur lors de l’exercice au cours duquel le montant soit des dépenses de réparation, soit de la perte comptable des stocks, a été admis en déduction pour la détermination du bénéfice imposable.') + p('L’application du taux le plus favorable ne nécessite aucune demande distincte de l’entreprise. Elle est établie à partir des éléments comptables et fiscaux justifiant l’indemnité et la déduction d’origine, sans attestation nouvelle.') + p('Pour les exercices relevant du régime d’imposition à la distribution de l’article 219, le taux ainsi déterminé est conservé pour la fraction éligible du bénéfice et s’applique lors de sa distribution, sans impôt ordinaire sur sa seule conservation et sans seconde imposition de bénéfices déjà taxés. La dispense de demande distincte s’applique aux liquidations et réclamations restant à effectuer à compter de l’entrée en vigueur de la loi qui l’institue, dans les délais de prescription et de recours applicables. Les droits antérieurs, y compris le bénéfice d’une demande déjà formée, ne sont pas retirés et aucun remboursement général d’impositions définitives n’est créé.')
add(8, x,
    'Réforme de fond ciblée : retrait de la demande distincte conditionnant le taux historique favorable des indemnités de guerre. Le choix du taux le plus favorable devient directement applicable, sans nouveau taux inventé. Coordination nécessaire avec la distribution pour conserver le taux de la fraction d’origine et éviter une imposition annuelle ou un second impôt.',
    'Le sinistre est un fait de guerre concernant actifs immobilisés ou stocks : le terme « indemnités » ne désigne ni licenciement ni préavis. L’exercice de déduction d’origine fixe le taux historique, pas l’année de distribution ; le comparer au taux normalement applicable évite d’imposer un ancien taux plus élevé que celui de droit commun. Les renvois nouveaux à la distribution précisent le champ du renvoi préexistant à 219, dont le projet V/VI a été lu dans le corpus local ; les cibles obligatoires sont exclusivement celles de reference-targets. Les preuves de la dépense/perte et de l’indemnisation restent nécessaires sans nouveau document. Les prescriptions ne sont ni rouvertes ni raccourcies.',
    'material_reduction',
    'La source exige une demande pour un taux historique optionnel ; la proposition retire ce préalable et garantit directement le plus faible du taux normal et du taux historique. Les assiettes et populations ne sont pas élargies par assimilation aux indemnités de rupture.',
    'Seules les indemnités de guerre et les déductions d’origine établies sont couvertes. Aucun montant de gain ni volume d’affaires survivantes n’est démontré ; les années prescrites ne sont pas rouvertes.',
    'Aucune charge nouvelle n’est identifiée : la preuve du taux et de l’assiette était déjà nécessaire à la demande, et aucun formulaire, attestation ou demande de remplacement n’est créé.',
    effects=[effect('obligation_removed', 'indemnites-guerre-taux-favorable-sans-demande',
        'Retrait de la demande distincte pour appliquer le taux historique plus favorable.',
        'Les entreprises doivent demander l’application du taux de l’exercice de déduction des réparations ou pertes de stocks.',
        'Le taux historique s’applique directement lorsqu’il est inférieur au taux normalement applicable ; aucune demande distincte.',
        'legal_duty', 'Entreprises sinistrées par faits de guerre percevant les indemnités définies à 219 ter.',
        'Liquidations et réclamations encore recevables dès entrée en vigueur ; pas de réouverture générale des prescriptions.',
        'Preuves comptables utiles conservées, sans attestation ni déclaration supplémentaire.',
        'peuvent, sur demande de ces entreprises, n\'être soumises à l\'impôt sur les sociétés qu\'au taux de l\'impôt sur les bénéfices industriels et commerciaux',
        'L’application du taux le plus favorable ne nécessite aucune demande distincte de l’entreprise.')],
    benefit='L’avantage possible est le taux historique de l’impôt BIC ou IS de l’exercice où la réparation de l’actif ou la perte des stocks a été déduite. Il reste applicable aux indemnités de guerre futures recevables et aux droits antérieurs sans demande distincte, avec garantie qu’un taux normal plus faible conserve la priorité. La fraction éligible garde ce taux lors de la distribution, sans annualité ni double taxation de réserves déjà imposées. Aucun lien n’est créé avec les indemnités ordinaires ou spéciales du contrat de travail ; ces protections restent à leur champ propre.',
    removed=['Demande distincte de l’entreprise pour obtenir l’application du taux historique favorable aux indemnités de guerre.'])

add(9, None,
    'Maintien nécessaire d’une imputation favorable qui évite le cumul de la retenue à la source et de l’IS sur le même revenu. La formule « éventuellement exigible » n’impose pas une taxation annuelle et reste compatible avec le fait générateur de distribution.',
    'Les retenues de 182 B et de 182 A bis ne sont pas supprimées ou refondues par cet article. L’IS d’un régime distinct reste visé s’il existe. La note ouvre ce mécanisme aux sommes versées depuis le 1er janvier 2009 ; cette date historique ne fixe aucune entrée en vigueur future. La source ne contient ni nouvelle demande, ni délai minimal, ni justificatif distinct à retirer. Les règles générales d’imputation et le contrôle du même revenu empêchent un double emploi sans créer de crédit remboursable en l’absence d’IS.',
    'retained_necessary',
    'La source entière offre uniquement un mécanisme anticumul de deux impôts. La conserver préserve un droit utile, sans présenter une retenue qui subsiste comme supprimée.',
    'Aucune abolition des retenues, restitution nouvelle ou modification conventionnelle n’est démontrée. Les autres revenus ne sont pas couverts par cette imputation spéciale.',
    'Aucune charge nouvelle n’est identifiée : maintien intégral de l’imputation existante, sans nouveau suivi distinct, donnée ou échéance.')


# Les crédits ne sont pas subordonnés à une distribution et leurs horloges propres subsistent.
def credit_coord(i, extra, reason, notes, assessment, scope, benefit):
    x = S[i]['source_xml'] + p(extra)
    quote = plain(S[i]['source_xml']).strip().split('\n')[0]
    add(i, x, reason, notes, 'coordination_only', assessment, scope,
        'Aucune charge nouvelle propre n’est identifiée : les conditions et déclarations du crédit restent celles du dispositif existant ; aucun dépôt, registre ou justificatif supplémentaire n’est ajouté pour les bénéfices conservés. L’imputation et le remboursement ne peuvent être cumulés sur une même fraction.',
        effects=[effect('coordination', IS,
            'Maintien du calendrier et des droits de la créance fiscale sans obligation de distribuer.',
            'Imputation sur l’IS selon les conditions et délais du régime spécial cité par la source, dans le système annuel officiel.',
            'Imputation sur l’IS exigible, y compris à la distribution ; absence d’IS traitée comme excédent sans reporter les délais propres de remboursement.',
            'other', benefit[0],
            'Exercices relevant de la distribution, créances anciennes et nouvelles encore éligibles protégées ; conditions propres du crédit maintenues.',
            'Aucune déclaration de remplacement ; maintien des règles de transfert et d’usage unique de la créance.',
            quote, extra)], benefit=benefit[1])
    return A[-1]

credit_coord(10,
    'Pour les exercices relevant du régime d’imposition à la distribution, l’absence de distribution ne diffère ni la constatation du crédit d’impôt, ni les délais d’utilisation ou de remboursement de la créance prévus à l’article 199 ter B. Le crédit s’impute sur l’impôt sur les sociétés effectivement dû dans ces délais, y compris à raison des distributions. En l’absence d’impôt dû, le crédit non utilisé constitue l’excédent soumis aux mêmes règles ; les entreprises pouvant prétendre au remboursement immédiat le conservent sans avoir à distribuer de bénéfice. Les créances antérieures non consommées conservent leur échéance et leurs conditions de transfert, de cession et de remboursement. Une fraction imputée ou remboursée ne peut être utilisée une seconde fois.',
    'Coordination nécessaire du CIR avec l’IS à la distribution : l’avantage ne devient pas une créance suspendue jusqu’au premier dividende. Le renvoi intégral à 199 ter B, les trois années d’utilisation et les remboursements immédiats de ses bénéficiaires restent applicables ; aucune réduction du CIR n’est décidée par le cadre de chiffrage.',
    '199 ter B a été lu en entier dans le corpus local : dépenses de l’année, créance d’excédent, utilisation sur trois années puis remboursement, transferts de fusion et cession CMF ; remboursements immédiats des entreprises nouvelles éligibles, procédures collectives, JEI et PME, pièces des entreprises de moins de deux ans, exclusion des parts de certaines personnes physiques. Aucun de ces droits ou conditions n’est supprimé. Le renvoi déjà présent à l’annexe III 49 septies L reste conservé, à coordonner sur l’IS exigible sans faire attendre une distribution. La transition ne crée pas un second remboursement ni une réouverture de prescription. Le chiffrage net de l’IS doit garder ce CIR dans la trajectoire des aides maintenues, sans économie de suppression fictive ni financement inventé.',
    'Le CIR et sa remboursabilité sont préservés sous un nouveau fait générateur d’IS ; aucune taxe ou obligation autonome n’est retirée par cette coordination. Aucun effet d’autofinancement ne remplace juridiquement une créance remboursable.',
    'Le champ des dépenses et le calcul de 244 quater B ne sont pas modifiés. Les délais propres, les groupes, les créances cédées et le traitement du minimum international nécessitent leurs règles générales, sans rendement chiffré.',
    ('Entreprises bénéficiaires du CIR au titre de 244 quater B, y compris futures dépenses éligibles.',
     'Le CIR de 244 quater B reste imputable et, pour son excédent, utilisable trois années puis remboursable dans les conditions de 199 ter B. Le remboursement immédiat des catégories éligibles, les droits de transfert en fusion et de mobilisation de créance ne sont pas subordonnés à un dividende. Les droits antérieurs et les dépenses futures encore éligibles sont couverts ; aucun CIR n’est aboli au titre des hypothèses de chiffrage et aucune fraction déjà remboursée ou imputée n’est recréée.'))

credit_coord(11,
    'Pour les exercices relevant du régime d’imposition à la distribution, l’absence de distribution ne diffère ni la constatation du crédit d’impôt, ni les délais d’utilisation ou de remboursement prévus à l’article 199 ter B bis. L’imputation porte sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions ; à défaut d’impôt dû, le crédit non utilisé relève des règles d’excédent de ce même article. Les remboursements immédiats restent ouverts aux catégories qui y ont droit, sans distribution préalable. Les créances antérieures gardent leurs échéances, leurs conditions de cession et de transfert et leurs voies de recours. Une même fraction ne peut être utilisée deux fois au titre d’une imputation ou d’un remboursement ; les transferts successifs d’une même créance ne créent pas de droit supplémentaire.',
    'Coordination nécessaire de l’utilisation du crédit de recherche collaborative avec l’IS à la distribution ; aucune suppression de crédit, de remboursement ni de catégorie favorable. Le premier alinéa est conservé entier.',
    '199 ter B bis a été lu en entier dans le corpus : facturation de l’organisme de recherche, trois années d’utilisation puis remboursement, cession/mobilisation, fusion, exclusion de certaines parts de personnes physiques et remboursements immédiats entreprises nouvelles, procédures collectives, JEI et PME. La note source vise les contrats conclus à compter du 1er janvier 2022 et reste applicable ; une date de facturation n’est pas une date de distribution. La réforme ne rouvre pas la durée légale des contrats éligibles ni ne ferme les créances nouvelles recevables. Aucune réduction des aides d’innovation n’est déduite du seul changement d’IS.',
    'Le droit et le calendrier de remboursement du crédit collaboratif sont conservés sans annualité implicite ni dividende imposé. Il s’agit d’une coordination de créance, pas d’une nouvelle réduction d’impôt distincte.',
    'Les conditions de 244 quater B bis et de 199 ter B bis restent intégrales ; le coût du crédit et l’effet net de l’IS sur l’innovation et les recettes ne sont pas chiffrés.',
    ('Entreprises bénéficiant du crédit de recherche collaborative sur des contrats et dépenses légalement éligibles.',
     'L’imputation du crédit de recherche collaborative et les droits d’excédent, de remboursement après trois années ou immédiatement pour les catégories prévues à 199 ter B bis, de cession et de transfert sont conservés. Ils restent accessibles aux contrats et facturations futurs recevables selon leur champ légal, sans distribution préalable, et aux créances antérieures non consommées. Aucun montant, taux, condition favorable ou remboursement n’est supprimé.'))

credit_coord(12,
    'Pour les exercices relevant du régime d’imposition à la distribution, le crédit reste constaté selon l’année de versement des rémunérations éligibles et les conditions de l’article 199 ter C. Il s’impute sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions. L’absence de distribution ne suspend ni les trois années d’utilisation de l’excédent ni son remboursement à leur expiration, ni les remboursements immédiats prévus au II du même article. Les créances antérieures, leurs conditions de cession ou de nantissement, leurs transferts en cas de fusion et leurs échéances demeurent ; aucune fraction déjà imputée ou remboursée ne peut être utilisée à nouveau. Les périodes de rémunération éligibles ne sont ni rouvertes ni raccourcies par le présent alinéa.',
    'Coordination nécessaire de l’utilisation des créances de 244 quater C avec l’IS à la distribution. Le renvoi complet à 199 ter C est conservé, sans réouverture artificielle du dispositif ni suppression d’une créance survivante.',
    'Lecture intégrale de 199 ter C et de ses notes : origine aux rémunérations versées, trois années puis remboursement ; PME, entreprises nouvelles, procédures collectives et JEI en remboursement immédiat ; cession/nantissement et information préalable, interdiction des cessions partielles multiples, transfert en fusion. Le présent texte ne supprime ni ces protections ni les conditions de la créance. La proposition n’invente pas une nouvelle année de CICE ; l’origine des périodes éligibles demeure 244 quater C. Les règles de distribution ne doivent pas bloquer les demandes ou litiges afférents au stock ancien.',
    'Les droits d’utilisation et de remboursement d’un crédit existant demeurent malgré le changement d’IS. Aucune nouvelle baisse de prélèvement ni prolongation générale d’éligibilité des salaires n’est revendiquée.',
    'Seules les créances légalement nées ou encore éligibles de 244 quater C sont visées ; les périodes closes ne sont pas rouvertes et les transferts de groupe restent régis par leurs textes.',
    ('Entreprises titulaires de créances de 244 quater C encore utilisables ou litigieuses.',
     'Le crédit de 244 quater C, son excédent utilisable trois années puis remboursable, les remboursements immédiats du II de 199 ter C et les droits de mobilisation et de transfert en fusion restent applicables. Le passage à la distribution ne ferme ni ne repousse ces droits et ne rétablit pas un crédit sur des rémunérations hors période légale. Les créances anciennes et les cas futurs encore légalement recevables restent protégés sans double utilisation.'))

credit_coord(13,
    'Pour les exercices relevant du régime d’imposition à la distribution, le crédit est constaté à raison de l’acquisition, de la création ou de la location des biens éligibles dans les conditions de l’article 199 ter D. Il s’impute sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions. L’absence de distribution ne reporte ni les neuf années d’utilisation de l’excédent ni les échéances de remboursement de ce même article, y compris le remboursement sur demande à compter de la cinquième année et les remboursements immédiats de son II. En l’absence d’impôt dû, la fraction non utilisée suit ces règles d’excédent. Les créances antérieures gardent leurs échéances, leurs conditions de transfert et de mobilisation, leurs limites de remboursement et leurs recours. Une même fraction ne peut être imputée ou remboursée deux fois.',
    'Coordination nécessaire du crédit d’investissement de 244 quater E : l’absence d’IS annuel ne réduit ni ne retarde ses remboursements et n’efface pas les créances. Les plafonds favorables et les modes anticipés sont maintenus sans invention d’un remboursement intégral nouveau.',
    '199 ter D officiel et proposé ont été lus dans le corpus : neuf années, remboursement final limité à 50 % et 300 000 €, option à partir de la cinquième année limitée à 35 % et 300 000 €, créance non imposable et mobilisable, transmissions 244 quater E III et 210 A, proportion d’actif net réel en scission/apport partiel et remboursements immédiats des catégories du II. Ces montants et règles demeurent par le renvoi intégral. Les bornes d’acquisition et les reprises de 244 quater E ne sont pas modifiées. Le crédit non remboursable au-delà de ses propres limites ne devient pas intégralement remboursable au seul motif de la distribution.',
    'Le même crédit et ses différentes échéances demeurent utilisables sous l’IS à la distribution ; cette coordination ne compte pas une deuxième baisse d’impôt ni une accélération nouvelle des remboursements.',
    'Les plafonds de remboursement et le champ territorial et matériel de 244 quater E restent applicables. Le solde net de l’IS et des aides ne peut être déduit de cette coordination.',
    ('Entreprises bénéficiaires du crédit de 244 quater E, créances antérieures et investissements futurs éligibles.',
     'Le crédit de 244 quater E conserve son imputation, son report de neuf années, ses remboursements à 50 %/300 000 €, sur demande à partir de la cinquième année à 35 %/300 000 €, et ses remboursements immédiats des catégories prévues au II de 199 ter D. L’absence de distribution ne les ferme pas et n’allonge pas les délais. La non-imposition de la créance, sa mobilisation et ses transferts conservent leur champ pour les droits anciens et les investissements futurs recevables.'))

# 220 E : conserver le mécénat, retirer la péremption du report et le dépôt spécial.
x = p('La réduction d’impôt définie à l’article 238 bis est imputée sur l’impôt sur les sociétés dû au titre de l’exercice au cours duquel les dépenses ont été réalisées. L’excédent éventuel est utilisé pour le paiement de l’impôt sur les sociétés dû au titre des exercices suivants, sans limitation de durée, jusqu’à son utilisation intégrale.') + p('Un décret précise les modalités d’imputation des dispositions du présent article. Le montant de la réduction et de son report est porté dans la déclaration fiscale de droit commun permettant sa liquidation ; aucune déclaration distincte n’est exigée au seul titre du présent article. Les obligations autonomes prévues à l’article 238 bis conservent leur champ.') + p('Pour les exercices relevant du régime d’imposition à la distribution, la réduction est constatée au titre de l’exercice de réalisation des dépenses et s’impute sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions. Aucune distribution préalable n’est exigée pour constater ou conserver son report. Le report ne constitue pas une créance remboursable ; une même fraction n’est utilisable qu’une fois. La suppression de la limite de cinq exercices s’applique aux réductions constatées à compter de l’entrée en vigueur de la loi qui la prévoit et aux reports non expirés à cette date ; elle ne rétablit pas les reports déjà expirés. Les imputations, droits et recours antérieurs demeurent.')
add(14, x,
    'Réduction de fond : suppression de l’expiration du report après cinq exercices pour les réductions de mécénat futures et les reports encore vivants, afin de ne pas conditionner le bénéfice à une distribution forcée. Suppression de l’exigence d’une déclaration distincte fondée sur la seule habilitation de cet article, sans toucher les obligations autonomes de 238 bis. La réduction reste non remboursable et son année de naissance demeure celle de la dépense.',
    'Le texte officiel de 220 E, y compris son habilitation déclarative, a été lu entier. Le plafond d’assiette, les taux, catégories de dons, éventuels reports de dépenses et obligations propres de 238 bis ne sont pas modifiés par le report du crédit de réduction ici traité. La suppression de la limite de cinq exercices ne crée ni déduction supplémentaire de dépense ni remboursement. Identifier les décrets/formulaires fondés exclusivement sur 220 E pour mise en cohérence ; ils ne sont pas présentés comme tous réécrits ici. Une déclaration déjà commune ne constitue pas une seconde obligation supprimée : l’effet démontré principal est la disparition de la péremption. Les stocks expirés ne sont pas ressuscités. Le renvoi préexistant à 238 bis est conservé et aucun renvoi de travail ou de succession n’est créé.',
    'material_reduction',
    'Par rapport à la source entière, les réductions de mécénat ne s’éteignent plus faute d’IS imputable dans les cinq exercices suivants ; la durée illimitée retire une restriction réelle. Le gain ne peut être assimilé à une restitution immédiate ni à une baisse du taux d’IS.',
    'Seul le report de la réduction d’impôt est étendu, pas les plafonds de dons ou les reports de dépenses. Le coût budgétaire du maintien des stocks et le coût net administratif sont inconnus.',
    'Aucune charge nouvelle n’est identifiée : le report devait déjà être suivi, et l’indication commune remplace toute déclaration exclusivement fondée sur cet article. Un suivi plus long peut être nécessaire aux bénéficiaires qui choisissent d’utiliser le droit prolongé ; aucun registre séparé n’est ajouté.',
    effects=[effect('relief_extended', 'mecenat-reduction-report-sans-peremption',
        'Suppression de l’expiration de la réduction de mécénat après cinq exercices.',
        'Excédent de réduction utilisable seulement sur les cinq exercices suivant sa constatation.',
        'Excédent utilisable sans limite de durée jusqu’à épuisement, sans restitution nouvelle et sans changement des taux ou de l’assiette de 238 bis.',
        'other', 'Entreprises soumises à l’IS titulaires d’un excédent de réduction de 238 bis.',
        'Réductions nouvelles et reports non expirés lors de l’entrée en vigueur ; aucune réouverture des reports expirés.',
        'Suivi fiscal existant prolongé selon l’usage du droit, sans registre distinct ni remboursement ajouté.',
        "L'excédent éventuel est utilisé pour le paiement de l'impôt sur les sociétés dû au titre des cinq exercices suivant celui au titre duquel elle est constatée.",
        'L’excédent éventuel est utilisé pour le paiement de l’impôt sur les sociétés dû au titre des exercices suivants, sans limitation de durée, jusqu’à son utilisation intégrale.')],
    removed=['Limite de cinq exercices pour utiliser l’excédent de réduction d’impôt de mécénat, applicable aux reports encore vivants et futurs.', 'Possibilité d’exiger une déclaration distincte au seul fondement de l’habilitation déclarative de l’article 220 E.'])

# 220 F : contrôle de fond et achèvement subsistent, le second agrément est retiré.
q = paras(S[15]['source_xml'])
assert len(q) == 4
q[2] = p('La part du crédit d’impôt obtenu au titre des dépenses mentionnées au 1 du III de l’article 220 sexies afférente à une œuvre qui n’a pas rempli les conditions prévues au II de ce même article fait l’objet d’un reversement. Aucun agrément à titre définitif du président du Centre national du cinéma et de l’image animée n’est exigé au titre du présent article. L’absence de cet agrément ou l’expiration du délai de huit mois qui lui était attaché ne constitue pas, à elle seule, un motif de reversement. Les contrôles de l’éligibilité effective des œuvres et des dépenses restent applicables dans les conditions de droit commun.')
q.append(p('Pour les exercices relevant du régime d’imposition à la distribution, le crédit est constaté au titre de l’exercice au cours duquel les dépenses ont été exposées et s’impute sur l’impôt sur les sociétés effectivement dû au titre de cet exercice, y compris à raison des distributions. L’absence de distribution ne diffère pas cette constatation et ne fait pas obstacle à la restitution de l’excédent, y compris lorsque l’impôt dû est nul, dans les limites et le champ temporel propres aux dispositions applicables au crédit. Les créances antérieures et leurs droits de mobilisation demeurent. Une même fraction ne peut donner lieu à une double imputation ou à un double remboursement ; en cas de cession, les droits de l’entreprise et du cessionnaire sont exercés selon les règles applicables à cette cession.'))
q.append(p('La suppression de l’agrément définitif et du reversement fondé sur sa seule absence s’applique aux crédits afférents aux dépenses exposées à compter de l’entrée en vigueur de la loi qui la prévoit et aux agréments définitifs restant à obtenir à cette date ; elle ne remet pas en cause les reversements devenus définitifs. Les agréments déjà délivrés restent valables et aucun dossier n’est à déposer de nouveau. L’agrément provisoire prévu au IV de l’article 220 sexies, les conditions culturelles et sociales, les plafonds et intensités d’aide et les délais d’achèvement ou de visa du quatrième alinéa du présent article demeurent. Les modifications du régime d’aide sont mises en œuvre dans le respect des exigences européennes d’exemption, de notification ou de compatibilité applicables, sans que le présent article vaille décision de la Commission européenne. Les dettes, créances, restitutions, prescriptions et recours antérieurs restent régis par leurs règles, sous réserve de la suppression prospective des formalités encore dues.'))
x = '\n'.join(q)
add(15, x,
    'Réduction de fond : retrait du second agrément national, définitif, qui reprend les conditions du II de 220 sexies déjà examinées à l’agrément provisoire. Le reversement pour simple défaut de ce titre ou retard de huit mois disparaît. L’éligibilité effective reste contrôlable et les reversements de fond ainsi que le délai de deux ans pour visa ou achèvement sont maintenus. Coordination du crédit et de sa restitution avec l’IS à la distribution, sans fermeture des créances.',
    'Les quatre alinéas officiels sont lus intégralement. 220 sexies, source, notes et proposition fournie, ont été lus en entier : l’agrément provisoire et la sélection culturelle restent au IV, les plafonds, dépenses, taux et intensités d’aide aux III, VI et VII ne sont pas modifiés ici. Le contrôle à l’achèvement reste nécessaire ; sa fonction est conservée au moyen des conditions matérielles et du contrôle fiscal existant, sans autorisation finale obligatoire de remplacement. Les règlements CNC et les articles réglementaires imposant le dossier d’agrément définitif doivent être coordonnés ; leur suppression n’est pas déclarée achevée. La modification d’une aide culturelle doit être confrontée au cadre européen et aux décisions de compatibilité applicables avant sa mise en œuvre ; les pièces locales ne permettent pas d’attester une nouvelle autorisation européenne. La note de 220 sexies issue de la loi du 19 février 2026 limite certaines dispositions aux sommes venant en déduction de l’impôt dû : ne pas étendre silencieusement une majoration réservée à l’imputation à la restitution. La réserve de champ temporel dans le nouveau texte préserve cette distinction sans inventer de ventilation absente du lot. L’ancienne note législative sur une compensation tabac n’est pas une recette nouvelle décidée par cette proposition. La production d’une œuvre n’autorise aucun nouveau CDD ni fin automatique du contrat unique ; les rémunérations, congés et indemnités de travail ne sont pas plafonnés par le crédit.',
    'material_reduction',
    'Un agrément définitif national et son risque de reversement pour seul défaut de délai sont effectivement retirés ; l’agrément provisoire, l’éligibilité réelle et le délai d’achèvement subsistent. L’adaptation à la distribution conserve le crédit, sans comptabiliser une seconde baisse d’IS.',
    'Le contrôle fiscal de l’œuvre et la coordination européenne demeurent indispensables. Les règles CNC extérieures ne sont pas entièrement réécrites et le gain net de coût administratif et budgétaire n’est pas établi.',
    'Aucune charge nouvelle propre n’est identifiée : le contrôle des conditions culturelles et des dépenses existait déjà et aucune déclaration, attestation ou autorisation de remplacement du titre final n’est créée. Une charge publique de contrôle peut subsister ; son coût net est inconnu.',
    effects=[
        effect('authorization_removed', 'cinema-credit-fin-agrement-definitif',
            'Suppression de l’agrément définitif supplémentaire et du reversement pour son seul défaut.',
            'Titre définitif CNC à obtenir sous huit mois après visa cinéma ou achèvement audiovisuel, à défaut reversement de la part du crédit.',
            'Aucun titre définitif exigé ; les conditions effectives du II restent contrôlées, et les deux ans pour visa/achèvement subsistent.',
            'legal_duty', 'Entreprises de production bénéficiaires du crédit de 220 sexies.',
            'Dépenses futures et agréments définitifs restant à obtenir ; titres acquis et reversements définitifs préservés ; exigences européennes réservées.',
            'Aucune déclaration ni attestation finale de remplacement ; agrément provisoire préexistant conservé.',
            plain(paras(S[15]['source_xml'])[2]),
            'Aucun agrément à titre définitif du président du Centre national du cinéma et de l’image animée n’est exigé au titre du présent article.'),
        effect('coordination', IS,
            'Conservation de la restitution du crédit sans distribuer des bénéfices.',
            'Excédent de crédit au titre de l’exercice de dépenses restitué selon le champ propre du crédit.',
            'Même restitution et même exercice, y compris si aucun IS ordinaire n’est dû faute de distribution.',
            'other', 'Entreprises bénéficiaires du crédit cinéma/audiovisuel dans leurs limites temporelles et matérielles.',
            'Exercices de distribution et créances antérieures, sous les limites légales particulières des montants imputables et remboursables.',
            'Pas de nouveau dossier ni remboursement en double ; cession CMF conservée.',
            "Si le montant du crédit d'impôt excède l'impôt dû au titre dudit exercice, l'excédent est restitué.",
            'L’absence de distribution ne diffère pas cette constatation et ne fait pas obstacle à la restitution de l’excédent, y compris lorsque l’impôt dû est nul, dans les limites et le champ temporel propres aux dispositions applicables au crédit.')],
    benefit='Le crédit de 220 sexies, l’imputation lors de l’exercice des dépenses, la restitution de l’excédent et la créance mobilisable dans les conditions L313-23 à L313-35 du CMF sont préservés, y compris pour les productions futures éligibles en contrat unique et sans distribution. Les taux, assiettes, catégories culturelles, plafonds et intensités de 220 sexies demeurent. L’absence d’agrément définitif ou le retard au-delà de huit mois ne peut plus, à elle seule, faire perdre le crédit ; les titres déjà acquis ne sont pas retirés. Les conditions de fond, l’agrément provisoire et les deux ans de visa ou d’achèvement restent pour empêcher un avantage sur une œuvre inéligible ou non achevée. La note de 2026 sur les seules sommes imputables interdit de présumer que toute majoration récente est remboursable ; la règle conserve le champ légal exact des remboursements sans le réduire ni l’élargir par inférence.',
    removed=['Agrément définitif national du CNC et son dossier propre attestant les conditions culturelles du II déjà examinées provisoirement.', 'Reversement du crédit fondé uniquement sur l’absence d’agrément définitif dans les huit mois du visa cinéma ou de l’achèvement audiovisuel.'])

credit_coord(16,
    'Pour les exercices relevant du régime d’imposition à la distribution, le crédit est constaté au titre de l’année au cours de laquelle l’entreprise a engagé les dépenses éligibles, selon les conditions de l’article 199 ter E. Il s’impute sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions. L’absence de distribution ne diffère pas la constatation du crédit et ne fait pas obstacle à la restitution de l’excédent prévue à ce même article, y compris lorsque l’impôt dû est nul. Les créances antérieures et les dépenses futures légalement éligibles conservent leur régime ; une même fraction ne peut être imputée ou remboursée deux fois.',
    'Coordination nécessaire du crédit d’impôt famille avec l’IS à la distribution. Le renvoi intégral à 199 ter E garde la restitution immédiate de l’excédent, sans introduire de délai lié au premier dividende ni modifier les dépenses éligibles.',
    '199 ter E officiel et proposé ont été lus dans le corpus, et la cible 244 quater F est lue intégralement avec sa note. Les taux de 50 % pour les établissements d’accueil et 25 % pour l’aide financière, la déduction des subventions, le plafond de 500 000 € et la répartition entre associés restent au champ de 244 quater F. Son 3 du I au taux de 10 % n’est applicable, selon la note, qu’aux dépenses exposées jusqu’au 31 décembre 2009 : les congés qui y sont cités ne rouvrent pas ce volet. Les autres dépenses futures éligibles ne sont pas fermées. Les congés parentaux et autres congés de travail conservent leur régime autonome, sans effet des quinze jours de préavis ni du seuil d’indemnité ordinaire.',
    'Le crédit famille conserve sa restitution malgré l’absence de dividende ; aucun taux social, congé ou indemnité de travail n’est modifié. L’article ne constitue pas une baisse nouvelle distincte.',
    'Le volet historique à 10 % demeure limité aux dépenses jusqu’en 2009 ; le crédit de 50 %/25 % et son plafond ne sont pas étendus. L’impact net des aides n’est pas chiffré.',
    ('Entreprises bénéficiaires du crédit famille et associés éligibles au titre de 244 quater F.',
     'Le crédit famille et sa restitution de l’excédent sont conservés sans distribution préalable. Restent les taux de 50 % sur la création et le fonctionnement des accueils d’enfants et de 25 % sur l’aide financière, leurs dépenses futures recevables, le plafond de 500 000 €, la déduction des subventions et les droits des associés éligibles. Le volet de 10 % du 3 du I de 244 quater F garde ses seuls effets historiques pour les dépenses exposées jusqu’au 31 décembre 2009 ; il n’est pas supprimé pour les litiges anciens ni rouvert pour de nouvelles dépenses.'))

credit_coord(17,
    'Lorsqu’une créance relevant du présent article subsiste au cours d’un exercice soumis au régime d’imposition à la distribution, l’absence de distribution ne modifie ni la date d’origine des cinq fractions annuelles prévues à l’article 199 ter I, ni la restitution de la fraction excédant l’impôt sur les sociétés effectivement dû. Les cas de reversement ou de cessation d’utilisation des fractions restent ceux de ce même article. Les droits et recours relatifs aux avances émises entre le 1er février 2005 et le 31 décembre 2009 demeurent, sans réouverture de cette période ni recommencement du délai d’imputation ; une fraction déjà utilisée ou restituée ne peut l’être de nouveau.',
    'Coordination nécessaire pour les seules créances et procédures survivantes du prêt à taux zéro ancien : la réforme de l’IS ne recommence pas l’échelonnement en cinq fractions ni ne bloque leur restitution à défaut de dividende. Aucun nouveau prêt éligible n’est créé.',
    '199 ter I a été lu en entier dans le corpus : un cinquième l’année du versement puis quatre fractions égales, restitution annuelle de l’excédent ; reversement en cas d’inéligibilité initiale, exception de ressources justifiées par l’emprunteur avec limite avantage majoré de 25 %, cessation des fractions en cas de changement d’affectation ou de remboursement anticipé, et possibilité contractuelle d’exigibilité. Les notes des deux articles bornent les avances émises du 1er février 2005 au 31 décembre 2009. L’ancienneté de la créance et les prescriptions restent déterminantes ; aucune créance contemporaine n’est présumée exister. La contribution de sécurité immobilière, les successions et les nouveaux prêts de régimes différents ne sont pas visés.',
    'Le calendrier historique et les restitutions éventuelles sont protégés contre une attente artificielle de distribution, sans recréer de fractions épuisées. Il s’agit d’une coordination, pas d’un nouveau report ni d’une taxe supprimée.',
    'Seules les créances anciennes encore légalement vivantes ou litigieuses sont couvertes. Aucune éligibilité nouvelle après le 31 décembre 2009 ni réouverture de prescription n’est décidée.',
    ('Établissements de crédit ou sociétés de financement titulaires d’une créance ancienne de 244 quater J.',
     'L’imputation par cinquièmes, la restitution de chaque excédent et les droits relatifs aux avances émises du 1er février 2005 au 31 décembre 2009 sont conservés selon 199 ter I. Le nouveau régime d’IS ne remet ni à zéro l’horloge ni en cause une fraction encore recevable ; il n’exige aucun dividende pour restituer. Les exceptions favorables à l’établissement prêteur lorsque la justification des ressources relève de l’emprunteur et les limites propres à ce recouvrement restent au renvoi. Aucun dispositif légalement échu n’est artificiellement renouvelé.'))

x = S[18]['source_xml'] + p('Pour les exercices relevant du régime d’imposition à la distribution, le crédit est constaté et imputé au titre de l’exercice déterminé par les deux premières phrases du présent article, sur l’impôt sur les sociétés effectivement dû, y compris à raison des distributions. L’absence de distribution ne diffère pas cette constatation et ne fait pas obstacle à la restitution de l’excédent prévue à la troisième phrase, y compris lorsque l’impôt dû est nul, dans les limites et le champ temporel propres au crédit défini à l’article 244 quater L. Les créances antérieures et les situations futures légalement éligibles conservent leurs droits ; aucune fraction ne peut être imputée ou remboursée deux fois et aucun exercice d’origine n’est recommencé.')
add(18, x,
    'Coordination nécessaire du crédit d’agriculture biologique avec l’IS à la distribution : maintien des deux calendriers d’exercice civil ou décalé et de la restitution de l’excédent. Aucun taux, montant ni critère de recettes biologiques n’est changé par cet article.',
    'La source entière et 244 quater L officiel du corpus ont été lus. Ce dernier prévoit 2011 à 2028, au moins 40 % de recettes éligibles, 4 500 €, cumul d’aides plafonné à 5 000 €, multiplication GAEC dans la limite de quatre, droits des associés et de minimis agricoles/pêche. Sa note issue du E du I de l’article 31 de la loi du 19 février 2026 réserve les dispositions de cette rédaction aux seules sommes en déduction de l’impôt dû ; 220 M conserve pourtant une restitution générale. Cette articulation préexistante exige de confronter la loi modificative pour ventiler exactement la fraction imputable et la fraction restituable ; aucun ancien montant, ni remboursement d’une majoration récente, n’est inventé. La réserve de champ légal dans la proposition signale cette limite sans supprimer la restitution qui subsiste. Le calendrier décalé est conservé exactement : exercice clos l’année suivant l’année de respect des conditions. Il n’est pas converti en exercice de première distribution. Les aides maintenues ne sont pas comptées comme économies du chiffrage IS.',
    'coordination_only',
    'Le crédit biologique conserve son exercice d’imputation et son droit à restitution dans son champ légal malgré une absence d’IS sur les bénéfices conservés. Aucun montant de crédit supplémentaire ni accélération distincte n’est créé.',
    'La restriction d’imputation de la loi de 2026 reste à articuler avec la restitution générale préexistante ; le lot ne prouve pas le montant remboursable de chaque cohorte. Les conditions et années de 244 quater L subsistent.',
    'Aucune charge nouvelle n’est identifiée : les éléments du mode biologique, des recettes et des aides étaient déjà nécessaires, et aucun dépôt ni registre distinct n’est créé pour suivre une distribution.',
    effects=[effect('coordination', IS,
        'Conservation du calendrier et de la restitution légalement disponible du crédit biologique.',
        'Imputation sur l’exercice civil ou sur l’exercice clos l’année suivante et restitution de l’excédent selon les dispositions applicables.',
        'Même exercice et même droit d’excédent, sans report jusqu’à distribution, sous le champ temporel propre du crédit.',
        'other', 'Entreprises agricoles à l’IS et associés titulaires du crédit de 244 quater L.',
        'Exercices du nouveau régime et créances antérieures ; restriction légale 2026 et cohortes maintenues sans inférence de montant.',
        'Aucun nouveau dépôt ; pas de crédit remboursé puis réimputé.',
        "Si le montant du crédit d'impôt excède le montant de l'impôt dû au titre dudit exercice, l'excédent est restitué.",
        'L’absence de distribution ne diffère pas cette constatation et ne fait pas obstacle à la restitution de l’excédent prévue à la troisième phrase, y compris lorsque l’impôt dû est nul, dans les limites et le champ temporel propres au crédit défini à l’article 244 quater L.')],
    benefit='Le crédit d’agriculture biologique, l’imputation pour les exercices civils et décalés et la restitution de l’excédent sont conservés pour toutes situations encore éligibles de 244 quater L, anciennes et futures jusqu’à ses échéances. Aucun critère de 40 %, montant de 4 500 €, limite cumulée de 5 000 €, régime GAEC ou droit d’associé n’est retiré ici. Les règles européennes de minimis restent au champ propre du dispositif. La note législative 2026 réservant certaines dispositions aux sommes imputées doit être ventilée avant de promettre un montant restituable ; la proposition maintient tout droit légal de remboursement sans inventer le remboursement d’une fraction qui n’y aurait pas droit et sans attendre un dividende.')

# Analyses de chaque cible obligatoire, sans cible de contexte supplémentaire.
CHECKS = {
    '217 undecies': {
        'L1234-1': 'Aucun alinéa de 217 undecies ne renvoie au préavis de L1234-1. Le III, 1, b vise un objectif de création ou maintien d’emplois pour l’aide outre-mer, non leur durée ou leur rupture. Le projet de préavis de quinze jours pour les nouveaux contrats et la conservation des anciens préavis ne modifient ni les cinq/sept/dix/quinze ans d’affectation des biens ni la rétrocession de l’aide ; la notification et les procédures protectrices restent dans le droit du travail.',
        'L1221-2': 'L’emploi visé au III est un critère matériel de l’investissement, non une autorisation de CDD. La source officielle L1221-2 admet encore des termes légaux ; sa proposition les ferme pour les nouveaux contrats. Aucun délai d’exploitation, de location ou de souscription de 217 undecies ne devient la durée du contrat de travail. Les nouveaux emplois éligibles en contrat unique gardent l’accès à l’aide ; les anciens contrats et créances restent à leur régime.',
        'L1234-9': 'La déduction fiscale, l’exigence de respect des obligations sociales et l’objectif d’emploi ne renvoient pas au barème d’indemnité de L1234-9. Le projet atteint un an au terme effectif, préavis inclus, puis 0,20 mois par année totale avec mois complets et plafond six mois ; les anciens droits et indemnités spéciales restent distincts. Ni ce seuil ni ce plafond ne sont transposés à l’avantage outre-mer, aux durées d’exploitation ou aux aides de futures embauches.'
    },
    '218': {
        '206': 'Le second alinéa de 218 vise exactement le 4 de 206 : part des commanditaires et des associés non indéfiniment responsables ou non identifiés de sociétés en commandite simple ou en participation. La cote au nom de la société ou du gérant connu des tiers reste cohérente. Le nouveau 12 de 206 fait relever le 4 du régime ordinaire de distribution, sans changer ce redevable ; le 5 patrimonial demeure distinct. Aucun renvoi de préavis ou d’ancienneté de travail n’existe ici.'
    },
    '218 bis': {
        '206': 'Le renvoi de 218 bis comprend les personnes morales passibles de l’IS mais exclut expressément celles du 5 de 206 ; cette exclusion est reproduite. Le projet de 206, 12 soumet les bénéfices ordinaires des 1 à 4 et 6 à 10 à la distribution et maintient le 5 dans son régime patrimonial. L’alinéa ajouté empêche donc que la part transparente rétablisse une annualité chez l’associé ordinaire, sans exonérer le 5 ou transférer son revenu à un autre régime. Aucune règle de contrat de travail n’est visée.'
    },
    '219 ter': {
        'L1234-1': 'Les indemnités de 219 ter réparent des actifs immobilisés ou stocks détruits par faits de guerre, sans rapport avec l’indemnité compensatrice de préavis de L1234-1. Le préavis proposé de quinze jours, sa notification et les anciens préavis plus favorables n’en déterminent ni le taux historique ni l’assiette. Aucun renvoi de travail ne doit être ajouté par rapprochement du seul mot indemnité ; les procédures collectives et protections spéciales restent inchangées.',
        'L1221-2': 'La règle de L1221-2 concerne le terme des contrats de travail privés ; 219 ter vise la fiscalité d’une indemnité de guerre attribuée à une entreprise. Il n’y a aucun contrat d’emploi à convertir dans cet article. Le maintien de taux historiques et la suppression de la demande distincte ne rouvrent aucun CDD et ne conditionnent pas l’avantage à l’embauche en contrat unique, ni ne ferment les droits des entreprises ayant d’anciens contrats.',
        'L1234-9': 'La source de L1234-9 fixe un droit de licenciement et son projet prévoit un an au terme effectif avec préavis inclus, puis 0,20 mois par année totale, mois complets et plafond six mois, avec transition des anciens droits et indemnités spéciales. Ces paramètres ne concernent pas les actifs ou stocks de guerre de 219 ter : aucune indemnité fiscale n’est ramenée à zéro avant un an et aucun plafond salarial n’est importé. L’inapplicabilité est liée à l’objet réel des deux normes.'
    },
    '220 F': {
        '220 sexies': 'Le renvoi du premier alinéa vise le crédit entier ; le troisième vise précisément les dépenses du III, 1 et les conditions culturelles du II. La proposition fournie de 220 sexies maintient l’agrément provisoire au IV et adapte le second alinéa du I : anciens CDD d’usage valables conservés, nouveaux emplois en contrat unique éligibles, sans terme lié à l’œuvre. Le nouveau 220 F retire seulement l’agrément définitif supplémentaire, garde le contrôle des conditions réelles et les deux ans de visa/achèvement. La note 2026 sur les sommes en déduction impose de vérifier la ventilation imputable/restituable ; aucun barème d’ancienneté ou d’indemnité de rupture n’est importé dans les dépenses éligibles.'
    },
    '220 G': {
        '244 quater F': 'Le renvoi de 220 G désigne tout le crédit famille : 50 % pour l’accueil des moins de trois ans, 25 % pour l’aide financière, plafond de 500 000 €, subventions déduites et parts des associés. La cible officielle seule, sans proposition, doit être distinguée d’une réforme. Son I, 3 à 10 % et ses renvois aux congés ne concernent, selon la note, que les dépenses jusqu’au 31 décembre 2009 ; les autres dépenses futures éligibles restent ouvertes. Les congés parentaux et garanties spéciales ne sont pas supprimés par les règles de rupture du contrat unique. L’article 220 G coordonne seulement l’imputation et la restitution sans attendre une distribution.'
    }
}

by_num = {a['number']: a for a in A}
by_num['218 A']['review_notes'] += ' Vérification facultative complémentaire : l’article 23 ter de l’annexe IV, source et proposition locales lues en entier, confirme le principal établissement, le service des impôts des entreprises étrangères en l’absence d’établissement et le lieu des immeubles, avec centralisation dans ce service en cas de pluralité de lieux. Ce renvoi reste opérant sans imposer une nouvelle démarche.'
by_num['220 B']['review_notes'] += ' Vérification facultative complémentaire de l’annexe III 49 septies L, source et proposition locales lues en entier : elle fixe seulement l’ordre d’imputation du CIR après les prélèvements non libératoires et les autres crédits. Cet ordre est maintenu ; ce texte ne fixe lui-même aucune annualité ni attente d’un dividende et n’appelle pas de nouveau gain à comptabiliser.'
by_num['217 duodecies']['reason'] += ' Le renvoi aux suppressions de procédure de 217 undecies les étend aux démarches restant à accomplir sous l’option historique, sans les compter comme une seconde mesure.'
by_num['217 duodecies']['substantive_impact']['effects'].extend([
    effect('coordination', OM,
        'Le régime ultramarin encore recevable ne rétablit pas les procédures nationales supprimées par 217 undecies.',
        'Renvoi de 217 duodecies aux conditions de 217 undecies, y compris agréments nationaux et option historique.',
        'Suppression des seules procédures nationales pour les démarches restant à accomplir, sans réouverture des conditions historiques d’éligibilité.',
        'other', 'Entreprises et opérations de 217 duodecies encore recevables dans les transitions de 2021.',
        'Démarches futures, y compris sous option pour la rédaction antérieure ; droits acquis et conditions européennes maintenus.',
        'Aucune déclaration de remplacement ; la demande historique parvenue en 2021 n’est pas effacée comme condition d’accès à la transition.',
        "peuvent, dans les mêmes conditions, bénéficier du régime prévu à l'article 217 undecies",
        'Les suppressions de procédure nationale prévues aux II quater, III et VIII de l’article 217 undecies s’appliquent aux démarches restant à accomplir pour ces opérations, même sous cette option, sans remettre en cause les conditions historiques d’éligibilité.'),
    effect('coordination', IS,
        'Les déductions encore recevables de 217 duodecies suivent la même utilisation unique dans les bases différées que 217 undecies.',
        'Déduction des bénéfices investis dans les conditions de 217 undecies et des voies transitoires historiques.',
        'Déduction et reprise au résultat de référence, sans double utilisation ni impôt ordinaire sur le seul bénéfice conservé.',
        'other', 'Bénéficiaires de 217 duodecies relevant du régime ordinaire de distribution.',
        'Exercices relevant du nouveau régime, en conservant les dates historiques d’éligibilité.',
        'Pas de nouveau registre ni d’obligation de distribuer ; même règle commune de suivi des déductions.',
        "peuvent, dans les mêmes conditions, bénéficier du régime prévu à l'article 217 undecies",
        'Les règles de constatation et d’utilisation sans double emploi des déductions et de leurs reprises dans le régime de distribution prévues au VII de l’article 217 undecies s’appliquent aussi aux opérations relevant du présent article, y compris en cas d’option pour la rédaction antérieure à la loi n° 2020-1721 du 29 décembre 2020 de finances pour 2021.')
])
by_num['219 ter']['substantive_impact']['effects'].append(
    effect('coordination', IS,
        'Le taux favorable de l’indemnité de guerre est conservé au moment où l’IS de distribution devient exigible.',
        'Taux historique favorable de l’exercice de déduction, appliqué à l’indemnité selon le système annuel officiel.',
        'Même taux favorable conservé dans la fraction correspondante du bénéfice, taxée seulement à sa distribution.',
        'other', 'Entreprises titulaires d’indemnités éligibles de guerre relevant du nouveau régime ordinaire.',
        'Exercices de distribution ; réserves déjà taxées, prescriptions et droits antérieurs conservés.',
        'Aucun nouveau taux, aucune déclaration ou demande de remplacement.',
        "au taux de l'impôt sur les bénéfices industriels et commerciaux ou de l'impôt sur les sociétés en vigueur lors de l'exercice",
        'Pour les exercices relevant du régime d’imposition à la distribution de l’article 219, le taux ainsi déterminé est conservé pour la fraction éligible du bénéfice et s’applique lors de sa distribution, sans impôt ordinaire sur sa seule conservation et sans seconde imposition de bénéfices déjà taxés.')
)
by_num['220 E']['substantive_impact']['effects'].append(
    effect('coordination', IS,
        'Conservation de la naissance annuelle de la réduction de mécénat sans obligation de distribuer.',
        'Réduction imputée sur l’IS de l’exercice de réalisation de la dépense.',
        'Même exercice de naissance, imputation sur l’IS effectivement dû et report conservé sans distribution imposée.',
        'other', 'Entreprises bénéficiaires de la réduction de mécénat relevant de l’IS à la distribution.',
        'Exercices de distribution ; les stocks non expirés bénéficient séparément de la fin de péremption.',
        'Aucune créance remboursable créée, aucune utilisation double et aucun dépôt distinct nouveau.',
        "La réduction d'impôt définie à l'article 238 bis est imputée sur l'impôt sur les sociétés dû au titre de l'exercice au cours duquel les dépenses ont été réalisées.",
        'Aucune distribution préalable n’est exigée pour constater ou conserver son report.')
)
for s in S:
    key = s['code_id'] + '|' + s['source_id']
    required = R['requirements'][key]
    a = by_num[s['number']]
    if required:
        a['reference_checks'] = []
        for target_key in required:
            t = R['targets'][target_key]
            a['reference_checks'].append(dict(target_key=target_key,
                view_sha256=t['view_sha256'], assessment=CHECKS[s['number']][t['number']]))

assert len(A) == 19
Path('answer.json').write_text(json.dumps(A, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(A), 'articles')
