import html
import json
import re
from pathlib import Path


source = json.loads(Path('source.json').read_text())[0]
paragraphs = re.findall(r'<p>.*?</p>', source['source_xml'], flags=re.S)
iv_start = next(i for i, p in enumerate(paragraphs) if p.startswith('<p>IV.'))
iv = paragraphs[iv_start:]
assert len(iv) == 13

intro = [
    "I. – Les obligations de taux minimal de logements sociaux imposées aux communes par les I et II du présent article dans leur rédaction antérieure, ainsi que le quota par opération prévu au III ter dans cette même rédaction, sont supprimés à l'entrée en vigueur de la loi portant la présente rédaction. Il en va de même des objectifs de rattrapage, prélèvements, majorations, procédures de carence et pouvoirs de substitution dont le seul fondement est le non-respect de ces taux ou de ces objectifs. Aucun renvoi à ces dispositions dans un autre texte ne peut en maintenir l'application pour l'avenir, sous réserve des seules situations antérieures définies au V.",
    "II. – Abrogé.",
    "III. – Abrogé.",
    "III bis. – Abrogé.",
    "III ter. – Abrogé.",
    "IV. – Les catégories et assimilations du présent IV définissent les logements sociaux pour l'application des dispositions qui y renvoient. Elles n'instituent aucun quota communal, objectif de rattrapage, inventaire ou déclaration obligatoire. Les logements locatifs sociaux retenus pour l'application du présent IV sont :",
]

proposed = [f'<p>{html.escape(p, quote=False)}</p>' for p in intro]
# Maintien littéral des six catégories et des trois premiers alinéas d'assimilation.
proposed.extend(iv[1:10])
proposed.append(
    "<p>Lorsqu'une disposition distincte du régime de quotas supprimé renvoie au présent IV pour déterminer les résidences principales, sont retenues celles qui figurent dans les données légalement disponibles de l'administration fiscale, principalement issues de la déclaration des propriétaires prévue à l'article 1418 du code général des impôts, déduction faite des logements concédés par nécessité absolue de service en application de l'article L. 4145-2 du code de la défense et de ceux concédés à des militaires des armées dans des immeubles dépendant du domaine de l'Etat. Cette définition n'impose aucune transmission ni collecte supplémentaire au titre du régime supprimé.</p>"
)
# Les alinéas douze et treize du IV conservent aussi leur place et leur texte.
proposed.extend(iv[11:13])
proposed.append(
    "<p>Les renvois au présent article qui ont pour seul objet de désigner une catégorie de logements, sans définir un territoire ou une commune assujettie, s'entendent comme visant le présent IV. Ils ne rétablissent ni les taux ni les obligations supprimés. Les catégories, assimilations et durées du présent IV restent applicables aux dispositifs autonomes qui utilisent ces définitions, y compris pour les opérations futures qui en remplissent les conditions, ainsi qu'à la liquidation des situations antérieures. Pour la détermination des résidences principales à l'article L. 444-2, le renvoi à l'avant-dernier alinéa du présent article s'entend du onzième alinéa du présent IV.</p>"
)

