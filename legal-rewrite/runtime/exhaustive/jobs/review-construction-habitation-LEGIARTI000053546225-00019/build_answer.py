import html
import json
import re
from pathlib import Path

source = json.loads(Path('source.json').read_text())[0]
references = json.loads(Path('reference-targets.json').read_text())
proposed = Path('proposed.xml').read_text().strip()
old = re.findall(r'<p>(.*?)</p>', source['source_xml'], re.S)
new = re.findall(r'<p>(.*?)</p>', proposed, re.S)


def plain(x):
    return html.unescape(re.sub(r'<[^>]+>', '', x))


effects = []


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           source_quote, proposed_quote, replacement_or_new_burdens=None):
    effects.append(dict(
        kind=kind, measure_id=measure_id, description=description,
        before=before, after=after, unit=unit,
        affected_population=affected_population,
        conditions_and_transition=conditions_and_transition,
        replacement_or_new_burdens=replacement_or_new_burdens or
        "Aucune déclaration, attestation, transmission ou autorisation de remplacement ; les conditions de fond et les contrôles légalement autonomes demeurent.",
        source_quote=plain(source_quote), proposed_quote=plain(proposed_quote)))


transition = (
    "À compter de l'entrée en vigueur de la loi portant la nouvelle rédaction, y compris pour les procédures en cours sans nouveau dépôt ; "
    "actes réguliers, engagements contractuels autonomes, droits antérieurs et recours préservés."
)

effect(
    'authorization_removed', 'sa-hlm-gestion-privee-sans-accord-maire',
    "Retrait de l'accord du maire au premier alinéa, notamment pour la gestion de logements privés vacants hors des interventions déjà dispensées par L411-2 proposé.",
    "Accord du maire imposé à la gestion visée au premier alinéa, en plus du mandat privé et des conditions de L442-11.",
    "Aucun accord municipal au titre de cette compétence ; mandat, décence et plafonds locatifs subsistent. Pour les activités déjà couvertes par la dispense de L411-2 proposé, il s'agit du même allègement, non d'une deuxième autorisation supprimée.",
    'legal_duty', "Sociétés anonymes HLM exerçant la faculté de gestion du premier alinéa et propriétaires concernés.",
    transition, old[0][old[0].index('Elles peuvent également gérer, en qualité'):],
    new[0][new[0].index('Elles peuvent également gérer, en qualité'):])

effect(
    'relief_extended', 'sa-hlm-gestion-vacance-sans-duree-minimale',
    "Ouverture de la faculté du premier alinéa aux logements privés vacants depuis un an ou moins, sans supprimer les garanties de leur mise en location.",
    "Cette branche de compétence exige un logement privé vacant depuis plus d'un an ; d'autres facultés de gestion existent déjà ailleurs dans l'article.",
    "Aucune durée minimale de vacance pour cette branche ; mêmes conditions de décence, de loyer et de ressources. Les autres voies de gestion restent ouvertes sans restriction supplémentaire.",
    'other', "SA HLM, propriétaires et occupants des logements privés nouvellement recevables au premier alinéa.",
    transition + " Il ne s'agit ni d'une réduction de 365 jours garantie à chaque opération, ni de la création d'un droit général de gestion auparavant inexistant.",
    "les logements appartenant à des personnes privées et vacants depuis plus d'un an.",
    "les logements appartenant à des personnes privées et vacants, sans durée minimale de vacance.",
    "Les garanties de L442-11 sont appliquées à la seule faculté élargie, sans dossier nouveau ; les autres facultés de gestion de l'article ne sont pas restreintes. Aucun bénéficiaire antérieurement éligible n'est soumis à une condition nouvelle.")

effect(
    'authorization_removed', 'sa-hlm-amenagement-sans-accord-local',
    "Suppression de l'accord local spécifique aux interventions foncières et opérations d'aménagement.",
    "Accord des collectivités ou communautés intéressées requis par le quatrième alinéa, même lorsque la SA HLM agit pour son propre compte.",
    "Pas d'accord administratif autonome sur cette compétence ; conventions de mission, consentement des propriétaires, commande publique et autorisations d'urbanisme conservent leur champ.",
    'legal_duty', "SA HLM réalisant une intervention foncière ou une opération d'aménagement, pour elles-mêmes ou pour un tiers.",
    transition,
    old[3].split(" Lorsqu'elles")[0], new[3].split(" Lorsqu'elles")[0])

