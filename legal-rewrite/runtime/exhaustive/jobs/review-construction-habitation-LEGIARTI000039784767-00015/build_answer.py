import html
import json
import re
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())


def paragraphs(xml):
    return re.findall(r'<p>.*?</p>', xml, re.S)


def plain(xml):
    return html.unescape(re.sub(r'<[^>]+>', '', xml))


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return {
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population,
        'conditions_and_transition': transition,
        'replacement_or_new_burdens': burdens,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }


answer = []
for source in sources:
    answer.append({
        key: source[key]
        for key in ['code_id', 'source_id', 'source_sha256', 'number']
    })

# L411-1 : conserver la réduction acquise et réparer le renvoi de stationnement.
a = answer[0]
p = paragraphs(sources[0]['previous_draft']['proposed_xml'])
p[1] = (
    "<p>Des dépendances, des annexes et des jardins privatifs ou collectifs peuvent être adjoints à ces habitations, qu'ils soient accolés ou non aux immeubles. "
    "Aucune condition particulière d'adjonction ne peut être imposée par décision administrative sur le fondement du présent alinéa. "
    "Les règles d'urbanisme, de sécurité, de salubrité et d'accessibilité qui disposent d'un fondement distinct demeurent applicables.</p>"
)
p[5] = (
    "<p>Lorsque les aires de stationnement sont mutualisées dans le respect des règles d'urbanisme applicables, "
    "les organismes d'habitations à loyer modéré peuvent également louer librement les aires dont ils disposent.</p>"
)
p[-1] = (
    "<p>La suppression des conditions administratives particulières d'adjonction prévue au deuxième alinéa et la faculté de location prévue au sixième alinéa "
    "s'appliquent à compter de la date d'entrée en vigueur de la loi, y compris aux opérations et mutualisations en cours, "
    "sans remise en cause des droits des tiers, des aides accordées et des engagements contractuels valablement souscrits avant cette date.</p>"
)
a.update({
    'proposed_xml': '\n'.join(p),
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Assujettissement de l'adjonction de dépendances, annexes et jardins à des conditions administratives particulières prises sur le fondement du deuxième alinéa."
    ],
    'reason': (
        "La seconde passe conserve la suppression de fond déjà acquise : l'adjonction de dépendances, annexes ou jardins ne dépend plus de conditions administratives spéciales propres à ce texte. "
        "Ces conditions ne démontrent pas de fonction essentielle distincte des règles générales de sécurité, salubrité, accessibilité et urbanisme, qui restent applicables. "
        "Elle corrige en outre réellement le sixième alinéa : le renvoi à L. 151-47 du code de l'urbanisme, qui ne définit pas la mutualisation des places, est remplacé par un fondement autonome de location des aires légalement mutualisées. "
        "Cette correction favorable ne dispense d'aucune règle d'urbanisme. Les caractéristiques techniques et de prix de revient définissent les logements sociaux et leur financement ; les retirer indistinctement exposerait les aides et la qualité des logements. "
        "La destination aux ménages modestes, les constructions accessoires et les droits des locataires demeurent nécessaires. "
        "Les facultés de location libre, la précarité et la révocabilité, l'usage de toute place libre sans préférence et la limite des droits disponibles sont conservés à droit constant. "
        "Aucune nouvelle coupe de ces protections n'est justifiée ; la réduction de l'adjonction n'est pas présentée comme nouvelle par rapport au précédent brouillon."
    ),
    'review_notes': (
        "Les huit alinéas substantiels gardent leur position ; seul le neuvième porte la transition. Source entière, notes vides, précédent brouillon et texte initial SRU 144 lus : SRU 144 n'a ajouté que la location des places vacantes et la priorité des locataires, non l'ensemble de cet article. "
        "R. 411-1, lu dans le corpus, appelle la suppression de son second alinéa pour les seules conditions d'adjonction. Son premier alinéa relatif aux caractéristiques techniques et au prix de revient reste autonome. "
        "Les arrêtés d'application ne sont pas fournis : leur inventaire et le retrait de leurs seules prescriptions fondées sur l'habilitation supprimée restent à effectuer ; aucune purge réglementaire exhaustive n'est affirmée. "
        "L. 442-6-4, lu en entier, protège la renonciation au stationnement, la réduction correspondante de loyer et de charges et la validité du bail : ces droits ne sont pas supprimés. "
        "L. 151-47, lu avec ses notes, porte sur le PLU tenant lieu de plan de mobilité, et ne formule pas la mutualisation alléguée par le renvoi source. L. 151-33 et R. 151-45, lus, comportent des possibilités distinctes et ne sont pas substitués artificiellement à ce renvoi. "
        "Le nouveau sixième alinéa couvre expressément toute mutualisation licite ; il conserve ainsi la faculté favorable sans restriction au seul PLU tenant lieu de plan de mobilité. L'étendue exacte auparavant attribuable au renvoi erroné n'est pas démontrée : aucune extension chiffrée ni seconde réduction de formalité n'est comptée. "
        "Le troisième alinéa reste le support des produits des locaux annexes et accessoires nécessaires à la vie économique et sociale : CGI 207, 1, 4° b et 4° quater b, lu en entier avec ses notes, conserve ses exonérations, y compris pour les opérations futures éligibles. "
        "La présente correction ne crée aucun renvoi à une cible non fournie dans reference-targets.json ; les contrôles facultatifs de R. 411-1, L. 442-6-4, L. 151-47, L. 151-33, R. 151-45 et CGI 207 reposent sur le corpus public fourni. La filiation réglementaire des conditions d'adjonction reste partiellement documentée ; ce lot ne solde pas l'examen des 209 articles SRU."
    ),
    'reference_checks': [],
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': (
            "Par rapport à la source officielle entière, les conditions administratives spécifiques d'adjonction sont effectivement retirées, sans remplacement. "
            "La réduction était déjà présente dans le précédent brouillon ; cette passe la conserve et corrige le renvoi incohérent du stationnement. "
            "Elle ne revendique ni baisse d'impôt ni suppression des normes techniques générales ou des droits des locataires."
        ),
        'scope_limitations': (
            "Seule l'habilitation spéciale du deuxième alinéa est supprimée ; les normes techniques, prix de revient, urbanisme, sécurité et conditions de financement autonomes demeurent. "
            "R. 411-1 et les arrêtés nécessitent coordination hors du lot. Le champ historique exact du renvoi de stationnement n'est pas établi ; aucun gain national ni solde global de complexité n'est chiffré."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : ni autorisation, ni déclaration, ni registre, ni justificatif ou délai ne remplace les conditions d'adjonction. "
            "La réserve des règles générales et la protection des contrats antérieurs n'imposent pas de nouvelle démarche ; le stationnement conserve ses garanties existantes."
        ),
        'effects': [
            effect(
                'obligation_removed', 'hlm-annexes-fin-conditions-administratives',
                "Suppression de l'assujettissement à des conditions administratives particulières pour adjoindre dépendances, annexes et jardins aux logements sociaux.",
                "Organismes et opérations de logement social : adjonction soumise aux conditions fixées par décision administrative, outre le droit commun.",
                "Mêmes organismes et aménagements : aucune condition administrative particulière sur ce fondement ; seules les règles autonomes demeurent.",
                'legal_duty', "Organismes HLM et opérations portant sur les dépendances, annexes et jardins des habitations du premier alinéa.",
                "Dès l'entrée en vigueur de la loi, opérations en cours comprises ; droits des tiers, aides attribuées et engagements contractuels antérieurs préservés.",
                "Aucune demande ou déclaration de remplacement ; coordination de R. 411-1 et des arrêtés encore nécessaire.",
                "A ces habitations peuvent être adjoints, dans des conditions fixées par décision administrative, des dépendances, des annexes et des jardins privatifs ou collectifs, accolés ou non aux immeubles.",
                "Aucune condition particulière d'adjonction ne peut être imposée par décision administrative sur le fondement du présent alinéa."
            ),
            effect(
                'coordination', 'hlm-stationnement-mutualise-fondement-autonome',
                "Fondement autonome de la location libre des places légalement mutualisées après constat d'un renvoi sans correspondance explicite.",
                "La faculté favorable renvoie à L. 151-47, texte sur le PLU tenant lieu de plan de mobilité qui ne définit pas cette mutualisation.",
                "La faculté favorable vise toute mutualisation respectant les règles d'urbanisme applicables, avec maintien des droits d'usage et des priorités.",
                'regime', "Organismes HLM, leurs locataires et autres usagers de stationnements mutualisés.",
                "Entrée en vigueur de la loi, mutualisations en cours comprises ; contrats valables et droits des tiers préservés.",
                "Aucune formalité nouvelle ; la légalité urbanistique reste requise sur ses fondements propres. Aucun gain quantitatif supplémentaire démontré.",
                "Lorsque les aires de stationnement sont mutualisées en application de l'article L. 151-47 du code de l'urbanisme, les organismes d'habitations à loyer modéré peuvent également louer librement les aires de stationnement dont ils disposent.",
                plain(p[5])
            ),
        ],
    },
})

