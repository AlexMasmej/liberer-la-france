import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}

def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml))

def paragraphs(*items):
    return ''.join('<p>' + item + '</p>' for item in items)

def effect(kind, measure, description, before, after, unit, population,
           transition, replacement, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure, description=description,
                before=before, after=after, unit=unit,
                affected_population=population, conditions_and_transition=transition,
                replacement_or_new_burdens=replacement,
                source_quote=source_quote, proposed_quote=proposed_quote)

def put(number, proposed, reason, notes, classification, assessment, limitations,
        burdens, effects=None, removed=None, repeal=None, benefit=None):
    source = by_number[number]
    a = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
             status='retained_unchanged' if proposed is None else 'rewrite_draft')
    if proposed is None:
        a['classification'] = 'retained_necessary'
    if removed:
        a.update(change_type='normative_reduction',
                 reform_policy_id='editorial_direction_2026_10_19',
                 removed_provisions=removed)
    if repeal:
        a.update(change_type='full_repeal',
                 repeal_policy_id='editorial_direction_2026_10_19',
                 repeal_scope=repeal)
    if benefit:
        a['benefit_review'] = benefit
    a['substantive_impact'] = dict(version=1, classification=classification,
        assessment=assessment, scope_limitations=limitations,
        new_burdens_review=burdens, effects=effects or [])
    a['reference_checks'] = []
    answers[number] = a

put('L552-6', None,
    "Maintien intégral après examen : l'intervention du juge et du délégué protège l'affectation des prestations aux besoins de la famille. Le texte ne crée ni prélèvement sur l'allocataire ni démarche périodique ; il attribue les frais à un seul organisme, celui qui verse la prestation la plus élevée en cas de pluralité.",
    "Conserver le champ de l'article 375-9-1 du code civil et du RSA des personnes isolées de L262-9 du code de l'action sociale et des familles. Ces textes extérieurs ne sont pas fournis intégralement ici ; leur régime n'est pas réécrit. La prise en charge de frais de protection judiciaire n'est pas une taxe accessoire supprimable sans autre financement.",
    'retained_necessary',
    "La source entière est maintenue : mesure judiciaire ciblée, perception de tout ou partie des prestations et règle évitant le partage des frais entre organismes. Aucune simplification nouvelle n'est revendiquée.",
    "La nécessité du financement de la mesure est conservée, sans chiffrage de son coût ni modification de la procédure civile extérieure au lot.",
    "Aucune charge nouvelle identifiée : ni dossier ni certificat ni financement nouveau n'est ajouté ; les frais restent imputés selon la règle source.")

put('L552-7', None,
    "Maintien intégral des droits après le décès d'un enfant : prestations énumérées, prise en compte de l'enfant pour les autres prestations, allocation de rentrée scolaire et acquisition de l'avance d'ASF sans recouvrement contre l'autre parent. Ce sont des protections de revenu, non des prélèvements successoraux ou des contraintes à supprimer.",
    "Les cinq séquences normatives du paragraphe source et la transition de la loi du 8 juin 2020 sont conservées. R552-4 a été lu dans le corpus : ouverture préalable du droit, montant du mois du décès, exception R541-1 et conditions propres restent à leur champ. L543-1 vise notamment l'apprentissage ; la durée pédagogique ne devient pas le terme de l'emploi. Aucun délai du droit du travail n'est importé.",
    'retained_necessary',
    "La source complète conserve pour les décès futurs éligibles les prestations et la neutralisation temporaire des conséquences du décès ; aucune suppression de charge nouvelle n'est comptée.",
    "Les durées et la date relatives à la rentrée restent celles des décrets applicables, sans création d'un montant ni d'une durée. Il ne s'agit pas de droits de succession.",
    "Aucune charge nouvelle identifiée : le maintien ne requiert aucune attestation, démarche ou condition supplémentaire par rapport à la source.")

put('L553-3', None,
    "Maintien intégral du mécanisme différentiel : la priorité des prestations familiales ne retire pas le surplus des majorations, le cumul spécial pour les enfants infirmes demeure, et l'ASF reste hors du dispositif. La règle coordonne plusieurs financeurs sans taxe ni justificatif additionnel.",
    "Les quatre catégories 1° à 4°, l'exception d'âge pour l'allocation de logement et l'exclusion de l'ASF sont conservées. Les majorations de pensions publiques ou de prévoyance ne sont ni l'indemnité de rupture du contrat unique ni la capitalisation des salariés privés. Le renvoi descriptif ancien à l'allocation de logement n'est pas transformé en allocation aux adultes handicapés.",
    'retained_necessary',
    "La source entière évite le double paiement d'une même majoration tout en garantissant le complément différentiel et les deux exceptions favorables ; aucun allègement inédit n'est démontré.",
    "Aucun régime de majoration extérieur n'est réécrit ni déclaré supprimé. Les effets budgétaires de ces cumuls ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : les priorités de paiement restent identiques, sans déclaration, contrôle préalable ni délai nouveau.")

put('L553-4', None,
    "Maintien intégral de l'incessibilité et de l'insaisissabilité, avec les seules exceptions énumérées : fraude, dettes alimentaires, soins et entretien de l'enfant handicapé, ainsi que le prélèvement volontaire de cotisations. Ce sont des garanties essentielles de subsistance et des droits des enfants, non des formalités redondantes.",
    "L553-2 garde ses sept alinéas d'origine ; son troisième alinéa, visé pour le calcul des retenues, reste entier. D553-1 à D553-3 lus : calcul selon ressources, composition et logement, actualisation et saisie demeurent. Conserver I, II abrogé, III, l'accord pour l'intermédiation, la priorité alimentaire et le retrait mensuel malgré blocage bancaire. La note source vise un 'troisième alinéa du 2° du I' alors que le découpage affiché est différent : anomalie historique signalée, sans déplacement d'alinéa.",
    'retained_necessary',
    "La source complète protège les prestations sur les comptes et encadre leurs saisies ; l'exception volontaire d'assurance ne constitue pas une cotisation obligatoire nouvelle. Aucun gain propre n'est compté.",
    "La suppression des frais de gestion d'indus dans L553-2 ne supprime pas le principal ni les saisies alimentaires. Les règles bancaires et d'exécution extérieures ne sont pas réécrites.",
    "Aucune charge nouvelle identifiée : mêmes consentements, mêmes catégories saisissables et même limite mensuelle ; aucun fichier ou justificatif ajouté.")

put('L553-5', None,
    "Maintien intégral après examen de la contrainte : l'évaluation n'est déclenchée que par une disproportion marquée constatée lors d'une demande ou d'un contrôle. Elle permet de traiter une dissimulation de ressources sans généraliser une déclaration patrimoniale périodique. Son exclusion expresse de l'allocation de logement familiale est conservée.",
    "Le a du 2° de L821-1 du code de la construction et de l'habitation a été lu : il s'agit de l'allocation de logement familiale, non de l'AAH de l'article homonyme du CSS fourni parmi les cibles. Le patrimoine, la période déclarée, la France et l'étranger, ainsi que les modalités réglementaires sont maintenus. L114-17 lu distingue la bonne foi et la fraude ; ne pas transformer le simple constat de train de vie en qualification pénale automatique.",
    'retained_necessary',
    "La source entière conserve un contrôle ciblé de sincérité des ressources et son exclusion favorable de logement ; aucune suppression de prélèvement ou de déclaration n'est revendiquée.",
    "Le barème réglementaire de l'évaluation n'est pas assigné ici ; aucun rendement du contrôle ni solde global de complexité n'est établi. Aucun nouveau contrôle universel n'est décidé.",
    "Aucune charge nouvelle identifiée : le fait déclencheur et le périmètre des éléments examinés restent ceux de la source, sans nouvelle collecte périodique.")

put('L581-1', None,
    "Maintien intégral de l'habilitation d'aide au recouvrement des créances d'entretien d'enfants. Elle fonde un service favorable aux familles et ne prescrit ni contribution, ni autorisation individuelle, ni dossier autonome supplémentaire.",
    "L'habilitation doit rester le support du recouvrement des articles L581-2 à L581-10 et de L582-1. Les allègements des frais et du visa préfectoral proposés dans ce lot ne retirent ni la créance d'aliments ni l'accès au service.",
    'retained_necessary',
    "La source entière conserve l'accès à l'aide au recouvrement, y compris pour les futures créances remplissant les conditions du chapitre ; aucune nouvelle réduction n'est comptée.",
    "La portée des procédures civiles d'exécution ne résulte pas de cette seule habilitation ; aucune réécriture de ces procédures extérieures n'est revendiquée.",
    "Aucune charge nouvelle identifiée : l'organisme conserve sa compétence existante, sans taxe, déclaration ou autorisation de remplacement.")

put('L581-2', None,
    "Maintien intégral des avances d'ASF en cas de défaut total ou partiel, de la limite de subrogation et du surplus acquis au créancier. L'allocation différentielle du 4° du I de L523-1 demeure non recouvrable. Supprimer ces dispositions fermerait des avantages futurs et la garantie de revenu des enfants.",
    "L523-1 lu en entier dans le corpus : conserver les titres exécutoires du IV et le complément différentiel du 4° du I, qui est distinct d'une avance récupérable. La suppression des frais de L581-5 ne modifie ni le principal alimentaire ni l'étendue de la subrogation. Ne pas déduire une disparition de la dette du seul décès ou d'une réforme successorale.",
    'retained_necessary',
    "La source entière maintient le versement d'avance, le complément différentiel et les sommes définitivement acquises au parent ; aucun allègement nouveau n'est imputé à ce maintien.",
    "Les conditions d'ouverture de L523-1 et les montants réglementaires restent distincts. Le coût des avances et leur taux de recouvrement ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucune pièce, déclaration de ressources ou contrepartie supplémentaire n'est exigée pour ces avantages.")

