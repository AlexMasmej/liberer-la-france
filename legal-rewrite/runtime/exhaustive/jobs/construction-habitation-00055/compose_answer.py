import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', xml or ''))).strip()


def paragraphs(*items):
    return ''.join('<p>' + p + '</p>' for p in items)


def effect(kind, measure, description, before, after, unit, population, transition,
           replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(n, proposed, reason, review, impact_class, assessment, limitations, burdens,
        effects=None, benefit=None, removed=None, repeal_scope=None):
    s = by_number[n]
    a = {k: s[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    a.update(proposed_xml=proposed, reason=reason, review_notes=review,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal_scope:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal_scope)
    a['substantive_impact'] = dict(version=1, classification=impact_class,
                                 assessment=assessment, scope_limitations=limitations,
                                 new_burdens_review=burdens, effects=effects or [])
    if benefit:
        a['benefit_review'] = benefit
    answers[n] = a
    return a


n = 'L445-2'
s = by_number[n]
old_first = re.findall(r'<p>(.*?)</p>', s['source_xml'], re.S)[0]
new_first = "Les engagements pris par l'organisme en matière de gestion sociale mentionnés à l'article L. 445-1 précisent les actions d'accompagnement menées, en lien avec les associations d'insertion, en faveur des personnes mentionnées au II de l'article L. 301-1, notamment celles occupant les logements ayant bénéficié des financements prévus au II de l'article R. 331-1. Ils portent sur l'ensemble des logements pour lesquels l'organisme détient un droit réel. Les obligations de l'organisme relatives aux conditions d'occupation et de peuplement des logements, les engagements fixés par les accords mentionnés aux articles L. 441-1-1 et L. 441-1-2 et les objectifs de mixité sociale définis aux vingt-troisième à vingt-sixième alinéas de l'article L. 441-1 demeurent applicables dans leur champ propre, sans avoir à être récapitulés dans ces engagements."
p = s['source_xml'].replace(old_first, new_first, 1)
p += paragraphs("La dispense de récapitulation s'applique à compter de l'entrée en vigueur de la loi, y compris aux conventions et avenants en cours d'élaboration. Elle n'impose aucune modification des conventions déjà conclues et ne retire aucun engagement d'accompagnement, droit des locataires ou aide valablement acquis. Elle n'autorise à rétablir aucun quota communal, rattrapage, prélèvement ou effet de carence supprimé par la loi.")
add(n, p,
    "Réforme de fond ciblée : retrait de la récapitulation obligatoire dans la CUS de règles d'occupation, de peuplement et d'accords qui demeurent opposables par leurs fondements propres. Les actions d'accompagnement restent à préciser. Les neuf alinéas initiaux, dont les quatre rubriques numérotées de la politique facultative des loyers, sont conservés à leur place ; aucune simple substitution de vocabulaire n'est comptée comme une coupe.",
    "L445-1, L441-1-1 et L441-1-2 ont été lus en entier dans le corpus, source et proposition : la CUS et les accords prioritaires subsistent, même lorsque leurs avis et périodicités sont allégés. La dispense ne supprime ni les priorités DALO ni les objectifs d'attribution autonomes de L441-1 ; ces derniers ne sont pas les quotas communaux de production SRU. L445-3 et L445-3-1 sont traités dans ce lot. Le 1er janvier suivant la signature, l'application aux seuls baux nouveaux et la condition de plus de six ans des conventions L831-1 restent inchangés. Adapter les modèles de CUS pour retirer seulement la recopie des règles, sans rétablissement par un tableau ou une annexe. R445-5, lu intégralement avec son tableau, comporte des indicateurs autonomes : aucun n'est supprimé par cette dispense ni présenté comme déjà réécrit.",
    'material_reduction',
    "La source imposait une récapitulation contractuelle de règles déjà applicables. Cette recopie cesse d'être obligatoire ; les actions concrètes d'accompagnement et l'encadrement de la politique facultative des loyers demeurent entiers.",
    "La CUS, ses indicateurs autonomes et les obligations légales d'attribution restent. Le coût évité de la seule récapitulation n'est pas chiffré ; aucune réduction globale de complexité n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier, attestation, transmission ou avenant de remplacement n'est exigé. Les contrôles et engagements d'accompagnement existaient déjà.",
    [effect('obligation_removed', 'cus-fin-recapitulation-regles',
            "Suppression de la recopie obligatoire des règles d'occupation et de peuplement dans les engagements de gestion sociale.",
            "Les engagements de gestion sociale de la CUS doivent récapituler les obligations d'occupation et de peuplement, les accords et les objectifs mentionnés au premier alinéa.",
            "Ces règles demeurent applicables par leur fondement propre, sans récapitulation obligatoire dans la CUS ; les actions d'accompagnement restent décrites.",
            'legal_duty', 'Organismes HLM concluant ou modifiant une convention d’utilité sociale.',
            "Dispense immédiate, y compris pour les projets en cours ; conventions, aides et droits antérieurs conservés sans avenant imposé.",
            "Aucune formalité substitutive ; maintien des obligations matérielles et des indicateurs autonomes.",
            "Les engagements pris par l'organisme en matière de gestion sociale mentionnés à l'article L. 445-1 récapitulent les obligations de l'organisme relatives aux conditions d'occupation et de peuplement des logements qui tiennent compte des engagements fixés par les accords mentionnés aux articles L. 441-1-1 et L. 441-1-2, ainsi que des objectifs de mixité sociale définis aux vingt-troisième à vingt-sixième alinéas de l'article L. 441-1.",
            "Les obligations de l'organisme relatives aux conditions d'occupation et de peuplement des logements, les engagements fixés par les accords mentionnés aux articles L. 441-1-1 et L. 441-1-2 et les objectifs de mixité sociale définis aux vingt-troisième à vingt-sixième alinéas de l'article L. 441-1 demeurent applicables dans leur champ propre, sans avoir à être récapitulés dans ces engagements.")],
    removed=["La récapitulation obligatoire dans les engagements de gestion sociale des obligations d'occupation, de peuplement et des engagements et objectifs déjà applicables par leurs fondements propres est supprimée."])

n = 'L445-3'
s = by_number[n]
p = s['source_xml'].replace(", après avis du conseil d'administration de la caisse", '')
p += paragraphs("La suppression de l'avis particulier du conseil d'administration de la Caisse de garantie du logement locatif social prévu au II s'applique aux demandes d'avenant non encore décidées à la date d'entrée en vigueur de la loi et aux demandes ultérieures. Elle ne dispense ni de l'approbation du plan de redressement par la caisse ni de la conclusion de l'avenant et ne modifie aucun loyer ou bail de plein droit. Les avenants antérieurement conclus et les droits des locataires demeurent applicables.")
add(n, p,
    "Réforme de fond limitée au second avis du conseil d'administration de la CGLLS sur un avenant demandé par un organisme dont le plan de redressement est déjà approuvé par cette caisse. Cet avis supplémentaire est retiré sans déclaration substitutive. Les six subdivisions et tous les plafonds, indices, possibilités de modulation et autorisations protégeant les locataires sont maintenus.",
    "II : maintien de la demande de l'organisme, du plan de redressement approuvé, du déséquilibre financier grave et durable et de l'avenant ; seule la consultation particulière supplémentaire disparaît. III : l'accord administratif pour les opérations d'amélioration, sa durée et le plafond de 5 % en sus de l'IRL restent, car ils encadrent une dérogation aux plafonds de loyers. IV : exception des logements PLI ou équivalents et plafond PLS inchangés. V : révision au 1er janvier et IRL du deuxième trimestre précédent conservés. L353-9-3 et L442-1, sources et propositions lues entières, conservent leurs règles autonomes de révision ; les deux derniers alinéas de L442-1 restent effectivement les alinéas visés. La formule préexistante « convention d'utilité sociale charges en application du III » est signalée comme anomalie rédactionnelle et laissée visible, sans correction silencieuse de son sens. Adapter les circuits d'avenant et règlements de la caisse ; aucune réforme des loyers par simple avis supprimé.",
    'material_reduction',
    "Un avis particulier est effectivement supprimé après l'approbation du plan par la même caisse. La faculté dérogatoire de relèvement de la masse des loyers reste encadrée ; aucune hausse automatique ou nouveau tarif n'est créé.",
    "Le gain porte seulement sur cette consultation supplémentaire, pas sur l'approbation du plan ni sur l'accord administratif du III. L'effet sur les délais et les loyers effectivement pratiqués n'est pas chiffré.",
    "Aucune charge nouvelle n'est identifiée : la demande, le plan approuvé et l'avenant existaient déjà. Aucune déclaration ou pièce de remplacement de l'avis supprimé n'est instituée.",
    [effect('obligation_removed', 'cus-avenant-fin-second-avis-cglls',
            "Retrait de l'avis particulier du conseil d'administration sur l'avenant au plafond global après plan approuvé.",
            "L'organisme signataire d'un plan de redressement approuvé doit encore obtenir l'avis du conseil d'administration de la caisse pour l'avenant du II.",
            "L'avenant reste nécessaire dans les mêmes conditions de fond, mais le second avis de la caisse n'est plus requis.",
            'legal_duty', 'Organismes signataires d’un plan de redressement CGLLS sollicitant l’avenant du II.',
            "Demandes nouvelles et demandes non décidées à l'entrée en vigueur ; aucun bail ou avenant ancien n'est modifié de plein droit.",
            "Aucune formalité de remplacement ; approbation du plan, avenant et garanties de loyers subsistent.",
            "Par avenant, la convention d'utilité sociale peut être modifiée, si nécessaire, afin de prévoir un montant maximal plus élevé que celui résultant du présent II, à la demande d'un organisme signataire d'un plan de redressement approuvé par la Caisse de garantie du logement locatif social et en vue de résoudre des difficultés dues à un déséquilibre financier grave et durable, après avis du conseil d'administration de la caisse.",
            "Par avenant, la convention d'utilité sociale peut être modifiée, si nécessaire, afin de prévoir un montant maximal plus élevé que celui résultant du présent II, à la demande d'un organisme signataire d'un plan de redressement approuvé par la Caisse de garantie du logement locatif social et en vue de résoudre des difficultés dues à un déséquilibre financier grave et durable.")],
    removed=["L'avis particulier du conseil d'administration de la CGLLS préalable à l'avenant du II est supprimé lorsque le plan de redressement de l'organisme a déjà été approuvé par cette caisse."])

n = 'L445-3-1'
p = by_number[n]['source_xml'].replace("conventions conclues au titre de l'article L. 351-2", "conventions conclues au titre de l'article L. 831-1")
add(n, p,
    "Coordination nécessaire à droit constant : remplacement du renvoi historique à L351-2 par L831-1, support actuel des conventions ouvrant droit à l'APL. L'intégralité de la prorogation dérogatoire, de l'indexation et de sa sortie à l'intégration dans la nouvelle politique des loyers est maintenue, sans prétendre créer un allègement nouveau.",
    "Les deux notes source ont été lues, y compris la note de concordance de l'ordonnance 2019-770 et la mention documentaire relative à la fonction publique qui ne modifie pas le régime locatif. L353-1, L821-2, L831-1 et L831-2 ont été lus intégralement : L831-1 est le support conventionnel pertinent ; L353-1 règle les rapports locatifs, L821-2 la résidence principale et L831-2 certaines exclusions propres à l'accession. Il n'est créé ni nouvelle condition d'aide ni réouverture d'une période historiquement close. Les engagements fixés selon l'ancien L445-2 continuent à chaque renouvellement ; le 1er janvier, le deuxième trimestre précédent, L353-9-3 et les deux derniers alinéas de L442-1 sont conservés. Aucun nouveau renvoi n'est créé aux trois cibles travail : elles sont hors de ce champ.",
    'coordination_only',
    "La correction du support conventionnel évite un renvoi obsolète, sans changer les loyers, la durée de la prorogation ou les conditions de sortie de la dérogation. Aucun prélèvement ni dossier supplémentaire n'est supprimé ici.",
    "Le régime reste réservé aux immeubles déjà couverts par l'ancienne politique des loyers. Il protège leurs futurs renouvellements ; il n'étend pas cette catégorie historique à des immeubles qui n'en relevaient pas.",
    "Aucune charge nouvelle n'est identifiée : seul le numéro du support conventionnel actuel remplace son ancien numéro ; aucune attestation de concordance ni nouvelle convention n'est exigée.",
    [effect('coordination', 'apl-concordance-conventions-l831-1',
            "Actualisation du renvoi conventionnel issu de la recodification des aides personnelles au logement.",
            "Substitution des engagements dérogatoires aux engagements des conventions désignées par l'ancien L351-2.",
            "Même substitution aux engagements de même nature des conventions désignées par L831-1, sans nouveau conventionnement.",
            'other', 'Immeubles ayant conservé la politique de loyers antérieure à la loi du 27 janvier 2017.',
            "Continuité à chaque renouvellement ; cessation seulement lors de l'intégration à la nouvelle politique de L445-2.",
            "Aucun dépôt, agrément ou justificatif nouveau.",
            "en substitution des engagements de même nature des conventions conclues au titre de l'article L. 351-2.",
            "en substitution des engagements de même nature des conventions conclues au titre de l'article L. 831-1.")],
    benefit="L'avantage possible est la prorogation, à chaque renouvellement de CUS, des engagements de loyers fixés sous l'ancien L445-2, en substitution des engagements conventionnels de même nature. Elle demeure ouverte aux futurs renouvellements des immeubles éligibles, avec la même indexation et la même cessation lors de leur intégration à la nouvelle politique. La concordance L831-1 ne retire ni cette dérogation ni un droit à l'APL.")

add('L445-6', None,
    "Maintien intégral nécessaire de l'habilitation au décret en Conseil d'Etat : le chapitre conserve le conventionnement, la politique facultative des loyers et ses garanties. Cette disposition n'impose elle-même ni agrément, ni déclaration, ni délai minimal à l'organisme ou au locataire ; une reformulation ne réduirait aucune charge.",
    "L'habilitation ne peut légalement rétablir la récapitulation ni l'avis supplémentaire supprimés dans L445-2 et L445-3. Les modèles et circuits réglementaires doivent respecter ces lois nouvelles. Les obligations autonomes d'attribution, l'accompagnement, les plafonds et les avantages de L445-3-1 et L445-7 conservent leur support d'application. L'habilitation n'est ni un quota SRU ni un impôt.",
    'retained_necessary',
    "La disposition conserve uniquement une compétence réglementaire utile aux règles substantielles du chapitre ; aucun allègement matériel n'est attribué à son maintien.",
    "Les décrets et arrêtés pris sur ce fondement ne sont pas tous assignés dans ce lot. Leur examen individuel n'est pas déclaré achevé par le maintien de l'habilitation.",
    "Aucune charge nouvelle n'est identifiée : le texte source est intégralement maintenu, sans nouvelle procédure ni nouvelle délégation.")

add('L445-7', None,
    "Maintien intégral de la dérogation favorable aux organismes ayant conclu une CUS : les deux premiers alinéas de l'article 32 bis de la loi de 1948 demeurent inopposables dans ce champ. Supprimer cette disposition rétablirait une contrainte au lieu de la réduire.",
    "Le champ reste celui des organismes ayant conclu avec l'Etat une CUS, y compris ceux qui en concluront une à l'avenir. Le renvoi à L353-15 demeure la règle à laquelle la dérogation s'applique ; ni l'ensemble de la loi de 1948 ni les autres protections des occupants ne sont abrogés. Le texte extérieur exact de l'article 32 bis n'est pas fourni dans le corpus autorisé : aucune suppression supplémentaire de ses autres alinéas ni description de leur contenu n'est inventée. La portée d'inopposabilité expressément inscrite dans la source suffit à justifier sa conservation favorable.",
    'retained_necessary',
    "La source est déjà une dispense ciblée. Son maintien préserve cette dispense pour les conventions futures sans prétendre supprimer une seconde fois les obligations rendues inopposables.",
    "La dérogation ne bénéficie pas aux organismes sans CUS et ne neutralise que les deux alinéas expressément désignés ; les autres règles locatives restent distinctes.",
    "Aucune charge nouvelle n'est identifiée : maintien littéral de la dispense, sans demande d'agrément ou justification additionnelle pour en bénéficier.",
    benefit="L'avantage est l'inopposabilité des premier et deuxième alinéas de l'article 32 bis de la loi du 1er septembre 1948, par dérogation à L353-15. Cette dispense est maintenue intégralement pour les organismes qui ont conclu ou concluront une CUS ; elle n'est limitée ni aux conventions anciennes ni aux droits déjà consommés. Les autres protections locatives et les alinéas non visés restent hors de cette dispense.")

n = 'L451-5'
p = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi.",
    "À compter de cette date, les acquisitions et cessions immobilières des organismes d'habitations à loyer modéré et des sociétés d'économie mixte agréées en application de l'article L. 481-1 ne sont plus soumises à l'avis préalable de l'autorité compétente de l'Etat prévu par le présent article. Cette suppression s'applique également aux opérations en cours pour lesquelles l'avis n'a pas été rendu. Aucune déclaration, évaluation administrative préalable ou consultation de remplacement n'est exigée sur ce fondement, et aucun délai d'attente attaché à cet avis ne demeure opposable.",
    "Les règles autonomes d'acquisition, d'aliénation et de gestion des actifs sociaux, les autorisations de vente ayant un autre fondement, les droits des occupants, les engagements de financement et de garantie ainsi que les contrôles légalement applicables demeurent régis par leurs dispositions propres.",
    "Les acquisitions et cessions valablement conclues avant cette entrée en vigueur, leurs créances, leurs effets civils et les recours qui s'y rapportent ne sont pas remis en cause. Les exceptions et dispenses applicables aux opérations antérieures restent invocables pour apprécier la régularité de ces opérations.")
add(n, p,
    "Abrogation de fond du contrôle préalable général de valeur vénale des acquisitions et cessions HLM et SEM agréées. L'avis des finances publiques et son attente sont retirés sans déclaration équivalente. Les règles autonomes de vente sociale, de gouvernance, de contrôle des fonds et de protection des occupants justifient de conserver les protections sans cet avis général supplémentaire.",
    "R451-10 a été lu en entier : l'avis porte sur la valeur vénale et doit être formulé en un mois, à défaut de quoi l'opération peut se réaliser. Ce règlement doit être abrogé dans le nouveau champ, sans transférer son délai à une autre formalité. L451-6 est abrogé avec transition dans ce lot. Les références à L451-5 relevées dans L443-7, L422-3 et l'annexe à R422-6 doivent être retirées pour cet avis seulement ; leurs prix, autorisations et garanties autonomes ne disparaissent pas. La nouvelle règle législative écarte l'avis même si ces coordinations d'exécution restent à effectuer hors du lot. Aucun droit de préemption, contrôle ANCOLS, règle de commande publique ou autorisation de vente distincte n'est prétendu abrogé. Pas de délai effectif moyen ni d'économie nationale chiffrés.",
    'material_reduction',
    "L'obligation générale de solliciter un avis préalable sur la valeur vénale disparaît réellement, avec son attente réglementaire. Les opérations déjà dispensées par les exceptions de la source ne reçoivent pas un gain nouveau.",
    "Le retrait concerne seulement l'avis L451-5/R451-10 ; les autorisations de vente et les règles d'actifs sociaux autonomes restent. L'effet net sur les coûts publics et privés n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : aucun dépôt, certificat, estimation administrative ou déclaration de remplacement n'est créé ; les contrôles subsistants ont un fondement autonome antérieur.",
    [effect('obligation_removed', 'hlm-suppression-avis-valeur-venale',
            "Suppression de l'avis préalable général de l'Etat sur les acquisitions et cessions immobilières HLM/SEM agréées.",
            "Avis préalable obligatoire hors accession à la propriété, opérations entre organismes HLM/SEM agréées et autres dispenses légales ; R451-10 prévoit une fenêtre d'un mois, sans que toutes les opérations l'utilisent intégralement.",
            "Aucun avis ni attente sur ce fondement, sans consultation ou déclaration substitutive ; les autorisations distinctes restent.",
            'legal_duty', 'Organismes HLM et SEM agréées de L481-1 pour leurs opérations auparavant soumises à cet avis.',
            "Dès l'entrée en vigueur, opérations en cours incluses ; actes antérieurs, exceptions anciennes, créances et recours conservés.",
            "Aucun remplacement ; règles autonomes d'actifs sociaux et droits des occupants maintenus.",
            "L'avis de l'autorité compétente de l'Etat est requis par les organismes d'habitations à loyer modéré et les sociétés d'économie mixte de construction et de gestion de logements sociaux agréées en application de l'article L. 481-1 préalablement à leurs acquisitions ou cessions immobilières à l'exception de celles relatives aux opérations entreprises en vue de l'accession à la propriété et de celles intervenant entre deux organismes d'habitations à loyer modéré ou sociétés d'économie mixte de construction et de gestion de logements sociaux agréées en application du même article L. 481-1.",
            "À compter de cette date, les acquisitions et cessions immobilières des organismes d'habitations à loyer modéré et des sociétés d'économie mixte agréées en application de l'article L. 481-1 ne sont plus soumises à l'avis préalable de l'autorité compétente de l'Etat prévu par le présent article.")],
    repeal_scope="Suppression prospective de l'avis préalable général de l'Etat sur les acquisitions et cessions immobilières HLM et SEM agréées, de sa demande et du délai d'attente qui lui est exclusivement attaché.")

n = 'L451-6'
p = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi, en conséquence de la suppression de l'avis préalable prévu à l'article L. 451-5.",
    "Aucun avis fondé sur l'article L. 451-5 ne peut être rétabli pour les cessions ou acquisitions régies par le chapitre III du titre IV du livre IV. L'exception antérieure demeure applicable pour apprécier la régularité des opérations réalisées avant cette entrée en vigueur et pour les recours qui s'y rapportent. Les actes valablement conclus, les créances et les droits des parties et des tiers demeurent préservés.")
add(n, p,
    "Abrogation de coordination d'une exception devenue sans objet pour les opérations futures après l'abolition générale de l'avis L451-5. Cette coordination ne supprime aucun avantage tant que sa charge subsiste : l'avis entier disparaît, et la dispense ancienne reste invocable pour le stock ancien.",
    "Le chapitre III du titre IV du livre IV est le régime autonome d'aliénation et d'accession, non une procédure d'emploi. Ses autres règles ne sont pas supprimées. L451-5 est rédigé dans ce lot et R451-10 a été lu en entier ; le retrait de cette exception ne permet ni une requalification de l'avis ni un avis général de remplacement. Une seule mesure d'avis supprimé est comptée, sous la même clé que L451-5.",
    'coordination_only',
    "La dispense ne devient inutile pour l'avenir que parce que l'avis général est entièrement supprimé. L'abrogation de son article d'exception n'est pas un second allègement.",
    "Les formalités autonomes du chapitre III ne sont pas abolies. La régularité des opérations anciennes reste appréciée avec la dispense qui leur était applicable.",
    "Aucune charge nouvelle n'est identifiée : le texte interdit expressément de rétablir l'avis pour les opérations anciennement dispensées et ne crée aucun nouveau dépôt.",
    [effect('coordination', 'hlm-suppression-avis-valeur-venale',
            "Coordination de la dispense spéciale avec la disparition de l'avis général.",
            "Les opérations du chapitre III étaient spécialement exemptées de l'avis L451-5.",
            "L'avis disparaît pour l'ensemble du champ, avec conservation de la dispense pour le contrôle des opérations anciennes.",
            'legal_duty', 'Opérations du chapitre III du titre IV du livre IV, déjà dispensées.',
            "Même entrée en vigueur que L451-5 ; effets et recours anciens protégés.",
            "Aucune charge de remplacement ni nouvelle économie attribuée à la seule suppression du renvoi.",
            "L'article L. 451-5 n'est pas applicable aux cessions ni aux acquisitions régies par le chapitre III du titre IV du livre IV.",
            "Aucun avis fondé sur l'article L. 451-5 ne peut être rétabli pour les cessions ou acquisitions régies par le chapitre III du titre IV du livre IV.")],
    repeal_scope="Retrait pour l'avenir de l'article portant exception à l'avis L451-5 lui-même entièrement supprimé, avec maintien exprès de cette dispense pour le contrôle des opérations antérieures.")

n = 'L452-2-1'
p = paragraphs(
    "Le conseil d'administration mentionné à l'article L. 452-2 statue sur les concours financiers précisés aux troisième et cinquième alinéas de l'article L. 452-1. Ces décisions ne sont subordonnées ni à la saisine ni à la décision d'une commission de péréquation et de réorganisation distincte. Aucun rapport annuel distinct relatif à cette commission n'est exigé.",
    "La suppression de cette commission et l'attribution de ses compétences au conseil d'administration prennent effet à l'entrée en vigueur de la loi, y compris pour les demandes en cours. Le conseil reprend ces demandes en l'état, sans nouveau dépôt, nouvelle pièce exigée du seul fait de ce transfert ou recommencement des délais. Les règles de prévention des conflits d'intérêts, les contrôles budgétaires et comptables et les conditions de fond des concours demeurent applicables.",
    "Les décisions et conventions antérieurement prises ou conclues par la commission conservent leurs effets, ainsi que les droits à concours financiers, les engagements, les créances et les recours qui s'y rattachent. Les concours restent ouverts aux futures opérations éligibles selon les dispositions qui les régissent.")
add(n, p,
    "Réforme de fond : fusion du circuit de décision des concours de réorganisation et de formation dans le conseil d'administration existant, au lieu d'une commission légalement obligatoire distincte. La décision d'aide, les représentations déjà présentes au conseil, la prévention des conflits et les contrôles sont conservés ; aucun dossier ni rapport séparé de remplacement n'est créé.",
    "L452-1 fourni dans reference-targets a été lu intégralement dans ses deux versions : ses troisième et cinquième alinéas visent respectivement les concours de réorganisation/fusion/regroupement et la formation ou le soutien technique de renouvellement urbain. Ils ne visent ni contrats de travail à durée déterminée ni indemnités des salariés. L452-2, lu en entier, assure déjà la représentation des quatre familles d'acteurs au conseil ; la proportion de sièges n'est pas identique à R452-17, qui compte douze membres : le transfert institutionnel est assumé, sans prétendre conserver tous les mandats de la commission supprimée. R452-10 19°/20°, R452-14 1°/2°/12°, R452-17 et R452-12 ont été lus et sont à coordonner : retirer la saisine de commission, ses mandats et son rapport distinct, sans rétablir une approbation ministérielle déjà retirée dans la proposition L452-1 pour les conventions de son septième alinéa. Les comités des aides R452-16/16-1 et le fonds d'innovation R452-16-2, également lus, ont d'autres compétences ; leur suppression n'est pas décidée ici. Le traitement des dossiers est transféré au conseil, coût net public inconnu.",
    'material_reduction',
    "Une instance obligatoire distincte, son circuit de saisine et son rapport annuel propre sont retirés. Les mêmes concours sont décidés par le conseil existant, sans condition d'éligibilité supplémentaire ni réduction d'aide.",
    "Les comités autonomes et les décisions d'aide subsistent. La charge de traitement passe au conseil ; le coût net d'organisation et l'effet sur les délais réels ne sont pas établis.",
    "Aucun dossier, registre, délai ou justificatif nouveau n'est identifié. Le conseil assume les décisions auparavant attribuées à la commission ; ce transfert de travail existant ne crée pas une seconde décision ni un second rapport.",
    [effect('regime_merged', 'cglls-instance-concours-unifiee',
            "Réunion au conseil d'administration du circuit de décision des concours de la commission de péréquation et de réorganisation.",
            "Une commission distincte et obligatoirement constituée statue sur les concours des troisième et cinquième alinéas de L452-1 ; le conseil intervient notamment sur saisine en cas de partage.",
            "Le conseil statue directement, sans commission, saisine, nouveau dossier ou rapport annuel propre à celle-ci.",
            'regime', 'CGLLS et organismes demandant les concours de réorganisation, formation et soutien technique concernés.',
            "Transfert à l'entrée en vigueur, demandes en cours reprises en l'état ; décisions, conventions, aides et créances antérieures préservées, futures opérations éligibles couvertes.",
            "Décision conservée au conseil déjà existant ; aucun document de remplacement, coût public net non établi.",
            "Cette commission statue sur les concours financiers précisés aux troisième et cinquième alinéas de l'article L. 452-1.",
            "Ces décisions ne sont subordonnées ni à la saisine ni à la décision d'une commission de péréquation et de réorganisation distincte.")],
    removed=["La constitution obligatoire d'une commission de péréquation et de réorganisation distincte et son circuit propre de décision des concours des troisième et cinquième alinéas de L452-1 sont supprimés ; aucun rapport annuel de cette commission ne subsiste."])

n = 'L452-2-2'
p = paragraphs(
    "Aucun membre du conseil d'administration ne peut prendre part au vote dans une affaire où il a un intérêt personnel et direct.",
    "Aucun membre des instances placées auprès du conseil d'administration ne peut prendre part au vote dans une affaire où il a un intérêt personnel et direct.")
add(n, p,
    "Coordination nécessaire du retrait de la commission L452-2-1 : les deux mentions particulières des commissions de péréquation et de réorganisation sont retirées, tandis que l'interdiction de voter en cas d'intérêt personnel et direct demeure intégralement applicable au conseil et à toutes les instances subsistantes. Aucune dispense de déport n'est créée.",
    "La formulation source distingue encore une commission de péréquation et une commission de réorganisation, alors que L452-2-1 organise une commission réunie ; cette discordance de dénomination préexistante est signalée. Le nouveau deuxième alinéa conserve la catégorie générale de toutes les instances placées auprès du conseil, donc les comités autonomes maintenus. Le conseil qui reprend les concours est couvert par le premier alinéa, sans trou de protection. Les deux emplacements d'alinéas sont conservés. Aucun régime de conflit d'intérêts pénal, budgétaire ou de commande publique n'est neutralisé.",
    'coordination_only',
    "Seuls les noms d'instances supprimées disparaissent. Le déport reste obligatoire pour les mêmes intérêts personnels et directs dans tous les organes qui continuent à voter ; aucune obligation de probité n'est supprimée.",
    "La coordination ne simplifie pas indépendamment le régime des conflits d'intérêts et ne crée aucune réduction de prélèvement ou de formalité privée.",
    "Aucune charge nouvelle n'est identifiée : les mêmes règles d'abstention subsistent, sans déclaration d'intérêts ou registre supplémentaire institué par cet article.",
    [effect('coordination', 'cglls-instance-concours-unifiee',
            "Retrait de désignations d'instances supprimées sans diminuer la prévention des conflits d'intérêts.",
            "Interdiction de vote au conseil, dans ses instances et dans deux commissions nommément mentionnées.",
            "Même interdiction au conseil et dans toutes ses instances subsistantes, sans renvoi aux commissions supprimées.",
            'legal_duty', 'Membres des organes décisionnels de la CGLLS.',
            "Coordination à l'entrée en vigueur du transfert au conseil ; aucune décision antérieure n'est validée ni annulée de ce seul fait.",
            "Aucune déclaration ou procédure nouvelle ; garantie de déport conservée.",
            "Aucun membre des instances placées auprès du conseil d'administration, de la commission de péréquation ou de la commission de réorganisation ne peut prendre part au vote dans une affaire où il a un intérêt personnel et direct.",
            "Aucun membre des instances placées auprès du conseil d'administration ne peut prendre part au vote dans une affaire où il a un intérêt personnel et direct.")])

n = 'L452-4-1'
p = paragraphs(
    "Le présent article est abrogé pour les années de contribution commençant le 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi et pour les années suivantes.",
    "Pour ces années, aucune cotisation additionnelle à la Caisse de garantie du logement locatif social n'est due par les organismes d'habitations à loyer modéré, les organismes bénéficiant de l'agrément relatif à la maîtrise d'ouvrage prévu à l'article L. 365-2 et les sociétés d'économie mixte agréées en application de l'article L. 481-1. La suppression porte sur la part forfaitaire et sur la part variable, même lorsque l'activité, les logements ou l'exercice de référence sont antérieurs à la première année supprimée. Aucune déclaration, donnée, justification, acompte ou garantie exclusivement nécessaire à cette cotisation ne peut être exigé pour ces années. Aucune taxe, cotisation additionnelle ou extension d'assiette de remplacement n'est instituée par le présent article.",
    "Les années de contribution antérieures à la première année supprimée demeurent régies par les dispositions qui leur étaient applicables pour l'assujettissement, les périodes de référence, les parts forfaitaire et variable, leurs plafonds, exclusions d'assiette, déductions et réfaction. Leurs déclarations, liquidations, contrôles, recouvrements, dégrèvements, restitutions, prescriptions et recours demeurent possibles, même lorsque leur échéance ou leur réalisation est ultérieure. Les sanctions non définitives restent soumises à l'application de la loi répressive plus douce dans son champ.",
    "Les sommes versées au titre d'une année pour laquelle la cotisation additionnelle est supprimée sont restituables selon les règles de réclamation applicables, sans déclaration annuelle nouvelle de cette cotisation ni double restitution. Aucun remboursement général des cotisations légalement dues pour les années antérieures n'est créé.",
    "La suppression est distincte du régime de la cotisation générale de l'article L. 452-4 et des versements favorables maintenus au titre de sa modulation. Elle ne supprime ni les aides et concours de la caisse ni la cotisation de contrôle prévue à l'article L. 342-21. Aucun renvoi réglementaire ou législatif au présent article ne peut rétablir la cotisation additionnelle pour une année supprimée ou majorer un prélèvement distinct pour la remplacer.")
add(n, p,
    "Abrogation de fond de la cotisation additionnelle CGLLS, accessoire à la cotisation générale déjà supprimée dans sa proposition propre. Les deux parts disparaissent entièrement à compter de la même première année nouvelle, sans taux intermédiaire ni financement de remplacement inventé. Le stock ancien conserve toutes ses exclusions, déductions, réfactions, plafonds et recours ; les versements favorables de la modulation L452-4 ne sont pas supprimés.",
    "L452-4, ses notes et sa proposition ont été lus en entier dans reference-targets. Son troisième alinéa définit le champ des logements SEM et organismes L365-2 : la présente abolition couvre ce champ sans réutiliser les montants de référence comme une dette. Le premier janvier de l'avant-dernière année et le 31 décembre de cette même année restent des références des seules contributions anciennes ; ils ne justifient aucune contribution pour une année supprimée. R452-25-1 a été lu intégralement : exclusions de subventions, cessions, sinistres et calcul des annuités, y compris prêts antérieurs à 1997, restent applicables au stock ancien. L452-5/6/7 et R452-25 ont été lus : coordonner leurs renvois, R445-5 G1 et L452-3 c pour limiter les encaissements aux anciennes années. L452-5 est affecté d'une abrogation différée au 1er janvier 2027 dans le corpus ; son support successeur manque et doit être coordonné, sans que cette lacune puisse recréer la cotisation abolie. L342-21 est un prélèvement distinct, non supprimé ici. Le financement des garanties, aides, innovation et concours ANRU reste à documenter par les textes financiers pertinents : aucune réduction de ces droits ni recette compensatrice n'est décidée, et aucun rendement budgétaire n'est inventé.",
    'material_reduction',
    "Suppression réelle des deux parts de la cotisation additionnelle et de leurs formalités exclusivement dédiées pour toutes les années nouvelles. Il s'agit d'un prélèvement unique supprimé, distinct de l'abolition de la cotisation générale L452-4.",
    "Les années anciennes, la cotisation ANCOLS et les autres prélèvements autonomes subsistent. La perte de recettes de la caisse et le financement de ses missions ne sont pas chiffrés ; aucun solde public net n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau taux, paiement, formulaire, registre, garantie ou financement obligatoire ne remplace la cotisation. Les contrôles résiduels portent seulement sur les anciennes créances.",
    [effect('tax_removed', 'cglls-cotisation-additionnelle-suppression',
            "Abolition prospective de la cotisation additionnelle CGLLS, part forfaitaire et part variable.",
            "Part forfaitaire : somme annuelle au plus égale à 10 euros multipliée par les logements et unités de foyers ouvrant droit à redevance détenus en droit réel au 31 décembre de l'avant-dernière année. Part variable : taux arrêté au plus égal à 15 % sur l'autofinancement net de l'avant-dernière année ou exercice clos, après exclusions et déductions légales et réfaction d'au moins 5 % des produits locatifs assujettis. Les taux effectifs annuels ne sont pas fournis.",
            "Aucune de ces deux parts ni assiette taxable au titre de cette cotisation pour les années commençant le 1er janvier suivant l'entrée en vigueur ; pas de remplacement.",
            'euro', 'Organismes HLM, organismes agréés de maîtrise d’ouvrage L365-2 et SEM agréées L481-1 dans le champ locatif visé par la source.',
            "Années nouvelles supprimées même si la référence est ancienne ; anciennes années et tous leurs avantages maintenus ; indus des années supprimées restituables sans déclaration annuelle nouvelle.",
            "Aucun prélèvement ou formalité substitutif ; besoins de financement des missions CGLLS non chiffrés et aides maintenues.",
            "Les organismes d'habitations à loyer modéré, les organismes bénéficiant de l'agrément relatif à la maîtrise d'ouvrage prévu à l'article L. 365-2 et les sociétés d'économie mixte agréées en application de l'article L. 481-1, au titre des logements locatifs et des logements-foyers mentionnés au troisième alinéa de l'article L. 452-4, versent, chaque année, une cotisation additionnelle à la Caisse de garantie du logement locatif social.",
            "Pour ces années, aucune cotisation additionnelle à la Caisse de garantie du logement locatif social n'est due par les organismes d'habitations à loyer modéré, les organismes bénéficiant de l'agrément relatif à la maîtrise d'ouvrage prévu à l'article L. 365-2 et les sociétés d'économie mixte agréées en application de l'article L. 481-1.")],
    benefit="La source comporte le plafond de 10 euros de la part forfaitaire, les déductions d'emprunts et de soldes de mutualisation, les exclusions d'amortissements/provisions et de leurs reprises, de donations, dons et legs et de produits exceptionnels, la réfaction d'au moins 5 % et le plafond de 15 % de la part variable. Tous restent opposables pour les années anciennes. Pour les années nouvelles, la cotisation entière est abolie sans remplacement ni extension d'assiette ; aucun de ces allègements n'est perdu face à une charge maintenue. Les aides de la caisse et le versement favorable de L452-4 restent distincts et ouverts aux situations futures éligibles.",
    repeal_scope="Suppression pour toutes les années de contribution nouvelles de la cotisation additionnelle CGLLS dans ses deux parts forfaitaire et variable, ainsi que des déclarations, justifications et paiements exclusivement dédiés à ce prélèvement.")

add('L471-1', None,
    "Maintien intégral de la faculté locale des associations coopératives de production et de consommation de construire des logements dans le Haut-Rhin, le Bas-Rhin et la Moselle. Cette règle d'articulation avec le droit local ne crée elle-même ni avis préalable ni prélèvement ; son abrogation risquerait de fermer une capacité favorable de construction.",
    "La référence reste la loi du 1er juin 1924, article 7, 6., et la loi locale modifiée du 1er mai 1889. Ces textes extérieurs ne sont pas reproduits dans le corpus fourni : leurs conditions particulières ne sont ni inventées, ni réputées toutes vérifiées, ni supprimées par interprétation. La source maintient une faculté, pas un agrément administratif individuel à retirer. Le champ territorial demeure celui du chapitre ; les opérations futures recevables conservent la faculté.",
    'retained_necessary',
    "La disposition est déjà permissive et assure la continuité d'une capacité de construire. Aucun doublon déclaratif ou prélèvement propre à cet article n'a été identifié à supprimer.",
    "Les conditions contenues dans la loi locale extérieure ne sont pas réécrites ici ; aucun élargissement à d'autres personnes ou territoires n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : maintien intégral de la source, sans déclaration ni autorisation ajoutée à la faculté locale.")

add('L472-1', paragraphs(
    "Les modalités d'application des dispositions du présent livre à la Guadeloupe, à la Guyane, à la Martinique, à La Réunion, à Mayotte et à Saint-Martin et, notamment les modalités de financement et de contrôle des organismes d'habitations à loyer modéré font l'objet d'arrêtés conjoints des ministres intéressés. Lorsqu'elles relèvent d'un décret prévu par le présent livre, les mesures d'application nécessitées par la situation particulière aux départements d'outre-mer ainsi que par celle des Français d'outre-mer sont précisées par ce décret."),
    "Coordination nécessaire du renvoi ancien à L431-6, absent du corpus fourni : la compétence des arrêtés conjoints est conservée et la réserve des décrets reste expressément limitée aux décrets prévus par une disposition du livre. Aucun contenu supposé de L431-6 n'est reconstitué et aucun décret supplémentaire n'est exigé. Cette clarification n'est pas présentée comme une charge supprimée.",
    "Les six territoires sont conservés, sans ajout de Saint-Pierre-et-Miquelon que L472-2 régit séparément. Le renvoi L431-6 ne peut pas être confronté à une fiche du corpus ; son contenu historique et son éventuelle concordance ne sont pas affirmés. La rédaction le retire et exprime directement l'articulation des arrêtés avec les décrets effectivement prévus par le livre, sans remplacer ce numéro par L431-1 ou par une habilitation nouvelle et sans abolir une adaptation favorable. Les modalités de financement, les contrôles et les règles supérieures de compétence réglementaire demeurent. Aucun taux, justificatif ou calendrier nouveau n'est établi. Les suppressions législatives de cotisations priment les arrêtés d'exécution ; l'habilitation ne peut les rétablir. Les arrêtés extérieurs restent à examiner individuellement.",
    'coordination_only',
    "La proposition retire une désignation ancienne non documentée et conserve la compétence réglementaire effectivement prévue par le livre, sans modifier les droits au financement ni imposer un nouveau décret. Aucun allègement individuel démontré n'est compté.",
    "L'historique de L431-6 et les arrêtés extérieurs ne sont pas fournis ; la rédaction ne prétend ni reconstituer cette filiation ni achever la purge des contraintes de financement ultramarin.",
    "Aucune charge nouvelle n'est identifiée : la réserve ne concerne que les décrets déjà prévus par le livre et ne crée ni procédure, nouvelle habilitation, déclaration ou demande individuelle.",
    [effect('coordination', 'outremer-articulation-actes-application',
            "Articulation directe des arrêtés conjoints avec les décrets légalement prévus, sans renvoi à un numéro ancien non documenté.",
            "Les arrêtés conjoints sont prévus pour le livre et une exception renvoie aux décrets de L431-6, dont le contenu n'est pas fourni.",
            "Même compétence d'arrêtés ; réserve limitée aux décrets effectivement prévus par le livre, sans nouveau décret ni substitution de numéro supposée.",
            'other', 'Organismes HLM et autorités réglementaires dans les six territoires énumérés.',
            "Aucune date d'application historique ni droit de financement n'est changé ; les actes existants restent soumis à leurs fondements légaux.",
            "Aucune formalité privée ou obligation de décret supplémentaire ; aucune réduction chiffrée revendiquée.",
            "Toutefois, les décrets pris pour l'application de l'article L. 431-6 précisent les mesures d'application nécessitées par la situation particulière aux départements d'outre-mer ainsi que par celle des Français d'outre-mer.",
            "Lorsqu'elles relèvent d'un décret prévu par le présent livre, les mesures d'application nécessitées par la situation particulière aux départements d'outre-mer ainsi que par celle des Français d'outre-mer sont précisées par ce décret.")])

n = 'L472-1-1'
s = by_number[n]
p = s['source_xml'].replace(
    "de la caisse de prêts aux organismes d'habitations à loyer modéré, de la caisse de garantie du logement social et de la caisse des dépôts et consignations",
    "de la caisse de prêts aux organismes d'habitations à loyer modéré ou, dans la limite des droits, obligations et missions légalement transférés, des établissements qui lui sont substitués, de la Caisse de garantie du logement locatif social et de la caisse des dépôts et consignations")
add(n, p,
    "Coordination institutionnelle nécessaire, sans restriction des avantages : la CGLLS légalement substituée à la caisse de garantie du logement social est désignée par son nom actuel. La référence à la caisse de prêts est rendue opérante à l'égard de ses seuls successeurs légaux pour les missions et droits transférés, sans inventer leur identité ni rétablir un organisme disparu. Le champ des SEM agréées et l'égalité d'accès aux prêts HLM sont maintenus.",
    "L472-1, L472-2, L431-1 et les deux versions de L452-1 ont été lus. Le premier alinéa de L452-1 établit la substitution de la CGLLS aux droits et obligations de la caisse de garantie du logement social au 1er janvier 2001 : il fonde la correction, sans nouveau renvoi ajouté au corps. L431-1 conserve des avances de l'ancienne caisse de prêts dans les sûretés historiques ; son texte de succession complet n'est pas fourni. La clause fonctionnelle est donc limitée aux substitutions réellement prévues par la loi, sans désigner un successeur supposé ni lui attribuer des missions supplémentaires. L'accès reste soumis aux mêmes conditions que pour les sociétés HLM et protège aussi les droits sur prêts anciens ; aucun concours nouveau inconditionnel n'est créé. La CDC, la loi du 30 avril 1946 et les modalités de L472-1 première phrase restent dans leur position. L'agrément social n'est pas un second agrément démontré inutile, car il qualifie l'accès aux aides et au service d'intérêt général. L'exception territoriale de L472-2 est conservée.",
    'coordination_only',
    "Les dénominations de financement sont coordonnées aux substitutions légales sans fermer l'accès des SEM agréées aux prêts éligibles. Aucune nouvelle taxe, suppression d'agrément ou économie de formalité n'est revendiquée.",
    "L'identité complète des successeurs de l'ancienne caisse de prêts n'est pas documentée ici ; la clause ne présume aucune substitution ou mission non établie et ne garantit aucun prêt inconditionnel.",
    "Aucune charge nouvelle n'est identifiée : mêmes conditions d'accès que les sociétés HLM, sans attestation de succession institutionnelle imposée au demandeur, nouveau dossier ou nouvel agrément.",
    [effect('coordination', 'sem-outremer-concordance-financeurs',
            "Continuité de l'accès aux financements auprès des établissements légalement substitués aux anciennes caisses.",
            "La source de 1985 désigne la caisse de prêts HLM, la caisse de garantie du logement social et la CDC.",
            "La CGLLS est désignée selon sa substitution légale établie ; les éventuels successeurs légaux de la caisse de prêts n'interviennent que pour les droits et missions effectivement transférés ; la CDC reste visée.",
            'other', 'SEM agréées visées par la loi du 30 avril 1946 dans le champ territorial applicable.',
            "Continuité des anciens droits et des futures situations éligibles, sans nouvelle date, fermeture de régime ou extension des missions des prêteurs.",
            "Aucune démarche ou preuve supplémentaire demandée à la SEM ; il s'agit de la continuité du financeur légal.",
            "de la caisse de prêts aux organismes d'habitations à loyer modéré, de la caisse de garantie du logement social et de la caisse des dépôts et consignations en application du livre IV du présent code.",
            "de la caisse de prêts aux organismes d'habitations à loyer modéré ou, dans la limite des droits, obligations et missions légalement transférés, des établissements qui lui sont substitués, de la Caisse de garantie du logement locatif social et de la caisse des dépôts et consignations en application du livre IV du présent code.")])

n = 'L472-1-3'
s = by_number[n]
old = "Toutefois, l'application de ces dispositions à l'une des sociétés précitées ne peut intervenir que consécutivement à la passation d'une convention révisable annuellement entre cette société et l'Etat, définissant notamment des objectifs de loyers. "
new = "L'application de ces dispositions aux sociétés précitées n'est pas subordonnée à la passation ou au renouvellement d'une convention avec l'Etat. Les conventions valablement conclues, notamment leurs plafonds de loyers plus favorables aux locataires, demeurent applicables selon leurs stipulations ; la suppression de cette condition ne permet pas de les écarter unilatéralement."
assert old in s['source_xml']
p = s['source_xml'].replace(old, new)
p += paragraphs("La suppression de la condition de conventionnement s'applique à compter de l'entrée en vigueur de la loi aux logements et aux sociétés remplissant les conditions du présent article, y compris lorsque la procédure de conventionnement est en cours. Aucun nouveau dossier, avenant, déclaration ou justificatif de remplacement n'est exigé sur ce seul fondement. Elle n'ouvre aucun droit à une hausse de loyer de plein droit, ne réduit aucun droit aux aides et ne remet en cause ni les créances, ni les protections locatives, ni les recours relatifs aux périodes antérieures.")
add(n, p,
    "Réforme de fond : les règles de loyers HLM visées deviennent applicables aux SEM et logements ultramarins éligibles sans convention préalable avec l'Etat exigée par ce seul article. Le verrou administratif est retiré, sans déclaration équivalente. Les conditions de financement, le champ de propriété ou de gestion, les baux en cours et les plafonds conventionnels favorables restent protégés.",
    "Les cinq alinéas initiaux restent dans l'ordre ; seul le deuxième perd sa condition préalable, puis une transition est ajoutée. L442-1 a été lu dans ses deux versions : son troisième alinéa imposant un loyer de rétablissement financier demeure exclu par le premier alinéa du présent article ; la suppression proposée du plancher général de loyers s'applique sans rétablissement local. Le renvoi « L442-1, à l'exception du troisième alinéa, à L442-2 » est conservé dans son emplacement et sa portée de plage. Les financements de l'Etat, du Crédit foncier et de la Caisse centrale de coopération économique restent dans le troisième alinéa comme conditions historiques d'identification des logements ; aucune nouvelle offre de prêt de ces institutions n'est présumée. Les conventions existantes ne sont ni annulées ni privées de leurs plafonds plus favorables. Adapter les règlements et circuits de conventionnement fondés sur cet article, sans supprimer les conventions APL ou d'aide qui ont une base légale distincte. Aucun effet sur l'emploi, le CDI ou le préavis professionnel.",
    'material_reduction',
    "La convention bilatérale exigée avant application du régime de loyers est effectivement retirée. L'article conserve les conditions sociales des logements et les plafonds plus favorables déjà convenus, sans autoriser automatiquement une hausse.",
    "Les conventions nécessaires sur un autre fondement, notamment aux aides, restent. Les effets sur les loyers et sur le coût administratif net ne sont pas chiffrés ; le champ ne couvre que les logements financés et les six territoires énumérés.",
    "Aucune charge nouvelle n'est identifiée : suppression sans déclaration, avenant ou pièce substitutive. L'application des règles légales de loyers et le respect des contrats n'ajoutent pas une seconde procédure.",
    [effect('obligation_removed', 'sem-outremer-fin-convention-prealable-loyers',
            "Suppression de la convention préalable Etat-SEM conditionnant l'application des dispositions de loyers visées.",
            "Même après financement public, le régime des loyers ne peut s'appliquer à une SEM concernée qu'après passation d'une convention avec l'Etat, révisable annuellement.",
            "Application légale aux logements et sociétés éligibles sans convention ni renouvellement imposé sur ce fondement ; plafonds contractuels favorables antérieurs maintenus.",
            'legal_duty', 'SEM de la loi de 1946 et SEM locales des six territoires, pour les logements visés au premier et au troisième alinéa.',
            "Entrée en vigueur immédiate, procédures en cours comprises ; contrats, aides, plafonds favorables et créances anciennes préservés.",
            "Aucune déclaration ou convention équivalente ; conventions légalement nécessaires aux aides sur un autre fondement conservées.",
            "Toutefois, l'application de ces dispositions à l'une des sociétés précitées ne peut intervenir que consécutivement à la passation d'une convention révisable annuellement entre cette société et l'Etat, définissant notamment des objectifs de loyers.",
            "L'application de ces dispositions aux sociétés précitées n'est pas subordonnée à la passation ou au renouvellement d'une convention avec l'Etat.")],
    removed=["La passation préalable d'une convention Etat-SEM, révisable annuellement, cesse d'être une condition obligatoire d'application des règles légales de loyers visées par le présent article."])

add('L472-1-4', None,
    "Maintien intégral du préavis locatif réduit à un mois pour la mobilité dans le parc du même bailleur ultramarin. Ce délai est un avantage pour le locataire et facilite le déménagement ; il ne doit pas être remplacé par le préavis individuel de quinze jours du contrat de travail.",
    "L472-1-2, lu avec sa proposition, conserve les six territoires, la propriété de la SEM et le concours financier de l'Etat qui définissent les logements. Le départ et la nouvelle attribution doivent concerner deux logements de ce champ et le même bailleur. La loi 89-462, article 15 I, est un texte locatif extérieur ; son renvoi n'est ni un renvoi au code du travail ni une condition d'ancienneté salariée. La dispense reste ouverte aux prochaines attributions éligibles, sans limitation aux baux conclus avant la réforme. Les trois cibles travail requises font l'objet des analyses séparées, sans ajout de renvoi dans le corps.",
    'retained_necessary',
    "La source est déjà un allègement de délai favorable au départ du locataire. Le maintien n'est pas compté comme une nouvelle réduction ; aucune formalité de preuve supplémentaire ne figure dans cet article.",
    "L'avantage suppose une nouvelle attribution par le même bailleur dans le champ L472-1-2 ; il ne fixe pas le préavis d'un congé patronal ou d'un changement de bailleur hors de ce champ.",
    "Aucune charge nouvelle n'est identifiée : délai et conditions restent exactement ceux de la source, sans justificatif ou déclaration supplémentaire.",
    benefit="Le bénéfice est le préavis ramené à un mois, par dérogation au I de l'article 15 de la loi de 1989, lors d'une attribution d'un autre logement éligible du même bailleur dans les six territoires énumérés. Il demeure intégralement applicable aux futures mobilités recevables et aux baux existants, sans condition d'ancienneté professionnelle ajoutée. Le préavis de quinze jours du travail n'est pas appliqué aux baux.")

add('L472-1-6', None,
    "Maintien intégral de la dérogation permettant de financer une amélioration par un nouveau loyer après travaux aidés, sans congé. L'encadrement administratif de ce loyer et sa notification sont nécessaires pour protéger les locataires d'une hausse non bornée ou non portée à leur connaissance ; aucun second agrément ou justificatif redondant n'est identifié dans cet article.",
    "Le champ reste celui des six territoires et des améliorations aidées de R323-13 à R323-21. L442-1, source et proposition lues entières, conserve en dernier alinéa une dérogation générale à l'indexation, qui est précisément écartée ici au profit du régime spécial. Les limites administratives de loyer, l'achèvement des travaux et la notification des locataires ou bénéficiaires du maintien dans les lieux restent ; la suppression du plancher général de L442-1 n'est pas annulée. Le texte dispense déjà de donner congé : cette facilité reste utilisable pour de futurs travaux éligibles. Le renvoi réglementaire identifie un financement public et ne constitue pas une autorisation d'expulsion privée.",
    'retained_necessary',
    "Le régime combine déjà une dérogation utile à l'amélioration avec une protection sur le montant et l'information du locataire. Retirer ces limites ferait disparaître une garantie essentielle plutôt qu'un doublon démontré.",
    "Aucun nouveau droit à hausse au-delà des limites administratives n'est créé. Le financement réglementaire n'est pas chiffré et l'article n'autorise pas tous travaux privés à déroger aux loyers.",
    "Aucune charge nouvelle n'est identifiée : maintien littéral du contrôle du loyer et de la notification déjà requis, sans nouveau dossier ni délai préalable.")

add('L472-1-7', None,
    "Maintien intégral de l'ouverture du régime des sociétés civiles d'accession progressive aux SEM ultramarines et de la dérogation leur permettant de gérer et attribuer selon L472-1-3. La disposition étend des possibilités d'accession et ne prescrit aucun agrément ou dépôt propre à supprimer.",
    "L443-6-3, lu en entier source et proposition, conserve les prêts, les parts et la gestion tout en retirant l'acquisition simultanée obligatoire de parts à la location. Le renvoi à la section entière relaie cet allègement sans l'annuler. La dérogation du deuxième alinéa porte sur la gestion et l'attribution par la SEM associée-gérante, pas sur l'obligation d'acheter des parts. L472-1-3 est rédigé dans ce lot : son conventionnement préalable supprimé ne renaît pas par ce renvoi. Propriété de la SEM, concours financier de l'Etat, logements locatifs et six territoires demeurent. L'habilitation finale conserve le support de conditions d'application protectrices des associés et occupants, sans délai ou formulaire nouveau.",
    'retained_necessary',
    "La source ouvre un régime favorable d'accession et adapte sa gestion à l'outre-mer. Son maintien préserve cette ouverture pour les opérations futures ; les coupes opérées dans les articles cibles ne sont pas comptées une seconde fois.",
    "Les règles sociétaires, les financements et l'éligibilité des logements restent. Le maintien n'étend pas l'article aux logements seulement gérés ou dépourvus du concours financier requis.",
    "Aucune charge nouvelle n'est identifiée : aucun achat de parts, agrément, convention ou dossier supplémentaire n'est ajouté ; les renvois s'appliquent dans leur rédaction coordonnée.",
    benefit="Les deux avantages possibles sont l'accès des SEM concernées au régime de la section 1 bis d'accession progressive et la dérogation à L443-6-3 permettant la gestion et l'attribution selon L472-1-3. Ils sont conservés intégralement pour les futures opérations éligibles des six territoires et pour les droits déjà constitués. Le renvoi ne rétablit ni l'achat simultané de parts supprimé dans la cible ni la convention préalable supprimée dans L472-1-3.")

add('L472-1-8', None,
    "Maintien intégral du congé pour démolition avec relogement : les trois offres appropriées, leur exception lorsqu'un logement est spécialement conçu, et le préavis de six mois concilient la réalisation de l'opération avec la protection du logement. Ce préavis n'est pas une attente administrative sans fonction essentielle.",
    "Le texte distingue l'autorisation de démolir L443-15-1 et la démolition prévue par convention de rénovation urbaine. Ces supports immobiliers ne sont pas des autorisations de licenciement. Le renvoi à l'article 13 bis de la loi de 1948 protège la qualité du relogement ; ses critères ne sont pas remplacés par une formule inventée. L'exception du logement spécialement conçu est maintenue pour les futurs cas où le bailleur la démontre. Le délai de six mois court dans un régime de congé locatif ; aucun minimum d'ancienneté salariée, indemnité d'emploi ou délai de quinze jours n'y est introduit. Le terme du titre d'occupation n'autorise pas une expulsion privée sans les procédures distinctes applicables.",
    'retained_necessary',
    "Les conditions et le délai protègent le relogement effectif lors d'une démolition, tandis que l'exception du logement spécialement conçu allège déjà l'obligation d'offres. Aucun doublon de déclaration propre à l'article n'est établi.",
    "L'article ne règle ni toute autorisation de démolir ni toute procédure d'exécution. Les lois de 1948 et de 2003 sont extérieures au corpus ; aucune réécriture de leur contenu n'est présumée.",
    "Aucune charge nouvelle n'est identifiée : les mêmes trois offres ou la même exception, le même préavis et les mêmes conditions de relogement sont intégralement maintenus.")

add('L472-1-9', None,
    "Maintien intégral de l'habilitation favorable à prendre des participations et à construire, vendre ou gérer pour les sociétés civiles et entreprises visées. Les conditions de location nue, résidence principale, ressources et loyers plafonnés préservent l'affectation sociale des moyens HLM ; aucune autorisation administrative additionnelle ne figure dans l'article à retirer.",
    "Les subdivisions 1, 1°, 2° et 2 sont conservées avec les deux branches de location directe ou de sous-location à des personnes physiques. Le champ reste celui des sociétés anonymes HLM et coopératives HLM dans les six territoires cités. La faculté de prestation de services du 2 reste rattachée aux sociétés du 1 et aux mêmes plafonds. Il ne s'agit ni d'un quota communal SRU ni d'une obligation de construire un volume de logements. Les plafonds réglementaires ne sont pas des taux d'imposition et leur suppression retirerait la qualification sociale de l'activité sans coordination des aides ; aucun tel retrait n'est décidé.",
    'retained_necessary',
    "La source facilite déjà les prises de participation et prestations utiles à la construction sociale. Ses conditions définissent ce champ plutôt qu'un doublon de formalité démontré ; aucune simplification nouvelle n'est revendiquée.",
    "Le maintien n'ouvre pas les moyens HLM à toute activité immobilière sans plafond ni à tous organismes ou territoires. Aucun gain financier ou nombre de logements nouveaux n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : toutes les conditions sont celles de la source et aucun agrément, registre, déclaration ou plafond supplémentaire n'est créé.")

add('L472-1-10', None,
    "Maintien intégral de l'agrément réputé acquis à Mayotte et de l'accès aux exonérations et aides d'Etat afférentes au service d'intérêt général. Retirer cette disposition rétablirait une démarche et pourrait priver les SEM bénéficiaires d'avantages ; la référence européenne n'est pas effacée implicitement.",
    "La date de publication de la loi du 24 mars 2014 identifie la situation d'agrément réputé acquis ; elle ne limite pas aux seules aides déjà versées l'activité de construction et de gestion des sociétés bénéficiaires. Les futures opérations de ces sociétés restent éligibles aux aides et exonérations selon leurs conditions propres. Le texte ne crée pas une présomption générale pour toutes les SEM constituées après cette date ; les autres sociétés conservent l'accès de droit commun à l'agrément L481-1, lu en entier, et aux avantages correspondants. L472-1-1 et L411-2 restent les supports de champ. La conformité aux exigences SIEG de la décision 2012/21/UE demeure requise ; aucun agrément national supprimé n'est réputé abolir le droit de l'Union.",
    'retained_necessary',
    "Une dispense d'agrément et l'accès aux exonérations et aides sont préservés intégralement. Ce maintien d'avantages existants ne constitue pas une nouvelle suppression de prélèvement.",
    "Le texte demeure propre à Mayotte et à la situation historique d'agrément qu'il définit. Il ne garantit ni une aide inconditionnelle ni une conformité européenne de toutes les opérations.",
    "Aucune charge nouvelle n'est identifiée : l'agrément réputé acquis reste sans nouvelle demande, et aucune attestation, date limite d'opération ou condition d'aide additionnelle n'est instaurée.",
    benefit="Trois avantages sont possibles : l'agrément réputé acquis sans nouvelle décision individuelle, la faculté d'exercer la construction et la gestion sociales sous ce statut, et le bénéfice des exonérations fiscales et aides spécifiques de l'Etat. Tous sont maintenus, y compris pour les futures opérations éligibles des sociétés bénéficiaires. La date légale de 2014 n'est pas une extinction des aides futures ; les nouveaux entrants conservent leurs voies d'agrément et d'avantages de droit commun. Les conditions SIEG et le champ de L411-2 restent applicables.")

add('L472-2', None,
    "Maintien intégral de la non-application du livre IV à Saint-Pierre-et-Miquelon, avec son exception favorable L472-1-1. L'abrogation étendrait des contraintes territoriales et risquerait de retirer l'accès au financement maintenu par l'exception.",
    "Le renvoi L472-1-1 vise l'accès des SEM aux financements et reste conservé dans ce lot ; il ne rend pas l'ensemble du livre IV applicable à la collectivité. Aucun prélèvement CGLLS nouveau ne peut être déduit de cette exception après la suppression de L452-4-1. Le régime de la collectivité et les prêts de droit commun ne sont pas remplacés par une extension des dispositions métropolitaines. Ce maintien territorial n'est pas une nouvelle exonération ni une seconde abolition d'impôt.",
    'retained_necessary',
    "La source est une dispense territoriale accompagnée d'une exception d'accès au financement. La maintenir évite une extension de contraintes et conserve l'avantage ; aucune réduction nouvelle n'est comptée.",
    "Le texte ne tranche pas l'ensemble des compétences et régimes de financement de Saint-Pierre-et-Miquelon ; les textes statutaires extérieurs ne sont pas réécrits.",
    "Aucune charge nouvelle n'est identifiée : absence d'extension du livre et conservation littérale de son unique exception, sans déclaration ni agrément supplémentaire.")

add('L472-3', None,
    "Maintien intégral des adaptations mahoraises de publicité foncière, des exclusions et du calendrier historique d'application du livre IV. Les dispenses et la garantie du dépôt des demandes restent utiles ; les échéances anciennes ne doivent pas être remplacées par des dates nouvelles ou par les délais professionnels de la réforme du travail.",
    "Les onze rubriques ont été examinées : 2°, 3° et 9° sont déjà abrogés et ne sont pas des suppressions nouvelles ; 1°/10° maintiennent le livre foncier ; 4° et 5° sont des non-applications ; 6° adapte l'attestation et conserve le butoir du 31 décembre 2015 ; 7°/8° conservent le 1er janvier 2013 ; 11° conserve le 1er janvier 2018. L441-2-1 a été lu dans ses deux versions : la dernière phrase du sixième alinéa reste celle de l'attestation et du délai de recours, sans déplacement dans la proposition ; l'adaptation de Mayotte continue donc à viser la phrase pertinente. La cible L441-2-3-3, lue dans reference-targets, concerne une indemnité de relogement et sa sûreté, exclue ici par le 5°, sans devenir une indemnité de licenciement. Aucun quota SRU n'est rétabli par le renvoi général du 11° au chapitre V, qui s'applique avec ses réformes de fond. Les anciens contrats de travail et leurs droits sont hors de cet article.",
    'retained_necessary',
    "Les adaptations territoriales et les dispenses sont conservées sans nouvelle date ni procédure. Les rubriques déjà abrogées ne sont pas comptées comme des charges retirées par ce projet.",
    "Le régime DALO demeure exclu à Mayotte dans le champ exprès du 5° ; aucune extension de ces recours ni réforme de l'ensemble des règles foncières locales n'est décidée ici.",
    "Aucune charge nouvelle n'est identifiée : la source entière et ses calendriers restent ; aucune attestation professionnelle, nouvelle inscription ou nouvelle enquête n'est ajoutée.")

n = 'L482-3'
s = by_number[n]
clarification = "Pour l'application du présent I aux sociétés d'économie mixte, l'enquête mentionnée à l'article L. 441-9 demeure applicable pour apprécier les ressources des locataires, dans les conditions de demande, de délai de réponse, de dispense et de réemploi des informations prévues au premier alinéa de cet article."
p = s['source_xml'].replace('</p>', clarification + '</p>', 1)
p += paragraphs("Pour l'application du présent article aux périodes d'occupation à compter de l'entrée en vigueur de la loi, l'enquête a pour seule finalité propre d'apprécier les ressources dans les conditions du I. Elle ne rétablit ni supplément de loyer de solidarité supprimé ni indemnité pour frais de dossier à ce titre. Les informations exactes et à jour déjà légalement disponibles sont réemployées dans les conditions prévues à l'article L. 441-9 ; aucune seconde enquête ni accès nouveau à des données n'est institué. Cette coordination ne modifie ni les périodes de constatation des ressources, ni les délais, ni les baux ou protections prévus aux I à III. Les droits des locataires, les restitutions et les recours relatifs aux périodes antérieures sont conservés.")
add(n, p,
    "Coordination nécessaire après le retrait du supplément de loyer et le recentrage proposé de L441-9 : l'enquête de ressources reste explicitement applicable aux SEM pour le seul contrôle matériel du seuil de L482-3, avec les délais, dispenses et règles de réemploi de la cible. Les six alinéas initiaux conservent leurs positions et toutes les protections et conditions de maintien ; aucune nouvelle enquête ni suppression du préavis de six mois n'est créée.",
    "L441-9, lu en entier dans sa version officielle et sa proposition, réserve désormais ses demandes aux finalités autonomes L442-2-1 et L442-3-3, sans nommer L482-3 : le présent article assure expressément son application dans le champ SEM, au lieu de maintenir un renvoi de finalité devenu incomplet. Une mention correspondante de L482-3 devra aussi être intégrée à L441-9 à l'assemblage ; cette cible n'est pas modifiée ici. Restent deux années consécutives strictement au-dessus de 150 % des plafonds PLS, le départ au 1er janvier suivant la seconde enquête, dix-huit mois, l'information sans délai et la notification six mois avant échéance. Le retour sous les plafonds PLS eux-mêmes, non sous 150 %, ouvre le bail de trois ans renouvelable du II. Le III conserve l'âge de 65 ans dans l'année suivant les résultats, les deux cas de handicap, les QPV et la sauvegarde ZUS pour les résidents au plus tard le 31 décembre 2014. La note source fixe l'application historique au 1er janvier 2018 et n'est pas la date de la réforme future. L482-4, lu, permet une extension hors zones par délibération : ce pouvoir distinct n'est ni supprimé ni exercé par cette coordination. L482-3-1 est abrogé séparément : l'absence de réponse ne remplace pas la preuve de ressources supérieures. Les notifications locatives et les recours gardent leur régime, sans assimilation à une rupture du contrat de travail.",
    'coordination_only',
    "La proposition maintient le contrôle de ressources SEM déjà prévu dans la source malgré le changement de finalité de L441-9. Elle ne compte ni l'enquête réemployée ni l'abolition du supplément dans un autre article comme un nouvel allègement.",
    "La sortie du logement pour dépassement matériel de ressources et le pouvoir autonome d'extension de L482-4 subsistent. La présente coordination ne démontre aucune baisse de loyer ou de coût de conformité supplémentaire.",
    "Aucune charge nouvelle n'est identifiée par rapport à la source officielle : l'enquête, l'information et les notifications existaient déjà. La reprise de l'enquête pour ce même contrôle ne crée ni deuxième collecte ni accès nouveau aux données.",
    [effect('coordination', 'supplement-loyer-solidarite-suppression',
            "Conservation du fondement autonome de l'enquête SEM pour le contrôle de ressources après suppression du supplément de loyer.",
            "Le seuil de sortie est établi au vu de l'enquête L441-9, dont la source organise principalement le calcul du supplément de loyer.",
            "Même enquête dans le champ SEM expressément maintenue pour le seuil de sortie, avec les mêmes dispenses et sans reconstitution d'un supplément ou d'une seconde collecte.",
            'legal_duty', 'Locataires des logements sociaux SEM dans le champ du I et bailleurs concernés.',
            "Coordination des périodes nouvelles sans modifier les deux années de ressources, les délais, le retour au bail ni les exemptions ; anciens droits et recours conservés.",
            "Enquête existante maintenue à finalité autonome, aucune obligation nouvelle ni économie supplémentaire comptée.",
            "les baux des locataires dont les ressources, au vu des résultats de l'enquête mentionnée à l'article L. 441-9, sont, deux années consécutives, supérieures à 150 % des plafonds de ressources pour l'attribution des logements financés par des prêts locatifs sociaux sont prorogés afin de leur permettre de disposer du logement qu'ils occupent pour une durée de dix-huit mois.",
            "Pour l'application du présent article aux périodes d'occupation à compter de l'entrée en vigueur de la loi, l'enquête a pour seule finalité propre d'apprécier les ressources dans les conditions du I.")])

n = 'L482-3-1'
p = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi.",
    "À compter de cette date, le défaut de réponse à l'enquête mentionnée à l'article L. 441-9, même pendant deux années consécutives, ne peut plus, sur le fondement du présent article, entraîner une prorogation limitée du bail, la perte du titre d'occupation ou une obligation de libérer les lieux. Cette suppression s'applique aux défauts de réponse antérieurs comme postérieurs à cette date et aux procédures en cours qui n'ont pas donné lieu à une décision de justice passée en force de chose jugée. Les notifications déjà adressées cessent de produire pour l'avenir ces effets sur ce seul fondement. Les baux qui ne sont pas définitivement résiliés se poursuivent selon les règles qui leur sont propres.",
    "Les décisions de justice passées en force de chose jugée et les évictions déjà exécutées ne sont pas remises en cause par la présente abrogation. Les créances légalement nées avant cette entrée en vigueur, les restitutions, prescriptions et voies de recours restent régies par leurs règles propres ; aucun remboursement général ni remise en cause de l'autorité de la chose jugée n'est institué.",
    "Les garanties de maintien ou de rétablissement du bail et les exemptions prévues aux II et III dans leur rédaction antérieure demeurent invocables pour les situations et recours anciens. La suppression générale du motif de déchéance s'applique aussi aux situations futures de personnes âgées, handicapées ou résidant dans les quartiers auparavant exemptés, sans justificatif destiné à obtenir une exemption d'une déchéance désormais supprimée.",
    "Les obligations d'information nécessaires à une finalité légalement maintenue, le contrôle des ressources effectivement établies dans le champ de l'article L. 482-3, les droits des locataires et les autres obligations du bail demeurent applicables selon leurs dispositions propres. Aucun défaut de réponse ne peut être assimilé, à lui seul, à la preuve d'un dépassement des plafonds de ressources. Aucun congé, sanction locative ou formalité équivalente de remplacement n'est créé par le présent article.")
