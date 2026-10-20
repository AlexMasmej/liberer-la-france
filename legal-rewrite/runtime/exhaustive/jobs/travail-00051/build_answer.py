import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
by_number = {x['number']: x for x in sources}
answers = {}


class Plain(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def handle_starttag(self, tag, attrs):
        if tag == 'br':
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in {'p', 'div', 'li', 'tr'}:
            self.parts.append('\n')


def plain(xml):
    parser = Plain()
    parser.feed(xml)
    return ''.join(parser.parts)


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def base(n, proposed, reason, notes, substantive, benefit=None, removed=None,
         repeal=None):
    source = by_number[n]
    obj = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               substantive_impact=substantive)
    if proposed is None:
        obj['classification'] = 'retained_necessary'
    if benefit is not None:
        obj['benefit_review'] = benefit
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal:
        obj.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal)
    answers[n] = obj
    return obj


def effect(obj, kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    e = dict(kind=kind, measure_id=measure, description=description,
             before=before, after=after, unit=unit,
             affected_population=population, conditions_and_transition=transition,
             replacement_or_new_burdens=replacement,
             source_quote=source_quote, proposed_quote=proposed_quote)
    obj['substantive_impact']['effects'].append(e)


base('L2312-13', None,
     "Maintien intégral après examen des inspections, enquêtes et concours occasionnels. Leur objet est la prévention des atteintes à la santé et la recherche des causes d'accidents ou de maladies professionnelles, et non un agrément ou un rapport administratif supplémentaire. Supprimer leur régularité ou l'information sur les suites priverait le contrôle de son efficacité ; le concours interne reste facultatif.",
     "Source et note de 2017 lues intégralement. R2312-2 et R2312-3 lus dans le corpus public : délégation d'enquête et accès aux registres de prévention restent distincts. Coordination avec L2315-27 pour les réunions de santé ; aucune assimilation au préavis individuel de quinze jours. Cadre supérieur de participation à la prévention à respecter, notamment directive 89/391/CEE, article 11 ; texte européen non joint, conformité exhaustive non attestée.",
     impact('retained_necessary',
            "Les inspections régulières, enquêtes et auditions nécessaires à la prévention sont conservées sans reformulation ni réduction revendiquée.",
            "Aucune fréquence chiffrée ni économie de fonctionnement n'est établie ici ; les règlements d'enquête ne sont pas réécrits dans ce lot.",
            "Aucune charge nouvelle n'est identifiée : aucun nouveau texte n'est proposé et les facultés de concours occasionnel demeurent facultatives."))

base('L2312-14', None,
     "Maintien intégral de la consultation préalable, indispensable à une participation utile avant décision. Les trois allègements existants sont également conservés : dérogation avant lancement d'OPA, absence de consultation sur les projets, révisions et dénonciations d'accords collectifs, et dispense dans le domaine couvert par un accord de gestion prévisionnelle des emplois et compétences. Aucun second contrôle ne leur est substitué.",
     "L2312-49 lu en entier : la dispense avant lancement n'efface pas la réunion dans les deux jours ouvrables après publication ou annonce. Les exceptions restent ouvertes aux futures opérations et futurs accords éligibles. Les procédures collectives distinctes et les droits européens d'information-consultation ne sont pas supprimés par le contrat unique.",
     impact('retained_necessary',
            "Le principe de consultation avant décision et ses dispenses précises restent applicables ; il n'existe aucune nouvelle simplification à comptabiliser.",
            "La dispense GPEC reste limitée au domaine couvert ; ni l'ensemble des décisions patronales ni l'information après lancement d'une OPA n'en sont dispensés.",
            "Aucune charge nouvelle n'est identifiée puisque le corps source et les dispenses existantes sont intégralement maintenus."))

base('L2312-15', None,
     "Maintien intégral : informations précises et écrites, délai utile, réponse motivée et accès au juge rendent la consultation effective. L'accès aux documents administratifs est déjà limité par son droit propre. La saisine non automatiquement suspensive, avec prolongation judiciaire motivée, concilie l'effectivité du recours et la sécurité du calendrier ; aucune pièce ni autorisation autonome sans objet n'a été identifiée.",
     "Note d'application aux demandes introduites à compter du 1er janvier 2020 examinée. Le cinquième alinéa, visé par L2312-16, conserve sa place et son contenu. Ne pas confondre le délai de consultation avec le préavis individuel de quinze jours. Cadre à coordonner avec la directive 2002/14/CE, article 4 ; aucune vérification intégrale du texte européen non joint n'est revendiquée.",
     impact('retained_necessary',
            "Le droit à une information suffisante et le recours accéléré demeurent entiers ; les réponses motivées sont nécessaires au dialogue, sans réduction fictive.",
            "Le maintien ne chiffre aucun coût judiciaire et ne crée aucun accès aux informations publiques au-delà des règles légales existantes.",
            "Aucune charge nouvelle n'est identifiée : maintien sans nouveau corps, sans délai, justificatif ou registre ajouté."))

base('L2312-16', None,
     "Maintien intégral du choix conventionnel des délais, de la majorité des élus en l'absence de délégué syndical et du délai supplétif. Le temps d'examen utile protège la consultation ; l'avis négatif réputé rendu évite qu'une absence d'avis bloque indéfiniment la décision. La source n'institue pas elle-même un délai minimal chiffré qui pourrait être retiré.",
     "L2312-19, L2312-55 et R2312-5/6 lus. Les délais supplétifs d'un, deux ou trois mois relèvent de R2312-6, non du préavis individuel ; ils ne sont pas modifiés. Renvoi au cinquième alinéa de L2312-15 cohérent et maintenu. La modification du seul plancher de réunions de L2312-19 ne modifie pas les majorités ni ces délais.",
     impact('retained_necessary',
            "Le mécanisme conventionnel et supplétif de consultation demeure nécessaire ; ni baisse de délai ni suppression de formalité n'est revendiquée.",
            "Les délais réglementaires et spéciaux restent à leur champ ; aucun résultat sur la durée totale d'une procédure collective n'est établi.",
            "Aucune charge nouvelle n'est identifiée : la source reste entière et les possibilités d'accord sont conservées."))

base('L2312-17', None,
     "Maintien intégral des trois thèmes de consultation et de l'information environnementale. La consultation sur la durabilité s'insère déjà dans au moins une des consultations existantes, au choix de l'employeur, plutôt que dans un circuit supplémentaire. Les cas d'entreprises dispensées de publication autonome demeurent couverts selon les deux renvois commerciaux, sans créer ici une obligation de publication ni supprimer une dispense.",
     "Les deux occurrences numérotées 1° et 2° après les trois thèmes sont conservées dans leur structure source. Les renvois à L232-6-3 et L233-28-4 du code de commerce, y compris les V et second alinéa du V, nécessitent une vérification dans ce code hors corpus fourni. Cadre CSRD de consultation des représentants à coordonner, notamment directive 2013/34/UE, articles 19 bis et 29 bis modifiés ; aucune conformité ni calendrier européen actuel n'est présumé vérifié. La source ne contient pas de note d'entrée en vigueur.",
     impact('retained_necessary',
            "Les thèmes et le choix de rattachement de la consultation de durabilité sont conservés ; aucun rapport ou prélèvement nouveau n'est institué.",
            "Le champ des exemptions et le calendrier des obligations de durabilité du code de commerce restent hors vérification intégrale dans ce lot.",
            "Aucune charge nouvelle n'est identifiée : le maintien ne transforme pas les entreprises dispensées en entreprises soumises à une publication autonome."),
     benefit="Les dispenses visées au second alinéa du V de L232-6-3 et au V de L233-28-4 du code de commerce sont des avantages possibles de publication autonome : elles restent intégralement mentionnées et ne sont ni fermées aux entreprises futures ni transformées en obligation de publier. Leur inclusion dans la consultation du CSE demeure celle de la source. Le choix patronal de la consultation de rattachement reste ouvert ; aucun avantage fiscal n'est supprimé.")

n = 'L2312-18'
p = by_number[n]['source_xml']
needle = "Ces informations comportent en particulier"
addition = ("La base peut être constituée des documents et données déjà établis par l'entreprise, sur support papier ou informatique, ou d'un accès organisé à ces documents et données, sans recopie ni saisie dans un recueil distinct. Aucun logiciel spécifique, abonnement ou support informatique n'est imposé par les seules dispositions légales ou réglementaires relatives à la base. Les stipulations conventionnelles autonomes sur son support demeurent applicables. Ce choix ne réduit ni le contenu des informations dues, ni leur actualisation, ni les droits d'accès des destinataires ; les éléments manquants sont complétés dans les conditions applicables à chaque consultation. ")
p = p.replace(needle, addition + needle, 1)
p += ("<p>Ces modalités s'appliquent aux mises à disposition effectuées à compter de l'entrée en vigueur de la loi les instituant, y compris pour des informations relatives à des périodes antérieures. Les informations déjà communiquées n'ont pas à être déposées à nouveau ; les droits d'accès, de conservation et de confidentialité applicables à ces informations demeurent.</p>")
o = base(n, p,
     "Coordination législative de la liberté de support : le choix papier est ouvert aussi à partir de 300 salariés, contrairement à la restriction informatique de R2312-12. Les documents existants peuvent constituer la base sans ressaisie, à accès effectif et contenu inchangés. Tous les indicateurs d'égalité, le bilan des formations après entretiens ou reconversion et les destinataires sont conservés. L'article source n'imposait lui-même ni abonnement ni logiciel spécifique : leur absence d'obligation et l'équivalence existante entre mise à disposition et communication ne sont pas comptées comme des suppressions nouvelles.",
     "Les quatre alinéas sources sont conservés dans leur ordre ; le renvoi du quatrième au troisième reste exact. R2312-12, lu intégralement, impose un « support informatique pour les entreprises d'au moins trois cents salariés » : cette restriction est à retirer dans son propre article, sous la même measure_id, sans y compter une deuxième réduction. R2312-11/14 sur mise à jour et analyse sont aussi lus. L2312-21/23 restent compatibles, de même que L2312-36. L'accès organisé doit être effectif, les éléments manquants restent dus et les conventions existantes gardent leurs stipulations autonomes jusqu'à modification valable. Aucun coût national ni économie nette d'équipement n'est chiffré.",
     impact('coordination_only',
            "Le nouveau fondement législatif coordonne la liberté de support, dont la restriction concrète est portée par R2312-12. Aucune obligation autonome de ressaisie ou d'abonnement n'est démontrée dans L2312-18 et aucune seconde suppression n'est comptée.",
            "La réduction matérielle du support obligatoire doit être suivie dans R2312-12, hors lot. Les entreprises utilisant déjà des supports adéquats peuvent ne réaliser aucun gain ; coûts nets et gains effectifs non mesurés.",
            "Aucune charge nouvelle n'est identifiée : le choix des supports est facultatif ; compléter les informations manquantes et assurer un accès effectif reprennent des obligations existantes, sans index ni registre supplémentaire."),
     removed=["L'exclusivité du support informatique, applicable réglementairement à partir de trois cents salariés, est écartée par le libre choix législatif du support ; son exécution est à coordonner dans R2312-12."])
effect(o, 'coordination', 'cse-base-sans-recueil-ou-outil-impose',
       "Fondement législatif de la liberté de support ; la restriction concrète du règlement n'est pas comptée comme une seconde obligation dans cet article.",
       "L2312-18 exige une base rassemblant les informations ; R2312-12 impose le support informatique aux entreprises d'au moins 300 salariés et permet papier ou informatique en deçà.",
       "Les documents existants ou leur accès organisé peuvent constituer la base sans recopie ; papier ou informatique pour tous les effectifs, sans prescription légale ou réglementaire exclusive, sous réserve des stipulations conventionnelles autonomes et à contenu et accès inchangés.",
       'legal_duty', "Employeurs soumis à la BDESE et représentants destinataires, notamment entreprises d'au moins 300 salariés pour le support.",
       "Mises à disposition à compter de l'entrée en vigueur, y compris périodes anciennes ; aucun redépôt des informations déjà communiquées et droits antérieurs conservés.",
       "Aucun outil ni abonnement de remplacement ; informations manquantes toujours dues selon leurs règles existantes.",
       "Une base de données économiques, sociales et environnementales rassemble l'ensemble des informations nécessaires aux consultations et informations récurrentes que l'employeur met à disposition du comité social et économique.",
       "La base peut être constituée des documents et données déjà établis par l'entreprise, sur support papier ou informatique, ou d'un accès organisé à ces documents et données, sans recopie ni saisie dans un recueil distinct. Aucun logiciel spécifique, abonnement ou support informatique n'est imposé par les seules dispositions légales ou réglementaires relatives à la base.")

n = 'L2312-19'
p = by_number[n]['source_xml'].replace(
    "2° Le nombre de réunions annuelles du comité prévues à l'article L. 2315-27, qui ne peut être inférieur à six ;",
    "2° Le nombre de réunions annuelles du comité, dans le respect des réunions requises par l'article L. 2315-27 et des autres réunions obligatoires prévues au présent code ;")
p = p.replace("La périodicité des consultations prévue par l'accord ne peut être supérieure à trois ans.",
              "La périodicité des consultations prévue par l'accord ne peut être supérieure à trois ans. Le 2° s'applique aux accords conclus ou révisés à compter de l'entrée en vigueur de la loi supprimant le plancher général de six réunions ; les accords antérieurs continuent de produire leurs effets tant qu'ils ne sont pas valablement révisés ou dénoncés.")
o = base(n, p,
     "Réforme de fond : retrait du plancher général de six réunions lorsqu'un accord valide organise leur nombre. Le minimum propre aux quatre réunions annuelles de santé et sécurité et les réunions nécessitées par les accidents ou demandes légalement prévues restent imposés par L2315-27. Les majorités, le maximum de trois ans entre consultations, les quatre objets de négociation et la faculté d'avis unique demeurent inchangés.",
     "L2315-27 et L2315-28 lus en entier. Le rythme supplétif mensuel à partir de 300 salariés ou bimestriel en deçà n'est pas supprimé : la coupe ne joue qu'en présence d'un accord valide. Les quatre réunions SSCT, réunions après événement grave et demandes protégées restent distinctes. Les accords existants ne sont pas automatiquement révisés et les notes historiques de 2017 ne fixent pas la date future de réforme.",
     impact('material_reduction',
            "Un accord futur ou révisé peut fixer moins de six réunions ordinaires sans neutraliser les réunions SSCT et spéciales ; le plancher général négociable est effectivement retiré.",
            "Pas de réduction automatique du nombre réel de réunions ni du régime sans accord ; aucun coût net ni effet sur la qualité des échanges n'est chiffré.",
            "Aucune charge nouvelle n'est identifiée : les conditions de majorité, les réunions protégées et la nécessité d'un accord sont déjà prévues par la source et les articles connexes."),
     removed=["Le minimum général de six réunions annuelles imposé même à un accord valide est supprimé ; les réunions de santé et les réunions spéciales restent protégées."])
effect(o, 'obligation_removed', 'cse-fin-plancher-six-reunions-negociees',
       "Suppression du seuil général de six réunions dans le seul régime organisé par accord.",
       "L'accord ne peut prévoir moins de six réunions annuelles du CSE, en plus du respect des règles spéciales applicables.",
       "Pas de plancher général de six par accord ; au moins quatre réunions SSCT annuelles et les autres réunions légalement nécessaires subsistent.",
       'legal_duty', "Employeurs et CSE adoptant un accord conforme à L2312-19.",
       "Accords conclus ou révisés après entrée en vigueur ; accords antérieurs maintenus jusqu'à révision ou dénonciation valable.",
       "Aucune réunion, déclaration ou procédure de remplacement ; les obligations de sécurité sont existantes.",
       "2° Le nombre de réunions annuelles du comité prévues à l'article L. 2315-27, qui ne peut être inférieur à six ;",
       "2° Le nombre de réunions annuelles du comité, dans le respect des réunions requises par l'article L. 2315-27 et des autres réunions obligatoires prévues au présent code ;")

base('L2312-20', None,
     "Maintien intégral de la faculté de consulter sur les orientations stratégiques au niveau du groupe. La transmission de l'avis aux CSE et à l'organe dirigeant est la contrepartie utile de cette mutualisation, non un second rapport de gestion. Les CSE restent consultés seulement sur les conséquences de ces orientations dans leur champ ; retirer leur accès à l'avis rendrait la consultation locale inopérante.",
     "L2312-19 et L2312-22 demeurent compatibles avec la consultation de groupe. La définition de l'entreprise dominante de L2331-1 est conservée sans élargissement de champ. Aucun minimum de réunions, dépôt CPPNI ni délai de négociation supprimé n'est rétabli.",
     impact('retained_necessary',
            "La mutualisation conventionnelle au niveau du groupe et ses transmissions ciblées sont maintenues ; elles ne constituent pas une nouvelle fusion créée par ce lot.",
            "Les consultations sur les conséquences locales ne sont pas abolies et aucun gain budgétaire lié au groupe n'est démontré.",
            "Aucune charge nouvelle n'est identifiée : le dispositif facultatif existant est conservé sans document supplémentaire."))

base('L2312-21', None,
     "Maintien intégral des choix négociés d'organisation, de support, d'accès et de contenu de la base. Les dix thèmes minimaux rendent possible un examen cohérent de l'entreprise et protègent notamment l'égalité professionnelle ; ils ne justifient pas une saisie distincte de données déjà disponibles. La faculté d'intégrer les négociations obligatoires et les consultations ponctuelles évite déjà une multiplication de supports. Le relais de branche des moins de 300 salariés reste ouvert.",
     "Le maintien se combine avec les nouveaux modes de constitution de L2312-18, applicables sans supprimer les choix conventionnels valables. L2312-36 garde ses thèmes et son 2° expressément visé par L2312-26. Les références de majorité L2232-12 et de négociations L2242-1/11/13 ne sont pas modifiées ; aucune transmission ou ancien délai L2232 n'est rétabli.",
     impact('retained_necessary',
            "Les marges conventionnelles et les thèmes indispensables sont maintenus en entier ; leur mutualisation déjà prévue n'est pas comptée une seconde fois comme allègement.",
            "Le maintien n'atteste pas que tous les détails réglementaires soient indispensables ; les tableaux réglementaires ne sont pas réécrits par cet article.",
            "Aucune charge nouvelle n'est identifiée : pas de nouvelle négociation obligatoire, condition d'accès, index ou registre ; le choix négocié des supports demeure."))

base('L2312-22', None,
     "Maintien intégral de la consultation annuelle supplétive et de ses trois objets. L'information en temps utile sur économie, stratégie et emploi ne peut être remplacée par une simple information après décision. L'accord de L2312-19 permet déjà une autre périodicité et un avis unique. L'articulation entreprise/établissements évite de consulter chaque établissement en l'absence d'adaptation spécifique ; cette limite favorable est conservée.",
     "L2312-20 lu pour le niveau groupe ; L2312-24, L2312-25 et L2312-26 lus pour le contenu. L'abrogation du seul bilan social de L2312-28 ne retire aucune des trois consultations. Les adaptations locales restent à leur champ, sans appliquer le préavis individuel à ces consultations collectives.",
     impact('retained_necessary',
            "Les consultations annuelles à défaut d'accord et leurs limites de niveau restent utiles ; aucune baisse de fréquence ou nouvelle fusion n'est revendiquée.",
            "L'annualité ne concerne pas l'IS et ne rétablit aucun impôt annuel ; les modalités conventionnelles plus souples demeurent possibles.",
            "Aucune charge nouvelle n'est identifiée : maintien de la règle supplétive et de ses exceptions sans ajouter réunion ou rapport."))

base('L2312-23', None,
     "Maintien intégral du renvoi supplétif au sous-paragraphe 4. Il donne un contenu à l'obligation d'information quand aucun accord n'organise la base et évite un vide de droits d'accès. Le renvoi reste cohérent avec L2312-36, dont seuls le volet prospectif et la coordination au contrat unique sont modifiés, et avec la souplesse de support de L2312-18.",
     "Le sous-paragraphe 4 ne disparaît pas. Les contenus de L2312-36 et les destinataires sont maintenus ; la réforme n'impose pas de nouvel accord pour utiliser les documents existants. R2312-12 doit être coordonné au libre support, sans abroger ce renvoi législatif utile.",
     impact('retained_necessary',
            "Le renvoi à la base supplétive demeure opérant et nécessaire ; le seul maintien d'un renvoi n'est pas une réduction normative.",
            "Le présent article ne détermine lui-même ni les rubriques ni leur périodicité et n'achève pas la coordination des règlements.",
            "Aucune charge nouvelle n'est identifiée : aucune modification du texte ni nouvelle formalité pour accéder au régime supplétif."))

n = 'L2312-24'
p = by_number[n]['source_xml'].replace(
    "à des contrats temporaires et à des stages.",
    "aux contrats temporaires conclus avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée et à des stages. Pour les contrats de travail conclus à compter de cette entrée en vigueur, elle porte également sur les conséquences des missions ou affectations temporaires exécutées dans le cadre du contrat unique à durée indéterminée ; leur durée ne fixe pas celle de l'emploi. La présente consultation n'autorise aucun nouveau contrat de travail à durée déterminée ni renouvellement d'un tel contrat après cette entrée en vigueur.")
o = base(n, p,
     "Coordination de fond nécessaire au contrat unique : le suivi des contrats temporaires antérieurs demeure, mais ce thème de consultation ne peut autoriser de nouveaux CDD ou renouvellements. Les missions et affectations temporaires demeurent examinées pour leurs conséquences sans limiter la durée de l'emploi. Tous les autres objets, l'avis, les orientations alternatives, la réponse argumentée de l'organe dirigeant et la faculté de réplique du CSE sont conservés.",
     "Même mesure contrat-unique-duree-indeterminee que les articles instituant le régime, et non une seconde suppression des CDD. L2312-26, hors lot mais lu en entier, doit être coordonné pour ses II 1° et 9° relatifs aux CDD/intérim/portage ; son II 5° d) vise encore les demandes de dérogation au plancher de temps partiel retiré. Préserver ses aides, apprentissage, reconversion, durée de formation et informations sur contrats anciens. Les dispositifs spéciaux n'acquièrent ici aucun droit au CDD.",
     impact('coordination_only',
            "Le thème stratégique est rendu compatible avec la suppression des nouveaux CDD sans retirer de consultation ni créer un régime d'emploi temporaire de remplacement.",
            "Les articles instituant le contrat unique ne sont pas dans ce lot ; leur réduction ne peut être comptée à nouveau ici. L2312-26 demeure à coordonner hors lot.",
            "Aucune charge nouvelle n'est identifiée : le suivi des conséquences des missions et affectations relève déjà de l'activité, de l'emploi et de l'organisation du travail visés par la source."))
effect(o, 'coordination', 'contrat-unique-duree-indeterminee',
       "Coordination du vocabulaire et du champ temporel de l'information stratégique avec le contrat unique.",
       "La consultation vise le recours à des contrats temporaires sans distinction de leur date de conclusion.",
       "Les contrats temporaires ne sont visés comme contrats de travail que pour le stock antérieur ; les nouvelles missions n'emportent aucun terme de l'emploi.",
       'regime', "Entreprises soumises à la consultation stratégique, leurs CSE et salariés sous anciens ou nouveaux contrats.",
       "Stock conclu avant l'entrée en vigueur conservé selon son régime ; aucun nouveau CDD ni renouvellement autorisé après bascule.",
       "Pas de déclaration, registre de missions ou consultation supplémentaire ; contenu stratégique existant coordonné.",
       "le recours à la sous-traitance, à l'intérim, à des contrats temporaires et à des stages.",
       "La présente consultation n'autorise aucun nouveau contrat de travail à durée déterminée ni renouvellement d'un tel contrat après cette entrée en vigueur.")

base('L2312-25', None,
     "Maintien intégral de la consultation économique et de la recherche. Les pièces comptables sont celles déjà établies ou communiquées aux associés : leur accès par le CSE ne crée pas une seconde comptabilité. Confidentialité, explications des commissaires et documents des entreprises non commerciales sont utiles au contrôle. L'examen de l'utilisation du crédit d'impôt recherche ne supprime ni ne conditionne le crédit ; le cadre de chiffrage de l'IS ne justifie aucun retrait d'aide.",
     "Note de 2023 : entrée en vigueur historique au 1er janvier 2025, non date future de réforme. I, II, 1° à 5° et alinéa final conservés. Le mot source « conseil » pour convoquer les commissaires est une ambiguïté préexistante signalée sans correction silencieuse. Les renvois commerciaux L225-100 à 102, L225-108, L225-115 à 118, L232-2 à 4, L251-13, L232-6-4 et L233-28-5 nécessitent confrontation au code de commerce hors corpus. Le maintien de perspectives pour l'année à venir demeure compatible avec la dispense générale de prévisions à trois ans de L2312-36.",
     impact('retained_necessary',
            "Les pièces utiles à la consultation économique et la transparence sur le CIR sont conservées intégralement sans attribuer une nouvelle économie à la réutilisation de documents déjà prescrite.",
            "Le CIR, ses taux et son champ ne sont pas réécrits ici ; la validité actuelle de tous les renvois commerciaux ne peut être certifiée à partir des seuls textes fournis.",
            "Aucune charge nouvelle n'est identifiée : aucune comptabilité, certification ou condition d'avantage supplémentaire n'est proposée."),
     benefit="L'utilisation du crédit d'impôt pour dépenses de recherche est un objet d'information et non le fondement du crédit : celui-ci demeure ouvert aux futures dépenses et entreprises éligibles selon ses textes propres. La politique de recherche et les documents de durabilité ne créent ici ni réduction ni retrait d'aide. La confidentialité du II 3° demeure entière. La faculté d'obtenir les explications des commissaires et l'utilisation des documents comptables déjà établis sont conservées ; aucun nouvel agrément ou justificatif d'accès au CIR n'est institué.")

n = 'L2312-27'
p = by_number[n]['source_xml']
old = "Le procès-verbal de la réunion du comité consacrée à l'examen du rapport et du programme est joint à toute demande présentée par l'employeur en vue d'obtenir des marchés publics, des participations publiques, des subventions, des primes de toute nature ou des avantages sociaux ou fiscaux."
new = ("Pour les demandes présentées à compter de l'entrée en vigueur de la loi supprimant cette pièce obligatoire, le procès-verbal de la réunion consacrée au rapport et au programme n'a pas à être joint aux demandes de marchés publics, de participations publiques, de subventions, de primes ou d'avantages sociaux ou fiscaux. Son absence ne peut, sur le seul fondement du présent article, faire obstacle à leur recevabilité ou à leur attribution. Les demandes antérieures et les droits qui s'y rattachent demeurent régis par les dispositions applicables à leur date ; aucun nouvel envoi n'est exigé pour les demandes déjà complètes.")
p = p.replace(old, new)
o = base(n, p,
     "Réduction normative : suppression de la pièce systématique constituée du procès-verbal de prévention pour chaque demande de marché, participation, subvention, prime ou avantage. Cette annexion générale n'est pas nécessaire au contrôle concret de l'aide et répète un document de fonctionnement du CSE. Le rapport annuel de santé et sécurité, le traitement spécifique du travail de nuit et des facteurs de risques, le programme de prévention, les propositions du comité et l'explication des mesures inexécutées restent intégralement requis.",
     "Source et note de 2021 lues ; les dates des 31 mars 2022 et conditions de l'article 40 sont historiques. L4121-3-1 lu en entier : ni DUERP, ni traçabilité, ni programme détaillé, calendrier, ressources et coût des mesures ne sont supprimés. Les conditions autonomes de commande publique, des aides ou du droit européen restent à leur champ, sans généraliser sous un autre fondement cette pièce retirée. Coordonner formulaires et textes d'application reprenant cette seule annexion ; leur inventaire exhaustif n'est pas disponible dans ce lot.",
     impact('material_reduction',
            "Une pièce obligatoire transversale à chaque demande publique est retirée pour l'avenir. Les exigences substantielles de prévention et les avis correspondants demeurent.",
            "Les autres critères d'octroi et pièces légalement autonomes ne disparaissent pas ; le nombre de dossiers concernés et le coût de traitement évité ne sont pas chiffrés.",
            "Aucune charge nouvelle n'est identifiée : aucun justificatif, attestation de prévention ou déclaration de remplacement n'est créé."),
     benefit="Les subventions, primes, participations et avantages sociaux ou fiscaux ne sont pas supprimés. Leur accès demeure ouvert aux futures demandes recevables et devient indépendant de cette annexion systématique ; seules leurs conditions autonomes continuent de s'appliquer. Les demandes antérieures gardent leur régime et leurs droits, sans nouvel envoi pour les dossiers déjà complets. Les garanties de santé au travail, le programme et l'avis du CSE restent entiers.",
     removed=["L'annexion obligatoire du procès-verbal de prévention à chaque demande de marché, participation, subvention, prime ou avantage social ou fiscal est supprimée pour les demandes nouvelles."])
effect(o, 'obligation_removed', 'cse-fin-annexion-pv-demandes-publiques',
       "Suppression du procès-verbal de prévention comme pièce systématique des demandes publiques.",
       "Un procès-verbal est joint à toute demande patronale de marché public, participation, subvention, prime ou avantage social ou fiscal.",
       "Aucun procès-verbal joint sur ce seul fondement pour les demandes nouvelles ; pas d'irrecevabilité ou refus d'attribution pour cette absence.",
       'legal_duty', "Employeurs demandeurs de marchés, financements et avantages mentionnés, et organismes instructeurs.",
       "Demandes à compter de l'entrée en vigueur ; droit antérieur et droits liés aux demandes précédentes conservés, sans renvoi des dossiers complets.",
       "Aucune attestation ni déclaration équivalente ; les garanties de prévention et critères autonomes demeurent.",
       old, "le procès-verbal de la réunion consacrée au rapport et au programme n'a pas à être joint aux demandes de marchés publics, de participations publiques, de subventions, de primes ou d'avantages sociaux ou fiscaux.")

bilan_transition = ("Les consultations engagées avant cette entrée en vigueur demeurent régies par les dispositions antérieures. Les droits d'accès aux bilans déjà établis demeurent garantis dans les conditions de l'article L. 2312-31. La suppression du bilan social ne dispense ni de la consultation sur la politique sociale, les conditions de travail et l'emploi, ni des informations dues en application des articles L. 2312-18, L. 2312-26 et L. 2312-36.")
n = 'L2312-28'
p = ("<p>Le présent article est abrogé pour les consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire. Aucun bilan social d'entreprise ou d'établissement n'est exigé sur son fondement pour ces consultations, y compris lorsqu'elles portent sur des périodes antérieures.</p><p>" + bilan_transition + "</p>")
o = base(n, p,
     "Abrogation prospective de l'obligation supplémentaire de bilan social des entreprises et établissements d'au moins 300 salariés. Des informations économiques et sociales sont déjà dues au titre de L2312-18, L2312-26 et L2312-36 : la récapitulation spécifique et cet objet supplémentaire de la consultation sociale sont retirés, plutôt qu'une reformulation de leurs rubriques. La source n'imposant pas à elle seule une réunion séparée sur le bilan, aucune réunion entière supprimée n'est revendiquée. Les consultations sociales de fond, la prévention, l'égalité, les procédures déjà engagées et l'accès aux bilans existants sont protégés.",
     "L2312-26, L2311-1 et L2312-35 lus pour délimiter le champ. L2312-29/30/32 sont abrogés pour le même champ temporel ; L2312-31/33/35 sont coordonnés dans ce lot. L2317-2 lu : il prévoit 7 500 euros et vise déjà à tort L2312-14 ; sa sanction spéciale doit être coordonnée hors lot, avec loi pénale plus douce pour les infractions non définitivement jugées et effets de l'article 112-4 du code pénal à vérifier. Ne pas l'appliquer aux bilans désormais non exigibles. Les cadres hospitaliers D4626-7/32, lus, doivent être coordonnés pour leurs mentions de présentation/annexion, sans retirer les rapports médicaux ou les bilans ayant un fondement public autonome. Aucun autre régime public n'est implicitement abrogé.",
     impact('material_reduction',
            "La récapitulation et l'objet supplémentaire de consultation propres au bilan social à partir de 300 salariés sont abolis pour les nouvelles consultations ; les informations et consultations ayant une base autonome subsistent, sans réunion entière réputée supprimée.",
            "Une grande partie des données demeure due dans la BDESE : ni toute collecte sociale ni tout tableau de R2312-9 n'est supprimé. L2317-2 et les textes sectoriels restent à coordonner, sans bilan hospitalier autonome réputé aboli.",
            "Aucune charge nouvelle n'est identifiée : aucune synthèse, attestation ou consultation de remplacement n'est créée ; les obligations sociales conservées ont leurs fondements antérieurs."),
     repeal="Suppression pour les nouvelles consultations du bilan social obligatoire d'entreprise et d'établissement d'au moins trois cents salariés et de sa consultation supplémentaire, avec maintien des informations et droits autonomes.")
effect(o, 'obligation_removed', 'cse-suppression-bilan-social-obligatoire',
       "Suppression du dispositif supplémentaire de bilan social sans suppression des informations sociales autonomes.",
       "Au moins 300 salariés : la consultation sociale porte en outre sur le bilan de l'entreprise et, pour chaque établissement atteignant ce seuil, sur son bilan particulier ; aucune réunion séparée n'est imposée par cette seule source.",
       "Aucun bilan social obligatoire pour les nouvelles consultations ; informations de L2312-26 et BDESE conservées sans nouvelle synthèse imposée.",
       'legal_duty', "Entreprises et établissements d'au moins 300 salariés relevant de L2312-28, dont les organismes expressément compris dans son champ.",
       "Consultations engagées dès entrée en vigueur, même sur périodes précédentes ; procédures déjà engagées et accès aux bilans existants préservés.",
       "Aucun bilan ou rapport équivalent ; les informations sociales autonomes et les contrôles de prévention restent dus.",
       "la consultation sur la politique sociale de l'entreprise, les conditions de travail et l'emploi prévue au 3° de l'article L. 2312-17 porte, en outre, sur le bilan social de l'entreprise lorsque l'entreprise compte au moins trois cents salariés.",
       "Aucun bilan social d'entreprise ou d'établissement n'est exigé sur son fondement pour ces consultations, y compris lorsqu'elles portent sur des périodes antérieures.")

n = 'L2312-29'
p = ("<p>Le présent article est abrogé pour les consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire. Aucun premier ou deuxième bilan social ni bilan de l'année de passage sous le seuil de trois cents salariés n'est exigé sur son fondement pour ces consultations.</p><p>Les consultations engagées avant cette entrée en vigueur restent régies par les dispositions antérieures, y compris les allègements de contenu des deux premiers bilans. Les autres règles de franchissement de seuil et les délais favorables prévus à l'article L. 2312-34 demeurent applicables aux obligations qui subsistent.</p>")
o = base(n, p,
     "Abrogation de l'exécution initiale et résiduelle du bilan social, conséquence de L2312-28 : pas de premier bilan, deuxième bilan ou bilan maintenu pendant l'année de baisse d'effectif pour les nouvelles consultations. Les dispenses des premières années restent utilisables pour les consultations anciennes encore soumises au bilan. Le seuil et le délai général favorables de L2312-34 ne disparaissent pas.",
     "Même mesure que L2312-28, sans seconde obligation générale comptée. Ne pas rétablir un bilan à la baisse de seuil par décret ou formulaire. La source juxtapose « atteint » au seuil et le renvoi à L2312-34 qui dit « dépasse » : cette différence préexistante n'est pas résolue silencieusement pour les procédures anciennes. Le régime résiduel de ces procédures reste à appliquer selon son droit.",
     impact('coordination_only',
            "L'entrée progressive et la sortie différée d'un bilan supprimé sont retirées dans son même champ ; les allègements des anciens premiers bilans demeurent, sans comptabiliser une deuxième mesure.",
            "L'article ne supprime ni le seuil général de 300 salariés ni ses autres effets ; les consultations antérieurement engagées restent couvertes par leur transition.",
            "Aucune charge nouvelle n'est identifiée : aucun bilan de clôture ou de sortie n'est ajouté et les allègements anciens sont conservés."),
     repeal="Suppression des premiers et deuxièmes bilans sociaux et du bilan obligatoire de l'année de baisse sous trois cents salariés pour les nouvelles consultations, sans toucher les autres obligations de seuil.")
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Retrait des règles d'entrée et de sortie du bilan supprimé.",
       "Premier bilan l'année suivant le seuil, contenu allégé les deux premières années et bilan encore exigé l'année de passage sous 300 salariés.",
       "Ces bilans ne sont plus exigés pour les nouvelles consultations ; les règles favorables restent pour les procédures anciennes.",
       'legal_duty', "Entreprises et établissements entrant dans ou sortant du champ ancien du bilan social.",
       "Même bascule que L2312-28 ; maintien des allègements pour les consultations déjà engagées.",
       "Aucun bilan de cessation ou nouvelle déclaration de seuil.",
       "un bilan social est néanmoins présenté pour l'année en cours.",
       "Aucun premier ou deuxième bilan social ni bilan de l'année de passage sous le seuil de trois cents salariés n'est exigé sur son fondement pour ces consultations.")