put('L581-3', None,
    "Maintien intégral : la demande d'ASF vaut déjà mandat pour le surplus et les autres échéances, ce qui évite un second mandat. L'accord du créancier pour les créances connexes protège son consentement ; la priorité de remboursement des avances évite leur double financement.",
    "Conserver les trois alinéas et les créances civiles des articles 214, 276 et 342, sans en inventer le contenu non fourni dans ce corpus. R581-3 lu maintient le mandat de l'enfant majeur. La note source fixe l'application de la rédaction au 1er avril 2026 : date historique conservée, distincte de l'entrée en vigueur du projet.",
    'retained_necessary',
    "Le mandat déjà fusionné avec la demande est conservé, ainsi que la priorité des avances et le consentement pour les créances connexes ; aucune nouvelle fusion n'est revendiquée.",
    "Les titres et conditions de droit civil restent à leur champ propre, sans modification de la dette entre parents ni des droits d'un enfant majeur.",
    "Aucune charge nouvelle identifiée : pas de mandat additionnel ni de demande périodique ; l'accord existant n'est pas étendu à d'autres créances.")

put('L581-6', None,
    "Maintien intégral de l'aide au recouvrement pour le parent non éligible à l'ASF. La demande exprime le choix du créancier ; elle n'est pas un agrément payant. L'âge limite et l'exigence d'un titre exécutoire protègent le champ de compétence et le débiteur.",
    "L523-1 IV lu confirme la diversité des titres recevables, sans limiter le service aux seuls jugements. Conserver les termes échus et à échoir et la transition au 1er avril 2026 figurant dans la note source. Le renvoi aux articles L581-2 et suivants suit les suppressions de frais et le circuit public simplifié proposés, sans perdre cet accès futur.",
    'retained_necessary',
    "La source entière garantit l'accès au recouvrement même sans droit à l'ASF ; ce maintien favorable n'est pas une nouvelle obligation supprimée.",
    "Le service demeure demandé et suppose un titre exécutoire ainsi que l'âge limite légal ; il n'est pas étendu à toute créance civile ni à tous les âges.",
    "Aucune charge nouvelle identifiée : la demande initiale et les conditions utiles restent identiques, sans justificatif ou visa nouveau.")

put('L581-8', None,
    "Maintien intégral de l'accès aux renseignements nécessaires à l'exécution et de la faculté de les transmettre au créancier pour une créance impayée. Ces pouvoirs circonscrits à la mission évitent des recherches privées et soutiennent l'effectivité des droits des enfants.",
    "Les renvois L152-1 et L152-2 du code des procédures civiles d'exécution demeurent dans leur champ, sans extension d'accès aux données ni suppression implicite de leurs garanties. Leur texte intégral n'est pas fourni ; aucune réécriture de ce code n'est annoncée. La communication vise l'adresse et la solvabilité du débiteur défaillant, pas un fichier général de familles.",
    'retained_necessary',
    "Le dispositif source est intégralement maintenu pour les créances alimentaires impayées ; aucun nouveau partage de données ni gain de conformité n'est créé.",
    "Les garanties du code d'exécution et de protection des données restent applicables ; leur coordination détaillée ne peut être déclarée achevée sur ces seuls alinéas.",
    "Aucune charge nouvelle identifiée : pas de nouveau registre, d'obligation déclarative parentale ou de transmission systématique supplémentaire.")

put('L581-9', None,
    "Maintien intégral de la faculté d'avances sur pensions à partir du fonds d'action sanitaire et sociale et de la subrogation limitée au montant avancé. Ce mécanisme favorable n'impose ni contribution privée ni autorisation préalable nouvelle au créancier.",
    "La loi du 11 juillet 1975 conserve son champ extérieur ; son texte intégral n'est pas présent dans les pièces locales du lot. Ne pas confondre une créance alimentaire ou une avance avec un droit de succession, ni une imputation sur un fonds existant avec une économie budgétaire. Le remboursement d'avance reste coordonné à L581-10.",
    'retained_necessary',
    "La source entière préserve les avances facultatives et leur limite de subrogation, y compris pour les futures situations recevables ; aucune baisse de prélèvement n'est revendiquée.",
    "L'octroi dépend toujours du fonds et du champ de la loi de 1975 ; aucun budget, montant d'avance ou droit automatique illimité n'est créé.",
    "Aucune charge nouvelle identifiée : le financement et les recours subrogatoires restent ceux de la source, sans taxe ni déclaration ajoutée.")

health = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant sa suppression. Pour les prestations afférentes aux périodes commençant à compter de cette entrée en vigueur, la présentation des certificats de santé ne peut plus conditionner le versement de la fraction des allocations familiales et du complément familial afférente à l'enfant n'ayant pas atteint l'âge de l'obligation scolaire. Aucun justificatif ou déclaration de remplacement n'est exigé à ce titre.",
    "Les droits, rappels, restitutions et recours relatifs aux périodes antérieures restent régis par les dispositions qui leur étaient applicables. L'abrogation ne modifie pas les obligations de suivi médical de l'enfant prévues par le code de la santé publique.")
put('L552-2', health,
    "Réforme de fond : suppression de la condition de production des certificats de santé pour le paiement des prestations et du pouvoir de suspendre ou supprimer leur fraction pour un simple retard documentaire. Le suivi médical conserve son fondement autonome ; la sanction sur les ressources de l'enfant n'est pas nécessaire à son maintien.",
    "L584-1 lu est une habilitation générale, qui ne permet pas de rétablir la condition abrogée. L2132-2 du code de la santé publique n'est pas fourni intégralement et n'est pas réécrit ; les examens de santé ne sont pas supprimés. Coordonner les prescriptions d'application et formulaires exclusivement fondés sur L552-2, sans nouvelle attestation. Les périodes antérieures et leurs droits de rappel restent protégés.",
    'material_reduction',
    "La source entière subordonnait potentiellement une fraction de prestations à des certificats et permettait leur suspension ou suppression. Ce mécanisme documentaire disparaît pour les nouvelles périodes, sans remplacer le certificat par une autre déclaration.",
    "Les obligations médicales autonomes et les autres conditions d'ouverture des prestations subsistent. Les économies administratives et effets sur le recours aux soins ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucune déclaration, transmission automatique ou contrôle médical supplémentaire ne remplace la condition supprimée.",
    [effect('obligation_removed','prestations-familiales-fin-certificats-sante',
        "Suppression du certificat de santé comme condition de versement des prestations familiales concernées.",
        "Fraction des allocations familiales et du complément familial des enfants avant l'âge scolaire : paiement conditionnable au certificat, avec suspension ou suppression.",
        "Pour les nouvelles périodes : aucune condition documentaire de santé au titre de cet article ; suivi médical autonome conservé.",
        'legal_duty',"Allocataires pour un enfant avant l'âge de l'obligation scolaire.",
        "Périodes commençant dès l'entrée en vigueur ; droits et contentieux anciens conservés.",
        "Aucune pièce ou déclaration de remplacement.",
        "Le versement de la fraction des allocations familiales et du complément familial, afférent à l'enfant n'ayant pas atteint l'âge de l'obligation scolaire, peut être subordonné à la présentation des certificats de santé établis en application de l'article L. 2132-2 du code de la santé publique.",
        "Aucun justificatif ou déclaration de remplacement n'est exigé à ce titre.")],
    repeal="Suppression pour les périodes nouvelles de la présentation des certificats de santé conditionnant les prestations, de la suspension et de la suppression de leur fraction pour défaut de justification, et de l'habilitation réglementaire propre à ce mécanisme.")

school = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant sa suppression. Pour les prestations familiales afférentes aux périodes commençant à compter de cette entrée en vigueur, leur versement ne peut plus être subordonné, sur son fondement, à la production d'un certificat d'inscription scolaire ou d'une autorisation d'instruction dans la famille. Aucun justificatif ou déclaration de remplacement n'est exigé à ce titre.",
    "Les périodes antérieures restent régies par les dispositions qui leur étaient applicables, y compris les possibilités de paiement rétroactif ou de rétablissement lorsque le retard de production résultait de motifs indépendants de la volonté de l'allocataire. Les obligations d'instruction et les conditions propres à l'allocation de rentrée scolaire ne sont pas modifiées par cette abrogation.")
put('L552-4', school,
    "Réforme de fond : suppression de la production systématique d'une pièce scolaire comme préalable à toutes les prestations familiales et de la privation de versement attachée à son absence. L'obligation d'instruction et les conditions spécifiques de l'allocation de rentrée scolaire subsistent ; aucun circuit déclaratif de substitution n'est créé.",
    "D552-6 lu : ses deux premiers alinéas doivent perdre l'application à L552-4 ; le troisième, propre à L552-5, n'est pas supprimé par cette proposition. Coordonner l'arrêté interministériel de production, non fourni ici. L131-5 éducation reste autonome, hors des codes fournis ; L543-1 lu maintient le champ propre de la rentrée scolaire. La date de rentrée 2022 de la note est historique. Protéger expressément les paiements rétroactifs anciens favorables.",
    'material_reduction',
    "La condition générale de paiement et sa sanction documentaire sont retirées par rapport à la source entière. Il ne s'agit pas d'une simple réutilisation de données déjà détenues : aucune pièce scolaire n'est désormais exigible sur ce fondement.",
    "La scolarisation, l'instruction en famille et les conditions propres à la rentrée scolaire restent régies par leurs textes ; aucune exonération de ces obligations distinctes n'est revendiquée.",
    "Aucune charge nouvelle identifiée : pas de nouvelle déclaration scolaire, d'attestation parentale ou de collecte de remplacement par les caisses.",
    [effect('obligation_removed','prestations-familiales-fin-piece-scolaire',
        "Suppression de la pièce scolaire générale conditionnant le versement des prestations familiales.",
        "Toutes prestations afférentes à l'enfant soumis à l'obligation scolaire : certificat d'inscription ou autorisation exigé avant paiement.",
        "Nouvelles périodes : paiement sans cette production générale ; conditions particulières de rentrée et obligations d'instruction conservées.",
        'legal_duty',"Familles ayant un enfant soumis à l'obligation scolaire.",
        "Périodes nouvelles dès l'entrée en vigueur ; ancien droit au rétablissement pour retard indépendant de la volonté conservé.",
        "Aucune formalité de remplacement.",
        "En l'absence de production effective de l'une de ces pièces, aucune de ces prestations ne peut être versée.",
        "Aucun justificatif ou déclaration de remplacement n'est exigé à ce titre.")],
    repeal="Suppression prospective de la production des certificats d'inscription ou autorisations d'instruction comme condition générale de paiement, de la privation de prestations pour défaut de pièce et des échéances de dépôt propres à ce mécanisme.")

