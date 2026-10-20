import json
import re
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
references = json.loads(Path('reference-targets.json').read_text())
answers = []


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', xml))).strip()


def base(index, reason, review, assessment, limitations, burdens):
    source = sources[index]
    result = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    result.update({
        'proposed_xml': None,
        'reason': reason,
        'review_notes': review,
        'status': 'retained_unchanged',
        'classification': 'retained_necessary',
        'substantive_impact': {
            'version': 1,
            'classification': 'retained_necessary',
            'assessment': assessment,
            'scope_limitations': limitations,
            'new_burdens_review': burdens,
            'effects': [],
        },
        'reference_checks': [],
    })
    answers.append(result)
    return result


def draft(result, xml, classification):
    result['proposed_xml'] = xml.strip()
    result['status'] = 'rewrite_draft'
    result.pop('classification', None)
    result['substantive_impact']['classification'] = classification


def reduction(result, removed):
    result['change_type'] = 'normative_reduction'
    result['reform_policy_id'] = 'editorial_direction_2026_10_19'
    result['removed_provisions'] = removed


def repeal(result, scope):
    result['change_type'] = 'full_repeal'
    result['repeal_policy_id'] = 'editorial_direction_2026_10_19'
    result['repeal_scope'] = scope


def effect(result, *, kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition, replacement_or_new_burdens,
           source_quote, proposed_quote):
    result['substantive_impact']['effects'].append({
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': affected_population,
        'conditions_and_transition': conditions_and_transition,
        'replacement_or_new_burdens': replacement_or_new_burdens,
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    })


# 1722 quater : le sursis est un avantage, et non le fait générateur de la taxe.
a = base(0,
    "Coordination de fond de l'abolition des droits de succession : l'article ne crée aucun impôt, mais ouvre un sursis favorable pour un terrain soumis au délaissement. Sa règle devient sans objet uniquement pour les décès entièrement soustraits aux droits successoraux. L'abrogation prospective du précédent brouillon est conservée et sa transition est précisée pour laisser demander le sursis des successions anciennes après l'entrée en vigueur. Aucune seconde suppression de taxe n'est comptée ici.",
    "Source et note intégralement examinées. Le texte initial intégral de l'article 22 de SRU joint à sru_context distingue la renumérotation de l'ancien L. 230-1 en L. 221-3, au I, de la nouvelle organisation du titre des délaissements, au II ; il contient le sursis dans L. 230-2. Le L. 230-1 actuel fourni dans reference-targets n'est ni un contrat de travail ni une règle d'ancienneté. Son délai de deux mois concerne les autres titulaires de droits et leur indemnisation. La piste historique LEGIARTI000006313665 est une référence documentaire sans texte historique intégral dans le lot ; aucun service externe n'a été consulté et aucune filiation exhaustive ou clôture des 209 articles SRU n'est déclarée. Le L. 230-2 public du corpus a été lu : moitié de l'actif successoral, demande d'acquisition sous six mois si le défunt ne l'avait pas faite, sursis limité au prix et jusqu'à son paiement. Ces conditions restent applicables aux décès anciens. Sa proposition locale demeure à droit constant et nécessite une coordination avec l'abolition pour les décès nouveaux ; cette coordination extérieure au lot n'est pas présentée comme réalisée. L'effet fiscal principal doit rester porté par les articles d'assiette successorale et 990 I, sans donation entre vifs abolie ni impôt de remplacement. Les formalités civiles, la publicité foncière et l'exonération autonome des plus-values en cas de délaissement restent distinctes.",
    "Par rapport à la source officielle entière, disparition prospective du seul mécanisme de sursis devenu inutile en l'absence de droits de succession. L'avantage reste intégral pour les décès anciens. Il s'agit d'une coordination de la mesure successorale, sans diminution d'impôt supplémentaire propre à cet article.",
    "L'abolition générale dépend du corps successoral coordonné hors de ces douze articles. Le L. 230-2 fourni par le corpus n'a pas encore de proposition coordonnée à cette abolition. L'histoire complète du numéro 1722 quater n'est pas fournie ; aucune conclusion d'achèvement du volet SRU n'en est tirée.",
    "Aucune charge nouvelle n'est identifiée : aucun certificat, dépôt, garantie ou délai de remplacement n'est créé. Les conditions anciennes du sursis sont conservées pour leurs seuls décès, et les procédures civiles de délaissement subsistent selon leurs fondements propres.")
