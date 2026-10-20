import json
import re
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def plain(xml):
    return unescape(re.sub(r'<[^>]*>', '', xml))


def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)


def paragraphs(xml):
    return [plain(x) for x in re.findall(r'<p>(.*?)</p>', xml, re.S)]


def effect(kind, measure, description, before, after, unit, population,
           conditions, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=conditions,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def put(number, reason, review, assessment, limitations, burdens,
        proposed=None, classification='retained_necessary', effects=None,
        removed=None, repeal_scope=None):
    source = by_number[number]
    obj = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    obj.update(proposed_xml=proposed, reason=reason, review_notes=review,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               classification=classification,
               substantive_impact=dict(version=1, classification=classification,
                   assessment=assessment, scope_limitations=limitations,
                   new_burdens_review=burdens, effects=effects or []))
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal_scope:
        obj.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal_scope)
    answers[number] = obj
    return obj


put('L381-23',
    "Maintien intégral à droit constant après examen du prélèvement : il finance directement la couverture maladie des invalides de guerre et ayants droit visés par L381-20, et non une procédure accessoire. Le plafond aligné sur les fonctionnaires retraités et leurs veuves limite favorablement la cotisation ; la contribution budgétaire prend en charge le complément. Aucun taux nouveau ni transfert de financement n'est décidé ici.",
    "L381-20 a été lu dans le corpus : invalides, veuves, orphelins et autres catégories de victimes de guerre non déjà couvertes. L381-25, également traité, laisse la cotisation des sapeurs-pompiers volontaires concernés à la charge de l'Etat. Les notes emploient l'ancienne dénomination de sapeurs-pompiers communaux non professionnels : ce décalage documentaire ne modifie pas les bénéficiaires du corps actuel. Le taux réglementaire n'est pas fourni par cet article ; aucune baisse chiffrée n'est affirmée.",
    "La source entière, ses deux modes de financement et son plafond favorable sont maintenus. L'examen ne fait apparaître ni déclaration ni agrément autonome à supprimer dans cet article ; aucune réduction n'est comptée.",
    "Le coût et le taux effectivement pratiqué ne sont pas établis par ce lot. Les anciens renvois du code des pensions militaires figurant dans L381-20 ne sont pas présentés comme coordonnés ici.",
    "Aucune charge nouvelle n'est identifiée : aucun taux, dépôt, justificatif ou délai n'est ajouté au financement existant et la prise en charge favorable de L381-25 reste entière.")

put('L381-24',
    "Maintien à droit constant de l'habilitation à organiser les versements aux caisses compétentes. Ce texte ne crée pas une déclaration individuelle supplémentaire ; il assure l'acheminement des financements de L381-23, dont les bénéficiaires de L381-25 restent dispensés personnellement.",
    "Renvoi à L381-23 cohérent avec son maintien dans ce lot. L'extension favorable aux sapeurs-pompiers volontaires et ayants droit résulte de L381-25, sans nouveau versement mis à leur charge. L'habilitation ne démontre par elle-même ni doublon de dépôt ni autorisation préalable à abroger.",
    "La règle entière est conservée pour rendre effectif le paiement des ressources aux caisses. Elle n'est ni réécrite ni comptée comme une simplification ou une baisse de cotisation.",
    "L'article ne donne pas les modalités réglementaires ni les coûts de circulation des fonds. Aucune économie administrative ou nationale n'est déduite de ce seul renvoi.",
    "Aucune charge nouvelle n'est identifiée : l'habilitation existante est conservée sans ajouter de formalité, de registre, d'échéance ou de condition d'accès aux prestations.")

put('L381-25',
    "Maintien intégral de l'extension de couverture aux sapeurs-pompiers volontaires invalides, conjoints non remariés et orphelins répondant aux conditions de rente et d'absence d'autre assurance. La cotisation est supportée par l'Etat. Supprimer ce texte supprimerait une couverture et une prise en charge favorables, sans retirer une charge privée.",
    "La section 5 maintenue fournit la couverture des invalides de guerre ; le deuxième alinéa (1°) de L381-23 porte bien la cotisation prise en charge par l'Etat. Tous les critères de rente, réversion, pension d'orphelin et assurance de la personne ayant recueilli l'orphelin restent conservés pour les futures situations éligibles. L'article 13 de la loi 91-1389, extérieur aux cinq codes, n'est pas fourni intégralement dans ce lot : son contenu ne fait l'objet d'aucune modification supposée.",
    "Les trois catégories et le paiement public de la cotisation sont maintenus sans restriction temporelle nouvelle. Le maintien d'un avantage existant n'est pas compté comme une réduction supplémentaire.",
    "Le taux minimum d'invalidité et le contenu complet de la loi spéciale ne sont pas chiffrés ni réécrits ici. Aucun gain budgétaire n'est démontré par le maintien.",
    "Aucune charge nouvelle n'est identifiée : aucune demande, preuve ou condition supplémentaire n'est ajoutée, et les personnes couvertes ne deviennent pas redevables de la cotisation.")

put('L381-32',
    "Maintien intégral de l'affiliation vieillesse des membres du Conseil économique, social et environnemental. Il s'agit de l'attribution d'un régime de retraite, sans autorisation ni déclaration accessoire dans l'article ; l'abroger ferait perdre son fondement à cette couverture.",
    "La note limite l'application aux membres entrant en fonction à compter du 1er septembre 2023 ; cette transition reste applicable. Un mandat au CESE n'est pas un contrat privé : ni le contrat unique, ni les quinze jours, ni le transfert vers la capitalisation réservé d'abord aux salariés privés ne s'appliquent par ce seul article.",
    "La source entière et sa transition de 2023 restent intactes. Aucune fusion de régimes, baisse de prélèvement ou suppression d'obligation n'est revendiquée.",
    "Les droits des mandats antérieurs à septembre 2023 et le financement des autres régimes ne sont pas modifiés. Aucun rendement ni financement de transition n'est présumé.",
    "Aucune charge nouvelle n'est identifiée : le maintien ne crée ni compte de capitalisation, ni cotisation additionnelle, ni formalité liée au contrat de travail.")

src = by_number['L382-1']['source_xml']
new = replace_once(src, 'articles L. 761-2 et suivants du code du travail',
                   'articles L. 7111-3 à L. 7111-5 du code du travail')
new = replace_once(new, " et qui exercent leur activité depuis au moins trois années civiles", '')
new += "<p>La suppression de la condition de trois années civiles d'activité s'applique aux activités exercées à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsqu'elles ont commencé auparavant. Elle s'applique aux demandes d'affiliation en cours, sans nouvelle demande. Les droits déjà ouverts, les créances, restitutions et recours afférents aux périodes antérieures demeurent régis par les dispositions qui leur sont applicables ; cette suppression n'ouvre pas, à elle seule, de droits rétroactifs pour ces périodes.</p>"
new = replace_once(new, '</p>\n<p>La suppression de la condition', ' La suppression de la condition')
put('L382-1',
    "Réforme de fond : suppression des trois années civiles d'activité exigées des photographes non journalistes relevant des BNC. Les autres conditions professionnelles et fiscales, toutes les branches, la couverture familiale et la saisine favorable de la commission sur refus restent intégralement maintenues. Coordination du renvoi périmé à L761-2 avec les définitions actuelles des journalistes, assimilés et journalistes de communication électronique ; aucune durée d'emploi n'est créée.",
    "Les articles L7111-3, L7111-4 et L7111-5 ont été lus intégralement dans travail.json ; ce sont de nouvelles cibles normatives non fournies dans reference-targets.json, signalées ici sans les ajouter aux reference_checks requis. L311-2 a aussi été lu : la subordination effective continue de relever du régime salarié, quelle que soit la forme du contrat. Les deuxième à quatrième alinéas restent à leur place. La période historique de deux ans de la loi du 1er août 2006 et le champ des revenus photographiques de presse restent inchangés ; ce n'est pas un nouveau délai. R382-16 à R382-16-5, lus, gardent leur rôle de décision, preuve et recours ; ils ne peuvent rétablir le seuil supprimé. L'entrée en vigueur historique au 1er avril 2026 n'est pas la date de cette réforme proposée.",
    "Par rapport à la source officielle entière, le seul minimum de trois années est réellement retiré : un photographe BNC peut accéder au régime sans cette attente. La correction du renvoi journaliste ne constitue pas une seconde réduction.",
    "Les critères de revenu et de qualité d'auteur, les conditions propres aux prestations et le contrôle d'une activité réelle subsistent. L'effet en effectifs, cotisations et prestations n'est pas chiffré ; aucune rétroactivité générale n'est créée.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration ni agrément de remplacement. Le dossier en cours continue sans nouveau dépôt et les vérifications professionnelles et recours déjà prévus restent applicables.",
    proposed=new, classification='material_reduction',
    removed=["Condition d'exercice de l'activité photographique non journalistique pendant au moins trois années civiles avant l'accès au régime."],
    effects=[effect('deadline_reduced', 'artistes-photographes-fin-attente-trois-ans',
        "Retrait du minimum d'activité pour l'affiliation des photographes BNC non journalistes.",
        "Au moins trois années civiles d'activité, outre les conditions de qualité d'auteur et de revenus BNC.",
        "Aucun minimum d'années d'activité ; qualité d'auteur et revenus BNC toujours nécessaires.",
        'other', "Auteurs d'œuvres photographiques non journalistes professionnels relevant des BNC.",
        "Activités à compter de l'entrée en vigueur, y compris commencées auparavant ; demandes en cours sans nouveau dépôt ; périodes antérieures préservées.",
        "Aucun dossier ou justificatif de remplacement ; autres conditions et contrôle inchangés.",
        paragraphs(src)[3], paragraphs(new)[3])])

src = by_number['L382-2']['source_xml']
new = replace_once(src,
    "Les délibérations du conseil d'administration ne deviennent exécutoires que si aucune opposition n'est faite dans un délai et dans les conditions fixées par décret en Conseil d'Etat.",
    "Les délibérations du conseil d'administration deviennent exécutoires dès leur adoption, sans délai préalable d'opposition ni approbation générale. Le cadre financier prévu au 1° du I, les règles propres à l'approbation du budget et les contrôles légaux de régularité et de gestion demeurent applicables.")