n = 'L2312-30'
p = ("<p>Le présent article est abrogé pour les consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire. La récapitulation triennale et les rubriques du bilan social ne peuvent être exigées sur son seul fondement pour ces consultations.</p><p>Les consultations engagées auparavant demeurent soumises aux règles antérieures, y compris les allègements de l'article L. 2312-29 dans sa rédaction alors applicable. Les informations légalement dues sur un fondement distinct, notamment les articles L. 2312-26 et L. 2312-36, demeurent exigibles. Les droits d'accès aux informations et bilans existants sont conservés dans les conditions de l'article L. 2312-31.</p>")
o = base(n, p,
     "Abrogation de la définition et des rubriques propres au bilan social supprimé, y compris sa récapitulation sur l'année écoulée et les deux précédentes. La suppression vise le fondement supplémentaire du bilan, non toutes les données d'emploi, salaires, santé, formation, détachement ou conditions de vie qui restent requises par d'autres textes. Les droits d'accès sont expressément coordonnés.",
     "Aucune rubrique du bilan n'est réputée supprimée d'un tableau réglementaire lorsqu'elle possède aussi une base dans L2312-26 ou L2312-36. Leurs deux années historiques restent distinctes et conservées. R2312-9 et R2312-20, ce dernier lu, nécessitent examen des tableaux hors lot ; l'examen intégral de ces tableaux n'est pas revendiqué ici. Les régimes de travailleurs détachés et de logement restent autonomes.",
     impact('coordination_only',
            "Les rubriques et l'horizon propres au bilan obligatoire sont retirés avec ce dispositif, sans seconde réduction revendiquée ni suppression des données autonomes.",
            "Le volume exact des données devenant inutiles n'est pas déterminé faute de confrontation intégrale des tableaux réglementaires ; les historiques BDESE subsistent.",
            "Aucune charge nouvelle n'est identifiée : aucun tableau synthétique alternatif ni données sociales supplémentaires ne sont prescrits."),
     repeal="Suppression de la récapitulation sur trois années et des rubriques spécifiques du bilan social pour les nouvelles consultations, sans disparition des informations requises sur un fondement autonome.")
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Retrait de la définition du bilan et maintien des informations sociales autonomes.",
       "Le bilan récapitule les principales données chiffrées sur l'année écoulée et les deux précédentes, avec rubriques sociales propres.",
       "Cette récapitulation n'est plus imposée comme bilan ; l'information requise indépendamment du bilan reste due.",
       'legal_duty', "Entreprises et établissements anciennement tenus au bilan social.",
       "Nouvelles consultations après entrée en vigueur ; anciennes consultations et allègements initiaux préservés.",
       "Aucun tableau ou recueil de remplacement, sans dispense des informations ayant une base distincte.",
       "Le bilan social récapitule les principales données chiffrées permettant d'apprécier la situation de l'entreprise dans le domaine social, d'enregistrer les réalisations effectuées et de mesurer les changements intervenus au cours de l'année écoulée et des deux années précédentes.",
       "La récapitulation triennale et les rubriques du bilan social ne peuvent être exigées sur son seul fondement pour ces consultations.")

