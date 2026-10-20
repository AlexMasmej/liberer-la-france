import json
import re
from pathlib import Path


source = json.loads(Path('source.json').read_text())[0]
original = re.findall(r'<p>.*?</p>', source['source_xml'], re.S)
assert len(original) == 92
paragraphs = original.copy()


def set_paragraph(number, text):
    assert '<' not in text and '>' not in text
    paragraphs[number - 1] = '<p>' + text + '</p>'


def plain(fragment):
    return re.sub(r'<[^>]+>', '', fragment)


# Les parties maintenues sont reproduites depuis la source officielle entière.
# Le renvoi du III, 1°, a ne désignait pas l'alinéa énonçant le taux moyen.
paragraphs[24] = original[24].replace(
    'le taux moyen pondéré mentionné au premier alinéa',
    'le taux moyen pondéré mentionné au deuxième alinéa',
)

set_paragraph(37,
    "La commission peut faire appel, pour l'exercice de sa mission, à des experts. "
    "Elle rend ses conclusions l'année de l'adoption de la cotisation foncière des entreprises unique "
    "par l'établissement public de coopération intercommunale et lors de chaque transfert de charges "
    "ultérieur, sous réserve de la dispense prévue au neuvième alinéa du présent IV."
)

set_paragraph(43,
    "Lorsqu'il est fait application à un établissement public de coopération intercommunale des "
    "dispositions du présent article, la commission d'évaluation des transferts de charges doit rendre "
    "ses conclusions sur le montant des charges qui étaient déjà transférées à l'établissement public "
    "de coopération intercommunale et celui de la fiscalité ou des contributions des communes qui "
    "étaient perçues pour les financer. Toutefois, aucune nouvelle évaluation ni nouvelle conclusion "
    "n'est requise pour les mêmes compétences lorsque ces deux montants ont déjà été établis selon "
    "les méthodes prévues aux quatrième à sixième alinéas du présent IV par un rapport d'évaluation "
    "régulièrement approuvé, que le périmètre des charges et ces montants demeurent inchangés à la "
    "date de cette application et qu'ils ne font l'objet d'aucune contestation en cours. Les montants "
    "ainsi établis sont retenus sans nouvelle attestation, déclaration ou délibération exigée pour "
    "bénéficier de cette dispense. Ce rapport antérieur tient lieu des conclusions de la commission "
    "pour ces seuls éléments et est pris en compte pour l'application du 1° bis du V. "
    "Les éléments non évalués, modifiés ou contestés restent soumis "
    "à l'évaluation prévue au présent IV. La dispense ne s'applique pas aux nouveaux transferts de "
    "charges et ne supprime ni le rapport, ni son approbation, ni, le cas échéant, la constatation "
    "préfectorale prévus aux septième et huitième alinéas pour les éléments qui restent à évaluer."
)

set_paragraph(47,
    "Les attributions de compensation fixées conformément aux 2° et 5° ou, le cas échéant, au 1° bis, "
    "ainsi que celles légalement fixées en application du 4° du présent V dans sa rédaction antérieure "
    "à son abrogation, constituent une dépense obligatoire pour l'établissement public de coopération "
    "intercommunale ou, le cas échéant, les communes membres. Le conseil de l'établissement public "
    "de coopération intercommunale communique aux communes membres, avant le 15 février de chaque "
    "année, le montant prévisionnel des attributions au titre de ces reversements. Lorsque ce montant "
    "est identique au dernier montant régulièrement communiqué à la commune, aucune nouvelle "
    "communication n'est requise."
)

set_paragraph(54,
    "A défaut d'accord, le montant de l'attribution est fixé dans les conditions figurant aux 2° et 5°, "
    "sans remise en cause des attributions légalement fixées en application du 4° du présent V dans "
    "sa rédaction antérieure à son abrogation ;"
)

