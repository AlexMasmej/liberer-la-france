import json
import re
import html
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {s['number']: s for s in sources}
answers = {}


def plain(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))


def ps(*paragraphs):
    return '\n'.join('<p>' + html.escape(p, quote=False) + '</p>' for p in paragraphs)


def effect(kind, measure_id, description, before, after, unit, population,
           transition, burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=population,
                conditions_and_transition=transition,
                replacement_or_new_burdens=burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def put(number, proposed, reason, notes, impact_class, assessment, limitations,
        burdens, effects=None, removed=None, repeal_scope=None, benefit=None):
    s = by_number[number]
    a = {k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    a.update(proposed_xml=proposed, reason=reason, review_notes=notes,
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
    a['substantive_impact'] = dict(
        version=1, classification=impact_class, assessment=assessment,
        scope_limitations=limitations, new_burdens_review=burdens,
        effects=effects or [])
    if benefit is not None:
        a['benefit_review'] = benefit
    answers[number] = a
    return a


# L245-6 : conservation de la liste autonome utile au plafond, au même III A.
s = by_number['L245-6']['source_xml']
paragraphs = re.findall(r'<p>(.*?)</p>', s, re.S)
start = next(i for i, p in enumerate(paragraphs) if 'III.- A.-' in p)
categories = [plain(p) for p in paragraphs[start + 1:start + 8]]
assert len(categories) == 7 and categories[0].strip().startswith('1°') and categories[-1].strip().startswith('7°')
# Le premier renvoi complet à cette loi était dans un bloc d'assiette supprimé.
categories[5] = categories[5].replace(
    "loi n° 2021-1754 du 23 décembre 2021 précitée",
    "loi n° 2021-1754 du 23 décembre 2021 de financement de la sécurité sociale pour 2022")
new0 = ps(
    "I. - A. - La contribution de base est supprimée pour les années civiles commençant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression.",
    "B. - Abrogé pour les années mentionnées au A.",
    "C. - Abrogé pour les années mentionnées au A.",
    "D. - Abrogé pour les années mentionnées au A.",
    "E. - Abrogé pour les années mentionnées au A.",
    "II. - A. - La contribution additionnelle est supprimée pour les mêmes années.",
    "B. - Abrogé pour ces années.",
    "C. - Abrogé pour ces années.",
    "III. - A. - La contribution supplémentaire est supprimée pour les mêmes années. Pour le seul calcul du plafond prévu au E, les spécialités pharmaceutiques retenues sont les suivantes :",
    *categories,
    "B. - Abrogé pour les années mentionnées au I.",
    "C. - Abrogé pour les années mentionnées au I.",
    "D. - Abrogé pour les années mentionnées au I.",
    "E. - Pour les années mentionnées au I, le montant dû par chaque entreprise au titre de la contribution prévue aux articles L. 138-10 à L. 138-16 ne peut excéder 10 % de son chiffre d'affaires en France métropolitaine, en Guadeloupe, en Guyane, en Martinique, à La Réunion, à Saint-Barthélemy et à Saint-Martin, au cours de l'année civile considérée, au titre des spécialités mentionnées au A du présent III, y compris celles qui étaient exclues de l'assiette de la contribution supplémentaire par le B du présent III dans sa rédaction antérieure à la loi portant suppression de cette contribution, après déduction des remises mentionnées aux articles L. 162-16-5-1-1, L. 162-16-5-1-2, L. 162-16-5-2, L. 162-17-5, L. 162-18, L. 162-18-1, L. 162-18-2 et L. 162-22-7-1 et à l'article 62 de la loi n° 2021-1754 du 23 décembre 2021 de financement de la sécurité sociale pour 2022, à l'exclusion de toutes autres remises mentionnées à l'article L. 138-9 du présent code. Ce plafond s'applique également aux entreprises devenant éligibles après la suppression des contributions. Il ne modifie pas les exonérations, déductions, remises et plafonds plus favorables applicables à la contribution prévue aux articles L. 138-10 à L. 138-16.",
    "F. - Aucune remise tenant lieu de la contribution supplémentaire ne peut être exigée pour les années mentionnées au I. Les facultés de versement sous forme de remise prévues par les dispositions antérieures restent ouvertes pour les contributions des années antérieures, selon leurs conditions propres.",
    "IV. - L'exclusion des charges déductibles prévue par le présent IV dans sa rédaction antérieure reste applicable aux seules contributions de base et additionnelle dues au titre des années antérieures à la suppression. La présente loi ne crée aucune déduction d'une contribution supprimée.",
    "V. - A. - Aucune déclaration, taxation d'office ou demande de données exclusivement destinée à établir les contributions supprimées n'est exigible au titre des années mentionnées au I. Les déclarations communes subsistent uniquement pour les prélèvements et les obligations ayant un fondement légal distinct.",
    "B. - Aucune majoration propre aux contributions supprimées ne peut être appliquée au titre de ces années.",
    "VI. - Aucun versement provisionnel ni aucune régularisation des contributions supprimées n'est dû au titre des années mentionnées au I, même sur le fondement d'un renvoi législatif ou réglementaire à ces contributions. Les versements provisionnels effectués sans être dus au titre de ces années sont restitués selon les règles de réclamation applicables, sans déclaration annuelle de remplacement et sans double restitution.",
    "Les contributions dues au titre des années antérieures demeurent régies par les dispositions applicables à ces années, même si leur liquidation, leur régularisation ou leur paiement intervient après la suppression. Sont conservés les exclusions d'assiette, déductions, taux différenciés favorables, plafonds, facultés de remise, affectations à la Caisse nationale de l'assurance maladie, contrôles, recouvrements, restitutions, prescriptions et recours correspondants, sous réserve de l'application de la loi répressive plus douce dans son champ. Aucune restitution générale des contributions légalement dues n'est instituée.",
    "La suppression des trois contributions ne supprime ni les prises en charge des médicaments, ni les autorisations sanitaires, ni les remises et restitutions fondées sur une disposition distincte. Elle n'institue aucun prélèvement de remplacement. Les modifications à entrée en vigueur différée relatives aux contributions supprimées ne peuvent en rétablir l'exigibilité ; le plafond du E du III demeure applicable aux années futures."
)
pharma_transition = "Années civiles commençant le 1er janvier suivant l'entrée en vigueur ; année de bascule et années antérieures conservées ; plafond III E ouvert aux futurs éligibles."
pharma_burdens = "Aucun prélèvement, registre, déclaration, délai ou agrément de remplacement ; conservation du calcul du plafond déjà existant et des contrôles propres aux autres régimes."
pharma_effects = [
    effect('tax_removed', 'pharmacie-contribution-base-suppression',
           'Suppression de la contribution de base sur le chiffre d’affaires pharmaceutique.',
           '0,20 % du chiffre d’affaires HT annuel des médicaments des I B à D, net des remises L138-9 et des ventes à l’étranger ; exclusions génériques et orphelins selon I C.',
           'Aucune contribution de base sur ce chiffre d’affaires pour les années nouvelles ; aucune assiette de remplacement.',
           'percent', 'Entreprises exploitantes, importatrices parallèles et distributrices parallèles relevant du I A.',
           pharma_transition, pharma_burdens,
           'Le taux de la contribution de base est fixé à 0,20 %.',
           "La contribution de base est supprimée pour les années civiles commençant à compter du 1er janvier de l'année suivant celle de l'entrée en vigueur de la loi portant sa suppression."),
    effect('tax_removed', 'pharmacie-contribution-additionnelle-suppression',
           'Suppression de la contribution additionnelle assise sur les spécialités prises en charge du II.',
           '1,6 % du chiffre d’affaires HT annuel métropolitain et ultramarin défini au II B par les conditions des I B à D et les listes du II A.',
           'Aucune contribution additionnelle sur ce chiffre d’affaires pour les années nouvelles.',
           'percent', 'Entreprises du I A commercialisant les spécialités visées au II A.',
           pharma_transition, pharma_burdens,
           'Le taux de la contribution additionnelle est fixé à 1,6 %.',
           'La contribution additionnelle est supprimée pour les mêmes années.'),
    effect('tax_removed', 'pharmacie-contribution-supplementaire-suppression',
           'Suppression du troisième prélèvement sur le chiffre d’affaires pharmaceutique, distinct de la clause de sauvegarde.',
           'Chiffre d’affaires annuel des spécialités du III A, exclusions III B et remises III C ; taux de base et taux différencié sous 50 millions d’euros, dont les valeurs ne sont pas données par cet article ; plafond cumulé de 10 % au III E.',
           'Aucune contribution supplémentaire ni remise de substitution pour les années nouvelles ; clause de sauvegarde distincte toujours plafonnée.',
           'legal_duty', 'Entreprises exploitant, important ou distribuant parallèlement les spécialités du III A.',
           pharma_transition, pharma_burdens,
           'Une contribution supplémentaire à la contribution de base et à la contribution additionnelle, dénommée “ contribution supplémentaire ”, est instituée',
           'La contribution supplémentaire est supprimée pour les mêmes années.'),
    effect('coordination', 'pharmacie-contribution-supplementaire-suppression',
           'Le plafond cumulé est rendu autonome pour empêcher la perte d’un avantage sur la clause de sauvegarde survivante.',
           'Total de la contribution supplémentaire et de la contribution L138-10 à L138-16 limité à 10 % du chiffre d’affaires défini au III E, y compris les spécialités exclues par III B.',
           'La seule contribution survivante conserve la limite de 10 % sur la même base territoriale et matérielle, sans exclusions III B du dénominateur.',
           'percent', 'Entreprises éligibles au plafond du III E, présentes et futures.',
           pharma_transition, pharma_burdens,
           'Le montant total dû par chaque entreprise au titre de la contribution supplémentaire et de la contribution prévue aux articles L. 138-10 à L. 138-16 ne peut excéder 10 % de son chiffre d’affaires'.replace('d’affaires', "d'affaires"),
           "le montant dû par chaque entreprise au titre de la contribution prévue aux articles L. 138-10 à L. 138-16 ne peut excéder 10 % de son chiffre d'affaires")
]
put('L245-6', new0,
    "Réforme de fond : suppression des trois contributions de chiffre d'affaires, au lieu de leur reformulation, ainsi que de leurs acomptes, déclarations, taxation d'office, majorations propres et remises de substitution pour les années nouvelles. Ces prélèvements de rendement se superposent aux mécanismes de prix, de remises et de sauvegarde ; aucune fonction de sécurité sanitaire n'exige leur conservation. Maintien à droit constant des prises en charge et remises autonomes. Le III A et le III E subsistent comme support du plafond favorable de la clause de sauvegarde ; l'article n'est donc pas intégralement abrogé.",
    "Source et notes lues intégralement : rédaction applicable aux contributions 2026, avec fin de version indiquée au 1er janvier 2028, qui n'est pas une date de promulgation du projet. Le premier millésime supprimé dépend de l'entrée en vigueur réelle de la loi ; les contributions de l'année de cette entrée restent dues. Le III A conserve ses sept catégories et le III E son dénominateur, son territoire et tous ses renvois aux remises ; le B supprimé n'exclut pas de spécialités du dénominateur. Les subdivisions I B à E, II B/C et III B à D cessent d'établir une assiette ou un taux ; leurs anciennes règles subsistent pour les anciennes années par la transition du VI. Lecture complémentaire du corpus : L138-10 à L138-16, L138-20, L241-2 IV 6°, R138-19, R245-17 et R245-18. Ces derniers textes, les modèles Urssaf et les modifications différées de L245-6 doivent être coordonnés hors de ce lot pour n'exiger que les anciennes contributions et les prélèvements distincts. Aucun transfert vers une remise CEPS, aucune hausse de M, d'assiette ou de taux de sauvegarde n'est décidée ici pour compenser les recettes supprimées. Le taux de la contribution supplémentaire n'est pas chiffré dans la source : aucun taux n'est inventé. Le coût pour la CNAM et les effets nets sur les autres recettes restent à chiffrer, sans autofinancement présumé. Les textes de santé publique et la loi de financement de 2022 ne sont pas déclarés réécrits. Les cibles de travail requises sont sans rapport normatif avec cette contribution ; aucune condition d'ancienneté n'est ajoutée.",
    'material_reduction',
    "Les trois prélèvements institués par la source entière et leurs obligations propres disparaissent pour les années nouvelles. Le plafond favorable sur le prélèvement distinct de sauvegarde reste opérant ; il ne s'agit ni d'un simple changement de financeur ni d'un report d'impôt à la distribution.",
    "Années antérieures et année d'entrée en vigueur non abolies. Clause de sauvegarde, remises de prix et autorisations sanitaires distinctes maintenues. Coordinations législatives et réglementaires périphériques identifiées mais non rédigées dans ce lot ; incidence budgétaire et solde global inconnus.",
    "Aucune charge nouvelle identifiée : aucun formulaire, registre, justificatif, agrément ou prélèvement de remplacement. Le calcul du plafond utilise son champ antérieur ; les obligations autonomes de remboursement et de contrôle ne sont pas étendues.",
    effects=pharma_effects,
    removed=[
        "Contribution de base de 0,20 % et ses règles d'assiette pour les années civiles nouvelles.",
        "Contribution additionnelle de 1,6 % et son assiette propre pour les années civiles nouvelles.",
        "Contribution supplémentaire, taux différencié et facultés de remise de substitution devenues sans objet pour les années nouvelles.",
        "Déclarations, taxation d'office et majorations forfaitaires exclusivement attachées aux trois contributions des années nouvelles.",
        "Acompte de 95 % au 1er juin et régularisation au 1er octobre exclusivement liés aux trois contributions supprimées."
    ],
    benefit="Les exclusions des génériques et des médicaments orphelins sous le seuil de 20 millions d'euros, les déductions de remises et d'exportations, les exclusions de spécialités de référence, le taux différencié sous 50 millions d'euros et les deux facultés de remise du III F restent applicables aux années anciennes. Pour les années nouvelles, les trois contributions sont entièrement supprimées, sans contribution ni remise fiscale de remplacement : ces allègements n'ont plus d'objet sur ces seules contributions. Le plafond cumulé de 10 % pourrait néanmoins limiter la clause de sauvegarde survivante : son fondement, ses sept catégories et son dénominateur sont expressément conservés au III A et E, pour les futurs éligibles aussi. Les remises et restitutions des trois cibles de prise en charge restent dans leur régime autonome ; aucune exonération sur une charge survivante n'est retirée.")


# Une seule suppression de cotisation sur les alcools, avec sept coordinations.
alcohol_transition = "Produits pour lesquels l'accise devient exigible à compter de l'entrée en vigueur de la loi ; produits d'exigibilité antérieure et droits correspondants conservés."
alcohol_old = ("Pour les produits pour lesquels l'accise est devenue exigible avant cette date, les dispositions antérieures de la présente section restent applicables à la liquidation, aux exonérations, au plafonnement, au paiement, au contrôle, au recouvrement, aux restitutions, aux prescriptions, au contentieux et à la non-déductibilité fiscale de la cotisation, même lorsque ces opérations interviennent après cette date. Il n'est institué aucune restitution générale des cotisations légalement dues. Les sanctions restent soumises à la loi répressive plus douce dans son champ.")
alcohol_distinct = "La suppression de cette cotisation ne modifie ni l'accise sur les alcools, ni ses exonérations, ni les règles sanitaires, de protection des mineurs et de sécurité applicables aux boissons alcooliques. Aucun prélèvement ni aucune déclaration de remplacement de cette cotisation n'est institué."
alcohol_burdens = "Aucune charge nouvelle : suppression de la seule cotisation additionnelle et de ses obligations propres ; accise, obligations communes et protections sanitaires indépendantes non étendues."
alcohol_repeals = {
    'L245-7': (
        "Aucune cotisation au titre de la présente section n'est due pour les boissons alcooliques d'une teneur en alcool supérieure à 18 % lorsque l'accise devient exigible à compter de cette entrée en vigueur.",
        "Institution de la cotisation nationale additionnelle sur les boissons de plus de 18 % d'alcool, pour les nouvelles exigibilités.",
        "Réforme de fond : suppression de cette cotisation accessoire à l'accise, plutôt que réécriture de son motif sanitaire. Les règles sanitaires et l'accise conservent leur fondement propre ; la suppression d'un prélèvement ne vaut pas disparition de ces protections.",
        'tax_removed',
        "Il est institué une cotisation perçue sur les boissons alcooliques d'une teneur en alcool supérieure à 18 %",
        "Cotisation nationale sur les boissons de plus de 18 % : tarifs source L245-9 de 599,31 euros par hectolitre d'alcool pur ou 50,6 euros par hectolitre des autres boissons, avec indexation, plafond de relèvement de 1,75 % et plafond de 40 % de l'accise pour certains codes NC ; ce ne sont pas des tarifs 2026 recalculés.",
        "Aucune cotisation de cette section sur les mêmes produits pour les nouvelles exigibilités ; accise distincte maintenue."),
    'L245-8': (
        "Les règles de fait générateur, d'exigibilité, de désignation des redevables, de constatation et de paiement auxquelles renvoyait le présent article ne peuvent établir la cotisation supprimée pour les produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur.",
        "Renvoi aux règles d'accise pour établir et payer la cotisation supprimée sur les nouvelles exigibilités.",
        "Coordination nécessaire de la suppression de L245-7 : le renvoi au CIBS ne doit pas rendre exigible une cotisation supprimée. La procédure commune de l'accise reste applicable à cette accise et aux anciennes cotisations.",
        'coordination',
        "Les règles relatives au fait générateur, à l'exigibilité, aux personnes soumises aux obligations fiscales, à la constatation et au paiement de la taxe",
        "Procédure d'accise rendue applicable à la cotisation par renvoi aux sections 2 et 4 à 7 du chapitre III du CIBS.",
        "Aucun renvoi opérant pour établir la cotisation sur les nouvelles exigibilités ; procédure d'accise autonome et anciennes dettes conservées."),
    'L245-9': (
        "Aucun tarif ni relèvement annuel prévu par le présent article ne s'applique à la cotisation supprimée pour les produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur.",
        "Tarifs, indexation et publication annuelle de la cotisation supprimée, pour les nouvelles exigibilités.",
        "Coordination tarifaire de la suppression de L245-7 : retrait intégral du barème et de son indexation pour l'avenir, sans supprimer les plafonds favorables sur les anciennes dettes. Ce retrait ne constitue pas une deuxième taxe supprimée.",
        'coordination',
        "1° 599,31 euros par hectolitre d'alcool pur pour les boissons relevant de la catégorie fiscale des alcools",
        "599,31 euros/hl d'alcool pur ou 50,6 euros/hl d'autres boissons dans le texte source ; indexation annuelle au plus 1,75 % et limite de 40 % de l'accise pour NC 2204, 2205, 2206.",
        "Barème et indexation sans application aux nouvelles exigibilités ; plafonds et tarifs légalement applicables aux produits anciens préservés."),
    'L245-9-1': (
        "Pour les produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur, l'absence de cotisation résulte de la suppression intégrale prévue à l'article L. 245-7, qu'ils bénéficient ou non d'une exonération d'accise.",
        "Exonérations de la seule cotisation entièrement supprimée pour les nouvelles exigibilités ; aucune exonération d'accise supprimée.",
        "Coordination de l'abolition intégrale de la cotisation. Son exonération dérivée devient sans objet pour les produits nouveaux, tous libérés de la cotisation, sans taxe de remplacement ; elle est expressément conservée pour les produits anciens et ne modifie pas les exonérations autonomes du CIBS.",
        'coordination',
        "sont également exonérés de la cotisation prévue à l'article L. 245-7 du présent code.",
        "Exonération de cotisation pour les produits exonérés d'accise par L313-7 à L313-14, L313-32, L313-34, L313-36 et L313-36-1 du CIBS.",
        "Absence générale de la cotisation pour les produits nouveaux, sans condition d'exonération d'accise ; avantages sur les anciennes cotisations et sur l'accise conservés."),
    'L245-10': (
        "Aucun contrôle ni recouvrement ne peut établir la cotisation supprimée pour les produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur. Les recours contre une perception indue restent ouverts.",
        "Application aux nouvelles cotisations du circuit de contrôle, recouvrement et contentieux par renvoi à l'accise.",
        "Coordination procédurale de L245-7 : le contrôle d'une dette inexistante ne peut rétablir la cotisation ; les anciennes créances, les réclamations pour indus et les garanties de recours restent régies par leurs règles. Aucun contrôle d'accise n'est supprimé.",
        'coordination',
        "Les règles relatives au contrôle, au recouvrement et au contentieux de la taxe sont celles applicables à l'accise sur les alcools",
        "Renvoi à la section 8 du chapitre III du CIBS pour le contrôle, recouvrement et contentieux de la cotisation.",
        "Renvoi conservé pour les anciennes dettes et les recours, sans nouvelle cotisation ; accise autonome inchangée."),
    'L245-11': (
        "L'interdiction de déduire la cotisation supprimée pour l'établissement de l'impôt sur le revenu ou de l'impôt sur les sociétés ne concerne plus aucune cotisation au titre des produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur. Aucune déduction d'une cotisation inexistante n'est créée.",
        "Non-déductibilité fiscale de la cotisation supprimée pour les nouvelles exigibilités, sans nouvelle déduction fictive.",
        "Coordination fiscale de la suppression de la cotisation. La non-déductibilité survit pour la cotisation légalement due au titre des produits anciens ; la suppression ne crée ni crédit d'impôt ni déduction fictive et ne modifie pas la fiscalité personnelle ou le fait générateur propre de l'IS proposé.",
        'coordination',
        "La cotisation n'est pas déductible pour l'établissement de l'impôt sur le revenu",
        "Cotisation non déductible pour l'IR ou l'IS dû par le consommateur.",
        "Non-déductibilité conservée pour les cotisations anciennes ; aucun montant à déduire pour les produits nouveaux libérés de cotisation."),
    'L245-12': (
        "Aucun décret pris pour l'application de la présente section ne peut instituer de cotisation, déclaration ou versement sur son fondement pour les produits pour lesquels l'accise devient exigible à compter de cette entrée en vigueur. Les dispositions réglementaires nécessaires aux anciennes dettes et aux recours restent applicables dans ce seul champ.",
        "Habilitation réglementaire d'application de la cotisation supprimée pour les nouvelles exigibilités.",
        "Coordination de fermeture de l'habilitation : les règlements de cette section ne doivent pas recréer le prélèvement ni une formalité de remplacement. Le traitement des anciennes dettes et les règlements sanitaires ou d'accise autonomes ne sont pas abrogés.",
        'coordination',
        "Un décret fixe les conditions d'application de la présente section.",
        "Habilitation à réglementer l'ensemble de la section relative à la cotisation additionnelle.",
        "Habilitation sans effet pour les produits nouveaux, maintien borné au traitement des anciennes cotisations et recours.")
}
for n, (rule, scope, reason, kind, sq, before, after) in alcohol_repeals.items():
    xml = ps("Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant suppression de la cotisation sur les boissons alcooliques prévue par la présente section.", rule, alcohol_old, alcohol_distinct)
    q = rule.split('. ')[0] + ('.' if '. ' in rule else '')
    # Les points des références L. ne servent pas de coupe de citation.
    q = rule
    notes = "Lecture intégrale de la source et des notes, lorsqu'elles existent. La note de 2023 vise le droit antérieur applicable depuis le 1er janvier 2024 et ne date pas la réforme proposée. La frontière est l'exigibilité de l'accise, afin de ne pas taxer deux fois ni rouvrir les anciennes périodes. Les sept articles L245-7 à L245-12 forment une seule mesure de suppression ; les articles d'exécution sont classés comme coordinations. Le CIBS, ses règles d'accise et le droit de l'Union restent distincts, sans présomption d'abolition d'une accise européenne. D245-15, lu dans le corpus, et les formulaires et affectations éventuelles doivent être coordonnés dans leur champ propre ; leur réécriture n'est pas revendiquée ici. La perte de recette de cette cotisation et le financement des protections sanitaires restent à évaluer, sans compensation inventée."
    if n == 'L245-9':
        notes += " Les deux tarifs source, le plafond d'accise de 40 %, les codes NC 2204/2205/2206, la règle d'arrondi et le maximum de relèvement de 1,75 % restent entièrement régis par l'ancienne rédaction pour les produits anciens. Aucun tarif courant recalculé n'est avancé."
    benefit = None
    if n == 'L245-9-1':
        benefit = "L'avantage est l'exonération de cotisation attachée à chacune des exonérations d'accise visées : L313-7 à L313-14, L313-32, L313-34, L313-36 et L313-36-1 du CIBS. Toutes restent mobilisables pour liquider ou restituer les cotisations des produits d'exigibilité antérieure. Pour toute exigibilité future, la cotisation est entièrement supprimée pour tous les produits, sans remplacement ni extension d'assiette : aucun ancien bénéficiaire ne devient redevable. Les exonérations d'accise elles-mêmes restent intactes, y compris pour les situations futures recevables."
    put(n, xml, reason, notes,
        'material_reduction' if n == 'L245-7' else 'coordination_only',
        "La cotisation de la section est effectivement supprimée sur les nouvelles exigibilités ; les limites temporelles et les avantages anciens sont explicites." if n == 'L245-7' else "La norme d'exécution est retirée pour la cotisation supprimée, sans additionner un nouveau prélèvement ou une nouvelle réduction à la suppression de L245-7. Les fonctions autonomes de l'accise et les droits anciens demeurent.",
        "Suppression limitée à cette cotisation française additionnelle. Accise et protections sanitaires indépendantes subsistent ; aucune restitution générale pour les exigibilités anciennes. Les conséquences budgétaires et les coordinations hors lot ne sont pas chiffrées ni réputées terminées.",
        alcohol_burdens,
        effects=[effect(kind, 'alcools-cotisation-additionnelle-suppression',
                        'Suppression de la cotisation sur les boissons de plus de 18 %.' if kind == 'tax_removed' else scope,
                        before, after, 'euro' if n in {'L245-7', 'L245-9'} else 'legal_duty',
                        "Redevables et consommateurs des boissons relevant de L245-7 ; anciens exonérés compris.",
                        alcohol_transition, alcohol_burdens, sq, q)],
        repeal_scope=scope, benefit=benefit)


new8 = ps(
    "Lorsque le solde moyen de trésorerie de l'Agence centrale des organismes de sécurité sociale pour le dernier exercice clos est positif, la Caisse nationale d'assurance vieillesse affecte au Fonds de réserve pour les retraites mentionné à l'article L. 135-6 :",
    "1° Le résultat excédentaire de l'exercice clos de chacun des fonds dont elle a la gestion, à l'exception de celui du régime spécial mentionné à l'article L. 715-1 ; le versement intervient sans arrêté conjoint annuel des ministres chargés de la sécurité sociale et du budget, selon le calendrier de trésorerie de la caisse ;",
    "2° Le cas échéant, en cours d'exercice, un montant représentatif d'une fraction de l'excédent prévisionnel de l'exercice tel que présenté par la Commission des comptes de la sécurité sociale lors de sa réunion du second semestre de ce même exercice ; la caisse détermine le montant et les dates du versement sans arrêté conjoint des ministres chargés de la sécurité sociale et du budget.",
    "La suppression des arrêtés particuliers prévue aux 1° et 2° s'applique aux versements restant à effectuer à compter de l'entrée en vigueur de la loi qui la prévoit, sans nouvelle demande ni procédure de remplacement. Les montants valablement affectés et les versements déjà exécutés restent acquis. Les décisions antérieures de versement conservent leurs effets, notamment leurs montants et échéances. Les obligations de financement, de comptabilité, de contrôle et de sécurité de la trésorerie fondées sur une disposition distincte demeurent applicables."
)
put('L251-6-1', new8,
    "Réduction de fond ciblée : retrait des deux arrêtés interministériels particuliers fixant calendrier et, pour le versement prévisionnel, montant. La CNAV exécute directement l'affectation légale sans visa de remplacement. Restent la condition de trésorerie positive, le résultat excédentaire, l'exclusion du régime L715-1 et le caractère éventuel du prélèvement sur excédent prévisionnel présenté au second semestre.",
    "L135-6 et L715-1 ont été lus dans le corpus : réserves du régime général et engagements du FRR restent distincts du régime spécial des chemins de fer secondaires. L'allègement ne transforme pas ces réserves en comptes individuels capitalisés et ne finance aucun palier de retraite par anticipation. Les modalités réglementaires d'affectation et de trésorerie devront perdre les visas particuliers incompatibles ; contrôles et engagements financiers indépendants demeurent. Les deux subdivisions sont conservées. Aucun montant ni délai de paiement nouveau n'est fixé.",
    'material_reduction',
    "Deux décisions ministérielles particulières ne conditionnent plus l'exécution d'une affectation déjà définie par la loi. Le flux de réserves entre organismes n'est ni supprimé ni diminué et ne constitue pas une économie de cotisations.",
    "Seuls ces arrêtés d'exécution sont supprimés. Ressources du FRR, engagements envers la CADES, solde positif et exclusion du régime spécial demeurent ; effets sur délais réels et coûts publics non quantifiés.",
    "Aucune charge nouvelle identifiée : choix opérationnel du calendrier et du montant dans le champ déjà exécuté par la CNAV, sans déclaration, registre ni nouvelle instance. La suppression ne garantit aucun gain net de coût public.",
    effects=[effect('obligation_removed', 'retraites-affectation-excedents-sans-arrete-particulier',
                    'Retrait des arrêtés particuliers de versement des excédents au FRR.',
                    'Arrêté conjoint annuel de date au 1° et arrêté conjoint de montant et dates au 2°, avant exécution des affectations légales.',
                    'Exécution par la CNAV dans le champ et les conditions légales, sans les deux arrêtés particuliers.',
                    'legal_duty', 'CNAV, FRR et ministres chargés de la sécurité sociale et du budget.',
                    "Versements restant à effectuer dès l'entrée en vigueur ; affectations acquises et opérations exécutées conservées.",
                    'Aucun visa ou dépôt de remplacement ; contrôles financiers autonomes conservés.',
                    'un arrêté conjoint des ministres chargés de la sécurité sociale et du budget fixe chaque année la date de ce versement',
                    'le versement intervient sans arrêté conjoint annuel des ministres chargés de la sécurité sociale et du budget')],
    removed=["Arrêté conjoint annuel fixant la date de versement du résultat excédentaire au Fonds de réserve pour les retraites.",
             "Arrêté conjoint particulier fixant les montants et les dates du versement éventuel d'une fraction d'excédent prévisionnel."])


def keep(n, reason, notes, assessment, limitations, burdens):
    return put(n, None, reason, notes, 'retained_necessary', assessment, limitations, burdens)


keep('L252-1',
     "Maintien intégral nécessaire après examen : les dotations financent le service effectif des prestations maladie, maternité, invalidité, décès et AT-MP. Leur adaptation aux charges protège la continuité des droits. L'arrêté de règles communes et l'avis du conseil encadrent une répartition entre caisses ; aucune double déclaration ni autorisation imposée à l'assuré ou à l'employeur n'est instituée par cet article.",
     "Les deux dotations maladie/soins et incapacités-décès, puis la dotation AT-MP dans les mêmes conditions, restent entières. Leur annualité budgétaire ne constitue ni l'ancienne annualité de l'IS ni un nouveau prélèvement. Pas de financement inventé pour les suppressions fiscales du lot ; modalités réglementaires non réécrites ici.",
     "Aucune réduction démontrée dans cet article : le financement ajusté aux prestations est conservé intégralement, sans changement stylistique ni comptage d'une simplification.",
     "Le niveau des dotations et leur gestion réglementaire ne sont pas évalués ; la conservation n'établit aucun solde global des finances sociales.",
     "Aucune charge nouvelle identifiée puisque le texte reste intégralement inchangé ; aucune donnée, demande ou condition d'accès supplémentaire aux prestations n'est ajoutée.")

keep('L252-2',
     "Maintien intégral : l'affectation des excédents entre action sanitaire et sociale locale et réserve nationale protège deux emplois utiles des ressources. Ce virement interne ne prélève rien de plus sur un cotisant et n'exige aucun justificatif individuel. Supprimer la réserve priverait L252-3 d'un financement explicite des insuffisances sans alléger une obligation privée.",
     "L252-3, également assigné, garde le recours à la réserve à concurrence des excédents de la caisse. L'arrêté répartit ces excédents, sans montant ni proportion inventés. Les excédents ne sont pas présentés comme économies nationales ou ressource libre pour plusieurs réformes.",
     "L'affectation des excédents reste entière ; aucun gain fiscal ni baisse de dépense n'est revendiqué pour ce transfert interne nécessaire.",
     "Aucune évaluation du montant des excédents ou de la répartition entre action sociale et réserve ; les autres règles financières restent hors de cette décision.",
     "Aucune charge nouvelle identifiée : maintien exact d'une affectation comptable existante, sans formulaire ni collecte supplémentaire auprès des assurés.")

new11 = ps("Si les dotations attribuées à une caisse primaire ne lui permettent pas d'assurer la couverture des charges correspondantes, l'équilibre financier doit être maintenu ou rétabli par un prélèvement sur le fonds de réserve de la caisse nationale, à concurrence des excédents qui y ont été affectés par la caisse primaire intéressée conformément aux dispositions de l'article L. 252-2, ou, à défaut, par une avance ou une subvention que la caisse nationale peut accorder sans demande motivée préalable de la caisse primaire.",
           "Cette dispense s'applique aux avances et subventions restant à décider à compter de l'entrée en vigueur de la loi qui la prévoit, y compris aux procédures en cours. Elle ne crée pas un droit automatique à une avance ou à une subvention et ne supprime ni les règles budgétaires et comptables ni les contrôles de l'emploi des fonds. Les demandes déjà déposées restent utilisables sans renouvellement et les décisions et créances antérieures sont préservées.")
put('L252-3', new11,
    "Réduction de fond : retrait de la demande motivée obligatoire de la caisse primaire pour recevoir une avance ou une subvention de rééquilibrage. La caisse nationale peut décider à partir de ses informations de financement, sans dossier de remplacement. L'obligation de rétablir l'équilibre, la priorité de la réserve et sa limite liée aux excédents L252-2 sont intégralement conservées.",
    "Le mécanisme L252-2 a été confronté à cet article : le plafond du prélèvement de réserve n'est pas remplacé par une subvention automatique ou illimitée. Les modalités réglementaires qui imposeraient la même demande préalable doivent être coordonnées ; l'absence de demande n'empêche pas les contrôles budgétaires ni la vérification des charges. Aucun montant d'aide, date de promulgation ou financement nouveau n'est inventé.",
    'material_reduction',
    "Une démarche motivée préalable expressément imposée par la source est supprimée. La caisse nationale garde sa faculté d'aide et l'objectif d'équilibre ; aucune baisse de prélèvement ou de dépense globale n'est démontrée.",
    "Dispense limitée au dossier préalable de rééquilibrage entre ces caisses ; conditions de fonds et contrôles autonomes subsistent. Le temps administratif économisé n'est pas chiffré.",
    "Aucune charge nouvelle identifiée : ni nouvelle transmission périodique ni attestation de remplacement ; la décision de financement et ses contrôles existaient déjà.",
    effects=[effect('obligation_removed', 'cpam-reequilibrage-sans-demande-motivee',
                    'Suppression de la demande motivée préalable au soutien financier.',
                    'Avance ou subvention de la caisse nationale seulement sur demande motivée de la caisse primaire.',
                    'Avance ou subvention possible sans cette demande, priorité et plafond de réserve conservés.',
                    'legal_duty', 'Caisses primaires et caisse nationale de la branche maladie.',
                    "Décisions restant à prendre dès l'entrée en vigueur, y compris dossiers en cours ; décisions acquises conservées.",
                    'Aucun dossier de remplacement ; règles budgétaires, comptables et contrôles maintenus.',
                    'une avance ou une subvention que la caisse nationale peut accorder sur demande motivée de la caisse primaire.',
                    'une avance ou une subvention que la caisse nationale peut accorder sans demande motivée préalable de la caisse primaire.')],
    removed=["Demande motivée préalable de la caisse primaire comme condition d'une avance ou subvention de rééquilibrage de la caisse nationale."])

keep('L253-1',
     "Maintien nécessaire : la règle d'affectation empêche de détourner une ressource de l'institution pour laquelle elle est légalement perçue ; l'injonction de virement remédie aux rétentions de fonds par un organisme collecteur. Ce n'est ni un agrément d'employeur ni une double déclaration. La supprimer fragiliserait les droits financés sans réduire un prélèvement.",
     "Les deux alinéas sont conservés. La note d'application à l'ancien L614-1 est historique et ne crée pas une extension actuelle non vérifiée. Une affectation nouvelle de cotisations vieillesse relève de sa loi propre, avec financement de transition ; cet article ne décide ni capitalisation automatique ni cotisation supplémentaire.",
     "Aucune réforme matérielle de cet article : affectation et exécution des virements restent entières pour protéger les fonds destinés aux droits sociaux.",
     "La compatibilité des futures affectations de chaque réforme devra être organisée dans leurs propres textes ; aucun gain national de trésorerie n'est établi ici.",
     "Aucune charge nouvelle identifiée : conservation exacte des deux obligations financières existantes, sans ajout de données, autorisation ou délai légal nouveau.")

keep('L255-1',
     "Maintien intégral : l'attribution des intérêts créditeurs, débiteurs et produits selon le solde quotidien prévient les subventions croisées opaques entre branches et déposants. Le suivi de trésorerie existe déjà dans L225-1 ; cet article ne demande pas un second relevé au cotisant. Le supprimer déplacerait les charges financières sans démontrer une économie.",
     "L225-1 et L225-1-3 lus dans le corpus : le dernier alinéa du premier concerne les placements des excédents, le second les dépôts rémunérés d'autres régimes et fonds. Sa proposition supprime l'approbation de convention sans abolir la rémunération ; le présent renvoi reste cohérent et ne rétablit aucun visa. La note relative aux conventions conclues à compter de 2008 est conservée dans son champ.",
     "Répartition existante des produits et intérêts intégralement maintenue ; aucun transfert de financement n'est présenté comme une baisse de prélèvement.",
     "Taux de rémunération et montants de trésorerie non chiffrés ; le décret d'application reste à son champ et n'est pas réécrit dans le lot.",
     "Aucune charge nouvelle identifiée : ni nouvelle fréquence de compte ni registre additionnel ; le texte et sa base de solde quotidien sont conservés sans modification.")

keep('L256-3',
     "Maintien intégral utile : l'habilitation à purger les hypothèques légales facilite la gestion des garanties de prêts consentis par les organismes. Elle constitue une faculté favorable et non un agrément ou une obligation du débiteur. Sa suppression retirerait un outil de réalisation ou de libération des garanties sans alléger une charge démontrée.",
     "La source n'ajoute ni coût ni pièce ni délai de purge ; les garanties civiles et les droits des tiers conservent leur régime. Les notes visant L623-1 et L721-8 ne sont pas le corps normatif : le L623-1 fourni est désormais consacré à la maternité et ne vaut pas extension actuelle de cette habilitation. Pas de rattachement au contrat de travail unique.",
     "La faculté de purge des hypothèques est conservée entière ; aucun gain nouveau ni suppression de formalité civile indépendante n'est revendiqué.",
     "Les procédures civiles de purge ne sont pas fournies ni réécrites ; les anciennes notes de renvoi ne prouvent pas la portée actuelle des extensions historiques.",
     "Aucune charge nouvelle identifiée puisque l'habilitation reste exactement celle de la source ; aucun dépôt ni justificatif supplémentaire n'est ajouté.")

new15 = ps("A l'exception des cotisations et majorations de retard, les créances des caisses nées de l'application de la législation de sécurité sociale, notamment dans des cas mentionnés aux articles L. 374-1, L. 376-1 à L. 376-3, L. 452-2 à L. 452-5 et L. 454-1, peuvent être réduites en cas de précarité de la situation du débiteur par décision motivée par la caisse, sauf en cas de manœuvre frauduleuse ou de fausses déclarations.",
           "Cette faculté demeure ouverte aux créances encore régies par des dispositions antérieures, notamment celles nées de faits antérieurs à l'abrogation de l'article L. 244-8 et celles qui demeurent régies par l'ancien article L. 811-6. Elle reste ouverte aux situations futures remplissant les conditions du premier alinéa. La réduction d'une créance de la caisse ne diminue ni les prestations et réparations dues à la victime ou à ses ayants droit ni la priorité de leurs droits sur ceux de la caisse.")
put('L256-4', new15,
    "Coordination nécessaire, sans nouveau gain matériel : la liste illustrative ne présente plus L244-8 comme une source actuelle de créance pour les faits nouveaux après son abrogation proposée. L811-6 est identifié comme ancien et n'est plus présenté comme disposition active du corpus. La transition préserve expressément la faculté de remise des créances anciennes. La précarité, la décision motivée, l'exclusion des cotisations et majorations et les exceptions de fraude/fausses déclarations restent inchangées ; aucune pièce nouvelle n'est demandée.",
    "Les cibles fournies L376-1/2, L452-2/3/4/5 et L454-1 ont été lues intégralement, y compris la réserve constitutionnelle des notes de L452-3 et L452-5 : la remise d'une créance de caisse ne modifie pas les réparations propres des victimes, les majorations AT-MP, la priorité subrogatoire ni les responsabilités spéciales. Lecture complémentaire L244-8 et sa proposition transitoire, L374-1 et L376-3 dans le corpus. L811-6 est absent du corpus courant : aucune concordance moderne inventée, aucune ancienne créance exclue du champ général et historique. Les notes L633-1, L721-8 et L721-14 sont des mentions historiques, non des conditions de travail ou de licenciement. Les textes extérieurs de responsabilité et de contentieux ne sont pas déclarés réécrits. Le plafond ordinaire de rupture ne limite pas ces réparations.",
    'coordination_only',
    "La remise pour précarité garde le même champ général, les mêmes exclusions et les mêmes conditions. Les références anciennes sont cantonnées aux créances qui demeurent régies par elles ; aucune remise nouvelle de cotisations ou de dommages dus à la victime n'est créée.",
    "Montant et existence des créances anciennes à contrôler dossier par dossier ; contenu historique intégral de L811-6 non fourni, donc aucune équivalence actuelle n'est affirmée. Ce lot ne réécrit pas les articles cibles de réparation.",
    "Aucune charge nouvelle identifiée : ni attestation de précarité ni notification supplémentaire ; la motivation de la décision existait déjà. Les réserves de droits des victimes explicitent les limites des créances de caisse.",
    effects=[effect('coordination', 'securite-sociale-remise-precarite-creances-anciennes',
                    'Cantonnement des références anciennes sans fermer la remise pour précarité.',
                    'Liste illustrative de créances citant L244-8 et L811-6 sans précision temporelle, avec faculté générale de remise hors cotisations et majorations.',
                    'Liste actuelle et alinéa historique explicite ; faculté conservée pour créances anciennes et situations futures, droits propres des victimes intacts.',
                    'legal_duty', 'Débiteurs précaires de créances des caisses, victimes et ayants droit.',
                    'Coordination avec la transition de L244-8 ; aucun effacement général des créances anciennes ni restriction des futurs bénéficiaires.',
                    'Aucun formulaire ou condition de remise supplémentaire.',
                    'peuvent être réduites en cas de précarité de la situation du débiteur par décision motivée par la caisse',
                    'Cette faculté demeure ouverte aux créances encore régies par des dispositions antérieures')])

keep('L261-1',
     "Maintien intégral d'une protection utile : détection du non-recours et accompagnement vers les droits et prestations. L'obligation porte sur les organismes, au bénéfice des personnes éligibles présentes et futures. Elle ne prescrit ni rapport annuel distinct, ni déclaration à la charge du bénéficiaire, ni accès illimité à des données ; aucune formalité redondante identifiable n'est à retirer de ce corps.",
     "Le lien avec d'autres administrations reste limité aux informations pouvant identifier le non-recours dans le respect de leurs régimes d'accès ; le présent maintien n'invente pas d'échange de données ni d'attribution automatique. Les pensions et autres prestations ne sont pas confondues avec les conditions de financement des réformes fiscales ou de retraite.",
     "L'aide à l'accès aux droits est conservée intégralement, sans nouveau corps stylistique et sans la compter comme une réduction de prélèvement ou de formalité.",
     "Efficacité, moyens et coûts de détection non mesurés ; aucune ouverture de droit au-delà des conditions propres à chaque prestation ni coordination de données nouvelle.",
     "Aucune charge nouvelle identifiée : le texte demeure entier ; aucune attestation, collecte, durée de conservation ou fréquence de transmission supplémentaire n'est ajoutée.")

keep('L262-1',
     "Maintien intégral des actions sanitaires et sociales prioritaires contre la précarité et de prévention de la désinsertion professionnelle. Ces obligations de service protègent la santé et le maintien dans l'emploi ; elles ne conditionnent pas l'embauche à une autorisation ni l'aide à un CDD. Le cadre de programmes et la coordination CNAM évitent la dispersion d'une mission essentielle plutôt qu'un doublon déclaratif identifiable.",
     "Les deux alinéas et tous leurs renvois sont conservés. L221-1 3°/4° et L215-1 4° ont été lus dans le corpus : coordination sanitaire/sociale et service social cohérents. Les renvois au code du travail L5214-3-1 et L5211-2 3°/4° et au CASF concernent handicap, préorientation et réadaptation, pas la durée ou la rupture du contrat ; leurs textes entiers ne sont pas fournis comme cibles et aucun contenu supplémentaire n'en est inventé. La note d'entrée en vigueur au 31 mars 2022 et ses conditions d'application restent à leur champ. Le préavis de quinze jours et le seuil d'indemnité ne limitent pas ces actions ni les protections de santé.",
     "Aucune réduction nouvelle : les missions de prévention, d'information et d'accompagnement sont maintenues sans les transformer en une formalité patronale ou une durée d'emploi.",
     "Pas de réécriture des dispositifs handicap du code du travail ou du CASF ni d'évaluation de leurs coûts. Les mesures de contrat unique ne valent pas suppression de protections ou de procédures spéciales.",
     "Aucune charge nouvelle identifiée : maintien exact de la source, sans dossier, registre, donnée ou procédure de licenciement ajouté pour bénéficier des actions.")

keep('L263-1',
     "Maintien intégral de l'action sanitaire et sociale des CAF au bénéfice de leurs ressortissants et familles. Le renvoi au 2° de L223-1 reste exact dans la source et la proposition cible : il désigne le fonds et son programme. Il ne rétablit pas l'arrêté ministériel distinct supprimé dans cette proposition et ne crée aucune obligation de transmission ou sanction.",
     "L223-1 entier, sa note relative aux enfants nés/adoptés à compter du 1er janvier 2026 et sa proposition ont été lus. Le 2° est maintenu à son numéro, avec programme arrêté par le conseil d'administration dans la proposition. Le présent article n'appelle aucune coordination textuelle pour cela. Les remboursements des 5° à 8° de la cible, dont les 60 % du 6° a et les congés des agents publics, ne sont pas visés ici. Les contrats privés nouveaux et anciens n'affectent pas le bénéfice de l'action sociale.",
     "La mission favorable d'action sociale est conservée entière ; le maintien du renvoi ne constitue ni une nouvelle simplification ni une seconde suppression d'approbation de programme.",
     "Aides individuelles et conditions réglementaires non chiffrées ; le seul 2° est visé, sans extension aux remboursements de congés ou à un régime de rupture d'emploi.",
     "Aucune charge nouvelle identifiée : maintien exact de la mission et de son renvoi valide, sans nouveau programme parallèle ni justificatif du ressortissant.")

new19 = ps("Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant l'obligation de prévoir un régime de sanctions dans les conventions de subvention du fonds d'action sanitaire et sociale.",
           "Les conventions conclues à compter de cette date par les organismes débiteurs de prestations familiales ne sont plus tenues, sur le fondement du présent article, de définir un régime de sanctions en cas de manquement à leurs règles. Les conventions en cours n'ont pas à être complétées pour satisfaire cette seule obligation ; aucune clause ni procédure de sanction de remplacement n'est imposée.",
           "Les conventions valablement conclues, les subventions et droits acquis ainsi que les créances antérieures restent soumis à leurs règles propres. La présente abrogation ne fait pas obstacle à la modification conventionnelle des clauses existantes et ne crée pas une restitution générale des sanctions légalement acquittées, sous réserve de l'application de la loi répressive plus douce dans son champ.",
           "Le fonds et le programme mentionnés au 2° de l'article L. 223-1, les aides ouvertes aux futures situations éligibles, le contrôle de l'emploi des fonds, la restitution des sommes indûment versées, la répression de la fraude et les recours ayant un fondement distinct demeurent applicables. L'abrogation ne crée aucune sanction ni condition nouvelle d'accès aux aides.")
put('L263-2', new19,
    "Réforme de fond : suppression de l'obligation générale, ajoutée à chaque convention de subvention, de définir un régime propre de sanctions. Le contrôle de l'emploi des subventions, l'indu, la fraude et les recours autonomes suffisent à conserver leur fonction sans imposer cette couche conventionnelle systématique. L'aide et le fonds ne sont pas abrogés ; les conventions antérieures valables restent protégées et peuvent être modifiées selon leur droit.",
    "La note de la loi de 2023 fixe l'entrée en vigueur du dispositif source au 1er janvier 2025, non celle de la réforme. L223-1 2° reste le fondement du fonds et du programme, y compris sous sa proposition actuelle sans arrêté ministériel distinct. L263-1 garde la mission d'action sociale ; aucune réduction de ses bénéficiaires ni de droits futurs n'est décidée. Les modèles conventionnels et textes réglementaires qui imposeraient ce régime sur le seul fondement de L263-2 sont à coordonner ; aucun renvoi hors lot n'est déclaré traité. La portée répressive des sanctions contractuelles et l'application de la loi plus douce doivent être appréciées selon leur nature. Le barème de rupture ordinaire ne s'applique ni aux sanctions ni aux subventions.",
    'material_reduction',
    "L'obligation légale de rédiger un régime de sanctions propre à chaque convention disparaît, sans supprimer le contrôle des fonds ou l'accès aux aides. La source ne chiffrait aucune amende : aucun montant économisé n'est avancé.",
    "Les clauses de conventions existantes ne sont pas automatiquement annulées ; les responsabilités, indus et sanctions reposant sur des bases distinctes subsistent. Le coût net et les modèles hors lot restent à examiner.",
    "Aucune charge nouvelle identifiée : aucune déclaration, clause obligatoire ou procédure de remplacement ; les droits et contrôles indépendants sont maintenus dans leur champ.",
    effects=[effect('obligation_removed', 'caf-subventions-fin-regime-sanctions-obligatoire',
                    'Suppression du régime de sanctions conventionnel obligatoirement distinct.',
                    'Chaque convention de subvention du fonds L223-1 2° doit définir un régime de sanctions pour les manquements à ses règles.',
                    'Aucune obligation de prévoir ce régime dans les nouvelles conventions ou de compléter les conventions en cours à cette fin ; contrôles autonomes conservés.',
                    'legal_duty', 'Organismes débiteurs de prestations familiales et bénéficiaires de leurs subventions du fonds.',
                    "Conventions futures dès l'entrée en vigueur ; anciennes conventions et créances valables préservées, sous réserve de loi répressive plus douce applicable.",
                    'Aucune clause ni procédure de remplacement ; ni fermeture du fonds ni restriction des aides.',
                    "définissent un régime de sanctions en cas de manquement aux règles qu'elles prévoient.",
                    "aucune clause ni procédure de sanction de remplacement n'est imposée.")],
    repeal_scope="Obligation de définir un régime de sanctions dans chaque convention de subvention du fonds d'action sanitaire et sociale ; aucune suppression du fonds ni des aides.")

keep('L271-1',
     "Maintien intégral : le cadre réglementaire des relations financières, comptables et administratives entre le régime général et la mutualité sociale agricole est nécessaire à leur articulation sans fusion implicite des régimes. L'article n'impose aucun nouveau dossier à un assuré ou un employeur ; aucun doublon précis n'est démontré par cette habilitation générale.",
     "Les quatre caisses nationales et l'agence centrale sont conservées dans leur champ ; la note fixe la date effective au 14 mai 2022. Les salariés agricoles ne sont pas intégrés par ce renvoi au premier champ de capitalisation du salarié privé du régime général et les régimes publics ne sont pas réformés par le contrat unique. Décrets et conventions d'application non déclarés réécrits.",
     "Le cadre d'interopérabilité des deux réseaux reste entier ; aucune réduction fiscale ou obligation supprimée n'est attribuée à ce maintien.",
     "Pas d'analyse détaillée des décrets d'application ni de leurs coûts ; les régimes agricole et général demeurent juridiquement distincts.",
     "Aucune charge nouvelle identifiée : maintien exact de l'habilitation existante, sans déclaration, transfert de cotisations ou nouvelle condition d'affiliation.")

keep('L272-1',
     "Maintien intégral d'une protection essentielle contre la fraude et les fausses déclarations dans l'encaissement et la gestion des organismes. L'infraction ne punit pas un simple retard ou défaut de formulaire et vise les responsables et agents, pas le cotisant honnête. Sa suppression affaiblirait la protection des fonds sans retirer une formalité redondante ; seule la sursanction automatique de L272-2 est retirée séparément.",
     "Amende de 3 750 euros, emprisonnement de six mois, personnes visées et réserve de peines plus fortes conservés. Cette infraction de gestion ne se confond ni avec la cotisation sur les alcools supprimée ni avec les obligations propres aux contrats de travail. Les qualifications pénales autonomes et les garanties procédurales gardent leur champ.",
     "Aucune modification de l'infraction principale : maintien nécessaire de la protection anti-fraude, sans la compter comme un allègement ou une nouvelle sanction.",
     "Aucune évaluation du contentieux ni des infractions pénales autonomes ; les maxima de cette infraction demeurent, sous les règles générales de jugement.",
     "Aucune charge nouvelle identifiée : infraction et maxima strictement inchangés, sans registre, justificatif ou pénalité administrative supplémentaire.")

new22 = ps("Le présent article est abrogé à compter de l'entrée en vigueur de la loi supprimant les peines maximales obligatoires et la publicité spéciale qu'il prévoyait.",
           "La condamnation antérieure pour la même infraction n'impose plus, sur le fondement du présent article, l'application automatique du maximum de l'amende et de l'emprisonnement prévus à l'article L. 272-1. L'insertion du jugement dans des journaux aux frais du condamné ne peut plus être ordonnée sur le seul fondement du présent article.",
           "Les faits constitutifs de fraude ou de fausse déclaration restent punissables selon l'article L. 272-1 et, le cas échéant, les autres dispositions pénales applicables. Les règles générales de récidive, d'individualisation de la peine et de réparation demeurent applicables dans leur champ.",
           "Les dispositions répressives plus douces s'appliquent aux faits antérieurs qui n'ont pas donné lieu à une condamnation définitive. Les condamnations et publications définitivement prononcées avant cette entrée en vigueur restent régies par les règles qui leur sont applicables ; aucune restitution générale des sommes légalement acquittées ni annulation automatique d'une condamnation définitive n'est créée. Les règles générales d'application de la loi pénale dans le temps sont réservées.")
put('L272-2', new22,
    "Réforme de fond : retrait du maximum obligatoirement appliqué aux deux peines après une condamnation antérieure, ainsi que de la publicité spéciale aux frais du condamné. La protection anti-fraude reste assurée par L272-1, la récidive générale et le juge ; cette surcouche mécanique n'est pas indispensable à cette protection. L'abrogation est entière : le plafond favorable de 7,5 euros ne disparaît qu'avec la faculté spéciale de publication qu'il limite, sans publicité de remplacement.",
    "L272-1 reste intégralement maintenu avec ses maxima de 3 750 euros et six mois. Le coût maximum de 7,5 euros de publication n'est ni revalorisé ni transféré à un autre mécanisme. Les notes de champ ont été lues : le L623-1 fourni est aujourd'hui un texte de maternité, non le fondement de l'ancienne extension vieillesse ; aucun renvoi au contrat privé n'en découle. Les extensions du corpus L382-29, L612-2, L641-1 et L766-11 ont été lues : elles doivent retirer L272-2 ou cantonner ses effets temporels sans supprimer leurs autres dispositions. Les anciens L614-1, L721-8 et R642-10 mentionnés en note ne sont pas certifiés comme concordances actuelles. Les règles générales de loi pénale plus douce, d'exécution des condamnations définitives et de récidive sont réservées ; leurs textes entiers hors lot ne sont pas réécrits.",
    'material_reduction',
    "Suppression effective de l'automaticité des deux maxima et d'une publicité pénale spéciale ; l'infraction principale de fraude subsiste et aucune peine de remplacement n'est ajoutée.",
    "Pas de dépénalisation de la fraude ni de suppression des autres qualifications ou de la récidive générale. Condamnations définitives et application temporelle relèvent de leurs règles propres ; aucun montant national de coût pénal évité n'est chiffré.",
    "Aucune charge nouvelle identifiée : retrait des deux mécanismes spéciaux sans obligation de publication, registre ou peine compensatoire ; les règles générales ne sont pas étendues.",
    effects=[effect('obligation_removed', 'fraude-sociale-fin-maxima-obligatoires-publicite-speciale',
                    'Retrait de la peine maximale automatique et de la publication pénale spéciale.',
                    'Maximum des deux peines toujours appliqué après condamnation pour la même infraction ; insertion facultative en journaux à la charge du condamné plafonnée à 7,5 euros.',
                    'Plus de maximum obligatoire ni de publicité sur le fondement de L272-2 ; fraude L272-1 et règles générales conservées.',
                    'legal_duty', 'Membres des conseils, administrateurs, directeurs et agents des organismes de sécurité sociale poursuivis pour la même infraction.',
                    'Application immédiate et loi répressive plus douce pour les affaires non définitivement jugées ; condamnations définitives soumises aux règles générales.',
                    'Aucune sursanction, publicité ni registre spécial de remplacement.',
                    "Le maximum des deux peines sera toujours appliqué au délinquant lorsqu'il aura déjà subi une condamnation pour la même infraction",
                    "La condamnation antérieure pour la même infraction n'impose plus, sur le fondement du présent article, l'application automatique du maximum de l'amende et de l'emprisonnement prévus à l'article L. 272-1.")],
    repeal_scope="Application automatique des deux peines maximales après condamnation antérieure pour la même infraction et faculté spéciale d'insertion du jugement aux frais du condamné.")

keep('L273-1',
     "Maintien intégral nécessaire : la surveillance de l'affiliation et du versement des cotisations protège l'ouverture et le financement des droits. L'article charge les autorités publiques de veiller aux seules obligations légalement existantes ; il ne crée ni autorisation d'embauche, ni document annuel, ni contrôle supplémentaire du contrat unique. Aucune formalité autonome redondante n'est identifiée dans ce corps.",
     "La note visant L623-1 est historique : la cible actuelle porte sur maternité/paternité et non sur l'ancienne extension vieillesse. L752-13, lu dans le corpus, renvoie bien à L273-1 pour son champ territorial. Cette surveillance ne peut ressusciter une cotisation supprimée, modifier le plafond microsocial ni étendre aux indépendants la capitalisation réservée au premier champ du projet. Aucun barème de rupture ne découle de cet article.",
     "La mission publique de surveillance des obligations d'affiliation et de paiement reste entière, sans prétendre supprimer ou créer une obligation de cotisation.",
     "Les modalités de contrôle et les bases de chaque cotisation ne sont pas réécrites ici ; seules les obligations subsistant légalement peuvent être surveillées.",
     "Aucune charge nouvelle identifiée : maintien exact d'une compétence de surveillance existante, sans demande de données, délai, registre ou déclaration supplémentaire.")


# Vérifications requises : chaque cible conserve son empreinte exacte.
work_keys = list(refs['targets'])[:3]
contexts = {
    'L245-6': "Cet article concerne le chiffre d'affaires pharmaceutique et les remises de prix, non la rupture d'un emploi ; les durées des prises en charge médicamenteuses ne sont pas des durées de contrat de travail.",
    'L256-3': "L'habilitation vise la purge d'hypothèques garantissant des prêts des organismes, non un contrat de travail ; les notes de champ historiques ne modifient pas cet objet civil.",
    'L256-4': "La remise pour précarité porte sur des créances propres aux caisses ; les réparations d'accidents ou de fautes de l'employeur sont distinctes de l'indemnité ordinaire de rupture.",
    'L262-1': "La prévention sanitaire et le maintien dans l'emploi visent les ressortissants malades ou accidentés ; les renvois travail concernent le handicap et la réadaptation, pas les règles de rupture.",
    'L263-1': "L'action sanitaire et sociale des CAF relève du fonds du 2° de L223-1 et bénéficie aux ressortissants et familles ; elle n'est pas conditionnée par une catégorie ou une ancienneté de contrat privé.",
    'L263-2': "L'article concerne les clauses de sanctions des conventions de subvention du fonds d'action sociale des CAF ; ces conventions ne sont pas des contrats de travail.",
    'L272-2': "Les peines pour fraude dans la gestion des organismes relèvent du droit pénal, même si un auteur a la qualité d'agent ; elles ne constituent pas une indemnité ordinaire de rupture de son emploi.",
    'L273-1': "La surveillance publique vise l'affiliation et les cotisations des employeurs et bénéficiaires ; elle ne fixe ni préavis ni forme ni indemnité de contrat de travail."
}
work_analyses = {
    'L1234-1': "La source fixe un préavis de licenciement selon l'ancienneté, alors que la proposition fixe quinze jours calendaires pour les nouveaux contrats, sans effacer autorisations, procédures collectives et anciens préavis. Ce délai individuel et sa notification n'ont pas à être importés dans la présente règle.",
    'L1221-2': "La source admet encore des CDD ; la proposition impose une durée indéterminée aux relations privées nouvelles et conserve la transition des anciens contrats. Aucune formation, aide, prise en charge ou mission visée ici ne peut rétablir un terme automatique de l'emploi, ni fermer les avantages aux futurs éligibles.",
    'L1234-9': "La source ouvre l'indemnité de licenciement à huit mois ; la proposition distingue les contrats nouveaux avec seuil d'un an au terme effectif, préavis inclus, puis 0,20 mois sur toute l'ancienneté, mois complets au prorata, plafond de six mois, employeur seul, et les droits antérieurs. Elle réserve la faute grave, les indemnités plus favorables et les réparations distinctes. Ce barème ne limite aucun droit propre visé ici."
}
special = {
    ('L245-6', 'L162-16-5-2'): "Le renvoi porte sur les remises du III et sur la prise en charge compassionnelle, non sur le 1 an/quinze jours du contrat unique. La source et la proposition conservent notamment la restitution/prise en charge par indication et leurs conditions. Leur déduction reste intégralement dans le dénominateur du plafond III E ; la suppression des contributions ne supprime ni remises autonomes ni continuité de traitement des patients.",
    ('L245-6', 'L162-16-5-1-2'): "Les renvois identifient le régime temporaire après accès précoce et les remises correspondantes : le 3° bis de L138-10 lu au corpus reste distinct. Dans L245-6, la catégorie reste au III A 4° pour le plafond, et les remises restent déduites au III E. Durée de prise en charge, avis médical, décote et droits de futurs patients ne sont pas des termes d'emploi et ne sont pas supprimés.",
    ('L245-6', 'L162-16-5-1-1'): "La cible fixe les remises annuelles, restitutions et remises supplémentaires liées à l'accès précoce, dont le III B permet deux années de versement ou une décote d'au plus 3 %. Ces avantages autonomes, y compris pour futurs éligibles, ne sont pas confondus avec la contribution supplémentaire L245-6 supprimée. Le plafond III E conserve expressément la déduction des remises de cette cible ; son annualité de prix n'est ni celle de l'IS ni celle d'un contrat de travail.",
    ('L256-3', 'L623-1'): "Le renvoi figure seulement dans la note historique d'extension à la vieillesse non salariée. Le texte actuel fourni de L623-1 concerne maternité, paternité, adoption et deuil des indépendants, avec cessation d'activité, et ses notes incluent la réserve QPC de 2025 sur la filiation d'un couple de femmes. Il ne crée aucune extension actuelle du pouvoir de purge ni condition d'ancienneté de salarié : l'habilitation générale de L256-3 demeure, sans fermeture de ces prestations.",
    ('L256-4', 'L376-1'): "La source organise un recours subrogatoire poste par poste, exclut en principe les préjudices personnels et préserve la préférence de la victime partiellement indemnisée. La réduction pour précarité ne porte que sur la créance propre de la caisse et n'éteint pas la réparation de la victime. Aucune condition d'ancienneté, notification de licenciement ou plafond de six mois ne s'applique à ces droits d'accident.",
    ('L256-4', 'L376-2'): "La priorité de la victime ou de ses ayants droit sur la caisse pour les débours est expressément l'objet de ce renvoi inclus dans L376-1 à L376-3. Elle reste intacte lorsqu'une créance de caisse est réduite pour précarité ; la proposition le dit. Il ne s'agit ni d'un préavis individuel ni d'une indemnité de rupture, même si la victime est salariée.",
    ('L256-4', 'L452-2'): "La cible règle la majoration AT-MP pour faute inexcusable et ses limites liées au capital, au salaire annuel et aux rentes des ayants droit, avec récupération par la caisse. La remise pour précarité de sa créance ne réduit pas la majoration due à la victime ; la note vise les majorations prenant effet depuis le 1er avril 2013. Ni le seuil d'un an ni le plafond ordinaire de six mois ne s'y substituent.",
    ('L256-4', 'L452-3'): "La cible reconnaît les réparations de souffrances et préjudices propres, l'indemnité forfaitaire à 100 % d'incapacité et le préjudice moral des ayants droit ; la caisse avance puis récupère. Sa note QPC de 2010 conserve la réserve indiquée. L256-4 ne remet que la créance de caisse et maintient le droit du bénéficiaire, sans franchise d'un an ni limitation au barème ordinaire de rupture.",
    ('L256-4', 'L452-4'): "Le renvoi inclut le juge de la faute inexcusable, les garanties, l'assurance et l'appel en cause de l'organisme d'accueil pour certains stages ; la note fixe la rédaction au 1er juillet 2026 et comporte une date de loi à contrôler sans correction silencieuse. Ces garanties et la responsabilité restent distinctes de la remise de créance et du contrat unique : la durée du stage n'est pas assimilée à la durée d'un emploi.",
    ('L256-4', 'L452-5'): "La faute intentionnelle ouvre la réparation de droit commun non couverte, impose à la caisse le service des prestations et lui ouvre un recours, avec constitution de certaines rentes dans les deux mois. La réserve constitutionnelle de 2010 de la note est conservée. La remise pour précarité ne plafonne pas le droit de la victime ni ce régime spécial par le préavis de quinze jours ou l'indemnité ordinaire.",
    ('L256-4', 'L454-1'): "Le recours contre un tiers responsable, les préjudices personnels réservés à la victime, les frais de gestion et les conditions de subrogation composent le champ de cette cible. La remise ne porte que sur les créances propres des caisses et laisse les réparations du tiers envers la victime. Les deux mois de constitution de rente ne sont pas un préavis de rupture ; aucune condition d'ancienneté n'est importée.",
    ('L263-1', 'L223-1'): "Le seul 2° est visé : fonds d'action sanitaire et sociale et son programme, conservés à cette subdivision dans la proposition qui retire l'arrêté ministériel distinct. L263-1 n'impose pas ce visa et peut rester entier. Les 5° à 8°, leurs remboursements de congés, la fraction de 60 %, les agents publics et la transition naissance 2026 ne sont pas modifiés ni soumis à une ancienneté de contrat unique.",
    ('L263-2', 'L223-1'): "Le 2° identifie seulement le fonds finançant les subventions ; la suppression de l'obligation de clauses de sanctions ne supprime ni ce fonds, ni son programme, ni son soutien à l'accueil du jeune enfant. La proposition cible confie le programme au conseil sans arrêté distinct et reste compatible. Les remboursements de congés des 5° à 8° et leurs bénéficiaires futurs, publics ou privés, ne relèvent pas de la réforme des sanctions conventionnelles.",
    ('L272-2', 'L623-1'): "L623-1 n'est mentionné que dans une note historique d'application aux indépendants ; son texte actuel fourni porte sur maternité/paternité/adoption/deuil, avec réserve QPC de filiation en 2025. Il ne renvoie pas à ces maxima pénaux et n'est pas une règle de licenciement. La suppression de la sursanction n'altère ni les prestations, ni les durées protectrices de cessation d'activité, ni leurs situations futures éligibles.",
    ('L273-1', 'L623-1'): "L'ancienne note d'extension à la vieillesse n'est pas la matière de la cible actuelle, qui protège maternité, paternité, adoption et deuil des indépendants. Ses durées de cessation, son indemnisation et la réserve QPC de 2025 demeurent dans leur champ. La surveillance de cotisations légalement dues n'ajoute aucun préavis ni seuil d'ancienneté de salarié et ne ferme aucun avantage futur de cette cible."
}

for n, a in answers.items():
    key = a['code_id'] + '|' + a['source_id']
    checks = []
    for target_key in refs['requirements'][key]:
        t = refs['targets'][target_key]
        tn = t['number']
        if target_key in work_keys:
            assessment = contexts[n] + ' ' + work_analyses[tn]
        else:
            assessment = special[(n, tn)]
        checks.append(dict(target_key=target_key, view_sha256=t['view_sha256'], assessment=assessment))
    a['reference_checks'] = checks

answers['L245-6']['review_notes'] += " Le renvoi du III A 6° à la loi de financement pour 2022 est développé en toutes lettres : sa première mention figurait dans l'ancien II A supprimé. Les lettres des subdivisions supprimées restent individualisées ; le III E nouveau ne s'applique qu'aux années nouvelles, le plafond cumulé antérieur étant conservé pour les anciennes années."
answers['L256-4']['review_notes'] += " Incohérence documentaire préexistante à contrôler : la note de L452-4 date la loi n° 2025-1403 du 31 décembre 2025, tandis que les autres sources fournies la datent du 30 décembre ; aucune correction de cette note extérieure au lot n'est prétendue."

ordered = [answers[s['number']] for s in sources]
assert len(ordered) == 24
Path('answer.json').write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + '\n')