new += "<p>La suppression du délai général d'opposition s'applique aux délibérations adoptées à compter de l'entrée en vigueur de la loi portant la présente rédaction et à celles pour lesquelles ce délai court encore à cette date. Elle ne remet pas en vigueur une délibération ayant déjà fait l'objet d'une opposition et ne supprime pas les recours contre celle-ci. Par dérogation au II, jusqu'au 31 décembre 2026, les modalités de fixation de la composition du conseil d'administration restent celles prévues au premier alinéa du présent article dans sa rédaction antérieure à la loi n° 2025-1403 du 31 décembre 2025.</p>"
put('L382-2',
    "Réforme de fond ciblée : suppression du délai général d'opposition qui suspend chaque délibération du conseil. Le contrôle financier spécifique du budget est conservé, ainsi que le cadre financier de l'action sociale, l'agrément de l'association, l'élection professionnelle, la représentation, le médiateur et le rapport public. Le contrôle de toutes les décisions avant exécution se superpose à ces garanties sans nécessité démontrée pour chaque acte.",
    "R382-8-1, lu, fixe actuellement un mois à compter de la transmission : son dernier alinéa est à coordonner, sans créer un nouveau visa ni un nouvel envoi. R382-13, R382-14 et R382-15, lus, conservent respectivement le budget approuvé, les pouvoirs en cas de carence ou d'irrégularité grave et les contrôles sur pièces et place. Ces règles distinctes ne sont pas supprimées par la fin du délai général. R382-8 et R382-8-3/4 conservent représentation, rapport et médiateur. Le I et le II restent numérotés ; la transition de composition jusqu'au 31 décembre 2026, contenue dans la note source, est rendue expresse sans inventer une date de réforme.",
    "La source suspendait toutes les délibérations jusqu'à l'absence d'opposition ; la proposition retire cette suspension générale. Elle conserve le contrôle du budget et ne compte ni le rapport maintenu ni l'agrément initial comme supprimés.",
    "Le délai d'un mois est vérifié dans R382-8-1 mais la durée législative était renvoyée au décret. Les délibérations budgétaires restent soumises à leur approbation propre ; aucun coût net ou solde national n'est établi.",
    "Aucune charge nouvelle n'est identifiée : pas de déclaration ou transmission de remplacement. Les mentions de contrôle et d'approbation budgétaire réservent des dispositifs déjà existants, sans les étendre.",
    proposed=new, classification='material_reduction',
    removed=["Suspension générale de l'exécution des délibérations du conseil pendant le délai administratif d'opposition fixé par décret."],
    effects=[effect('authorization_removed', 'artistes-auteurs-fin-opposition-generale-deliberations',
        "Fin du contrôle préalable général par absence d'opposition aux délibérations.",
        "Chaque délibération attend l'absence d'opposition dans le délai réglementaire, actuellement un mois après transmission.",
        "Exécution dès adoption sans délai général d'opposition ; approbation propre du budget et contrôles de gestion maintenus.",
        'legal_duty', "Association nationale de protection sociale des artistes auteurs et son conseil d'administration.",
        "Nouvelles délibérations et délais encore en cours à l'entrée en vigueur ; oppositions déjà intervenues et recours non effacés.",
        "Aucun visa, déclaration ou rapport de remplacement ; contrôles existants réservés.",
        paragraphs(src)[8], paragraphs(new)[8])])

src = by_number['L382-3']['source_xml']
new = replace_once(src,
    "Ils sont constitués du montant des revenus imposables au titre des bénéfices non commerciaux majorés de 15 % lorsque cette assimilation n'est pas applicable.",
    "Ils sont constitués du montant des revenus imposables au titre des bénéfices non commerciaux, sans majoration, lorsque cette assimilation n'est pas applicable.")
new += "<p>La suppression de la majoration de 15 % s'applique aux cotisations et aux contributions dont l'assiette est définie au troisième alinéa, dues au titre des périodes d'activité courant à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les cotisations et contributions des périodes antérieures, leurs exonérations et prises en charge, les régularisations, restitutions, prescriptions et recours demeurent régis par les règles applicables à ces périodes.</p>"
new += "<p>Pour l'ouverture et le calcul des droits aux prestations du présent régime, le revenu retenu lorsque l'assimilation fiscale à des traitements et salaires n'est pas applicable demeure le montant des revenus imposables au titre des bénéfices non commerciaux majoré de 15 %, dans les limites et selon les conditions propres à chaque prestation. Cette majoration pour les droits aux prestations n'entre pas dans l'assiette des cotisations. Les droits déjà constitués, les exonérations et les prises en charge de cotisations ne sont pas réduits du seul fait de la suppression de la majoration de l'assiette des cotisations. L'option volontaire de cotisation sur l'assiette forfaitaire prévue à l'article L. 382-3-1 reste ouverte.</p>"
put('L382-3',
    "Réforme de fond : retrait de la majoration de 15 % des BNC pour calculer les cotisations des artistes auteurs, sans modifier les taux ni la base brute des droits fiscalement assimilés aux traitements et salaires. L'exclusion AT-MP est conservée. Pour éviter que cette coupe retire simultanément un avantage de prestations, le niveau de revenu retenu pour ouvrir et calculer les droits reste celui majoré de 15 %, avec les limites propres aux prestations. Ce maintien impose de distinguer deux bases ; il n'est pas présenté comme une simplification nette du calcul.",
    "Le 1 quater de CGI 93 fourni a été lu en entier avec sa proposition : l'assimilation fiscale des droits intégralement déclarés par des tiers n'en fait pas des salaires contractuels ; les abattements fiscaux et le revenu BNC imposable ne sont pas remplacés par des recettes brutes. R382-24 à R382-28 et R382-31 à R382-35, lus, doivent appliquer la base sans majoration aux cotisations et la base de droits préservée aux prestations ; ce sont des coordinations réglementaires nécessaires, non des textes déjà réécrits dans ce lot. La baisse de recettes et le coût du maintien des droits sont à établir en LFSS, sans financement ni rendement inventé et sans condition suspensive ajoutée à cette coupe. L6331-65 du travail, lu, renvoie à cette assiette pour sa contribution de 0,35 % ; son effet d'assiette doit être coordonné, sans supprimer la formation ni confondre ce taux avec le CPF-CDD. La CSG et les assiettes propres des régimes complémentaires ne sont pas déclarées réformées par analogie. Nouveau renvoi à L382-3-1, source intégrale du lot mais non cible fournie pour cet article, signalé sans référence_check supplémentaire.",
    "La majoration sociale obligatoire de 15 % des BNC est retirée pour les nouvelles périodes. Les taux restent inchangés et les prestations conservent leur base antérieure ; la distinction cotisations/prestations ajoute une complexité réelle. Le bilan est donc mixed, sans promesse de gain budgétaire net.",
    "Le gain individuel dépend des taux, plafonds, exonérations et prises en charge ; il n'est pas automatiquement 15 % de la cotisation finale. Les coûts de droits maintenus, les renvois réglementaires et les assiettes d'autres prélèvements restent à coordonner et chiffrer.",
    "Aucune déclaration, donnée ou taxe nouvelle n'est créée, mais deux bases doivent désormais être calculées à partir du même BNC : base de cotisation sans majoration et base de prestations avec 15 %. Cette complexité ajoutée est recensée ; le coût administratif et le solde global restent inconnus.",
    proposed=new, classification='mixed',
    removed=["Majoration obligatoire de 15 % des revenus imposables BNC dans l'assiette des cotisations des artistes auteurs pour les périodes nouvelles."],
    effects=[effect('tax_reduced', 'artistes-auteurs-fin-majoration-assiette-bnc',
        "Réduction de l'assiette des cotisations BNC, à taux légaux et réglementaires inchangés.",
        "Assiette égale à 115 % du revenu imposable BNC ; taux de droit commun sous adaptations et plafonds du régime.",
        "Assiette égale à 100 % du même revenu imposable BNC ; mêmes taux et plafonds, option forfaitaire volontaire préservée.",
        'percent', "Artistes auteurs dont les droits ne sont pas assimilés fiscalement aux traitements et salaires.",
        "Périodes d'activité à compter de l'entrée en vigueur ; anciennes dettes et avantages, régularisations et recours préservés.",
        "Pas de prélèvement compensatoire ; base de prestations distincte conservée et coût de financement non établi.",
        "Ils sont constitués du montant des revenus imposables au titre des bénéfices non commerciaux majorés de 15 % lorsque cette assimilation n'est pas applicable.",
        "Ils sont constitués du montant des revenus imposables au titre des bénéfices non commerciaux, sans majoration, lorsque cette assimilation n'est pas applicable."),
        effect('complexity_added', 'artistes-auteurs-fin-majoration-assiette-bnc',
        "Dissociation des bases pour préserver les droits sociaux lors de la réduction de cotisation.",
        "L'assiette BNC majorée de 15 % sert aux cotisations et, par les règlements de prestations, au calcul de droits.",
        "Les cotisations utilisent le BNC non majoré ; l'ouverture et le calcul des prestations gardent le BNC majoré de 15 %.",
        'other', "Organismes liquidant les cotisations et les prestations des artistes auteurs BNC.",
        "Même entrée en vigueur que la réduction, droits constitués et options favorables maintenus.",
        "Double calcul sur le même revenu, sans déclaration supplémentaire ; coût et solde net non établis.",
        "Ils sont constitués du montant des revenus imposables au titre des bénéfices non commerciaux majorés de 15 % lorsque cette assimilation n'est pas applicable.",
        "Cette majoration pour les droits aux prestations n'entre pas dans l'assiette des cotisations.")])

