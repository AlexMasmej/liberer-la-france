import json
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
refs = json.loads((ROOT / 'reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}

def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))

def p(text):
    return '<p>' + text + '</p>'

def replace_once(text, old, new):
    assert text.count(old) == 1, old
    return text.replace(old, new, 1)

def impact(classification, assessment, limitations, burdens, effects=None):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=limitations, new_burdens_review=burdens,
                effects=effects or [])

def effect(kind, measure_id, description, before, after, unit, population,
           transition, source_quote, proposed_quote, burdens='Aucune obligation de remplacement ni charge nouvelle créée par cette mesure.'):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def put(number, proposed, reason, notes, substantive, benefit=None, removed=None, repeal=None):
    a = by_number[number]
    out = {k:a[k] for k in ['code_id','source_id','source_sha256','number']}
    out.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if proposed is None else 'rewrite_draft',
               substantive_impact=substantive)
    if proposed is None:
        out['classification'] = 'retained_necessary'
    if benefit is not None:
        out['benefit_review'] = benefit
    if removed:
        out.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal:
        out.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal)
    answers[number] = out

def retain(number, reason, notes, assessment, limitations, benefit=None):
    put(number, None, reason, notes,
        impact('retained_necessary', assessment, limitations,
               'Aucune charge nouvelle n’est identifiée : le texte officiel entier est maintenu sans ajout de pièce, de registre, de condition ni de délai.'), benefit=benefit)

GOV = 'caisses-fin-approbation-statuts-reglements'
CONTRACT = 'contrat-unique-duree-indeterminee'
MEDICAL = 'accord-prealable-motifs-medicaux'

retain('L281-1',
       'Maintien intégral du principe de contrôle de l’État sur la gestion du régime général. Il protège les fonds sociaux et les droits des assurés sans instituer à lui seul un agrément, une déclaration périodique ou un prélèvement. La suppression des approbations particulières de L281-4 et L282-1 n’exige pas de supprimer ce contrôle général.',
       'La note relative à L752-13 et L623-1 est une note de champ, non une règle de préavis ou de licenciement. Son renvoi à L623-1 pour l’assurance vieillesse des non-salariés est devenu discordant : L623-1 actuel, fourni dans les cibles, règle les prestations de maternité, paternité, adoption et deuil des indépendants. Cette note ne prouve donc pas une extension actuelle du contrôle de L281-1 à leur assurance vieillesse ; concordance historique extérieure à établir sans corriger silencieusement le corps. Ses durées de cessation d’activité ne sont pas celles du contrat privé. Les textes de rupture du travail n’ont aucun renvoi direct dans cet article. Les autres modalités de tutelle demeurent distinctes des approbations expressément supprimées dans ce lot.',
       'Le contrôle public des organismes est conservé dans son champ entier ; aucune nouvelle réduction de cotisation ni de formalité ne résulte de ce maintien.',
       'La nécessité des modalités particulières de contrôle doit être appréciée dans leurs propres articles ; ce principe ne valide pas toutes les procédures de tutelle.')

retain('L281-2',
       'Maintien intégral de la substitution en cas de carence pour exécuter une dépense ou recouvrer une recette déjà obligatoire en vertu de la loi, du règlement ou d’un jugement. Ce mécanisme protège notamment le paiement effectif des prestations et ne crée pas une recette autonome ni une autorisation à obtenir par un assuré.',
       'R281-1, lu dans le corpus public, fixe à huit jours après mise en demeure le délai visé ; il permet une exécution subsidiaire, et non une formalité préalable à une embauche. Le directeur comptable et financier reste chargé de l’exécution. La note d’application au 1er janvier 2023 et les modalités de l’ordonnance de 2022 restent à leur objet historique, sans fixer l’entrée en vigueur de la réforme.',
       'La source entière conserve un mécanisme d’exécution des obligations existantes ; supprimer ce mécanisme pourrait empêcher le paiement de créances obligatoires.',
       'Aucune suppression du principal des recettes ou dépenses visées, ni baisse d’un délai de rupture de contrat, n’est déduite de cet article.')

retain('L281-3',
       'Maintien intégral des interventions contre les irrégularités graves, la mauvaise gestion et la carence. La suspension ou dissolution du conseil avec administrateur provisoire, et la révocation des seuls membres responsables après avis du conseil, répondent à une fonction essentielle de protection des fonds et de continuité des prestations ; l’avis conservé participe aux garanties de cette intervention individuelle.',
       'Le 1° conserve ses quatre catégories d’organismes et ses trois motifs ; le 2° conserve l’imputabilité personnelle et l’avis du conseil. Il ne s’agit ni de l’approbation ordinaire de tous les règlements intérieurs ni d’une autorisation de rupture individuelle du contrat privé. Les garanties générales du contradictoire et les recours ne sont pas supprimés.',
       'Aucune charge administrative courante n’est retirée : sont conservés des pouvoirs de redressement en cas de défaillance qualifiée et leurs garanties.',
       'Le coût des interventions et la pertinence de chaque décision ne sont pas évalués par le maintien de leur base légale.')

new = ''.join([
    p("Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme."),
    p("À compter de cette date, les statuts et règlements intérieurs des organismes qui relevaient du présent article, ainsi que leurs modifications, entrent en vigueur selon leurs règles d’adoption et de publicité applicables, sans approbation préalable de l’autorité de l’État. Cette suppression ne peut être remplacée par un visa, une homologation ou une déclaration préalable conditionnant leur entrée en vigueur."),
    p("Les procédures d’approbation en cours prennent fin à cette date, sans nouveau dépôt. La suppression de l’approbation ne dispense pas du respect des dispositions législatives et réglementaires applicables ni des dispositions obligatoires des modèles prévus à l’article L. 281-5. Les contrôles de légalité et de gestion demeurent applicables sans rétablir cette approbation particulière."),
    p("Les actes régulièrement adoptés avant cette date, les droits et engagements qu’ils ont valablement créés et les recours relatifs à leur légalité sont préservés. Les modifications adoptées à compter de cette date bénéficient de la suppression de l’approbation, même lorsque les statuts ou règlements initiaux ont été approuvés antérieurement. La présente abrogation ne régularise pas les illégalités antérieures.")
])
put('L281-4', new,
    'Réforme de fond : suppression de l’approbation initiale et de chaque approbation modificative des statuts et règlements intérieurs. Le cadre commun obligatoire de L281-5 et les contrôles de gestion rendent inutile cette seconde validation systématique. Aucun dépôt déclaratif équivalent n’est créé. La transition couvre les procédures pendantes sans légalisation des actes illégaux.',
    'R281-4, lu en entier, rétablit actuellement une approbation avec trente jours d’opposition : sa coordination réglementaire est indispensable et reste hors des articles assignés. R213-5 étend ce circuit aux URSSAF : retirer le renvoi à L281-4 et R281-4, conserver L281-5, R231-1 et R281-6 dans leur champ. L281-6 est coordonné dans ce lot. L281-5, L281-1 à L281-3 et L283-1 ne doivent pas servir à recréer le visa supprimé. Les renvois nouveaux à L281-5 portent sur une source intégralement fournie dans le lot, sans ajout de cible dans reference_checks.',
    impact('material_reduction',
           'Deux catégories de validations systématiques disparaissent réellement par rapport à la source entière : approbation initiale et approbation de chaque modification. Les conditions légales de gouvernance restent opposables.',
           'Seule l’approbation particulière des documents de gouvernance est supprimée ; les contrôles financiers, la légalité des décisions et la responsabilité des dirigeants subsistent. Aucun coût net global n’est chiffré.',
           'Aucune charge nouvelle n’est identifiée : les règles d’adoption et de publicité évoquées sont celles déjà applicables et aucun visa, dépôt, registre ni déclaration de remplacement n’est exigé.',
           [effect('authorization_removed', GOV,
                   'Suppression du visa étatique obligatoire des statuts et règlements locaux, à l’adoption et lors de chaque modification.',
                   'Approbation de l’État des statuts et du règlement intérieur de chaque caisse visée, puis de toute modification avant effet ; opposition réglementaire sous trente jours.',
                   'Aucune approbation particulière, initiale ou modificative, ni déclaration préalable équivalente ; cadre légal et modèles obligatoires maintenus.',
                   'legal_duty', 'CPAM, CARSAT, CAF et caisse d’Alsace-Moselle visées par la source ; extensions coordonnées séparément.',
                   'Suppression dès l’entrée en vigueur, y compris pour les dossiers pendants ; actes, droits, engagements et recours antérieurs conservés.',
                   "Toute modification aux statuts ou au règlement intérieur doit être également approuvée, préalablement à son entrée en vigueur, par l'autorité compétente de l'Etat.",
                   'Cette suppression ne peut être remplacée par un visa, une homologation ou une déclaration préalable conditionnant leur entrée en vigueur.')]),
    repeal='Suppression pour l’avenir de l’approbation étatique initiale des statuts et règlements intérieurs des caisses visées et de l’approbation préalable de toute modification, avec clôture des procédures pendantes et protection des actes et droits antérieurs.')

retain('L281-5',
       'Maintien intégral du cadre commun des modèles de statuts et de règlement intérieur, après avis des instances nationales compétentes. Il distingue dispositions obligatoires et facultatives, garantit des règles communes de gouvernance et laisse les choix facultatifs ouverts ; il n’exige pas une nouvelle validation de chaque acte local une fois les approbations particulières supprimées.',
       'Les dispositions obligatoires du règlement intérieur modèle restent applicables dès publication ; aucune nouvelle période d’attente n’est ajoutée. R281-6, lu en entier, désigne le ministre compétent pour ce pouvoir de modèle. Son maintien ne permet pas de recréer une approbation individuelle prohibée par les propositions de L281-4 et L281-6.',
       'Le modèle normatif commun et ses options sont conservés ; la disparition du contrôle préalable individuel est portée par L281-4, sans compter ici une seconde suppression.',
       'Les arrêtés contenant les modèles ne sont pas réécrits dans ce lot ; leurs clauses d’approbation éventuelles nécessitent une coordination spécifique.')