draft(a, """<p>Le présent article est abrogé pour les transmissions résultant de décès survenus à compter de l'entrée en vigueur de la loi portant suppression des droits de succession. Ces transmissions ne donnent lieu à aucun droit de mutation à titre gratuit par décès ; aucun sursis de paiement ni justificatif exclusivement destiné à l'obtention de ce sursis ne peut être exigé à leur titre.</p>
<p>Pour les décès antérieurs à cette entrée en vigueur, le sursis au recouvrement des droits de mutation afférents à la succession demeure ouvert dans les conditions des articles L. 230-1 et L. 230-2 du code de l'urbanisme applicables à la date du décès, même lorsque la demande d'acquisition, le paiement du prix ou le recouvrement intervient après cette entrée en vigueur. Il demeure limité au montant du prix du terrain et prend fin au paiement de ce prix. Les règles antérieures continuent de régir la liquidation, les garanties, les contrôles, le recouvrement, les restitutions, les prescriptions et les recours relatifs à ces décès, sans droit général au remboursement des sommes légalement dues.</p>
<p>L'abrogation laisse subsister les droits de délaissement et leurs garanties civiles. Elle ne modifie ni les donations entre vifs ni les impôts dont le fait générateur est distinct de la transmission par décès.</p>""", 'coordination_only')
repeal(a, "Suppression, pour les seuls décès postérieurs à la bascule successorale, du mécanisme de sursis et des justificatifs exclusivement destinés à ce sursis, l'impôt successoral correspondant étant intégralement supprimé ; maintien du sursis et de ses conditions pour les décès anciens.")
a['benefit_review'] = "L'unique avantage de la source est le sursis au recouvrement des droits successoraux, à concurrence du prix du terrain délaissé et jusqu'à son paiement. Il demeure ouvert, même sur demande postérieure à la réforme, pour tout décès ancien remplissant les conditions de L. 230-2. Pour les décès nouveaux, la suppression intégrale des droits successoraux rend ce sursis sans objet, sans prélèvement équivalent ni fermeture du droit civil de délaissement."
target_key = references['requirements'][a['code_id'] + '|' + a['source_id']][0]
a['reference_checks'] = [{
    'target_key': target_key,
    'view_sha256': references['targets'][target_key]['view_sha256'],
    'assessment': "Le L. 230-1 officiel et sa proposition fournie ont été lus en entier : ils organisent le délaissement des terrains visés par L. 152-2, L. 311-2 et L. 424-1, la mise en demeure en mairie et la publicité collective des autres intéressés. Le délai de deux mois assorti d'une perte du droit à indemnité concerne ces intéressés, sans rapport avec le préavis de quinze jours, le seuil d'un an ou l'indemnité du contrat privé unique. Aucun salarié ni contrat de travail n'est visé. La proposition, de même portée, n'est pas le droit en vigueur. Le renvoi est maintenu expressément pour les décès anciens ; pour les décès nouveaux, l'impôt supprimé n'exige plus de sursis, tandis que la procédure civile de délaissement reste applicable. La condition de moitié d'actif et le délai de six mois appartiennent au L. 230-2 distinct, également lu dans le corpus, et ne sont pas attribués au L. 230-1."
}]
effect(a,
    kind='coordination', measure_id='droits-succession-suppression',
    description="Retrait du sursis devenu sans objet pour les décès sans aucun droit successoral, avec maintien intégral de l'avantage des décès anciens.",
    before="Sursis des droits de mutation successoraux à concurrence du prix du terrain soumis au délaissement, jusqu'à son paiement et aux conditions des renvois ; l'article ne fixe ni taux ni assiette d'un impôt autonome.",
    after="Aucun sursis nécessaire pour les décès à compter de la bascule, puisque leurs droits successoraux sont intégralement supprimés ; le sursis antérieur reste ouvert pour les décès précédents.",
    unit='legal_duty', affected_population="Ayants droit d'un propriétaire décédé dont le terrain relève d'un droit de délaissement.",
    conditions_and_transition="Date du décès déterminante. Les demandes postérieures relatives à un décès ancien restent recevables selon les conditions anciennes, sans remboursement rétroactif général.",
    replacement_or_new_burdens="Aucun justificatif ni impôt de remplacement ; procédures civiles maintenues. Coordination du L. 230-2 et du corps successoral à assurer séparément.",
    source_quote=plain(sources[0]['source_xml']),
    proposed_quote="Ces transmissions ne donnent lieu à aucun droit de mutation à titre gratuit par décès ; aucun sursis de paiement ni justificatif exclusivement destiné à l'obtention de ce sursis ne peut être exigé à leur titre.")


# 4 A : fondement territorial, sans obligation procédurale autonome.
a = base(1,
    "Maintien intégral de la source officielle après examen du brouillon stylistique. Les deux alinéas délimitent respectivement l'assujettissement des résidents sur leurs revenus mondiaux et celui des non-résidents sur leurs seuls revenus français. Ils évitent notamment d'imposer les revenus étrangers des non-résidents et ne créent aucun agrément, justificatif ou dépôt autonome à retirer. Supprimer ce fondement reviendrait à abolir ou rendre indéterminé l'IR personnel, au-delà des suppressions décidées ; aucune reformulation n'est nécessaire.",
    "Le brouillon précédent ne changeait aucun élément normatif et n'est pas compté comme une simplification. Articulation contrôlée avec les 4 B et 4 bis assignés : critères de domicile et réserve conventionnelle au 4 B, attribution conventionnelle au 4 bis. Les taux, exonérations catégorielles, règles de source et conventions gardent leur champ. Le régime de distribution concerne l'IS ordinaire, pas cet IR. Les capitaux successoraux ne deviennent pas des revenus par ce seul texte.",
    "Aucune modification par rapport à la source officielle entière : maintien du champ territorial nécessaire de l'IR, y compris la limitation favorable des non-résidents aux seuls revenus français. Aucun impôt ni formalité supprimé n'est revendiqué.",
    "Les règles détaillées de source, les conventions applicables à chaque personne et les taux d'IR ne sont pas révisés dans cet article. Ce maintien ne mesure ni recettes ni complexité globale.",
    "Aucune charge nouvelle n'est identifiée, car aucun nouveau corps ni nouvelle condition n'est introduit ; les deux règles territoriales de la source seront reproduites intégralement.")


# 4 B : supprimer une présomption spéciale, garder les critères effectifs et les conventions.
a = base(2,
    "Réduction de fond supplémentaire au regard du brouillon antérieur : retirer la présomption spéciale d'activité professionnelle principale des dirigeants tirée du siège français et du chiffre d'affaires supérieur à 250 millions d'euros, ainsi que la liste devenue inutile et le calcul de groupe attachés à cette présomption. Le siège et le volume d'activité de l'entreprise ne suffisent pas à localiser l'activité effective de son dirigeant. Les critères ordinaires de foyer, séjour, activité professionnelle et intérêts économiques demeurent ; leur application permet toujours de caractériser et contrôler une domiciliation réelle ou frauduleusement dissimulée. À droit constant pour la réserve des conventions, l'exception d'activité accessoire et le régime des agents publics à l'étranger.",
    "Les huit alinéas de la source ont été examinés. Le deuxième alinéa du b porte désormais l'absence de présomption spéciale ; le troisième reste matérialisé comme abrogé, sans déplacer le c, la réserve conventionnelle ou le 2. Le seuil strictement supérieur à 250 millions et l'agrégation au sens de L. 233-16 du code de commerce sont retirés avec la seule présomption dont ils définissaient le champ ; aucun seuil nouveau n'est fixé. Le renvoi à ce code extérieur ne subsiste donc plus dans le corps proposé ; son régime de consolidation n'est pas modifié. Les critères généraux restent alternatifs. Le 2 conserve l'exigence d'absence d'impôt personnel sur l'ensemble des revenus dans le pays d'exercice, et non celle d'un simple taux inférieur. La transition porte sur les années civiles commençant à compter de l'entrée en vigueur, sans changement rétroactif du domicile ni des contentieux. Aucun domicile conventionnel n'est présumé français.",
    "Suppression réelle de la présomption légale spéciale et de la preuve contraire qu'elle imposait à certains dirigeants, comparée à la source entière. Il n'est supprimé ni l'IR des dirigeants ni les critères généraux de résidence ; aucun montant de baisse d'impôt n'est démontré.",
    "Seules les années nouvelles et la présomption spéciale des dirigeants sont concernées. La justification du caractère accessoire de l'activité prévue au premier alinéa du b subsiste. Les règles de contrôle et de preuve de droit commun et les conventions ne sont pas réécrites ; les conséquences individuelles et le solde de recettes sont inconnus.",
    "Aucune charge nouvelle n'est identifiée : l'examen de l'activité effective relève des critères déjà applicables, sans dossier, attestation, registre ou déclaration de remplacement. La précision négative interdit de reconstituer la présomption par le seul siège ou chiffre d'affaires.")