set_paragraph(64,
    "L'évolution des attributions de compensation au regard des dépenses liées à l'exercice des "
    "compétences de l'établissement public de coopération intercommunale n'est soumise, sur le "
    "fondement du présent 2°, à aucun rapport quinquennal, débat obligatoire, délibération spécifique "
    "ou transmission obligatoire aux communes membres."
)

set_paragraph(72,
    "Aucun protocole financier général n'est requis pour déterminer, calculer ou verser les "
    "attributions de compensation entre l'établissement public de coopération intercommunale issu "
    "de la fusion et les communes. Les règles du présent article et les délibérations qu'il prévoit "
    "s'appliquent sans ce protocole."
)

set_paragraph(81,
    "6° Les attributions de compensation fixées conformément aux 2° et 5° ou, le cas échéant, au "
    "1° bis du présent V, ainsi que celles légalement fixées en application du 4° du présent V dans "
    "sa rédaction antérieure à son abrogation, sont recalculées dans les conditions prévues au IV "
    "lors de chaque nouveau transfert de charges. Elles ne peuvent être indexées ;"
)

transitions = [
    "X. – La dispense de nouvelle évaluation et de nouvelles conclusions prévue au neuvième alinéa "
    "du IV et la dispense de communication d'un montant prévisionnel inchangé prévue au troisième "
    "alinéa du 1° du V s'appliquent aux conclusions à rendre et aux communications exigibles à "
    "compter de l'entrée en vigueur de la loi portant la présente réforme. Elles s'appliquent aux "
    "procédures en cours sans nouveau dossier ni reprise des délais. Les conclusions déjà rendues "
    "et les communications déjà effectuées ne sont pas à refaire.",
    "A compter de la même date, aucun rapport quinquennal, débat, délibération spécifique ou "
    "transmission supprimé par le dernier alinéa du 2° du V ne peut être exigé sur ce seul fondement, "
    "même au titre d'une période antérieure. La suppression de l'obligation de protocole prévue au "
    "cinquième alinéa du 1 du 5° du V s'applique également aux fusions en cours, sans nouveau dossier "
    "ni nouvelle délibération. Les rapports déjà présentés et les transmissions déjà effectuées "
    "ne sont pas à refaire.",
    "Les protocoles et délibérations valablement adoptés avant cette date, notamment le protocole "
    "concernant la métropole de Lyon, conservent leurs effets dans le respect des règles de révision "
    "applicables. Les montants d'attribution, les créances et les droits à compensation antérieurement "
    "constitués, y compris ceux légalement fixés en application du 4° du V dans sa rédaction antérieure "
    "à son abrogation, ne sont pas modifiés du seul fait des suppressions et dispenses prévues au "
    "présent article. Les contrôles et les recours relatifs à ces droits demeurent ouverts dans "
    "leurs conditions légales.",
    "Pour les centrales de production d'énergie électrique d'origine hydraulique relevant du régime "
    "d'autorisation mentionné au premier alinéa de l'article L. 511-5 du code de l'énergie, les "
    "dispositions du présent article résultant de l'article 8 de la loi n° 2026-554 du 29 juin 2026 "
    "s'appliquent à compter des impositions établies au titre de l'année qui suit la résiliation "
    "de leur contrat de concession.",
]

proposed_xml = '\n'.join(paragraphs + ['<p>' + t + '</p>' for t in transitions]) + '\n'


def effect(kind, measure_id, description, before, after, unit, population,
           conditions, replacement, source_quote, proposed_quote):
    return dict(
        kind=kind, measure_id=measure_id, description=description,
        before=before, after=after, unit=unit, affected_population=population,
        conditions_and_transition=conditions,
        replacement_or_new_burdens=replacement,
        source_quote=source_quote, proposed_quote=proposed_quote,
    )