n = 'L2312-31'
p = ("<p>Les informations des bilans sociaux établis pour les consultations engagées avant l'entrée en vigueur de la loi supprimant le bilan social obligatoire restent mises à la disposition de tout salarié qui en fait la demande. Pour les consultations engagées à compter de cette entrée en vigueur, dans les entreprises et établissements appartenant aux catégories d'employeurs visées à l'article L. 2312-28 dans sa rédaction antérieure à cette entrée en vigueur et qui remplissent les conditions d'effectif de trois cents salariés prévues à l'article L. 2312-34, les principales données chiffrées déjà établies pour la consultation sur la politique sociale sont mises à la disposition de tout salarié qui en fait la demande lorsqu'elles portent sur l'emploi, les rémunérations et charges accessoires, les conditions de santé et de sécurité, les autres conditions de travail, la formation, les relations professionnelles, le nombre de salariés détachés et le nombre de travailleurs détachés accueillis, ou les conditions de vie des salariés et de leurs familles dans la mesure où ces conditions dépendent de l'entreprise. Cette mise à disposition ne requiert ni collecte supplémentaire ni établissement d'un bilan distinct ; les règles de protection des données personnelles demeurent applicables.</p>"
     "<p>Les informations mentionnées au premier alinéa sont mises à la disposition de l'agent de contrôle de l'inspection du travail mentionné à l'article L. 8112-1 avec l'avis du comité social et économique dans un délai de quinze jours à compter de la réunion de ce dernier.</p>")