xml = sources[2]['source_xml']
paragraphs = re.findall(r'<p>.*?</p>', xml, re.S)
assert len(paragraphs) == 8
paragraphs[3] = "<p>L'exercice à titre principal en France de l'activité professionnelle d'un dirigeant s'apprécie d'après son activité effective, sans présomption tirée du siège ou du chiffre d'affaires de l'entreprise qu'il dirige.</p>"
paragraphs[4] = "<p>(Abrogé.)</p>"
xml = '\n'.join(paragraphs) + "\n<p>La suppression de la présomption spéciale applicable aux dirigeants et de ses modalités s'applique pour la détermination du domicile fiscal au titre des années civiles commençant à compter de l'entrée en vigueur de la loi portant la présente réforme. Les années antérieures demeurent soumises aux dispositions qui leur étaient applicables, y compris pour les contrôles, le recouvrement, les restitutions, les prescriptions et les recours.</p>"
draft(a, xml, 'material_reduction')
reduction(a, [
    "Présomption d'activité principale en France attachée au siège français et au chiffre d'affaires annuel supérieur à 250 millions d'euros, avec charge spéciale de preuve contraire pour les dirigeants concernés.",
    "Calcul agrégé du chiffre d'affaires des entreprises contrôlées et liste spéciale des fonctions dirigeantes, devenus sans objet avec le retrait de cette présomption.",
])
effect(a,
    kind='obligation_removed', measure_id='domicile-dirigeants-fin-presomption',
    description="Suppression de la charge spéciale de renverser une présomption d'activité principale, fondée sur les caractéristiques de l'entreprise plutôt que sur l'activité effective du dirigeant.",
    before="Dirigeants énumérés d'une entreprise à siège français réalisant en France plus de 250 millions d'euros de chiffre d'affaires annuel, avec agrégation du groupe : activité principale en France présumée sauf preuve contraire. Aucun taux d'impôt n'est fixé par cette règle.",
    after="Pas de présomption liée au siège ou au chiffre d'affaires ; appréciation de l'activité effective selon les critères ordinaires de domicile, avec réserve conventionnelle inchangée. Aucun taux ou assiette d'IR générale n'est modifié ici.",
    unit='legal_duty', affected_population="Dirigeants que la source soumet à la présomption spéciale, et futurs dirigeants de même situation.",
    conditions_and_transition="Années civiles commençant à compter de l'entrée en vigueur de la loi ; maintien des règles des années antérieures et de leurs recours.",
    replacement_or_new_burdens="Aucun justificatif de remplacement. Les critères ordinaires, la preuve d'une activité accessoire et les contrôles de domiciliation restent applicables.",
    source_quote="Les dirigeants des entreprises dont le siège est situé en France et qui y réalisent un chiffre d'affaires annuel supérieur à 250 millions d'euros sont considérés comme exerçant en France leur activité professionnelle à titre principal, à moins qu'ils ne rapportent la preuve contraire.",
    proposed_quote="L'exercice à titre principal en France de l'activité professionnelle d'un dirigeant s'apprécie d'après son activité effective, sans présomption tirée du siège ou du chiffre d'affaires de l'entreprise qu'il dirige.")


# 4 bis : l'assujettissement conventionnel ne double pas une formalité.
a = base(3,
    "Maintien intégral, sans reconduire la reformulation du précédent brouillon. Le 2° est le fondement interne d'assujettissement lorsque l'imposition de bénéfices ou revenus est attribuée à la France par une convention, quelles que soient nationalité et résidence. Il complète 4 A sans créer de dépôt ou de seconde taxation automatique. Sa suppression retirerait ce fondement général d'IR et ne constituerait pas l'élimination d'une obligation administrative en double. Le 1° déjà abrogé ne porte aucune charge à retirer.",
    "Les deux subdivisions et l'introduction sont maintenues. La convention doit effectivement attribuer l'imposition à la France ; ses limites et mécanismes contre la double imposition ne sont pas écartés. Lecture conjointe des 4 A et 4 B assignés, notamment de la réserve conventionnelle du 1 du 4 B. Le 1° abrogé n'est pas un emplacement Réservé. Aucun nouveau renvoi, taux, certificat ou critère de nationalité n'est ajouté.",
    "Aucun changement par rapport à la source entière : maintien du fondement conventionnel d'assujettissement et des limites qu'il implique. Aucun allègement n'est imputé à la simple réécriture stylistique du brouillon écarté.",
    "L'application de chaque convention et les règles catégorielles d'assiette relèvent de leurs textes propres. Aucune vérification de toutes les conventions françaises ni aucun bilan financier global ne sont revendiqués.",
    "Aucune charge nouvelle n'est identifiée : la source reste entière, avec le même 2° actif et le même 1° abrogé, sans nouvelle déclaration ou preuve conventionnelle spéciale.")


# 5 : préserver une exonération future, pas seulement les situations anciennes.
a = base(4,
    "Maintien intégral de l'exonération des ambassadeurs, agents diplomatiques, consuls et agents consulaires étrangers sous condition d'avantages analogues accordés aux agents français. Le brouillon ne faisait que reformuler cette règle favorable ; aucune nouvelle rédaction n'est nécessaire. L'exonération demeure ouverte aux futurs représentants remplissant ses conditions. La réciprocité délimite la règle diplomatique bilatérale ; aucune procédure nationale d'agrément ou déclaration redondante n'est instituée dans cet article.",
    "Les quatre catégories, la nationalité étrangère, la mesure des avantages analogues et la réciprocité restent exactement celles de la source. Les 1°, 2° et 2° bis restent respectivement périmé, abrogé et abrogé. Les immunités et exonérations conventionnelles autonomes ne sont ni supprimées ni révisées ; cet examen ne prétend pas avoir lu ou renégocié tous les traités diplomatiques.",
    "Aucune réduction nouvelle par rapport à la source entière ; conservation de l'exonération et de son accès futur. Supprimer cet avantage tant que l'IR subsiste augmenterait la charge de ses bénéficiaires.",
    "Seul le maintien du régime de l'article 5 est constaté. La portée de conventions diplomatiques ou consulaires particulières et l'appréciation concrète de la réciprocité ne sont pas tranchées pour chaque État.",
    "Aucune charge nouvelle n'est identifiée : aucun dossier, justificatif périodique ou autorisation n'est ajouté à l'exonération existante, conservée intégralement.")