put('L382-3-1',
    "Maintien intégral de la faculté de cotiser volontairement sur une assiette forfaitaire lorsque les revenus artistiques sont trop faibles. Ce n'est pas un plancher obligatoire : cette option ouvre des droits sociaux et son retrait supprimerait un avantage. Elle reste accessible aux futures situations éligibles, même après la baisse d'assiette BNC.",
    "La demande est l'exercice d'une option volontaire, non un agrément à conserver artificiellement. R382-25, R382-26 dernier alinéa et R382-31, lus, relient cette option aux droits et tiennent compte des précomptes déjà effectués. L382-3 proposé réserve expressément cette faculté ; aucun double appel n'est autorisé. La note d'application au plus tard au 1er janvier 2019 n'est pas un calendrier de réforme future.",
    "La totalité de la source demeure : revenus inférieurs au seuil réglementaire et choix de cotiser sur l'assiette correspondante. Aucun minimum imposé n'est créé ni prétendument supprimé.",
    "Le montant fixé par décret et le coût des prestations ne sont pas déterminés ici. Le maintien de l'option ne démontre aucune baisse supplémentaire des prélèvements.",
    "Aucune charge nouvelle n'est identifiée : le cotisant conserve sa liberté d'opter et aucune cotisation minimale obligatoire, attestation ou condition supplémentaire n'est ajoutée.")

put('L382-3-2',
    "Maintien intégral de la régularisation dans les quatre mois lorsque les revenus annuels cumulés dépassent le plafond. Cette garantie évite les excès de cotisations plafonnées et bénéficie aux situations futures ; le délai maximal n'est pas un délai minimal imposé à l'assuré.",
    "L241-3 fourni définit le plafond au premier alinéa officiel, devenu premier alinéa du I dans sa proposition : le renvoi à l'article conserve un objet identifiable et ne nécessite pas de déplacement. Le II de sa proposition ne transfère vers la capitalisation que les salariés privés visés, pas automatiquement les revenus d'auteur. R382-26, lu, préserve les remboursements automatiques, l'articulation avec les salaires, le plafond unique et la cotisation déplafonnée ; la déclaration de revenus visée n'est pas une nouvelle déclaration créée par ce texte. La note au 1er janvier 2026 reste sa portée historique.",
    "La source entière protège une régularisation obligatoire sous quatre mois. La garantie est conservée ; ni un report de paiement ni une nouvelle baisse de taux ne sont revendiqués.",
    "Ce plafond ne concerne pas la cotisation assise sur la totalité des revenus. Aucun gain de trésorerie nouveau ni effet sur les droits futurs de salariés soumis à un autre volet de réforme n'est calculé.",
    "Aucune charge nouvelle n'est identifiée : le délai existant et le déclencheur déclaratif sont maintenus, sans nouvelle demande d'autorisation ni procédure de capitalisation des revenus d'auteur.")

put('L382-4',
    "Maintien intégral de la contribution des diffuseurs qui tient lieu de financement des charges patronales d'assurances sociales et de prestations familiales. Sa fonction est le financement mutualisé de ces risques et de l'action sociale de L382-7, et non une cotisation accessoire de dossier. La supprimer ici sans traiter ces droits et cette affectation retirerait leur ressource dédiée. Les bases alternatives selon les œuvres et opérations sont conservées sans extension.",
    "R382-17 et R382-18 ont été lus : la base des ventes graphiques et plastiques retient notamment 30 % du prix ou la commission, et le taux relève d'un arrêté non fourni ; aucun taux n'est inventé. R382-30-1 et R382-37 confirment les affectations sociales. La mention d'artistes morts vise la diffusion commerciale, non la transmission gratuite par décès : la suppression des droits de succession n'abroge pas ce prélèvement par assimilation. Les contributions de formation et le CPF-CDD restent distincts. Aucun rapport ni agrément n'est imposé par cet article lui-même.",
    "Le financement social et ses deux branches d'assiette sont conservés après examen intégral. Aucune taxe nouvelle, taxe supprimée ou baisse fictive fondée sur le seul décès de l'auteur n'est comptée.",
    "L'utilité de cette ressource est identifiée par les risques et l'action sociale financés ; son rendement, son taux d'arrêté et un financement alternatif ne sont pas établis. Aucune compensation n'est présumée.",
    "Aucune charge nouvelle n'est identifiée : le champ des diffuseurs, les catégories d'œuvres et les bases prévues restent identiques, sans dépôt, prélèvement ou autorisation de remplacement.")

put('L382-5',
    "Maintien intégral des modalités de versement et du précompte, nécessaires au recouvrement unique et à l'attribution des droits des auteurs. Les trois alinéas distinguent la part de l'auteur, le précompte par le diffuseur et les contributions propres du diffuseur et de formation. Aucun paiement supplémentaire n'est créé et aucune contribution existante n'est confondue avec le CPF-CDD supprimé ailleurs.",
    "L213-1 et L382-1 fournis confirment les organismes et personnes ; L6331-65 du travail a été lu dans le corpus : contributions de formation de 0,35 % pour l'auteur et 0,1 % pour le diffuseur, distinctes du CPF-CDD de 1 %. R382-26 et R382-27, lus, préservent la dispense de précompte BNC, les plafonds, remboursements et l'acquit résultant de la retenue. Ce maintien du texte légal ne ferme pas ces dérogations aux futurs bénéficiaires. R382-19, lu, contient un agrément ministériel propre aux conventions de tiers habilités, absent de cet article : son examen réglementaire est à traiter séparément et aucune suppression de cet agrément n'est comptée ici.",
    "Les trois règles de recouvrement restent entières. Le précompte est une modalité de règlement d'une dette existante ; ni lui ni le renvoi à une contribution ne sont présentés comme une nouvelle réduction.",
    "Les formulaires, conventions des tiers et arrêtés de dispense ne sont pas tous réécrits dans ce lot. L'effet de la réduction d'assiette BNC relève de L382-3 et ne devient pas une seconde baisse dans cet article de recouvrement.",
    "Aucune charge nouvelle n'est identifiée : pas de second paiement, dossier ou registre ajouté ; les dispenses et l'acquit du précompte existants restent applicables.")

src = by_number['L382-6']['source_xml']
oldp = paragraphs(src)[0]
newp = "Les personnes redevables des cotisations et contributions sociales mentionnées aux articles L. 382-3 et L. 382-4 peuvent effectuer les déclarations et les versements afférents à ces cotisations et contributions par voie dématérialisée ou par les autres moyens légalement admis. Le choix d'un moyen non dématérialisé n'est subordonné ni à une autorisation ni à la justification d'une impossibilité d'utiliser la voie dématérialisée. Il ne donne pas lieu aux majorations prévues au II de l'article L. 133-5-5. Les personnes qui ne sont pas en mesure de procéder par voie dématérialisée conservent la faculté de déclarer et de payer par les autres moyens légalement admis, sans être tenues de signaler cette impossibilité. Les informations à déclarer, les échéances et le principal des cotisations et contributions restent inchangés."
newp = replace_once(newp,
    "Les informations à déclarer, les échéances et le principal des cotisations et contributions restent inchangés.",
    "Le choix du moyen utilisé ne modifie ni les informations à déclarer, ni les échéances, ni le montant des cotisations et contributions dû en application des règles d'assiette, de taux, de plafond et d'exonération en vigueur.")
new = replace_once(src, re.findall(r'<p>(.*?)</p>', src, re.S)[0], newp)
new += "<p>La liberté de choix du moyen de déclaration et de versement s'applique aux démarches et paiements effectués à compter de l'entrée en vigueur de la loi portant la présente rédaction, y compris lorsqu'ils portent sur des périodes antérieures. Elle ne dispense pas de régulariser les informations ou les sommes légalement dues. Les majorations fondées sur le seul emploi d'un moyen non dématérialisé avant cette date restent soumises aux règles qui leur sont applicables, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.</p>"
obj = put('L382-6',
    "Réforme de fond : la voie électronique devient un choix, sans justification d'une impossibilité ni autorisation pour employer une autre voie légale. Les majorations spécifiques au support non dématérialisé cessent pour les démarches futures. L'obligation utile de déclarer et payer subsiste, ainsi que l'identification des auteurs au deuxième alinéa ; l'exemption antérieure des personnes empêchées est conservée et élargie à tous les redevables.",
    "Le II de L133-5-5, lu dans le corpus, sanctionne distinctement déclaration et paiement non dématérialisés ; seul son emploi par renvoi au titre du support est écarté ici, sans supprimer les sanctions de fraude, de données absentes ou de paiement tardif ayant un fondement autonome. L114-12-1 fourni a été lu en entier : son avant-dernier alinéa est bien le NIR, avec identification réglementaire des personnes qui en sont dépourvues au dernier alinéa. Aucun nouvel accès au répertoire n'est accordé aux diffuseurs. R382-20 et R382-28 doivent ouvrir les mêmes canaux sans nouvelle attestation ; leurs textes sont lus mais non réécrits dans ce lot. Le réemploi de données déjà accessibles n'est pas compté comme un gain CRPA nouveau. L'obligation d'identifier reste au deuxième alinéa.",
    "La source imposait le support électronique sauf déclaration d'impossibilité ; la proposition retire l'obligation de support et cette déclaration, ainsi que la sanction propre à ce support pour l'avenir. Le contenu et les échéances ne sont pas allégés par cette seule mesure.",
    "Les moyens de paiement restent ceux légalement admis : aucun paiement anonyme ou sans identification n'est créé. Les coûts de traitement du papier et le solde financier ne sont pas mesurés ; aucune baisse de cotisation n'est revendiquée.",
    "Aucune obligation nouvelle n'est identifiée : pas de déclaration d'option ni de justificatif de remplacement. Les organismes devront accepter les voies légales existantes ; le coût de leur traitement demeure non chiffré, sans nouveau rapport obligatoire.",
    proposed=new, classification='material_reduction',
    removed=["Obligation de recourir à la voie dématérialisée pour les déclarations et versements des auteurs et diffuseurs, avec signalement d'impossibilité pour en être dispensé.",
             "Application aux diffuseurs des majorations spéciales sanctionnant le seul recours à un support non dématérialisé pour déclarer ou payer."],
    effects=[effect('obligation_removed', 'artistes-auteurs-libre-support-declarations-paiements',
        "Retrait de l'exclusivité électronique et de la démarche pour bénéficier d'une autre voie légale.",
        "Voie dématérialisée obligatoire ; dérogation après indication à l'Urssaf d'une impossibilité ; majorations spécifiques pour les diffuseurs.",
        "Choix entre voie dématérialisée et autres voies légalement admises, sans indication d'impossibilité ni majoration liée au seul support.",
        'legal_duty', "Artistes auteurs et diffuseurs redevables des cotisations et contributions de L382-3 et L382-4.",
        "Démarches et paiements après entrée en vigueur, y compris sur anciennes périodes ; principal et données dus conservés ; loi répressive plus douce réservée.",
        "Aucune autorisation ni déclaration équivalente ; échéances et identification inchangées, coût public de traitement non évalué.",
        oldp, newp)])
