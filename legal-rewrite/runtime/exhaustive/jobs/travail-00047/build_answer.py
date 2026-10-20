import json
import re
from pathlib import Path
from html import unescape

SOURCES = json.loads(Path('source.json').read_text())
REFERENCES = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()


def paragraphs(*items):
    return ''.join('<p>' + x + '</p>' for x in items)


def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])


def effect(kind, measure, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


ANSWERS = {}


def retain(number, reason, notes, assessment, limitations, burdens):
    a = BY_NUMBER[number]
    ANSWERS[number] = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    ANSWERS[number].update(
        proposed_xml=None, reason=reason, review_notes=notes,
        status='retained_unchanged', classification='retained_necessary',
        substantive_impact=impact('retained_necessary', assessment, limitations, burdens))


def rewrite(number, xml, reason, notes, assessment, limitations, burdens,
            effects, removed=None):
    a = BY_NUMBER[number]
    ANSWERS[number] = {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    ANSWERS[number].update(
        proposed_xml=xml, reason=reason, review_notes=notes,
        status='rewrite_draft', substantive_impact=impact(
            'material_reduction' if removed else 'coordination_only',
            assessment, limitations, burdens, effects))
    if removed:
        ANSWERS[number].update(change_type='normative_reduction',
            reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)


retain('L2253-2',
    "Maintien intégral après examen des quatre matières : la prévention des risques, l'emploi des personnes handicapées, la représentation syndicale et les primes de danger ou d'insalubrité ont une fonction protectrice précise. La possibilité d'un accord d'entreprise assurant des garanties au moins équivalentes évite déjà un verrou absolu. Aucun prélèvement, dépôt ou agrément administratif autonome à supprimer dans cet article.",
    "Conserver les 1° à 4° et l'appréciation par ensemble de garanties de même matière. Les deux notes transitoires de l'article 16 de l'ordonnance du 22 septembre 2017, avec confirmation avant le 1er janvier 2019 et effets sur les accords étendus, restent applicables ; ce délai historique n'est pas rouvert. Le renvoi à L4161-1 concerne les facteurs de risques, non un dispositif de CDD.",
    "Les garanties de branche expressément verrouillées restent protégées, avec équivalence possible en entreprise ; aucune contrainte nouvelle ni réduction normative n'est revendiquée.",
    "Le maintien ne vaut pas examen de chaque accord de branche ni chiffrage des primes ; les effets des confirmations antérieures à 2019 restent à apprécier dans chaque accord.",
    "Aucune charge nouvelle identifiée : aucun nouveau support, visa, délai ou justificatif n'est ajouté aux quatre protections et à leur faculté d'équivalence.")


base = BY_NUMBER['L2253-3']['source_xml']
guard = "La priorité prévue au présent article ne permet pas de déroger à l'interdiction des nouveaux contrats à durée déterminée résultant de l'article L. 1221-2 ni à la durée impérative du préavis individuel des contrats nouveaux prévue à l'article L. 1234-1. Les contrats antérieurs conservent leurs règles transitoires. Les indemnités conventionnelles ou contractuelles plus favorables demeurent applicables dans les conditions de l'article L. 1234-9."
xml = base + paragraphs(guard)
rewrite('L2253-3', xml,
    "Coordination de fond nécessaire avec le contrat unique : la priorité de l'accord d'entreprise demeure hors des matières de L2253-1 et L2253-2, mais ne peut servir à créer un nouveau CDD ou à modifier le préavis impératif des contrats nouveaux. Les indemnités plus favorables et la transition des contrats antérieurs restent ouvertes. Aucun allègement supplémentaire de prélèvement ou de dépôt.",
    "Le premier alinéa est intégralement conservé. La note du IV de l'article 16 de l'ordonnance de 2017 conserve ses effets au 1er janvier 2018. L2253-1 fourni est une proposition : ses 7°, 8° et 10° sont transitoires pour les anciens régimes, sans autorisation nouvelle de CDD, de fin automatique de chantier ou de renouvellement d'essai. Les majorités et les protections de L2253-2 ne sont pas modifiées.",
    "La priorité conventionnelle déjà existante est conservée ; la proposition ferme seulement une lecture qui réintroduirait un CDD ou les anciens préavis par accord d'entreprise. Cette coordination n'est pas une seconde réduction des coûts de rupture.",
    "Le barème de rupture et les règles de notification ne sont pas fixés ici. Leur mise en œuvre dépend des articles du contrat unique ; aucune baisse nette de coût du présent article n'est démontrée.",
    "Aucune charge nouvelle identifiée : aucun dépôt, vote, délai ou donnée n'est ajouté. La réserve reprend des limites impératives et les droits plus favorables de l'indemnisation.",
    [effect('coordination', 'contrat-unique-coordination-accords',
        "Articulation de la priorité d'entreprise avec le contrat unique et les droits indemnitaires plus favorables.",
        "Priorité des stipulations d'entreprise de même objet hors L2253-1 et L2253-2, sans explicitation du futur contrat unique.",
        "Même priorité ; interdiction de nouveaux CDD et préavis impératif des nouveaux contrats réservés, avec indemnités plus favorables conservées.",
        'regime', "Employeurs et salariés couverts par les accords d'entreprise.",
        "Application dans le champ temporel propre des articles L1221-2, L1234-1 et L1234-9 ; règles des anciens contrats préservées.",
        "Aucune formalité de remplacement ; aucune suppression de protection collective.",
        "En l'absence d'accord d'entreprise, la convention de branche ou l'accord couvrant un champ territorial ou professionnel plus large s'applique.",
        guard)])


retain('L2253-4',
    "Maintien intégral de la faculté de modalités salariales propres à l'entreprise ou à l'établissement. Le plancher d'augmentation de masse salariale et les minima hiérarchiques protègent les augmentations déjà reconnues aux salariés ; les enlever retirerait un avantage pendant que la règle générale de rémunération subsiste. Aucun dossier ou prélèvement accessoire distinct n'est institué.",
    "Les deux conditions cumulatives, la population des salariés concernés et le renvoi à L2253-3 sont maintenus. La masse salariale totale n'est pas une garantie d'augmentation individuelle identique ; ne pas transformer l'une en l'autre. Le seuil de quarante heures des contrats nouveaux ne relève pas de cet article et n'autorise aucune baisse du salaire contractuel.",
    "La souplesse de répartition des majorations et ses contreparties salariales subsistent en totalité ; aucun gain nouveau de simplification n'est compté.",
    "Les accords et montants de salaires ne sont pas fournis ; aucun gain de masse salariale, d'emploi ou de prélèvements n'est calculé.",
    "Aucune charge nouvelle identifiée : les deux garanties salariales et la faculté conventionnelle demeurent exactement celles de la source.")

for number, level, perimeter in [
    ('L2253-5', 'du groupe', "les entreprises et établissements compris dans l'accord de groupe"),
    ('L2253-6', "de l'entreprise", "les établissements compris dans l'accord d'entreprise"),
    ('L2253-7', 'interentreprises', "les entreprises et établissements compris dans l'accord interentreprises"),
]:
    retain(number,
        f"Maintien intégral de la faculté de substitution au niveau {level}. L'exigence d'une stipulation expresse établit le consentement à l'éviction des accords de même objet ; elle n'est ni un agrément ni une déclaration administrative. La supprimer rendrait automatique un effet que les négociateurs peuvent actuellement écarter. Aucun doublon de dépôt n'est créé par ce texte.",
        f"Substitution limitée à {perimeter}, aux seules stipulations de même objet, y compris celles conclues antérieurement ou postérieurement. Les conditions de validité et les règles impératives du contrat unique restent distinctes ; cette règle d'articulation n'autorise aucun CDD nouveau ni fin automatique d'emploi. Aucun renvoi n'est ajouté.",
        f"La substitution facultative au niveau {level} permet déjà d'éviter l'accumulation de stipulations concurrentes ; maintien sans fusion nouvelle revendiquée.",
        f"Les accords effectivement conclus dans {perimeter} ne sont pas audités. Aucune économie nouvelle ni disparition des droits individuels n'est démontrée.",
        "Aucune charge nouvelle identifiée : la stipulation expresse de substitution reste une condition existante et aucun nouvel acte ou registre n'est exigé.")


guard = "Pour les contrats nouveaux relevant de l'article L. 1221-2, aucune stipulation ne peut rétablir un contrat à durée déterminée ni écarter la durée impérative du préavis individuel prévue à l'article L. 1234-1. Les dispositions transitoires relatives aux contrats antérieurs demeurent applicables. La réserve des stipulations plus favorables conserve notamment les indemnités conventionnelles ou contractuelles prévues à l'article L. 1234-9 ; elle ne transforme pas le préavis impératif des contrats nouveaux en un minimum conventionnel."
xml = paragraphs("Lorsqu'un employeur est lié par les clauses d'une convention ou d'un accord, ces clauses s'appliquent aux contrats de travail conclus avec lui, sauf stipulations plus favorables.", guard)
rewrite('L2254-1', xml,
    "Coordination du principe de faveur avec les dispositions impératives expressément retenues pour les nouveaux contrats. La règle d'application des clauses collectives reste entière ; la réserve de faveur ne peut réintroduire les CDD ou remplacer le préavis individuel de quinze jours. Les indemnités plus favorables et les contrats antérieurs restent protégés.",
    "L1234-1 proposé substitue quinze jours aux durées conventionnelles et contractuelles des seuls nouveaux contrats ; L1234-9 laisse les indemnités plus favorables hors du plafond légal. Il faut lire ces deux effets distinctement. Le point de départ dépend de la notification écrite selon L1234-3, non fourni comme cible dans ce lot et non nouvellement visé dans le corps. Les protections et procédures collectives ou spéciales ne sont pas supprimées.",
    "Le principe de faveur demeure et son articulation avec les deux règles impératives nouvelles est explicitée. Aucun allègement autonome ne s'ajoute ici au contrat unique.",
    "Cette disposition ne réécrit ni la notification, ni les motifs, ni les autorisations collectives ou de salariés protégés. Aucun montant individuel d'indemnisation n'est calculé.",
    "Aucune charge nouvelle identifiée : ni écrit individuel supplémentaire ni choix obligatoire. La réserve coordonne des règles décidées ailleurs sans réduire les indemnités plus favorables.",
    [effect('coordination', 'contrat-unique-coordination-accords',
        "Préservation du principe de faveur avec ses limites propres aux nouveaux contrats et au préavis impératif.",
        "Application des clauses collectives aux contrats, sous réserve de stipulations plus favorables, sans réserve relative au futur contrat unique.",
        "Même principe ; règles impératives de forme du contrat et de préavis réservées, indemnités plus favorables maintenues.",
        'regime', "Employeurs liés par une convention ou un accord et leurs salariés.",
        "Nouveaux contrats dans le champ de la réforme ; contrats antérieurs et indemnités plus favorables selon leurs régimes propres.",
        "Aucune formalité ajoutée et aucune nouvelle exclusion des indemnités favorables.",
        "ces clauses s'appliquent aux contrats de travail conclus avec lui, sauf stipulations plus favorables.", guard)])


xml = paragraphs(
    "Les conventions et accords sont applicables, sauf stipulations contraires, à compter du jour de leur dépôt auprès du service compétent, dans des conditions déterminées par voie réglementaire.",
    "Cette règle s'applique aux dépôts effectués à compter de l'entrée en vigueur de la loi. Elle ne dispense ni du dépôt ni du respect des conditions de validité et des délais légaux d'opposition. Les dates d'application des conventions et accords déjà déposés demeurent inchangées.")
rewrite('L2261-1', xml,
    "Réduction de fond circonscrite : suppression du décalage légal par défaut jusqu'au lendemain du dépôt. La date d'application devient le jour du dépôt, sans toucher aux stipulations contraires, au dépôt, aux majorités ni à l'opposition. Le gain concerne seulement les accords futurs déposés qui ne fixent pas une autre date.",
    "La faculté d'une date conventionnelle différente est conservée. Coordination d'application avec L2231-6 et L2261-8 : le dépôt auprès du service compétent suffit, sans attente d'une transmission au greffe ; le dépôt unique est déjà proposé à L2231-6 et n'est pas une nouvelle coupe du présent lot. Les textes réglementaires de dépôt et le récépissé doivent refléter cette date sans rétablir un jour d'attente. Pas de date de promulgation inventée.",
    "Par rapport à toute la source, un seul jour calendaire de décalage légal est retiré pour la règle supplétive ; aucun dépôt ou prélèvement n'est supprimé par cet article.",
    "Aucun gain pour les accords qui fixent eux-mêmes leur date d'effet ou les dépôts antérieurs. Aucun délai d'opposition n'est réduit et aucun coût global n'est chiffré.",
    "Aucune charge nouvelle identifiée : même dépôt et mêmes pièces ; application supplétive avancée d'un jour, avec liberté des parties de stipuler une date différente.",
    [effect('deadline_reduced', 'accords-collectifs-effet-jour-depot',
        "Suppression du jour d'attente supplétif entre dépôt et application.",
        "Sauf stipulations contraires, application le lendemain du dépôt : décalage d'un jour calendaire.",
        "Sauf stipulations contraires, application le jour du dépôt : aucun jour calendaire d'attente.",
        'calendar_days', "Conventions et accords déposés sans date d'application conventionnelle différente.",
        "Dépôts effectués à compter de l'entrée en vigueur ; dates anciennes et conditions de validité/opposition préservées.",
        "Le dépôt subsiste, sans acte de remplacement ni réduction des délais d'opposition.",
        "à partir du jour qui suit leur dépôt auprès du service compétent",
        "à compter du jour de leur dépôt auprès du service compétent")],
    ["Le décalage supplétif d'un jour calendaire après le dépôt auprès du service compétent est supprimé pour les dépôts futurs."])


retain('L2261-2',
    "Maintien intégral de la règle de rattachement à l'activité principale et de la faculté conventionnelle en cas de pluralité incertaine. Ce critère évite de choisir opportunément une convention pour écarter les minima et droits applicables. Les clauses réciproques de nature identique règlent un conflit réel de champ ; aucun agrément ni déclaration séparée n'est imposé ici.",
    "Conserver la condition cumulative de pluralité d'activités et d'incertitude, ainsi que la réciprocité et l'identité des clauses. Le texte n'exige pas de nouvelle notification publique du choix. Les changements d'activité relèvent aussi de L2261-14, dont la garantie de rémunération est coordonnée dans ce lot.",
    "Le rattachement conventionnel et sa faculté de résolution en cas d'incertitude sont conservés sans nouveau gain de simplification.",
    "Aucune analyse des activités d'une entreprise particulière ni des accords de réciprocité n'est fournie ; aucun changement automatique de branche n'est décidé.",
    "Aucune charge nouvelle identifiée : aucun critère, dépôt, délai ou document n'est ajouté au rattachement par l'activité principale.")


first = "Peuvent adhérer à une convention ou à un accord toute organisation syndicale représentative de salariés ainsi que toute organisation syndicale ou association d'employeurs ou des employeurs pris individuellement."
second = "Toutefois, si l'activité qu'ils exercent ou qu'exercent leurs adhérents n'entre pas dans le champ d'application de la convention ou de l'accord, leur adhésion est soumise aux dispositions des articles L. 2261-5 ou L. 2261-6, selon le cas."
third = "L'adhésion est notifiée aux signataires de la convention ou de l'accord, à la diligence de son ou de ses auteurs. Elle ne fait pas l'objet d'un dépôt administratif distinct. Les accords collectifs modifiant le champ d'application de la convention ou de l'accord restent soumis aux règles de dépôt qui leur sont applicables."
xml = paragraphs(first, second, third,
    "La dispense de dépôt distinct s'applique aux adhésions notifiées à compter de l'entrée en vigueur de la loi. Elle ne dispense ni de la notification ni de l'accord ou de l'agrément requis dans les cas prévus aux articles L. 2261-5 et L. 2261-6. Les effets des adhésions antérieures et les recours correspondants demeurent régis par les dispositions qui leur étaient applicables ; aucun nouveau dépôt d'une adhésion déjà régulièrement déposée n'est exigé.")
rewrite('L2261-3', xml,
    "Réforme de fond : retrait du dépôt administratif séparé de l'acte d'adhésion, qui n'apporte aucun nouveau contenu à l'accord déjà déposé lorsque son champ n'est pas modifié. La notification aux signataires assure leur information. Le dépôt d'un véritable accord modifiant le champ, le consentement hors champ, la représentativité et les droits des adhérents sont conservés ; aucune déclaration de remplacement.",
    "D2231-8, lu dans le corpus public, impose actuellement le dépôt des adhésions et dénonciations : retirer sa seule branche adhésion pour ce nouveau champ, conserver le dépôt des dénonciations et le récépissé des dépôts qui subsistent. L2231-6 reste applicable aux accords de L2261-5. Aucun texte du corpus en lecture seule n'est modifié ici. L2261-4 demeure applicable aux nouveaux adhérents sans faire de l'ancien dépôt une condition implicite de leurs droits. Notification ne vaut pas agrément hors champ.",
    "L'obligation de déposer séparément une adhésion est effectivement supprimée pour les notifications futures ; l'information privée et le dépôt des accords modifiant le champ restent. Ce retrait est distinct du dépôt unique des accords déjà proposé ailleurs.",
    "La coordination de D2231-8 reste à rédiger dans son lot réglementaire. Aucun nombre de dossiers évités ou solde national de coût n'est établi ; les adhésions antérieures gardent leur régime.",
    "Aucune charge nouvelle identifiée : la notification était déjà obligatoire, sans nouvelle attestation, formulaire ni transmission substitutive au dépôt supprimé.",
    [effect('obligation_removed', 'adhesion-collective-fin-depot-distinct',
        "Suppression du dépôt administratif distinct de l'acte d'adhésion.",
        "L'auteur doit notifier l'adhésion aux signataires puis la déposer selon les modalités réglementaires.",
        "Notification aux signataires seule pour l'acte d'adhésion ; les accords collectifs modifiant le champ restent déposés.",
        'legal_duty', "Organisations et employeurs auteurs d'une adhésion à une convention ou à un accord.",
        "Adhésions notifiées dès l'entrée en vigueur ; consentements hors champ et effets des adhésions antérieures protégés.",
        "Aucune déclaration de remplacement ; la notification existante et le dépôt des véritables accords collectifs subsistent.",
        "L'adhésion est notifiée aux signataires de la convention ou de l'accord et fait l'objet d'un dépôt dans des conditions prévues par voie réglementaire, à la diligence de son ou de ses auteurs.",
        "Elle ne fait pas l'objet d'un dépôt administratif distinct.")],
    ["L'obligation pour l'auteur de déposer administrativement un acte d'adhésion distinct est retirée pour les adhésions futures, sans supprimer le dépôt des accords modifiant le champ."])


retain('L2261-4',
    "Maintien intégral des droits de l'organisation représentative qui adhère à toutes les clauses : égalité avec les signataires, participation paritaire, gestion et révision. Ces avantages demeurent pour les adhésions futures, y compris celles dispensées de dépôt distinct par L2261-3 proposé. Les obligations identiques à celles des signataires sont la contrepartie de l'adhésion volontaire, sans justificatif administratif supplémentaire.",
    "La totalité des clauses et la représentativité dans le champ demeurent les conditions du régime ; aucune exigence nouvelle de signature initiale ou de dépôt n'est introduite. La réforme de l'accès à la procédure de révision en L2261-7 n'enlève aucun des droits déjà attachés à l'adhésion. Les organismes paritaires et institutions conservent leurs missions autonomes.",
    "Égalité des droits des adhérents avec les signataires conservée intégralement, sans privatiser les organismes ni réduire les avantages des futurs adhérents.",
    "Les statuts et accords créant les institutions ne sont pas examinés individuellement. Le maintien ne démontre aucune suppression nouvelle de cotisation ou de formalité.",
    "Aucune charge nouvelle identifiée : l'adhésion totale reste volontaire et l'article n'ajoute aucun dépôt ni déclaration aux droits paritaires.")

retain('L2261-5',
    "Maintien intégral du consentement collectif nécessaire à l'extension territoriale ou professionnelle du champ. Il ne s'agit pas d'un agrément administratif : un employeur ou une organisation ne doit pas imposer unilatéralement un nouveau champ aux autres parties. La forme d'accord garantit les parties et leurs droits ; le dépôt relève du régime déjà allégé des accords.",
    "L2231-1 a été lu dans le corpus : salariés représentatifs d'un côté, organisations ou employeurs habilités de l'autre. Le présent texte associe aussi les signataires du texte dont le champ change. La dispense de dépôt de L2261-3 ne couvre pas cet accord collectif. Aucun renvoi ajouté et aucun nouveau secteur inclus par la loi.",
    "La voie conventionnelle d'élargissement demeure accessible ; sa condition de consentement est nécessaire, sans suppression de charge revendiquée.",
    "Aucun accord sectoriel concret n'est analysé ; l'article ne remplace pas la procédure administrative distincte d'élargissement ministériel.",
    "Aucune charge nouvelle identifiée : les parties et la forme d'accord restent inchangées, sans nouvelle ratification ou autorisation administrative.")

retain('L2261-6',
    "Maintien intégral après examen du mot agrément : celui-ci exprime ici le consentement des organisations syndicales de salariés après négociation, non un visa administratif. Son retrait autoriserait l'employeur à appliquer hors champ une convention choisie sans leur accord. La négociation et le consentement effectif ont une fonction essentielle de protection, distincte du dépôt d'adhésion supprimé.",
    "L2232-16 a été lu dans le corpus public : il désigne les organisations représentatives dans l'entreprise et l'employeur, avec régime d'établissement et articulation avec les entreprises sans délégué syndical dans la proposition actuelle. La source présente de L2261-6 ne règle pas explicitement ce dernier cas : cette limite préexistante est signalée, aucune règle de majorité ou voie d'approbation n'est inventée. L2261-3 conserve expressément cet agrément privé hors champ.",
    "Aucun agrément public supprimable n'est identifié ; le consentement collectif à l'adhésion hors champ est conservé pour les situations futures.",
    "L'hypothèse d'une entreprise dépourvue d'organisations visées par L2232-16 n'est pas réglée expressément par la source et reste un point de concordance à contrôler, sans nouveau pouvoir unilatéral créé.",
    "Aucune charge nouvelle identifiée : négociation et consentement syndical sont ceux de la source, sans déclaration ou attestation administrative ajoutée.")


old = BY_NUMBER['L2261-7']['source_xml']
xml = old
xml = xml.replace("représentatives dans le champ d'application de la convention ou de l'accord et signataires ou adhérentes de la convention ou de l'accord ;", "représentatives dans le champ d'application de la convention ou de l'accord ;")
xml = xml.replace("b) Une ou plusieurs organisations professionnelles d'employeurs signataires ou adhérentes. Si", "b) Une ou plusieurs organisations professionnelles d'employeurs de la branche. Si")
xml += paragraphs("La suppression, au 1° du I, de la condition de qualité de signataire ou d'adhérent s'applique aux procédures de révision engagées à compter de l'entrée en vigueur de la loi. Elle n'affecte ni la validité des actes antérieurs ni les conditions de validité des avenants prévues au II. Elle n'emporte aucune révision automatique des conventions et accords existants.")
rewrite('L2261-7', xml,
    "Réforme de fond : suppression de la qualité obligatoire de signataire ou d'adhérent pour engager une révision pendant le cycle électoral initial. Les critères d'accès sont alignés sur ceux qui existent après le cycle, sans changer les conditions de validité, les majorités, l'opposition ou la représentativité patronale exigée en cas d'extension. Un non-signataire peut proposer une révision, pas imposer son contenu.",
    "Conserver I, 1°, 2°, leurs a) et b), puis II et son dernier alinéa. Les habilitations après le cycle restent entières, y compris l'exigence de représentativité dans le champ si l'accord est étendu. Les renvois aux sections 1 et 2 du chapitre II du titre III et au chapitre Ier du titre V du livre Ier conservent leur objet de validité et de représentativité. L2261-7-1 applique la même mesure à l'entreprise sans constituer une seconde mesure générale.",
    "L'exclusivité des signataires ou adhérents est retirée pour la seule initiative de révision pendant le premier cycle ; la validité du futur avenant et les droits des salariés restent soumis aux règles collectives existantes.",
    "Aucune durée maximale du cycle ni économie en jours n'est inventée. Les procédures déjà engagées et actes antérieurs conservent leur régime ; les majorités ne sont pas recalculées ici.",
    "Aucune charge nouvelle identifiée : l'ouverture de l'initiative ne crée ni réunion périodique, dépôt supplémentaire ni obligation d'accepter un avenant ; les garanties de validité demeurent.",
    [effect('regime_merged', 'revision-collective-fin-exclusivite-signataires',
        "Unification de l'habilitation à engager la révision avant et après la fin du cycle électoral.",
        "Pendant le cycle initial, organisation salariée représentative et signataire ou adhérente ; organisation patronale signataire ou adhérente, représentative si le texte est étendu.",
        "Pendant comme après le cycle : organisation salariée représentative ; organisation patronale de branche, représentative si le texte est étendu. Les conditions de validité des avenants restent entières.",
        'regime', "Organisations habilitées à engager la révision des accords interprofessionnels et conventions ou accords de branche.",
        "Procédures de révision engagées après l'entrée en vigueur ; actes antérieurs et accords existants préservés.",
        "Aucun consentement présumé, aucune nouvelle réunion imposée ; les règles de majorité et d'opposition demeurent.",
        "Une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord et signataires ou adhérentes de la convention ou de l'accord ;",
        "Une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord ;")],
    ["La condition d'être signataire ou adhérent pour engager une révision pendant le cycle initial est retirée pour les organisations salariées représentatives et les organisations patronales de branche."])


xml = paragraphs(
    "I. - Sont habilitées à engager la procédure de révision d'une convention ou d'un accord d'entreprise ou d'établissement :",
    "1° Jusqu'à la fin du cycle électoral au cours duquel cette convention ou cet accord a été conclu, une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord ;",
    "2° A l'issue de cette période, une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord.",
    "II. - La validité d'un avenant de révision s'apprécie conformément à la section 3 du chapitre II du titre III du présent livre II.",
    "La suppression, au 1° du I, de la condition de qualité de signataire ou d'adhérent s'applique aux procédures de révision engagées à compter de l'entrée en vigueur de la loi. Elle n'affecte ni la validité des actes antérieurs ni les conditions de validité des avenants prévues au II. Elle n'emporte aucune révision automatique des conventions et accords existants.")
rewrite('L2261-7-1', xml,
    "Réforme de fond de la même mesure que L2261-7 : une organisation représentative peut engager la révision d'un accord d'entreprise ou d'établissement dès le cycle initial sans devoir signer ou rejoindre le texte initial. La représentativité dans le champ et toutes les conditions de validité de l'avenant demeurent. Le simple déclenchement n'emporte ni modification ni accord présumé.",
    "Les I, 1°, 2° et II gardent leurs places. Le renvoi à la section 3 du chapitre II du titre III conserve les différentes voies et majorités de validité ; il ne rétablit ni les transmissions ni les délais supprimés dans les propositions L2232. Les droits attachés aux adhésions de L2261-4 subsistent. Cette application au niveau de l'entreprise partage l'identifiant de mesure de L2261-7.",
    "La restriction d'initiative pendant le cycle initial est effectivement supprimée au niveau de l'entreprise ; c'est l'application d'une même ouverture de la révision collective, sans baisse de majorité.",
    "Aucun délai de vote ou de négociation n'est diminué ici. Les procédures antérieures et la validité des accords conclus restent à leur régime ; aucun gain net global n'est chiffré.",
    "Aucune charge nouvelle identifiée : aucune consultation ou déclaration de remplacement n'est créée ; ouvrir l'initiative à une organisation représentative ne vaut pas obligation d'adopter sa proposition.",
    [effect('regime_merged', 'revision-collective-fin-exclusivite-signataires',
        "Alignement de l'habilitation à réviser un accord d'entreprise ou d'établissement pendant le cycle sur celle de l'après-cycle.",
        "Pendant le cycle initial, seules les organisations salariées représentatives signataires ou adhérentes sont habilitées à engager la révision.",
        "Organisation salariée représentative habilitée pendant et après le cycle, sans signature ou adhésion préalable ; validité de l'avenant inchangée.",
        'regime', "Organisations représentatives dans le champ des accords d'entreprise ou d'établissement.",
        "Procédures engagées dès l'entrée en vigueur ; accords existants et actes antérieurs non remis en cause.",
        "Aucun nouvel acte d'adhésion, mandat, transmission ou vote créé en remplacement de la condition supprimée.",
        "une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord et signataires ou adhérentes de cette convention ou de cet accord ;",
        "1° Jusqu'à la fin du cycle électoral au cours duquel cette convention ou cet accord a été conclu, une ou plusieurs organisations syndicales de salariés représentatives dans le champ d'application de la convention ou de l'accord ;")],
    ["La qualité obligatoire de signataire ou d'adhérent à l'accord d'entreprise ou d'établissement est supprimée pour engager sa révision pendant le cycle électoral initial."])


retain('L2261-8',
    "Maintien intégral de la substitution de plein droit de l'avenant aux seules stipulations modifiées. L'opposabilité à tous les employeurs et salariés liés évite une réadhésion individuelle ; le dépôt conserve une fonction de preuve et de connaissance du texte. Le dépôt unique est déjà traité dans la proposition de L2231-6 ; aucun second allègement n'est fabriqué ici.",
    "Le renvoi à L2231-6 a été lu dans le corpus : dépôt signé unique et transmission au greffe par le service dans la proposition, sans remise séparée par l'employeur. L2261-1 proposé avance seulement au jour du dépôt la date supplétive. L'ouverture de l'initiative de révision en L2261-7 et L2261-7-1 ne change pas les conditions de validité de l'avenant.",
    "Le mécanisme évitant un nouvel accord individuel de chaque salarié demeure ; cette souplesse existe déjà dans toute la source et n'est pas comptée à nouveau.",
    "La coordination réglementaire du dépôt unique est extérieure à cet article et n'est pas déclarée accomplie. Aucun gain supplémentaire de délai ou de coût n'est établi ici.",
    "Aucune charge nouvelle identifiée : maintien du même renvoi au dépôt, sans redépôt de l'accord initial ni consentement individuel supplémentaire.")

retain('L2261-9',
    "Maintien intégral de la possibilité de dénoncer et de son préavis supplétif de trois mois. Ce préavis collectif protège l'adaptation des parties et les droits de survie ; il ne concerne pas la rupture individuelle d'un contrat de travail et n'est pas ramené à quinze jours. Notification et dépôt de la cessation ont une fonction propre de preuve et d'information du champ conventionnel, distincte d'une simple adhésion.",
    "Conserver les quatre alinéas, la faculté de stipulation expresse différente et le point de départ des droits de survie de L2261-10, L2261-11, L2261-13 et L2261-14. D2231-8, lu dans le corpus, doit conserver la branche dénonciation lorsque la branche adhésion sera retirée. Ne pas rétablir par ce dépôt les doubles supports déjà supprimés à L2231-6 ; aucun nouveau renvoi normatif n'est introduit.",
    "Le préavis de dénonciation d'une norme collective et ses deux actes d'information sont conservés pour garantir la transition ; aucune réduction réelle n'est revendiquée.",
    "La durée conventionnelle peut être différente mais n'est pas connue dans ce lot. Ce maintien ne mesure pas la durée totale d'une négociation et ne concerne pas le préavis individuel.",
    "Aucune charge nouvelle identifiée : mêmes notification et dépôt, même préavis supplétif de trois mois et mêmes possibilités de stipuler autrement.")

retain('L2261-10',
    "Maintien intégral de la survie de l'accord dénoncé pendant un an après le préavis, ou davantage si prévu, et de la négociation à la demande d'une partie dans les trois mois du début du préavis. Il s'agit d'une borne maximale de déclenchement, non d'une attente minimale. La majorité exigée après perte de représentativité et la possibilité de négocier pendant le préavis protègent le consentement et évitent une rupture du socle collectif.",
    "Conserver les quatre alinéas, le secteur de L2261-12, l'alternative accord de substitution ou durée de survie et les suffrages exprimés au dernier alinéa. La note de la loi du 8 août 2016 vise la date de cessation des effets, même si la dénonciation est antérieure : ce champ historique subsiste. Le contrat unique ne transforme ni ce préavis collectif ni la durée d'un accord en durée d'emploi.",
    "Les droits de survie et la négociation pendant le préavis sont maintenus pour les dénonciations futures ; aucun calendrier plus court n'est prétendu créé.",
    "Les majorités et stipulations particulières de chaque accord restent à vérifier lors de sa dénonciation ; aucune économie ou indemnité de rupture n'est évaluée par cet article.",
    "Aucune charge nouvelle identifiée : l'ouverture de négociation, sa borne de trois mois et la condition de majorité sont intégralement celles de la source.")

retain('L2261-11',
    "Maintien intégral de la règle de dénonciation partielle : l'accord continue entre les autres signataires et produit encore effet à l'égard de ses dénonciateurs selon la survie d'un an ou la durée supérieure stipulée. Ces effets protègent des avantages collectifs futurs sans imposer une nouvelle adhésion. Les retirer ne serait pas une suppression de formalité mais une perte de droits.",
    "Conserver les deux alinéas, l'entrée en vigueur d'un texte substitutif et le calcul de l'année après l'expiration du préavis de dénonciation. Le préavis individuel de L1234-1 et le barème de L1234-9 ne s'appliquent pas à cette sortie d'une convention collective. La dénonciation partielle n'emporte aucune cessation automatique des emplois.",
    "Le maintien de l'accord entre les non-dénonciateurs et la protection transitoire des autres demeurent ; aucune obligation ou taxe nouvelle supprimée n'est comptée.",
    "Le texte ne résout pas les conditions particulières de validité d'une dénonciation concrète ; les préavis conventionnels plus longs ne sont pas évalués ici.",
    "Aucune charge nouvelle identifiée : les effets de survie et leur durée restent exactement ceux du texte officiel, sans rapport ou dépôt ajouté.")

retain('L2261-12',
    "Maintien intégral de la modification du champ lors d'une dénonciation sectorielle par l'organisation seule signataire d'un côté. Cette règle circonscrit les effets à la zone ou profession effectivement concernée et protège les autres secteurs. Aucun agrément, tableau, prélèvement ou pièce autonome n'est demandé ; une abrogation créerait une incertitude sur le champ plutôt qu'un allègement démontré.",
    "Maintenir le caractère seul signataire pour la partie employeurs ou salariés et la condition de secteur déjà inclus. Les garanties de L2261-10, L2261-11 et L2261-13 restent applicables dans leur champ ; aucun dépôt collectif n'est assimilé à un préavis individuel. Le texte ne permet pas une extension unilatérale du champ.",
    "La limitation territoriale ou professionnelle des effets demeure sans formalité nouvelle ; aucun gain de réduction n'est attribué à ce maintien.",
    "Aucun périmètre de convention concret n'est fourni ; la validité d'une dénonciation sectorielle et ses effets restent à apprécier selon les autres dispositions applicables.",
    "Aucune charge nouvelle identifiée : même condition de signataire unique et même effet de modification du champ, sans autorisation supplémentaire.")


definition_old = "Cette garantie de rémunération s'entend au sens de l'article L. 242-1 du code de la sécurité sociale, à l'exception de la première phrase du deuxième alinéa du même article L. 242-1."
definition_new = "Cette garantie de rémunération s'entend au sens de l'article L. 242-1 du code de la sécurité sociale, sans qu'une déduction pour frais professionnels puisse minorer la rémunération brute prise en compte. Cette coordination ne réduit aucun élément de rémunération compris dans la garantie avant l'entrée en vigueur de la loi ; cette protection s'applique également aux situations futures éligibles. Elle ne modifie pas les exclusions d'assiette ni le régime social ou fiscal des sommes versées."
historic = "Les dispositions du présent article demeurent applicables à tous les accords ou conventions dénoncés ou mis en cause ayant cessé de produire leurs effets à compter du 9 août 2016, y compris si la date de leur dénonciation ou de leur mise en cause est antérieure à cette date. La coordination de la définition de la garantie s'applique à compter de l'entrée en vigueur de la loi, sans diminution des droits déjà constitués, sans répétition de sommes régulièrement versées et sans remise en cause des décisions passées en force de chose jugée."
for number, trigger in [('L2261-13', 'dénonciation'), ('L2261-14', 'mise en cause')]:
    a = BY_NUMBER[number]
    assert definition_old in a['source_xml']
    xml = a['source_xml'].replace(definition_old, definition_new) + paragraphs(historic)
    rewrite(number, xml,
        f"Coordination nécessaire d'un renvoi ordinal préexistant devenu incohérent : le deuxième alinéa de L242-1 ouvre désormais le II des exclusions d'assiette. La référence générale à cet article est conservée, mais l'exception ordinale est remplacée par une règle explicite interdisant de minorer la rémunération brute par une déduction de frais professionnels. La garantie annuelle après {trigger}, ses bénéficiaires futurs et ses éléments antérieurement protégés demeurent, sans suppression d'exonération sociale ni application du barème de rupture à cette garantie.",
        "Incohérence préexistante signalée : la version actuelle fournie de L242-1 ne permet pas de lire littéralement l'ancienne exception comme un renvoi valide à une règle de déduction. Sa version historique n'est pas fournie ; la concordance historique de chaque élément de rémunération n'est donc pas présentée comme établie. La clause normative de non-réduction protège ces éléments, également pour les situations futures, et sépare le calcul de la garantie des exclusions sociales. Le contrôle de concordance historique reste un point précis à sécuriser, pas une validation revendiquée. Maintien du montant annuel, des douze mois de référence, de la durée de travail équivalente, de l'indemnité différentielle et de la note d'application aux cessations depuis le 9 août 2016. " + (
            "Le délai d'un an après préavis et le délai conventionnel supérieur demeurent ; cette indemnité différentielle n'est pas l'indemnité ordinaire de rupture de L1234-9."
            if number == 'L2261-13' else
            "Conserver les sept alinéas existants : le premier renvoi à L2261-9, la durée de survie, les 1° et 2° propres aux accords à durée déterminée et la borne de trois mois pour négocier. Une convention collective à durée déterminée n'est pas un CDD de travail ; son terme ne met fin à aucun emploi."),
        f"Correction du renvoi de définition de la garantie après {trigger}, avec maintien de tous les montants et délais protecteurs de la source. Aucun allègement de cotisation, ni nouvelle baisse de rémunération, n'est imputé à cette coordination.",
        "La version historique à laquelle renvoyait l'exception n'est pas dans les cibles fournies : neutralité historique détaillée non démontrée. La non-réduction normative des éléments garantis empêche de traiter cette incertitude comme une économie ; aucun solde financier ou national de complexité n'est établi.",
        "Aucune charge nouvelle n'est identifiée dans le dispositif : aucun nouveau registre, justificatif, taux, délai ou dépôt n'est créé. La garantie existante est protégée ; la vérification de concordance de ses éléments peut demander une analyse, dont le coût n'est pas évalué ni présenté comme nul.",
        [effect('coordination', 'garantie-remuneration-renvoi-assiette',
            f"Coordination de la définition de rémunération garantie après {trigger} avec la structure actuelle de L242-1.",
            "Définition par L242-1 assortie d'une exception visant la première phrase de son deuxième alinéa, désormais ouverture des exclusions d'assiette.",
            "Référence générale conservée ; règle expresse sur la rémunération brute sans déduction de frais et maintien de tous les éléments protégés, pour les situations futures aussi.",
            'other', f"Salariés bénéficiant de la garantie de rémunération après {trigger} d'une convention ou d'un accord.",
            "Application historique depuis les cessations d'effets du 9 août 2016 maintenue ; coordination prospective sans diminution des droits constitués ni réouverture des décisions définitives.",
            "Aucune nouvelle formalité ; exclusions sociales préservées ; contrôle de concordance historique à sécuriser.",
            definition_old, definition_new)])


retain('L2261-14-1',
    "Maintien intégral de la règle qui empêche la perte de représentativité de tous les signataires de mettre à elle seule l'accord en cause. Elle protège la continuité des droits et épargne une renégociation déclenchée par ce seul événement. Aucune formalité, taxe ou autorisation n'est imposée ; supprimer cette dispense retirerait un avantage utile.",
    "Le champ reste celui de toutes les organisations signataires perdant leur représentativité. La règle ne fige pas l'accord : les procédures de révision, désormais ouvertes selon les propositions de L2261-7 et L2261-7-1, restent utilisables. Aucun nouveau contrôle périodique de représentativité n'est ajouté.",
    "La dispense de mise en cause automatique est intégralement maintenue pour les futurs événements comme les situations existantes ; ce bénéfice préexiste au lot.",
    "Les résultats électoraux et procédures concrètes ne sont pas examinés. Aucun gain nouveau ni immunité générale contre révision ou dénonciation n'est démontré.",
    "Aucune charge nouvelle identifiée : aucun dossier, déclaration ou renouvellement de l'accord ne devient obligatoire par cette disposition maintenue.")

retain('L2261-14-2',
    "Maintien intégral de la négociation anticipée d'un accord de substitution lors d'une opération juridique. C'est déjà une faculté favorable permettant d'éviter des négociations successives. La limite de trois ans protège l'articulation avec les accords d'accueil et ne borne pas la durée des contrats de travail. La retirer pourrait prolonger des conditions moins favorables sans le concours des représentants de l'entreprise d'accueil prévu par une autre voie.",
    "Conserver les employeurs concernés, les syndicats représentatifs de l'entreprise d'origine, les contrats susceptibles d'être transférés, le premier alinéa de L2261-14, la prise d'effet à la réalisation de l'événement, la substitution pour le même objet et l'application finale des accords d'accueil. L2261-14-3 a été lu dans le corpus : il offre une voie distincte associant les employeurs et organisations des entreprises concernées ; aucune fusion de ces voies n'est inventée. Le terme de l'accord ne constitue pas un terme d'emploi.",
    "La faculté d'anticiper la substitution et sa transition de trois ans au maximum sont conservées ; aucune nouvelle suppression de régime ou de délai n'est comptée.",
    "Aucune opération de fusion ou transfert ni accord concret n'est fourni. Le maintien ne valide pas une durée d'emploi déterminée et ne mesure pas les coûts des négociations.",
    "Aucune charge nouvelle identifiée : la négociation demeure facultative, avec les mêmes parties et le même plafond de durée pour le seul accord collectif.")


# Analyses distinctes pour chaque source et chaque cible requise, sans élargir la liste.
CHECKS = {
 'L2253-3': {
  'L1234-1': "La priorité d'entreprise n'est pas une faculté de rétablir les préavis d'un ou deux mois : le corps ajouté réserve la durée impérative des contrats nouveaux. Les préavis et conditions d'ancienneté des contrats antérieurs restent préservés ; la computation à partir de la notification n'est pas modifiée ici.",
  'L1221-2': "Le renvoi général à L2253-1 peut toucher des matières de contrats spéciaux ; la proposition interdit expressément d'en déduire un nouveau CDD. Les anciens contrats suivent leur transition et la durée d'une mission ou formation n'est pas celle de l'emploi.",
  'L1234-9': "L'indemnité plus favorable reste possible malgré le plafond légal : la réserve ajoutée vise expressément cette faculté. Le seuil d'un an à la fin effective préavis inclus, les 0,20 mois sur l'ancienneté totale par mois complets et le plafond de six mois ne sont ni déplacés ni recalculés par la priorité conventionnelle.",
  'L2253-1': "Le renvoi vise les treize matières et la règle d'équivalence de garanties de la branche. Dans la proposition fournie, les 7°, 8° et 10° ne maintiennent les anciens CDD, chantiers et renouvellements d'essai que dans leur champ résiduel ou transitoire ; L2253-3 ne leur redonne pas un champ futur interdit. Le premier alinéa et son renvoi restent cohérents avec cette limite."
 },
 'L2254-1': {
  'L1234-1': "La réserve générale de faveur ne doit pas annuler la substitution impérative des quinze jours pour les contrats nouveaux. L'ajout l'indique expressément, tout en conservant le régime des contrats antérieurs ; il ne touche ni la notification écrite, ni le paiement sans exécution en cas de faute grave prévu par la cible proposée, ni les autorisations spéciales.",
  'L1221-2': "Les clauses collectives restent applicables aux contrats, mais aucune clause dite plus favorable ne peut autoriser une nouvelle embauche avec terme. Les contrats antérieurs et leurs créances restent à leur transition ; une durée limitée de mission n'est pas une fin automatique d'emploi.",
  'L1234-9': "La proposition de L1234-9 laisse l'indemnité contractuelle ou conventionnelle plus favorable hors du plafond légal : le principe de faveur est maintenu sur ce point. Il ne crée aucune indemnité ordinaire de démission et ne retire pas la première année du calcul une fois le seuil d'un an atteint à la fin effective, préavis compris."
 },
 'L2261-10': {
  'L1234-1': "Le préavis cité ici est celui de la dénonciation d'un accord collectif, non le préavis de licenciement de L1234-1. Les trois mois de L2261-9 et la survie d'un an sont donc maintenus ; les quinze jours des contrats nouveaux et la notification individuelle ne s'y substituent pas.",
  'L1221-2': "La durée de survie d'une convention dénoncée ne fixe aucun terme aux contrats de travail. Le maintien est compatible avec l'interdiction des nouveaux CDD et préserve les anciens contrats selon leur transition ; il ne crée ni reconduction de CDD ni rupture automatique à l'expiration de l'accord.",
  'L1234-9': "La survie de l'accord peut conserver une indemnité conventionnelle plus favorable, comme l'autorise la cible proposée. Elle ne règle pas le seuil d'un an, le préavis inclus ou les 0,20 mois par année totale de l'indemnité légale, et ne ramène pas ses droits transitoires à zéro."
 },
 'L2261-11': {
  'L1234-1': "Le délai de préavis auquel succède l'année de survie est celui de la dénonciation partielle d'une norme collective. Aucun licenciement individuel n'est notifié par cet acte ; appliquer quinze jours ou les seuils d'ancienneté des anciens licenciements serait une confusion de champs.",
  'L1221-2': "La continuation de l'accord entre les autres signataires et sa survie pour les dénonciateurs concernent une norme collective. Elles ne créent aucun CDD futur et ne mettent fin ni au contrat unique ni aux anciens contrats dont les droits sont maintenus dans leur transition.",
  'L1234-9': "Le maintien d'une convention peut protéger des droits indemnitaires plus favorables, sans les plafonner à six mois. La cible légale réserve le seuil d'un an à la fin effective avec préavis pour les contrats nouveaux et les parts anciennes pour les autres ; cet article ne change aucun de ces calculs ni les indemnités spéciales."
 },
 'L2261-13': {
  'L1234-1': "Le préavis déterminant ici le début de l'année est celui de dénonciation prévu à L2261-9 ; ce n'est pas celui de rupture individuelle de L1234-1. La garantie annuelle ne commence pas quinze jours après une notification de licenciement ; les régimes nouveaux et anciens de licenciement restent distincts.",
  'L1221-2': "La garantie de rémunération après extinction conventionnelle bénéficie aux salariés dans son champ, y compris les contrats uniques futurs. Aucun terme d'emploi n'est créé par la fin de la convention, et les anciens CDD ne sont ni renouvelés ni privés de leurs droits par cette coordination.",
  'L1234-9': "L'indemnité différentielle de rémunération est distincte de l'indemnité ordinaire de rupture. Elle n'est soumise ni au seuil d'un an d'ancienneté, ni au taux de 0,20 mois par année totale ou au plafond de six mois ; préavis inclus et droits de rupture anciens ne sont pas affectés.",
  'L242-1': "Le renvoi définit la rémunération garantie, non une nouvelle cotisation. La source et la proposition de L242-1 comportent un I d'assiette et un II d'exclusions : l'exception de première phrase du deuxième alinéa est préexistante et incohérente. Elle est remplacée par une règle explicite sur la rémunération brute sans déduction de frais, avec non-réduction des éléments protégés aussi pour l'avenir. La concordance avec la version historique absente n'est pas prétendue établie ; les exclusions sociales restent intactes."
 },
 'L2261-14': {
  'L1234-1': "Le premier alinéa vise explicitement L2261-9 : c'est le préavis collectif de mise en cause, distinct du préavis individuel de L1234-1. La survie d'un an et les clauses de durée supérieure ne sont pas comprimées à quinze jours ; les autorisations et procédures de rupture conservent leur champ.",
  'L1221-2': "Les 1° et 2° visent le terme d'une convention ou d'un accord collectif à durée déterminée, pas un contrat de travail. Leur maintien ne rétablit aucun CDD nouveau ; transferts et mise en cause n'effacent pas les droits des anciens contrats ni la durée indéterminée des nouveaux emplois.",
  'L1234-9': "L'indemnité différentielle du troisième alinéa sert à maintenir la rémunération annuelle, sans rupture nécessaire du contrat. Le zéro avant un an, le calcul de 0,20 mois sur toute l'ancienneté au seuil atteint avec préavis et le plafond légal ne lui sont donc pas applicables ; les indemnités spéciales et plus favorables restent distinctes.",
  'L242-1': "Le deuxième alinéa reprend une définition sociale de rémunération avec une exception ordinale obsolète ; le deuxième alinéa de la cible actuelle ouvre le II des exclusions et ne fournit pas la règle historique attendue. Le corps proposé retire ce renvoi ordinal, maintient la rémunération brute sans déduction de frais et interdit la réduction des éléments garantis pour les futurs bénéficiaires aussi. Les exonérations du II, les seuils d'indemnités et leur réforme propre restent sans modification ; la concordance historique détaillée reste à sécuriser."
 },
 'L2261-14-2': {
  'L1234-1': "La prise d'effet de l'accord à la réalisation de l'opération juridique ne constitue pas une notification de licenciement. Aucun préavis individuel, qu'il soit de quinze jours pour les contrats nouveaux ou plus long pour les anciens, ne se substitue au calendrier de cet accord collectif.",
  'L1221-2': "La limite de trois ans porte exclusivement sur l'accord de substitution anticipé. Elle ne fixe ni terme ni période d'essai aux emplois transférés : le contrat unique nouveau reste indéterminé et les contrats antérieurs conservent leurs droits et leur régime de transition, sans nouveau CDD autorisé.",
  'L1234-9': "L'accord de substitution ne rompt pas en lui-même les contrats transférés et ne déclenche donc pas l'indemnité ordinaire. Toute rupture ultérieure reste soumise à son champ : seuil d'un an à la fin effective préavis inclus pour le contrat nouveau, calcul sur l'ancienneté totale, droits anciens et indemnités plus favorables ou spéciales conservés."
 }
}

for a in SOURCES:
    number = a['number']
    out = ANSWERS[number]
    required = REFERENCES['requirements'][a['code_id'] + '|' + a['source_id']]
    checks = []
    for key in required:
        target = REFERENCES['targets'][key]
        checks.append(dict(target_key=key, view_sha256=target['view_sha256'],
                           assessment=CHECKS[number][target['number']]))
    out['reference_checks'] = checks

ordered = [ANSWERS[a['number']] for a in SOURCES]
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(ordered), 'articles')