new = by_number['L281-6']['source_xml']
new = replace_once(new, 'des articles L. 281-4 et L. 281-5 ci-dessus sont applicables', 'de l’article L. 281-5 sont applicables')
new += p("À compter de l’entrée en vigueur de la loi portant la présente réforme, l’approbation préalable des statuts et règlements intérieurs des organismes mentionnés au premier alinéa et de leurs modifications n’est plus exigée. Les procédures en cours prennent fin sans nouveau dépôt. Les dispositions obligatoires et facultatives des modèles ainsi que les avis prévus au présent article demeurent applicables. Aucun visa ou déclaration préalable de remplacement ne peut être imposé sur le fondement du présent article. Les actes, droits et engagements antérieurs valablement constitués et les recours correspondants sont préservés.")
put('L281-6', new,
    'Coordination nécessaire de l’abrogation de L281-4 : retrait de ce renvoi pour les unions et fédérations, suppression de son circuit d’approbation dans ce champ, maintien entier de l’extension des modèles de L281-5 et des deux avis nationaux propres aux fédérations de L216-3. Cette extension appartient à la même mesure de gouvernance et ne constitue pas une nouvelle taxe supprimée.',
    'Les trois références L216-2, L216-4 et L216-3 restent distinctes et dans le même ordre ; le second alinéa conserve le double avis. Ne pas confondre cet avis sur les modèles avec l’approbation de chaque modification individuelle. La coordination de R281-4 et des arrêtés de modèles reste nécessaire ; les textes extérieurs au lot ne sont pas déclarés modifiés.',
    impact('coordination_only',
           'La proposition retire le renvoi devenu incohérent à L281-4 et assure que la même suppression des approbations vaut pour les organismes de L281-6 ; les modèles et les deux avis sont conservés.',
           'Il s’agit du champ d’extension de la mesure commune de gouvernance, non d’une deuxième réduction à additionner à L281-4. Les trois catégories d’unions et fédérations ne sont pas fusionnées.',
           'Aucune charge nouvelle n’est identifiée : aucun formulaire, transmission, délai d’attente ou nouvelle condition de fonctionnement n’est créé ; les avis existants demeurent.',
           [effect('coordination', GOV, 'Retrait de l’extension de l’approbation abrogée et maintien de l’extension des modèles.',
                   'Extension conjointe de L281-4 et L281-5 aux unions et fédérations désignées.',
                   'Extension de L281-5 seulement, avec exclusion explicite de toute approbation de remplacement.',
                   'legal_duty', 'Unions et fédérations visées par L216-2, L216-4 et L216-3.',
                   'Application à l’entrée en vigueur, procédures pendantes closes sans dépôt et droits antérieurs préservés.',
                   'Les dispositions des articles L. 281-4 et L. 281-5 ci-dessus sont applicables',
                   'Les dispositions de l’article L. 281-5 sont applicables')]))

new = ''.join([
    p("Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant la présente réforme."),
    p("À compter de cette date, le règlement intérieur de chaque caisse nationale et de l’agence centrale, ainsi que ses modifications, n’est plus soumis à l’approbation particulière de l’autorité de l’État. Aucun visa, homologation ou déclaration préalable de remplacement ne conditionne son entrée en vigueur. Les règles d’adoption et de publicité applicables et le contrôle économique et financier de l’État demeurent, sans rétablir cette approbation."),
    p("Les procédures d’approbation en cours prennent fin sans nouveau dépôt. Les règlements régulièrement adoptés antérieurement, les droits et engagements qu’ils ont valablement créés et les recours correspondants sont préservés ; leurs modifications futures relèvent de la suppression de l’approbation. La présente abrogation ne régularise pas les illégalités antérieures.")
])
put('L282-1', new,
    'Réforme de fond : suppression du visa étatique du règlement intérieur des organismes nationaux et de l’agence centrale. Le contrôle économique et financier existant reste assuré et ne justifie pas une seconde approbation systématique des règles internes. La suppression est effective pour les dossiers pendants et modifications futures, sans transmission de remplacement.',
    'R282-1, lu en entier, soumet les caisses nationales, l’UNCAM et l’agence centrale au contrôle économique et financier selon le décret du 26 mai 1955 : ce contrôle distinct n’est pas abrogé. Les clauses réglementaires ou arrêtés imposant encore le visa particulier doivent être coordonnés ; leur inventaire exhaustif hors corpus n’est pas affirmé. La réforme ne supprime pas une approbation d’un programme, d’un budget ou d’un tarif reposant sur un fondement autonome.',
    impact('material_reduction',
           'Le règlement intérieur national n’a plus à obtenir l’approbation particulière de l’État prévue par la source ; cette coupe complète le champ local de la mesure commune de gouvernance.',
           'Aucune suppression du contrôle économique et financier, des compétences légales ou d’un prélèvement social n’est opérée. Le gain administratif et le coût public net ne sont pas chiffrés.',
           'Aucune charge nouvelle n’est identifiée : le visa supprimé n’est remplacé par aucune déclaration ; les règles d’adoption et contrôles cités sont ceux déjà applicables.',
           [effect('authorization_removed', GOV,
                   'Suppression de l’approbation particulière du règlement intérieur des organismes nationaux et de l’agence centrale, dans le champ national de la même mesure.',
                   'Règlement intérieur de chaque caisse nationale et de l’agence centrale soumis à l’approbation de l’État.',
                   'Règlement intérieur et modifications sans cette approbation ; contrôles publics autonomes conservés.',
                   'legal_duty', 'Caisses nationales et agence centrale visées par L282-1.',
                   'Entrée en vigueur de la loi, clôture des procédures pendantes, actes et droits valablement constitués antérieurement préservés.',
                   "Le règlement intérieur de chaque caisse nationale et de l'agence centrale sont soumis à l'approbation de l'autorité compétente de l'Etat.",
                   'Aucun visa, homologation ou déclaration préalable de remplacement ne conditionne son entrée en vigueur.')]),
    repeal='Suppression prospective de l’approbation particulière par l’État du règlement intérieur de chaque caisse nationale et de l’agence centrale, sans déclaration de remplacement et sans retrait du contrôle économique et financier autonome.')

retain('L283-1',
       'Maintien intégral de l’habilitation réglementaire d’application du livre II et du contrôle financier, avec décret en Conseil d’État sauf disposition contraire. Cette habilitation assure l’exécution des protections et du contrôle de fonds sociaux ; elle n’impose par elle-même aucune déclaration aux cotisants ni taxe nouvelle.',
       'Les abrogations proposées de L281-4 et L282-1 prohibent expressément les visas et déclarations de remplacement : le pouvoir réglementaire d’application conservé ne permet pas de les rétablir. La réserve de disposition contraire et le caractère subsidiaire « en tant que de besoin » restent intacts.',
       'Aucun allègement nouveau n’est compté pour cette base réglementaire nécessaire ; les suppressions particulières restent portées par leurs articles propres.',
       'La conservation de l’habilitation n’atteste pas la nécessité de chaque mesure réglementaire existante, qui conserve son examen propre.')

retain('L311-1',
       'Maintien intégral de la définition des prestations en espèces couvertes par le régime général : maladie, invalidité, vieillesse, décès, veuvage, maternité et paternité. C’est une garantie de couverture des risques et non une taxe accessoire ni une formalité supprimable sans fermer des droits.',
       'Le capital ou la prestation sociale de décès n’est pas un droit français de succession à supprimer. La réforme de capitalisation ne transfère ici aucune cotisation et ne modifie pas les pensions déjà liquidées. L’article ne fixe ni condition d’ancienneté du contrat ni délai de rupture.',
       'Les sept risques ou charges et le renvoi aux articles suivants sont intégralement conservés ; aucune baisse de prélèvement n’est revendiquée.',
       'Les paramètres de financement, les taux et les conditions de chaque prestation restent dans leurs dispositions propres ; aucun rendement ou équilibre financier n’est présumé.')

retain('L311-2',
       'Maintien intégral de l’affiliation obligatoire indépendamment de l’âge, de la pension, de la nationalité, du sexe, de l’employeur, du lieu, de la rémunération et de la validité ou de la nature du contrat ou du statut. La règle ferme les lacunes de couverture et l’évitement de l’affiliation ; ce n’est pas une cotisation accessoire à retirer isolément.',
       'Le contrat unique entre dans cette règle déjà indépendante de la forme du contrat : aucune réécriture n’est nécessaire pour en faire bénéficier les nouvelles embauches ou préserver les anciens contrats. La note du 1er septembre 2023 garde sa fonction historique. Les allègements d’assiette et de taux demeurent dans leurs articles propres.',
       'Le champ universel des salariés est conservé sans ajout de condition d’un an ni de condition liée au préavis ; l’affiliation n’est pas transférée vers un autre financeur.',
       'La conservation de l’affiliation ne démontre aucune diminution du montant des cotisations ; la transition retraite et les régimes agricoles ou spéciaux ne sont pas refondus ici.')

new = by_number['L311-3']['source_xml']
for old, replacement in [
    ('articles L. 721-1 et suivants du code du travail', 'articles L. 7411-1 et suivants du code du travail'),
    ('articles L. 751-1 et suivants du code du travail', 'articles L. 7311-1 et suivants du code du travail'),
    ('articles L. 762-1 et suivants, L. 763-1 et L. 763-2 du code du travail', 'articles L. 7121-2 à L. 7121-8 et L. 7123-2 à L. 7123-6 du code du travail'),
    ('articles L. 761-1 et L. 761-2 du code du travail', 'articles L. 7111-3 et L. 7111-4 du code du travail')]:
    new = replace_once(new, old, replacement)