intermediary = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant sa suppression. Le seul fait d'offrir, moyennant des émoluments convenus d'avance, une aide pour obtenir des prestations dues à un allocataire ne constitue plus l'infraction prévue par le présent article.",
    "Aucune poursuite ne peut être engagée ni aucune sanction prononcée sur son fondement pour des faits commis à compter de cette entrée en vigueur. Les faits antérieurs et les condamnations correspondantes bénéficient des règles d'application de la loi pénale plus douce. L'abrogation ne modifie pas les dispositions légales distinctes réprimant la fraude ou l'abus de vulnérabilité, ni les règles propres aux professions réglementées.")
put('L554-2', intermediary,
    "Réforme de fond : suppression de l'incrimination générale de l'aide rémunérée, qui frappe même une assistance loyale visant des prestations effectivement dues. Le seul paiement anticipé d'honoraires ne démontre pas une fraude. Les infractions distinctes et les règles professionnelles protectrices demeurent ; aucune autorisation ou déclaration professionnelle n'est créée à la place.",
    "Le montant source de 4 500 euros disparaît avec l'infraction spéciale. L554-3 est coordonné par une abrogation propre de la publication accessoire. L114-17, lu dans le corpus, maintient notamment la sanction des agissements visant un indu même sans en être bénéficiaire ; aucun droit à une prestation indue n'est ouvert. Les coordinations pénales, de consommation et professionnelles hors corpus restent à examiner dans leurs textes intégraux ; aucune conformité générale n'est affirmée.",
    'material_reduction',
    "La source entière interdisait l'intermédiation rémunérée sans exiger un préjudice ou une fraude ; cette interdiction spéciale et l'amende de 4 500 euros sont retirées. Les sanctions autonomes de comportements frauduleux ne sont pas abrogées.",
    "Le coût d'une assistance privée reste possible et n'est pas une économie pour toute famille. L'existence et l'efficacité des autres protections ne font pas ici l'objet d'une évaluation chiffrée.",
    "Aucune charge nouvelle identifiée : aucune licence, déclaration, rémunération obligatoire ou procédure de substitution n'est instituée.",
    [effect('obligation_removed','prestations-familiales-fin-interdiction-aide-remuneree',
        "Abolition de l'interdiction pénale spéciale de l'aide rémunérée à l'obtention de prestations dues.",
        "Offre de services avec émoluments convenus d'avance : amende spéciale de 4 500 euros, même pour des prestations dues.",
        "Cette seule offre ne constitue plus l'infraction spéciale ; fraudes et règles professionnelles distinctes demeurent.",
        'legal_duty',"Intermédiaires et allocataires recourant à une aide rémunérée.",
        "Abrogation à l'entrée en vigueur ; application des règles pénales plus douces aux faits antérieurs.",
        "Aucun agrément ni déclaration de remplacement.",
        "Sera puni d'une amende de 4 500 euros tout intermédiaire convaincu d'avoir offert ou fait offrir ses services moyennant émoluments convenus d'avance, à un allocataire en vue de lui faire obtenir des prestations qui peuvent lui être dues.",
        "Le seul fait d'offrir, moyennant des émoluments convenus d'avance, une aide pour obtenir des prestations dues à un allocataire ne constitue plus l'infraction prévue par le présent article.")],
    repeal="Suppression de l'incrimination et de l'amende spéciale de 4 500 euros pour l'offre d'assistance rémunérée visant l'obtention de prestations dues, avec application de la loi pénale plus douce aux faits antérieurs.")

publication = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant sa suppression. Aucune insertion d'un jugement aux frais du condamné ne peut être ordonnée sur son fondement à compter de cette date, y compris lorsque son application résultait d'un renvoi d'un autre texte.",
    "Les faits antérieurs et les condamnations correspondantes bénéficient des règles d'application de la loi pénale plus douce. Les restitutions et recours portant sur des sommes indûment perçues restent ouverts ; l'abrogation n'institue pas une restitution générale de frais légalement acquittés. Les mesures de publicité disposant d'un fondement légal distinct ne sont pas modifiées.")
put('L554-3', publication,
    "Réforme de fond : suppression de la peine accessoire d'insertion dans la presse locale aux frais du condamné, plafonnée à 150 euros. La publicité de presse n'est pas indispensable au remboursement des indus ni aux sanctions distinctes de fraude. L'abrogation couvre les applications par renvoi, sans supprimer ces autres régimes.",
    "La note source mentionne l'ancien L843-1 pour les aides à l'emploi de garde et l'article 47 V de l'ordonnance du 27 mars 2002. Ces deux textes ne sont pas fournis intégralement ; leurs renvois à cette seule publicité doivent être coordonnés, sans prétendre abroger leurs prestations ou leurs autres infractions. L554-2 est lui-même abrogé dans ce lot. Les effets sur les condamnations antérieures relèvent des règles pénales plus douces, sans nouvelle règle inventée de remboursement général.",
    'material_reduction',
    "Le pouvoir source d'imposer des frais de publication jusqu'à 150 euros est supprimé dans tout le champ de cet article, y compris ses applications par renvoi ; ce n'est pas la suppression d'une taxe générale.",
    "Aucun montant national économisé n'est établi. Les publicités judiciaires fondées sur d'autres lois et les frais déjà légalement acquittés ne sont pas indistinctement annulés.",
    "Aucune charge nouvelle identifiée : aucune autre publication, notification payante ou déclaration n'est imposée en remplacement.",
    [effect('obligation_removed','prestations-familiales-fin-publication-penale',
        "Suppression de la publication pénale accessoire aux frais du condamné.",
        "Publication possible dans un ou plusieurs journaux locaux, coût à charge du condamné plafonné à 150 euros.",
        "Aucune insertion ordonnée sur ce fondement ; publicité disposant d'une base autonome non modifiée.",
        'euro',"Personnes condamnées dans le champ de L554-3 et de ses renvois.",
        "Dès l'entrée en vigueur, avec application de la loi pénale plus douce aux situations antérieures concernées.",
        "Aucune publication ou dépense de substitution.",
        "En cas de condamnation le tribunal pourra ordonner l'insertion du jugement dans un ou plusieurs journaux de la localité, le tout aux frais du condamné, sans que le coût de l'insertion puisse dépasser 150 euros.",
        "Aucune insertion d'un jugement aux frais du condamné ne peut être ordonnée sur son fondement à compter de cette date, y compris lorsque son application résultait d'un renvoi d'un autre texte.")],
    repeal="Suppression de la peine d'insertion du jugement dans les journaux aux frais du condamné, plafonnée à 150 euros, y compris ses applications par renvoi et sous réserve de la loi pénale plus douce pour les faits antérieurs.")

prescription_source = by_number['L553-1']['source_xml']
old_interruption = "La prescription est interrompue tant que l'organisme débiteur des prestations familiales se trouve dans l'impossibilité de recouvrer l'indu concerné en raison de la mise en œuvre d'une procédure de recouvrement d'indus relevant des articles L. 553-2, L. 821-5-1 ou L. 845-3, L. 844-3 (1) du code de la sécurité sociale, L. 262-46 du code de l'action sociale et des familles ou L. 823-9 du code de la construction et de l'habitation."
new_interruption = "L'impossibilité de recouvrer un indu en raison de la mise en œuvre d'une procédure de recouvrement d'indus ne constitue pas, par elle-même, une cause d'interruption de la prescription. Les autres causes légales d'interruption restent applicables."
assert prescription_source.count(old_interruption) == 1
prescription = prescription_source.replace(old_interruption, new_interruption) + paragraphs(
    "Le troisième alinéa s'applique aux procédures de recouvrement engagées à compter de l'entrée en vigueur de la loi supprimant l'interruption spéciale de prescription. Les interruptions intervenues avant cette entrée en vigueur conservent leurs effets selon les règles antérieures. Les droits et recours de l'allocataire ne sont pas restreints par cette transition.")
put('L553-1', prescription,
    "Réforme de fond : retrait de l'interruption spéciale qui prolongeait la possibilité de recouvrer un indu pendant le recouvrement d'autres indus. Les prescriptions de deux ans, et de cinq ans en cas de fraude ou fausse déclaration, ainsi que les causes légales ordinaires d'interruption sont maintenues. Ce retrait limite une prolongation liée au seul ordonnancement des retenues sans effacer les outils distincts de recouvrement.",
    "Les deux premiers alinéas sont reproduits intégralement. L'ancien troisième alinéa comportait le renvoi incohérent L844-3, expressément corrigé par la note source en L845-3 ; l'ensemble de cette règle spéciale est retiré, et non conservé avec ce renvoi. La transition préserve les interruptions déjà intervenues. L821-5-1, L845-3 et L553-2 fournis confirment les recouvrements croisés ; leur principal, leurs recours et leurs remises ne sont pas supprimés. L262-46 action sociale reste distinct et extérieur au corpus.",
    'material_reduction',
    "Par rapport à la source entière, une cause spéciale d'interruption de prescription est supprimée pour les nouvelles procédures. Cela peut limiter la durée d'exposition au recouvrement ; aucune remise immédiate et générale du principal n'est instituée.",
    "Les deux et cinq ans restent inchangés, les interruptions anciennes sont préservées et d'autres causes légales peuvent encore interrompre la prescription. Aucun montant de créance éteinte n'est chiffré.",
    "Aucune charge nouvelle identifiée : aucun acte de confirmation, déclaration ou demande du débiteur n'est requis pour bénéficier du retrait de la cause spéciale.",
    [effect('relief_extended','indus-familiaux-fin-interruption-speciale',
        "Fin de la prolongation spéciale du recouvrement liée à l'impossibilité de prélever pendant d'autres recouvrements d'indus.",
        "Action de l'organisme : deux ans, cinq en cas de fraude ou fausse déclaration, avec interruption pendant l'impossibilité de recouvrer liée aux recouvrements visés.",
        "Mêmes délais de deux et cinq ans ; l'impossibilité liée au recouvrement d'indus n'est plus, à elle seule, interruptive pour les nouvelles procédures.",
        'other',"Débiteurs d'indus de prestations familiales visés par une nouvelle procédure de recouvrement.",
        "Nouvelles procédures dès l'entrée en vigueur ; effets des interruptions déjà intervenues conservés.",
        "Aucune formalité nouvelle ; causes légales ordinaires inchangées.",
        old_interruption,
        "L'impossibilité de recouvrer un indu en raison de la mise en œuvre d'une procédure de recouvrement d'indus ne constitue pas, par elle-même, une cause d'interruption de la prescription.")],
    removed=["Interruption spéciale de la prescription pendant l'impossibilité de recouvrer un indu du fait de la mise en œuvre des procédures de recouvrement d'indus énumérées au troisième alinéa source."])