o = base(n, p,
     "Coordination nécessaire des droits d'accès après suppression du bilan. L'accès aux bilans existants demeure ; pour les situations futures atteignant le même seuil, il porte sur les données chiffrées déjà établies pour la consultation sociale dans les domaines de l'ancien bilan. Aucun nouveau bilan n'est demandé. L'accès de l'inspection, l'avis et le délai de quinze jours restent requis. La protection des données personnelles n'autorise pas une nouvelle collecte.",
     "Les catégories du champ ancien sont désignées par la rédaction antérieure, pour couvrir aussi leurs futurs employeurs éligibles et les organismes adaptés de L2312-35, sans étendre ce droit à toutes les entreprises de 50 salariés. Le délai de L2312-34 reste intact. La liste reprend tous les domaines de L2312-30 et les deux nombres distincts de travailleurs détachés, sans rétablir sa collecte. L'alinéa de l'inspection demeure le deuxième et les droits sur les bilans existants demeurent. Cette coordination ne prétend pas conserver des données futures dont le seul fondement de production était le bilan supprimé.",
     impact('coordination_only',
            "L'accès des salariés et de l'inspection est détaché du document abrogé et rattaché aux données existantes dans les mêmes domaines et le même champ d'effectif.",
            "Le droit futur ne recrée pas des données dont la production n'aurait plus aucun fondement. L'équivalence quantitative avec toutes les anciennes rubriques du bilan n'est donc pas affirmée.",
            "Aucune charge nouvelle de collecte ou de synthèse n'est identifiée : accès déjà obligatoire dans ce champ, délai de quinze jours conservé et réutilisation des données existantes seulement."))
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Maintien d'un fondement autonome aux accès utiles après retrait du document obligatoire.",
       "Accès des salariés aux informations du bilan et de l'inspection au bilan avec l'avis sous quinze jours après réunion.",
       "Accès au stock des bilans et, à l'avenir, aux données sociales existantes des mêmes domaines ; accès de l'inspection avec avis et même délai de quinze jours.",
       'legal_duty', "Salariés et inspection du travail dans l'ancien champ des entreprises et établissements soumis au bilan social.",
       "Bilans des consultations anciennes conservés ; accès futur ouvert pour les entreprises et établissements remplissant à l'avenir les conditions de seuil.",
       "Pas de collecte ou de bilan alternatif ; mise à disposition nécessaire au maintien du droit existant.",
       "Les informations du bilan social sont mises à la disposition de tout salarié qui en fait la demande.",
       "Cette mise à disposition ne requiert ni collecte supplémentaire ni établissement d'un bilan distinct ; les règles de protection des données personnelles demeurent applicables.")