new += p("Les règles d’affiliation du présent article demeurent applicables aux situations qui en remplissent les conditions, y compris lorsqu’un contrat de travail unique à durée indéterminée est conclu à compter de l’entrée en vigueur de la loi l’instituant. Le présent article n’autorise ni la conclusion ni le renouvellement d’un contrat de travail à durée déterminée après cette entrée en vigueur. La durée d’une mission, d’une formation ou d’un accompagnement ne fixe pas la durée de l’emploi. Les références à un statut ou à un dispositif particulier, notamment au 32°, ne dérogent pas à ces règles pour les nouveaux contrats de travail de droit privé. Les contrats antérieurs conservent leur régime transitoire, leur ancienneté et les droits acquis ; les options d’affiliation, abattements et dérogations prévus au présent article restent ouverts aux nouvelles situations qui en remplissent les conditions. Les régimes publics et les règles de coordination internationale de sécurité sociale demeurent distincts.")
put('L311-3', new,
    'Coordination nécessaire, sans suppression fictive de cotisations : les renvois au code du travail antérieur à la recodification sont remplacés par les dispositions actuelles relatives au travail à domicile, aux représentants, artistes, mannequins et journalistes. Les trente-neuf rubriques et tous les autres alinéas sont maintenus, y compris les abattements et options. Un alinéa précise la continuité de l’affiliation dans le contrat unique et interdit de tirer d’un statut spécial un nouveau terme d’emploi ; les régimes publics et anciens contrats restent distincts.',
    'Les nouvelles références de travail L7411-1 et suivants, L7311-1 et suivants, L7121-2 à L7121-8, L7123-2 à L7123-6 et L7111-3/L7111-4 ne figurent pas parmi les cibles imposées de reference-targets.json ; leurs dispositions de définition et de présomption ont été lues dans travail.json du corpus public. Elles remplacent des numéros périmés, sans supprimer les exceptions européennes L7121-5 et L7123-4-1 ni les règles de rémunérations d’exploitation L7121-8/L7123-6. La concordance historique détaillée des anciennes subdivisions doit encore être confrontée aux tables de recodification : elle n’est pas présentée comme certifiée. L7331-3, lu dans le corpus, conserve une fin automatique au défaut d’association à trois ans : sa coordination pour les nouveaux emplois est nécessaire dans le code du travail, hors du présent lot ; le renvoi d’affiliation du 32° ne l’autorise pas. Le 27° concerne des agents publics et ne supprime pas leurs autorisations de cumul ; l’actualité de son renvoi au décret du 29 octobre 1936 exige une concordance avec les textes de fonction publique hors du corpus fourni, sans présumer une autorisation nouvelle. Le 36° désigne littéralement les particuliers donneurs d’ordre plutôt que les prestataires : cette particularité de la source est signalée et conservée sans inversion silencieuse du sujet de l’affiliation. Le 22° vise le deuxième alinéa du d du 1° du 7 de CGI261, et non le préavis ou l’indemnité de rupture ; la note de reprise de CGI261 en 2027 doit être coordonnée avec le CIBS sans fermer l’affiliation. Les 60 %, 87 %, 1 500 €, deux années consécutives et seuil triple sont conservés exactement. Aucun plafond microsocial de 20 % n’est étendu à ce régime distinct. La note du 1er janvier 2025 demeure à son champ propre.',
    impact('coordination_only',
           'La source officielle entière est conservée hors corrections de références périmées et coordination du contrat unique ; aucune baisse nouvelle des cotisations ni suppression de déclaration de marge du 20° n’est revendiquée.',
           'Les tables historiques de recodification et la reprise fiscale de CGI261 demandent une coordination documentaire complémentaire. L’affiliation sociale ne suffit pas à réécrire les régimes spéciaux de travail hors lot.',
           'Aucune charge nouvelle n’est identifiée : aucune nouvelle option, pièce, déclaration ou ancienneté n’est imposée. Les obligations existantes nécessaires au calcul des droits et à l’assiette demeurent dans leur champ.',
           [effect('coordination', CONTRACT,
                   'Maintien de l’affiliation des catégories spéciales pour les futurs emplois à durée indéterminée sans habilitation à recréer un CDD.',
                   'Liste d’affiliation comportant plusieurs renvois anciens et des statuts spéciaux, dont les entrepreneurs salariés du 32°.',
                   'Mêmes catégories, options et abattements ; renvois actualisés et absence explicite de dérogation au contrat unique pour les nouveaux emplois privés.',
                   'regime', 'Catégories affiliées par les 1° à 39°, dans le champ propre de chaque rubrique.',
                   'Contrats uniques futurs ; anciens contrats, droits acquis, régimes publics et coordination internationale réservés.',
                   'Les entrepreneurs salariés et les entrepreneurs salariés associés mentionnés aux articles L. 7331-2 et L. 7331-3 du code du travail',
                   'Les références à un statut ou à un dispositif particulier, notamment au 32°, ne dérogent pas à ces règles pour les nouveaux contrats de travail de droit privé.')]),
    benefit='Sont préservés pour les situations futures comme antérieures : le champ favorable d’affiliation malgré travail hors établissement, outillage ou pourboires ; les limites et exceptions des 4°, 11°, 19°, 21°, 24° et 27°, dont les options des indépendants et l’exclusion des risques CNBF sauf invalidité-décès ; les affiliations des créateurs accompagnés, services civiques, arbitres et gens de mer avec leurs réserves de régimes ; l’option du 35°, son seuil lié à 102 ter et ses abattements de 60 % et 87 % ; l’option du 37° sous 1 500 €, ses bornes d’abattement et sa sortie seulement après deux années consécutives ou dépassement du triple, à compter de l’année suivante. Le 22° ne crée pas une exonération de TVA autonome : son renvoi définit les dirigeants d’associations affiliés. La communication de marge du 20° est conservée pour le calcul social, sans nouveau justificatif. La durée d’une mission, formation ou aide n’éteint pas l’affiliation d’un emploi unique futur. Aucun avantage fiscal, abattement, dispense ou rattachement favorable de la source n’est supprimé au motif du contrat unique, de la CVAE ou de la capitalisation.')

new = ''.join([
    p("Sous réserve des dispositions applicables au régime agricole, les salariés employés par une entreprise de travail temporaire pour l’exécution de missions relèvent ou, le cas échéant, continuent de relever du régime général de sécurité sociale, même si leur activité est exercée pour le compte d’un utilisateur entrant dans le champ d’application, soit d’une organisation spéciale de sécurité sociale, soit d’un autre régime de sécurité sociale."),
    p("Cette règle s’applique aux contrats de travail uniques à durée indéterminée conclus à compter de l’entrée en vigueur de la loi les instituant, pendant les missions et les intermissions. La fin d’une mission n’emporte ni rupture du contrat ni changement d’affiliation. Les contrats de travail temporaire conclus avant cette entrée en vigueur et les droits nés de leur exécution restent régis par leurs dispositions transitoires ; le présent article n’autorise aucune conclusion ni aucun renouvellement à durée déterminée après cette date. La garantie mensuelle de rémunération et la prise en compte des intermissions prévues pour l’emploi intérimaire à durée indéterminée ne sont pas réduites par le présent article.")
])
put('L311-4', new,
    'Coordination nécessaire de l’intérim avec le contrat unique : la règle de régime social demeure attachée au salarié de l’entreprise de travail temporaire, indépendamment du régime de l’utilisateur. Le nouveau corps couvre explicitement les missions et intermissions sans recréer un contrat de mission à terme ; réserve agricole et transition des anciens contrats conservées.',
    'Le texte ne convertit pas tous les salariés agricoles, agents publics ou régimes spéciaux au contrat privé. La mention de la garantie mensuelle et des intermissions conserve la protection de l’intérim à durée indéterminée sans promettre de nouvelle rémunération au portage. L1251-58-1 a été lu dans le corpus : contrat de mise à disposition et lettre de mission ne sont pas la durée de l’emploi ; aucun renvoi nouveau à cet article non fourni comme cible n’est ajouté dans proposed_xml. L1234-3 proposé n’est pas fourni ; son point de départ, fixé par la coordination, ne doit pas être remplacé par la fin de mission.',
    impact('coordination_only',
           'La proposition adapte le support contractuel de la couverture sociale existante ; elle ne supprime aucune cotisation et ne compte pas les intermissions déjà protégées comme un avantage nouveau.',
           'Les règles de rupture et de rémunération sont portées par le code du travail ; leur réécriture réglementaire complète n’est pas faite ici. La réserve agricole reste opposable.',
           'Aucune charge nouvelle n’est identifiée : pas de déclaration de mission supplémentaire ni d’affiliation nouvelle par mission ; garanties de rémunération et d’intermission existantes préservées.',
           [effect('coordination', CONTRACT,
                   'Raccordement du régime social de l’intérim aux nouveaux contrats uniques, avec maintien de la transition et de la couverture entre missions.',
                   'Rattachement au régime général des salariés liés par un contrat de travail temporaire, sous réserve agricole, quel que soit le régime de l’utilisateur.',
                   'Même rattachement pour les emplois intérimaires uniques à durée indéterminée et transition des anciens contrats temporaires.',
                   'regime', 'Salariés employés pour des missions d’intérim, sous réserve du régime agricole.',
                   'Nouvelles embauches à durée indéterminée ; contrats antérieurs et droits acquis conservés jusqu’à leur terme selon leur régime.',
                   'les salariés liés par un contrat de travail temporaire relèvent ou, le cas échéant, continuent de relever du régime général de sécurité sociale',
                   'La fin d’une mission n’emporte ni rupture du contrat ni changement d’affiliation.')]))

new = by_number['L311-5']['source_xml']
new = replace_once(new,
                   "Toute personne percevant l'une des allocations mentionnées à l'article L. 5123-2 ou aux articles L. 1233-65 à L. 1233-69 et L. 1235-16 ou au 8° de l'article L. 1233-68 du code du travail ou l'un des revenus de remplacement mentionnés à l'article L. 5421-2 du même code",
                   "Toute personne percevant l’une des allocations mentionnées à l’article L. 5123-2, aux articles L. 1233-65 à L. 1233-69 ou au 8° de l’article L. 1233-68 du code du travail, l’indemnité prévue au deuxième alinéa de l’article L. 1235-16 du même code ou l’un des revenus de remplacement mentionnés à l’article L. 5421-2 de ce code")
put('L311-5', new,
    'Coordination de renvoi nécessaire : la source qualifie globalement d’allocations les sommes visées, alors que le deuxième alinéa de L1235-16 prévoit une indemnité de réparation après annulation collective. La proposition la nomme expressément sans supprimer le maintien social qui y était rattaché. Les autres alinéas sont intégralement maintenus : chômage après congé parental, reprise insuffisante, indemnités maladie nulles ou maternité indépendante de faible niveau. Aucun allègement de prélèvement n’est attribué à cette rectification.',
    'L1233-67 rompt le contrat lors de l’adhésion au CSP ; L1233-68 8° fixe l’allocation, ses cumuls et suspensions. L1233-69 proposé supprime une contribution patronale de financement, non les allocations ni le maintien de droits sociaux : conserver ce champ ne rétablit pas le versement. Le renvoi L1235-16 est précisé à son deuxième alinéa : indemnité d’au moins six mois de salaire en l’absence de réintégration, distincte de l’indemnité ordinaire et de son plafond. La source présentait cette indemnité comme une allocation ; cette discordance est explicitement corrigée sans inventer une nouvelle durée de maintien ni qualifier la réparation de salaire. La note de 2021 conserve ses dates d’arrêts et de maternité 2019/2020 ; elles ne deviennent pas la date de la réforme. La durée déterminée par décret au premier alinéa concerne les prestations et non un terme d’emploi. Les droits antérieurs et futurs couverts par le maintien ne sont pas fermés.',
    impact('coordination_only',
           'La catégorie de somme visée par L1235-16 est rectifiée, en conservant les bénéficiaires du maintien social déjà désignés par la source entière ; aucune réduction ni nouvelle prestation n’est comptée.',
           'Le financement du CSP, les durées réglementaires du maintien et les règles d’assurance chômage restent à leur champ ; aucun plafond d’indemnité ou délai de préavis n’est importé dans ce droit social.',
           'Aucune charge nouvelle n’est identifiée : pas de demande, pièce, ancienneté ou notification nouvelle ; seul le renvoi à une indemnité déjà visée est précisé.',
           [effect('coordination', 'maintien-droits-assurance-rupture',
                   'Rectification de la qualification et de la subdivision de L1235-16 sans fermeture du maintien d’assurance.',
                   'L1235-16 est cité parmi des textes d’allocations, bien qu’il prévoie une indemnité spéciale d’annulation collective.',
                   'La réparation du deuxième alinéa de L1235-16 est expressément identifiée comme indemnité, avec le même maintien de droits.',
                   'other', 'Personnes percevant l’indemnité spéciale après annulation collective sans réintégration, déjà visées par le renvoi source.',
                   'Coordination sans suppression des droits des bénéficiaires antérieurs ou futurs ; durées réglementaires et autres conditions du maintien inchangées.',
                   'aux articles L. 1233-65 à L. 1233-69 et L. 1235-16',
                   'l’indemnité prévue au deuxième alinéa de l’article L. 1235-16 du même code')]))