family_source = by_number['L553-2']['source_xml']
family_fee = "En contrepartie des frais de gestion qu'il engage lorsque le versement indu est le résultat d'une fraude de l'allocataire, l'organisme payeur recouvre auprès de ce dernier une indemnité équivalant à 10 % des sommes réclamées au titre des prestations versées à tort. Cette indemnité est recouvrée dans les mêmes conditions que les indus recouvrés au titre du présent article."
assert family_source.count(family_fee) == 1
family = family_source.replace(' ' + family_fee, '') + paragraphs(
    "Aucune indemnité de frais de gestion n'est due au titre du présent article pour les versements indus effectués à compter de l'entrée en vigueur de la loi supprimant cette indemnité. Cette suppression ne modifie ni la restitution du principal ni les sanctions de la fraude ayant un fondement légal distinct.",
    "Les versements indus effectués avant cette entrée en vigueur restent régis par les règles qui leur étaient applicables, y compris les garanties de rectification et de recours, les possibilités de réduction ou de remise et les prescriptions, sous réserve de l'application des dispositions répressives plus douces lorsqu'elle est requise. Aucune restitution générale des indemnités légalement acquittées n'est instituée.")
put('L553-2', family,
    "Réforme de fond : suppression pour les nouveaux indus de l'indemnité forfaitaire de gestion de 10 % ajoutée au principal en cas de fraude. Cette surcharge de gestion n'est pas nécessaire à la récupération du principal ni aux sanctions autonomes de fraude de L114-17. Les sept alinéas d'origine restent à leur place, avec le troisième alinéa entier pour les retenues et les renvois extérieurs.",
    "Conserver le remboursement en un versement sur option, le tiers payant, le calcul familial des retenues, la majoration des seules retenues en cas de fraude (plafond 50 %, doublement si réitération dans cinq ans), les prêts et la remise pour précarité hors fraude/fausse déclaration. L133-4-1 fourni : les quatrième à neuvième alinéas organisent rectification et mise en recouvrement différée ; les suivants précisent délais et notification. L821-5-1 et L845-3 gardent leur champ et leurs indemnités propres non supprimées par cet article. L823-9 CCH lu renvoie à L553-2 : coordonner cette exécution de la même mesure sans compter une seconde suppression. La cible fournie L262-1 CSS concerne la prévention, pas le RSA du CASF.",
    'material_reduction',
    "La comparaison à la source officielle entière établit le retrait de la seule indemnité accessoire de 10 % sur les nouveaux indus frauduleux dans le champ de cet article. Principal, barème des retenues, recours et remises favorables sont intégralement conservés.",
    "Les indemnités propres à d'autres articles et les sanctions autonomes ne disparaissent pas. La majoration des retenues accélère le recouvrement sans majorer le principal ; elle reste distincte. Aucun solde national de recettes n'est établi.",
    "Aucune charge nouvelle identifiée : aucun justificatif, délai, registre ou sanction de remplacement n'est créé ; les recouvrements et contrôles existants subsistent.",
    [effect('obligation_removed','indus-familiaux-fin-indemnite-gestion',
        "Retrait de l'indemnité de gestion de 10 % ajoutée aux indus frauduleux de prestations familiales.",
        "Fraude de l'allocataire : principal indu et indemnité de gestion égale à 10 % des prestations réclamées à tort, dans le champ de L553-2.",
        "Nouveaux versements indus : principal récupérable, sans indemnité de gestion sur ce fondement ; sanctions autonomes conservées.",
        'percent',"Allocataires débiteurs d'indus relevant de L553-2 et applications par renvoi dans le même champ.",
        "Indus versés dès l'entrée en vigueur ; stock ancien et garanties conservés, sous réserve du droit répressif plus doux applicable.",
        "Aucune surtaxe ou pénalité de remplacement.",
        "En contrepartie des frais de gestion qu'il engage lorsque le versement indu est le résultat d'une fraude de l'allocataire, l'organisme payeur recouvre auprès de ce dernier une indemnité équivalant à 10 % des sommes réclamées au titre des prestations versées à tort.",
        "Aucune indemnité de frais de gestion n'est due au titre du présent article pour les versements indus effectués à compter de l'entrée en vigueur de la loi supprimant cette indemnité.")],
    removed=["Indemnité forfaitaire de frais de gestion de 10 % des prestations versées à tort en cas de fraude de l'allocataire, et son recouvrement accessoire selon les voies de l'indu."],
    benefit="L'option de remboursement intégral en un versement reste volontaire. Le calcul des retenues selon composition familiale, ressources, logement et prestations exclues reste entier au troisième alinéa. La réduction ou remise pour précarité reste ouverte aux futures situations éligibles, hors manœuvre frauduleuse ou fausse déclaration. Les garanties de rectification de L133-4-1, la condition d'absence d'autre indu sur les prestations subsidiaires, l'accord de l'organisme gestionnaire et les modalités propres à ces prestations sont conservés. Le tiers payant et les prêts ne perdent aucune de ces garanties applicables. La seule surcharge de gestion supprimée n'est remplacée par aucune autre charge.")

service_source = by_number['L553-2-1']['source_xml']
late_fee = "Une majoration de 10 % est applicable aux sommes réclamées qui n'ont pas été réglées aux dates d'exigibilité mentionnées dans la mise en demeure. Cette majoration peut faire l'objet d'une remise."
service_fee = "En contrepartie des frais de gestion qu'il engage lorsque le versement indu est le résultat d'une fraude de l'établissement ou du service, l'organisme débiteur des prestations familiales recouvre auprès de ce dernier une indemnité équivalente à 10 % des sommes réclamées au titre des prestations versées à tort. Cette indemnité est recouvrée dans les mêmes conditions que les indus recouvrés au titre du présent article."
assert service_source.count(late_fee) == 1 and service_source.count(service_fee) == 1
service = service_source.replace(' ' + late_fee, '').replace(service_fee,
    "Aucune majoration de retard ni indemnité de frais de gestion n'est due sur le fondement du présent article pour les versements indus effectués à compter de l'entrée en vigueur de la loi supprimant ces accessoires. La restitution du principal et les sanctions de la fraude ayant un fondement légal distinct demeurent applicables.") + paragraphs(
    "Pour les versements indus effectués avant cette entrée en vigueur, les règles antérieures restent applicables, y compris la possibilité de remise de la majoration de retard, les garanties de procédure et les recours, sous réserve de l'application des dispositions répressives plus douces lorsqu'elle est requise. Aucune restitution générale des accessoires légalement acquittés n'est instituée.")
put('L553-2-1', service,
    "Réforme de fond : suppression de la majoration de retard de 10 % et de l'indemnité de gestion de 10 % des indus réclamés aux établissements et services de garde dans le champ de l'article. La notification, les observations, la mise en demeure d'un mois et la contrainte permettent déjà le recouvrement ; les sanctions distinctes de fraude restent possibles. La dette ne peut toujours pas être refacturée aux parents.",
    "L531-6 lu en entier confirme le champ du dernier alinéa : complément mode de garde en établissement sous capacité et tarif horaire plafonnés. La récupération contre le prestataire n'est pas une suppression de l'aide. Conserver la notification limitée aux sommes initialement réclamées, le tribunal spécialement désigné et l'opposition à contrainte. L553-2 garde son champ général ; ses retenues ne deviennent pas une voie contre les parents pour cet indu spécifique. L211-16 organisation judiciaire et L2324-1 santé publique ne sont pas fournis intégralement et ne sont pas réécrits. L'indemnité de gestion est coordonnée sous la même mesure que L553-2 ; le retrait de la majoration de retard est une mesure distincte.",
    'material_reduction',
    "Deux accessoires effectivement présents dans la source entière sont retirés pour les nouveaux indus : majoration de retard et indemnité de gestion, chacune de 10 % de l'assiette prévue. Le principal, le contradictoire et la protection des parents restent inchangés.",
    "La remise de l'ancienne majoration subsiste pour le stock antérieur, où la charge peut rester due. Les sanctions autonomes, frais d'exécution ayant une autre base et conditions de l'aide ne sont pas supprimés ; aucun coût net global n'est chiffré.",
    "Aucune charge nouvelle identifiée : pas de nouvelle garantie, déclaration ou pénalité. La procédure de notification et d'opposition demeure celle de la source.",
    [effect('coordination','indus-familiaux-fin-indemnite-gestion',
        "Application au recouvrement contre le prestataire de la suppression de l'indemnité de gestion des indus familiaux.",
        "Fraude de l'établissement ou du service : indemnité de gestion de 10 % des prestations réclamées à tort en plus du principal.",
        "Nouveaux versements indus : absence d'indemnité de gestion dans ce régime particulier ; principal contre le prestataire maintenu.",
        'percent',"Établissements et services relevant de L553-2-1.",
        "Même bascule selon la date des versements indus ; anciens droits et loi répressive plus douce réservés.",
        "Aucun accessoire de remplacement ; une seule famille de mesure de suppression de frais de gestion.",
        "En contrepartie des frais de gestion qu'il engage lorsque le versement indu est le résultat d'une fraude de l'établissement ou du service, l'organisme débiteur des prestations familiales recouvre auprès de ce dernier une indemnité équivalente à 10 % des sommes réclamées au titre des prestations versées à tort.",
        "Aucune majoration de retard ni indemnité de frais de gestion n'est due sur le fondement du présent article pour les versements indus effectués à compter de l'entrée en vigueur de la loi supprimant ces accessoires."),
     effect('obligation_removed','indus-garde-fin-majoration-retard',
        "Suppression de la majoration de retard propre aux indus de garde réclamés aux établissements et services.",
        "Majoration de 10 % des sommes réclamées non réglées aux dates d'exigibilité de la mise en demeure, avec faculté de remise.",
        "Pour les nouveaux versements indus : aucune majoration de retard sur ce fondement, même principal et mêmes dates de paiement.",
        'percent',"Établissements et services débiteurs d'indus dans le champ de L553-2-1.",
        "Versements indus effectués dès l'entrée en vigueur ; remise des anciennes majorations conservée.",
        "Aucune nouvelle pénalité ou condition d'aide.",
        "Une majoration de 10 % est applicable aux sommes réclamées qui n'ont pas été réglées aux dates d'exigibilité mentionnées dans la mise en demeure.",
        "Aucune majoration de retard ni indemnité de frais de gestion n'est due sur le fondement du présent article pour les versements indus effectués à compter de l'entrée en vigueur de la loi supprimant ces accessoires.")],
    removed=["Majoration de retard de 10 % sur les sommes non réglées aux dates d'exigibilité de la mise en demeure, pour les nouveaux versements indus.",
             "Indemnité de frais de gestion de 10 % du montant des prestations versées à tort en cas de fraude de l'établissement ou du service, pour les nouveaux versements indus."],
    benefit="La dérogation à L553-2 qui fait supporter l'indu au prestataire reste entière et continue de protéger les parents pour les futures situations éligibles : aucune refacturation de l'indu n'est permise. Le mois accordé par la mise en demeure, les observations, la limitation aux sommes déjà notifiées et l'opposition au tribunal sont conservés. La faculté de remise de la majoration de 10 % est expressément maintenue pour les anciens indus qui restent soumis à cette majoration ; pour les nouveaux, elle devient sans objet parce que la majoration correspondante est entièrement supprimée, sans prélèvement de remplacement. L'indemnité de fraude de 10 % est également retirée, tandis que le principal demeure dû par le prestataire.")