# L411-2 : rendre générale la suppression ciblée du double accord, sans toucher aux aides.
a = answer[1]
p = paragraphs(sources[1]['previous_draft']['proposed_xml'])
p[9] = (
    "<p>- la gestion ou l'acquisition en vue de la revente de logements situés dans des copropriétés connaissant des difficultés importantes de fonctionnement "
    "ou faisant l'objet d'un plan de sauvegarde en application de l'article L. 615-1 ou d'une opération programmée d'amélioration de l'habitat visée à l'article L. 303-1, "
    "ou situés dans le périmètre d'opérations de requalification de copropriétés dégradées prévues à l'article L. 741-1. "
    "Ce service comprend également, pendant dix ans au plus à compter de la première cession, la gestion des copropriétés issues de la cession des logements locatifs "
    "mentionnés au neuvième alinéa du présent article, tant que l'organisme vendeur y reste propriétaire de logements. "
    "Ces activités sont exercées sans accord préalable du maire de la commune d'implantation ni du représentant de l'État dans le département, "
    "sans demande à cette fin et sans délai d'opposition. Aucun avis ni aucune déclaration de remplacement n'est exigé sur ce fondement. "
    "Cette dispense s'applique également aux accords des mêmes autorités exigés par les dispositions définissant les compétences des organismes, pour les seules activités mentionnées au présent alinéa ; "
    "les autres limites de ces compétences demeurent applicables ;</p>"
)
p.append(
    "<p>La suppression des accords, demandes et délais d'opposition prévue au onzième alinéa s'applique dès l'entrée en vigueur de la loi, "
    "y compris aux opérations et demandes en cours, sans nouveau dépôt. Les exonérations fiscales et aides spécifiques restent ouvertes aux opérations futures remplissant les autres conditions du présent article. "
    "Les aides régulièrement accordées, les droits des occupants et des tiers ainsi que les engagements contractuels valablement souscrits avant cette date sont préservés. "
    "Les stipulations qui se bornent à rappeler les accords légaux supprimés cessent de les imposer pour l'avenir. "
    "Cette suppression ne remet pas en cause les décisions et responsabilités relatives à des faits antérieurs et ne crée aucun droit à un remboursement rétroactif général.</p>"
)
a.update({
    'proposed_xml': '\n'.join(p),
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Accord préalable du maire et du représentant de l'État conditionnant les activités relatives aux copropriétés en difficulté et leur appartenance au service d'intérêt général, y compris les mêmes accords prévus par les règles organiques pour ces seules activités.",
        "Demande administrative et circuit d'opposition préfectorale de deux mois propres à ces accords, sans déclaration ni avis de substitution."
    ],
    'reason': (
        "Réforme de fond supplémentaire par rapport au précédent brouillon, qui ne faisait que coordonner L. 302-5 : les interventions visées dans les copropriétés en difficulté "
        "ne sont plus subordonnées à l'accord du maire et du préfet, ni à une demande et au circuit d'opposition de deux mois. "
        "Le même double accord ne peut subsister au titre des compétences organiques pour ces seules activités ; les autres limites organiques sont conservées. "
        "Ce filtrage supplémentaire n'a pas de fonction essentielle distincte démontrée, dès lors que subsistent les catégories de copropriétés, les plans et opérations légalement encadrés, "
        "les droits de leurs propriétaires et occupants, les contrôles des organismes et les règles européennes de financement. Aucune déclaration ne remplace l'accord. "
        "La suppression étend aux autres organismes éligibles le principe déjà retenu pour les coopératives HLM et en assure la cohérence dans la définition du service d'intérêt général. "
        "La coordination antérieure vers le IV autonome de L. 302-5 est conservée sans rétablir quotas ou inventaires. "
        "Les exonérations, aides, garanties des accédants et la possibilité de dividende limité sont maintenues, de même que les conditions de ressources et loyers, "
        "les seuils de 10 %, 11 % et 25 %, la période historique jusqu'au 1er janvier 2020 et la limite de dix ans avec propriété persistante. "
        "La comptabilité distincte et l'affectation des résultats ont une fonction de traçabilité des compensations et de prévention de leur emploi hors mission ; ce ne sont pas deux déclarations redondantes à supprimer. "
        "L'interdiction d'être tiers-financeur limite un risque financier distinct et n'est pas effacée. Ces maintiens de fond ne sont pas comptés comme simplifications."
    ),
    'review_notes': (
        "Source, notes, précédent brouillon, SRU 82 et SRU 145 lus intégralement. SRU 145 avait ajouté le bénéfice fiscal et la faculté d'action pour la mixité ; "
        "il n'établit pas la filiation de chacune des règles actuelles. SRU 82 porte notamment sur les lots sous plan de sauvegarde ; ses anciennes positions d'alinéas ne sont pas réimportées. "
        "La structure de la liste, y compris les sociétés de vente après les sociétés de coordination, est conservée ; aucune insertion avant le renvoi au neuvième alinéa. "
        "Les alinéas définissant le service restent à leur place, afin de préserver notamment CGI 207, 1, 4° a, 4° quater a, 14° a et 15° b ; CGI 207 et ses notes ont été lus en entier. "
        "Le neuvième alinéa au sens de la liste légale vise les opérations locatives : la séparation source par br entre sociétés de coordination et de vente est conservée. "
        "La qualification SIEG reste soumise au cadre européen cité par la source ; la suppression de deux accords français ne dispense ni d'un mandat nécessaire, ni de la traçabilité des compensations, ni des contrôles de surcompensation. "
        "Le contenu et l'applicabilité actuels de l'ensemble du droit européen des aides n'ont pas été vérifiés hors des pièces locales : aucune conformité générale n'est certifiée. "
        "Les passages pertinents de L. 421-1, L. 422-2 et L. 422-3 ont été confrontés : L. 422-2 comporte encore le double accord et L. 422-3 proposé le retire déjà pour les coopératives. "
        "La dispense expresse dans le présent corps évite son rétablissement pour les seules activités qu'il définit ; l'harmonisation rédactionnelle de ces dispositions et de leurs règlements reste nécessaire hors du lot. "
        "Les autres accords du maire, notamment pour des compétences plus larges de gestion relevant de L. 442-11, ne sont pas supprimés en bloc ; aucune acquisition en dehors de l'objet légal n'est autorisée. "
        "La décision du syndic ou des copropriétaires, le plan de sauvegarde de L. 615-1 et les procédures de L. 615-10 ne sont pas remplacés par cette dispense. "
        "L. 831-1 et la source ainsi que la proposition de L. 302-5 ont été lus : la référence au IV conserve les catégories et assimilations de logements, et ne fait pas revivre les quotas. "
        "L'expiration au 1er janvier 2020 du volet intermédiaire historique n'est pas repoussée ; ses droits et contentieux restent possibles, sans nouvelle fermeture des avantages non expirés. "
        "La note source relative à l'ancien dernier alinéa vise le compte SIEG, devenu avant-dernier après ajout de la transition : son application aux exercices ouverts à compter du 1er janvier 2021 reste dans ce champ, et ne date pas la présente réforme. "
        "Les trois cibles de droit du travail requises par reference-targets.json ne sont pas citées dans la source : elles ne régissent ni le compte SIEG ni le contrat de concession immobilière de L. 615-10. "
        "Aucun renvoi nouveau à une cible absente n'est introduit dans le corps proposé. Les autres références conservées, notamment loi du 10 juillet 1965, article 29-11, L. 303-1, L. 741-1, L. 422-5 et titre IX du livre III, "
        "ne sont pas prétendues intégralement auditées par les quatre contrôles requis. Le lot ne clôt pas les 209 filiations SRU."
    ),
    'benefit_review': (
        "Avantages examinés séparément : les exonérations fiscales et aides spécifiques de l'État au titre du service d'intérêt général sont expressément maintenues pour tous les types d'organismes énumérés et les futures opérations éligibles. "
        "Leur appartenance au service ne peut plus être refusée pour la seule absence des deux accords supprimés. "
        "Les opérations locatives pour ménages sous plafonds et loyers plafonnés conservent leur champ ; l'inclusion intermédiaire de moins de 10 % jusqu'au 1er janvier 2020 reste disponible pour les seules périodes historiques qu'elle couvrait, "
        "sans nouvelle suppression ni réouverture d'un avantage déjà expiré dans la source. "
        "L'accession conserve la majoration de 11 % des plafonds, ainsi que la dérogation pour revenus intermédiaires dans la limite de 25 % des logements vendus et des plafonds du titre IX majorés de 11 %, avec les garanties pour l'accédant. "
        "Le service relatif aux copropriétés en difficulté, plans de sauvegarde, OPAH et opérations de requalification conserve ses catégories ; la gestion après première cession demeure incluse pendant dix ans au plus tant que l'organisme possède des logements. "
        "L'intervention comme opérateur, les services accessoires et les services entre organismes gardent le bénéfice de leur inclusion. La faculté d'aménagement, d'accession et de prestations de services pour la mission d'intérêt général est maintenue sans quota communal nouveau. "
        "La faculté de distribuer un dividende dans la limite des clauses types de L. 422-5 reste ouverte : l'affectation du compte SIEG ne la neutralise pas. "
        "Les plafonds et garanties protègent la destination sociale et les bénéficiaires ; la séparation comptable et l'interdiction d'être tiers-financeur ne sont pas des exonérations supprimées. "
        "L. 615-10 conserve la possibilité d'intervention et le droit des propriétaires occupants aux allocations de logement selon son régime propre. "
        "Aucune exonération de CGI 207 attachée à ces activités n'est supprimée, et l'IS à la distribution ne sert pas à taxer ces produits exonérés ; sa mise en œuvre fiscale reste dans les articles du CGI compétents. "
        "Aucune taxe n'étant supprimée dans cet article, aucun avantage n'est déclaré sans objet pour ce motif."
    ),
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': (
            "La source officielle entière impose encore deux accords et une demande avec opposition préfectorale sous deux mois pour le volet copropriétés. "
            "Le corps proposé les supprime pour ce seul champ, sans remplacement, et maintient les bénéfices du service d'intérêt général. "
            "Il s'agit d'une coupe supplémentaire réelle par rapport au brouillon, dédupliquée avec la même dispense déjà retenue pour les coopératives ; le renvoi au IV de L. 302-5 est seulement coordonné."
        ),
        'scope_limitations': (
            "La dispense concerne les seules activités de copropriétés définies par cet alinéa ; les autres compétences, limites, accords autonomes, procédures de copropriété et exigences européennes demeurent. "
            "La cohérence rédactionnelle des textes organiques et réglementaires extérieurs au lot reste à assurer. Ni économie budgétaire ni réduction nette de l'ensemble des codes ne sont établies."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : aucun avis, déclaration, registre, dossier, attestation ou délai ne remplace les deux accords. "
            "Le maintien de la comptabilité SIEG, de ses affectations, plafonds et garanties reprend des exigences déjà présentes dans la source ; il ne crée pas de condition supplémentaire d'aide."
        ),
        'effects': [
            effect(
                'authorization_removed', 'hlm-coproprietes-fin-accords-prealables',
                "Suppression du double accord local et préfectoral et de son circuit de demande/opposition pour le volet copropriétés du service d'intérêt général.",
                "Organismes HLM : accord du maire et du préfet ; une opposition préfectorale peut être notifiée sous deux mois après réception de la demande. Ce délai n'est pas un minimum général d'attente.",
                "Mêmes activités éligibles : absence d'accord préalable, de demande et de délai d'opposition sur ce fondement, y compris les mêmes accords organiques pour ces activités ; autres conditions inchangées.",
                'legal_duty', "Organismes HLM exerçant les activités relatives aux copropriétés en difficulté énumérées à cet alinéa ; dispense coopérative déjà retenue incluse, non recomptée.",
                "Dès l'entrée en vigueur, demandes et opérations en cours comprises ; aides, occupants, tiers et contrats antérieurs protégés ; aucune nouvelle procédure de remplacement.",
                "Aucun avis ni déclaration de remplacement. Les règles européennes, civiles et les limites organiques autres que ces accords restent applicables.",
                "avec l'accord du maire de la commune d'implantation et du représentant de l'Etat dans le département",
                "Ces activités sont exercées sans accord préalable du maire de la commune d'implantation ni du représentant de l'État dans le département, sans demande à cette fin et sans délai d'opposition."
            ),
            effect(
                'coordination', 'sru-quotas-communaux-suppression',
                "Précision du renvoi de définition vers le IV autonome de L. 302-5 ; aucune nouvelle suppression de quota n'est comptée dans cet article.",
                "Le volet historique intermédiaire renvoie globalement aux logements locatifs sociaux de L. 302-5, qui contient également des quotas et territoires.",
                "Le même dénominateur renvoie expressément au IV définissant les logements ; maintien du seuil inférieur à 10 % et de l'échéance historique du 1er janvier 2020.",
                'regime', "Organismes HLM et situations historiques de revenu intermédiaire couvertes par cet alinéa.",
                "Coordination à l'entrée en vigueur avec la suppression des quotas ; aucun avantage historique ni recours n'est fermé, aucune période expirée n'est rouverte.",
                "Aucun inventaire, collecte ou justificatif supplémentaire ; aucune nouvelle réduction fiscale dénombrée.",
                "des logements locatifs sociaux mentionnés à l'article L. 302-5 détenus par l'organisme",
                "des logements locatifs sociaux mentionnés au IV de l'article L. 302-5 détenus par l'organisme"
            ),
        ],
    },
})