transition = [
    "V. – La suppression des obligations prévues aux I, II et III ter dans leur rédaction antérieure s'applique à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris aux demandes d'autorisation et aux périodes de rattrapage en cours. Aucun nouveau constat de carence, aucune nouvelle majoration ni sanction ne peut être prononcé après cette date pour le seul non-respect des obligations supprimées, même au titre d'une période antérieure. Les effets futurs des arrêtés de carence cessent à cette date. Les autorités compétentes de droit commun reprennent les instructions en cours sur les dossiers déjà constitués, sans nouveau dépôt ni recommencement des délais écoulés.",
    "Aucun prélèvement, contribution obligatoire, reprise de déduction ou charge équivalente ne peut naître, sur le seul fondement des dispositions supprimées, d'un fait générateur survenu à compter de cette date. Les créances légalement nées de faits générateurs antérieurs restent régies par les dispositions antérieurement applicables pour leur liquidation, leur rectification, leur exigibilité, leur recouvrement, leurs exonérations, leurs plafonds, leurs déductions, leur affectation, leur restitution, leur prescription et leurs recours, même si une échéance ou un encaissement intervient ensuite. Une nouvelle décision de carence ou de majoration ne peut être prise pour faire naître une créance après la suppression. Les dispositions répressives plus douces s'appliquent aux sanctions qui ne sont pas devenues définitives. Aucun remboursement général ni crédit remboursable au titre d'un report de déduction inutilisable n'est institué.",
    "Les actes régulièrement pris, les conventions valablement conclues et les engagements financiers acquis avant cette date, les opérations valablement engagées, les droits des occupants, des cocontractants et des tiers ainsi que les aides régulièrement attribuées sont préservés. Leurs conditions d'exécution et les recours correspondants restent applicables. Les stipulations qui se bornent à rappeler les quotas ou obligations légales supprimés cessent d'en imposer le respect pour l'avenir. Aucun avenant ne peut, sur le seul fondement d'une carence abrogée, mettre à la charge d'une commune une nouvelle opération ou une contribution supplémentaire obligatoire ; les engagements librement consentis sur un fondement distinct restent possibles.",
    "Les prescriptions d'une autorisation d'urbanisme régulièrement délivrée avant cette date ne sont pas automatiquement supprimées. Elles restent susceptibles d'être modifiées ou contestées selon les voies ordinaires, dans le respect des droits des tiers. La suppression des quotas ne supprime pas les règles d'urbanisme, de sécurité, de salubrité, d'attribution, de conventionnement, de financement ou de protection des occupants qui disposent d'un fondement légal autonome. Les aides, exonérations, dispenses et dérogations relevant de ces fondements distincts demeurent applicables, y compris aux opérations et situations futures qui en remplissent les conditions ; leur refus ne peut être fondé sur la seule suppression des quotas ou de leurs listes d'application.",
]
proposed.extend(f'<p>{html.escape(p, quote=False)}</p>' for p in transition)
proposed_xml = '\n'.join(proposed)


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml))


reason = (
    "Réforme de fond par rapport à la source officielle entière : suppression des quotas communaux de 25 % et de 20 %, du quota de 25 % par opération au III ter, des circuits de fixation des taux et d'exemption devenus sans objet, et de la transmission fiscale exclusivement destinée au décompte supprimé. Aucun agrément, inventaire ou déclaration de remplacement. Les conséquences sur le rattrapage, le prélèvement et la carence sont coordonnées, sans les compter comme autant de nouvelles suppressions dans cet article. Le IV conserve littéralement les six catégories et les assimilations, sauf son introduction devenue autonome et la définition fiscale sans transmission SRU. Le V assure une extinction prospective et protège les anciennes créances, exonérations, opérations, conventions et recours. Seconde passe : aucune coupe supplémentaire des conditions matérielles du IV n'est justifiée. Les conditions de ressources, plafonds de loyer, conventions et agrément de financement identifient les logements aidés et protègent leurs occupants ; le seul renvoi à un agrément existant ne démontre pas un second agrément. Les durées favorables de décompte ne sont ni des délais d'attente ni des formalités. La proposition antérieure de suppression des quotas est donc conservée sur le fond, avec une garantie explicite des avantages futurs et la coordination du renvoi incohérent de L444-2 ; ces précisions ne sont pas présentées comme une coupe nouvelle."
)