# 6 : préserver les options, ouvrir une correction et éviter deux dépôts nouveaux.
a = base(5,
    "Réforme de fond conservée et allégée davantage : supprimer l'irrévocabilité et la forclusion de l'option d'imposition distincte de l'année du mariage ou du PACS au seul délai de la déclaration initiale. Après ce délai, l'exercice ou la révocation est possible dans le délai de réclamation, avec l'accord des deux personnes dont les impositions sont affectées. Une réclamation commune vaut rectification pour chacune : la double déclaration rectificative imposée par le brouillon antérieur est retirée. À droit constant, toutes les règles du foyer, de rattachement, de partage des revenus, de séparation et d'imposition des revenus au décès sont maintenues dans leurs alinéas.",
    "Tous les alinéas sources ont été relus, y compris la formule « de l'un ou des parents de l'un des conjoints » au 3 et la seconde présomption de partage du 6, dont la suppression silencieuse pourrait changer la portée. Les âges de moins de vingt et un ans et de moins de vingt-cinq ans, études, service militaire, infirmité, accueil d'un orphelin et revenus de l'année entière sont conservés. Le quatrième alinéa du 2° du II de l'article 156 a été lu dans le corpus : il exclut le cumul pension alimentaire/rattachement pour le même enfant et la même année, avec règle spéciale à la majorité ; le renvoi demeure exact. Les articles 196 et 196 A bis et l'article 170 ont été lus : enfants à charge, invalidité/cohabitation, déclaration et signature commune restent à leur champ. La nouvelle voie après le délai initial doit être coordonnée avec l'article 170 et ses modalités sans exiger deux rectifications des mêmes éléments ; ces articles extérieurs au lot ne sont pas annoncés comme modifiés. L'exclusion de l'option lorsque des partenaires déjà pacsés une année antérieure se marient est conservée : elle évite de rouvrir par le mariage l'option propre à la première constitution du même foyer. Le 8 concerne les revenus non encore taxés et le survivant, sans taxation du capital transmis par décès. Aucun seuil successoral, quotient familial ou barème nouveau n'est ajouté.",
    "La source officielle rend l'option du 5 irrévocable et limitée à la déclaration initiale. La proposition ouvre une correction dans le délai de réclamation et retire du brouillon l'exigence de deux déclarations rectificatives séparées. Classification mixed : l'accès est élargi, mais la voie nouvelle exige un accord et une réclamation communs ; aucun solde global de coût ou d'impôt n'est établi.",
    "Seule l'option de l'année de l'union est modifiée, pour les années civiles commençant à compter de l'entrée en vigueur. Les autres options de rattachement, les années anciennes et les règles générales de réclamation ne sont pas étendues. Le montant de l'avantage dépend des revenus des deux personnes ; aucune économie nationale n'est chiffrée.",
    "La réclamation commune comportant les éléments utiles et l'accord des deux intéressés sont les conditions de la nouvelle correction facultative après le délai initial. Elles ne s'ajoutent pas à l'option exercée à temps. Aucun dépôt rectificatif séparé, agrément, pièce en double ou délai spécial nouveau n'est imposé. Leur coût net par rapport au droit officiel ne peut pas être chiffré ici.")
paragraphs = re.findall(r'<p>.*?</p>', sources[5]['source_xml'], re.S)
assert len(paragraphs) == 19
original = paragraphs[14]
assert 'Cette option est exercée de manière irrévocable' in original
paragraphs[14] = original.replace(
    "Cette option est exercée de manière irrévocable dans les délais prévus pour le dépôt de la déclaration initiale des revenus mentionnée à l'article 170.",
    "Cette option peut être exercée ou révoquée dans les délais prévus pour le dépôt de la déclaration initiale des revenus mentionnée à l'article 170. Après l'expiration de ces délais, elle peut être exercée ou révoquée, d'un commun accord entre les deux intéressés, dans le délai de réclamation applicable à l'impôt établi au titre de cette année. Une réclamation commune comportant les éléments nécessaires à l'établissement concordant de leurs impositions vaut déclaration rectificative pour chacun des intéressés ; aucun dépôt séparé n'est exigé pour ces mêmes éléments."
)
paragraphs[14] = paragraphs[14].replace("Elle n'est pas applicable lorsque les partenaires", "Cette option n'est pas applicable lorsque les partenaires")
xml = '\n'.join(paragraphs) + "\n<p>Les règles d'exercice et de révocation de l'option prévues au second alinéa du 5 et les modalités de rectification qui les accompagnent s'appliquent à l'imposition des revenus des années civiles commençant à compter de l'entrée en vigueur de la loi portant la présente réforme. Les années antérieures restent régies par les dispositions qui leur étaient applicables, y compris pour les contrôles, le recouvrement, les restitutions, les prescriptions et les recours.</p>"
draft(a, xml, 'mixed')
reduction(a, [
    "Irrévocabilité de l'option pour l'imposition distincte des revenus de l'année du mariage ou du PACS, pour les seules années nouvelles visées par la transition.",
    "Forclusion attachée au seul dépôt initial de la déclaration pour exercer cette option, remplacée par l'accès facultatif au délai de réclamation de l'impôt de l'année concernée.",
])
effect(a,
    kind='relief_extended', measure_id='option-union-correction-delai-reclamation',
    description="Ouverture de l'exercice tardif ou de la révocation de l'option d'imposition distincte pour l'année de l'union, par une seule réclamation commune.",
    before="Option du 5 irrévocable et exercée au plus tard à la déclaration initiale de l'IR ; aucun nouveau taux ni assiette, mais un choix entre imposition commune et distincte pour cette seule année.",
    after="Option initiale conservée ; exercice ou révocation d'un commun accord encore possible dans le délai de réclamation applicable à l'impôt de l'année. Une réclamation vaut rectification pour les deux impositions.",
    unit='legal_duty', affected_population="Époux et partenaires pacsés éligibles à l'option de l'année de leur union ; exclusion des anciens partenaires pacsés se mariant entre eux maintenue.",
    conditions_and_transition="Revenus des années civiles commençant à compter de l'entrée en vigueur ; accord commun après le délai initial ; années anciennes inchangées.",
    replacement_or_new_burdens="Réclamation commune facultative et éléments nécessaires à des impositions concordantes ; pas de deuxième déclaration rectificative pour les mêmes éléments.",
    source_quote="Cette option est exercée de manière irrévocable dans les délais prévus pour le dépôt de la déclaration initiale des revenus mentionnée à l'article 170.",
    proposed_quote="Après l'expiration de ces délais, elle peut être exercée ou révoquée, d'un commun accord entre les deux intéressés, dans le délai de réclamation applicable à l'impôt établi au titre de cette année.")