assessments = {
    'L1234-1': (
        "La source L. 411-2 ne renvoie pas à cet article : ses accords de copropriété et ses plafonds ne sont pas un préavis de licenciement. "
        "Le texte officiel L. 1234-1 module le préavis selon six mois et deux ans d'ancienneté ; la proposition fournie retient quinze jours calendaires indépendamment de l'ancienneté pour les nouveaux contrats, "
        "avec conservation des anciennes règles pour les contrats antérieurs et des procédures collectives et protections. "
        "La notification et son point de départ ne sont pas fixés par L. 411-2 : la coordination travail renvoie à L. 1234-3 proposé, non fourni parmi ces cibles. "
        "Le contrat de concession de L. 615-10 et le statut public d'un organisme ne permettent pas de transposer ce préavis à une concession ou aux agents publics."
    ),
    'L1221-2': (
        "Aucun renvoi à L. 1221-2 n'existe dans la source L. 411-2. La cible officielle admet encore le terme dans les cas de CDD ; sa proposition impose une durée indéterminée aux contrats de travail nouveaux et "
        "préserve les anciens contrats sans renouvellement contournant la bascule. Les dix ans de gestion d'une copropriété, la durée d'un plan, d'une aide ou de la concession de L. 615-10 ne sont pas une durée d'emploi. "
        "Aucun nouveau CDD n'est donc autorisé ici ; l'emploi privé éventuellement exercé par un HLM relève séparément du contrat unique, sans assimilation automatique des agents publics."
    ),
    'L1234-9': (
        "L. 411-2 ne vise aucune indemnité de licenciement. La source de L. 1234-9 ouvre le droit après huit mois avec exception de faute grave ; la proposition fournie distingue les nouveaux contrats "
        "(un an au terme effectif, préavis exécuté ou non inclus, sous réserve de l'essai ; 0,20 mois par année totale, fractions par mois complets, plafond de six mois, initiative patronale et exception de faute grave) "
        "des contrats antérieurs et de leurs composantes acquises. La première année n'est pas déduite lorsque le seuil est atteint ; la démission ordinaire n'ouvre pas l'indemnité, et les indemnités spéciales, "
        "salaires, congés et réparations restent distincts. Aucun de ces calculs ni aucune notification n'est modifié par le compte SIEG ou la suppression des accords immobiliers de L. 411-2."
    ),
    'L615-10': (
        "Renvoi effectivement présent dans le volet opérateur de L. 411-2 : il vise l'expérimentation d'expropriation des parties communes, sa concession, leur entretien et la redevance, "
        "non un contrat de travail. La cible officielle prévoit vingt ans depuis la loi du 24 mars 2014 ; la proposition retire seulement l'actualisation triennale obligatoire du plan, sans prolonger l'expérimentation "
        "ni supprimer entretien, responsabilité, provisions, droits des propriétaires ou allocation logement des propriétaires occupants. "
        "Le renvoi est conservé avec l'interdiction pour le HLM d'être tiers-financeur ; la dispense d'accords du volet précédent ne supprime pas les procédures d'expropriation ou avis propres à L. 615-10. "
        "Aucune ancienneté salariale ni notification de rupture n'est pertinente pour cette concession : les quinze jours et l'indemnité ordinaire du contrat unique ne s'y appliquent pas."
    ),
}
key = a['code_id'] + '|' + a['source_id']
a['reference_checks'] = [
    {
        'target_key': target_key,
        'view_sha256': references['targets'][target_key]['view_sha256'],
        'assessment': assessments[references['targets'][target_key]['number']],
    }
    for target_key in references['requirements'][key]
]

