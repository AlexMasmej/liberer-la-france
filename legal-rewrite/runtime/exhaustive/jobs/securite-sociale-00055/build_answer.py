import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


class TextOnly(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'br', 'div', 'li', 'tr'):
            self.parts.append(' ')

    def handle_endtag(self, tag):
        if tag in ('p', 'div', 'li', 'tr'):
            self.parts.append(' ')

    def handle_data(self, text):
        self.parts.append(text)


def plain(xml):
    p = TextOnly()
    p.feed(xml or '')
    return re.sub(r'\s+', ' ', ''.join(p.parts)).strip()


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def retained(number, reason, review, assessment, limits, burdens, benefit=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(
        proposed_xml=None,
        reason=reason,
        review_notes=review,
        status='retained_unchanged',
        classification='retained_necessary',
        substantive_impact={
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burdens,
            'effects': [],
        },
    )
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out
    return out


def draft(number, xml, reason, review, classification, assessment, limits, burdens, effects,
          removed=None, benefit=None):
    a = by_number[number]
    out = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    out.update(
        proposed_xml=xml,
        reason=reason,
        review_notes=review,
        status='rewrite_draft',
        substantive_impact={
            'version': 1,
            'classification': classification,
            'assessment': assessment,
            'scope_limitations': limits,
            'new_burdens_review': burdens,
            'effects': effects,
        },
    )
    if removed:
        out.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if benefit:
        out['benefit_review'] = benefit
    answers[number] = out
    return out


def effect(kind, measure, description, before, after, unit, population, transition,
           replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


retained(
    'L357-10-1',
    "Maintien intégral nécessaire : l'article ouvre aux titulaires des pensions locales de veuf ou de veuve la majoration forfaitaire régie par L. 353-5. Son retrait supprimerait un avantage familial et non une taxe ou une démarche redondante. Aucun nouveau corps à droit constant n'est produit.",
    "L. 353-5 et D. 357-2-1 ont été lus dans le corpus public : majoration pour enfant à charge, conditions propres de non-cumul, revalorisation et âge local de cinquante-cinq ans. La prestation ne se confond ni avec un capital successoral taxable ni avec l'indemnité de rupture. L. 353-5 conserve ses conditions propres ; aucune clôture des demandes futures recevables n'est créée.",
    "La source entière est conservée : maintien du droit à la majoration forfaitaire et de son articulation avec L. 353-5, sans réduction nouvelle de prélèvement ni de formalité.",
    "Le montant et les conditions de la majoration restent ceux des textes auxquels la source renvoie ; aucun élargissement aux personnes hors du régime local ni gain budgétaire n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : aucun formulaire, justificatif, délai ou condition supplémentaire n'est introduit par ce maintien intégral.",
    "La majoration forfaitaire de la pension locale est préservée avec ses conditions d'âge et celles de L. 353-5, notamment pour les enfants à charge. Elle reste accessible aux futures demandes éligibles ; elle n'est ni abrogée ni réservée aux seuls bénéficiaires actuels."
)

retained(
    'L357-10-2',
    "Maintien intégral nécessaire : le renvoi à L. 353-6 étend une majoration de réversion aux pensions locales. Il ne crée pas de cotisation accessoire ou d'autorisation individuelle. Le retirer ferait perdre une protection de revenu aux survivants modestes.",
    "L. 353-6 a été lu entièrement : âge du taux plein, plafond de l'ensemble des pensions françaises, étrangères et d'organisations internationales, majoration proportionnelle, écrêtement du seul dépassement et liquidation préalable des avantages. Cette dernière condition permet de vérifier le plafond global ; elle n'est pas ici remplacée par une nouvelle attestation. Les droits futurs dans le champ local demeurent ouverts.",
    "La source conserve la majoration sous plafond des pensions de veuf ou de veuve ; aucun allègement nouveau n'est compté pour la simple conservation de cet avantage.",
    "La condition de liquidation des pensions et le plafond du texte cible sont maintenus pour l'équité de l'avantage ciblé ; leurs modalités réglementaires ne sont pas réécrites dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : la proposition ne crée ni dépôt supplémentaire ni modification des données nécessaires au calcul du plafond.",
    "La majoration de L. 353-6 et son écrêtement limité au dépassement du plafond restent applicables aux pensions locales, pour les bénéficiaires actuels et futurs éligibles. Aucun taux réduit, dispense ou complément de pension n'est supprimé."
)

retained(
    'L357-11',
    "Maintien intégral nécessaire : l'article garantit aux survivants une pension calculée à partir de l'invalidité du défunt, y compris l'invalidité théorique. Les conditions particulières de la loi du 20 décembre 1911 délimitent le droit ; leur suppression indifférenciée modifierait ce régime de solidarité sans coordination de ses montants.",
    "L. 357-2, L. 357-8 et D. 357-20 ont été lus : âge de référence, minimum d'invalidité et fraction égale à la moitié. Le renvoi à l'article 1258 du code local est conservé dans son champ historique ; son texte intégral n'est pas fourni par le corpus consulté, ce qui ne permet pas d'affirmer la suppression de ses critères. Aucune condition d'ancienneté du contrat unique n'est ajoutée.",
    "Le calcul de pension sur la base d'invalidité et les deux voies d'accès du régime de 1911 sont conservés ; cet article ne comporte pas de prélèvement ou de rapport périodique à supprimer.",
    "Le régime ancien et ses critères d'incapacité ne sont pas remplacés par le régime de rupture du contrat de travail ; aucune extinction démographique du droit n'est présumée.",
    "Aucune charge nouvelle n'est identifiée : les mêmes conditions d'âge ou d'incapacité demeurent, sans nouveau certificat, délai minimal ou autorisation.",
    "La pension du survivant fondée sur l'invalidité réelle ou théorique du défunt demeure entière. Les ouvertures de droit ultérieures relevant des régimes locaux restent possibles ; le maintien de critères historiques ne réserve pas l'avantage aux seules pensions déjà liquidées."
)

retained(
    'L357-12',
    "Maintien intégral nécessaire : l'article protège les droits de réversion locaux par des règles historiques expressément figées et par l'assimilation du conjoint divorcé. Le décret d'adaptation est utile au service de ces droits et ne constitue pas un agrément à demander au bénéficiaire.",
    "L. 161-23, L. 353-1 et L. 353-3 actuels ainsi que D. 357-22 à D. 357-24 ont été lus. Le premier alinéa vise expressément la rédaction antérieure à la publication de la loi du 21 août 2003 : il ne doit pas être lu comme un renvoi aux alinéas actuels de L. 353-1. Cette version historique complète n'est pas jointe au corpus consulté ; aucune reconstruction de ses ressources ou minima n'est prétendue. L'application aux pensions prenant effet à compter du 1er juillet 2004 reste entière. Le partage et l'accroissement des parts du conjoint divorcé ne sont pas supprimés.",
    "La protection historique des pensions locales et les droits des conjoints divorcés restent intégralement maintenus ; aucun gain de simplification n'est attribué à cette conservation.",
    "Le renvoi historique est conservé avec sa date et ses alinéas exacts, sans substitution de la version actuelle. La concordance historique externe complète reste une limite documentaire identifiée.",
    "Aucune charge nouvelle n'est identifiée : le maintien ne crée ni demande, ni nouveau délai d'instruction, ni condition supplémentaire pour le conjoint divorcé.",
    "Le rétablissement éventuel du droit après remariage, les garanties historiques de calcul et les droits du conjoint divorcé restent fondés sur les renvois conservés. Les pensions prenant effet après le 1er juillet 2004 et toutes les situations ultérieures recevables demeurent couvertes."
)

retained(
    'L357-13',
    "Maintien intégral nécessaire : le calcul sur l'invalidité théorique lorsqu'elle est supérieure à la vieillesse du défunt est une garantie de montant pour le survivant. L'article ne contient aucune charge fiscale, autorisation ou déclaration autonome à retrancher.",
    "La comparaison entre pension de vieillesse et pension d'invalidité se fait au moment où la première pension a pris effet ; cette référence temporelle n'est pas déplacée au décès. La base la plus favorable prévue par la source reste applicable aux liquidations et révisions recevables, sans condition nouvelle.",
    "La base d'invalidité plus favorable de la pension de veuve ou de veuf est conservée sans changement de calcul ; aucune baisse de prélèvement n'en résulte.",
    "L'article ne fixe pas les taux des pensions d'invalidité ni de réversion ; ils ne sont ni inventés ni modifiés et aucune extension hors des régimes locaux n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : le maintien de la comparaison existante n'ajoute ni pièces, ni attestation, ni délai pour le survivant.",
    "Le remplacement favorable de la base vieillesse par la base d'invalidité théorique reste garanti lorsque les conditions de comparaison sont réunies, pour les dossiers futurs aussi bien que les droits antérieurs. Aucun plafonnement supplémentaire n'est ajouté."
)

retained(
    'L357-14',
    "Maintien intégral nécessaire : l'attribution de l'appréciation de l'inaptitude à la caisse d'Alsace-Moselle et le recours devant les juridictions de sécurité sociale assurent un examen identifiable et une contestation effective. Il ne s'agit pas d'une autorisation de licenciement ni d'un contrôle professionnel redondant.",
    "Le 4° de L. 142-1 vise effectivement l'état d'inaptitude au travail dans le contentieux social. Les trois cibles du code du travail ne sont pas des renvois du présent article et n'en changent pas le champ. La note source de l'article 96, VII de la loi du 23 mars 2019, applicable aux recours introduits au plus tard à partir du 1er janvier 2020, reste distincte de toute réforme future. Aucun nouveau délai de quinze jours n'est introduit.",
    "La compétence de la caisse et l'accès au juge sont conservés ; retirer ces règles ne supprimerait pas une taxe mais fragiliserait l'instruction et les recours des assurés.",
    "L'appréciation de l'inaptitude pour une pension locale reste distincte de l'inaptitude professionnelle et des indemnités de rupture ; aucun changement de juridiction ou d'ancienneté n'est opéré.",
    "Aucune charge nouvelle n'est identifiée : l'article demeure exactement en vigueur dans la proposition, sans expertise, autorisation ou justificatif additionnel."
)

retained(
    'L357-15',
    "Maintien intégral nécessaire : la règle articule les avantages de L. 357-3 en cas de coexistence d'une pension personnelle et d'une pension de survivant, tout en conservant expressément la seconde pension. Aucun prélèvement ni dépôt administratif autonome n'est institué ici.",
    "L. 357-3 renvoie effectivement à la majoration pour enfants de L. 351-12 et au seul premier alinéa de L. 351-13 ; ces textes ont été lus. Le troisième alinéa de L. 351-13 ferme la majoration générale avec maintien au stock de 2010 : cette restriction n'est pas étendue d'office au renvoi local au seul premier alinéa, dont l'articulation historique reste à contrôler. Aucune situation future éligible sur un fondement local autonome n'est fermée. L'emploi ancien des mots 'pension revalorisée' est plus large que les renvois familiaux : cette ambiguïté préexistante est signalée, sans la transformer en nouveau gel général des pensions ni modifier silencieusement le cumul. La seconde pension reste acquise en sus.",
    "La limitation d'application du même dispositif de majoration à la pension la plus élevée et la conservation de la seconde pension restent inchangées ; aucun allègement matériel n'est revendiqué.",
    "Le maintien ne résout pas l'ambiguïté historique du mot revalorisation au regard du renvoi familial à L. 357-3 ; aucune suppression supplémentaire des droits ou modification de leurs taux n'en est déduite.",
    "Aucune charge nouvelle n'est identifiée : aucune information périodique, demande de cumul ou preuve supplémentaire n'est ajoutée au régime existant.",
    "La pension la plus élevée conserve les avantages de L. 357-3 et la seconde pension reste acquise en sus selon la règle source. Les situations futures relevant du cumul local ne sont pas exclues ; aucune autre majoration ni indexation n'est supprimée par une réinterprétation du texte."
)

retained(
    'L357-16',
    "Maintien intégral nécessaire : l'habilitation au calcul des pensions pour les affiliations successives, alternatives ou simultanées aux deux régimes locaux permet d'utiliser des périodes anciennes. Elle ne prescrit ni agrément individuel ni déclaration annuelle de l'assuré.",
    "La borne reste antérieure au 1er juillet 1946, sans que l'ancienneté du texte prouve l'extinction de tout droit dérivé ou contentieux. D. 357-25 désigne le ministre chargé de la sécurité sociale pour cet arrêté ; il a été lu. Les arrêtés eux-mêmes ne sont pas joints : aucun de leurs calculs n'est remplacé par une formule supposée.",
    "La base réglementaire de coordination des droits acquis dans les deux assurances locales est maintenue ; aucun prélèvement ni formalité individuelle n'est retiré artificiellement.",
    "Le champ demeure celui des affiliations antérieures au 1er juillet 1946 ; la proposition ne crée ni nouvelles cotisations ni ouverture de ce régime aux nouvelles affiliations.",
    "Aucune charge nouvelle n'est identifiée : l'arrêté de calcul reste une norme générale et aucune demande d'autorisation individuelle n'est créée.",
    "La prise en compte des périodes passées entre les deux régimes locaux reste possible dans ses trois configurations. Les demandes, révisions et droits dérivés futurs recevables ne sont pas fermés du seul fait de l'ancienneté des affiliations."
)

retained(
    'L357-17',
    "Maintien intégral nécessaire : l'article donne une base au cumul entre pensions de régimes différents pour les anciennes affiliations locales. La formule 'est autorisé le cumul' habilite un arrêté général ; elle ne démontre pas l'existence d'une autorisation administrative individuelle à supprimer. Abroger cette base pourrait retirer la possibilité même de cumul.",
    "L. 357-1, D. 357-25 et D. 357-27 ont été lus : options en faveur du régime le plus favorable, droits du survivant et coordination des pensions demeurent. Le contenu des arrêtés de cumul n'étant pas joint, leurs plafonds ou formalités ne sont pas déclarés abrogés ou inutiles sans lecture. La cohorte d'affiliation reste antérieure au 1er juillet 1946 et n'est pas assimilée au contrat unique privé.",
    "La possibilité légale de cumul et son cadre de coordination sont conservés ; l'article ne permet pas d'identifier une taxe ou une procédure individuelle de visa effectivement supprimable.",
    "Les conditions des arrêtés extérieurs ne sont pas présentes dans les sources lues ; le maintien n'est pas présenté comme un audit de toutes leurs modalités ni comme une suppression de leurs plafonds.",
    "Aucune charge nouvelle n'est identifiée : aucune autorisation, déclaration de remplacement, attestation ou registre n'est ajouté par la conservation de l'habilitation.",
    "Le cumul d'une pension locale avec celle d'un autre régime garde son fondement légal, au bénéfice des droits anciens et des liquidations futures recevables. Les options plus favorables du régime local ne sont pas fermées ni réservées aux seuls bénéficiaires actuels."
)

xml_35718 = (
    "<p>Les coefficients de revalorisation applicables pour la période postérieure au 31 décembre 1948 aux pensions d'invalidité et aux pensions de veuves ou de veufs du présent chapitre sont fixés par arrêté du ministre chargé de la sécurité sociale.</p>"
    "<p>Les coefficients légalement fixés avant l'entrée en vigueur de la loi portant la présente réforme et les revalorisations acquises conservent leurs effets. Les créances afférentes aux périodes antérieures, leur liquidation, leur paiement, leurs régularisations, leurs prescriptions et les recours restent régis par les dispositions qui leur étaient applicables.</p>"
)
draft(
    'L357-18', xml_35718,
    "Coordination nécessaire, sans réduction de pension : le L. 357-4 actuel ne mentionne plus les arrêtés visés par la source. Une habilitation autonome à fixer les coefficients remplace ce renvoi devenu inopérant. La période postérieure au 31 décembre 1948, les deux catégories de pensions et les droits acquis sont conservés ; aucun taux ni nouveau gel n'est créé.",
    "L. 357-4 a été lu intégralement : ses quatre alinéas portent sur les dispositions du régime général applicables, le cumul et un décret d'adaptation ; ils ne désignent aucun arrêté de revalorisation. L. 161-23-1, L. 351-11 et D. 357-25 ont également été lus. Le présent corps ne remplace pas les coefficients existants par ceux d'un autre régime et ne modifie pas leurs valeurs, non fournies ici. Le ministre chargé de la sécurité sociale reçoit expressément l'habilitation auparavant attachée à un renvoi vide ; aucun arrêté séparé supplémentaire n'est imposé. Le dispositif temporaire de L. 161-23-1 proposé, dans son propre champ de pensions de vieillesse et de réversion, n'est ni écarté ni étendu à l'invalidité par cette coordination. Aucun nouveau renvoi numéroté n'est ajouté.",
    'coordination_only',
    "Le changement réel est la suppression d'un renvoi sans objet à L. 357-4 et l'explicitation du fondement des arrêtés. Il ne démontre ni baisse de prélèvement ni suppression d'une formalité à la charge de l'assuré.",
    "Les valeurs des coefficients et le contenu des arrêtés historiques ne sont pas reproduits faute de ces textes dans le dossier. Leurs effets acquis sont conservés ; aucun rendement budgétaire ni changement de montant n'est affirmé.",
    "Aucune charge nouvelle pour les assurés n'est identifiée : aucun dossier, délai ou justificatif n'est ajouté. L'habilitation ministérielle poursuit la fonction des arrêtés déjà prévue par la source, sans imposer un nouvel acte distinct périodique.",
    [effect(
        'coordination', 'pensions-locales-renvoi-revalorisation',
        "Rendre autonome la base des coefficients de revalorisation sans modifier leur montant.",
        "Arrêtés désignés par un renvoi à L. 357-4, alors que sa rédaction actuelle ne comporte plus cette désignation.",
        "Coefficients des pensions locales d'invalidité et de survivant fixés par arrêté ministériel sur le fondement direct de l'article ; coefficients et revalorisations acquis conservés.",
        'legal_duty', "Titulaires des pensions locales d'invalidité, de veuve ou de veuf et administration chargée de leur revalorisation.",
        "Période postérieure au 31 décembre 1948 inchangée ; préservation des actes, créances et recours antérieurs à la réforme.",
        "Aucun dépôt ou visa individuel nouveau ; aucun taux ni calendrier de revalorisation supplémentaire n'est fixé.",
        plain(by_number['L357-18']['source_xml']),
        "Les coefficients de revalorisation applicables pour la période postérieure au 31 décembre 1948 aux pensions d'invalidité et aux pensions de veuves ou de veufs du présent chapitre sont fixés par arrêté du ministre chargé de la sécurité sociale."
    )],
    benefit="Le droit à revalorisation des pensions d'invalidité et de survivant n'est pas supprimé. Les coefficients déjà légalement fixés et les revalorisations acquises sont expressément conservés, tandis que l'habilitation autonome permet les revalorisations futures sans fermer le dispositif."
)

retained(
    'L357-19',
    "Maintien intégral nécessaire : le renvoi aux deuxième et troisième alinéas de L. 341-15 et à L. 351-10 garantit des minima de retraite aux assurés locaux. Les alinéas visés existent et portent effectivement sur ces garanties ; il n'y a pas lieu de les remplacer par une condition de contrat ou d'indemnité de rupture.",
    "L. 341-15 a été lu en entier dans le corpus : deuxième alinéa, plancher de la pension substituée ; troisième alinéa, garantie du montant d'invalidité pour les pensions liquidées avant le 31 mai 1983. L. 351-10 a été lu dans le fichier de cibles : minimum contributif, majoration des périodes éligibles, majorations s'ajoutant au minimum et revalorisation annuelle au moins liée au SMIC restent entiers. La fermeture générale de L. 351-13 à compter de 2011 et ses droits maintenus restent distincts du fondement local de L. 357-3, qui vise son seul premier alinéa ; aucune restriction supplémentaire ni réouverture générale n'est déduite ici de cette articulation. Les références du code du travail fournies à titre contextuel sont inapplicables à ces minima.",
    "Toutes les garanties de montant de la source sont conservées, y compris la protection historique d'invalidité et le minimum contributif avec ses majorations ; aucune réduction nouvelle n'est comptée.",
    "Le champ reste celui des pensions des deux législations locales ; aucune condition d'un an d'emploi, de notification de rupture ou de contribution à la capitalisation n'est ajoutée au bénéfice des minima.",
    "Aucune charge nouvelle n'est identifiée : maintien des renvois cohérents et des garanties existantes, sans justificatif ou demande supplémentaire.",
    "Les deux planchers de L. 341-15, dont celui propre aux pensions d'invalidité liquidées avant le 31 mai 1983, et tous les compléments du minimum de L. 351-10 demeurent applicables dans leurs champs. Les futures liquidations recevables restent couvertes, sans étendre artificiellement une cohorte historique."
)

retained(
    'L357-20',
    "Maintien intégral nécessaire : la neutralisation de l'absence de cotisations pendant la guerre est une dispense favorable de déchéance. Sa suppression pourrait éteindre des pensions ou droits dérivés et ne réduirait aucun prélèvement actuel.",
    "Les deux bornes, 27 août 1939 et 1er juin 1946, sont maintenues exactement. La garantie vise le défaut de versement pendant cet intervalle, sans créer une validation générale de toutes autres conditions de pension. Les demandes ou contentieux futurs recevables restent protégés ; aucune preuve nouvelle de paiement pendant la période n'est exigée.",
    "La source entière conserve la protection contre la déchéance pour non-versement pendant la période de guerre ; il s'agit d'un avantage maintenu, non d'une nouvelle exonération.",
    "La dispense reste limitée à la cause et à la période énoncées ; aucun droit hors du chapitre ou pour des périodes supplémentaires n'est créé.",
    "Aucune charge nouvelle n'est identifiée : ni justificatif additionnel de cotisation ni nouveau délai de réclamation ne sont instaurés par ce maintien.",
    "La dispense de déchéance pour absence de versements du 27 août 1939 au 1er juin 1946 reste entière. Elle peut être invoquée dans toute situation ultérieure recevable du chapitre et n'est pas limitée aux pensions déjà attribuées."
)

retained(
    'L357-21',
    "Maintien intégral nécessaire : l'habilitation réglementaire assure l'application des calculs et droits locaux énumérés, y compris les minima et pensions de survivants. Elle ne constitue pas une obligation de dépôt ou une autorisation individuelle à remplacer.",
    "Tous les articles visés ont été lus : L. 357-1, L. 357-2, L. 357-3, L. 357-5, L. 357-8, L. 357-9, L. 357-10, L. 357-11 et L. 357-19 ; les renvois numérotés restent en place. La plage L. 357-8 à L. 357-11 conserve ainsi minima, fractions et droits de survivant, y compris la condition spéciale des pensions sans justification d'invalidité de L. 357-10. D. 357-25 identifie les ministres intéressés. Aucun décret ne peut sur cette seule base fermer les majorations ou droits conservés par la loi.",
    "L'article conserve la compétence réglementaire utile au service de pensions et non une formalité répétée des assurés ; aucune suppression matérielle n'est revendiquée.",
    "Cette habilitation ne réécrit pas à elle seule chaque décret ou arrêté d'application. Les règles de calcul et avantages des dispositions énumérées conservent leurs champs respectifs.",
    "Aucune charge nouvelle n'est identifiée : la liste et le niveau réglementaire restent inchangés, sans nouveau dossier, rapport ou contrôle préalable."
)

retained(
    'L358-1',
    "Maintien intégral nécessaire : l'article crée la pension d'orphelin par assuré et couvre le décès, la disparition judiciairement déclarée et l'absence. Les actes d'état civil et décisions judiciaires identifient les personnes et les droits ; ils ne sont pas des déclarations fiscales de succession devenues inutiles.",
    "D. 358-1 et D. 358-2 ont été lus : pourcentage réglementaire de 54 %, pension théorique lorsque le défunt n'avait pas liquidé sa retraite et paramètres de calcul restent à leur place. Les références civiles 88, 112, 122, 310-1, 356 et 358 sont conservées sans leur attribuer un effet fiscal. La note source limite le dispositif aux décès, disparitions et absences survenus à compter du 1er septembre 2023 ; cette transition demeure. Les déclarations de variation sont examinées séparément à L. 358-7.",
    "Le droit à une pension pour chaque assuré décédé, disparu ou absent demeure entier ; aucun taux ni prélèvement n'est modifié et aucune réécriture stylistique n'est comptée.",
    "Le champ familial et les événements d'ouverture restent ceux de la source avec sa transition de 2023. Les articles civils extérieurs ne sont pas présentés comme réécrits dans ce lot.",
    "Aucune charge nouvelle n'est identifiée : le maintien ne crée aucune nouvelle déclaration judiciaire, donnée, procédure d'agrément ou condition d'emploi.",
    "La pension liée à chacun des parents assurés et le calcul sur une pension réelle ou théorique sont maintenus pour les événements futurs éligibles. Le droit n'est pas supprimé par l'abolition des droits de succession : une prestation d'assurance sociale n'est pas un prélèvement sur la succession."
)

retained(
    'L358-2',
    "Maintien intégral nécessaire : le plafond par assuré et le partage égal permettent de servir tous les orphelins demandeurs sans multiplier la pension du parent. La révision à l'arrivée d'un bénéficiaire protège l'égalité entre enfants ; ce mécanisme de répartition n'est ni une taxe ni une formalité redondante.",
    "La dérogation favorable de L. 358-3 au premier alinéa est maintenue intégralement : le plafond ne neutralise pas le minimum légal dérogatoire. La reprise de versement prévue au L. 358-6 proposé entraîne, s'il y a lieu, les révisions futures nécessaires selon le présent article, sans récupération des parts régulièrement dues aux autres orphelins pour les périodes antérieures. La note d'application aux événements survenus depuis le 1er septembre 2023 est conservée.",
    "Plafond, partage par parts égales et révision lors de l'ouverture d'un nouveau droit restent inchangés, avec la dérogation au profit du minimum. Leur maintien n'est pas une mesure d'allègement nouvelle.",
    "La reprise d'une pension suspendue peut modifier les parts futures des autres enfants selon les règles existantes ; aucun montant net global ou gain pour chaque famille n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée dans cet article : les mêmes calculs et la même révision sont conservés, sans dépôt supplémentaire ou nouveau plafond.",
    "Le partage égal entre orphelins ayant demandé la prestation reste garanti et le minimum dérogatoire de L. 358-3 reste applicable au-delà de la règle générale du premier alinéa. Les nouveaux bénéficiaires éligibles ne sont pas exclus pour préserver seulement les pensions en cours."
)

retained(
    'L358-3',
    "Maintien intégral nécessaire : l'article garantit un minimum de pension d'orphelin par dérogation au plafond et au partage du premier alinéa de L. 358-2. L'abroger ferait perdre une protection de revenu, sans supprimer une taxe ou une obligation administrative.",
    "D. 358-3 a été lu entièrement : montant réglementaire de base de 100 euros bruts mensuels et revalorisation aux dates et conditions de L. 161-23-1. Ce chiffre de base ne vaut pas affirmation du montant revalorisé à la date présente. Le renvoi dérogatoire vise bien le premier alinéa de L. 358-2 ; il n'est pas transformé en minimum soumis à ce plafond. Aucun montant nouveau n'est fixé ici.",
    "La source entière maintient le plancher favorable de pension, y compris sa dérogation au premier alinéa de L. 358-2. Aucun avantage préexistant n'est compté comme une réduction nouvelle.",
    "Le montant courant dépend de sa revalorisation réglementaire ; il n'est pas recalculé sans les coefficients applicables et aucune extension à un autre régime n'est postulée.",
    "Aucune charge nouvelle n'est identifiée : le bénéfice du plancher conserve ses mêmes conditions et ne requiert aucune nouvelle demande, attestation ou durée minimale.",
    "L'avantage identifié est le montant minimal de pension d'orphelin, dérogatoire au plafond et au partage du premier alinéa de L. 358-2. Il est intégralement conservé, avec son fondement réglementaire et sa revalorisation, pour les pensions actuelles et les futures situations éligibles ; aucun plafond de la règle générale ne lui est réappliqué."
)

retained(
    'L358-4',
    "Maintien intégral nécessaire : le versement sur un compte personnel de l'orphelin affecte la prestation à son bénéficiaire et protège ses fonds, particulièrement lorsqu'il est mineur. Supprimer cette règle au profit d'un compte de tiers retirerait une garantie patrimoniale sans établir de doublon administratif.",
    "Le renvoi à L. 312-1 du code monétaire et financier et le caractère personnel du compte sont conservés. Cet article ne prescrit ni ouverture d'un second compte si un compte personnel existe déjà, ni nouvelle attestation périodique. Les règles de représentation du mineur ne sont pas abrogées. La note source d'application aux événements survenus depuis le 1er septembre 2023 reste distincte d'une date future de réforme.",
    "L'affectation du paiement au compte personnel de l'orphelin demeure inchangée ; aucune suppression démontrée de frais ou d'obligation redondante n'est revendiquée.",
    "Le maintien ne règle pas les modalités bancaires ou de représentation hors du présent code ; il ne permet pas de chiffrer le coût d'accès au compte pour chaque bénéficiaire.",
    "Aucune charge nouvelle n'est identifiée : aucun second compte, service payant, registre ou envoi périodique de coordonnées bancaires n'est ajouté."
)

retained(
    'L358-5',
    "Maintien intégral nécessaire : les prolongations sous plafond de revenus, le droit sans limite d'âge en cas d'incapacité et le seuil d'incapacité abaissé sont des avantages de solidarité. Les supprimer ou remplacer l'ensemble par une limite uniforme ferait perdre des droits. Les conditions ne constituent pas un délai minimal d'emploi.",
    "D. 358-4 et L. 821-2 ont été lus entièrement : âge de vingt et un ans, prolongation de quatre ans, taux d'incapacité normal ou abaissé par renvoi, restriction substantielle et durable d'accès à l'emploi et plafond calculé sur les revenus réglementaires des douze mois restent dans leur champ. Aucun taux d'incapacité ou plafond en euros n'est inféré de renvois non chiffrés dans la source. Le dernier alinéa de D. 358-4, actuellement rédigé comme une fin de pension, devra être coordonné à la suspension de L. 358-6 proposé. Les deux alinéas législatifs restent cohérents avec cette suspension réversible et sont maintenus intégralement.",
    "Les trois voies de maintien de la pension et les conditions d'âge, de revenus et d'incapacité sont conservées ; le retrait de la déchéance définitive pour revenus est porté exclusivement par L. 358-6.",
    "La pension sans condition d'âge exige toujours l'incapacité à l'âge de référence et le plafond de revenus. Aucun élargissement de ces paramètres ni prise en charge hors des événements éligibles n'est affirmé.",
    "Aucune charge nouvelle n'est identifiée : les mêmes conditions de fond demeurent et la proposition n'impose ni nouveau taux ni attestation d'incapacité supplémentaire.",
    "Sont préservés la prolongation d'âge sous plafond de revenus, le versement sans limite d'âge en cas d'incapacité éligible et l'abaissement favorable du taux en présence des conditions de L. 821-2, 2°. Ces trois avantages restent ouverts aux futures situations recevables sans nouvelle durée d'emploi ou d'affiliation."
)

xml_3586 = (
    "<p>La pension prend fin ou est suspendue dans les conditions suivantes :</p>"
    "<p>1° Elle prend définitivement fin en cas d'adoption plénière de l'orphelin ou lorsque le parent absent ou disparu reparaît au lieu de son domicile ;</p>"
    "<p>2° Lorsque la condition de revenus mentionnée à l'article L. 358-5 n'est plus remplie, le versement de la pension est suspendu à compter du premier jour du mois suivant celui du dépassement du plafond. Il reprend au premier jour du mois suivant celui au cours duquel cette condition est de nouveau remplie, si les autres conditions du droit à pension sont réunies. La suspension n'éteint pas le droit à pension. La reprise du versement n'est subordonnée ni à une nouvelle demande de liquidation ni à une nouvelle liquidation des droits. L'organisme qui sert la pension procède à la reprise sur le fondement des informations exactes et à jour dont il dispose légalement, y compris les changements déclarés en application de l'article L. 358-7. Le plafond, les revenus à retenir et leur période de référence restent ceux applicables en vertu de l'article L. 358-5. La reprise donne lieu, le cas échéant, à la révision des parts prévue à l'article L. 358-2, sous réserve du minimum prévu à l'article L. 358-3.</p>"
    "<p>La présente rédaction s'applique aux prestations dues pour les périodes courant à compter de l'entrée en vigueur de la loi portant la présente réforme, dans le champ des décès, disparitions et absences survenus à compter du 1er septembre 2023. Les pensions auxquelles il a été définitivement mis fin pour le seul motif mentionné au 2° sont soumises au même régime pour ces périodes ; si les conditions de versement sont remplies à cette entrée en vigueur, leur versement reprend pour ces périodes sans nouvelle demande de liquidation. Les prestations afférentes aux périodes antérieures, les parts régulièrement dues aux autres bénéficiaires pour ces périodes, les créances, indus, prescriptions et recours demeurent régis par les dispositions antérieurement applicables, sans réouverture générale des périodes antérieures ni double paiement.</p>"
)
draft(
    'L358-6', xml_3586,
    "Réforme de fond : suppression de la déchéance définitive pour un dépassement, même temporaire, du plafond de revenus. Une suspension limitée aux périodes non éligibles la remplace, avec reprise sans nouveau dossier de liquidation lorsque les conditions reviennent. La finalité du plafond demeure et la cessation liée à l'adoption plénière ou au retour du parent est conservée. Le traitement d'office de la reprise ajoute une tâche à l'organisme : cette tâche et son coût sont explicitement recensés ; l'absence de nouvelle demande est une modalité de l'avantage créé, non une ancienne formalité supprimée.",
    "L. 358-5 reste entier, notamment l'incapacité requise à l'âge de référence et la voie au taux abaissé. D. 358-4 a été lu : conserver le plafond annuel, la période de douze mois et le début au mois suivant le dépassement ; coordonner son dernier alinéa qui prévoit encore la fin de pension. R. 358-1 et R. 358-2 ont été lus : les règles de première liquidation ne doivent pas imposer une nouvelle demande ou une perte de date pour une reprise ; ces dispositions réglementaires ne sont pas déclarées réécrites ici. Le minimum dérogatoire de L. 358-3 et le partage de L. 358-2 sont réservés expressément, avec les effets possibles sur les parts futures des autres orphelins, jamais sur leurs échéances antérieures régulièrement dues. L. 358-7 proposé fournit les déclarations résiduelles utiles sans périodicité nouvelle. Les extinctions antérieures pour revenus sont réversibles seulement pour les périodes nouvelles ; aucun rappel général antérieur n'est créé. Le coût supplémentaire de prestations et de gestion reste à évaluer ; aucune économie nationale n'est annoncée. Les renvois législatifs ajoutés à L. 358-2, L. 358-3 et L. 358-7, absents des cibles du fichier reference-targets, correspondent à des sources assignées lues intégralement et coordonnées dans le présent lot.",
    'mixed',
    "La source entière imposait une perte définitive en cas de dépassement de revenus. Le texte retire cette déchéance et permet la reprise sans nouveau dossier lors du retour à l'éligibilité, mais impose à la caisse de reprendre le service à partir des informations disponibles. L'absence de nouvelle liquidation n'est pas comptée comme le retrait d'une formalité qui existait avant la réforme. L'extension de prestation ne démontre pas une économie publique nette.",
    "Le plafond de revenus, la période de référence, les conditions d'âge et d'incapacité et les cessations du 1° subsistent. D. 358-4 et les procédures de reprise doivent être coordonnés ; le partage peut diminuer les parts futures d'autres orphelins. Aucun chiffrage du coût ou du solde global n'est établi.",
    "Aucun formulaire, registre, délai minimal ou justificatif nouveau n'est imposé au bénéficiaire. En revanche, le rétablissement du paiement et le calcul des parts créent pour la caisse une tâche supplémentaire sur les droits auparavant éteints ; ce traitement d'office est recensé et son coût net n'est pas établi.",
    [
        effect(
            'relief_extended', 'pension-orphelin-fin-decheance-revenus',
            "Supprimer l'extinction définitive pour dépassement du plafond et rétablir les versements futurs lorsque l'éligibilité revient.",
            "Dépassement du plafond de revenus de L. 358-5 : pension définitivement éteinte, même si les revenus baissent ensuite.",
            "Même plafond, mêmes revenus et période de référence : suspension dès le mois suivant le dépassement, puis reprise dès le mois suivant le retour sous le plafond si toutes autres conditions subsistent.",
            'regime', "Orphelins dont la prolongation ou le droit sans limite d'âge est soumis au plafond de revenus de L. 358-5.",
            "Événements éligibles depuis le 1er septembre 2023 ; prestations des périodes nouvelles après entrée en vigueur, y compris pour les extinctions antérieures dues aux seuls revenus. Pas de rappel général sur les périodes anciennes.",
            "Pas de nouveau dossier de liquidation ; plafond et contrôles utiles maintenus, reprise et révision des parts à traiter par l'organisme. Coût de prestation supplémentaire non chiffré.",
            plain(by_number['L358-6']['source_xml']),
            "La suspension n'éteint pas le droit à pension. La reprise du versement n'est subordonnée ni à une nouvelle demande de liquidation ni à une nouvelle liquidation des droits."
        ),
        effect(
            'obligation_added', 'pension-orphelin-fin-decheance-revenus',
            "Faire assurer par la caisse la reprise sans nouvelle liquidation, en utilisant les informations légalement disponibles.",
            "Après l'extinction définitive pour revenus, aucun rétablissement ultérieur de la même pension n'était prévu par cet article.",
            "L'organisme doit reprendre le paiement et, s'il y a lieu, réviser les parts sur la base des changements connus ; aucun nouveau flux de données n'est autorisé.",
            'legal_duty', "Organismes servant les pensions d'orphelin concernées par un retour à l'éligibilité.",
            "Même transition que la suppression de la déchéance ; informations exactes, à jour et légalement disponibles, avec respect des minima et des droits afférents aux périodes antérieures.",
            "Tâche publique de rétablissement ajoutée ; pas de nouveau formulaire privé ou de liquidation de remplacement. Coût administratif net inconnu.",
            plain(by_number['L358-6']['source_xml']),
            "L'organisme qui sert la pension procède à la reprise sur le fondement des informations exactes et à jour dont il dispose légalement, y compris les changements déclarés en application de l'article L. 358-7."
        ),
    ],
    removed=[
        "Extinction définitive du droit à pension d'orphelin en raison du seul dépassement du plafond de revenus d'activité."
    ],
    benefit="La pension sous plafond est rétablie pour les périodes futures lorsque les conditions reviennent, y compris après une extinction antérieure due aux seuls revenus. Les droits sans limite d'âge, le taux d'incapacité abaissé, le minimum de L. 358-3 et les parts antérieures régulièrement dues sont préservés ; le partage légal des périodes futures reste applicable."
)

xml_3587 = (
    "<p>I.-Le bénéficiaire de la pension d'orphelin est tenu de déclarer à l'organisme qui lui sert cette pension tout changement survenu dans ses liens de filiation. À compter de l'âge mentionné à la première phrase du premier alinéa de l'article L. 358-5, il déclare les changements de ses revenus d'activité qui entraînent le franchissement, dans l'un ou l'autre sens, du plafond prévu au même alinéa. Les revenus et le plafond sont appréciés selon les conditions et la période de référence applicables en vertu de cet article. Les variations de revenus qui ne modifient pas le respect de ce plafond ne donnent lieu à aucune déclaration au titre du présent article. Lorsque le bénéficiaire justifie de l'incapacité permanente prévue au second alinéa de l'article L. 358-5, il déclare au même organisme les seuls changements au regard de cette incapacité susceptibles de modifier le respect du taux applicable ou des conditions permettant l'application du taux abaissé prévu au même second alinéa. Les variations qui ne modifient ni le respect de ce taux ni celui de ces conditions ne donnent lieu à aucune déclaration au titre du présent article. Les conditions permettant l'application du taux abaissé demeurent inchangées.</p>"
    "<p>II.-Lorsque le bénéficiaire de la pension d'orphelin est un mineur non émancipé, les déclarations prévues au I du présent article sont effectuées par ses tuteurs.</p>"
    "<p>La présente rédaction s'applique aux changements survenus à compter de l'entrée en vigueur de la loi portant la présente réforme, pour les pensions relevant du présent chapitre, y compris celles déjà liquidées. Elle n'impose aucun renouvellement périodique de déclaration ou de justificatif en l'absence d'un changement à déclarer. Les obligations échues avant cette entrée en vigueur et les créances, indus, prescriptions et recours afférents aux périodes antérieures restent régis par les dispositions antérieurement applicables, sous réserve de l'application des dispositions répressives plus douces aux sanctions non définitives.</p>"
)
draft(
    'L358-7', xml_3587,
    "Réforme de fond : retrait de la déclaration de chaque variation de revenus ou d'incapacité lorsque cette variation ne change pas le respect du plafond, du taux applicable ou des conditions permettant le taux abaissé. Les déclarations utiles à l'ouverture, à la suspension ou à la reprise du droit demeurent ; celles de filiation et leur réalisation par les tuteurs restent entières. La suppression n'est pas remplacée par une déclaration périodique ni une attestation négative.",
    "L. 358-5, L. 358-6, L. 821-2, R. 358-3 et D. 358-4 ont été lus. Le franchissement de revenus est apprécié selon les revenus réglementaires et leur période de douze mois, pas sur une seule paie mensuelle ; le retour sous le plafond est déjà un changement au sens de la source et n'est pas une nouvelle obligation. Le taux d'incapacité peut être le taux abaissé : son bénéfice et les critères de L. 821-2, 2° restent intacts, sans nouvelle attestation. Les changements susceptibles d'affecter la restriction substantielle et durable d'accès à l'emploi demeurent déclarables même si le taux numérique d'incapacité ne change pas. La filiation reste déclarée sans restriction. Les pièces nécessaires à établir un changement affectant réellement le droit et les contrôles de fraude demeurent dans leurs fondements propres ; aucun accès nouveau aux données n'est ouvert. Les deux catégories de variations neutres sont documentées dans un seul effet de la mesure pension-orphelin-changements-sans-incidence, sans double compte par type de donnée. Les modèles ou instructions exigeant toutes les variations neutres devront être coordonnés, sans prétendre qu'ils sont ici réécrits. La date historique du 1er septembre 2023 mentionnée par la note source n'est ni déplacée ni une date de promulgation de la réforme.",
    'material_reduction',
    "Par rapport à l'intégralité de la source, une même mesure allège le signalement des variations neutres : revenus restant du même côté du plafond et changements d'incapacité sans effet sur le taux applicable ou les conditions du taux abaissé. Les deux catégories de données ne sont pas comptées comme deux mesures. La baisse porte sur le contenu obligatoire des signalements, pas sur les prélèvements ou le droit de réemploi déjà existant.",
    "La filiation, les franchissements de plafond après l'âge de référence, les changements pertinents d'incapacité ou des conditions du taux abaissé, les contrôles et les anciennes obligations échues demeurent. Le nombre de déclarations évitées et le coût total pour les organismes ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : la source exigeait déjà tout changement, donc aussi les franchissements dans les deux sens. Ni nouveau registre, ni périodicité, ni attestation négative, ni déclaration de remplacement n'est imposé ; les informations utiles au droit restent exigibles dans leur champ propre.",
    [
        effect(
            'obligation_removed', 'pension-orphelin-changements-sans-incidence',
            "Dispenser, au sein du même signalement social, les variations de revenus et d'incapacité sans incidence sur les conditions du droit à pension.",
            "À partir de l'âge de référence, tout changement de revenus d'activité était déclaré ; le bénéficiaire justifiant d'une incapacité permanente déclarait tout changement au regard de celle-ci, même sans incidence sur son droit.",
            "Seuls les franchissements du plafond dans l'un ou l'autre sens et les changements susceptibles d'affecter le taux d'incapacité applicable ou les conditions du taux abaissé sont déclarés ; filiation, plafond, revenus et période de référence restent inchangés.",
            'legal_duty', "Bénéficiaires de pension d'orphelin soumis au plafond de revenus ou à la condition d'incapacité permanente, et leurs tuteurs dans les cas prévus au II.",
            "Changements à compter de l'entrée en vigueur, y compris pour les pensions déjà liquidées ; obligations échues et périodes antérieures conservées sous réserve des dispositions répressives plus douces.",
            "Aucune déclaration périodique, négative ou attestation de stabilité ne remplace les signalements retirés. Les changements affectant les conditions du taux abaissé restent déclarables même sans variation du taux numérique.",
            plain(by_number['L358-7']['source_xml']).split(' II.-')[0],
            plain(xml_3587).split(' II.-')[0]
        ),
    ],
    removed=[
        "Déclaration de toute variation des revenus d'activité sans franchissement du plafond applicable à la pension d'orphelin.",
        "Déclaration de toute variation d'incapacité permanente sans incidence sur le taux applicable ou sur les conditions permettant le taux abaissé."
    ],
    benefit="La dispense créée concerne les seuls signalements sans effet sur l'éligibilité. Le droit prolongé sous plafond, le droit sans limite d'âge, le taux d'incapacité abaissé, les minima et la reprise de la pension restent accessibles aux bénéficiaires actuels et futurs ; aucune déclaration annuelle ou de stabilité ne les conditionne."
)

xml_3611 = (
    "<p>Sans préjudice de l'application de l'article L. 313-1, l'assurance décès garantit aux ayants droit de l'assuré le paiement d'un capital égal à un montant forfaitaire déterminé par décret lorsque l'assuré, moins de trois mois avant son décès, exerçait une activité salariée, percevait l'une des allocations ou l'un des revenus de remplacement mentionnés au premier alinéa de l'article L. 311-5 ou l'indemnité mentionnée au même alinéa, était titulaire d'une pension d'invalidité mentionnée à l'article L. 341-1 ou d'une rente allouée en vertu de la législation sur les accidents du travail et maladies professionnelles mentionnée à l'article L. 371-1, ou lorsqu'il bénéficiait, au moment de son décès, du maintien de ses droits à l'assurance décès au titre de l'article L. 161-8.</p>"
    "<p>La présente rédaction s'applique aux décès survenus à compter de l'entrée en vigueur de la loi portant la présente réforme. Les capitaux dus au titre de décès antérieurs, leurs conditions d'ouverture, liquidation et paiement, les indus, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables.</p>"
)
draft(
    'L361-1', xml_3611,
    "Coordination nécessaire : le renvoi aux seules 'allocations' du premier alinéa de L. 311-5 est explicité pour conserver aussi les revenus de remplacement et l'indemnité désormais nommés dans la proposition cible. L'avantage lié à l'illégalité d'un licenciement ne doit pas disparaître par cette clarification de vocabulaire. Toutes les autres voies d'ouverture, le forfait et le délai de moins de trois mois restent entiers ; aucune baisse de taxe ou cotisation n'est attribuée à cette précision.",
    "Les six cibles requises ont été lues intégralement et sont distinguées dans reference_checks. Le I, 3° de L. 313-1 vise l'assurance décès ; la suppression proposée au II de sa seule durée d'affiliation ne transforme pas cette condition en ancienneté de contrat. L. 311-5 proposé distingue explicitement l'indemnité du deuxième alinéa de L. 1235-16 des allocations et revenus de remplacement : le présent texte suit cette nomenclature sans inclure toutes les indemnités de rupture. L. 1235-16 a été lu en entier dans travail.json : réparation minimale de six mois en l'absence de réintégration, distincte de L. 1234-9, et procédure collective propre. Ce contrôle complémentaire est consigné ici sans ajout à reference_checks et aucun nouveau renvoi direct à cette cible n'est introduit. L. 341-1, L. 371-1 et R. 361-3 ont été lus ; la troisième voie de maintien reste appréciée au décès selon L. 161-8. D. 361-1 fixe un forfait de base de 3 400 euros revalorisé : aucun montant courant n'est inventé. Le capital décès est une prestation ; l'abolition des droits de succession n'en supprime ni l'ouverture ni le versement. Aucun seuil d'un an d'emploi et aucune attente de quinze jours ne sont ajoutés.",
    'coordination_only',
    "La source entière est conservée quant au capital, aux catégories d'assurés et aux périodes ; le seul ajustement substantiel de rédaction empêche que la nouvelle désignation de l'indemnité dans L. 311-5 ferme le renvoi existant. Cette coordination protectrice n'est pas comptée comme une taxe supprimée ou une nouvelle baisse de cotisations.",
    "Le texte n'élargit pas le capital à toute indemnité de rupture et ne modifie pas le forfait réglementaire. L'interprétation antérieure du mot allocations n'étant pas chiffrée, aucun nombre de nouveaux ayants droit ou gain financier n'est affirmé.",
    "Aucune charge nouvelle n'est identifiée : mêmes conditions d'affiliation et même fenêtre de moins de trois mois, sans nouvelle déclaration, preuve fiscale de succession, ancienneté de contrat ou délai de notification.",
    [effect(
        'coordination', 'capital-deces-renvoi-maintien-droits',
        "Conserver le périmètre du renvoi à L. 311-5 après sa clarification des allocations, revenus de remplacement et indemnité réparatrice.",
        "Renvoi aux allocations mentionnées au premier alinéa de L. 311-5, dont la source vise aussi des revenus de remplacement et L. 1235-16 sans nommer distinctement son indemnité.",
        "Renvoi explicite aux allocations, revenus de remplacement et à l'indemnité nommée au même alinéa ; autres voies et délai de moins de trois mois inchangés.",
        'other', "Ayants droit des assurés remplissant la condition de prestation récente visée par L. 311-5.",
        "Décès à compter de l'entrée en vigueur ; capitaux afférents aux décès antérieurs et recours préservés selon leur droit.",
        "Aucune nouvelle formalité ou preuve d'ancienneté ; pas d'indemnité ordinaire supplémentaire ni changement de financeur.",
        plain(by_number['L361-1']['source_xml']),
        plain(xml_3611).split(' La présente rédaction')[0]
    )],
    benefit="Le capital forfaitaire et chacune de ses voies d'ouverture sont préservés : activité salariée, prestations du premier alinéa de L. 311-5 avec leur désignation coordonnée, invalidité, rente AT-MP ou maintien de droits au décès. Les anciens capitaux et les futurs décès éligibles restent couverts ; aucun impôt successoral de remplacement n'est créé."
)

retained(
    'L361-4',
    "Maintien intégral nécessaire : la priorité des personnes à charge effective, totale et permanente et l'ordre subsidiaire des proches évitent qu'un paiement précipité prive les personnes dépendantes du capital. Le délai de revendication a une fonction de protection, distincte d'un délai minimum d'autorisation inutile.",
    "R. 361-3, R. 361-4 et R. 361-5 ont été lus : ordre entre prioritaires, représentation et protection des mineurs, délai d'un mois suivant le décès pour revendiquer la priorité. Ce délai n'est pas ramené au préavis de quinze jours du contrat de travail. Le conjoint non séparé de droit ou de fait, le partenaire de PACS, puis descendants et ascendants conservent exactement leur ordre et leurs conditions. La suppression des déclarations fiscales de succession ne ferme pas la demande sociale du capital.",
    "L'intégralité de la priorité et de la dévolution subsidiaire du capital est conservée ; le retrait du délai porterait atteinte à la possibilité effective des personnes à charge de se manifester.",
    "Le délai réglementaire d'un mois et les demandes de capital restent dans leur champ social propre ; aucune accélération globale des successions ou économie de formalités civiles n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun certificat fiscal, nouveau délai ou critère de parenté n'est ajouté à l'ordre de paiement existant.",
    "La priorité des personnes entièrement à charge et les droits subsidiaires du conjoint, partenaire de PACS, descendants et ascendants sont conservés avec leur ordre exact. Les futures personnes éligibles restent recevables et les mineurs gardent leurs garanties de représentation."
)

retained(
    'L361-5',
    "Maintien intégral nécessaire : l'incessibilité et l'insaisissabilité protègent l'usage du capital décès par les proches. Les deux exceptions, dettes alimentaires et récupération d'un capital obtenu par fraude ou fausse déclaration, protègent d'autres droits essentiels ; aucune de ces garanties n'est une taxe à supprimer.",
    "Les exceptions restent limitées au paiement de dettes alimentaires et au recouvrement de ce capital indûment versé dans les circonstances énoncées. Le texte n'autorise pas toute saisie fiscale ou tout recouvrement d'indu sur ce capital. Ni l'abolition des droits de succession ni le barème d'indemnité de rupture ne justifient une réduction de l'insaisissabilité.",
    "L'intégralité de la protection du capital et de ses deux exceptions est maintenue ; aucun allègement nouveau n'est attribué à une insaisissabilité qui existe déjà.",
    "La garantie ne supprime pas les autres dettes du bénéficiaire et ne les fait pas payer par la collectivité ; elle conserve seulement le traitement du capital prévu par la source.",
    "Aucune charge nouvelle n'est identifiée : le maintien ne crée aucune déclaration, inscription de sûreté, demande de dispense ou condition additionnelle au versement.",
    "L'incessibilité et l'insaisissabilité restent acquises pour les capitaux antérieurs et futurs, sous les seules exceptions de la source. La protection n'est pas fermée aux nouveaux bénéficiaires et aucune exception fiscale nouvelle ne la réduit."
)

retained(
    'L371-1',
    "Maintien intégral nécessaire : la prise en charge maladie-maternité des titulaires d'une rente ou allocation AT-MP non agricole présentant l'incapacité requise est un droit social favorable. Le supprimer réduirait la protection et pourrait faire perdre les exonérations de participation auxquelles le texte renvoie.",
    "L. 160-14 a été lu intégralement : ses 13° et 14° mentionnent les bénéficiaires de L. 371-1 et les personnes rattachées, sans supprimer les autres cas de limitation ou suppression de participation. Le champ non agricole et le taux minimum à fixer selon les règles existantes restent inchangés ; aucun taux n'est inféré du seul mot minimum. Il ne s'agit ni d'inaptitude à un poste de travail ni d'indemnité de licenciement, et le contrat unique n'y impose pas son seuil d'un an.",
    "La couverture des frais de santé maladie-maternité et le renvoi protecteur aux réductions de participation sont intégralement conservés ; aucun prélèvement nouveau ou allègement supplémentaire n'est compté.",
    "Le texte reste limité aux législations AT-MP non agricoles et à l'incapacité requise ; aucune extension aux régimes agricoles ou indemnités spéciales de rupture n'est affirmée.",
    "Aucune charge nouvelle n'est identifiée : ni nouvelle reconnaissance médicale, ni délai d'affiliation, ni justificatif périodique ne s'ajoute aux conditions existantes.",
    "Sont conservés le droit à prise en charge maladie-maternité du titulaire éligible et l'accès aux limitations ou suppressions de participation de L. 160-14 dans leurs champs respectifs, y compris les protections des personnes rattachées. Les situations futures éligibles restent ouvertes sans nouvelle ancienneté d'emploi."
)


def reference_checks(number, assessments):
    a = by_number[number]
    key = a['code_id'] + '|' + a['source_id']
    required = references['requirements'][key]
    assert len(assessments) == len(required)
    answers[number]['reference_checks'] = [
        dict(target_key=k, view_sha256=references['targets'][k]['view_sha256'], assessment=assessments[i])
        for i, k in enumerate(required)
    ]


reference_checks('L357-14', [
    "L. 1234-1 règle le préavis de licenciement : la proposition vise quinze jours calendaires pour les nouveaux contrats, avec droits antérieurs et procédures collectives distincts. L. 357-14 ne règle aucune rupture et ne renvoie pas à cet article ; la compétence pour apprécier l'inaptitude à pension n'est subordonnée ni à l'ancienneté chez l'employeur ni à la notification de rupture.",
    "L. 1221-2 proposé impose la durée indéterminée aux nouvelles relations privées en préservant les anciens contrats. Il ne transforme pas l'état d'inaptitude à pension locale en critère de contrat et n'est pas un renvoi de L. 357-14. La caisse et le juge gardent leur champ indépendamment d'un ancien CDD ou d'un nouveau contrat unique.",
    "L. 1234-9 concerne l'indemnité ordinaire patronale, proposée nulle avant un an puis à 0,20 mois par année totale, mois complets au prorata, plafond de six mois et ancienneté au terme avec préavis. Ce barème et la transition des anciens contrats sont étrangers à l'appréciation d'inaptitude et à son recours ; ils ne ferment ni pension ni indemnité spéciale.",
    "Le renvoi effectif est L. 142-1, dont le 4° couvre l'état d'inaptitude au travail. La source et sa proposition conservent ce contentieux social ; la compétence prévue à L. 357-14 reste donc cohérente. La note transitoire de 2019 sur les recours est conservée ; aucun délai de notification ou seuil d'ancienneté du contrat privé n'est importé.",
])

reference_checks('L357-19', [
    "L. 1234-1 et ses préavis d'un ou deux mois selon l'ancienneté, puis la proposition de quinze jours pour les contrats nouveaux, n'interviennent pas dans le calcul des pensions locales. L. 357-19 ne vise pas cette cible. Ni la notification de licenciement ni son calendrier ne conditionnent les minima de L. 341-15 ou L. 351-10.",
    "L. 1221-2 proposé remplace les nouvelles embauches à terme par le contrat unique, en conservant les situations anciennes. Cette règle de contrat privé n'est pas un renvoi de L. 357-19 : elle ne retire pas les pensions des affiliations locales et ne réserve pas leurs minima aux titulaires d'un contrat nouveau ou d'une durée d'emploi particulière.",
    "L. 1234-9 distingue indemnité ordinaire et indemnités spéciales, avec seuil d'un an au terme effectif, préavis inclus, puis 0,20 mois de l'ancienneté totale et plafond de six mois pour la composante nouvelle. Ces conditions ne sont pas transposables aux planchers de retraite locaux, qui restent ouverts selon leurs règles propres et leurs cohortes historiques.",
    "L. 351-10, fourni ici en source officielle seule, définit le minimum contributif au taux plein, ses majorations, les autres compléments qui s'y ajoutent et sa revalorisation au moins liée au SMIC. Le renvoi de L. 357-19 à l'article entier préserve tous ces éléments ; aucune ancienneté d'un an, notification de rupture ou réduction au plafond de six mois ne s'y substitue.",
])

reference_checks('L361-1', [
    "L. 1234-1 concerne le préavis de licenciement, remplacé dans sa proposition par quinze jours pour les contrats nouveaux et conservé pour les anciens. La fenêtre de moins de trois mois de L. 361-1 mesure l'activité ou la situation sociale récente avant le décès ; elle n'est pas un préavis et ne commence pas à une notification patronale. Aucun renvoi à L. 1234-1 n'est ajouté.",
    "L. 1221-2 proposé réserve les nouvelles relations privées à la durée indéterminée et protège les contrats antérieurs. L'activité salariée de L. 361-1 reste indépendante du type de contrat : anciens CDD dans leur transition et nouveaux contrats uniques peuvent ouvrir les mêmes droits sociaux. Aucune durée de mission ne met ici fin à l'emploi et aucune ancienneté minimale de contrat n'est créée.",
    "L. 1234-9 proposé règle la seule indemnité ordinaire patronale : un an au terme préavis inclus, puis 0,20 mois par année totale, fractions en mois complets et plafond légal de six mois avec transition. Le capital décès n'est pas cette indemnité ; il n'est donc ni supprimé pendant la première année ni plafonné en mois de salaire. La réparation spéciale visée par L. 311-5 reste distincte.",
    "Le renvoi à L. 313-1 porte notamment sur son I, 3° : prestations en espèces de l'assurance décès, sous les conditions alternatives de rémunérations cotisées ou d'heures pendant la période de référence. Son II vise d'autres prestations ; sa suppression proposée de durée d'affiliation ne supprime ni n'ajoute une ancienneté de contrat pour le capital. La réserve de L. 361-1 est maintenue, sans la confondre avec le seuil de L. 1234-9.",
    "Le premier alinéa de L. 311-5 maintient les droits maladie, maternité, invalidité et décès des bénéficiaires d'allocations ou de revenus de remplacement. La proposition cible distingue aussi l'indemnité du deuxième alinéa de L. 1235-16. Le renvoi de L. 361-1 est donc explicité pour ces catégories, sans le réduire aux seules allocations ni l'étendre à toute indemnité ordinaire de rupture. Les situations futures éligibles restent couvertes.",
    "L. 161-8 maintient temporairement les prestations en espèces après perte des conditions d'activité, avec résidence et séjour, absence de réouverture de droits équivalents et prolongation propre aux demandeurs d'emploi ; les cas d'indemnités nulles ou faibles subsistent. L. 361-1 vise ce maintien au moment du décès, distinctement de sa fenêtre de trois mois. Ni notification de rupture ni ancienneté d'un an ne sont ajoutées.",
])


result = [answers[a['number']] for a in sources]
assert len(result) == len(sources) == 24
for source, article in zip(sources, result):
    impacts = article['substantive_impact']['effects']
    pairs = [(item['measure_id'], item['kind']) for item in impacts]
    assert len(pairs) == len(set(pairs)), (article['number'], 'Duplicate measure and effect in one article')
    for item in impacts:
        assert item['source_quote'] in plain(source['source_xml']), (article['number'], 'source_quote')
        assert item['proposed_quote'] in plain(article['proposed_xml']), (article['number'], 'proposed_quote')
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(result), 'articles')