review_notes = (
    "Lecture intégrale de la source, de sa note d'entrée au 1er janvier 2023, du previous_draft et de l'article 55 initial joint au sru_context. L'article 55 initial portait notamment un taux de 20 % ; la source actuelle porte aussi 25 %, l'EPCI, les III bis/ter et des assimilations ultérieures : la filiation SRU ne prouve donc pas que chaque condition actuelle provient de 2000. Aucune prétention d'achèvement de l'examen des 209 articles. La note de 2023 n'est pas la date de la réforme proposée.\n"
    "Contrôle du IV : positions conservées des treize alinéas initiaux, six catégories, 5 janvier 1977, 31 décembre 2016, cinq ans après convention, dix ans après vente, assimilation des logements financés ou attribués dans les conditions du dixième alinéa, deux exclusions militaires du dénominateur, signature de location-accession postérieure à la publication de la loi du 23 novembre 2018, cinq ans après levée d'option et BRS depuis le 1er janvier 2019. Le dernier alinéa ajouté ne déplace pas les huitième, neuvième, douzième ou treizième alinéas visés par R302-15. Ce règlement a été lu en entier : ses inventaires et données SRU doivent disparaître avec L302-6, mais ses équivalences de logements ont une utilité autonome à conserver. D331-76-5-1, lu en entier, rattache la convention et l'agrément de location-accession au financement, aux plafonds, aux garanties de rachat et de relogement ; L302-5 n'en impose pas une seconde demande. L365-4 et L831-1 ont également été lus ; le renvoi à L365-4 ne rétablit pas les renouvellements ou extensions territoriales que sa proposition du corpus supprime.\n"
    "Incohérence préexistante vérifiée : L444-2 renvoie à l'avant-dernier alinéa de L302-5 pour les résidences principales, alors que, dans la source actuelle, cet alinéa traite de la location-accession. La coordination interprétative ajoutée au IV vise explicitement son onzième alinéa ; elle n'abaisse ni ne supprime le seuil autonome de 20 % de L444-2. Les renvois de catégorie, notamment L253-8, L302-16, L342-2, L411-2 et urbanisme L151-28/R151-37, doivent viser le IV sans rétablir un territoire déficitaire. Les durées autonomes, dont les six ans de L411-5, ne sont pas remplacées par les cinq ans du huitième alinéa du IV.\n"
    "Coordinations distinctes identifiées, non réécrites par ce fichier : CCH L302-4, L302-6 à L302-9-1-2, R302-14/14-1/15 et les dispositions de décompte ou de prélèvement ; urbanisme L111-24, L131-9 et R*431-16-3 ; CGI 150 U et 150 VE pour les conditions supplémentaires liées aux communes déficitaires, sans retrait de leurs exonérations autonomes. L353-15 VII, L411-5-1, L443-7, L443-13, L443-15-2-3, L443-15-6 et L445-1 appellent la suppression de leurs seules restrictions liées au déficit ou à la carence, en maintenant les protections autonomes des occupants. La fin de L302-5 ne signifie pas l'abrogation générale de ces articles.\n"
    "Point territorial à coordonner expressément : urbanisme L151-22 et L151-36-1 utilisent l'ancienne liste du dernier alinéa du II pour des objets distincts. Le premier porte une règle environnementale autonome ; le second une dispense favorable de stationnement, à laisser ouverte aux futures opérations éligibles. Le V interdit de refuser cette dispense du seul fait de la suppression de la liste, mais ne tient pas lieu de la réécriture de son critère territorial dans L151-36-1 ni de sa coordination réglementaire. Cette coordination demeure identifiée et non déclarée achevée. Les seuils autonomes de parc social dans CGI 279-0 bis A, 1384 B/C/G et 1391 D ne sont pas des quotas de production supprimés ici ; leurs définitions, champs et avantages restent distincts.\n"
    "Hors des cinq codes : coordonner notamment l'imputation des anciennes sommes au CGCT L2332-2 et les subventions foncières visées à L2254-1, ainsi que les textes financiers d'affectation des recettes anciennes. Ces textes ne sont pas présentés comme réécrits. Les normes de bruit, risques technologiques/naturels/miniers, recul du trait de côte, captages et défense citées aux anciens III bis/ter ne sont pas abrogées : seule leur fonction d'exemption d'un quota désormais supprimé disparaît. Les dérogations littorales et la franchise TASCOM de 1 500 euros sont hors du champ des suppressions. Aucun taux fiscal, financement de remplacement, rendement ou effet national chiffré n'est créé. Les créances antérieures peuvent avoir des échéances postérieures ; une créance nouvelle ne peut naître d'un fait générateur postérieur sur le fondement supprimé."
)