retain('L311-6',
       'Maintien intégral de l’affiliation du conjoint salarié participant effectivement, professionnellement et habituellement à l’activité. Le salaire normal de la catégorie et le plancher horaire SMIC pour les activités diverses ou non conventionnées protègent l’activité réelle et la rémunération ; les retirer isolément pourrait réduire les droits du conjoint ou permettre des affiliations fictives.',
       'La participation effective et le salaire de catégorie ne sont ni un agrément préalable ni un justificatif périodique supplémentaire. La règle n’impose pas de durée déterminée du contrat et s’applique aux futurs emplois éligibles ; elle ne transforme pas un conjoint collaborateur non salarié en salarié sans travail rémunéré.',
       'Le rattachement et les deux garanties salariales sont conservés en entier ; aucun prélèvement accessoire supprimable n’est institué par la source.',
       'L’article ne fixe pas le taux des cotisations et ne démontre pas une baisse du coût de l’emploi ; les autres statuts du conjoint ne sont pas refondus ici.')

retain('L311-7',
       'Maintien intégral des droits sociaux des travailleurs étrangers, de l’exception de résidence pour la vieillesse, du maintien des soins des anciens migrants lors de leurs séjours en France et de la couverture conventionnelle des frontaliers résidant à l’étranger. La condition territoriale distingue les risques et garde ses dérogations ; elle ne justifie pas la production répétée de pièces déjà légalement disponibles.',
       'Le renvoi à L117-3 du code de l’action sociale et des familles conserve l’aide à la réinsertion et les soins lors des séjours futurs recevables, pas seulement avant la réforme. Les règles européennes et conventions internationales de sécurité sociale gardent leur primauté et leur coordination ; aucune abrogation nationale de leur champ n’est présumée. Le réemploi de justificatifs déjà détenus est déjà prévu par le CRPA et ne serait pas une nouvelle coupe propre à cet article.',
       'Les exceptions favorables à la résidence et les régimes conventionnels sont conservés ; aucune restriction de résidence supplémentaire ou fermeture de droit futur n’est créée.',
       'Les conventions et droits européens applicables selon le pays ne sont pas tous joints ; le maintien ne prétend pas constituer leur inventaire exhaustif.',
       benefit='Le premier alinéa ouvre les assurances sociales aux travailleurs étrangers et personnes rattachées et dispense expressément la vieillesse de justification de résidence en France. Le deuxième maintient les prestations en nature maladie et maternité, lors des séjours en France des bénéficiaires de l’aide L117-3, dans l’ancien régime ou à défaut au régime général : cette dérogation reste ouverte aux futurs bénéficiaires éligibles. Le troisième conserve le bénéfice conventionnel pour les résidents à l’étranger travaillant de façon permanente en France. Aucune de ces exceptions ni la coordination européenne n’est supprimée ; la résidence pour les autres prestations reste une condition de champ, non un impôt ou une nouvelle obligation déclarative autonome.')

new = by_number['L311-11']['source_xml']
new = replace_once(new, "au premier alinéa de l'article L. 8221-6", "au I de l’article L. 8221-6")
new = replace_once(new, 'dans le délai de deux mois', 'dans le délai d’un mois')
new += p("Le délai d’un mois s’applique aux demandes reçues à compter de l’entrée en vigueur de la loi portant la présente réforme. Les demandes antérieures restent soumises au délai de deux mois ; les réponses et garanties déjà acquises sont conservées. Aucun dépôt de renouvellement ou de confirmation périodique n’est exigé du seul fait de cette réforme.")
put('L311-11', new,
    'Réforme de fond : le silence protecteur sur le rattachement social devient acquis après un mois au lieu de deux pour les nouvelles demandes. La demande reste facultative et les seules causes de remise en cause demeurent la modification substantielle d’activité ou les informations erronées. Coordination du renvoi aux personnes du I de L8221-6, dont l’énumération ne tient pas au seul premier alinéa introductif.',
    'L8221-6 officiel a été lu en entier dans travail.json ; il n’est pas une cible fournie dans reference-targets.json mais figure déjà dans la source. Le I énumère les personnes présumées indépendantes et le II réserve la subordination permanente et le travail dissimulé. Aucun droit à un CDD, aucune immunité de fraude et aucune ancienneté de licenciement ne sont créés. Le délai est d’un mois, sans conversion arbitraire en trente jours et sans notion nouvelle de dossier complet. Capacité de traitement des organismes et effet contentieux à apprécier ; aucun coût net ni recette de compensation n’est inventé.',
    impact('material_reduction',
           'Le délai avant sécurisation tacite de la situation d’affiliation est effectivement réduit de deux mois à un mois ; la condition de subordination permanente et les exceptions à l’opposabilité restent intactes.',
           'Ce délai ne réduit ni cotisations dues ni préavis de rupture ; les demandes antérieures restent à deux mois. Le coût administratif et le solde net global ne sont pas établis.',
           'Aucune charge nouvelle n’est identifiée : même demande facultative, sans nouvelle pièce ni confirmation périodique. Le délai de réponse de l’organisme est raccourci, sans prestation de traitement nouvelle.',
           [effect('deadline_reduced', 'rescrit-affiliation-silence-un-mois',
                   'Réduction de l’attente avant l’opposabilité du silence de l’organisme sur le rattachement social.',
                   'Deux mois suivant la demande facultative pour obtenir la protection du silence, pour les personnes physiques présumées indépendantes visées.',
                   'Un mois suivant la même demande, pour les demandes nouvelles ; même protection et mêmes exceptions.',
                   'other', 'Personnes physiques du I de L8221-6 demandant la détermination de leur affiliation.',
                   'Demandes reçues à compter de l’entrée en vigueur ; demandes antérieures, réponses et garanties acquises préservées.',
                   'A défaut de réponse dans le délai de deux mois suivant la date de cette demande',
                   'A défaut de réponse dans le délai d’un mois suivant la date de cette demande')]),
    removed=['Attente supplémentaire du deuxième mois avant que le silence de l’organisme ne protège le demandeur contre une affiliation ultérieure, pour les demandes nouvelles.'])

new = by_number['L313-1']['source_xml']
new = replace_once(new, "l'assuré doit, en outre, justifier d'une durée minimale d'affiliation.",
                   'aucune durée minimale d’affiliation distincte des conditions de rémunération ou de travail salarié ou assimilé n’est exigée. Les conditions de rémunération ou de travail salarié ou assimilé applicables à chacune de ces prestations demeurent inchangées.')
new += p("III.-La suppression de la durée minimale d’affiliation prévue au II s’applique aux prestations dues pour les périodes courant à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris lorsque l’arrêt de travail ou le congé a débuté avant cette date. Aucun justificatif de cette seule durée ne peut être exigé pour ces périodes. Les conditions de rémunération, d’heures de travail, de période de référence, de constatation de l’incapacité et de cessation d’activité propres à chaque prestation demeurent applicables. Les assimilations et dérogations plus favorables sont préservées pour les situations antérieures et futures éligibles. Les prestations afférentes aux périodes antérieures, leurs créances, régularisations, restitutions, prescriptions et recours restent régis par les dispositions antérieures, sans restitution générale ni double paiement.")
put('L313-1', new,
    'Réforme de fond : suppression de la condition additionnelle de durée minimale d’affiliation du II, qui s’ajoute aux seuils de rémunération ou de travail. Les alternatives contributives et les conditions propres à chaque durée de maladie et à la maternité sont maintenues, ainsi que les numéros I, 1° abrogé, 2°, 3° et II, 1°, 2°. L’allègement s’applique aux périodes futures même après un arrêt déjà commencé, sans rétroactivité générale ni fermeture des assimilations favorables.',
    'R313-3, lu en entier, impose six mois d’affiliation pour les indemnités de maternité et douze mois pour la maladie au-delà du sixième mois ; seuls ces minima d’affiliation doivent être retirés. Conserver 1 015 SMIC/150 heures sur les références courtes et 2 030 SMIC/600 heures sur douze mois pour la maladie prolongée, les conditions n’étant pas fusionnées. R313-4 doit perdre son seul minimum de six mois d’affiliation pour l’adoption, sans suppression de ses conditions de cotisations/heures ni de la preuve civile de l’adoption ; sa formule « trois mois civils ou des trois mois » est une incohérence source signalée, non corrigée silencieusement. R313-1 conserve ses dates de référence, dont le congé supplémentaire de naissance au 1er juillet 2026. R313-7 conserve l’alternative favorable saisonnière/discontinue et CESU. Les textes réglementaires restent hors lot à coordonner. Aucun minimum d’invalidité ou de prestation d’indépendant n’est supprimé par extension. Ce délai d’affiliation n’est ni le seuil d’un an de L1234-9 ni le préavis de quinze jours.',
    impact('material_reduction',
           'L’obstacle additionnel d’affiliation minimale pour la maladie prolongée et les indemnités de maternité disparaît par rapport à la source entière, avec maintien des seuils contributifs spécifiques et des droits plus favorables.',
           'Ni les seuils d’heures ou de rémunération, ni les règles des indépendants, d’invalidité et de contrôle médical ne sont abolis. L’extension des droits peut augmenter les prestations versées ; son coût public net n’est pas chiffré.',
           'Aucune charge nouvelle n’est identifiée : aucun agrément, délai, pièce, registre ou déclaration ne remplace la durée d’affiliation retirée. Les conditions restantes sont celles de chaque régime existant.',
           [effect('obligation_removed', 'prestations-fin-minimum-affiliation-additionnel',
                   'Suppression de la durée minimale d’affiliation additionnelle et de sa seule justification pour les prestations du II.',
                   'Condition additionnelle d’affiliation minimale ; règlements lus : six mois pour la maternité/adoption, douze mois pour la maladie prolongée, en plus des seuils de travail ou de cotisations.',
                   'Aucune durée minimale d’affiliation autonome pour ces prestations ; conditions de rémunération ou de travail et autres conditions propres inchangées.',
                   'legal_duty', 'Assurés demandant la maladie au-delà de la première durée ou les indemnités journalières de maternité couvertes par le II.',
                   'Périodes indemnisées à compter de l’entrée en vigueur, même pour arrêt ou congé en cours ; périodes anciennes et dérogations favorables conservées.',
                   "l'assuré doit, en outre, justifier d'une durée minimale d'affiliation.",
                   'aucune durée minimale d’affiliation distincte des conditions de rémunération ou de travail salarié ou assimilé n’est exigée.')]),
    removed=['Condition additionnelle de durée minimale d’affiliation prévue au II, distincte des seuils de rémunération ou de travail, pour la maladie prolongée et les indemnités journalières de maternité.',
             'Exigence de justifier cette seule durée minimale d’affiliation pour les périodes de prestations couvertes par la réforme.'])

