"""Full proposals for the distribution-tax coordination, separate from sources."""
from pathlib import Path
import json,html,hashlib,sqlite3,sys,re

ROOT=Path(__file__).resolve().parents[2]
SOURCES=json.loads((Path(__file__).parent/'sources.json').read_text())
SOURCES+=json.loads((Path(__file__).parent/'annexe-2-sources.json').read_text())
BY={a['number']:a for a in SOURCES}
ROWS=[]
POLICY='editorial_direction_2026_10_19'

def clean(value):
    value=re.sub(r'(?<=[A-Za-zÀ-ÿ])(?=\d)|(?<=\d)(?=[A-Za-zÀ-ÿ])',' ',value)
    value=re.sub(r'\b(articles?)(?=[A-Z])',r'\1 ',value)
    value=re.sub(r'\b(quater|ter|bis|quinquies|sexies|septies|octies|nonies|decies|undecies|duodecies|terdecies|quaterdecies|quindecies|sexdecies|septdecies)(?=[A-Z])',r'\1 ',value)
    value=re.sub(r'(?<=[A-Z])(?=bis\b|ter\b|quater\b|quinquies\b|sexies\b|septies\b|octies\b|nonies\b)',' ',value)
    value=re.sub(r'\b([LRDA])\.(?=\d)',r'\1. ',value)
    value=re.sub(r'\b(du|au|des|les|de)(?=XI\b|XII\b|XIII\b|IV\b|VI\b|III\b)',r'\1 ',value)
    value=re.sub(r'(?<=\d)%',' %',value)
    value=re.sub(r'([,;:])(?=\S)',r'\1 ',value)
    value=re.sub(r'(?<=[a-zÀ-ÿ])\.(?=[A-Z0-9])','. ',value)
    value=re.sub(r'\b(\d+) er\b',r'\1er',value)
    value=re.sub(r'\bn°(?=\d)','n° ',value)
    for old,new in {
        'catégoriesa':'catégories a','àzquinquies':'à z quinquies',
        'CAconsolidé':'chiffre d’affaires consolidé ',
        'dérogationarticle':'dérogation de l’article',
        'directive(UE)':'directive (UE) ',
        'XMLDILA':'XML DILA',
        'annexeII':'annexe II','annexeIII':'annexe III',
        'bénéficiaireFrance':'bénéficiaire établi en France',
        'décembreannée':'décembre de l’année',
        'auprincipal':'au principal',
        'nouvelIS':'nouvel IS',
        'centralechezlamère':'central chez la mère',
    }.items():value=value.replace(old,new)
    return value

def clean_meta(value):
    return ''.join(piece if piece.startswith(('https://','http://')) else clean(piece) for piece in re.split(r'(https?://\S+)',value))

def paragraphs_html(paragraphs):
    return '\n'.join('<p>'+html.escape(clean(p),quote=False)+'</p>' for p in paragraphs)

def add(number,paragraphs,reason,review,removed=None):
    a=BY[number]
    row={k:a[k] for k in ('code_id','source_id','source_sha256','number')}
    row.update(status='rewrite_draft',proposed_xml=paragraphs_html(paragraphs),reason=clean_meta(reason),review_notes=clean_meta(review))
    if removed:
        row.update(change_type='normative_reduction',reform_policy_id=POLICY,removed_provisions=removed)
    ROWS.append(row)

def from_prior(number,body,reason,review):
    a=BY[number]
    row={k:a[k] for k in ('code_id','source_id','source_sha256','number')}
    row.update(status='rewrite_draft',proposed_xml=body,reason=clean_meta(reason),review_notes=clean_meta(review))
    ROWS.append(row)

add('109',[
    'I. Pour l’imposition des bénéficiaires, sont des revenus distribués :',
    '1° Les bénéfices ou produits effectivement attribués aux associés, actionnaires ou porteurs de parts, en argent ou en nature, au lieu d’être conservés dans la société ;',
    '2° Les autres sommes ou valeurs mises à leur disposition, directement ou par personne interposée, sous réserve des exclusions de l’article 112.',
    'La conservation de bénéfices en réserve, en report à nouveau, en trésorerie ou dans des actifs professionnels ne constitue pas une distribution. L’absence d’une affectation formelle du résultat ne suffit pas à établir une mise à disposition. La distribution est rattachée à la date à laquelle le bénéficiaire dispose effectivement et sans condition des sommes ou valeurs.',
    'Les sommes distribuées sont établies à partir des comptes, des décisions d’attribution et des mouvements de valeurs. Une variation des bilans peut servir à démontrer une distribution dissimulée ; elle ne crée pas, à elle seule, une distribution de bénéfices restés dans la société.',
    'II. L’impôt sur les sociétés dû par la société qui distribue est établi dans les conditions des articles 209 et 219. Sa base est distincte du revenu imposable du bénéficiaire. Le paiement de cet impôt ne dispense ni du prélèvement prévu à l’article 117 quater, ni de la retenue prévue à l’article 119 bis, ni des autres impositions personnelles légalement applicables.',
    'III. Les règles du présent article relatives au nouveau fait générateur s’appliquent pendant les exercices ouverts à compter de l’entrée en vigueur de la loi qui les institue. Les distributions et impositions afférentes aux exercices antérieurs demeurent régies par les dispositions alors applicables.'
],
    'Remplacer la présomption annuelle de distribution par la mise à disposition effective ; distinguer l’IS de distribution et l’impôt personnel des associés.',
    'Source et précédent projet lus en entier. L’ancienne comparaison des bilans n’est plus un fait générateur autonome. Les articles40,41,42,44,45,46 et47 de l’annexeII sont réécrits dans le présent lot pour supprimer leurs présomptions automatiques contraires ; l’article43 est absent de l’inventaire officiel courant. Le prélèvement personnel et les retenues conventionnelles sont maintenus.',
    ['Suppression de la distribution déduite mécaniquement du seul défaut de mise en réserve formelle et de la comparaison annuelle des bilans.'])

add('110',[
    'Pour l’application du 1° du I de l’article 109, les bénéfices distribuables s’entendent du résultat net réellement dégagé et des réserves disponibles, déterminés à partir des comptes et rectifiés des sommes ou avantages non comptabilisés qui ont été attribués aux bénéficiaires.',
    'Ils comprennent les bénéfices légalement exonérés, les produits de participations bénéficiant de l’article 216 et les bénéfices réalisés dans les entreprises exploitées hors de France. L’impôt sur les sociétés effectivement supporté par la société et les impôts sur les bénéfices étrangers effectivement supportés sont retranchés seulement dans la mesure où ils n’ont pas déjà été déduits du résultat, des réserves ou du montant attribué au bénéficiaire. Un même impôt ne peut ainsi diminuer deux fois le revenu distribué ; un impôt dont le paiement est seulement différé n’est pas réputé acquitté.',
    'Le revenu du bénéficiaire correspond à la somme ou à la valeur nette de l’impôt de la société qui lui est effectivement attribuée. L’impôt personnel retenu ou prélevé pour le compte de ce bénéficiaire ne diminue pas ce revenu brut.',
    'L’inscription d’un bénéfice au compte des bénéfices protégés d’un second IS prévu au 1 du XI de l’article 209 n’exonère pas le revenu du bénéficiaire lorsqu’il est distribué. Un même montant ne peut être déduit deux fois.'
],
    'Détacher le revenu distribué de l’ancienne assiette annuelle de l’IS et conserver l’impôt personnel sur le dividende effectivement reçu.',
    'Le montant net après impôt de la société ne doit pas être confondu avec le net après prélèvements de l’associé. Le crédit d’un impôt de société fictif est exclu ; bénéfices exonérés et étrangers restent distribuables et imposables personnellement selon leurs règles propres.')