obj['benefit_review'] = "La dérogation source dispense expressément les auteurs et diffuseurs qui indiquent ne pas pouvoir déclarer ou payer en ligne. Cet avantage reste ouvert à toutes leurs démarches futures et est élargi : ils utilisent une autre voie légale sans signalement d'impossibilité. Le choix est ouvert aussi aux autres redevables et aucune majoration ne sanctionne désormais le seul support futur. Les délais de droit commun, dispenses de précompte, plafonds et autres exonérations ne sont pas retirés ; l'identification NIR conservée protège l'attribution des droits et n'est pas une taxe ni un avantage fiscal supprimé. La réserve de loi répressive plus douce protège les sanctions antérieures non définitives sans amnistier le principal."

put('L382-7',
    "Maintien intégral de l'action sanitaire et sociale des artistes auteurs et de son financement sur une fraction de la contribution des diffuseurs. C'est un fondement d'aides, pas un état annuel de protection complémentaire à supprimer. Les futurs auteurs éligibles, dont les photographes nouvellement admis sans trois ans d'attente, restent couverts.",
    "L213-1 désigne l'Urssaf chargée de mettre en œuvre les orientations de L382-2. Le cadre financier, l'association agréée et la contribution de L382-4 subsistent dans ce lot. R382-30-1/2, lus, précisent prises en charge, fraction de 2 % du montant recouvré l'année précédente, critères et règlement d'action sociale : ces conditions réglementaires ne sont ni résumées comme supprimées ni réécrites ici. R382-30-3 lu renvoie à R382-20-2 alors que les dispositions actuelles lues sont R382-30-1/2 : incohérence réglementaire préexistante signalée, sans correction silencieuse. L'application historique au 1er juin 2026 demeure.",
    "La source entière, qui ouvre l'action sociale et lui affecte une ressource, demeure utile. Aucun rapport, prélèvement ou agrément n'est supprimé dans cet article et aucun gain nouveau n'est compté.",
    "Les décisions individuelles d'aide, leur coût et le règlement approuvé ne sont pas tous fournis. Le financement ne devient pas une recette de compensation des autres réformes.",
    "Aucune charge nouvelle n'est identifiée : les droits et le circuit existants sont maintenus sans nouvelle attestation, sans restriction aux anciens bénéficiaires et sans rapport supplémentaire.")

src = by_number['L382-9']['source_xml']
new = "<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant cette abrogation.</p><p>À compter de cette date, le règlement des prestations en espèces des assurances maladie et maternité des artistes auteurs ne peut être refusé ou suspendu au seul motif que l'assuré n'est pas à jour de ses cotisations. Cette règle s'applique aux prestations afférentes aux périodes postérieures à cette date ainsi qu'aux demandes de règlement encore en cours à cette date, même si elles portent sur des périodes antérieures. Les autres conditions d'ouverture et de calcul des droits restent applicables.</p><p>Les cotisations légalement dues, leur recouvrement, les régularisations, prescriptions et recours subsistent selon les règles qui leur sont applicables ; aucun nouveau paiement préalable de ces dettes ne conditionne le versement des prestations. Les prestations déjà acquises restent dues. Les décisions antérieures devenues définitives ne sont pas rouvertes du seul fait de cette abrogation ; les recours et restitutions encore ouverts sont préservés, sans remboursement général ni double versement.</p>"
put('L382-9',
    "Abrogation de fond de la condition d'apurement des cotisations pour recevoir les prestations maladie et maternité. Le recouvrement dispose de ses voies propres et le blocage du revenu de remplacement, notamment de maternité, n'est pas conservé comme moyen de recouvrement supplémentaire. Les conditions médicales et d'ouverture des droits distinctes, les dettes réellement dues et les recours restent applicables.",
    "La suppression s'étend aux demandes de règlement pendantes pour éviter d'exiger encore l'apurement d'une dette sur un dossier déjà constitué. Elle ne crée ni droits sans condition d'affiliation ou de ressources ni reprise des décisions définitives. R382-31 à R382-35, lus, concernent seuils, affiliations, calcul et carence distincts ; ils ne sont pas abrogés par cette mesure. L382-14 est coordonné dans ce lot pour empêcher qu'un décret reconstitue le blocage supprimé. Les règles d'acquit par précompte de R382-27 restent favorables et applicables.",
    "La source entière consistait dans une condition supplémentaire de paiement préalable. Cette condition disparaît réellement ; la dette de cotisations n'est pas supprimée et l'effet est une extension d'accès au versement des prestations, non une baisse de taux.",
    "L'effet sur le versement des prestations et sur le recouvrement est à évaluer. Les autres conditions sociales et médicales et les refus antérieurs définitifs restent hors de la suppression ; aucune économie nationale n'est chiffrée.",
    "Aucune charge nouvelle n'est identifiée : aucune attestation de régularité, déclaration de remplacement ou garantie de dette n'est créée. Le traitement des demandes relève des organismes déjà compétents, sans droit à un double paiement.",
    proposed=new, classification='material_reduction',
    repeal_scope="Suppression de la condition d'être à jour de ses cotisations pour le règlement des prestations en espèces des assurances maladie et maternité des artistes auteurs, pour les nouvelles périodes et les demandes de règlement encore en cours, avec maintien des dettes et des autres conditions de droits.",
    effects=[effect('relief_extended', 'artistes-auteurs-prestations-sans-blocage-paiement',
        "Versement maladie et maternité indépendant du seul défaut d'apurement des cotisations.",
        "L'assuré doit être à jour de ses cotisations pour obtenir le règlement des prestations en espèces maladie et maternité.",
        "Le seul impayé de cotisations ne permet plus de refuser ou suspendre le règlement ; autres conditions de droits et dettes conservées.",
        'legal_duty', "Artistes auteurs remplissant les autres conditions des prestations en espèces maladie et maternité.",
        "Périodes nouvelles et demandes en cours à l'entrée en vigueur ; décisions définitives non rouvertes et recours existants conservés.",
        "Pas de formalité compensatoire ; coût de prestations et effet de recouvrement non établis.",
        paragraphs(src)[0], paragraphs(new)[1])])

src = by_number['L382-10']['source_xml']
new = replace_once(src,
    "L'article L. 351-14 n'est pas applicable aux personnes mentionnées à l'article L. 382-1.",
    "Les personnes mentionnées à l'article L. 382-1 peuvent demander l'application de l'article L. 351-14 dans les conditions prévues par cet article, sans double validation d'une même période déjà prise en charge au titre des alinéas suivants.")
new += "<p>La faculté prévue au premier alinéa est ouverte aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente rédaction ainsi qu'à celles encore en cours à cette date. Elle n'impose aucun rachat ni versement nouveau aux personnes qui ne l'exercent pas. Elle ne remet en cause ni les droits pris en charge depuis le 1er janvier 1977 ni les liquidations devenues définitives ; les révisions, restitutions et recours prévus par les dispositions applicables restent ouverts.</p>"
put('L382-10',
    "Réforme de fond limitée au premier alinéa : retrait de l'exclusion générale des artistes auteurs du rachat de périodes antérieures à leur affiliation obligatoire prévu par L351-14. Le rachat est volontaire et soumis aux conditions communes, sans double validation. Les trois alinéas qui protègent depuis 1977 les droits anciens des professions libérales, l'assurance maladie des pensionnés et la prise en compte des cotisations antérieures restent intégralement conservés.",
    "L351-14, lu en entier dans le corpus avec sa note, vise les périodes antérieures à l'affiliation obligatoire d'une catégorie, y compris certaines révisions après liquidation, et renvoie aux cotisations de L351-14-1. Il ne s'agit ni de valider gratuitement toute période ni d'ouvrir un deuxième droit pour des périodes déjà reprises par le présent article. L351-14-1 n'a pas été fourni parmi les cibles : son contenu n'est pas inventé, et les modalités du rachat restent celles légalement applicables. Ce n'est pas une capitalisation privée et la date du 1er janvier 1977 reste historique. Nouveau renvoi affirmatif à L351-14, auparavant cité négativement, signalé hors de la liste des cibles requises ; la source complète de L351-14 a été lue.",
    "L'exclusion entière d'un mécanisme volontaire est retirée ; les garanties historiques sont maintenues mot pour mot. Il s'agit d'une ouverture d'option favorable, sans réduction annoncée du prix du rachat ni création de trimestre gratuit.",
    "Le nombre de périodes encore rachetables, leur coût et les effets actuariels ne sont pas établis. L'absence de double validation et les conditions communes demeurent ; aucun droit antérieur pris en charge ne disparaît.",
    "Aucune charge obligatoire nouvelle n'est identifiée : la demande et les cotisations de rachat ne concernent que l'assuré qui exerce volontairement le dispositif existant. Aucun justificatif spécial ou agrément de remplacement n'est ajouté.",
    proposed=new, classification='material_reduction',
    removed=["Exclusion générale des artistes auteurs de la faculté de rachat des périodes antérieures à l'affiliation obligatoire prévue par l'article L351-14."],
    effects=[effect('relief_extended', 'artistes-auteurs-ouverture-rachat-periodes-anterieures',
        "Ouverture du rachat volontaire auparavant exclu pour cette catégorie.",
        "L351-14 est inapplicable à toutes les personnes relevant de L382-1.",
        "L351-14 peut être demandé aux conditions communes, sans doubler les périodes déjà prises en charge depuis 1977.",
        'regime', "Artistes auteurs ayant des périodes éligibles au dispositif de L351-14 non déjà prises en charge.",
        "Demandes nouvelles ou en cours ; maintien des droits de 1977 et des décisions définitives sous réserve des révisions légales.",
        "Option et paiement de rachat préexistants étendus, non imposés ; pas de nouveau dossier spécial ni tarif inventé.",
        "L'article L. 351-14 n'est pas applicable aux personnes mentionnées à l'article L. 382-1.",
        "Les personnes mentionnées à l'article L. 382-1 peuvent demander l'application de l'article L. 351-14 dans les conditions prévues par cet article, sans double validation d'une même période déjà prise en charge au titre des alinéas suivants.")])