retain('L313-2',
       'Maintien intégral du fondement des assimilations de périodes d’inactivité au travail salarié pour ouvrir les droits. Ce renvoi favorable évite que l’interruption d’activité ferme nécessairement les prestations ; le supprimer ferait disparaître une protection future sans retirer la condition contributive générale.',
       'L383-1 reste le renvoi réglementaire de mise en œuvre déjà présent, sans nouveau texte ou attestation inventé. La suppression du minimum d’affiliation de L313-1 II ne supprime pas les assimilations utiles aux seuils d’heures ou de rémunération, ni les périodes antérieures couvertes.',
       'Les assimilations favorables restent intégralement fondées pour les futurs assurés éligibles ; aucune simplification nouvelle n’est comptée pour leur maintien.',
       'La liste et les modalités réglementaires des assimilations doivent conserver leur champ propre ; cet article ne prouve pas une baisse des taux ou une disparition de toute condition contributive.')

retain('L313-6',
       'Maintien intégral de la neutralisation des interruptions liées à un accident ou une maladie en service de sapeur-pompier volontaire dans les durées de droits maladie pour les autres affections. Cette dérogation favorable à L313-1 reste utile malgré la suppression du minimum d’affiliation : elle protège les durées de service des prestations, non cette seule condition d’ouverture.',
       'Le renvoi à L313-1 demeure cohérent avec la proposition qui conserve les prestations, leurs durées et leurs conditions contributives. Le champ est l’arrêt imputable au service volontaire et non tout arrêt professionnel ou tout agent public ; ni quinze jours de préavis ni un an d’ancienneté de rupture ne s’y substituent.',
       'La neutralisation favorable est conservée en entier pour les services et sinistres futurs comme les droits antérieurs ; ce maintien ne constitue pas une nouvelle réduction.',
       'Les autres durées maximales de droits et les conditions des régimes professionnels distincts ne sont pas supprimées par cette exception.',
       benefit='L’avantage est la non-imputation des interruptions de travail dues à l’accident ou à la maladie contractés en service de sapeur-pompier volontaire sur les durées de droits maladie utilisables pour d’autres accidents ou maladies. Il est intégralement maintenu sans restriction aux situations antérieures et prime L313-1 ainsi que toute disposition contraire. La suppression proposée du minimum d’affiliation additionnel n’épuise pas cet avantage, qui concerne aussi la durée de service des prestations. Aucune nouvelle attestation ou ancienneté de contrat ne le conditionne.')

retain('L314-1',
       'Maintien intégral des vérifications de prise en charge, de conformité clinique, de tarification, d’engagements conventionnels et d’inscription ordinale obligatoire. La demande d’éléments est limitée à ce qui est nécessaire ; elle sert à contrôler le droit réel et la fraude, et n’est pas un rapport périodique général. La responsabilité respective de l’assuré et du professionnel reste appréciée avant les conséquences sur la prise en charge.',
       'Le 1° vise L315-2 dans son champ réformé : aucune preuve d’accord ne sera exigible pour le seul coût d’une prestation, contrairement aux motifs médicaux maintenus. L162-4-1 a un plafond de prescription et sa dérogation clinique, sans rapport avec le préavis de travail. L114-17-1 conserve notamment bonne foi et sanctions de fraude ; L162-1-15 concerne une mesure ciblée sur pratiques atypiques, contradictoire et au plus six mois, avec dispense d’urgence, distincte des accords généraux de L315-2. Aucun nouvel accès aux données n’est créé : les droits de réemploi du CRPA existent déjà. La note du 1er janvier 2026 ne date pas la réforme.',
       'La source officielle entière est conservée : contrôles nécessaires et imputabilité de l’irrégularité, sans nouvelle restriction des avantages médicaux ou tarifaires.',
       'Aucune baisse nouvelle de cotisation ni suppression globale des accords préalables n’est démontrée ici ; les sanctions et procédures visées conservent leur contrôle propre.')

new = by_number['L315-1']['source_xml']
old = "Lorsque l'activité de prescription d'arrêt de travail apparaît anormalement élevée au regard de la pratique constatée chez les professionnels de santé appartenant à la même profession, des contrôles systématiques de ces prescriptions sont mis en oeuvre dans des conditions définies par la convention mentionnée à l'article L. 227-1."
replacement = "Le seul constat d’une activité de prescription d’arrêt de travail anormalement élevée au regard de la pratique des professionnels de santé de la même profession ne rend pas obligatoire le contrôle systématique de ces prescriptions. Le service du contrôle médical conserve ses pouvoirs de contrôle et de constatation des abus prévus au présent article."
new = replace_once(new, old, replacement)
new += p("IX.-La suppression de l’obligation de contrôle systématique prévue au deuxième alinéa du II s’applique aux contrôles effectués à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris lorsqu’ils portent sur des prescriptions antérieures. Les contrôles en cours se poursuivent, s’il y a lieu, dans l’exercice des pouvoirs de contrôle maintenus, sans contrôle systématique rendu obligatoire par le seul niveau statistique de prescription. Les constatations, décisions, créances, prescriptions et recours antérieurs sont préservés. Les droits de la défense, le secret médical et les droits des assurés prévus au présent article demeurent applicables.")
put('L315-1', new,
    'Réforme de fond ciblée : retrait du contrôle obligatoirement systématique de toutes les prescriptions dès qu’un niveau statistique est anormalement élevé. Les pouvoirs d’enquête, de contrôle et de constatation des abus restent entiers, tout comme la contre-visite patronale, les examens de droit et les garanties médicales. L’alinéa est conservé à sa place avec une règle de non-automaticité ; tous les autres alinéas I à VIII et leurs références restent exacts.',
    'La convention L227-1 doit perdre le seul automatisme retiré ; ses autres missions ne sont pas supprimées. L1226-1, cible directe non fournie dans reference-targets.json mais déjà citée dans la source, a été lu en entier dans le corpus : l’année d’ancienneté de son complément maladie est distincte de l’année de l’indemnité ordinaire L1234-9, et reste à son champ. La transmission du rapport sous quarante-huit heures, le nouvel examen de droit si le premier était impossible, l’avis motivé au médecin patronal sans effet du défaut sur les droits, la vérification d’identité, la stricte nécessité des données et l’opposition au transfert sont conservés. La baisse du nombre effectif de contrôles et le coût net ne sont pas chiffrés. Les pouvoirs ciblés de L162-1-15 ne sont pas implicitement abrogés.',
    impact('material_reduction',
           'Une obligation de contrôle automatique et exhaustif liée au seul écart statistique est supprimée, sans retirer aucun pouvoir de contrôle médical ni aucune protection procédurale de la source entière.',
           'La réforme ne garantit pas moins de contrôles dans chaque cas : les contrôles justifiés et la lutte contre la fraude restent possibles. Aucun gain budgétaire ou coût net national n’est établi.',
           'Aucune charge nouvelle n’est identifiée : les pouvoirs de contrôle sont ceux déjà existants ; aucun registre, indicateur supplémentaire, protocole ou rapport de remplacement n’est créé.',
           [effect('obligation_removed', 'controle-medical-fin-systematisme-statistique',
                   'Suppression de l’obligation de contrôler systématiquement les prescriptions en raison du seul niveau statistique.',
                   'Contrôle systématique obligatoire lorsque les prescriptions d’arrêts apparaissent anormalement élevées par rapport à la même profession.',
                   'Absence d’automatisme obligatoire sur ce seul constat ; pouvoirs de contrôle et de constatation des abus maintenus.',
                   'legal_duty', 'Service du contrôle médical et professionnels dont le niveau de prescription est statistiquement élevé.',
                   'Contrôles effectués après l’entrée en vigueur, y compris sur prescriptions anciennes ; contrôles justifiés en cours et droits antérieurs préservés.',
                   old, 'Le seul constat d’une activité de prescription d’arrêt de travail anormalement élevée au regard de la pratique des professionnels de santé de la même profession ne rend pas obligatoire le contrôle systématique de ces prescriptions.')]),
    benefit='Sont intégralement maintenus : le droit de demander un examen après suspension d’indemnités, les délais réglementaires de saisine et de décision, le nouvel examen de droit quand le médecin patronal n’a pas pu examiner l’assuré, les droits de la défense lors de l’analyse de l’activité, le secret médical et l’accès aux seules données strictement nécessaires, l’opposition du bénéficiaire au transfert d’informations entre services et la qualification encadrée des délégations. L’avis écrit motivé adressé au médecin patronal lorsqu’il n’est pas suivi reste dû ; son omission reste sans effet sur les droits des salariés ou employeurs. Les prestations maladie, maternité, invalidité, AME et soins urgents ne sont pas réduites et les futurs bénéficiaires restent éligibles. Le retrait du systématisme ne dispense pas des contrôles utiles et ne supprime aucune garantie médicale favorable.',
    removed=['Contrôles rendus systématiquement obligatoires par le seul constat statistique d’une prescription d’arrêts de travail anormalement élevée, ainsi que l’habilitation conventionnelle à imposer cet automatisme.'])

new = by_number['L315-2']['source_xml']
new = replace_once(new, 'Cet accord préalable peut être exigé pour une prestation dans l\'un des cas suivants :',
                   'Cet accord préalable ne peut être exigé que pour l’un des deux motifs médicaux mentionnés aux deuxième et troisième alinéas du présent A.')
