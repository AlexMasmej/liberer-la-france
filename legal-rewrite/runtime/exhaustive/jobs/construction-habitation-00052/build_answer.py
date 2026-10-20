import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_num = {a['number']: a for a in sources}
answers = {}

def plain(xml):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', ' ', xml))).strip()

def replace(xml, old, new, count=1):
    assert xml.count(old) == count, (old, xml.count(old), count)
    return xml.replace(old, new)

def effect(kind, measure, description, before, after, unit, population, transition, sq, pq):
    return dict(kind=kind, measure_id=measure, description=description, before=before,
                after=after, unit=unit, affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens="Aucune formalité de remplacement n'est créée ; les obligations autonomes expressément conservées gardent leur champ.",
                source_quote=sq, proposed_quote=pq)

def record(num, proposed, reason, notes, assessment, limitations, burdens, effects=None,
           removed=None, benefit=None, impact_class=None):
    a = by_num[num]
    kept = proposed is None
    out = {k: a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    out.update(proposed_xml=proposed, reason=reason, review_notes=notes,
               status='retained_unchanged' if kept else 'rewrite_draft')
    if kept:
        out['classification'] = 'retained_necessary'
    if removed:
        out.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19', removed_provisions=removed)
    if benefit:
        out['benefit_review'] = benefit
    out['substantive_impact'] = dict(version=1,
        classification=impact_class or ('retained_necessary' if kept else 'material_reduction'),
        assessment=assessment, scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    out['reference_checks'] = []
    answers[num] = out

SLS = 'supplement-loyer-solidarite-suppression'

# L442-5 : sept alinéas fonctionnels conservés à leur place, transition ajoutée.
n = 'L442-5'
p = by_num[n]['source_xml']
paras = re.findall(r'<p>.*?</p>', p, re.S)
assert len(paras) == 7
paras[0] = "<p>Aux fins de permettre la transmission au Parlement des informations visées au 5° de l'article L. 300-3, les organismes d'habitations à loyer modéré communiquent les renseignements statistiques nécessaires au représentant de l'Etat dans le département du lieu de situation des logements à partir des seules données dont ils disposent légalement ou qu'ils peuvent légalement obtenir sans les demander aux occupants. Le présent article n'impose aucune enquête ni demande de pièces aux locataires, aucun délai de réponse à leur charge et aucun recueil de leur numéro d'immatriculation au répertoire national d'identification des personnes physiques. Aucune pénalité ne peut être fondée sur l'absence de réponse à une telle enquête pour les demandes relevant du présent article à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>"
paras[1] = "<p>Les données ainsi disponibles peuvent être utilisées pour les finalités autonomes de l'article L. 441-9 dans les limites de cet article et des règles de protection des données à caractère personnel. Le présent article ne fonde aucune enquête supplémentaire au titre du supplément de loyer de solidarité pour les périodes d'occupation à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>"
paras[3] = replace(paras[3], "recueillies à l'occasion des enquêtes mentionnées au premier alinéa du présent article", "légalement disponibles dans les conditions du premier alinéa du présent article")
paras[4] = replace(paras[4], "recueillies à l'occasion des enquêtes mentionnées au premier alinéa du présent article", "légalement disponibles dans les conditions du premier alinéa du présent article")
paras[5] = replace(paras[5], "notamment le contenu de l'enquête, dont la liste des données recueillies", "notamment la liste des données légalement disponibles qui peuvent être utilisées, sans rétablir d'enquête auprès des occupants ni de collecte obligatoire de leur numéro d'immatriculation au répertoire national d'identification des personnes physiques")
p = '\n'.join(paras) + "\n<p>La suppression de l'enquête et des demandes de pièces s'applique également aux demandes en cours auxquelles le locataire n'a pas encore répondu à la date d'entrée en vigueur de la loi portant la présente réforme. Aucune réponse ni régularisation n'est exigée après cette date sur ce seul fondement. Les données antérieurement recueillies restent soumises aux règles de finalité, d'accès, de sécurité et de conservation qui leur sont applicables. Les créances légalement nées avant cette date et les recours restent soumis aux dispositions antérieures, sous réserve de l'application, dans son champ, de la loi répressive plus douce aux pénalités non définitives. Les demandes nécessaires à des droits ou obligations ayant un autre fondement légal conservent leur régime propre. Le présent article n'ouvre aucun accès nouveau à des données.</p>"
record(n, p,
 "Réforme de fond : retire l'enquête statistique obligatoire auprès des locataires, les avis fiscaux et numéros d'identification à recueillir sur ce seul fondement, le délai d'un mois et la pénalité de 7,62 euros augmentée chaque mois. Le reporting nécessaire, l'évaluation ANCOLS, les finalités d'analyse sociale et énergétique, l'exploitation par le GIP, l'anonymisation et le champ des bailleurs demeurent. La statistique repose sur les données légalement disponibles, sans déclaration substitutive. Le réemploi n'est pas compté comme un nouveau droit d'accès aux données.",
 "Sept alinéas fonctionnels conservés, puis transition ajoutée. Coordonner R442-13 et R442-14, lus avec leurs notes du décret du 26 juin 2024, ainsi que l'arrêté d'enquête : ils ne peuvent rétablir questionnaire ou NIR obligatoire. R442-14 vise encore le cinquième alinéa pour les destinataires alors que leur liste figure au sixième dans cette source : discordance préexistante à rectifier dans ce règlement. Les finalités autonomes de L441-9 sont celles de sa proposition fournie, distincte du droit officiel ; le supplément supprimé ne renaît pas. La liste complète des destinataires et le seuil d'au moins cinq logements restent intacts. Le 24e alinéa de L441-1 lu correspond aux territoires des EPCI. L300-3 reste à coordonner si des séries statistiques indisponibles y sont prescrites ; son rapport n'est pas abrogé ici. Pertes éventuelles de fraîcheur et de complétude des statistiques et coût public non évalués ; aucune fin de l'examen des 209 articles SRU n'est affirmée.",
 "La source entière imposait une enquête aux occupants et une sanction mensuelle ; ces obligations disparaissent, au-delà d'une simple dispense de pièces déjà détenues. Les transmissions statistiques et contrôles autonomes subsistent.",
 "Le volume de demandes évitées et le coût public ne sont pas chiffrés. Les enquêtes utiles à des aides ou à d'autres règles autonomes, les créances anciennes et les délais propres aux recours ne sont pas supprimés.",
 "Aucune charge nouvelle n'est identifiée : ni registre, ni accès aux données, ni pièce ou déclaration de remplacement. Les analyses et transmissions conservées existaient déjà ; leur qualité avec moins de données reste à évaluer.",
 [effect('obligation_removed', 'occupation-sociale-fin-enquete-locataires',
    "Suppression du questionnaire statistique obligatoire des occupants et de ses pièces et sanctions propres.",
    "Enquête auprès des locataires, avis fiscaux ou RFR et NIR de chaque majeur, réponse sous un mois ; pénalité de 7,62 euros plus 7,62 euros par mois entier, avec exception pour difficultés particulières.",
    "Aucune enquête ni demande de pièces sur ce fondement, aucun NIR à recueillir ni délai de réponse ; statistiques à partir des données légalement disponibles. Pas de pénalité pour les nouvelles demandes, anciennes sanctions sous réserve de la loi plus douce.",
    'legal_duty', 'Locataires et occupants majeurs des parcs HLM et des patrimoines conventionnés visés au dernier alinéa.',
    "Demandes futures et demandes en cours sans réponse ; créances antérieures et protection des données préservées selon la transition.",
    "Les locataires sont tenus de répondre dans le délai d'un mois.",
    "Le présent article n'impose aucune enquête ni demande de pièces aux locataires, aucun délai de réponse à leur charge et aucun recueil de leur numéro d'immatriculation au répertoire national d'identification des personnes physiques.")],
 removed=["Enquête statistique obligatoire auprès des locataires et recueil, sur ce seul fondement, des avis fiscaux ou du RFR et du NIR de chaque occupant majeur.", "Délai obligatoire d'un mois de réponse du locataire à l'enquête statistique et pénalité propre de 7,62 euros majorée de 7,62 euros par mois entier de retard."])

n = 'L442-5-1'
p = "<p>Lorsque l'enquête mentionnée à l'article L. 441-9 fait apparaître que le logement fait l'objet d'une sous-occupation telle que définie à l'article L. 621-2, le bailleur procède avec le locataire à un examen de sa situation et des possibilités d'évolution de son parcours résidentiel.</p><p>Le bailleur informe le locataire des différentes possibilités d'accession à la propriété auxquelles il peut prétendre.</p><p>A compter de l'entrée en vigueur de la loi portant la présente réforme, l'assujettissement au supplément de loyer de solidarité au titre d'une période d'occupation antérieure ne peut, à lui seul, imposer un nouvel examen ou la poursuite d'un examen du parcours résidentiel. Les propositions et engagements valablement acquis avant cette date et les droits du locataire sont préservés.</p>"
record(n, p,
 "Coordination de la suppression du supplément de loyer : retire son seul rôle de déclencheur obligatoire de l'examen résidentiel. Le déclencheur autonome de sous-occupation et l'information sur l'accession sont conservés pour les futurs locataires comme pour ceux déjà présents. Aucun préavis locatif ou professionnel n'est modifié.",
 "L441-9 fourni conserve une enquête pour RLS et L442-3-3, avec réemploi des données et sans supplément futur. Le maintien de ce renvoi ne rétablit donc pas une enquête exclusivement SLS. Le supplément ancien reste liquidable sans obliger à un nouvel entretien du seul fait de cette dette. L621-2 est le critère autonome de sous-occupation ; les offres, aides et protections de L442-3-1 restent distinctes. Les deux fonctions initiales sont à leur place ; seule une transition est ajoutée.",
 "Retire une conséquence procédurale du supplément déjà supprimé par la mesure commune ; ce n'est pas une deuxième suppression de prélèvement. L'examen pour sous-occupation et l'information favorable demeurent.",
 "Ni le nombre d'entretiens évités ni une économie de loyer ne sont établis par cet article. Les règles autonomes de mobilité, d'attribution et les anciennes dettes restent hors de cette coordination.",
 "Aucune charge nouvelle n'est identifiée : aucun entretien, formulaire, préavis ou condition d'ancienneté de travail ne remplace le déclencheur SLS retiré.",
 [effect('coordination', SLS, 'Retrait du déclencheur résidentiel fondé sur le seul supplément supprimé.',
    'Examen obligatoire si assujettissement au supplément ou sous-occupation révélés par l’enquête.',
    'Seule la sous-occupation reste un déclencheur dans cet article ; information accession et droits acquis maintenus.',
    'legal_duty', 'Locataires HLM dont la situation est examinée dans le cadre de L441-9.',
    'Application dès entrée en vigueur aux examens futurs ou en cours, sans annulation des engagements acquis.',
    "un locataire est assujetti au supplément de loyer de solidarité mentionné à l'article L. 441-3",
    "Lorsque l'enquête mentionnée à l'article L. 441-9 fait apparaître que le logement fait l'objet d'une sous-occupation")],
 removed=["Déclenchement et poursuite obligatoires de l'examen résidentiel du seul fait d'un assujettissement au supplément de loyer de solidarité."], impact_class='coordination_only')

n = 'L442-5-2'
p = by_num[n]['source_xml']
p = replace(p, "le bailleur examine, tous les trois ans à compter de la date de signature du contrat de location, les conditions d'occupation du logement. Il transmet", "le bailleur examine, à la demande du locataire, les conditions d'occupation du logement. A la demande de ce dernier, il transmet")
p = replace(p, "les dossiers des locataires qui sont dans une des situations suivantes", "le dossier de ce locataire lorsqu'il est dans une des situations suivantes")
p += "<p>Le caractère systématique de l'examen triennal et de la transmission des dossiers cesse à l'entrée en vigueur de la loi portant la présente réforme, y compris pour les baux et examens en cours. Les locataires conservent la possibilité de demander cet examen et la saisine de la commission dans les situations énumérées au présent article. Les droits aux offres de relogement, aux aides à la mobilité, à un logement adapté et aux protections contre la perte du maintien dans les lieux résultant des dispositions applicables demeurent. Les avis et actes régulièrement intervenus ainsi que les engagements valablement acquis avant cette entrée en vigueur sont préservés.</p>"
record(n, p,
 "Réforme de fond : supprime le passage obligatoire tous les trois ans et l'envoi automatique des dossiers en commission. Le service d'examen et l'accès à la commission deviennent mobilisables à la demande du locataire. Les cinq situations, les fonctions de la commission, l'examen avec le locataire et les renvois protecteurs à L442-3-1 et L442-3-2 sont maintenus intégralement.",
 "La note de 2018 fixait l'application du dispositif officiel aux baux en cours dès le 1er janvier 2019 ; elle n'est pas la date de cette réforme. L441-2 IV, lu en entier avec L441-2, demeure le fondement de l'avis et de sa notification ; il faudra y préciser le nouveau mode de saisine. L442-3-1 et L442-3-2, lus en entier, conservent offres hors plafonds, loyer inférieur, aide à la mobilité, refus et exceptions d'âge/handicap/QPV, délais de six et dix-huit mois dans leurs champs. La fin de la revue automatique ne les abroge pas. Les règlements doivent perdre la périodicité et l'envoi systématique sans déclaration de remplacement. La demande peut désormais déclencher un examen hors du cycle triennal : cette obligation de traitement ciblé est recensée comme ajout, avec solde de charge non établi.",
 "La revue triennale systématique et l'envoi automatique cessent, mais l'examen et la saisine deviennent exigibles à la demande du locataire, éventuellement hors cycle. La réforme combine suppression de procédures générales et obligation ciblée ; son solde net n'est pas démontré.",
 "Le nombre d'examens évités et de demandes supplémentaires, leur fréquence et leur coût ne sont pas établis. Les dispositifs autonomes de relogement restent applicables ; la perte du maintien n'est pas abrogée par cette seule réforme.",
 "Charge nouvelle identifiée pour le bailleur : traiter l'examen et la transmission demandés par le locataire sans attendre l'ancien cycle triennal. Aucun dossier-type, justificatif, registre ou délai de réponse nouveau n'est prescrit. Cette contrepartie doit être comparée à la fin du traitement systématique ; solde net inconnu.",
 [effect('obligation_removed', 'occupation-logements-fin-examen-triennal',
    'Suppression de la périodicité obligatoire et de la transmission systématique des dossiers en zone tendue.',
    'Examen obligatoire tous les trois ans depuis la signature du bail ; transmission en commission des dossiers relevant des cinq situations.',
    'Examen et transmission à la demande du locataire ; aucune cadence triennale ni transmission générale obligatoire dans cet article.',
    'legal_duty', 'Bailleurs et locataires des logements des zones géographiques de déséquilibre important définies par décret.',
    'Baux nouveaux et en cours dès entrée en vigueur ; avis, engagements acquis et protections de mobilité maintenus.',
    "le bailleur examine, tous les trois ans à compter de la date de signature du contrat de location, les conditions d'occupation du logement.",
    "le bailleur examine, à la demande du locataire, les conditions d'occupation du logement.")],
 removed=["Examen systématique des conditions d'occupation tous les trois ans à compter de la signature de chaque bail en zone tendue.", "Transmission automatique à la commission des dossiers relevant des cinq situations d'occupation, sans demande du locataire."], impact_class='mixed')
answers[n]['substantive_impact']['effects'][0]['replacement_or_new_burdens'] = "L'examen et la transmission sont remplacés par un traitement exigible à la demande du locataire, susceptible d'intervenir hors de l'ancien cycle ; aucun formulaire ou justificatif nouveau n'est imposé, solde net non chiffré."
added = effect('obligation_added', 'occupation-logements-fin-examen-triennal',
    "Obligation ciblée d'examiner et de saisir la commission à la demande du locataire, sans attendre l'ancien cycle triennal.",
    "Cet article imposait un examen systématique tous les trois ans et l'envoi des dossiers éligibles ; il ne prévoyait pas ce déclenchement à la demande.",
    "Le bailleur doit examiner à la demande et transmettre le dossier du demandeur dans les cinq situations, sans nouveau délai de réponse fixé par cet article.",
    'legal_duty', 'Bailleurs et locataires des logements des zones de déséquilibre important définies par décret.',
    'A compter de l’entrée en vigueur, y compris baux en cours ; avis et droits antérieurs protégés.',
    "le bailleur examine, tous les trois ans à compter de la date de signature du contrat de location, les conditions d'occupation du logement.",
    "A la demande de ce dernier, il transmet à la commission d'attribution des logements et d'examen de l'occupation des logements le dossier de ce locataire lorsqu'il est dans une des situations suivantes")
added['replacement_or_new_burdens'] = "Traitement exigible hors cycle sur demande du locataire, sans dossier-type, pièce ni délai réglementaire nouveau institué dans cet article ; le coût net avec la suppression du systématisme n'est pas établi."
answers[n]['substantive_impact']['effects'].append(added)

record('L442-6-2', None,
 "Maintien intégral nécessaire : l'interdiction de réclamer des frais lors de la demande ou de la signature du bail évite une charge d'entrée dans le logement social. Elle ne comporte ni déclaration, ni agrément, ni délai minimum à retirer. L'abroger recréerait une possibilité de facturation contraire à l'objectif de baisse des charges.",
 "La règle concerne les deux moments distincts, demande d'attribution et signature, et tous frais à quelque titre que ce soit. Aucun tarif, exception ou mécanisme de compensation n'est ajouté. Elle demeure ouverte aux futures demandes.",
 "La gratuité d'accès à la demande et à la signature est conservée intégralement ; aucun allègement nouveau n'est revendiqué.",
 "Cette interdiction spéciale ne chiffre ni les charges locatives ordinaires ni le coût de gestion des bailleurs et ne règle pas les autres actes immobiliers.",
 "Aucune charge nouvelle n'est identifiée : maintien de l'interdiction existante de frais sans procédure de preuve, registre ou autorisation supplémentaire.")

record('L442-6-3', None,
 "Maintien intégral de la dérogation favorable de préavis locatif d'un mois pour une mutation dans le parc du même bailleur. C'est un allègement utile à la mobilité, sans formalité autonome à supprimer. Le préavis professionnel de quinze jours ne concerne pas ce congé donné par un locataire.",
 "Conserver exactement le renvoi au I de l'article 15 de la loi du 6 juillet 1989 et le double rattachement au parc de L441-1. Le texte extérieur de 1989 n'est pas intégralement fourni ici ; aucune nouvelle règle de notification n'en est déduite. Les renvois de contrôle au code du travail sont matériellement étrangers à cette disposition.",
 "Le délai réduit existant d'un mois est conservé, sans le compter comme une réduction nouvelle ni le confondre avec une rupture d'emploi.",
 "La règle est limitée aux logements de L441-1 et au parc du même bailleur. Le régime des autres congés, les formes de notification et les contrats de travail ne sont pas réécrits.",
 "Aucune charge nouvelle n'est identifiée : aucune pièce, condition d'ancienneté, durée minimale d'emploi ou nouvelle notification n'est ajoutée.",
 benefit="La dérogation réduit le préavis locatif à un mois pour le locataire qui obtient un autre logement du même bailleur dans le champ de L441-1. Elle est maintenue sans restriction pour les futures mutations éligibles comme pour celles en cours ; aucune ancienneté de travail ni préavis professionnel n'est substitué.")

record('L442-6-4', None,
 "Maintien intégral nécessaire : protège le locataire de la location forcée d'une place de stationnement, même mutualisée, et garantit la baisse de loyer et de charges s'il y renonce. Les catégories de financements et la date du 1er octobre 1996 délimitent l'avantage ; leur suppression pourrait le faire perdre ou modifier des régimes distincts.",
 "Les deux alinéas sont conservés, y compris la possibilité de renoncer depuis la publication de la loi du 29 juillet 1998 et l'absence d'incidence sur la validité du bail malgré une stipulation contraire. La décision favorable de financement n'est pas un agrément supplémentaire imposé par cet article au locataire.",
 "L'interdiction de coupler le parking au logement et la réduction correspondante des loyers et charges demeurent ; aucun gain nouveau n'est attribué au maintien.",
 "L'avantage garde son champ exact : immeubles collectifs et logements financés ou décidés dans les conditions source. Aucune économie moyenne ni extension à tout le parc privé n'est démontrée.",
 "Aucune charge nouvelle n'est identifiée : la renonciation et son effet sur le prix existaient ; ni dossier, ni autorisation, ni délai nouveau n'est institué.")

n = 'L442-6-5'
p = by_num[n]['source_xml']
p = replace(p, "un plan d'apurement de sa dette locative approuvé par le représentant de l'organisme payeur de l'allocation et joint au protocole.", "un plan d'apurement de sa dette locative joint au protocole. Ce plan n'est soumis à aucune approbation préalable de l'organisme payeur, y compris pour l'ouverture du droit aux allocations de logement et pour leur extension à la période mentionnée au premier alinéa.")
p = replace(p, "le représentant de l'organisme payeur mentionné au deuxième alinéa", "le représentant de l'organisme payeur de l'allocation")
p += "<p>La suppression de l'approbation préalable s'applique aux protocoles et avenants conclus à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsque leur préparation a commencé auparavant. Aucune approbation ni déclaration de remplacement n'est exigée. Les protocoles déjà conclus, les droits aux allocations, les engagements, les créances et les recours antérieurs restent préservés. Les conditions légales des allocations, leurs contrôles autonomes et les règles de traitement du surendettement demeurent applicables ; la suppression de l'approbation n'ouvre pas, à elle seule, un droit à restitution pour une période antérieure.</p>"
record(n, p,
 "Réforme de fond ciblée : retire l'approbation préalable du plan d'apurement par l'organisme payeur, sans la remplacer par un visa ou une déclaration. L'accord locatif, le plan joint, les paiements convenus, les aides et leur extension possible, la saisine du FSL, l'accompagnement social, le rétablissement du bail et les suspensions liées au surendettement restent entiers. Le rôle du représentant payeur au troisième alinéa est nommé directement pour éviter un renvoi devenu vide.",
 "D824-15 lu exige encore l'approbation avant l'ouverture de l'aide : coordonner sa première phrase dans le seul champ de L442-6-5 et du protocole de sous-location de L442-8-2 qui s'y rattache ; ne pas abroger ses rappels d'aide, seuil de 450 euros, versements semestriels et premier paiement à trois mois. Le mécanisme autonome de L353-15-2 n'est pas modifié par simple analogie. Les huit paragraphes source, dont les deux alinéas distincts sans dette/durée réunis dans un même p, restent dans leur ordre. Deux ans, prolongation de trois ans, bail sous trois mois et l'ensemble des références de surendettement sont conservés. La durée du protocole n'est pas celle d'un emploi. Aucun chiffrage des effets sur organismes payeurs ou impayés n'est disponible.",
 "Une autorisation administrative préalable du plan disparaît réellement. Le protocole protecteur et les critères autonomes d'aide ne sont pas abolis ; la baisse porte sur le circuit d'approbation, pas sur la dette locative.",
 "Les économies de délai et de coût ne sont pas mesurées. D824-15 doit être coordonné sans fermer le rappel d'aide ; les dettes, contrôles indépendants et procédures judiciaires d'expulsion restent à leur champ.",
 "Aucune charge nouvelle n'est identifiée : le plan joint et la transmission sans dette existaient déjà. Aucun nouvel agrément, déclaration, information périodique ou délai de remplacement n'est imposé.",
 [effect('authorization_removed', 'protocole-hlm-fin-approbation-plan',
    "Suppression du visa préalable du plan d'apurement dans les protocoles de rétablissement du bail.",
    "Plan approuvé par le représentant de l'organisme payeur et joint au protocole ; D824-15 en fait une condition préalable d'aide.",
    "Plan convenu et joint sans approbation préalable, y compris pour l'aide et son extension ; contrôles légaux indépendants conservés.",
    'legal_duty', 'Occupants et bailleurs HLM concluant un protocole après résiliation judiciaire pour impayés, et organismes payeurs.',
    'Protocoles et avenants futurs, y compris projets en cours ; anciens accords et droits acquis préservés.',
    "un plan d'apurement de sa dette locative approuvé par le représentant de l'organisme payeur de l'allocation et joint au protocole.",
    "Ce plan n'est soumis à aucune approbation préalable de l'organisme payeur, y compris pour l'ouverture du droit aux allocations de logement et pour leur extension à la période mentionnée au premier alinéa.")],
 removed=["Approbation préalable du plan d'apurement par l'organisme payeur de l'allocation comme condition du protocole et de son effet sur le droit à l'aide."])

record('L442-7', None,
 "Maintien intégral nécessaire de l'équilibre du logement de fonction : la clause est facultative, doit identifier l'emploi et n'agit qu'après la fin effective de ses fonctions. Le délai d'action d'un an, les six mois au moins de préavis locatif, le délai exceptionnel et le maintien lié au handicap protègent les occupants. Leur suppression ne serait pas un allègement favorable. Il n'existe ici ni CDD ni indemnité de rupture professionnelle à coordonner.",
 "L441-1 lu en entier : son 39e alinéa concerne bien les réservations, et son 43e prévoit la mention de la clause dans les conventions employeur/bailleur. Préavis locatif d'au moins six mois à compter de la notification par le bailleur, puis délai exceptionnel d'un an au plus, sans réduction à quinze jours. La source présente un II sans afficher de I avant les premiers alinéas : incohérence formelle préexistante signalée, sans création stylistique d'un nouveau corps. Le texte intégral du code des transports L1221-3 et du décret des situations exceptionnelles n'est pas fourni dans le contexte de renvois ; leur réécriture n'est pas prétendue effectuée.",
 "Le régime facultatif de clause de fonction, ses bornes temporelles et les protections médicales, familiales et de handicap restent intégraux, sans réduction de charge revendiquée.",
 "Agents publics et salariés des services de transport ont des régimes d'emploi distincts ; l'article ne donne aucun effet locatif à une simple fin de mission et ne modifie pas les procédures professionnelles.",
 "Aucune charge nouvelle n'est identifiée : clause, identification de l'emploi et notification sont les garanties existantes d'une résiliation locative, sans nouveau formulaire ni délai.")

# Le II renvoie au I : rendre cette subdivision explicite sans déplacer d'alinéa.
out = answers['L442-7']
out['proposed_xml'] = replace(by_num['L442-7']['source_xml'], '<p>Le droit au maintien', '<p>I. - Le droit au maintien')
out['status'] = 'rewrite_draft'
del out['classification']
out['reason'] = "Coordination formelle nécessaire : le II vise un préavis mentionné au I alors que la source n'affiche aucun I. Ce numéro est rétabli au début des dispositions de la clause de fonction, sans déplacement d'alinéa ni autre modification. Le fond est intégralement maintenu : clause facultative identifiant l'emploi, action sous un an, notification du bailleur, six mois de préavis locatif au moins, délai exceptionnel et maintien lié au handicap. Il ne s'agit pas du préavis professionnel de quinze jours."
out['review_notes'] = "La source a été confrontée à L441-1 entier : le 39e alinéa porte bien les réservations et le 43e prévoit la clause de fonction. Le défaut d'affichage du I est une incohérence préexistante expressément corrigée ; le II et ses deux alinéas gardent leur position et leurs références au préavis. Aucun changement des bornes d'un an et de six mois, de la notification par le bailleur ou de l'exception de handicap non connu à la conclusion du bail. Le code des transports L1221-3 et le décret des situations exceptionnelles ne sont pas fournis intégralement dans le contexte de renvois et ne sont pas présentés comme réécrits. Le régime des agents publics n'est pas assimilé au droit privé."
out['substantive_impact'] = dict(version=1, classification='coordination_only',
    assessment="Seule la subdivision I manquante est rendue explicite afin que le renvoi du II soit cohérent. Les conditions, protections et préavis du logement de fonction sont intégralement conservés ; aucune réduction matérielle n'est revendiquée.",
    scope_limitations="Cette coordination ne modifie ni le bail ni l'emploi, ni les procédures collectives ou les autorisations professionnelles. Les régimes publics et le décret des situations exceptionnelles restent distincts.",
    new_burdens_review="Aucune charge nouvelle n'est identifiée : aucun document, avis, délai ou condition ne change ; l'ajout du numéro I sert exclusivement le renvoi déjà écrit dans le II.",
    effects=[effect('coordination', 'logement-fonction-reperage-subdivision',
        "Affichage du I auquel renvoie le II pour le préavis locatif.",
        "Le II vise le I, non affiché dans la source, qui contient déjà les règles de clause de fonction et de préavis.",
        "Les mêmes dispositions sont précédées de I ; le II continue de viser le préavis locatif d'au moins six mois, sans modification de champ.",
        'other', 'Locataires et ayants droit des logements soumis à la clause de fonction de L442-7.',
        "Repérage de la subdivision sans changement des actes, délais ou droits des baux anciens et futurs.",
        "Le droit au maintien dans les lieux d'un agent public civil ou militaire",
        "I. - Le droit au maintien dans les lieux d'un agent public civil ou militaire")])

n = 'L442-8'
p = by_num[n]['source_xml']
p = replace(p, "il est interdit de louer en meublé ou de sous-louer un logement", "il est interdit de sous-louer un logement")
p = replace(p, "sous peine d'une amende de 9 000 €.</p>", "sous peine d'une amende de 9 000 €. La location meublée est admise dans les mêmes conditions d'attribution et de loyer que la location non meublée, sous réserve des dispositions applicables au prix de location des meubles.</p>")
p += "<p>La suppression de l'interdiction de louer en meublé s'applique aux locations conclues ou en cours à compter de l'entrée en vigueur de la loi portant la présente réforme. Elle n'autorise pas une modification unilatérale du loyer ou du bail. L'interdiction de sous-location et ses dérogations légales conservent leur champ. Les droits et créances antérieurs sont préservés ; les sanctions non définitives relatives à la seule location meublée bénéficient, dans son champ, de la loi répressive plus douce. Aucune autorisation ni déclaration de remplacement n'est exigée au titre de la suppression de cette interdiction.</p>"
record(n, p,
 "Réforme de fond : supprime la prohibition générale de louer en meublé, qui restreignait l'offre sans distinguer l'ameublement de la destination sociale. Les règles d'attribution, de loyer et de prix des meubles restent applicables. L'interdiction de sous-louer hors dérogations et l'amende de 9 000 euros dans ce seul champ protègent les actifs sociaux contre leur détournement. Les foyers et la location intermédiaire aux personnes morales pour leurs agents ou salariés gardent expressément leurs régimes favorables.",
 "Les trois alinéas initiaux restent à leur place, transition ajoutée. Les références L633-1, L411-2 et L302-16, et les deux conditions distinctes 2° ressources et 3° loyers des sous-locations intermédiaires sont inchangées. L442-8-1 et L442-8-2 lus confirment des dérogations autonomes de sous-location qui ne doivent pas être fermées. L442-8-3-1 du lot demeure la règle du prix des meubles. Coordination nécessaire des dispositions et formulaires qui assimileraient encore une simple location meublée à l'interdiction supprimée ; aucun régime d'hébergement ni bail d'emploi nouveau n'est créé. Les sanctions pour sous-location illicite ne sont pas supprimées sous couvert de l'ameublement.",
 "La location meublée devient possible dans le champ général des logements financés du livre III. La suppression porte sur une interdiction, sans disparition des plafonds ni des conditions de sous-location.",
 "Le nombre de logements ainsi mobilisables et l'effet sur les coûts ne sont pas chiffrés. Les réglementations autonomes de décence, d'attribution et de sous-location restent opposables ; l'article ne libéralise pas les loyers sociaux.",
 "Aucune charge nouvelle n'est identifiée : les conditions d'attribution et de loyer sont celles déjà applicables aux mêmes logements ; aucune déclaration ne remplace la prohibition retirée.",
 [effect('obligation_removed', 'logement-social-fin-interdiction-meuble',
    'Retrait de la prohibition générale de louer les logements sociaux en meublé.',
    'Location meublée interdite dans les immeubles locatifs financés par crédits du livre III, hors exceptions, sous peine de 9 000 euros.',
    'Location meublée admise avec règles sociales et prix des meubles applicables ; amende de 9 000 euros maintenue pour la seule sous-location illicite.',
    'legal_duty', 'Bailleurs et occupants des immeubles locatifs financés par les crédits du livre III.',
    'Locations nouvelles ou en cours dès entrée en vigueur ; pas de modification unilatérale du bail ; loi répressive plus douce dans son champ.',
    "il est interdit de louer en meublé ou de sous-louer un logement, meublé ou non, sous quelque forme que ce soit, sous peine d'une amende de 9 000 €.",
    "La location meublée est admise dans les mêmes conditions d'attribution et de loyer que la location non meublée, sous réserve des dispositions applicables au prix de location des meubles.")],
 removed=["Interdiction de la location meublée et sanction de cette seule modalité d'occupation dans les immeubles locatifs financés par les crédits du livre III."],
 benefit="L'exclusion des logements-foyers du premier alinéa est intégralement conservée. La dérogation autorisant les logements intermédiaires, meublés ou non, loués à une personne morale pour ses agents ou salariés subsiste avec ses plafonds de ressources et de loyer. Ces avantages restent ouverts aux futures locations et sous-locations recevables ; aucune fin de contrat de travail ne s'en déduit.")

n = 'L442-8-1-1'
p = by_num[n]['source_xml']
p = replace(p, " dès lors que les besoins ont été identifiés dans le plan départemental d'action pour le logement et l'hébergement des personnes défavorisées", "", count=2)
p = replace(p, "par la victime,.", "par la victime.")
p += "<p>La suppression de la condition d'identification préalable des besoins dans le plan départemental s'applique, à compter de l'entrée en vigueur de la loi portant la présente réforme, aux nouvelles opérations et à celles en cours. L'accès à cette faculté de location n'est subordonné à aucune identification, autorisation ou déclaration de remplacement. Les conventions, aides, droits des personnes hébergées et engagements valablement acquis avant cette date sont préservés. Les conditions de sécurité, de salubrité et de fonctionnement des structures d'hébergement ayant un autre fondement légal demeurent applicables.</p>"
record(n, p,
 "Réforme de fond : retire dans les deux branches la condition de programmation préalable des besoins au plan départemental. Un besoin individuel d'hébergement, notamment une urgence de violences conjugales, n'a pas à attendre cette inscription. Le caractère subsidiaire, les organismes habilités, les bénéficiaires du II de L301-1, les preuves de violences et le statut propre de l'hébergement restent intacts.",
 "I, 1°, 2° et II restent à leur place. L365-4 demeure l'agrément de l'intermédiaire ; il n'est pas remplacé ni étendu. Les structures CASF L312-1 I 8° et L322-1 sont conservées comme catégories autonomes, sans modifier leur régime. L'ordonnance de protection et le récépissé de plainte restent des voies alternatives, non cumulatives. La référence au conventionnement de L831-1 et l'exclusion de L442-8-2 pour les personnes hébergées subsistent. Le plan départemental lui-même, institué hors de ce lot, n'est pas abrogé. Aucune garantie de financement d'une place nouvelle n'est créée.",
 "L'identification des besoins au plan départemental cesse d'être une condition d'accès aux deux facultés d'hébergement. Les qualifications des structures et les protections des personnes demeurent.",
 "Cette suppression n'abroge pas le plan ni les règles CASF de sécurité et de financement ; le nombre de places, leur coût et les crédits effectivement disponibles ne sont pas établis.",
 "Aucune charge nouvelle n'est identifiée : pas de nouvelle attestation de besoin, autorisation, déclaration ou programmation de substitution ; les justificatifs de violence conservés sont ceux de la source.",
 [effect('obligation_removed', 'hebergement-hlm-fin-condition-plan-besoins',
    "Suppression de la condition d'identification préalable des besoins au plan départemental dans les deux branches d'hébergement.",
    'Les deux facultés de location sont subordonnées à des besoins identifiés dans le plan départemental.',
    "Les mêmes facultés sont accessibles sans cette programmation préalable ; opérateurs, publics et autres conditions maintenus.",
    'legal_duty', 'Organismes HLM, intermédiaires habilités et personnes ou familles défavorisées, notamment victimes de violences au sein du couple.',
    "Opérations futures et en cours dès entrée en vigueur ; aides et conventions acquises protégées.",
    "dès lors que les besoins ont été identifiés dans le plan départemental d'action pour le logement et l'hébergement des personnes défavorisées",
    "L'accès à cette faculté de location n'est subordonné à aucune identification, autorisation ou déclaration de remplacement.")],
 removed=["Condition d'identification préalable des besoins dans le plan départemental pour l'hébergement des publics de L301-1 II et pour l'hébergement d'urgence ou relais des victimes de violences."],
 benefit="Les deux possibilités dérogatoires de location pour l'hébergement sont conservées et ouvertes aux opérations futures sans inscription préalable du besoin au plan. Subsistent les opérateurs des 1° et 2°, le conventionnement pour l'urgence ou le relais, les deux preuves alternatives des violences et le statut d'hébergé. L'exclusion de l'assimilation aux locataires n'est pas une exonération fiscale ; c'est la qualification de l'hébergement, maintenue sans fermer les droits autonomes.")

record('L442-8-1-2', None,
 "Maintien intégral nécessaire de la dérogation facilitant l'habitat inclusif : location à un intermédiaire agréé, sous-location adaptée, locaux collectifs et cohabitation avec des personnes de L433-2 CASF. L'autorisation spécifique de L441-2 III ouvre une attribution prioritaire aux personnes en perte d'autonomie ; la supprimer isolément ici ferait perdre son articulation avec cette faveur et les réservations. Les garanties d'un opérateur qualifié et de loyers plafonnés ont une fonction essentielle de protection.",
 "L441-2 lu intégralement : le troisième alinéa du III porte bien l'autorisation des programmes pour âge/handicap, distincte du cinquième pour les jeunes de moins de trente ans. Ce n'est pas un agrément de contrat de travail. Conserver les I 1°/2°, la faculté du dernier alinéa du I et le II. L'exception ne concerne que la première phrase du troisième alinéa de L442-8-4, relative à la procédure d'attribution des articles L441 à L441-2-9 ; sa seconde phrase, appréciant le plafond de ressources par contrat, n'est pas exclue. La réserve 'le cas échéant' du I pour les personnes de L433-2 CASF reste également intacte. Les sources L442-8-2 et L442-8-4 ont été confrontées. Une suppression générale de l'autorisation spécifique devrait préserver expressément la priorité de L441-2 et coordonner ses règlements ; elle n'est pas simulée par un simple retrait de renvoi ici.",
 "Toutes les possibilités d'habitat inclusif et leurs garanties sont maintenues ; aucun gain nouveau ni agrément supprimé n'est revendiqué.",
 "La règle conserve le champ des publics en perte d'autonomie, des intermédiaires agréés et de leurs locaux collectifs. L'autorisation prioritaire et les textes CASF extérieurs ne sont pas réécrits.",
 "Aucune charge nouvelle n'est identifiée : agrément, autorisation et plafonds sont ceux de la source, conservés pour la destination sociale et la protection des publics vulnérables.",
 benefit="Sont maintenus pour les situations futures éligibles : la dérogation à l'interdiction de sous-location et à l'article 40 de la loi de 1989, la sous-location meublée ou non et en colocation pour âge/handicap, les locaux collectifs de vie partagée et la présence de personnes de L433-2 CASF. Les plafonds ne s'appliquent que le cas échéant comme dans la source ; les droits de L442-8-2 et l'exception ciblée de L442-8-4 subsistent intégralement.")

n = 'L442-8-3'
p = by_num[n]['source_xml']
p = replace(p, " Deux mois avant l'échéance de cette période d'examen, dont la durée est fixée par la convention, l'organisme défini à l'article L. 411-2 indique au représentant de l'Etat dans le département où est situé le logement s'il propose un bail au sous-locataire et, dans la négative, les motifs de cette décision.", "")
p += "<p>A compter de l'entrée en vigueur de la loi portant la présente réforme, aucune transmission au représentant de l'Etat n'est exigée sur le seul fondement du présent article, y compris pour les périodes d'examen et les conventions en cours. Aucun envoi de remplacement n'est imposé. La convention tripartite, l'examen périodique contradictoire, les droits à l'information et au recours ayant un fondement autonome, ainsi que les engagements et droits antérieurement acquis restent applicables.</p>"
record(n, p,
 "Réforme de fond : supprime l'envoi systématique au préfet de l'offre ou du refus de bail et de ses motifs deux mois avant l'échéance d'examen. La convention tripartite annexée, le parcours vers un bail direct et l'examen contradictoire demeurent nécessaires à la protection du sous-locataire. Les contrôles et recours autonomes permettent de les faire respecter sans ce reporting anticipé général.",
 "Les trois alinéas source restent dans leur ordre ; seule la seconde phrase du troisième est retirée, puis une transition est ajoutée. R442-4-1 lu conserve l'entretien tous les six mois à compter de la sous-location entre bailleur, locataire principal et sous-locataire ; cette périodicité n'est pas supprimée ici. L441-2-3 pour les prioritaires DALO, L301-1 II, article 7 loi de 1989 et R441-1 sont conservés dans leur champ. L'envoi retiré n'est pas une notification à l'intéressé ni un délai de préavis professionnel. Le contrôle préfectoral ayant une autre base légale n'est pas abrogé.",
 "Une transmission administrative systématique anticipée disparaît. La convention et la revue contradictoire protectrices restent entières : aucun second gain n'est attribué à leur maintien.",
 "Les coûts de transmission évités ne sont pas évalués. Les obligations autonomes d'information des occupants, DALO, de motivation ou de contrôle gardent leur champ.",
 "Aucune charge nouvelle n'est identifiée : pas de formulaire, déclaration de refus, calendrier ou envoi substitutif ; la convention et l'entretien existaient déjà.",
 [effect('obligation_removed', 'bail-glissant-fin-transmission-prefet',
    "Retrait de la transmission générale anticipée au préfet sur l'offre ou le refus de bail direct.",
    "Deux mois avant l'échéance de chaque période d'examen, indication au préfet de l'offre de bail ou des motifs du refus.",
    'Aucun envoi sur ce seul fondement ; examen périodique contradictoire et convention tripartite conservés.',
    'legal_duty', 'Organismes HLM, personnes morales locataires et sous-locataires relevant du bail glissant visé par cet article.',
    "Envois futurs y compris conventions et périodes d'examen en cours ; droits et engagements antérieurs préservés.",
    "l'organisme défini à l'article L. 411-2 indique au représentant de l'Etat dans le département où est situé le logement s'il propose un bail au sous-locataire et, dans la négative, les motifs de cette décision.",
    "aucune transmission au représentant de l'Etat n'est exigée sur le seul fondement du présent article")],
 removed=["Transmission obligatoire au préfet deux mois avant chaque échéance d'examen de la proposition de bail au sous-locataire ou des motifs de l'absence de proposition."])

record('L442-8-3-1', None,
 "Maintien intégral nécessaire : la faculté de facturer les meubles est encadrée par leur coût, leur amortissement et un plafond égal au loyer. Retirer ce plafond ou le tarif réglementé pourrait augmenter la charge des occupants, notamment après l'ouverture de la location meublée par L442-8. L'arrêté fixe une règle générale de prix, sans agrément ou dépôt individuel à supprimer dans cet article.",
 "Les trois alinéas sont conservés, y compris la faculté de révision du seul prix des meubles dans les conditions de l'arrêté. Le plafond ne devient pas une autorisation de doubler automatiquement le loyer : le prix fixé selon l'amortissement s'applique aussi. L'arrêté extérieur n'est pas fourni intégralement ; aucune formule ou montant n'est inventé.",
 "Le régime de majoration pour les meubles et son plafond protecteur sont maintenus intégralement ; aucune baisse nouvelle du prix des meubles n'est revendiquée.",
 "L'article ne permet pas de calculer un prix effectif sans l'arrêté applicable, le coût et l'amortissement des meubles. Il ne modifie pas le loyer principal ou les autres plafonds sociaux.",
 "Aucune charge nouvelle n'est identifiée : aucune évaluation, pièce, autorisation ou échéance n'est ajoutée au mécanisme réglementaire existant.")

record('L442-8-4', None,
 "Maintien intégral nécessaire de la faculté de colocation sociale et de ses garanties : demande volontaire, bail individuel, plafonds appréciés par contrat, décence, plafond global des loyers et forfait de charges optionnel sans régularisation. L'individualisation du bail protège chaque occupant ; elle n'est pas un doublon administratif à supprimer. Aucun agrément ni reporting spécial sans utilité n'est ajouté par cette source.",
 "Les six alinéas fonctionnels sont conservés à leur place : L442-8-1-2 II exclut précisément la première phrase du troisième alinéa pour sa colocation particulière. La somme des loyers ne peut dépasser le loyer conventionné de L353-2 ou celui de L442-1. Le forfait ne doit pas devenir obligatoire et demeure fondé sur les montants récupérables de l'article 23 de la loi de 1989, sans disproportion manifeste. Les références I et II de l'article 8-1 et article 40 de cette loi restent à leur champ propre, hors code du travail.",
 "L'autorisation dérogatoire de colocation et ses limites favorables sont maintenues sans réduction nouvelle ni fusion de baux susceptible d'affaiblir les droits individuels.",
 "Les plafonds, la décence et les règles locatives extérieures demeurent nécessaires ; l'effet du forfait dépend du contrat et des charges réelles, sans économie chiffrée établie.",
 "Aucune charge nouvelle n'est identifiée : contrats individuels et plafonds existent déjà ; ni condition d'emploi, ni registre, ni procédure nouvelle n'est créé.",
 benefit="La faculté de colocation demandée par les intéressés, meublée ou non, est maintenue pour les demandes futures. Les plafonds de ressources restent appréciés par contrat, la somme des loyers demeure plafonnée et le forfait de charges reste facultatif, sans complément ni régularisation et sans disproportion manifeste. Le maintien des alinéas permet de conserver aussi l'exception favorable de L442-8-1-2 II.")

n = 'L442-10'
p = by_num[n]['source_xml']
p = replace(p, "gérés par un organisme d'HLM Le plafond de ressources à prendre en compte pour l'application de l'article L. 441-3 est", "gérés par un organisme d'HLM. Pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, le plafond de ressources à prendre en compte pour l'application de l'article L. 441-3 est")
p += "<p>Aucun des renvois du présent article ne peut fonder un supplément de loyer de solidarité, une enquête ou une formalité exclusivement liée à ce supplément pour une période d'occupation à compter de cette entrée en vigueur. Pour les périodes antérieures, les règles de liquidation, de plafonnement, d'exemption, de régularisation, de restitution, de prescription et de recours demeurent applicables, y compris lorsque la liquidation ou le paiement intervient après cette date. Pour une période d'occupation à cheval sur cette date, seule sa fraction antérieure peut donner lieu au supplément.</p>"
record(n, p,
 "Coordination nécessaire de l'extension du supplément de loyer supprimé : rend inopérants les renvois pour les périodes nouvelles et réserve expressément le plafond majoré de 50 % aux anciennes périodes encore liquidables. Les autres extensions des règles locatives et d'accession, y compris leur champ historique de 1928 et les logements publics gérés par les organismes, restent intactes. La suppression n'est pas comptée une seconde fois.",
 "Le plafond majoré de 50 % bénéficie aux locataires des logements construits sous la loi du 13 juillet 1928 dans le champ exact de la source ; il reste opposable pour tous suppléments anciens liquidés ultérieurement. La disparition du supplément futur rend ce plafond sans objet pour l'avenir, sans taxe ni majoration de remplacement. Les plages L442-1 à L442-9, chapitres Ier/II titre IV livre IV, sections I/II chapitre III de ce titre et section II chapitre III titre V livre III sont toutes conservées. Le point absent après HLM dans la source est ajouté à l'occasion de cette coordination, sans lui attribuer de gain matériel. L442-7 du présent lot est maintenu et n'importe pas le préavis professionnel.",
 "L'extension par renvoi ne peut plus rétablir le supplément supprimé pour les périodes nouvelles. Le plafond favorable des périodes anciennes et toutes les autres extensions légales demeurent.",
 "Il s'agit d'une exécution de la mesure commune de suppression du supplément, sans nouvelle baisse autonome ni chiffrage. Les loyers, aides, attributions et cessions conservent leurs régimes distincts.",
 "Aucune charge nouvelle n'est identifiée : ni nouveau recensement, ni nouveau plafond défavorable, ni préavis ou justificatif d'emploi n'est créé par la limitation temporelle du renvoi.",
 [effect('coordination', SLS,
    "Neutralisation de l'extension future du supplément et conservation du plafond historique majoré.",
    'Renvoi à L441-3 pour le parc visé ; plafond de ressources supérieur de 50 % pour les locataires du champ de la loi du 13 juillet 1928.',
    'Aucun supplément pour les nouvelles périodes ; même plafond majoré de 50 % pour les seules périodes anciennes liquidables, sans remplacement.',
    'regime', 'Locataires des logements HLM et publics visés, notamment logements construits sous la loi du 13 juillet 1928.',
    'Frontière par période d’occupation, non par date de paiement ; restitutions, exemptions et recours anciens maintenus.',
    "Le plafond de ressources à prendre en compte pour l'application de l'article L. 441-3 est",
    "Pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, le plafond de ressources à prendre en compte pour l'application de l'article L. 441-3 est")],
 impact_class='coordination_only')

record('L442-11', None,
 "Maintien intégral nécessaire : les logements OPAH et les logements privés vacants depuis plus d'un an pris en gérance HLM doivent rester décents, à loyers plafonnés et attribués sous conditions sociales. Ces règles protègent les occupants et la destination des interventions HLM ; elles ne prescrivent aucun dossier ou agrément individuel supplémentaire. Leur retrait pourrait augmenter les loyers et réduire la protection contre l'habitat indigne.",
 "Le délai de vacance de plus d'un an délimite ici une catégorie de logements privés gérés, sans imposer au propriétaire d'attendre avant toute location. Le supprimer isolément pourrait étendre des plafonds contraignants à une autre population et ne constitue donc pas un allègement démontré. L303-1 et l'article 6 de la loi du 6 juillet 1989 gardent leur champ. La voie de rénovation de vingt-quatre mois exige une réforme distincte de la loi de 1989 et ne résulte pas de cet article.",
 "La décence et les plafonds sociaux restent entiers ; aucun allègement supplémentaire n'est établi par une modification de cette source.",
 "L'article ne chiffre pas le loyer plafonné ni les aides à l'amélioration et ne réforme pas les normes énergétiques ou les procédures d'impayés hors du lot.",
 "Aucune charge nouvelle n'est identifiée : les exigences de décence, de loyer et de ressources sont conservées, sans nouvelle autorisation ou demande de pièces.")

n = 'L442-12'
p = replace(by_num[n]['source_xml'], "Sont considérées comme personnes vivant au foyer au titre des articles L. 441-1, et L. 441-4 ;", "Sont considérées comme personnes vivant au foyer au titre de l'article L. 441-1 et, pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, de l'article L. 441-4 :")
record(n, p,
 "Coordination nécessaire : réserve le renvoi à la définition du foyer pour le plafonnement du supplément aux seules périodes anciennes, puisque ce supplément est supprimé pour l'avenir. Les six catégories du foyer et leur application autonome à l'attribution des logements par L441-1 restent strictement inchangées. Aucune reformulation des catégories ni restriction des enfants hébergés n'est opérée.",
 "L441-4 officiel, lu avec le projet de L441-3, plafonne le supplément à 30 % des ressources et prévoit un plafond au mètre carré dans son champ particulier : cette définition du foyer reste utile aux anciennes créances même liquidées plus tard. Conserver les références fiscales distinctes 194, 196, 196 A bis et 196 B et les enfants avec droit de visite et d'hébergement. Aucun renvoi au code du travail ou condition d'emploi n'est ajouté. La coordination future de L441-4 reste à effectuer dans son propre article, sans fermeture des plafonds anciens.",
 "La définition continue de servir l'attribution sociale et les anciens plafonnements ; la référence au supplément ne fonde plus d'application aux nouvelles périodes. Aucun nouveau prélèvement ou avantage n'est créé.",
 "La règle n'élargit ni ne rétrécit les catégories du foyer. Les modalités de calcul fiscales et le corps de L441-4 ne sont pas réécrits ici ; la mesure de supplément reste unique.",
 "Aucune charge nouvelle n'est identifiée : aucune catégorie, donnée, attestation ou vérification d'emploi n'est ajoutée à la définition existante.",
 [effect('coordination', SLS,
    'Limitation temporelle du renvoi au plafonnement du supplément dans la définition du foyer.',
    'Définition commune pour L441-1 et L441-4 sans réserve temporelle dans cet article.',
    'Mêmes six catégories pour L441-1 ; application à L441-4 pour les seules anciennes périodes d’occupation.',
    'regime', 'Foyers des locataires HLM concernés par l’attribution et par les anciennes créances de supplément.',
    'Périodes anciennes conservées sans dépendre de la date de liquidation ou de paiement ; application future à L441-1 intacte.',
    "Sont considérées comme personnes vivant au foyer au titre des articles L. 441-1, et L. 441-4",
    "Sont considérées comme personnes vivant au foyer au titre de l'article L. 441-1 et, pour les seules périodes d'occupation antérieures à l'entrée en vigueur de la loi portant la présente réforme, de l'article L. 441-4")],
 impact_class='coordination_only')

n = 'L443-1'
p = "<p>Les conditions auxquelles doivent satisfaire les bénéficiaires des opérations d'accession à la propriété en ce qui concerne le montant des ressources, les conditions d'occupation et l'apport personnel sont fixées par décision de l'autorité administrative.</p><p>Aucun apport personnel minimal ne peut être imposé aux bénéficiaires sur le fondement du présent article. Cette suppression s'applique aux demandes et opérations nouvelles ainsi qu'aux demandes en cours à la date d'entrée en vigueur de la loi portant la présente réforme. Elle ne modifie pas les actes et engagements de financement valablement conclus avant cette date. Les plafonds d'apport personnel et les autres modalités plus favorables aux bénéficiaires, les conditions de ressources et d'occupation plus favorables ainsi que les aides légalement applicables restent ouverts aux situations futures éligibles. Les règles autonomes de solvabilité et les conditions de financement librement convenues conservent leur régime, sans qu'une décision administrative puisse rétablir l'apport minimal supprimé sur ce seul fondement.</p>"
p = replace(p, "restent ouverts aux situations futures éligibles", "demeurent applicables aux situations futures éligibles")
record(n, p,
 "Réforme de fond : supprime l'habilitation à imposer administrativement un apport personnel minimal pour l'accession. Le ciblage des ressources et de l'occupation reste la condition sociale utile ; aides et conditions favorables sont préservées pour les futurs accédants. La suppression n'est pas remplacée par une preuve de fonds ou une autorisation nouvelle et ne crée pas un droit à un prêt sans examen de solvabilité.",
 "R443-1 lu confie la décision à un arrêté conjoint des ministres construction, finances et santé : coordonner ses minima d'apport, sans abroger ses plafonds et faveurs de ressources/occupation. L'habilitation pour les autres modalités d'apport reste écrite et les éventuels plafonds ou conditions d'apport plus favorables sont expressément préservés pour l'avenir : la source ne démontre pas leur existence ni leurs valeurs, aussi aucune formule n'est inventée. Le texte entier de l'arrêté n'est pas fourni. Les financements et prêts antérieurs ne sont pas annulés ; L443-2 et L443-4 gardent leurs champs. Un apport volontaire reste possible.",
 "L'apport personnel minimal ne peut plus être une condition administrative de l'accession au titre de cet article. Les autres critères sociaux demeurent ; l'effet financier dépend des financements réellement proposés.",
 "Le niveau des minima administratifs et la population effectivement bloquée ne sont pas documentés. L'examen autonome de solvabilité et les conditions contractuelles de prêt peuvent encore exiger des fonds propres.",
 "Aucune charge nouvelle n'est identifiée : aucun justificatif de solvabilité nouveau n'est créé, aucun nouveau taux ou condition de prêt n'est fixé ; les règles autonomes déjà applicables sont réservées.",
 [effect('obligation_removed', 'accession-hlm-fin-apport-minimal-administratif',
    "Suppression de l'apport personnel minimal imposé par décision administrative pour l'accession.",
    "L'autorité fixe les conditions relatives aux ressources, à l'occupation et à l'apport personnel ; montant non indiqué dans la source.",
    "Aucun apport minimal imposé sur ce fondement ; ressources et occupation maintenues ; financement volontaire et règles autonomes distincts.",
    'legal_duty', "Bénéficiaires d'opérations d'accession relevant de L443-1.",
    "Demandes futures et en cours dès entrée en vigueur ; actes et engagements de financement antérieurs préservés.",
    "en ce qui concerne le montant des ressources, les conditions d'occupation et l'apport personnel",
    "Aucun apport personnel minimal ne peut être imposé aux bénéficiaires sur le fondement du présent article.")],
 removed=["Pouvoir de fixer un apport personnel minimal administratif comme condition d'accès aux opérations d'accession à la propriété relevant de cet article."])

record('L443-2', None,
 "Maintien intégral nécessaire de l'assurance décès garantissant les annuités des avances d'Etat : elle protège le remboursement de fonds publics et évite que le décès laisse le financement du logement sans couverture. Les solutions favorables d'assurance sur conjoint ou tiers en cas de refus et de contrat collectif par les organismes sont conservées. Il ne s'agit ni d'un impôt sur la succession ni d'un capital taxé au décès.",
 "Quatre alinéas conservés : risque couvert limité aux annuités restant à échoir au décès, substitution possible avec engagement solidaire, faculté collective HLM et sociétés de crédit immobilier, décret d'application. R443-3, R443-5 et R443-6 lus : libre organisme habilité dans le cadre tarifaire prévu, substitution pour risque de santé ou professionnel et faculté de résiliation avec restitution de provision restent distincts. La suppression fiscale des successions n'efface ni dette civile ni contrat d'assurance. Aucun nouveau contrôle de santé ou taux de prime n'est introduit.",
 "Le dispositif de couverture des avances publiques et ses solutions alternatives favorables sont conservés ; aucune suppression de prime ou d'impôt n'est revendiquée.",
 "Les primes, les garanties effectives et les conditions assurantielles ne sont pas chiffrées. Les donations, transmissions civiles et impôts sur capitaux décès relèvent d'autres textes.",
 "Aucune charge nouvelle n'est identifiée : l'assurance et l'engagement solidaire ne sont pas étendus ; les options protectrices existantes ne deviennent pas des obligations supplémentaires.")

n = 'L443-4'
p = "<p>Les prêts consentis en vue des opérations d'acquisition, de grosses réparations, d'aménagement et d'assainissement des habitations rurales sont garantis, soit par une assurance en cas de décès, soit par une hypothèque sans condition légale de premier rang, soit par une caution solvable.</p><p>La suppression de la condition légale de premier rang s'applique aux prêts conclus à compter de l'entrée en vigueur de la loi portant la présente réforme. Elle n'impose pas au prêteur d'accepter une garantie insuffisante et ne crée pas un droit à l'octroi d'un prêt. Les contrats, sûretés, rangs et droits des créanciers constitués antérieurement restent inchangés ; aucune radiation ni modification d'inscription ne résulte de cette suppression.</p>"
record(n, p,
 "Réforme de fond ciblée : retire le premier rang hypothécaire imposé par la loi, obstacle possible au financement d'un logement rural déjà grevé. L'obligation de garantie et les trois options assurance décès, hypothèque ou caution solvable subsistent. Le prêteur garde l'appréciation d'une garantie suffisante ; aucune assurance ou procédure équivalente nouvelle ne remplace la condition de rang supprimée.",
 "Les quatre types d'opérations et le champ rural restent identiques. Les nouveaux prêts peuvent être couverts par une hypothèque d'un autre rang sans modification forcée des contrats ou inscriptions anciens. Les règles civiles de constitution, de publicité, de rang et de réalisation des sûretés ne sont pas réécrites. La suppression de la contribution de sécurité immobilière est une mesure fiscale distincte, non un effet supplémentaire de cet article. Le risque de crédit et le gain effectif des emprunteurs restent à évaluer.",
 "Le premier rang n'est plus une condition légale de l'option hypothécaire des nouveaux prêts ruraux ; la garantie reste obligatoire avec les alternatives initiales.",
 "Les prêteurs peuvent encore demander un premier rang contractuellement selon le risque ; aucune baisse certaine des primes, intérêts ou frais n'est démontrée, et aucune sûreté antérieure n'est déplacée.",
 "Aucune charge nouvelle n'est identifiée : pas de registre ou d'évaluation obligatoire substitutive, pas de transfert forcé de rang ; l'exigence de garantie existe déjà dans la source.",
 [effect('obligation_removed', 'accession-rurale-fin-premier-rang-legal',
    "Suppression du rang hypothécaire légalement imposé, sans disparition de la garantie des prêts ruraux.",
    "Garantie par assurance décès, hypothèque obligatoirement de premier rang ou caution solvable, pour les opérations rurales énumérées.",
    "Mêmes garanties alternatives ; hypothèque sans premier rang légal obligatoire pour les nouveaux prêts, sous réserve de l'accord du prêteur.",
    'legal_duty', "Emprunteurs et prêteurs finançant l'acquisition, les grosses réparations, l'aménagement et l'assainissement d'habitations rurales.",
    'Nouveaux prêts dès entrée en vigueur ; sûretés et rangs des prêts antérieurs protégés.',
    "soit par une hypothèque de premier rang",
    "soit par une hypothèque sans condition légale de premier rang")],
 removed=["Obligation légale de constituer l'hypothèque au premier rang lorsque cette forme de garantie est choisie pour un nouveau prêt rural visé par l'article."])

record('L443-6', None,
 "Maintien intégral de l'avantage de sûreté et de recouvrement reconnu aux sociétés de crédit immobilier. Supprimer cet article en raison de l'ancienneté de ses références pourrait retirer un droit favorable ou affecter des prêts et tiers sans démonstration d'un doublon. L'article n'institue ni taxe, ni autorisation, ni dépôt nouveau à enlever. Aucune reformulation stylistique n'est produite.",
 "La référence vise le décret du 28 février 1852 et la loi du 10 juin 1853, non un contrat d'emploi. Leur texte et leurs éventuelles concordances hors des cinq codes ne sont pas fournis ici. Portée actuelle des privilèges et éventuelle codification au code monétaire et financier à vérifier avant une substitution de référence ; aucune abrogation ou équivalence n'est présumée. Cette réserve documentaire n'est pas présentée comme une filiation historique achevée ni comme un examen de tous les privilèges extérieurs.",
 "L'avantage légal de sûreté et de recouvrement reste intégral ; aucun allègement nouveau ou suppression de prélèvement n'est établi.",
 "La portée des textes historiques extérieurs et leur articulation contemporaine restent documentaires. Aucun montant recouvrable ni droit nouveau au détriment de l'emprunteur n'est déduit de ce maintien.",
 "Aucune charge nouvelle n'est identifiée : le texte est inchangé et ne crée aucun titre, garantie, déclaration ou délai de recouvrement supplémentaire.")

n = 'L443-6-1'
p = by_num[n]['source_xml']
p = replace(p, "Dans ce cas, il verse les frais de liquidation fixés par cet arrêté.", "Pour ces contrats, aucun frais de liquidation n'est dû lorsque le fait générateur de ces frais intervient à compter de l'entrée en vigueur de la loi portant la présente réforme.")
p += "<p>La suppression des frais de liquidation ne permet ni majoration des frais de gestion ni prélèvement de remplacement. Les créances de frais de liquidation légalement nées à raison de faits générateurs antérieurs à cette entrée en vigueur, y compris si leur exigibilité ou leur paiement est ultérieur, restent régies par les dispositions antérieures, avec leurs droits, options, prescriptions et recours. Aucun remboursement général des frais antérieurement dus n'est institué. Le taux réduit des frais de gestion et l'option plus favorable selon la situation de l'accédant demeurent applicables aux contrats relevant du présent article, sans nouveau contrat ni nouvelle condition d'emploi.</p>"
record(n, p,
 "Réforme de fond limitée au stock historique : supprime les frais de liquidation dont le fait générateur est futur pour les contrats non échus au 1er juin 1992, en conservant le taux réduit de frais de gestion. L'option alternative à la demande de l'accédant, sa révision plafonnée par l'ICC et l'absence de frais de liquidation liée à cette option restent entières. Les liquidations et paiements légalement dus des anciennes cohortes ne sont pas annulés.",
 "Quatre alinéas historiques gardés à leur place, seul paiement obligatoire futur du troisième retiré, puis transition ajoutée. Contrats en cours au 13 novembre 1974 ; échéance, absence de recours et paiement au 1er juin 1992 du deuxième alinéa conservés exactement. L'arrêté du 13 novembre 1974 n'est pas intégralement fourni : ni taux de frais ni assiette ou fait générateur précis supplémentaires ne sont inventés. La frontière suit le fait générateur légal, non la seule date de paiement ; il faut vérifier l'existence de contrats encore concernés avant tout chiffrage. La non-restitution du deuxième alinéa ne ferme pas un recours autonome pour indu ou illégalité hors de son champ. Aucun lien avec une indemnité de licenciement.",
 "Le droit de percevoir de nouveaux frais de liquidation sur la cohorte du troisième alinéa disparaît ; les frais de gestion réduits restent. Le gain pratique dépend de l'existence de faits générateurs encore futurs dans ce stock historique.",
 "Ni le nombre de contrats survivants ni le montant fixé par l'arrêté ne sont établis. Aucune économie immédiate n'est affirmée pour les contrats déjà liquidés ou les créances légalement nées avant la réforme.",
 "Aucune charge nouvelle n'est identifiée : ni calcul alternatif imposé, ni frais de gestion relevé, ni déclaration de substitution. L'option existante reste facultative et les dettes anciennes gardent leur droit.",
 [effect('compliance_cost_reduced', 'accession-historique-fin-frais-liquidation',
    "Suppression des nouveaux frais de liquidation de la cohorte non échue au 1er juin 1992, avec frais de gestion réduits conservés.",
    "Contrats HLM en cours au 13 novembre 1974 et non échus au 1er juin 1992 : taux réduit de gestion mais frais de liquidation fixés par arrêté, montant non donné par la source.",
    "Même taux réduit de gestion, zéro frais de liquidation pour un fait générateur futur, sans frais de remplacement ; créances nées auparavant conservées.",
    'euro', "Accédants de la cohorte historique du troisième alinéa, dans la mesure où des faits générateurs de frais restent futurs.",
    "Suppression à compter de l'entrée en vigueur selon le fait générateur, sans restitution générale ni annulation des créances antérieures.",
    "Dans ce cas, il verse les frais de liquidation fixés par cet arrêté.",
    "Pour ces contrats, aucun frais de liquidation n'est dû lorsque le fait générateur de ces frais intervient à compter de l'entrée en vigueur de la loi portant la présente réforme.")],
 removed=["Obligation de payer des frais de liquidation pour les faits générateurs futurs des contrats encore non échus au 1er juin 1992, sans retrait du taux réduit de gestion."],
 benefit="Le taux réduit des frais de gestion applicable depuis l'arrêté du 13 novembre 1974 reste acquis et applicable jusqu'à l'extinction des contrats éligibles. L'option demandée par l'accédant en cas de désaccord, le plafonnement annuel à la variation de l'ICC et la non-exigibilité des frais de liquidation dans cette option sont conservés mot pour mot. La cohorte de 1974 est un régime fermé par la source elle-même ; aucun bénéficiaire encore éligible n'en est exclu par une date nouvelle.")

n = 'L443-6-3'
p = by_num[n]['source_xml']
p = replace(p, "à des personnes physiques qui doivent simultanément acquérir des parts de ces sociétés.", "à des personnes physiques sans que la location puisse être subordonnée à l'acquisition simultanée de parts de ces sociétés. L'acquisition de parts demeure facultative et peut intervenir ultérieurement dans les conditions applicables à la société.")
p += "<p>La suppression de l'acquisition simultanée obligatoire s'applique aux locations conclues à compter de l'entrée en vigueur de la loi portant la présente réforme et aux demandes de location en cours. Aucune acquisition différée obligatoire ni formalité de remplacement ne peut être imposée sur ce seul fondement. Elle ne modifie ni les parts et droits sociaux antérieurement acquis ni les conditions de constitution, de pluralité des associés et de dissolution des sociétés. Les aides, prêts et garanties légalement applicables restent ouverts aux futures opérations éligibles. La location sans acquisition de parts ne confère pas la qualité d'associé ; l'accès ultérieur à cette qualité conserve son régime.</p>"
record(n, p,
 "Réforme de fond : retire le financement forcé d'une acquisition de parts au même instant que l'entrée dans un logement vacant de la SCI. La location sociale peut précéder une acquisition volontaire. Créateurs HLM, prêts aidés, associés autorisés, gérance HLM, plafonds et règles locatives, exclusion de L442-5 et catégorie d'immeubles demeurent. La modification ne transforme pas le locataire sans parts en associé et ne fait pas disparaître les garanties attachées à des parts effectivement acquises.",
 "Les cinq alinéas fonctionnels restent dans l'ordre, transition ajoutée. L443-6-2, L443-6-5, L443-6-6 et R443-9-1 à R443-9-4 lus : la location peut exister sans qualité d'associé ; l'acquisition ultérieure reste conditionnée à la régularité des obligations locatives dans L443-6-5. L'annexe entière à R443-9-4 a été lue en trois plages continues ; confronter ses articles 5/6, 9/10, 17/19 et 25 lors de la coordination réglementaire, sans imposer de parts minimales différées. L'article 25 prévoit la dissolution si tous les associés personnes physiques reviennent au statut de locataires ; cette cause n'est pas supprimée ici. La pluralité nécessaire des associés et l'entrée volontaire d'associés lors de la constitution sont réservées, sans contourner une dissolution obligatoire. L'évaluation et les pièces patrimoniales de L443-6-4 sont conservées. Aucun gain n'est attribué à la simple exclusion de L442-5 déjà inscrite dans la source.",
 "La condition d'achat simultané de parts pour louer les logements vacants apportés disparaît ; l'accession progressive et les garanties de rachat restent disponibles pour les acquisitions volontaires.",
 "La règle ne permet pas une SCI sans pluralité d'associés et ne neutralise pas sa dissolution. Montant des parts évitées à l'entrée, coût du portage par l'organisme et effet sur le financement ne sont pas chiffrés.",
 "Aucune charge nouvelle n'est identifiée : aucun achat différé obligatoire, registre ou déclaration de remplacement ; constitution et gestion sociale restent à leurs conditions antérieures, sans nouveaux droits sociaux imposés aux locataires.",
 [effect('obligation_removed', 'sci-accession-fin-achat-parts-simultane',
    "Suppression de l'achat simultané de parts comme condition d'entrée en location dans les logements vacants apportés.",
    'Les personnes physiques qui louent un logement libre apporté à la SCI doivent acquérir des parts au même moment.',
    "Location possible sans acquisition simultanée ; acquisition ultérieure volontaire selon le régime existant, sans qualité d'associé automatique.",
    'legal_duty', "Locataires entrants des logements libres apportés à une SCI d'accession progressive légalement constituée.",
    "Nouveaux baux et demandes en cours dès entrée en vigueur ; droits sur parts acquises, pluralité d'associés et dissolution conservés.",
    "à des personnes physiques qui doivent simultanément acquérir des parts de ces sociétés.",
    "à des personnes physiques sans que la location puisse être subordonnée à l'acquisition simultanée de parts de ces sociétés.")],
 removed=["Obligation faite au locataire entrant d'acquérir simultanément des parts sociales pour pouvoir louer un logement vacant apporté à la SCI d'accession progressive."])

record('L443-6-4', None,
 "Maintien intégral nécessaire des pièces qui identifient les lots, les quotes-parts et les droits de jouissance et limitent les restrictions statutaires. L'évaluation indépendante du service des domaines et la conformité de la valeur d'apport évitent une valorisation arbitraire des actifs sociaux et des parts que les locataires acquièrent et peuvent faire racheter. Aucune double évaluation n'est prescrite ici ; sa suppression sans garantie équivalente démontrée affaiblirait la protection patrimoniale.",
 "Les quatre alinéas sont maintenus : état descriptif, règlement conforme à la loi du 10 juillet 1965, annexion aux statuts et évaluation préalable. L'annexe entière à R443-9-4 lue confirme à son article 5 la mention de l'évaluation domaniale, aux articles 6 et 19 le lien avec le capital et les parts nominales, et à l'article 20 leur rachat garanti. L443-6-6 lu impose cette garantie ; la valorisation engage donc les occupants et l'organisme. La loi de copropriété et le droit civil extérieurs ne sont pas présentés comme intégralement réécrits. L'état et le règlement n'ont pas un contenu identique : les fusionner sans préserver les fonctions et l'opposabilité n'est pas un allègement démontré.",
 "Les garanties de délimitation, de droits de jouissance et de valorisation des apports restent entières. Aucun avis supprimé ou coût net réduit n'est revendiqué.",
 "Le coût et le délai de l'évaluation ne sont pas documentés ; aucun double contrôle équivalent inutile n'est établi. Les formalités civiles de copropriété et les droits des tiers conservent leur régime.",
 "Aucune charge nouvelle n'est identifiée : aucun expert, document, exemplaire, autorisation ou délai supplémentaire n'est ajouté aux quatre alinéas conservés.")

checks = {
 'L442-5': {
  'L1234-1': "L442-5 régit une enquête d'occupation et son délai d'un mois, non le préavis de licenciement de L1234-1. Le préavis de quinze jours des nouveaux contrats privés et les anciennes durées liées à l'ancienneté ne remplacent aucun délai statistique ; aucun renvoi professionnel n'est créé.",
  'L1221-2': "La collecte sur les occupants majeurs n'est pas un régime d'embauche. L442-5 ne renvoie pas au CDI ou au CDD : le contrat unique de L1221-2, l'interdiction de terme nouveau et la transition des anciens contrats ne modifient pas les personnes logées ni leurs avantages.",
  'L1234-9': "La pénalité statistique de 7,62 euros n'est pas une indemnité de rupture. Le seuil professionnel d'un an au terme effectif avec préavis, les 0,20 mois par année totale et le plafond de six mois sont sans application à l'enquête ; aucune indemnité spéciale ou créance salariale n'est retirée.",
  'L441-9': "La proposition de L441-9 conserve les demandes annuelles nécessaires à la RLS et à L442-3-3, le délai d'un mois et les dispenses pour bénéficiaires d'aides ; elle réserve le supplément et sa liquidation provisoire aux anciennes périodes. L442-5 retire sa propre enquête obligatoire, laisse réemployer les données légalement disponibles et ne rétablit ni enquête exclusivement SLS ni sanction pour les périodes nouvelles."
 },
 'L442-5-1': {
  'L1234-1': "L'examen du parcours résidentiel n'est ni une rupture d'emploi ni un congé locatif. Le préavis patronal de quinze jours du contrat unique et les anciennes durées selon l'ancienneté de L1234-1 sont inapplicables ; ils ne justifient aucun délai nouveau d'entretien ou de relogement.",
  'L1221-2': "Le parcours et l'information sur l'accession de L442-5-1 ne dépendent pas de la forme du contrat de travail. Aucun renvoi au CDD n'est présent ; le nouveau CDI unique et la conservation des anciens contrats ne limitent pas l'accès des futurs locataires à cet accompagnement.",
  'L1234-9': "L442-5-1 ne calcule aucune indemnité professionnelle. Le seuil d'un an à la fin effective préavis inclus, le prorata en mois complets de l'ancienneté totale et les six mois plafonnés de L1234-9 ne sont pas transposables à la mobilité locative ; les anciens droits de travail restent distincts.",
  'L441-9': "La source officielle de L441-9 portait une enquête pour le supplément ; sa proposition la conserve pour RLS et L442-3-3 avec les dispenses et droits anciens. Le premier alinéa de L442-5-1 perd seulement le déclencheur SLS : la sous-occupation révélée par une enquête autonome reste pertinente, sans nouvelle enquête générale ni restriction de l'information sur l'accession."
 },
 'L442-6-3': {
  'L1234-1': "Le mois de L442-6-3 est un préavis locatif de départ vers un autre logement du même bailleur, calculé selon le régime du congé locatif, non une durée liée à l'ancienneté chez un employeur. Les quinze jours professionnels de L1234-1 ne le remplacent pas ; l'avantage d'un mois demeure pour les futures mutations éligibles.",
  'L1221-2': "Le bénéfice du préavis locatif réduit repose sur l'attribution du second logement et le même bailleur, non sur un CDI ou CDD. L1221-2 et son contrat unique ne sont pas visés ; ni la fin d'une mission ni la transition d'un ancien emploi ne conditionnent ce droit au logement.",
  'L1234-9': "Aucune indemnité de rupture n'est instituée par ce préavis locatif. L'ancienneté d'un an appréciée à la fin effective avec préavis, les 0,20 mois par année totale et le plafond de six mois de L1234-9 n'ont aucun effet sur le congé d'un mois ou sur l'accès au second logement."
 },
 'L442-6-5': {
  'L1234-1': "L442-6-5 traite d'un protocole après résiliation judiciaire du bail pour impayés ; ses deux ans, trois ans de prolongation et trois mois de rétablissement ne sont pas des préavis d'emploi. Les quinze jours de L1234-1 ne modifient ni la procédure judiciaire ni ces garanties locatives.",
  'L1221-2': "Le protocole d'occupation à durée limitée n'est pas un CDD et ne fixe pas la durée de l'emploi. L1221-2 ne commande donc aucune transformation de ces deux ans en CDI ; allocations, rappels d'aide, accompagnement et accès futur au protocole restent indépendants du type de contrat de travail.",
  'L1234-9': "L'indemnité d'occupation et les arriérés locatifs ne sont pas l'indemnité ordinaire patronale de L1234-9. Le seuil d'un an au terme effectif préavis inclus, les 0,20 mois par année totale et les droits des anciens salariés ne réduisent ni ces dettes ni les aides ; l'approbation retirée est seulement locative."
 },
 'L442-7': {
  'L1234-1': "Le préavis minimal de six mois part de la notification au locataire par le bailleur de la décision de l'employeur ; il est distinct du préavis professionnel de quinze jours de L1234-1. Les autorisations et procédures d'emploi restent autonomes, et les agents publics ne relèvent pas automatiquement de ce préavis privé.",
  'L1221-2': "La clause doit viser l'emploi effectivement exercé ; sa fin n'est pas créée par un terme de mission ou de formation. Le contrat unique de L1221-2 ne peut être raccourci par le bail : seules les fins de fonctions régulièrement intervenues permettent la demande locative. Agents publics et anciens emplois conservent leurs régimes propres.",
  'L1234-9': "La clause de fonction ne fixe aucune indemnité de licenciement. Pour les salariés privés concernés, le seuil d'un an à la fin effective préavis inclus et les 0,20 mois par année totale de L1234-9 restent professionnels, avec transition des anciens contrats et indemnités spéciales ; ils ne suppriment ni les six mois locatifs ni les protections de handicap."
 },
 'L442-10': {
  'L1234-1': "L442-10 étend un ensemble de règles locatives au patrimoine HLM ou public ; il ne renvoie pas au préavis d'emploi de L1234-1. Les quinze jours des nouveaux emplois privés ne remplacent aucun préavis du bail, et l'ancienneté du salarié ne délimite pas le parc historique de 1928.",
  'L1221-2': "Les logements acquis ou construits sous législation HLM, y compris le régime de 1928, ne sont pas des contrats de travail. Le renvoi d'ensemble ne crée aucun terme d'emploi contraire à L1221-2 ; contrat unique, anciens CDD et éventuels régimes publics restent hors de cette extension immobilière.",
  'L1234-9': "La majoration de 50 % du plafond de ressources de l'ancien supplément n'est ni un taux d'indemnité ni une condition d'ancienneté. L1234-9 et son seuil à la fin effective préavis inclus ne sont pas applicables à cette majoration ; les droits salariaux anciens et indemnités spéciales restent distincts.",
  'L442-7': "La plage L442-1 à L442-9 comprend L442-7, dont la vue fournie est la source officielle seule, maintenue dans ce lot. La clause facultative de fonction garde son emploi identifié, l'action de l'employeur sous un an, la notification par le bailleur et six mois au moins, ainsi que les protections exceptionnelles et de handicap ; l'extension n'importe pas le préavis de travail."
 },
 'L443-6-1': {
  'L1234-1': "Les échéances du 13 novembre 1974 et du 1er juin 1992 concernent des contrats immobiliers, non l'ancienneté professionnelle ou un préavis. L1234-1 et les quinze jours du contrat unique sont inapplicables ; aucune notification de licenciement ne déclenche les frais de liquidation.",
  'L1221-2': "Les contrats de location-attribution et de vente à terme de L443-6-1 sont des actes d'accession immobilière déjà en cours en 1974, non des CDD. L'interdiction de nouveaux CDD par L1221-2 ne les abroge pas, ne les convertit pas et ne ferme pas leurs taux réduits et options encore applicables.",
  'L1234-9': "Les frais de gestion et de liquidation sont distincts de l'indemnité patronale. L'année d'ancienneté au terme effectif avec préavis, les 0,20 mois par année totale et le plafond de six mois de L1234-9 ne sont pas des règles de liquidation immobilière ; la suppression ciblée de frais respecte les créances antérieures et n'affecte aucune indemnité spéciale."
 }
}

for source in sources:
    n = source['number']
    required = refs['requirements'][source['code_id'] + '|' + source['source_id']]
    assert len(checks.get(n, {})) == len(required), n
    for key in required:
        target = refs['targets'][key]
        answers[n]['reference_checks'].append(dict(target_key=key,
            view_sha256=target['view_sha256'], assessment=checks[n][target['number']]))

assert len(answers) == len(sources) == 24
result = [answers[a['number']] for a in sources]
for a, out in zip(sources, result):
    for key in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert out[key] == a[key]
    imp = out['substantive_impact']
    for key in ['assessment', 'scope_limitations', 'new_burdens_review']:
        assert len(imp[key]) >= 40, (a['number'], key)
    if a['benefit_check_required']:
        assert len(out.get('benefit_review', '')) >= 100, a['number']
    for e in imp['effects']:
        assert re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)+', e['measure_id'])
        assert 6 <= len(e['measure_id']) <= 96
        assert len(e['source_quote']) >= 12 and e['source_quote'] in plain(a['source_xml']), (a['number'], 'source', e['source_quote'])
        assert len(e['proposed_quote']) >= 12 and e['proposed_quote'] in plain(out['proposed_xml']), (a['number'], 'proposed', e['proposed_quote'])
    for check in out['reference_checks']:
        assert len(check['assessment']) >= 80
    for removed in out.get('removed_provisions', []):
        assert len(removed) >= 30
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': len(result)}, ensure_ascii=False))