n = 'L2312-32'
p = ("<p>Le présent article est abrogé pour les bilans relatifs aux consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire. Aucun bilan social ni avis correspondant n'est à adresser ou à mettre à la disposition des actionnaires sur son fondement pour ces consultations.</p><p>Les obligations et droits de communication aux actionnaires concernant les bilans des consultations engagées avant cette entrée en vigueur demeurent régis par les dispositions antérieures, même si leur communication intervient ultérieurement. Les obligations d'information des actionnaires fondées sur d'autres dispositions, notamment celles du code de commerce, demeurent applicables.</p>")
o = base(n, p,
     "Abrogation prospective du circuit actionnarial propre au bilan social supprimé. Aucun bilan ni avis de remplacement n'est créé. Les droits relatifs aux bilans des consultations déjà engagées et les informations commerciales indépendantes dues aux actionnaires sont conservés. Cette exécution est rattachée à la même suppression que L2312-28, sans seconde mesure générale comptée.",
     "Les renvois L2312-28, L225-108 et L225-115 sont retirés du champ futur du seul bilan ; les droits commerciaux ne sont pas abrogés. Leur contenu doit être vérifié dans le code de commerce hors corpus. Le champ de la source est celui des sociétés par actions, sans extension à toutes formes sociales. Les anciens bilans restent communicables même après la bascule.",
     impact('coordination_only',
            "Le circuit de communication aux actionnaires du document supprimé disparaît pour les nouvelles consultations, au titre de la même mesure de suppression du bilan.",
            "Les comptes, rapports de durabilité et autres informations autonomes du code de commerce restent hors suppression et hors vérification intégrale de ce lot.",
            "Aucune charge nouvelle n'est identifiée : aucun document social alternatif, nouvelle transmission ou nouvelle obligation actionnariale n'est institué."),
     repeal="Suppression de l'envoi ou de la mise à disposition aux actionnaires du bilan social et de l'avis afférent pour les nouvelles consultations, avec communication ancienne et droits commerciaux autonomes préservés.")
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Retrait du circuit actionnarial attaché au bilan social abrogé.",
       "Dans les sociétés par actions, dernier bilan et avis du CSE adressés ou mis à disposition des actionnaires selon les règles commerciales visées.",
       "Pas de bilan ou avis à communiquer pour les nouvelles consultations sur ce fondement ; stock ancien et informations commerciales autonomes conservés.",
       'legal_duty', "Sociétés par actions relevant de l'ancien régime du bilan social et leurs actionnaires.",
       "Bascule selon la date d'engagement de la consultation ; droits de communication anciens maintenus même à échéance ultérieure.",
       "Aucun rapport, avis ou dépôt actionnarial substitutif.",
       "Dans les sociétés par actions, le dernier bilan social accompagné de l'avis du comité social et économique prévu à l'article L. 2312-28 est adressé aux actionnaires ou mis à leur disposition dans les mêmes conditions que les documents prévus aux articles L. 225-108 et L. 225-115 du code de commerce.",
       "Aucun bilan social ni avis correspondant n'est à adresser ou à mettre à la disposition des actionnaires sur son fondement pour ces consultations.")