asf_source = by_number['L581-4']['source_xml']
old_suspend = "L'organisme débiteur de prestations familiales peut suspendre le versement de l'allocation de soutien familial en cas de refus par le créancier d'aliments de donner le pouvoir spécial de saisie en matière immobilière."
new_suspend = "Le refus du créancier d'aliments de donner un pouvoir spécial de saisie en matière immobilière ne peut entraîner la suspension du versement de l'allocation de soutien familial. Ce pouvoir n'est pas présumé donné du fait du maintien de l'allocation."
assert asf_source.count(old_suspend) == 1
asf = asf_source.replace(old_suspend, new_suspend) + paragraphs(
    "Le troisième alinéa s'applique aux allocations dues au titre des périodes commençant à compter de l'entrée en vigueur de la loi supprimant cette cause de suspension, y compris lorsque le refus ou la suspension est antérieur. Les droits et recours relatifs aux périodes antérieures sont conservés selon les règles qui leur étaient applicables.")
put('L581-4', asf,
    "Réforme de fond : retrait de la suspension d'ASF destinée à obtenir du parent créancier un pouvoir de saisie immobilière. L'accès à une ressource de subsistance ne doit pas dépendre de ce choix de procédure patrimoniale. L'obligation de communiquer les renseignements utiles, la renonciation libre à l'ASF et la subrogation restent entières ; aucun pouvoir de saisie n'est attribué d'office.",
    "Conserver les quatre alinéas d'origine et l'exception d'intermédiation de L582-1. L'accord de l'organisme pour le paiement direct reste nécessaire à la cohérence de sa subrogation et n'est pas supprimé avec le pouvoir spécial. R581-1 et R581-4 lus restent distincts ; les informations utiles ne sont pas une nouvelle déclaration créée ici. L523-1 et L581-2 conservent l'ASF et les avances. La date du 1er mars 2022 de la note est historique. Les suspensions anciennes cessent de priver de l'ASF pour les périodes nouvelles sur ce seul motif.",
    'material_reduction',
    "La source entière permettait une suspension d'ASF pour refus d'autoriser la saisie immobilière ; cette contrainte disparaît effectivement. Le droit futur au maintien est ouvert également aux parents déjà suspendus sur ce seul motif.",
    "Les autres conditions d'ASF, la subrogation et les procédures légales d'exécution restent en place. Aucun rappel automatique pour les périodes anciennes ni coût budgétaire chiffré n'est créé.",
    "Aucune charge nouvelle identifiée : aucun mandat, attestation ou autorisation de remplacement ; le maintien de l'ASF n'emporte pas consentement à la saisie.",
    [effect('obligation_removed','asf-fin-pression-saisie-immobiliere',
        "Fin du conditionnement du maintien de l'ASF à un pouvoir spécial de saisie immobilière.",
        "Refus du créancier de donner le pouvoir : suspension possible de l'ASF.",
        "Refus sans suspension sur ce seul motif ; consentement à la saisie toujours nécessaire selon les règles propres à celle-ci.",
        'legal_duty',"Créanciers d'aliments bénéficiaires de l'ASF, y compris suspensions déjà décidées pour les périodes nouvelles.",
        "Prestations des nouvelles périodes dès l'entrée en vigueur ; contentieux et droits anciens préservés.",
        "Aucun pouvoir présumé ni mandat de remplacement.",
        old_suspend,
        "Le refus du créancier d'aliments de donner un pouvoir spécial de saisie en matière immobilière ne peut entraîner la suspension du versement de l'allocation de soutien familial.")],
    removed=["Pouvoir de suspendre l'allocation de soutien familial au seul motif que le créancier refuse de conférer un pouvoir spécial de saisie en matière immobilière."])

fees = paragraphs(
    "Sauf dans le cas où il est fait application du premier alinéa de l'article 7 de la loi n° 75-618 du 11 juillet 1975 relative au recouvrement public des pensions alimentaires, les sommes à recouvrer par l'organisme débiteur ne sont assorties d'aucune majoration au titre de ses frais de gestion et de recouvrement. Les frais effectivement payés aux officiers ministériels et aux auxiliaires de justice ne peuvent pas davantage être ajoutés à ces sommes sur le fondement du présent article.",
    "Ces frais ne peuvent être mis à la charge du créancier d'aliments.",
    "Ces dispositions s'appliquent aux frais afférents aux actes de gestion et de recouvrement accomplis à compter de l'entrée en vigueur de la loi supprimant ces majorations, quelle que soit la date de la créance alimentaire ou de l'avance. Aucune majoration ne peut être créée sur leur fondement pour ces actes. Les frais légalement nés à raison d'actes antérieurs, les exonérations applicables, les restitutions, les prescriptions et les recours demeurent régis par les dispositions antérieures.",
    "Les frais dus sur un fondement légal distinct dans le cadre du recouvrement public mentionné au premier alinéa conservent leur régime. La suppression prévue au présent article n'autorise aucun transfert de frais vers le créancier d'aliments.")
put('L581-5', fees,
    "Réforme de fond : suppression de la majoration de gestion et de recouvrement de l'organisme et du remboursement accessoire de frais d'auxiliaires sur ce seul fondement. L'interdiction de faire payer le créancier reste entière ; il ne s'agit donc pas d'une abrogation intégrale. L'exception du recouvrement public autonome est conservée sans extension à un frais de remplacement.",
    "R581-6 à R581-8 lus dans le corpus : 7,5 % et frais effectivement payés aux officiers ministériels et auxiliaires, plus 2,5 % sans leur intervention, voies de recouvrement et affectation administrative. Coordonner leur retrait pour les actes nouveaux sous cette même mesure ; ces règlements ne sont pas modifiés dans ce dossier. La loi du 11 juillet 1975, notamment article 7, n'est pas fournie intégralement : ses frais autonomes ne sont pas déclarés abolis, et son exception favorable est maintenue. Le principal alimentaire et les avances restent récupérables. Perte de recettes administratives et financement du service à évaluer, sans compensation inventée.",
    'material_reduction',
    "La source entière imposait des frais de gestion et de recouvrement ; la proposition retire les majorations et frais fondés sur cet article pour les nouveaux actes. Elle préserve la gratuité pour le créancier et l'exception du recouvrement public distinct.",
    "Le règlement lu prévoit 7,5 %, avec 2,5 % supplémentaires en l'absence d'auxiliaire, et des frais réels. Les frais autonomes du recouvrement public et le stock d'actes anciens restent hors de cette coupe ; le solde public net demeure inconnu.",
    "Aucune charge nouvelle identifiée : aucune déclaration, frais de substitution ou contribution du créancier. La perte de recettes de gestion n'est pas transformée en taxe compensatoire.",
    [effect('obligation_removed','creances-alimentaires-fin-frais-organisme',
        "Retrait des majorations de frais de gestion et de recouvrement fondées sur L581-5.",
        "Sommes recouvrées hors exception du recouvrement public : majorations fixées par décret ; R581-6 prévoit 7,5 % et frais réels, plus 2,5 % en l'absence d'auxiliaire.",
        "Nouveaux actes : aucune majoration ni ajout de frais réels sur le fondement de cet article ; créance alimentaire et frais légaux autonomes inchangés.",
        'legal_duty',"Débiteurs de créances alimentaires recouvrées par les organismes dans le champ de L581-5.",
        "Actes accomplis dès l'entrée en vigueur même sur une créance ancienne ; droits et recours sur anciens frais conservés.",
        "Aucun frais de remplacement ni transfert autorisé au créancier ; financement public du service non chiffré.",
        "Sauf dans le cas où il est fait application du premier alinéa de l'article 7 de la loi n° 75-618 du 11 juillet 1975 relative au recouvrement public des pensions alimentaires, les sommes à recouvrer par l'organisme débiteur sont majorées de frais de gestion et de recouvrement dont le montant est fixé par décret en Conseil d'Etat.",
        "Sauf dans le cas où il est fait application du premier alinéa de l'article 7 de la loi n° 75-618 du 11 juillet 1975 relative au recouvrement public des pensions alimentaires, les sommes à recouvrer par l'organisme débiteur ne sont assorties d'aucune majoration au titre de ses frais de gestion et de recouvrement.")],
    removed=["Majorations forfaitaires de gestion et de recouvrement fixées par décret pour les sommes recouvrées par l'organisme, hors exception autonome de recouvrement public.",
             "Ajout au montant recouvré des frais effectivement payés aux officiers ministériels et auxiliaires de justice sur le seul fondement de cet article et de ses règlements d'application."])

executory = paragraphs(
    "Par dérogation aux articles 2 et 3 de la loi n° 75-618 du 11 juillet 1975, le directeur de l'organisme débiteur de prestations familiales intervenant au titre des articles L. 581-2 et suivants établit et certifie l'état des sommes à recouvrer. Sa signature rend cet état exécutoire. Il l'adresse directement au directeur départemental des finances publiques du département, sans visa ni transmission par le représentant de l'Etat dans le département. Les règles de contestation et les garanties du recouvrement public restent applicables.",
    "Ces dispositions s'appliquent aux états établis et certifiés à compter de l'entrée en vigueur de la loi supprimant le visa préfectoral. Les états établis et certifiés auparavant conservent le régime qui leur était applicable, notamment le délai de cinq jours ouvrables imparti au représentant de l'Etat ; aucun nouvel état ni nouveau dossier n'est exigé pour les sommes déjà régulièrement transmises.")