add('111',[
    'Sont notamment considérés comme revenus distribués :',
    'a. Sauf preuve contraire, les sommes mises à la disposition des associés à titre d’avances, de prêts ou d’acomptes, directement ou par des personnes ou sociétés interposées. La présomption est écartée lorsque la société démontre une opération réelle de crédit, conclue dans son intérêt à des conditions normales, assortie d’une obligation effective de remboursement et exécutée conformément à cette obligation. Le seul intitulé de prêt ou d’avance ne suffit pas à écarter une distribution.',
    'Lorsqu’une somme ainsi imposée est effectivement remboursée à la personne morale qui l’avait versée, le bénéficiaire ou son ayant cause obtient la restitution de la fraction des impositions personnelles correspondant au remboursement. La demande mentionne l’imposition initiale, le montant et la date du remboursement. Elle est accompagnée des justificatifs de paiement ; aucun nouveau prêt ou jeu d’écritures sans remboursement réel n’ouvre droit à restitution. Les modalités procédurales prévues aux articles 49 bis à 49 sexies de l’annexe III demeurent applicables dans la mesure où elles ne réduisent pas ce droit.',
    'b. Les sommes ou valeurs attribuées aux porteurs de parts bénéficiaires ou de fondateur pour le rachat de ces parts ;',
    'c. Les rémunérations et avantages occultes ;',
    'd. La fraction des rémunérations non déductible en application du 1° du 1 de l’article 39 ;',
    'e. Les dépenses et charges dont le premier alinéa et le 3° du 4 de l’article 39 interdisent la déduction, dans la mesure où elles procurent un avantage privé à un associé, à un dirigeant ou à une personne qui leur est liée.',
    'Pour l’impôt dû par la société en application du V de l’article 219, constituent une distribution les sommes et avantages définitivement prélevés sur ses ressources au bénéfice privé de ces personnes. Une dépense professionnelle réelle, un salaire normal, l’achat d’un bien, une prestation réelle ou un financement conforme au premier alinéa du a n’est pas une distribution du seul fait qu’il entraîne une sortie d’argent. L’avantage privé est évalué à sa valeur normale, diminuée de la contrepartie réelle reçue par la société.',
    'Le remboursement réel d’une avance précédemment soumise à l’IS de distribution ouvre une correction de cet impôt à hauteur de la seule somme remboursée et de l’impôt effectivement acquitté sur elle, dans les conditions de l’article 1668. Il ne constitue ni un nouvel apport ni un nouveau crédit au compte des bénéfices protégés d’un second IS.',
    'Ces règles de l’IS de distribution s’appliquent pendant les exercices ouverts à compter de l’entrée en vigueur de la loi qui les institue ; elles ne rouvrent pas les impositions antérieures.'
],
    'Conserver une règle ciblée contre les distributions déguisées, avec preuve contraire pour les vrais prêts et neutralité des dépenses professionnelles réelles.',
    'Les catégories a à e et le renvoi au premier alinéa du a demeurent identifiables pour 119 bis. La restitution personnelle préexistante est séparée de la correction d’IS nouveau : aucun crédit ni double compte ne naît du remboursement. Le caractère privé est ajouté au e pour éviter d’assimiler toute charge professionnelle non déductible à un dividende.',
    ['Suppression de l’assimilation automatique de toute dépense non déductible de la catégorie e à une distribution, sans preuve d’un avantage privé.'])

add('111 bis',[
    'Lorsqu’une personne morale cesse d’être assujettie à l’impôt sur les sociétés, ses bénéfices et réserves, qu’ils aient ou non été incorporés au capital, sont réputés distribués aux associés en proportion de leurs droits. Si une fraction seulement des résultats cesse d’être assujettie, la règle s’applique à cette seule fraction.',
    'Cette règle ne s’applique pas aux sociétés admises au régime de l’article 208 C ni aux sociétés soumises à l’impôt sur les sociétés qui se transforment en sociétés de placement à prépondérance immobilière à capital variable mentionnées au 3° nonies de l’article 208.',
    'La seule substitution de l’imposition à la distribution à l’imposition annuelle des bénéfices, prévue aux articles 209 et 219, ne constitue pas une cessation d’assujettissement. La conservation d’un bénéfice dans la société pendant cette transition ne vaut donc pas distribution aux associés.',
    'L’impôt éventuellement dû par la société à l’occasion d’une cessation, d’un transfert ou d’une liquidation est calculé selon les articles 209, 219, 221 et 221 bis, en respectant les bénéfices protégés d’un second IS. Cette protection ne supprime pas l’imposition personnelle de la distribution réelle ou réputée réalisée.'
],
    'Empêcher que l’entrée dans le régime à la distribution déclenche elle-même l’imposition de toutes les réserves.',
    'Maintien des exclusions SIIC et SPPICAV et de l’assimilation personnelle en cas de vraie sortie d’assujettissement. La note source rendait le texte antérieur applicable aux exercices ouverts depuis le 1er janvier 2008 ; elle ne fixe pas la date de la réforme nouvelle.')

add('111 ter',[
    'La transformation en société d’investissement à capital variable d’une société qui n’était pas exonérée d’impôt sur les sociétés produit, pour les associés, les mêmes conséquences fiscales que la répartition de son boni de liquidation.',
    'L’impôt dû par la société à raison de cette transformation est établi dans les conditions des articles 209, 219 et 221. Les bénéfices dont la société justifie qu’ils sont protégés d’un second IS ne sont pas soumis une seconde fois à cet impôt ; les règles d’imposition des associés demeurent applicables.',
    'Le passage au seul régime d’IS à la distribution sans changement de forme sociale ni sortie d’assujettissement n’est pas une transformation au sens du présent article.'
],
    'Coordonner la transformation en SICAV avec la protection des réserves déjà taxées, sans exonérer le boni des associés.',
    'La conséquence personnelle existante est préservée ; le changement du fait générateur de l’IS n’est pas assimilé à une transformation.')

prior=BY['112']['proposed_xml']
from_prior('112',prior+'\n'+''.join('<p>'+html.escape(p,quote=False)+'</p>\n' for p in [
    'Pour l’application du V de l’article 219 à la société qui attribue les sommes ou valeurs, le présent article ne crée pas d’exonération distincte de celles des articles 209 et 219. Le rachat de titres mentionné au 6° peut constituer une distribution imposable à la société pour la fraction qui excède les apports réellement reçus et non encore remboursés attachés aux titres annulés ; il demeure soumis, pour l’associé, au régime des plus-values prévu au même 6°.',
    'Les réserves incorporées au capital et les primes de fusion, de scission ou d’apport qui ne correspondent pas à un apport extérieur réel ne deviennent pas, du fait de leur inscription comptable, des apports remboursables en franchise d’IS. Leur origine et, le cas échéant, leur protection d’un second IS demeurent suivies dans les comptes prévus au XI de l’article 209.',
    'Les salaires, intérêts, prix d’achats et rémunérations de services réels versés dans l’intérêt de l’exploitation, à des conditions normales, ne sont pas soumis à l’IS de distribution du seul fait de leur versement. Les avantages privés et opérations fictives restent régis par l’article 111.',
    'Ces coordinations de l’IS de distribution concernent les exercices ouverts à compter de l’entrée en vigueur de la loi qui les institue ; les exclusions personnelles prévues aux 1° à 8° ne sont pas supprimées.'
]),
    'Préserver le régime des associés, tout en empêchant de convertir un bénéfice non encore taxé en remboursement de capital ou rachat de titres exonéré côté société.',
    'Le précédent projet complet, qui reformulait les 1° à 8° de la source, est conservé et coordonné. Les références 1949, l’exclusion des vraies rémunérations, le régime des plus-values du 6° et les opérations de 2025 restent présents. Les notes QPC et transitions de la source restent à apprécier pour les opérations anciennes, sans abroger silencieusement la version 2025. Le calcul de l’IS de société est autonome de la qualification personnelle.')

add('113',[
    'Pour l’application des articles 109 et 112, l’incorporation directe de bénéfices au capital est traitée comme l’incorporation de réserves au capital.',
    'L’opération ne déclenche pas à elle seule l’impôt sur les sociétés prévu au V de l’article 219, puisqu’elle ne met aucune somme ni aucun bien à la disposition des associés. Elle ne transforme pas les bénéfices incorporés en apports extérieurs remboursables en franchise de cet impôt. Leur origine est conservée dans les comptes du XI de l’article 209.'
],
    'Permettre la capitalisation des bénéfices conservés sans IS immédiat, tout en préservant leur origine lors d’un remboursement ultérieur.',
    'L’assimilation préexistante des bénéfices et des réserves demeure ; la nouvelle règle n’exonère pas un retrait ultérieur des bénéfices nouveaux.')

add('115 quinquies',[
    '1. Pour les exercices ouverts à compter de l’entrée en vigueur de la loi instituant l’IS à la distribution, les bénéfices réalisés en France par une société étrangère ne sont réputés distribués à ses associés non résidents que dans la mesure où ils sont effectivement désinvestis hors de France.',
    'Il y a désinvestissement lorsqu’une somme ou une valeur provenant de l’établissement français est mise définitivement à la disposition du siège étranger ou d’une personne qui lui est liée, sans contrepartie professionnelle normale, ou lorsque le droit de la France d’imposer les bénéfices correspondants disparaît. Un transfert de trésorerie remboursable dans des conditions normales, le paiement d’une dette professionnelle réelle, un achat, un investissement ou la rémunération normale d’un travail ne suffit pas à caractériser un désinvestissement.',
    'Le bénéfice distribué est déterminé après l’IS effectivement dû sur cette attribution, dans les conditions du XII de l’article 209 et du V de l’article 219. La retenue prévue au 2 de l’article 119 bis porte sur le montant net ainsi réputé distribué ; elle n’est pas prélevée sur les bénéfices demeurés affectés à l’activité française.',
    '2. La société peut demander une nouvelle liquidation de cette retenue lorsqu’elle démontre que le montant retenu excède les sommes effectivement désinvesties ou ses distributions effectives. L’excédent est restitué. La même restitution s’applique si elle prouve que les bénéficiaires ont leur domicile fiscal ou leur siège en France et qu’elle leur a transféré la somme correspondant à la retenue. La demande identifie le fait générateur, le bénéficiaire, l’imposition initiale et les transferts réellement exécutés ; les modalités des articles 380 à 382 de l’annexe II restent applicables dans la mesure de leur compatibilité.',
    '3. La présomption de distribution du 1 ne s’applique pas à la société étrangère qui a son siège dans un Etat membre de l’Union européenne ou de l’Espace économique européen et y est passible, sans possibilité d’option et sans exonération, de l’impôt sur les sociétés, sans bénéficier d’une exonération spécifique des bénéfices concernés.',
    'L’exclusion de retenue du 3 ne supprime pas l’IS dû au titre de l’activité ou de l’établissement français selon les articles 209 et 219. Les conventions fiscales demeurent applicables.',
    '4. Les bénéfices, retenues et demandes de restitution relatifs aux exercices antérieurs restent soumis aux dispositions qui leur étaient applicables. L’ouverture du nouveau régime ne constitue, à elle seule, ni un désinvestissement ni une distribution réputée.'
],
    'Supprimer la distribution fictive annuelle des bénéfices de succursales étrangères et taxer le désinvestissement effectif, avec maintien des garanties européennes et conventionnelles.',
    'L’ancienne possibilité de restitution des retenues excessives est conservée ; aucune retenue annuelle n’est avancée sur de la trésorerie restée en France. Le simple mouvement de trésorerie à contrepartie réelle est distingué du prélèvement définitivement hors du périmètre français. Les articles379 et380 de l’annexeII sont coordonnés dans ce lot ;381 (bénéficiaire français et preuve de transfert) et382 (principal hors pénalités) demeurent compatibles et inchangés après lecture intégrale.',
    ['Suppression de la présomption annuelle de distribution des bénéfices français conservés par une société étrangère, avec taxation limitée au désinvestissement effectif.'])

