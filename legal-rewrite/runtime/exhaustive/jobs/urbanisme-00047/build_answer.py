import json
import re
from html import unescape, escape
from html.parser import HTMLParser

S = json.load(open('source.json'))
R = json.load(open('reference-targets.json'))
OUT = {}

def text_of(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml or ''))

def paras(*texts):
    return ''.join('<p>' + escape(t, quote=False) + '</p>' for t in texts)

def effect(kind, measure_id, description, before, after, unit, population, transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition, replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)

def put(n, proposed, reason, notes, cls, assessment, limitations, burdens, effects=None, removed=None, repeal_scope=None, benefit=None):
    s = next(a for a in S if a['number'] == n)
    o = {k:s[k] for k in ('code_id','source_id','source_sha256','number')}
    o.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft',
             substantive_impact=dict(version=1, classification=cls, assessment=assessment,
                 scope_limitations=limitations, new_burdens_review=burdens, effects=effects or []),
             reference_checks=[])
    if proposed is None:
        o['classification']='retained_necessary'
    if removed:
        o.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if repeal_scope:
        o.update(change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19', repeal_scope=repeal_scope)
    if benefit:
        o['benefit_review']=benefit
    OUT[n]=o

PRO='urbanisme-recours-professionnels-facultatif'
DIV='lotissements-sans-permis-fin-declaration'
INFO='lotissements-fin-double-remise-documents'

put('L433-6', None,
    "Maintien intégral nécessaire du régime patrimonial des constructions précaires : l'absence d'indemnité à la charge de l'autorité pour les droits réels et baux désignés permet la remise en état inhérente à cette autorisation dérogatoire. Les deux catégories de bâtiments et la date de constitution des droits du second alinéa sont conservées. Ni déclaration, agrément, prélèvement ni justificatif répétitif à retirer dans cet article. Ce maintien n'est pas une simplification.",
    "Sources et notes entières examinées. Les dates de 2006 et 2007 concernent la recodification historique, non l'entrée en vigueur du projet. L433-3 à L433-5 sont lus dans reference-targets.json, avec distinction de leurs propositions et du droit officiel. L'indemnité proportionnelle de L433-4 demeure autonome ; l'articulation de son bénéficiaire avec les titulaires de droits visés par la formule « Nonobstant toutes dispositions contraires » de L433-6 doit rester contrôlée, sans supprimer cette indemnité ni prétendre indemniser tous les preneurs. L'exclusion vise l'autorité de remise en état, non les responsabilités contractuelles de leurs cocontractants ou les créances de salariés. Aucun contrat de travail ni calcul d'ancienneté n'est régi ici.",
    'retained_necessary',
    "Aucun allègement nouveau : maintien des deux exclusions patrimoniales liées au permis précaire, après examen de leur fonction dans la remise en état et de l'indemnité autonome de L433-4.",
    "Ne tranche pas le contentieux d'articulation entre titulaire du permis et titulaire de droits dérivés. Aucun effet sur préavis, salaires, indemnités de licenciement ou finances nationales n'est établi.",
    "Aucune charge nouvelle identifiée : aucun corps nouveau, registre, justificatif ou délai n'est ajouté ; le maintien ne crée pas une condition d'accès supplémentaire au permis précaire.")

p = paras(
    "Tout acte portant vente, location ou constitution de droits réels sur des bâtiments édifiés sur le fondement d'un permis délivré à titre précaire en application des dispositions du présent chapitre doit mentionner ce caractère précaire.",
    "L'omission de cette mention n'entraîne pas, à elle seule, la nullité de l'acte. Les règles relatives à l'information, au consentement et à la responsabilité demeurent applicables.",
    "La suppression de cette cause spéciale de nullité s'applique aux actes conclus à compter de l'entrée en vigueur de la loi qui la prévoit. Les actes conclus auparavant et les actions qui s'y rapportent demeurent régis par les dispositions antérieures.")
put('L433-7', p,
    "Réforme de fond : suppression de la nullité automatique spécialement attachée à l'omission de la mention de précarité. L'information écrite de l'acquéreur, du preneur ou du titulaire de droit réel reste obligatoire, car l'enlèvement sans indemnité peut affecter la valeur et la durée de son droit. Les recours de droit commun pour défaut d'information, vice du consentement ou responsabilité sont réservés ; aucune déclaration administrative ne remplace la sanction retirée.",
    "Transition limitée aux actes nouveaux, sans validation rétroactive des actes anciens. L433-3 à L433-6 restent applicables : terme éventuel, enlèvement, remise en état, évaluation du terrain et exclusions d'indemnisation ne deviennent pas des règles de rupture d'emploi. L'obligation de mention concerne aussi la location, quelle que soit sa durée, non un nouveau CDD. Les règles civiles et la publicité foncière sont hors du lot ; leurs recours ne sont pas abrogés par cette suppression ciblée.",
    'material_reduction',
    "Le seul défaut de mention ne peut plus anéantir un acte nouveau ; la mention et les sanctions civiles reposant sur leurs conditions propres demeurent. Il s'agit d'une suppression de sanction spéciale, sans suppression d'une obligation d'information.",
    "Ne réduit ni une taxe ni le coût ordinaire de licenciement. Les actes antérieurs conservent la sanction spéciale ; la responsabilité civile et les vices du consentement peuvent encore être invoqués.",
    "Aucune charge nouvelle identifiée : la mention préexistante subsiste sans pièce, déclaration, visa, délai ou preuve supplémentaire ; les recours de droit commun sont seulement réservés.",
    [effect('compliance_cost_reduced','permis-precaires-fin-nullite-speciale',
        "Suppression du risque de nullité fondé sur la seule omission formelle de la précarité.",
        "Actes de vente, location ou constitution de droits réels : mention du permis précaire imposée à peine de nullité.",
        "Même information obligatoire ; omission seule sans nullité spéciale pour les actes nouveaux.",
        'legal_duty',"Parties aux actes portant sur les bâtiments édifiés sous permis précaire.",
        "Actes conclus dès l'entrée en vigueur ; actes et actions relatifs aux actes antérieurs sous leur régime antérieur.",
        "Aucune formalité de remplacement ; information et recours civils conservés.",
        "A peine de nullité, tout acte portant vente, location ou constitution de droits réels",
        "L'omission de cette mention n'entraîne pas, à elle seule, la nullité de l'acte.")],
    removed=["La nullité spéciale de l'acte fondée sur la seule omission de la mention du permis de construire précaire est supprimée pour les actes nouveaux."])

put('L434-1', None,
    "Maintien intégral nécessaire de l'habilitation à préciser par décret en Conseil d'État les conditions d'application du titre relatif aux constructions. Cet article n'impose en lui-même ni demande, redevance, délai minimal ni recours à un professionnel ; son abrogation ne supprimerait pas les procédures de fond et fragiliserait leur exécution.",
    "Le décret doit respecter les dispenses et allègements législatifs, notamment le caractère facultatif du recours professionnel proposé à L431-1 et coordonné à L441-2. L'habilitation ne permet pas de rétablir par règlement une obligation expressément supprimée. Aucun texte source réservé ni note transitoire dans cet article.",
    'retained_necessary',
    "L'habilitation réglementaire demeure ; aucune obligation autonome des administrés n'est supprimée par ce maintien intégral.",
    "N'établit pas l'utilité de chaque règle réglementaire du titre : celles-ci exigent un examen propre. Aucune simplification ou économie nationale n'est comptée.",
    "Aucune charge nouvelle identifiée : le texte source est conservé sans extension du pouvoir réglementaire ni nouveau dossier, donnée ou délai.")

s = next(a for a in S if a['number']=='L441-2')
first = "Lorsque les travaux d'aménagement impliquent, de façon accessoire, la réalisation par l'aménageur de constructions et d'installations diverses sur le terrain aménagé, la demande de permis d'aménager peut porter à la fois sur l'aménagement du terrain et sur le projet de construction."
p=paras(first,
    "Dans ce cas, le recours à un architecte pour établir le projet de construction est facultatif dans les conditions de l'article L. 431-1. Les dispenses prévues à l'article L. 431-3 demeurent applicables ; leur champ ne limite pas cette faculté. La demande ne peut être écartée de l'instruction au seul motif de l'absence de recours à un architecte.",
    "Le deuxième alinéa s'applique aux demandes nouvelles et aux demandes en cours à la date d'entrée en vigueur de la loi ayant rendu ce recours facultatif, sans nouveau dépôt ni reprise des délais. Les contrats valablement conclus et les rémunérations contractuellement dues demeurent régis par leurs stipulations. Les décisions de refus devenues définitives ne sont pas rouvertes.")
put('L441-2',p,
    "Réforme de fond et coordination du recours facultatif à l'architecte déjà proposé à L431-1 : retrait de la condition bloquant l'instruction du permis d'aménager commun lorsque la construction accessoire n'est pas dispensée par L431-3. La possibilité favorable de demander un seul permis pour terrain et construction est maintenue intégralement, de même que les dispenses, sans attestation de remplacement. Le premier alinéa reste à droit constant.",
    "L431-1 et L431-3 officiels, notes et propositions du corpus public ont été lus : le recours facultatif de la proposition de L431-1 n'est pas présenté comme droit positif. L441-3 continue de donner effet au permis commun. Les règles de contenu du projet, de sécurité, d'accessibilité et de patrimoine restent à leur champ propre. Coordination extérieure identifiée : article 3 de la loi n°77-2 du 3 janvier 1977 et décret n°78-171 du 26 janvier 1978 ; leurs textes intégraux ne sont pas fournis ici et leur modification n'est pas déclarée achevée. Le renvoi L431-1 ajouté figure dans le corpus lu mais pas parmi les cibles de reference-targets.json ; il n'est donc pas ajouté aux reference_checks imposés.",
    'material_reduction',
    "La condition légale de recours professionnel qui bloquait l'instruction du permis commun est effectivement supprimée. Cette exécution de la facultativité appartient à la même mesure que le retrait de l'intervention professionnelle imposée en urbanisme ; elle ne vaut pas une nouvelle fusion d'autorisations.",
    "Le permis commun était déjà possible. Les exigences techniques et le projet complet subsistent ; le gain financier des honoraires évités n'est pas chiffré et les conventions professionnelles anciennes ne sont pas annulées.",
    "Aucune charge nouvelle identifiée : ni attestation de compétence, ni déclaration de substitution, ni délai ne remplace le recours supprimé ; le projet utile et les dispenses préexistantes restent.",
    [effect('obligation_removed',PRO,
        "Retrait de l'intervention obligatoire de l'architecte pour le volet construction du permis d'aménager commun.",
        "Instruction conditionnée au recours à un architecte pour les constructions hors dispenses L431-3.",
        "Instruction ouverte sans architecte, projet et conditions de fond conservés ; choix professionnel volontaire.",
        'legal_duty',"Aménageurs incluant des constructions et installations accessoires dans leur permis d'aménager.",
        "Demandes nouvelles et en cours dès l'entrée de la réforme ; conventions et rémunérations dues préservées.",
        "Pas de document de remplacement ; contenu de projet et règles de fond inchangés.",
        "la demande de permis d'aménager ne peut être instruite que si le demandeur a fait appel à un architecte",
        "le recours à un architecte pour établir le projet de construction est facultatif")],
    removed=["La condition d'instruction imposant un architecte pour les constructions accessoires non couvertes par les dispenses de L431-3 est retirée."],
    benefit="Le permis d'aménager peut toujours réunir l'aménagement et les constructions accessoires : ce bénéfice reste ouvert aux opérations futures. Les dispenses d'architecte de L431-3 ne sont pas supprimées et leur champ ne devient pas une limite au recours facultatif général proposé ; aucune aide ni droit acquis n'est fermé.")

put('L441-3',None,
    "Maintien intégral nécessaire de l'effet du permis d'aménager commun : dans les cas de L441-1 et L441-2, il autorise les constructions ou démolitions et évite déjà un titre distinct. Le supprimer détruirait une simplification existante ; le reformuler n'ajouterait aucune fusion.",
    "L441-1 officiel et L441-2 du lot lus intégralement : seules les démolitions intégrées et les constructions accessoires couvertes par ces articles sont visées. La suppression de l'architecte obligatoire à L441-2 ne retire ni l'effet du permis commun ni ses règles de fond. Aucun renvoi orphelin identifié.",
    'retained_necessary',
    "Le même titre conserve son double effet déjà acquis dans la source ; aucune seconde autorisation n'est nouvellement supprimée.",
    "Ne généralise pas le permis d'aménager à toute construction ou démolition. Les autres accords sectoriels et conditions de fond demeurent.",
    "Aucune charge nouvelle identifiée : maintien pur d'un mécanisme favorable, sans nouvel agrément, dépôt, donnée ni délai.")

p=paras(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui supprime le recours professionnel obligatoire pour l'établissement du projet architectural, paysager et environnemental d'un lotissement. L'absence de recours à des compétences professionnelles déterminées ou à un architecte ou paysagiste concepteur ne peut plus, sur le fondement du présent article, faire obstacle à l'instruction d'une demande de permis d'aménager, quelle que soit la superficie du terrain.",
    "Cette suppression s'applique aux demandes nouvelles et aux demandes en cours, sans nouveau dépôt ni reprise des délais. Elle n'exige aucune attestation ou déclaration de remplacement. Les obligations relatives au contenu du projet et au respect des règles de sécurité, de salubrité, d'accessibilité, d'urbanisme, de protection du patrimoine et de l'environnement restent applicables sur leurs fondements propres.",
    "Les contrats valablement conclus, les rémunérations contractuellement dues et les responsabilités professionnelles demeurent régis par leurs règles propres. Les décisions de refus devenues définitives ne sont pas rouvertes.")
put('L441-4',p,
    "Abrogation de fond pour l'avenir de l'obligation de faire appel aux compétences professionnelles imposées pour le projet de lotissement et, au-dessus du seuil réglementaire, à un architecte ou paysagiste concepteur. Le contenu architectural, paysager et environnemental du dossier reste contrôlé sur ses fondements autonomes ; le statut professionnel imposé ne démontre pas à lui seul une fonction de sécurité qui justifierait de bloquer l'instruction. Aucun agrément ou justificatif équivalent n'est institué.",
    "R.441-4-2 officiel et sa note lus : seuil de deux mille cinq cents mètres carrés, demandes depuis le 1er mai 2017. Son seuil doit être retiré pour les demandes nouvelles et en cours ; L442-1-3 est coordonné dans ce lot sans fermer le permis multisite. Le contenu utile des deux plans de R*441-4 demeure, sans rétablir des supports obligatoirement séparés lorsqu'un support commun est légalement admis. Hors corpus : article 9 de la loi n°77-2 de 1977 et article 174 de la loi n°2016-1087 de 2016 sont des références aux qualités professionnelles, non des autorisations de lotissement abrogées indistinctement ; leurs textes intégraux ne sont pas fournis. Les mentions et modèles réglementaires imposant ces professionnels doivent être coordonnés. L'absence de titre professionnel ne dispense pas des responsabilités et prescriptions techniques autonomes ; aucun coût national n'est chiffré.",
    'material_reduction',
    "L'intégralité de la condition d'intervention professionnelle qui verrouillait l'instruction du lotissement est retirée, y compris le seuil imposant architecte ou paysagiste. Le dossier de fond et ses contrôles sont conservés sur d'autres bases.",
    "Ne supprime pas le permis d'aménager, les études environnementales, les responsabilités ni les obligations contractuelles déjà souscrites. Le coût net et les effets sur la qualité des projets restent non chiffrés.",
    "Aucune charge nouvelle identifiée : choix libre de recourir à un professionnel, sans déclaration, attestation, registre ou visa de remplacement ; exigences de projet préexistantes conservées.",
    [effect('obligation_removed',PRO,
        "Suppression de l'intervention professionnelle imposée pour établir le projet du lotissement.",
        "Compétences d'architecture, urbanisme et paysage imposées pour toute demande ; architecte ou paysagiste concepteur au-delà de 2 500 m² de terrain à aménager.",
        "Aucune obligation professionnelle sur ce fondement, quelle que soit la surface ; le projet complet et les règles de fond restent exigibles.",
        'legal_duty',"Demandeurs de permis d'aménager un lotissement, y compris opérations dépassant le seuil de terrain.",
        "Demandes nouvelles et pendantes dès entrée en vigueur ; contrats professionnels, rémunérations dues et refus définitifs préservés.",
        "Aucune formalité de remplacement ; pas de retrait des plans ni des études autonomes.",
        "La demande de permis d'aménager concernant un lotissement ne peut être instruite que si",
        "L'absence de recours à des compétences professionnelles déterminées ou à un architecte ou paysagiste concepteur ne peut plus, sur le fondement du présent article, faire obstacle à l'instruction d'une demande de permis d'aménager, quelle que soit la superficie du terrain.")],
    repeal_scope="Suppression de la condition légale de recours aux compétences d'architecture, d'urbanisme et de paysage et de l'intervention d'un architecte ou paysagiste concepteur au-dessus du seuil pour les demandes nouvelles et en cours, sans remise en cause des conventions acquises.")

put('L441-5',None,
    "Maintien intégral de la garantie de trois ans contre les règles d'urbanisme intervenues après le permis initial : elle facilite les permis modificatifs tant que les travaux ne sont pas achevés et que le permis demeure valide. La seule exception conserve les mesures nécessaires à la sécurité ou à la salubrité publiques. Retirer cette protection serait contraire à la conservation des dérogations favorables ; aucune formalité répétée n'est exigée ici.",
    "Trois ans à compter de la délivrance initiale, non de chaque modification ; absence d'achèvement et validité du permis restent cumulatives. La date de validité de la source au 28 novembre 2025 n'est pas celle de la réforme future. Aucun élargissement silencieux aux travaux achevés, permis périmés ou normes non urbanistiques.",
    'retained_necessary',
    "La protection existante des permis modificatifs est conservée dans son intégralité, avec son exception essentielle de sécurité et de salubrité ; aucun gain nouveau n'est revendiqué.",
    "La garantie ne s'étend pas au-delà de trois ans ni aux permis périmés ou aux travaux achevés. Les normes distinctes et protections supérieures restent à examiner dans leur champ.",
    "Aucune charge nouvelle identifiée : aucune attestation, déclaration ou condition supplémentaire n'est ajoutée aux deux alinéas officiels maintenus.",
    benefit="L'avantage consiste à interdire pendant trois ans un refus ou des prescriptions spéciales fondés sur des dispositions d'urbanisme postérieures au permis initial. Il reste ouvert aux futures demandes éligibles et aux permis existants selon sa durée propre. Seules les règles nouvelles préservant sécurité ou salubrité publiques peuvent déroger à cette garantie, sans restriction ajoutée.")

put('L442-1-1',None,
    "Maintien intégral nécessaire de la base législative des exclusions de lotissement : objet particulier ou contrôle par une autre procédure. Après examen du décret R*442-1, ses neuf catégories évitent des formalités inutiles ; abroger l'habilitation pourrait fragiliser ces dispenses. L'article n'institue pas une déclaration supplémentaire.",
    "R*442-1 et ses neuf lettres a à i lus en entier : groupes de bâtiments, remembrements, ZAC, permis valant division, terrains bâtis, rattachements contigus, expropriations et cessions, terrains réservés, participations foncières historiques ou conventionnelles. Aucun de ces bénéficiaires n'est réintégré dans le régime du lotissement par la réforme de L442-3. Notes 2011/2012 conservées à leur objet historique ; pas de nouvelle date législative déduite.",
    'retained_necessary',
    "Conservation d'une habilitation favorable qui permet déjà d'écarter neuf catégories du régime du lotissement. Ni nouvelle exclusion ni seconde suppression de déclaration n'est comptée.",
    "Ne prouve pas que les procédures distinctes contrôlant ces divisions soient toutes nécessaires ou supprimées. Les conditions des neuf exclusions restent celles du règlement.",
    "Aucune charge nouvelle identifiée : habilitation et exclusions existantes maintenues sans déclaration, justificatif ou contrôle de remplacement.")

put('L442-1-2',None,
    "Maintien intégral nécessaire du périmètre opérationnel : lots à bâtir, voies, équipements et espaces communs seulement s'ils sont prévus ; inclusion des parties déjà bâties laissée au choix du lotisseur. La définition ne force ni création d'équipement ni incorporation de tous les terrains et ne constitue pas une formalité à retirer.",
    "La faculté d'inclure le bâti reste utilisable pour les opérations futures ; elle n'est pas transformée en obligation. L442-1 et ses exclusions ainsi que la dérogation multisite L442-1-3 ont été confrontés au texte. Les notes du 1er mars 2012 n'établissent aucune nouvelle entrée en vigueur du projet. La suppression d'une déclaration de division ne supprime pas la qualification de lotissement.",
    'retained_necessary',
    "Le périmètre et le choix favorable d'inclure les parties bâties demeurent ; aucune obligation ou surface réglementaire n'est ajoutée ou retirée par ce maintien.",
    "Ne dispense pas des droits de propriété, des équipements effectivement nécessaires ni des autorisations de travaux distinctes. Aucun gain de surface ou coût global n'est calculé.",
    "Aucune charge nouvelle identifiée : ni plan distinct ni déclaration supplémentaire n'est créé ; la faculté d'inclusion et la condition des équipements prévus restent inchangées.")

p=paras(
    "Par dérogation à l'article L. 442-1, un permis d'aménager concernant un lotissement peut porter sur des unités foncières non contiguës si le projet répond à l'ensemble des critères suivants :",
    "1° La demande est déposée par un demandeur unique ;",
    "2° Le projet constitue un ensemble unique et cohérent ;",
    "3° Le projet garantit l'unité architecturale et paysagère des sites concernés.",
    "Le recours à un architecte ou à un paysagiste concepteur est facultatif, quelle que soit la superficie totale des unités foncières non contiguës concernées par le permis d'aménager.",
    "L'assiette du projet peut également comprendre une ou plusieurs unités foncières ou parties de site destinées à être renaturées ou réaffectées à des fonctions écologiques ou paysagères, même en l'absence de travaux d'aménagement, si ces unités participent à la cohérence globale du projet.",
    "Le cinquième alinéa s'applique aux demandes nouvelles et aux demandes en cours à la date d'entrée en vigueur de la loi supprimant l'obligation prévue à l'article L. 441-4, sans nouveau dépôt ni reprise des délais. Les contrats valablement conclus et les rémunérations contractuellement dues restent applicables.")
put('L442-1-3',p,
    "Coordination nécessaire de l'abrogation de L441-4 : le cinquième alinéa ne calcule plus le seuil d'une obligation supprimée ; il explicite le libre recours professionnel pour les sites non contigus. Maintien intégral des trois critères du permis commun et de l'inclusion favorable des sites à renaturer ou à réaffecter, même sans travaux. Ce retrait de renvoi n'est pas une deuxième obligation professionnelle supprimée.",
    "Le rang du cinquième alinéa est conservé pour la coordination du seuil. L442-1 officiel et R.441-4-2 avec sa note ont été lus. La cohérence globale et l'unité architecturale et paysagère restent des exigences de résultat du projet, non une obligation de recruter un professionnel. Alignement temporel avec L441-4, sans rupture des contrats de prestation. Les attributs align des paragraphes de la source sont retirés car non autorisés dans proposed_xml ; aucun contenu normatif n'est omis.",
    'coordination_only',
    "Le seuil cumulé renvoyant à L441-4 disparaît comme conséquence de la seule mesure de facultativité professionnelle. Les permis multisites et les inclusions écologiques restent accessibles dans les mêmes conditions.",
    "Aucun nouveau nombre de lotissements ou coût d'honoraires évité n'est imputé à cette coordination. Les trois critères de la dérogation restent opposables aux opérations futures.",
    "Aucune charge nouvelle identifiée : ni attestation de cohérence supplémentaire ni déclaration ne remplace le seuil ; les critères et le dossier commun préexistants sont conservés.",
    [effect('coordination',PRO,
        "Neutralisation du calcul cumulé du seuil professionnel désormais supprimé, sans fermer la dérogation multisite.",
        "Surfaces de toutes les unités non contiguës cumulées pour apprécier le seuil de L441-4.",
        "Pas de seuil de recours professionnel obligatoire ; mêmes trois critères et possibilité d'intégrer des espaces à renaturer.",
        'legal_duty',"Demandeurs de permis d'aménager portant sur des unités foncières non contiguës.",
        "Demandes nouvelles et en cours à la même entrée en vigueur que L441-4 ; contrats de prestation conservés.",
        "Aucun dépôt ni justificatif substitutif ; coordination de la même suppression professionnelle.",
        "Le seuil mentionné à l'article L. 441-4 s'apprécie à l'échelle de la totalité des surfaces",
        "Le recours à un architecte ou à un paysagiste concepteur est facultatif, quelle que soit la superficie totale des unités foncières non contiguës concernées par le permis d'aménager.")],
    removed=["Le renvoi au seuil de recours professionnel obligatoire de L441-4 et son appréciation par cumul des surfaces des sites non contigus sont retirés."],
    benefit="La dérogation permettant un permis unique sur des unités non contiguës reste ouverte aux nouveaux projets : demandeur unique, ensemble cohérent et unité architecturale et paysagère sont conservés. L'inclusion de terrains à renaturer ou à réaffecter sans travaux reste expressément possible. Le calcul du seuil n'est pas un avantage : il déclenchait un recours professionnel obligatoire désormais supprimé, sans suppression de ces possibilités favorables.")

p=paras(
    "Les lotissements qui ne sont pas soumis à la délivrance d'un permis d'aménager sont dispensés de déclaration préalable au titre de leur seule qualité de lotissement. Cette dispense ne s'applique pas aux divisions soumises à déclaration préalable en application de l'article L. 115-3.",
    "La dispense ne retire ni les exigences de conformité prévues à l'article L. 421-8, ni les autorisations ou déclarations exigées pour des travaux, constructions, installations ou protections ayant un objet distinct de la seule division en lotissement. Aucune déclaration, attestation ou transmission de remplacement n'est exigée au titre de la dispense.",
    "La dispense s'applique aux divisions réalisées à compter de l'entrée en vigueur de la loi qui la prévoit. Les déclarations déposées avant cette date continuent d'être instruites selon les règles antérieures, sauf renonciation du déclarant, sans nouveau dossier ni reprise des délais. Leur dépôt ne peut, à lui seul, subordonner à une décision la réalisation d'une division désormais dispensée. La garantie de l'article L. 442-14 reste applicable dans les conditions qu'il prévoit.",
    "Les divisions réalisées auparavant, les décisions déjà prises et les droits et recours qui s'y rapportent restent régis par les dispositions antérieures, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives. La dispense n'emporte aucune régularisation rétroactive d'une division non conforme aux règles de fond.")
put('L442-3',p,
    "Réforme de fond : retrait de la déclaration préalable imposée au seul titre du lotissement lorsqu'aucun permis d'aménager n'est requis. Pour les divisions sans aménagement commun soumis à permis, le contrôle de la constructibilité et des travaux conserve ses bases autonomes ; un dossier général de division supplémentaire n'est pas nécessaire à cette fonction. La déclaration ciblée de protection des sites, milieux et paysages de L115-3 est expressément maintenue, ainsi que les exigences de fond et les autorisations d'objets distincts. Aucun dépôt équivalent ne remplace la déclaration supprimée.",
    "L421-2/4/6/8, L115-3, L442-1/2, R*421-19/20/23, R*442-1/2 ainsi que L480-4-1 et L480-15 officiels lus. R*421-23 a doit être retiré dans le champ dispensé, sans toucher son b fondé sur L115-3 ni ses autres lettres ; R*442-2 doit conserver son utilité pour les déclarations résiduelles, sans réintroduire un dépôt général. L480-4-1 doit distinguer les divisions dispensées des manquements résiduels, sans amende pour une déclaration supprimée. R*421-19 comporte une note d'application aux demandes à compter du 28 septembre 2026 malgré son début de version au 29 juillet : distinction conservée pour les anciens dossiers. L442-4/5/6/7/11/14 sont coordonnés dans ce lot. Les autres formulaires, arrêtés et renvois réglementaires restent à coordonner ; ils ne peuvent, par leur seule mention de la division, rétablir la déclaration générale. Nouveaux renvois L115-3, L421-8 et L442-14 : textes lus localement, non cibles de reference-targets.json. Aucun achèvement de leurs modifications extérieures n'est affirmé.",
    'material_reduction',
    "Une déclaration obligatoire de division, avec son dépôt et son attente de décision ou non-opposition, est réellement retirée pour les lotissements sans permis hors L115-3. Les règles de constructibilité, les déclarations de protection ciblée et les contrôles de travaux demeurent ; aucune autorisation générale nouvelle n'est créée.",
    "Aucun gain n'est compté pour les divisions déjà exclues du lotissement par R*442-1 ni pour le permis tenant déjà lieu de déclaration à R*442-2. Les opérations soumises à permis et les zones de L115-3 restent hors dispense. Coûts et effets nationaux non chiffrés.",
    "Aucune charge nouvelle identifiée : pas de registre, attestation ou information de remplacement. Les obligations sectorielles réservées sont préexistantes et les dossiers anciens ne sont poursuivis que selon leur régime déjà ouvert, avec faculté d'y renoncer.",
    [effect('obligation_removed',DIV,
        "Suppression de la déclaration préalable générale des lotissements non soumis à permis, hors protection ciblée de L115-3.",
        "Tout lotissement non soumis à permis d'aménager doit faire l'objet d'une déclaration préalable ; les exclusions R*442-1 et la substitution R*442-2 existent déjà.",
        "Aucune déclaration au seul titre du lotissement sans permis ; déclaration L115-3 et procédures d'autres objets conservées.",
        'legal_duty',"Auteurs de divisions constitutives de lotissement sans permis d'aménager et non soumises à la déclaration de L115-3.",
        "Divisions réalisées dès entrée en vigueur ; anciennes déclarations peuvent continuer sans redépôt ; anciens actes et recours réservés, avec loi répressive plus douce.",
        "Aucune formalité substitutive ; maintien des règles de fond, des autorisations distinctes et de la garantie de cinq ans coordonnée à L442-14.",
        "Les lotissements qui ne sont pas soumis à la délivrance d'un permis d'aménager doivent faire l'objet d'une déclaration préalable.",
        "Les lotissements qui ne sont pas soumis à la délivrance d'un permis d'aménager sont dispensés de déclaration préalable au titre de leur seule qualité de lotissement.")],
    removed=["La déclaration préalable générale, son dépôt et l'attente de la décision de non-opposition sont supprimés pour les lotissements sans permis hors déclaration spéciale de L115-3."])

p=paras(
    "Pour les lotissements soumis à permis d'aménager, aucune promesse de vente ou de location d'un terrain situé dans le lotissement ne peut être consentie et aucun acompte ne peut être accepté avant la délivrance de ce permis.",
    "L'absence de permis d'aménager ne fait pas obstacle à une promesse lorsque le lotissement en est dispensé. Les règles de fond, les déclarations demeurant légalement requises et la protection des parties au contrat restent applicables.",
    "Ces dispositions s'appliquent aux promesses consenties et aux acomptes acceptés à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale des lotissements sans permis. Les actes, paiements, droits et recours antérieurs demeurent régis par les dispositions qui leur étaient applicables.")
put('L442-4',p,
    "Coordination nécessaire : cantonner explicitement l'interdiction de promettre ou d'encaisser avant permis aux opérations effectivement soumises à permis. La dispense de déclaration de L442-3 ne doit pas être neutralisée par l'attente d'un permis que ces opérations n'ont jamais à obtenir. L'interdiction des engagements et acomptes avant permis demeure intégrale pour les lotissements soumis à ce titre : elle protège l'acquéreur contre une commercialisation engageante avant autorisation.",
    "Incohérence de portée littérale préexistante signalée : la source dit tout « terrain situé dans un lotissement » sans préciser que le permis doit être requis, alors que L442-2/3 distinguent les régimes. La proposition borne expressément ce champ, sans prétendre démontrer qu'une interdiction de toute promesse était effectivement appliquée aux divisions déclarées. L442-8 et R*442-12 lus : dix jours de rétractation, vingt et un jours de restitution après rétractation, plafond réglementaire de 5 % de l'indemnité et consignation restent à leur champ ; aucun de ces délais ou avantages n'est supprimé. L480-4-1/15 restent à coordonner pour le champ dispensé ; pas de suppression de l'information ni de validation des actes anciens.",
    'coordination_only',
    "Le champ de l'interdiction avant permis est rendu cohérent avec la dispense de L442-3 et la distinction préexistante permis/déclaration. Aucune nouvelle suppression d'acompte ou délai n'est comptée en sus de cette coordination.",
    "L'application passée de la formulation littérale aux lotissements sans permis n'est pas établie ; aucun gain contractuel autonome n'est chiffré. L'interdiction avant permis requis et les protections financières demeurent.",
    "Aucune charge nouvelle identifiée : pas de condition suspensive imposée, de notification ou garantie substitutive ; seules les protections contractuelles et obligations sectorielles déjà applicables sont réservées.",
    [effect('coordination',DIV,
        "Précision du champ de l'interdiction de promesse et acompte avant permis pour ne pas exiger un permis d'une opération dispensée.",
        "Formulation générale visant un terrain situé dans un lotissement avant délivrance du permis, malgré les deux régimes de lotissement.",
        "Interdiction avant permis pour les seuls lotissements soumis à permis ; absence de permis sans effet bloquant pour les autres.",
        'legal_duty',"Lotisseurs et cocontractants des opérations soumises ou dispensées de permis d'aménager.",
        "Promesses et acomptes futurs dès réforme ; actes et recours antérieurs protégés.",
        "Pas de procédure de remplacement ; interdiction avant permis requis et protections financières subsistantes.",
        "Aucune promesse de vente ou de location d'un terrain situé dans un lotissement ne peut être consentie",
        "L'absence de permis d'aménager ne fait pas obstacle à une promesse lorsque le lotissement en est dispensé.")],
    removed=["La formulation faisant attendre un permis d'aménager aux opérations qui en sont légalement dispensées est écartée expressément pour les promesses futures."])

p=paras(
    "Toute publicité, sous quelque forme que ce soit, relative à la vente ou à la location de terrains situés dans un lotissement doit mentionner de manière explicite si le lotissement est dispensé de permis d'aménager et de déclaration préalable ou, dans le cas contraire, si le permis a été ou non délivré ou si la déclaration préalable a ou non fait l'objet d'une opposition.",
    "Cette règle s'applique aux publicités diffusées à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale des lotissements sans permis. Aucune publicité antérieure n'est à refaire au seul titre de cette coordination ; la responsabilité encourue pour son contenu demeure régie par les règles qui lui étaient applicables.")
put('L442-5',p,
    "Coordination de l'information publicitaire avec les lotissements désormais dispensés de déclaration : la mention du statut réel peut indiquer la dispense. L'information sur la délivrance ou non du permis et sur les oppositions subsiste pour les opérations qui relèvent encore de ces procédures. Une publicité doit permettre de connaître le statut effectif du terrain ; supprimer cette transparence ne serait pas un allègement de dossier justifié.",
    "La déclaration spéciale des zones de L115-3 demeure à son champ ; les déclarations antérieures maintenues à L442-3 peuvent toujours produire une décision dont le statut doit être exposé. La publicité ne devient ni une déclaration administrative ni une autorisation de construire. Aucune date de décision ou mention de consultation en mairie n'est ajoutée ici : ces deux mentions de L442-6 sont retirées dans le même lot.",
    'coordination_only',
    "La mention publicitaire préexistante est adaptée au statut dispensé ; la suppression de déclaration est portée par L442-3 et ne constitue pas un deuxième allègement à chaque renvoi.",
    "L'information sur le statut reste obligatoire pour toutes les formes de publicité. Aucun effet sur les taxes, les droits civils ou une autorisation de construire n'est établi.",
    "Aucune charge nouvelle autonome identifiée : l'unique indication du statut réel remplace celle de l'ancienne procédure pour les divisions dispensées, sans nouvelle donnée à transmettre à un service ni obligation de refaire les publicités anciennes.",
    [effect('coordination',DIV,
        "Adaptation de la mention du statut administratif aux divisions bénéficiant de la dispense.",
        "Publicité indiquant si permis délivré ou déclaration frappée d'opposition.",
        "Même information de statut ; mention de dispense lorsque ni permis ni déclaration n'est requis.",
        'legal_duty',"Auteurs des publicités de vente ou location de lots et leurs destinataires.",
        "Publicités futures dès entrée en vigueur ; publicités antérieures sans reprise obligatoire et responsabilités anciennes conservées.",
        "Aucun dépôt administratif ou justificatif supplémentaire ; une alternative dans la mention existante.",
        "doit mentionner de manière explicite si le permis a été ou non délivré",
        "doit mentionner de manière explicite si le lotissement est dispensé de permis d'aménager et de déclaration préalable")])

p=paras(
    "Toute publicité postérieure à l'intervention du permis d'aménager ou de la décision de non-opposition à la déclaration préalable est dispensée de la mention de la date de la décision et de celle de la possibilité de consulter le dossier en mairie.",
    "Elle ne doit comporter aucune indication qui ne serait pas conforme aux prescriptions dont la décision a, le cas échéant, été assortie ou qui serait susceptible d'induire l'acquéreur en erreur sur les charges et conditions auxquelles le lotisseur entend subordonner la vente ou la location des lots.",
    "Pour un lotissement dispensé de permis d'aménager et de déclaration préalable, l'interdiction des indications susceptibles d'induire l'acquéreur en erreur sur les charges et conditions de la vente ou de la location s'applique à la publicité postérieure à la réalisation de la division.",
    "Ces dispositions s'appliquent aux publicités diffusées à compter de l'entrée en vigueur de la loi qui supprime ces mentions. Les publicités antérieures et les droits et recours qui s'y rapportent demeurent régis par les dispositions antérieures, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.")
put('L442-6',p,
    "Réforme de fond : retrait des deux mentions imposées dans chaque publicité après autorisation, date de la décision et consultation en mairie. Le statut de l'autorisation reste indiqué par L442-5 et les documents utiles sont communiqués avant engagement par L442-7 ; répéter les deux mentions dans toute publicité n'est pas indispensable à ces fonctions. L'interdiction des informations contraires aux prescriptions et de la tromperie sur charges et conditions est intégralement maintenue ; elle est coordonnée aux divisions dispensées sans créer une procédure publicitaire.",
    "L442-5 et L442-7 du lot lus et coordonnés. L'accès effectif au dossier administratif conserve son fondement propre ; seule l'annonce systématique de cet accès est retirée. Pour les divisions dispensées, l'interdiction de tromperie est rattachée à la division réalisée, à défaut de décision ; elle remplace le même contrôle matériel autrefois attaché à la non-opposition, sans publicité préalable nouvelle. Les autres législations interdisant une publicité trompeuse restent distinctes. Aucun coût public ou privé total n'est chiffré ; aucune dette d'urbanisme n'est supprimée.",
    'material_reduction',
    "Deux mentions obligatoires par publicité sont réellement supprimées ; le statut administratif et les informations contractuelles utiles demeurent. La coordination de l'interdiction de tromperie suit la suppression de déclaration, sans la remplacer par un dépôt.",
    "Ne supprime pas la mention de statut de L442-5, les prescriptions applicables, l'information avant contrat ou les recours pour tromperie. Les publicités anciennes restent sous leur régime propre, avec réserve de sanction plus douce.",
    "Aucune charge nouvelle identifiée : aucun support ou envoi de remplacement ; la loyauté préexistante de la publicité est conservée pour les nouvelles divisions dispensées, sans étendre son déclenchement à la phase précédant la division dans cet article.",
    [effect('obligation_removed','lotissements-publicite-fin-mentions-repetitives',
        "Suppression de la date de décision et de la mention de consultation en mairie dans toute publicité postérieure à autorisation.",
        "Chaque publicité postérieure au permis ou à la non-opposition doit indiquer date et consultation du dossier en mairie.",
        "Ces deux mentions ne sont plus requises ; statut de l'opération et interdiction de tromperie subsistent.",
        'legal_duty',"Lotisseurs et annonceurs de terrains à vendre ou louer dans un lotissement.",
        "Publicités diffusées dès entrée de la suppression, y compris pour opérations anciennes ; ancien contenu sous ses règles, sanctions plus douces réservées.",
        "Aucune mention ou transmission de remplacement ; communication contractuelle préexistante conservée.",
        "doit faire connaître la date de la décision et mentionner que le dossier peut être consulté à la mairie.",
        "Toute publicité postérieure à l'intervention du permis d'aménager ou de la décision de non-opposition à la déclaration préalable est dispensée de la mention de la date de la décision et de celle de la possibilité de consulter le dossier en mairie.")],
    removed=["L'obligation de faire connaître la date du permis ou de la décision de non-opposition dans toute publicité postérieure est supprimée.","L'obligation de mentionner dans chaque publicité la possibilité de consulter le dossier en mairie est supprimée, sans fermer cet accès."])

p=paras(
    "Le permis d'aménager, lorsqu'il est requis, et, s'il y a lieu, le cahier des charges fixant les conditions de vente ou de location des lots sont communiqués à l'acquéreur avant la signature de la promesse ou de l'acte de vente ainsi qu'au preneur avant la signature des engagements de location.",
    "Les documents ainsi communiqués ne sont pas remis de nouveau lors de la signature si leur contenu n'a pas été modifié et s'ils demeurent en possession du destinataire. Toute modification intervenue depuis cette communication lui est communiquée avant la signature. Aucune attestation distincte de réception ou de conservation n'est exigée par le présent article.",
    "La dispense de seconde remise s'applique aux signatures intervenant à compter de l'entrée en vigueur de la loi qui la prévoit, y compris si la première communication est antérieure. Elle ne remet pas en cause les droits et responsabilités nés d'actes antérieurs.")
put('L442-7',p,
    "Réforme de fond : supprimer la seconde remise systématique au moment de la signature quand les mêmes documents ont déjà été communiqués et restent détenus. La communication préalable demeure pour que l'acquéreur ou le preneur connaisse permis et cahier des charges avant de s'engager ; une version modifiée reste communiquée avant signature. L'absence de permis légalement dispensé ne crée pas une pièce impossible à fournir. Aucune attestation de conservation n'est instituée.",
    "La suppression porte sur un doublon matériel propre à cet article, pas sur le simple droit CRPA de réemploi des données entre administrations. Si le destinataire ne détient plus le document ou si son contenu a changé, la dispense de répétition ne joue pas ; aucune forme nouvelle de support, signature ou accusé n'est imposée. Les obligations civiles autonomes de preuve et de consentement conservent leur régime. L442-3/5/6 sont coordonnés sans fermer l'information du cahier des charges pour les lots dispensés de déclaration.",
    'material_reduction',
    "La remise à la signature cesse d'être un second envoi obligatoire de documents inchangés déjà détenus. L'information avant consentement et les mises à jour subsistent ; le bénéfice s'étend aux signatures futures même après une première communication ancienne.",
    "Pas de gain pour les documents jamais reçus, perdus ou modifiés ; aucune réduction des informations utiles ni des recours contractuels n'est établie. Coûts unitaires et solde global non chiffrés.",
    "Aucune charge nouvelle identifiée : pas d'attestation de réception, de support durable spécial ou de registre ; la connaissance de la version exacte avant signature était déjà nécessaire à la communication préalable imposée par la source.",
    [effect('obligation_removed',INFO,
        "Retrait de la remise répétée au moment de signer lorsque les documents identiques ont déjà été communiqués et restent détenus.",
        "Permis et cahier des charges remis à la signature et communiqués préalablement, sans dispense explicite du second exemplaire.",
        "Communication préalable conservée ; pas de seconde remise des mêmes documents encore détenus ; modifications communiquées avant signature.",
        'legal_duty',"Lotisseurs, acquéreurs de lots et preneurs lors de promesses, ventes ou engagements de location.",
        "Signatures dès entrée de la réforme, même pour première communication ancienne ; droits des actes antérieurs réservés.",
        "Aucune attestation ou formalité substitutive ; nouvelle remise seulement si les documents ne sont plus détenus ou ont changé.",
        "Ils doivent leur avoir été communiqués préalablement.",
        "Les documents ainsi communiqués ne sont pas remis de nouveau lors de la signature si leur contenu n'a pas été modifié et s'ils demeurent en possession du destinataire.")],
    removed=["La seconde remise systématique du permis et du cahier des charges à la signature est retirée lorsque les mêmes documents déjà communiqués restent détenus par le destinataire."])

put('L442-9',None,
    "Maintien intégral nécessaire de la caducité des règles d'urbanisme propres au lotissement après dix ans lorsque le PLU ou son équivalent couvre le site, et de la cessation des maintiens majoritaires dans le champ de la loi ALUR. Ces mécanismes libèrent déjà les projets de règles publiques superposées. Le troisième alinéa protège séparément les droits contractuels entre colotis et la gestion commune ; il n'est pas un quota ni une formalité administrative répétitive à supprimer.",
    "Dix ans depuis l'autorisation de lotir, condition de couverture au terme, distinction règlement/cahier approuvé/clauses réglementaires non approuvées : éléments tous conservés. La date de la loi du 24 mars 2014 est historique. Les anciennes décisions de non-opposition et les autorisations de lotir demeurent des titres auxquels la caducité peut s'appliquer ; la suppression de déclaration générale ne fait pas revivre leurs règles caduques. Les rapports privés ne sont pas assimilés à une autorisation publique. La caducité de la règle publique n'est pas une suppression indistincte d'une éventuelle stipulation favorable privée.",
    'retained_necessary',
    "Les extinctions de règles publiques déjà prévues et les protections des rapports privés sont conservées. Aucun nouveau délai raccourci ni contrainte supplémentaire retirée n'est compté.",
    "Les règles peuvent subsister avant dix ans ou sans document d'urbanisme couvrant le lotissement. Les obligations privées demeurent ; leur coût ni leur disparition ne sont présumés.",
    "Aucune charge nouvelle identifiée : aucun vote, envoi, inventaire, dépôt ou attestation n'est ajouté pour bénéficier de la caducité légale.")

put('L442-10',None,
    "Maintien intégral nécessaire de la voie de modification des documents à la demande ou avec l'acceptation de la moitié des propriétaires détenant ensemble au moins la moitié de la superficie. Elle évite une unanimité et permet d'adapter les contraintes, avec compatibilité des règles publiques et protection temporaire du lotisseur propriétaire d'un lot constructible. Aucun rapport, agrément de remplacement ou délai minimum d'instruction n'est imposé par cet article.",
    "La source exige la moitié des propriétaires et au moins la moitié de la superficie, non les anciennes majorités des deux tiers/trois quarts. Le veto du lotisseur dure cinq ans depuis l'achèvement et suppose au moins un lot constructible ; il ne devient ni droit permanent ni agrément préfectoral. R*442-19/20/21 lus : autorité compétente, champs historiques et exceptions de subdivision autonomes conservés. L'allègement de forme de l'accord exprès du lotisseur proposé à R*442-21 ne doit pas être rétabli comme attestation exclusive.",
    'retained_necessary',
    "La faculté majoritaire de modification et ses garanties patrimoniales demeurent. Retirer la procédure sans autre fondement supprimerait une voie utile d'allègement des documents, sans démontrer une baisse de charges.",
    "La protection de cinq ans du lotisseur et les droits des colotis peuvent limiter des projets ; aucun coût net de leur suppression n'est établi et aucune autorisation n'est retirée par ce maintien.",
    "Aucune charge nouvelle identifiée : majorités, champ documentaire, compatibilité et protection du lotisseur sont maintenus sans nouvelle attestation, délai ou publicité.")

s=next(a for a in S if a['number']=='L442-11')
p=s['source_xml'].replace(
    "ou à la décision de non-opposition à une déclaration préalable,",
    "ou à la décision de non-opposition à une déclaration préalable ou à la réalisation de la division d'un lotissement dispensé de déclaration préalable en application de l'article L. 442-3,")
p+=paras("La référence aux divisions dispensées s'applique à celles réalisées à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale des lotissements sans permis. Elle ne modifie pas automatiquement les documents du lotissement et ne dispense ni de l'enquête publique ni de la délibération prévues au premier alinéa. Les modifications et procédures déjà engagées conservent leur régime, sans nouvelle enquête du seul fait de cette coordination.")
put('L442-11',p,
    "Coordination nécessaire : la mise en concordance avec un PLU approuvé après le lotissement doit rester possible pour les divisions futures dispensées de déclaration, comme elle l'était pour les divisions déclarées. L'événement de référence devient leur réalisation, sans nouvelle décision de non-opposition. Le reste des deux alinéas est maintenu intégralement : enquête publique, délibération, champ des documents même non approuvés, densité et voies de transformation urbaine.",
    "L151-7-3 et L315-1 officiels et notes lus : OAP de renouvellement, besoins de réseaux, qualité environnementale et opération délibérée restent à leurs objets. L442-10 protège une voie majoritaire distincte ; L442-13 conserve l'enquête commune avec la DUP. Le code de l'environnement cité pour l'enquête n'est pas fourni dans le corpus des cinq codes : cette référence préexistante ne peut être réputée réécrite ni supprimée. Nouveau renvoi L442-3 lu dans le lot, non cible de reference-targets.json. Aucun quota SRU n'est rétabli et aucune modification de cahier privé n'est automatique.",
    'coordination_only',
    "Le mécanisme de concordance existant continue pour les divisions passant de déclaration obligatoire à dispense. Cette coordination ne supprime aucune enquête et n'institue pas une seconde réduction ou une nouvelle modification d'office.",
    "Le coût de l'enquête et les effets sur les clauses des colotis restent ceux de la procédure existante. Le corpus environnemental et les coûts globaux n'ont pas été audités ; aucune baisse nationale n'est déduite.",
    "Aucune charge nouvelle autonome identifiée : la procédure déjà applicable à ces lotissements après non-opposition suit désormais la division dispensée, avec les mêmes garanties, sans nouveau dépôt ni nouvelle enquête pour la seule transition.",
    [effect('coordination',DIV,
        "Maintien de la mise en concordance des documents pour les lotissements futurs dispensés de déclaration.",
        "PLU approuvé après permis ou non-opposition : modification possible après enquête et délibération.",
        "Même procédure pour PLU approuvé après une division dispensée, sans non-opposition fictive.",
        'regime',"Collectivités et colotis des lotissements dont les documents peuvent être mis en concordance avec un PLU postérieur.",
        "Divisions dispensées réalisées dès réforme ; procédures engagées sans nouvelle enquête liée à la seule coordination.",
        "Enquête et délibération déjà existantes conservées ; aucune modification automatique ou procédure de remplacement de la déclaration.",
        "intervient postérieurement au permis d'aménager un lotissement ou à la décision de non-opposition à une déclaration préalable,",
        "ou à la réalisation de la division d'un lotissement dispensé de déclaration préalable en application de l'article L. 442-3,")])

put('L442-12',None,
    "Maintien intégral nécessaire d'une habilitation encadrant l'assimilation des subdivisions aux modifications de documents de lotissement : son règlement prévoit des exclusions favorables qui évitent une nouvelle procédure lorsque la division respecte le cadre déjà autorisé. Abroger l'habilitation sans traiter les documents communs supprimerait aussi le support de ces exceptions, sans démontrer une obligation autonome inutile dans cet article.",
    "R*442-21 lu intégralement : rattachement à un lot contigu exempté au a ; au b, respect du nombre maximum de lots, quatre voies de division et accord exprès du lotisseur. Sa proposition courante admet un acte signé au lieu d'une attestation distincte et conserve les consentements requis ; le présent maintien ne rétablit pas une attestation exclusive. La dispense nouvelle de L442-3 ne doit pas être subordonnée à une nouvelle déclaration pour bénéficier du b : R*442-21 b reste à coordonner sur ce point, en conservant nombre maximal et consentement. L'habilitation n'impose pas elle-même ce document ; L442-10/11 gardent leurs majorités et enquête dans leurs champs respectifs. Notes 2011/2012 non utilisées comme calendrier de réforme.",
    'retained_necessary',
    "Aucune procédure supplémentaire n'est retirée par le maintien de cette habilitation ; les exceptions de subdivision et les voies de modification des documents restent disponibles avec leurs protections.",
    "La coordination réglementaire de R*442-21 b pour la division désormais dispensée reste à rédiger hors du lot. Aucune suppression générale des droits du lotisseur ou des colotis ni coût global n'est démontré.",
    "Aucune charge nouvelle identifiée dans l'article conservé : ni accord, déclaration, registre ou attestation n'est ajouté ; le renvoi habilitant les exceptions demeure, sans rétablir l'ancien support exclusif.")

put('L442-13',None,
    "Maintien intégral nécessaire de l'enquête publique commune à l'utilité publique d'une opération et à la modification des règles incompatibles du lotissement : elle évite deux enquêtes et la DUP emporte elle-même modification. La participation est une garantie essentielle lors d'une opération pouvant conduire à expropriation ; la supprimer ne se justifie pas comme retrait d'un doublon.",
    "Champ limité aux dispositions à caractère réglementaire régissant un lotissement approuvé, non à l'effacement général des droits privés. L442-14 conserve expressément l'opposabilité de ces modifications. La réforme de déclaration à L442-3 ne crée pas une nouvelle autorisation ou enquête pour une simple division ; la présente enquête ne joue qu'en présence de l'opération d'utilité publique incompatible. La base environnementale et le régime général de DUP restent extérieurs au lot.",
    'retained_necessary',
    "L'enquête unique et l'effet de modification de la DUP préexistent et sont conservés ; aucune seconde fusion de procédure n'est revendiquée.",
    "Ne retire ni expropriation, indemnisation, règles privées ou participation du public. Les procédures générales de DUP et le solde global des coûts ne sont pas examinés ici.",
    "Aucune charge nouvelle identifiée : maintien d'une procédure déjà commune, sans nouveau dossier, formalité de confirmation ou délai ajouté.")

s=next(a for a in S if a['number']=='L442-14')
p=s['source_xml']+paras(
    "Pour un lotissement dont la division est réalisée à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale et qui est dispensé de cette déclaration en application de l'article L. 442-3, le permis de construire ne peut être refusé ou assorti de prescriptions spéciales sur le fondement de dispositions d'urbanisme nouvelles intervenues depuis la date à laquelle la division en propriété ou en jouissance est réalisée, et ce pendant cinq ans à compter de cette date. Les règles du présent article relatives à l'opposabilité des modifications des documents du lotissement et au maintien des règles après annulation ou déclaration d'illégalité s'appliquent à cette garantie. Pour l'application de la règle relative à l'annulation ou à la déclaration d'illégalité, les règles maintenues sont celles en vigueur à la date de la division. La date de division peut être établie par tout moyen légal, sans déclaration, attestation ou dépôt supplémentaire propre à cette garantie.",
    "Les garanties attachées aux permis d'aménager et aux décisions de non-opposition déjà intervenus demeurent applicables pour toute leur durée. Les déclarations déposées avant cette entrée en vigueur et poursuivies conformément à l'article L. 442-3 conservent la garantie attachée à leur décision de non-opposition, sans cumul de durées pour une même division.")
put('L442-14',p,
    "Coordination nécessaire avec la suppression de déclaration : conserver le bénéfice de cinq ans pour les futures divisions dispensées, sans demander une non-opposition qui n'existe plus. Leur date de division devient le point de départ de la garantie automatique. Les trois paragraphes sources sont conservés intégralement, avec les deux points de départ existants, les modifications opposables et les effets limités de l'annulation ou de l'illégalité d'un document d'urbanisme. Ce maintien favorable n'est pas une seconde déclaration supprimée.",
    "Cinq ans depuis la non-opposition pour le régime déclaré ; cinq ans depuis l'achèvement des travaux pour le permis d'aménager, avec règles nouvelles appréciées depuis délivrance de ce permis : aucune confusion entre ces dates. L442-10/11/13 lus et maintenus ou coordonnés dans le lot ; leurs modifications restent opposables même pendant la garantie. Le dernier alinéa source ne vise que le motif étranger aux règles d'urbanisme applicables au lotissement, condition conservée. Pour les divisions dispensées, pas de certificat obligatoire de date ni de déclaration volontaire reconstituée ; les garanties anciennes restent entières et sans double durée. Nouveau renvoi à L442-3 lu dans le lot, non cible de reference-targets.json. La note de 2018 concerne le 1er janvier 2019 et non l'entrée en vigueur future.",
    'coordination_only',
    "Le régime favorable de cinq ans est maintenu pour les opérations futures passant à la dispense, avec un fait déclencheur matériel à défaut de décision. Les garanties existantes et leurs exceptions restent intégrales ; la suppression déclarative est comptée une fois à L442-3.",
    "Le changement du point de départ peut décaler le calendrier par rapport à une ancienne non-opposition : son incidence n'est pas chiffrée. Pas d'extension des cinq ans du permis d'aménager ni de suppression des modifications légalement opposables.",
    "Aucune charge nouvelle identifiée : date prouvable par tout moyen légal sans attestation, registre ou dépôt ; pas de procédure facultative rendue nécessaire pour conserver la garantie des futures divisions.",
    [effect('coordination',DIV,
        "Conservation automatique de la garantie de stabilité urbanistique pour les divisions désormais dispensées de déclaration.",
        "Pour le lotissement déclaré, règles nouvelles inopposables pendant cinq ans depuis non-opposition ; régime distinct du permis depuis achèvement des travaux.",
        "Régimes anciens conservés ; pour la future division dispensée, même protection de cinq ans à compter de la division, sans nouvelle formalité.",
        'regime',"Demandeurs de permis de construire sur des lots issus de divisions désormais dispensées et titulaires des garanties antérieures.",
        "Divisions nouvelles dès réforme ; garanties anciennes et déclarations anciennes poursuivies préservées sans cumul pour la même division.",
        "Aucune attestation ni décision substitutive ; modifications des documents et condition propre à l'illégalité conservées.",
        "et ce pendant cinq ans à compter de cette même date.",
        "La date de division peut être établie par tout moyen légal, sans déclaration, attestation ou dépôt supplémentaire propre à cette garantie.")],
    benefit="La stabilité de cinq ans reste entière pour les lotissements déclarés et ceux autorisés par permis, avec leurs points de départ distincts. Elle reste ouverte aux nouvelles divisions dispensées de déclaration par une garantie automatique de cinq ans depuis la division, sans justificatif spécial. Les modifications L442-10/11/13 restent opposables et l'exception relative à l'illégalité étrangère aux règles du lotissement est conservée, sans réduction d'une garantie ancienne.")

put('L442-15',None,
    "Maintien intégral nécessaire du champ des terrains lotis pour jardins : ils bénéficient aussi de la caducité des règles publiques et des voies d'adaptation des documents de L442-9 à L442-11 et L442-13. Supprimer ce renvoi retirerait des voies favorables de déblocage et des garanties communes, sans supprimer une déclaration ou prélèvement propre à cet article.",
    "Les cibles sont toutes lues dans le présent lot : caducité, modification majoritaire, concordance avec PLU et enquête commune avec DUP. L442-11 coordonné n'ajoute aucune formalité de division aux jardins ; L442-14 n'est pas ajouté au champ par analogie. Aucun quota de logement social ni régime d'emploi n'est visé.",
    'retained_necessary',
    "Le champ utile des mécanismes de caducité et de modification reste identique pour les jardins ; aucune réduction supplémentaire n'est comptée par ce renvoi.",
    "Ne rend pas les jardins constructibles et n'étend pas les garanties de L442-14. Les droits privés et la gestion commune conservent leur régime sans chiffrage de coût.",
    "Aucune charge nouvelle identifiée : le renvoi existant est conservé sans nouvelle liste, attestation, autorisation ou délai propre aux jardins.")

put('L443-2',None,
    "Maintien intégral nécessaire des prescriptions d'information, d'alerte et d'évacuation des campings exposés à un risque naturel ou technologique prévisible : leur fonction essentielle est la sécurité des personnes, y compris après ouverture du terrain. Consultation du propriétaire et de l'exploitant, avis de l'autorité administrative et compatibilité avec le plan de prévention sont conservés ; ils coordonnent le risque et le contradictoire plutôt qu'un contrôle de pure opportunité redondant.",
    "L443-3 du lot lu : fermeture seulement après défaut d'exécution au terme fixé, substitution préfectorale après mise en demeure. La « carence » de l'autorité n'est pas la carence SRU ni un quota de logement social. La source ne prévoit aucun délai minimal uniforme à retirer : le délai est fixé pour l'exécution des mesures propres au risque. La référence au chapitre II du titre VI du livre V du code de l'environnement est extérieure aux cinq codes ; elle est conservée sans prétendre l'avoir réécrite. L443-1 et R*421-19 lus pour le champ des terrains, non pour changer les seuils.",
    'retained_necessary',
    "Les mesures de sauvegarde et la procédure contradictoire restent intégrales après examen de leurs charges ; aucune prescription indispensable à l'évacuation n'est supprimée ou remplacée.",
    "Le coût des dispositifs peut être important mais leur nécessité doit être appréciée selon le risque local. Aucun bilan national de coût, ni audit complet du droit environnemental n'est établi.",
    "Aucune charge nouvelle identifiée : pouvoir, consultations, avis, délai d'exécution adapté et compatibilité avec le plan sont ceux de la source entière, sans nouveau rapport ou registre.")

put('L443-3',None,
    "Maintien intégral nécessaire du pouvoir de fermer et d'évacuer un camping lorsque les prescriptions de sécurité n'ont pas été exécutées à l'issue du délai imparti, jusqu'à leur exécution. La substitution du préfet après mise en demeure évite qu'une carence locale expose les occupants. Ce mécanisme n'est ni une autorisation préalable superflue ni une fermeture économique discrétionnaire à retirer.",
    "L443-2 lu avec ses zones à risques, avis, consultation du propriétaire et de l'exploitant et compatibilité avec le plan de prévention. Le défaut d'exécution et l'expiration du délai sont cumulatifs ; la fermeture n'est pas automatique et cesse avec l'exécution. La mise en demeure vise l'autorité compétente avant substitution préfectorale, non un second agrément de l'exploitant. Aucune assimilation à la carence SRU, au préavis de quinze jours ou à la durée d'un contrat de travail.",
    'retained_necessary',
    "Maintien des moyens d'exécution des mesures essentielles de sécurité, sans nouvelle autorisation ni nouvelle sanction autonome. Aucun allègement n'est revendiqué pour cet article.",
    "Ne supprime pas les voies de recours de droit commun ni les pouvoirs de police d'autres fondements. Ni coût d'évacuation ni effet global des procédures de risque n'est chiffré.",
    "Aucune charge nouvelle identifiée : maintien du délai d'exécution déjà fixé et de la mise en demeure avant substitution, sans notification ou justification ajoutée.")

# Coordinations des avantages dont le fait déclencheur était la déclaration supprimée.
s=next(a for a in S if a['number']=='L442-9')
p=s['source_xml']+paras(
    "Pour les lotissements dont la division est réalisée à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale et qui sont dispensés de cette déclaration en application de l'article L. 442-3, le délai de dix années prévu au premier alinéa court à compter de la date à laquelle la division en propriété ou en jouissance est réalisée. La couverture par un plan local d'urbanisme ou un document d'urbanisme en tenant lieu reste requise à l'expiration de ce délai. La date de division peut être établie par tout moyen légal, sans déclaration, attestation ou dépôt supplémentaire. Les autres dispositions du présent article demeurent applicables.",
    "Les délais déjà ouverts par une autorisation de lotir, un permis d'aménager ou une décision de non-opposition ne sont pas recommencés. Pour les déclarations déposées avant cette entrée en vigueur et poursuivies conformément à l'article L. 442-3, le point de départ reste attaché à la décision de non-opposition prise à leur terme, sans cumul ou redémarrage du délai pour une même division.")
put('L442-9',p,
    "Coordination nécessaire pour ne pas faire perdre la caducité décennale aux futurs lotissements dispensés de déclaration : leur division remplace l'autorisation comme point de départ, sans nouvelle formalité. Les trois alinéas sources sont maintenus intégralement : catégories de règles publiques, couverture par le PLU, cessation des anciens maintiens majoritaires et préservation des droits contractuels et de la gestion commune. Ce n'est pas une nouvelle réduction du délai de dix ans.",
    "La date de la loi du 24 mars 2014 reste historique. La date matérielle de division n'est utilisée que pour les lotissements futurs effectivement dispensés par L442-3 ; les régimes soumis à permis ou à déclaration résiduelle conservent leurs titres. Les délais anciens ne repartent pas de zéro. Les règles privées ne deviennent pas caduques par cette coordination. Nouveau renvoi L442-3 lu dans le lot, non cible de reference-targets.json. Les modalités réglementaires de constat de la division et de caducité doivent être alignées sans réintroduire un dépôt pour obtenir la date.",
    'coordination_only',
    "L'avantage de caducité décennale est rendu opératoire pour les divisions passant à la dispense ; les trois règles sources restent intégrales et les situations antérieures ne perdent aucun délai acquis.",
    "Le passage d'une décision antérieure à la division matérielle peut décaler la date de caducité pour les opérations futures ; aucune variation de coût ou de valeur n'est chiffrée. Les obligations privées demeurent.",
    "Aucune charge nouvelle identifiée : date établissable par tout moyen légal sans attestation, registre ou dépôt ; la condition de couverture par un document d'urbanisme et le délai décennal sont préexistants.",
    [effect('coordination',DIV,
        "Maintien de la caducité des règles publiques du lotissement quand la division ne donne plus lieu à une décision administrative.",
        "Caducité au terme de dix années depuis l'autorisation de lotir, sous couverture par un PLU ou équivalent à cette date.",
        "Même caducité et même couverture requise ; pour la division future dispensée, dix années depuis sa réalisation, sans nouveau titre.",
        'regime',"Colotis et propriétaires des lotissements futurs dispensés, ainsi que titulaires de délais anciens conservés.",
        "Divisions dispensées réalisées dès réforme ; délais anciens et déclarations anciennes poursuivies sans remise à zéro.",
        "Aucune déclaration de date ; droits et obligations privés ainsi que gestion commune conservés.",
        "deviennent caduques au terme de dix années à compter de la délivrance de l'autorisation de lotir",
        "le délai de dix années prévu au premier alinéa court à compter de la date à laquelle la division en propriété ou en jouissance est réalisée.")])

s=next(a for a in S if a['number']=='L442-12')
p=s['source_xml']+paras(
    "Les subdivisions dispensées de déclaration préalable en application de l'article L. 442-3 conservent le bénéfice des exceptions à cette assimilation sans être subordonnées au dépôt d'une déclaration supprimée. En particulier, une telle subdivision n'est pas assimilée à une modification des règles du lotissement lorsqu'elle intervient dans la limite du nombre maximum de lots autorisés et que le lotisseur a donné son accord exprès sur cette opération. L'accord peut être établi par une attestation ou par un acte signé par le lotisseur identifiant la subdivision et manifestant expressément son accord ; aucune attestation distincte n'est exigée lorsque cet acte établit déjà l'accord. Le silence ne vaut pas accord. Les autres droits ou consentements privés légalement requis ne sont pas écartés.",
    "Les exceptions existantes, notamment celles relatives au détachement d'une partie de lot pour la rattacher à un lot contigu, demeurent applicables sans condition nouvelle. Les subdivisions excédant le nombre maximum de lots autorisés ou modifiant les documents du lotissement sur un autre objet restent soumises aux règles de modification qui leur sont applicables.",
    "Ces dispositions s'appliquent aux subdivisions réalisées à compter de l'entrée en vigueur de la loi supprimant la déclaration préalable générale des lotissements sans permis, y compris dans un lotissement autorisé auparavant. Les accords et actes régulièrement établis restent utilisables, sans nouveau dépôt ni reprise des délais ; les décisions et les droits des tiers ne sont pas automatiquement modifiés.")
put('L442-12',p,
    "Coordination de fond nécessaire : conserver pour les subdivisions futures dispensées de déclaration l'exception favorable qui reposait à R*442-21 b sur une déclaration ou un autre titre. Le décret reste habilité par le premier alinéa intégralement maintenu, mais ne peut exiger un dépôt supprimé pour laisser jouer cette exception. Nombre maximal de lots autorisés, accord exprès et droits privés restent protégés ; l'acte signé déjà admis dans la proposition courante de R*442-21 remplace, au choix, l'attestation distincte.",
    "R*442-21 source, notes et proposition lus intégralement : a de rattachement contigu sans condition nouvelle ; b avec plafond des lots et consentement exprès maintenu. L'exemption législative nouvelle transpose la voie anciennement déclarée aux mêmes subdivisions désormais dispensées, sans étendre l'exemption à des modifications d'autres documents ou à un dépassement du nombre autorisé. R*442-21 b et son renvoi R*442-3 restent à aligner, sans nouvelle attestation exclusive ni déclaration volontaire imposée. L442-10/11 gardent leurs majorités et enquête dans leurs champs résiduels. Nouveau renvoi à L442-3, lu dans le lot mais non cible de reference-targets.json ; aucun contrôle automatique ne vaut appréciation du consentement ou des droits des tiers.",
    'coordination_only',
    "Le bénéfice de l'exception de subdivision demeure ouvert aux futures divisions passant à la dispense. L'accord par acte signé n'est pas compté comme une seconde suppression de pièce, déjà proposée à R*442-21 ; la suppression déclarative reste une seule mesure.",
    "Ne supprime pas le nombre maximal de lots, le consentement exprès du lotisseur ou les droits des colotis. L'assimilation et les procédures de modification subsistent pour les changements d'autres objets ; les textes réglementaires restent à aligner.",
    "Aucune charge nouvelle identifiée : pas de nouveau dépôt pour bénéficier de l'exception ; les conditions de nombre et d'accord reprennent l'exception existante, avec acte signé ou attestation au choix, sans preuve supplémentaire de remplacement.",
    [effect('coordination',DIV,
        "Conservation de l'exemption d'assimilation à une modification de lotissement pour les subdivisions désormais dispensées de déclaration.",
        "Habilitation à l'assimilation ; exception R*442-21 b attachée notamment à une déclaration préalable, dans le nombre maximal autorisé et avec accord du lotisseur.",
        "Même exception ouverte à la subdivision dispensée sans dépôt fictif ; nombre maximal et accord exprès conservés, ainsi que rattachement contigu.",
        'regime',"Propriétaires subdivisant des lots issus d'un lotissement autorisé, dans la limite du nombre de lots et avec accord exprès.",
        "Subdivisions dès entrée de la dispense, même dans un ancien lotissement ; accords antérieurs utilisables, décisions et droits des tiers non modifiés automatiquement.",
        "Pas de déclaration ni attestation additionnelle ; mêmes conditions de nombre et consentement, preuve possible par acte signé.",
        "sont assimilées aux modifications des règles d'un lotissement prévues aux articles L. 442-10 et L. 442-11",
        "Les subdivisions dispensées de déclaration préalable en application de l'article L. 442-3 conservent le bénéfice des exceptions à cette assimilation sans être subordonnées au dépôt d'une déclaration supprimée.")])

checks_6 = {
 'L1234-1': "Aucun renvoi littéral ni relation d'emploi dans L433-6 : ses baux et droits réels sont patrimoniaux. Le L1234-1 officiel règle un préavis de licenciement selon moins de six mois, six mois à moins de deux ans, puis deux ans ; sa proposition porte quinze jours calendaires pour les nouveaux contrats, avec anciens contrats préservés. Ni ces anciennetés ni ce préavis ne s'appliquent à la remise en état d'un bâtiment ou à l'exclusion d'indemnité du présent article.",
 'L1221-2': "L1221-2 concerne la durée du contrat de travail privé, et sa proposition réserve les contrats antérieurs tout en interdisant les nouveaux CDD et leur renouvellement. Les baux de toute nature de L433-6 ne sont pas des contrats de travail : aucune conversion de bail en contrat unique, aucun terme de bail effacé et aucune condition d'ancienneté d'emploi ne découle ici de cette cible de contexte.",
 'L1234-9': "L'indemnité de L433-6 concerne des droits sur bâtiments et l'autorité ayant ordonné la remise en état, pas un licenciement. Le L1234-9 officiel vise huit mois d'ancienneté, hors faute grave ; sa proposition distingue seuil d'un an au terme effectif, préavis inclus, calcul sur toute l'ancienneté à 0,20 mois par année, mois complets et plafond de six mois, ainsi que droits des anciens contrats. Aucun de ces paramètres ne réduit une indemnité foncière ni une créance salariale ici.",
 'L433-3': "L433-3 officiel impose enlèvement et remise en état aux frais du titulaire ou ayant droit à la date du permis ou, sur emplacement réservé ou périmètre de DUP, à la première demande du bénéficiaire ou expropriant. Sa proposition réserve explicitement L433-4. L433-6 maintenu règle distinctement l'indemnisation des titulaires de droits sur les deux catégories de bâtiments ; il ne modifie ni le déclencheur du retrait ni une notification ou ancienneté de travail.",
 'L433-4': "L433-4 officiel et proposé ouvrent une indemnité proportionnelle au délai restant lorsque la puissance publique fait remettre en état avant le délai fixé au permis. Cet avantage demeure ; la portée de l'exclusion visant les droits dérivés à L433-6 doit être articulée avec ce droit propre, sans l'effacer par analogie avec une indemnité de licenciement. Le seuil d'un an du contrat unique et son plafond ne s'y appliquent pas ; la tension de la clause générale est signalée en review_notes.",
 'L433-5': "L433-5 exclut dans l'acquisition publique la valeur des constructions précaires et celle ou l'augmentation de valeur des fonds qu'elles ont permis, puis déduit les frais de démolition si la remise en état n'a pas précédé le transfert. Le fonds du terrain n'est pas supprimé de toute indemnisation par ce texte. L433-6 concerne les titulaires de droits réels ou baux ; son maintien n'ajoute ni ancienneté, préavis ou condition de travail à l'évaluation foncière.",
}
checks_7 = {
 'L1234-1': "L433-7 porte une mention de précarité dans l'acte immobilier ; il n'institue aucune notification de licenciement. La source de L1234-1 distingue les seuils de six mois et deux ans ; la proposition fixe quinze jours calendaires pour les nouveaux contrats et réserve les anciens contrats et protections spéciales. La suppression de la seule nullité immobilière n'applique aucun de ces seuils ni préavis à une vente ou un bail et n'écarte aucune procédure collective de rupture.",
 'L1221-2': "La règle nouvelle de L1221-2 interdit les nouveaux CDD de travail privé et préserve les contrats antérieurs ; elle ne concerne pas les ventes, locations ou constitutions de droits réels de L433-7. La mention du caractère précaire reste obligatoire pour l'acte immobilier nouveau, quelle que soit la durée du bail. L'allègement de nullité ne convertit donc ni un bail en contrat unique ni une location ancienne en emploi indéterminé.",
 'L1234-9': "La nullité spéciale de l'acte et l'indemnité de licenciement ont des objets distincts. L1234-9 proposé mesure un an à la fin effective du contrat de travail, préavis inclus, puis toute l'ancienneté à 0,20 mois par année et fractions de mois complets, plafond de six mois, avec régime propre des anciens contrats. Ni ce seuil ni ce barème ne s'appliquent à l'omission de la mention immobilière ; les réparations civiles et créances de salariés ne sont pas supprimées par L433-7.",
 'L433-3': "L433-3 conserve la remise en état à la date fixée ou, dans ses deux zones foncières spéciales, sur première demande ; son texte proposé précise la réserve d'indemnité L433-4. L433-7 réécrit conserve la mention qui avertit l'acquéreur ou le preneur de cette précarité. Retirer la nullité attachée à la seule omission n'efface ni l'obligation d'enlever, ni la qualité d'ayant droit, ni la protection d'une indemnité fondée sur L433-4 ; aucun préavis d'emploi de quinze jours ne s'y substitue.",
 'L433-4': "Le droit proportionnel au délai restant de L433-4 suppose un terme fixé au permis et une remise en état publique anticipée. La mention de précarité conservée à L433-7 permet d'en connaître le cadre ; sa nouvelle transition ne valide pas rétroactivement un acte omettant cette mention. Le retrait de la nullité spéciale ne supprime pas l'indemnité de L433-4, n'ajoute aucune ancienneté et ne lui applique pas le zéro d'indemnité de travail avant un an.",
 'L433-5': "La cible régit l'évaluation lors de l'acquisition publique et les frais de démolition avant ou après transfert, non une indemnité ordinaire d'emploi. Le destinataire de l'acte reste informé par L433-7 de la précarité affectant la valeur des constructions et du fonds commercial. La nullité spéciale supprimée pour les actes nouveaux ne modifie ni l'assiette d'évaluation de L433-5 ni les coûts de remise en état ; les actes anciens gardent leur régime d'information et de recours.",
 'L433-6': "La vue requise de L433-6 est la source officielle seule, sans proposition préalable ; elle exclut l'indemnisation par l'autorité pour les bâtiments précaires et, sous conditions de date et d'engagement, les bâtiments existants voués à suppression. L433-7 continue d'informer sur la précarité sans étendre cette exclusion à d'autres bâtiments, créances contractuelles ou salariés. Le maintien intégral de L433-6 dans le présent lot n'est pas présenté comme une nouvelle cible de droit positif réformé.",
}

for n, analyses in [('L433-6', checks_6), ('L433-7', checks_7)]:
    o=OUT[n]
    req=R['requirements'][o['code_id']+'|'+o['source_id']]
    o['reference_checks']=[dict(target_key=k,view_sha256=R['targets'][k]['view_sha256'],
                                assessment=analyses[R['targets'][k]['number']]) for k in req]

# Passages complets, sans ellipse : chaque preuve source conserve aussi ses conditions.
proof_paragraphs={'L433-7':1,'L441-2':1,'L441-4':0,'L442-1-3':4,
                  'L442-3':0,'L442-4':1,'L442-5':0,'L442-6':0,'L442-7':1,
                  'L442-9':3,'L442-11':0,'L442-12':1,'L442-14':3}
for n,i in proof_paragraphs.items():
    s=next(a for a in S if a['number']==n)
    o=OUT[n]
    quoted_proposal=unescape(re.findall(r'<p>(.*?)</p>',o['proposed_xml'],flags=re.S)[i])
    for e in o['substantive_impact']['effects']:
        e['source_quote']=text_of(s['source_xml']).strip()
        e['proposed_quote']=text_of(quoted_proposal)

# Contrôles de structure et de citations ; aucune de ces vérifications n'est une validation juridique.
allowed={'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
class XMLCheck(HTMLParser):
    def handle_starttag(self, tag, attrs):
        assert tag in allowed, tag
        for k,v in attrs:
            assert k in {'rowspan','colspan'} and v and v.isdigit(), (k,v)
    handle_startendtag=handle_starttag

answer=[OUT[s['number']] for s in S]
assert len(answer)==24 and len(OUT)==24
for s,o in zip(S,answer):
    for k in ['code_id','source_id','source_sha256','number']:
        assert o[k]==s[k]
    si=o['substantive_impact']
    assert si['version']==1
    for k in ['assessment','scope_limitations','new_burdens_review']:
        assert len(si[k])>=40,(o['number'],k)
    if s.get('benefit_check_required'):
        assert len(o.get('benefit_review',''))>=100,o['number']
    key=s['code_id']+'|'+s['source_id']
    assert [c['target_key'] for c in o['reference_checks']]==R['requirements'][key]
    for c in o['reference_checks']:
        assert len(c['assessment'])>=80
        assert c['view_sha256']==R['targets'][c['target_key']]['view_sha256']
    if o['status']=='retained_unchanged':
        assert o['proposed_xml'] is None and o['classification']=='retained_necessary'
        assert not si['effects'] and si['classification']=='retained_necessary'
    else:
        assert o['proposed_xml'] and o['proposed_xml']!=s['source_xml']
        parser=XMLCheck();parser.feed(o['proposed_xml']);parser.close()
    if o.get('change_type')=='normative_reduction':
        assert all(len(x)>=30 for x in o['removed_provisions'])
    if o.get('change_type')=='full_repeal':
        assert text_of(o['proposed_xml']).startswith(('Le présent article est abrogé','Abrogé'))
        assert len(o['repeal_scope'])>=30
    for e in si['effects']:
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',e['measure_id'])
        assert 6<=len(e['measure_id'])<=96
        for k,full in [('source_quote',text_of(s['source_xml'])),('proposed_quote',text_of(o['proposed_xml']))]:
            assert len(e[k])>=12 and e[k] in full,(o['number'],k,e[k])

with open('answer.json','w') as f:
    json.dump(answer,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'output_file':'answer.json','article_count':len(answer),
                  'statuses':{x:sum(o['status']==x for o in answer) for x in ['rewrite_draft','retained_unchanged']},
                  'classes':{x:sum(o['substantive_impact']['classification']==x for o in answer) for x in sorted({o['substantive_impact']['classification'] for o in answer})}},ensure_ascii=False))