add(n, p,
    "Abrogation de fond de la perte du logement sanctionnant deux non-réponses à une enquête administrative. La gravité de cette déchéance n'est pas justifiée par la seule absence de pièces, alors que L482-3 conserve le contrôle des ressources réellement établies et que les obligations locatives autonomes restent applicables. La suppression vaut également pour les procédures non définitivement jugées, sans retirer les garanties anciennes ni inventer de sanction de remplacement.",
    "Les I à III et les deux notes source ont été lus en entier. La prorogation limitée de dix-huit mois, le congé notifié six mois avant terme, la déchéance et la condition de nouveau bail après production de pièces perdent leur objet pour le motif supprimé. Les exemptions âge 65 ans, handicap personnel ou à charge et QPV ainsi que le rétablissement du II restent invocables dans les litiges anciens ; pour l'avenir, la suppression générale protège aussi ces catégories. La protection ZUS de la note avait une échéance au 31 décembre 2020 : elle n'est pas artificiellement transformée en échéance nouvelle ni en droit limité de la réforme. L441-9, dans reference-targets, conserve des demandes à finalités autonomes et ses délais, mais la présente abolition n'y rétablit pas la finalité SLS ; L482-3 est coordonné dans ce lot pour les ressources réelles. Les obligations d'enquête ou sanctions ayant un autre fondement ne sont pas déclarées abolies. Coordonner les formulaires et notifications de déchéance pour cesser d'appliquer ce seul motif aux procédures non définitivement jugées. Le maintien des jugements passés en force de chose jugée est une limite expresse, pas une promesse d'effacement de toutes les évictions anciennes.",
    'material_reduction',
    "Le défaut de réponse cesse de provoquer à lui seul une échéance forcée du bail et une perte de titre. Les démarches exclusivement nécessaires pour éviter cette déchéance deviennent inutiles, sans supprimer le contrôle des ressources effectives.",
    "Les jugements passés en force de chose jugée et évictions exécutées restent protégés. Les enquêtes utiles à d'autres finalités, les loyers dus et les sorties fondées sur les ressources réellement établies subsistent ; aucun coût national n'est chiffré.",
    "Aucun formulaire, registre, délai ou justificatif nouveau n'est créé. Le bailleur perd ce motif particulier de déchéance et le bail existant se poursuit dans son régime propre ; aucune procédure punitive de remplacement n'est identifiée.",
    [effect('obligation_removed', 'sem-fin-decheance-pour-non-reponse-enquete',
            "Suppression de la libération forcée des lieux et de la perte du titre fondées sur deux non-réponses à l'enquête.",
            "Dans le champ géographique du I, deux non-réponses annuelles entraînent une prorogation limitée de dix-huit mois puis une déchéance, après notification six mois avant le terme, sous réserves et exemptions des II/III.",
            "Aucune échéance forcée ou perte de titre sur ce seul motif, même pour les manquements anciens non définitivement jugés ; aucune déchéance substitutive.",
            'legal_duty', 'Locataires du parc social SEM concernés par le I, avec maintien des garanties et catégories auparavant exemptées.',
            "Entrée en vigueur immédiate, procédures non définitivement jugées incluses ; jugements passés en force de chose jugée, évictions exécutées et droits anciens protégés.",
            "Contrôle des ressources réelles L482-3 et obligations du bail maintenus ; aucun dispositif de sanction ou justificatif de remplacement.",
            "A l'issue de cette échéance, les locataires sont déchus de tout titre d'occupation des locaux loués.",
            "À compter de cette date, le défaut de réponse à l'enquête mentionnée à l'article L. 441-9, même pendant deux années consécutives, ne peut plus, sur le fondement du présent article, entraîner une prorogation limitée du bail, la perte du titre d'occupation ou une obligation de libérer les lieux.")],
    benefit="Le II protège le rétablissement par un bail de trois ans renouvelable lorsque les ressources et pièces sont régularisées ; le III protège les personnes atteignant 65 ans dans l'année considérée, les personnes handicapées ou ayant une personne handicapée à charge et les résidents QPV. Ces moyens restent invocables dans les affaires anciennes, avec la protection ZUS de la note dans sa période propre. Pour l'avenir et les procédures non définitivement jugées, la déchéance fondée sur la non-réponse est entièrement supprimée pour tous, sans sanction équivalente ni preuve supplémentaire imposée aux catégories protégées ; aucun avantage n'est retiré face à une charge subsistante.",
    repeal_scope="Suppression de la prorogation limitée du bail, du congé et de la déchéance du titre d'occupation exclusivement fondés sur deux défauts consécutifs de réponse à l'enquête L441-9, avec extinction des effets futurs non définitivement jugés.")