prior=BY['145']['proposed_xml']
from_prior('145',prior+'\n'+''.join('<p>'+html.escape(p,quote=False)+'</p>\n' for p in [
    '10. Pour les exercices ouverts à compter de l’entrée en vigueur de la loi instituant l’imposition à la distribution, le présent article et l’article 216 sont appliqués en distinguant les produits déjà protégés d’un second IS et les autres produits de participation.',
    'Les sommes reçues d’une société soumise à l’IS français à la distribution, dont il est justifié qu’elles ont régulièrement donné lieu à liquidation de cet impôt ou qu’elles proviennent de son compte des bénéfices protégés d’un second IS, sont inscrites au même compte du bénéficiaire pour leur montant net réellement reçu. La liquidation peut appliquer un taux réduit légal ainsi que les déficits, réductions ou crédits légalement disponibles ; elle ne donne pas lieu à un complément au taux normal lors de la redistribution. Les dettes d’impôt non encore payées restent dues par leur redevable. Cette neutralisation n’est subordonnée ni au pourcentage de participation ni à une durée de conservation des titres. Elle ne s’applique qu’à concurrence de la fraction attestée par la société distributrice et vérifiable dans ses comptes ; aucune somme fictive ou déjà créditée ne peut être inscrite.',
    'Les autres produits de participation ne bénéficient de la protection prévue à l’article 216 que s’ils satisfont aux conditions du présent article, y compris les exclusions du 6. La simple conservation d’un dividende reçu dans la trésorerie du bénéficiaire n’entraîne toutefois aucun IS immédiat.',
    'L’impôt différé en application de l’article 219 reste un impôt sur les sociétés pour apprécier l’assujettissement du bénéficiaire. L’absence d’IS exigible au cours d’un exercice sans distribution ne rend pas, à elle seule, une société exonérée de cet impôt.',
    'La neutralisation ne crée ni crédit d’impôt remboursable ni exonération des impôts personnels dus lors d’une distribution aux associés. Les impôts minimaux annuels prévus au chapitre II bis restent régis par leurs dispositions propres.',
    'Les produits et reprises d’exonérations rattachables aux exercices antérieurs demeurent régis par les dispositions alors applicables. L’entrée dans le nouveau régime ne remet pas en cause une exonération définitivement acquise.'
]),
    'Ajouter au régime mère-fille un mécanisme sans seuil contre le double IS sur les mêmes dividendes français déjà taxés ; conserver les conditions et garde-fous pour les autres participations.',
    'Les 1 à 9 sont repris du précédent projet complet lu avec la source : 5%,2,5%/5%,délais2/5ans,exclusions non-coopératives et hybrides,participations de réseaux,réorganisations. Leur portée dans le nouveau régime est précisée au 10. Pas de nouvelle exonération annuelle automatique des dividendes étrangers, pas de crédit fictif. Les formalités de preuve peuvent résulter des comptes et déclarations existants ; aucun agrément discrétionnaire supplémentaire n’est créé. L’ancienne note évoquant un IS territorial0à5points est expressément abandonnée.')

add('216',[
    'I. Pour les exercices antérieurs à l’ouverture du régime d’IS à la distribution, les produits nets de participations remplissant les conditions de l’article 145 peuvent être retranchés du bénéfice total de la société mère, sous déduction d’une quote-part de frais et charges de 5 % de leur montant total, crédit d’impôt compris.',
    'Cette quote-part est de 1 % pour les produits perçus d’une autre société membre du même groupe des articles 223 A ou 223 A bis depuis plus d’un exercice. Elle est également de 1 % pour les produits d’une société soumise à un impôt équivalent dans un Etat de l’Union européenne ou de l’Espace économique européen lié à la France par une convention d’assistance administrative contre la fraude et l’évasion fiscales, lorsque, si cette société était française, les conditions de constitution d’un tel groupe auraient été remplies depuis plus d’un exercice.',
    'Dans le cas de titres transférés à un patrimoine fiduciaire mentionné au c du 1 de l’article 145, cette règle porte sur la part du bénéfice du constituant correspondant aux produits nets de ces titres, déterminée conformément à l’article 238 quater F.',
    'II. Pour les exercices ouverts à compter de l’entrée en vigueur du régime d’IS à la distribution, aucun produit de participation n’est soumis à l’IS ordinaire du seul fait de sa réception ou de sa conservation par la société bénéficiaire.',
    'Le montant net reçu d’une société française et justifié dans les conditions du 10 de l’article 145 est intégralement inscrit au compte des bénéfices protégés d’un second IS du 1 du XI de l’article 209. Sa redistribution est prélevée sur ce compte sans nouvelle cotisation d’IS. Aucune quote-part de frais et charges de 5 % ou de 1 % n’est imposée à cette occasion.',
    'Pour les autres produits ouvrant droit au régime de l’article 145, 100 % du montant net reçu est inscrit au même compte. Les conditions, durées de conservation, règles de reprise et exclusions prévues à cet article restent applicables. Si une condition cesse d’être remplie avant que le droit ne soit définitivement acquis, la société retranche du compte le montant indûment protégé. La fraction déjà redistribuée est régularisée au titre du mois de cette défaillance, au taux et dans les conditions des articles 219 et 1668 ; les fractions non encore redistribuées deviennent imposables lors de leur distribution ultérieure. Les sommes déjà effectivement taxées ne sont pas taxées deux fois.',
    'Les autres produits reçus sont suivis parmi les bénéfices nouveaux dont l’imposition est différée dans les conditions du 2 du XI de l’article 209. Leur conservation n’est subordonnée à aucun investissement déterminé ni à aucun délai de réemploi.',
    'Les frais réellement exposés restent comptabilisés et traités selon les règles qui leur sont propres ; leur absence de quote-part forfaitaire ne permet aucune double déduction, aucun avantage privé occulté ni aucun bénéfice fictif.',
    'III. Une opération de fiducie, de fusion ou de scission qui demeure fiscalement neutre transfère avec les sommes correspondantes leur origine et leur caractère déjà protégé ou encore différé. Elle ne crée ni protection supplémentaire ni crédit d’impôt. Les règles du présent article ne dispensent pas de l’imposition personnelle des associés ni de l’imposition minimale prévue aux articles 223 VJ et suivants.'
],
    'Supprimer les quotes-parts forfaitaires de 5% et1% pour le nouveau régime et protéger intégralement les dividendes bénéficiant d’une neutralisation mère-fille contre un second IS.',
    'La suppression des quotes-parts est un choix de réforme explicite conforme à la demande de couper les impôts en cascade. Le premier impôt sur distribution demeure dû à l’émettrice française. Les dividendes étrangers admissibles conservent les conditions145 ; les dividendes déductibles chez l’émetteur et exclusions sectorielles demeurent exclus. Un manquement au délai de conservation est régularisé une seule fois, à la redistribution déjà intervenue ou à la distribution future.',
    ['Suppression des quotes-parts forfaitaires de frais et charges de5% et1% qui imposaient à nouveau des dividendes admissibles, pour les exercices nouveaux.'])

