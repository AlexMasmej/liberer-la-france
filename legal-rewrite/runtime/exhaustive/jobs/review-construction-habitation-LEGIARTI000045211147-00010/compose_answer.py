import json
import re
from html import unescape
from pathlib import Path


sources = json.loads(Path('source.json').read_text())


def plain(xml):
    return unescape(re.sub(r'<[^>]+>', '', xml))


def effect(kind, measure_id, description, before, after, unit,
           affected_population, conditions_and_transition,
           replacement_or_new_burdens, source_quote, proposed_quote):
    return dict(kind=kind, measure_id=measure_id, description=description,
                before=before, after=after, unit=unit,
                affected_population=affected_population,
                conditions_and_transition=conditions_and_transition,
                replacement_or_new_burdens=replacement_or_new_burdens,
                source_quote=source_quote, proposed_quote=proposed_quote)


def article(i, proposed, reason, notes, impact, **extra):
    s = sources[i]
    return dict(**{k: s[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
                proposed_xml=proposed, reason=reason, review_notes=notes,
                status='rewrite_draft', substantive_impact=impact, **extra)


sru_measure = 'sru-suppression-quotas-et-carence'

p0 = """<p>Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui en prononce l'abrogation. Le quota d'au moins 30 % de logements familiaux locatifs sociaux, hors logements financés avec un prêt locatif social, dans les opérations de construction d'immeubles collectifs de plus de douze logements ou de plus de 800 mètres carrés de surface de plancher situées dans les communes faisant l'objet d'un arrêté de carence n'est plus opposable aux décisions d'autorisation prises à compter de cette date, y compris lorsque la demande a été déposée auparavant. Aucune demande de dérogation à ce quota n'est requise pour ces décisions.</p>
<p>Les dérogations accordées et l'inopposabilité du quota aux opérations destinées aux agents du ministère de la défense sur les terrains affectés aux besoins de ce ministère demeurent acquises aux autorisations délivrées avant cette date. Les prescriptions des autorisations régulièrement délivrées avant cette date ne sont pas automatiquement supprimées ; elles peuvent être modifiées ou contestées selon les procédures ordinaires, dans le respect des droits des tiers.</p>
<p>Les contrats et conventions valablement conclus, les opérations valablement engagées, les aides régulièrement attribuées, les engagements financiers acquis et les droits des occupants, des cocontractants et des tiers sont préservés, dans les conditions du V de l'article L. 302-5. Les stipulations qui se bornent à rappeler le quota supprimé cessent de l'imposer pour l'avenir. Les règles de sécurité, de salubrité, d'urbanisme, d'attribution, de conventionnement et de financement qui disposent d'un fondement légal autonome demeurent applicables. Les aides, exonérations, dispenses et dérogations qui relèvent de ces fondements demeurent ouvertes aux opérations et situations futures qui en remplissent les conditions, sans que la suppression du présent quota puisse justifier leur refus.</p>"""

a0 = article(
    0, p0,
    "Réforme de fond : abrogation prospective intégrale du quota de composition des opérations en commune carencée et de la nécessité de solliciter sa dérogation. Le précédent brouillon supprimait déjà toute la charge de cet article : aucune coupe supplémentaire de cette même obligation ne peut être comptée. La nouvelle rédaction précise la surface de plancher, rend explicite le maintien des dérogations et de l'exception défense pour les autorisations anciennes et protège les avantages autonomes pour les opérations futures. La conservation des prescriptions des permis antérieurs et des engagements valables protège la sécurité juridique, les occupants et les tiers ; elle ne maintient pas le quota pour les décisions nouvelles. Ce texte ne supprime aucun impôt par lui-même.",
    "Lecture intégrale des deux alinéas sources, des notes vides et du précédent brouillon. Les seuils alternatifs de plus de douze logements OU de plus de 800 mètres carrés de surface de plancher, le minimum de 30 %, l'assiette en logements familiaux et l'exclusion des logements PLS identifient la norme abrogée ; ils n'instituent aucun seuil futur. L'article 55 SRU joint a été lu en entier : son texte initial ne contient pas L. 302-9-1-2 ni ce quota par opération. La suppression actuelle repose sur la décision expresse de coordination, non sur une filiation intégrale démontrée par cette seule pièce ; l'origine et les étapes législatives du quota postérieur ne sont pas documentées ici. Le V proposé de L. 302-5 a été vérifié dans le corpus : il protège notamment les engagements antérieurs, met fin aux effets futurs de la carence et n'efface pas automatiquement les permis. Les sources et propositions courantes d'urbanisme L. 111-24 et R*431-16-3 ont été lues : leurs abrogations coordonnées doivent être adoptées ensemble pour retirer la répétition du quota et son tableau de dossier. Elles ne constituent pas deux autres mesures de réduction. Le quota distinct de 25 % du III ter de L. 302-5 relève de la même coordination générale, sans être l'objet du présent article. Les définitions autonomes du IV de L. 302-5 et les aides qui les utilisent restent nécessaires. Aucun examen achevé des 209 articles SRU n'est revendiqué ; aucune instruction en cours n'est remise à zéro et aucun contrat, permis ou avantage ancien n'est annulé par la seule abrogation.",
    dict(version=1, classification='material_reduction',
         assessment="Par rapport à la source officielle entière, suppression de l'obligation de réserver au moins 30 % des logements familiaux aux logements sociaux hors PLS dans les opérations visées. La dérogation administrative n'est plus nécessaire puisque la charge entière disparaît. Le précédent brouillon accomplissait déjà cette suppression ; les précisions de la présente passe ne sont pas un second gain.",
         scope_limitations="Les prescriptions des autorisations antérieures et les engagements acquis restent à leur régime ; aucune baisse du prix des logements, de fiscalité ni économie nationale n'est établie. L'adoption coordonnée de L. 111-24 et R*431-16-3 et de la transition de L. 302-5 reste nécessaire. La pièce SRU initiale ne démontre pas toute la filiation du quota actuel.",
         new_burdens_review="Aucune charge nouvelle n'est identifiée : aucun quota, registre, donnée, déclaration ou accord ne remplace la règle abrogée. Les procédures ordinaires de modification des anciens permis existaient déjà ; leur maintien protège les tiers. Les contraintes autonomes subsistent et le solde de l'ensemble des codes n'est pas chiffré.",
         effects=[effect(
             'obligation_removed', sru_measure,
             "Suppression du quota de logements sociaux par opération et de la nécessité de demander sa dérogation ; une seule mesure de suppression des quotas et de la carence avec ses articles de coordination.",
             "En commune faisant l'objet d'un arrêté L. 302-9-1, opération collective de plus de douze logements ou de plus de 800 m² de surface de plancher : au moins 30 % des logements familiaux doivent être sociaux hors PLS, sous dérogation préfectorale motivée et exception défense.",
             "Aucun quota de ce type ni demande de dérogation pour les autorisations décidées après l'entrée en vigueur, y compris sur demandes pendantes ; aucun impôt n'est modifié par cette règle.",
             'legal_duty',
             "Communes carencées, maîtres d'ouvrage et demandeurs d'autorisations d'opérations collectives entrant dans le champ des deux seuils alternatifs.",
             "Décisions nouvelles dès l'entrée en vigueur ; autorisations antérieures, dérogations accordées, exception défense, droits des occupants et engagements acquis protégés. Autres fondements légaux inchangés.",
             "Aucune obligation ou taxe de remplacement ; coordinations de L. 111-24 et R*431-16-3 nécessaires, sans les compter comme nouvelles suppressions distinctes.",
             "Dans les communes faisant l'objet d'un arrêté au titre de l'article L. 302-9-1, dans toute opération de construction d'immeubles collectifs de plus de douze logements ou de plus de 800 mètres carrés de surface de plancher, au moins 30 % des logements familiaux sont des logements locatifs sociaux définis à l'article L. 302-5, hors logements financés avec un prêt locatif social.",
             "Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui en prononce l'abrogation."
         )]),
    change_type='full_repeal', repeal_policy_id='editorial_direction_2026_10_19',
    repeal_scope="Suppression pour les décisions nouvelles du quota de 30 % de logements familiaux locatifs sociaux hors PLS dans les opérations collectives visées en commune carencée, ainsi que de la nécessité de demander une dérogation à ce quota ; anciens permis, avantages et engagements protégés.",
    benefit_review="La source comporte une dérogation préfectorale sur demande motivée de la commune, une inopposabilité aux logements destinés aux agents du ministère de la défense sur ses terrains et une dispense des opérations qui ne franchissent aucun des deux seuils. Pour les décisions futures, ces allègements sont absorbés par la suppression intégrale du quota pour toutes les opérations, sans quota ni autorisation de remplacement ; leurs bénéficiaires ne deviennent donc pas plus contraints. Les dérogations acquises et l'exception défense restent expressément opposables aux autorisations anciennes. L'exclusion des logements financés par un PLS est une restriction de la composition du quota, non une exonération fiscale : son retrait avec le quota ne supprime aucune aide ou exonération propre au PLS. Les définitions sociales et avantages autonomes restent applicables aux futures situations éligibles ; les prescriptions des anciens permis conservent leurs voies ordinaires de modification."
)


p1 = sources[1]['previous_draft']['proposed_xml'].replace('\\n', '\n')
old_parties = "Ces opérations donnent lieu à une convention entre la commune ou l'établissement public de coopération intercommunale compétent en matière d'habitat, ou le syndicat mixte mandaté par ces derniers, l'Agence nationale de l'habitat et l'État."
new_parties = "Ces opérations donnent lieu à une convention entre la commune ou l'établissement public de coopération intercommunale compétent en matière d'habitat, ou le syndicat mixte mandaté par ces derniers, et l'Agence nationale de l'habitat. L'État est également signataire lorsque la convention comporte des engagements qu'il prend directement, distincts de ceux de l'agence. En l'absence de tels engagements, sa signature n'est pas requise ; aucun accord, visa, avis ou déclaration préalable de remplacement ne peut être exigé au titre du présent article."
assert old_parties in p1
p1 = p1.replace(old_parties, new_parties)
old_delegation = "Lorsqu'un département ou un établissement public de coopération intercommunale a conclu avec l'État une convention en application des articles L. 301-5-1 ou L. 301-5-2, son représentant signe les conventions prévues au présent article en lieu et place du représentant de l'État et de l'Agence nationale de l'habitat, dans les conditions fixées par les conventions conclues au titre de ces articles."
new_delegation = "Lorsqu'un département ou un établissement public de coopération intercommunale a conclu avec l'État une convention en application des articles L. 301-5-1 ou L. 301-5-2, son représentant signe les conventions prévues au présent article en lieu et place du représentant de l'Agence nationale de l'habitat et, lorsque la signature de l'État est requise, du représentant de l'État, dans les conditions fixées par les conventions conclues au titre de ces articles."
assert old_delegation in p1
p1 = p1.replace(old_delegation, new_delegation)
p1 = p1.replace("Les règles de non-discrimination et les procédures d'évaluation environnementale et de participation du public requises sur un autre fondement demeurent applicables.", "Les règles de non-discrimination et les procédures d'évaluation environnementale et de participation du public requises sur un autre fondement demeurent applicables. La dispense de signature de l'État ne vaut ni accord ni délégation au titre de l'article L. 303-1-1.")
p1 = p1.replace("La dispense de signature de l'État ne vaut ni accord ni délégation au titre de l'article L. 303-1-1.", "La dispense de signature de l'État ne vaut ni accord ni délégation au titre de l'article L. 303-1-1. Pour l'application de cet article, le représentant de l'État dans le département conserve, même lorsque l'État n'est pas signataire de la convention, les compétences que cet article lui attribue en qualité de signataire ; les accords, avis et garanties qu'il prévoit demeurent requis.")

a1 = article(
    1, p1,
    "Réforme de fond supplémentaire par rapport au précédent brouillon : la signature de l'État n'est plus obligatoire s'il ne prend aucun engagement direct distinct de ceux de l'Anah ; aucun avis, visa, accord ou déclaration de remplacement n'est créé. Son consentement reste requis pour ses engagements propres et les délégations favorables restent applicables. Les coupes déjà acquises sont conservées : suppression de la publicité préalable d'un mois et des objectifs généraux d'équilibre social et d'organisation de la diversité de la population. La convention, son périmètre, les cinq rubriques a à e, les objets des aides et la consultation en mairie sont nécessaires pour identifier les engagements financiers et protéger les occupants ; leur suppression ferait perdre le support des aides et des garanties sans supprimer une charge autonome démontrée. Les droits des occupants, le caractère social de l'occupation, le maintien sur place et la non-discrimination sont maintenus. Les autres passages du précédent corps sont conservés sans nouvelle réécriture stylistique ; les clauses de transition et de suppression des quotas subsistent.",
    "Les dix alinéas sources, leurs notes vides, la pièce SRU 140 et le précédent brouillon ont été lus intégralement. SRU 140, III, a ajouté seulement le recours au syndicat mixte mandaté : cette faculté favorable est conservée pour les futures opérations. La publicité préalable et les deux objectifs retirés ne sont pas attribués à SRU par simple identité de numéro. Les lettres a à e et leur emplacement demeurent. Le mois de mise à disposition est supprimé comme procédure et délai minimal, sans le convertir artificiellement en trente jours ni toucher aux participations requises par un autre texte. L. 303-2 a été lu en entier : son III permet déjà qu'une convention d'ORT réunissant a à e tienne lieu d'OPAH, sans seconde convention ; ce mécanisme existant n'est pas un nouveau gain. L'État reste signataire d'une ORT conformément à son régime autonome : la dispense proposée ne concerne que l'obligation de signature issue de L. 303-1. L. 303-1-1 a été lu en entier : l'accord du préfet, l'accompagnement social, le rapport d'expert et les garanties judiciaires de division des copropriétés subsistent ; la dispense de signature OPAH ne vaut aucun de ces accords. Les passages de délégation de L. 301-5-1 et L. 301-5-2 et L. 321-1-1 ont été vérifiés : la substitution de signature reste conditionnée par les conventions de délégation, sans compétence nouvelle au syndicat mixte ni au délégataire. R. 321-5, I, 6° et 12°, et ses clauses types doivent être coordonnés pour ne pas exiger la signature ou un visa de l'État en l'absence d'engagement direct distinct ; aucun engagement budgétaire de l'État ne naît de sa seule tutelle sur l'Anah. Les conventions en cours non signées bénéficient des dispenses sans nouveau dépôt ni reprise des délais ; les anciennes conventions et aides restent protégées, sauf clauses de simple rappel des quotas abrogés. Aucune aide n'est réservée aux opérations anciennes, aucun montant ou droit automatique à subvention n'est créé. La rénovation locative de vingt-quatre mois exige séparément les articles 6 et 20-1 de la loi n° 89-462 et le décret n° 2002-120, hors du lot ; elle n'est ni réalisée ni financée par cette convention. Le périmètre des 209 articles SRU n'est pas déclaré achevé.",
    dict(version=1, classification='material_reduction',
         assessment="La comparaison à l'ensemble de la source montre le retrait du mois de publicité préalable, de deux objectifs généraux de composition sociale et, pour les conventions sans engagement propre de l'État, de sa signature obligatoire. Cette dernière coupe s'ajoute réellement au précédent brouillon ; les autres coupes y étaient déjà acquises. Les aides, actions de maintien des occupants et facultés de délégation restent ouvertes.",
         scope_limitations="Aucune réduction chiffrée du coût des conventions ou des logements n'est établie. La dispense de signature ne s'étend pas au régime autonome des ORT ni aux accords de L. 303-1-1. Les clauses types et les conventions de délégation restent à coordonner. Les engagements acquis et les autres procédures légales de participation demeurent.",
         new_burdens_review="Aucune charge nouvelle n'est identifiée : la signature supprimée n'est remplacée par aucun visa, avis, accord ou déclaration, ni par une preuve distincte d'absence d'engagement. Le consentement de l'État pour ses propres engagements existait déjà. La convention et sa consultation en mairie subsistent sans nouveau registre ni donnée ; aucun solde global de complexité n'est présumé.",
         effects=[
             effect('obligation_removed', 'opah-signature-etat-sans-engagement-suppression',
                    "Dispense de la signature obligatoire de l'État dans les seules OPAH où il ne souscrit aucun engagement direct distinct de ceux de l'agence.",
                    "Convention OPAH obligatoirement conclue avec l'État, l'Anah et la commune, l'EPCI compétent ou son syndicat mixte mandaté, même sans engagement propre distinct de l'État ; substitution du délégataire possible.",
                    "La signature de l'État n'est requise que pour ses engagements directs distincts de ceux de l'Anah ; sans ces engagements, aucun circuit d'accord de remplacement. Les autres parties et les délégations conventionnelles restent.",
                    'legal_duty',
                    "Communes, EPCI, syndicats mixtes mandatés, Anah et services de l'État préparant des conventions OPAH sans engagement direct distinct de l'État.",
                    "Conventions non signées à l'entrée en vigueur, y compris dossiers en cours sans recommencement ; conventions déjà conclues et engagements acquis préservés. Autres textes exigeant un accord ou une signature inchangés.",
                    "Aucun avis, visa, accord ou déclaration préalable de remplacement ; aucune attestation de non-engagement. Le consentement aux engagements de l'État reste requis.",
                    "Ces opérations donnent lieu à une convention entre la commune ou l'établissement public de coopération intercommunale compétent en matière d'habitat ou le syndicat mixte qui aurait reçu mandat de ces derniers, l'Agence nationale de l'habitat et l'Etat.",
                    "En l'absence de tels engagements, sa signature n'est pas requise ; aucun accord, visa, avis ou déclaration préalable de remplacement ne peut être exigé au titre du présent article."),
             effect('obligation_removed', 'opah-publicite-prealable-suppression',
                    "Retrait de la mise à disposition préalable obligatoire du projet et du mois d'attente correspondant, déjà acquis dans le précédent brouillon.",
                    "Tout projet de convention OPAH doit être mis à disposition du public pendant un mois avant sa signature ; durée mensuelle, sans conversion en nombre fixe de jours.",
                    "Aucune mise à disposition préalable imposée par cet article et aucun minimum d'attente de remplacement ; consultation de la convention signée pendant sa validité conservée.",
                    'legal_duty',
                    "Parties aux conventions OPAH et services chargés de leur préparation ; autres participations du public conservées dans leur champ.",
                    "Dispense pour les conventions non encore signées à l'entrée en vigueur ; anciennes conventions valables et procédures environnementales autonomes préservées.",
                    "Aucun dépôt ni publicité préalable équivalente ; maintien de la consultation après signature, déjà présente dans la source.",
                    "Avant sa signature, le projet de convention est mis à disposition du public pendant un mois.",
                    "La signature de la convention n'est subordonnée à aucune mise à disposition préalable du projet au titre du présent article."),
             effect('obligation_removed', 'opah-objectifs-composition-sociale-suppression',
                    "Suppression des deux prescriptions générales de composition sociale : respect des équilibres sociaux au premier alinéa et actions destinées à assurer la diversité de population au d. Ces deux volets, déjà acquis au brouillon, forment une seule mesure et un seul effet recensé.",
                    "L'opération est soumise au respect des équilibres sociaux ; sa convention doit prévoir des actions destinées au respect de la diversité de population. Les droits des occupants, les objectifs du plan départemental et du PLH, le caractère social de l'occupation et le maintien sur place s'y ajoutent.",
                    "Les prescriptions générales d'équilibre social et d'organisation de la diversité de population sont retirées. Droits des occupants, objectifs autonomes des plans, caractère social de l'occupation et maintien sur place restent applicables, sans typologie ni répartition de population de remplacement.",
                    'legal_duty', "Porteurs et signataires d'OPAH, acteurs des actions d'accompagnement et occupants des logements concernés.",
                    "Conventions non encore signées à l'entrée en vigueur ; non-discrimination, garanties d'occupation et conventions anciennes conservées.",
                    "Aucun objectif chiffré, fichier, justificatif, typologie ou répartition de population de remplacement. Les règles autonomes des plans et la non-discrimination demeurent.",
                    ('Elles sont mises en oeuvre' + plain(sources[1]['source_xml']).split('Elles sont mises en oeuvre', 1)[1].split('e) Les actions', 1)[0]).rstrip(),
                    ('Leur mise en œuvre' + plain(p1).split('Leur mise en œuvre', 1)[1].split('e) Les actions', 1)[0]).rstrip()),
             effect('coordination', sru_measure,
                    "Empêche la convention OPAH de rétablir les quotas, rattrapages, prélèvements et effets de carence supprimés ; coordination de la mesure générale, non nouvelle réduction distincte.",
                    "Les opérations doivent respecter les objectifs du PLH et la source ne règle pas la cessation des clauses qui reprennent les obligations légales de quota.",
                    "Ces objectifs autonomes restent applicables, mais aucun contrat fondé sur l'article ne rétablit les obligations légales supprimées ; les clauses de simple rappel cessent pour l'avenir.",
                    'legal_duty', "Collectivités et autres parties aux conventions OPAH touchées par l'abolition des quotas et de la carence.",
                    "Effets futurs après entrée en vigueur ; engagements librement consentis sur un fondement distinct et aides acquises restent protégés.",
                    "Aucune taxe, contribution ou opération forcée de remplacement ; aucune nouvelle suppression de taxe comptée dans cet article.",
                    "Elles sont mises en oeuvre dans le respect des équilibres sociaux, de la sauvegarde du droit des occupants et des objectifs du plan départemental d'action pour le logement et l'hébergement des personnes défavorisées ainsi que, s'il existe, du programme local de l'habitat.",
                    "Aucune convention conclue en application du présent article ne peut rétablir les quotas communaux de logements sociaux, les obligations de rattrapage, les prélèvements ou les effets de carence supprimés par la loi.")
         ]),
    change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Signature obligatoire de l'État dans toute convention OPAH, supprimée lorsqu'aucun engagement direct distinct de ceux de l'Anah n'est souscrit par l'État.",
        "Mise à disposition obligatoire du projet de convention au public pendant un mois avant toute signature, sans publicité ou délai minimal de remplacement.",
        "Condition générale de mise en œuvre de l'opération dans le respect des équilibres sociaux, sans supprimer les droits des occupants ni les objectifs autonomes des plans.",
        "Obligation de prévoir à la rubrique d des actions destinées à assurer le respect de la diversité de la population dans les quartiers, sans supprimer le maintien sur place et le caractère social de l'occupation."
    ]
)


a1['reason'] += " La dispense de signature conserve expressément les compétences préfectorales de L. 303-1-1 : l'accès aux procédures de redressement des copropriétés n'est pas perdu du seul fait que l'État ne signe plus systématiquement la convention."
a1['review_notes'] += " Coordination opératoire dans le corps de L. 303-1 : L. 303-1-1 attribue certaines facultés au préfet signataire. La nouvelle disposition lui conserve ces seules compétences même sans signature, afin de ne pas fermer les procédures pour les OPAH signées uniquement par l'EPCI et l'agence ; elle n'attribue aucun pouvoir nouveau au syndicat mixte ou à l'EPCI et ne supprime ni accord préfectoral, ni avis, ni saisine du juge. L. 303-1-1 devra reprendre explicitement cette dérogation de qualité de signataire lors de sa coordination propre."
a1['substantive_impact']['new_burdens_review'] += " Les compétences préfectorales conservées à L. 303-1-1 étaient déjà ouvertes dans le régime où l'État signait toute convention ; cette conservation n'étend donc pas les pouvoirs de contrainte par rapport à la source."
a1['substantive_impact']['effects'][0]['after'] += " Les compétences que L. 303-1-1 réserve au préfet signataire sont expressément conservées sans signature systématique, avec ses accords, avis et garanties."
a1['substantive_impact']['effects'][0]['replacement_or_new_burdens'] += " Les pouvoirs préfectoraux préexistants de L. 303-1-1 sont conservés dans le même champ, sans extension des motifs ou moyens de contrainte."


p2 = sources[2]['previous_draft']['proposed_xml'].replace('\\n', '\n')
old_approval = "Elle peut aussi participer au financement des travaux d'auto-réhabilitation accompagnée par des organismes agréés au titre de l'article L. 365-1."
new_approval = "Elle peut aussi participer au financement des travaux d'auto-réhabilitation accompagnée par des organismes agréés, pour les activités concernées, en application des articles L. 365-2 à L. 365-4, y compris ceux qui sont légalement réputés détenir l'agrément correspondant."
assert old_approval in p2
p2 = p2.replace(old_approval, new_approval)
assert "<p>3° Le produit des amendes prévues à l'article L. 651-2 ;</p>" in p2
p2 = p2.replace("<p>3° Le produit des amendes prévues à l'article L. 651-2 ;</p>", "<p>3° (Abrogé).</p>")
old_transition = "La règle de nomination par le seul ministre chargé du logement s'applique aux nominations intervenant à compter de l'entrée en vigueur de la loi ; elle ne met pas fin aux mandats en cours. La règle de réutilisation des pièces et données s'applique à compter de la même date, y compris aux demandes d'aides et aux conventions en cours d'instruction, sans nouveau dépôt ni reprise des délais déjà courus. Les aides accordées, les conventions valablement conclues et les droits qui en résultent sont préservés."
new_transition = "La règle de nomination par le seul ministre chargé du logement s'applique aux nominations intervenant à compter de l'entrée en vigueur de la loi portant la présente rédaction ; elle ne met pas fin aux mandats en cours. La règle de réutilisation des pièces et données s'applique à compter de la même date, y compris aux demandes d'aides et aux conventions en cours d'instruction, sans nouveau dépôt ni reprise des délais déjà courus. La précision du fondement des agréments pour l'accompagnement de l'auto-réhabilitation n'impose aucun nouvel agrément, renouvellement ou justificatif aux organismes déjà agréés ou légalement réputés agréés pour l'activité concernée. Les aides accordées, les conventions valablement conclues et les droits qui en résultent sont préservés ; les aides et les avantages liés au conventionnement demeurent ouverts aux situations futures éligibles. L'abrogation du 3° du III ne modifie ni les amendes et astreintes de l'article L. 651-2 ni leur affectation à la commune prévue par cet article. Les droits et créances légalement nés avant cette date restent régis par les dispositions qui leur sont applicables ; aucune restitution générale ni réaffectation rétroactive n'est instituée."
assert old_transition in p2
p2 = p2.replace(old_transition, new_transition)

a2 = article(
    2, p2,
    "Réforme de fond acquise au précédent brouillon et conservée : retrait de la cosignature du ministre chargé des finances pour les nominations au conseil ; le ministre chargé du logement signe seul sans supprimer les représentants financiers, la tutelle ni les contrôles budgétaires. Après réexamen, aucune autre coupe de charge n'est justifiée dans le présent article : les missions contre l'insalubrité et la précarité énergétique, l'accompagnement agréé, les plafonds de ressources et de loyers, la résidence principale et les contrôles de qualité protègent les occupants et l'utilisation des aides ; les délégations territoriales ne sont pas des autorisations cumulatives ; l'autorisation d'emprunts et de placements protège les fonds publics. Les ressources du III n'instituent pas par elles-mêmes les prélèvements auxquels elles se rattachent : effacer leur affectation ne démontrerait pas une baisse d'impôt. Le réemploi des pièces conserve le droit déjà applicable et ne constitue pas une nouvelle obligation supprimée. Deux coordinations nécessaires s'ajoutent sans gain fiscal revendiqué : remplacement du renvoi impropre à l'agrément de L. 365-1 par les fondements d'agrément du même chapitre, en conservant les organismes réputés agréés ; retrait au 3° du III de la mention d'une recette que L. 651-2 attribue intégralement à la commune. Les autres dispositions du précédent corps sont maintenues, non réécrites pour changer des mots.",
    "Les vingt et un alinéas sources, leurs notes vides, le précédent brouillon et SRU 185 ont été lus en entier ; les subdivisions I, II, III, III bis, IV et les rubriques numérotées demeurent à leur place. Le 3° du III est expressément abrogé, sans renumérotation des 4° à 10°. L. 651-2 et sa note ont été relus : l'amende civile et l'astreinte y sont intégralement versées à la commune ; l'incohérence préexistante de leur mention comme ressource Anah est donc traitée explicitement, sans supprimer la sanction, déplacer sa recette ou présumer un produit nouveau. Les créances anciennes légalement nées gardent leur régime, sans remboursement général. L. 365-1 définit les activités et le cadre européen, mais ne délivre aucun agrément : L. 365-2, L. 365-3, L. 365-4, leurs notes et R. 365-1 ont été lus pour établir les fondements applicables. La référence est désormais précise sans choisir arbitrairement un seul agrément pour toutes les formes d'accompagnement, ni retirer les agréments de plein droit ou réputés détenus ; la décision 2012/21/UE et la directive 2006/123/CE gardent leur champ. Le renvoi à L. 301-1 a été vérifié ; la carence d'immeuble de L. 615-6 reste distincte de la carence communale SRU et n'est pas supprimée. R. 321-1, R. 321-4, R. 321-5 et R. 321-6 ont été lus : les tutelles, les représentants financiers, les trois collèges égaux, les mandats, votes, majorités, budget et contrôles demeurent ; seules les éventuelles exigences réglementaires ou pratiques de cosignature des nominations doivent être retirées. Leurs autres actes conjoints ne sont pas supprimés. L'écart d'appellation préexistant entre Assemblée des communautés de France et Intercommunalités de France est signalé, sans remplacement silencieux. L. 321-3, L. 321-4, L. 321-8, L. 312-2-1 et L. 321-1-1 ont été lus en entier, et les passages de délégation de L. 301-5-1 et L. 301-5-2 vérifiés : aucune durée de convention, notamment le minimum de six ans de L. 321-4, ni aide, garantie ou avantage fiscal autonome n'est supprimé ; ils restent ouverts aux futurs bénéficiaires éligibles. Le réemploi des données reprend les droits déjà ouverts, notamment CRPA L. 113-12/L. 114-8 selon la coordination locale : aucun nouveau gain CRPA, accès aux données, registre ou certification n'est compté. Décret, règlement général et conventions types restent à mettre en conformité. R. 321-12 a été lu en entier : ses catégories d'aides, cas exceptionnels, cumuls favorables et contreparties ne sont pas retirés par les présents changements. SRU 185 portait les missions et le financement des travaux et ne justifie pas d'attribuer toute la gouvernance ou les ressources actuelles à cette loi ; ses autres volets et les 209 articles ne sont pas déclarés soldés. Aucune taxe, compensation ou économie nationale n'est inventée. La rénovation locative de vingt-quatre mois reste une coordination hors lot de la loi n° 89-462, articles 6 et 20-1, et du décret n° 2002-120.",
    dict(version=1, classification='material_reduction',
         assessment="Par rapport à la source officielle entière, une cosignature ministérielle obligatoire disparaît pour les nominations futures. Les contreparties des aides, les missions et la gouvernance restent utiles. Le réemploi des données reprend un droit existant et les corrections de renvois n'abolissent ni agrément ni impôt : aucune nouvelle baisse n'est ajoutée au gain déjà acquis par le précédent brouillon.",
         scope_limitations="Aucun coût monétaire de cosignature ni solde national n'est mesuré. Les tutelles et contrôles financiers, les actes conjoints autres que les nominations, les agréments des activités, les aides et leurs règles de durée demeurent. Les textes réglementaires, le règlement général et les actes de nomination doivent être coordonnés ; les autres volets SRU restent hors de cette conclusion.",
         new_burdens_review="Aucune charge nouvelle n'est identifiée : pas de signature, déclaration, contrôle ou agrément de remplacement. Le réemploi précise les droits existants sans nouvel accès aux données ; la correction des agréments dispense explicitement les organismes déjà reconnus de toute nouvelle démarche. Le retrait de la recette incohérente ne transfère pas de charge aux communes ; le solde global des codes n'est pas établi.",
         effects=[
             effect('obligation_removed', 'anah-nominations-signature-ministre-logement',
                    "Suppression de la cosignature du ministre chargé des finances pour la nomination du président et des membres du conseil d'administration, déjà acquise dans le précédent brouillon.",
                    "Chaque nomination est faite par arrêté conjoint des ministres chargés du logement et des finances ; aucune taxe ou assiette fiscale dans cette obligation de signature.",
                    "Nomination par arrêté du seul ministre chargé du logement ; collège de l'État, tutelles et contrôles budgétaires préservés, sans accord de remplacement.",
                    'legal_duty', "Ministres et services préparant les nominations au conseil d'administration de l'Anah ; membres et président concernés.",
                    "Nominations à compter de l'entrée en vigueur ; aucun mandat en cours interrompu ; autres actes interministériels inchangés.",
                    "Aucun visa ou avis financier de remplacement ; la représentation financière et les contrôles autonomes existaient déjà et demeurent.",
                    "Le président et les membres du conseil d'administration sont nommés par arrêté conjoint du ministre chargé du logement et du ministre chargé des finances.",
                    "Le ministre chargé du logement nomme, par arrêté, le président et les membres du conseil d'administration."),
             effect('coordination', 'reemploi-donnees-droit-existant',
                    "Explicitation du réemploi des pièces déjà légalement disponibles pour les aides et conventions ; aucun nouveau gain de suppression attribué à cette reprise du droit existant.",
                    "Le II renvoie à une procédure simplifiée par décret ; les droits de non-redépôt résultant du CRPA et des coordinations locales existent indépendamment de cette rédaction.",
                    "Le texte précise le réemploi des pièces exactes, à jour, disponibles et exploitables, sans redépôt ni certification répétée ; données manquantes ou à vérifier restent exigibles dans leur champ légal.",
                    'legal_duty', "Demandeurs d'aides, bailleurs conventionnés et services de l'Anah soumis au droit existant de réemploi.",
                    "Application immédiate y compris aux dossiers en cours, sans nouveau dépôt ni reprise des délais ; finalités autorisées, secrets et données personnelles protégés.",
                    "Aucun nouveau registre ou accès aux données ; aucune déclaration de substitution. La reprise d'une interdiction préexistante n'est pas comptée comme coupe nouvelle.",
                    "Un décret détermine les modalités d'application du présent II. Ce décret définit une procédure d'entrée en vigueur simplifiée des conventions.",
                    "Pour l'instruction des aides et l'entrée en vigueur des conventions, l'agence réutilise les pièces et données exactes et à jour qu'elle détient ou auxquelles elle a légalement accès."),
             effect('coordination', 'anah-auto-rehabilitation-fondement-agrements',
                    "Correction du renvoi à L. 365-1, qui définit les activités, vers les articles du même chapitre établissant les agréments ; conservation des équivalences légales favorables.",
                    "Financement possible de l'auto-réhabilitation accompagnée par des organismes dits agréés au titre de L. 365-1, alors que les agréments de ces activités sont fondés sur L. 365-2 à L. 365-4.",
                    "Référence aux agréments des activités concernées de L. 365-2 à L. 365-4, y compris ceux légalement réputés détenus ; aucun nouveau type d'agrément ni restriction d'un avantage existant.",
                    'regime', "Organismes d'accompagnement de l'auto-réhabilitation, bénéficiaires des travaux et Anah.",
                    "Dès l'entrée en vigueur ; aucun nouvel agrément, renouvellement ou justificatif pour les organismes déjà agréés ou légalement réputés agréés pour l'activité concernée ; accès des futurs éligibles maintenu.",
                    "Aucune autorisation supprimée ni ajoutée ; aucune déclaration de remplacement ; contrôles et cadre européen préexistants maintenus.",
                    "Elle peut également participer au financement des travaux d'auto-réhabilitation accompagnée par des organismes agréés au titre de l'article L. 365-1.",
                    new_approval),
             effect('coordination', 'anah-amendes-affectation-commune',
                    "Retrait de la mention incohérente du produit de L. 651-2 parmi les ressources de l'Anah, sans suppression ni nouvelle affectation d'une amende.",
                    "Le 3° du III cite ces amendes comme ressource Anah alors que L. 651-2 attribue intégralement le produit de l'amende et de l'astreinte à la commune.",
                    "Rubrique 3° abrogée ; amendes, astreintes et affectation communale de L. 651-2 inchangées, sans recette de compensation ni redistribution rétroactive.",
                    'other', "Anah, communes bénéficiaires des sanctions de L. 651-2 et personnes auxquelles ces sanctions s'appliquent.",
                    "Entrée en vigueur de la nouvelle rédaction ; droits et créances antérieurs légalement nés préservés selon leur régime, sans restitution générale.",
                    "Aucun impôt ou obligation supprimé du seul fait du retrait de cette mention de ressource ; aucune charge de remplacement.",
                    "3° Le produit des amendes mentionnées à l'article L. 651-2 ;",
                    "L'abrogation du 3° du III ne modifie ni les amendes et astreintes de l'article L. 651-2 ni leur affectation à la commune prévue par cet article.")
         ]),
    change_type='normative_reduction', reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Cosignature obligatoire par le ministre chargé des finances de l'arrêté de nomination du président et des membres du conseil d'administration de l'Anah, sans avis ou visa de remplacement."
    ]
)


answer = [a0, a1, a2]
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