old_cost = "-la prestation, à titre unitaire ou compte tenu de son volume global, a, de manière prévisible ou constatée, un caractère particulièrement coûteux pour l'assurance maladie ou pour l'Etat en ce qui concerne les prestations servies en application des articles L. 251-2 et L. 254-1 du code de l'action sociale et des familles ;"
old_alt = '-le recours à une autre prestation est moins coûteux.'
new = replace_once(new, old_cost,
                   '-le seul coût de la prestation, à titre unitaire ou compte tenu de son volume global, ne peut justifier un accord préalable ;')
new = replace_once(new, old_alt,
                   '-le seul recours possible à une autre prestation moins coûteuse ne peut justifier un accord préalable.')
new = replace_once(new, "Dans ces cas, les conditions d'application du présent article sont fixées par décret en Conseil d'Etat.",
                   "Dans ces cas, les conditions d'application du présent article sont fixées par décret en Conseil d'Etat. Les décisions du collège des directeurs et les arrêtés ministériels prévus au présent A ne peuvent imposer un accord préalable que pour les motifs médicaux prévus aux deuxième et troisième alinéas du présent A, à l’exclusion du seul coût ou de la seule existence d’une prestation moins coûteuse.")
new += p("V.-L’exclusion des motifs exclusivement économiques d’accord préalable prévue au II s’applique aux prestations réalisées ou délivrées à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris sur prescription antérieure. Pour ces prestations, les clauses des décisions ou arrêtés imposant un accord préalable sur ces seuls motifs cessent de s’appliquer ; les demandes en cours fondées exclusivement sur ces motifs sont closes sans nouveau dépôt ni déclaration de remplacement. Les accords déjà obtenus et les décisions tacites favorables restent opposables dans leur champ, sans nouvelle demande. Les conditions médicales de prise en charge, les contrôles prévus aux I, III et IV et les régimes particuliers de contrôle reposant sur un fondement autonome restent applicables. Les prestations antérieures, créances, régularisations, restitutions, prescriptions et recours correspondants conservent leur régime, sous réserve de l’application des dispositions répressives plus douces aux sanctions non définitives.")
put('L315-2', new,
    'Réforme de fond : le seul coût, unitaire ou global, et la seule existence d’une prestation moins chère ne permettent plus d’imposer un accord préalable. Le circuit est conservé pour les indications médicales, le mésusage, l’innovation à évaluer et les risques encourus ; les voies UNCAM et ministérielles ne peuvent contourner la suppression. Les alinéas des anciens motifs économiques sont conservés à leur place sous forme d’exclusions, sans déplacer les autres subdivisions. Accords tacites, dispense d’homologation des formulaires, information, contrôles, suspension médicalement justifiée et recours restent complets.',
    'Les deuxième et troisième alinéas du II A sont les deux motifs médicaux suivant son premier alinéa introductif : leur désignation exclut les deux alinéas économiques devenus négatifs. Les régimes de produits et listes cités dans le long alinéa ministériel, L5123-2 santé publique et l’association L162-18-1 restent dans leur champ, soumis à cette limite. Les cibles L162-16-5-1-1 et L162-16-5-2 portent sur prix/remises et accès précoce ou compassionnel : leurs remises, restitutions, décote de 3 %, étalement et continuités de soins ne sont pas supprimés. La proposition n’abroge pas la mise sous accord préalable ciblée L162-1-15, régime autonome de prévention d’abus avec urgence protégée. Les décisions UNCAM, arrêtés, formulaires et règlements d’exécution doivent être purgés des seuls motifs retirés ; leur réécriture intégrale n’est pas déclarée réalisée. L315-3 est coordonné dans le présent lot. Le coût accru éventuel des prestations et l’effet administratif net restent à évaluer sans compensation inventée.',
    impact('material_reduction',
           'Le champ de l’autorisation de remboursement est réellement réduit : deux motifs purement économiques de la source entière disparaissent pour les soins futurs, y compris par voie ministérielle. Les critères et protections médicales sont maintenus.',
           'Tous les accords préalables ne sont pas supprimés ; les deux motifs médicaux et les dispositifs autonomes ciblés demeurent. Ni baisse du prix des produits ni économie nationale ou solde public net ne sont démontrés.',
           'Aucune charge nouvelle n’est identifiée : aucun agrément, formulaire, déclaration, justificatif ou délai ne remplace les accords retirés. La limitation des motifs réduit le pouvoir existant et les échanges sécurisés restants sont conservés.',
           [effect('authorization_removed', MEDICAL,
                   'Suppression des accords préalables fondés exclusivement sur le coût de la prestation ou une alternative moins coûteuse, par toutes les voies du II A.',
                   'Accord préalable possible du seul fait d’un coût unitaire ou global particulièrement élevé ou d’une autre prestation moins coûteuse ; critères médicaux également possibles.',
                   'Coût et alternative moins chère insuffisants à eux seuls ; seuls les deux motifs médicaux maintenus peuvent fonder l’accord général du II A.',
                   'legal_duty', 'Assurés, bénéficiaires AME/soins urgents, prescripteurs et distributeurs concernés par les prestations du II.',
                   'Prestations réalisées ou délivrées dès l’entrée en vigueur, même prescrites avant ; anciens soins et accords favorables préservés, dossiers exclusivement économiques clos.',
                   old_alt,
                   '-le seul recours possible à une autre prestation moins coûteuse ne peut justifier un accord préalable.')]),
    benefit='Restent intégralement ouverts, pour les situations futures : l’accord tacite à défaut de réponse dans le délai réglementaire propre à la prestation ; l’information sur l’accord éventuellement nécessaire ; la dérogation à l’homologation de formulaires du II B 2° ; l’information de l’assuré avant suspension, son information directe après examen, le pouvoir de différer la date d’effet et les contestations médicales. La réserve de L324-1 et les soins AME/urgents restent dans leur champ. Les régimes d’accès précoce, compassionnel et transitoire visés ne perdent ni leur prise en charge favorable ni leurs restitutions ou remises aménagées : seule une condition préalable exclusivement économique cesse pour les nouveaux soins. Les accords exprès et tacites déjà favorables restent opposables sans nouvelle demande ; aucun avantage n’est limité aux situations antérieures. Les motifs médicaux et contrôles d’abus autonomes sont conservés.',
    removed=['Faculté d’imposer un accord préalable au seul motif du coût particulièrement élevé, unitaire ou global, pour l’assurance maladie ou l’État dans le champ de l’article.',
             'Faculté d’imposer un accord préalable au seul motif qu’une autre prestation serait moins coûteuse, y compris par décision UNCAM ou arrêté ministériel.'])

retain('L315-2-1',
       'Maintien intégral de l’évaluation thérapeutique individualisée hors des cas de L324-1. Elle repose sur l’importance des soins ou la fréquence des arrêts, permet des recommandations avec le médecin choisi par l’intéressé et conserve un circuit de communication médicale protecteur. Elle n’est pas une autorisation économique préalable et ne double pas un rapport périodique général.',
       'La convocation facultative évalue l’intérêt thérapeutique et ne vaut ni retrait automatique de prestations ni obligation nouvelle de soins imposés. Les assurés, bénéficiaires de l’AME et des soins urgents restent couverts. La suppression du systématisme de L315-1 et des motifs économiques de L315-2 ne supprime pas cette évaluation clinique distincte.',
       'Le dispositif clinique et le choix du médecin sont conservés en entier ; aucune réduction nouvelle de charge n’est attribuée à leur maintien.',
       'L’évaluation peut conduire aux contrôles ou suites légalement prévus ailleurs ; cet article ne démontre pas une suppression de toutes les convocations médicales.',
       benefit='L’avantage procédural est la participation possible d’un médecin choisi par l’intéressé à l’élaboration des recommandations et, lorsqu’elles sont conjointes, leur transmission par ce médecin. Cette possibilité et la communication subsidiaire par le service médical sont intégralement maintenues pour les assurés, l’AME et les soins urgents, sans fermeture des situations futures. L’exclusion des cas relevant déjà de L324-1 conserve leur régime spécifique ; elle ne supprime pas leur prise en charge. La convocation sert l’évaluation thérapeutique et ne constitue ni une exonération fiscale ni un accord économique désormais supprimé.')

new = ''.join([
    p("I.-Lorsque la prise en charge de médicaments, ou de produits et prestations éventuellement associées mentionnés à l’article L. 165-1, demeure légalement subordonnée à la procédure d’accord préalable prévue au II de l’article L. 315-2, le pharmacien, le prestataire de services ou tout autre distributeur de matériel auprès du public informe le patient de ces conditions particulières de prise en charge."),
    p("II.-Tout pharmacien, distributeur ou prestataire est tenu de s’assurer que l’accord du service du contrôle médical autorisant la prise en charge par l’assurance maladie des médicaments ou des produits et prestations mentionnés au I a été donné, expressément ou tacitement dans les conditions de l’article L. 315-2. Pour la prise en charge de ces médicaments ou produits et prestations par l’assurance maladie, il est tenu d’agir conformément à la décision du service du contrôle médical. Aucune preuve d’accord préalable n’est exigée sur le fondement du présent article lorsque cet accord n’est plus requis en application de l’article L. 315-2."),
    p("III.-Le non-respect par tout pharmacien, distributeur ou prestataire des obligations prévues au II peut donner lieu à un recouvrement de l’indu selon la procédure prévue à l’article L. 133-4."),
    p("IV.-Pour les prestations réalisées ou délivrées à compter de l’entrée en vigueur de la loi portant la présente réforme, les obligations du présent article s’appliquent dans le seul champ des accords préalables maintenus par l’article L. 315-2. Aucun recouvrement ne peut être fondé, pour ces prestations, sur l’absence d’un accord supprimé. Les prestations antérieures, leurs créances, régularisations, restitutions, prescriptions et recours conservent leur régime, sous réserve des dispositions répressives plus douces applicables aux sanctions non définitives. Les accords favorables déjà obtenus restent opposables dans leur champ sans nouvelle demande.")
])
put('L315-3', new,
    'Coordination de la réduction des accords de L315-2 : l’information, la vérification par le distributeur et l’indu ne concernent que les accords encore légalement requis. Le caractère exprès ou tacite, déjà prévu par L315-2, est explicité sans seconde décision ni attestation. Le renvoi de recouvrement à L133-4 et l’information protectrice du patient sont conservés ; aucun indu ne peut sanctionner l’absence d’un accord économique supprimé pour des soins futurs.',
    'L133-4, fourni en source et proposition, conserve le recouvrement auprès du responsable, le contradictoire, prescription de trois ans sauf fraude, deux mois pour observations, un mois après mise en demeure, restitution aux assurés et complémentaires, minoration HAD et remises possibles. Ce renvoi ne rétablit pas les obligations d’accord retirées. L165-1 est déjà un renvoi de la source, sans nouvelle liste de produits inventée. Les prescriptions anciennes pour délivrances futures suivent la transition L315-2 ; les soins anciens conservent leur régime et les sanctions non définitives restent soumises à la loi plus douce. Aucun nouveau certificat de silence de l’organisme n’est imposé.',
    impact('coordination_only',
           'La proposition empêche que l’exécution et le recouvrement rétablissent les accords économiques retirés par L315-2 ; les obligations résiduelles d’information et de vérification ne sont pas une seconde suppression à compter.',
           'Les accords médicaux maintenus restent contrôlés, et les indus de soins antérieurs ne sont pas effacés de façon générale. Aucun gain national ou solde net de coût n’est établi.',
           'Aucune charge nouvelle n’est identifiée : les accords tacites étaient déjà favorables selon L315-2 et aucun certificat ou dépôt supplémentaire n’est créé. Information et contrôle restants sont ceux de la source.',
           [effect('coordination', MEDICAL,
                   'Limitation des vérifications du distributeur et des indus au champ d’accords effectivement maintenu.',
                   'Obligation de vérifier l’accord et de respecter la décision, avec recouvrement L133-4 en cas de manquement.',
                   'Mêmes obligations pour les seuls accords légalement maintenus ; aucune preuve ni indu au titre d’un accord économique supprimé.',
                   'legal_duty', 'Pharmaciens, distributeurs et prestataires délivrant les médicaments, produits et prestations visés, ainsi que leurs patients.',
                   'Prestations nouvelles même sur prescriptions anciennes ; créances et recours de soins antérieurs réservés, accords favorables conservés.',
                   "Tout pharmacien, distributeur ou prestataire est tenu de s'assurer que l'accord du service du contrôle médical autorisant la prise en charge par l'assurance maladie des médicaments ou des produits et prestations mentionnés à l'article L. 165-1 a été donné.",
                   'Aucune preuve d’accord préalable n’est exigée sur le fondement du présent article lorsque cet accord n’est plus requis en application de l’article L. 315-2.')]))