add('223 A',[
    'I. Une société ou un établissement stable soumis en France à l’impôt sur les sociétés peut, avec l’accord des autres membres, être désigné société mère et regrouper la déclaration et le paiement de l’IS dû par un groupe dans les conditions du présent article.',
    'Le groupe comprend la société mère et les sociétés françaises ou établissements stables imposables en France dont elle détient de manière continue au moins 95 % des droits à dividendes et des droits de vote en pleine propriété, directement ou par une chaîne d’entités détenues dans les mêmes proportions. Les entités intermédiaires peuvent être établies en France ou dans un Etat de l’Union européenne ou de l’Espace économique européen lié à la France par une convention d’assistance administrative permettant effectivement de contrôler ces conditions et être soumises à un impôt équivalent à l’IS.',
    'Des sociétés ou établissements stables imposables en France détenus dans ces conditions par une même entité mère non résidente établie dans un de ces Etats peuvent constituer un groupe horizontal ; ils désignent ensemble le membre français chargé des obligations de société mère. L’accord écrit de l’entité mère non résidente et des entités étrangères interposées est joint à la désignation. Un même membre ne peut appartenir simultanément à deux groupes de déclaration de l’IS.',
    'La société mère est placée au sommet du périmètre français remplissant ces conditions. Une détention étrangère interposée n’exclut pas la constitution du groupe ; elle ne fait entrer dans l’assiette française aucun résultat d’une entreprise étrangère qui n’y est pas imposable.',
    'II. Les personnes morales soumises à l’IS qui établissent des comptes combinés en application de l’article L.345-2 du code des assurances, de l’article L.212-7 du code de la mutualité ou de l’article L.931-34 du code de la sécurité sociale peuvent former un groupe autour de l’entreprise combinante. En font partie les personnes morales dénuées de capital du périmètre combiné liées par une direction commune, des services communs entraînant un comportement commercial, technique ou financier commun, ou des liens réglementaires, statutaires ou contractuels importants et durables, ainsi que leurs filiales détenues à95% dans les conditions du I.',
    'Un organe central mentionné à l’article L.511-30 du code monétaire et financier ou une caisse départementale ou interdépartementale de l’article L.512-55 de ce code titulaire d’un agrément collectif peut regrouper les banques, caisses et sociétés des articles L.512-11,L.512-20,L.512-55,L.512-60,L.512-69 et L.512-86 qui lui sont affiliées au sens de l’article L.511-31 ou relèvent du même agrément, et leurs filiales détenues à95%. Les personnes morales du réseau, hors filiales détenues par le capital, sont toutes comprises dans ce périmètre.',
    'Pour apprécier les95%, il est fait abstraction, dans la limite de10% du capital, des titres attribués ou émis aux salariés dans les dispositifs des articles L.225-177 à L.225-184,L.225-197-1 à L.225-197-5,L.22-10-56 et L.22-10-59 du code de commerce, des articles L.3332-18 à L.3332-24 du code du travail, ou de dispositifs étrangers équivalents. L’exclusion prend fin à la cession des titres ou à la cessation des fonctions dans le périmètre du plan ; lorsque leur conservation demeure légalement obligatoire, elle se poursuit jusqu’au terme de cette obligation. En cas de perte temporaire du seuil due à la fin de cette exclusion, le seuil peut être rétabli au plus tard au terme du délai annuel de déclaration prévu au1 de l’article223.',
    'Les titres transférés en fiducie dans les conditions de l’article238 quaterB restent comptés chez le constituant s’ils comportent droits de vote et droits à dividendes et si le constituant conserve les droits de vote ou en détermine l’exercice par le fiduciaire, sous réserve des limites nécessaires à la protection des créanciers de la fiducie.',
    'III. Pour les exercices relevant du V de l’article219, chaque société détermine l’IS de ses propres distributions. La société mère en déclare et acquitte la somme dans les conditions des articles223B,223N et1668. La désignation n’exonère pas la première distribution réalisée par une société du groupe ; la neutralisation d’un même bénéfice dans une chaîne de participations résulte exclusivement des articles145,216 et209XI.',
    'Chaque société conserve ses comptes, justificatifs de distribution et comptes de suivi de l’article209. Ils peuvent être contrôlés selon les articles L.13,L.47 et L.57 du livre des procédures fiscales, dans le respect des garanties de procédure. La société mère répond des obligations qu’elle assume et des droits et pénalités légalement mis à sa charge ; chaque membre n’est solidairement tenu que dans la limite de l’IS et des pénalités qu’il aurait lui-même dus hors du groupe.',
    'IV. La désignation, l’accord de chaque membre et la liste du périmètre sont adressés au service des impôts avant le premier dépôt groupé. Ils prennent effet pour les faits générateurs du mois suivant leur notification. Toute modification est portée sur la déclaration du mois où elle produit effet. L’option se poursuit sans renouvellement annuel ; elle peut être dénoncée pour les faits générateurs du mois suivant sa notification, sans durée minimale obligatoire. Les membres n’ont pas à aligner leurs dates de clôture pour ce seul regroupement mensuel.',
    'Les options et accords d’intégration valablement en cours à l’ouverture du nouveau régime valent désignation et accords de paiement pour les mêmes membres, sans nouvelle formalité. Le changement de régime ne vaut ni sortie du groupe ni distribution de réserves.',
    'V. Les articles223A à223U, dans leur rédaction applicable aux exercices antérieurs à l’ouverture du régime du V de l’article219, restent applicables à la détermination, au contrôle et au règlement des droits et obligations attachés à ces exercices, ainsi qu’aux déficits, créances et neutralisations qui en proviennent. Leur application ne peut, pour un exercice nouveau, rétablir un impôt ordinaire annuel sur les bénéfices conservés ni un acompte calculé sur un tel impôt.',
    'Les compartiments de bénéfices relevant d’un taux particulier, les reprises et les réserves sont suivis selon les articles209 et219. Leur calendrier d’imposition est celui prévu expressément par ces articles ; le seul calcul d’un résultat d’ensemble ne rend pas exigible un impôt différé. Les règles d’imposition minimale des articles223VJ et suivants, distinctes du regroupement du présent article, demeurent intégralement applicables.'
],
    'Transformer l’intégration annuelle ordinaire en regroupement facultatif de déclaration et de paiement des distributions, en conservant les droits anciens et les principaux périmètres95%,horizontaux,mutualistes et bancaires.',
    'Source223A complète lue. La réforme abandonne expressément la cotisation annuelle sur somme des résultats, les engagements obligatoires de cinq exercices, les options/lists annuelles et la clôture commune pour le seul IS de distribution. Les critères de contrôle95%,l’exclusion salarié10%,la fiducie,les groupes horizontaux et réseaux sont explicités. Les anciennes conditions détaillées restent applicables aux droits anciens ; les règles nouvelles ne sont pas présentées comme une reconduction à droit constant. Les références d’alinéas des articles de la section qui restent à réécrire ne doivent pas être appliquées au nouvelarticle mais à la version historique pertinente.',
    ['Suppression de l’intégration annuelle des bénéfices ordinaires conservés et de l’obligation de recalculer un résultat d’ensemble taxable chaque année pour ce seul IS.',
     'Suppression de l’engagement obligatoire pour cinq exercices, des formalités annuelles répétées et de l’exigence de clôture commune pour une simple déclaration mensuelle des distributions.'])

add('223 A bis',[
    'I. Un établissement public industriel et commercial soumis à l’impôt sur les sociétés peut exercer les fonctions de société mère prévues à l’article223A lorsqu’il établit des comptes consolidés dans les conditions du premier alinéa de l’articleL.233-18 du code de commerce et assure, pour le groupe, le contrôle, le pilotage stratégique et des missions transversales ou mutualisées.',
    'Le périmètre comprend cet établissement, les établissements publics industriels et commerciaux soumis à l’IS qui appartiennent à son périmètre de consolidation et les sociétés qu’ils détiennent dans les conditions de l’article223A. Tous ces établissements publics font partie du groupe ; un même membre ne peut être tête d’un autre groupe d’IS.',
    'II. L’établissement tête de groupe ne peut être contrôlé par un autre établissement remplissant lui-même ces conditions. Les consentements, garanties, limites de solidarité et obligations déclaratives de l’article223A sont applicables.',
    'III. Pour les exercices relevant du V de l’article219, le groupe déclare et paie l’IS des distributions de chacun de ses membres ; l’existence de comptes consolidés ou d’un résultat d’ensemble ne crée pas un IS annuel sur les bénéfices conservés. Les articles223B à223U s’appliquent dans les limites temporelles et matérielles du V de l’article223A.',
    'Les résultats et droits relatifs aux exercices antérieurs demeurent régis par les règles alors applicables ; le passage au régime à la distribution ne vaut pas cessation du groupe.'
],
    'Conserver les groupes d’EPIC tout en les faisant relever du même calendrier à la distribution que les groupes privés.',
    'La source et sa note d’application aux exercices ouverts depuis2015 ont été lues. Les conditions de consolidation,pilotage,stratégie,périmètre obligatoire et absence de double tête sont conservées ; aucune consolidation annuelle ne déclenche le nouvelIS.')