benefit_review = (
    "II : le taux communal de 20 %, plus favorable que 25 %, devient sans objet uniquement parce qu'aucun des deux quotas ne subsiste pour l'avenir. III : les exemptions pour isolement/faible attractivité et faible tension locative, ainsi que III bis : les exemptions liées au bruit, aux servitudes, aux risques technologiques, naturels ou miniers, au recul du trait de côte et aux captages, ne sont pas remplacées par une contrainte générale : toutes les communes sont libérées des quotas. Les protections de sécurité et les dérogations littorales autonomes subsistent. III ter : la dérogation préfectorale et la non-opposabilité aux logements d'agents de la défense n'ont plus à être sollicitées ou invoquées, puisque le quota par opération est entièrement supprimé, sans quota de remplacement. IV : les six catégories restent entières, y compris outre-mer, foyers, personnes handicapées, hébergement, accueil des demandeurs d'asile, terrains familiaux et intermédiation locative. Restent applicables aux futures situations éligibles les cinq ans après fin de convention, dix ans après vente au locataire, l'assimilation du dixième alinéa notamment pour les anciens supplétifs, les exclusions des logements militaires du dénominateur, la location-accession dès le contrat éligible et pendant cinq ans après l'option, ainsi que les BRS depuis 2019. Les dates historiques ne ferment pas ces catégories aux opérations nouvelles qui satisfont leurs conditions. Le conventionnement, les ressources, le plafond de loyer et l'agrément existant qualifient l'avantage ou protègent l'occupant ; aucun nouveau dossier n'est requis ici. Le V préserve explicitement les aides, exonérations, dispenses et dérogations autonomes pour les opérations futures, en particulier sans refus fondé sur la disparition des listes ; la dispense de stationnement de L151-36-1 nécessite la coordination territoriale précisément signalée. Les avantages fiscaux utilisant le IV ne sont pas abrogés. Les exonérations, plafonds, déductions, restitutions et recours restent intégralement applicables aux créances SRU anciennes ; l'absence de prélèvement nouveau n'ouvre ni remboursement général ni crédit artificiel. La franchise TASCOM et les exemptions littorales ne sont pas supprimées par ce texte."
)

impact = {
    'version': 1,
    'classification': 'material_reduction',
    'assessment': (
        "Par rapport à l'intégralité de L302-5 officiel, le texte supprime effectivement les taux communaux de 25 %/20 %, le quota opérationnel de 25 % et leurs circuits de listes et de dérogation, sans formalité équivalente. Ils sont regroupés en un seul effet de suppression du régime de quotas ; les renvois aux prélèvements, au rattrapage et à la carence ne sont pas des taxes supplémentaires supprimées par cet article. La seconde passe ne revendique aucune coupe supplémentaire des conditions du IV par rapport au previous_draft. Le maintien des définitions, des avantages futurs et la correction du renvoi de L444-2 sont des coordinations, sans gain fiscal nouveau."
    ),
    'scope_limitations': (
        "La réduction porte sur les quotas nationaux de cet article pour l'avenir et sur leurs seuls prolongements, non sur toute obligation locale d'urbanisme ou de logement. Les créances, engagements et permis antérieurs sont soumis aux réserves du V. La réécriture des articles d'exécution et des critères territoriaux autonomes, notamment la dispense de L151-36-1, n'est pas accomplie par ce fichier. Les sources annexées ne prouvent pas l'achèvement des 209 volets SRU. Aucun coût de conformité, solde budgétaire, gain de logement ou effet national net de complexité n'est chiffré ni démontré."
    ),
    'new_burdens_review': (
        "Aucune charge nouvelle n'est identifiée dans l'article proposé : ni dépôt, déclaration, registre, donnée supplémentaire, autorisation de remplacement, minimum temporel ni condition fiscale nouvelle. La référence aux données fiscales légalement disponibles n'impose aucune nouvelle transmission et ne modifie pas l'obligation autonome de CGI 1418. Les conditions du IV existent déjà ; la reprise des instructions en cours réattribue une tâche existante aux autorités de droit commun sans nouveau dossier ni reprise de délai. L'adaptation des services et la coordination des textes ont un coût non chiffré ; aucune réduction nette de coût sur l'ensemble des codes n'en est déduite."
    ),
    'effects': [
        {
            'kind': 'obligation_removed',
            'measure_id': 'sru-suppression-quotas-logements-sociaux',
            'description': (
                "Suppression du régime de quotas de L302-5 : taux communaux, quota de 25 % par opération, listes triennales nécessaires à leurs taux et exemptions, et demande préfectorale pour déroger au quota opérationnel. Un effet unique couvre ces composantes et leurs dispenses devenues inutiles ; aucune suppression distincte de taxe n'est comptée ici."
            ),
            'before': (
                "Quota communal de 25 % des résidences principales au I, abaissé à 20 % dans les cas du II : communes d'au moins 1 500 habitants dans l'unité urbaine de Paris ou 3 500 ailleurs, dans une agglomération/EPCI de plus de 50 000 habitants comprenant une commune de plus de 15 000 habitants ; extension à certaines communes de plus de 15 000 habitants en croissance. Listes et exemptions des III/III bis. Dans les communes du III ter, au moins 25 % de logements familiaux sociaux pour les opérations collectives de plus de douze logements ou plus de 800 mètres carrés de surface de plancher, sous les dérogation et exception de ce III ter. Ces pourcentages sont des quotas de logements, pas des taux d'impôt."
            ),
            'after': (
                "Aucun taux minimal communal de 20 % ou de 25 % ni quota de 25 % par opération ne subsiste sur ces fondements pour les décisions et situations futures. Les listes d'assujettissement/exemption et la demande de dérogation correspondantes cessent sans procédure de remplacement. La définition autonome du IV et les protections distinctes demeurent. Les prélèvements et obligations d'exécution font l'objet de leurs coordinations propres, sans être comptés ici une seconde fois."
            ),
            'unit': 'legal_duty',
            'affected_population': (
                "Communes entrant dans les I ou II antérieurs, communes exemptées des III/III bis et maîtres d'ouvrage des opérations collectives du III ter ; services et EPCI chargés des listes et dérogations de ce dispositif. Les autres fondements d'urbanisme et les occupants protégés par des régimes distincts restent hors de cette suppression."
            ),
            'conditions_and_transition': (
                "À l'entrée en vigueur de la loi portant la nouvelle rédaction, sans date de promulgation inventée ; demandes d'autorisation et périodes de rattrapage en cours incluses. Aucun nouveau constat de carence ni majoration fondés sur le seul manquement ancien. Créances légalement nées, exonérations et déductions anciennes, contrats, opérations, droits des tiers et permis régulièrement délivrés préservés selon le V ; réserve des dispositions répressives plus douces. Avantages autonomes encore ouverts aux futures situations éligibles."
            ),
            'replacement_or_new_burdens': (
                "Aucun quota, agrément, inventaire ou déclaration de remplacement. Pas de nouveau dossier ou délai lors du retour des instructions à l'autorité de droit commun. Le IV conserve les conditions existantes des catégories aidées et ne crée aucune transmission ; les textes autonomes et les anciens engagements restent dans leur champ. Les coûts administratifs de transition ne sont pas chiffrés."
            ),
            'source_quote': plain('\n'.join(paragraphs[:iv_start])),
            'proposed_quote': intro[0],
        }
    ],
}

