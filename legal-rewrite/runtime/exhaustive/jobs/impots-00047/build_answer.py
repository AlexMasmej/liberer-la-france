import json
import re
from html import unescape
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
REFS = json.loads(Path('reference-targets.json').read_text())
BY_NUMBER = {a['number']: a for a in SOURCES}
ANSWERS = []


def clean_xml(value):
    # Remove presentation attributes from the source table, retaining every cell.
    return re.sub(r'\s+(?:align|border|cellpadding|cellspacing)="[^"]*"', '', value)


def plain(value):
    return unescape(re.sub(r'<[^>]*>', '', value or ''))


def impact(classification, assessment, scope, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope, new_burdens_review=burdens, effects=effects or [])


def effect(kind, measure, description, before, after, unit, population, transition,
           burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def add(number, text, reason, notes, benefits, substantive, checks=None, **extra):
    source = BY_NUMBER[number]
    item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(proposed_xml=text, reason=reason, review_notes=notes,
                status='retained_unchanged' if text is None else 'rewrite_draft',
                benefit_review=benefits, substantive_impact=substantive)
    if text is None:
        item['classification'] = 'retained_necessary'
    required = REFS['requirements'].get(source['code_id'] + '|' + source['source_id'], [])
    checks = checks or {}
    assert set(checks) == set(required), (number, required, checks)
    item['reference_checks'] = [dict(target_key=k, view_sha256=REFS['targets'][k]['view_sha256'],
                                     assessment=checks[k]) for k in required]
    item.update(extra)
    ANSWERS.append(item)


T44 = 'LEGITEXT000006069577|LEGIARTI000051217272'
T206 = 'LEGITEXT000006069577|LEGIARTI000054373514'
T163 = 'LEGITEXT000006069577|LEGIARTI000027795200'
T223 = 'LEGITEXT000006069577|LEGIARTI000048834056'
T39 = 'LEGITEXT000006069577|LEGIARTI000053542680'
T38 = 'LEGITEXT000006069577|LEGIARTI000051203585'
L1 = 'LEGITEXT000006072050|LEGIARTI000006901112'
L2 = 'LEGITEXT000006072050|LEGIARTI000019071087'
L9 = 'LEGITEXT000006072050|LEGIARTI000035644154'


add('208 D', None,
    "Maintien intégral d'un régime d'exonération, sans réécriture stylistique. Les plafonds de participation et d'actifs ainsi que l'absence de fonctions dirigeantes délimitent l'investissement à risque indépendant ; ils n'instituent ni agrément ni dépôt supplémentaire à retirer. La dérogation en cas de décès et les avances autorisées sont favorables. Le régime, réservé aux sociétés créées avant le 1er juillet 2008, ne doit pas être rouvert artificiellement ni supprimé au détriment d'effets historiques encore opposables. Les bénéfices définitivement exonérés relèvent déjà de la protection du XI de l'article 209 proposé.",
    "Lecture des I à III et du renvoi au caractère nouveau défini à l'article 44 sexies. Les seuils de 30 % (société et famille), de 15 % et de 5 %, le délai de cinq ans et le dixième exercice sont conservés. Le renvoi au 1° du 1 du III de l'article 975 vise les fonctions sociales, dont le texte public a été lu, et non une indemnité de rupture. L'assujettissement de droit commun des sociétés investies reste distinct de l'exigibilité de leur IS. Les XI à XIII de 209 et V à VI de 219, consultés dans le corpus comme propositions, protègent les exonérations définitives sans réouvrir la fenêtre de création. La transmission au décès n'est ici qu'une condition favorable de maintien de l'IS : elle n'autorise aucun droit de succession.",
    "L'exonération d'IS jusqu'au dixième exercice, la faculté d'avances en compte courant à hauteur de 15 % de l'actif et d'autres actifs à hauteur de 5 %, ainsi que le maintien après décès malgré la pluralité d'associés, sont intégralement conservés. Les effets restant juridiquement ouverts aux sociétés créées dans la fenêtre légale ne sont pas fermés ; aucune condition nouvelle n'est ajoutée. Les bénéfices définitivement exonérés ne deviennent pas imposables lors d'une distribution ultérieure du seul fait de la réforme générale de l'IS.",
    impact('retained_necessary',
           "L'article entier organise une exonération ciblée et ses tolérances, non une taxe accessoire autonome ; aucune réduction nouvelle n'est revendiquée.",
           "La date limite de création de 2008 et la durée propre de l'exonération ne sont pas prolongées ; aucune économie nationale n'est évaluée.",
           "Aucune charge nouvelle n'est identifiée : le texte reste intégralement maintenu et aucun agrément, état ou justification supplémentaire n'est ajouté."),
    {T44: "Le I, 2, b de 208 D vise la nouveauté de l'entreprise : c'est le III de 44 sexies qui exclut concentrations, restructurations, extensions et reprises. Il ne renvoie pas au seuil de trois salariés du I ni à sa référence à des contrats d'au moins six mois. La proposition fournie reste une proposition et ne coordonne pas encore cette dernière formule au contrat unique ; cette lacune de la cible n'autorise ni à créer un CDD dans 208 D ni à fermer l'exonération historique. Aucun préavis, ancienneté de rupture ou notification n'est condition du présent avantage."})

add('208 ter', None,
    "Maintien intégral des trois exclusions favorables de revenus patrimoniaux. Leur suppression élargirait l'assiette du régime distinct applicable aux organismes du 5 de l'article 206. L'article n'exige ni autorisation, ni déclaration spéciale, ni justificatif autonome pouvant être supprimé.",
    "Le 5 de 206 reste un régime patrimonial annuel distinct dans le 12 proposé de cet article : l'IS à la distribution ne rend donc pas ces exonérations inutiles. Les textes publics de 133, 138 et 146 quater et leurs notes ont été lus : leurs fenêtres historiques d'emprunt demeurent, sans interdire les produits futurs d'emprunts recevables. Le renvoi à 133, 1° est expressément étendu ici aux emprunts non négociables et ne doit pas être remplacé par un renvoi générique à tout 133. La note de 2011 demeure historique.",
    "Les intérêts des livrets A, les produits des emprunts non négociables locaux sous les réserves du 1° de 133 et les produits des emprunts visés à 138, 4° et 146 quater restent exclus. La dispense de négociabilité du c est conservée. Le maintien couvre les revenus futurs remplissant ces conditions ; le régime patrimonial distinct n'est pas absorbé par la réforme de l'IS ordinaire.",
    impact('retained_necessary',
           "Les trois exclusions d'assiette sont entièrement maintenues ; aucune nouvelle taxe ou formalité supprimée n'est comptée.",
           "Les autres revenus patrimoniaux et les conditions historiques des emprunts gardent leur régime ; aucune exonération générale de l'organisme n'est créée.",
           "Aucune charge nouvelle n'est identifiée puisque les conditions et renvois de l'exonération sont conservés sans démarche supplémentaire."),
    {T206: "Le renvoi vise exactement le 5 de 206, qui impose les revenus patrimoniaux sans rattachement aux activités lucratives, sous ses exclusions personnelles. Le 12 de la proposition 206 maintient expressément ce régime et celui de 219 bis hors de l'IS ordinaire à la distribution. L'exclusion des intérêts de 208 ter conserve donc son utilité pour les revenus futurs. Les dispositions de 206 relatives aux associations employeuses n'imposent ici aucune ancienneté, indemnité de rupture ou notification de contrat."})

add('208 ter A', None,
    "Maintien intégral de l'exclusion des intérêts de parts sociales des caisses locales non bancaires. Elle évite de soumettre ces produits au régime patrimonial résiduel de 206, 6, 2°. Supprimer le texte serait une hausse d'assiette ; il ne porte aucune formalité ou prélèvement accessoire à retirer.",
    "Le 2° du 6 de 206 concerne les caisses sans activité bancaire pour leur propre compte ou sans activité rémunérée d'intermédiaire financier, et renvoie à 206, 5 et 219 bis. Il demeure distinct dans la proposition 206, 12. L'exonération des intérêts reçus ne doit pas être confondue avec une exonération de toute l'activité bancaire des caisses du 1°. Aucun renvoi au contrat privé ni règle nouvelle d'ancienneté n'est concerné.",
    "Les intérêts versés sur les parts sociales détenues dans les caisses d'affiliation restent intégralement hors revenu imposable des caisses locales relevant du 2° du 6 de 206. Le bénéfice continue pour les intérêts futurs et les caisses nouvellement éligibles à ce régime, sans nouvelle autorisation ni réserve aux seules participations anciennes.",
    impact('retained_necessary',
           "L'exclusion des intérêts de parts dans les caisses d'affiliation est préservée intégralement, sans prétendre simplifier un article sans procédure autonome.",
           "Le maintien est limité aux caisses visées au 2° du 6 de 206 ; il n'étend pas l'exonération aux activités bancaires ordinaires.",
           "Aucune charge nouvelle n'est identifiée : aucun dépôt, délai ou condition n'est ajouté au texte maintenu."),
    {T206: "Le renvoi est au 2° du 6, non au 1° : il vise les caisses locales dépourvues des activités bancaires ou d'intermédiation rémunérée qui y sont définies, imposées selon le 5 et 219 bis. La proposition 206, 12 réserve expressément les revenus patrimoniaux relevant de ces règles propres. La franchise d'intérêts reste applicable aux situations futures éligibles, sans dépendre de l'ancienneté d'un salarié, d'un préavis ou d'une notification."})


def employment_checks(article):
    subject = ('les organismes bénéficiaires et les intérêts de livrets ouverts avant 2009' if article == '208 ter B'
               else "l'indemnité sanitaire d'abattage et la reconstitution du cheptel")
    return {
        L1: f"L'article {article} concerne {subject} ; il ne comporte aucun renvoi à L1234-1. La cible porte sur le préavis de licenciement, anciennement modulé selon six mois et deux ans, proposé à quinze jours pour les nouveaux contrats. Ni ce préavis ni sa notification ne sont des conditions de cet avantage fiscal ; aucun renvoi ne doit être créé artificiellement.",
        L2: f"L'article {article} concerne {subject}, sans contrat de travail ni terme d'emploi. L1221-2 proposé supprime les nouvelles embauches à durée déterminée en conservant les anciens contrats. La durée d'ouverture d'un livret ou celle de reconstitution d'un cheptel n'est pas la durée d'un emploi ; cette cible ne justifie aucune modification du champ fiscal ni restriction d'avantage futur.",
        L9: f"L'article {article} ne renvoie pas à l'indemnité ordinaire de rupture. L1234-9 proposé retient un an au terme effectif, préavis inclus, puis 0,20 mois pour l'ancienneté totale, fractions en mois complets, plafond de six mois et employeur seul, avec transition des anciens droits. Ces conditions sont inapplicables à {subject} ; l'indemnité d'abattage, lorsqu'elle est en cause, n'est pas une indemnité de licenciement."
    }


add('208 ter B', None,
    "Maintien intégral de l'exonération des intérêts des comptes spéciaux sur livrets antérieurs à 2009 pour les quatre catégories bénéficiaires. La liste des syndicats et CSE protège leur avantage fiscal et n'impose aucune procédure d'embauche ou de rupture. Le texte n'institue ni taxe ni état annuel à supprimer.",
    "La limite du 1er janvier 2009 qualifie l'ouverture du compte, non la date de perception des intérêts ni la création de l'organisme bénéficiaire. La note de 2017 explique le remplacement des institutions représentatives par le CSE. Les trois cibles de travail imposées par le dossier ont été lues ; aucun renvoi à elles n'apparaît dans cet article. Le renvoi au titre III du livre Ier de la deuxième partie vise les syndicats professionnels et unions, non le contrat unique.",
    "L'exonération des intérêts est conservée pour les associations de 1901 et de droit local, les organismes cultuels, les syndicats et unions et les CSE. Elle s'applique aux intérêts futurs des livrets ouverts avant le 1er janvier 2009 qui restent éligibles. Ni une nouvelle durée de contrat, ni une condition de licenciement ou d'ancienneté ne restreint cet avantage.",
    impact('retained_necessary',
           "Les quatre catégories bénéficiaires gardent l'exclusion d'assiette ; aucun allègement nouveau n'est attribué à ce maintien.",
           "Les livrets ouverts à compter de 2009 restent hors du champ ; le régime des autres placements et impôts n'est pas modifié.",
           "Aucune charge nouvelle n'est identifiée : l'exonération et sa liste de bénéficiaires restent exactement celles de la source."),
    employment_checks('208 ter B'))

text = clean_xml(BY_NUMBER['208 septies']['source_xml']).strip() + """
<p>III. – Pour les exercices relevant du régime de distribution prévu aux V et VI de l'article 219, les transferts mentionnés aux I et II ne constituent pas, par eux-mêmes, une distribution. Les exonérations et la continuité des valeurs fiscales prévues aux mêmes I et II demeurent applicables. Les résultats dont la prise en compte est différée et les profits de cession ultérieurs sont suivis dans les conditions du XI de l'article 209 ; leur constatation ne déclenche pas un impôt sur les sociétés ordinaire sur un bénéfice conservé.</p>
<p>Pour l'application aux I et II du a du 3 de l'article 210 A, aucune reprise à une réserve spéciale des plus-values relevant de l'article 209 quater n'est exigée à compter de l'abrogation de cet article. La reprise des provisions dont l'imposition est différée et de la réserve de provisions pour fluctuation des cours demeure régie par ce a. Les bénéfices définitivement exonérés ou déjà imposés et les comptes qui les représentent conservent leur protection chez le bénéficiaire du transfert, sans double inscription.</p>
<p>Le présent III s'applique aux exercices ouverts à compter de l'entrée en vigueur de la présente loi, sans modifier les dates d'application prévues aux I et II. Les exercices antérieurs, leurs dettes, créances, exonérations, contrôles et recours restent régis par les dispositions qui leur étaient applicables. Les impositions de sortie et l'impôt minimum international demeurent régis par leurs dispositions propres.</p>"""
add('208 septies', text,
    "Coordination de fond nécessaire de deux neutralités fiscales avec l'IS à la distribution et avec la suppression de la réserve spéciale de 209 quater. Les I et II sont intégralement conservés, y compris leur valeur nette comptable, leurs destinataires et leurs dates. Le III empêche que le transfert ou un résultat de référence rétablisse une annualité ordinaire et écarte la reprise d'une réserve supprimée. Il ne constitue ni une seconde suppression de taxe ni une nouvelle dispense de toutes les obligations de 210 A.",
    "Les a, b, c et e du 3 de 210 A ont été lus dans le corpus : provisions et réserves au a, reprises au b, valeur fiscale des immobilisations non amortissables au c et des autres actifs au e ; le d n'est pas visé par les I et II et n'est pas ajouté. La référence du a à l'ancienne réserve de plus-values doit être coordonnée aussi dans 210 A, hors du lot ; la réserve pour fluctuation des cours reste autonome. Les nouveaux renvois à 209 XI et 219 V-VI ne sont pas des cibles fournies dans reference-targets.json ; leurs paragraphes proposés pertinents ont été consultés en lecture seule dans le corpus. Les dates du 1er janvier 2007 et du 7 janvier 2006 sont conservées. Aucun agrément agricole ni droit européen de reconnaissance n'est abrogé par cette coordination fiscale.",
    "La non-imposition des deux catégories de transferts à la valeur nette comptable demeure entière, pour toute opération future remplissant les conditions historiques et matérielles des I et II. Les valeurs fiscales, provisions et résultats différés assurent la neutralité sans effacement fictif d'une plus-value latente. Les bénéfices définitivement exonérés ou déjà taxés restent protégés après le transfert ; l'ancien compte de réserve de 209 quater n'est pas recréé.",
    impact('coordination_only',
           "Les deux neutralités de transfert et leurs conditions sont conservées ; le nouveau III coordonne seulement l'exigibilité et la réserve supprimée ailleurs.",
           "Les règles de reconnaissance des organismes, les reprises propres au régime et les obligations autonomes de 210 A restent à leur champ ; aucun rendement n'est établi.",
           "Aucune charge nouvelle propre à cet article n'est identifiée : le suivi est celui déjà prévu par 209 et la continuité fiscale existante, sans déclaration ni agrément supplémentaire.",
           [effect('coordination', 'is-distribution',
                   "Préserver la neutralité de ces transferts sans faire renaître un IS annuel ordinaire par leur suivi fiscal.",
                   "Les transferts sont exonérés ; les valeurs et résultats ultérieurs suivent a, b, c et e du 3 de 210 A.",
                   "La neutralité reste entière ; un résultat conservé alimente le suivi de 209 sans IS ordinaire avant distribution.",
                   'regime', "Syndicats et organismes bénéficiaires des transferts visés aux I et II.",
                   "Nouveau régime pour les exercices ouverts à l'entrée en vigueur ; dates sectorielles de 2006 et 2007 conservées.",
                   "Aucune déclaration de remplacement ; obligations de continuité fiscale existantes maintenues.",
                   "Pour la détermination de leurs résultats imposables, les bénéficiaires des transferts doivent se conformer aux dispositions prévues aux a, b, c et e du 3 de l'article 210 A",
                   "les transferts mentionnés aux I et II ne constituent pas, par eux-mêmes, une distribution."),
            effect('coordination', 'reserve-plus-values-complement-is-suppression',
                   "Écarter la reprise de la réserve spéciale de plus-values supprimée, sans écarter les provisions et réserves autonomes du a de 210 A.",
                   "Le renvoi au a du 3 de 210 A impose la reprise de la réserve spéciale de plus-values et des autres éléments visés par ce a.",
                   "La reprise de la seule réserve de 209 quater n'est plus exigée ; provisions différées et réserve de fluctuation des cours sont maintenues.",
                   'legal_duty', "Bénéficiaires des transferts relevant des I et II qui reprennent une réserve historique de plus-values.",
                   "Effet dans les nouveaux exercices, à compter de l'abrogation de 209 quater ; droits et résultats antérieurs conservés.",
                   "Pas de registre ni de déclaration de remplacement ; une même protection ne peut être inscrite deux fois.",
                   "les bénéficiaires des transferts doivent se conformer aux dispositions prévues aux a, b, c et e du 3 de l'article 210 A",
                   "aucune reprise à une réserve spéciale des plus-values relevant de l'article 209 quater n'est exigée à compter de l'abrogation de cet article.")]))

text = BY_NUMBER['208 octies']['source_xml'].strip() + """
<p>III. – Pour les exercices relevant des V et VI de l'article 219, l'exonération du I est attachée au bénéfice provenant de l'indemnité et réalisé pendant la période d'application du présent article. La distribution ultérieure de ce bénéfice ne fait pas perdre l'exonération du seul fait qu'elle intervient après cette période. Les montants concernés sont suivis selon le XI de l'article 209, sans double inscription ni double utilisation.</p>
<p>À l'expiration du délai de deux ans prévu au deuxième alinéa du I, la fraction rapportée au résultat corrige, à due concurrence, le traitement fiscal du bénéfice correspondant. La fraction demeurée dans l'entreprise ne supporte aucun impôt sur les sociétés ordinaire avant sa distribution. Pour la seule fraction déjà distribuée en exonération, l'impôt correspondant est régularisé, au titre de l'exercice au cours duquel expire ce délai, à l'échéance de régularisation annuelle prévue au 8 de l'article 1668, selon les règles de taux et d'assiette de l'article 219, sans imposer une seconde fois une fraction déjà taxée. Les déficits et crédits légalement imputables demeurent utilisables une seule fois, dans leurs conditions propres.</p>
<p>Les dispositions du présent article restent applicables aux indemnités prises en compte au titre des exercices ouverts entre le 1er janvier 2025 et le 31 décembre 2027. Le présent III s'applique aux exercices ouverts à compter de l'entrée en vigueur de la présente loi. Il ne modifie ni le délai de reconstitution du cheptel ni les conditions du II. Les dettes, créances, exonérations et recours relatifs aux exercices antérieurs restent régis par les dispositions qui leur étaient applicables.</p>"""
add('208 octies', text,
    "Coordination nécessaire de l'exonération sanitaire avec le fait générateur de distribution : qualification au titre du bénéfice d'origine, maintien après la fin de la fenêtre et reprise limitée à la fraction non remployée. Les deux ans et le règlement européen sont conservés car ils circonscrivent cette aide de reconstitution ; leur suppression sans lecture des conditions d'aide ne peut être présumée compatible. La reprise d'un montant resté dans l'entreprise n'est plus une exigibilité annuelle d'IS ordinaire. Aucun taux ni nouvelle aide n'est créé.",
    "La note de la loi du 19 février 2026 réserve les exercices ouverts du 1er janvier 2025 au 31 décembre 2027 : cette fenêtre est rendue explicite sans prolongation. Le délai de deux ans part de la perception de l'indemnité, non de la distribution. Si une fraction déjà distribuée doit être reprise, la régularisation annuelle concerne cette distribution passée, pas les bénéfices conservés. Les renvois nouveaux à 209 XI, 219 et 1668, 8 sont signalés comme non fournis parmi les cibles ; les paragraphes pertinents proposés de 209 et 219, ainsi que la source et la proposition complètes de 1668, ont été lus dans le corpus. Le 8 proposé de 1668 prévoit l'échéance annuelle du 15 du quatrième mois ou du 15 mai pour clôture au 31 décembre : son champ devra inclure expressément cette reprise, sans nouvelle échéance mensuelle. Le règlement (UE) 2022/2472 n'est pas annexé en texte intégral : aucune suppression de sa condition ni conformité européenne de la réforme générale n'est présumée. Les cibles de travail fournies sont sans rapport avec l'indemnité d'abattage.",
    "L'écart positif entre indemnité d'abattage et valeur nette à l'actif demeure exonéré, avec la reprise du seul excédent sur l'indemnité affectée à la reconstitution à deux ans. L'exonération reste ouverte à toutes les indemnités des exercices recevables jusqu'à 2027, sous le cadre européen, même si la distribution est plus tardive. La part conservée n'est pas taxée du seul fait de la reprise comptable ; déficits et crédits ne sont ni supprimés ni multipliés. L'indemnité sanitaire ne doit pas être confondue avec une indemnité de rupture du contrat de travail.",
    impact('coordination_only',
           "L'exonération et son remploi à deux ans sont maintenus ; la nouvelle disposition règle leur articulation avec l'IS à la distribution et la reprise éventuelle.",
           "Aucune extension après les exercices ouverts en 2027 ni suppression de la condition européenne ; reprise à inclure dans la régularisation annuelle du 8 proposé de 1668.",
           "Aucune pièce, autorisation ou déclaration autonome nouvelle n'est créée ; suivi et régularisation adaptent la reprise déjà prévue et utilisent le dispositif commun de distribution, dont le coût n'est pas chiffré.",
           [effect('coordination', 'is-distribution',
                   "Maintenir la condition de reconstitution et éviter la taxation ordinaire d'une reprise encore conservée.",
                   "L'excédent non remployé est rapporté au résultat de l'exercice où expire le délai de deux ans.",
                   "Reprise suivie dans le compartiment correspondant ; IS seulement sur la fraction distribuée, avec régularisation si elle l'était déjà.",
                   'regime', "Sociétés percevant l'indemnité sanitaire visée au I.",
                   "Exercices éligibles ouverts entre 2025 et 2027 ; coordination pour les exercices ouverts à l'entrée en vigueur, sans report du délai de deux ans.",
                   "Pas de nouveau dossier ; suivi commun et correction de l'imposition d'une distribution antérieure si nécessaire.",
                   "cette différence est rapportée au résultat de l'exercice au cours duquel intervient l'expiration de ce délai.",
                   "La fraction demeurée dans l'entreprise ne supporte aucun impôt sur les sociétés ordinaire avant sa distribution.")] ),
    employment_checks('208 octies'))

text = """<p>Le présent article est abrogé pour les exercices ouverts à compter de l'entrée en vigueur de la présente loi. Aucune évaluation fiscale annuelle à la valeur liquidative des parts, actions ou droits qu'il visait, aucun état spécifique des écarts et aucune annexe déclarative de ces écarts ne sont exigés sur son fondement pour ces exercices. Cette suppression s'applique aux détentions directes et indirectes et à celles réalisées par l'intermédiaire d'une société de financement spécialisé.</p>
<p>Aucune taxe pour rupture de l'engagement de conservation de cinq ans n'est due lorsque cette rupture intervient à compter de l'entrée en vigueur de la présente loi, y compris pour les engagements pris antérieurement. Aucune déclaration ou paiement propre à cette taxe ne peut être exigé au titre d'une telle rupture. Les exonérations et régimes favorables des parts ou actions concernés, prévus par d'autres dispositions, demeurent applicables dans leurs conditions propres, y compris pour les acquisitions et situations futures éligibles ; les dérogations à la seule évaluation annuelle supprimée ne constituent plus une condition pour en être dispensé.</p>
<p>Les exercices ouverts avant cette entrée en vigueur restent régis par les dispositions qui leur étaient applicables, sous réserve de la suppression de la taxe pour les ruptures postérieures prévue au deuxième alinéa. Leurs écarts positifs et négatifs déjà compris dans les résultats imposables corrigent le prix d'acquisition ou de souscription retenu lors de la cession ultérieure des titres, à hauteur des seuls montants qui n'ont pas déjà été neutralisés. Les reprises de provisions antérieurement non déduites sont exclues des résultats à due concurrence de cette non-déduction. Aucun écart, provision, profit ou perte ne peut être imposé ou déduit deux fois. Les dettes, créances, restitutions, prescriptions, contrôles et recours relatifs aux périodes et ruptures antérieures demeurent régis par leur droit.</p>
<p>Les règles comptables et prudentielles d'évaluation, les règles générales de détermination des profits et pertes lors de leur réalisation, les conditions générales de déduction des provisions et les règles propres à l'impôt minimum international ne sont pas abrogées. Pour les bénéfices relevant de l'IS ordinaire à la distribution, la réalisation d'un profit de cession n'entraîne pas, à elle seule, l'exigibilité de cet impôt tant que ce bénéfice reste dans l'entreprise. Aucune disposition d'application ni aucun renvoi au présent article ne peut rétablir pour un exercice nouveau l'évaluation fiscale, l'état des écarts ou la taxe supprimés.</p>"""
add('209-0 A', text,
    "Abrogation de fond du régime fiscal autonome de valorisation annuelle des OPC : disparition de l'évaluation et de son état spécifique, ainsi que de la taxe accessoire de 0,75 % par mois liée à la rupture d'une conservation de cinq ans. Ce n'est pas une suppression de l'IS sur les profits réalisés : ils suivent les règles générales et, dans le régime ordinaire nouveau, la distribution. Les corrections transitoires du prix de revient et des provisions évitent doubles impositions et doubles déductions. Les exceptions assurance/retraite, fonds investis à 90 % et FCPR n'ont plus à être satisfaites pour échapper à la seule valorisation abrogée ; leurs avantages autonomes ne sont pas supprimés.",
    "Tous les alinéas 1° à 5°, y compris les exclusions vie/capitalisation et retraite professionnelle, les moyennes journalières semestrielles de 90 %, les détentions indirectes, la société de financement spécialisé et les règles de provisions ont été lus. La note de 2018 ne fixe pas la date de la réforme proposée. Le 5 ter de l'article 38, dernière phrase, devra perdre son exclusion désormais sans objet pour les exercices nouveaux ; le renvoi de sa proposition actuelle à l'ancien 209-0 A est identifié, pas maintenu dans le nouveau texte. Coordonner aussi la seule mention de 209-0 A dans 242 quinquies et 1763 C sans supprimer leurs obligations et avantages autonomes liés à 38, 163 quinquies B, 150-0 A et 219. Ces deux articles ont été lus en entier dans le corpus. Le renvoi de l'annexe IV 56 J vicies concerne l'homonyme 209-0 A de l'annexe III sur la garantie des métaux précieux : il est étranger à la présente abrogation. Les régimes minimaux internationaux demeurent distincts. La baisse permanente concerne la taxe accessoire, pas la totalité de l'impôt futur sur les gains ; l'effet net public n'est pas chiffré.",
    "Les dispenses d'écarts pour l'assurance-vie, la capitalisation, les organismes de retraite supplémentaire, les OPC composés d'actions à 90 % et les FCPR/FPCI perdent leur seul objet restrictif parce que l'évaluation fiscale correspondante disparaît pour tous dans le nouveau champ temporel. Aucun impôt de remplacement sur les écarts ne les rend moins favorables. Les avantages distincts des fonds et des souscripteurs demeurent ouverts aux futures situations éligibles ; le délai de cinq ans de 163 quinquies B pour l'IR n'est pas abrogé. Les anciens écarts et provisions sont neutralisés une seule fois à la cession ou à leur reprise ; les remboursements et contentieux anciens sont protégés.",
    impact('material_reduction',
           "L'obligation fiscale annuelle d'évaluer les OPC et de produire l'état disparaît ; la taxe accessoire de rupture est abolie pour les ruptures nouvelles. L'IS sur les gains réalisés n'est pas aboli.",
           "Le report d'imposition des plus-values latentes n'est pas une baisse définitive de leur taux ; comptabilité, prudence, minimum international et obligations autonomes des fonds subsistent. Le solde global reste inconnu.",
           "Aucune charge nouvelle n'est identifiée : aucun état ou déclaration remplaçant l'ancien dispositif n'est créé. Seules les corrections d'anciens écarts et provisions sont maintenues pour prévenir les doubles emplois.",
           [effect('obligation_removed', 'opc-fin-evaluation-fiscale-annuelle',
                   "Retirer l'évaluation fiscale annuelle et l'état des écarts propre à cet article.",
                   "Valorisation à chaque clôture et état par catégorie annexé à la déclaration 53 A, sous les exceptions du 1°.",
                   "Aucune évaluation fiscale annuelle ni état des écarts sur ce fondement ; évaluations comptables et prudentielles autonomes conservées.",
                   'legal_duty', "Entreprises détenant directement ou indirectement les OPC et droits visés par l'ancien article.",
                   "Exercices ouverts à compter de l'entrée en vigueur ; suivi des écarts des exercices antérieurs conservé pour leur dénouement.",
                   "Aucun relevé de remplacement ; obligations comptables autonomes inchangées.",
                   "évaluent ces parts ou actions, à la clôture de chaque exercice, à leur valeur liquidative.",
                   "aucun état spécifique des écarts et aucune annexe déclarative de ces écarts ne sont exigés sur son fondement pour ces exercices."),
            effect('tax_removed', 'opc-taxe-rupture-conservation-suppression',
                   "Supprimer la taxe accessoire de rupture de l'engagement de conservation des parts de capital-investissement.",
                   "Taxe de 0,75 % par mois appliquée à l'impôt qui aurait été versé sur les écarts, en cas de rupture de l'engagement de cinq ans ; paiement sous trois mois de la clôture.",
                   "Zéro taxe accessoire sur les ruptures à compter de l'entrée en vigueur ; pas de taxe ou déclaration de remplacement, sans abolition de l'IS de droit commun sur les gains.",
                   'percent', "Entreprises ayant utilisé la dispense d'écarts sur des parts de FCPR ou FPCI sous engagement de conservation.",
                   "Ruptures nouvelles, même d'engagements anciens ; ruptures antérieures et leurs recours restent sous leur droit.",
                   "Aucune charge de remplacement au titre de la taxe ; avantages fiscaux distincts sous leurs conditions propres.",
                   "En cas de rupture de l'engagement, l'entreprise acquitte spontanément une taxe dont le montant est calculé en appliquant à l'impôt qui aurait été versé en application du deuxième alinéa un taux de 0,75 p. 100 par mois",
                   "Aucune taxe pour rupture de l'engagement de conservation de cinq ans n'est due lorsque cette rupture intervient à compter de l'entrée en vigueur de la présente loi, y compris pour les engagements pris antérieurement."),
            effect('payment_deferred', 'opc-fin-evaluation-fiscale-annuelle',
                   "Mettre fin à l'anticipation de l'IS sur la seule variation annuelle de valeur liquidative.",
                   "Les écarts positifs et négatifs annuels, nets de compensation, sont compris dans le résultat fiscal, sous exceptions ; aucun taux autonome d'IS n'est fixé ici.",
                   "Profits et pertes reconnus selon le droit commun à leur réalisation ; pour l'IS ordinaire nouveau, exigibilité seulement à la distribution et aux exceptions propres.",
                   'other', "Entreprises auparavant soumises aux écarts de valeur liquidative.",
                   "Nouveaux exercices ; prix fiscal ajusté des anciens écarts déjà retenus, sans second impôt sur la même base.",
                   "Pas de baisse de taux des gains réalisée par cet effet de calendrier ; aucun dépôt nouveau.",
                   "L'écart entre la valeur liquidative à l'ouverture et à la clôture de l'exercice constaté lors de cette évaluation est compris dans le résultat imposable de l'exercice concerné.",
                   "les règles générales de détermination des profits et pertes lors de leur réalisation")]),
    {T163: "Le 1° de 209-0 A renvoie au II ou au III bis de 163 quinquies B pour qualifier les FCPR/FPCI dispensés d'écarts sous conservation de cinq ans. La source et la proposition de la cible concernent l'IR des personnes physiques, son quota de 50 %, son indisponibilité et ses dérogations invalidité/décès/retraite/licenciement. L'abrogation de l'évaluation chez les entreprises ne supprime aucun de ces avantages ou conditions autonomes ni ne les réserve aux anciennes souscriptions. Les anciens écarts et ruptures restent traités par la transition ; aucune ancienneté de travail n'est importée.",
     T39: "Le deuxième alinéa du 2° de 209-0 A déroge à la provision du 5° du 1 de 39 pour les détentions indirectes, afin de ne pas déduire deux fois un écart négatif. L'abrogation supprime cette dérogation spéciale pour les exercices nouveaux, laisse jouer les conditions générales de provision de 39 et impose une neutralisation transitoire des anciennes non-déductions. Le 12 de 39 définit par ailleurs la dépendance mais n'est pas le renvoi de cet alinéa. Ni les congés payés ni les provisions de licenciement du long article 39 ne sont supprimés par cette mesure."},
    change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression de l'évaluation fiscale annuelle des OPC, de l'intégration des écarts, de leur état et annexe, des restrictions spéciales de provisions pour les nouveaux exercices et de la taxe accessoire sur les ruptures nouvelles de conservation.")

text = clean_xml(BY_NUMBER['209-0 B']['source_xml']).strip() + """
<p>VI. – Pour les exercices ouverts à compter de l'entrée en vigueur de la présente loi, le présent article demeure un régime distinct de détermination et d'imposition annuelle des bénéfices relevant de l'option au tonnage. Le passage de l'IS de droit commun à l'imposition à la distribution ne met pas fin à une option en cours, ne recommence pas sa période décennale et ne constitue pas, à lui seul, un événement visé aux IV ou V. Il ne prive pas une entreprise devenant éligible du droit d'opter dans les conditions du III.</p>
<p>Les bénéfices des opérations qui ne relèvent pas de cette option, notamment ceux mentionnés au dernier alinéa du II, suivent, lorsqu'ils en remplissent les conditions, le régime de distribution des V et VI de l'article 219. Leur détermination dans les conditions de droit commun ne déclenche pas un IS ordinaire avant distribution. Les charges et produits ne sont pas imputés deux fois entre le régime au tonnage et le régime de droit commun.</p>
<p>Les montants nets demeurant dans les capitaux propres qui correspondent aux bénéfices économiques tirés de l'exploitation ayant effectivement supporté l'imposition annuelle du présent article sont protégés d'un second IS lors de leur distribution, sans ajouter une seconde fois un montant déjà protégé. Les bénéfices conservés d'autres opérations qui n'ont pas supporté cette imposition ne sont pas protégés à ce titre. Les opérations et bénéfices exonérés en vertu d'autres dispositions conservent leur régime. Les dettes, créances, options, contrôles et recours des exercices antérieurs, ainsi que l'impôt minimum international dans son champ propre, demeurent régis par leurs dispositions applicables.</p>"""
add('209-0 B', text,
    "Coordination nécessaire du régime distinct au tonnage et de ses opérations hors option avec l'IS à la distribution. Le tableau entier, les conditions de pavillon et de groupe, les dérogations de 60 % et de moyenne sur trois exercices, l'option décennale, les sorties et leurs reprises sont maintenus. Il s'agit d'un régime favorable facultatif de transport maritime, dont les conditions peuvent relever de l'encadrement européen des aides : ni abolition indistincte ni suppression non documentée de ses garde-fous. Le VI évite à la fois une sortie forcée de l'option et un second IS sur les bénéfices de l'activité déjà imposée au tonnage.",
    "Tableau conservé : 0,93 / 0,71 / 0,47 / 0,24 euro par tranche de jauge nette de 100 UMS et par jour ; seuils 1 000 / 10 000 / 25 000 ; arrondi à la centaine supérieure et périodes d'indisponibilité maintenus. Ces montants sont une assiette forfaitaire et non des taux d'IS. Le renvoi au dernier alinéa du II vise exactement les bénéfices hors exploitation et leur ventilation d'intérêts. Les a et b du V restent applicables à leurs faits, sans inventer une clôture de l'option lors du changement de calendrier ordinaire. Les autorisations de location du code monétaire et financier ne sont pas une autorisation d'embauche. Les renvois à 223 A et 223 A bis nécessitent une coordination du périmètre dans les articles de groupe ; la proposition de 223 A ne doit pas étendre implicitement les reprises d'une option ancienne. Le nouveau renvoi à 219 V-VI n'est pas une cible du fichier : sa proposition a été lue dans le corpus. Le suivi de protection doit porter les bénéfices économiques déjà couverts par le tonnage, pas seulement l'assiette forfaitaire du barème. L'encadrement européen du tonnage et le minimum international restent à vérifier dans leurs textes propres, sans conformité présumée ni chiffrage d'aide.",
    "Le choix de l'assiette au tonnage, le barème intégral, les exceptions aux conséquences d'une baisse de pavillon européen, la possibilité d'option des nouvelles entreprises et lors d'une entrée en groupe, le renouvellement et les exceptions du V aux fusions/scissions/apports sont conservés. Aucun taux ni seuil favorable n'est relevé. La durée commerciale d'affrètement n'est pas celle d'un emploi. Le VI garantit la continuité des options et la protection des bénéfices déjà couverts par l'imposition au tonnage ; les bénéfices hors option bénéficient, dans leur champ, du calendrier de distribution.",
    impact('coordination_only',
           "L'assiette au tonnage et ses contraintes restent identiques ; la proposition sépare expressément l'annualité de ce régime et l'IS ordinaire différé des autres opérations.",
           "Aucune baisse du barème ni suppression de l'option décennale n'est démontrée ; l'encadrement européen, les groupes et les coûts du suivi commun restent à coordonner.",
           "Aucune obligation déclarative nouvelle propre à l'option n'est ajoutée. Le cloisonnement des résultats et la protection contre un second IS utilisent les comptes existants et le suivi commun de la réforme ; leur solde de coût n'est pas établi.",
           [effect('coordination', 'is-distribution',
                   "Réserver l'imposition annuelle au tonnage et conserver le nouveau calendrier pour les bénéfices hors option.",
                   "Bénéfices directement liés à l'exploitation forfaitisés ; autres bénéfices déterminés dans les conditions de droit commun.",
                   "Tonnage annuel maintenu ; les autres bénéfices éligibles ne déclenchent l'IS ordinaire qu'à leur distribution, sans double emploi.",
                   'regime', "Entreprises maritimes ayant opté et réalisant aussi des opérations hors option.",
                   "Nouveaux exercices ; aucune fin, réinitialisation ou fermeture des options antérieures du seul fait de la réforme.",
                   "Aucun nouveau formulaire ; ventilation et conditions de fond existantes maintenues.",
                   "Le bénéfice tiré des opérations qui ne sont pas directement liées à l'exploitation de navires éligibles est déterminé dans les conditions de droit commun.",
                   "Leur détermination dans les conditions de droit commun ne déclenche pas un IS ordinaire avant distribution.")]),
    {T223: "Les I, III et IV de 209-0 B utilisent le groupe de 223 A pour apprécier le pavillon et imposer l'option de tous les membres éligibles. La proposition 223 A transforme l'intégration en regroupement de paiement avec accord et notification avant le premier dépôt, effet au mois suivant, sans durée minimale. Cette simplification ne doit pas être lue comme une cessation de l'option décennale au tonnage ou un changement automatique de membres : le VI le précise pour le seul passage de régime. Les conditions de tonnage de toute entrée ou sortie réelle restent à appliquer, distinctement des règles d'ancienneté d'un salarié.",
     T39: "Les I, b et e, et II, a de 209-0 B renvoient précisément au 12 de 39 pour les entreprises liées : détention majoritaire ou pouvoir de décision, ou contrôle commun. Ils ne visent ni le 1° sur les rémunérations ni les provisions de licenciement. Cette définition demeure dans la proposition 39 et justifie de conserver les restrictions d'affrètement, d'acquisition et la majoration pour libéralités intragroupe sans les étendre aux contrats de travail. Aucun seuil d'un an ou préavis de quinze jours ne conditionne ici l'option."})

text = BY_NUMBER['209 B']['source_xml'].strip() + """
<p>V. – Pour les exercices ouverts à compter de l'entrée en vigueur de la présente loi, l'imposition prévue au I demeure une imposition anti-évasion distincte de l'IS ordinaire à la distribution. Elle reste établie au titre de l'exercice comprenant la date d'acquisition réputée fixée au 3 du I, même en l'absence de distribution, sous les exclusions et garanties des II et III et les imputations des 4 et 5 du I. Elle ne rend pas imposables annuellement les autres bénéfices conservés de la personne morale établie en France.</p>
<p>Les bénéfices ou revenus effectivement répartis qui correspondent à des montants déjà imposés en application du présent article ne sont pas soumis une seconde fois à l'impôt sur les sociétés à raison de cette répartition. Le montant net correspondant, demeuré dans les capitaux propres et disponible pour distribution, est protégé d'un second IS lors d'une distribution ultérieure par la personne morale établie en France selon le 1 du XI de l'article 209. Les impositions et imputations antérieures, les pertes ayant absorbé ces bénéfices et les montants déjà protégés sont pris en compte une seule fois ; la protection n'efface pas une dette d'impôt antérieure. Les produits non imposés en application des II ou III ne sont pas réputés avoir supporté un impôt du seul fait de ces exclusions et conservent les exonérations auxquelles ils ont droit par ailleurs.</p>
<p>Les exercices antérieurs, leurs impositions, crédits, restitutions, contrôles, prescriptions et recours demeurent régis par les dispositions qui leur étaient applicables. Le présent V ne modifie ni les conventions fiscales ni le champ et les modalités propres de l'impôt minimum international.</p>"""
add('209 B', text,
    "Coordination nécessaire de la règle anti-évasion sur les entités étrangères faiblement imposées avec le nouvel IS. La source entière est maintenue ; l'imposition réputée acquise après clôture reste une exception annuelle expressément identifiée, non un IS annuel rétabli sur tous bénéfices français conservés. Les exceptions pour l'Union européenne sans montage artificiel et pour les activités à objet principalement non fiscal sont conservées. Le V rend opératoire la protection contre une seconde imposition à la réception puis à la redistribution des montants déjà imposés.",
    "Seuil de plus de 50 %, abaissement à 5 % dans les cas définis, multiplication de la chaîne et exclusion des détentions a à d du pourcentage de résultat : tous maintenus. Le 3 du I vise le premier jour du mois suivant la clôture étrangère, et exclut les règles de calcul de groupe, non les quinze jours de préavis d'un salarié. Les crédits étrangers des 4 et 5 restent limités à leur objet et à la convention ; aucune créance remboursable nouvelle. La contrainte européenne des sociétés étrangères contrôlées, notamment les articles 7 et 8 de la directive (UE) 2016/1164, doit être coordonnée : son texte n'est pas fourni dans ce lot, et la présente rédaction ne présume pas que le nouveau système français la rend inutile ni qu'il satisfait automatiquement le minimum international. Le renvoi nouveau à 209 XI, non fourni comme cible, repose sur la proposition consultée dans le corpus. Les modalités du décret au IV doivent conserver les exclusions et éviter le double emploi sans ajouter une deuxième déclaration.",
    "Les exclusions des II et III, la présomption favorable d'activité industrielle ou commerciale effective, les crédits d'impôt local et de retenues conventionnelles des 4 et 5, et l'évitement de double imposition du IV sont préservés pour les situations futures recevables comme anciennes. Les distributions de montants déjà imposés ne subissent pas un second IS français. Les exclusions anti-abus ne deviennent pas un crédit d'impôt fictif sur une somme jamais taxée, et les autres exonérations applicables ne sont pas fermées.",
    impact('coordination_only',
           "Le dispositif anti-évasion reste annuel dans son champ exact ; le V clarifie cette exception et empêche la double imposition de bénéfices déjà couverts.",
           "Aucun impôt anti-évasion n'est supprimé ni taux diminué par cet article ; compatibilité conventionnelle et européenne et modalités réglementaires restent à coordonner.",
           "Aucune charge nouvelle n'est identifiée dans cet article : les contrôles, preuves d'activité et déclarations de la source restent ceux du régime existant. La protection contre le double IS utilise le suivi commun, sans état spécial ajouté.",
           [effect('coordination', 'is-distribution',
                   "Maintenir l'exception annuelle anti-évasion en la séparant de l'IS ordinaire des bénéfices conservés.",
                   "Les résultats étrangers relevant du I sont réputés acquis le premier jour du mois suivant leur clôture, sous les exceptions et imputations existantes.",
                   "Même imposition anti-évasion ; aucune annualité étendue aux autres bénéfices français, et même bénéfice protégé contre un second IS.",
                   'regime', "Personnes morales françaises relevant du I et leurs entreprises ou entités étrangères.",
                   "Coordination aux exercices ouverts à l'entrée en vigueur ; dettes, crédits et recours anciens conservés.",
                   "Aucune formalité de remplacement ; décret de double imposition à coordonner sans second dépôt.",
                   "Le bénéfice de l'entreprise ou le revenu de capitaux mobiliers mentionné au 1 est réputé acquis le premier jour du mois qui suit la clôture de l'exercice de l'entreprise ou de l'entité juridique établie ou constituée hors de France.",
                   "Elle ne rend pas imposables annuellement les autres bénéfices conservés de la personne morale établie en France.")]),
    {T223: "Le 3 du I de 209 B exclut 223 A et 223 A bis de la détermination du bénéfice étranger réputé acquis. La proposition de 223 A porte sur le regroupement français de déclaration/paiement et ne permet toujours pas de consolider le résultat de l'entité étrangère pour annuler l'assiette anti-évasion. Son accord, sa notification et l'effet au mois suivant ne remplacent pas la date d'acquisition du premier jour du mois suivant la clôture fixée par 209 B. Le V conserve cette imposition distincte et les crédits, sans transposer préavis ni condition d'ancienneté du contrat unique."})

text = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la présente loi. Aucune inscription, reprise ou reconstitution de la réserve spéciale des plus-values qu'il prévoit n'est exigée à compter de cette date. Aucun prélèvement sur cette réserve intervenant à compter de cette date, y compris sa distribution, son incorporation au capital ou son emploi à l'apurement de pertes, ne donne lieu au complément d'impôt sur les sociétés prévu au 2 du présent article.</p>
<p>Les sommes nettes d'impôt encore inscrites à cette réserve lors de l'entrée en vigueur de la présente loi sont définitivement libérées de ce complément. Pour leur montant demeuré dans les capitaux propres et disponible pour distribution, elles sont comprises dans le compte des bénéfices protégés d'un second IS prévu au 1 du XI de l'article 209. Une inscription déjà réalisée dans ce compte ne peut être renouvelée ; les distributions et pertes qui ont déjà absorbé ces sommes en sont déduites. Leur transfert à un autre poste de capitaux propres ne constitue pas un bénéfice nouveau imposable à l'IS ordinaire à la distribution. La fiscalité personnelle des bénéficiaires des distributions demeure régie par ses dispositions propres.</p>
<p>Les prélèvements intervenus avant l'entrée en vigueur de la présente loi demeurent régis par les dispositions antérieures, y compris la déduction de l'impôt perçu lors de la réalisation des plus-values, les exceptions de dissolution, d'incorporation au capital et d'imputation de pertes, et les dates propres à ces exceptions. Les pertes déjà annulées ne redeviennent pas reportables du fait de l'abrogation. Les dettes, créances, restitutions, prescriptions, contrôles et recours relatifs à ces prélèvements sont conservés, sans restitution générale d'un impôt légalement dû.</p>
<p>Aucun renvoi au présent article ne peut rétablir, pour l'avenir, l'obligation de réserve spéciale ou le complément d'impôt supprimés. Les autres réserves, provisions et obligations comptables ayant un fondement autonome demeurent régies par leurs dispositions propres.</p>"""
add('209 quater', text,
    "Abrogation de fond du complément d'IS frappant les prélèvements sur la réserve historique de plus-values, et de l'obligation de maintenir ou reprendre cette réserve. L'inscription avait déjà cessé pour les exercices ouverts à compter du 1er janvier 2004 : ce fait ancien n'est pas compté comme un gain nouveau. La réduction réelle est la liberté d'emploi future du stock encore présent sans le complément du 2, y compris lors d'une distribution, expressément protégée de l'IS de remplacement. Les prélèvements antérieurs restent régis par leurs droits et exceptions.",
    "Le 3 réserve la dissolution, les incorporations au capital avant le 1er janvier 2005 et les pertes imputées avant cette date ; ces traitements anciens sont préservés pour les prélèvements anciens, leurs dates n'étant pas reportées. Le nouveau texte étend la dispense de complément à tout emploi futur sans plafond, mais ne recrée pas les pertes annulées. L'article 210 A, 3, a et l'article 223 D, quatrième et cinquième alinéas, lus dans le corpus, appellent le retrait du seul maintien de cette réserve pour l'avenir ; leur fiscalité autonome et les provisions pour fluctuation des cours ne sont pas abrogées. Le nouveau renvoi à 209 XI, non fourni comme cible obligatoire, a été contrôlé dans le paragraphe proposé du corpus ; il faut rendre la libération définitive de la présente réserve opposable à son compte protégé. L'ancienne imputation du complément ne devient pas un crédit remboursable. Ni 209 quater D ni sa réserve distincte de profits de construction ne sont supprimés.",
    "Les exceptions de dissolution, d'incorporation au capital et de pertes sont intégralement conservées pour le stock de prélèvements antérieurs. Pour les emplois nouveaux, le complément correspondant est entièrement supprimé, sans IS de remplacement sur ces mêmes sommes : la dispense devient générale plutôt que moins favorable. L'impôt ancien payé au taux réduit n'est ni rappelé ni remboursé de façon générale. Les règles distinctes des pertes et l'impôt personnel des associés subsistent.",
    impact('material_reduction',
           "Le complément d'IS sur tout prélèvement nouveau de l'ancienne réserve disparaît définitivement ; le simple transfert du fait générateur à la distribution ne le remplace pas.",
           "La suppression ne porte ni sur l'IS réduit payé à l'origine ni sur l'impôt personnel des associés ; le montant dépend des réserves restantes et n'est pas chiffré.",
           "Aucune charge nouvelle autonome n'est identifiée : la réserve spéciale est libérée sans demande, agrément ou déclaration de remplacement. Son inscription unique au compte protégé de la réforme prévient le double impôt et le double emploi.",
           [effect('tax_removed', 'reserve-plus-values-complement-is-suppression',
                   "Supprimer le complément d'IS lors des prélèvements sur la réserve historique de plus-values.",
                   "Sommes prélevées rapportées au résultat imposable : taux normal de 25 % de 219 I, ou 15 % dans la tranche PME de 42 500 euros par douze mois si les conditions de 219 I b sont remplies, sous déduction de l'impôt perçu lors de la réalisation des plus-values et exceptions du 3 de 209 quater ; ce dernier article ne fixe pas de taux autonome.",
                   "Aucun complément d'IS ni second IS de distribution sur les sommes nettes encore présentes, sous suivi unique du stock ; fiscalité personnelle distincte maintenue.",
                   'other', "Sociétés détenant encore la réserve de plus-values relevant de 209 quater, y compris les sociétés mères concernées.",
                   "Prélèvements à compter de l'entrée en vigueur ; prélèvements anciens et avantages correspondants conservés sans remboursement général.",
                   "Pas de prélèvement équivalent ni déclaration de remplacement ; protection simple contre la double utilisation du stock.",
                   "Les sommes prélevées sur cette réserve sont rapportées aux résultats de l'exercice en cours lors de ce prélèvement, sous déduction de l'impôt perçu lors de la réalisation des plus-values correspondantes.",
                   "Aucun prélèvement sur cette réserve intervenant à compter de cette date, y compris sa distribution, son incorporation au capital ou son emploi à l'apurement de pertes, ne donne lieu au complément d'impôt sur les sociétés prévu au 2 du présent article.")]),
    change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression pour tous les prélèvements futurs du complément d'impôt frappant la réserve spéciale de plus-values et libération de l'obligation de maintenir, reprendre ou reconstituer cette réserve historique, sans second IS de remplacement.")

text = BY_NUMBER['209 quater D']['source_xml'].strip() + """
<p>Pour les exercices relevant des V et VI de l'article 219, les bénéfices encore soumis à l'exonération sous condition de remploi du premier alinéa conservent ce régime jusqu'à leur distribution, sans imposition ordinaire du seul fait de leur conservation en trésorerie. À leur distribution, les fractions de moitié ou de 30 % prévues au présent article restent applicables lorsque leurs délais et conditions sont remplis. Elles déterminent la fraction d'assiette du compartiment correspondant pour l'application du XI de l'article 209 et du 4 du V de l'article 219, sans double déduction ni double inscription.</p>
<p>Le bénéfice de ces fractions d'assiette demeure attaché aux profits éligibles dans leur champ historique ; la présente coordination ne rouvre pas le régime de remploi pour des profits qui en sont exclus. Une somme définitivement exonérée ou déjà imposée n'est pas imposée une seconde fois à raison de la distribution. Les impositions, créances, exonérations, prescriptions et recours relatifs aux distributions des exercices antérieurs restent régis par les dispositions qui leur étaient applicables.</p>"""
add('209 quater D', text,
    "Coordination nécessaire d'un régime déjà déclenché à la distribution avec la nouvelle liquidation de l'IS. Les fractions favorables d'assiette de 50 % et 30 %, leurs délais et le renvoi réglementaire restent intégralement maintenus. Le complément distingue le calcul d'assiette du taux de 20 % et empêche qu'une distribution tardive perde l'ancien avantage ou qu'un bénéfice conditionnel soit réputé déjà définitivement exonéré. Aucun délai nouveau ni nouvelle condition d'investissement n'est ajouté.",
    "L'article 238 octies et l'annexe III 46 quater-0 R ont été lus intégralement dans le corpus. Le régime est fermé aux profits réalisés à compter du 1er janvier 1972 ; le règlement compte les quatre et sept ans de clôture à clôture et exige le remploi préalable. Il ne s'agit pas d'un délai de quatre ou sept ans nouvellement imposé à toute entreprise. Les mots source « plus de quatre ans mais moins de sept ans » sont conservés : aucune réécriture silencieuse de la borne exacte de quatre ans. Le renvoi à l'article 95 de la loi de finances pour 2004 figurant dans le règlement doit être vérifié dans son champ historique ; il n'est pas reproduit comme prélèvement nouveau. Les renvois ajoutés à 209 XI et 219 V, 4 ne sont pas fournis comme cibles : les paragraphes proposés pertinents ont été consultés dans le corpus. Leur formule doit appliquer q égal à 0,50 ou 0,30 au bénéfice avant IS et non transformer ces fractions en taux d'impôt. Le décret et la note (1) sont conservés, sans inventer un état supplémentaire.",
    "L'imposition différée jusqu'à la distribution, la base réduite à moitié au-delà de quatre ans et avant sept ans, puis à 30 % à partir de sept ans, sont conservées pour toutes distributions futures des profits historiques recevables. Le remploi conditionnel n'est pas confondu avec une exonération définitive. Les dates anciennes de réalisation et d'exercice restent celles du régime, sans réouverture artificielle aux nouveaux profits ni fermeture des distributions futures éligibles.",
    impact('coordination_only',
           "Le calendrier de distribution existait déjà ; seul son raccordement à la nouvelle assiette d'IS est rédigé, sans revendiquer une seconde réduction de 50 % ou 70 %.",
           "Les profits postérieurs au 1er janvier 1972 restent hors de ce régime historique ; le règlement et ses prélèvements anciens appellent un contrôle distinct.",
           "Aucune charge nouvelle n'est identifiée : ni délai supplémentaire, ni condition de remploi nouvelle, ni état spécial ne remplace les conditions existantes ; le compartiment est celui du suivi commun.",
           [effect('coordination', 'is-distribution',
                   "Conserver les fractions favorables de l'assiette historique au sein de la nouvelle liquidation à la distribution.",
                   "Bénéfices sous remploi imposés lors de leur distribution, base de moitié après plus de quatre et moins de sept ans, base de 30 % dès sept ans.",
                   "Mêmes fractions et délais ; rattachement à l'assiette avant IS du compartiment, sans les transformer en taux ni retaxer une somme déjà protégée.",
                   'regime', "Sociétés distribuant des profits historiques éligibles au remploi de 238 octies.",
                   "Exercices du nouveau régime ; profits historiques seuls, distributions antérieures sous leur droit.",
                   "Aucune condition ou déclaration supplémentaire ; suivi unique de l'assiette commune.",
                   "Pour 30 % de leur montant, lorsque cette distribution intervient sept ans au moins après leur réalisation.",
                   "À leur distribution, les fractions de moitié ou de 30 % prévues au présent article restent applicables lorsque leurs délais et conditions sont remplis.")]))

add('210', None,
    "Maintien intégral d'une exonération historique de fusions et d'apports. Le texte garantit encore la continuité des valeurs et la conservation des avantages de profits anciens ; sa suppression pourrait entraîner une imposition ou perdre des modalités favorables. L'agrément préalable du 2, 2°, b porte sur l'opération ancienne ayant ouvert l'avantage, non sur une nouvelle demande périodique ou une autorisation future créée par cet article. Aucun allègement réel ne résulterait de la simple suppression lexicale de cette condition historique.",
    "Lecture des 1 à 4, des exceptions avant 1950 et des deux renvois à 238 octies. Les trois quarts de superficie et la fermeture aux profits réalisés à compter du 1er janvier 1972 ressortent du texte de 238 octies et de l'annexe III 46 quater-0 R lus dans le corpus. La première phrase de 210 réserve les plus-values antérieures à l'entrée des articles 39 duodecies à 39 quindecies A ; le 4 vise aussi les plus-values du I de 238 octies. Ne pas attribuer les dates de 1950 ou 1972 à une réforme future. Les conditions territoriales, la simultanéité des conventions, la dissolution immédiate et les valeurs de continuité sont maintenues pour l'analyse des opérations historiques. Les bénéfices définitivement exonérés sont déjà protégés par le XI de 209 proposé ; les valeurs fiscales et reports conditionnels ne sont pas effacés. Aucun agrément de 210 B, 210 C ou de droit européen n'est supprimé par inférence.",
    "L'exonération des plus-values de fusion, l'extension aux scissions et apports partiels répondant aux conditions, les assimilations territoriales et l'exception de continuité des amortissements pour les opérations antérieures à 1950 agréées sont conservées. Les obligations de reprise des provisions et de calcul au prix fiscal évitent le double bénéfice ; elles ne justifient pas un second IS sur une exonération définitive. Les effets futurs recevables des opérations et profits historiques restent protégés, sans réserver ces effets à une réclamation antérieure à la réforme.",
    impact('retained_necessary',
           "L'exonération historique, ses extensions et ses règles de continuité sont maintenues intégralement ; aucun agrément actuel ni taxe nouvelle supprimée n'est compté.",
           "Les dates anciennes et agréments constitutifs des situations passées ne sont pas réouverts ; les régimes contemporains de 210 A à C restent distincts.",
           "Aucune charge nouvelle n'est identifiée : l'article est conservé avec ses conditions historiques, sans demande périodique, dossier ni délai supplémentaire."))

source = BY_NUMBER['210-0 A']['source_xml']
start = source.index('IV. – Lorsque')
# Preserve the complete I-III, including the paragraph breaks within the III.
text = source[:start] + """IV. – La déclaration spéciale relative aux motifs et conséquences d'une fusion, d'une scission ou d'un apport partiel d'actif placé sous le régime de l'article 210 A et réalisé au profit d'une personne morale étrangère n'est plus exigée pour les opérations réalisées à compter de l'entrée en vigueur de la présente loi. Son absence ne peut entraîner ni amende ni perte du régime fiscal de l'opération. Aucun agrément, attestation, dépôt ou déclaration propre à cette obligation supprimée ne la remplace.</p>
<p>Les conditions de fond, exclusions et garanties des I à III demeurent applicables, notamment le contrôle contradictoire de la fraude ou de l'évasion fiscales. Les obligations comptables, fiscales et de communication ayant un fondement autonome restent applicables ; les pouvoirs de contrôle de l'administration ne permettent pas de rétablir une déclaration spéciale systématique des mêmes opérations sur le seul fondement du présent IV.</p>
<p>Les opérations réalisées avant l'entrée en vigueur de la présente loi restent soumises aux règles déclaratives qui leur étaient applicables, même si leur échéance est postérieure, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives dans son champ légal. Les droits au régime favorable, les dettes, créances, restitutions, prescriptions et recours relatifs à ces opérations sont conservés.</p>
<p>V. – Pour les exercices relevant des V et VI de l'article 219, l'application des régimes visés aux I à III conserve leurs définitions, conditions et avantages sans déclencher, du seul fait de la réalisation d'un résultat de référence ou d'une opération fiscalement neutre, un IS ordinaire sur des bénéfices conservés. Les opérations sont suivies selon leurs dispositions propres et les comptes de l'article 209 ; une même réserve, perte ou créance ne peut être transmise ou utilisée deux fois. Les impositions de sortie et l'impôt minimum international restent régis par leurs dispositions propres.</p>"""
add('210-0 A', text,
    "Réduction de fond : suppression de la déclaration électronique spéciale imposée à chaque opération relevant de 210 A au profit d'une personne morale étrangère, sans déclaration ou agrément de remplacement. Les définitions complètes des opérations, la soulte de 10 %, les quatre catégories du I, l'exclusion internationale du II et les garanties anti-fraude du III restent intégralement maintenues. Le V est une coordination de l'IS à la distribution : la neutralité et les résultats de référence ne recréent pas l'ancienne annualité. Les déclarations fiscales générales ne sont pas supprimées par le retrait de ce seul formulaire.",
    "L'annexe III 46 quater-0 ZS ter a été lue, source et proposition : ses trois rubriques exécutent exclusivement l'ancien IV et doivent être supprimées pour les mêmes opérations nouvelles. L'article 1760 bis a été lu : l'amende spéciale de 10 000 euros doit être abrogée dans ce même champ, sous la réserve de loi plus douce ; le nouveau IV écarte déjà toute amende fondée sur l'obligation supprimée. Ces textes hors du lot ne sont pas présentés comme réécrits. Maintien du 3° du I étendu en 2025 aux associés de mêmes proportions et du 4° sur les apports sans dissolution ; la note d'application de l'ordonnance du 24 mai 2023 demeure à sa portée exacte. L'article 38, 7 bis vise le report d'échange, et non une dispense de toutes règles d'assiette. La directive 2009/133/CE citée au II et les contrôles distincts des opérations transfrontières demeurent ; la suppression nationale d'un formulaire ne vaut pas suppression d'une contrainte européenne ni conformité générale établie. Les renvois nouveaux à 209 et 219 sont signalés comme non fournis en cibles ; leurs paragraphes proposés pertinents ont été consultés dans le corpus. Le bénéfice des anciens régimes, déficits et créances n'est pas créé deux fois par une réorganisation.",
    "Les régimes favorables des fusions, scissions, opérations sans échange et apports de branches complètes restent accessibles à toutes les opérations futures éligibles, y compris transfrontières recevables. Le plafond de soulte, les catégories de détenteurs dispensés d'échange et l'assistance administrative sont inchangés ; le contradictoire et la preuve contraire du III sont préservés. La suppression du seul formulaire retire un obstacle et son amende propre sans faire disparaître les avantages, sans nouvelle autorisation ni condition documentaire équivalente. Les opérations anciennes conservent droits et recours.",
    impact('material_reduction',
           "Le dépôt spécial et son modèle obligatoire sont effectivement retirés pour les opérations nouvelles ; définitions, avantages et contrôle anti-abus restent entiers. La coordination d'IS n'est pas une seconde réduction.",
           "Déclarations générales, comptabilité, dispositifs transfrontaliers autonomes et droit de l'Union subsistent ; 1760 bis et l'annexe d'exécution doivent encore être coordonnés hors du lot. Aucun solde global n'est chiffré.",
           "Aucune charge nouvelle n'est identifiée : le formulaire supprimé n'est remplacé ni par déclaration, ni par agrément, ni par attestation. Les conditions de fond et la communication légalement fondée restent celles déjà applicables.",
           [effect('obligation_removed', 'fusions-transfrontieres-declaration-speciale-suppression',
                   "Supprimer le formulaire électronique spécial des réorganisations au profit d'une personne morale étrangère.",
                   "Chaque apporteuse dépose une déclaration spéciale électronique au modèle administratif, dans le délai de sa déclaration de résultat de l'exercice de l'opération.",
                   "Aucun dépôt spécial ni modèle obligatoire pour les opérations nouvelles ; aucune amende ou perte du régime pour son absence, sans remplacement équivalent.",
                   'legal_duty', "Sociétés apporteuses réalisant au profit d'une personne morale étrangère une opération placée sous 210 A.",
                   "Opérations à compter de l'entrée en vigueur ; opérations anciennes sous leur droit, sous réserve de loi répressive plus douce.",
                   "Aucun agrément, attestation ou déclaration substitué ; comptabilité et contrôles autonomes préservés.",
                   "la société apporteuse est tenue de souscrire, par voie électronique, dans le même délai que sa déclaration de résultat de l'exercice au cours duquel l'opération a été réalisée, une déclaration spéciale, conforme à un modèle établi par l'administration, permettant d'apprécier les motifs et conséquences de cette opération.",
                   "Aucun agrément, attestation, dépôt ou déclaration propre à cette obligation supprimée ne la remplace."),
            effect('coordination', 'is-distribution',
                   "Maintenir les définitions et neutralités des opérations pour la liquidation nouvelle de l'IS.",
                   "Les régimes énumérés s'appliquent aux opérations définies, sous exclusions internationales et clause anti-abus.",
                   "Mêmes définitions et conditions ; résultat de référence ou opération neutre ne déclenche pas seul l'IS ordinaire sur bénéfices conservés.",
                   'regime', "Sociétés relevant des régimes de restructuration énumérés aux I à III.",
                   "Exercices du nouveau régime de distribution ; opérations anciennes sous leurs garanties propres.",
                   "Pas de dossier supplémentaire ; comptes communs avec interdiction de double emploi.",
                   "aux opérations par lesquelles une société apporte, sans être dissoute, l'ensemble ou une ou plusieurs branches complètes de son activité",
                   "l'application des régimes visés aux I à III conserve leurs définitions, conditions et avantages")]),
    {T223: "Le I et le III de 210-0 A incluent les articles 223 A à U dans les opérations admissibles et dans l'exclusion anti-fraude. La proposition 223 A porte désormais sur le regroupement de paiement, ses accords et sa notification ; elle réserve les anciens déficits et neutralisations et exclut leur double emploi. Le V de 210-0 A empêche que cette plage rétablisse une annualité ordinaire ou qu'une fusion soit tenue pour une distribution par elle-même. Les nouvelles formalités de désignation du groupe ne sont ni la déclaration spéciale du IV supprimée ni une condition d'ancienneté de travail.",
     T38: "Le renvoi de 210-0 A au 7 bis de 38 vise le report du profit d'échange de droits sociaux lors d'une fusion/scission, le calcul au prix fiscal et la soulte de 10 %, non toutes les règles annuelles de 38. Le 12 de la proposition de 38 réserve justement l'exigibilité de l'IS à 209/219 et conserve les valeurs et reports sans double emploi. Les I à III de 210-0 A restent entiers et le V coordonne cette lecture ; l'IR des entreprises qui y restent soumises et les anciens reports ne sont pas effacés. Aucun terme d'emploi ni notification de rupture n'est créé."},
    change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=["Suppression de la déclaration spéciale électronique et de son modèle obligatoire pour les opérations nouvelles de fusion, scission ou apport partiel d'actif réalisées sous 210 A au profit d'une personne morale étrangère.",
                        "Retrait de l'habilitation réglementaire du IV à prescrire le contenu de cette déclaration supprimée et impossibilité de subordonner le régime favorable ou une amende au dépôt de ce seul formulaire pour les opérations nouvelles."])


def verify():
    assert len(ANSWERS) == len(SOURCES) == 13
    assert [a['number'] for a in ANSWERS] == [a['number'] for a in SOURCES]
    allowed = {'p', 'br', 'table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td', 'b', 'strong',
               'i', 'em', 'u', 'sup', 'sub', 'ul', 'ol', 'li', 'div', 'span', 'blockquote'}
    from html.parser import HTMLParser

    class Audit(HTMLParser):
        def handle_starttag(self, tag, attrs):
            assert tag in allowed, tag
            assert all(k in {'rowspan', 'colspan'} and (v or '').isdigit() for k, v in attrs), attrs

    for a, s in zip(ANSWERS, SOURCES):
        assert all(a[k] == s[k] for k in ('code_id', 'source_id', 'number', 'source_sha256'))
        assert len(a['benefit_review']) >= 100
        si = a['substantive_impact']
        assert si['version'] == 1
        for k in ('assessment', 'scope_limitations', 'new_burdens_review'):
            assert len(si[k]) >= 40, (a['number'], k)
        if a['proposed_xml'] is None:
            assert a['status'] == 'retained_unchanged'
            assert a['classification'] == si['classification'] == 'retained_necessary'
            assert si['effects'] == []
        else:
            Audit().feed(a['proposed_xml'])
        if a.get('change_type') == 'full_repeal':
            assert plain(a['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
            assert len(a['repeal_scope']) >= 30
        for removed in a.get('removed_provisions', []):
            assert len(removed) >= 30
        for c in a['reference_checks']:
            assert len(c['assessment']) >= 80
        for e in si['effects']:
            assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', e['measure_id'])
            assert 6 <= len(e['measure_id']) <= 96
            for q, field in [('source_quote', s['source_xml']), ('proposed_quote', a['proposed_xml'])]:
                assert len(e[q]) >= 12
                assert e[q] in plain(field), (a['number'], q, e[q])
    Path('answer.json').write_text(json.dumps(ANSWERS, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'output_file': 'answer.json', 'article_count': len(ANSWERS)}, ensure_ascii=False))


if __name__ == '__main__':
    verify()