effect(
    'relief_extended', 'hlm-ventes-personnes-morales-extension-territoriale',
    "Maintien de l'extension territoriale acquise au brouillon : les ventes complémentaires à des personnes morales ne sont plus limitées aux communes désignées par les anciens critères fiscaux et SRU.",
    "Ventes aux personnes morales limitées aux communes des zones d'urbanisation continue de plus de 50 000 habitants et à certaines communes de plus de 15 000 habitants en croissance ; plafonds de ressources et prix maxima.",
    "Même faculté dans toute la compétence géographique de la SA HLM ; maintien du caractère complémentaire, de l'offre insuffisante ou de la demande locale, des plafonds de ressources et des prix maxima. Aucun taux fiscal ni avantage Pinel nouveau.",
    'regime', "SA HLM, personnes morales acquéreuses et occupants répondant aux plafonds de ressources visés.",
    transition,
    old[5][old[5].index('Exclusivement'):], new[5][new[5].index("Sur l'ensemble"):])

effect(
    'obligation_removed', 'hlm-hebergement-sans-avis-local',
    "Suppression des quatre avis communaux ou intercommunaux pour l'hébergement, les victimes de violences, les établissements d'hébergement et les terrains familiaux locatifs.",
    "Aux alinéas 17 à 20, un avis local doit être recueilli même lorsque le besoin figure déjà au plan départemental ou au schéma.",
    "Aucun de ces quatre avis n'est requis ; identification du besoin, bénéficiaires, conventionnement, structures sécurisées et règles d'accueil demeurent.",
    'legal_duty', "SA HLM intervenant dans ces quatre activités subsidiaires et publics bénéficiaires.",
    transition, '\n'.join(old[16:20]), '\n'.join(new[16:20]))

effect(
    'authorization_removed', 'hlm-participation-amenagement-sans-accord-prefectoral',
    "Suppression de l'accord préfectoral spécial pour entrer dans une société d'aménagement ou de projet urbain partenarial.",
    "Demande au préfet du lieu de l'opération et accord, avec opposition possible pendant deux mois à compter de sa réception.",
    "Ni demande, ni accord, ni délai d'opposition pour la prise de participation ; les pouvoirs de contrôle et les règles de la société restent autonomes.",
    'legal_duty', "SA HLM souscrivant ou acquérant des parts ou actions des sociétés visées au vingt-septième alinéa.",
    transition, old[26], new[26])

effect(
    'authorization_removed', 'hlm-acquisition-sci-sans-autorisation-ministerielle',
    "Suppression de l'autorisation ministérielle pour la souscription ou l'acquisition de toutes les parts d'une SCI.",
    "Autorisation préalable du ministre chargé du logement ; autres conditions d'acquisition, dissolution et conventionnement.",
    "Aucune autorisation ministérielle ; date unique, dissolution dans l'année, objet et territoire, conventionnement dans l'année et nullité pour les violations des conditions restantes sont conservés.",
    'legal_duty', "SA HLM procédant à la souscription ou à l'acquisition de la totalité d'une SCI.",
    transition,
    "L'opération fait l'objet d'une autorisation préalable du ministre chargé du logement.",
    "L'opération n'est soumise à aucune autorisation préalable du ministre chargé du logement.")

effect(
    'authorization_removed', 'sa-hlm-prestations-sem-sans-agrement-specifique',
    "Retrait de l'agrément spécifique pour les prestations d'aménagement auprès des SEM.",
    "Un agrément à cet effet s'ajoute au statut de la SA HLM pour intervenir comme prestataire d'une SEM en aménagement.",
    "Prestation admise sans cet agrément spécifique, sous le statut et l'objet social ; l'agrément organique HLM et les règles d'attribution des marchés ne sont pas supprimés.",
    'legal_duty', "SA HLM prestataires des sociétés d'économie mixte pour les opérations d'aménagement.",
    transition, old[29], new[29])

effect(
    'coordination', 'hlm-coproprietes-sans-accord-prealable',
    "Mise en cohérence du trente et unième alinéa avec la suppression du double accord déjà portée par L411-2 proposé pour les copropriétés concernées.",
    "L422-2 officiel exige encore maire, préfet et circuit d'opposition de deux mois ; L411-2 proposé dispense déjà les mêmes activités de ces accords organiques.",
    "Retrait explicite du double accord, de la demande et de l'opposition, y compris au titre de L411-2 ; facultés de travaux, acquisition-revente et location provisoire maintenues.",
    'legal_duty', "SA HLM dans les copropriétés en difficulté, sous plan de sauvegarde, OPAH dédiée ou ORCOD visées.",
    transition + " Une seule mesure à rapprocher de L411-2 et de L422-3 ; aucune deuxième suppression générale comptée ici.",
    old[30], new[30])