n = 'L2312-33'
p = ("<p>Pour les consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire, les programmes annuels de formation légalement requis s'appuient sur les informations de formation déjà établies pour la consultation prévue à l'article L. 2312-26, sans établissement d'un bilan social. Le présent article ne crée aucune obligation autonome d'établir un programme de formation ni aucun versement.</p><p>Les obligations, créances, droits et recours nés avant cette entrée en vigueur demeurent régis par les textes qui leur étaient applicables. Les droits à la formation et les aides, exonérations ou financements prévus sur un fondement distinct restent ouverts aux situations futures qui en remplissent les conditions.</p>")
o = base(n, p,
     "Coordination avec suppression d'une contrainte de support : les programmes de formation déjà requis utilisent les informations existantes de L2312-26 au lieu d'exiger le bilan supprimé. Le renvoi à L6331-12 n'est pas reconduit pour les périodes futures. Aucun programme annuel, prélèvement ou condition d'aide n'est créé. Les obligations et créances anciennes, droits de formation et aides autonomes restent protégés.",
     "Incohérence préexistante : L6331-12 est absent du corpus public fourni ; son historique et son éventuelle abrogation restent à vérifier, sans affirmer cette abrogation sur la seule absence. Le nouveau corps n'en ressuscite aucun versement et ne laisse pas de renvoi futur à une cible non vérifiable. L2312-26 I et II 1°/3°/4° fournissent les informations de formation indépendantes du bilan ; les programmes ne sont requis que par leurs propres textes. Même mesure que L2312-28, sans nouvelle baisse de contribution alléguée.",
     impact('coordination_only',
            "Le bilan n'est plus le support obligatoire des programmes de formation ; la coordination réemploie les données existantes et n'institue aucun prélèvement.",
            "L'historique de L6331-12 reste une lacune documentaire signalée ; aucun montant ni suppression d'une contribution supposée n'est avancé.",
            "Aucune charge nouvelle n'est identifiée : pas de programme autonome, collecte, attestation ou paiement substitué au bilan ; seuls les programmes requis ailleurs restent dus."),
     removed=["Le bilan social est retiré comme base obligatoire des programmes annuels de formation pour les nouvelles consultations ; aucune collecte alternative n'est imposée."])
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Suppression du besoin de bilan comme support de la formation.",
       "Le bilan sert de base aux dispositions visées de L6331-12 et aux programmes annuels de formation.",
       "Les programmes requis utilisent l'information de formation existante sans bilan, sans nouveau versement ni programme autonome.",
       'legal_duty', "Entreprises soumises à des programmes de formation sur un fondement légal distinct.",
       "Nouvelles consultations après bascule ; créances, droits, recours et aides anciennes ou futures préservés selon leur fondement.",
       "Réemploi de l'information déjà due au CSE, sans nouvelle collecte ni contribution.",
       "Le bilan social sert de base à l'application des dispositions de l'article L. 6331-12 ainsi que de celles qui prévoient l'établissement de programmes annuels de formation.",
       "les programmes annuels de formation légalement requis s'appuient sur les informations de formation déjà établies pour la consultation prévue à l'article L. 2312-26, sans établissement d'un bilan social.")