answer = {
    key: source[key]
    for key in ('code_id', 'source_id', 'source_sha256', 'number')
}
answer.update({
    'proposed_xml': proposed_xml,
    'reason': reason,
    'review_notes': review_notes,
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Quotas communaux de 25 % et de 20 % des résidences principales, avec leur champ d'assujettissement et leur extension aux communes en forte croissance démographique.",
        "Décrets et listes périodiques de détermination des taux de 20 % ou de 25 %, sans nouveau classement d'assujettissement en remplacement.",
        "Procédure de liste des communes exemptées du III : proposition des EPCI, avis départemental et régional et avis de la commission nationale pour ce seul dispositif.",
        "Arrêté périodique de liste des communes exemptées pour inconstructibilité au III bis, sans abrogation des normes autonomes de risques, bruit, littoral et captage.",
        "Quota de 25 % des logements familiaux par opération au III ter et demande motivée d'une dérogation préfectorale à ce quota ; son exception défense devient sans objet.",
        "Transmission de la liste fiscale exclusivement destinée au décompte SRU supprimé ; maintien de la définition autonome des résidences principales sans transmission ni collecte de remplacement.",
    ],
    'benefit_review': benefit_review,
    'substantive_impact': impact,
})

Path('answer.json').write_text(
    json.dumps([answer], ensure_ascii=False, indent=2) + '\n'
)
print(json.dumps({
    'articles': 1,
    'source_paragraphs': len(paragraphs),
    'proposed_paragraphs': len(proposed),
    'proposed_characters': len(proposed_xml),
    'effects': len(impact['effects']),
}, ensure_ascii=False))