effect(
    'authorization_removed', 'hlm-filiales-intermediaires-fin-controle-prealable',
    "Suppression d'un même dispositif de contrôle préalable des filiales intermédiaires : opposition ministérielle à la création et préfectorale à l'augmentation de capital, avec ses transmissions spécifiques et son application aux sociétés sous contrôle conjoint. La correction du renvoi définissant l'objet de ces dernières est incluse comme coordination de cette mesure, sans gain distinct.",
    "Transmission de la création au ministre et de l'augmentation de capital au préfet de région ; opposition possible dans chacun des délais de trois mois. Les sociétés sous contrôle conjoint suivent les mêmes règles ; leur renvoi aux alinéas 47 à 50 omet le 3° figurant à l'alinéa 51.",
    "Aucune transmission spécifique ni délai d'opposition pour ces créations, participations et augmentations de capital. Les 1° à 3°, conditions a et b, règles d'apports, origine des fonds, remboursement, prix des prestations et contrôle conjoint restent opposables ; le renvoi à l'objet des sociétés est expressément rectifié.",
    'legal_duty', "SA HLM créant ou capitalisant les filiales intermédiaires et participant, avec d'autres organismes HLM, aux sociétés intermédiaires sous contrôle conjoint.",
    transition + " Une seule mesure pour ses deux autorités et ses différentes formes sociétaires ; les durées réelles d'opération et le coût net ne sont pas chiffrés.",
    '\n'.join(old[53:62]), '\n'.join(new[53:62]))

effect(
    'coordination', 'sru-suppression-quotas-communaux',
    "Coordination unique des renvois à L302-5 : rattachement des définitions sociales au IV conservé et fixation du seul renvoi historique du b relatif à l'usufruit. Ces corrections ne sont pas de nouvelles suppressions de quotas dans L422-2.",
    "Renvois globaux à L302-5 pour la limite de 10 % et pour l'exclusion des logements sociaux transformés par les filiales ; expérimentation d'usufruit de cinq ans depuis la loi du 24 mars 2014 définie par l'ancien II et ses décrets.",
    "Renvois définitionnels au seul IV, avec même limite autonome de 10 %, exclusion des logements sociaux et plafonds. Le renvoi territorial expérimental conserve la rédaction applicable aux opérations régulièrement engagées pendant sa fenêtre historique, sans liste nouvelle ni quota futur.",
    'regime', "SA HLM, filiales intermédiaires et parc social servant de référence ; opérations régulièrement engagées pendant l'expérimentation d'usufruit temporaire de 2014.",
    "Coordination avec L302-5 proposé : catégories préservées pour les opérations futures éligibles, droits et contentieux anciens conservés. La fenêtre d'usufruit de cinq ans n'est pas prorogée et aucun nouveau prélèvement, inventaire ou quota n'est institué.",
    '\n'.join(old[38:52]), '\n'.join(new[38:52]))

effect(
    'coordination', 'hlm-conventionnement-logements-transmis-sci',
    "Correction du renvoi de conventionnement après transmission des logements d'une SCI intégralement acquise.",
    "Renvoi à l'ancien L351-2 pour conclure les conventions dans l'année de la transmission effective du patrimoine.",
    "Renvoi au régime locatif de L831-1, sans changement de la durée d'un an ni nouvelle demande d'aide ; conventions et droits anciens préservés.",
    'regime', "SA HLM, logements transmis par la SCI et occupants concernés.",
    "Recodification de 2019 documentée par la note de L631-12 et confrontation au texte de L831-1 ; cette correction ne supprime pas le conventionnement utile.",
    "Les logements transmis font l'objet de conventions conclues en application de l'article L. 351-2 du présent code dans un délai d'un an à compter de la transmission effective du patrimoine.",
    "Les logements transmis font l'objet de conventions conclues en application de l'article L. 831-1 du présent code dans un délai d'un an à compter de la transmission effective du patrimoine.")

effect(
    'coordination', 'hlm-affectation-resultats-sieg',
    "Remplacement des deux renvois au dernier alinéa de L411-2 par leur objet financier précis, car le projet de cette cible ajoute une transition finale.",
    "Les alinéas 12 et 65 renvoient au dernier alinéa de L411-2, qui porte dans la source sur le compte affecté aux activités SIEG.",
    "Les renvois visent expressément l'affectation des résultats SIEG ; pas de comptabilité ou de restriction financière nouvelle, pas de renvoi accidentel à la transition.",
    'legal_duty', "SA HLM menant les travaux de rénovation énergétique ou les activités accessoires visés.",
    "Coordination nécessaire de la proposition de L411-2 ; conditions financières maintenues, sans gain matériel distinct.",
    old[11], new[11])