put('L581-7', executory,
    "Réforme de fond : suppression du visa exécutoire préfectoral et du détour de transmission pour un état déjà établi et certifié par le directeur. La signature de ce dernier suffit et l'envoi devient direct aux finances publiques, sans nouvelle demande du créancier ni du débiteur. Les contestations et garanties du recouvrement public demeurent.",
    "L581-10 est coordonné dans ce lot pour les avances, l'arrêt des poursuites parallèles et la clôture du recouvrement ; même mesure, pas une seconde suppression. Le délai source de cinq jours ouvrables était un maximum imposé au préfet, non une attente minimale : ne pas revendiquer un gain automatique de cinq jours. Articles 2, 3 et 4 de la loi du 11 juillet 1975 extérieurs au corpus à coordonner et à contrôler intégralement ; aucun recours n'est retiré. Les anciens états gardent leur délai et leur validité sans réédition.",
    'material_reduction',
    "La source entière imposait une certification par l'organisme puis une intervention préfectorale pour donner force exécutoire et transmettre. Le second visa et ce relais disparaissent, sans supprimer le titre, la certification ou le contrôle juridictionnel.",
    "L'état reste nécessaire au recouvrement public ; son caractère exécutoire est attribué à la signature déjà requise du directeur. Les recours extérieurs restent applicables ; aucun délai effectif économisé ni coût net n'est chiffré.",
    "Aucune charge nouvelle identifiée : la signature, la certification et l'envoi existent déjà ; un envoi direct remplace le relais préfectoral sans dossier ou attestation supplémentaire. Aucun nouveau pouvoir de collecte de données n'est ajouté.",
    [effect('authorization_removed','creances-alimentaires-fin-visa-prefectoral',
        "Suppression du visa préfectoral donnant force exécutoire aux états de créances alimentaires et du relais de transmission.",
        "État établi et certifié par le directeur, adressé au préfet qui le rend exécutoire sous cinq jours ouvrables et le transmet aux finances publiques.",
        "État exécutoire par la signature du directeur, transmission directe aux finances publiques ; garanties et contestations conservées.",
        'legal_duty',"Organismes de prestations familiales, autorités de recouvrement et familles concernées.",
        "États établis et certifiés dès l'entrée en vigueur ; anciens états et délai maximum de cinq jours ouvrables protégés.",
        "Aucune démarche privée de remplacement ; même état certifié et signé, destinataire direct modifié.",
        "Celui-ci rend cet état exécutoire dans un délai de cinq jours ouvrables et le transmet au directeur départemental des finances publiques du département.",
        "Sa signature rend cet état exécutoire.")],
    removed=["Intervention du représentant de l'Etat pour rendre exécutoire l'état déjà établi et certifié par le directeur de l'organisme de prestations familiales.",
             "Transmission obligatoire de l'état de l'organisme au préfet puis de celui-ci au directeur départemental des finances publiques, remplacée par un seul envoi direct du même état."],
    benefit="La dérogation aux articles 2 et 3 de la loi de 1975, qui facilite le recouvrement public pour les familles, reste explicite et ouverte aux futurs états éligibles. Le maximum de cinq jours ouvrables protégeait le créancier contre un retard de visa préfectoral ; pour les nouveaux états ce visa disparaît et la force exécutoire résulte immédiatement de la signature du directeur, sans nouvelle attente ni agrément. Le délai de cinq jours est expressément conservé pour les états anciens soumis à l'ancien circuit. Les recours et garanties du recouvrement public sont réservés, et aucun nouveau dossier n'est demandé pour les sommes déjà transmises.")

advance_source = by_number['L581-10']['source_xml']
advance_old_2 = "Le directeur de l'organisme débiteur de prestations familiales établit et certifie l'état des sommes à recouvrer et l'adresse au représentant de l'Etat dans le département. Celui-ci rend cet état exécutoire dans un délai de cinq jours ouvrables et le transmet au directeur départemental des finances publiques."
advance_new_2 = "Le directeur de l'organisme débiteur de prestations familiales établit et certifie l'état des sommes à recouvrer. Sa signature rend cet état exécutoire. Il l'adresse directement au directeur départemental des finances publiques, sans visa ni transmission par le représentant de l'Etat dans le département."
advance_old_3 = "Dès qu'ils ont saisi le représentant de l'Etat dans le département, les organismes débiteurs de prestations familiales ne peuvent plus, jusqu'à ce qu'ils soient informés de la cessation de la procédure de recouvrement par les comptables publics compétents, exercer aucune action en vue de récupérer les sommes qui font l'objet de leur demande."
advance_new_3 = "Dès qu'ils ont transmis l'état exécutoire au directeur départemental des finances publiques, les organismes débiteurs de prestations familiales ne peuvent plus, jusqu'à ce qu'ils soient informés de la cessation de la procédure de recouvrement par les comptables publics compétents, exercer aucune action en vue de récupérer les sommes qui font l'objet de leur demande."
advance_old_7 = "En cas de décès du débiteur ou lorsque l'impossibilité de recouvrer la créance a été constatée par le comptable public compétent, ce dernier renvoie le titre exécutoire à la caisse d'allocations familiales qui en décharge le comptable public et informe de sa décision le représentant de l'Etat dans le département."
advance_new_7 = "En cas de décès du débiteur ou lorsque l'impossibilité de recouvrer la créance a été constatée par le comptable public compétent, ce dernier renvoie le titre exécutoire à la caisse d'allocations familiales qui en décharge le comptable public."
advance = advance_source
for before, after in [(advance_old_2, advance_new_2),(advance_old_3,advance_new_3),(advance_old_7,advance_new_7)]:
    assert advance.count(before) == 1
    advance = advance.replace(before, after)
advance += paragraphs(
    "Les deuxième, troisième et septième alinéas s'appliquent aux états établis et certifiés à compter de l'entrée en vigueur de la loi supprimant le visa préfectoral. Les états établis et certifiés avant cette date conservent le régime qui leur était applicable, y compris le délai de cinq jours ouvrables, la suspension des actions parallèles et l'information du représentant de l'Etat. Aucun nouvel état ni nouveau dossier n'est exigé pour les sommes déjà régulièrement transmises.")
put('L581-10', advance,
    "Coordination nécessaire de la suppression du visa préfectoral décidée dans L581-7 : état exécutoire par la signature du directeur et envoi direct aux finances publiques. Le déclencheur d'arrêt des poursuites parallèles devient cet envoi et l'information finale du préfet est retirée du nouveau circuit. Les huit alinéas d'origine sont conservés à leur rang ; les autres règles restent intégrales.",
    "Conserver les contestations de l'article 4 et les procédures des articles 7 à 9 de la loi de 1975, les actions et garanties du créancier, la priorité des avances et l'extension à toute la créance de L581-2 à L581-5. R581-10 lu confirme les comptables de la DGFiP ; pas de nouvelle catégorie de comptable. Les états anciens gardent cinq jours ouvrables et les anciennes notifications. Le décès du débiteur n'est pas un impôt de succession et le renvoi du titre n'est pas une remise générale de dette. Les textes extérieurs de 1975 restent à coordonner dans leur champ propre.",
    'coordination_only',
    "La source entière est coordonnée au circuit sans visa préfectoral de L581-7, sous la même clé de mesure. Le retrait du relais et de son information finale n'est pas compté comme une seconde procédure générale supprimée.",
    "Les règles d'exécution, contestation, priorité et clôture demeurent ; les anciens états conservent leur circuit. Aucun délai global de recouvrement ni économie supplémentaire n'est démontré.",
    "Aucune charge nouvelle identifiée : mêmes états, signatures et informations de fond ; l'envoi direct remplace les relais. L'interdiction d'actions parallèles empêche un double recouvrement sans nouvelle pièce à fournir.",
    [effect('coordination','creances-alimentaires-fin-visa-prefectoral',
        "Coordination des avances avec l'état exécutoire direct et de l'arrêt des actions parallèles avec sa transmission.",
        "Visa et transmission par le préfet, arrêt des actions dès sa saisine et information du préfet à la décharge du comptable.",
        "État rendu exécutoire par signature du directeur et transmission directe ; arrêt des actions dès cet envoi, sans information finale du préfet dans le nouveau circuit.",
        'legal_duty',"Organismes et comptables recouvrant les avances et les créances alimentaires du champ de L581-10.",
        "Nouveaux états dès l'entrée en vigueur ; anciens états et leurs garanties conservés sans réédition.",
        "Aucun nouveau dossier ; attribution différente d'une transmission existante.",
        "Celui-ci rend cet état exécutoire dans un délai de cinq jours ouvrables et le transmet au directeur départemental des finances publiques.",
        "Sa signature rend cet état exécutoire.")],
    removed=["Visa exécutoire et relais préfectoral de transmission de l'état des avances, en coordination avec la même suppression dans L581-7.",
             "Information du préfet à la décharge du comptable public pour les nouveaux états, devenue sans objet avec la suppression de son intervention dans le circuit."])

intermediation_source = by_number['L582-1']['source_xml']
penalty_old_2 = "Fait l'objet d'une pénalité prononcée par le directeur de l'organisme débiteur des prestations familiales, le refus du parent débiteur ou le silence gardé par lui de transmettre les informations mentionnées au premier alinéa du présent II."
penalty_new_2 = "Aucune pénalité pécuniaire ne peut être prononcée sur le seul fondement du présent II pour le refus ou le silence du parent débiteur de transmettre les informations mentionnées au premier alinéa. Les sanctions disposant d'un fondement légal distinct ne sont pas modifiées par cette disposition."
penalty_old_3 = "Les délais de transmission des informations mentionnées au même premier alinéa, la procédure contradictoire applicable ainsi que le montant de la pénalité, qui ne peut excéder le montant de la base mensuelle de calcul des allocations familiales fixé en application de l'article L. 551-1, et ses modalités de recouvrement sont fixés par décret."
penalty_new_3 = "Les délais de transmission des informations mentionnées au premier alinéa du présent II et la procédure contradictoire applicable sont fixés par décret. Le recouvrement de la pension alimentaire ne peut être subordonné à la notification, au paiement ou au recouvrement d'une pénalité supprimée par le présent article."
assert intermediation_source.count(penalty_old_2) == 1 and intermediation_source.count(penalty_old_3) == 1
intermediation = intermediation_source.replace(penalty_old_2,penalty_new_2).replace(penalty_old_3,penalty_new_3) + paragraphs(
    "La suppression de la pénalité prévue au II s'applique aux manquements commis à compter de l'entrée en vigueur de la loi portant cette suppression, y compris dans les intermédiations déjà en cours. Pour les faits antérieurs, les garanties, prescriptions et recours restent applicables, sous réserve des règles d'application des dispositions répressives plus douces. Aucun dossier d'intermédiation régulièrement ouvert n'est à déposer de nouveau.")