base('L2312-34', None,
     "Maintien intégral des deux protections de seuil : douze mois consécutifs de dépassement avant franchissement et un an pour se conformer complètement aux obligations d'information et consultation qui en résultent. Le texte ne sert pas uniquement au bilan social : son champ est le présent chapitre. Le retirer avec le bilan aggraverait les autres obligations de seuil pour les futures entreprises concernées.",
     "Les chiffres douze mois, trois cents salariés et un an sont conservés sans assimilation à un délai minimal empêchant d'agir plus tôt. Le maintien bénéficie aussi aux franchissements futurs et reste compatible avec la disparition des obligations particulières du bilan. La différence source entre « atteint » dans L2312-29 et « dépasse » ici est signalée dans la transition de L2312-29, sans correction silencieuse des situations anciennes.",
     impact('retained_necessary',
            "Les délais favorables d'assujettissement restent entiers pour les obligations de chapitre encore applicables ; aucune nouvelle réduction n'est comptée.",
            "La disparition du bilan ne supprime pas tous les effets du seuil de 300 salariés ; les autres effets ne sont pas recensés exhaustivement ici.",
            "Aucune charge nouvelle n'est identifiée : conservation exacte des délais protecteurs, sans déclaration supplémentaire de franchissement."))

n = 'L2312-35'
p = ("<p>Un décret en Conseil d'Etat précise le contenu des informations prévues au présent paragraphe.</p>"
     "<p>Des décrets en Conseil d'Etat déterminent les adaptations nécessaires à la mise à disposition des informations relatives à la politique sociale, aux conditions de travail et à l'emploi et à l'exercice des droits d'accès prévus à l'article L. 2312-31 dans les entreprises tenues de constituer un comité social et économique ou des organismes de représentation du personnel qui en tiennent lieu en vertu soit de dispositions légales autres que celles du code du travail, soit de stipulations conventionnelles. Ces adaptations se limitent aux informations déjà requises sur un fondement distinct du bilan social supprimé, sans étendre le champ des employeurs ou les conditions d'effectif concernés.</p>"
     "<p>Ces décrets sont pris après avis des organisations syndicales représentatives dans les entreprises intéressées.</p>"
     "<p>Le nombre et la teneur de ces informations sont adaptés à la taille de l'entreprise et de l'établissement par arrêté du ou des ministres compétents.</p>"
     "<p>Pour les consultations engagées à compter de l'entrée en vigueur de la loi supprimant le bilan social obligatoire, aucun bilan social distinct, y compris spécifique à une branche, ne peut être imposé sur le fondement du présent article ni sur celui des articles L. 2312-28 à L. 2312-33 dans leur rédaction antérieure à cette entrée en vigueur. Les dispositions réglementaires prises sur ces seuls fondements cessent d'imposer un tel bilan pour ces consultations. Les consultations engagées antérieurement et les droits d'accès aux bilans déjà établis demeurent régis par les dispositions antérieures. Les stipulations conventionnelles autonomes et les obligations fondées sur une autre disposition législative demeurent applicables.</p>")
o = base(n, p,
     "Réduction et coordination de l'habilitation réglementaire : retrait de la possibilité de rétablir le bilan social supprimé sous une forme sectorielle. La précision du contenu des informations utiles, les adaptations aux organismes représentatifs équivalents, l'avis syndical et la modulation à la taille restent entiers. Les renvois globaux aux articles du bilan sont remplacés pour l'avenir par les objets d'information et les accès maintenus, avec préservation des fondements législatifs ou conventionnels autonomes.",
     "Les cinq alinéas sont conservés dans leur ordre fonctionnel ; le cinquième porte la fermeture du seul fondement de bilan obligatoire supprimé. Les décrets et arrêtés sectoriels pris sur ces fondements doivent être recensés et coordonnés hors lot. D4626-7 et D4626-32 lus : les rapports du service et du médecin du travail restent distincts et leurs mentions de bilan appellent une coordination, sans effacer le régime public hospitalier autonome. R2312-9 et R2312-20 doivent être confrontés rubrique par rubrique aux obligations sociales encore légales ; aucune purge automatique de leurs tableaux n'est affirmée.",
     impact('coordination_only',
            "La fermeture du pouvoir réglementaire de recréer le bilan donne effet à la même suppression de L2312-28 ; les pouvoirs de préciser les informations autonomes sont conservés.",
            "L'inventaire des arrêtés de branche n'est pas achevé dans ce lot ; les bilans ayant une base législative distincte ou un engagement conventionnel autonome ne sont pas supprimés.",
            "Aucune charge nouvelle n'est identifiée : maintien des consultations syndicales et adaptations existantes, sans nouvel avis, registre ou document social de remplacement."),
     removed=["L'habilitation permettant d'imposer des bilans sociaux spécifiques de branche et l'application future des règlements fondés sur le seul bilan supprimé sont retirées."])
effect(o, 'coordination', 'cse-suppression-bilan-social-obligatoire',
       "Fermeture des habilitations et règlements qui pourraient recréer le bilan supprimé.",
       "Le pouvoir réglementaire adapte les articles L2312-28 à L2312-33 et peut doter des branches de bilans sociaux spécifiques.",
       "Les adaptations ne concernent plus que l'information et l'accès maintenus ; aucun bilan distinct de branche ne peut être imposé sur le fondement supprimé.",
       'legal_duty', "Entreprises des branches et organismes de représentation du personnel couverts par les adaptations de L2312-35.",
       "Consultations nouvelles après entrée en vigueur ; procédures anciennes, bilans existants et fondements législatifs ou conventionnels autonomes protégés.",
       "Aucune procédure sectorielle ou formalité de remplacement ; adaptations utiles d'information conservées.",
       "Certaines branches d'activité peuvent être dotées, dans les mêmes formes, de bilans sociaux spécifiques.",
       "Les dispositions réglementaires prises sur ces seuls fondements cessent d'imposer un tel bilan pour ces consultations.")

n = 'L2312-36'
p = by_number[n]['source_xml']
p = p.replace("1° Investissements : investissement social (emploi, évolution et répartition des contrats précaires, des stages et des emplois à temps partiel, formation professionnelle, évolution professionnelle et conditions de travail), investissement matériel et immatériel ;",
              "1° Investissements : investissement social (emploi, évolution et répartition des contrats précaires, des stages et des emplois à temps partiel, formation professionnelle, évolution professionnelle et conditions de travail), investissement matériel et immatériel. Pour les contrats de travail, la mention des contrats précaires ne vise que les contrats conclus avant l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, sans autoriser aucun nouveau contrat à durée déterminée ni renouvellement après cette date ; une mission, une affectation ou une phase de formation limitée ne fixe pas la durée de l'emploi nouveau ;")