assessments = {
    '199 novovicies': (
        "Le sixième alinéa de L422-2 vise uniquement les plafonds de ressources du décret prévu au premier alinéa du III, et non le régime fiscal entier de 199 novovicies. Le III officiel et le III proposé conservent ces plafonds appréciés à la conclusion du bail ; la suppression proposée du délai de première location n'est pas une suppression des plafonds. Les bornes d'investissement 2013-2024, le 5° ouvert jusqu'en 2027 et les durées de six ou neuf ans ne deviennent pas des conditions temporelles des ventes HLM par ce renvoi ciblé. La dispense de reprise du XI B, étendue dans la proposition aux ruptures patronales du contrat unique même avant un an et pendant l'essai, reste à son champ fiscal propre : aucun droit à réduction, seuil d'indemnité ou délai de notification n'est inventé ici."
    ),
    'L1234-1': (
        "Aucun renvoi direct de L422-2 à L1234-1. La source de cette cible module le préavis selon six mois et deux ans d'ancienneté ; sa proposition prévoit quinze jours calendaires pour les contrats nouveaux, avec conservation des anciennes règles pour les contrats antérieurs et des procédures collectives et protections distinctes. Ces quinze jours ne réduisent ni les délais de dissolution et conventionnement des SCI ni un délai de marché immobilier. Le point de départ lié à la notification relève de la coordination L1234-3, dont le corps n'est pas fourni parmi les cibles ; aucun renvoi nouveau à cet article n'est introduit. Les fonctionnaires bénéficiaires de logements au trente-quatrième alinéa ne sont pas assimilés aux salariés privés."
    ),
    'L1221-2': (
        "L422-2 ne crée ni CDD ni contrat de travail spécial. La cible proposée remplace les nouveaux emplois privés à terme par le contrat unique à durée indéterminée, sans fin automatique de l'emploi à l'achèvement d'une mission ou formation, et réserve les contrats antérieurs. La durée de dix ans d'une SCI, la convention d'aménagement et l'expérimentation d'usufruit sont des durées de véhicules ou d'opérations immobilières, sans effet de terme sur l'emploi. Par le renvoi à L631-12, les apprentis et personnes en professionnalisation demeurent recevables au logement universitaire lorsque leur formation s'inscrit dans ce contrat unique ; aucune ancienneté ni notification de rupture n'est ajoutée à cet accès."
    ),
    'L1234-9': (
        "L422-2 ne renvoie pas à cette indemnité de travail ; les opérations d'achat, de vente, de gestion et de filiales n'en modifient pas le régime. La cible proposée prévoit, à la rupture patronale du nouveau contrat, zéro indemnité ordinaire avant un an puis 0,20 mois par année totale, fractions en mois complets, plafond six mois, sous son exception de faute grave. Le seuil est apprécié à la fin effective avec préavis inclus, sans retrancher la première année. Les anciennes conditions de huit mois et composantes acquises sont conservées par sa transition. Aucun seuil salarial n'est appliqué aux garanties de rachat ou de logement, aux indemnités civiles de vente ni à l'accès à L631-12. La notification ne clôt pas à elle seule les procédures collectives ou les régimes publics distincts."
    ),
    'L261-1': (
        "Les renvois de L422-2 à L261-1 et suivants, à la plage L261-1 à L261-22 et à L261-1 pour l'acquisition auprès d'une SCI visent la vente d'immeuble à construire. La source et la proposition de la cible distinguent vente à terme et VEFA, avec obligation contractuelle d'édifier dans un délai déterminé. Il s'agit du terme de la livraison immobilière, non d'un CDD ou d'une mission mettant fin à un emploi. Ni le préavis salarié de quinze jours ni le seuil d'un an d'indemnité ne se substituent à ce délai ; les contrats immobiliers antérieurs et les garanties légales restent dans leur régime propre."
    ),
    'L261-12': (
        "Cible comprise dans le renvoi exprès aux articles L261-1 à L261-22 pour les ventes à l'association de L313-34 ou à ses SCI détenues à 99 %, ainsi que dans le régime des ventes d'immeubles à construire visé ailleurs. La source et la proposition interdisent les versements avant contrat ou exigibilité en VEFA et cantonnent les dépôts progressifs de la vente à terme sur un compte protégé. Ces garanties des acquéreurs sont maintenues ; les agréments HLM retirés ne les écartent pas. Il n'existe ici ni condition d'ancienneté salariée ni notification de licenciement ; l'exigibilité immobilière ne devient pas un préavis de quinze jours."
    ),
    'L261-14': (
        "La plage L261-1 à L261-22 appelle ce plafond civil : l'indemnité forfaitaire de résolution est limitée à 10 % du prix, avec faculté de demander la réparation du préjudice effectivement subi. Source et proposition conservent les deux branches. Ce pourcentage porte sur le prix immobilier et ne se confond ni avec la limite de 10 % du parc social de L422-2 ni avec six mois de salaire de L1234-9 proposé. Le retrait d'autorisations HLM ne réduit pas les droits des acquéreurs, anciens ou futurs ; aucun seuil d'ancienneté ni préavis individuel de travail n'est incorporé à la résolution de vente."
    ),
    'L631-12': (
        "Le quarante-sixième alinéa conserve le renvoi aux résidences universitaires. La cible officielle distingue les publics, le bail d'un an au plus renouvelable, l'absence de maintien et l'interdiction de cession ou sous-location ; sa proposition retire autorisation spécifique et agrément supplémentaire, conserve le conventionnement et précise l'accès futur des apprentis et personnes en professionnalisation dans le contrat unique. Le bail et la phase de formation ne fixent pas le terme de l'emploi ; aucune ancienneté d'un an ni preuve de versement d'une indemnité ne conditionne l'accueil. Le champ historique des immeubles conventionnés à la publication de la loi de 2017 et les baux anciens restent réservés. Ces dispenses propres à L631-12 ne sont pas comptées une seconde fois dans L422-2."
    ),
    'L615-10': (
        "Le deuxième alinéa de L422-2 autorise l'intervention comme opérateur sans pouvoir être tiers-financeur. La cible porte sur l'expropriation expérimentale des parties communes pendant vingt ans depuis la loi du 24 mars 2014, non sur l'expérimentation d'usufruit de cinq ans du b de L422-2. Redevance mensuelle d'entretien, hypothèque, responsabilité, diagnostic, provisions et allocations de logement gardent leur régime. Le retrait de l'actualisation triennale du plan n'existe que dans la proposition de la cible et n'est pas un gain supplémentaire produit par cet article. Concession, servitude, procédures d'expropriation et indemnité de retour en copropriété ne sont pas des contrats privés de travail : ancienneté et notification de quinze jours leur sont inapplicables."
    ),
}

