import ast
import html
import json
import re
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
# Read only literal article drafts; do not execute the earlier script.
drafts = {}
for node in ast.parse(Path('draft_answer.py').read_text()).body:
    if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name) and node.value.func.id == 'add':
        args = [ast.literal_eval(x) for x in node.value.args]
        n, paragraphs, reason, notes = args[:4]
        row = dict(proposed_xml='\n'.join('<p>'+p+'</p>' for p in paragraphs), reason=reason, review_notes=notes)
        if len(args)>4:
            row.update(change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19', removed_provisions=args[4])
        drafts[n] = row

def text(xml):
    return html.unescape(re.sub(r'<[^>]*>', '', xml or ''))

def paragraphs(n):
    return re.findall(r'<p>(.*?)</p>', drafts[n]['proposed_xml'], re.S)

def set_paragraphs(n, ps):
    drafts[n]['proposed_xml'] = '\n'.join('<p>'+p+'</p>' for p in ps)

# No new stylistic rewriting of necessary or already optional rules.
retained = {
'L2241-1': (
    "Maintien intégral après examen : les thèmes obligatoires protègent les salaires, l'égalité, les proches aidants, la santé, le handicap, la formation, les salariés expérimentés et l'accès à l'épargne. Les plafonds de quatre et cinq ans permettent déjà la négociation conventionnelle. Les alléger dans les seuls textes supplétifs évite d'abroger ce socle. Aucune réduction n'est attribuée au présent article.",
    "Contrôle des 1° à 7°, y compris les 2° bis et 5° bis, des quatre/cinq ans, de L4161-1 et de la dispense du 7° en présence d'un accord. L4161-1 et sa réserve historique pour 2015, 2016 et les trois premiers trimestres de 2017 ont été lus. Aucun prélèvement, dépôt administratif, agrément ni justificatif distinct n'apparaît ici. Les rythmes supplétifs modifiés restent dans les plafonds conservés ; aucune obligation de conclure un accord n'est ajoutée."),
'L2241-2-1': (
    "Maintien intégral du plan d'action type, faculté favorable aux entreprises de moins de trois cents salariés après échec de la négociation avec leurs syndicats représentatifs. Le document unilatéral identifie le plan effectivement appliqué ; l'information et la consultation, déjà possibles par tous moyens, assurent la participation du CSE et des salariés. Aucune formalité administrative ou homologation à retirer n'est instituée.",
    "Seuil strictement inférieur à trois cents ; échec préalable de la négociation ; CSE s'il existe et salariés tous deux concernés. Le renvoi au 5° bis de L2241-1 reste valide après l'espacement supplétif de L2241-14-1. Ce mécanisme reste ouvert aux futures entreprises éligibles, sans être réservé aux plans déjà établis. Un document unilatéral ne devient pas un accord collectif."),
'L2241-3': (
    "Maintien intégral : l'information nécessaire, les réponses motivées et l'intervention de la commission en cas de négociation déloyale garantissent un consentement éclairé. La source n'impose ni rapport distinct ni nouvelle remise systématique de documents déjà communiqués ; leur suppression ne serait donc pas un gain démontré. Aucun nouveau circuit d'envoi ou justificatif n'est créé.",
    "L2261-20 a été lu intégralement : saisine d'une organisation représentative ou initiative administrative possibles ; convocation obligatoire à la demande de deux organisations. L'allègement du déclenchement purement documentaire à L2241-18 ne retire pas la garantie du présent article. D2241-1 maintient un rapport salarial quinze jours avant l'ouverture : ce délai de préparation n'est pas confondu avec le préavis individuel de rupture. Le CRPA n'est pas présenté comme supprimant une obligation privée de négociation."),
'L2241-4': (
    "Maintien intégral de la faculté de négocier l'organisation de la branche à la demande d'une organisation. Ce texte n'exige ni négociation préalable supplémentaire ni approbation administrative : le rendre facultatif à nouveau ne retirerait aucune charge. Sa suppression fermerait au contraire une voie d'adaptation du calendrier, des thèmes et des modalités.",
    "Le renvoi de L2241-5 à cette négociation reste cohérent avec la suppression proposée du plafond spécial de durée de l'accord. La demande d'une seule organisation suffit toujours. La faculté concerne la branche ou le secteur professionnel ; les compétences et majorités de conclusion ne sont pas modifiées. Aucun circuit CPPNI précédemment supprimé n'est rétabli."),
'L2241-6': (
    "Maintien intégral de la faculté favorable d'aménager la périodicité dans l'accord thématique lui-même, sans imposer un accord d'organisation distinct. Les plafonds de quatre et cinq ans gardent les négociations effectives et les protections essentielles. L'examen n'identifie dans ce texte ni taxe, ni dépôt supplémentaire, ni réunion autonome à supprimer.",
    "Les 1° à 5° bis restent soumis à quatre ans, les 6° et 7° à cinq ans. Les accords en vigueur et leurs engagements plus fréquents ne sont pas effacés par la transition de L2241-7. Le plafond de renégociation n'est pas la durée de vie de l'accord d'organisation, dont la limite spéciale est retirée à L2241-5."),
'L2241-14-2': (
    "Maintien intégral des six thèmes facultatifs relatifs aux salariés expérimentés. Le verbe peut et la liste non exhaustive n'imposent ni négociation autonome ni déclaration. Supprimer ces possibilités de formation, d'accompagnement, de prévention et d'aménagement du travail retirerait des facultés favorables sans démontrer un allègement d'obligation.",
    "L2241-14-1 reste le support de la négociation de branche et L2242-22 conserve son renvoi à la présente liste facultative en entreprise. Aucune périodicité propre, condition d'âge chiffrée ou durée maximale d'emploi n'est ajoutée ici. Les six numéros sont conservés par reproduction intégrale de la source ; aucun effet fiscal ou de pension ne leur est attribué."),
'L2241-15': (
    "Maintien intégral après examen : l'examen quinquennal n'oblige pas à réviser toutes les classifications. Il vérifie les critères qui pourraient produire des discriminations, toutes les compétences et la priorité de réduction d'un écart moyen de rémunération. Cette fonction ne se confond pas avec la négociation salariale et justifie le maintien de ses quatre alinéas.",
    "Cinq ans, objectif de mixité, priorité de réduction des écarts et analyse des critères sont conservés. Les articles L2241-1 6°, L2241-5 b) et L2241-17 restent coordonnés ; aucun dépôt ni rapport autonome n'est prescrit ici. Le délai de cinq ans n'est ni une suspension des droits salariaux ni un délai de recours contre la discrimination. Aucun minimum conventionnel favorable n'est abaissé."),
'L2241-16': (
    "Maintien intégral de l'accès à la négociation des plans d'épargne interentreprises et des plans de retraite collectifs interentreprises, ainsi que de la dispense lorsqu'un accord existe déjà à ce niveau. Le texte n'impose pas d'instituer un plan ou d'y souscrire. Aucune charge administrative distincte n'est démontrée ; fermer cette négociation supprimerait une possibilité favorable.",
    "Périodicité de cinq ans et deux catégories de plans conservées. Les notes source ont été lues : ordonnance 2019-766, article 9 I, limite du 1er janvier 2020 ; décret 2019-807, article 9 II, entrée en vigueur le 1er octobre 2019. Ces dates historiques ne sont pas des dates de la réforme. Les futurs plans éligibles et leurs avantages restent ouverts ; la capitalisation projetée ne remplace pas ces dispositifs."),
'L2242-1': (
    "Maintien intégral du socle de négociation dans les entreprises dotées de sections syndicales représentatives. Rémunération, temps de travail, partage de la valeur, égalité et qualité de vie et des conditions de travail sont des garanties essentielles. Le texte n'impose aucun formulaire, rapport ou double dépôt. Une reformulation seule ne produirait pas de réduction démontrée.",
    "Deux subdivisions et plafond de quatre ans conservés. L2242-13 maintient par défaut les deux négociations annuelles : l'allègement propre aux branches ne les modifie pas. L2242-4 et L2242-5, lus, conservent la limitation des décisions unilatérales et le procès-verbal d'entreprise. La note source rattache le texte au 31 mars 2022 et aux conditions du II de l'article 40 de la loi 2021-1018 ; cette réserve historique est maintenue et n'est pas utilisée comme date future."),
'L2242-2': (
    "Maintien intégral : la gestion des emplois et des parcours protège l'anticipation des transformations et les mesures de formation et de mobilité. L'examen de L2242-10 et L2242-11 confirme une faculté existante d'organisation conventionnelle. La source ne démontre pas l'obligation de répéter une discussion déjà valablement menée dans une négociation commune ; aucune seconde fusion fictive n'est comptée.",
    "L2331-1, L2341-1 et L2341-2 ont été lus. Premier champ : au moins trois cents salariés. Champ communautaire distinct : au moins un établissement ou une entreprise de cent cinquante salariés en France, avec les conditions communautaires de définition conservées ; aucune condition nouvelle de section syndicale. L2242-13 et L2242-20 maintiennent trois ans en supplétif. L2242-20 comporte encore le renvoi ancien L2323-10 : incohérence préexistante signalée, non corrigée implicitement. Le regroupement conventionnel ne dispense pas des thèmes et interlocuteurs propres à chaque négociation."),
'L2242-2-1': (
    "Maintien intégral de la négociation sur l'emploi, le travail et les conditions de travail des salariés expérimentés, dans les entreprises et groupes d'au moins trois cents salariés dotés de sections syndicales représentatives. Les possibilités d'organisation conventionnelle existent déjà ; faute de prohibition démontrée d'une négociation commune, leur rappel ne justifierait pas une réduction normative revendiquée.",
    "L2242-22 et D2242-17 ont été lus en entier : cadence supplétive de trois ans, diagnostic d'entreprise, thèmes des L2241-14-1 et L2241-14-2 et examen du fonds de prévention de l'usure professionnelle restent à leur champ. Le diagnostic propre à l'entreprise n'est pas supprimé par la réforme de branche. Ne pas importer ici le champ communautaire à cent cinquante salariés de L2242-2. L2242-4 conserve la protection contre les décisions unilatérales. Aucun terme de mission, formation ou aide ne devient un terme d'emploi.")
}
for n,(reason,notes) in retained.items():
    drafts[n] = dict(proposed_xml=None, reason=reason, review_notes=notes, status='retained_unchanged')

# Retain useful information duties, without inventing a new saving from presumed double transmission.
n='L2241-5'
ps=paragraphs(n)
ps[7] = "4° Les informations que les organisations professionnelles d'employeurs remettent aux négociateurs sur les thèmes de la négociation qui s'engage et la date de cette remise ;"
set_paragraphs(n, ps)
drafts[n]['review_notes'] = "Les numéros 1° à 5° et lettres a), b), c) gardent leurs positions. Quatre et cinq ans sont les plafonds de périodicité conservés. L2222-4, lu, permet une durée déterminée ou indéterminée mais fixe cinq ans si l'accord est silencieux ; l'indétermination suppose donc une stipulation. Aucun accord antérieur n'est prolongé automatiquement. Les informations et leur date restent dues selon le 4° ; aucun gain de réemploi de données ou de double dépôt n'est revendiqué. L2231-6 et les règles de validité restent applicables. Lieux et calendrier peuvent toujours être fixés volontairement ; seule leur prédétermination exhaustive dans l'accord cesse d'être requise."

# Do not describe an existing information report as necessarily a second autonomous document.
n='L2241-11';ps=paragraphs(n)
ps[4] = "Les informations nécessaires à la négociation sont déterminées par voie réglementaire."
ps[5] = "La périodicité prévue au premier alinéa suit la transition de l'article L. 2241-7. Les mesures de rattrapage déjà convenues continuent de s'appliquer selon leurs engagements et leurs échéances."
set_paragraphs(n, ps)
drafts[n]['reason'] = "Réforme de fond : la négociation supplétive sur l'égalité professionnelle passe de trois à quatre ans ; le suivi du rattrapage salarial est coordonné avec la négociation salariale qui n'est plus nécessairement annuelle. Tous les thèmes, l'accès à l'information et le rattrapage demeurent. Aucune suppression de rapport n'est revendiquée : l'obligation d'information réglementaire reste entière."
drafts[n]['review_notes'] = "D2241-2 a été lu : rapport comparé dans les domaines des 1° et 2°, indicateurs chiffrés par secteur et diagnostic des écarts restent exigibles. Seule sa qualification triennale doit être coordonnée avec le rythme de quatre ans ; aucun rapport administratif nouveau n'est créé. L2241-8, L2241-17 et L2241-18 cessent de rétablir une annualité supplétive salariale de branche. Les accords plus fréquents et mesures de rattrapage restent applicables. Les obligations d'égalité et de transparence du droit supérieur ne sont pas abolies ; leur articulation européenne doit être contrôlée sans présumer la conformité de la seule rédaction."
drafts[n]['removed_provisions'] = ["Les échéances supplétives triennales de négociation sur l'égalité sont retirées au profit d'un rythme de quatre ans ; les droits de rattrapage et les engagements conventionnels restent applicables."]

n='L2241-13';ps=paragraphs(n)
ps[2] = "Les informations nécessaires à la négociation sont déterminées par voie réglementaire."
ps[3] = "La périodicité prévue au premier alinéa suit la transition de l'article L. 2241-7. Les droits et mesures d'insertion, d'aménagement, de formation et de maintien dans l'emploi demeurent applicables dans leur champ propre, y compris aux futures situations éligibles."
set_paragraphs(n, ps)
drafts[n]['reason'] = "Réforme de fond limitée au calendrier supplétif : l'échéance de trois ans devient une échéance de quatre ans, dans le plafond de L2241-1. Les mesures d'insertion et de maintien dans l'emploi, tous les domaines d'accès et les informations nécessaires demeurent. Aucun allègement de contribution liée à l'emploi des travailleurs handicapés n'est déduit de cet article de négociation."
drafts[n]['review_notes'] = "D2241-3 a été lu intégralement : son rapport présentant la situation de chaque secteur au regard de l'obligation d'emploi demeure ; sa désignation triennale est à coordonner. L5212-1 et suivants restent le fondement du régime distinct de l'obligation d'emploi, non modifié ici. Les aides et aménagements restent accessibles aux situations futures éligibles. Les accords plus fréquents, échéances déjà dues et recours suivent la transition de L2241-7. Aucun registre, justificatif, collecte ou dépôt de remplacement n'est ajouté."
drafts[n]['removed_provisions'] = ["Les échéances supplétives triennales de négociation relatives aux travailleurs handicapés sont supprimées au profit d'un rythme de quatre ans, sans suppression de leur information ni de leurs droits."]

# Remove an actual prerequisite, while retaining the information specified by D2241-5.
n='L2241-14-1';ps=paragraphs(n)
ps[0] = "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour engager une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge. L'ouverture de la négociation n'est pas subordonnée à l'établissement préalable d'un diagnostic ; l'analyse de la situation de ces salariés est conduite au cours de la négociation."
ps[6] = "Les informations nécessaires à la négociation sont déterminées par voie réglementaire. L'analyse de la situation comporte des indicateurs pertinents, reposant sur des éléments chiffrés, pour chacun des domaines mentionnés aux 1° à 4° ; elle peut être intégrée aux documents de travail de la négociation, sans diagnostic distinct exigé."
ps[7] = "La périodicité suit la transition prévue à l'article L. 2241-7. La suppression du diagnostic préalable s'applique dès l'entrée en vigueur de la loi, y compris aux négociations en cours, sans imposer de refaire les travaux déjà réalisés. Les droits à l'aménagement de fin de carrière, au temps partiel et à la retraite progressive restent ouverts selon leurs conditions propres."
set_paragraphs(n, ps)
drafts[n]['reason'] = "Réforme de fond : les échéances supplétives triennales deviennent quadriennales et le diagnostic cesse d'être une condition préalable à l'ouverture. L'analyse et les indicateurs restent nécessaires pendant la négociation, sans document autonome imposé. Les quatre thèmes et les possibilités favorables de fin de carrière et de transmission des compétences sont conservés."
drafts[n]['review_notes'] = "D2241-5 a été lu : indicateurs pertinents et chiffrés par domaine conservés ; ses termes triennale et diagnostic préalable doivent être coordonnés. Le présent texte déroge directement au préalable de branche. L2242-22 et D2242-17, lus, imposent un diagnostic d'entreprise sur leur fondement propre : il demeure. Le renvoi du premier à la liste des 1° à 4° reste utilisable. L2241-2-1 et son plan type restent ouverts aux futures entreprises éligibles ; aucun aménagement, retraite progressive ou aide n'est retiré. Les indicateurs ne sont pas une nouvelle collecte : ils figurent déjà dans D2241-5."
drafts[n]['removed_provisions'][1] = "L'établissement préalable d'un diagnostic comme condition d'ouverture de la négociation de branche est supprimé ; l'analyse et ses indicateurs peuvent être traités pendant la négociation sans diagnostic autonome."

# Preserve the existing data and preparation obligations; do not claim a new CRPA saving.
n='L2241-12';ps=paragraphs(n)
ps[2] = "Les mêmes organisations se réunissent également au moins une fois tous les quatre ans pour négocier sur les matières définies aux articles L. 2242-15 et L. 2242-16."
ps[3] = "La transition prévue à l'article L. 2241-7 s'applique aux périodicités. La dispense de recours obligatoire à un observatoire s'applique dès l'entrée en vigueur de la loi, sans faire obstacle à la poursuite des négociations en cours ni aux engagements conventionnels en vigueur. Les observatoires et les obligations d'information disposant d'un fondement autonome conservent leur régime."
set_paragraphs(n, ps)
drafts[n]['reason'] = "Réforme de fond : les deux échéances supplétives de trois ans passent à quatre ans et le recours imposé aux travaux d'un observatoire déterminé est retiré. La négociation conserve la mixité, les conditions de travail, la prévention, les transitions écologique et énergétique et toutes les matières visées par les renvois du troisième alinéa. Le texte n'est pas présenté comme supprimant un observatoire institué sur un fondement autonome ou une seconde discussion prétendument toujours obligatoire."
drafts[n]['removed_provisions'] = drafts[n]['removed_provisions'][:2]
drafts[n]['review_notes'] = "L4161-1, L2242-15 et L2242-16 ont été lus en entier, notes comprises. Le renvoi préexistant depuis la branche vers des matières d'entreprise est conservé : il couvre notamment les salaires, le temps de travail, l'épargne et les mises à disposition syndicales, non l'annualité de la négociation d'entreprise. La référence ancienne L3334-1 du compagnon L2242-15 et l'articulation exacte de ce renvoi appellent une coordination distincte, sans retrait des plans ou avantages d'épargne. L'usage des travaux de l'observatoire devient facultatif ; ses obligations conventionnelles ou légales autonomes ne sont pas abolies. Aucun nouveau rapport, registre ni collecte n'est imposé. La durée d'une mission ou d'une formation ne met pas fin à un nouvel emploi à durée indéterminée."

drafts['L2241-8']['review_notes'] += " Les mentions de CDD de L2241-9 servent à analyser les contrats antérieurs et ne constituent aucun droit d'en conclure ou renouveler de nouveaux. Les missions à durée limitée ne déterminent pas la durée de l'emploi."

# Source L2241-18 makes transmission an alternative avoiding a commission, not an autonomous universal duty.
n='L2241-18'
drafts[n]['reason'] = "Réforme de fond partielle : le défaut de dépôt d'accord ou de transmission d'un procès-verbal ne déclenche plus automatiquement une commission mixte. La transmission du procès-verbal pour éviter ce déclenchement disparaît avec ce mécanisme, sans nouvelle déclaration. Le dépôt de l'accord prévu aussi par L2231-6 demeure ; l'unicité de ce dépôt n'est pas comptée comme un gain nouveau. Les voies de commission pour déloyauté ou selon L2261-20 sont préservées. L'annualité est coordonnée avec L2241-8."
drafts[n]['removed_provisions'] = [
    "Le mécanisme de convocation obligatoire d'une commission mixte pour le seul défaut de dépôt d'accord ou de transmission du procès-verbal de désaccord est supprimé, sans atteinte au contrôle de loyauté.",
    "La transmission des dernières propositions par un procès-verbal à l'administration comme moyen d'éviter ce déclenchement automatique n'est plus requise sur ce seul fondement."
]

# Updating an existing annual plan was not forbidden by the source; do not count it as a second saving.
n='L2242-3'
drafts[n]['removed_provisions'] = [drafts[n]['removed_provisions'][0]]
drafts[n]['reason'] = "Réforme de fond : suppression du dépôt administratif obligatoire du plan annuel d'égalité et de ses mises à jour, sans dépôt ou déclaration équivalente. L'évaluation annuelle, les objectifs, les actions qualitatives et quantitatives, leur coût et la programmation salariale restent dus. Le dépôt volontaire reste possible pour conserver le rescrit favorable. Les dépôts des décisions correctrices ont un fondement distinct et sont maintenus. L'actualisation d'un document existant est explicitée sans être comptée comme une seconde obligation supprimée, la source ne l'interdisant pas."
ps=paragraphs(n)
ps[2] += " Une pénalité ne peut être prononcée ou continuer de courir du seul fait de l'absence du dépôt ainsi supprimé. La communication du plan pour les besoins d'un contrôle reste due dans les conditions de droit commun ; elle ne constitue pas un dépôt périodique."
set_paragraphs(n,ps)
drafts[n]['review_notes'] += " L8113-4 et L8113-5 ont été lus : la présentation des documents obligatoires et la communication des éléments utiles au contrôle de l'égalité relèvent déjà des pouvoirs de contrôle ; elles ne remplacent pas le dépôt général supprimé. R2242-7, lu en entier, peut maintenir la pénalité jusqu'à réception du plan après mise en demeure : coordonner cette réception de contrôle sans reconstituer le dépôt général supprimé. R2242-8 à R2242-11, lus, conservent notification, recouvrement et demande facultative d'appréciation ; aucun second avantage n'est supprimé. Les exigences européennes de transparence salariale et d'égalité de rémunération restent à leur champ propre et leur articulation documentaire doit être contrôlée, sans conformité présumée."

# Additional reference checks that were not identified in the former draft.
drafts['L2241-7']['review_notes'] += " R2261-15 I 2°, lu, apprécie l'activité de branche sur trois ans : sa fenêtre doit être coordonnée pour ne pas traiter le simple respect d'une nouvelle périodicité légale comme un défaut de négociation. Ses autres critères autonomes ne sont pas supprimés ; cette coordination hors lot n'est pas déclarée rédigée."
drafts['L2241-10']['review_notes'] += " La réduction profite à l'initiative syndicale ; elle peut avancer l'obligation patronale d'ouverture et ne constitue pas une économie employeur chiffrée."
drafts['L2241-17']['review_notes'] = "L2241-8 conserve une obligation au moins quadriennale, sous réserve des accords plus fréquents et de L2241-10 ; L2241-15 conserve cinq ans. R2271-1 a été lu intégralement : le bilan annuel national d'égalité reste autonome et ne rétablit pas une négociation annuelle de branche. Aucun rapport annuel CPPNI supprimé dans L2232 n'est réintroduit. L'égalité de rémunération et les mesures déjà programmées restent immédiatement opposables. Le retrait du mot annuelle coordonne la mesure de L2241-8 ; ce n'est pas une seconde réduction."

# Specific benefit analyses, including articles not machine-flagged.
benefits = {
'L2241-1': "Les facultés d'épargne sans accord existant, mesures pour proches aidants, rattrapages salariaux, handicap, formation et aménagements pour salariés expérimentés demeurent intégralement. Tous les futurs salariés et opérations éligibles restent couverts ; aucun avantage n'est limité aux situations anciennes.",
'L2241-2': "Les minima conventionnels plus favorables, volumes contractuels garantis, rémunérations des heures complémentaires et délais de prévenance ne sont pas supprimés. Le minimum parental spécial de seize heures et les priorités d'accès à l'emploi restent sur leurs fondements propres, pour les futurs salariés aussi.",
'L2241-2-1': "Le plan type de branche demeure facultatif pour les entreprises de moins de trois cents salariés après l'échec de la négociation. Le document unilatéral et la consultation du CSE et des salariés gardent leur fonction ; les futures entreprises éligibles peuvent toujours utiliser la même voie.",
'L2241-3': "L'information des syndicats, la réponse motivée et l'intervention de la commission protègent la négociation éclairée et les recours. Ces garanties sont intégralement maintenues pour les négociations futures ; le texte ne contient pas d'exonération fiscale ou de dispense administrative distincte à retirer.",
'L2241-4': "Toute organisation conserve la possibilité de demander une négociation d'organisation favorable à l'adaptation de la branche ou du secteur. Cette faculté reste ouverte aux accords futurs et ne devient pas une autorisation préalable ou une condition supplémentaire de validité.",
'L2241-5': "L'aménagement conventionnel des périodicités subsiste, ainsi que l'information et le suivi des engagements. Les accords antérieurs conservent leur durée et leurs droits ; les futurs accords peuvent stipuler une durée indéterminée. Aucun minimum salarial, avantage d'épargne ou aménagement personnel n'est supprimé.",
'L2241-6': "La faculté d'aménager la renégociation dans l'accord thématique sans accord d'organisation séparé est préservée pour les accords futurs aussi. Les droits conventionnels plus fréquents restent applicables ; les maxima de quatre et cinq ans ne deviennent pas des délais minimaux.",
'L2241-7': "Les accords en vigueur et leurs calendriers plus fréquents, les créances et les recours déjà nés restent protégés. Les avantages d'emploi, d'insertion, de formation et d'épargne conservent leur accès pour les situations futures éligibles ; seul le calendrier légal supplétif bénéficie de la transition.",
'L2241-8': "Les salaires dus, le SMIC, les minima conventionnels et l'égalité de rémunération demeurent. Les accords imposant un rythme plus fréquent et le déclenchement lorsque le minimum professionnel passe sous le SMIC sont conservés ; l'espacement ne suspend aucun rappel salarial ou avantage acquis.",
'L2241-10': "Le déclenchement protecteur lorsque le minimum professionnel est inférieur au SMIC est maintenu et devient accessible sans l'attente préalable de quarante-cinq jours. Les minima et créances salariales restent exigibles et les demandes déjà faites ne perdent pas leur date ; aucune exonération n'est en cause.",
'L2241-11': "Toutes les mesures de rattrapage, l'accès à l'emploi, la formation, la promotion et les protections des salariés à temps partiel restent des thèmes obligatoires. Les mesures convenues gardent leurs échéances et leurs bénéficiaires futurs ; la nouvelle périodicité ne réduit aucun droit à salaire égal.",
'L2241-12': "Les mesures de formation, de transition professionnelle, de prévention et les dispositifs d'intéressement, participation ou épargne visés par L2242-15 demeurent avec leurs dispenses et conditions propres. Les mises à disposition syndicales de L2242-16 restent couvertes ; aucune durée de mission ne devient durée d'emploi.",
'L2241-13': "Insertion, accès à la formation et à la promotion, aménagements et maintien dans l'emploi des travailleurs handicapés demeurent. Ni leurs aides et exonérations ni les garanties d'emploi distinctes ne sont supprimées pour les futures situations éligibles ; le rapport sectoriel réglementaire reste requis.",
'L2241-14': "Abondements supplémentaires du CPF, égal accès à la formation, VAE, certifications, soutien au tutorat et prise en charge des dépenses de jury par les opérateurs de compétences sont conservés. Les futurs salariés éligibles restent bénéficiaires ; le seuil strict de plus de cinquante-cinq ans n'est pas modifié.",
'L2241-14-1': "Le maintien dans l'emploi, la retraite progressive, le temps partiel et la transmission des savoirs par mentorat, tutorat ou mécénat de compétences restent négociés. Ces possibilités favorables restent ouvertes aux situations futures éligibles ; le plan type de L2241-2-1 demeure disponible.",
'L2241-14-2': "Les six thèmes facultatifs de formation, accompagnement, santé, prévention et organisation sont maintenus intégralement et pour les futurs salariés concernés. Aucune faculté d'aménagement ou soutien au développement des compétences n'est fermée ; la liste n'est pas transformée en obligations supplémentaires.",
'L2241-15': "La priorité de réduction des écarts moyens, la correction des critères discriminatoires et la reconnaissance de toutes les compétences sont intégralement conservées. Les salariés futurs et présents restent protégés ; aucune classification ou rémunération conventionnelle plus favorable n'est abaissée.",
'L2241-16': "La dispense de négocier lorsqu'un accord existe déjà et l'accès aux deux catégories exactes de plans d'épargne demeurent. Les futurs plans éligibles conservent leurs avantages selon leur régime propre ; aucun avantage n'est réservé aux seuls plans antérieurs ni absorbé par la capitalisation projetée.",
'L2241-17': "La définition et la programmation de mesures de suppression des écarts de rémunération subsistent dans les négociations salariales et de classifications. Les engagements de rattrapage existants et le droit à l'égalité pour les salariés futurs restent opposables ; seule la qualification annuelle est coordonnée.",
'L2241-18': "Le dépôt des accords et les protections de négociation loyale demeurent ; la commission peut être réunie selon L2241-3 et L2261-20, y compris à la demande obligatoire de deux organisations représentatives. Les accords de rattrapage gardent tous leurs effets pour leurs futurs bénéficiaires.",
'L2242-1': "Salaires effectifs, partage de la valeur ajoutée, temps de travail, rattrapage des écarts et qualité de vie et des conditions de travail restent intégralement négociés. Les futurs salariés éligibles et les avantages conventionnels existants demeurent couverts ; aucune aide ou exemption n'est retirée.",
'L2242-2': "Les accompagnements, formations, abondements CPF et mobilités issus de la gestion des emplois restent accessibles suivant leurs règles propres. La possibilité d'organisation conventionnelle reste ouverte ; le maintien n'efface ni les garanties des groupes communautaires ni celles des futurs salariés éligibles.",
'L2242-2-1': "Les possibilités d'aménagement, de maintien dans l'emploi et de formation des salariés expérimentés et l'examen du fonds de prévention de l'usure professionnelle prévu par L2242-22 demeurent. Elles restent ouvertes aux futurs salariés éligibles ; aucun avantage de retraite ou de temps partiel n'est fermé.",
'L2242-3': "Le rescrit de conformité de L2242-9, son dépôt volontaire et son effet protecteur jusqu'au terme de la première année suivant ce dépôt restent ouverts aux futurs employeurs éligibles. Les plans et mesures de rattrapage, leurs objectifs et les garanties du CSE demeurent ; les décisions correctrices distinctes restent déposées."
}

# Effects use exact passages from each complete assigned source and its final proposal.
source_by_number = {x['number']:x for x in sources}
def effect(n,kind,mid,description,before,after,unit,population,conditions,replacement,sq,pq):
    assert len(sq)>=12 and sq in text(source_by_number[n]['source_xml']), (n,'source_quote',sq)
    assert len(pq)>=12 and pq in text(drafts[n]['proposed_xml']), (n,'proposed_quote',pq)
    return dict(kind=kind,measure_id=mid,description=description,before=before,after=after,unit=unit,affected_population=population,conditions_and_transition=conditions,replacement_or_new_burdens=replacement,source_quote=sq,proposed_quote=pq)

impacts={}
def impact(n,classification,assessment,limits,new,effects):
    assert all(len(x)>=40 for x in [assessment,limits,new])
    impacts[n]=dict(version=1,classification=classification,assessment=assessment,scope_limitations=limits,new_burdens_review=new,effects=effects)

for n,(reason,notes) in retained.items():
    impact(n,'retained_necessary',reason,
        "Aucune réduction normative n'est démontrée dans cet article conservé. Les mesures des articles voisins ne lui sont pas attribuées une seconde fois ; le solde de coût ou de complexité de l'ensemble des codes n'est pas établi. "+notes,
        "Aucune charge nouvelle n'est identifiée : texte, champs, conditions, informations et délais sont reproduits depuis la source sans modification, sans ajout de registre, dépôt ou attestation.",[])

n='L2241-2'
impact(n,'coordination_only',
    "L'obligation thématique de négocier un minimum hebdomadaire ou mensuel est retirée et remplacée par l'examen du volume contractuel garanti. C'est la coordination de la suppression du plancher général de temps partiel, non une seconde abolition de vingt-quatre heures : cet article source n'en fixait pas le chiffre. Les minima conventionnels favorables restent ouverts.",
    "Le seuil d'un tiers et la négociation de branche subsistent. Le plancher de vingt-quatre heures relève des L3123-7, L3123-19 et L3123-27 hors lot ; aucune baisse de cotisation ou économie de salaire n'est démontrée ici. Le renvoi parental erroné de la coordination est signalé.",
    "Aucun dépôt, donnée ou justificatif nouveau n'est ajouté. Le volume contractuel garanti remplace le thème du minimum légal dans une négociation déjà obligatoire ; la garantie contractuelle et les minima conventionnels favorables ne sont pas une déclaration de remplacement.",[
    effect(n,'coordination','temps-partiel-suppression-plancher-general',
        "Coordonne le thème de négociation au volume garanti sans rétablir le plancher général.",
        "À partir d'un tiers de salariés à temps partiel dans la branche, négociation notamment de la durée minimale hebdomadaire ou mensuelle.",
        "Même seuil et même négociation ; volume contractuel garanti examiné et minimum conventionnel favorable toujours possible, sans plancher légal général de vingt-quatre heures.",
        'legal_duty','Organisations et salariés des branches atteignant le seuil d’un tiers de temps partiel.',
        "Négociations ouvertes après l'entrée en vigueur ; volumes et droits conventionnels antérieurs maintenus, avantages futurs ouverts.",
        "Aucun dépôt ou justificatif substitutif ; le volume garanti constitue le thème coordonné, non une seconde négociation.",
        "Cette négociation porte notamment sur la durée minimale d'activité hebdomadaire ou mensuelle, le nombre et la durée des périodes d'interruption d'activité, le délai de prévenance préalable à la modification des horaires et la rémunération des heures complémentaires.",
        "La négociation peut fixer une durée minimale conventionnelle hebdomadaire ou mensuelle plus favorable aux salariés.")])

n='L2241-5'
impact(n,'material_reduction',
    "L'accord d'organisation n'est plus plafonné à cinq ans et n'a plus à prédéterminer les lieux et toutes les dates. Ces deux contraintes figurent expressément dans la source ; les plafonds de renégociation, le contenu thématique, l'information et le suivi restent entiers.",
    "L'allègement vise l'accord d'organisation de branche, pas les accords d'entreprise ni leurs règles distinctes. Un accord ancien n'est pas prorogé de plein droit et le silence sur la durée reste soumis aux cinq ans du droit commun. Économie de coût non chiffrée.",
    "Aucune charge nouvelle n'est identifiée : l'alternative de modalités de fixation du calendrier est facultative ; la durée indéterminée ne crée ni registre, ni dépôt supplémentaire, ni renouvellement périodique d'autorisation.",[
    effect(n,'obligation_removed','negociation-branche-accord-organisation-duree',
        "Supprime le plafond spécial de cinq ans de l'accord d'organisation.",
        "Durée maximale de cinq ans imposée à tout accord d'organisation de branche.",
        "Durée déterminée ou indéterminée possible ; en l'absence de stipulation, cinq ans demeurent selon L2222-4 ; négociations toujours dues au plus tard tous les quatre ou cinq ans.",
        'legal_duty','Parties aux futurs accords d’organisation de branche.',
        "Accords conclus après l'entrée en vigueur ; durée et engagements des accords antérieurs conservés sans prolongation automatique.",
        "Aucune formalité de renouvellement ou autorisation de remplacement ; règles de conclusion et dépôt de droit commun conservées.",
        "La durée de l'accord ne peut excéder cinq ans.",
        "L'accord peut être conclu pour une durée déterminée ou indéterminée dans les conditions de l'article L. 2222-4."),
    effect(n,'obligation_removed','negociation-branche-organisation-reunions-souple',
        "Retire la prédétermination obligatoire des lieux et du calendrier exhaustif dans l'accord.",
        "L'accord doit préciser le calendrier et les lieux des réunions au 3°.",
        "L'accord peut prévoir les modalités de fixation du calendrier ; les lieux n'ont pas à y être fixés. Thèmes, information et suivi demeurent.",
        'legal_duty','Parties aux futurs accords d’organisation de branche.',
        "Nouveaux accords ; les engagements des accords antérieurs subsistent et restent modifiables selon le droit commun.",
        "Aucun accord de lieux distinct ou déclaration de substitution n'est imposé.",
        "3° Le calendrier et les lieux des réunions ;",
        "3° Le calendrier des réunions ou les modalités permettant de le fixer au cours de l'exécution de l'accord ; les lieux des réunions n'ont pas à être fixés dans cet accord ;")])

period_id='negociation-branche-periodicite-quatre-ans'
transition="Échéances légales non échues après l'entrée en vigueur, calcul depuis l'ouverture précédente sans remise à zéro ; négociations en cours poursuivies ; engagements conventionnels plus fréquents et droits antérieurs conservés selon L2241-7."
pop='Organisations liées par une convention de branche ou, à défaut, par des accords professionnels.'
replacement='Aucune déclaration, autorisation ou réunion de substitution ; la négociation et ses informations utiles restent obligatoires.'

n='L2241-7'
impact(n,'coordination_only',
    "La transition rend applicables les nouvelles échéances supplétives sans remettre à zéro les périodes déjà courues ni éteindre les engagements conventionnels. Le renvoi aux sous-sections 2 à 6 et le déclenchement supplétif sont maintenus ; aucune réduction supplémentaire n'est comptée.",
    "Ne modifie ni les échéances déjà dues ni le régime supplétif d'entreprise. La fenêtre d'activité de branche de trois ans de R2261-15 nécessite une coordination hors lot ; ses autres critères ne sont pas réputés supprimés. Aucun gain financier national établi.",
    "Aucune charge nouvelle n'est identifiée : les dates d'ouverture servent à calculer des échéances existantes sans registre spécifique, nouvelle déclaration ou nouveau justificatif ; les négociations commencées ne sont pas réouvertes.",[
    effect(n,'coordination',period_id,'Organise la transition commune des périodicités supplétives de branche.',
        "À défaut d'accord d'organisation ou en cas de non-respect, application des sous-sections 2 à 6 et de leurs échéances annuelles ou triennales concernées.",
        "Même mécanisme supplétif ; les nouvelles périodicités quadriennales ne s'appliquent qu'aux échéances non échues, sans redémarrage du délai ni effacement de droits conventionnels.",
        'legal_duty',pop,transition,replacement,
        "les organisations liées par une convention de branche ou, à défaut, par des accords professionnels engagent les négociations mentionnées aux articles L. 2241-1 et L. 2241-2 dans les conditions précisées par les sous-sections 2 à 6 de la présente section.",
        "Les périodicités supplétives résultant de la loi s'appliquent, dès son entrée en vigueur, aux échéances légales qui ne sont pas encore échues.")])

cycles={
'L2241-8':('salaires', 'au moins une fois par an',"Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent, au moins une fois par an, pour négocier sur les salaires.","Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les salaires, sans préjudice d'une périodicité plus fréquente prévue par un accord en vigueur et du déclenchement prévu à l'article L. 2241-10."),
'L2241-11':('égalité professionnelle et rattrapage', 'tous les trois ans',"Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent pour négocier tous les trois ans sur les mesures tendant à assurer l'égalité professionnelle entre les femmes et les hommes et sur les mesures de rattrapage tendant à remédier aux inégalités constatées.","Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les mesures visant à assurer l'égalité professionnelle entre les femmes et les hommes et sur les mesures de rattrapage des inégalités constatées."),
'L2241-12':('conditions de travail et gestion des emplois ; matières des L2242-15 et L2242-16', 'au moins tous les trois ans pour la première négociation et tous les trois ans pour les matières du dernier alinéa',"Par ailleurs, les organisations mentionnées au premier alinéa se réunissent tous les trois ans pour négocier sur les matières définies aux articles L. 2242-15 et L. 2242-16.","Les mêmes organisations se réunissent également au moins une fois tous les quatre ans pour négocier sur les matières définies aux articles L. 2242-15 et L. 2242-16."),
'L2241-13':('insertion et maintien dans l’emploi des travailleurs handicapés', 'tous les trois ans',"Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent pour négocier, tous les trois ans, sur les mesures tendant à l'insertion professionnelle et au maintien dans l'emploi des travailleurs handicapés.","Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour négocier sur les mesures favorisant l'insertion professionnelle et le maintien dans l'emploi des travailleurs handicapés."),
'L2241-14':('priorités, objectifs et moyens de formation professionnelle', 'au moins tous les trois ans',"Les organisations liées par une convention de branche ou, à défaut, par un accord professionnel se réunissent au moins tous les trois ans pour négocier sur les priorités, les objectifs et les moyens de la formation professionnelle des salariés.","Les organisations liées par une convention de branche ou, à défaut, par un accord professionnel se réunissent au moins une fois tous les quatre ans pour négocier sur les priorités, les objectifs et les moyens de la formation professionnelle des salariés."),
'L2241-14-1':('emploi et travail des salariés expérimentés', 'une fois tous les trois ans',"Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent, une fois tous les trois ans, pour engager, après établissement d'un diagnostic, une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge.","Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent au moins une fois tous les quatre ans pour engager une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge.")}
for n,(topic,old,sq,pq) in cycles.items():
    assessment="La source officielle impose une négociation sur "+topic+" "+old+" ; la proposition porte le rythme supplétif à au moins une fois tous les quatre ans. Les échéances légales intermédiaires disparaissent effectivement, mais les thèmes, droits de fond et engagements plus fréquents demeurent."
    if n=='L2241-8': assessment+=" L'examen annuel lié des données de L2241-9 est expressément coordonné pour éviter de rétablir la même annualité."
    if n=='L2241-12': assessment+=" L'utilisation obligatoire des travaux d'un observatoire déterminé est également retirée."
    if n=='L2241-14-1': assessment+=" Le diagnostic préalable cesse en outre de conditionner l'ouverture ; son analyse reste nécessaire au cours de la négociation."
    limits="L'espacement diminue une fréquence de négociation, pas un taux fiscal, une cotisation ou un salaire. Il peut réduire la fréquence du dialogue en l'absence d'accord plus favorable ; aucun gain net de coût n'est chiffré. Les règles d'entreprise, protections et dispositifs sectoriels autonomes restent distincts."
    if n in ['L2241-11','L2241-13']: limits+=" Les rapports et informations réglementaires sont conservés ; aucune suppression de leur support n'est comptée."
    if n=='L2241-8': limits+=" Le délai préparatoire de quinze jours de D2241-1 et le rapport restent dus ; le SMIC et le déclenchement de L2241-10 demeurent."
    if n=='L2241-14-1': limits+=" L2242-22 et D2242-17 conservent le diagnostic d'entreprise sur leurs fondements propres."
    impact(n,'material_reduction',assessment,limits,
        "Aucune charge nouvelle n'est identifiée : aucun registre, donnée, dépôt ou condition d'aide supplémentaire n'est créé. Les informations et thèmes conservés existaient déjà ; l'espacement n'impose pas de négociation de remplacement. Le solde national de coûts n'est pas établi.",[
        effect(n,'obligation_removed',period_id,'Supprime les échéances supplétives intermédiaires de négociation sur '+topic+'.',
            "Négociation de branche sur "+topic+" "+old+", dans le régime supplétif ; obligations conventionnelles distinctes.",
            "Négociation de branche sur les mêmes thèmes au moins tous les quatre ans ; les accords plus fréquents restent applicables et les droits de fond sont maintenus.",
            'legal_duty',pop,transition,replacement,sq,pq)])

# Linked annual data review is part of the same salary-calendar measure, not an extra abolished negotiation.
impacts['L2241-8']['effects'][0]['description'] += " L'examen des données de L2241-9 suit ce calendrier, sans annualité légale distincte."
impacts['L2241-8']['effects'][0]['after'] += " Toutes les données de L2241-9 sont examinées à l'occasion de cette négociation, sans examen annuel distinct sur ce seul fondement."

n='L2241-12'
impacts[n]['effects'].append(effect(n,'obligation_removed','negociation-branche-source-observatoire-facultative',
    "Retire le recours obligatoire aux travaux d'un observatoire déterminé pour préparer la gestion des emplois.",
    "La négociation s'appuie obligatoirement sur les travaux de l'observatoire prospectif de la commission paritaire nationale de l'emploi.",
    "Travaux utilisables lorsqu'ils sont disponibles, sans condition de recours obligatoire à cet organisme ; attention à la mixité et aux transitions écologique et énergétique maintenue.",
    'legal_duty',pop,
    "Applicable dès l'entrée en vigueur aux négociations en cours ; engagements conventionnels et fondements autonomes des observatoires conservés.",
    "Aucun organisme, rapport ni registre substitutif ; l'analyse utile reste dans la négociation existante.",
    "La négociation sur la gestion prévisionnelle des emplois et des compétences peut se décliner à l'échelle du territoire et s'appuie sur les travaux de l'observatoire prospectif des métiers et des qualifications mis en place par la commission paritaire nationale de l'emploi au niveau de chaque branche, tout en veillant à l'objectif de mixité des métiers.",
    "Le recours à cet observatoire n'est pas une condition de la négociation ; le présent article n'impose pas la création ou le maintien d'un organisme distinct."))

n='L2241-14-1'
impacts[n]['effects'].append(effect(n,'obligation_merged','negociation-branche-diagnostic-seniors-sans-prealable',
    "Supprime le diagnostic de branche comme préalable d'ouverture ; conserve l'analyse et les indicateurs dans la négociation.",
    "La négociation ne s'engage qu'après établissement d'un diagnostic ; D2241-5 en précise les indicateurs chiffrés par domaine.",
    "L'ouverture n'est plus subordonnée à un diagnostic préalable ; analyse menée pendant la négociation, indicateurs conservés, sans diagnostic autonome imposé.",
    'legal_duty',pop,
    "Application immédiate aux négociations nouvelles et en cours ; aucun travail déjà fait n'est à recommencer ; diagnostic d'entreprise distinct maintenu.",
    "Pas de nouveau rapport substitutif : l'analyse et les indicateurs étaient déjà prévus par le régime source et D2241-5.",
    "Les organisations liées par une convention de branche ou, à défaut, par des accords professionnels se réunissent, une fois tous les trois ans, pour engager, après établissement d'un diagnostic, une négociation sur l'emploi et le travail des salariés expérimentés, en considération de leur âge.",
    "L'ouverture de la négociation n'est pas subordonnée à l'établissement préalable d'un diagnostic ; l'analyse de la situation de ces salariés est conduite au cours de la négociation."))

n='L2241-10'
impact(n,'material_reduction',
    "Le délai préalable de quarante-cinq jours réservé à l'initiative patronale est retiré : le syndicat représentatif peut déclencher aussitôt l'ouverture sous quinze jours lorsque le minimum de branche est inférieur au SMIC. C'est une réduction d'attente syndicale, pas une baisse de coût de rupture ou de prélèvement.",
    "L'obligation patronale peut devenir exigible plus tôt ; aucun gain employeur ni solde de coût net n'est établi. Les quinze jours après demande demeurent, ainsi que tous les minima salariaux. Les jours ne sont pas confondus avec le préavis individuel du contrat unique.",
    "Aucun registre, information ou dépôt nouveau n'est identifié. La même négociation et la même demande syndicale sont conservées ; la suppression de l'attente peut avancer l'effort patronal d'ouverture, effet de calendrier explicitement recensé, sans délai de remplacement.",[
    effect(n,'deadline_reduced','negociation-salaires-sous-smic-sans-attente',
        "Supprime l'attente préalable avant la demande syndicale obligatoire sous quinze jours.",
        "En l'absence d'initiative patronale dans les quarante-cinq jours, ouverture dans les quinze jours de la demande syndicale ; le préalable peut porter l'enchaînement à soixante jours.",
        "Aucun délai préalable de quarante-cinq jours ; demande possible dès constat du minimum inférieur au SMIC, ouverture dans les mêmes quinze jours après demande. Aucun nouveau délai minimum.",
        'calendar_days','Organisations représentatives et employeurs des branches dont le minimum professionnel des salariés sans qualification est inférieur au SMIC.',
        "Application dès l'entrée en vigueur, situations déjà constatées incluses ; demandes antérieures conservent leur date et aucun délai commencé n'est prolongé.",
        "Aucune démarche nouvelle ; accélération possible de la même obligation patronale, sans chiffrage de coût net.",
        "A défaut d'initiative de la partie patronale dans les quarante-cinq jours, la négociation s'engage dans les quinze jours suivant la demande d'une organisation syndicale de salariés représentative au sens de l'article L. 2231-1.",
        "La négociation s'engage dans les quinze jours suivant cette demande, sans délai préalable de quarante-cinq jours réservé à l'initiative patronale.")])

n='L2241-17'
impact(n,'coordination_only',
    "La qualification annuelle est retirée du renvoi salarial pour ne pas rétablir l'annualité supprimée à L2241-8. Définition et programmation des mesures contre les écarts restent intégralement incluses dans les négociations salariales et quinquennales de classifications ; aucune seconde réduction n'est comptée.",
    "Seul le calendrier salarial de branche est coordonné. Le bilan annuel national de R2271-1, la négociation d'entreprise et les droits immédiats à salaire égal restent distincts. Aucun coût national ni baisse de prélèvement n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun nouveau plan, donnée ou dépôt ; les mesures d'égalité demeurent au sein des mêmes négociations, avec les périodicités de leurs articles supports.",[
    effect(n,'coordination',period_id,'Coordonne la programmation de l’égalité avec le nouveau calendrier salarial de branche.',
        "Les négociations visées sont qualifiées d'annuelle et de quinquennale.",
        "Renvoi aux calendriers respectifs des L2241-8 et L2241-15, sans annualité supplémentaire ; objectif de suppression des écarts identique.",
        'legal_duty',pop,transition,replacement,
        "Les négociations annuelle et quinquennale prévues aux articles L. 2241-8 et L. 2241-15 visent également à définir et à programmer les mesures permettant de supprimer les écarts de rémunération entre les femmes et les hommes.",
        "Elles suivent les périodicités applicables à chacun de ces articles, sans annualité supplémentaire sur le fondement du présent article.")])

n='L2241-18'
impact(n,'material_reduction',
    "La convocation automatique d'une commission mixte fondée sur la seule absence de dépôt d'accord ou de transmission du procès-verbal est supprimée. La transmission des dernières propositions pour éviter cette convocation disparaît avec ce mécanisme. Le dépôt légal de l'accord et les autres garanties de loyauté restent dus ; il n'y avait pas deux dépôts à supprimer.",
    "La source prévoit une alternative documentaire évitant la commission, pas une obligation universelle autonome de transmettre tout procès-verbal. Le procès-verbal d'entreprise de L2242-5 et les dépôts autonomes ne sont pas supprimés ; aucun coût net administratif n'est chiffré.",
    "Aucune charge nouvelle n'est identifiée : ni déclaration de remplacement ni nouvelle preuve de désaccord. Les saisines de commission demeurent sur leurs fondements existants, sans nouvelles conditions d'accès aux recours.",[
    effect(n,'obligation_removed','negociation-branche-fin-commission-formalite',
        "Supprime la commission obligatoire déclenchée par une seule absence de document, et l'envoi alternatif destiné à l'éviter.",
        "À défaut de dépôt d'accord ou de transmission du procès-verbal contenant les dernières propositions, commission mixte obligatoirement réunie à l'initiative du ministre.",
        "Ces seules absences ne déclenchent plus la commission ; transmission du procès-verbal non requise sur ce fondement. Dépôt légal des accords, saisine pour déloyauté et L2261-20 conservés.",
        'legal_duty','Organisations de branche et administration chargée de convoquer la commission mixte.',
        "Application aux négociations et procès-verbaux en cours ; aucun envoi tardif ni redépôt. Réunions régulièrement convoquées pouvant continuer ; recours pour obligations maintenues conservés.",
        "Aucun dépôt, rapport ou attestation de remplacement ; les garanties de L2241-3 et L2261-20 existaient déjà.",
        "En l'absence de dépôt d'un accord ou de transmission d'un procès-verbal de désaccord auprès de cette autorité, contenant les propositions des parties en leur dernier état, la commission mixte mentionnée à l'article L. 2261-20 est réunie à l'initiative du ministre chargé du travail afin que s'engagent ou se poursuivent les négociations prévues à l'article L. 2241-17.",
        "Ni cette absence de dépôt ni l'absence d'une telle transmission ne déclenche, à elle seule, la réunion d'une commission mixte.")])

n='L2242-3'
impact(n,'material_reduction',
    "La source impose le dépôt du plan annuel d'égalité auprès de l'administration ; ce dépôt devient facultatif, sans déclaration de remplacement. Les obligations annuelles de fond, publications, contrôles et décisions correctrices distinctes demeurent. Le dépôt volontaire conserve le rescrit favorable ; l'actualisation d'un fichier existant n'est pas comptée comme une seconde réduction.",
    "Les dépôts de décisions correctrices des L1142-9 et L1142-13, le contrôle et le procès-verbal d'entreprise restent à leur régime. R2242-2-1 et R2242-7 doivent être coordonnés. Le dépôt volontaire reste utile au rescrit : aucune exonération de pénalité sur un manquement de fond n'est créée. Coût net inconnu.",
    "Aucune charge nouvelle n'est identifiée : pas de registre, attestation ou déclaration substitutifs. Mise à disposition du CSE et présentation lors d'un contrôle sont préexistantes ; le dépôt volontaire sert à conserver un droit existant et ne conditionne pas la dispense générale.",[
    effect(n,'obligation_removed','egalite-professionnelle-plan-depot-facultatif',
        "Supprime le dépôt administratif obligatoire du seul plan annuel, sans fermer le rescrit sur dépôt volontaire.",
        "Plan annuel d'égalité obligatoirement déposé auprès de l'autorité administrative après échec de l'accord.",
        "Plan annuel et mises à jour sans dépôt obligatoire ; dépôt volontaire possible pour le rescrit de L2242-9. Dépôts autonomes des décisions correctrices et obligations annuelles de fond maintenus.",
        'legal_duty','Employeurs tenus d’établir un plan annuel faute d’accord sur l’égalité professionnelle.',
        "Application immédiate aux plans et mises à jour en cours ; pas de dépôt tardif ou renouvelé du seul plan ; droits et réponses favorables antérieurs conservés, réserve des sanctions plus douces.",
        "Aucune déclaration équivalente ; documents tenus à disposition du CSE et du contrôle selon les régimes existants, dépôt volontaire sans agrément préalable nouveau.",
        "Ce plan d'action est déposé auprès de l'autorité administrative.",
        "Le plan et ses mises à jour ne sont pas soumis à un dépôt obligatoire auprès de l'autorité administrative.")])

assert len(sources)==24 and set(drafts)==set(source_by_number)==set(impacts)==set(benefits)
answer=[]
for s in sources:
    n=s['number'];row={k:s[k] for k in ['code_id','source_id','source_sha256','number']}
    row.update(drafts[n]);row.setdefault('status','rewrite_draft')
    row['benefit_review']=benefits[n]
    row['substantive_impact']=impacts[n]
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
print('answer.json :',len(answer),'articles;',sum(x['status']=='rewrite_draft' for x in answer),'propositions modifiées;',sum(x['status']=='retained_unchanged' for x in answer),'maintiens intégraux motivés.')