put('L582-1', intermediation,
    "Réforme de fond : suppression de la pénalité autonome pour silence ou refus d'information, de son montant et de son recouvrement. L'obligation de transmettre les informations nécessaires et le recouvrement de la pension en cas de défaut demeurent ; ils assurent le service sans cet accessoire punitif supplémentaire. Tous les I à IX, leurs exceptions de violences et les garanties de pension restent intégraux hors cette coupe ciblée du II.",
    "D582-2 lu en entier : délai initial quinze jours, rappel dix jours, pénalité réglementaire de 25 % de la base mensuelle arrondie à l'euro supérieur, mise en demeure huit jours, recouvrement et affectation administrative. Coordonner la suppression des seuls volets de pénalité et du couplage de la pension à leur attente ; conserver les délais propres et le contradictoire utiles au recouvrement. R582-7 lu conserve revalorisation, choix du jour et reversement au plus tard le lendemain ou le jour ouvré suivant ; R582-11 reste pour les pensions versées à tort. Le neuvième alinéa du I reste au même emplacement. La note d'application de la loi de 2021 n'est pas une date future. Les renvois au code civil, CPCE et LPF non fournis entièrement ne sont pas réécrits.",
    'material_reduction',
    "La comparaison avec la source entière établit la suppression de la pénalité propre au II et de son circuit accessoire, sans abolir le recouvrement dès le premier impayé, les informations nécessaires ni la protection contre les violences. La même pension reste due.",
    "Le plafond législatif était une base mensuelle et le taux d'exécution lu est 25 % de cette base. Les sanctions autonomes de fraude ou d'obstruction légalement caractérisées demeurent dans leur champ ; les coûts et délais nets ne sont pas chiffrés.",
    "Aucune charge nouvelle identifiée : aucune déclaration, sanction ou pièce de remplacement. Les informations, le contradictoire et les délais de recouvrement déjà exigés restent ; aucune nouvelle attente de paiement de pénalité n'est créée.",
    [effect('obligation_removed','intermediation-alimentaire-fin-penalite-information',
        "Suppression de la pénalité spéciale pour refus ou silence sur les informations d'intermédiation.",
        "Refus ou silence du parent débiteur : pénalité législativement plafonnée à une base mensuelle d'allocations ; D582-2 fixe 25 % de cette base, arrondi à l'euro supérieur.",
        "Nouveaux manquements : aucune pénalité fondée sur ce II ; information nécessaire et recouvrement de la pension conservés sans dépendre du paiement d'un accessoire supprimé.",
        'legal_duty',"Parents débiteurs soumis à l'intermédiation financière et organismes chargés de son exécution.",
        "Manquements commis dès l'entrée en vigueur, y compris dossiers en cours ; application du droit répressif plus doux réservée pour les faits anciens.",
        "Aucune pénalité ou démarche de remplacement ; sanctions autonomes inchangées.",
        penalty_old_2,
        "Aucune pénalité pécuniaire ne peut être prononcée sur le seul fondement du présent II pour le refus ou le silence du parent débiteur de transmettre les informations mentionnées au premier alinéa.")],
    removed=["Pénalité pécuniaire autonome prononcée contre le parent débiteur qui refuse ou omet de transmettre les informations nécessaires à l'intermédiation.",
             "Habilitation à fixer le montant et les modalités de recouvrement de cette pénalité, ainsi que la dépendance du recouvrement alimentaire à l'attente d'un accessoire supprimé."])

agreement_source = by_number['L582-2']['source_xml']
nullity_old = "Lorsque l'information mentionnée au 1° du présent article n'a pas été portée à la connaissance de l'organisme débiteur, la décision de ce dernier est frappée de nullité."
nullity_new = "Lorsque l'information mentionnée au 1° du présent article n'a pas été portée à la connaissance de l'organisme débiteur, la décision de ce dernier n'est frappée de nullité sur ce seul fondement que si l'une des conditions prévues au même 1° n'était pas réunie lors de sa délivrance. Le seul défaut de transmission de cette information n'entraîne pas la nullité lorsque ces conditions étaient réunies."
reporting_old = "Les parents sont tenus de signaler à l'organisme débiteur tout changement de situation susceptible d'entraîner la révision du montant de la contribution. "
assert agreement_source.count(nullity_old) == 1 and agreement_source.count(reporting_old) == 1
agreement_old_asf = "Lorsque ce changement entraîne une modification du droit à l'allocation mentionnée au 4° du I de l'article L. 523-1 du présent code, les parents qui ont conclu un nouvel accord le transmettent à l'organisme débiteur en vue du maintien de cette allocation."
agreement_new_asf = "Lorsqu'un changement de situation entraîne une modification du droit à l'allocation mentionnée au 4° du I de l'article L. 523-1 du présent code, les parents qui ont conclu un nouvel accord le transmettent à l'organisme débiteur en vue du maintien de cette allocation."
assert agreement_source.count(agreement_old_asf) == 1
agreement = agreement_source.replace(nullity_old,nullity_new).replace(reporting_old,'').replace(agreement_old_asf, agreement_new_asf) + paragraphs(
    "La suppression de l'obligation générale de signaler les changements de situation s'applique à compter de l'entrée en vigueur de la loi portant cette suppression, y compris aux titres déjà délivrés. Elle ne modifie pas les obligations déclaratives ayant un fondement légal distinct pour le service des prestations familiales. La règle excluant la nullité fondée sur le seul défaut formel d'information lorsque les conditions de fond étaient réunies s'applique aux titres délivrés à compter de cette entrée en vigueur et aux contestations en cours relatives aux titres antérieurs, sans remettre en cause les décisions juridictionnelles devenues irrévocables. Les droits et créances antérieurs, la faculté de saisir le juge et l'effet des décisions judiciaires postérieures demeurent préservés.")
put('L582-2', agreement,
    "Réforme de fond : retrait du signalement général de tout changement susceptible de justifier une révision de la pension, sans modification du titre, et retrait de la nullité attachée au seul défaut formel d'information lorsque l'absence de titre ou démarche concurrente était réelle. La transmission du nouvel accord nécessaire au maintien de l'ASF différentielle reste entière. La demande conjointe, l'attestation initiale et les conditions substantielles du titre sont conservées.",
    "L523-1 IV lu confirme les titres concurrents visés aux 1°, 2°, 4° et 5° ; le 3° correspond au titre de ce même L582-2. R582-2 lu conserve la signature des deux parents, la convention et l'attestation ; la coupe de nullité n'est pas une dispense de fournir les pièces au premier dépôt. R582-1 et D582-1 lus : préserver le seuil, le minimum de ressources laissé au débiteur, ses formules et les enfants pris en compte, sans créer de taux ni toucher aux minorations favorables. La voie du juge aux affaires familiales, le caractère exécutoire CPCE L111-3 6° et la primauté du jugement postérieur restent tels que la source les prévoit ; les textes extérieurs ne sont pas déclarés réécrits. L'absence de recours contre la décision de l'organisme demeure avec la saisine du juge expressément conservée : ce point de structure de la source n'est pas présenté comme un nouvel accès au recours.",
    'material_reduction',
    "La source entière imposait un signalement général même sans nouvel accord ni modification effective d'ASF et annulait le titre pour une information manquante malgré des conditions matériellement réunies. Ces deux contraintes sont réduites ; les conditions de fond, le consentement et les informations utiles au maintien de l'allocation demeurent.",
    "Aucune réduction de la pension due ni du seuil réglementaire n'est décidée. Les obligations déclaratives autonomes de prestations, les titres incompatibles et les décisions judiciaires irrévocables restent hors de cette coupe.",
    "Aucune charge nouvelle identifiée : l'attestation initiale et le nouvel accord pour l'ASF existaient déjà. Aucune déclaration de remplacement, vérification périodique ou demande de régularisation obligatoire n'est ajoutée.",
    [effect('obligation_removed','titre-alimentaire-fin-signalement-general',
        "Suppression du signalement général de changements seulement susceptibles de conduire à une révision du titre.",
        "Tous changements susceptibles de réviser la contribution à signaler, même sans nouvel accord ; nouvel accord à transmettre lorsque le droit à l'ASF est modifié.",
        "La déclaration générale de changement est retirée ; transmission du nouvel accord nécessaire au maintien de l'ASF et obligations autonomes de prestations conservées.",
        'legal_duty',"Parents titulaires d'un accord rendu exécutoire par l'organisme familial.",
        "Dès l'entrée en vigueur, y compris titres existants, sans modifier les créances et décisions judiciaires.",
        "Aucune déclaration de substitution ; les obligations distinctes pour les prestations restent à leur champ.",
        reporting_old.rstrip(),
        agreement_new_asf),
     effect('relief_extended','titre-alimentaire-fin-nullite-purement-formelle',
        "Protection du titre contre la nullité fondée uniquement sur une information omise lorsque les conditions matérielles étaient réunies.",
        "Omission de l'information du 1° : nullité de la décision même sans titre ou démarche concurrente.",
        "Omission seule insuffisante pour annuler si les conditions du 1° étaient effectivement réunies à la délivrance ; conditions substantielles inchangées.",
        'legal_duty',"Parents et enfants bénéficiaires d'un titre alimentaire délivré par l'organisme.",
        "Nouveaux titres et contestations en cours dès l'entrée en vigueur, sans remise en cause des jugements irrévocables.",
        "Aucune condition nouvelle : absence réelle de titre concurrent déjà exigée par le 1°.",
        nullity_old,
        "Le seul défaut de transmission de cette information n'entraîne pas la nullité lorsque ces conditions étaient réunies.")],
    removed=["Obligation générale faite aux parents de signaler tout changement seulement susceptible d'entraîner la révision de la contribution, sans nouveau titre ni nouvel accord requis pour l'ASF.",
             "Nullité automatique de la décision pour le seul défaut de transmission de l'information du 1°, lorsque les conditions de fond de ce 1° étaient réunies lors de sa délivrance."])

