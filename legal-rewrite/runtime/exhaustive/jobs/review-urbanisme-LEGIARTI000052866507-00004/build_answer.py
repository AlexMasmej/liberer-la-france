import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}


def paragraphs(xml):
    return re.findall(r'<p>.*?</p>', xml, re.S)


def base(number):
    a = by_number[number]
    return {k: a[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


def impact(classification, assessment, scope, burdens, effects):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
        'new_burdens_review': burdens,
        'effects': effects,
    }


def effect(kind, measure, description, before, after, population, transition,
           replacement, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure,
        'description': description,
        'before': before,
        'after': after,
        'unit': 'legal_duty',
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': replacement,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


sru25 = (
    "Le texte initial de SRU, article 25, et sa piste documentaire ont été lus en entier : "
    "ajout de l'EPCI, remplacement du a relatif à l'élaboration et à la révision du SCOT et du PLU, "
    "abrogation du II et remplacement d'un accord communal par un avis. Ces modifications ne prouvent "
    "pas que toutes les règles actuelles descendent de SRU. La version historique L300-2, "
    "LEGIARTI000006815161, n'est pas une source disponible dans le corpus public fourni ; "
    "la recherche locale dans les pièces textuelles n'a pas retrouvé son corps historique. "
    "Filiation non close, exclue de tout décompte de volet SRU achevé ; aucun achèvement des 209 articles n'est revendiqué."
)

answer = []

# L103-2 : seules l'introduction et la transition portent la réforme ; les
# subdivisions de la source sont conservées sans réécriture de remplissage.
a = by_number['L103-2']
old = paragraphs(a['source_xml'])
prior = paragraphs(a['previous_draft']['proposed_xml'])
r = base('L103-2')
r.update(
    proposed_xml='\n'.join([prior[0], *old[1:], prior[-1]]),
    reason=(
        "Réforme de fond conservée après réexamen : l'obligation de concertation pendant toute la durée "
        "d'élaboration est supprimée ; subsiste une période suffisante sur les choix encore ouverts. "
        "La permanence du dispositif durant des phases purement techniques n'a pas de fonction essentielle "
        "distincte de cette participation utile. Les quatre catégories, les lettres a à f et chacun de leurs "
        "champs et renvois sont intégralement maintenus à droit constant, dans les termes de la source. "
        "Aucune catégorie supplémentaire n'est retirée : documents fixant l'usage des sols, ZAC, opérations "
        "modifiant substantiellement le cadre de vie et renouvellement urbain peuvent affecter directement "
        "l'environnement et les habitants ; le seul chevauchement des catégories ne démontre pas une deuxième "
        "procédure exigible pour un même objet. Aucun prélèvement, agrément, déclaration, justificatif ni délai "
        "minimal chiffré n'est institué ici. Cette coupe figurait déjà dans previous_draft : elle est conservée, "
        "sans gain supplémentaire revendiqué par rapport à ce brouillon. La transition protège les actes et "
        "observations antérieurs ainsi que la durée déjà annoncée au public."
    ),
    review_notes=(
        "Lecture et confrontation intégrales de la source et de previous_draft ; source_notes_xml vide, "
        "aucun tableau ni source_companions. Les onze alinéas initiaux, 1° à 4° et a à f, gardent leurs "
        "emplacements ; la transition seule est ajoutée à la fin. Renvois L. 146-1 et environnement L. 122-1 "
        "conservés. L. 103-7 et R. 103-3 ont été relus en entier : leurs dispenses pour opérations sensibles "
        "et travaux d'entretien ou de grosses réparations restent ouvertes aux situations futures. R. 103-1 "
        "conserve ses huit rubriques, notamment 5 000, 3 000 et 2 000 mètres carrés, 1 900 000 euros, "
        "150 places et 10 % ; R. 103-2 conserve l'agrégation des tranches sur moins de cinq ans. Ces seuils "
        "extérieurs ne sont pas modifiés. L. 103-1, L. 300-2, L. 600-11 et L. 104-1 à L. 104-8 ont été lus "
        "intégralement : la coupe de continuité ne vaut ni dispense d'évaluation ni remplacement d'une enquête "
        "ou participation environnementale autonome. Le respect de la participation utile et des exigences "
        "constitutionnelles et européennes reste à coordonner ; aucune conformité générale n'est attestée. "
        + sru25
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Obligation de maintenir la concertation pendant toute la durée d'élaboration du projet, y compris ses phases techniques sans choix nouveau à soumettre au public."
    ],
    substantive_impact=impact(
        'material_reduction',
        "Par rapport à toute la source officielle, seule la continuité obligatoire de la concertation est "
        "retirée ; les quatre catégories et les six lettres demeurent. Une durée suffisante et des choix "
        "encore ouverts restent exigés. Il s'agit de la coupe déjà portée par previous_draft, sans coupe "
        "additionnelle démontrée dans cette passe et sans baisse de prélèvement.",
        "Aucun nombre de jours économisés ni coût net n'est établi. Les dispenses de L. 103-7 et R. 103-3, "
        "les seuils réglementaires et les participations environnementales autonomes conservent leur champ. "
        "Les périodes déjà annoncées ne sont pas raccourcies sur ce seul fondement ; la filiation SRU25 reste incomplète.",
        "Aucune charge nouvelle n'est identifiée : pas de registre, dépôt, donnée ou attestation de remplacement. "
        "La durée suffisante relève déjà de L. 103-4 ; les choix encore ouverts explicitent la participation "
        "utile, et la transition conserve les observations déjà recueillies. Aucun solde global des codes n'est chiffré.",
        [effect(
            'obligation_removed',
            'urbanisme-concertation-fin-continuite',
            "Retrait de la concertation continue pendant toute l'élaboration, avec maintien d'une participation utile et suffisante.",
            "Habitants, associations locales et autres personnes concernées sont associés pendant toute la durée d'élaboration pour les catégories 1° à 4° ; aucun nombre uniforme de jours n'est fixé.",
            "Pour les mêmes catégories et participants, la concertation se déroule au cours de l'élaboration sur des choix encore ouverts pendant un temps suffisant, sans continuité imposée.",
            "Autorités organisatrices, porteurs des procédures et projets des 1° à 4°, habitants, associations locales et autres personnes concernées.",
            "Concertations nouvelles et en cours dès l'entrée en vigueur de la loi proposée ; actes et observations conservés, aucune nouvelle ouverture et aucune réduction du temps déjà annoncé sur ce seul fondement.",
            "Aucune formalité de remplacement ; les garanties de L. 103-4 et les participations autonomes subsistent.",
            "Font l'objet d'une concertation associant, pendant toute la durée de l'élaboration du projet, les habitants, les associations locales et les autres personnes concernées :",
            "Cette concertation porte sur les choix encore ouverts et dure le temps suffisant prévu à l'article L. 103-4, sans devoir couvrir toute la durée de l'élaboration :",
        )],
    ),
)
answer.append(r)

# L103-3 : conserver les attributions spéciales et rendre opératoire la
# publicité de la décision substituée, sans nouveau circuit.
a = by_number['L103-3']
old = paragraphs(a['source_xml'])
prior = paragraphs(a['previous_draft']['proposed_xml'])
new_organization = prior[5].replace(
    '</p>',
    " La décision du président est soumise aux mesures de publicité et d'information applicables "
    "à la délibération à laquelle elle se substitue, sans cumul des mêmes formalités pour le même objet.</p>",
)
r = base('L103-3')
r.update(
    proposed_xml='\n'.join([*old[:5], new_organization, prior[-1]]),
    reason=(
        "Réforme de fond maintenue : dans les cas du 3°, le président peut fixer les objectifs et modalités "
        "de toutes les concertations sans délégation ou délibération préalable, au lieu d'une faculté limitée "
        "aux opérations des 2° et 3° de L. 103-2 et aux concertations facultatives. Les renvois à L. 143-17, "
        "L. 153-11 et L. 300-2 font l'objet d'une dérogation expresse limitée à ces éléments d'organisation. "
        "Cette réduction était déjà acquise dans previous_draft. La présente passe précise la substitution "
        "des publicités existantes pour empêcher un circuit cumulatif ; elle ne compte pas cette coordination "
        "comme une seconde obligation supprimée. Les attributions spéciales des 1°, 1° bis et 2° sont "
        "maintenues intégralement à droit constant. La fixation d'objectifs et de modalités reste nécessaire "
        "pour que le public connaisse l'objet et les moyens de sa participation ; aucune justification ne "
        "permet d'en dispenser totalement l'autorité. Les décisions de prescription, d'arrêt et d'approbation "
        "portent sur le fond du document ou de l'opération et ne sont pas des doublons de cette organisation."
    ),
    review_notes=(
        "Source et previous_draft lus en entier ; notes vides, aucun tableau ou compagnon. Subdivisions et "
        "cinq premiers alinéas de la source intégralement conservés ; le sixième est remplacé et une transition "
        "finale ajoutée. Le f du 1° de L. 103-2 reste à son emplacement. La référence à SNCF Réseau et sa filiale "
        "au 5° de transports L. 2111-9 est conservée exactement ; le code des transports n'est pas fourni et "
        "son contenu n'est pas présenté comme vérifié. L. 143-16, L. 143-17, L. 153-8, L. 153-11 et L. 300-2 "
        "ont été lus en entier : les compétences territoriales, délibérations de prescription et notifications "
        "restent distinctes. Coordonner le libellé de ces textes et R. 143-14 II 1° et R. 153-20 II 1°, lus "
        "en entier, pour viser la décision du président sans rétablir un vote préalable. La publicité est "
        "rendue applicable dans le présent corps par substitution, sans nouvelle formalité cumulative. "
        "R. 143-14 vise actuellement le quatrième alinéa de L. 103-3, renvoi préexistant décalé à corriger "
        "expressément ; la note de L. 153-11 signale déjà le double L. devant L. 153-8. Aucune correction "
        "silencieuse d'un fichier extérieur. L. 600-11, lu intégralement, conserve son régime et ses recours. "
        + sru25
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Exigence d'une intervention préalable de l'organe délibérant pour fixer les seuls objectifs et modalités des concertations du 3° non couvertes par l'ancienne faculté présidentielle."
    ],
    substantive_impact=impact(
        'material_reduction',
        "La source entière réserve déjà une voie présidentielle aux 2° et 3° de L. 103-2 et aux concertations "
        "volontaires. Le gain concerne seulement les autres concertations relevant du 3° : le vote sur leurs "
        "objectifs et modalités cesse d'être obligatoire. Cette extension était déjà dans previous_draft ; "
        "la substitution expresse des publicités la coordonne sans gain supplémentaire compté.",
        "Les compétences de l'État, du préfet et de SNCF restent hors de l'extension. Les votes de prescription, "
        "d'arrêt et d'approbation ne sont pas retirés : aucun nombre de réunions évitées ni raccourcissement "
        "certain du calendrier n'est démontré, notamment lorsque le vote était déjà combiné à une autre décision.",
        "Aucune charge obligatoire nouvelle n'est identifiée : les objectifs et modalités restent ceux déjà "
        "exigés et leur publicité est celle de l'acte remplacé, sans cumul. La voie présidentielle est une "
        "faculté et n'impose pas un acte supplémentaire à l'autorité qui conserve la voie délibérative. "
        "Aucun registre, délai, justificatif ou autorisation de remplacement, ni solde global chiffré.",
        [effect(
            'obligation_removed',
            'urbanisme-concertation-competence-president',
            "Suppression du passage obligatoire devant l'organe délibérant pour les seuls objectifs et modalités dans les cas locaux nouvellement ouverts au président.",
            "Dans le 3°, intervention de l'organe délibérant, sauf faculté présidentielle pour les opérations des 2° et 3° de L. 103-2 ou les concertations non obligatoires ; aucune délégation générale expresse dans cet article.",
            "Faculté présidentielle pour toutes les concertations du 3° sans délégation ni délibération préalable sur ces seuls éléments ; compétences de fond et publicité substituée maintenues.",
            "Collectivités et établissements publics du 3°, pour les concertations ne bénéficiant pas déjà de la faculté présidentielle.",
            "Dès l'entrée en vigueur, y compris les concertations en cours ; objectifs et modalités antérieurs restent valables sans confirmation.",
            "Une décision d'organisation remplace le vote lorsqu'il est fait usage de la faculté ; même publicité sans cumul, pas de déclaration ni d'autorisation supplémentaire.",
            "Toutefois, lorsque la concertation est rendue nécessaire en application du 2° ou du 3° de l'article L. 103-2 ou lorsqu'elle est organisée alors qu'elle n'est pas obligatoire, les objectifs poursuivis et les modalités de la concertation peuvent être précisés par le président de l'organe délibérant de la collectivité ou de l'établissement public compétent.",
            "Dans les cas relevant du 3°, le président de l'organe délibérant de la collectivité ou de l'établissement public compétent peut toutefois préciser les objectifs et les modalités de toute concertation, obligatoire ou facultative, sans délégation ni délibération préalable de cet organe.",
        )],
    ),
)
answer.append(r)

# L103-4 : absence de réforme matérielle justifiée, donc source conservée,
# et non présentation d'un changement stylistique comme une simplification.
r = base('L103-4')
r.update(
    proposed_xml=None,
    reason=(
        "Maintien intégral nécessaire après lecture de la source et du brouillon : l'accès aux informations "
        "du projet et aux avis requis, une durée suffisante, des moyens proportionnés et la possibilité "
        "d'observations et propositions rendent effective la participation avant les décisions. "
        "L'enregistrement et la conservation protègent les contributions et leur contrôle contentieux ; "
        "aucune archive ou saisie en double n'est prescrite. L'article n'exige ni agrément, déclaration "
        "distincte, registre spécial, exemplaires multiples, justificatif du public, taxe ou délai minimal "
        "chiffré. Sa proportionnalité permet déjà d'adapter les moyens à chaque projet. Supprimer ces "
        "garanties ne retirerait pas un doublon démontré. Le brouillon précédent ne faisait que diviser la "
        "phrase source : cette reformulation sans réforme n'est pas reconduite. Le maintien de la source "
        "est compatible avec le retrait de la continuité en L. 103-2 et la concertation commune en L. 103-5."
    ),
    review_notes=(
        "Article et previous_draft relus intégralement, notes vides, aucun tableau ni compagnon. "
        "proposed_xml nul signifie reproduction intégrale de la source, avec son unique alinéa, non omission "
        "des modalités, avis, observations ou propositions. Pas de chiffre, date ou renvoi à corriger dans "
        "cet article. L. 103-1, L. 103-2 à L. 103-7, L. 300-2 et L. 600-11 ont été confrontés : les voies "
        "de concertation volontaire ou unique restent possibles, les dispenses restent ouvertes aux "
        "situations futures et les modalités proportionnées ne sont pas une obligation d'ajouter un support. "
        "Les obligations environnementales autonomes ne sont pas supprimées par le maintien de cette "
        "garantie commune. Aucun nouveau texte à droit constant n'est compté comme réécriture. "
        + sru25
    ),
    status='retained_unchanged',
    classification='retained_necessary',
    substantive_impact=impact(
        'retained_necessary',
        "La source officielle entière est maintenue. Ses exigences d'information, de temps suffisant, "
        "de moyens adaptés et de traçabilité des contributions ont une fonction de participation et de "
        "recours identifiable. Aucun doublon documentaire autonome à retirer n'est établi ; le brouillon "
        "stylistique antérieur n'est pas compté comme réécriture ou allègement.",
        "Ce maintien ne réduit ni les coûts d'organisation ni les durées effectives. Il ne valide pas "
        "l'ensemble des procédures environnementales ; les coupes de L. 103-2 et L. 103-5 sont évaluées "
        "dans ces articles seulement. La filiation historique avec SRU25 reste non établie dans son intégralité.",
        "Aucune charge nouvelle n'est identifiée puisque aucun mot de la source n'est modifié et aucun "
        "support, registre, donnée, justificatif ou délai n'est ajouté. Les obligations existantes sont "
        "assumées comme nécessaires ; aucune baisse nette de complexité de l'ensemble des codes n'est avancée.",
        [],
    ),
)
answer.append(r)

# L103-5 : la faculté favorable existante devient une équivalence opératoire,
# sans effacer les objets qui doivent effectivement être présentés au public.
a = by_number['L103-5']
r = base('L103-5')
r.update(
    proposed_xml=a['previous_draft']['proposed_xml'],
    reason=(
        "Réforme de fond conservée : la concertation sur l'opération vaut directement concertation sur "
        "la révision nécessaire, lorsque les deux objets sont effectivement accessibles à la participation. "
        "La décision spéciale autorisant leur réunion et la reprise des étapes déjà accomplies sont "
        "retirées ; les compléments manquants peuvent être traités dans la même procédure. Le droit source "
        "offre déjà la concertation unique : il ne s'agit donc pas de prétendre créer pour la première fois "
        "cette faculté favorable. Son bénéfice devient direct et reste ouvert aux opérations futures, "
        "avec option pour celles en cours. Le texte normatif de previous_draft est conservé en entier. "
        "Aucune coupe additionnelle n'est justifiée après examen : sans la présentation réelle des deux "
        "objets, une concertation sur l'opération seule ne permet pas au public d'influer sur la révision "
        "du document. Les conditions de champ, les objectifs et modalités, et les compétences distinctes "
        "d'approbation sont nécessaires à cette équivalence et ne constituent pas une formalité de remplacement."
    ),
    review_notes=(
        "Source et previous_draft lus intégralement ; texte précédent conservé sans reformulation "
        "supplémentaire, notes vides et aucun tableau ou compagnon. Maintien des 2° et 3° de L. 103-2, "
        "de la révision nécessaire, du SCOT, du document unique de L. 146-1 et du PLU. La réforme "
        "ne s'étend pas par silence aux modifications ou mises en compatibilité. L. 143-16 a été lu : "
        "un établissement compétent pour le SCOT garde ses attributions ; aucune commune ni EPCI "
        "dépourvu de compétence ne reçoit un pouvoir d'approbation. Les conditions de L. 103-4 "
        "restent intégrales et L. 103-3 coordonne la fixation des modalités. L. 300-2 a été lu en entier : "
        "concertation volontaire préalable au permis, simultanéité en ZAC lorsque le projet est "
        "suffisamment précis et concertation unique pour certaines déclarations de projet gardent leur "
        "champ et leurs avantages. L'enquête publique de son dernier alinéa pour les projets évalués "
        "reste requise dans son champ ; aucune dispense générale n'est déduite de la réunion des "
        "concertations. L. 103-6 assure un bilan commun et non une réduction supplémentaire autonome "
        "au titre du même regroupement. Les étapes régulièrement accomplies et la durée annoncée "
        "restent protégées, sans prétendre rouvrir une procédure achevée. "
        + sru25
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Décision spéciale de la commune ou de l'EPCI autorisant la réunion de la concertation sur l'opération et de celle sur la révision du document qui lui est nécessaire.",
        "Répétition des étapes communes de concertation déjà régulièrement accomplies, lorsque le public participe effectivement sur l'opération et sur la révision nécessaire."
    ],
    substantive_impact=impact(
        'material_reduction',
        "La source permet déjà une concertation unique sur décision de la commune ou de l'EPCI. La "
        "réduction démontrée est la suppression de cette décision spéciale et la non-répétition des "
        "étapes communes, avec équivalence directe et compléments ciblés. Ces coupes étaient déjà "
        "dans previous_draft ; le maintien de ce texte n'est pas un nouveau gain de seconde passe.",
        "Champ limité aux opérations des 2° et 3° exigeant la révision des trois documents désignés. "
        "Aucune économie nouvelle pour les procédures déjà réunies dans les mêmes conditions ; ni "
        "temps ni coût global économisé ne sont établis. Les enquêtes, évaluations, compétences "
        "d'approbation et procédures de L. 300-2 restent distinctes.",
        "Aucune charge nouvelle n'est identifiée : les deux objets étaient déjà soumis à concertation "
        "et doivent toujours être présentés. Une étape complémentaire ne porte que sur ce qui manque "
        "pour la révision, au lieu d'une reprise complète ; aucun dossier, agrément, registre ou délai "
        "supplémentaire n'est créé et aucun solde net de l'ensemble des codes n'est présumé.",
        [effect(
            'obligation_merged',
            'urbanisme-concertation-operation-revision-unique',
            "Équivalence directe des concertations sur l'opération et sa révision nécessaire, sans autorisation spéciale de réunion ni répétition des étapes communes.",
            "La commune ou l'EPCI peut décider de réunir les deux concertations ; la réunion est déjà autorisée par la source mais dépend de cette décision.",
            "La concertation sur l'opération vaut aussi pour la révision si les deux objets sont soumis au public ; les compléments sont intégrés à la même concertation et les étapes utiles ne sont pas recommencées.",
            "Communes et EPCI compétents, porteurs d'opérations des 2° ou 3° de L. 103-2 nécessitant une révision de SCOT, de document unique ou de PLU, et publics concernés.",
            "Concertations ouvertes après entrée en vigueur ; celles déjà engagées peuvent bénéficier de la réunion sans nouvelle ouverture, remise à zéro des délais ni réduction de la durée annoncée.",
            "Aucune autorisation ou déclaration de remplacement ; participation sur les deux objets et compétences de fond maintenues, avec compléments pour les seuls éléments manquants.",
            "la commune ou l'établissement public de coopération intercommunale compétent peut décider que la révision du document d'urbanisme et l'opération font l'objet d'une concertation unique.",
            "la concertation sur l'opération vaut également concertation sur cette révision, sans décision spéciale autorisant leur réunion, dès lors que le public peut être informé et présenter ses observations et propositions sur les deux objets dans les conditions de l'article L. 103-4.",
        )],
    ),
)
answer.append(r)

# L103-6 : distinguer la suppression de l'adoption du bilan de la simple
# coordination du bilan commun, qui n'est pas une seconde fusion.
a = by_number['L103-6']
r = base('L103-6')
r.update(
    proposed_xml=a['previous_draft']['proposed_xml'],
    reason=(
        "Réforme de fond conservée en entier : l'autorité établit le bilan sans décision ni délibération "
        "d'adoption et peut l'intégrer à un dossier existant. Le retrait porte sur l'acte d'adoption obligatoire, "
        "pas sur la simple possibilité de combiner des délibérations, déjà ouverte en droit source. Le bilan "
        "commun coordonne L. 103-5 sans constituer une deuxième fusion à compter. Après nouvel examen, "
        "la suppression du bilan lui-même n'est pas justifiée : les seules contributions brutes conservées "
        "en L. 103-4 ne remplacent pas une restitution intelligible de la concertation pour les décideurs et "
        "le public de l'enquête. Sa présence dans l'enquête et les présentations requises sur un fondement "
        "distinct sont donc maintenues à droit constant. Aucun rapport périodique ni support autonome "
        "n'est ajouté. Le texte normatif de previous_draft est repris sans nouvelle modification et sans "
        "gain additionnel revendiqué ; les actes anciens restent utilisables sans réadoption."
    ),
    review_notes=(
        "Source et previous_draft relus en entier ; un alinéa source avec deux séquences séparées par br, "
        "dont l'ordre est maintenu, puis une transition ajoutée ; notes vides, aucun tableau ou compagnon. "
        "Le renvoi L. 103-3 et le chapitre III du titre II du livre Ier du code de l'environnement sont "
        "conservés. La présence du bilan dès l'ouverture précise son insertion au dossier d'enquête, "
        "sans introduire de délai chiffré ou enquête nouvelle. R. 143-7, R. 153-3 et R*311-2 ont été relus "
        "en entier : ils permettent déjà le bilan simultané à l'arrêt du SCOT ou du PLU ou à l'approbation "
        "du dossier de ZAC. Coordonner leur vocabulaire d'adoption sans retirer ces décisions de fond, "
        "les pièces de ZAC ni la taxe d'aménagement distincte visée par R*311-2. R. 313-7 a été lu en "
        "entier : sa présentation patrimoniale devant l'organe délibérant demeure ; coordonner « qui en "
        "délibère » pour ne pas rétablir une adoption obligatoire du seul bilan, sans supprimer le débat "
        "ou les compétences conjointes du préfet et de la collectivité. Les bilans et insertions de L. 300-2 "
        "restent applicables dans leur champ ; L. 600-11 est maintenu. Ces textes extérieurs au lot ne "
        "sont pas présentés comme réécrits. "
        + sru25
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Obligation d'arrêter le bilan par une décision ou délibération d'adoption, distincte de son établissement et des décisions de fond relatives au projet ou au document."
    ],
    substantive_impact=impact(
        'material_reduction',
        "La source officielle exige que l'autorité arrête le bilan et le joigne à l'enquête. Le projet "
        "retire l'adoption obligatoire, tout en conservant établissement, information de l'enquête et "
        "présentations autonomes. Cette coupe est déjà dans previous_draft. Le bilan commun ne "
        "compte pas comme une seconde réduction de la mesure de concertation unique de L. 103-5.",
        "La source réglementaire permet déjà certains bilans dans une délibération de fond : aucune "
        "réunion distincte évitée dans tous les cas n'est démontrée. Les décisions relatives au SCOT, "
        "PLU, ZAC ou plan patrimonial subsistent. Les coordinations réglementaires signalées restent "
        "à exécuter hors lot ; ni coût net ni économie nationale ne sont chiffrés.",
        "Aucune charge nouvelle n'est identifiée : le bilan existait déjà et son intégration à un dossier "
        "est facultative ; le bilan commun couvre les objets déjà soumis au public. L'insertion dès "
        "l'ouverture explicite la disponibilité du dossier d'enquête, sans nouveau délai, registre, "
        "donnée ou dépôt de remplacement. Aucun solde global des codes n'est établi.",
        [effect(
            'obligation_removed',
            'urbanisme-concertation-bilan-sans-adoption',
            "Suppression de l'acte obligatoire d'adoption du bilan, avec maintien de son établissement et de sa présence au dossier d'enquête.",
            "À l'issue de la concertation, l'autorité de L. 103-3 arrête le bilan ; cette adoption peut déjà être combinée avec certaines décisions de fond.",
            "La même autorité établit le bilan sans décision ou délibération d'adoption ; les décisions de fond, présentations autonomes et informations du public restent exigées.",
            "Autorités de L. 103-3 établissant un bilan de concertation, collectivités et établissements publics concernés.",
            "Bilans établis après entrée en vigueur, y compris concertations en cours ; bilans anciens utilisables sans second bilan ou nouvelle adoption, aucune procédure achevée à rouvrir.",
            "Aucun visa, déclaration ou rapport de remplacement ; le bilan existant peut être intégré à un dossier préparatoire.",
            "A l'issue de la concertation, l'autorité mentionnée à l'article L. 103-3 en arrête le bilan.",
            "L'établissement de ce bilan n'est subordonné à aucune décision ni délibération d'adoption.",
        ), effect(
            'coordination',
            'urbanisme-concertation-operation-revision-unique',
            "Coordination du bilan avec la réunion des concertations de L. 103-5, sans comptage d'une seconde fusion.",
            "Un bilan est arrêté à l'issue de la concertation, y compris lorsque celle-ci est déjà unique selon L. 103-5 ; aucun double bilan général n'est expressément prescrit ici.",
            "Un bilan commun couvre chacun des objets de la concertation unique, sans nouveau gain autonome attribué à cet article.",
            "Autorités et publics d'une concertation unique sur une opération et la révision nécessaire de son document d'urbanisme.",
            "Bilans établis après entrée en vigueur ; bilans anciens conservés et aucune procédure achevée à rouvrir.",
            "Aucune donnée ou formalité supplémentaire : le bilan commun reste limité aux objets effectivement soumis à concertation.",
            "A l'issue de la concertation, l'autorité mentionnée à l'article L. 103-3 en arrête le bilan.",
            "Une concertation unique donne lieu à un bilan commun couvrant chacun de ses objets.",
        )],
    ),
)
answer.append(r)

# L104-1 : préserver le champ nécessaire ; ne pas fabriquer de suppression
# de la directive ou de dispense fermant une dérogation littorale.
r = base('L104-1')
r.update(
    proposed_xml=None,
    reason=(
        "Maintien intégral nécessaire de la source après examen des neuf catégories et du brouillon. "
        "Cet article délimite l'évaluation environnementale des documents d'aménagement et d'usage "
        "des sols, dans le cadre expressément cité de la directive 2001/42/CE et de ses annexes. "
        "L. 104-4 et R. 104-18 établissent sa fonction essentielle : incidences notables, solutions de "
        "substitution et prévention des effets sur la santé, les milieux et le patrimoine avant adoption. "
        "Aucune catégorie entière n'est démontrée dépourvue de cette fonction ; la supprimer ici créerait "
        "une dispense générale sans examen des incidences ni coordination supérieure. Il n'existe dans "
        "cet article ni taxe, cotisation, agrément distinct, déclaration annuelle, délai minimal ou pièce "
        "en double à retirer séparément. Le document unique du 3° bis A n'exige pas, par ce seul texte, "
        "deux évaluations parce qu'il vaut SCOT et PLU. Le brouillon antérieur était une reformulation "
        "à droit constant : il est remplacé par le maintien de la source, sans compter une réécriture. "
        "Les allègements distincts d'actualisation et de transmission proposés dans L. 104-3 et L. 104-6 "
        "ne sont ni annulés ni comptés une seconde fois dans ce lot."
    ),
    review_notes=(
        "Lecture intégrale de la source, de previous_draft et du contexte SRU202 ; notes vides, aucun "
        "tableau ou compagnon. Les neuf catégories, dont 3° bis A avant 3° bis, la directive du 27 juin "
        "2001 et ses annexes, L. 146-1, L. 122-26, L. 123-24-1 et CGCT L. 4433-7 et L. 4424-9 restent "
        "exactement dans la source qui sera reproduite en entier. L. 146-1, L. 122-26 et L. 123-24-1 "
        "ont été lus en entier ; les deux articles du CGCT et la directive ne sont pas fournis ici "
        "en corps intégral et ne sont pas présentés comme vérifiés ou réécrits. L. 104-2 à L. 104-8 "
        "et R. 104-18 ont été lus en entier. Les dispenses favorables de L. 104-3, y compris ses "
        "règles et transitions liées au 26 mai 2026, restent distinctes et ne sont pas fermées pour "
        "les procédures futures recevables. L. 104-2 3° continue à viser les schémas de plage "
        "de L. 121-28 : aucune fermeture des dérogations littorales, de leur évaluation ou de leurs "
        "procédures pour les nouvelles opérations. Environnement L. 341-16 et R. 122-17 I 50° et la "
        "franchise TASCOM QPV de 1 500 euros ne sont pas modifiés ni présentés comme réécrits. "
        "SRU202 a été lu dans toutes ses subdivisions I à XXXIX ; son XXXIX abroge notamment les "
        "anciens L. 121-10 et L. 121-12. La réutilisation ultérieure de numéros ne démontre pas que "
        "les obligations actuelles d'évaluation proviennent de cette loi. La concordance vers "
        "LEGIARTI000006814400, ancien L121-10, ne livre pas son corps historique dans le corpus "
        "fourni ; la recherche textuelle locale ne l'a pas retrouvé. Filiation réservée, aucun volet "
        "SRU202 ni examen des 209 articles déclaré achevé. Aucune conformité européenne générale "
        "ou économie nationale n'est affirmée."
    ),
    status='retained_unchanged',
    classification='retained_necessary',
    substantive_impact=impact(
        'retained_necessary',
        "Toute la source officielle est maintenue : neuf catégories de documents, numérotation, "
        "qualifications, directive, annexes et renvois. Le champ sert la prévention des incidences "
        "notables décrites par L. 104-4 et R. 104-18. Aucun doublon ou prélèvement supprimable n'est "
        "démontré dans ce seul article ; le brouillon stylistique n'est pas retenu comme allègement.",
        "Aucune baisse de coût ou de durée n'est établie. Les coordinations avec les textes européens "
        "et le CGCT restent hors du contrôle intégral disponible ; le contenu historique de la piste "
        "SRU202 manque. Les allègements distincts de L. 104-3 et L. 104-6 ne sont pas des gains de "
        "cet article et les schémas de plage et leurs avantages restent ouverts dans leur champ.",
        "Aucune charge nouvelle n'est identifiée : proposed_xml nul conserve exactement la règle source, "
        "sans catégorie, donnée, registre, délai ou condition ajoutés. Les évaluations existantes "
        "demeurent nécessaires ; ni nouvelle double évaluation du document unique ni bilan net "
        "de complexité ou de finances publiques n'est prétendu établi.",
        [],
    ),
)
answer.append(r)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