required = references['requirements'][source['code_id'] + '|' + source['source_id']]
checks = []
for key in required:
    target = references['targets'][key]
    checks.append(dict(target_key=key, view_sha256=target['view_sha256'],
                       assessment=assessments[target['number']]))

answer = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
answer.update(
    proposed_xml=proposed,
    reason=(
        "Réforme de fond supplémentaire par rapport à la source officielle entière et au previous_draft, qui conservait encore ces filtres : retrait de l'accord municipal de gestion, du minimum de vacance d'un an pour cette branche, de l'accord local spécifique d'aménagement, de quatre avis locaux, de l'accord préfectoral de prise de participation et de son opposition de deux mois, de l'autorisation ministérielle d'acquisition intégrale de SCI et de l'agrément spécifique des prestations d'aménagement auprès des SEM. Les contrôles préalables de création et d'augmentation de capital des filiales intermédiaires, leurs transmissions et leurs fenêtres de trois mois disparaissent également, sans déclaration ni veto administratif de remplacement. Les règles légales de protection des actifs sociaux demeurent. Le double accord pour les copropriétés en difficulté est retiré en coordination avec la proposition de L411-2, sans compter deux fois cette mesure. Ces filtres particuliers n'apportent pas de protection essentielle distincte démontrée des règles d'objet social, de propriété, d'urbanisme, de financement, de contrôle des organismes et des mandats qui subsistent ; les avis locaux répètent l'identification départementale du besoin. L'attente d'un an laisse inutilement hors de cette faculté des logements déjà vacants. L'extension territoriale des ventes aux personnes morales, les deux renvois au IV autonome de L302-5 et le traitement historique de l'usufruit sont conservés du brouillon antérieur. Les renvois incohérents du conventionnement, de l'objet des filiales et de l'affectation des résultats sont corrigés expressément. Les autres dispositions sont maintenues dans leur texte source, sans réécriture stylistique ni réduction d'impôt revendiquée : plafonds, garanties, actifs cantonnés, évaluation des apports et financement aux conditions du marché ont une fonction de protection distincte."
    ),
    review_notes=(
        "Source entière, notes, previous_draft entier, coordination.json, policy.json et les neuf cibles de reference-targets.json lus. Les 68 paragraphes source conservent leur position ; deux paragraphes transitoires sont ajoutés après eux. Aucun tableau ni image dans l'article. Les dispositions inchangées sont reprises intégralement depuis la source, et non depuis ses reformulations antérieures.\n"
        "SRU : textes initiaux des articles 82 et 149 et leurs pistes joints lus entièrement. L'article 82 a ajouté notamment la faculté favorable d'acquisition, travaux et location provisoire dans les copropriétés sous plan de sauvegarde : elle reste ouverte aux futures opérations recevables, ainsi que les extensions autonomes ultérieures aux OPAH dédiées et ORCOD. L'article 149 a remanié les compétences d'aménagement et ouvert des activités d'accession et services ; il n'établit pas l'origine de chacune des 68 dispositions actuelles. L'exception à L443-14 et les compétences favorables ne sont pas abrogées pour leur filiation. Aucune prétention d'examen achevé des 209 articles ni de suppression des autres règles SRU.\n"
        "Corpus public consulté en lecture seule : L411-1, L411-2 source et proposition, L442-11, L831-1 source et proposition, L302-5 source et proposition, R442-23 et R422-17-1 à R422-17-4 avec leurs notes. Le double accord supprimé au trente et unième alinéa correspond à la dispense déjà portée par L411-2 proposé ; le premier alinéa comporte aussi une compétence de gestion plus large, notamment sur des logements privés vacants. L442-11 protège décence, loyers et ressources : ces mêmes garanties accompagnent l'accès anticipé par le premier alinéa, sans restreindre la faculté distincte de l'alinéa 63. Son seuil source de plus d'un an appelle une harmonisation de L442-11, qui n'est pas rédigée par ce fichier ; l'application au champ élargi est déjà expressément fixée dans L422-2 proposé.\n"
        "La correction de L351-2 vers L831-1 au vingt-huitième alinéa est un renvoi nouvellement placé à cet endroit vers une cible absente des neuf vues fournies, quoique déjà citée ailleurs dans l'article. Son texte entier et sa proposition ont été confrontés dans le corpus ; la note de L631-12 documente la recodification de 2019. Seul le conventionnement locatif est visé, non la juxtaposition de tous les articles cités par cette note. Le délai d'un an et les conventions anciennes restent. Le renvoi préexistant aux alinéas 47 à 50 pour l'objet des sociétés sous contrôle conjoint omettait le 3° à l'alinéa 51 ; il est remplacé explicitement par les 1° à 3°, sans déplacer ces subdivisions. Les renvois au dernier alinéa de L411-2 sont remplacés par l'objet financier exact, car sa proposition ajoute une transition finale. Aucune nouvelle référence aux articles du contrat unique n'est ajoutée.\n"
        "Contrôle des chiffres maintenus : détention à au moins 99 %, plafond de syndic de 30 %, limite autonome de 10 % du parc, capital d'un euro, seuil de 25 % des logements sociaux et durée maximale de dix ans de la SCI, assimilation des apports liée à la demande de permis avant le 1er mars 2014, acquisition à date unique et deux délais d'un an de dissolution/conventionnement. Le rapport du commissaire aux apports évalue les actifs et protège les associés ; il ne fait pas double emploi avec les autorisations retirées. Les plafonds de ressources, prix et loyers, le caractère complémentaire ou subsidiaire des activités et les conditions d'aide des 1° à 3° préservent le champ social et l'affectation des compensations. Les agréments organiques HLM, ceux de l'intermédiation et de l'OFS ne sont pas assimilés à l'agrément spécifique d'une prestation d'aménagement : leur suppression ou leur redondance ne sont pas démontrées par cette source. Le justificatif de violences et les structures sécurisées identifient le public protégé ; aucun justificatif répétitif nouveau n'est ajouté.\n"
        "Le renvoi de ressources au premier alinéa du III de CGI199 novovicies n'importe ni ses dates d'investissement, ni ses délais de location, ni sa reprise fiscale du XI dans le régime des ventes HLM. Les dispenses fiscales favorables pour rupture patronale restent à leur champ. Les dates et seuils du b d'usufruit demeurent historiques : cinq ans depuis la loi du 24 mars 2014, zones de plus de 50 000 habitants et communes de plus de 15 000 habitants selon les textes applicables à ces opérations. Pas de nouvelle expérimentation ni de nouvelle liste à quotas. La note source sur les impositions 2027 et la vacance avant le 1er janvier 2027 ne fixe pas l'entrée en vigueur de ces coupes et ne proroge aucune expérimentation.\n"
        "Coordinations à terminer séparément : R442-23 doit perdre demandes, dossier d'autorisation et opposition pour les activités dispensées ; son renvoi ordinal au douzième alinéa de L422-2 est déjà décalé dans le texte source et ne doit pas être reconduit. R422-17-1 et R422-17-2, puis R422-17-3 et R422-17-4 pour les sociétés conjointes, doivent perdre transmissions, pièces spécifiques et circuits d'opposition dans ce champ, sans rétablir le représentant déclarant unique ou un préavis de quinze jours comme nouvelle condition d'opération. Les arrêtés fixant les pièces et les clauses types pertinentes doivent être coordonnés ; leurs corps complets ne sont pas fournis dans ce lot et ne sont pas présentés comme réécrits. La règle législative proposée interdit déjà leur emploi pour rétablir la procédure supprimée. L411-2 et les compétences parallèles, notamment L422-3, restent à harmoniser dans leurs lots respectifs, avec une même mesure dédupliquée.\n"
        "La séparation des résultats, le compte affecté et les conditions de financement public de L411-2 demeurent ; le cadre d'aides d'État et de compensations SIEG, notamment la décision 2012/21/UE citée dans cette cible, doit être coordonné sans conformité européenne présumée. Aucun nouveau pouvoir d'opposition pour simple appréciation de la capacité financière ne remplace ceux retirés. Les consentements des propriétaires, les contrats de mandat, la commande publique et les contrôles légaux continuent sur leurs fondements autonomes. Les références préexistantes à l'ordonnance de 2004 sur les partenariats et aux articles sanitaires L6148-2 à L6148-5-3 restent signalées pour concordance avec le droit actuel de la commande publique et de la santé, hors corpus autorisé ; leur portée historique et les contrats valables ne sont pas supprimés ni leur actualité certifiée ici. Aucune taxe, recette compensatrice ou économie nationale chiffrée n'est créée ; le coût et le solde global des codes ne sont pas établis."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Accord préalable du maire pour la gestion des logements du premier alinéa, avec déduplication du champ déjà dispensé par L411-2 proposé.",
        "Condition de vacance depuis plus d'un an pour la faculté de gestion de logements privés du premier alinéa, sans restriction des autres voies de gestion.",
        "Accord administratif autonome des collectivités ou communautés intéressées pour les interventions foncières et opérations d'aménagement du quatrième alinéa.",
        "Limitation géographique des ventes complémentaires à des personnes morales aux seules communes désignées par les anciens renvois fiscaux et SRU.",
        "Quatre avis locaux obligatoires des alinéas 17 à 20, pour des besoins déjà identifiés dans le plan ou le schéma départemental.",
        "Accord du préfet, demande spécifique et opposition de deux mois pour les participations dans les sociétés d'aménagement ou de projet urbain partenarial.",
        "Autorisation préalable du ministre chargé du logement pour souscrire ou acquérir la totalité des parts d'une SCI, les conditions patrimoniales restantes demeurant.",
        "Agrément spécifique imposé aux SA HLM déjà constituées pour fournir des prestations d'aménagement aux sociétés d'économie mixte.",
        "Double accord du maire et du préfet, demande et opposition de deux mois du trente et unième alinéa, en coordination de la même dispense de L411-2.",
        "Opposition ministérielle préalable à la création d'une filiale intermédiaire, transmission spéciale et fenêtre d'exécution de trois mois.",
        "Opposition préfectorale préalable à l'augmentation de capital d'une filiale intermédiaire, transmission spéciale et fenêtre de trois mois ; même dispense pour les sociétés conjointes.",
    ],
    benefit_review=(
        "Les exonérations fiscales et aides spécifiques attachées au SIEG de L411-2 restent accessibles aux opérations futures remplissant leurs conditions, avec comptabilité distincte, affectation des résultats et garanties de financement. L'extension géographique des ventes aux personnes morales ne transforme pas toutes ces ventes en opérations fiscalement exonérées : caractère complémentaire, hypothèses d'intervention, ressources et prix maxima demeurent. Les plafonds du décret de 199 novovicies restent utilisables sans importer la fermeture de son volet fiscal principal aux acquisitions 2024. La garantie de rachat des accédants, la faculté de revendre les invendus de SCI à un organisme HLM, l'accession et la location-accession, les prestations à l'habitat participatif, aux OFS et en bail réel solidaire d'activité sont maintenues pour les situations futures recevables. La dérogation à L443-14 pour les cessions rendues nécessaires par l'aménagement demeure. Les facultés SRU82 d'acquérir et revendre des lots, d'y effectuer les travaux et de les louer provisoirement, avec dérogations réglementaires favorables, restent ouvertes ; seuls les filtres administratifs sont retirés. La dispense de la sous-section 1 de la section 2 du chapitre III du titre IV pour les trois alinéas d'usufruit/nue-propriété reste entière. L'expérimentation de cinq ans depuis 2014 conserve ses opérations et droits historiques, sans fermeture supplémentaire ni prorogation inventée d'une fenêtre déjà expirée. Les prestations pour les organismes agréés et l'association de L313-34, les logements à la sous-location, les hôtels sociaux, hébergements, terrains familiaux, logements conventionnés et services aux personnes âgées, handicapées et victimes de violences demeurent accessibles aux futurs publics éligibles ; garanties de décence, loyers, ressources et sécurité conservées. Les apprentis et personnes en professionnalisation restent accueillis en résidence universitaire par L631-12, y compris dans le contrat unique proposé. La gestion élargie des logements vacants applique les mêmes protections au titre du premier alinéa sans fermer les facultés déjà ouvertes, notamment à l'alinéa 63. Les 1° à 3° du logement intermédiaire conservent l'aide conditionnée, les plafonds et leur durée ; le capital d'un euro à défaut d'apports recevables, l'assimilation favorable des logements liée au permis antérieur au 1er mars 2014 et la faculté de contrôle conjoint demeurent. Les seuils 99 %, 30 %, 10 %, 25 % et dix ans ne sont pas supprimés comme prétendues charges fiscales : ils bornent des compétences ou protègent les actifs, sans constituer des prélèvements. Aucune taxe n'étant abolie par cet article, aucun avantage fiscal n'est déclaré sans objet. Droits anciens, aides et garanties régulièrement accordées sont préservés et les avantages maintenus ne sont pas réservés aux seuls dossiers anciens."
    ),
    reference_checks=checks,
    substantive_impact=dict(
        version=1,
        classification='material_reduction',
        assessment=(
            "Par rapport à la source officielle entière, le corps retire effectivement des accords, quatre avis, un agrément spécifique, une autorisation ministérielle et les transmissions et oppositions préalables des filiales ; il ouvre aussi la gestion avant plus d'un an de vacance et conserve l'extension territoriale déjà acquise. Les conditions et les avantages maintenus restent dans l'article intégral. Les coordinations du double accord de L411-2, des renvois SRU, du conventionnement et des sociétés conjointes ne sont pas autant de nouvelles coupes. Aucune taxe n'est supprimée ou réduite dans L422-2, et la longueur du texte transitoire ne mesure pas le gain."
        ),
        scope_limitations=(
            "Le lot couvre exclusivement L422-2. Les règlements, arrêtés de pièces, clauses types et articles parallèles identifiés doivent être harmonisés séparément ; aucune réécriture de ces textes ni clôture des 209 filiations SRU n'est revendiquée. Les contrats valides, droits anciens et fenêtres expérimentales expirées restent à leur champ. Les contraintes européennes de financement ne disparaissent pas. Les économies de coûts, les délais réels de réalisation, l'incidence financière des nouveaux pouvoirs et le solde net national ne sont pas chiffrés ni démontrés."
        ),
        new_burdens_review=(
            "Aucune charge administrative nouvelle autonome n'est identifiée : aucun registre, rapport, donnée, dossier, déclaration, délai d'attente ou visa ne remplace les procédures supprimées. Les garanties existantes de L442-11 accompagnent la seule faculté de gestion élargie aux vacances d'un an ou moins ; elles ne restreignent ni les bénéficiaires antérieurs de cette branche ni les autres voies déjà ouvertes. Les règles d'apports, de cantonnement et de financement sont maintenues, sans nouveau contrôle général de capacité ou obligation périodique. La suppression des avis et transmissions enlève aussi ces traitements aux autorités ; les contrôles légaux autonomes demeurent et leur coût net n'est pas établi. Aucun bilan de prélèvements ou de complexité pour l'ensemble des codes n'est revendiqué."
        ),
        effects=effects,
    ),
)

effect_keys = [(item['measure_id'], item['kind']) for item in effects]
assert len(effect_keys) == len(set(effect_keys)), 'Duplicate measure and effect in one article'
assert len({item['measure_id'] for item in effects}) == len(effects), 'Une seule entrée par mesure dans cet article'
source_text = plain(source['source_xml'])
proposal_text = plain(proposed)
for item in effects:
    assert len(item['source_quote']) >= 12 and item['source_quote'] in source_text, item['measure_id']
    assert len(item['proposed_quote']) >= 12 and item['proposed_quote'] in proposal_text, item['measure_id']
assert [item['target_key'] for item in checks] == required
assert all(len(item['assessment']) >= 80 for item in checks)

Path('answer.json').write_text(json.dumps([answer], ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'output_file': 'answer.json', 'article_count': 1,
                  'effects': len(effects), 'reference_checks': len(checks)}, ensure_ascii=False))