effect(a,
    kind='obligation_added', measure_id='option-union-correction-delai-reclamation',
    description="Condition procédurale de la voie nouvelle de correction : accord des deux personnes et réclamation commune contenant les éléments de rectification.",
    before="La source ne crée pas de procédure de révocation après le délai initial ; elle qualifie l'option d'irrévocable.",
    after="L'utilisation de la faculté nouvelle après le délai initial est subordonnée à un commun accord et à une réclamation commune ; celle-ci remplace toute déclaration rectificative séparée des mêmes éléments.",
    unit='legal_duty', affected_population="Seuls époux ou partenaires choisissant d'utiliser la correction nouvelle après le délai de déclaration initiale.",
    conditions_and_transition="Même transition que la faculté nouvelle ; aucune condition supplémentaire pour le choix effectué dans le délai initial ni obligation de demander une correction.",
    replacement_or_new_burdens="Condition nouvelle attachée à un droit nouveau ; aucun formulaire obligatoire ou dépôt séparé de remplacement. Solde net de conformité non chiffré.",
    source_quote="Cette option est exercée de manière irrévocable dans les délais prévus pour le dépôt de la déclaration initiale des revenus mentionnée à l'article 170.",
    proposed_quote="Une réclamation commune comportant les éléments nécessaires à l'établissement concordant de leurs impositions vaut déclaration rectificative pour chacun des intéressés ; aucun dépôt séparé n'est exigé pour ces mêmes éléments.")


# 7 : garantie autonome d'égalité de traitement PACS / mariage.
a = base(6,
    "Maintien intégral de la source officielle. L'égalité de traitement du PACS et du mariage vise les règles d'imposition, d'assiette, de liquidation et de déclaration du code dans leur ensemble ; elle ne se confond pas avec les seules règles de foyer de l'article 6. Son abrogation pourrait fermer des avantages aux partenaires futurs. Elle n'impose pas une déclaration supplémentaire propre au PACS et ne contient aucun agrément ou délai autonome supprimable. Le brouillon stylistique n'est donc pas repris comme une réforme.",
    "Source et deux paragraphes de notes lus en entier : le décret d'application mentionné et l'application depuis l'imposition des revenus de 2011 relèvent de l'article 95 IV et V de la loi n° 2010-1657 du 29 décembre 2010. Ils ne fixent pas la date de la réforme future. Le maintien de l'article 7 étend dans les mêmes conditions aux partenaires le mécanisme proposé au 5 de l'article 6 ; il n'impose aucune double démarche. Les règles personnelles des conventions ou des successions ne sont pas modifiées par assimilation implicite.",
    "Aucun changement au regard de la source entière : conservation nécessaire d'une égalité fiscale transversale, incluant les avantages futurs des partenaires pacsés. Aucun dépôt ni impôt nouveau supprimé n'est comptabilisé.",
    "Cette assimilation ne réalise pas à elle seule toutes les coordinations réglementaires de la nouvelle option de l'article 6. Aucune conclusion sur des régimes ne relevant pas de l'IR n'est tirée.",
    "Aucune charge nouvelle n'est identifiée puisque l'article source est maintenu sans ajout ; aucune déclaration commune ou séparée supplémentaire n'est créée par cet article.")


# 8 : rendre cohérente la condition d'identification, sans compter un gain CRPA déjà acquis.
a = base(7,
    "Coordination nécessaire conservant l'allègement du brouillon : rendre explicite que l'identité et l'adresse des membres indéfiniment responsables d'une société en participation sont réputées indiquées si l'administration les détient légalement, à jour et sans ambiguïté de rattachement. La dispense s'étend aux états annuels, sans suppression des résultats et de leur répartition. Le nouveau corps précise aussi l'effet sur le 4 de l'article 206 pour éviter qu'une absence de retransmission fasse basculer la quote-part à l'IS. Ce réemploi recouvre les droits existants du CRPA : il est classé coordination_only et non comme une nouvelle obligation nette supprimée. Les sept catégories et les avantages du démembrement sont maintenus à droit constant.",
    "Lecture intégrale des sources des articles 206 (notamment 4), 162, de l'annexe II 138 et de l'annexe III 48 et 359 dans le corpus. Le renvoi nouveau et précis au 4 de l'article 206 n'est pas une cible fournie dans reference-targets ; son contenu officiel public et sa proposition locale ont été lus séparément, sans les confondre. Le 4 doit être coordonné à l'identification réputée faite ; le corps proposé règle expressément son articulation pour les seuls membres du 2°. Même coordination nécessaire pour la formulation du 162, la présomption de l'annexe II 138, le 1° du 2 de l'annexe III 48 et le 2 de son 359 : les noms/adresses connus ne sont pas redemandés, mais les autres données, résultats et quotes-parts restent dus. Les états des autres catégories et les dates/lieux de naissance ou professions ne sont pas abolis par ce texte. Le CRPA est une limite existante aux demandes répétées, pas une baisse nouvelle comptée. Aucun accès nouveau à des données protégées n'est autorisé. Les propositions locales de 206 et 359 préservent encore leurs anciennes formulations avant une clause de distribution : elles ne sont pas présentées comme entièrement coordonnées au présent 2°. La transition acquise aux exercices ouverts à compter de l'entrée en vigueur est conservée ; les régimes anciens ne basculent pas rétroactivement. Les options des 239 bis AA/AB, le décret de 1955, les exceptions du 239 ter et la catégorie SISA demeurent. L'IR des associés reste distinct de l'IS à la distribution ; le 218 bis lu dans le corpus règle le cas des personnes morales associées sans transformer l'IR de cet article en report. Le 359 ne peut rétablir un acompte annuel ordinaire sur les bénéfices conservés.",
    "La source entière subordonne le régime des membres de sociétés en participation à l'indication de leurs noms et adresses. La proposition explicite la satisfaction de cette condition par les données déjà légalement détenues et son articulation avec l'IS. Cette clarification et la reprise des droits de réemploi ne démontrent pas une nouvelle réduction nette par rapport à l'ensemble du droit applicable.",
    "La dispense concerne les seuls noms et adresses des membres du 2°, pour les exercices nouveaux ; les données manquantes ou modifiées, résultats et répartitions restent communiqués. Les articles d'exécution cités ne sont pas modifiés dans ce lot. Aucun gain budgétaire ou coût net global n'est établi.",
    "Aucune charge nouvelle n'est identifiée : la communication des seules données manquantes ou modifiées et des résultats reste celle nécessaire à l'identification et à l'imposition existantes. Aucun nouveau registre, numéro, attestation ou dépôt d'absence de changement n'est exigé. L'absence de gain CRPA supplémentaire est expressément reconnue.")