effects = [
    effect(
        'obligation_removed',
        'attributions-compensation-fin-rapport-quinquennal',
        "Suppression du circuit quinquennal autonome : rapport du président, débat, "
        "délibération spécifique constatant le débat et transmission obligatoire aux communes.",
        "Un rapport tous les cinq ans, un débat, une délibération spécifique et une transmission "
        "aux communes sur l'évolution des attributions et des dépenses de compétences.",
        "Aucune de ces quatre formalités exigible sur le fondement du V 2° ; le rapport "
        "d'évaluation des transferts du IV et les délibérations financières utiles subsistent.",
        'legal_duty',
        "Présidents et organes délibérants des EPCI concernés, communes membres ; Lyon dans "
        "le champ d'assimilation de l'article 1656.",
        "Dès l'entrée en vigueur, y compris les rapports encore exigibles sur des périodes "
        "anciennes ; aucun document déjà présenté n'est à refaire et les droits financiers sont conservés.",
        "Aucun rapport, registre, calendrier ou dépôt de remplacement ; les obligations "
        "budgétaires et contrôles autonomes conservent leur fondement propre.",
        plain(original[63]),
        plain(paragraphs[63]),
    ),
    effect(
        'obligation_removed',
        'attributions-compensation-fin-protocole-fusion',
        "Retrait du protocole financier général obligatoire de fusion, distinct des décisions "
        "qui établissent les droits à attribution de compensation.",
        "Un protocole financier général obligatoire entre l'EPCI issu de la fusion et les communes "
        "pour définir les modalités de détermination des attributions.",
        "Aucun protocole exigé pour déterminer, calculer ou verser ces attributions ; application "
        "directe des méthodes légales et des délibérations qui demeurent nécessaires.",
        'legal_duty',
        "EPCI issus d'une fusion et communes relevant du V 5° 1 ; le protocole historique de Lyon "
        "au V 5° 5 n'est pas abrogé.",
        "Suppression dès l'entrée en vigueur, y compris pour les fusions en cours ; protocoles "
        "antérieurs valables, créances et droits à compensation préservés.",
        "Aucune convention, déclaration, approbation ou nouvelle délibération de remplacement ; "
        "les délibérations déjà requises par les autres alinéas sont maintenues.",
        plain(original[71]),
        plain(paragraphs[71]),
    ),
    effect(
        'obligation_removed',
        'attributions-compensation-fin-notification-identique',
        "Suppression de la répétition annuelle d'une communication prévisionnelle déjà "
        "régulièrement faite lorsque le montant reste identique.",
        "Communication avant le 15 février de chaque année, même si le montant prévisionnel "
        "de la commune n'a pas changé.",
        "Pas de nouvelle communication du même montant ; première communication et "
        "communication d'un montant modifié toujours exigées avant le 15 février.",
        'legal_duty',
        "Conseils des EPCI soumis au présent régime et communes destinataires dont le montant "
        "prévisionnel est identique au dernier montant régulièrement communiqué.",
        "Communications exigibles à compter de l'entrée en vigueur ; aucun rattrapage ni "
        "nouvelle transmission d'une communication déjà régulièrement effectuée.",
        "Aucune confirmation négative, attestation, autorisation ou nouveau registre ; "
        "la dispense repose sur le montant et la communication existants.",
        "Le conseil de l'établissement public de coopération intercommunale communique aux communes "
        "membres, avant le 15 février de chaque année, le montant prévisionnel des attributions "
        "au titre de ces reversements.",
        "Lorsque ce montant est identique au dernier montant régulièrement communiqué à la commune, "
        "aucune nouvelle communication n'est requise.",
    ),
    effect(
        'obligation_removed',
        'clect-fin-reexamen-charges-inchangees',
        "Coupe supplémentaire par rapport au brouillon : retrait de l'obligation formelle de "
        "nouvelles conclusions sur des éléments déjà établis par un rapport régulièrement approuvé.",
        "Lors de la mise en application du régime, la CLECT doit conclure de nouveau sur les "
        "charges déjà transférées et leur financement, sans dispense expresse pour une évaluation antérieure.",
        "Évaluation et conclusions non renouvelées pour les seules compétences et montants "
        "régulièrement évalués selon les méthodes légales, approuvés, inchangés et sans contestation en cours.",
        'legal_duty',
        "CLECT, EPCI et communes lors de la mise en application de l'article, uniquement en "
        "présence d'une évaluation antérieure remplissant les conditions ; population effective non chiffrée.",
        "Conclusions à rendre après l'entrée en vigueur, procédures en cours comprises. "
        "Tout nouvel élément, élément modifié ou contesté et tout nouveau transfert reste évalué ; "
        "rapport, approbation municipale et constat préfectoral restent pour les éléments non dispensés.",
        "Aucune nouvelle pièce, attestation, déclaration ou délibération pour obtenir la dispense. "
        "Elle retire les nouvelles conclusions obligatoires, au-delà du simple réemploi "
        "d'informations déjà prévu par le CRPA ; la source n'est pas supposée imposer une "
        "nouvelle collecte de données ou un recalcul intégral dans tous les cas.",
        plain(original[42]),
        "Toutefois, aucune nouvelle évaluation ni nouvelle conclusion n'est requise pour les mêmes "
        "compétences lorsque ces deux montants ont déjà été établis selon les méthodes prévues aux "
        "quatrième à sixième alinéas du présent IV par un rapport d'évaluation régulièrement approuvé, que "
        "le périmètre des charges et ces montants demeurent inchangés à la date de cette application "
        "et qu'ils ne font l'objet d'aucune contestation en cours.",
    ),
    effect(
        'coordination',
        'cfe-correction-renvoi-taux-moyen',
        "Correction explicite du renvoi préexistant du III 1° a au taux moyen pondéré ; "
        "aucune nouvelle baisse ou hausse de CFE n'est revendiquée.",
        "Renvoi au premier alinéa du a, qui énonce la compétence de vote sans définir le taux moyen pondéré.",
        "Renvoi au deuxième alinéa du a, où le taux moyen pondéré est effectivement défini ; "
        "la majoration antérieure par le taux de fiscalité additionnelle reste identique.",
        'other',
        "EPCI concernés par la première année du régime après perception d'une fiscalité additionnelle.",
        "Coordination de référence dans le corps proposé ; aucune remise en cause des "
        "impositions légalement établies ni nouvelle procédure de vote.",
        "Aucune charge nouvelle identifiée : seule la cible du renvoi est corrigée.",
        plain(original[24]),
        plain(paragraphs[24]),
    ),
    effect(
        'coordination',
        'attributions-compensation-anciens-fondements',
        "Coordination des trois références au 4° du V déjà abrogé, avec conservation expresse "
        "des attributions légalement fixées sous ses rédactions antérieures.",
        "Le V 1°, 1° bis et 6° vise encore le 4° du V, dont l'emplacement porte seulement la mention Abrogé.",
        "Les fixations nouvelles reposent sur les 2° et 5° ou le 1° bis ; les attributions "
        "anciennement fixées sous le 4° gardent leurs droits, leur caractère obligatoire, leur "
        "recalcul lors d'un transfert et l'interdiction d'indexation.",
        'other',
        "EPCI et communes titulaires ou débiteurs d'attributions de compensation, y compris "
        "celles légalement fixées sous l'ancien 4°.",
        "Droits et créances constitués maintenus par le V 1°, le V 6° et le X ; la rédaction "
        "ancienne du 4° n'est pas remise en vigueur pour de nouvelles fixations.",
        "Aucune nouvelle évaluation ou formalité créée par cette coordination ; aucune "
        "nouvelle économie, hausse ou baisse de prélèvement n'est comptée.",
        plain(original[53]),
        plain(paragraphs[53]),
    ),
]