add('223 B',[
    'I. Pour les exercices relevant du V de l’article219, la société mère calcule la cotisation groupée en faisant la somme de l’IS dû par chaque membre à raison des distributions du mois, après application, pour ce membre, des articles209,219 et216. Les déficits d’ensemble antérieurs légalement détenus par la mère sont imputés et ventilés une seule fois dans les conditions de l’article223I, avant cette somme ; aucun membre ne les déduit séparément. Une distribution d’une filiale à la société mère n’est pas dispensée de la première cotisation du seul fait de l’appartenance au groupe.',
    'Les dividendes et autres produits qui ont déjà supporté cet IS, ou proviennent de bénéfices déjà protégés, sont suivis chez leur bénéficiaire conformément aux articles145 et216. La redistribution du même montant net ne supporte pas un second IS. La société mère conserve, par membre et par flux, l’origine du bénéfice, l’impôt effectivement supporté et le montant net protégé.',
    'Les achats, ventes, prestations et financements réels entre membres, conclus dans l’intérêt de leur exploitation à des conditions normales, ne sont pas des distributions du seul fait du paiement. La facturation artificielle, l’abandon sans contrepartie professionnelle et la mise à disposition d’un avantage privé restent soumis aux articles111,209 et219. Les règles de prix de transfert et de lutte contre les montages artificiels demeurent applicables.',
    'La seule constatation d’un bénéfice comptable d’ensemble ou d’une plus-value interne ne rend pas exigible l’IS sur un bénéfice conservé. Les pertes, charges et créances ne peuvent ni créer un bénéfice protégé fictif ni être utilisées plusieurs fois ; les droits antérieurs sont suivis selon l’article223I.',
    'II. Les ajustements des résultats d’ensemble des exercices antérieurs, notamment les produits de participation, provisions, rémunérations, acquisitions de titres auprès d’un contrôlant et charges financières, restent calculés selon la rédaction du présent article applicable à chacun de ces exercices. Les droits, garanties de preuve et exclusions alors applicables demeurent attachés à ces opérations.',
    'Les neutralisations ou reprises anciennes encore en suivi à l’ouverture du nouveau régime conservent leur qualification et leur montant. Elles sont rattachées au compte approprié de l’article209 et ne font naître une cotisation nouvelle que dans les cas et aux dates expressément prévus à l’article219. La transition n’équivaut pas à une cession ni à une reprise automatique en résultat taxable.'
],
    'Supprimer le résultat d’ensemble annuel comme assiette de l’IS ordinaire nouveau et additionner uniquement les cotisations effectivement déclenchées par les distributions.',
    'Source lue en entier : ancienne déduction99%,provisions,tantièmes,transactions,amendement Charasse8exercices et reports de charges financières sont conservés pour droits anciens par référence précise à leur version applicable. Aucune quote-part forfaitaire99%/1% nouvelle n’est maintenue sur les dividendes déjà taxés. Les règles ATAD/prixtransfert/Pilier2 ne sont pas supprimées.',
    ['Suppression des calculs annuels d’intégration et des retraitements exclusivement nécessaires à une imposition annuelle ordinaire qui disparaît pour les exercices nouveaux.'])

add('223 C',[
    'Pour les exercices relevant du V de l’article219, la société mère n’est pas redevable d’un IS ordinaire du seul fait que le groupe réalise un bénéfice d’ensemble. Les cotisations des distributions de chaque membre sont déterminées selon les articles223B,209 et219.',
    'Le résultat d’un compartiment relevant d’un taux particulier, notamment celui des actifs éligibles à l’article238, est suivi distinctement. Son taux et son calendrier d’imposition sont ceux prévus aux articles209 et219 ; sa conservation dans le groupe ne peut être transformée par le présent article en distribution.',
    'Le déficit d’ensemble antérieur non encore utilisé reste suivi et imputé dans les conditions des articles223I et209. Une fraction déjà utilisée pour neutraliser un bénéfice, une distribution ou un résultat de compartiment spécial ne peut être reportée de nouveau.',
    'La liquidation et le contrôle des exercices antérieurs demeurent soumis à la rédaction du présent article applicable à chacun de ces exercices, y compris les règles d’imposition séparée et de compensation alors en vigueur.'
],
    'Supprimer la cotisation ordinaire annuelle du groupe et préserver les compartiments spéciaux ainsi que les pertes antérieures sans double usage.',
    'Le traitement du résultat IP ne crée pas un taux nouveau et suit219 ; pas de promesse d’abolition du minimum mondial. La note source2019 concerne le régime antérieur, préservé pour ces exercices.',
    ['Suppression de l’imposition ordinaire annuelle du bénéfice d’ensemble pour les exercices soumis au nouvelIS à la distribution.'])

add('223 I',[
    'I. A l’ouverture du régime du V de l’article219, les déficits, moins-values à long terme, charges financières nettes non déduites et capacités de déduction inemployées sont inventoriés par année d’origine, catégorie et titulaire. Les déficits propres antérieurs à l’entrée d’une société dans un groupe restent attachés à cette société. Les déficits d’ensemble encore reportables appartiennent à la société mère ou à son ayant droit qui en était légalement titulaire ; ils ne sont pas simultanément attribués aux filiales qui les avaient économiquement engendrés.',
    'Les transferts ou fractions de droits valablement attribués avant cette ouverture, notamment dans les conditions des articles223E,223L,223R et223S, demeurent opposables pour leur montant restant réellement disponible. La même somme ne peut être maintenue chez le cédant et transférée chez le bénéficiaire.',
    'II. Les déficits antérieurs peuvent être utilisés par leur seul titulaire dans les conditions du3 duXI de l’article209. Les limites et compartiments applicables à chaque catégorie demeurent respectés. Les moins-values à long terme ne sont imputables que sur les gains de la catégorie à laquelle elles se rattachent, selon l’article39quindecies et les dispositions qui les régissent ; elles ne deviennent pas un crédit remboursable contre n’importe quelle distribution.',
    'La société mère qui reste titulaire d’un déficit d’ensemble antérieur peut en imputer le montant réellement disponible sur les bases imposables des distributions de ses membres qui appartenaient au périmètre ouvrant ce droit avant la transition et continuent d’appartenir au groupe. Les restrictions déjà attachées à certaines fractions de déficit, notamment en cas d’imputation élargie, restent respectées. Cette utilisation est suivie exclusivement chez la mère ; elle ne transfère pas le déficit aux membres.',
    'Le plafond annuel prévu au3 duXI de l’article209 est appliqué une seule fois au déficit d’ensemble sur l’assiette cumulée ainsi autorisée, et non séparément à chaque membre. La mère ventile dans la déclaration les bases et fractions de déficit effectivement utilisées. La base réduite chez un membre ne peut être utilisée de nouveau pour consommer le même déficit. Aucun déficit nouveau d’un autre membre n’est ajouté à ce droit transitoire.',
    'La société mère identifie dans la déclaration groupée le titulaire de chaque droit et le montant consommé. Sous réserve de la couverture transitoire du déficit d’ensemble prévue ci-dessus, la seule appartenance au groupe de paiement ne permet pas à une filiale de déduire le déficit propre d’une autre, ni à une mère de reprendre un droit qui ne lui a pas été légalement transféré.',
    'III. Les pertes réelles constatées après l’ouverture du nouveau régime sont suivies selon le3 duXI de l’article209. Une perte ayant déjà réduit un bénéfice disponible, une base de distribution ou un compartiment spécial ne peut être utilisée de nouveau. La circulation de la même somme au sein du groupe ne multiplie pas les pertes ni les bénéfices protégés.',
    'Les charges financières nettes non déduites et les capacités de déduction inemployées conservent leur titulaire et leurs délais propres, y compris les suspensions de délai acquises pendant une ancienne intégration. Leur suivi ne transforme pas une capacité de déduction en créance d’IS et ne fait pas renaître une imposition annuelle ordinaire.',
    'IV. Les conditions d’imputation, corrections de réévaluation, agréments et transferts relatifs aux exercices ou opérations antérieurs demeurent ceux de la rédaction du présent article qui leur était applicable. Les fractions transférées conformément aux6 et7 de cette rédaction et les droits d’imputation élargie du5 sont conservés, à concurrence des droits non encore consommés et sans double emploi.',
    'Une fusion, une scission, une absorption ou un apport postérieur ne transfère les droits anciens que dans les conditions légales qui les régissent, notamment celles des articles209,210A et210B. Le simple passage à la taxation à la distribution ne nécessite pas un agrément nouveau et ne fait pas perdre un droit antérieurement acquis.'
],
    'Organiser le passage des pertes d’intégration au régime à la distribution sans perte des droits acquis, sans duplication et sans libre compensation entre sociétés.',
    'Source223I et note2019 lues entièrement ; les droits préentrée,d’ensemble,les transferts5/6/7,les contraintes de catégorie et les suspensions de durée sont identifiés. Le vrai déficit d’ensemble ancien peut couvrir les distributions des membres de l’ancien périmètre éligible, sous plafond209 appliqué une seule fois et consommation centralechezlamère ; aucun droit équivalent n’est créé pour les nouvelles pertes. L’ancienne procédure d’agrément n’est pas supprimée pour une opération distincte de la transition. Le renvoi de catégorie est à l’article39quindecies, comme dans la source.',
    ['Suppression des nouveaux retraitements annuels exclusivement destinés à la compensation annuelle des résultats ordinaires, avec maintien des droits antérieurs réellement disponibles.'])