old = "Ces informations portent sur les deux années précédentes et l'année en cours et intègrent des perspectives sur les trois années suivantes."
new = ("Ces informations portent sur les deux années précédentes et l'année en cours. Elles comprennent les perspectives déjà établies par l'entreprise, sans obligation d'établir pour les seuls besoins de la base des prévisions sur les trois années suivantes. Cette dispense ne limite pas les informations nécessaires aux consultations prévues aux articles L. 2312-24 et L. 2312-25, notamment les perspectives pour l'année à venir prévues au 1° du II de ce dernier article. Elle s'applique aux consultations engagées à compter de l'entrée en vigueur de la loi l'instituant ; les consultations engagées auparavant demeurent régies par les dispositions antérieures.")
p = p.replace(old, new)
o = base(n, p,
     "Réduction normative de la projection obligatoire sur trois années : les perspectives déjà établies demeurent communicables, mais la BDESE n'impose plus leur fabrication générale. Les besoins propres de la stratégie et les perspectives pour l'année à venir de L2312-25 restent dus. Coordination nécessaire des contrats précaires avec le contrat unique, sans effacer le suivi du stock ancien ni créer un emploi à terme. Les dix thèmes, les deux années historiques, l'année courante, l'accès permanent, les différences d'effectif et la confidentialité sont intégralement conservés.",
     "R2312-10 lu en entier : coordonner son exigence de projections chiffrées ou tendances à trois ans et les raisons de leur indisponibilité ; ne pas rétablir par règlement une justification générale de non-prévision. R2312-8/9 restent à examiner pour leurs rubriques prospectives, sans prétendre réécrire leurs tableaux dans ce lot. L2312-26 II 2° conserve un renvoi exact au 2° du présent article ; ses références au CDD et au temps partiel restent à coordonner hors lot. Le dernier alinéa de discrétion demeure le dernier, pour conserver les renvois de R2312-12/13. Note de 2023 au 1er janvier 2025 conservée à son seul objet historique.",
     impact('material_reduction',
            "L'obligation supplétive générale de fabriquer une perspective à trois ans est retirée ; les perspectives existantes et besoins précis des consultations subsistent. La mention des contrats précaires est seulement coordonnée.",
            "Le gain porte sur les entreprises sans accord de L2312-21 et sans perspectives déjà établies ; ni l'historique de deux ans ni les informations prospectives nécessaires à la consultation économique ne disparaissent.",
            "Aucune charge nouvelle n'est identifiée : pas de prévisions de remplacement ni d'attestation d'absence ; les informations existantes et nécessaires étaient déjà dues. La coordination des contrats ne crée pas de registre de missions."),
     removed=["L'obligation supplétive générale d'établir des perspectives sur les trois années suivantes pour les seuls besoins de la BDESE est supprimée, sans remplacer cette projection par une attestation."])
effect(o, 'obligation_removed', 'cse-fin-previsions-generales-trois-ans',
       "Suppression de la fabrication systématique de perspectives triennales pour la base supplétive.",
       "Sans accord sur la base : informations des deux années précédentes et de l'année en cours, avec perspectives sur les trois années suivantes ; R2312-10 prévoit chiffres ou tendances et motifs d'indisponibilité.",
       "Historique et année courante inchangés ; perspectives déjà établies et informations nécessaires à la stratégie ou à l'année à venir conservées, sans fabrication générale de projections sur trois ans.",
       'legal_duty', "Employeurs et représentants soumis à la BDESE supplétive faute d'accord de L2312-21.",
       "Consultations engagées après entrée en vigueur ; procédures antérieures gardent leurs règles.",
       "Aucune attestation de non-prévision ni nouvelle projection standardisée ; obligations de consultation autonomes conservées.",
       old,
       "Elles comprennent les perspectives déjà établies par l'entreprise, sans obligation d'établir pour les seuls besoins de la base des prévisions sur les trois années suivantes.")
effect(o, 'coordination', 'contrat-unique-duree-indeterminee',
       "Coordination de la rubrique des contrats précaires avec le champ temporel du contrat unique.",
       "La rubrique d'investissement social suit l'évolution et la répartition des contrats précaires sans distinction temporelle.",
       "Les anciens contrats temporaires restent suivis ; aucune nouvelle durée d'emploi limitée ne peut être déduite de cette rubrique.",
       'regime', "Employeurs tenant la base supplétive et salariés relevant d'anciens contrats temporaires ou du nouveau contrat unique.",
       "Ancien stock conservé, aucun nouveau CDD ou renouvellement après bascule ; durée des missions et phases pédagogiques distincte.",
       "Aucun registre ni décompte de missions supplémentaire créé par cette précision.",
       "emploi, évolution et répartition des contrats précaires, des stages et des emplois à temps partiel, formation professionnelle, évolution professionnelle et conditions de travail",
       "une mission, une affectation ou une phase de formation limitée ne fixe pas la durée de l'emploi nouveau")

base('L2312-37', None,
     "Maintien intégral des six cas numérotés, dont le 3° bis, de consultation ponctuelle. Les moyens de surveillance affectent les libertés ; restructurations, licenciements collectifs, concentrations, OPA et procédures d'insolvabilité affectent l'emploi et justifient une consultation avant décision. Les supprimer au nom du préavis individuel effacerait des garanties collectives distinctes et pourrait méconnaître des exigences européennes. Aucun doublon déclaratif autonome n'est créé par cette liste.",
     "L2312-8, L2312-14, L2312-49 et L2312-55 lus pour l'articulation générale, la dérogation avant lancement d'OPA et les modalités négociables. La liste 1°, 2°, 3°, 3° bis, 4°, 5° reste entière. Cadres supérieurs à coordonner : information-consultation (directive 2002/14/CE), licenciements collectifs (98/59/CE), OPA (2004/25/CE) et garanties d'insolvabilité selon leur champ. Leurs textes intégraux ne sont pas joints et aucune conformité complète n'est attestée. Aucun préavis individuel de quinze jours n'efface autorisations de salariés protégés ou procédure collective.",
     impact('retained_necessary',
            "Les consultations ponctuelles protégeant l'emploi et les libertés sont conservées en entier sans nouvelle mesure de simplification ni assimilation au préavis de rupture.",
            "La liste ne détermine pas à elle seule tous les délais ou autorisations ; les régimes de licenciement, concentration et procédures collectives restent distincts.",
            "Aucune charge nouvelle n'est identifiée : maintien de la liste source sans nouvelle consultation, autorisation, donnée ou délai."))


def verify():
    assert len(sources) == 24
    assert set(answers) == set(by_number)
    allowed = {'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong',
               'i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}

    class Check(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed, tag
            assert all(k in {'rowspan','colspan'} and v.isdigit() for k,v in attrs), attrs

    for src in sources:
        obj = answers[src['number']]
        for k in ['code_id','source_id','source_sha256','number']:
            assert obj[k] == src[k]
        si = obj['substantive_impact']
        assert si['version'] == 1
        for k in ['assessment','scope_limitations','new_burdens_review']:
            assert len(si[k]) >= 40
        if src.get('benefit_check_required'):
            assert len(obj.get('benefit_review','')) >= 100
        if obj['status'] == 'retained_unchanged':
            assert obj['proposed_xml'] is None
            assert si['classification'] == 'retained_necessary'
            assert si['effects'] == []
        else:
            Check().feed(obj['proposed_xml'])
            assert obj['proposed_xml'] != src['source_xml']
        if obj.get('change_type') == 'full_repeal':
            assert plain(obj['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
            assert len(obj['repeal_scope']) >= 30
        if obj.get('change_type') == 'normative_reduction':
            assert all(len(x) >= 30 for x in obj['removed_provisions'])
        for e in si['effects']:
            assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(src['source_xml']), (src['number'], 'source',e['source_quote'])
            assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(obj['proposed_xml']), (src['number'],'proposed',e['proposed_quote'])
    return [answers[x['number']] for x in sources]


if __name__ == '__main__':
    result = verify()
    Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'article_count':len(result), 'status':{s:sum(x['status']==s for x in result) for s in ['rewrite_draft','retained_unchanged']}, 'output_bytes':Path('answer.json').stat().st_size},ensure_ascii=False))