# Only the targets expressly required for each source are attached to that source.
work_ref_assessments = {
    'L452-2-1': [
        "L1234-1 règle le préavis de licenciement, porté dans sa proposition à quinze jours pour les nouveaux contrats, avec maintien de l'ancien régime selon l'ancienneté. L452-2-1 ne contient aucun renvoi à ce préavis : il désigne l'organe qui accorde des aides à des organismes, non les conditions de rupture de leurs salariés. Les protections et notifications d'emploi ne sont donc pas transférées à la commission ou au conseil.",
        "L1221-2 proposé impose le contrat privé nouveau à durée indéterminée et conserve le régime des anciens contrats. Les concours des troisième et cinquième alinéas de L452-1 ont pour objet une réorganisation ou une formation, dont la durée ne fixe pas la durée d'un emploi. La fusion de l'instance de décision L452-2-1 n'autorise aucun nouveau CDD ni renouvellement de CDD et ne régit pas les agents publics.",
        "L1234-9 proposé vise l'indemnité patronale ordinaire : seuil d'un an au terme effectif préavis inclus, puis 0,20 mois pour toute l'ancienneté et plafond de six mois, sans indemnité ordinaire de démission et avec transition ancienne. Les concours financiers attribués selon L452-2-1 ne sont pas ces indemnités ; ni leur montant ni les créances des salariés ne sont modifiés par le transfert de décision au conseil."
    ],
    'L452-4-1': [
        "L1234-1 distingue le préavis professionnel futur de quinze jours et les préavis des anciens contrats fondés sur l'ancienneté. L452-4-1 règle une contribution annuelle de personnes morales, avec année d'activité et année de référence, et non une notification de licenciement. Son abolition ne réduit donc aucune procédure collective ou autorisation de salarié protégé et ne modifie aucun préavis.",
        "Le contrat unique de L1221-2 concerne les nouveaux emplois privés ; l'avant-dernière année et les logements décomptés dans L452-4-1 sont des références fiscales, pas des termes de contrat de travail. La suppression des deux parts n'instaure ni CDD spécial au logement social ni terme automatique pour les salariés. Les anciens contrats et les futurs emplois éligibles à des aides restent à leur régime propre.",
        "Le seuil d'un an préavis inclus et le calcul de 0,20 mois sur toute l'ancienneté de L1234-9 proposé ne concernent pas l'autofinancement net, les remboursements d'emprunts et la réfaction de L452-4-1. Supprimer la cotisation n'efface aucune indemnité acquise, salaire ou réparation d'illégalité ; les fractions de carrière et anciens contrats n'entrent pas dans sa transition par année de contribution."
    ],
    'L472-1-4': [
        "L1234-1 proposé concerne un préavis patronal de quinze jours pour les nouveaux contrats de travail, avec ancienneté et préavis antérieurs réservés aux anciens contrats. L472-1-4 vise le congé donné par un locataire et son préavis favorable d'un mois lors d'une mobilité chez le même bailleur : il ne renvoie pas au licenciement et le mois n'est pas remplacé par quinze jours.",
        "L1221-2, dont la proposition interdit le terme automatique des nouveaux emplois privés, est sans effet sur la durée du bail ou sur la nouvelle attribution de logement visée par L472-1-4. L'avantage d'un mois reste accessible à toute future mobilité remplissant les conditions immobilières, que l'occupant ait un contrat unique, un ancien contrat ou aucun emploi ; aucun justificatif de CDI n'est ajouté.",
        "L1234-9 proposé mesure le seuil d'un an à la fin effective de l'emploi et calcule une indemnité patronale, distincte du préavis locatif. L472-1-4 ne subordonne le mois favorable ni à cette ancienneté ni à une indemnité de rupture. Le bailleur n'est pas réputé employeur ; les droits des anciens contrats et les indemnités spéciales n'ont aucune incidence sur la dispense locative maintenue."
    ],
    'L472-1-8': [
        "Le préavis de six mois de L472-1-8 accompagne un congé locatif pour démolition après trois offres de relogement ou logement spécialement conçu. L1234-1 proposé fixe quinze jours pour une rupture patronale de nouveau contrat de travail et conserve les anciens préavis selon l'ancienneté : ce régime ne vise pas le bail, ne raccourcit pas ses six mois et ne supprime pas l'autorisation de démolir distincte.",
        "L1221-2 proposé interdit de nouveaux emplois à terme, y compris pour une mission ou un chantier. La démolition d'un immeuble et la convention de rénovation visées par L472-1-8 ne sont pas une durée de contrat de travail ; leur achèvement n'est pas introduit comme fin automatique d'emploi. Les anciens contrats et les éventuels salariés ou agents publics concernés par l'opération restent soumis à leurs règles propres.",
        "L1234-9 proposé traite la rupture patronale et l'ancienneté totale après seuil d'un an, non l'indemnisation ou les conditions de relogement. Le congé L472-1-8 ne crée ni indemnité salariale plafonnée à six mois ni seuil professionnel pour obtenir trois offres appropriées. Les six mois locatifs et les droits de relogement sont intégralement maintenus, distincts des salaires, congés et indemnités spéciales d'emploi."
    ],
    'L472-3': [
        "L1234-1 proposé règle un préavis de licenciement, nouveau ou ancien selon la date du contrat et l'ancienneté. Les dates de 2013, 2015 et 2018 dans L472-3 sont des calendriers d'application territoriale du logement, et l'attestation du 6° certifie une demande de logement. Aucune notification d'emploi de quinze jours ne remplace ces dates ou la garantie de dépôt, ni les procédures propres des agents publics.",
        "L1221-2 proposé s'applique aux emplois privés nouveaux et préserve les anciens contrats. Aucun des onze points de L472-3 ne fixe un terme d'emploi : inscriptions au livre foncier, attestation, non-applications et dates historiques demeurent des adaptations immobilières mahoraises. La durée d'une demande ou d'une convention n'y ouvre aucun nouveau CDD, ni ne ferme un avantage à un futur demandeur en contrat unique.",
        "L1234-9 proposé ouvre l'indemnité patronale après un an à la fin effective préavis inclus et conserve les composantes des anciens contrats. L472-3 ne vise aucun de ses alinéas : les exclusions DALO et la publicité foncière ne sont pas des indemnités de licenciement. Aucun calcul d'ancienneté ou plafond de six mois de salaire n'est ajouté au régime mahorais ni à l'attestation du 6°."
    ],
    'L482-3': [
        "L1234-1 proposé fixe le préavis individuel patronal de quinze jours des nouveaux contrats et conserve l'ancien régime selon l'ancienneté. Les six mois de notification et dix-huit mois de prorogation de L482-3 concernent un bail social SEM, non une rupture d'emploi. La proposition locative conserve ces durées et les supports de notification ; aucune procédure collective ou autorisation de licenciement n'est implicitement supprimée.",
        "L1221-2 proposé distingue contrat unique privé nouveau et anciens contrats. Le bail de trois ans renouvelable du II de L482-3 est un bail d'habitation ouvert au retour sous les plafonds PLS, pas un CDD de travail. Il demeure applicable aux situations futures éligibles sans exigence de CDI, et la prorogation du I ne devient pas une durée d'emploi ni une fin automatique de contrat professionnel.",
        "L1234-9 proposé mesure un an d'ancienneté d'emploi à la fin effective, préavis inclus, puis 0,20 mois sur l'ancienneté totale sous plafond de six mois. Les deux années de ressources et le seuil de 150 % de L482-3 ne sont pas cette ancienneté : aucun salaire ou indemnité professionnelle n'est recalculé, et les exemptions âge, handicap et quartier restent sans condition de rupture d'emploi ou de notification patronale."
    ],
    'L482-3-1': [
        "Le préavis locatif de six mois de L482-3-1 est une étape d'une déchéance pour non-réponse, entièrement supprimée par la proposition, et n'est pas remplacé par quinze jours. L1234-1 proposé vise seulement le licenciement de contrats de travail nouveaux avec transition des anciens ; il n'autorise ni cette déchéance ni une procédure d'expulsion raccourcie, et ses conditions d'ancienneté ne gouvernent pas le bail.",
        "L1221-2 proposé interdit les nouveaux CDD d'emploi et préserve les anciens contrats. Les dix-huit mois et le bail de trois ans de la source L482-3-1 étaient des durées locatives, non des emplois à terme. Leur retrait avec la déchéance ne crée pas un CDD spécial ; les personnes en contrat unique comme les autres locataires bénéficient à l'avenir de la disparition du motif administratif, sous la réserve des jugements définitifs.",
        "L1234-9 proposé porte sur l'indemnité patronale ordinaire après seuil d'un an, total d'ancienneté préavis inclus et plafond de six mois. L482-3-1 ne fixe pas cette indemnité : la perte du titre pour deux non-réponses est supprimée, sans effacer salaires, indemnités spéciales ou droits d'anciens contrats. Aucun justificatif d'ancienneté ni paiement d'indemnité d'emploi ne remplace les pièces de ressources dans la transition du bail."
    ]
}

