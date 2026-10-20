import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
by_number = {item['number']: item for item in sources}
answers = {}


def impact(classification, assessment, scope, burdens, effects=None):
    return {
        'version': 1,
        'classification': classification,
        'assessment': assessment,
        'scope_limitations': scope,
        'new_burdens_review': burdens,
        'effects': effects or [],
    }


def effect(kind, measure_id, description, before, after, population, transition,
           replacement, source_quote, proposed_quote, unit='legal_duty'):
    return {
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': replacement,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


def base(number, proposed, reason, review, substantive):
    source = by_number[number]
    answers[number] = {
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': proposed,
        'reason': reason,
        'review_notes': review,
        'status': 'retained_unchanged' if proposed is None else 'rewrite_draft',
        'substantive_impact': substantive,
    }
    return answers[number]


def retained(number, reason, review, assessment, scope, burdens, benefit=None):
    entry = base(number, None, reason, review,
                 impact('retained_necessary', assessment, scope, burdens))
    entry['classification'] = 'retained_necessary'
    if benefit:
        entry['benefit_review'] = benefit


def reduced(number, proposed, reason, review, substantive, removed):
    entry = base(number, proposed, reason, review, substantive)
    entry.update({
        'change_type': 'normative_reduction',
        'reform_policy_id': 'editorial_direction_2026_10_19',
        'removed_provisions': removed,
    })
    return entry


exam_id = 'urbanisme-examen-conjoint-sans-reunion'
exam_transition = (
    "Examens nouveaux et examens en cours à l'entrée en vigueur des dispositions, "
    "sans reprise des actes régulièrement accomplis, réouverture des délais ou invalidation des procès-verbaux antérieurs."
)
exam_replacement = (
    "L'examen conjoint et son procès-verbal demeurent ; échanges écrits facultatifs entre tous les participants, "
    "sans nouvelle déclaration, autorisation, plateforme, attestation ou délai minimal."
)

proposed = """<p>Lorsqu'il y a lieu de procéder à l'examen conjoint des dispositions proposées pour assurer la mise en compatibilité du plan local d'urbanisme prévue par les articles L. 153-49 et L. 153-54, cet examen conjoint a lieu avant l'ouverture de l'enquête publique, à l'initiative de l'autorité chargée de la procédure. Cet examen peut être conduit par des échanges écrits entre l'ensemble des participants, sans réunion obligatoire. Ces échanges permettent à chaque participant de prendre connaissance des contributions des autres et de présenter ses observations avant la clôture de l'examen. Lorsque l'examen est conduit par écrit, la transmission à un stade précoce prévue à l'article R. 104-29 intervient avant l'ouverture de ces échanges.</p>
<p>Le procès-verbal de l'examen conjoint est joint au dossier de l'enquête publique.</p>
<p>Ces modalités s'appliquent aux examens conjoints engagés à compter de l'entrée en vigueur des présentes dispositions ainsi qu'à ceux en cours, sans reprise des actes régulièrement accomplis ni réouverture des délais. Les procès-verbaux établis auparavant restent utilisables.</p>"""
reduced(
    'R153-13', proposed,
    "Réforme de fond : la réunion n'est plus le passage obligé de l'examen conjoint. Une voie écrite collective est ouverte, avec accès réciproque aux contributions ; elle ne se réduit pas à juxtaposer des avis isolés. À droit constant restent les participants légaux, l'initiative de l'autorité chargée de la procédure, l'antériorité à l'enquête et le procès-verbal public. La saisine environnementale précoce reçoit un repère adapté au mode écrit.",
    "L153-52 et L153-54, lus avec L153-49, maintiennent l'examen conjoint, les personnes publiques de L132-7/L132-9 et l'invitation des maires concernés ; aucun participant n'est écarté. R153-14, R153-16 et R153-17 sont coordonnés dans ce lot. R104-29, lu en entier avec R104-30 à R104-33, vise encore la réunion : le présent corps fixe expressément son équivalent temporel pour le seul examen écrit du PLU. Aligner aussi cette terminologie dans un décret de coordination de R104-29, sans modifier ses autres régimes ni les décisions, consultations et délais environnementaux applicables. Les SCoT et L173-3 conservent leurs procédures propres. Le renvoi source à L153-49 vise le déclenchement ; le fondement de l'examen dans ce cas reste L153-52. Aucune filiation SRU globale ni clôture des 209 articles n'est affirmée.",
    impact(
        'material_reduction',
        "La source officielle entière impose le procès-verbal d'une réunion ; la proposition retire le caractère obligatoire de cette modalité pour les mises en compatibilité du PLU. Elle conserve la fonction collective, la trace et l'information préalable du public. Le gain concerne l'organisation de la réunion, pas une suppression de l'examen ou de l'évaluation environnementale.",
        "Pas d'extension aux examens propres aux SCoT, au schéma de secteur ou aux autres documents. Les délais d'enquête et de décision ne sont pas diminués. Les frais et temps évités ne sont pas chiffrés ; la coordination terminologique générale de R104-29 est identifiée hors lot.",
        "Aucune charge nouvelle autonome n'est identifiée : la voie écrite est facultative, le procès-verbal et l'examen de tous les participants étaient déjà exigés. L'accès réciproque aux contributions conserve le caractère conjoint ; la saisine environnementale demeure préalable. Aucun registre, certification, donnée ou calendrier supplémentaire n'est créé.",
        [effect(
            'obligation_removed', exam_id,
            "Retrait de la réunion obligatoire comme modalité unique de l'examen conjoint du PLU.",
            "Examen conjoint avant enquête avec procès-verbal d'une réunion ; aucune alternative écrite expressément ouverte par cet article.",
            "Examen conjoint avant enquête possible par échanges écrits collectifs ; réunion facultative et procès-verbal maintenu.",
            "Autorité chargée de la mise en compatibilité du PLU et ensemble des participants légaux.",
            exam_transition, exam_replacement,
            "Le procès-verbal de la réunion d'examen conjoint est joint au dossier de l'enquête publique.",
            "Cet examen peut être conduit par des échanges écrits entre l'ensemble des participants, sans réunion obligatoire.",
        )],
    ),
    ["Organisation obligatoire d'une réunion pour accomplir l'examen conjoint du PLU, remplacée par une faculté d'échanges écrits collectifs sans suppression de l'examen."],
)

for number, reason, review, assessment in [
    (
        'R153-14',
        "Coordination nécessaire de la mise en compatibilité liée à une déclaration d'utilité publique : le procès-verbal transmis est celui de l'examen conjoint, désormais réalisable sans réunion obligatoire selon R153-13. Le reste du corps est intégralement conservé : dossier éventuellement modifié, avis, observations et résultats de l'enquête, rapport, conclusions, organe consulté, deux mois et avis tacite favorable. Aucune seconde réduction de formalité n'est revendiquée.",
        "L153-57 1° et L153-58 1°, lus en entier, justifient l'avis local après enquête et l'approbation par la déclaration d'utilité publique ; l'avis ne peut être supprimé par cette seule coordination réglementaire. Le délai de deux mois n'est ni un préavis ni un délai fiscal. La source ne précise pas ici son point de départ ; aucune nouvelle règle n'est inventée. La transition des examens et la validité des anciens procès-verbaux résultent de R153-13 proposé.",
        "Seule la désignation du procès-verbal change pour accepter le résultat de l'examen écrit. Ni avis local supplémentaire, ni seconde réunion, ni réduction additionnelle de délai ou d'impôt n'est créée ou comptée.",
    ),
    (
        'R153-16',
        "Coordination nécessaire du procès-verbal avec la faculté d'examen conjoint écrit de R153-13. Le corps conserve les deux cas de déclaration de projet, tous les porteurs énumérés, les autorités de conduite et d'enquête, les pièces, les deux délais de deux mois, la substitution préfectorale et les notifications. Le doublon rédactionnel de compétence pour un établissement public de l'État est signalé dans les notes, sans lui attribuer un gain matériel.",
        "L153-55 1° b, L153-57 2° et L153-58 4°, lus intégralement, distinguent enquête d'État, décision locale et substitution préfectorale. Le délai local court de la réception de l'avis de l'enquêteur ; le délai préfectoral de notification court de la réception de l'ensemble du dossier en préfecture. Ces deux points de départ sont conservés. Anomalie préexistante conservée et signalée : la phrase d'autorité répète « ou, lorsque le projet émane d'un établissement public dépendant de l'Etat, par le président du conseil d'administration » après une attribution qui inclut déjà ce cas ; ce doublon ne crée pas deux approbations. Le renvoi au 5° de L2111-9 du code des transports est conservé ; sa cible hors corpus n'a pas été fournie et n'est pas déclarée vérifiée. Aucun changement de compétence n'est déduit de la répétition. Transition commune de R153-13.",
        "La source entière reste opératoire pour les mêmes porteurs et les mêmes décisions ; seul le terme relatif au procès-verbal est coordonné. La réunion facultative relève d'une seule mesure portée par R153-13, sans nouvelle réduction comptée ici.",
    ),
    (
        'R153-17',
        "Coordination nécessaire du procès-verbal avec l'examen conjoint écrit prévu par R153-13. Les deux hypothèses de projet d'État, l'absence de déclaration d'utilité publique, la consultation locale sur le dossier complet, les deux mois, l'avis tacite favorable, l'arrêté préfectoral et son effet d'approbation du PLU sont intégralement maintenus. Aucune nouvelle suppression d'avis n'est annoncée.",
        "L153-57 1° impose l'avis local après enquête pour la déclaration de projet adoptée par l'État ; L153-58 2° prévoit l'approbation par cette déclaration. Ces textes ont été lus entièrement. Le maintien des observations du public, résultats d'enquête, rapport et conclusions interdit de traiter le procès-verbal comme leur substitut. L126-1 du code de l'environnement reste une base distincte, dont le texte hors corpus n'est pas fourni. Deux mois et sens favorable du silence inchangés ; pas de nouveau point de départ ajouté. Transition commune de R153-13.",
        "L'acceptation du procès-verbal d'un examen écrit évite un renvoi qui rétablirait la réunion. L'article n'abolit ni la déclaration de projet ni l'avis local requis par la loi et n'est pas une deuxième réduction.",
    ),
]:
    source = by_number[number]['source_xml']
    proposed = source.replace("procès-verbal de la réunion d'examen conjoint", "procès-verbal de l'examen conjoint")
    assert proposed != source
    base(
        number, proposed, reason, review,
        impact(
            'coordination_only', assessment,
            "La faculté nouvelle est portée par R153-13 et ses conditions transitoires. Cet article conserve son propre champ, ses pièces et ses délais ; aucun coût net ni réduction supplémentaire n'est démontré par le seul changement de désignation du procès-verbal.",
            "Aucune charge nouvelle identifiée : mêmes destinataires, même dossier et même procès-verbal, sans attestation ni nouvelle transmission. Le mode écrit autorisé à R153-13 n'ajoute pas une pièce au dossier existant.",
            [effect(
                'coordination', exam_id,
                "Acceptation du procès-verbal d'examen conjoint, y compris lorsque l'examen se déroule par écrit.",
                "Le texte désigne le procès-verbal de la réunion d'examen conjoint.",
                "Le texte désigne le procès-verbal de l'examen conjoint ; les autres pièces, autorités et délais sont conservés.",
                "Autorités et porteurs de projet relevant du champ propre de l'article " + number + ".",
                exam_transition, exam_replacement,
                "le procès-verbal de la réunion d'examen conjoint",
                "le procès-verbal de l'examen conjoint",
            )],
        ),
    )

retained(
    'R153-15',
    "Maintien intégral après examen : l'article réunit déjà la déclaration de projet et l'approbation des nouvelles dispositions du PLU dans un même acte lorsque la commune ou l'EPCI compétent porte l'opération. Il répartit les compétences sans agrément, déclaration supplémentaire, minimum d'attente, justificatif ou prélèvement propre. Supprimer cette règle retirerait la voie intégrée favorable au lieu d'alléger une charge autonome.",
    "Confronté aux sources entières L153-54, L153-55, L153-57 2° et L153-58 2° : enquête et examen conjoint restent distincts de l'adoption de la déclaration. La faculté écrite de R153-13 s'appliquera sans modification de cet article, qui ne prescrit aucune réunion. L126-1 environnement n'est pas fourni dans le corpus ; maintien du renvoi sans prétendre réécrire cette loi extérieure. L300-6 demeure la seconde voie expressément visée.",
    "Le texte permet déjà une seule décision locale pour le projet et sa mise en compatibilité. Aucun doublon autonome de dépôt, de taxe ou d'autorisation n'a été identifié dans son corps entier ; sa suppression affaiblirait la lisibilité de cette voie intégrée.",
    "Aucun gain nouveau attribué à cet article. Les conditions d'intérêt général, d'enquête et d'évaluation demeurent dans leurs articles propres ; aucun effet budgétaire ou délai global n'est évalué.",
    "Aucune charge nouvelle identifiée, puisque le texte source est maintenu intégralement. Aucun formulaire, donnée, délai ou approbation supplémentaire n'est ajouté à l'acte intégré existant.",
    "L'effet favorable est l'approbation des nouvelles dispositions du PLU par la déclaration de projet elle-même. Il demeure ouvert aux opérations futures relevant des 1° ou 2°, avec les mêmes compétences et conditions ; aucun droit n'est cantonné au stock ancien.",
)

fiscal_id = 'urbanisme-suppression-envoi-fiscal-annexes'
fiscal_source = "La direction départementale ou, le cas échéant, régionale des finances publiques reçoit communication, à l'initiative du maire, de l'annexe du plan local d'urbanisme consacrée aux servitudes d'utilité publique affectant l'utilisation du sol."
proposed = """<p>La mise à jour du plan local d'urbanisme est effectuée chaque fois qu'il est nécessaire de modifier le contenu des annexes prévu aux articles R. 151-51 et R. 151-52, et notamment le report en annexe du plan des servitudes d'utilité publique mentionnées à l'article R. 151-51.</p>
<p>Un arrêté du président de l'établissement public de coopération intercommunale compétent ou du maire constate dans chaque cas qu'il a été procédé à la mise à jour du plan.</p>
<p>Aucune communication distincte de l'annexe consacrée aux servitudes d'utilité publique à la direction départementale ou régionale des finances publiques n'est requise au titre du présent article. Cette suppression s'applique aux communications restant à effectuer à l'entrée en vigueur des présentes dispositions, y compris pour les mises à jour déjà réalisées. Elle ne remet en cause ni les mises à jour ni les communications antérieures régulièrement effectuées. Les transmissions à l'Etat prévues à l'article L. 133-2 demeurent applicables.</p>"""
reduced(
    'R153-18', proposed,
    "Réforme de fond : suppression de l'envoi distinct de l'annexe des servitudes à la direction des finances publiques, sans déclaration de remplacement. La transmission électronique du PLU modifié à l'État existe déjà selon L133-2 ; retirer l'envoi sectoriel retire une obligation positive, et ne se borne pas à rappeler l'interdiction de redemander une pièce. La mise à jour de toutes les annexes et l'arrêté qui la constate restent intégralement exigés.",
    "Sources lues : R151-51, R151-52, L133-1 à L133-5 et R153-20 II 8°/R153-22. Le renvoi à R151-52 maintient notamment son 5° relatif aux schémas d'aménagement de plage : aucune annexe ou dérogation littorale n'est fermée. L'arrêté reste publié suivant R153-20 II 8° ; aucun renvoi n'est orphelin. La règle ne prétend pas que chaque agent fiscal dispose déjà de toutes les données et n'ouvre aucun accès nouveau à des données protégées. R163-8 comporte une communication fiscale analogue pour les cartes communales : coordination distincte identifiée hors lot, non présentée comme supprimée. Les transmissions à l'État et les mises à jour ne sont pas abolies par l'économie de cet envoi.",
    impact(
        'material_reduction',
        "Une obligation positive d'envoi d'une annexe aux services fiscaux disparaît par comparaison avec la source entière. Toutes les mises à jour, servitudes, annexes et leur constatation sont maintenues ; aucun impôt ou tarif n'est modifié.",
        "La suppression concerne seulement le PLU et la communication prescrite par R153-18. L'envoi analogue de R163-8 reste hors lot. Les modalités d'accès internes de l'État et le montant des frais évités ne sont pas établis ; aucun solde de l'ensemble des codes n'est chiffré.",
        "Aucune charge nouvelle identifiée : ni portail ni nouvelle transmission ne remplace l'envoi supprimé. L133-2 impose déjà la transmission à l'État des documents modifiés ; l'arrêté de mise à jour préexistait et reste soumis à sa publicité existante.",
        [effect(
            'obligation_removed', fiscal_id,
            "Suppression de la communication fiscale distincte de l'annexe des servitudes du PLU.",
            "À chaque mise à jour concernée, communication de l'annexe des servitudes aux finances publiques à l'initiative du maire, en plus de la transmission légale du document à l'État.",
            "Plus d'envoi distinct aux finances publiques sur ce fondement ; transmission légale à l'État, annexion et arrêté inchangés.",
            "Maires et services responsables des mises à jour de PLU ; directions départementales ou régionales des finances publiques.",
            "Communications non encore réalisées à l'entrée en vigueur, même relatives à une mise à jour antérieure ; actes et communications régulièrement accomplis préservés.",
            "Aucun dépôt, accès à des données, justificatif ou envoi sectoriel de remplacement ; maintien de L133-2.",
            fiscal_source,
            "Aucune communication distincte de l'annexe consacrée aux servitudes d'utilité publique à la direction départementale ou régionale des finances publiques n'est requise au titre du présent article.",
        )],
    ),
    ["Communication distincte au service départemental ou régional des finances publiques de l'annexe du PLU consacrée aux servitudes d'utilité publique, à l'initiative du maire."],
)

report_id = 'urbanisme-abrogation-plu-support-motifs-unique'
proposed = """<p>L'abrogation d'un plan local d'urbanisme est prononcée par l'organe délibérant de l'établissement public de coopération intercommunale compétent ou par le conseil municipal après enquête publique menée dans les formes prévues par le chapitre III du titre II du livre Ier du code de l'environnement.</p>
<p>Le dossier soumis à l'enquête publique expose, dans un rapport ou dans le projet de délibération qui lui est joint, les motifs et les conséquences juridiques de l'abrogation projetée. Lorsque ces éléments figurent dans le projet de délibération, aucun rapport distinct n'est exigé.</p>
<p>Cette faculté s'applique aux dossiers dont l'enquête publique n'est pas encore ouverte à l'entrée en vigueur des présentes dispositions. Les enquêtes déjà ouvertes se poursuivent sans remplacement de leur dossier ni reprise des actes régulièrement accomplis.</p>"""
reduced(
    'R153-19', proposed,
    "Réforme de fond limitée au support : le rapport n'est plus un document obligatoirement distinct lorsque le projet de délibération soumis au public expose lui-même tous les motifs et toutes les conséquences juridiques de l'abrogation. La commune ou l'EPCI peut conserver la présentation par rapport. L'enquête, son contenu informatif et l'autorité délibérante restent à droit constant ; il ne s'agit ni d'une dispense de participation ni d'une abrogation automatique du PLU.",
    "L'intégralité des deux exigences de la source est reprise : décision par l'organe délibérant compétent après enquête environnementale et information sur motifs et conséquences. Le projet de délibération n'est pas une nouvelle pièce obligatoire : il constitue seulement une alternative au rapport pour ces informations. Les formalités de publication de la délibération restent celles de R153-20 II 2° et R153-22, lus dans le corpus. La réforme n'affecte pas les autres pièces éventuellement imposées par le droit de l'environnement, dont les dispositions extérieures au corpus n'ont pas été intégralement fournies. Transition sans reprise des enquêtes déjà ouvertes.",
    impact(
        'material_reduction',
        "La source impose un rapport exposant motifs et conséquences ; la proposition permet de réunir ce contenu dans le projet de décision déjà joint au dossier. Le document distinct peut ainsi être retiré, mais aucune information ni étape de participation n'est supprimée. Le gain suppose le choix de cette présentation commune.",
        "Pas de dispense d'enquête, d'évaluation requise ailleurs ou de motivation. Aucun gain pour les dossiers continuant à utiliser un rapport et aucune réfection des dossiers d'enquête déjà ouverts. Temps et coût de préparation évités non chiffrés.",
        "Aucune charge nouvelle obligatoire identifiée : le rapport existant reste une voie suffisante. Le projet de délibération n'est joint que si cette alternative est choisie ; mêmes informations, aucun registre, délai minimal ou validation de remplacement.",
        [effect(
            'obligation_merged', report_id,
            "Possibilité de réunir dans le projet de délibération l'exposé imposé pour l'abrogation du PLU, sans rapport séparé.",
            "Rapport imposé au dossier d'enquête exposant motifs et conséquences juridiques de l'abrogation, même si le projet de délibération les expose déjà.",
            "Un seul support possible pour le projet de délibération et cet exposé ; rapport séparé requis seulement si le dossier ne présente pas ces informations dans le projet de délibération.",
            "Communes et EPCI préparant l'abrogation d'un PLU ; public participant à l'enquête.",
            "Dossiers dont l'enquête n'est pas encore ouverte lors de l'entrée en vigueur ; dossiers des enquêtes déjà ouvertes conservés.",
            "Contenu complet des motifs et conséquences préservé ; projet de délibération facultatif comme support commun, sans approbation ni déclaration supplémentaire.",
            "Le dossier soumis à l'enquête publique comprend un rapport exposant les motifs et les conséquences juridiques de l'abrogation projetée.",
            "Lorsque ces éléments figurent dans le projet de délibération, aucun rapport distinct n'est exigé.",
        )],
    ),
    ["Rapport obligatoirement séparé pour exposer les motifs et conséquences de l'abrogation du PLU lorsque le projet de délibération joint au dossier contient déjà intégralement cet exposé."],
)

retained(
    'R153-20',
    "Maintien intégral : l'article répartit les actes entre les deux régimes de publicité, sans imposer lui-même de dossier, de taxe ou d'agrément supplémentaire. Ses listes permettent de connaître les décisions qui affectent les droits à construire, l'évaluation environnementale et les annexes. Les formalités effectivement redondantes sont retirées dans R153-21 ; supprimer leurs actes générateurs ici priverait le public d'une publicité utile.",
    "Les trois rubriques du I et les huit du II sont maintenues, dont les 6° environnement, 7° évaluation et 8° mise à jour. Comparaison faite avec L153-51/53/58, R153-18/19/21/22 et R104-33 lus. Le renvoi de I à R153-21 demeure opérant après retrait de l'insertion dans la presse. Le corpus de R153-22 propose déjà un retrait d'annonce pour le II : même famille de mesure, sans ajouter les actes du I à son champ. Aucun acte ni numéro n'est déplacé, et aucun renvoi n'est utilisé pour rétablir quotas ou carence SRU.",
    "La liste source entière reste nécessaire à la publicité des décisions et à leur contestation. Son maintien n'est ni une simplification nouvelle ni autant de formalités supprimées qu'il existe de catégories d'actes.",
    "Le présent maintien ne tranche pas l'ensemble de l'opposabilité régie par L153-23 à L153-26 et L153-59. Les allègements de R153-21 et du projet de R153-22 doivent être distingués des actes dont la publicité subsiste.",
    "Aucune charge nouvelle identifiée : liste et renvois conservés intégralement. Les formalités applicables restent celles des articles visés, avec la réduction proposée séparément à R153-21.",
)

press_id = 'urbanisme-publicite-sans-insertion-presse'
proposed = """<p>Tout acte mentionné au I de l'article R. 153-20 est publié au Recueil des actes administratifs de l'Etat dans le département et affiché pendant une durée d'un mois au siège de l'établissement public de coopération intercommunale compétent et dans les mairies des communes membres concernées.</p>
<p>Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article. L'affichage mentionne le ou les lieux où le dossier peut être consulté.</p>
<p>La suppression de l'insertion dans un journal s'applique aux formalités de publicité restant à accomplir à l'entrée en vigueur des présentes dispositions, y compris pour des actes adoptés auparavant. Elle ne remet en cause ni les formalités déjà régulièrement accomplies ni les délais de recours qu'elles ont régulièrement fait courir et ne rouvre aucun délai expiré.</p>"""
reduced(
    'R153-21', proposed,
    "Réforme de fond : suppression de l'insertion obligatoire en caractères apparents dans un journal départemental pour les actes préfectoraux du I de R153-20. Publication au recueil et mois d'affichage dans tous les lieux prescrits sont conservés. Les lieux de consultation du dossier doivent désormais être indiqués sur cet affichage ; ce déplacement de la mention est recensé comme adaptation de charge, sans prétendre que toute la publicité disparaît.",
    "R153-20 I et II et R153-22 ont été lus en entier : le présent article vise seulement les trois catégories préfectorales du I. Le projet de R153-22 supprime déjà la presse dans son autre champ ; ces deux volets relèvent d'une même mesure de publicité sans insertion payante, non de deux taxes abolies. L153-53 et L153-59 font dépendre le caractère exécutoire des formalités applicables : publication au recueil et affichage subsistent. La transition préserve les actes de publicité accomplis et les délais de recours déjà courus, sans valider rétroactivement une autre omission. Pas de réduction du mois d'affichage et aucun portail ou support supplémentaire imposé.",
    impact(
        'mixed',
        "L'annonce dans la presse est effectivement supprimée par rapport à la source entière. Le recueil et le mois d'affichage subsistent. En contrepartie limitée, la mention des lieux de consultation auparavant portée par la formalité d'annonce doit figurer sur l'affichage existant ; cette adaptation est identifiée, sans établir un solde financier ou national de complexité.",
        "Seulement les actes préfectoraux du I de R153-20 ; le II relève de R153-22. Aucun effet sur les autres annonces exigées par des fondements autonomes. Coût des annonces évitées et adaptation des affiches non chiffrés ; délai de recours propre à chaque acte préservé.",
        "Une adaptation obligatoire est identifiée : reporter les lieux de consultation sur l'affichage déjà requis. Aucun nouveau renseignement substantiel, affiche séparée, registre, envoi, équipement ou délai n'est créé. Le solde net de coût n'est pas mesuré, même si l'obligation d'insertion dans la presse disparaît.",
        [
            effect(
                'obligation_removed', press_id,
                "Suppression de l'insertion obligatoire dans la presse départementale pour les actes préfectoraux visés.",
                "Publication au recueil, affichage pendant un mois et insertion apparente dans un journal diffusé dans le département.",
                "Publication au recueil et affichage pendant un mois ; aucune insertion de presse sur ce fondement.",
                "Autorités assurant la publicité des actes préfectoraux du I de R153-20 ; collectivités et public concernés.",
                "Formalités restant à accomplir lors de l'entrée en vigueur, même pour un acte antérieur ; publicités régulières et délais de recours préservés, sans réouverture.",
                "Les lieux de consultation passent sur l'affichage existant ; ce déplacement est recensé séparément sous la même mesure, sans nouvel affichage autonome.",
                "Mention de cet affichage est insérée en caractères apparents dans un journal diffusé dans le département.",
                "Aucune insertion dans un journal diffusé dans le département n'est requise au titre du présent article.",
            ),
            effect(
                'obligation_added', press_id,
                "Affectation à l'affichage existant de la mention des lieux de consultation du dossier.",
                "La source rattache la mention du lieu de consultation à la formalité d'annonce suivant l'affichage.",
                "L'affichage déjà imposé doit lui-même mentionner le ou les lieux de consultation ; aucune donnée nouvelle à constituer.",
                "Services rédigeant les affiches et personnes consultant les dossiers des actes préfectoraux concernés.",
                "Publicités restant à effectuer lors de l'entrée en vigueur ; pas de réfection des publicités régulièrement accomplies.",
                "Adaptation du contenu d'un support obligatoire existant ; coût non mesuré, sans deuxième affichage ni délai nouveau.",
                "Cette formalité de publicité mentionne le ou les lieux où le dossier peut être consulté.",
                "L'affichage mentionne le ou les lieux où le dossier peut être consulté.",
            ),
        ],
    ),
    ["Insertion en caractères apparents dans un journal diffusé dans le département de la mention de l'affichage des actes préfectoraux du I de R153-20."],
)

retained(
    'R161-1',
    "Maintien intégral : les études et l'arrêté ne sont joints que s'il y a lieu et servent aux règles dérogatoires d'implantation routière et de construction en montagne. Leur retrait de la carte pourrait couper le fondement documentaire d'une possibilité de construire. L'article ne crée ni nouveau prélèvement ni étude générale obligatoire indépendamment des cas légaux ; les annexes rendent les règles accessibles.",
    "L161-1, L111-9, L122-12 et L122-14 ont été lus intégralement. L111-9 permet de déroger à la bande d'inconstructibilité routière ; L122-14 2° ouvre des secteurs de construction près des plans d'eau et L122-12 1° permet l'exclusion de certains plans d'eau. Les accords et avis propres à ces lois ne sont pas abolis par cet article réglementaire. Aucun champ routier, seuil de rives ou critère environnemental n'est réécrit ici.",
    "Les pièces conditionnelles soutiennent des dérogations favorables et la publicité de leur fondement. L'examen de la source entière ne révèle pas de pièce autonome purement redondante pouvant être retirée sans fragiliser ces voies.",
    "Pas d'exemption nouvelle ni de suppression des accords légaux nécessaires aux études visées. L'éventuelle fusion technique de leur contenu avec une autre étude n'est pas imposée ou présentée comme déjà réalisée.",
    "Aucune charge nouvelle identifiée : maintien exact de la condition « s'il y a lieu », des annexes et des pièces liées aux dérogations. Aucun nouvel agrément, justificatif ou calendrier n'est ajouté.",
    "Les avantages possibles sont les règles d'implantation dérogatoires de L111-9, les secteurs autorisés de L122-14 2° et l'arrêté d'exclusion de L122-12 1°. Tous leurs supports demeurent dans la carte pour les nouvelles opérations éligibles autant que pour les décisions antérieures.",
)

retained(
    'R161-2',
    "Maintien intégral : diagnostic initial, prévisions et justification des secteurs constructibles rendent contrôlable le choix entre ouverture et fermeture à la construction ; l'examen des incidences environnementales évite une décision sans appréciation des risques et milieux. Ces éléments sont réunis dans le même rapport, sans étude, déclaration, agrément ou prélèvement supplémentaire. Aucun doublon de support distinct n'est imposé par l'article.",
    "Les 1° à 3° restent intacts, avec prévisions économiques et démographiques, motifs des changements lors d'une révision, préservation et mise en valeur de l'environnement. L161-1 à L161-4 lus ; L101-1/L101-2 conservent leur fonction d'objectifs sans reconstituer un quota SRU. R161-3 complète ce rapport dans les seuls cas d'évaluation environnementale et permet déjà proportionnalité et référence à d'autres études.",
    "Le même rapport comporte déjà les trois fonctions complémentaires ; les supprimer rendrait les choix de constructibilité et leurs effets moins contrôlables. Aucun gain nouveau ni nouvelle contrainte n'est revendiqué par ce maintien de la source entière.",
    "Aucun allègement documentaire inventé : les trois rubriques ne sont pas trois rapports. Les limites d'urbanisation et le régime d'évaluation des autres articles ne sont pas modifiés ici.",
    "Aucune charge nouvelle identifiée : maintien intégral du rapport existant, sans nouvelles statistiques, attestation, périodicité ou approbation. Les données requises restent liées aux choix de la carte.",
)

retained(
    'R161-3',
    "Maintien intégral après examen des sept rubriques, du suivi et des alinéas finaux : le rapport environnemental sert à identifier les impacts notables, comparer les solutions raisonnables et prévenir les dommages, notamment sur Natura 2000 et la santé. Il ne prescrit pas un deuxième rapport autonome. Proportionnalité et référence aux études existantes limitent déjà les doublons ; retirer une simple rubrique sans analyser le cadre européen ne constituerait pas une simplification juridiquement démontrée.",
    "Conserver intégralement 1° articulation et L131-4/L131-6 ; 2° évolution ; 3° tous facteurs et leurs interactions, L414-4 environnement ; 4° motifs et solutions ; 5° éviter/réduire/compenser ; 6° analyse au plus tard à six ans de l'approbation ou de la révision, critères/indicateurs/modalités et détection précoce ; 7° résumé non technique et méthode ; enfin proportionnalité, complément en révision et réemploi des études. Cadre européen à coordonner : directive 2001/42/CE, notamment rapport et suivi, et régime Natura 2000 ; leurs textes extérieurs ne sont pas fournis et aucune conformité exhaustive n'est affirmée. Note source lue en entier : article 26 du décret 2021-1345 du 13 octobre 2021 et distinction des décisions antérieures R104-28 restent applicables. Anomalie documentaire signalée : la note vise des procédures de PLU alors que l'article concerne les cartes communales ; elle n'est pas corrigée silencieusement ni transformée en date de réforme future.",
    "La source complète comporte une évaluation proportionnée, un résumé accessible et le suivi des effets imprévus ; elle autorise déjà le recours aux informations d'autres études. Aucun second dossier ni répétition automatique de l'étude ne peut être déduit de ses sept rubriques ; leur maintien ne compte pas comme réduction.",
    "Le rapport n'est exigé sous ce régime que lorsqu'une évaluation environnementale est due. Le cadre européen et Natura 2000 n'est pas abrogé ; la nécessité et le coût de chaque donnée d'une future évaluation ne sont pas audités au-delà de ce texte.",
    "Aucune charge nouvelle identifiée : texte maintenu en entier, avec le délai maximal de six ans, ses critères et sa faculté de référence aux autres études. Aucun nouvel indicateur, registre, dépôt ou échéance n'est ajouté.",
    "Les allègements internes sont la proportionnalité à l'importance de la carte et aux enjeux, ainsi que le droit de se référer aux renseignements d'autres études, plans ou documents. Ils sont maintenus sans condition nouvelle pour toute évaluation future relevant de l'article, avec la transition historique de la note source.",
)

retained(
    'R161-4',
    "Maintien intégral : la délimitation graphique est le support nécessaire de la constructibilité et laisse expressément ouvertes les exceptions de L161-4. L'avis légal est réputé favorable après un mois ; supprimer ce délai ou ce sens du silence supprimerait un avantage, sans abolir l'avis prévu par la loi. Aucun dépôt ni agrément autonome n'est créé ici.",
    "L161-4 a été lu en entier, avec toutes ses exceptions, conditions et dispositions relatives aux énergies renouvelables. La commission agricole concerne les b et d du 2° dans son champ légal. Conserver exactement le mois calculé à compter de la saisine par l'autorité compétente en autorisations, et non un délai en jours ou une autorisation tacite de construire. La source renvoie globalement à L161-4 sans viser un avis nouveau pour toutes ses dérogations ; ne pas étendre cette consultation.",
    "La carte reste lisible et les exceptions légales opposables ; l'avis tacite favorable à un mois conserve un mécanisme protecteur contre le blocage. Aucune réduction supplémentaire de délai n'est proposée faute de suppression coordonnée de l'avis législatif.",
    "Le silence favorable porte sur l'avis, pas sur le permis ni sur la compatibilité de tout projet. Le mois n'est pas un délai minimal obligatoire si un avis intervient plus tôt. Aucun effet financier démontré.",
    "Aucune charge nouvelle identifiée : mêmes documents graphiques, saisine et délai. Aucun nouvel avis, condition de dérogation ou justificatif n'est ajouté à la source maintenue.",
    "Les avantages sont les constructions admises par exception à L161-4 et le caractère favorable de l'avis non intervenu dans le mois. Ils restent ouverts aux futurs projets éligibles, sans restriction aux dossiers antérieurs ni transformation de l'avis en agrément.",
)

retained(
    'R161-5',
    "Maintien intégral de la faculté de prévoir un secteur d'activités, notamment pour celles incompatibles avec le voisinage habité. Cette séparation peut prévenir nuisances et risques et garantir des implantations économiques ; elle n'est ni un quota automatique ni un agrément d'entreprise. Le seul article ne justifie pas de retirer ce pouvoir local en supprimant aussi le support de ces implantations.",
    "L161-1 à L161-4 et R161-4 lus pour distinguer cette faculté de l'interdiction générale de construire hors secteur. L'article n'autorise pas à écarter les exceptions légales ni les protections sanitaires ou environnementales. Une restriction arbitraire d'un document concret pourrait être contestée ; aucun dossier local ne permet ici de supprimer sélectivement un secteur ni de chiffrer sa charge. Aucun quota SRU rétabli.",
    "La faculté source est conservée avec sa fonction d'implantation économique et de séparation des usages incompatibles. Elle peut limiter les autres usages dans les secteurs choisis ; ce coût de zonage est identifié, sans prétendre l'avoir retiré par un maintien.",
    "Ne démontre pas que tous les secteurs réservés existants sont nécessaires. Leur contrôle suppose leurs motifs et leurs effets locaux ; cet article ne les approuve ni ne les étend automatiquement.",
    "Aucune charge nouvelle identifiée : maintien de la seule faculté cartographique existante, sans obligation de créer un secteur, nouvelle procédure d'autorisation ou inventaire d'entreprises.",
    "La possibilité d'implanter des activités dans un secteur identifié, y compris celles qui coexistent difficilement avec l'habitat, reste disponible pour les projets futurs. Son caractère facultatif est conservé, sans obligation d'ouvrir un zonage ni avantage fiscal inventé.",
)

retained(
    'R161-6',
    "Maintien intégral : l'indication conditionnelle des petits plans d'eau rend utilisable et identifiable une dérogation à la protection montagnarde des rives. Ce n'est pas une nouvelle interdiction, une étude obligatoire indépendante ou une déclaration du constructeur. Retirer l'identification compromettrait la dérogation que l'auteur demande de préserver.",
    "L122-12 lu intégralement : le 2° permet à la carte d'exclure certains plans d'eau du régime en raison de leur faible importance ; le 1° et son critère de quart des rives demeurent distincts. Aucun seuil nouveau de faible importance n'est inventé et aucune substitution à l'arrêté du préfet du 1° n'est opérée. La représentation reste « le cas échéant » et vise bien le 2°.",
    "La source entière est le support graphique d'une exception favorable ; sa conservation ne compte pas comme nouvelle dispense ni comme suppression de l'ensemble de la protection des rives.",
    "Ne modifie ni les critères légaux de faible importance ni les autres règles applicables au projet. Aucun plan d'eau supplémentaire n'est classé ou exclu par ce maintien réglementaire.",
    "Aucune charge nouvelle identifiée : maintien du seul report graphique conditionnel existant. Aucun dossier particulier, certificat ou autorisation de remplacement n'est ajouté.",
    "Le bénéfice est l'exclusion du régime protecteur des rives pour les plans d'eau retenus en raison de leur faible importance sur le fondement du 2° de L122-12. L'identification graphique le conserve pour les décisions futures autant que pour les cartes déjà approuvées, avec ses conditions légales.",
)

retained(
    'R161-7',
    "Maintien intégral : l'article oblige seulement à rendre visibles les secteurs où la carte s'oppose à la reconstruction après sinistre ; il ne crée pas lui-même ce pouvoir, prévu à L111-15. Supprimer la représentation n'abolirait pas l'interdiction législativement permise et rendrait la limitation moins accessible. Les secteurs sont indiqués seulement s'il y a lieu.",
    "L111-15 lu entièrement : reconstruction à l'identique d'un bâtiment régulièrement édifié, détruit ou démoli, autorisée dans les dix ans sauf disposition contraire de la carte, du PLU ou du plan de prévention des risques naturels prévisibles. R161-7 vise seulement la représentation des interdictions après sinistre : ne pas l'étendre à toute démolition ni supprimer le droit légal en prétendant retirer une formalité. La nécessité de chaque interdiction, notamment face aux risques graves, relève du contrôle de la carte et non de ce seul support graphique.",
    "La disposition est conservée pour la transparence des restrictions et la protection des tiers. La retirer ne démontrerait aucune réduction réelle des restrictions permises par L111-15 ; aucun gain de constructibilité n'est donc compté.",
    "Aucune validation de toutes les interdictions locales existantes. Modifier le pouvoir d'opposition lui-même requerrait L111-15 et une coordination des risques, hors des articles assignés ; ce chantier n'est pas déclaré réalisé.",
    "Aucune charge nouvelle identifiée : cartographie conditionnelle existante conservée, sans nouveau secteur obligatoire, déclaration de sinistre, étude ou délai. Le droit légal de reconstruction reste distinct.",
    "Le droit favorable de reconstruction à l'identique de L111-15 n'est ni abrogé ni limité par une nouvelle condition. La carte montre seulement les exceptions qu'elle a régulièrement prévues ; conserver ce report évite de rendre invisible une restriction à ce droit pour les futurs demandeurs.",
)

retained(
    'R161-8',
    "Maintien intégral des cinq annexes : elles rendent accessibles les servitudes, risques de bruit, pollution des sols, incendie et fragilité structurelle, sans créer par elles-mêmes les obligations sectorielles. Supprimer ces informations ne supprimerait pas les normes autonomes correspondantes et pourrait masquer un risque grave. Aucun prélèvement, agrément ni déclaration supplémentaire des propriétaires n'est prescrit dans cet article.",
    "Conserver 1° catégories de servitudes, 2° L112-6, 3° L125-6 environnement, 4° titre III du livre Ier forestier, 5° L126-6-1 CCH. L161-1, L162-1, L163-10 et R163-8 lus : annexion, publication et opposabilité des servitudes demeurent distinctes ; notamment aucune remise en cause de la limitation favorable d'opposabilité de L162-1. Les textes environnemental et forestier extérieurs ne sont pas fournis en entier et ne sont pas déclarés réécrits. La suppression de la communication fiscale analogue à R163-8 reste à coordonner hors lot ; elle n'emporte pas suppression des cinq annexes.",
    "L'article entier est conservé comme information nécessaire sur des contraintes autonomes et des risques graves. Le nombre d'annexes n'est pas assimilé à cinq déclarations privées ni à cinq taxes supprimables par retrait de leur publicité.",
    "Ne vérifie pas au fond chaque servitude ou périmètre local et ne réforme pas les obligations de débroussaillement ou diagnostic elles-mêmes. Leur assise et leurs éventuelles dispenses restent à leur champ sectoriel.",
    "Aucune charge nouvelle identifiée : cinq rubriques inchangées, sans donnée personnelle, inventaire, échéance ou certification supplémentaire. Les propriétaires ne reçoivent aucune nouvelle obligation de dépôt.",
)

retained(
    'R162-1',
    "Maintien intégral : l'article identifie les normes applicables aux autorisations dans les territoires dotés d'une carte, où le règlement national continue de s'appliquer. Il ne crée pas une deuxième autorisation ni un prélèvement et ne conditionne pas une dérogation à une formalité nouvelle. Le retirer ne supprimerait pas le règlement national mais rendrait l'instruction moins lisible.",
    "Lu avec L161-2, L161-4 et R162-2 : les documents graphiques et exceptions légales de la carte ne sont pas remplacés par le règlement national ; les autres normes gardent leur champ et leurs dérogations. Aucun renvoi à une taxe ou à des quotas SRU n'est introduit. La portée de toutes les dispositions extérieures applicables à une parcelle n'est pas auditée par cette phrase générale.",
    "La règle source complète évite de traiter la carte comme un PLU doté d'un règlement propre. Son maintien conserve la base juridique de l'instruction sans compter artificiellement une simplification ou un nouveau régime fusionné.",
    "Ne supprime aucune règle substantielle d'implantation ni autorisation imposée ailleurs. L'examen de chaque régime particulier reste nécessaire pour les projets qui en relèvent ; aucun effet fiscal n'est établi.",
    "Aucune charge nouvelle identifiée : même base d'instruction, sans dossier, attestation ou délai supplémentaire. Les dispositions légales favorables continuent de s'appliquer dans leur champ.",
)

retained(
    'R162-2',
    "Maintien intégral : l'opposabilité des documents graphiques rend stables et contrôlables les secteurs constructibles comme les restrictions régulièrement instituées. Ce n'est ni un dépôt de plus ni une taxe ; supprimer la phrase ne garantit pas une liberté de construire et fragiliserait aussi les droits tirés de la carte.",
    "Confronté à L161-1/L161-4, R161-4 à R161-7 et R163-6/R163-9 : contenu, dérogations, publication et opposabilité sont des fonctions distinctes. L162-1 conserve ses conditions favorables d'opposabilité des servitudes et son délai d'un an ; l'opposabilité graphique générale ne les neutralise pas. Aucun effet automatique sur un permis déjà délivré n'est ajouté.",
    "La source entière assure l'effet des documents graphiques pour tous les tiers. Sa suppression retirerait également le support des possibilités de construire ; aucune réduction autonome de charge n'est démontrée.",
    "L'article ne dispense pas de publication ni ne valide une délimitation illégale. Les recours contre la carte et ses actes d'application conservent leurs régimes propres, sans délai nouveau fixé ici.",
    "Aucune charge nouvelle identifiée : phrase source intégralement conservée, sans registre, preuve, transmission ni formalité individuelle ajoutés à l'opposabilité existante.",
    "L'opposabilité bénéficie aussi aux propriétaires et porteurs de projet situés en secteur constructible ou couvert par une dérogation régulièrement cartographiée. Elle demeure pour les situations futures après les publicités requises, sans réduction du bénéfice légal de L162-1 sur les servitudes.",
)

retained(
    'R163-1',
    "Maintien intégral : la désignation du maire ou du président de l'EPCI comme conducteur de la procédure évite une compétence indéterminée. Aucun second pilote, agrément, déclaration, justificatif ou délai minimal n'est ajouté. Réécrire cette phrase sans changer la compétence ne serait qu'une retouche stylistique.",
    "L163-3 lu entièrement : initiative locale et substitutions de compétence en cas de création, fusion ou transfert restent régies par la loi. R163-1 ne déroge ni à ces transitions ni aux autorités d'approbation des autres articles ; la conduite de procédure n'est pas confondue avec le vote de l'organe délibérant.",
    "La source entière remplit une fonction nécessaire de compétence sans formalité autonome à retirer. Maintien sans nouveau corps et sans effet matériel revendiqué.",
    "Ne supprime ni les procédures d'élaboration ou de révision ni les décisions légalement requises. Les hypothèses de transfert et de commune nouvelle restent traitées par L163-1 à L163-3.",
    "Aucune charge nouvelle identifiée : même autorité, aucune désignation supplémentaire, convention de pilotage, donnée ou délai imposé. Le texte est conservé exactement.",
)

porter_id = 'urbanisme-porter-a-connaissance-sans-demande'
proposed = """<p>Le préfet transmet au maire ou au président de l'établissement public de coopération intercommunale compétent les dispositions et documents mentionnés à l'article L. 132-2, sans demande préalable de leur part, conformément aux obligations de porter à connaissance prévues par cet article.</p>"""
base(
    'R163-2', proposed,
    "Coordination nécessaire avec L132-2 : le porter à connaissance et la transmission des études nécessaires sont déjà des obligations légales de l'État. Le règlement ne doit pas les présenter comme subordonnés à une demande locale, avec initiative spontanée seulement facultative. Le nouveau corps retire cette ambiguïté, sans compter une nouvelle suppression de demande qui serait déjà exigible malgré L132-2.",
    "L132-2 et L132-3 lus intégralement : cadre législatif et réglementaire, projets existants ou en cours et études techniques nécessaires sont les données visées ; mise à disposition du public et absence d'effet des retards ou omissions sur les procédures demeurent régies par ces textes. La demande de liste d'immeubles de L132-4 est un autre régime et n'est pas supprimée. Le texte n'élargit pas les accès aux données ni les études à produire ; il ne crée pas de délai, de demande de confirmation ou de nouvelle périodicité. Application du cadre légal existant aux procédures futures et en cours, sans reprise des transmissions déjà effectuées.",
    impact(
        'coordination_only',
        "L'article source met en avant la demande locale et une initiative préfectorale facultative ; la loi L132-2 impose déjà le porter à connaissance. La proposition aligne le règlement sur ce droit existant. Aucune économie nouvelle de démarche n'est comptée sur la seule répétition de cette garantie légale.",
        "Aucune dispense pour des informations hors L132-2, notamment la liste particulière de L132-4. Aucun gain de délai ou coût mesuré ; le texte ne garantit ni exhaustivité instantanée ni accès à des données protégées.",
        "Aucune charge nouvelle identifiée par rapport au cadre légal complet : la transmission spontanée relève déjà de L132-2. Aucun fichier nouveau, inventaire, collecte, attestation, échéance ou obligation de relance n'est imposé à la commune ou à l'État.",
        [effect(
            'coordination', porter_id,
            "Alignement de la transmission préfectorale sur le porter à connaissance déjà obligatoire de L132-2.",
            "R163-2 présente la transmission sur demande locale et l'initiative spontanée comme facultative ; L132-2 impose déjà l'information et les études nécessaires.",
            "R163-2 exprime la transmission sans demande préalable conformément à L132-2, sans contenu ou délai nouveau.",
            "Préfet, maires et présidents d'EPCI compétents élaborant ou révisant une carte communale.",
            "Coordination du cadre légal existant pour les procédures nouvelles et en cours ; aucune transmission régulièrement accomplie n'est à refaire.",
            "Aucune collecte ni nouvelle obligation légale : maintien du périmètre d'information et des garanties de L132-2/L132-3.",
            "à la demande du maire ou du président de l'établissement public de coopération intercommunale compétent",
            "sans demande préalable de leur part, conformément aux obligations de porter à connaissance prévues par cet article.",
        )],
    ),
)

retained(
    'R163-4',
    "Maintien intégral : l'article met en œuvre les deux modes légaux de participation déjà ouverts, avec les pièces et avis nécessaires à un consentement public éclairé. Le porter à connaissance n'est annexé que facultativement. Aucun nouveau rapport, agrément ou justificatif privé autonome ne peut être retiré ici sans identifier la pièce ni son fondement ; supprimer toute annexe d'avis affaiblirait l'accès au débat environnemental.",
    "L163-5 et L163-6 lus intégralement : substitution électronique par décision motivée et accès papier en mairie restent garantis par la loi, sans les confondre avec une suppression de consultation. Note législative : rédaction entrée en vigueur le 26 mai 2026, sans application aux procédures d'évolution de SCoT ou PLU alors en cours ; aucune date future inventée. L132-3 permet déjà l'annexion facultative du porter à connaissance. R123-8 environnement n'est pas fourni dans le corpus autorisé : son contenu extérieur n'est ni réécrit ni supposé vide ; le maintien de son renvoi n'est pas une déclaration de vérification exhaustive. La version assignée du 5 août 2026 conserve les deux voies de participation.",
    "La source complète organise l'accès public au projet, aux pièces applicables et aux avis ; le dernier alinéa est déjà facultatif. Aucune répétition de dossier distinct obligatoire n'est établie dans cet article et aucun allègement nouveau n'est revendiqué.",
    "Pas d'examen complet du contenu externe de R123-8 environnement, absent du corpus. L'option électronique ne supprime pas les garanties légales de consultation sur support papier et ne constitue pas une dispense d'évaluation.",
    "Aucune charge nouvelle identifiée : mêmes deux voies, mêmes avis et pièces, aucune donnée supplémentaire. L'annexion du porter à connaissance demeure facultative et aucun dépôt identique n'est créé.",
    "L'option légale de participation électronique et la faculté de n'annexer que tout ou partie du porter à connaissance restent utilisables dans leurs champs et transitions, pour les procédures futures aussi ; aucune enquête supplémentaire ni nouvelle condition d'accès à cette option n'est introduite.",
)

retained(
    'R163-5',
    "Maintien intégral : le vote local et la transmission pour approbation préfectorale sont deux compétences expressément prévues par L163-6 et L163-7. Le second contrôle conserve ici sa fonction de vérification du cadre national et des protections applicables à une carte communale, avec silence légal favorable ; retirer seulement le mot « approbation » du règlement laisserait l'obligation légale entière et simulerait une suppression. L'article n'ajoute pas une troisième approbation ni une pièce distincte.",
    "L163-6 et L163-7 lus en entier : décision de l'organe délibérant après participation, transmission par maire ou président à l'État, deux mois au préfet et approbation tacite à leur expiration, puis mise à disposition du public. L163-8 étend ces règles aux révisions avec son exception de consultation ; R163-6 et R163-9 assurent la publication. Une éventuelle suppression future de la coapprobation exigerait de modifier L163-7, le renvoi de L163-8 et le dernier alinéa de R163-9 : elle n'est pas décidée ou accomplie par ce seul article. Les accords particuliers des dérogations L111-9/L122-14 restent distincts.",
    "La source entière reprend le circuit légal d'approbation de la carte et n'impose aucune procédure autonome supplémentaire. Le maintien est justifié par le contrôle national coordonné au document local et ne compte pas comme suppression d'autorisation.",
    "Le coût et l'utilité de chaque contrôle préfectoral concret ne sont pas mesurés. Aucun raccourcissement du délai légal de deux mois ni retrait d'un pouvoir d'approbation de L163-7 n'est revendiqué ; les coordinations d'une éventuelle autre réforme sont identifiées.",
    "Aucune charge nouvelle identifiée : maintien exact du vote et de la transmission légale, sans nouveau dossier, agrément ou délai. Le silence favorable légal à deux mois n'est pas transformé en condition plus contraignante.",
    "L'approbation préfectorale tacite après deux mois prévue à L163-7 reste applicable aux futures cartes et révisions concernées ; elle n'est pas remplacée par un agrément exprès. Les droits de consultation du public et les dérogations légales ne sont pas fermés.",
)

retained(
    'R163-7',
    "Maintien intégral : un arrêté du maire ou du président suffit déjà pour rectifier une erreur matérielle. Cette voie évite une révision complète pour une simple erreur sans ouvrir une modification de fond sous cette qualification. Aucune nouvelle enquête, approbation préfectorale ou pièce technique n'est exigée par cet article.",
    "L163-9, R163-6 et R163-9 lus : habilitation légale à rectifier, maintien de la publication de l'arrêté sur le portail avec solution technique de secours, et distinction des actes d'approbation de la carte. Les décisions qui modifient réellement les choix d'urbanisme ne deviennent pas des rectifications d'erreur matérielle. Aucun nouveau délai ou renvoi n'est nécessaire.",
    "La source entière constitue déjà la procédure simple de correction d'une erreur matérielle. Son maintien conserve une faculté utile sans la compter comme un nouvel allègement ou une suppression de l'approbation de la carte elle-même.",
    "Ne définit pas une erreur matérielle nouvelle et n'autorise pas une extension de constructibilité déguisée. Les garanties de publicité et recours restent applicables ; leur coût n'est pas chiffré.",
    "Aucune charge nouvelle identifiée : même arrêté, mêmes autorités et publicité existante. Aucune attestation, registre, étude, saisine ni délai préalable supplémentaire n'est ajouté.",
    "La faculté favorable de corriger une erreur matérielle par simple arrêté demeure ouverte à toute carte et à toute future erreur entrant dans ce champ, sans restriction aux erreurs déjà constatées ni remplacement par une procédure complète de révision.",
)


# Coordination du champ réglementaire avec les cinq catégories légales de L300-6.
# Les conditions de la loi sont conservées ; ce n'est pas une extension autonome.
project_id = 'urbanisme-declaration-projet-champ-l300-6'
project_before = "sur l'intérêt général d'une action ou d'une opération d'aménagement ou de la réalisation d'un programme de construction."
project_after = "sur l'intérêt général d'une action ou d'une opération d'aménagement ou de la réalisation d'un programme de construction, ou d'un projet mentionné aux 3° à 5° du même article."
for number in ['R153-15', 'R153-16', 'R153-17']:
    entry = answers[number]
    original = entry['proposed_xml'] or by_number[number]['source_xml']
    assert original.count(project_before) == 1
    entry['proposed_xml'] = original.replace(project_before, project_after)
    entry['status'] = 'rewrite_draft'
    entry.pop('classification', None)
    entry['reason'] += (
        " Coordination supplémentaire nécessaire : le 2° inclut désormais explicitement les projets des 3° à 5° de L300-6, "
        "déjà ouverts par la loi actuelle. Les catégories historiques sont maintenues ; ni nouvelle autorisation ni "
        "extension autonome des dérogations n'est instituée."
    )
    entry['review_notes'] += (
        " Vérification complémentaire : L300-6 a été lu dans sa version entière du corpus, qui comporte cinq catégories, "
        "alors que le 2° réglementaire n'en nomme explicitement que les deux premières. Ajout des projets des 3° à 5° "
        "par renvoi exact : énergies/stockage/hydrogène/réseaux, industrie et logistique associée, recherche et développement. "
        "Les conditions légales de L300-6, notamment l'exception touchant à l'économie générale du PADD et les exigences "
        "environnementales, continuent de s'appliquer ; le renvoi ne les écarte pas. Les R153-15/16/17 sont coordonnés ensemble, "
        "sans prétendre modifier les autres procédures de projet ni l'ensemble du régime industriel."
    )
    if number == 'R153-15':
        entry['reason'] = (
            "Coordination nécessaire du 2° avec le champ actuel de L300-6 : maintien des actions, opérations d'aménagement "
            "et programmes de construction, et mention explicite des projets des 3° à 5° déjà admis par la loi. "
            "Les compétences locales et l'approbation du PLU par la déclaration de projet restent intégralement inchangées. "
            "Il ne s'agit ni d'une nouvelle procédure ni d'un gain matériel autonome."
        )
        entry['substantive_impact'] = impact(
            'coordination_only',
            "La source réglementaire entière ne désigne explicitement dans son 2° que les actions, opérations et programmes, "
            "alors que L300-6 a été étendu à cinq catégories. Le corps proposé aligne ce champ sur la loi sans créer un "
            "nouvel avantage autonome ni supprimer une deuxième autorisation ; l'acte local intégré demeure.",
            "Les effets favorables des catégories législatives 3° à 5° existaient déjà dans L300-6. Aucun gain nouveau "
            "de délai, de taxe ou de dossier n'est compté et les exceptions de cette loi restent applicables.",
            "Aucune charge nouvelle identifiée : mêmes autorités, même déclaration et mêmes garanties de mise en compatibilité. "
            "Le renvoi aux catégories légales n'ajoute ni donnée, pièce, avis ni délai au régime prévu par la loi.",
        )
        entry['benefit_review'] = (
            "La déclaration de projet continue d'emporter l'approbation des nouvelles dispositions du PLU pour les futures "
            "opérations éligibles. Le renvoi aux projets des 3° à 5° de L300-6 rend explicite leur accès au cadre déjà légalement "
            "ouvert, sans leur retirer une condition favorable ni neutraliser les conditions environnementales de la loi."
        )
    else:
        entry['substantive_impact']['assessment'] += (
            " Le 2° est également aligné sur les trois catégories supplémentaires de L300-6 déjà légales ; "
            "ce rattrapage réglementaire n'est pas une nouvelle libéralisation autonome."
        )
    entry['substantive_impact']['effects'].append(effect(
        'coordination', project_id,
        "Alignement du 2° sur les projets des 3° à 5° de L300-6 déjà compris dans le champ légal.",
        "La loi actuelle comporte cinq catégories ; le 2° réglementaire ne nomme explicitement que les actions/opérations d'aménagement et programmes de construction.",
        "Le 2° mentionne aussi les projets des 3° à 5° de L300-6, avec maintien des conditions et exceptions de cette loi.",
        "Porteurs de projets et autorités relevant du champ propre de l'article " + number + ".",
        "Coordination du champ légal actuel pour les opérations futures et les procédures en cours légalement éligibles ; aucun acte antérieur annulé ni délai expiré rouvert.",
        "Aucune formalité ni exemption nouvelle ; régime légal existant et acte d'approbation déjà applicable conservés.",
        project_before, project_after,
    ))


# Réduction de la contrainte de destination, avec maintien des polices de risques.
activity_id = 'carte-communale-fin-exclusivite-secteurs-activites'
proposed = """<p>Le ou les documents graphiques peuvent identifier les secteurs d'implantation d'activités, notamment celles qui sont incompatibles avec le voisinage des zones habitées. Cette identification ne réserve pas ces secteurs aux seules activités.</p>
<p>Dans les secteurs où les constructions sont autorisées, une construction ne peut être interdite au seul motif de l'affectation du secteur aux activités. Les règles de salubrité et de sécurité, de prévention des nuisances et des risques et de protection de l'environnement et du patrimoine demeurent applicables, notamment lorsqu'elles font obstacle au voisinage d'activités et d'habitations.</p>
<p>Ces dispositions s'appliquent aux demandes d'autorisation déposées à compter de leur entrée en vigueur ainsi qu'aux demandes en cours, y compris lorsque la réservation aux activités résulte d'une carte communale approuvée auparavant. Les refus devenus définitifs ne sont pas remis en cause. Les autorisations régulièrement délivrées et les droits qu'elles ont créés demeurent préservés.</p>"""
reduced(
    'R161-5', proposed,
    "Réforme de fond : fin de l'exclusivité réglementaire des secteurs réservés aux activités. La carte peut toujours "
    "identifier leurs secteurs d'accueil et les activités y restent admissibles, mais cette seule affectation ne suffit "
    "plus à exclure un autre usage dans un secteur constructible. Les nuisances graves, risques et protections "
    "environnementales ou patrimoniales restent opposables sur leurs fondements autonomes ; aucun droit de construire "
    "en zone inconstructible n'est créé. La suppression est applicable aussi aux demandes futures relevant de cartes existantes.",
    "L161-1 à L161-4, R161-4, R162-1 et R111-1/2/3/14/26/27 lus en entier. L161-4 distingue secteurs constructibles "
    "et non constructibles sans imposer une réservation exclusive aux activités ; R111-2 et R111-3 permettent le refus "
    "ou les prescriptions liés aux risques et nuisances graves, y compris de voisinage. Les règles agricoles, environnementales, "
    "paysagères, servitudes et autres polices restent distinctes. La nouvelle règle neutralise expressément la seule "
    "exclusivité de destination dans les cartes antérieures, sans effacer leur délimitation de constructibilité, leurs "
    "autres protections, les refus définitifs ou les droits tirés de permis valables. Vérifier les éventuelles obligations "
    "d'évaluation environnementale du décret national de réforme au regard de la directive 2001/42/CE ; aucune dispense "
    "implicite n'est prévue et cette évaluation n'est pas déclarée accomplie. Les régimes extérieurs d'installations classées "
    "et de réciprocité des distances agricoles ne sont pas abrogés. Aucun quota social ou zonage nouveau obligatoire.",
    impact(
        'material_reduction',
        "La source entière permet de réserver un secteur aux seules activités, y compris sans incompatibilité particulière "
        "d'un autre usage. La proposition retire ce motif autonome d'exclusion et maintient l'accueil des activités, les "
        "limites de constructibilité et les protections de risques. Elle ouvre des usages potentiels, sans garantir un permis "
        "dans un cas où une autre norme l'interdit.",
        "Effet limité aux cartes communales, pas aux PLU ni aux secteurs non constructibles. Aucun nombre de logements, "
        "gain foncier ou baisse de coût n'est chiffré. L'évaluation environnementale éventuellement requise du décret de réforme "
        "reste à vérifier ; la présente proposition ne la dispense pas et ne constitue pas un audit de chaque zone locale.",
        "Aucune charge nouvelle identifiée : l'identification des secteurs reste facultative ; aucun changement de carte, "
        "dossier, avis, registre ou justificatif spécial n'est demandé au pétitionnaire pour écarter la seule exclusivité. "
        "L'examen des risques et nuisances repose sur les règles déjà applicables ; ses coûts de mise en œuvre et le solde net "
        "ne sont pas chiffrés.",
        [effect(
            'obligation_removed', activity_id,
            "Suppression de l'exclusivité d'usage fondée sur la seule réservation d'un secteur aux activités.",
            "La carte communale peut réserver un secteur à l'implantation d'activités, excluant les autres usages par ce seul zonage, sans que le texte exige une incompatibilité individualisée.",
            "Dans un secteur constructible, l'affectation aux activités ne suffit plus à interdire une autre construction ; risques, nuisances, servitudes et autres règles restent opposables.",
            "Propriétaires, entreprises, porteurs de logements ou d'autres constructions et autorités d'urbanisme dans les secteurs d'activités de cartes communales.",
            "Demandes nouvelles et en cours lors de l'entrée en vigueur, y compris sous des cartes antérieures ; refus définitifs, permis valables et droits créés préservés.",
            "Aucune procédure de dérogation ni déclaration de remplacement ; contrôle des protections autonomes existantes conservé.",
            "Le ou les documents graphiques peuvent préciser qu'un secteur est réservé à l'implantation d'activités, notamment celles qui sont incompatibles avec le voisinage des zones habitées.",
            "Dans les secteurs où les constructions sont autorisées, une construction ne peut être interdite au seul motif de l'affectation du secteur aux activités.",
        )],
    ),
    ["Faculté de réserver exclusivement un secteur constructible de la carte communale aux activités et d'écarter les autres constructions sur le seul fondement de cette affectation."],
)
answers['R161-5']['benefit_review'] = (
    "L'accueil des activités, y compris celles difficilement compatibles avec l'habitat, reste possible dans les secteurs "
    "identifiés. Aucun avantage fiscal ni dérogation à une interdiction de construire n'est supprimé : seule l'exclusion "
    "des autres usages par réservation exclusive est retirée. Les activités déjà autorisées conservent leurs droits ; les "
    "nouvelles demandes bénéficient des mêmes protections de sécurité, de salubrité et de nuisances que celles prévues ailleurs."
)

# Ne pas supposer que la source obligeait à produire deux supports dans tous les cas.
entry = answers['R153-19']
entry['reason'] = (
    "Réforme de fond limitée à la forme du dossier : l'exigence d'un rapport identifié comme tel est retirée lorsque "
    "le projet de délibération soumis au public expose lui-même tous les motifs et toutes les conséquences juridiques "
    "de l'abrogation. Le rapport reste une option. La source n'ordonne pas deux supports distincts dans toutes les "
    "procédures : le gain est donc conditionnel et porte sur cette alternative explicite, sans économie automatique "
    "de double rédaction revendiquée. L'enquête, les informations et la décision locale restent exigées."
)
entry['review_notes'] += (
    " Limite de la comparaison : la source exige un rapport mais n'emploie pas le mot « distinct ». La proposition "
    "supprime l'exigence formelle de rapport en ouvrant expressément l'alternative du projet de délibération complet ; "
    "elle ne prouve pas qu'une rédaction commune était auparavant systématiquement refusée. Aucun gain pour les dossiers déjà mutualisés."
)
entry['removed_provisions'] = [
    "Exigence formelle d'un rapport d'exposé lorsque le projet de délibération joint au dossier contient intégralement les motifs et conséquences juridiques de l'abrogation."
]
entry['substantive_impact']['scope_limitations'] += (
    " La source ne prescrit pas deux supports dans tous les cas ; aucun gain matériel supplémentaire n'est démontré pour les dossiers déjà mutualisés."
)
entry['substantive_impact']['effects'][0]['before'] = (
    "Le dossier doit comprendre un rapport exposant motifs et conséquences juridiques. La source ne prévoit pas expressément "
    "qu'un projet de délibération complet puisse en tenir lieu, mais n'impose pas deux supports dans tous les cas."
)

# La répétition de compétence ne porte aucune obligation autonome ; correction signalée.
entry = answers['R153-16']
duplicate = ", lorsque le projet émane d'un établissement public dépendant de l'Etat, par le président du conseil d'administration"
tail = " ou" + duplicate
assert entry['proposed_xml'].count(tail + '.') == 1
entry['proposed_xml'] = entry['proposed_xml'].replace(tail + '.', '.')
entry['reason'] = entry['reason'].replace(
    "Le doublon rédactionnel de compétence pour un établissement public de l'État est signalé dans les notes, sans lui attribuer un gain matériel.",
    "La répétition finale d'une même attribution au président du conseil d'administration d'un établissement public de l'État est retirée à titre rédactionnel, explicitement et sans lui attribuer un gain matériel."
)
entry['review_notes'] = entry['review_notes'].replace(
    "Anomalie préexistante conservée et signalée :",
    "Anomalie préexistante signalée et corrigée sans changement de compétence :"
).replace(
    "ce doublon ne crée pas deux approbations.",
    "ce doublon ne créait pas deux approbations ; seule sa dernière répétition est retirée."
)
entry['substantive_impact']['assessment'] = (
    "Le procès-verbal est coordonné à R153-13 et le 2° au champ actuel de L300-6. Les mêmes porteurs, autorités, "
    "pièces, décisions et délais sont maintenus. La répétition d'une attribution identique est corrigée sans changer "
    "le titulaire de compétence. Ces coordinations et cette correction rédactionnelle ne constituent pas des réductions matérielles supplémentaires."
)
answers['R153-13']['review_notes'] += (
    " Autre anomalie préexistante hors lot repérée lors de cette lecture : R104-30 renvoie à R104-32 pour la décision "
    "implicite, alors que le corps de R104-31 porte ce silence et R104-32 sa publicité. Ce renvoi n'est pas corrigé "
    "implicitement par la nouvelle modalité d'examen conjoint."
)

# La publicité ne doit pas conserver une liste de documents dépassée par L153-49.
entry = answers['R153-20']
old_refs = "un document mentionné aux articles L. 131-4 et L. 131-5"
new_refs = "un document mentionné aux articles L. 131-4, L. 131-5, L. 131-6 ou L. 131-8"
original = by_number['R153-20']['source_xml']
assert original.count(old_refs) == 2
entry['proposed_xml'] = original.replace(old_refs, new_refs)
entry['status'] = 'rewrite_draft'
entry.pop('classification', None)
entry['reason'] = (
    "Coordination nécessaire des seuls I 3° et II 5° : leurs références réglementaires s'arrêtent à L131-4/L131-5 "
    "alors que L153-49, L153-50 et les procédures L153-51/L153-53 couvrent aussi les documents de L131-6/L131-8. "
    "Les deux listes sont alignées sur ce champ légal existant. Toutes les catégories et leurs numéros sont conservés ; "
    "la publicité nécessaire aux droits des tiers subsiste. Le retrait de l'annonce de presse est porté par R153-21, "
    "pas compté une deuxième fois ici."
)
entry['review_notes'] = (
    "L131-4 à L131-8, L153-49 à L153-53, L153-58/59, L153-23 et R153-21/22 lus intégralement. "
    "Incohérence préexistante signalée : I 3° et II 5° omettent deux renvois présents dans le champ légal de mise "
    "en compatibilité. La correction n'étend aucune obligation de compatibilité ou de prise en compte ; elle explicite "
    "le régime de publicité des actes correspondants, déjà soumis aux exigences légales de publication. La distinction "
    "entre compatibilité et prise en compte demeure dans les lois visées. Les trois rubriques du I et huit du II "
    "restent à leur place, y compris environnement, évaluation et mise à jour. R153-21 conserve le recueil et le mois "
    "d'affichage mais retire la presse ; R153-22 vise le II et conserve son propre régime. Les transitions historiques "
    "de L131-6 (1er avril 2021) et L131-7/8 et L153-51 (26 mai 2026, procédures antérieures exclues selon leurs "
    "notes) demeurent ; aucune date de réforme future n'en est déduite. Aucun acte régulièrement publié n'est à republier "
    "du seul fait de cette clarification, et aucun délai de recours expiré n'est rouvert."
)
entry['proposed_xml'] += (
    "\n<p>La coordination des références figurant au 3° du I et au 5° du II s'applique aux publicités restant à accomplir "
    "à l'entrée en vigueur des présentes dispositions. Elle n'impose pas de republier les actes ayant déjà fait l'objet "
    "d'une publicité régulière et ne rouvre aucun délai de recours expiré.</p>"
)
entry['substantive_impact'] = impact(
    'coordination_only',
    "La source réglementaire entière conserve deux listes de références plus étroites que les dispositions législatives "
    "qu'elle applique. Leur alignement rend explicite le régime de publicité de mises en compatibilité déjà prévues "
    "par la loi ; il ne supprime aucune obligation autonome et ne compte pas comme nouvelle réduction.",
    "Les modalités de publication restent nécessaires à l'opposabilité et aux recours. Le coût d'application explicite "
    "du régime aux actes relatifs à L131-6/L131-8 n'est pas évalué ; aucune baisse nette de publicité ou de coût n'est "
    "attribuée à cette coordination. Les mesures de R153-21/R153-22 restent distinctes de la liste des actes.",
    "Aucune obligation substantielle nouvelle de compatibilité, de pièce ou de collecte n'est créée. Le rattachement "
    "réglementaire aux modalités de publicité est explicité pour deux références légales omises, la publication étant "
    "déjà exigée par L153-53 et L153-23/59 ; aucun support autonome de remplacement ni reprise des actes régulièrement "
    "publiés n'est imposé. Le coût des modalités applicables reste non chiffré.",
    [effect(
        'coordination', 'urbanisme-publicite-champ-mise-compatibilite',
        "Alignement des listes de documents des I 3° et II 5° sur le champ légal actuel des mises en compatibilité.",
        "Les I 3° et II 5° ne citent que L131-4 et L131-5, tandis que L153-49 et L153-50 couvrent aussi L131-6 et L131-8 ; les lois imposent déjà la publication des décisions.",
        "Les deux rubriques citent aussi L131-6 et L131-8 sans nouvelle obligation substantielle de compatibilité ; leurs actes suivent le régime de publicité applicable.",
        "Autorités publiant les mises en compatibilité de PLU relatives aux documents légalement visés ; personnes ayant intérêt à leur consultation ou contestation.",
        "Publicités restant à accomplir ; aucune republication des actes régulièrement publiés ni réouverture des délais de recours expirés. Les transitions des dispositions législatives visées restent applicables.",
        "Pas de nouveau dossier ou collecte ; explicitation du rattachement aux publicités existantes, dont le coût de mise en œuvre n'est pas mesuré.",
        old_refs, new_refs,
    )],
)
answers['R161-8']['review_notes'] += (
    " L126-6-1 CCH a également été lu en entier : son diagnostic poursuit une fonction de sécurité structurelle et "
    "le projet de plan pluriannuel de travaux en copropriété peut le satisfaire. L'annexe maintenue ne retire ni "
    "cette substitution favorable ni ses autres conditions ; elle ne crée pas de second diagnostic."
)
answers['R161-5']['proposed_xml'] = answers['R161-5']['proposed_xml'].replace(
    "Les autorisations régulièrement délivrées et les droits qu'elles ont créés demeurent préservés.</p>",
    "Les autorisations régulièrement délivrées et les droits qu'elles ont créés demeurent préservés, sans faire obstacle "
    "aux règles de sécurité, de salubrité et de protection de l'environnement ni aux voies de recours qui leur sont applicables.</p>"
)


assert set(answers) == set(by_number)
output = [answers[source['number']] for source in sources]
Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')
print(f'{len(output)} articles écrits dans answer.json')