put('L382-12',
    "Maintien intégral des régimes complémentaires vieillesse des artistes auteurs. Sont conservés le précompte audiovisuel, la fraction à la charge du producteur, le raccordement des catégories non couvertes en 2003 et la prise en charge d'une fraction de cotisation des auteurs de livres par la rémunération du prêt en bibliothèque, jusqu'à la moitié. Ces mécanismes financent une retraite et des aides ciblées, non une formalité accessoire sans objet.",
    "L644-1 a été lu dans le corpus : le renvoi porte sur l'institution des régimes complémentaires, pas sur la capitalisation proposée pour les salariés privés de L241-3. Les contrats d'édition et de production de la propriété intellectuelle sont distincts de contrats de travail. Les articles CPI L132-23/24 et L133-3/4 ne sont pas fournis intégralement dans le périmètre local autorisé et ne sont donc pas présentés comme entièrement vérifiés ; leurs renvois, la condition de plus de la moitié des revenus et le maximum d'une moitié de cotisations restent intacts. Les aides restent ouvertes pour de futures œuvres et personnes éligibles. L133-4 CSS fourni dans les cibles traite les indus médicaux et n'est pas le L133-4 CPI cité : aucune substitution de code n'est opérée.",
    "La totalité des quatre alinéas, avec leurs prises en charge et leur financement, est conservée. Aucun transfert vers la capitalisation ni baisse de cotisation n'est attribué à ce maintien de garanties complémentaires.",
    "Les paramètres par décret, les accords de producteurs et les textes CPI extérieurs restent à leur champ propre. Ni le montant des aides ni l'effet des autres réformes d'assiette sur chaque régime complémentaire ne sont établis ici.",
    "Aucune charge nouvelle n'est identifiée : les précomptes existants et les participations du producteur et du prêt en bibliothèque sont conservés sans nouvelle condition d'emploi ou de durée de contrat.")

src = by_number['L382-14']['source_xml']
new = src + "<p>Les modalités ainsi fixées respectent la distinction entre l'assiette des cotisations et le revenu retenu pour l'ouverture et le calcul des prestations prévue à l'article L. 382-3. Elles ne peuvent rétablir la condition de trois années civiles d'activité supprimée à l'article L. 382-1, imposer la voie dématérialisée en méconnaissance de l'article L. 382-6 ni subordonner le règlement des prestations en espèces des assurances maladie et maternité au seul fait d'être à jour des cotisations. Cette dernière interdiction s'applique dans le champ temporel de l'abrogation de l'article L. 382-9. Les autres conditions d'ouverture des droits, règles de calcul, délais de carence et contrôles ayant un fondement distinct restent applicables.</p>"
put('L382-14',
    "Coordination nécessaire des pouvoirs réglementaires avec les réformes des articles L382-1, L382-3, L382-6 et l'abrogation de L382-9. Les deux alinéas d'habilitation restent intégralement maintenus ; le décret ne peut recréer le délai photographique, l'exclusivité électronique ou le blocage pour impayé, et doit préserver la base des prestations dissociée de celle des cotisations. Les délais de carence et conditions médicales distinctes ne sont pas supprimés implicitement.",
    "Les articles R382-20/28, R382-31 à R382-35 et les dispositions de gouvernance ont été lus pour délimiter les coordinations. Le délai du point de départ de l'incapacité est la carence maladie de R382-33 renvoyant à R323-1, distincte des trois années photographiques et des quinze jours de préavis privé. Les obligations de chiffre d'affaires restent nécessaires au calcul de L382-4 maintenu ; les doublons réglementaires éventuels, notamment récapitulatif annuel R382-20 après déclarations trimestrielles, ne sont pas comptés comme supprimés par cet article. Les renvois ajoutés à L382-1/3/6/9 portent sur des sources intégrales du lot, non sur des cibles fournies pour cet article ; ils sont signalés ici. Aucun article réglementaire non assigné n'est présenté comme réécrit.",
    "Cet ajout borne l'habilitation afin qu'elle n'annule pas les mesures de fond du même lot. Il n'est pas une seconde suppression de chacune des contraintes déjà retirées et ne modifie pas les autres champs réglementaires.",
    "Les coordinations réglementaires restent à transcrire dans leurs véritables articles, et le coût des droits préservés doit être évalué. Aucun solde financier ou gain autonome de formalité n'est démontré ici.",
    "Aucune charge nouvelle autonome n'est identifiée : pas de registre, dépôt ni délai ajouté. La distinction des bases reprend exactement celle créée par L382-3 ; sa complexité est recensée une seule fois dans cet article de fond.",
    proposed=new, classification='coordination_only',
    effects=[effect('coordination', 'artistes-auteurs-prestations-sans-blocage-paiement',
        "Empêcher l'habilitation réglementaire de rétablir le blocage pour impayé supprimé à L382-9.",
        "Habilitation générale aux conditions de droits et de recouvrement, articulée avec la condition de paiement de L382-9.",
        "Habilitation maintenue avec interdiction de rétablir ce blocage ; autres conditions, carence et contrôles distincts inchangés.",
        'legal_duty', "Organismes et pouvoir réglementaire appliquant le régime social des artistes auteurs.",
        "Même champ temporel que L382-9 abrogé ; les autres réformes du lot gardent leurs transitions propres.",
        "Aucun dépôt ou contrôle de remplacement ; aucune deuxième réduction imputée à ce renvoi.",
        paragraphs(src)[0], paragraphs(new)[2])])

put('L382-14-1',
    "Maintien intégral du rattachement social des revenus journalistiques de L132-42 CPI au régime des auteurs, avec exclusion favorable des cotisations AT-MP. La nature de cette rémunération d'exploitation n'est pas celle d'une indemnité ordinaire de rupture ni d'un emploi temporaire ; aucun nouveau CDD n'est autorisé par ce texte.",
    "Le renvoi à la propriété intellectuelle est conservé à son champ de rémunération ; le texte intégral de L132-42 CPI n'est pas fourni dans les cinq codes locaux et n'est pas reconstitué par inférence. La réforme d'assiette de L382-3 s'applique dans son champ réel, sans prétendre que toutes les rémunérations journalistiques deviennent des BNC. L'exception AT-MP reste ouverte aux futurs revenus éligibles et les droits existants ne sont pas supprimés.",
    "La source entière rattache des revenus à une couverture et exclut un risque de l'assujettissement. Son maintien n'est ni une suppression de cotisation nouvelle ni une réécriture stylistique.",
    "Le régime du salaire journalistique et les conditions de la rémunération CPI restent distincts. Aucune baisse de CSG salariale ni capitalisation des revenus d'auteur n'est transposée par analogie.",
    "Aucune charge nouvelle n'est identifiée : aucun contrat, agrément, justificatif ou prélèvement supplémentaire n'est ajouté à ce rattachement existant.")

src = by_number['L382-15']['source_xml']
oldp = paragraphs(src)[1]
newp = "L'affiliation est prononcée par l'organisme de sécurité sociale prévu à l'article L. 382-17, sans consultation préalable de la commission consultative instituée auprès de l'autorité compétente de l'Etat, qui comprend des représentants de l'administration et des personnalités choisies en raison de leur compétence, compte tenu de la diversité des cultes concernés. Cette commission conserve sa mission consultative générale ; aucun de ses avis ne conditionne ni ne suspend la décision d'affiliation."
new = replace_once(src, re.findall(r'<p>(.*?)</p>', src, re.S)[1], newp)
new += "<p>La suppression de la consultation préalable à l'affiliation s'applique aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente rédaction et à celles en cours à cette date, sans nouveau dossier ni reprise des délais. Les décisions prises antérieurement, les droits acquis et les recours restent régis par les dispositions qui leur sont applicables. La vérification des conditions légales d'affiliation, les obligations de motivation et les voies de recours sont maintenues.</p>"
put('L382-15',
    "Réforme de fond ciblée : retrait du passage consultatif préalable à l'affiliation des ministres des cultes, membres des congrégations et collectivités. La caisse vérifie et décide directement. La commission conserve ses avis généraux de L382-19, sa composition pluraliste et les possibilités de saisine sur les problèmes du régime ; seul son rôle dans le circuit individuel préalable disparaît. Le champ subsidiaire par rapport aux autres régimes et l'exclusion de l'affiliation au seul titre de la résidence restent intacts.",
    "R382-56 à R382-69 ont été lus : la commission est consultative, le ministre la saisit et la CAVIMAC reste l'organisme d'affiliation. Le conseil pluraliste de L382-17, le contrôle et le contentieux de L382-20 demeurent. Il ne s'agit pas d'abroger la commission ni ses remboursements et indemnités de mission. R382-57 maintient les conditions d'affiliation et situations de temps partiel, qui ne sont pas remplacées par le contrat privé. Le deuxième alinéa demeure celui qui institue et décrit la commission : le renvoi de L382-19 reste cohérent. La consultation est actuellement éventuelle, non générale ; aucune durée chiffrée gagnée n'est affirmée.",
    "Le recours éventuel à un avis préalable cesse d'appartenir à la procédure d'affiliation. La mission générale de conseil est conservée, ainsi que les critères sociaux et les recours ; la réduction ne concerne que les dossiers qui auraient été soumis à cette étape.",
    "Aucun délai légal de cette consultation n'est chiffré dans la source. La décision de la caisse peut encore exiger les vérifications nécessaires ; aucun droit automatique à l'affiliation ni délai garanti de quinze jours n'est créé.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration ni visa de remplacement, ni nouveau dossier pour les demandes en cours. La commission existante conserve ses attributions générales sans nouvelle mission obligatoire.",
    proposed=new, classification='material_reduction',
    removed=["Consultation éventuelle de la commission auprès de l'Etat au sein de la procédure préalable à la décision individuelle d'affiliation au régime des cultes."],
    effects=[effect('obligation_removed', 'cultes-fin-consultation-prealable-affiliation',
        "Retrait d'une étape consultative individuelle sans supprimer les avis généraux utiles du régime.",
        "Affiliation prononcée par la caisse, s'il y a lieu après consultation de la commission auprès de l'Etat.",
        "Décision directe de la caisse sans consultation préalable ; avis généraux de la commission sans effet suspensif sur l'affiliation.",
        'legal_duty', "Demandeurs d'affiliation relevant du régime des cultes dont le dossier aurait nécessité la consultation éventuelle.",
        "Dossiers nouveaux et en cours à l'entrée en vigueur, sans nouveau dépôt ; droits antérieurs et recours préservés.",
        "Vérifications de fond et motivation existantes conservées ; aucune procédure équivalente créée.",
        oldp, newp)])