paragraphs = re.findall(r'<p>.*?</p>', sources[7]['source_xml'], re.S)
assert len(paragraphs) == 9
paragraphs[3] = "<p>2° Des membres des sociétés en participation, y compris les syndicats financiers, qui sont indéfiniment responsables et dont les noms et adresses ont été indiqués à l'administration. Pour l'application du présent 2° et du 4 de l'article 206, ces noms et adresses sont réputés indiqués à l'administration lorsqu'elle détient légalement ces informations exactes et à jour et peut les rattacher sans ambiguïté à la société concernée. Ces informations ne font alors l'objet d'aucune communication supplémentaire, y compris dans les états annuels relatifs aux membres de la société. À défaut, seules les informations manquantes ou modifiées nécessaires à cette identification sont communiquées. L'absence de retransmission des informations ainsi détenues n'entraîne pas, à elle seule, l'assujettissement de la quote-part du membre à l'impôt sur les sociétés en application du 4 de l'article 206. Les obligations de déclarer les résultats et leur répartition entre les membres restent applicables ;</p>"
xml = '\n'.join(paragraphs) + "\n<p>Les règles d'identification et de dispense de retransmission prévues au 2° s'appliquent aux résultats des exercices ouverts à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les sociétés déjà constituées. Les résultats des exercices ouverts avant cette entrée en vigueur restent soumis aux dispositions qui leur étaient applicables, y compris pour les contrôles, le recouvrement, les restitutions, les prescriptions et les recours.</p>"
draft(a, xml, 'coordination_only')
effect(a,
    kind='coordination', measure_id='societes-participation-identification-reemploi',
    description="Articulation de la condition d'identification de l'article 8 avec l'article 206 et les droits existants de réemploi des informations détenues ; pas de seconde réduction comptée.",
    before="Membres indéfiniment responsables et noms/adresses indiqués à l'administration ; un défaut d'indication est aussi visé par le 4 de l'article 206. Les droits de réemploi existants restent extérieurs à la rédaction source.",
    after="Condition réputée satisfaite par les informations légalement détenues, exactes, à jour et rattachables à la société ; dispense explicite dans les états annuels et absence de bascule à l'IS pour leur seule non-retransmission.",
    unit='legal_duty', affected_population="Membres indéfiniment responsables de sociétés en participation, syndicats financiers compris, visés au 2°.",
    conditions_and_transition="Exercices ouverts à compter de l'entrée en vigueur, sociétés futures comme déjà constituées ; exercices précédents inchangés.",
    replacement_or_new_burdens="Seules informations manquantes ou modifiées communiquées ; résultats et répartition maintenus ; aucune collecte, autorisation d'accès ou attestation nouvelle. Gain supplémentaire au-delà du CRPA non démontré.",
    source_quote="2° Des membres des sociétés en participation-y compris les syndicats financiers-qui sont indéfiniment responsables et dont les noms et adresses ont été indiqués à l'administration ;",
    proposed_quote="Pour l'application du présent 2° et du 4 de l'article 206, ces noms et adresses sont réputés indiqués à l'administration lorsqu'elle détient légalement ces informations exactes et à jour et peut les rattacher sans ambiguïté à la société concernée.")


# 8 bis : éliminer le doublon sans perdre le champ des renvois par plages.
a = base(8,
    "Abrogation de la disposition autonome répétant l'imposition personnelle déjà énoncée au second alinéa de 1655 ter, conservée du précédent brouillon. Le contrôle des renvois est complété : les plages 8 à 8 ter et 8 à 8 quinquies englobent aussi ces sociétés et ne doivent pas perdre leur champ par cette suppression. Une clause expresse en préserve l'application, y compris les avantages. La règle d'imposition demeure dans 1655 ter ; aucune baisse d'IR, disparition de déclaration ou fusion d'obligations effectives n'est revendiquée.",
    "1655 ter et sa note ont été lus intégralement : son second alinéa prévoit l'IR ou l'IS des membres selon leur cas et leurs droits, avec réserves à 60, au 2° du I de 827 et au 2° du I de 828 et note vers 372 à 375 de l'annexe II. 218 bis renvoie déjà directement à 1655 ter. La recherche des renvois dans les sources du CGI et de ses quatre annexes ne relève pas de renvoi nominal explicite à l'article 8 bis du CGI ; elle ne suffit toutefois pas à exclure les renvois par plages. Les 150 U et 150 UB visent 8 à 8 ter et 150 UA vise 8 à 8 quinquies : ces trois textes, lus en entier, justifient la clause de continuité, sans supprimer leurs exonérations, seuils ou reports. Le renvoi nouveau au second alinéa de 1655 ter et les plages reprises ne sont pas des cibles du fichier reference-targets ; leur contenu public a été vérifié dans le corpus, sans cible supplémentaire ajoutée aux reference_checks. Les articles 6, 7, 8, 10 et 10 bis A de l'annexe III emploient le numéro 8 bis pour l'article de cette annexe relatif aux stocks : ils restent distincts et ne sont pas supprimés. L'abrogation est une coordination de structure et non une suppression de la transparence immobilière ; le régime IS des membres personnes morales demeure soumis à ses propres coordinations à la distribution.",
    "Au regard de la source entière, retrait d'un doublon de règle d'imposition personnelle, conservée intégralement par 1655 ter. Les renvois englobants gardent leurs bénéficiaires et redevables. Aucune charge fiscale ou procédurale effectivement distincte n'est supprimée : classement coordination_only.",
    "Le nombre de règles effectivement appliquées aux membres ne diminue pas. La recherche est bornée au CGI et aux quatre annexes du corpus ; elle ne constitue pas un inventaire de tous les textes extérieurs. Les avantages des renvois par plages sont préservés par la clause expresse.",
    "Aucune charge nouvelle n'est identifiée : la clause conserve les champs existants et ne requiert ni option, ni registre, ni déclaration, ni justification nouvelle. Aucun gain national de complexité n'est déduit de la seule abrogation du doublon.")