specific_checks = {
    ('L452-2-1', 'L452-1'): "Le troisième alinéa officiel et proposé de L452-1 concerne les aides aux réorganisations, fusions et regroupements ; le cinquième concerne la formation et le soutien technique de renouvellement urbain. Leurs positions restent identiques dans la vue fournie. L452-2-1 transfère leurs décisions au conseil sans modifier les bénéficiaires, les anciens concours ou l'ouverture aux futures opérations éligibles. Il ne confond pas le septième alinéa de subventions fédérales avec ces deux alinéas et ne rétablit pas son approbation particulière supprimée.",
    ('L452-4-1', 'L452-4'): "Le troisième alinéa du I de L452-4 définit les logements et produits des SEM et organismes L365-2, avec conventionnement ou concours de l'Etat outre-mer. La vue proposée conserve ces définitions pour les prélèvements distincts tout en supprimant la cotisation générale à partir du 1er janvier suivant l'entrée en vigueur. L452-4-1 supprime désormais sa propre cotisation additionnelle à la même première année, sans confondre les deux mesures, sans rendre ses exercices de référence recouvrables et sans supprimer les versements favorables futurs du II de L452-4. Les exclusions et réfactions de l'additionnelle restent opposables aux seules anciennes années.",
    ('L472-3', 'L441-2-3-3'): "Le 5° de L472-3 exclut expressément à Mayotte L441-2-3-3, qui organise le versement à l'Etat et les sûretés d'une créance de relogement d'occupants lorsque le propriétaire ou exploitant a manqué à son obligation. La proposition cible plafonne certains frais et préserve les créances anciennes ; elle n'est pas une indemnité salariale. Maintenir l'exclusion territoriale ne fait donc appliquer ni ces frais ni le régime nouveau à Mayotte par simple renvoi, sans préjuger les autres fondements autonomes de protection des occupants.",
    ('L482-3', 'L441-9'): "La source L441-9 organise l'enquête annuelle avec un mois pour répondre, dispenses des bénéficiaires d'aides, mise en demeure de quinze jours et régularisation du supplément. Sa proposition supprime la finalité SLS pour les périodes nouvelles et ne cite au premier alinéa que L442-2-1 et L442-3-3. L482-3 doit donc expliciter le maintien de cette même enquête dans le champ SEM pour le contrôle des ressources effectives, avec les mêmes délais, dispenses et réemploi, sans nouvelle collecte ni majoration. La proposition le fait au I et préserve intégralement les deux années, les 150 %, le retour sous plafond PLS et les exemptions ; une mention symétrique dans L441-9 reste à assembler.",
    ('L482-3-1', 'L441-9'): "L441-9 officiel règle une demande annuelle de ressources, un délai d'un mois, des dispenses d'aides, puis certaines conséquences sur le supplément après quinze jours de mise en demeure. Sa proposition conserve seulement les finalités autonomes pour les périodes nouvelles et le stock SLS ancien. Aucune de ces règles n'impose de conserver la déchéance du bail de L482-3-1 : cette sanction distincte est abolie sans effacer les demandes utiles restantes, ni les garanties anciennes. Le contrôle matériel de L482-3 est coordonné séparément ; un défaut de réponse ne prouve pas un dépassement des plafonds."
}

work_numbers = ['L1234-1', 'L1221-2', 'L1234-9']
for s in sources:
    n = s['number']
    key = s['code_id'] + '|' + s['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        tn = t['number']
        if tn in work_numbers:
            assessment = work_ref_assessments[n][work_numbers.index(tn)]
        else:
            assessment = specific_checks[(n, tn)]
        checks.append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))
    answers[n]['reference_checks'] = checks

result = [answers[s['number']] for s in sources]
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json: {len(result)} articles')