# Ces retraits d'exécution appartiennent aux mesures principales déjà identifiées.
# Ils restent des coordinations, sans compter une nouvelle réduction autonome.
for number, removed in {
    'L281-6': ['Extension aux unions et fédérations de l’approbation préalable des statuts, règlements intérieurs et modifications, retirée en coordination de l’abrogation de L281-4.'],
    'L315-3': ['Vérification d’un accord préalable et recouvrement pour sa seule absence lorsque les soins futurs relèvent exclusivement des motifs économiques supprimés à L315-2.']
}.items():
    answers[number].update(change_type='normative_reduction',
                           reform_policy_id='editorial_direction_2026_10_19',
                           removed_provisions=removed)

# Les analyses des cibles sont attachées seulement aux exigences de cet article.
work_contexts = {
    'L281-1': 'Le contrôle de la gestion des organismes sociaux ne règle pas la rupture de leurs emplois privés et le texte ne comporte aucun renvoi à cette cible.',
    'L311-3': 'La liste d’affiliation comprend des salariés privés, des assimilés et des agents publics ; elle ne transforme pas tous leurs statuts en contrats privés ni en droits à indemnité de rupture.',
    'L311-4': 'Le rattachement de l’intérimaire subsiste entre les missions de son emploi à durée indéterminée ; la fin de la mission commerciale ne vaut ni notification ni rupture de l’emploi.',
    'L311-5': 'Le maintien des prestations après chômage, congé parental ou reprise faiblement indemnisée ne prend pas pour condition l’ancienneté d’une indemnité ordinaire de rupture.',
    'L311-11': 'Le rescrit porte sur la subordination juridique permanente et le régime social des personnes présumées indépendantes ; son délai de réponse est distinct des règles de rupture d’un emploi salarié.',
    'L313-1': 'Les seuils de travail ou rémunération pour les prestations sociales et la suppression du minimum d’affiliation additionnel sont distincts de l’ancienneté de rupture chez un employeur.',
    'L313-6': 'La neutralisation de l’arrêt du sapeur-pompier volontaire pour le décompte des droits maladie demeure indépendante de la rupture de son éventuel emploi privé.',
    'L314-1': 'Les vérifications portent sur la prise en charge des soins et les responsabilités en cas d’irrégularité ; elles ne règlent aucune notification de licenciement ni indemnité de rupture.',
    'L315-1': 'Le contrôle des arrêts et de leur justification médicale n’est pas une procédure de rupture du contrat ; la contre-visite L1226-1 conserve son objet de complément maladie.',
    'L315-2': 'La prise en charge et les accords médicaux ne déterminent pas la durée de l’emploi ni ses indemnités ; les motifs économiques d’accord sont retirés dans leur seul champ social.',
    'L315-3': 'L’information du patient et la vérification de l’accord médical par le distributeur sont étrangères aux formalités de notification d’une rupture d’emploi.'
}
work_rules = {
    'L1234-1': 'L1234-1 officiel prévoit les paliers moins de six mois, six mois à moins de deux ans et au moins deux ans ; sa proposition substitue quinze jours calendaires pour les nouveaux contrats, même en faute grave avec paiement sans exécution. Les anciens préavis et les procédures collectives ou autorisations spéciales restent distincts. Le point de départ relève de L1234-3 proposé, non fourni ici : la coordination impose le lendemain de présentation ou réception de la notification écrite, jamais une fin de mission ou un contrôle médical.',
    'L1221-2': 'L1221-2 officiel permet encore un terme dans les cas du CDD ; sa proposition impose une durée indéterminée aux nouveaux contrats privés, sans rupture automatique à la fin d’une mission, formation ou aide. Les anciens contrats et créances gardent leur transition, sans renouvellement nouveau à terme ; aucune durée de prestations, d’accompagnement ou régime public n’est convertie en CDD.',
    'L1234-9': 'L1234-9 officiel ouvre l’indemnité après huit mois ; la proposition réserve l’indemnité ordinaire patronale aux nouveaux contrats atteignant un an au terme effectif, préavis inclus. Une fois le seuil atteint, 0,20 mois par année totale, fractions par mois complets, plafond six mois, sans retrait de la première année ; démission ordinaire exclue. Les droits anciens, salaires, congés, dommages d’illégalité et indemnités spéciales restent distincts. Ce seuil ne conditionne pas l’affiliation ou la prise en charge des soins.'
}