# L411-3 : conserver la suppression de copie et rendre opératoire la coordination SRU.
a = answer[2]
p = paragraphs(sources[2]['previous_draft']['proposed_xml'])
p[2] = p[2].replace(
    "ou du VI de l'article L. 353-15 ;</p>",
    "ou du VI de l'article L. 353-15 ; pour l'application de ce VI et de la présente exception, "
    "l'exclusion territoriale prévue au VII du même article ne s'applique plus à compter de l'entrée en vigueur de la loi, y compris aux opérations en cours ;</p>"
)
a.update({
    'proposed_xml': '\n'.join(p),
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Reproduction intégrale obligatoire du présent article dans chaque nouvel acte de transfert de propriété ou de jouissance ou constatant ce transfert, sans mention ni attestation de remplacement.",
        "Nullité de plein droit et action spéciale fondées uniquement sur l'absence de cette reproduction dans les actes nouveaux ; conservation de leur régime pour les actes antérieurs.",
        "Application, par le renvoi au VI de L. 353-15, de l'exclusion territoriale de son VII liée aux anciennes communes à quotas, pour les opérations futures et en cours."
    ],
    'reason': (
        "La suppression de fond acquise au précédent brouillon est conservée : les nouveaux actes ne doivent plus recopier l'article entier et leur validité ne dépend plus de cette seule copie. "
        "Aucune mention, attestation ou dépôt de substitution n'est créé. La seconde passe ajoute une coordination opératoire jusque-là seulement signalée en note : "
        "l'exclusion territoriale du VII de L. 353-15 ne peut plus faire obstacle à son VI ni à l'exception du troisième alinéa, y compris pour les opérations en cours. "
        "C'est une coordination de la mesure SRU déjà décidée, non une deuxième suppression de quota. "
        "Après réexamen, aucune suppression supplémentaire des conditions de ressources, de loyers, du maintien dans les lieux et de l'action au juge n'est justifiée : "
        "ces protections empêchent la disparition des droits des occupants lors de la cession de logements financés par l'État, y compris les cessions non volontaires. "
        "L'annulation pour violation du fond, distincte de la copie formelle, reste utile et ne recrée pas celle-ci. "
        "Les six exclusions sont des dérogations favorables conservées pour toutes les futures opérations éligibles, non réservées au stock ancien. "
        "Les autres parties du précédent corps sont maintenues à droit constant sans leur attribuer une nouvelle simplification."
    ),
    'review_notes': (
        "Source entière, notes vides, précédent brouillon et SRU 145 entier lus. Les onze alinéas substantiels conservent leur place : "
        "dispense de copie au dixième, pouvoir du juge au onzième, transition au douzième. Les exceptions actuelles, enrichies depuis 2000, ne sont pas réduites aux trois anciennes catégories SRU. "
        "Sont conservés les deux critères d'entrée (financement public ou convention), les logements appartenant ou ayant appartenu à un organisme, les transferts non volontaires et les six exclusions distinctes. "
        "L. 443-11 et L. 353-15, lus en entier, confirment les cibles : premier alinéa du II, III et VI du premier texte ; VI du second ; "
        "vente à un OFS au premier alinéa du I de L. 443-11, sans importation des autres catégories de son I ou VII. "
        "L. 353-15 VII conserve dans sa source une exclusion liée aux communes des I ou II de L. 302-5 : le troisième alinéa proposé y déroge expressément, "
        "pour l'application du VI comme pour l'exception du présent article, sans rétablir quotas ni carence. Son harmonisation formelle dans L. 353-15 reste à rédiger hors du lot ; elle n'est plus une condition implicite laissée active ici. "
        "Ce renvoi exprès au VII de L. 353-15 est nouveau dans le corps et absent des cibles de reference-targets.json ; son texte officiel entier a été vérifié dans le corpus public fourni. "
        "Les conditions propres du VI (convention ANRU, autres accords, départ du dernier locataire, habitabilité et performance énergétique applicables) ne sont pas supprimées par la coordination territoriale. "
        "L. 443-6-2 et L. 615-1, lus en entier, ainsi que les passages sur lots et plans de sauvegarde de L. 421-1, L. 422-2 et L. 422-3, "
        "confirment les objets des exclusions SCI et portage provisoire ; l'acquisition de parts SCI seule ne rend pas le logement propriété de l'associé personne physique. "
        "L. 353-14 et L. 442-6 ont été lus intégralement ; les régimes autonomes de convention et maintien dans les lieux ne sont pas réécrits. "
        "R. 491-1, R. 491-2, R. 491-5 et R. 491-6, lus avec leurs notes, gardent les plafonds, leur actualisation et les mentions de bail utiles sur l'origine du régime et le loyer maximal ; "
        "ils n'exigent pas une copie intégrale substituée à celle supprimée. Le délai spécial de cinq ans après publication immobilière est expressément conservé pour la seule ancienne nullité de copie, "
        "même si la publication est postérieure à la réforme ; il n'est ni rouvert ni étendu à l'action de fond. "
        "Les anciens renvois SRU à L. 353-15-1 et L. 442-6-1 ne sont pas rétablis. La filiation de toutes les règles contemporaines et de tous les textes extérieurs n'est pas déclarée close. "
        "Aucune validation par un juriste ni réduction nationale chiffrée n'est affirmée."
    ),
    'reference_checks': [],
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': (
            "Comparée à la source officielle entière, la proposition retire la copie intégrale dans les actes nouveaux et sa nullité spécifique, tout en maintenant les règles de fond et les six exclusions. "
            "Ce gain était déjà acquis au brouillon. La présente passe rend également opératoire la neutralisation du filtre territorial de L. 353-15 VII, simple coordination de l'abolition des quotas déjà décidée."
        ),
        'scope_limitations': (
            "La dispense de copie ne vaut que pour les actes conclus après l'entrée en vigueur ; les anciens actes et leur délai spécial de cinq ans gardent leur régime. "
            "Les protections substantielles, droits des tiers et procédures autonomes des ventes et de l'ANRU restent applicables. L'harmonisation rédactionnelle de L. 353-15 est hors du lot ; aucun bilan national n'est établi."
        ),
        'new_burdens_review': (
            "Aucune charge nouvelle n'est identifiée : aucune formule obligatoire, déclaration, attestation, donnée, registre ou délai ne remplace la copie. "
            "L'action judiciaire pour violation des règles de fond existait déjà ; la protection des actes antérieurs n'impose pas de réfection des actes nouveaux."
        ),
        'effects': [
            effect(
                'obligation_removed', 'hlm-transferts-fin-copie-integrale-article',
                "Suppression de la copie intégrale de l'article dans les actes nouveaux et de l'anéantissement du contrat pour la seule absence de copie.",
                "Tout acte transférant ou constatant le transfert de propriété ou de jouissance des logements concernés doit reproduire l'article, à peine de nullité ; action de cinq ans depuis publication immobilière.",
                "Pour les actes nouveaux, les règles de fond s'appliquent de plein droit sans reproduction ; la seule omission de copie n'entraîne pas nullité. Aucun changement des conditions de ressources, loyers ou maintien dans les lieux.",
                'legal_duty', "Parties et rédacteurs des actes concernant les logements dans le champ, hors les six exclusions maintenues.",
                "Actes conclus dès l'entrée en vigueur de la loi ; pour les actes antérieurs, copie, nullité et action de cinq ans après publication restent régies par les anciennes dispositions, même si publication ultérieure.",
                "Aucune mention ou attestation de remplacement ; information utile des baux, contrôle du fond et accès au juge restent distincts.",
                "Tout acte transférant la propriété ou la jouissance de ces logements ou constatant ledit transfert doit, à peine de nullité de plein droit, reproduire les dispositions du présent article.",
                "Les règles de fond du présent article s'appliquent de plein droit aux actes qui transfèrent la propriété ou la jouissance de ces logements ou qui constatent ce transfert, sans qu'il soit nécessaire de les reproduire. La seule absence de reproduction du présent article dans un acte n'entraîne pas sa nullité."
            ),
            effect(
                'coordination', 'sru-quotas-communaux-suppression',
                "Neutralisation expresse du filtre territorial attaché au renvoi au VI de L. 353-15, sans compter une nouvelle abolition de quota.",
                "L'exception renvoie au VI de L. 353-15, dont le VII exclut les immeubles situés dans les communes des I ou II de L. 302-5.",
                "L'exclusion territoriale du VII ne fait plus obstacle au VI ni à l'exception de L. 411-3 ; toutes les autres conditions du VI subsistent.",
                'regime', "Opérations de vente ou changement d'usage d'ensembles de plus de cinq logements relevant du VI de L. 353-15, dans les communes auparavant exclues.",
                "Dès l'entrée en vigueur de la loi, opérations en cours comprises ; maintien des droits des occupants et conditions autonomes de la convention.",
                "Aucun dossier ni accord supplémentaire ; les accords et garanties autonomes du VI ne sont pas supprimés par le présent renvoi.",
                "en application du premier alinéa du II et des III et VI de l'article L. 443-11  ou du VI de l'article L. 353-15",
                "pour l'application de ce VI et de la présente exception, l'exclusion territoriale prévue au VII du même article ne s'applique plus à compter de l'entrée en vigueur de la loi, y compris aux opérations en cours ;"
            ),
        ],
    },
})

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