add('223 N',[
    '1. Pour les faits générateurs relevant du V de l’article219, la société mère déclare et paie au plus tard le15 du mois suivant la somme des cotisations de chaque membre prévue à l’article223B, dans les conditions de l’article1668. Les distributions des sociétés qui ne sont pas encore comprises dans le périmètre notifié restent déclarées et payées par ces sociétés.',
    'Aucun acompte d’IS ordinaire n’est dû du seul fait de l’entrée ou de la sortie du groupe, ni du seul fait d’un bénéfice conservé. Les cotisations effectivement nées avant une sortie restent dues par le redevable légal du mois concerné.',
    '2. Les acomptes antérieurement versés et non encore imputés sont identifiés par titulaire et année. Ils s’imputent ou sont restitués dans les conditions de l’article1668 ; un même acompte ne peut être utilisé par la société mère et par le membre qui l’a versé. Le regroupement de paiement ne transfère pas une créance que la loi n’attribue pas à la société mère.',
    '3. Les versements et régularisations relatifs aux exercices antérieurs restent soumis aux dispositions alors applicables, notamment pour l’attribution à la mère d’un excédent d’acomptes de la première année d’intégration et pour les obligations de versement lors de la sortie. Ces dettes ne sont pas annulées par la réforme.'
],
    'Remplacer les acomptes annuels d’entrée et de sortie par le paiement mensuel des seules distributions effectivement taxables.',
    'Alignement1668 au15 du mois suivant. Les acomptes anciens ne sont ni perdus ni remboursés deux fois ; les droits anciens de la mère sont préservés.',
    ['Suppression des acomptes d’IS ordinaire de douze mois déclenchés par la seule entrée ou sortie d’un groupe sous le régime nouveau.'])

# Preserve and rephrase every credit category rather than deleting a long list.
credit_map=[
 ('a','des crédits attachés aux produits reçus par les membres et qui ne bénéficient pas des articles145 et216',None),
 ('b','du crédit de recherche de l’article244quaterB','199terB'),
 ('b bis','du crédit de recherche collaborative de l’article244quaterBbis','199terBbis'),
 ('c','du crédit de l’article244quaterC','199terC'),
 ('d','du crédit d’investissement de l’article244quaterE','199terD'),
 ('e','des réductions de l’article238bis',None),
 ('f','du crédit de l’article244quaterF','199terE'),
 ('g','du crédit de l’article220sexies','220F'),
 ('h','des réductions de l’article220undecies',None),
 ('i','du crédit de l’article244quaterI','244quaterI'),
 ('j','du crédit de l’article220decies','220decies'),
 ('k','du crédit de l’article244quaterJ','220K'),
 ('l','du crédit de l’article244quaterT','220Zocties'),
 ('n','du crédit de l’article244quaterL','220M'),
 ('o','du crédit de l’article244quaterK','244quaterK'),
 ('p','du crédit de l’article244quaterO','220P'),
 ('q','du crédit de l’article220octies','220Q'),
 ('r','du crédit de l’article220nonies','220R'),
 ('s','du crédit de l’article220quindecies','220S'),
 ('t','des réductions de l’article220undeciesA',None),
 ('v','du crédit de l’article220sexdecies','220T'),
 ('w','du crédit de l’article220terdecies',None),
 ('x','du crédit de l’article220septdecies','220Qbis'),
 ('y','du crédit de l’article244quaterU','220Z'),
 ('z','du crédit de l’article220quaterdecies','220Zbis'),
 ('z bis','du crédit de l’article244quaterV','220Zter'),
 ('z ter','du crédit de l’article244quaterW','220Zquater'),
 ('z quater','du crédit de l’article244quaterX','220Zquinquies'),
 ('z quinquies','des réductions de l’article244quaterY','220Zsexies')]
paras=['1. La société mère se substitue aux membres du groupe pour imputer les crédits et réductions suivants sur l’IS dont elle assure légalement le paiement :']
for label,subject,rule in credit_map:
    paras.append(label+'. Il s’agit '+subject+'.'+((' Les règles de l’article'+rule+' sont appliquées à la somme de ces crédits ou réductions.') if rule else ''))
paras += [
    'Les subdivisions m et u sont abrogées.',
    '2. Pour les exercices relevant du V de l’article219, cette substitution ne rend aucun IS exigible avant le fait générateur d’une distribution. Les crédits et réductions réellement acquis conservent leur montant, leur durée, leurs plafonds et leurs conditions légales de restitution ; l’absence d’IS de distribution ne les transforme pas en remboursement immédiat si leur texte ne le prévoit pas.',
    'Les crédits antérieurs détenus par la société mère restent détenus par elle ; ceux dont un membre conserve légalement la titularité ne sont pas transférés du seul fait du regroupement de paiement. Tout montant effectivement imputé est retranché du compte de son titulaire et ne peut être utilisé par un autre membre.',
    'Un impôt étranger ou un IS français déjà neutralisé par les articles145,216 et209 ne crée pas un second crédit contre la même distribution. Les conventions fiscales et les règles propres à chaque crédit restent applicables. Aucune imputation sur l’impôt complémentaire des articles223VJ et suivants n’est créée par le présent article.',
    '3. Pour les exercices antérieurs, la substitution et les règles de restitution demeurent régies par la version du présent article qui leur était applicable. Les dates d’engagement des dépenses propres à chaque crédit, y compris celles résultant de la loi n°2026-103 du19février2026, demeurent respectées.'
]
add('223 O',paras,
    'Préserver l’ensemble des crédits de groupe et leurs modalités légales sans créer un remboursement fictif du fait du passage à l’IS de distribution.',
    'Source et toutes les catégoriesa àzquinquies lues ; aucune catégorie de crédit n’est supprimée par simplification de présentation. Les droits existants et crédits remboursables selon leur propre texte demeurent ; l’absence d’IS ne crée pas une nouvelle restitution ni une imputation Pilier2.')

add('223 Q',[
    'Pour les faits générateurs relevant du V de l’article219, la société mère souscrit la déclaration groupée du mois prévue à l’article1668. Elle identifie chaque membre, les distributions effectivement taxables, les montants protégés d’un second IS, les pertes ou crédits effectivement utilisés et la cotisation correspondante.',
    'Les données déjà déclarées et accessibles à l’administration ne sont pas redéposées sous un autre format. Une correction d’une donnée est rattachée à sa déclaration d’origine et transmise une seule fois. Les justificatifs sont conservés et produits sur demande dans les délais légaux de contrôle.',
    'Pour le seul IS ordinaire différé, il n’est pas exigé de déclaration annuelle supplémentaire d’un résultat d’ensemble imposable. La société mère transmet avec l’état annuel des comptes de suivi prévu à l’article209 un rapprochement des déclarations mensuelles et de leurs soldes ; ce rapprochement ne constitue pas un nouveau fait générateur.',
    'Les comptes annuels et les déclarations nécessaires à d’autres impôts, aux compartiments spéciaux ou à l’imposition minimale des articles223VJ et suivants restent exigibles conformément à leurs textes propres.',
    'Les déclarations et états des exercices antérieurs, y compris les suivis de subventions, abandons de créances et neutralisations des articles223B,223D et223F, restent conservés ou souscrits lorsqu’ils sont nécessaires à des droits et obligations encore en cours. Leur montant est rapproché des comptes de transition de l’article209 pour éviter toute double imposition ou double utilisation.'
],
    'Supprimer la double liasse annuelle du groupe pour un IS qui n’est plus dû annuellement, en gardant un suivi vérifiable des flux et des droits anciens.',
    'Les autres obligations comptables,fiscales et de minimum international ne sont pas supprimées. Le principe de déclaration unique ne dispense pas de justifier une donnée contestée.',
    ['Suppression des nouvelles liasses annuelles du résultat d’ensemble pour le seul IS ordinaire de distribution et des redépôts des mêmes données déjà accessibles.'])

add('223 S',[
    'I. Un membre sort du groupe de paiement lorsqu’il cesse de remplir les conditions de l’article223A ou223Abis ou lorsque son accord cesse dans les conditions de l’article223A. Le groupe prend fin si la société mère dénonce sa désignation sans successeur ou si aucun autre membre n’y demeure.',
    'Pour les exercices relevant du V de l’article219, l’entrée, la sortie, le changement de mère ou la fin du groupe de déclaration ne constituent ni une distribution ni une réalisation taxable de bénéfices conservés. Chaque société continue le suivi de ses bénéfices protégés, bénéfices différés et pertes dans les comptes de l’article209. Le paiement des distributions antérieures à la sortie demeure dû par le redevable légal de la période.',
    'II. Le déficit d’ensemble antérieur et les moins-values à long terme restant reportables appartiennent à la société qui était légalement redevable de l’IS du groupe, sous réserve des fractions légalement transférées ou attribuées à d’autres membres. Les conditions de l’article223I et les règles de catégorie et de non-double emploi restent applicables.',
    'Les charges financières nettes non déduites et les capacités de déduction inemployées encore disponibles à la fin d’une ancienne intégration restent suivies par leur titulaire dans les conditions de l’article212bis et de l’article223I. Elles ne deviennent pas une créance remboursable du fait de cette fin.',
    'III. Les neutralisations anciennes qui devraient être reprises lors d’une véritable cession, d’une perte du droit d’imposer ou d’un autre fait générateur conservent leur suivi. La simple transition vers l’IS de distribution ne constitue pas ce fait générateur. Les obligations relatives aux exercices antérieurs restent régies par les versions des articles223A à223U qui leur étaient applicables.',
    'Une fusion éligible à l’article210A de la société mère dans un autre membre ne remet pas à zéro les comptes, droits ou suivis. Le successeur légal assume les obligations transférées ; les déficits ne lui sont transférés que dans les conditions légales des articles209 et223I. Les éventuels agréments distincts de la transition ne sont pas supprimés.',
    'IV. L’impôt sur les sociétés dû lors d’une liquidation, d’un transfert d’actifs ou de siège ou d’une perte effective du droit de la France d’imposer reste établi selon les articles209,219,221 et221bis. Les impositions personnelles des associés et le minimum international ne sont pas neutralisés par la sortie du groupe.'
],
    'Empêcher une taxation des réserves à la seule sortie du groupe ou lors de la transition, tout en conservant les dettes, titulaires de pertes et suivis antérieurs.',
    'Source et notes2018/2019 lues. La mère conserve le déficitd’ensemble légalement détenu et les droits transférés restent chez leur attributaire. Les clauses de cessation,absorption et maintien des suivis sont remplacées pour les faits nouveaux,avec application explicite des anciennes versions aux droits anciens.',
    ['Suppression de la taxation d’un bénéfice conservé résultant uniquement de la sortie ou de la fin du groupe de déclaration sous le nouveau régime.'])