draft(a, """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme.</p>
<p>Pour l'application des dispositions qui visent les sociétés ou groupements relevant des articles 8 à 8 ter ou 8 à 8 quinquies, les sociétés mentionnées à l'article 1655 ter demeurent comprises dans ces références dans les mêmes conditions qu'avant cette abrogation. Leur régime fiscal et celui de leurs membres, notamment les exonérations, abattements, reports et autres avantages qui leur sont applicables, ne sont pas modifiés par cette abrogation. L'imposition personnelle de leurs associés ou actionnaires reste régie par le second alinéa de l'article 1655 ter.</p>
<p>Les impositions relatives aux revenus des périodes antérieures à cette entrée en vigueur restent régies par les dispositions qui leur étaient applicables, y compris pour les contrôles, le recouvrement, les restitutions, les prescriptions et les recours.</p>""", 'coordination_only')
repeal(a, "Retrait intégral de la disposition autonome de l'article 8 bis répétant l'assujettissement personnel des membres des sociétés transparentes immobilières, lequel subsiste sur le fondement distinct de 1655 ter ; aucun impôt ni obligation déclarative n'est supprimé, et les champs des renvois par plages sont expressément conservés.")
effect(a,
    kind='coordination', measure_id='transparence-immobiliere-retrait-doublon',
    description="Abrogation du doublon de la règle personnelle de 1655 ter, sans perte du champ des renvois englobant le numéro abrogé.",
    before="L'article 8 bis répète pour l'IR la règle de quote-part des revenus déjà prévue par le second alinéa de 1655 ter ; il n'impose pas de formalité séparée.",
    after="Dispositif autonome abrogé ; même IR ou IS personnel conservé par 1655 ter, et continuité expresse du champ des renvois 8 à 8 ter ou 8 à 8 quinquies, avec leurs avantages.",
    unit='regime', affected_population="Associés et actionnaires des sociétés immobilières transparentes mentionnées à 1655 ter.",
    conditions_and_transition="Abrogation à l'entrée en vigueur, continuité des règles de fond et des avantages pour les opérations futures ; impositions et recours anciens préservés.",
    replacement_or_new_burdens="Aucun remplacement d'impôt ou de déclaration ; clause de continuité de champ, sans formalité nouvelle.",
    source_quote="Les associés ou actionnaires des sociétés visées à l'article 1655 ter sont personnellement soumis à l'impôt sur le revenu pour la part des revenus sociaux correspondant à leurs droits dans la société.",
    proposed_quote="L'imposition personnelle de leurs associés ou actionnaires reste régie par le second alinéa de l'article 1655 ter.")


# 8 ter : régime professionnel d'IR distinct du régime d'IS.
a = base(9,
    "Maintien intégral de la source officielle après examen du brouillon. L'article attribue le bénéfice aux associés des sociétés civiles professionnelles et conserve cette transparence lorsqu'elles adoptent un statut coopératif. Ce n'est pas un IS annuel à abolir et il ne crée pas ici de déclaration spéciale ou d'agrément. Le renvoi au livre II de l'ordonnance définit les sociétés professionnelles éligibles ; sa disparition ferait perdre une délimitation et un avantage de régime, sans supprimer une charge administrative distincte. Aucun changement stylistique n'est conservé comme une réduction.",
    "Source et note lues en entier. Le 1er septembre 2024 est l'entrée en vigueur historique issue de l'article 134 de l'ordonnance n° 2023-77, pas celle de la présente réforme. L'article 206 officiel lu dans le corpus réserve expressément 8 ter à son 1 et permet l'option à l'IS au h du 3, avec renvoi au 239 également lu. Ces règles restent cohérentes sans modifier 8 ter : l'imposition annuelle des associés restés à l'IR n'est pas reportée à la distribution. Le délai de renonciation du 239 encore exprimé par référence aux acomptes d'IS doit être coordonné dans son propre lot avec le 1668 réformé ; il ne justifie pas de changer la présente attribution d'IR. L'ordonnance extérieure n'est ni prétendue réécrite ni utilisée pour recréer un CDD ou une formalité fiscale nouvelle.",
    "Aucun changement par rapport à la source entière. Maintien de la transparence professionnelle et de son extension aux coopératives, sans perte d'option favorable ni report fictif de l'IR personnel.",
    "L'organisation professionnelle du livre II de l'ordonnance extérieure et les modalités d'option du 239 ne sont pas réécrites ici. Aucun impôt acquitté par un associé particulier ni solde global n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : la règle d'attribution et ses conditions restent exactement celles de la source, sans nouvelle déclaration, autorisation ou condition de distribution.")


# 8 quater : quote-part maritime, sans déclaration individuelle en double.
a = base(10,
    "Maintien intégral de la source officielle. L'attribution du résultat déclaré par la copropriété de navire détermine le redevable et sa quote-part ; elle ne demande pas un état individuel supplémentaire. Supprimer cette attribution ou attendre une distribution étendrait le report d'IS à un IR personnel distinct. La référence au code des transports définit la copropriété éligible, pas une autorisation fiscale. Après examen des charges, aucun doublon de cette règle propre aux navires ne justifie une abrogation ; le précédent brouillon était seulement stylistique.",
    "Le renvoi L. 5114-30 à L. 5114-50 est conservé avec ses bornes exactes ; le contenu du code des transports n'a pas été fourni et aucune réécriture ou vérification exhaustive de ce code extérieur n'est revendiquée. L'article 61 A du CGI, lu en entier avec sa note vers LPF L. 53, détermine le résultat au bénéfice réel avant amortissement et impose les obligations correspondantes à la copropriété. Le 218 bis lu dans le corpus vise les membres personnes morales passibles de l'IS : son corps proposé distingue le résultat fiscal de référence de la distribution, sans report de l'IR des membres personnes physiques. La dispense d'identité du 2° de l'article 8 ne s'étend pas aux copropriétés de navires par le seul voisinage des articles. Les droits et proportions dans les résultats demeurent nécessaires.",
    "Aucune différence avec la source entière : maintien nécessaire de l'attribution personnelle des résultats maritimes. Aucune déclaration, cotisation ou taxe autonome supprimée n'est revendiquée.",
    "Le code des transports et les procédures du LPF ne sont pas compris dans la réécriture de ce lot. Les obligations de résultat de la copropriété ne sont pas simplifiées par le seul maintien de son attribution aux membres.",
    "Aucune charge nouvelle n'est identifiée puisque le corps officiel demeure intact ; aucun dépôt individuel supplémentaire ni condition d'emploi des bénéfices n'est introduit.")