put('L382-16',
    "Maintien intégral de la continuité de couverture des personnes du régime des cultes temporairement détachées à l'étranger. L'engagement des associations, congrégations et collectivités de payer les cotisations permet de garantir ce maintien ; ce n'est pas un agrément supplémentaire. Supprimer le texte retirerait une dérogation favorable aux futurs détachements.",
    "L382-15 et L382-17 demeurent les fondements de l'affiliation et de l'organisme. La durée maximale est réglementaire : l'article ne fournit aucun nombre à raccourcir ou à remplacer. Les règles européennes de coordination et conventions internationales, si applicables à un détachement, nécessitent leur propre examen et ne sont pas réputées abrogées par ce maintien national. Les personnes concernées ne sont pas transformées en salariés privés et le préavis de quinze jours n'est pas une durée de détachement.",
    "La règle entière protège une continuité d'assurance sous financement assuré. L'engagement contributif est conservé avec l'avantage qu'il conditionne, sans en réserver le bénéfice aux détachements déjà engagés.",
    "La durée du décret et les situations internationales individuelles ne sont pas établies ici. Aucune suppression de cotisation, baisse de taux ou économie nationale n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucun justificatif, agrément ou durée minimale ne s'ajoute à l'engagement de paiement déjà prévu pour conserver la couverture.")

put('L382-17',
    "Maintien intégral de la CAVIMAC, de ses missions de prestation et d'action sociale, de ses quatre sections et de sa gouvernance tenant compte de la pluralité des cultes. La séparation des flux et le contrôle de l'Etat protègent des financements sociaux ; aucune double déclaration privée ou autorisation d'exercice n'est créée par cet article. Le supprimer ne constituerait pas une simple suppression de doublon.",
    "Les quatre sections sont conservées exactement : assurance maladie, maternité et invalidité ; assurance vieillesse ; action sanitaire et sociale ; gestion administrative. La fixation préalable du financement de l'action sociale appartient à la programmation du budget du régime, non à une condition nouvelle d'aide individuelle. Les notes sur les périodes à compter du 1er janvier 2023 et sur les reports ou anticipations limités à deux ans restent des transitions historiques des lois citées, sans nouvelle date de réforme. La suppression du visa des conventions à L382-18 ne supprime pas le contrôle de l'Etat de ce texte.",
    "L'organisme, les assurances, l'action sociale et les garanties de gouvernance restent entiers. Aucune fusion de caisse, économie de fonctionnement ou baisse de prélèvement n'est prétendue démontrée.",
    "L'organisation par décret et le coût des sections ne sont pas chiffrés. La réforme de capitalisation des salariés privés n'est pas étendue automatiquement aux ministres des cultes ou aux membres religieux.",
    "Aucune charge nouvelle n'est identifiée : les sections et le budget existants restent applicables sans nouveau registre, reporting ou contribution, et le contrôle de l'Etat n'est pas étendu.")

src = by_number['L382-18']['source_xml']
new = replace_once(src,
    "Ces conventions sont soumises à l'approbation des ministres chargés de la sécurité sociale et du budget.",
    "Ces conventions prennent effet dès leur signature, sans approbation ministérielle préalable. Le contrôle de l'Etat sur les organismes, les règles budgétaires et comptables et les affectations légales des cotisations demeurent applicables.")
new += "<p>La suppression de l'approbation ministérielle s'applique aux conventions signées à compter de l'entrée en vigueur de la loi portant la présente rédaction. Les conventions déjà signées dont l'approbation est encore en cours prennent effet à cette date sans nouvelle signature. Les conventions déjà approuvées, leurs engagements valables, les prestations, créances, prescriptions et recours antérieurs restent régis par les dispositions qui leur sont applicables. Aucune nouvelle transmission, déclaration ou autorisation ne se substitue à l'approbation supprimée.</p>"
put('L382-18',
    "Réforme de fond : suppression de l'approbation ministérielle des deux conventions de financement et de reversement entre organismes. Les signatures des organismes engagent les parties sans second visa ; le contrôle de l'Etat de L382-17 et les règles de finances sociales demeurent. Le contenu utile des deux conventions, les ressources des prestations, de l'action sociale et de gestion et les reversements de cotisations sont conservés intégralement.",
    "La première convention associe ACOSS, CNAV et CAVIMAC ; la seconde, de même nature, associe ACOSS, CNAM et CAVIMAC. L382-25, lu dans le corpus avec sa note, maintient les cotisations forfaitaires, contributions et possibilité favorable de répartition selon les capacités contributives : ni taux ni assiette ne sont modifiés par la disparition du visa. Les modalités réglementaires et conventions de financement existantes devront être coordonnées uniquement pour retirer cette approbation, sans les déclarer déjà réécrites. Aucun financement de compensation ni pouvoir de dépense hors budget n'est créé.",
    "Le seul contrôle préalable ministériel propre à ces conventions disparaît réellement. Les obligations de conclure les deux conventions et d'assurer leurs flux restent, sans prétendre qu'il s'agit d'une suppression de cotisations.",
    "Le délai d'approbation et les coûts administratifs ne sont pas quantifiés par la source. Les normes budgétaires et contrôles autonomes subsistent ; le solde national de complexité n'est pas établi.",
    "Aucune charge nouvelle n'est identifiée : aucune transmission, déclaration, autorisation ou délai de remplacement. Les signatures, contrôles et règles comptables mentionnés sont déjà attachés aux organismes et aux conventions.",
    proposed=new, classification='material_reduction',
    removed=["Approbation préalable des ministres de la sécurité sociale et du budget pour les deux conventions de financement et de reversement du régime des cultes."],
    effects=[effect('authorization_removed', 'cultes-conventions-financement-sans-approbation',
        "Exécution des conventions de financement entre organismes sans visa ministériel spécial.",
        "Les deux conventions sont soumises à l'approbation des ministres chargés de la sécurité sociale et du budget.",
        "Prise d'effet dès signature sans approbation ministérielle préalable ; contrôle de l'Etat et règles budgétaires existants réservés.",
        'legal_duty', "ACOSS, CNAV, CNAM et CAVIMAC, parties aux conventions de financement et reversement.",
        "Conventions nouvelles ; conventions signées en attente d'approbation exécutoires à la bascule ; engagements antérieurs et droits préservés.",
        "Aucun visa, envoi ou déclaration de remplacement ; mêmes affectations et cotisations.",
        "Ces conventions sont soumises à l'approbation des ministres chargés de la sécurité sociale et du budget.",
        "Ces conventions prennent effet dès leur signature, sans approbation ministérielle préalable.")])

put('L382-19',
    "Maintien intégral de la mission consultative générale sur les difficultés du régime des cultes. Cette voie d'avis pluraliste peut être mobilisée par les organismes et représentants religieux ; elle n'impose pas une autorisation individuelle. Elle reste distincte de la consultation préalable d'affiliation supprimée à L382-15.",
    "La commission reste instituée et décrite au deuxième alinéa de L382-15 proposé : aucun renvoi orphelin. R382-58 à R382-69, lus, organisent composition, saisine, rapports, frais, vacations et confidentialité ; leur maintien ne permet plus d'en faire une étape préalable d'affiliation. Les possibilités de saisine de R382-60 et les remboursements de mission restent ouverts pour les interventions futures éligibles, pas seulement pour les réunions antérieures. Aucun nouveau rapport obligatoire n'est ajouté.",
    "La mission générale est conservée après distinction du circuit individuel retiré. Ce maintien de conseil et de représentation n'est ni une nouvelle simplification ni une seconde suppression d'étape d'affiliation.",
    "La fréquence et les coûts de ces avis ne sont pas chiffrés. Les procédures internes réglementaires restent à leur champ propre et aucune économie de dissolution de commission n'est revendiquée.",
    "Aucune charge nouvelle n'est identifiée : l'avis général existant n'est pas transformé en agrément, et ni déclaration périodique ni saisine préalable supplémentaire n'est imposée.")