add('223 VJ',[
    'Les groupes d’entreprises multinationales et les groupes nationaux entrant dans le champ de l’article223VL restent soumis à une imposition minimale annuelle.',
    'Cette imposition prend la forme de l’impôt complémentaire déterminé, selon les cas, par la règle d’inclusion du revenu, par la règle relative aux bénéfices insuffisamment imposés ou par les règles de l’impôt national complémentaire. Cet impôt n’est déductible ni de l’assiette de l’impôt sur les sociétés ni de celle de l’impôt sur le revenu.',
    'Le report de l’IS ordinaire jusqu’à la distribution prévu aux articles209 et219 ne dispense pas de cette imposition minimale, de son calcul annuel, de sa déclaration ou de son paiement. L’absence de distribution ne vaut pas, par elle-même, exonération de l’impôt complémentaire.',
    'Le régime français de distribution nouvellement institué n’est pas réputé, du seul fait de ses modalités ou de son taux nominal, remplir la condition d’antériorité du c du39° de l’article223VK. L’application des dispositions réservées aux régimes éligibles exige que toutes les conditions de cette définition soient effectivement remplies ; aucun impôt fictif de distribution ne peut être ajouté aux impôts couverts du seul fait du présent report.',
    'Le champ, les exclusions, le taux minimum de15%, les règles de détermination du résultat qualifié et des impôts couverts, ainsi que les mesures de sauvegarde, reports et coordinations propres au présent chapitre, restent ceux prévus aux articles223VK et suivants. Le suivi de l’IS effectivement acquitté sur les distributions s’effectue selon ces dispositions, sans double prise en compte du même impôt.'
],
    'Conserver explicitement le minimum international annuel pour les grands groupes malgré le report de l’IS ordinaire à la distribution.',
    'Vérification primaire : directive(UE)2022/2523,article3(42)c, régime en vigueur au plus tard le 1er juillet2021 ; transposition223VK39°c identique.223VL : CAconsolidé≥750M€ sur2des4exercices précédents, groupes nationaux inclus ;223VK45° :15%. Les exclusions et régimes de sauvegarde ne sont pas abolis. Le nouveau dispositif français ne revendique pas la dérogationarticle40 applicable aux régimes antérieurs. Sources : https://eur-lex.europa.eu/legal-content/EN-PL/ALL/?uri=CELEX%3A32022L2523 et XMLDILA courant conservé dans le corpus.')

add('40',[
    'Pour les revenus distribués qui relèvent du nouveau régime du fait générateur prévu à l’article109 du code général des impôts, la masse des revenus distribués comprend les sommes et valeurs effectivement mises à disposition des bénéficiaires pendant la période légalement déclarée. Elle est déterminée dans les conditions des articles41 à47 de la présente annexe.',
    'Le rattachement à l’impôt sur le revenu suit la date de mise à disposition effective ; celui de l’IS de la société suit les articles209,219 et1668 du code général des impôts. Un exercice bénéficiaire sans distribution ne produit pas une masse distribuée du seul fait de son bénéfice.',
    'Les périodes antérieures à l’ouverture du nouveau régime restent régies par les dispositions qui leur étaient applicables.'
],
    'Supprimer le lien automatique entre période annuelle de bénéfice IS et revenu réputé distribué.',
    'Ancienne version et précédent projet lus intégralement. Le renvoi41à47 est conservé avec des règles nouvelles cohérentes ;43 n’est pas une entrée courante du corpus. Aucun taux d’impôt personnel n’est modifié.',
    ['Suppression du calcul d’une masse distribuée automatique à chaque période annuelle de bénéfice IS, en l’absence de mise à disposition effective.'])

add('41',[
    'Les distributions de la période sont établies à partir des écritures comptables, des décisions d’attribution et des paiements ou avantages réellement exécutés. Les sommes et valeurs sont ventilées entre bénéficiaires, avec la date de leur mise à disposition.',
    'La comparaison entre les postes de capital, de réserves et de résultats à l’ouverture et à la clôture peut servir à vérifier l’exhaustivité de ces distributions. Elle est rapprochée des apports, remboursements, résultats conservés et opérations sans paiement ; elle ne crée pas de présomption irréfragable de distribution.',
    'Pour une société nouvelle, les comptes d’ouverture sont ceux de sa constitution définitive. L’état de rapprochement est tenu à disposition avec les comptes existants ; il n’est pas déposé séparément si les données correspondantes ont déjà été régulièrement déclarées.',
    'Ces règles s’appliquent aux périodes nouvelles visées à l’article40 ; pour les périodes antérieures, la comparaison demeure celle de la version alors applicable.'
],
    'Faire de la comparaison des bilans un contrôle des flux et non le mécanisme qui crée un dividende fictif.',
    'Les trois postes comptables et le bilan de constitution subsistent comme éléments de preuve. Aucune déclaration autonome redondante n’est créée.',
    ['Suppression de la comparaison des bilans utilisée comme preuve automatique suffisante d’une distribution fictive de bénéfices conservés.'])

add('42',[
    'Pour les périodes nouvelles visées à l’article40, la masse des revenus distribués est égale à la somme des versements en argent et de la valeur normale des biens et avantages effectivement attribués, directement ou par personne interposée, aux bénéficiaires des articles109 et111 du code général des impôts.',
    'Elle est augmentée des distributions dissimulées établies par l’administration selon les règles de preuve et de procédure applicables. Une variation du bilan ou une rectification du bénéfice de la société ne suffit pas à elle seule à établir une attribution aux associés.',
    'Les opérations exclues par les articles112 à115 du code général des impôts sont retranchées si elles ont déjà été comprises dans cette somme. Les impôts effectivement supportés par la société sont pris en compte selon l’article110 de ce code sans être déduits deux fois. L’impôt personnel prélevé pour le bénéficiaire reste compris dans son revenu brut.',
    'Les sanctions, amendes, confiscations et pénalités mises à la charge propre de la société ne constituent pas un revenu de l’associé du seul fait de leur paiement. Une sanction personnelle acquittée pour le compte d’un associé est, en revanche, un avantage à examiner selon l’article111 de ce code.',
    'Les bénéfices conservés et les pertes de la période n’ajoutent ni ne retirent une distribution réellement exécutée. Aucun versement ni aucune correction n’est compté deux fois. Pour la société distributrice, l’assiette distincte de l’IS est établie selon les articles209 et219 de ce code.',
    'Les anciennes formules faisant la différence entre bénéfice, perte et variation des postes de bilan demeurent applicables exclusivement aux périodes antérieures, selon la rédaction alors en vigueur.'
],
    'Remplacer les formules automatiques bénéfice moins réserve par la somme des flux réellement distribués, en préservant les exclusions et la preuve des avantages occultes.',
    'Source lue intégralement : formules bénéfice−accroissement,bénéfice+diminution,diminution−perte abandonnées pour les périodes nouvelles. Catégories b et c de111,exclusions112à115,sanctions et principe sans double emploi explicitement traités. Le taux et le recouvrement personnels ne changent pas.',
    ['Suppression des trois formules mécaniques de distribution par écart entre bénéfice ou perte et variation des postes du bilan pour les périodes nouvelles.'])

add('44',[
    'Pour le rapprochement comptable de l’article41, le capital retenu correspond aux apports réellement reçus ; la fraction non appelée et les sommes seulement promises ne sont pas des ressources versées par les associés.',
    'Les réserves comprennent les résultats conservés et reports bénéficiaires à nouveau ainsi que, dans leur catégorie comptable respective, les provisions, amortissements et dotations légalement constitués. Leur inscription à un poste de réserve ou de provision ne suffit pas à démontrer qu’ils ont déjà supporté l’impôt.',
    'La protection contre un second IS résulte exclusivement des sommes justifiées dans le compte du1 duXI de l’article209 du code général des impôts. Les bénéfices nouveaux conservés restent suivis comme différés, sans être assimilés à des apports ni à des bénéfices déjà taxés.',
    'Les qualifications historiques, notamment des provisions et amortissements ayant supporté l’impôt sur les bénéfices industriels et commerciaux ou l’IS et des provisions, décotes et dotations sur stocks légalement constituées, restent appliquées aux périodes antérieures selon la version alors en vigueur.'
],
    'Distinguer la réserve comptable, le vrai capital apporté et le bénéfice fiscalement protégé, pour éviter une fausse exonération lors de la redistribution.',
    'Exclusion du capital non appelé préservée. Les historiques de BIC et stocks ne sont pas effacés pour les exercices anciens ; aucune présomption de paiement de l’IS n’est attachée au simple libellé comptable.')