specific = {
    ('L281-1','L623-1'): 'La note source vise L623-1 au titre de la vieillesse des non-salariés, mais la cible actuelle règle maternité, paternité, adoption et deuil des indépendants : discordance historique signalée, sans prétendre étendre le contrôle de gestion à un régime absent du texte actuel. Ce régime ne relève pas du contrat privé unique et ses minima de cessation ne sont pas des préavis. La réserve QPC du 8 août 2025 sur la filiation conjointe et le régime des élus locaux restent à leur objet ; aucun agrément de gouvernance n’en est déduit.',
    ('L311-3','261'): 'Le 22° vise le deuxième alinéa du d du 1° du 7 de CGI261 : rémunération de dirigeants associatifs compatible avec gestion désintéressée sous transparence, élection, contrôle et adéquation. Ce renvoi identifie une catégorie affiliée ; ce n’est ni une exonération de cotisations nouvelle ni un renvoi de rupture. Les seuils et la majorité des deux tiers des alinéas suivants gardent leur objet fiscal. La note de reprise en 2027 exige la concordance CIBS, sans fermer l’affiliation future ni modifier les délais de notification.',
    ('L311-3','L242-1-4'): 'Le 31° rattache les salariés au titre des rémunérations versées par un tiers dans son intérêt. L242-1-4 conserve le forfait libératoire de 20 % au-delà de 15 % du SMIC mensuel et jusqu’à 1,5 SMIC mensuel, ses exclusions de groupe et de fraude et ses obligations propres ; il ne s’agit pas de l’indemnité ordinaire de licenciement. Le contrat unique ne supprime ni cet avantage ni ses limites et ne transfère pas une notification de rupture au tiers.',
    ('L311-3','L133-5-6'): 'Le 36° utilise précisément le 8° de L133-5-6, qui vise les services ponctuels de conseil ou formation rendus entre particuliers et en laisse durée et activités au décret. La durée de la prestation n’est pas un terme d’emploi autorisé. Le dispositif simplifié reste facultatif, la proposition de cible conserve son champ et les neuf catégories ; aucune condition d’ancienneté ou notification de rupture ne peut être tirée de ce renvoi social.',
    ('L311-3','L131-6'): 'Le troisième alinéa du 21° vise l’assiette des indépendants optant pour leur régime habituel lorsque la mission publique prolonge leur activité ; L131-6 exclut L613-7 et les sommes d’épargne salariale visées, et réserve les revenus de remplacement liés aux ALD. L’option et le champ agricole alternatif sont conservés. Ce renvoi ne transforme pas l’agent public ou l’expert indépendant en contrat privé et n’applique ni le seuil indemnitaire d’un an ni le préavis de quinze jours.',
    ('L311-3','L223-1'): 'L311-3 29° vise L223-1 du code du sport, relatif aux arbitres et juges : la cible fournie est L223-1 du CSS, qui définit les missions de la CNAF, donc un homonyme inapplicable à ce renvoi. Ses remboursements de congés, dont 60 % au 6° a et les régimes publics aux 7°/8°, ne sont pas la règle d’affiliation des arbitres. Ne pas remplacer le renvoi sportif par cette cible ni lui attribuer une règle de contrat unique ou d’ancienneté.',
    ('L311-3','L242-1'): 'L311-3 36° renvoie à la rémunération au sens de L242-1 ; son I lie l’assiette aux revenus d’activité et le II conserve les exclusions d’intéressement, participation, épargne, protection complémentaire et rupture. Le 7° proposé retire les effets de seuil de cinq et dix PASS mais conserve la limite de deux PASS et sa transition ; rien de cela ne fixe l’indemnité de rupture due ni son seuil d’ancienneté. Les abattements autonomes des 35°/37° de L311-3 restent distincts.',
    ('L311-5','L1235-16'): 'L1235-16 concerne l’annulation d’une validation ou homologation collective, réintégration consentie ou indemnité d’au moins six mois, distincte de L1234-9. Les quinze jours du troisième alinéa courent de la notification du jugement à l’administration pour refaire une motivation : ce ne sont pas les quinze jours du préavis individuel. Le renvoi de L311-5 ne supprime ni cette réparation ni la conservation de droits sociaux ; la dispense proposée de seconde transmission datée ne change pas l’allocation.',
    ('L311-5','L1233-67'): 'L1233-67 rompt le contrat lors de l’adhésion au CSP ; les douze mois de contestation ne sont opposables qu’après mention dans la proposition. La proposition conserve les anciens préavis et droits, verse au salarié le montant correspondant au préavis sans déduire la contribution supprimée pour les adhésions nouvelles et distingue l’ancienneté propre de L1234-9. Le bénéficiaire reste stagiaire ; une phase de travail future relève du contrat unique sans terme de formation et conserve le maintien L311-5.',
    ('L311-5','L1233-68'): 'Le renvoi effectif du maintien vise notamment le 8° de L1233-68 : allocation, incitations et règles de cumul, suspension et interruption du CSP. Les conditions d’ancienneté et délais de réponse sont fixés par le dispositif et ne sont pas remplacés par quinze jours de préavis. La proposition du 3° réserve le contrat unique pour l’emploi futur ; le 10° b ne conserve le financement patronal que pour les adhésions anciennes. La durée d’accompagnement ne termine pas l’emploi ni les droits sociaux.',
    ('L311-5','L1233-69'): 'L1233-69 proposé supprime le versement patronal de financement pour les adhésions nouvelles, tout en conservant dettes, recours anciens et allocations et droits du bénéficiaire. L311-5 ne renvoie qu’aux allocations visées dans l’ensemble L1233-65 à L1233-69 : le maintien d’assurance ne rétablit ni contribution ni préavis à trois mois. Le versement dû directement au salarié et la contribution distincte pour défaut de proposition du CSP restent à leur champ propre.',
    ('L311-5','L313-1'): 'L311-5 prolonge les droits lorsque la reprise d’activité ne satisfait pas L313-1, et aussi lorsque les indemnités maladie sont nulles ou la maternité indépendante à faible niveau. La cible fournie est la source officielle sans proposition ; le présent lot supprime seulement l’affiliation minimale additionnelle de son II. Les seuils de travail ou de rémunération, les maintiens du premier alinéa et le congé parental subsistent : le seuil d’un an d’indemnité de rupture ne s’y substitue pas.',
    ('L311-5','L623-1'): 'Le dernier alinéa vise les indemnités journalières forfaitaires de maternité des indépendantes de L623-1, et non un emploi temporaire privé. Le maintien reste possible quand leur niveau réglementaire est faible ; la cessation d’activité, les prestations d’adoption, de deuil et l’indexation de la cible conservent leur régime. Les quinze jours de deuil du III bis ne sont pas un préavis ; la réserve QPC sur les couples de femmes reste à respecter, sans nouvelle condition d’ancienneté.',
    ('L313-1','L242-1'): 'Le I de L313-1 utilise les rémunérations soumises à cotisations au sens de L242-1, pas le montant d’une indemnité de rupture indépendamment de son assujettissement. Les exclusions du II de L242-1, notamment limite de deux PASS pour les indemnités éligibles, restent hors rémunérations cotisées. La proposition de cette cible retire des effets de seuil sans recréer d’assiette ici. La suppression d’affiliation minimale ne modifie ni le fait générateur ni les seuils de rémunération ou d’heures propres aux prestations.',
    ('L313-1','L321-1'): 'L313-1 I 2° et II 1° renvoient aux indemnités maladie de L321-1, versées pour une incapacité physique constatée dans les compétences médicales autorisées. La réserve des cures thermales et ses exceptions demeure, avec L162-4-1 et les limites de téléconsultation visées par la cible. Le minimum d’affiliation est retiré sans abolir la preuve de l’incapacité, les durées de prestations ou les seuils contributifs ; les délais de prescription médicale ne deviennent pas un préavis d’emploi.',
    ('L313-6','L313-1'): 'La dérogation de L313-6 neutralise le temps d’arrêt imputable au service volontaire dans les durées de droits maladie pour d’autres affections. La source cible exige travail ou rémunérations au I et affiliation additionnelle au II ; la proposition de ce lot retire cette dernière, mais pas les durées de service. La dérogation garde donc un objet pour les futurs sinistres et ne peut être fermée au prétexte d’un an d’ancienneté de licenciement ou d’une notification de quinze jours.',
    ('L314-1','L315-2'): 'L314-1 1° vérifie notamment les exigences de L315-2 ; la cible fournie est officielle, sans proposition. La proposition du présent lot retire les seuls motifs économiques généraux d’accord mais maintient avis médical, accord tacite, information, suspension justifiée et recours. La vérification ne peut demander pour les soins futurs la preuve d’un accord supprimé, ni une notification d’emploi ; les accords médicaux et régimes autonomes ciblés restent contrôlables.',
    ('L314-1','L162-4-1'): 'L314-1 1° vérifie le contenu médical des prescriptions de L162-4-1 : motifs, durée et identification/authentification ; le plafond réglementaire ne peut être inférieur à un mois en première prescription et deux en prolongation, avec dérogation motivée par l’état du patient. La note fixe le 1er septembre 2026. Ces durées médicales ne sont ni une ancienneté de travail ni le préavis individuel de quinze jours ; la dérogation favorable n’est pas supprimée par le contrôle.',
    ('L314-1','L114-17-1'): 'Le dernier alinéa de L314-1 renvoie aux procédures de sanctions de L114-17-1 après appréciation des responsabilités. Bonne foi aux II 1°/2°, procédure propre, plafonds de 70 %, quatre plafonds mensuels et régimes aggravés de fraude ne sont pas des indemnités ordinaires de rupture. Le renvoi conserve ces garanties et ne sanctionne pas l’absence d’un accord économique supprimé pour les soins nouveaux ; aucune notification de licenciement ni ancienneté d’un an ne remplace le contradictoire social.',
    ('L314-1','L162-1-15'): 'Le dernier alinéa vise la mise sous accord préalable ciblée de L162-1-15 : observations préalables, six mois au plus, pratiques comparables et dispense en urgence, plus objectif alternatif proposé. Ce régime autonome de prévention d’abus est distinct des deux motifs économiques retirés de L315-2. Ses six mois ne sont pas un plafond d’indemnité ni un préavis ; maintenir le renvoi n’autorise ni CDD ni contrôle sans ses garanties et sans l’avis conforme requis.',
    ('L315-2','L162-16-5-2'): 'Le long alinéa du II A vise les produits en accès compassionnel L162-16-5-2 ; la cible conserve bases de prise en charge, remises progressives, part minimale non reversée et continuations de traitement du VI, avec conditions médicales et délais propres. La réduction d’accord préalable ne supprime pas ces avantages ni les remises/prix et n’introduit pas d’ancienneté de travail. L’accord général reste possible sur motif médical pour ces produits, sans autorisation fondée sur le seul coût.',
    ('L315-2','L162-16-5-1-1'): 'L162-16-5-1-1 règle indemnité maximale, remises d’accès précoce et restitution différentielle, non la rupture d’emploi. Le III B permet notamment une convention avant le 1er mai avec étalement sur deux années ou décote jusqu’à 3 % ; ces avantages restent ouverts et les délais de 180 jours ou de deux mois ont leur objet pharmaceutique propre. Le renvoi dans L315-2 ne rétablit pas un accord exclusivement économique et ne modifie ni ces créances ni leur transition.',
    ('L315-2','L321-1'): 'Le III vise la suspension d’une indemnité maladie L321-1 lorsqu’elle est médicalement injustifiée, après information et sous recours médical. Le droit initial reste fondé sur l’incapacité constatée par les professions compétentes et la réserve de cure thermale ; aucun seuil d’un an de licenciement ni quinze jours de notification ne s’y applique. La suppression des motifs économiques du II n’interdit pas ce contrôle clinique et ne retire pas les exceptions favorables de L321-1.',
    ('L315-2','L315-1'): 'Le I de L315-2 rend opposables à la caisse les avis sur les éléments médicaux du I de L315-1 ; ce renvoi ne vise pas l’automatisme statistique du II que la proposition du présent lot retire. Les examens de droit, droits de la défense, secret et opposition au transfert du VI restent intacts. Aucun délai de rupture d’emploi n’en résulte ; les décisions médicales doivent rester dans le champ de la prise en charge et des garanties existantes.',
    ('L315-3','L315-2'): 'La cible fournie montre l’accord tacite du II et les motifs économiques encore présents en droit officiel. La proposition de ce lot retire ces deux motifs ; L315-3 est donc explicitement limité aux accords restants, exprès ou tacites, pour les soins futurs même sur prescription ancienne. Aucun nouveau certificat n’est demandé pour prouver le silence ; la transition conserve les soins anciens et accords favorables. Il ne s’agit ni d’un délai de préavis ni d’une ancienneté d’emploi.',
    ('L315-3','L133-4'): 'Le III utilise L133-4 pour recouvrer l’indu auprès du responsable : prescription de trois ans sauf fraude, observations deux mois, mise en demeure un mois, opposition et restitution à l’assuré/complémentaire. Minoration HAD et remise de majoration sont conservées par la cible. La nouvelle limite du II empêche l’indu fondé sur un accord supprimé, sans abolir les recouvrements légitimes ; ces délais et la notification de l’indu sont distincts du préavis et du seuil indemnitaire de travail.'
}

for a in sources:
    out = answers[a['number']]
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        target = refs['targets'][target_key]
        number = target['number']
        if number in work_rules and target['code_id'] == 'LEGITEXT000006072050':
            assessment = work_contexts[a['number']] + ' ' + work_rules[number]
        else:
            assessment = specific[(a['number'], number)]
        checks.append(dict(target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))
    out['reference_checks'] = checks

# Passages probants complets, sans ellipse ni coupure de la condition citée.
for number in ['L281-6', 'L311-3', 'L311-4', 'L311-5', 'L311-11']:
    src = by_number[number]['source_xml']
    proposed = answers[number]['proposed_xml']
    eff = answers[number]['substantive_impact']['effects'][0]
    if number == 'L281-6':
        eff['source_quote'] = plain(src).strip().splitlines()[0].strip()
        eff['proposed_quote'] = plain(proposed).strip().splitlines()[0].strip()
    elif number == 'L311-3':
        eff['source_quote'] = plain(re.search(r'<p>32°.*?</p>', src, re.S).group())
    elif number == 'L311-4':
        eff['source_quote'] = plain(src).strip()
    elif number == 'L311-5':
        eff['source_quote'] = plain(re.findall(r'<p>.*?</p>', src, re.S)[0])
        eff['proposed_quote'] = plain(re.findall(r'<p>.*?</p>', proposed, re.S)[0])
    elif number == 'L311-11':
        eff['source_quote'] = plain(re.findall(r'<p>.*?</p>', src, re.S)[2])
        eff['proposed_quote'] = plain(re.findall(r'<p>.*?</p>', proposed, re.S)[2])

result = [answers[a['number']] for a in sources]
(ROOT / 'answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(result)} articles')