src = by_number['L382-20']['source_xml']
new = "<p>Les différends auxquels donne lieu l'application de la présente section sont réglés conformément aux dispositions du chapitre 2 du titre IV du livre Ier.</p>"
put('L382-20',
    "Coordination nécessaire du renvoi contentieux : le chapitre 2 actuel regroupe les règles de recours préalables, compétence, représentation et instruction. Les anciens chapitres 3 et 4 n'ont plus de contenu actif dans le corpus fourni. La proposition désigne le chapitre effectivement applicable, sans modifier les conditions d'accès au juge ou les délais.",
    "L142-1 et L142-4 ont été lus intégralement avec leurs notes et la structure du titre IV a été vérifiée dans le corpus : chapitre 2 actif, anciens chapitres 3 et 4 absents, chapitres 5 et 6 de contrôle technique distincts. Le renvoi préexistant devenu partiellement vide est signalé et corrigé expressément ; il n'est pas maintenu comme si l'ancienne architecture subsistait. Le renvoi au chapitre 2 conserve ses exceptions de recours préalable et ses garanties ; aucune règle de préavis du travail ne s'y substitue. Aucun délai échu n'est rouvert et les transitions des procédures antérieures gardent leur fondement propre.",
    "Le changement corrige uniquement la portée structurelle d'un renvoi ancien. Il ne supprime aucune procédure contentieuse et n'est pas compté comme une réduction de charge ou de délai.",
    "Les dispositions de procédure et leurs transitions ne sont pas réécrites dans ce lot. Aucun résultat contentieux individuel ni réduction du coût de justice n'est démontré par cette correction.",
    "Aucune charge nouvelle n'est identifiée : pas de saisine, dossier, délai ou recours supplémentaire ; les règles actuelles du chapitre 2 conservent leur champ et leurs exceptions.",
    proposed=new, classification='coordination_only',
    effects=[effect('coordination', 'cultes-contentieux-renvoi-chapitre-deux',
        "Correction d'un renvoi comprenant des chapitres disparus, sans modification de la procédure actuelle.",
        "Renvoi aux chapitres 2 à 4 du titre IV du livre Ier, dont seuls les articles du chapitre 2 restent actifs.",
        "Renvoi au chapitre 2 actuel du même titre et livre, sans changement des recours ou délais.",
        'legal_duty', "Justiciables et organismes concernés par les différends du régime des cultes.",
        "Coordination structurelle ; transitions procédurales autonomes et décisions antérieures demeurent régies par leurs règles.",
        "Aucune procédure, donnée ou obligation nouvelle ; aucun allègement matériel attribué au renvoi.",
        "Les différends auxquels donne lieu l'application de la présente section sont réglés conformément aux dispositions des chapitres 2 à 4 du titre IV du livre Ier.",
        paragraphs(new)[0])])


work_context = {
    'L382-1': "La source règle l'affiliation des créateurs et la définition des photographes journalistes, non la durée d'un emploi. La condition de trois années civiles supprimée est une durée d'activité artistique indépendante.",
    'L382-3': "La source fixe les cotisations sur droits d'auteur ou BNC. L'assimilation fiscale aux traitements et salaires de CGI 93 ne suffit pas à caractériser un contrat de travail, et la suppression de la majoration BNC ne modifie pas les indemnités de rupture.",
    'L382-3-2': "La source règle la régularisation annuelle de cotisations plafonnées en cas de cumul de revenus d'auteur et d'autres rémunérations. Les quatre mois courent après la déclaration de revenus, sans lien avec une notification de rupture.",
    'L382-5': "La source organise le paiement des cotisations des artistes et leur précompte par un diffuseur, lequel n'est pas nécessairement un employeur. Ni la perception de droits ni leur retenue sociale ne constitue une clause de contrat de travail.",
    'L382-6': "La source impose des modalités de déclaration et versement et l'identification des auteurs. Le retrait de l'exclusivité électronique porte sur les cotisants auteurs et diffuseurs, sans notification de rupture ou création d'emploi temporaire.",
    'L382-7': "La source ouvre une action sanitaire et sociale aux artistes auteurs. L'accès à ces aides ne dépend pas d'un licenciement, d'une durée de contrat ou d'une indemnité ordinaire de rupture ; les futurs auteurs éligibles restent couverts.",
    'L382-10': "La source protège les droits vieillesse des auteurs issus des professions libérales avant 1977 ; la réforme ouvre une faculté de rachat de périodes. Les périodes d'assurance ne sont pas une ancienneté chez un employeur.",
    'L382-12': "La source organise les retraites complémentaires et cite des contrats de production audiovisuelle et d'édition. Leur objet est la propriété intellectuelle, sans assimilation automatique à un contrat de travail privé.",
}

work_rules = {
    'L1234-1': "La vue proposée de L1234-1 substitue quinze jours calendaires au préavis des contrats privés nouveaux et garde le régime des contrats antérieurs. Aucune disposition de cet article social ne renvoie à ce préavis ni ne peut le faire courir par une déclaration de revenus ; notification et protections de rupture gardent leur champ propre.",
    'L1221-2': "La source officielle de L1221-2 admet encore des CDD ; sa vue proposée les ferme pour les nouvelles relations privées au profit du contrat unique. Cette proposition n'est pas le droit en vigueur. Le présent article social ne permet aucun nouveau CDD, et un contrat d'exploitation, une période d'assurance ou une durée d'aide ne fixe pas un terme d'emploi.",
    'L1234-9': "La source officielle de L1234-9 prévoit huit mois ; sa vue proposée distingue les anciens contrats et le contrat unique avec un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, mois complets au prorata, plafond de six mois, initiative patronale et exception de faute grave. Ce barème ne s'applique ni aux droits d'auteur ni à une période d'assurance et ne supprime aucun avantage social de cet article.",
}

specific_checks = {
    ('L382-1', 'L213-1'): "L213-1 confie aux Urssaf le recouvrement et le contrôle, avec délégations possibles ; la compétence d'affiliation des auteurs résulte ici de L382-1 et le directeur de l'ACOSS désigne l'organisme. La suppression des trois années ne transfère pas cette décision à un employeur ou au médiateur. La vue proposée conserve l'organisme et les garanties, sans faire du réemploi des données une baisse nouvelle comptée ici.",
    ('L382-3', '93'): "Le renvoi vise exactement le 1 quater de CGI 93 : droits des œuvres de l'esprit intégralement déclarés par les tiers, fiscalement soumis aux traitements et salaires, avec déduction fiscale de 10 % sur droits diminués des cotisations obligatoires. Le corps proposé de L382-3 garde les droits bruts dans cette branche et retire seulement les 15 % dans la branche BNC ; les autres abattements de CGI 93 restent à leur champ propre. La vue fiscale proposée n'est pas traitée comme un droit déjà entré en vigueur.",
    ('L382-3', 'L382-1'): "La cible fournie est la source officielle de L382-1, sans proposition, qui définit les branches d'auteurs et l'affiliation, non des salariés par nature. Le renvoi d'assujettissement reste pertinent ; le L382-1 rédigé dans ce lot ouvre les photographes BNC sans trois ans et cette même population accède aux taux et à la base allégée. Aucune ancienneté d'emploi ni indemnité de rupture n'est ajoutée comme condition sociale.",
    ('L382-3-2', 'L213-1'): "La cible identifie l'Urssaf de recouvrement et de contrôle. Le renvoi de L382-3-2 désigne l'organisme qui doit régulariser, sans déplacer cette tâche sur l'assuré ni créer une nouvelle déclaration distincte de celle déjà visée. Les quatre mois restent un maximum à compter du dépôt ; les délais de contrôle ou les quinze jours du contrat unique ne le remplacent pas.",
    ('L382-3-2', 'L241-3'): "Le plafond annuel recherché figure au premier alinéa officiel de L241-3 et au premier alinéa du I de sa vue proposée ; le renvoi à l'article demeure identifiable et le remboursement de l'excès ne devient pas une exonération de la part déplafonnée. Les II à VII proposés sur la capitalisation visent d'abord les salariés privés et ne captent pas les revenus d'auteur. Ni la date de déclaration ni le plafond ne sont remplacés par un seuil d'ancienneté de rupture.",
    ('L382-5', 'L213-1'): "Le premier alinéa désigne une Urssaf choisie par le directeur de l'ACOSS, puis le deuxième et le troisième conservent ce même destinataire pour précompte et contributions. L213-1 reste cohérent avec cette activité confiée par la loi ; ses réformes proposées de C3S et CPF-CDD ne suppriment pas par analogie les cotisations des auteurs ni la formation de L6331-65. Aucun second organisme ni paiement ne résulte du renvoi.",
    ('L382-5', 'L382-1'): "La source officielle cible détermine les personnes dont la part de cotisations est payée ou précomptée. L'extension sans trois ans rédigée pour les photographes dans ce lot reste bénéficiaire du même circuit et des dispenses réglementaires BNC ; le maintien du renvoi n'enferme pas cette faculté dans les affiliations anciennes. La référence ne transforme ni diffuseur en employeur ni contrat d'exploitation en emploi temporaire.",
    ('L382-6', 'L382-5'): "La cible fournie est le texte officiel, sans proposition, de L382-5. Son premier alinéa désigne l'organisme Urssaf recevant la part des auteurs ; le renvoi du deuxième alinéa de L382-6 pour l'identification pointe donc un destinataire réel. Le libre choix de support ne supprime ni l'acquit du précompte ni les dispenses BNC et ne crée pas de deuxième versement à l'auteur ou au diffuseur.",
    ('L382-6', 'L213-1'): "L'organisme désigné est une Urssaf de recouvrement, non une autorité d'agrément du support papier. L213-1 conserve le recouvrement et la vérification ; dans L382-6 proposé, aucun signalement d'impossibilité ne conditionne l'autre voie légale. Les contrôles des données manquantes subsistent et les principes de réemploi de la vue proposée ne sont pas comptés comme une nouvelle suppression autonome.",
    ('L382-6', 'L114-12-1'): "L'avant-dernier alinéa officiel et celui de la vue proposée désignent bien le numéro d'inscription au répertoire national d'identification des personnes physiques. Le dernier alinéa règle aussi les personnes sans ce numéro ; le renvoi d'identification n'est donc ni un identifiant employeur ni une condition d'ancienneté. Le choix de support conserve cette identification sans ouvrir aux diffuseurs un droit d'accès nouveau au répertoire ni demander une déclaration d'option.",
    ('L382-7', 'L213-1'): "L213-1 identifie les unions et leurs missions de recouvrement et d'action sociale ; la mission spéciale pour les artistes auteurs est donnée ici par L382-7. Le directeur de l'ACOSS désigne l'organisme exécutant les orientations de L382-2, sans transférer l'octroi de l'aide à un employeur. Les adaptations proposées de recouvrement ne ferment pas les aides futures et n'ajoutent pas un état annuel de protection complémentaire.",
    ('L382-7', 'L382-1'): "Le renvoi vise l'ensemble des artistes auteurs affiliés selon les branches de L382-1, non une catégorie de salariés licenciés. L'accès à l'action sanitaire et sociale demeure pour toute future situation éligible, notamment les photographes admis sans les trois années retirées dans ce lot. La cible fournie est seulement officielle et la réforme de son champ n'est pas présentée comme déjà en vigueur.",
    ('L382-10', 'L382-1'): "La cible officielle identifie les artistes auteurs dont les droits des professions libérales antérieurs au 1er janvier 1977 sont repris. Elle ne fait pas de cette date un anniversaire d'emploi. L'ouverture proposée de L351-14 concerne aussi les futures demandes éligibles et ne retranche aucun droit de 1977 ; elle ne valide pas une période deux fois et ne ferme pas les droits des catégories photographiques élargies dans ce lot.",
    ('L382-12', 'L382-1'): "Les personnes affiliées d'après L382-1 restent le champ du complémentaire, y compris à l'avenir pour les photographes nouvellement éligibles. Cette référence ne subordonne pas la retraite complémentaire à un an d'emploi chez un producteur et ne supprime ni sa participation ni celle du prêt en bibliothèque. La vue fournie de L382-1 est officielle seulement ; son nouveau champ proposé reste un projet distinct du droit actuel.",
    ('L382-12', 'L133-4'): "La cible fournie L133-4 du code de la sécurité sociale concerne la récupération des indus de tarification, distribution ou facturation médicale, avec contradictoire et délais propres. L382-12 cite en réalité L133-4 du code de la propriété intellectuelle, pour la limite d'affectation du prêt en bibliothèque. La similitude de numéro ne permet aucune substitution : la cible CSS n'est pas applicable à ce renvoi et ne fonde ni précompte complémentaire ni ancienneté d'emploi.",
}