add('45',[
    'Pour les périodes nouvelles visées à l’article40, les apports extérieurs et appels de capital sont pris en compte à la date où les fonds ou biens sont réellement reçus par la société. Il n’est pas attendu l’exercice suivant pour établir leur absence de caractère distribué.',
    'Les primes d’émission correspondant à un apport réel suivent la même règle. Les primes de fusion, réserves de réévaluation et réserves constituées en franchise d’IS sont suivies selon leur origine et le régime légal de l’opération ; leur inscription comptable ne crée pas un apport extérieur ni une protection nouvelle d’un second IS.',
    'Les incorporations de bénéfices ou réserves au capital demeurent régies par les articles112 et113 du code général des impôts. Le rapprochement doit conserver leur nature et éviter de les traiter comme une distribution exécutée ou comme un apport nouveau.',
    'Le décalage à la période suivante prévu par l’ancienne rédaction reste appliqué seulement pour la détermination des distributions des périodes antérieures.'
],
    'Supprimer le décalage artificiel d’un exercice pour les vrais apports, tout en conservant l’origine fiscale des primes et réserves.',
    'Ancien décalage lu et explicitement abandonné pour les faits nouveaux. Les réserves de réévaluation ou de fusion ne sont pas automatiquement exonérées et ne deviennent pas des apports réels.',
    ['Suppression de l’attente de l’exercice suivant pour tenir compte d’un apport ou appel de capital réellement reçu dans le contrôle des distributions nouvelles.'])

add('46',[
    'Pour les périodes nouvelles visées à l’article40, les plus-values des articles39duodecies et238octies du code général des impôts sont comprises dans les éléments de résultat suivis par la société selon leur qualification propre.',
    'Leur réalisation ou leur inscription au bilan ne les rend pas distribuées lorsqu’elles restent dans la société. Leur attribution effective aux bénéficiaires est retenue dans la masse des revenus distribués selon les articles109 et110 de ce code et les articles41 et42 de la présente annexe.',
    'L’IS de la société suit le taux et le fait générateur prévus à l’article219 de ce code, avec le suivi des compartiments de l’article209. Le calcul d’un résultat ne déclenche pas un IS ordinaire annuel sur une plus-value conservée.',
    'Pour les périodes antérieures, l’inclusion intégrale au poste de résultat et ses effets sur les distributions restent ceux de la rédaction alors applicable.'
],
    'Conserver le suivi des plus-values tout en supprimant leur assimilation à une distribution par le seul effet du calcul annuel.',
    'Renvois39duodecies et238octies conservés ; les taux spéciaux et exclusions légales sont traités par209/219 et ne sont pas remplacés par un taux normal universel20%.',
    ['Suppression de tout effet automatique de distribution ou d’IS ordinaire annuel résultant de la seule inclusion des plus-values dans le poste résultats pour les périodes nouvelles.'])

add('47',[
    'Une rectification de l’impôt sur les sociétés n’entraîne une correction des revenus distribués que si elle révèle ou modifie une somme ou un avantage effectivement mis à disposition d’un bénéficiaire, ou réputé distribué par une disposition légale distincte.',
    'La correction personnelle est rattachée à la période de cette mise à disposition, dans le respect des délais de reprise et garanties de procédure qui lui sont propres. Elle ne suit pas automatiquement l’année de réalisation du bénéfice rectifié si ce bénéfice a été conservé dans la société.',
    'Le principal d’IS effectivement supporté est pris en compte dans les conditions de l’article110 du code général des impôts, sans double déduction. Aucune correction ne crée un crédit d’impôt personnel fictif.',
    'La règle de rattachement automatique prévue par l’ancienne rédaction demeure appliquée aux seules distributions des périodes antérieures visées à l’article40, selon la version alors en vigueur.'
],
    'Supprimer le redressement automatique de dividendes personnels lorsqu’un bénéfice de société corrigé n’a pas été distribué.',
    'La possibilité de redresser une vraie distribution occulte reste entière. Les délais personnels de reprise et la preuve de mise à disposition ne sont pas remplacés par ceux de la société.',
    ['Suppression du report mécanique de toute rectification du bénéfice IS dans des revenus réputés distribués au titre de la même année.'])

add('379',[
    '1. La société étrangère qui réalise des bénéfices en France sans y avoir son siège déclare la retenue effectivement exigible en vertu de l’article115quinquies du code général des impôts.',
    'Pour les désinvestissements et distributions relevant du régime nouveau de cet article, la déclaration est adressée au service dont relève l’établissement français au plus tard le15 du mois suivant le fait générateur. Elle peut être jointe à la déclaration d’IS de distribution de l’article1668 de ce code ; une donnée commune n’est fournie qu’une fois.',
    '2. La déclaration distingue, en euros, la date et le montant des sommes ou valeurs désinvesties, les apports réels remboursés, les bénéfices protégés d’un second IS, les autres bénéfices concernés, l’IS effectivement dû et la base nette de retenue. Elle indique le taux de retenue appliqué et, le cas échéant, l’exclusion ou la stipulation conventionnelle invoquée.',
    'Aucune retenue ne résulte de la seule réalisation annuelle d’un bénéfice conservé ou réinvesti en France. En l’absence de retenue exigible, aucun versement de retenue n’est demandé ; les justifications des exclusions restent conservées dans les comptes de l’établissement.',
    '3. La retenue exigible est payée au dépôt de la déclaration. Les rectifications et restitutions suivent les articles380 à382. Pour les exercices antérieurs à l’ouverture du nouveau régime, la déclaration et le versement restent soumis aux dispositions alors applicables, notamment au délai de la déclaration annuelle de résultats.'
],
    'Remplacer la retenue annuelle des succursales sur bénéfices fictivement distribués par la déclaration et le paiement des désinvestissements réellement taxables.',
    'Source et ancien projet lus intégralement. La date mensuelle du15 est coordonnée à1668 ; aucun taux de retenue nouveau n’est ajouté. Les droits des conventions, de115quinquies3 et des restitutions restent applicables.',
    ['Suppression de la liquidation annuelle automatique de la retenue sur les bénéfices de succursale française conservés dans l’entreprise pour les faits nouveaux.'])

add('380',[
    'I. La société peut demander une nouvelle liquidation de la retenue de l’article379 lorsqu’elle établit que les sommes retenues excèdent les distributions ou désinvestissements effectivement imposables en application de l’article115quinquies du code général des impôts. Elle n’a pas à attendre la clôture de l’exercice ni l’expiration de douze mois pour corriger une retenue portant sur un fait générateur nouveau.',
    'II. La demande est adressée au service compétent dans les délais de réclamation légalement applicables à la retenue. Elle indique l’identité du redevable, la déclaration et le paiement contestés, ainsi que, pour chaque distribution ou désinvestissement, sa date et son montant en euros calculé au cours des changes du jour de la mise à disposition.',
    'III. La société joint les décisions ou délibérations de distribution et les documents comptables ou bancaires établissant les mouvements réellement exécutés. Les procès-verbaux d’approbation des comptes et leur traduction en français ne sont demandés que dans la mesure nécessaire pour vérifier les éléments invoqués ; un document déjà accessible à l’administration n’est pas produit une seconde fois, mais sa référence est indiquée.',
    'Les remboursements réels ou rectifications ne peuvent donner lieu à une restitution supérieure au principal de retenue effectivement acquitté sur les sommes concernées. La restitution de ce principal est soumise à l’article382 ; le droit de contester séparément une pénalité reste régi par les procédures qui lui sont propres.',
    'IV. Les demandes relatives aux exercices antérieurs demeurent régies par la rédaction alors applicable : les distributions effectives retenues sont celles des douze mois suivant la clôture de l’exercice ou de la période dont les résultats avaient servi à liquider la retenue, quel que soit leur exercice d’origine, et la demande est présentée dans les trois mois suivant ces douze mois. Les droits déjà ouverts ne sont pas raccourcis par la réforme.',
    'La demande concernant un bénéficiaire domicilié ou établi en France reste possible selon les conditions et le délai de l’article381.'
],
    'Permettre la correction d’une retenue indue sans attendre douze mois et supprimer les justificatifs redondants, tout en préservant intégralement les recours anciens.',
    'Les anciens délais12mois+3mois sont expressément maintenus pour les anciennes retenues. Les faits nouveaux suivent la réclamation de droit commun, sans délai réglementaire nouveau plus court.381 garde sa voie distincte bénéficiaireFrance,délai31décembreannée suivante et preuve transfert ;382 maintient limitation auprincipal.',
    ['Suppression de l’attente de douze mois après clôture pour réclamer la correction d’une retenue indue sur les distributions nouvelles.',
     'Suppression du redépôt systématique de documents déjà détenus par l’administration et des justificatifs non nécessaires au contrôle de la demande.'])

out=Path(__file__).parent/'drafts.json'
out.write_text(json.dumps(ROWS,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'articles':len(ROWS),'numbers':[r['number'] for r in ROWS],'characters':sum(len(r['proposed_xml']) for r in ROWS)},ensure_ascii=False))
