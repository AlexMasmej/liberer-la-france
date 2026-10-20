import json
import re
from html.parser import HTMLParser
from pathlib import Path

S = json.loads(Path('source.json').read_text())
R = json.loads(Path('reference-targets.json').read_text())
BY = {s['number']: s for s in S}
ANSWER = []


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br', 'div', 'li', 'tr'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('p', 'div', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        self.parts.append(data)


def plain(xml):
    parser = Plain()
    parser.feed(xml or '')
    return ''.join(parser.parts).strip()


def paras(*texts):
    return ''.join('<p>' + t + '</p>' for t in texts)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, source_quote, proposed_quote, burdens=None):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens or 'Aucune obligation de remplacement ni charge nouvelle n’est instituée par cette mesure.',
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, xml, reason, notes, classification, assessment, limitations,
        burdens, effects, change=None, removed=None, scope=None, benefit=None):
    s = BY[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    a['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects)
    if change:
        a['change_type'] = change
        if change == 'full_repeal':
            a['repeal_policy_id'] = 'editorial_direction_2026_10_19'
            a['repeal_scope'] = scope
        elif change == 'normative_reduction':
            a['reform_policy_id'] = 'editorial_direction_2026_10_19'
            a['removed_provisions'] = removed
    if benefit:
        a['benefit_review'] = benefit
    ANSWER.append(a)


NO_NEW = 'Aucune charge nouvelle n’est identifiée : aucun registre, jeu de données, justificatif, autorisation ou délai supplémentaire n’est créé. Les obligations maintenues ont leur fondement propre ; aucun solde de l’ensemble des codes n’est chiffré.'
RELEVE = 'releve-mensuel-missions-supprime'
GARANT = 'garantie-financiere-mentions-repetitives'
UNIQUE = 'contrat-unique-duree-indeterminee'


add('D1251-3', paras(
    'La décision du conseil de prud’hommes rendue sur une demande de requalification d’un contrat de mission en contrat de travail à durée indéterminée, en application de l’article L. 1251-41, est exécutoire de droit à titre provisoire.',
    'Cette garantie s’applique aux demandes relatives aux contrats de mission conclus avant l’entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, même si la saisine ou la décision intervient après cette date. Elle s’applique également, dans le champ de l’article L. 1251-41 et de ses adaptations légales, aux demandes relatives à des emplois irrégulièrement conclus à durée déterminée après cette date. Elle n’autorise ni la conclusion ni le renouvellement d’un tel contrat.'
),
    'La seconde passe maintient l’exécution provisoire, nécessaire à l’effectivité du recours du salarié, et précise son articulation avec les anciens contrats et les emplois à terme irréguliers nouveaux. Il s’agit d’une coordination du contrat unique, sans suppression d’une formalité patronale ni réduction de l’indemnité de requalification. La seule réécriture de la phrase source n’est pas comptée comme un allègement.',
    'L1251-41 est fourni uniquement en source officielle : saisine directe du bureau de jugement, décision au fond dans un mois, indemnité d’au moins un mois de salaire à la charge de l’entreprise utilisatrice. Aucune de ces garanties n’est retirée. L1251-58-5, lu en entier dans le corpus public mais non fourni comme cible empreintée, adapte déjà L1251-41 aux lettres de mission : la portée de la requalification et la qualité d’employeur de l’utilisateur restent appréciées sur les fondements législatifs applicables, sans droit automatique créé contre tout utilisateur. L’indemnité de requalification et les réparations d’illégalité ne relèvent pas de l’indemnité ordinaire de L1234-9. Le préavis individuel ne supprime aucune autorisation ou procédure collective. La coordination législative des situations nouvelles doit accompagner l’entrée en vigueur ; aucune date future n’est inventée.',
    'coordination_only',
    'Par rapport à la source officielle entière, l’exécution provisoire reste obligatoire et aucun coût ou délai de procédure n’est supprimé. La proposition explicite seulement sa continuité dans le passage au contrat unique et le maintien du recours pour les emplois à terme irréguliers.',
    'Le champ de la requalification demeure celui de L1251-41 et de ses adaptations ; le présent règlement ne crée ni une relation d’emploi avec tout utilisateur ni un recours nouveau hors de ce champ. Aucun effet financier net n’est démontré.',
    NO_NEW,
    [effect('coordination', UNIQUE,
        'Préservation de l’exécution provisoire dans la transition du contrat unique, sans réduction supplémentaire revendiquée.',
        'Exécution provisoire de droit de la décision rendue sur la demande de requalification prévue à L1251-41.',
        'Même exécution provisoire ; ancienneté du contrat ou date postérieure du jugement ne ferme pas les recours légalement ouverts.',
        'legal_duty', 'Salariés intérimaires et entreprises parties à une demande relevant de L1251-41.',
        'Contrats antérieurs et emplois à terme irréguliers nouveaux, dans le champ législatif de la requalification.',
        "La décision du conseil de prud'hommes saisi d'une demande de requalification d'un contrat de mission en contrat de travail à durée indéterminée, en application de l'article L. 1251-41, est exécutoire de droit à titre provisoire.",
        'Cette garantie s’applique aux demandes relatives aux contrats de mission conclus avant l’entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, même si la saisine ou la décision intervient après cette date.')])


add('R1251-3-1', paras(
    'I. – Lorsque l’entreprise utilisatrice propose au salarié un contrat à durée indéterminée dans les conditions de l’article L. 1251-33-1, elle lui communique cette proposition par écrit. Aucune obligation de notification avant le terme de la mission ni de recours à un moyen donnant date certaine à sa réception n’est imposée par le présent article.',
    'II. – L’entreprise utilisatrice laisse au salarié un délai raisonnable pour examiner sa proposition et lui en indique l’échéance. Le silence ne vaut ni acceptation ni refus opposable pour l’ouverture du droit à l’allocation d’assurance.',
    '1° Abrogé.<br/>a) Abrogé.<br/>b) Abrogé.',
    '2° Abrogé.<br/>a) Abrogé.<br/>b) Abrogé.',
    '3° Abrogé.',
    'À compter de l’entrée en vigueur de la loi portant la présente réforme, aucun signalement à France Travail du refus exprès ou de l’absence d’acceptation de cette proposition n’est exigé. Sont supprimés le descriptif et les justifications à joindre, les mentions relatives au délai de réponse et à la date du refus, le délai d’un mois de signalement et le délai de quinze jours pour fournir des compléments. Aucun dépôt ou rattrapage n’est exigé sur ce fondement après cette date, même pour une proposition ou un refus antérieur. Aucune déclaration de remplacement n’est instituée.',
    'La restriction d’ouverture du droit à l’allocation d’assurance fondée sur deux refus de propositions de contrat à durée indéterminée cesse d’être opposable dans le champ de l’article L. 5422-1. Aucun nouveau refus ou retrait d’allocation ne peut être fondé sur cette restriction supprimée. Les recours et restitutions légalement ouverts demeurent applicables ; les décisions antérieures devenues définitives ne sont pas rouvertes par le seul effet du présent article. Les autres conditions de l’assurance chômage demeurent applicables.',
    'Ces dispositions s’appliquent aux propositions et aux transmissions effectuées à compter de l’entrée en vigueur de la loi portant la présente réforme, sans réfection des offres déjà régulièrement communiquées. Pour les contrats uniques conclus à compter de l’entrée en vigueur de la loi les instituant, la fin de la mission ne rompt pas l’emploi auprès de l’entreprise de travail temporaire. L’acceptation d’une embauche par l’entreprise utilisatrice ne dispense pas de régler cet emploi selon les règles de rupture et les dispenses favorables applicables.'
),
    'Les suppressions acquises du signalement des refus, de ses pièces et délais et de la restriction au chômage sont conservées. Coupe supplémentaire par rapport au brouillon : suppression de l’obligation réglementaire de notifier avant le terme et de donner date certaine à la réception. L’offre écrite et le temps raisonnable d’examen restent nécessaires à un choix effectif ; aucun refus tacite ne peut être imputé au salarié. La durée de la mission ne termine pas l’emploi nouveau.',
    'L5422-1 fourni supprime dans sa proposition le cinquième alinéa du I relatif aux deux refus en douze mois, pour les deux circuits CDD et intérim. La source officielle ne l’a pas encore supprimé : entrée en vigueur simultanée indispensable. L1251-33-1, lu intégralement dans le corpus mais non fourni comme cible empreintée, contient encore le signalement dans sa source et sa proposition locale : sa seconde phrase du premier alinéa doit être supprimée expressément, tandis que l’offre écrite demeure. Coordonner L1243-11-1/R1243-2 et l’arrêté de transmission sans prétendre les avoir réécrits dans ce lot ; leur contenu intégral n’est pas fourni ici. Les subdivisions I, II, 1° à 3° et a/b sont conservées. Le délai de quinze jours supprimé concerne la réponse de l’entreprise à France Travail, jamais le préavis individuel du contrat unique. Les données déjà reçues restent soumises aux règles de protection et de conservation. Les procédures collectives et les autres obligations du demandeur d’emploi restent distinctes.',
    'material_reduction',
    'La source entière impose une réception à date certaine avant le terme, puis une déclaration dématérialisée circonstanciée du refus et des compléments. La proposition retire ces formalités et coordonne la suppression de la restriction au chômage ; elle garde l’écrit et une réflexion effective. La seconde passe retire en outre les contraintes de notification encore maintenues dans le brouillon.',
    'La fermeture de droits et le signalement ont un fondement législatif : ils ne peuvent être écartés par ce seul règlement. La suppression doit être coordonnée avec L1251-33-1 et L5422-1. Ni toutes les conditions de chômage ni les règles de rupture ne sont supprimées.',
    NO_NEW,
    [effect('obligation_removed', 'offre-cdi-formalites-notification',
        'Retrait du mode de réception à date certaine et de l’obligation d’adresser l’offre avant le terme, en conservant l’écrit.',
        'Entreprise utilisatrice : notification de la proposition avant le terme du contrat de mission, avec date certaine de réception.',
        'Entreprise utilisatrice : proposition écrite sans mode de réception imposé ni obligation de notification avant le terme ; délai raisonnable d’examen maintenu.',
        'legal_duty', 'Entreprises utilisatrices proposant une embauche dans le champ de L1251-33-1 et salariés destinataires.',
        'Propositions effectuées après l’entrée en vigueur ; offres antérieures régulièrement communiquées sans réfection.',
        "elle notifie cette proposition au salarié concerné par lettre recommandée avec accusé de réception, par lettre remise en main propre contre décharge, ou par tout autre moyen donnant date certaine à sa réception, avant le terme du contrat de mission.",
        'Aucune obligation de notification avant le terme de la mission ni de recours à un moyen donnant date certaine à sa réception n’est imposée par le présent article.'),
     effect('coordination', 'refus-cdi-sans-signalement',
        'Retrait réglementaire du signalement et de ses annexes, en coordination avec la suppression législative du circuit et de la restriction au chômage.',
        'Refus exprès ou tacite : signalement à France Travail dans un mois, données sur emploi, lieu et refus, compléments sous quinze jours ; restriction législative possible après deux refus en douze mois.',
        'Aucun signalement, annexe ou rattrapage ; silence sans refus opposable ; restriction législative des deux refus supprimée avec la coordination de L5422-1.',
        'legal_duty', 'Entreprises utilisatrices, France Travail et salariés concernés par une proposition à l’issue d’une mission.',
        'Transmissions futures, y compris pour refus anciens ; pas de réouverture automatique des décisions définitives ; autres conditions d’assurance maintenues.',
        "En cas de refus exprès ou tacite du salarié dans ce délai, l'entreprise utilisatrice dispose d'un délai d'un mois pour informer l'opérateur France Travail de ce refus.",
        'À compter de l’entrée en vigueur de la loi portant la présente réforme, aucun signalement à France Travail du refus exprès ou de l’absence d’acceptation de cette proposition n’est exigé.')],
    change='normative_reduction', removed=[
        'Notification de la proposition obligatoirement avant le terme et par un moyen donnant date certaine à sa réception.',
        'Signalement dématérialisé du refus exprès ou tacite sous un mois, avec descriptif, justifications et toutes les mentions des 1° et 2°.',
        'Réponse obligatoire sous quinze jours aux demandes de compléments relatives au signalement et information de ses conséquences restrictives.',
        'Assimilation du silence à un refus opposable et circuit réglementaire de la restriction au chômage supprimée avec sa coordination législative.'
    ])


add('R1251-7', paras(
    'Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme.',
    'À compter de cette date, l’entreprise de travail temporaire n’a plus à établir ni à transmettre à France Travail le relevé spécial mensuel des contrats de mission. L’échéance avant le 20 de chaque mois, le relevé distinct par établissement utilisateur et la transmission de ce relevé aux services régionaux de contrôle cessent de s’appliquer. Aucun relevé résiduel, complément périodique, dépôt ou rattrapage n’est exigé sur ce fondement, y compris pour des missions ou périodes antérieures. Aucune déclaration de remplacement n’est instituée.',
    'Les droits au revenu de remplacement et les recours des salariés restent régis par leurs dispositions propres, pour les contrats antérieurs comme pour les situations futures éligibles. L’absence du relevé supprimé ne peut, à elle seule, faire obstacle à leur examen ou à leur ouverture ; les faits nécessaires peuvent être prouvés par les moyens légalement admissibles. Les obligations sociales et les contrôles disposant d’un fondement légal distinct demeurent applicables, sans habilitation nouvelle de collecte ou de communication de données.',
    'Les relevés déjà transmis restent soumis aux règles de conservation, de confidentialité, d’accès et de rectification applicables et n’ont pas à être refaits. Les droits et recours relatifs aux périodes antérieures sont préservés, sous réserve de l’application des dispositions répressives plus douces. La fin d’une mission exécutée dans le cadre du contrat unique à durée indéterminée ne rompt pas l’emploi et ne réduit ni la garantie mensuelle de rémunération ni la prise en compte des intermissions selon leurs règles propres.'
),
    'La seconde passe supprime tout le relevé spécial, et non plus seulement ses doubles saisies ou sa ventilation par établissement. Cette abrogation réglementaire coordonne la proposition actuelle d’abrogation de L1251-46. L’ancien brouillon résiduel avant le 20 est écarté. Les droits des salariés et les contrôles légalement autonomes demeurent, sans reconstitution du relevé par une extraction ou une confirmation périodique à la charge de l’employeur.',
    'L1251-46 fourni propose une abrogation complète, contrairement aux notes de l’ancien brouillon du présent article. La source officielle reste en vigueur : l’abrogation législative doit entrer en vigueur simultanément. R1251-8 et R1251-9 ainsi que R1255-3 et R1255-4 sont coordonnés dans ce lot. Les déclarations sociales existantes ne sont pas présentées comme contenant nécessairement toute donnée ancienne ; aucune DSN enrichie ou habilitation nouvelle n’est créée. Les notes source de 2009/2010 distinguent les anciennes transitions régionales et ultramarines ; celle de 2024 concerne France Travail. Elles ne fixent pas la date de la réforme, et l’abrogation ne crée aucune compétence territoriale. L1251-58-2/3 lus dans le corpus, non fournis comme cibles empreintées, conservent congés, ancienneté et garantie mensuelle entre missions. La suppression du relevé est une seule mesure avec L1251-46, non une seconde suppression de prélèvement.',
    'coordination_only',
    'La source entière organise un relevé spécial mensuel avant le 20, un document par établissement et sa circulation administrative. Tous ces éléments sont effectivement retirés. Ce résultat est la coordination réglementaire d’une seule mesure d’abrogation portée par L1251-46, sans double comptage du même reporting.',
    'La suppression requiert l’entrée en vigueur de l’abrogation législative de L1251-46. Les autres déclarations sociales, les preuves utiles aux allocations et les contrôles reposant sur leurs propres bases légales ne sont pas supprimés ; aucune économie nationale n’est chiffrée.',
    NO_NEW,
    [effect('coordination', RELEVE,
        'Abrogation du calendrier et du circuit réglementaires du relevé spécial supprimé à L1251-46.',
        'Entreprises de travail temporaire : relevé des contrats de mission avant le 20 de chaque mois, distinct par établissement utilisateur, puis transmission administrative.',
        'Aucun relevé spécial ni échéance mensuelle sur ce fondement ; déclarations et contrôles autonomes conservés.',
        'legal_duty', 'Entreprises de travail temporaire, France Travail et services régionaux destinataires.',
        'À compter de l’entrée en vigueur avec L1251-46, même pour des périodes antérieures sans rattrapage ; données déjà reçues protégées.',
        "Un relevé distinct est établi pour chaque établissement accueillant un ou des salariés mis à la disposition de l'entreprise.",
        'L’échéance avant le 20 de chaque mois, le relevé distinct par établissement utilisateur et la transmission de ce relevé aux services régionaux de contrôle cessent de s’appliquer.')],
    change='full_repeal', scope='Suppression intégrale du relevé spécial mensuel des missions, de son échéance avant le 20, de ses exemplaires par établissement et de son circuit de transmission, y compris les rattrapages futurs de périodes anciennes.')


add('R1251-8', paras(
    'Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme.',
    'À compter de cette date, le modèle et l’ensemble des mentions du relevé spécial des contrats de mission cessent d’être exigés sur le fondement du présent article. Cette suppression comprend les données relatives à l’entreprise utilisatrice, à ses établissements et aux lieux d’exécution, les identifiants, les données d’identité et de résidence, la nationalité, la qualification, les dates des missions et les rémunérations. Aucun formulaire, fichier, complément périodique ou dépôt de remplacement n’est imposé sur ce fondement. Aucun relevé ni complément n’est à établir ou à refaire après cette date, même pour des missions antérieures.',
    'Les relevés déjà transmis restent soumis aux règles de conservation, de confidentialité, d’accès et de rectification applicables. Les droits au revenu de remplacement et les recours restent ouverts dans les conditions qui leur sont propres, pour les situations antérieures comme pour les situations futures éligibles. L’absence du relevé supprimé ne peut, à elle seule, faire obstacle à leur examen ou à leur ouverture ; les faits nécessaires peuvent être établis par les moyens légalement admissibles.',
    'Les obligations de paie, les déclarations sociales, les contrôles et les informations du salarié disposant d’un fondement distinct restent applicables. La présente abrogation ne crée aucune habilitation de collecte ou de communication de données et ne permet pas de reconstituer le relevé périodique sur son seul fondement. Pour le contrat unique à durée indéterminée, la fin d’une mission ne vaut pas rupture de l’emploi ; la garantie mensuelle et les droits liés aux intermissions demeurent régis par leurs dispositions propres.'
),
    'Abrogation intégrale coordonnée avec L1251-46 et R1251-7 : le brouillon conservait encore un modèle facultatif et de nombreuses mentions résiduelles. La seconde passe supprime le relevé lui-même et donc toute sa liste de données, plutôt que de limiter la coupe au code postal et à la nationalité. Elle maintient les droits aux allocations, les pièces légalement admissibles et les obligations autonomes de paie et de protection des données.',
    'L1251-46 fourni propose l’abrogation du support législatif ; le R1251-7 fourni comme cible est encore l’ancien brouillon résiduel : sa contradiction est corrigée par son abrogation dans le présent answer.json. La source conserve bien Siret/Siren à titre facultatif ; aucune obligation nouvelle n’en est tirée. Les 1° et 2° et la dernière phrase sur les salaires sont tous supprimés avec la norme entière, sans omission masquée. Adapter ou abroger l’arrêté de modèle et ses circuits techniques, dont le texte n’est pas fourni : son contenu n’est pas réputé réécrit. R1255-4 est abrogé ici. Les bulletins et autres données légalement accessibles restent soumis à leurs propres règles ; ni exhaustivité de la DSN, ni ouverture de nouveaux accès ne sont présumées. Les garanties de L1251-58-2/3 ont été lues dans le corpus et restent distinctes. Pas de seconde réduction comptée pour ce règlement d’exécution.',
    'coordination_only',
    'La source officielle entière impose un modèle et des rubriques détaillées. La proposition supprime toutes ces prescriptions, y compris celles conservées dans le brouillon, comme conséquence de l’abrogation unique du relevé spécial. Elle ne supprime ni le salaire ni les déclarations sociales distinctes.',
    'L’effet suppose la coordination législative de L1251-46 et celle de l’arrêté de modèle. Les obligations issues d’autres régimes et les traitements déjà effectués demeurent régis par leurs bases propres ; aucun gain de coût global n’est établi.',
    NO_NEW,
    [effect('coordination', RELEVE,
        'Retrait intégral du modèle et des rubriques d’exécution du relevé spécial, sous la même mesure que L1251-46.',
        'Un modèle ministériel et les rubriques détaillées des 1°, 2° et de la rémunération s’imposent pour le relevé spécial ; Siret et Siren restent facultatifs.',
        'Aucun modèle ni rubrique de ce relevé n’est exigé ; les données nécessaires sur d’autres fondements gardent leur régime.',
        'legal_duty', 'Entreprises de travail temporaire et destinataires du relevé spécial.',
        'Transmissions futures, y compris au titre de missions anciennes, sans rattrapage ; données déjà reçues et recours protégés.',
        'Le relevé des contrats de mission est conforme à un modèle fixé par arrêté du ministre chargé du travail.',
        'À compter de cette date, le modèle et l’ensemble des mentions du relevé spécial des contrats de mission cessent d’être exigés sur le fondement du présent article.')],
    change='full_repeal', scope='Suppression de l’ensemble du modèle obligatoire et des rubriques nominatives, professionnelles, temporelles et salariales du relevé spécial des missions, avec fermeture des compléments et rattrapages sur ce fondement.')


add('R1251-9', paras(
    'Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme.',
    'À compter de cette date, l’entreprise de travail temporaire n’est plus tenue de délivrer l’information particulière relative à la communication des relevés spéciaux des contrats de mission supprimés. Aucune information, attestation ou confirmation nouvelle n’est exigée sur ce fondement, y compris à raison d’un relevé antérieurement transmis.',
    'Cette abrogation ne porte pas atteinte aux obligations autonomes d’information et aux droits d’accès, de rectification et de recours applicables à la protection des données personnelles. Les salariés conservent ces droits à l’égard des données contenues dans les relevés déjà transmis, auprès des organismes qui les détiennent. Les règles de conservation, de confidentialité et de traitement de ces données restent applicables. Aucune communication de données n’est autorisée par le présent article.',
    'Les informations relatives à d’autres traitements légalement maintenus demeurent dues sur leurs fondements propres. La suppression du relevé spécial et de son information particulière ne réduit ni les droits au revenu de remplacement, ni les droits liés aux contrats antérieurs, ni les garanties de l’emploi à durée indéterminée et des périodes entre missions.'
),
    'L’information particulière sur un circuit de transmission supprimé n’a plus d’objet propre. La seconde passe abroge donc cette obligation spéciale au lieu de conserver le brouillon qui annonçait encore le relevé. Les protections des données personnelles, notamment pour les relevés déjà reçus et les traitements légalement maintenus, subsistent sur leurs fondements autonomes : aucun droit du salarié n’est converti en avantage réservé au passé.',
    'Coordination avec l’abrogation proposée de L1251-46, lue dans reference-targets, et avec R1251-7/8 abrogés dans ce lot. Les 1° et 2° de la source ont été examinés en entier : ils concernent la communication du relevé et l’exercice des droits auprès de France Travail et du directeur régional. Le renvoi aux anciens articles 39 et 40 de la loi du 6 janvier 1978 et la dénomination DIRECCTE sont préexistants ; ils ne sont pas transportés dans un nouveau dispositif ni silencieusement présentés comme une concordance actuelle. La loi modifiée et le RGPD ne sont pas fournis intégralement dans ce dossier : leur mise en concordance extérieure demeure à vérifier, sans présumer la suppression de leurs obligations supérieures. Le texte préserve expressément les protections autonomes et ne supprime pas l’information due pour d’autres traitements. La note de juillet 2024 est historique. L’abrogation concerne la règle spéciale entière, pas les droits généraux qu’elle rappelait.',
    'coordination_only',
    'La source entière impose une information spéciale sur le relevé et rappelle des droits généraux. La proposition retire seulement cette couche spéciale devenue sans objet avec l’abrogation du relevé, tout en maintenant les protections autonomes des personnes et des données anciennes. C’est une coordination de la même mesure, pas une réduction indépendante des droits.',
    'Les obligations générales de protection des données restent applicables ; le lot n’en réalise pas l’audit complet. Les informations dues au titre d’autres déclarations ou traitements ne sont pas supprimées et aucun solde net national n’est démontré.',
    NO_NEW,
    [effect('coordination', RELEVE,
        'Suppression de l’information spéciale liée au seul circuit du relevé abrogé, avec sauvegarde des protections générales.',
        'Information des salariés de chaque établissement sur les destinataires du relevé nominatif et les droits d’accès et de rectification rappelés par la source.',
        'Aucune information particulière sur ce circuit supprimé ; information et droits relatifs aux données et traitements subsistants conservés sur leurs bases autonomes.',
        'legal_duty', 'Entreprises de travail temporaire, salariés et organismes détenant les relevés anciens.',
        'Dès l’entrée en vigueur de la suppression du relevé ; données historiques et droits d’accès/rectification protégés.',
        "L'entreprise de travail temporaire informe, par tout moyen, les salariés temporaires de chaque établissement :",
        'À compter de cette date, l’entreprise de travail temporaire n’est plus tenue de délivrer l’information particulière relative à la communication des relevés spéciaux des contrats de mission supprimés.')],
    change='full_repeal', scope='Abrogation de l’information réglementaire particulière des salariés concernant la transmission des relevés spéciaux supprimés ; maintien des obligations et droits autonomes de protection des données, y compris pour les relevés anciens.')


add('R1251-15', BY['R1251-15']['previous_draft']['proposed_xml'],
    'La seconde passe conserve la suppression matérielle déjà proposée : plus de nom, d’adresse du garant ou de référence légale à répéter sur tous les documents ; la référence légale n’est plus à afficher. Elle n’ajoute pas une reformulation à droit constant. Une coupe supplémentaire de l’identification visible du garant n’est pas retenue : cette information permet aux salariés et créanciers d’actionner directement une garantie essentielle en cas de défaillance, sans rechercher des documents dispersés. La garantie n’est ni diminuée ni remplacée par une déclaration.',
    'L1251-49 à L1251-52 et R1251-11 à R1251-29 ont été lus intégralement dans le corpus public, sans être fournis comme cibles empreintées pour cet article. La garantie couvre salaires, accessoires, indemnités, cotisations et certains remboursements ; ses règles de constitution et d’action sont distinctes de ces mentions. R1251-14 maintient attestation, disponibilité et transmissions ; R1255-5 demeure distinct. R1255-6 du présent lot supprime la sanction des mentions retirées et conserve celle de l’affichage limité au nom, à l’adresse et aux deux dates. Dans le portage, les mentions réellement exigibles par L1254-21/23 et la transition historique de L1254-15 sont coordonnées dans R1254-2 ; leurs dispenses législatives ne doivent pas être neutralisées. Aucun contrat antérieur n’est à refaire et aucun emploi à terme nouveau n’est autorisé par la citation des contrats de mission.',
    'material_reduction',
    'Par rapport à l’intégralité de la source officielle, disparaissent la mention générale répétée sur tous les documents et la référence légale affichée. Le nom, l’adresse et les dates du garant restent affichés dans chaque établissement. Le brouillon portait déjà cette réduction ; son maintien après seconde passe ne constitue pas une coupe supplémentaire.',
    'Les mentions ayant un fondement législatif propre et l’attestation de garantie ne disparaissent pas. La réduction concerne la documentation réglementaire générale, sans baisse du montant garanti, des cotisations ou des créances et sans chiffrage de coût global.',
    NO_NEW,
    [effect('obligation_removed', GARANT,
        'Suppression de la répétition du garant sur tous les documents et de la référence légale dans l’affichage ; identification visible maintenue.',
        'Tous les documents de l’entreprise de travail temporaire mentionnent nom, adresse et L1251-49 ; l’affichage reprend ces trois mentions et les deux dates.',
        'Aucune mention documentaire imposée par cet article ; affichage du nom, de l’adresse et des deux dates seulement, sous réserve des mentions législatives autonomes.',
        'legal_duty', 'Entreprises de travail temporaire et personnes consultant leurs documents ou établissements.',
        'Documents établis après l’entrée en vigueur, y compris pour contrats anciens ; aucune réfection ; garanties et recours préservés.',
        "Tous les documents concernant l'entreprise de travail temporaire, notamment les contrats de mise à disposition et les contrats de mission, mentionnent le nom et l'adresse de son garant ainsi que la référence à l'article L. 1251-49.",
        "Sans préjudice des mentions expressément prescrites par la loi, les documents de l'entreprise de travail temporaire, notamment les contrats de mise à disposition et les contrats de mission, ne sont soumis, au titre du présent article, à aucune obligation de mentionner le nom et l'adresse du garant ou la référence à l'article L. 1251-49.")],
    change='normative_reduction', removed=[
        'Mention obligatoire du nom et de l’adresse du garant et de la référence à L1251-49 sur tous les documents de l’entreprise.',
        'Répétition obligatoire de la référence légale L1251-49 dans l’affichage de garantie de chaque établissement.'
    ])


add('R1254-2', paras(
    'Les modalités de constitution et de mise en œuvre de la garantie financière prévues au paragraphe 2 de la sous-section unique de la section 3 du chapitre Ier du titre V du livre II de la première partie du présent code, dans sa partie réglementaire, s’appliquent aux entreprises de portage salarial, à l’exception des articles R. 1251-12, R. 1251-18 et R. 1251-25 à R. 1251-29, avec les adaptations suivantes :',
    '1° Les termes « entrepreneur de travail temporaire » et « entreprise de travail temporaire » désignent l’entreprise de portage salarial ;',
    '2° Pour l’application de l’article R. 1251-15, les documents concernés comprennent les contrats de travail de portage salarial et les contrats commerciaux de prestation de portage salarial. La dispense de mentions documentaires du premier alinéa de cet article leur est applicable, sous réserve des mentions demeurant exigibles en application des articles L. 1254-21 et L. 1254-23 et de leurs dispenses de répétition. Pour les contrats à durée déterminée antérieurs à l’entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, les exigences de l’article L. 1254-15 restent appréciées selon les dispositions transitoires qui leur sont applicables, sans réédition des contrats déjà régulièrement établis. Le nom et l’adresse du garant ainsi que les dates de prise d’effet et d’échéance de la garantie sont affichés de manière visible dans chaque établissement conformément au deuxième alinéa de l’article R. 1251-15 ;',
    '3° Pour l’application de l’article R. 1251-13, la masse salariale remplace le chiffre d’affaires ;',
    '4° Les références aux articles L. 1251-49, L. 1251-50, L. 1251-51 et L. 1251-52 désignent respectivement le I de l’article L. 1254-26, le II du même article, le III du même article et le I du même article.',
    'La dispense prévue au 2° s’applique aux documents établis à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris lorsqu’ils concernent des contrats antérieurs. Aucun document déjà établi n’est à refaire. La garantie, les créances couvertes et les recours demeurent régis par leurs dispositions propres. Pour les relations de travail nouvelles, l’emploi est à durée indéterminée ; la durée ou la fin d’une prestation commerciale ne termine pas cet emploi. Les anciens contrats conservent leur régime jusqu’à leur terme, sans possibilité de conclure ou de renouveler un contrat de travail à durée déterminée après l’entrée en vigueur du contrat unique.'
),
    'Coordination de la dispense documentaire de R1251-15 avec le portage, sans double comptage comme réduction nouvelle. La seconde passe corrige le brouillon qui traitait encore L1254-15 comme une liste applicable aux nouveaux contrats et ignorait la dispense de répétition désormais proposée au 8° de L1254-21. Les exceptions, les quatre adaptations et la masse salariale demeurent ; la garantie protège des créances essentielles, ce qui justifie de ne pas abroger son cadre de constitution et d’action.',
    'Toutes les règles R1251-11 à R1251-29 et L1251-49 à L1251-52 ont été lues dans le corpus, hors des cibles empreintées obligatoires : R1251-12 et son minimum de 8 % du chiffre d’affaires sont exclus ; les règles propres de montant du portage ne sont pas modifiées. L1254-26, lu intégralement, conserve le calcul sur masse salariale et son plancher annuel, ses quatre créances et cinq catégories de cautions. Les quatre correspondances du 4° sont conservées exactement ; le I correspondant à L1251-52 ne réintroduit pas la substitution du client car R1251-25 à R1251-29 sont exclus. L1254-15 fourni est proposé abrogé pour l’avenir ; son 1° i ne survit que pour les anciens CDD. L1254-21 I 8° fourni permet une communication écrite conservable sans répétition ; L1254-23 8°, lu dans le corpus mais non fourni comme cible empreintée, garde sa mention du garant. L1254-21 II exclut la rémunération générale des périodes sans prestation ; elle n’est pas créée ici. L1254-27 officiel, lu, ne contient plus de déclaration préalable, tandis que R1254-3/4 officiels la prescrivent encore : incohérence préexistante à traiter expressément dans ces articles non assignés, non prétendument purgée par ce lot.',
    'coordination_only',
    'La source applique au portage la réglementation de garantie de l’intérim par substitutions. La proposition applique la suppression des mentions répétées décidée à R1251-15 et respecte les dispenses législatives actuelles proposées, sans créer une autre baisse de garantie ou de prélèvement. Elle distingue les anciens CDD des nouveaux emplois sans terme.',
    'Les obligations législatives autonomes et les règles propres de calcul de garantie subsistent. Les déclarations résiduelles de R1254-3/4 restent une coordination non réalisée ici. Aucun salaire général d’interprestation ni baisse financière nette ne sont démontrés.',
    NO_NEW,
    [effect('coordination', GARANT,
        'Application au portage de la dispense des mentions réglementaires répétées, sans rétablir les listes ou répétitions législatives supprimées.',
        'Les contrats de portage et commerciaux entrent dans les mentions générales importées de R1251-15, en plus de leurs exigences législatives.',
        'La dispense de R1251-15 s’applique ; seules les mentions législatives réellement exigibles subsistent avec leurs dispenses et transitions ; affichage utile conservé.',
        'legal_duty', 'Entreprises de portage salarial, salariés portés et entreprises clientes.',
        'Documents futurs relatifs à des contrats anciens ou nouveaux ; L1254-15 réservé aux CDD antérieurs ; aucune réédition.',
        '2° Les mots : "les contrats de mise à disposition et les contrats de mission" sont remplacés par les mots : "les contrats de travail de portage salarial et contrats commerciaux de prestation de portage salarial" ;',
        'La dispense de mentions documentaires du premier alinéa de cet article leur est applicable, sous réserve des mentions demeurant exigibles en application des articles L. 1254-21 et L. 1254-23 et de leurs dispenses de répétition.')],
    change='normative_reduction', removed=[
        'Application au portage des mentions réglementaires répétées du garant sur tous les documents, désormais retirées à R1251-15.'
    ])


add('R1255-1', paras(
    'Le fait de conclure un contrat de mission ne comportant pas les mentions exigibles aux 2°, 4° et 5° de l’article L. 1251-16 est puni de l’amende prévue pour les contraventions de la troisième classe.',
    'À compter de l’entrée en vigueur de la loi portant la présente réforme, les dispenses de reproduction, de répétition et de clause particulière prévues à l’article L. 1251-16 s’appliquent à la détermination des manquements punissables. La seule absence de répétition d’une information déjà régulièrement communiquée dans les conditions de cet article ou d’une clause particulière dont cet article dispense ne constitue pas l’infraction prévue au premier alinéa. Le droit au rapatriement applicable sans clause particulière demeure garanti.',
    'La présente incrimination n’est pas étendue par analogie aux lettres de mission établies dans le cadre d’un contrat de travail à durée indéterminée. Elle n’autorise ni la conclusion ni le renouvellement d’un contrat de travail à durée déterminée après l’entrée en vigueur du contrat unique. Une lettre de mission ne peut instituer un nouvel essai ni mettre fin à l’emploi par la seule fin de la mission.',
    'Les contrats de mission conclus antérieurement restent appréciés selon les règles qui leur sont applicables, sous réserve des dispositions pénales plus douces. Les faits antérieurs non définitivement jugés bénéficient de celles-ci dans les conditions de l’article 112-1 du code pénal. Les peines relatives aux faits qui perdent leur caractère d’infraction cessent de recevoir exécution dans les conditions de l’article 112-4 du même code. Les droits à l’information, au rapatriement et à réparation, ainsi que les infractions ayant un fondement distinct, demeurent applicables.'
),
    'La seconde passe réduit expressément la portée de la contravention afin que le renvoi à L1251-16 ne punisse pas les répétitions et clauses particulières désormais dispensées. La classe de l’amende et la protection des informations encore exigibles sont conservées : qualification, essai effectivement stipulé et rapatriement ont une fonction substantielle pour le salarié. Aucune incrimination nouvelle des lettres de mission n’est créée par analogie. Cette adaptation coordonne une réduction documentaire déjà décidée au fond ; elle ne prétend pas supprimer toutes les obligations d’information.',
    'L1251-16 fourni distingue les 2° qualification, 4° essai éventuel et 5° rapatriement hors du territoire métropolitain. Sa proposition dispense de répétitions et rend le rapatriement directement applicable sans clause, sauf rupture de l’emploi à l’initiative du salarié ; les anciennes clauses restent appréciées selon leur transition. Le règlement ne doit ni recréer ces clauses ni effacer les droits substantiels. L1251-58-4/5 et L1251-14 lus en entier dans le corpus, non fournis comme cibles empreintées : la substitution législative de « lettre de mission » ne suffit pas à étendre par analogie R1255-1 ; L1251-14 est en outre exclu des missions sous CDI par L1251-58-4. Le renvoi au 4° de L1251-16 proposé doit être coordonné sur ce point : aucun essai de mission nouveau, essai unique de trois mois sans renouvellement pour l’emploi nouveau. Code pénal 112-1/112-4 non fourni dans les cibles ni dans les cinq codes : application temporelle à contrôler sur leur texte intégral, sans maintien artificiel d’une peine abolie ni remboursement automatique des amendes déjà payées. Exigences européennes de sanctions effectives et proportionnées à coordonner, sans conformité d’ensemble présumée.',
    'coordination_only',
    'Par rapport à la source officielle, la contravention ne peut plus viser les répétitions et clauses dont le texte de fond dispense ; les informations réellement exigibles restent protégées par la même classe d’amende. Cette limitation pénale accompagne la mesure documentaire de L1251-16 et ne compte pas comme une seconde suppression de formalités.',
    'Les anciens contrats et leurs clauses gardent leur régime sous réserve de la loi pénale plus douce. Le champ pénal des lettres de mission ne doit pas être étendu sans texte exprès ; l’efficacité globale des sanctions et la coordination européenne ne sont pas établies par cette seule disposition.',
    NO_NEW,
    [effect('coordination', 'missions-mentions-sans-doublons',
        'Neutralisation de la sanction documentaire lorsque le texte législatif dispense de répétition ou de clause particulière.',
        'Contravention de troisième classe pour omission des mentions visées aux 2°, 4° et 5° de L1251-16 dans le contrat de mission.',
        'Même classe pour les mentions restant exigibles ; aucune contravention pour une répétition ou une clause légalement dispensée, sans extension aux lettres de mission.',
        'legal_duty', 'Entreprises de travail temporaire et salariés concernés par les mentions de mission.',
        'Entrée en vigueur avec les dispenses de L1251-16 ; contrats anciens et faits antérieurs sous réserve de la loi pénale plus douce.',
        "Le fait de conclure un contrat de mission ne comportant pas les mentions prévues aux 2°, 4° et 5° de l'article L. 1251-16 est puni de l'amende prévue pour les contraventions de la troisième classe.",
        'La seule absence de répétition d’une information déjà régulièrement communiquée dans les conditions de cet article ou d’une clause particulière dont cet article dispense ne constitue pas l’infraction prévue au premier alinéa.')],
    change='normative_reduction', removed=[
        'Répression de la seule absence de répétition d’informations déjà régulièrement communiquées lorsque L1251-16 dispense de cette répétition.',
        'Répression de l’absence d’une clause particulière de rapatriement dans les situations où L1251-16 ouvre directement ce droit sans clause.'
    ])


PENAL_TRANSITION = 'Les faits antérieurs qui n’ont pas donné lieu à une condamnation passée en force de chose jugée bénéficient de la loi pénale plus douce dans les conditions de l’article 112-1 du code pénal. Les peines relatives aux faits qui perdent leur caractère d’infraction cessent de recevoir exécution dans les conditions de l’article 112-4 du même code. Les recours et restitutions légalement ouverts demeurent applicables ; aucune restitution générale des amendes déjà acquittées n’est instituée.'
PENAL_NOTES = 'La note source du 1er juillet 2024 est historique. Les articles 112-1 et 112-4 du code pénal ne figurent pas dans les cibles fournies : leur application temporelle doit être contrôlée sur les textes intégraux hors des cinq codes, sans maintien d’une répression abolie pour les affaires non définitives. La directive 2008/104/CE, notamment son article 10, appelle le maintien de sanctions effectives, proportionnées et dissuasives pour les droits substantiels ; son texte n’est pas fourni ici et la conformité d’ensemble n’est pas présumée. Les fraudes, entraves ou manquements ayant une base autonome conservent leur régime.'

for number, classe, wording, sourceq in [
    ('R1255-3', 'troisième', 'le défaut ou le retard de transmission à France Travail du relevé spécial des contrats de mission dans le délai de l’article R. 1251-7', "Le fait de ne pas fournir à l'opérateur France Travail, dans le délai prévu à l'article R. 1251-7, le relevé des contrats de mission, en méconnaissance des dispositions de l'article L. 1251-46, est puni de l'amende prévue pour les contraventions de la troisième classe."),
    ('R1255-4', 'deuxième', 'la transmission à France Travail d’un relevé spécial des contrats de mission non conforme aux prescriptions de l’article R. 1251-8', "Le fait d'adresser à l'opérateur France Travail un relevé des contrats de mission non conforme aux prescriptions de l'article R. 1251-8 est puni de l'amende prévue pour les contraventions de la deuxième classe.")
]:
    sentence = 'La contravention de ' + classe + ' classe réprimant ' + wording + ' est supprimée.'
    add(number, paras(
        'Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme.',
        sentence,
        PENAL_TRANSITION,
        'L’abrogation accompagne la suppression du relevé spécial. Aucun relevé, complément, dépôt tardif ou sanction de remplacement ne peut être exigé sur les fondements supprimés, y compris à raison de missions ou périodes antérieures. Les droits des salariés au revenu de remplacement, les règles de protection des données déjà reçues et les obligations ou infractions ayant un fondement distinct restent applicables.'
    ),
        'L’abrogation de la contravention autonome, déjà acquise dans le brouillon, est conservée et mise en cohérence avec la suppression entière du relevé spécial. Il ne subsiste donc ni sanction sans objet ni relevé résiduel présenté à tort comme maintenu. Cette coordination pénale fait partie de la même mesure que L1251-46 et R1251-7/8 ; elle n’est pas une seconde suppression de prélèvement. La transition plus douce protège les affaires antérieures dans son champ.',
        ('Pour le défaut ou retard, L1251-46 fourni est proposé abrogé et R1251-7 est abrogé dans ce lot ; sa cible empreintée conserve encore le calendrier avant le 20, qui ne doit plus être appliqué. ' if number == 'R1255-3' else 'Pour la non-conformité, R1251-8 est abrogé dans ce lot ; sa cible empreintée maintient encore des mentions résiduelles, en contradiction avec la proposition actuelle d’abrogation de L1251-46. ') + 'Les notes de l’ancien brouillon disant que la déclaration, la ventilation ou le modèle demeurent sont expressément écartées. La suppression pénale ne neutralise ni droits aux allocations ni obligations déclaratives distinctes. ' + PENAL_NOTES,
        'coordination_only',
        'La source officielle entière crée une contravention de ' + classe + ' classe attachée au relevé spécial. Elle est entièrement retirée, dans la même mesure de suppression du relevé ; aucune autre amende ni déclaration n’est instituée. Le brouillon avait déjà supprimé cette contravention, sans avoir encore coordonné la disparition totale du relevé.',
        'Les infractions distinctes, les droits substantiels et les déclarations sociales autonomes subsistent. L’effet sur les peines anciennes dépend des règles pénales temporelles ; aucune annulation générale des condamnations définitives ni économie nationale n’est revendiquée.',
        NO_NEW,
        [effect('coordination', RELEVE,
            'Suppression de la contravention de ' + classe + ' classe en exécution de l’abrogation du relevé spécial, sans double comptage.',
            'Entreprise de travail temporaire : contravention de ' + classe + ' classe pour ' + wording + '.',
            'Cette contravention est abolie ; aucune sanction de remplacement ; les infractions autonomes demeurent.',
            'legal_duty', 'Entreprises de travail temporaire poursuivies ou susceptibles de l’être sur ce seul fondement.',
            'Entrée en vigueur avec la réforme ; faits non définitivement jugés et peines cessant de s’exécuter dans les conditions du code pénal ; pas de remboursement général.',
            sourceq, sentence)],
        change='full_repeal', scope='Suppression intégrale de la contravention de ' + classe + ' classe réprimant ' + wording + ', avec application des règles pénales plus douces aux faits et peines antérieurs dans leur champ légal.')


add('R1255-6', BY['R1255-6']['previous_draft']['proposed_xml'],
    'La seconde passe conserve la suppression de l’amende pour les mentions documentaires retirées de R1251-15, et ne modifie pas le brouillon pour produire une variation de vocabulaire. La contravention de deuxième classe relative à l’affichage restant exigible est maintenue : l’identification immédiate du garant protège l’exercice des créances de salaire en cas de défaillance, contrairement à la répétition sur chaque document. Le renvoi est limité au contenu allégé et ne rétablit pas l’affichage de la référence légale.',
    'R1251-15 fourni et conservé dans ce lot dispense les mentions documentaires, mais maintient au deuxième alinéa le nom, l’adresse et les dates de prise d’effet et d’échéance de la garantie. Sa référence à L1251-49 n’est plus à afficher : aucune sanction de son absence ne peut subsister par renvoi. Les deux alinéas de sanction source gardent leur place, avec suppression de la première branche et maintien de la seconde dans son champ réduit. R1255-5, lu dans le corpus et non fourni comme cible empreintée, concerne l’attestation de R1251-14 et reste distinct. La garantie et ses bénéficiaires ne sont pas diminués. L’application de 112-1/112-4 du code pénal, non fournis, doit être contrôlée hors corpus ; pas de répression des faits dépénalisés ni remboursement automatique des amendes définitives déjà payées. Le régime des salariés portés et les mentions législatives propres du portage ne sont pas assimilés à cette seule contravention d’intérim.',
    'coordination_only',
    'La source entière punit les omissions sur les documents et les omissions d’affichage. La proposition retire la première branche et limite la seconde au contenu d’affichage maintenu par R1251-15. Elle coordonne cette unique simplification documentaire, sans prétendre supprimer toute sanction de garantie ou créer une baisse de cotisations.',
    'L’affichage utile et sa contravention de deuxième classe restent applicables ; l’attestation de garantie et les sanctions distinctes subsistent. La portée des règles pénales plus douces doit être vérifiée pour chaque affaire ancienne ; aucun solde financier global n’est établi.',
    NO_NEW,
    [effect('coordination', GARANT,
        'Retrait de l’incrimination des mentions générales supprimées, sans pénalisation d’une référence légale qui n’est plus à afficher.',
        'Contravention de deuxième classe pour omission des mentions sur les documents et pour manquement à l’affichage des coordonnées, de la référence légale et des deux dates.',
        'Aucune contravention documentaire sur ce fondement ; deuxième classe seulement pour l’affichage restant exigible du nom, de l’adresse et des deux dates.',
        'legal_duty', 'Entreprises de travail temporaire soumises à R1251-15.',
        'Entrée en vigueur avec la dispense documentaire ; application de la loi pénale plus douce aux faits et peines antérieurs dans son champ.',
        "Le fait de méconnaître les dispositions relatives à l'affichage des informations sur la garantie financière prévu au second alinéa de l'article R. 1251-15, est puni de la même peine.",
        "L'absence, sur les documents de l'entreprise de travail temporaire, du nom et de l'adresse du garant ou de la référence à l'article L. 1251-49 n'est pas punie au titre du présent article.")],
    change='normative_reduction', removed=[
        'Contravention de deuxième classe réprimant l’absence de mentions générales du garant et de référence légale sur les documents de l’entreprise.',
        'Application de la sanction d’affichage à la référence légale L1251-49 que le nouvel article R1251-15 ne rend plus obligatoire.'
    ])


add('D1272-1', paras(
    'La déclaration d’identification du salarié prévue à l’article D. 133-13-1 du code de la sécurité sociale comporte les informations suivantes, sous réserve des dispenses du présent article et de l’article D. 1272-4. Les données exactes et à jour déjà légalement disponibles auprès de l’organisme gestionnaire sont réutilisées ; l’employeur ne fournit que les informations manquantes ou modifiées et peut les corriger. Aucune attestation de non-changement ni transmission supplémentaire du contrat déjà valablement établi n’est exigée à ce titre.',
    '1° Les mentions relatives au salarié et à son embauche prévues aux 2° et 3° de l’article R. 1221-1, relatif à la déclaration préalable à l’embauche ;',
    '2° Les mentions relatives à l’emploi :',
    'a) Pour un contrat antérieur à l’entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, la nature du contrat et, s’il est à durée déterminée, son motif de recours et sa date de fin. Pour un contrat conclu à compter de cette entrée en vigueur, la durée indéterminée résulte de la loi et n’a pas à être déclarée à nouveau. Aucune durée de mission, de formation, de convention ou d’aide ne constitue un terme de l’emploi. Ces mentions ne permettent aucun nouveau contrat à durée déterminée ni renouvellement d’un tel contrat après cette entrée en vigueur ;',
    'b) La durée du travail ;',
    'c) La durée de l’essai éventuellement stipulé, uniquement lorsque la déclaration tient lieu de contrat de travail. Si un contrat distinct a été signé dans les conditions de l’article D. 1272-4, cette durée n’est pas déclarée à nouveau ;',
    'd) La catégorie et la nature de l’emploi ainsi que, le cas échéant, son niveau hiérarchique et son coefficient ;',
    'e) Le cas échéant, l’intitulé de la convention collective applicable ;',
    'f) Le montant de la rémunération et de ses différentes composantes, y compris les primes et accessoires de salaire lorsqu’il en existe ;',
    'g) Abrogé ;',
    'h) Le taux de cotisation au titre des accidents du travail et des maladies professionnelles, lorsque plusieurs taux s’appliquent dans l’établissement et que le taux applicable au salarié n’est pas déjà connu de l’organisme gestionnaire ;',
    'i) Les abattements applicables à l’assiette ou au taux des cotisations. L’organisme gestionnaire applique ceux dont les conditions sont établies par les données légalement disponibles ; les seuls éléments manquants nécessaires au bénéfice de l’avantage peuvent être complétés, sans nouvelle production des éléments déjà disponibles ;',
    'j) Le taux de cotisation de prévoyance spécifique au salarié, s’il existe et n’est pas déjà connu de l’organisme gestionnaire ;',
    'k) Le cas échéant, l’assujettissement au versement de transport, sans nouvelle indication si cette information est déjà légalement disponible auprès de l’organisme gestionnaire ;',
    'l) Abrogé ;',
    '3° La signature de l’employeur et, lorsque la déclaration tient lieu de contrat de travail, celle du salarié. La signature par le salarié d’un contrat distinct dans les conditions de l’article D. 1272-4 le dispense d’une seconde signature sur la déclaration.',
    'L’employeur transmet au salarié une copie de la déclaration d’identification dans les délais prévus par le présent code. La remise effective de cette copie par l’organisme gestionnaire, pour le compte de l’employeur et dans les mêmes délais, vaut transmission par l’employeur ; aucune seconde remise du même document n’est exigée.',
    'La rubrique générale relative aux particularités du contrat et l’indication autonome de première embauche sont supprimées. La suppression de ces rubriques ne ferme aucun avantage lié aux caractéristiques du contrat ou à la première embauche. L’organisme gestionnaire réutilise les données légalement disponibles permettant d’établir ces conditions ; les seuls éléments légalement nécessaires qui manquent peuvent être complétés, sans rubrique générale ou attestation supplémentaire de remplacement.',
    'Ces simplifications s’appliquent aux déclarations et remises effectuées à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris pour les contrats antérieurs, sans réfection des documents déjà établis. Elles ne modifient ni les taux des cotisations et contributions ni les garanties de prévoyance. Les abattements, exonérations, aides et dispenses restent ouverts aux situations futures éligibles de même objet dans le contrat unique, sous leurs autres conditions propres ; les droits antérieurs sont préservés. Aucun justificatif nouveau ne conditionne leur maintien du seul fait des simplifications du présent article.'
),
    'La seconde passe supprime en plus du brouillon la rubrique indéterminée des particularités du contrat et l’indication autonome obligatoire de première embauche ; leurs fonctions utiles éventuelles sont limitées aux conditions légales des avantages, sans formulaire de remplacement. Elle retire la redéclaration du caractère indéterminé des nouveaux emplois. Pour l’essai, elle explicite la dispense déjà attachée au contrat distinct signé selon D1272-4, sans la compter comme une nouvelle réduction. Les suppressions acquises de doubles saisies sont conservées ; la signature et la remise uniques sont rendues expresses. Les données de salaire, de temps de travail et de liquidation des cotisations restent nécessaires, sans changement de taux ni restriction des avantages.',
    'D1272-4 et R1221-1 fournis sont lus dans leurs sources et propositions. Le 1° importe seulement les 2° et 3° de R1221-1, pas son ancien 4° sur l’essai et la durée du contrat. D1272-4 dispense déjà les clauses signées à l’embauche : le réemploi ne suppose ni copie supplémentaire du contrat ni seconde signature du salarié. D133-13-1 CSS, lu intégralement dans le corpus mais non fourni comme cible empreintée, exige officiellement l’identification avant la première déclaration de rémunération ; sa proposition permet la transmission unique si les échéances d’embauche maintenues sont respectées. D1272-1 n’ajoute aucune étape ni ne diffère la déclaration préalable à l’embauche. D1272-2/3/5 et L1272-4/L1273-5 ont été lus hors cibles : les dispenses des dispositifs simplifiés et l’exclusion du guichet spectacle sont conservées ; D1272-5 n’appartient pas au lot et son 2° b doit être aligné pour ne pas rétablir la redéclaration d’essai, ses signatures et son volet étant déjà proposés intégrés à D1272-1. Les futurs CDD restent interdits ; l’essai stipulé du contrat nouveau relève de trois mois sans renouvellement, sans essai par mission. Le doublon source « d’identification du salarié » est retiré expressément. Le libellé ancien « versement de transport » est conservé dans son champ : concordance avec le versement mobilité à vérifier dans les textes extérieurs, sans hausse, extension d’assiette ou prélèvement nouveau. Les rubriques et leur ordre restent 1°, 2° a à l, 3° ; g/l demeurent des emplacements abrogés.',
    'material_reduction',
    'D1272-1 officiel énumère les mentions a à l, les deux signatures et la copie employeur, sous la dispense préexistante de clauses de D1272-4. La proposition retire les saisies déjà disponibles, deux rubriques autonomes et la redéclaration du CDI nouveau ; elle rend expresses la signature et la remise uniques. La dispense de redéclarer l’essai déjà valablement stipulé selon D1272-4 est une coordination, pas une coupe supplémentaire. Paie et avantages futurs sont conservés sans baisse de taux revendiquée.',
    'Les informations réellement manquantes nécessaires à la paie, à l’identité ou à un avantage restent à compléter selon leur fondement légal. Les dispenses n’élargissent pas le champ des dispositifs à des employeurs exclus. La coordination de D1272-5 et du CSS demeure nécessaire ; aucun solde net national n’est chiffré.',
    'Aucune charge nouvelle n’est identifiée : les données réutilisées doivent déjà être légalement disponibles et à jour ; la possibilité de compléter une condition d’avantage remplace des rubriques obligatoires sans créer de dossier, attestation, registre ou délai. La signature et la remise réellement nécessaires subsistent, sans prétendre chiffrer le solde de l’ensemble des codes.',
    [effect('obligation_removed', 'identification-salarie-rubriques-inutiles',
        'Suppression des rubriques générales de particularités contractuelles et de première embauche, sans fermeture des avantages qui pourraient en dépendre.',
        'Employeur utilisant la déclaration simplifiée : rubrique g sur les particularités et rubrique l sur la première embauche à renseigner s’il y a lieu.',
        'Rubriques g et l abrogées ; conditions des avantages appréciées avec les données disponibles et les seuls éléments légalement nécessaires manquants, sans rubrique de remplacement.',
        'legal_duty', 'Employeurs et salariés relevant de la déclaration simplifiée de D1272-1.',
        'Déclarations futures, y compris pour contrats antérieurs ; bénéfices futurs éligibles et droits antérieurs maintenus.',
        "g) Les particularités du contrat de travail s'il y a lieu ;",
        'La rubrique générale relative aux particularités du contrat et l’indication autonome de première embauche sont supprimées.'),
     effect('obligation_merged', 'identification-salarie-transmission-unique',
        'Réemploi des données et des clauses déjà établies, dispense de seconde signature du salarié et de seconde remise effective.',
        'Mentions de D1272-1 sous la substitution des clauses déjà prévue par D1272-4 ; signatures de l’employeur et du salarié, copie à transmettre par l’employeur sans règle expresse de remise unique dans cet article.',
        'Seules les données manquantes ou modifiées sont fournies ; clauses du contrat déjà signé non ressaisies ; signature du salarié seulement si la déclaration tient lieu de contrat ; remise effective par l’organisme pour l’employeur suffisante.',
        'legal_duty', 'Employeurs et salariés des dispositifs simplifiés et organismes gestionnaires dans leur champ légal.',
        'Déclarations/remises futures sans refaire les pièces anciennes ; mêmes délais de remise et mêmes conditions de validité du contrat.',
        '3° Signature de l’employeur et du salarié.'.replace('’', "'"),
        'La signature par le salarié d’un contrat distinct dans les conditions de l’article D. 1272-4 le dispense d’une seconde signature sur la déclaration.'),
     effect('coordination', UNIQUE,
        'Suppression de la durée d’emploi déclarée pour le contrat unique, sans rétablir un CDD par une durée de formation ou d’aide.',
        'La rubrique a exige la nature CDI ou CDD et, pour le CDD, le motif et la date de fin.',
        'Le CDI nouveau résulte de la loi sans redéclaration ; motif et date de fin restent réservés aux CDD conclus avant la réforme, sans nouveau renouvellement.',
        'legal_duty', 'Employeurs recourant aux dispositifs simplifiés et salariés nouveaux ou sous anciens contrats.',
        'Contrats nouveaux après entrée en vigueur ; règles des anciens CDD maintenues jusqu’à leur terme, avantages futurs éligibles conservés.',
        'a) La nature du contrat de travail : contrat à durée indéterminée ou à durée déterminée, avec, dans ce cas, indication du motif de recours et de la date de fin de contrat ;',
        'Pour un contrat conclu à compter de cette entrée en vigueur, la durée indéterminée résulte de la loi et n’a pas à être déclarée à nouveau.')],
    change='normative_reduction', removed=[
        'Rubrique obligatoire générale g relative aux particularités du contrat, sans identification d’une fonction autonome nécessaire.',
        'Indication autonome obligatoire l de première embauche, sans suppression des avantages et conditions de fond qui lui sont liés.',
        'Nouvelle saisie des données exactes et à jour légalement disponibles et des clauses déjà valablement signées selon D1272-4.',
        'Déclaration répétée du caractère indéterminé de l’emploi nouveau, désormais fixé par le régime légal du contrat unique.',
        'Seconde signature du salarié lorsque le contrat distinct est déjà signé et seconde remise lorsque la copie est effectivement remise par l’organisme pour l’employeur.'
    ],
    benefit='Le i) vise expressément les abattements d’assiette ou de taux : ils restent applicables et l’organisme les met en œuvre lorsque les données disponibles en établissent les conditions ; seuls les éléments manquants peuvent être complétés. Le l) peut permettre un avantage de première embauche : son abrogation comme rubrique obligatoire ne supprime ni l’avantage ni la possibilité d’en établir les conditions pour une embauche future. Le g) pouvait signaler des particularités ouvrant exonération, aide ou dispense : sa suppression est accompagnée d’une sauvegarde expresse de ces avantages et des compléments strictement nécessaires. Les taux AT/MP variables du h), la prévoyance du j) et l’assujettissement conditionnel du k) ne sont pas des prélèvements nouveaux : leur champ, leurs conditions, leurs éventuels allègements et les garanties demeurent. D1272-4 et les dispositifs CEA/TESE procurent déjà des dispenses de clauses ou formalités : elles sont conservées et les signatures/remises doublonnées sont retirées. Ni délai minimal d’emploi ni condition supplémentaire ne ferme ces bénéfices ; les futures situations du même objet restent éligibles dans le contrat unique sous les autres conditions légales, et les anciens droits restent protégés.')


# Analyses propres à chaque renvoi ; les vues de référence ne sont pas le droit en vigueur.
PREAVIS = {
    'D1251-3': 'L1234-1 proposé fixe quinze jours calendaires au licenciement du contrat nouveau, et conserve les règles des contrats anciens. Ce préavis ne remplace ni la décision prud’homale ni son exécution provisoire ; le délai de jugement de L1251-41 n’est pas un préavis.',
    'R1251-3-1': 'Les quinze jours du L1234-1 proposé concernent la rupture patronale du contrat nouveau après notification, pas l’acceptation d’une offre par l’utilisateur. La fin de mission ou le refus ne vaut pas rupture ; contrats anciens et procédures spéciales gardent leur champ.',
    'R1251-7': 'L1234-1 proposé règle le préavis patronal de quinze jours calendaires des contrats nouveaux ; son calendrier est distinct de l’ancienne échéance du relevé avant le 20. Abroger le relevé ne rompt aucun emploi et ne modifie pas les préavis des contrats antérieurs.',
    'R1251-8': 'Les dates de mission autrefois déclarées à R1251-8 ne déclenchent pas le préavis de quinze jours du L1234-1 proposé. Une rupture patronale reste distincte avec sa notification ; les anciens contrats conservent leur préavis et les protections collectives subsistent.',
    'R1251-9': 'L1234-1 proposé concerne la rupture de l’emploi nouveau, avec quinze jours calendaires de préavis patronal, non l’information sur les données de mission. La suppression de cette information spéciale ne dispense de notification de rupture ni pour les anciens contrats ni pour les nouveaux.',
    'R1251-15': 'L1234-1 proposé fixe le préavis patronal de quinze jours des contrats nouveaux et préserve les règles antérieures. La dispense de mentions du garant n’affecte ni ce préavis ni les créances qu’il peut produire et qui restent garanties selon leur régime propre.',
    'R1254-2': 'L1234-1 proposé vise le préavis de rupture patronale des contrats nouveaux, quinze jours calendaires après notification selon sa coordination. La fin de prestation n’y supplée pas. La garantie de portage et ses modalités ne changent ni les préavis anciens ni les procédures spéciales.',
    'R1255-1': 'Les quinze jours calendaires de préavis patronal du L1234-1 proposé ne sont ni une période d’essai ni une sanction documentaire. Le renvoi pénal à la durée d’essai ne rétablit aucun préavis par mission ; les contrats antérieurs gardent leurs règles de rupture.',
    'R1255-3': 'L1234-1 proposé fixe un préavis patronal de quinze jours pour l’emploi nouveau, distinct du délai de dépôt du relevé dont la sanction est abolie. Aucun préavis, notification ou protection de rupture n’est supprimé par cette dépénalisation ; anciens contrats réservés.',
    'R1255-4': 'La contravention de conformité du relevé n’est pas une règle de préavis. L1234-1 proposé maintient pour les emplois nouveaux quinze jours calendaires après notification dans le régime coordonné ; anciennes durées et procédures collectives restent à leur champ.',
    'R1255-6': 'L1234-1 proposé régit le préavis patronal de quinze jours pour les nouveaux contrats, avec notification distincte de la mission. La suppression de l’amende documentaire ne retire pas les créances de préavis couvertes selon leur régime ni les droits des anciens contrats.',
    'D1272-1': 'L1234-1 proposé règle quinze jours calendaires de préavis patronal pour le contrat nouveau, pas une date à préremplir lors de l’identification. Les délais de remise de la déclaration restent les leurs ; les droits de préavis des contrats antérieurs sont conservés.'
}

EMPLOI = {
    'D1251-3': 'L1221-2 proposé exclut tout nouveau terme d’emploi et tout renouvellement de CDD après l’entrée en vigueur, sans effacer les anciens contrats. La garantie de D1251-3 ne les autorise pas : elle reste attachée aux demandes légalement recevables, y compris contre un terme irrégulier nouveau.',
    'R1251-3-1': 'L1221-2 proposé impose le contrat unique aux embauches nouvelles. L’offre de l’utilisateur n’est donc pas une transformation automatique de l’emploi auprès de l’agence : le refus et la fin de mission ne le terminent pas. Les anciens contrats et leurs droits restent distincts.',
    'R1251-7': 'L1221-2 proposé interdit de confondre durée de mission et durée d’emploi. La suppression du relevé vaut pour les transmissions futures d’anciens ou nouveaux contrats, sans CDD nouveau ni renouvellement, et ne modifie pas le statut d’agents publics d’un éventuel utilisateur.',
    'R1251-8': 'L1221-2 proposé permet une mission limitée au sein d’un emploi indéterminé et protège les contrats antérieurs. L’abrogation des dates et rubriques du relevé ne crée pas une fin d’emploi par mission, formation ou aide, ni une nouvelle exception au contrat unique.',
    'R1251-9': 'L1221-2 proposé maintient l’emploi nouveau au-delà de la mission et les droits des contrats anciens. L’abrogation du relevé et de son information particulière ne ferme donc aucune protection des données aux nouveaux salariés ; les droits autonomes restent ouverts.',
    'R1251-15': 'L1221-2 proposé impose la durée indéterminée aux nouveaux emplois. La référence documentaire aux contrats de mission ne crée aucune faculté de nouveau CDD ; la garantie et la dispense documentaire concernent aussi les documents futurs relatifs aux anciens contrats.',
    'R1254-2': 'L1221-2 proposé interdit les nouveaux CDD de portage et leur renouvellement après réforme, sans transformer la durée commerciale en durée d’emploi. L’ancienne liste de L1254-15 garde seulement son champ transitoire ; les droits des contrats anciens et la garantie restent protégés.',
    'R1255-1': 'L1221-2 proposé réserve les contrats à terme à la transition des contrats déjà conclus. Le maintien de la contravention pour les mentions encore exigibles n’autorise aucun nouveau CDD et n’étend pas par analogie la sanction aux lettres de mission du contrat unique.',
    'R1255-3': 'L1221-2 proposé conserve les contrats antérieurs mais supprime les nouveaux emplois à terme. La disparition de l’amende de dépôt concerne tout relevé futur sur le fondement abrogé, sans créer de renouvellement de CDD ni retirer les droits d’un salarié en intermission.',
    'R1255-4': 'L1221-2 proposé distingue emploi indéterminé nouveau et mission limitée. La dépénalisation du relevé ne rend licite aucun nouveau CDD ; anciens contrats et droits aux allocations restent appréciés dans leurs champs propres, sans fin d’emploi déduite d’une date de mission.',
    'R1255-6': 'L1221-2 proposé s’applique aux emplois nouveaux, sans terme tiré d’une mission. La suppression des mentions générales et de leur amende ne retire aucune garantie aux contrats anciens ni futurs et n’autorise pas de nouveau contrat de mission à durée déterminée.',
    'D1272-1': 'L1221-2 proposé supprime les nouveaux CDD, y compris leur renouvellement après réforme. Le 2° a de D1272-1 réserve motif et terme aux CDD antérieurs ; le CDI nouveau n’est pas redéclaré et les dates de formation, mission, convention ou aide ne fixent pas sa fin. Les avantages futurs restent ouverts.'
}

INDEMNITE = {
    'D1251-3': 'L1234-9 proposé règle l’indemnité ordinaire patronale : seuil d’un an au terme effectif avec préavis, puis 0,20 mois sur toute l’ancienneté, fractions en mois complets, plafond six mois. L’indemnité de requalification d’au moins un mois prévue à L1251-41 et l’exécution provisoire sont distinctes et ne subissent ni ce seuil ni ce plafond.',
    'R1251-3-1': 'Le refus de l’offre de l’utilisateur n’est pas une rupture ouvrant l’indemnité ordinaire de L1234-9 proposé. Celle-ci exige une initiative patronale et un an au terme effectif avec préavis ; 0,20 mois sur toute l’ancienneté, prorata des mois complets, plafond six mois. Anciens droits, dommages et indemnités spéciales ne sont pas supprimés.',
    'R1251-7': 'L1234-9 proposé apprécie le seuil d’un an au terme réel de l’emploi, préavis inclus, pas à la fin d’une mission ni au dépôt du relevé. Toute l’ancienneté entre alors dans les 0,20 mois par an, mois complets et plafond six mois ; la suppression du relevé n’efface pas les anciens droits ni la preuve de l’ancienneté.',
    'R1251-8': 'Les dates de mission du relevé abrogé ne fixent pas le seuil de L1234-9 proposé : un an au terme effectif de l’emploi, préavis inclus, puis 0,20 mois sur toute l’ancienneté, prorata des mois complets, plafond six mois, initiative patronale. La preuve reste admissible autrement et les anciennes composantes sont conservées sans double compte.',
    'R1251-9': 'L1234-9 proposé concerne une indemnité ordinaire de rupture patronale, non le droit d’accès ou de rectification des données : un an au terme effectif préavis inclus, puis 0,20 mois sur toute l’ancienneté, mois complets et plafond six mois. L’abrogation de l’information spéciale n’affecte ni preuve des droits ni anciennes indemnités.',
    'R1251-15': 'La garantie de L1251-49 couvre les indemnités dans leur champ propre ; retirer les mentions répétées ne les réduit pas. L1234-9 proposé prévoit, pour la rupture patronale nouvelle, un an au terme effectif préavis compris, puis 0,20 mois sur toute l’ancienneté, mois complets et plafond six mois ; droits anciens et indemnités spéciales restent distincts.',
    'R1254-2': 'La garantie de portage conserve les indemnités légalement dues. L1234-9 proposé vise l’initiative patronale avec un an au terme effectif préavis inclus, puis 0,20 mois sur toute l’ancienneté, prorata des mois complets et plafond six mois. Fin de prestation et absence de prestation ne déclenchent pas seules cette indemnité ; anciens droits réservés.',
    'R1255-1': 'L1234-9 proposé ne régit ni l’amende de troisième classe ni les dommages pour information illicite : seuil d’un an au terme effectif préavis inclus, 0,20 mois sur toute l’ancienneté et plafond six mois pour la seule indemnité ordinaire patronale, prorata des mois complets. Rapatriement, salaires et droits anciens ne sont pas absorbés par ce barème.',
    'R1255-3': 'L1234-9 proposé ne se substitue pas à l’amende abrogée et ne conditionne pas les allocations à son seuil : l’indemnité ordinaire est patronale, zéro avant un an au terme effectif préavis inclus, puis 0,20 mois sur toute l’ancienneté, mois complets et plafond six mois. Anciens droits et réparations restent hors de cette dépénalisation.',
    'R1255-4': 'L1234-9 proposé ne transforme pas l’amende de non-conformité abolie en indemnité : un an au terme effectif préavis inclus, puis 0,20 mois sur toute l’ancienneté, prorata des mois complets et plafond six mois pour la rupture patronale ordinaire. Les anciens contrats, dommages et indemnités spéciales gardent leur régime.',
    'R1255-6': 'La branche documentaire dépénalisée ne réduit pas les indemnités couvertes par la garantie. L1234-9 proposé exige un an au terme effectif préavis inclus, puis 0,20 mois sur toute l’ancienneté, mois complets et plafond six mois pour l’initiative patronale ordinaire. Composantes anciennes sans double compte et indemnités spéciales restent préservées.',
    'D1272-1': 'L1234-9 proposé n’impose aucune donnée de rupture supplémentaire à l’identification : un an au terme effectif préavis inclus, 0,20 mois sur toute l’ancienneté dès ce seuil, prorata des mois complets et plafond six mois, employeur seul. Le retrait des rubriques g/l ne ferme ni anciens droits ni aides futures et ne soustrait pas la première année du calcul.'
}

SPECIFIC = {
    ('D1251-3', 'L1251-41'): 'La source officielle entière, seule vue disponible, prévoit la saisine directe du bureau de jugement, une décision au fond dans un mois et au moins un mois de salaire à la charge de l’utilisateur. D1251-3 maintient l’exécution provisoire de ces décisions sans supprimer ce délai ni confondre l’indemnité avec L1234-9. La coordination des lettres de mission est limitée au champ légal, non une requalification automatique contre tout utilisateur.',
    ('R1251-3-1', 'L5422-1'): 'Le cinquième alinéa du I officiel impose une restriction après deux refus en douze mois, avec exceptions ; la proposition le supprime pour L1243-11-1 et L1251-33-1. Le règlement retire donc signalement, pièces et délais sans supprimer les autres critères des I/II. Les recours anciens restent ouverts dans leur régime ; entrée simultanée requise, car la proposition n’est pas le droit en vigueur.',
    ('R1251-7', 'L1251-46'): 'La source législative impose encore le relevé et sa communication administrative ; la vue proposée les abroge entièrement, même pour les rattrapages futurs de périodes anciennes, sans reporting résiduel. R1251-7 est donc abrogé plutôt que maintenu avec réemploi DSN. Droits futurs au chômage, preuves admissibles et données déjà transmises restent protégés ; mise en vigueur législative simultanée indispensable.',
    ('R1251-8', 'R1251-7'): 'La vue fournie de R1251-7 est l’ancien brouillon : relevé résiduel avant le 20, regroupement et réemploi de données. Elle n’est ni la source officielle ni la version à retenir après l’abrogation proposée de L1251-46. Le présent lot abroge R1251-7 et R1251-8 ensemble, sans modèle résiduel ni nouveau calendrier ; anciens droits et garanties d’intermission restent préservés.',
    ('R1254-2', 'R1251-15'): 'La vue proposée dispense les mentions générales du premier alinéa, conserve au deuxième nom, adresse et deux dates affichés et dispense de refaire les documents anciens. Le 2° de R1254-2 importe cette coupe au portage, sans réintroduire la référence légale dans l’affichage ni supprimer les mentions législatives réellement exigibles avec leurs dispenses. C’est la même mesure documentaire, pas une deuxième réduction.',
    ('R1254-2', 'L1254-15'): 'Le 1° i officiel exige le garant dans le CDD de portage, mais la proposition abroge la liste pour les nouveaux emplois. R1254-2 ne peut plus la rendre applicable prospectivement : elle est réservée aux CDD antérieurs et à leurs droits sans réédition. Les durées aux 1° a et 2° c/d ne rétablissent aucun terme d’emploi nouveau ; garanties et informations autonomes demeurent.',
    ('R1254-2', 'L1254-21'): 'Le I 8° proposé dispense de répéter le garant déjà communiqué par écrit sur support conservable et exact ; R1254-2 respecte cette dispense au lieu d’exiger toujours une mention contractuelle. Le II reste sans rémunération générale des périodes sans prestation. Le I 5° conserve l’essai stipulé, trois mois sans renouvellement pour l’emploi nouveau, sans essai par prestation ; les anciens essais gardent leur régime.',
    ('R1255-1', 'L1251-16'): 'Les 2°, 4° et 5° portent sur qualification, essai éventuel et rapatriement hors métropole. La proposition dispense des répétitions et de la clause particulière de rapatriement, tout en conservant le droit sauf rupture de l’emploi par le salarié. R1255-1 limite donc l’incrimination aux mentions exigibles et ne l’étend pas aux lettres par analogie ; les anciens contrats restent sous leur transition et la loi pénale plus douce.',
    ('R1255-3', 'L1251-46'): 'L1251-46 officiel fonde encore le relevé, tandis que sa proposition le supprime entièrement et sauvegarde droits futurs au chômage et contrôles autonomes. L’amende de défaut ou retard de R1255-3 perd son support dans la réforme et est abrogée avec elle ; ce n’est pas une seconde déclaration supprimée. Les faits anciens suivent la loi pénale plus douce et aucune donnée nouvelle n’est exigée.',
    ('R1255-3', 'R1251-7'): 'Le R1251-7 fourni porte encore un relevé résiduel avant le 20, alors que L1251-46 proposé est entièrement abrogé. Le présent answer.json retire ce relevé et ce calendrier ; R1255-3 ne peut donc maintenir une contravention liée à ce délai. La cible empreintée décrit le brouillon antérieur, pas une obligation à rétablir pour les contrats anciens ou nouveaux.',
    ('R1255-4', 'R1251-8'): 'La source officielle impose modèle et toutes les données ; la vue proposée conserve encore un modèle facultatif et certaines rubriques. Le présent lot remplace cette vue par l’abrogation entière, en cohérence avec L1251-46. L’amende de deuxième classe de non-conformité est abrogée sans reconstituer les mentions pour les anciens mois ; données reçues et droits autonomes sont conservés.',
    ('R1255-4', 'L1251-46'): 'Le L1251-46 proposé abroge l’établissement et la transmission du relevé spécial, et non les droits au chômage ou les contrôles légalement autonomes. R1255-4 est donc une coordination pénale de cette suppression unique. La source officielle maintient encore le relevé : la mise en vigueur législative et réglementaire doit être conjointe, avec loi pénale plus douce pour les faits antérieurs.',
    ('R1255-6', 'R1251-15'): 'Le premier alinéa proposé de R1251-15 dispense les mentions générales sur les documents ; le deuxième ne maintient que nom, adresse et dates d’effet/échéance visibles, sans référence légale. R1255-6 retire la sanction documentaire et ne punit que cet affichage réduit. Les documents antérieurs ne sont pas à refaire, et les faits dépénalisés suivent la loi pénale plus douce sans restitution générale automatique.',
    ('D1272-1', 'R1221-1'): 'Le 1° de D1272-1 renvoie exactement aux 2° identité et 3° date/heure d’embauche de R1221-1, pas à l’ancien 4° sur l’essai ou la durée du contrat. La proposition cible retire notamment APE et essai de la DPAE, sans supprimer ces 2°/3°. Le réemploi évite leur ressaisie ; aucune durée de mission ne devient un terme d’emploi nouveau et les anciennes déclarations n’ont pas à être refaites.',
    ('D1272-1', 'D1272-4'): 'D1272-4 officiel substitue déjà les clauses du contrat signé à l’embauche aux mentions correspondantes ; sa proposition explicite l’absence de seconde saisie et la transition des CDD antérieurs. D1272-1 respecte ce champ et dispense la seconde signature ainsi que la redéclaration d’essai, sans demander une nouvelle copie du contrat. Les données nécessaires manquantes et la remise effective au salarié demeurent, sans nouveau CDD.'
}

TARGET_BY_NUMBER = {v['number']: (k, v) for k, v in R['targets'].items()}
for a in ANSWER:
    n = a['number']
    checks = []
    for key in R['requirements'][a['code_id'] + '|' + a['source_id']]:
        target = R['targets'][key]
        tn = target['number']
        if tn == 'L1234-1':
            assessment = PREAVIS[n]
        elif tn == 'L1221-2':
            assessment = EMPLOI[n]
        elif tn == 'L1234-9':
            assessment = INDEMNITE[n] + ' La vue conserve aussi l’exception de faute grave et les indemnités conventionnelles ou contractuelles plus favorables ; le présent article ne les étend ni ne les supprime.'
        else:
            assessment = SPECIFIC[(n, tn)]
        checks.append(dict(target_key=key, view_sha256=target['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

Path('answer.json').write_text(json.dumps(ANSWER, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(ANSWER)}, ensure_ascii=False))