# 8 quinquies : supprimer effectivement l'obligation fiscale de statuts types.
a = base(11,
    "Réduction de fond conservée après seconde lecture : supprimer la conformité obligatoire des statuts et du fonctionnement des copropriétés d'étalon à des statuts types approuvés par décret comme condition du régime fiscal. La déclaration d'un résultat, la quote-part des droits et l'inscription des biens communs visée par 238 bis M suffisent à l'attribution fiscale sans imposer une convention civile uniforme. Le premier alinéa officiel est maintenu intégralement ; le second porte la suppression opératoire et sa transition. Aucun agrément individuel n'est prétendu aboli : la source exige une conformité à un modèle, pas un visa de chaque copropriété. Aucune coupe supplémentaire dans l'identification du résultat ou les droits de chaque membre n'est justifiée.",
    "Les deux alinéas sources et le brouillon ont été lus intégralement. 238 bis M, lu en entier, exige l'inscription à l'actif des biens dont les membres d'une société en participation ont convenu de mettre la propriété en commun pour l'application des articles 8 et 60 ; il ne contient pas de formule ni de statuts types équins. La formulation source du renvoi est conservée : son articulation avec une copropriété équine doit être appréciée selon sa constitution et les biens effectivement communs, et ne vaut pas affirmation que toute indivision de cheval est une société en participation. Cette difficulté de champ préexistante est signalée, sans création d'un renvoi de substitution ni prétendue résolution exhaustive. Les articles 39 F, 61 A, 156 I 1° bis, 218 bis et 238 bis K ont été lus dans le corpus : amortissement de la part et calcul des plus-values, résultat avant amortissement, régime des déficits, cas des personnes morales et détermination de la quote-part selon le membre conservent leur portée. Le décret d'approbation des statuts types, extérieur aux sources fournies et non identifié avec certitude, doit perdre son effet de condition fiscale pour les exercices nouveaux ; il n'est ni numéroté fictivement ni présenté comme réécrit. Les clauses contractuelles des copropriétés anciennes gardent leurs effets civils. La protection animale et les règles sanitaires ne sont pas supprimées. L'IS à la distribution n'est pas étendu à l'IR personnel.",
    "Par rapport à la source officielle entière, une condition fiscale effective est retirée pour les copropriétés d'étalon : conformité des statuts et du fonctionnement à un modèle réglementaire. Le régime de quote-part et les avantages connexes restent ouverts aux futures copropriétés éligibles. Aucun taux fiscal ou résultat imposable n'est diminué par cet article.",
    "Suppression limitée à la condition fiscale du second alinéa pour les exercices ouverts à compter de l'entrée en vigueur. La portée préexistante du renvoi à 238 bis M et le décret d'approbation extérieur restent des points de coordination ; les règles civiles, sanitaires et les années anciennes demeurent distinctes. Coût net et perte de recettes non établis.",
    "Aucune charge nouvelle n'est identifiée : la conformité au modèle n'est remplacée ni par une déclaration, ni par un agrément, ni par une attestation. Résultats, droits des membres et conditions autonomes déjà présentes dans le premier alinéa sont conservés ; aucun nouveau registre n'est créé.")
first = re.sub(r'<[^>]+>', '', sources[11]['source_xml'].split('<br />')[1]).strip()
assert first.startswith('Chaque membre') and first.endswith('copropriété.')
draft(a, '<p>' + first + '</p>\n' + """<p>L'application du premier alinéa n'est pas subordonnée à la conformité des statuts ou des modalités de fonctionnement des copropriétés d'étalon à des statuts types approuvés par décret. Cette suppression de condition fiscale s'applique aux résultats des exercices ouverts à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour les copropriétés déjà constituées. Les exercices ouverts avant cette entrée en vigueur restent soumis aux dispositions qui leur étaient applicables, y compris pour les contrôles, le recouvrement, les restitutions, les prescriptions et les recours. Les conventions en cours conservent leurs effets civils ; leurs clauses ne sont ni annulées ni modifiées de plein droit. Les règles civiles régissant la copropriété ainsi que les règles sanitaires et de protection animale demeurent applicables.</p>""", 'material_reduction')
reduction(a, [
    "Conformité obligatoire des statuts et des modalités de fonctionnement des copropriétés d'étalon à des statuts types approuvés par décret comme condition d'application du régime fiscal, pour les seuls exercices nouveaux.",
])
effect(a,
    kind='obligation_removed', measure_id='coproprietes-etalons-fin-statuts-types-fiscaux',
    description="Suppression de la condition fiscale de conformité des statuts et du fonctionnement des copropriétés d'étalon à des statuts types réglementaires.",
    before="Pour les copropriétés d'étalon, imposition personnelle de la quote-part du résultat subordonnée à des statuts et un fonctionnement conformes aux statuts types approuvés par décret ; aucun taux n'est fixé ici.",
    after="Même imposition de la quote-part, mêmes conditions du premier alinéa et même résultat déclaré, sans condition fiscale de conformité aux statuts types ni formalité de remplacement.",
    unit='legal_duty', affected_population="Membres des copropriétés d'étalon relevant du premier alinéa, y compris les futures copropriétés et les futures années des copropriétés déjà constituées.",
    conditions_and_transition="Exercices ouverts à compter de l'entrée en vigueur ; exercices anciens et leurs recours conservés ; clauses civiles des conventions existantes non modifiées de plein droit.",
    replacement_or_new_burdens="Aucun agrément, déclaration ou modèle de remplacement. Règles civiles, sanitaires et de protection animale autonomes maintenues.",
    source_quote="Pour l'application de ces dispositions, les statuts et les modalités de fonctionnement des copropriétés d'étalon doivent être conformes à des statuts types approuvés par décret.",
    proposed_quote="L'application du premier alinéa n'est pas subordonnée à la conformité des statuts ou des modalités de fonctionnement des copropriétés d'étalon à des statuts types approuvés par décret.")


assert len(answers) == len(sources) == 12
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