work_context = {
 'L552-7': "L552-7 maintient les prestations après le décès d'un enfant, y compris la rentrée scolaire ; il ne régit aucune rupture d'emploi du parent ou de l'apprenti.",
 'L553-1': "L553-1 règle la prescription du paiement et des indus familiaux ; les deux et cinq ans ne sont ni une ancienneté d'emploi ni un délai de notification de licenciement.",
 'L553-2': "L553-2 règle les indus et les retenues sociales ; l'indemnité de gestion de 10 % supprimée n'est pas l'indemnité de rupture du contrat d'un allocataire.",
 'L553-2-1': "L553-2-1 récupère un indu de complément de garde contre un établissement ou service ; ce dernier n'est pas licencié et le mois de mise en demeure concerne sa dette.",
 'L553-4': "L553-4 protège les prestations contre cession et saisie ; les retenues qu'il autorise pour les enfants ne sont pas le préavis ou l'indemnité de rupture d'un emploi.",
 'L553-5': "L553-5 évalue les ressources en cas de disproportion du train de vie ; il ne définit ni la durée d'un contrat ni l'indemnité de cessation d'emploi."
}
work_assessments = {
 'L1234-1': "La source de L1234-1 fixe un préavis de licenciement selon l'ancienneté et hors faute grave ; sa proposition prévoit quinze jours calendaires pour les nouveaux contrats et conserve les anciens régimes. Aucun renvoi de cet article familial ne vise ce préavis : aucune transposition, aucune modification d'ancienneté ou de notification, et aucune suppression de procédure collective n'en résulte.",
 'L1221-2': "La source de L1221-2 admet des CDD par exception au CDI ; sa proposition ferme les nouvelles embauches à terme, conserve les contrats antérieurs et distingue la durée d'une formation de celle de l'emploi. Le champ de cet article familial est autonome : aucun CDD n'est créé, aucune aide future n'est réservée aux anciens contrats et aucun critère d'ancienneté ou de notification d'emploi n'est ajouté.",
 'L1234-9': "La source de L1234-9 ouvre l'indemnité après huit mois, hors faute grave ; sa proposition vise un an au terme effectif préavis inclus, 0,20 mois sur l'ancienneté totale, mois complets et plafond six mois, employeur seul, avec transition et indemnités spéciales distinctes. Cet article familial ne renvoie pas à cette indemnité : il n'importe ni seuil, ni notification, ni plafond dans les prestations ou leur recouvrement."
}
special_checks = {
 'L552-7': {
  'L543-1': "Le renvoi vise les conditions propres à la rentrée scolaire : ressources, inscription et, pour les enfants concernés, études ou apprentissage sous plafond de rémunération. L552-7 y déroge lorsque le décès empêche de remplir ces conditions à la rentrée et conserve ce droit pour les décès futurs recevables. L'apprentissage n'introduit ici aucun terme d'emploi ; aucune ancienneté ni notification de rupture n'est exigée."
 },
 'L553-1': {
  'L845-3': "L'ancien troisième alinéa visait le recouvrement de prime d'activité, dont la source L845-3 contient des recours suspensifs et des retenues calculées selon L553-2. Seule l'interruption spéciale liée à l'impossibilité de recouvrer est retirée pour les nouvelles procédures. La mention L844-3 était déjà signalée erronée dans la note source ; elle n'est pas conservée. Les prescriptions deux/cinq ans et les effets des interruptions anciennes restent distincts des délais de rupture d'emploi.",
  'L821-5-1': "La cible récupère les indus du titre AAH, avec option de remboursement, retenues et garanties de L133-4-1. L553-1 la visait uniquement pour son interruption spéciale de prescription : cette référence devient sans objet avec le retrait de cette règle pour les nouvelles procédures. Aucun indu AAH n'est effacé ni soumis à une ancienneté d'emploi ; les interruptions anciennes conservent leurs effets.",
  'L553-2': "La source de L553-2 organise les retenues et la remise pour précarité ; son troisième alinéa fixe les critères familiaux. La proposition de ce lot conserve ces sept alinéas à leur rang et retire seulement les frais de gestion. Dans L553-1, la référence à ces recouvrements disparaît avec l'interruption spéciale, sans supprimer les dettes ni les garanties ; deux et cinq ans restent des prescriptions sociales, non une ancienneté de contrat."
 },
 'L553-2': {
  'L168-8': "La référence vise l'allocation journalière du proche aidant parmi les prestations pouvant supporter un recouvrement croisé. Source et proposition de la cible incluent aussi les agents publics et les personnes de L544-8, sous résidence et séjour ; elles ne se limitent pas au contrat privé. Le renvoi reste intact sans durée d'emploi nouvelle ni retrait du congé ou de l'allocation, et les conditions d'accord et d'absence d'autre indu applicables aux retenues subsidiaires sont conservées.",
  'L262-1': "La cible fournie est L262-1 du CSS, relatif à la prévention sanitaire et à la désinsertion professionnelle, y compris non professionnelle. Le renvoi de L553-2 nomme expressément L262-1 du code de l'action sociale et des familles pour le RSA : ce sont deux normes distinctes. Aucune substitution vers le CSS ni vers le contrat unique n'est effectuée ; le texte CASF n'est pas fourni intégralement. Aucune ancienneté ou notification de licenciement n'est déduite de cette homonymie.",
  'L845-3': "L845-3 vise les indus de prime d'activité et renvoie précisément au troisième alinéa de L553-2 pour les retenues. Cet alinéa demeure au même rang, avec critères familiaux et plafonds de majoration des retenues en fraude ; la suppression de l'indemnité de gestion de L553-2 ne supprime pas l'indemnité propre à L845-3. Les recours suspensifs et remises de cette cible ne sont pas modifiés, sans condition d'ancienneté d'emploi ajoutée.",
  'L821-5-1': "L821-5-1 concerne les indus d'AAH et ses retenues renvoient au troisième alinéa de L553-2. Ce troisième alinéa est conservé intégralement à sa place, y compris les ressources, charges de logement et composition familiale. Les indemnités propres à la cible ne sont pas abolies par un renvoi de calcul ; l'option d'un versement et les garanties L133-4-1 restent ouvertes, sans délai de préavis d'emploi importé.",
  'L133-4-1': "La cible source a treize alinéas : les quatrième à neuvième portent sur la rectification des informations et le moment de mise en recouvrement, et les suivants habilitent le décret sur les délais et mentions. L553-2 conserve les renvois aux quatrième à neuvième et aux quatrième à dernier, ainsi que l'accord du gestionnaire et l'absence d'indu concurrent. La proposition de la cible ne renumérote pas ces séquences. La suppression de frais de gestion n'écarte aucune de ces garanties ni leur notification ; ce ne sont pas des délais du contrat unique.",
  'L821-1': "L821-1 fourni appartient au CSS et ouvre l'AAH, notamment avec conditions de séjour et règles de complément de pension. Le premier alinéa de L553-2 cite au contraire L821-1 du code de la construction et de l'habitation : lu dans le corpus, il définit les aides personnelles au logement et leurs catégories. Le renvoi de code est maintenu explicitement ; l'AAH demeure couverte séparément par le titre II du livre VIII. Aucun avantage de la cible AAH ni ancienneté d'emploi n'est modifié."
 },
 'L553-2-1': {
  'L553-2': "La dérogation au régime général L553-2 transfère cet indu de garde au prestataire et interdit sa refacturation aux parents. Le retrait des deux accessoires de 10 % dans le régime spécial ne retire pas cette protection ; le principal est poursuivi avec observations, mise en demeure d'un mois et opposition à contrainte. L553-2 général conserve ses retenues et remises. Ce mois et ces notifications sont des garanties de recouvrement, sans rapport avec les quinze jours de préavis d'un salarié."
 },
 'L553-4': {
  'L553-2': "Le deuxième alinéa du I de L553-4 renvoie au troisième alinéa de L553-2 pour les modalités de saisie. La proposition de ce lot garde ce troisième alinéa entier, à son rang d'origine : composition, ressources, logement et majorations des retenues en fraude restent donc identifiables. La coupe des frais de gestion dans le premier alinéa ne change pas ce barème ni l'insaisissabilité générale. Aucune ancienneté ou notification de rupture n'intervient dans ce renvoi."
 },
 'L553-5': {
  'L821-1': "La cible fournie L821-1 CSS est l'AAH, dont le texte énumère séjour, handicap, retraites et cumuls ; elle n'est pas la norme citée par L553-5. Le a du 2° de L821-1 CCH, lu dans le corpus, désigne l'allocation de logement familiale, exclue de l'évaluation du train de vie. Cette exemption future est préservée sans substitution vers l'AAH. Les anciennes références de droit du travail présentes dans la cible AAH ne deviennent pas des conditions d'ancienneté ou de notification dans L553-5."
 }
}

for source in sources:
    number = source['number']
    key = source['code_id'] + '|' + source['source_id']
    for target_key in references['requirements'][key]:
        target = references['targets'][target_key]
        target_number = target['number']
        if target['code_id'] == 'LEGITEXT000006072050':
            assessment = work_context[number] + ' ' + work_assessments[target_number]
        else:
            assessment = special_checks[number][target_number]
        answers[number]['reference_checks'].append(dict(
            target_key=target_key, view_sha256=target['view_sha256'], assessment=assessment))

result = [answers[a['number']] for a in sources]
answers['L581-3']['review_notes'] += " R581-9 lu prévoit, dans tous les cas, l'imputation prioritaire du dernier terme échu et son reversement au créancier ; cette règle particulière doit être articulée avec la priorité des avances, qui n'est pas présentée ici comme absolue. Aucun changement silencieux de cet ordre de paiement n'est effectué."
answers['L581-10']['review_notes'] += " R581-9, lu dans le corpus, réserve par ailleurs la priorité du dernier terme échu au créancier : articulation avec la priorité législative des avances à contrôler, sans réécriture implicite de ce règlement."
assert len(result) == 24
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print('answer.json:', len(result), 'articles')