answer = {
    key: source[key] for key in ['code_id', 'source_id', 'source_sha256', 'number']
}
answer.update(
    proposed_xml=proposed_xml,
    reason=(
        "Réforme de fond ciblée, comparée à l'intégralité de la source officielle et du brouillon "
        "antérieur : maintien des trois coupes déjà acquises, à savoir le circuit quinquennal "
        "rapport-débat-délibération-transmission, le protocole financier général obligatoire des "
        "fusions et la notification annuelle répétée d'un montant prévisionnel inchangé. Coupe "
        "supplémentaire : suppression de l'obligation formelle de nouvelles conclusions "
        "de la CLECT pour les mêmes compétences et montants déjà évalués selon les méthodes du IV, "
        "régulièrement approuvés, inchangés et non contestés, sans attestation ni décision de "
        "remplacement. Cette dispense retire un acte obligatoire ; elle ne compte pas le seul "
        "réemploi des données comme un gain nouveau. Les éléments nouveaux, modifiés, contestés ou "
        "non évalués et chaque nouveau transfert restent évalués. La CLECT, la représentation de "
        "chaque commune, les méthodes de coût net, les majorités et le constat préfectoral subsidiaire "
        "sont nécessaires pour établir et rendre opposables les droits financiers sans permettre "
        "une réduction unilatérale injustifiée des ressources communales. L'estimation prospective "
        "reste un droit d'information de l'organe délibérant ou du tiers des conseils municipaux, "
        "sans exercice annuel automatique. Les transmissions du rapport d'évaluation permettent "
        "son approbation, les recours et le calcul des attributions ; elles ne sont pas assimilées "
        "au reporting quinquennal supprimé. A droit constant, les parties non visées sont reprises "
        "intégralement de la source, sans reformulation destinée à compter une simplification. "
        "Deux coordinations explicites corrigent la cible du taux moyen au III 1° a et les renvois "
        "au 4° du V déjà abrogé, tout en préservant ses droits anciens. Aucun taux ni assiette n'est "
        "modifié ici : affecter ou transférer un produit fiscal n'abolit pas la taxe autonome qui "
        "l'engendre. Aucun financement compensatoire n'est inventé."
    ),
    review_notes=(
        "Lecture et confrontation des 92 paragraphes de la source, des deux notes source_notes_xml, "
        "des deux entrées sru_context et du previous_draft entier ; le proposed_xml de premier niveau "
        "est identique à ce brouillon une fois les entités d'apostrophe décodées. Aucun tableau, "
        "source_companions ni formule-image assigné. Les identifiants et source_sha256 sont repris "
        "exactement et concordent avec l'entrée du corpus public local ; son XML décodé est "
        "identique à la source assignée. L'empreinte fournie n'est toutefois pas le SHA256 du "
        "champ source_xml seul ; sa méthode de calcul n'étant pas fournie, aucune "
        "authentification cryptographique n'est affirmée. Les 92 emplacements sont conservés ; quatre "
        "paragraphes X sont ajoutés. Les dispositions maintenues sont reproduites depuis la source, "
        "ce qui conserve notamment au V 1° la conjonction « ainsi qu'au III de l'article 79 » que le "
        "brouillon avait remplacée par « ou » : aucune extension silencieuse de cette faculté. "
        "Contrôle des cibles : troisième et neuvième alinéas du IV pour la dispense ; méthodes aux "
        "quatrième à sixième, rapport au septième, défaut au huitième ; le cinquième alinéa du IV "
        "reste celui du coût annualisé. Le rapport antérieur régulièrement approuvé tient lieu "
        "de nouvelles conclusions pour les seuls éléments dispensés et reste utilisable au "
        "V 1° bis : ce renvoi ne réimpose donc pas un nouveau rapport pour ces éléments. "
        "Les cinquième et avant-dernier alinéas du V 1° restent "
        "les mêmes. Le dernier alinéa du V 2° demeure occupé par la suppression du reporting, "
        "sans déplacer le recalcul à son avant-dernier alinéa visé par les V 5° 1 a et 2 a. "
        "Le protocole de fusion reste au cinquième alinéa du V 5° 1. Le III 1° a, troisième alinéa, "
        "visait erronément le premier alinéa pour le taux moyen : correction motivée vers le deuxième. "
        "Les trois mentions du 4° abrogé du V sont rendues opératoires pour les seuls droits "
        "légalement fixés avant son abrogation ; aucune formule historique manquante n'est inventée "
        "ni réactivée. Le VIII 2°, dernier alinéa, continue de viser son avant-dernier alinéa, "
        "applicable à compter de 2012. Incohérence préexistante laissée expressément à décision "
        "distincte : au III 1° b, les bornes strictes ne règlent pas explicitement les rapports "
        "exactement égaux à 10 %, 20 %, 30 %, 40 %, 50 %, 60 %, 70 %, 80 %, 90 % ou 100 % ; "
        "choisir un lissage à ces bornes sans instruction pourrait modifier l'impôt. Aucun seuil "
        "n'est donc modifié silencieusement. Contrôle des valeurs maintenues : 60 %, 20 %, cinq "
        "sixièmes, douze ans, 5 %, 30 %, 0,960, neuf et trois mois, trois et sept ans, 15 janvier "
        "et 15 février ; les dates 1986, 1991, 2010, 2011, 2012, 2014, 2016, 2019, 2023 et 2026 "
        "gardent leurs champs. Les facultés expirées en 2014 et le protocole Lyon à établir avant "
        "fin 2016 ne sont pas rouverts. Les deux notes de la loi n° 2026-554 ne datent pas la réforme "
        "future ; l'application hydraulique l'année suivant la résiliation de la concession est "
        "reprise expressément au X. Vérifications en lecture seule dans impots.json : 1379-0 bis, "
        "1519 I, 1636 B decies et 1656, ainsi que les paragraphes pertinents des renvois à 1609 nonies C, "
        "notamment 1609 quinquies C, 1638-0 bis, 1638 quater, 1639 A ter et les annexes. Les renvois "
        "entrant aux b et c du III et aux autres numéros conservent leurs cibles. Le régime de Lyon "
        "est confirmé par 1656 ; le protocole historique du V 5° 5 est maintenu. Hors des cinq codes, "
        "l'articulation des procédures de fusion avec CGCT L. 5211-41-3, des approbations avec "
        "L. 5211-5 II, des dotations avec L. 2334-7 et L. 5211-28-1, ainsi que les textes réglementaires "
        "financiers autonomes, reste à coordonner si elle exige le protocole retiré ; ces textes "
        "ne sont pas présentés comme réécrits. Les produits FNGIR et DCRTP de l'article 78 de la "
        "loi de finances pour 2010 et la fraction de TVA de l'article 55 XXIV de la loi de finances "
        "pour 2023 conservent leurs fondements propres. SRU 57 : l'ajout initial joint majorait "
        "l'attribution d'une fraction de la contribution de l'ancien CCH L. 302-8 ; cette clause "
        "n'est plus présente dans la source actuelle. SRU 92 modifiait le zonage de La Grande Borne "
        "dans l'annexe à la loi n° 96-987, sans démontrer une filiation du corps actuel. La version "
        "historique LEGIARTI000006306657 n'est pas dans le corpus fourni ; aucune pièce locale "
        "correspondante n'a été identifiée. La chaîne historique complète ne peut être certifiée "
        "avec ces seules données ; les deux filiations restent non soldées, aucun des 209 volets "
        "SRU n'est déclaré achevé sur cette base. Aucun quota, carence, prélèvement ou contribution "
        "SRU nouveau n'est rétabli. CVAE : aucune perception ni déclaration ne figure dans le corps "
        "actuel ; conserver la fraction de TVA et les montants historiques ne rétablit pas la CVAE. "
        "L'intitulé de section encore relatif à la CVAE appelle une coordination distincte avec "
        "sa suppression au 1er janvier suivant l'entrée en vigueur, sans toucher la CFE. Les "
        "exonérations CFE des microentrepreneurs et les baisses du plafonnement de 1647 B sexies "
        "gardent leur champ autonome ; ni leur taux ni leur base ni leur montant net ne sont "
        "confondus avec une attribution de compensation. La taxe additionnelle foncière de 1519 I "
        "est une taxe autonome, pas la taxe additionnelle CVAE-CCI : sa suppression éventuelle "
        "nécessiterait son propre corps et les affectations de 1379/1379-0 bis, non le seul retrait "
        "du produit au I bis 2. La franchise TASCOM QPV de 1 500 euros n'est pas restreinte par le "
        "renvoi au produit perçu. Les réformes IS à la distribution, successions, travail, retraite, "
        "littoral et rapports sociaux n'ont pas ici de fait générateur ou d'obligation à modifier. "
        "Ni gain national de recettes, ni coût administratif net, ni population effectivement "
        "bénéficiaire de la nouvelle dispense n'est chiffré. Les contrôles textuels ne constituent "
        "pas une validation juridique indépendante."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Rapport quinquennal, débat obligatoire, délibération spécifique et transmission "
        "aux communes sur l'évolution des attributions de compensation, exigibles après la réforme.",
        "Protocole financier général imposé pour déterminer les attributions de compensation "
        "après une fusion, y compris une fusion en cours, sans document de remplacement.",
        "Répétition annuelle avant le 15 février de la communication d'un montant prévisionnel "
        "strictement identique au dernier montant régulièrement communiqué à la commune.",
        "Obligation formelle de nouvelles conclusions de la CLECT pour les mêmes compétences "
        "et montants déjà établis par un rapport régulièrement approuvé, inchangés et non contestés.",
    ],
    benefit_review=(
        "I à III : les dérogations de partage et de calendrier, notamment la faculté locale de "
        "transférer une fraction d'IFER, le 15 janvier, les limites de première année, l'étalement "
        "des écarts et sa durée maximale de douze ans restent applicables aux futures situations "
        "éligibles ; les taux fiscaux autonomes ne sont pas augmentés. Les 60 %, 20 % et cinq "
        "sixièmes sont des parts de produit, pas des réductions de l'impôt des entreprises. "
        "I bis, I ter : FNGIR et DCRTP, exclusions et transferts concordants demeurent possibles ; "
        "aucune nouvelle recette ou diminution des droits n'est créée. IV : la déduction des "
        "ressources afférentes aux charges, les méthodes de coût réel et annualisé, la représentation "
        "de chaque commune, l'approbation qualifiée et la solution préfectorale subsidiaire "
        "protègent le calcul net ; elles subsistent pour les éléments à évaluer, y compris futurs. "
        "La nouvelle dispense ne réduit aucun montant approuvé et ne ferme ni expertise ni recours. "
        "V : le versement obligatoire, l'accord communal préalable aux réductions hors exceptions, "
        "le plafond lié à la perte réelle, la protection de 5 % ou du prélèvement sur recettes "
        "le plus élevé, l'étalement compensé, la fixation libre concordante, l'imputation "
        "en investissement et les majorations liées aux dotations, compensations, rattachements "
        "et anciens produits sont maintenus. Les seuils et plafonds de 30 %, 5 % et 20 %, les "
        "droits de restitution de compétences et les dispositions de Lyon gardent leur champ. "
        "Les droits issus de l'ancien 4° abrogé sont expressément protégés, sans rouvrir une "
        "faculté historique expirée. V bis, VII à IX : les références 2010/2011, taux historiques, "
        "sommes restant acquises, compensation de 1987, bases exonérées, abattements et facteur "
        "0,960 demeurent intégralement. Les références au pacte de relance pour la ville et à la "
        "zone franche de Corse sont conservées, sans déduction défavorable tirée du signalement "
        "SRU 92. Le produit TASCOM ne change ni l'assiette ni la franchise QPV de 1 500 euros de "
        "l'article 3 de la loi n° 72-657 ; cet avantage reste ouvert aux impositions futures "
        "éligibles. La substitution de l'EPCI n'écarte aucune exonération, franchise, réduction "
        "ou plafonnement autonome de CFE, y compris l'exonération intégrale des microentrepreneurs "
        "décidée dans la réforme et les baisses programmées du plafonnement en 2028-2030. Aucun "
        "avantage CVAE ancien n'est supprimé ici et aucune CVAE n'est recréée ; le corps ne "
        "contient déjà plus cette perception. Les quatre coupes portent sur des actes "
        "administratifs supplémentaires, avec maintien des évaluations nécessaires et des droits "
        "financiers, non sur un crédit ou une exonération fiscale. Le X protège actes valables, "
        "créances, protocoles et recours antérieurs ; il ne réserve pas les allègements aux "
        "situations anciennes. Aucune taxe générale n'est intégralement abolie dans cet article "
        "et aucun avantage n'est déclaré sans objet pour ce motif."
    ),
    substantive_impact=dict(
        version=1,
        classification='material_reduction',
        assessment=(
            "Par rapport à la source officielle entière, quatre ensembles d'actes obligatoires "
            "sont réellement retirés : circuit quinquennal, protocole de fusion, répétition de "
            "communication inchangée, nouvelles conclusions sur les éléments déjà évalués "
            "inchangés. Les trois premiers étaient déjà acquis dans le brouillon et ne sont "
            "pas présentés comme trois gains nouveaux de seconde passe ; le quatrième est "
            "supplémentaire. Les deux coordinations de renvois ne sont pas des réductions "
            "additionnelles. Aucune baisse de taux, d'assiette ou de dette fiscale n'est démontrée "
            "par cet article de répartition ; le gain de coût administratif reste non chiffré."
        ),
        scope_limitations=(
            "Seul l'article 1609 nonies C est proposé en entier. Les formalités financières "
            "autonomes du CGCT, le droit budgétaire, les dispositifs fiscaux et leurs formulaires "
            "ne sont pas abolis. La nouvelle dispense n'atteint ni charges nouvelles, modifiées, "
            "contestées ou non évaluées, ni nouveaux transferts ; le nombre de cas éligibles "
            "n'est pas connu. La source n'imposait pas expressément une nouvelle collecte ou un "
            "recalcul intégral à partir de zéro : le gain propre démontré est la dispense de "
            "nouvelles conclusions formelles, non une collecte supposée supprimée. "
            "Le protocole historique Lyon subsiste. La filiation SRU des deux "
            "pistes n'est pas entièrement documentée. Les bornes strictes de lissage demeurent "
            "une incohérence préexistante signalée. Ni solde budgétaire national ni réduction "
            "nette de complexité de l'ensemble des codes ne sont établis."
        ),
        new_burdens_review=(
            "Aucune charge nouvelle identifiée dans le texte proposé : pas de registre, de "
            "donnée supplémentaire, d'attestation, de déclaration, de protocole de remplacement, "
            "de délai minimal ni d'autorisation nouvelle. Les conditions de la dispense de "
            "réévaluation se vérifient dans l'évaluation approuvée et la situation existante, "
            "sans nouveau dépôt exigé ; elles bornent une suppression de procédure auparavant "
            "obligatoire dans tous les cas. Les rapports, décisions, majorités, notifications "
            "initiales ou modifiées et contrôles subsistants existaient dans la source. La "
            "transition n'impose ni dossier à refaire ni reprise des délais. Les coûts de mise "
            "en œuvre et le solde administratif global ne sont pas chiffrés."
        ),
        effects=effects,
    ),
)

Path('answer.json').write_text(json.dumps([answer], ensure_ascii=False, indent=2) + '\n')
print('answer.json écrit : 1 article,', len(proposed_xml), 'caractères de proposed_xml.')