for number, obj in answers.items():
    key = obj['code_id'] + '|' + obj['source_id']
    obj['reference_checks'] = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        target_number = target['number']
        if target_number in work_rules:
            assessment = work_context[number] + ' ' + work_rules[target_number]
        else:
            assessment = specific_checks[(number, target_number)]
        assert len(assessment) >= 80
        obj['reference_checks'].append(dict(target_key=target_key,
            view_sha256=target['view_sha256'], assessment=assessment))

answers['L382-1']['review_notes'] += " La transition est intégrée au dernier alinéa de la commission professionnelle : le renvoi de R382-16-4 au dernier alinéa de L382-1 garde ainsi sa cible, sans déplacement de la commission."
answers['L382-2']['review_notes'] += " L'articulation entre les ministères cités au II législatif (culture, santé, travail) et les deux représentants culture/sécurité sociale de R382-8 reste à vérifier dans les actes de composition ; elle n'est pas corrigée implicitement à l'occasion de la suppression de l'opposition générale."
answers['L382-7']['review_notes'] += " R382-30-2 cite également L213-6, qui ne figure pas comme article actif dans le corpus local ; ce second renvoi réglementaire préexistant est signalé. Il ne rend pas incohérent le renvoi propre de L382-7 à L213-1, maintenu et vérifié."
answers['L382-10']['review_notes'] += " L351-14-1 a ensuite été lu intégralement dans le corpus avec ses notes : les cotisations relèvent d'un décret de neutralité actuarielle, et les tarifs favorables de ses II à IV gardent leur champ propre. Le renvoi de L351-14 aux cotisations de L351-14-1 n'est pas utilisé pour importer dans les périodes pré-affiliation les conditions d'études ou le plafond de douze trimestres du mécanisme distinct du I ; aucun prix du rachat n'est inventé."
answers['L382-1']['substantive_impact']['effects'].append(effect(
    'coordination', 'journalistes-concordance-definition-code-travail',
    "Actualisation du renvoi ancien à la définition professionnelle des journalistes photographes.",
    "Définition par L761-2 et suivants de l'ancienne numérotation du code du travail.",
    "Renvoi aux définitions actuelles L7111-3 à L7111-5, journalistes, assimilés et communication électronique.",
    'legal_duty', "Auteurs photographes journalistes professionnels ou assimilés.",
    "Coordination de la définition, sans modification du champ des revenus de presse ni délai d'emploi.",
    "Aucune formalité ni critère d'ancienneté supplémentaire ; aucune baisse matérielle comptée pour ce renvoi.",
    paragraphs(by_number['L382-1']['source_xml'])[2],
    paragraphs(answers['L382-1']['proposed_xml'])[2]))
answers['L382-3']['proposed_xml'] = replace_once(
    answers['L382-3']['proposed_xml'],
    "L'option volontaire de cotisation sur l'assiette forfaitaire prévue à l'article L. 382-3-1 reste ouverte.",
    "L'option volontaire de cotisation sur l'assiette forfaitaire prévue à l'article L. 382-3-1 reste ouverte. L'exercice de cette option conserve les conditions d'ouverture et de calcul des droits attachées à cette assiette forfaitaire.")
answers['L382-3']['reason'] += " Le II, 2° de L136-1-1 renvoie directement au troisième alinéa : l'assiette de CSG suit la même baisse, avec son taux propre inchangé, sans lui appliquer le taux salarial privé proposé de 6,6 %."
answers['L382-3']['review_notes'] = replace_once(
    answers['L382-3']['review_notes'],
    "La CSG et les assiettes propres des régimes complémentaires ne sont pas déclarées réformées par analogie.",
    "L136-1-1, L136-2 et L136-5 ont été lus intégralement dans le corpus : le II, 2° de L136-1-1 reprend les revenus du troisième alinéa de L382-3 et l'assiette CSG suit donc directement la baisse, sans modification de son taux ni de l'abattement propre aux traitements et salaires. Le troisième alinéa reste à sa place. Les effets sur la CRDS de l'ordonnance n° 96-50 et les assiettes propres des complémentaires exigent leurs coordinations distinctes, non présumées accomplies. La transition couvre expressément les contributions qui utilisent cette assiette, sans rétroactivité générale.")
impact = answers['L382-3']['substantive_impact']
impact['assessment'] = "La majoration sociale obligatoire de 15 % des BNC est retirée pour les nouvelles périodes ; la CSG qui reprend directement ce revenu suit cette baisse d'assiette. Les taux propres restent inchangés et les prestations conservent leur base antérieure ; la distinction cotisations/prestations ajoute une complexité réelle. Le bilan est donc mixed, sans promesse de gain budgétaire net."
change = impact['effects'][0]
change['description'] = "Réduction de l'assiette des cotisations BNC et de la CSG qui reprend ce revenu, à taux propres inchangés."
change['before'] = "Assiette de 115 % du revenu imposable BNC pour les cotisations, reprise pour la CSG par L136-1-1 II, 2° ; taux de droit commun et taux propres fixés hors cet article, non chiffrés ici, sous les adaptations et plafonds applicables."
change['after'] = "Assiette de 100 % du même revenu imposable BNC pour les cotisations et la CSG par ce renvoi ; taux de droit commun et taux propres inchangés, non chiffrés ici, mêmes plafonds et option forfaitaire volontaire préservée."
change['conditions_and_transition'] = "Périodes d'activité à compter de l'entrée en vigueur pour les cotisations et contributions utilisant le troisième alinéa ; anciennes dettes, exonérations, prises en charge, régularisations et recours préservés."

for measure, description, before, after in [
    ('artistes-photographes-fin-attente-trois-ans',
     "Coordination de l'habilitation avec la suppression des trois années d'activité photographique.",
     "Conditions réglementaires de droits définies sous l'exigence légale de trois années civiles des photographes BNC.",
     "Le décret ne peut rétablir la durée supprimée à L382-1 ; conditions professionnelles et de prestations distinctes maintenues."),
    ('artistes-auteurs-fin-majoration-assiette-bnc',
     "Coordination des calculs réglementaires avec la baisse de cotisation et les droits conservés.",
     "Calculs de prestations et cotisations adossés au revenu BNC majoré de 15 %.",
     "Le décret respecte le BNC non majoré pour les cotisations et le revenu de droits aux prestations conservé par L382-3."),
    ('artistes-auteurs-libre-support-declarations-paiements',
     "Coordination de l'habilitation avec la liberté de support social.",
     "Modalités réglementaires de déclaration sous l'obligation légale de voie dématérialisée, sauf impossibilité signalée.",
     "Le décret ne peut rétablir l'exclusivité électronique retirée par L382-6, sans préjudice des données et échéances dues."),
]:
    answers['L382-14']['substantive_impact']['effects'].append(effect(
        'coordination', measure, description, before, after,
        'legal_duty', "Pouvoir réglementaire et organismes appliquant le régime des artistes auteurs.",
        "Champ et transition propres à la mesure de fond correspondante ; aucune seconde réduction.",
        "Aucune formalité de remplacement ; la complexité des deux bases est recensée à L382-3.",
        paragraphs(by_number['L382-14']['source_xml'])[0],
        paragraphs(answers['L382-14']['proposed_xml'])[2]))

result = [answers[a['number']] for a in sources]
assert len(result) == len(sources) == 24
for source, answer in zip(sources, result):
    for name in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert answer[name] == source[name]
    impact = answer['substantive_impact']
    for name in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(impact[name]) >= 40
    for change in impact['effects']:
        assert len(change['source_quote']) >= 12
        assert len(change['proposed_quote']) >= 12
        assert change['source_quote'] in plain(source['source_xml']), (answer['number'], 'source quote')
        assert change['proposed_quote'] in plain(answer['proposed_xml']), (answer['number'], 'proposed quote')
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', change['measure_id'])
        assert 6 <= len(change['measure_id']) <= 96
    if source.get('benefit_check_required'):
        assert len(answer.get('benefit_review', '')) >= 100
    if answer['proposed_xml'] is None:
        assert answer['status'] == 'retained_unchanged'
        assert impact['classification'] == 'retained_necessary' and not impact['effects']
    else:
        assert answer['status'] == 'rewrite_draft'
    if answer.get('removed_provisions'):
        assert all(len(x) >= 30 for x in answer['removed_provisions'])
    if answer.get('change_type') == 'full_repeal':
        assert plain(answer['proposed_xml']).startswith(('Le présent article est abrogé', 'Abrogé'))
        assert len(answer['repeal_scope']) >= 30

(ROOT / 'answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'article_count': len(result),
    'rewritten': sum(a['status'] == 'rewrite_draft' for a in result),
    'retained': sum(a['status'] == 'retained_unchanged' for a in result),
    'reference_checks': sum(len(a['reference_checks']) for a in result),
    'effects': sum(len(a['substantive_impact']['effects']) for a in result)}, ensure_ascii=False))
