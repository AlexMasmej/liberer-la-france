import json
import re
from html import unescape
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
paragraphs = re.findall(r'<p\b[^>]*>(.*?)</p>', sources[0]['source_xml'], re.S)


def p(text):
    return '<p>' + text.replace('<br />', '<br>') + '</p>'


def plain(text):
    return unescape(re.sub(r'<[^>]+>', '', text))


def base(source):
    return {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}


tax_id = 'taxe-annuelle-locaux-idf-suppression'
# Clé déjà utilisée dans le corpus pour l'exécution documentaire de L. 520-1.
creation_tax_id = 'taxe-creation-idf-piece-permis'

out = []
a = base(sources[0])
body = [
    "I. – La taxe annuelle sur les locaux à usage de bureaux, les locaux commerciaux, les locaux de stockage et les surfaces de stationnement situés dans les limites territoriales de la région d'Ile-de-France, composée de Paris et des départements de l'Essonne, des Hauts-de-Seine, de la Seine-et-Marne, de la Seine-Saint-Denis, du Val-de-Marne, du Val-d'Oise et des Yvelines, est supprimée pour les faits générateurs intervenant à compter de l'entrée en vigueur de la présente loi. Aucune taxe n'est due sur le fondement du présent article à raison de la disposition de ces biens au 1er janvier d'une année lorsque ce 1er janvier intervient à compter de cette entrée en vigueur.",
    "II. – Pour ces nouveaux faits générateurs, aucune obligation de déclaration ou de paiement ne pèse, sur le fondement du présent article, sur les personnes privées ou publiques propriétaires des locaux ou surfaces ou titulaires d'un droit réel portant sur ces biens.",
    "Cette suppression s'applique au propriétaire, à l'usufruitier, au preneur à bail à construction, à l'emphytéote ou au titulaire d'une autorisation d'occupation temporaire du domaine public constitutive d'un droit réel. Aucune déclaration sans montant à payer, confirmation d'exonération, pièce justificative ou déclaration de remplacement exclusivement liée à la taxe supprimée n'est exigée. Aucun engagement de transformation n'est requis au titre de cette taxe pour ces faits générateurs.",
    "III. – Pour l'application des dispositions fiscales autonomes qui renvoient au présent article, les catégories de locaux et surfaces sont définies comme suit :",
]
for i in range(4, 8):
    text = paragraphs[i].replace('° Pour les ', '° Les ', 1)
    text = text.replace(", qui s'entendent", " s'entendent", 1)
    body.append(text)
body.extend([
    paragraphs[8].replace('visées au 3° du V et au VI', 'visées au 3° du V'),
    paragraphs[9],
    "V. – Pour les seuls renvois opérés par des dispositions fiscales autonomes aux catégories de locaux ou de surfaces exonérés, les catégories suivantes sont maintenues :",
])
body.extend(paragraphs[11:18])
body.append(paragraphs[18].replace(
    'V bis.-A.-Sont également exonérés de la taxe,',
    "V bis. – A. Pour les seuls faits générateurs antérieurs à l'entrée en vigueur de la présente loi, sont également exonérés de la taxe,", 1))
body.extend(paragraphs[19:21])
body.append(paragraphs[21] + " Cette disposition ne peut rendre exigible une taxe pour un fait générateur auquel s'applique la suppression prévue au I. Les sanctions restent soumises aux règles d'application dans le temps de la loi répressive plus douce.")
body.extend([
    "VI. – Les tarifs et les circonscriptions tarifaires ne s'appliquent plus aux faits générateurs mentionnés au I, sous réserve de la définition conservée au 2° du a du 1 pour les renvois des impositions distinctes.",
    "1. a. La définition suivante est maintenue pour ces seuls renvois :",
    "1° (Abrogé) ;",
    "1° bis (Abrogé) ;",
    paragraphs[26],
    "3° (Abrogé).",
    "b. (Abrogé).",
    "2. a) (Abrogé).",
    "b) (Abrogé).",
    "c) (Abrogé).",
    "d) (Abrogé).",
    "e) (Abrogé).",
    "VI bis. – Pour l'application des renvois aux V et VI par des dispositions fiscales autonomes, les parcs d'exposition et locaux à usage principal de congrès sont assimilés à des locaux de stockage.",
    "VII. – Aucune déclaration ni aucun paiement de la taxe supprimée n'est exigé pour les faits générateurs mentionnés au I. Pour la seule taxe distincte prévue à l'article 1599 quater C, les modalités auxquelles renvoie le VII de cet article demeurent le dépôt d'une déclaration accompagnée du paiement de cette seule taxe, avant le 1er mars de chaque année, auprès du comptable public compétent du lieu de situation des surfaces imposables. Ce dépôt ne comprend aucune déclaration ni aucun paiement au titre de la taxe supprimée.",
    "VIII. – Pour les faits générateurs antérieurs à l'entrée en vigueur de la présente loi, le contrôle, le recouvrement, le contentieux, les garanties et les sanctions relatifs à la taxe demeurent régis par les règles applicables en matière de taxe sur les salaires jusqu'au 31 décembre 2003, sous réserve des règles d'application dans le temps de la loi répressive plus douce.",
    "IX. – La taxe due à raison de ces faits générateurs antérieurs n'est pas déductible de l'assiette de l'impôt sur le revenu ou de l'impôt sur les sociétés.",
    "X. – Les faits générateurs antérieurs à l'entrée en vigueur de la présente loi restent régis par les dispositions qui leur étaient applicables, même si la déclaration, l'échéance de paiement, la liquidation ou la mise en recouvrement est postérieure. Sont conservés, pour ces faits, l'ensemble des exonérations, seuils, tarifs réduits, réductions et règles de classement territorial applicables, ainsi que les créances légalement nées, leur liquidation, leur recouvrement, les garanties, les imputations, les restitutions, les prescriptions et les recours. La suppression n'ouvre aucun droit général au remboursement des taxes antérieurement dues.",
    "Les définitions et catégories maintenues aux III, IV, V, VI et VI bis ne constituent aucun fondement d'imposition au titre du présent article. Les renvois qui déterminent le champ d'un avantage fiscal ou d'un régime distinct continuent de s'appliquer à ces définitions et catégories, sans être privés d'effet par le I et sans modification du champ ni des exclusions propres à ces dispositions. Pour ces seuls renvois, la qualification de locaux taxables s'apprécie d'après le champ matériel et territorial et les exonérations qui auraient été applicables en l'absence de la suppression de la taxe ; elle ne rend exigible aucune déclaration au titre de la taxe supprimée. L'exonération de taxe foncière prévue à l'article 1384 F reste accessible aux nouvelles transformations de bureaux qui en remplissent les conditions. Les exclusions propres à l'article 1599 quater C demeurent applicables dans leur champ exact.",
])
a.update(
    proposed_xml='\n'.join(p(text) for text in body),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Suppression de la taxe annuelle de 231 ter pour tous les faits générateurs intervenant à compter de l'entrée en vigueur, dans les quatre catégories de locaux ou surfaces et pour tous les propriétaires ou titulaires de droits réels, publics ou privés.",
        "Suppression du dépôt annuel avant le 1er mars, du paiement, des déclarations à néant et des pièces exclusivement liées à 231 ter pour les faits générateurs nouveaux ; le dépôt distinct de 1599 quater C subsiste dans son champ.",
        "Suppression, pour les nouveaux faits générateurs, des quatre tableaux de tarifs au mètre carré du VI 2 a à d, comportant dix-sept montants pour 2026, et de leur indexation annuelle avec arrondi au centime supérieur du e.",
        "Suppression pour les nouveaux faits générateurs des engagements de transformation, du délai fiscal de quatre ans et des reprises ou majorations exclusivement attachées à l'exonération de la taxe supprimée ; les anciennes années gardent leur régime.",
    ],
    reason=(
        "Réforme de fond maintenue après seconde passe : abolition de la taxe annuelle francilienne sur la détention de bureaux, commerces, stockages et stationnements pour les nouveaux faits générateurs, avec suppression de son dépôt et de son paiement annuels. Les quatre tableaux et l'indexation disparaissent pour ce champ ; les conditions de l'exonération de transformation n'y sont plus nécessaires. Cette baisse de prélèvement procède de la politique entreprise et d'editorial_direction_2026_10_19, et non d'une attribution de toute la taxe à SRU 49. Par rapport à la source officielle, la réduction est matérielle ; par rapport au précédent brouillon, la taxe était déjà entièrement supprimée pour l'avenir : aucune seconde baisse fiscale n'est revendiquée. La seconde passe explicite la dispense des pièces exclusivement fiscales et restaure au plus près les définitions sources dans les parties conservées. Il demeure nécessaire de garder les catégories et exemptions appelées par 1384 F et 1599 quater C, la délimitation géographique appelée par ce dernier et ses modalités déclaratives existantes. Les supprimer ici pourrait retirer une exonération foncière ou rendre incohérent un régime distinct. Les créances et avantages des anciennes années restent protégés. L'article n'est donc pas intégralement abrogé et aucun prélèvement de remplacement n'est créé."
    ),
    review_notes=(
        "Source entière, quatre tableaux, notes vides et previous_draft entier examinés. Contrôle des dix-sept montants 2026 : bureaux 26,11/12,98 ; 21,99/10,94 ; 12,03/7,25 ; 5,82/5,26 euros par mètre carré ; commerces 8,96/4,66/2,39 ; stockage 4,69/2,39/1,23 ; stationnement 2,96/1,61/0,85. Leur absence dans la proposition correspond à la suppression du barème futur, non à une troncature. Les tarifs et leurs actualisations restent ceux légalement applicables aux années anciennes. Le fait générateur est le 1er janvier : aucune remise de l'année en cours si ce jour précède la bascule, aucun prorata ni date de promulgation inventés. Le V bis conserve pour les anciennes années la vacance au 1er janvier, le dépôt d'urbanisme de l'année civile précédente, les quatre ans depuis l'autorisation, la déclaration L. 462-1, l'exception pour circonstances indépendantes et la reprise de taxe avec majoration, sous réserve de la loi répressive plus douce. L'appel (1) du VI source n'a aucune note jointe ; aucun complément n'est supposé. "
        "Renvois vérifiés sur les sources entières de CGI 1384 F, 1599 quater C et 1764 et d'annexe III 344-0 B : maintenir le 1° du III pour l'exonération foncière facultative de cinq ans, ouverte aussi aux futures transformations éligibles ; conserver pour 1599 quater C ses exclusions des 2° à 2° bis et 5° du V et son seuil autonome de cinq cents mètres carrés, la définition d'unité urbaine au VI 1 a 2° et les modalités du VII. La taxe distincte n'est ni supprimée ni étendue. Les formulations sources du IV sont conservées, sauf le renvoi au calcul tarifaire futur devenu sans objet ; le X empêche que le mot taxable perde tout sens ou ressuscite 231 ter. Le V de 1764 doit être réservé aux engagements concernant les faits anciens de 231 ter, sans effacer son champ distinct de 231 quater. Le 15° de 344-0 B doit retirer 231 ter pour les nouveaux faits ; sa proposition actuellement exportée le mentionne encore sans cette réserve, coordination restant à exécuter hors lot. Le gel procédural à la taxe sur les salaires au 31 décembre 2003 n'est pas transformé en renvoi à cette taxe employeur désormais supprimée dans le projet. "
        "Passages référents repérés et lus dans CGI 31 I 1° c, 39 1 4° et 10, 93 1 : non-déductibilité des seules sommes anciennes et champ autonome du crédit-bail à coordonner expressément, sans modification silencieuse des exclusions zonales ou des limites de déduction. Urbanisme L. 520-1 source et proposition lus : sa taxe de création, déjà supprimée dans le projet avec transition propre, est distincte et son ancien renvoi importait seulement les définitions du III. Les articles hors lot ne sont pas déclarés réécrits. L'affectation du produit de 231 ter et ses plafonds budgétaires hors corpus restent à identifier et coordonner pour les encaissements anciens ; aucune recette de compensation ni économie nationale n'est chiffrée. SRU 49 et sa piste documentaire sont lus en entier : la phrase initiale de 2000 classait des communes DSU en troisième circonscription ; la norme actuelle à quatre circonscriptions et double éligibilité DSU/FSRIF diffère. La version historique LEGIARTI000006314639 n'est pas dans les fichiers impots/urbanisme du corpus consultés ; la filiation précise demeure non établie et ne compte pas comme volet SRU achevé. Les dotations CGCT L. 2334-15 et L. 2531-12 restent autonomes. Aucun effet sur la franchise TASCOM ni les dérogations littorales. L'empreinte fournie est recopiée ; elle diffère du SHA-256 brut de source_xml, dont la convention de calcul d'origine n'est pas documentée."
    ),
    benefit_review=(
        "Examen des avantages : le V couvre les fondations et associations reconnues d'utilité publique ; les archives et activités de recherche, sanitaires, sociales, éducatives ou culturelles ; les locaux administratifs et stationnements scolaires publics ou privés sous contrat ; les seuils stricts de 100, 2 500, 5 000 et 500 mètres carrés ; les stockages des coopératives agricoles et unions ; les parcs relais, y compris les seules places ainsi utilisées ; les emplacements sportifs attenants aux commerces. Ces catégories sont conservées pour les renvois autonomes, notamment les exclusions de stationnement de 1599 quater C, sans élargissement de cette taxe. Les exclusions topographiques des sites de production et des parties communes sont préservées. Le V bis maintient intégralement le bénéfice ancien de transformation en logements, ses conditions et l'exception de circonstances indépendantes, même si travaux ou recours sont postérieurs. Pour les années nouvelles, aucune taxe 231 ter ni condition pour son exonération ne subsiste. Le déclassement territorial favorable DSU/FSRIF, la réduction de 10 %, tous les tarifs réduits des organismes publics, professionnels et organismes sans but lucratif éligibles, y compris l'établissement immobilier de l'Etat créé par la loi du 18 août 2026 et ses sociétés intégralement détenues, restent garantis pour les faits anciens par le X. Ils deviennent sans objet pour les faits nouveaux parce que la taxe est intégralement supprimée, sans remplacement ni extension d'assiette. L'assimilation des parcs d'exposition et congrès au stockage reste au VI bis. L'exonération foncière autonome de cinq ans de 1384 F reste ouverte aux futures transformations recevables selon ses propres conditions et délibérations. La non-déductibilité du IX est une restriction, non un avantage retiré."
    ),
)
a['substantive_impact'] = {
    'version': 1,
    'classification': 'material_reduction',
    'assessment': "La source officielle établit un prélèvement annuel de surface et son dépôt avant le 1er mars. La proposition les supprime définitivement pour les faits générateurs nouveaux, au-delà d'une reformulation ou d'un report. Cette même abolition était déjà acquise dans previous_draft ; les précisions de seconde passe ne sont pas comptées comme une deuxième réduction. Les définitions et protections utiles à des régimes distincts restent opérantes.",
    'scope_limitations': "La taxe reste due pour les 1er janvier antérieurs à l'entrée en vigueur, selon tous leurs avantages et recours. 1599 quater C et 231 quater restent distincts. Les coordinations budgétaires et les articles déclaratifs ou de déduction hors lot ne sont pas intégralement exécutés ici ; ni le coût net national ni la filiation SRU complète ne sont établis.",
    'new_burdens_review': "Aucune charge nouvelle n'est identifiée : ni taxe, déclaration à néant, justificatif, registre ou engagement de remplacement. Le dépôt résiduel pour 1599 quater C reprend son renvoi existant au VII, sans nouvelle donnée ni échéance. Les contrôles des seules créances anciennes et les règles autonomes conservées ne constituent pas un remplacement de la taxe supprimée ; le solde de complexité de l'ensemble des codes n'est pas chiffré.",
    'effects': [
        {
            'kind': 'tax_removed',
            'measure_id': tax_id,
            'description': "Suppression du seul prélèvement annuel 231 ter pour les nouveaux faits générateurs, avec ses quatre catégories et ses tarifs au mètre carré.",
            'before': "Propriétaires et titulaires de droits réels publics ou privés en Ile-de-France au 1er janvier : surface taxable regroupée par nature et adresse/groupement, hors parties communes, sous exemptions ; tarifs 2026 bureaux normaux/réduits 26,11/12,98, 21,99/10,94, 12,03/7,25, 5,82/5,26 €/m² ; commerces 8,96/4,66/2,39 ; stockages 4,69/2,39/1,23 ; stationnements 2,96/1,61/0,85, avec classements et réductions favorables, puis indexation annuelle.",
            'after': "Aucune taxe 231 ter ni barème de remplacement pour les faits générateurs à compter de l'entrée en vigueur, sur ces mêmes catégories et pour toutes les personnes concernées ; anciennes années inchangées. Il s'agit d'un tarif de surface, non d'un taux proportionnel à un revenu.",
            'unit': 'euro',
            'affected_population': "Personnes privées ou publiques propriétaires, usufruitiers, preneurs à bail à construction, emphytéotes ou titulaires d'une AOT constitutive d'un droit réel sur les biens concernés en Ile-de-France.",
            'conditions_and_transition': "Premier 1er janvier à compter de l'entrée en vigueur, sans prorata. Créances, exonérations, restitutions et recours des faits antérieurs conservés ; aucun remboursement rétroactif général.",
            'replacement_or_new_burdens': "Aucun prélèvement ou financement de remplacement. Définitions et exonérations autonomes conservées ; les autres taxes gardent leur propre champ.",
            'source_quote': plain(paragraphs[0]),
            'proposed_quote': body[0],
        },
        {
            'kind': 'obligation_removed',
            'measure_id': tax_id,
            'description': "Suppression du dépôt et du paiement annuels exclusivement liés à la taxe abolie, conséquence de la même mesure, sans second prélèvement supprimé.",
            'before': "Pour chaque année imposable, dépôt d'une déclaration accompagnée du paiement avant le 1er mars auprès du comptable public du lieu des biens, selon le VII.",
            'after': "Aucun dépôt, paiement, confirmation d'exonération ou pièce exclusivement liée à 231 ter pour les faits générateurs nouveaux ; les formalités nécessaires aux anciennes années et à 1599 quater C conservent leur champ.",
            'unit': 'legal_duty',
            'affected_population': "Redevables de la taxe annuelle francilienne de 231 ter et services qui en recevaient la déclaration.",
            'conditions_and_transition': "Même bascule par fait générateur que la taxe ; une échéance postérieure ne dispense pas des obligations légalement nécessaires pour une ancienne année.",
            'replacement_or_new_burdens': "Aucun dépôt à néant, confirmation ou nouveau registre ; pas de déclaration équivalente de remplacement. Le VII réserve seulement la procédure préexistante de la taxe distincte de stationnement.",
            'source_quote': plain(paragraphs[43]),
            'proposed_quote': body[body.index(next(t for t in body if t.startswith('VII. –')))].split(' Pour la seule taxe distincte')[0],
        },
    ],
}
out.append(a)

a = base(sources[1])
a.update(
    proposed_xml=None,
    status='retained_unchanged',
    classification='retained_necessary',
    reason=(
        "Maintien intégral de la source officielle après seconde passe, sans conserver la reformulation seulement stylistique du précédent brouillon. Cet article assure des exonérations de TVA pour les locations agricoles, certains baux à droit réel, les locations nues et la gestion foncière ainsi que les logements meublés d'habitation. Il ne prévoit aucun agrément, déclaration, justificatif périodique ni délai minimal de location à supprimer : les trente nuitées sont une durée maximale de l'offre hôtelière, non une durée obligatoire d'emploi ou de bail. Les exclusions des 2° et 4° délimitent l'activité économique imposable, avec incidences sur la déduction ; les enlever indistinctement n'est pas une simple économie de démarches et nécessiterait une réforme coordonnée de la TVA et de son cadre européen. L'exception favorable du c pour les logements-foyers sans droit à déduction doit subsister. Aucune charge autonome sans fonction identifiée n'est conservée pour remplir une réécriture. Les catégories et prestations servent aussi à des taux réduits et avantages extérieurs ; leur effacement serait préjudiciable. Le d déjà sans objet ne justifie ni abrogation des exonérations ni renaissance de l'ancien régime SRU. Aucun allègement nouveau n'est revendiqué."
    ),
    review_notes=(
        "Source intégrale de treize alinéas, notes vides, précédent brouillon et contexte SRU relus. Maintien exact des numéros 1°, 1° bis, 2°, 3°, 4° et lettres a, b, b bis, c, d. Tous les cas d'exclusion du 2° sont conservés : stationnement, poursuite d'exploitation commerciale, accroissement des débouchés et participation aux résultats. Le 3° continue de viser seulement les 1° et 2°. Au b, trente nuitées offertes avec possibilités de reconduction, mise à disposition d'un local meublé et au moins trois prestations sur quatre demeurent cumulatives ; b bis conserve l'usage résidentiel et les secteurs autres que le b ; la réception peut rester non personnalisée. Le c conserve les locaux nus, meublés ou garnis, son renvoi aux b/b bis et son exclusion favorable précise pour L. 633-1 lorsque l'activité n'ouvre pas droit à déduction. "
        "CGI 260 et CCH L. 633-1 lus en entier avec leurs notes : les options TVA, dans leur champ et leurs limites propres, et l'identification des logements-foyers restent autonomes. Les passages référents de CGI 279, 199 undecies B et CCH R. 631-20/R. 631-21 ainsi qu'annexe III 46 AGG bis ont été examinés : les définitions de prestations ne doivent pas disparaître en faisant perdre taux réduits, exceptions favorables d'investissement outre-mer ou faculté de prestations communes. Leurs autres dispositions ne sont pas déclarées réécrites. Le cadre européen identifié dans le précédent brouillon est la directive 2006/112/CE, article 135, paragraphes 1 l et 2, et article 137, pour les locations, exceptions et options ; son texte n'est pas joint aux pièces pertinentes et aucun service externe n'a été contacté. Aucune suppression de contrainte européenne n'est présumée ; trente nuitées et trois prestations ne sont pas présentées comme des chiffres imposés par la directive. "
        "SRU 186 initial et piste documentaire lus intégralement, y compris le régime urbanistique et la substitution fiscale de son II : ce II ne changeait que le renvoi du d du 4°. Le d actuel est déjà sans objet ; l'article actuel ne renvoie plus à L. 318-5. Ce dernier, lu en entier dans le corpus, possède un régime actuel d'opérations et d'aides qui ne disparaît pas ici. L'historique intermédiaire de la disparition du d n'est pas fourni : SRU 186 et ses descendants ne sont pas déclarés intégralement traités. La source est ABROGE_DIFF avec fin de version au 1er janvier 2027 ; le texte de remplacement et sa concordance TVA ne sont pas fournis dans ce lot. La conservation doit être portée dans les véritables dispositions de recodification sans inventer leur numéro, ni prolonger implicitement cette version au-delà de sa borne ; ce contrôle hors lot reste identifié. Aucune date future de réforme n'est tirée de cette métadonnée. Le SHA-256 fourni, différent du hachage brut de source_xml selon une convention d'origine non documentée, est recopié exactement."
    ),
    benefit_review=(
        "Tous les avantages demeurent dans la source intégralement conservée, pour les opérations futures qui en remplissent les conditions : 1° exonération des locations agricoles ; 1° bis exonération des baux conférant un droit réel ; 2° exonération des terrains non aménagés et locaux nus dans son champ, sous ses exclusions économiques ; 3° exonération des locations et concessions de droits des seuls 1° et 2° relevant de la gestion foncière ; 4° exonération des locations meublées ou garnies d'habitation, occasionnelles, permanentes ou saisonnières, sous les seules exceptions b, b bis et c existantes. Au c, l'exclusion des logements-foyers de L. 633-1 dont l'activité n'ouvre pas droit à déduction préserve leur exonération, sans la réserver aux contrats anciens. Les possibilités de reconduction, la réception non personnalisée et le seuil d'au moins trois prestations restent identiques. Les lettres a abrogée et d sans objet ne portent aucun avantage opératoire actuel à retirer. Les options favorables de 260 restent distinctes ; les définitions utilisées par 279 et les dispositifs d'investissement ou de résidence ne sont pas effacées. Cette conservation ne démontre aucune réduction fiscale supplémentaire."
    ),
    substantive_impact={
        'version': 1,
        'classification': 'retained_necessary',
        'assessment': "La source officielle est maintenue intégralement pour conserver les exonérations de locations et leur frontière avec l'activité hôtelière taxable. Le brouillon antérieur changeait la rédaction sans modifier la norme ; il est remplacé par un maintien déclaré, avec zéro suppression de taxe ou d'obligation revendiquée.",
        'scope_limitations': "Aucune baisse de TVA hôtelière ou du stationnement, ni nouvelle option de déduction n'est décidée ici. L'articulation européenne et la recodification annoncée au 1er janvier 2027 nécessitent des textes hors lot ; leur vérification intégrale n'est pas prétendue acquise. La continuité des avantages est à coordonner dans le texte de remplacement.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée puisque la source reste intégralement applicable sans nouveau texte : ni déclaration, agrément, registre ou durée minimale ajouté. Les durées d'offre et services existants délimitent la taxation et ne deviennent pas de nouvelles démarches. Aucun solde national de complexité ou coût n'est chiffré.",
        'effects': [],
    },
)
out.append(a)

a = base(sources[2])
old = re.findall(r'<p\b[^>]*>(.*?)</p>', sources[2]['source_xml'], re.S)
transition = (
    "Le a du I demeure applicable aux sommes légalement dues à raison de faits générateurs antérieurs à l'entrée en vigueur de la loi portant suppression du prélèvement mentionné à l'article L. 520-1 du code de l'urbanisme, même si leur paiement intervient après cette entrée en vigueur. Les renvois aux articles L. 520-1 à L. 520-22 s'entendent, pour ces sommes, de leur rédaction applicable à ces faits générateurs. Ils ne peuvent fonder une imposition pour les faits générateurs auxquels la suppression s'applique. Le II demeure applicable à la taxe d'aménagement dans son champ propre. Le présent article ne constitue pas un fondement d'imposition et ne peut rétablir un prélèvement supprimé."
)
a.update(
    proposed_xml='\n'.join(p(text) for text in old + [transition]),
    status='rewrite_draft',
    reason=(
        "Coordination nécessaire, sans nouvelle réduction de prélèvement : les cinq alinéas sources sont intégralement conservés et une transition réserve l'utilisation des anciens articles L. 520 au portefeuille légalement antérieur à la suppression déjà rédigée à L. 520-1. Elle préserve l'incorporation au prix du terrain des sommes effectivement payées pour ces faits anciens, même après la bascule, sans recréer le prélèvement. Le II et l'incorporation de la taxe d'aménagement au prix de revient de l'ensemble immobilier restent inchangés. Après réexamen du précédent brouillon, aucune coupe supplémentaire ne se justifie ici : l'article n'institue ni les taxes ni une déclaration, autorisation ou pièce autonome ; effacer un coût réellement supporté pourrait accroître le résultat ou la plus-value imposable. Les suppressions doivent porter sur leurs fondements, non sur cette règle de coût. La transition antérieure est conservée et rendue précise pour L. 520-1 ; aucune simple modernisation stylistique n'est comptée comme réforme."
    ),
    review_notes=(
        "Source entière de cinq alinéas, deux notes, previous_draft entier et SRU 202 initial entier lus. Conservation exacte des I, a, b, c, II, du caractère payé de la redevance, du prix du terrain au I et du prix de l'ensemble immobilier au II. Ni le b devenu sans objet ni le c abrogé n'est une mesure nouvelle de suppression. L. 520-1 source et proposition ont été lus en entier : la suppression porte sur les faits générateurs à compter de l'entrée en vigueur, non sur les paiements, et protège les droits et recours antérieurs. L. 520-2 à L. 520-6, L. 520-22 et L. 520-23 ont également été lus ; la bascule dépend de l'autorisation expresse ou tacite ou, à défaut, du début des travaux ou du changement d'usage selon le régime concerné. Le présent article ne liquide pas cette taxe et ne change pas son fait générateur. La différence préexistante entre le terme redevance de 302 septies B et le terme taxe du titre L. 520 actuel est signalée, sans substitution silencieuse ; la continuité historique de qualification reste à confronter aux textes de refonte. Le renvoi inverse L. 331-1 et CGI 1635 quater A sont lus en entier avec leurs notes : la taxe d'aménagement reste distincte et son incorporation au prix immobilier est conservée, y compris pour les futures opérations. "
        "Les notes sources visent l'article 1er du décret 2022-1102 du 1er août 2022 et le A du VI de l'article 155 de la loi 2020-1721 du 29 décembre 2020, pour les sommes dues à compter du 1er janvier 2021. Les notes de 1635 quater A/L. 331-1 visent aussi l'article 16 de l'ordonnance 2022-883 et le B du VI de l'article 155. Ces conditions historiques restent à leur champ, sans en faire la date de la nouvelle suppression ; les textes extérieurs non joints ne sont pas déclarés intégralement vérifiés. La règle de prix de revient demeure compatible avec le passage de l'IS à la distribution : elle ne rétablit ni impôt ordinaire annuel ni acompte sur bénéfice conservé, et n'autorise aucune double déduction ou remise en cause des réserves déjà taxées. Les coordinations 209/219 et des régimes de plus-values restent à leur objet propre. "
        "La clé taxe-creation-idf-piece-permis reprend celle déjà enregistrée dans substantive-impact.json pour la coordination documentaire de L. 520-1 ; malgré son libellé, l'effet ici est uniquement la conservation du traitement fiscal du coût ancien et non une nouvelle dispense de pièce de permis. Une harmonisation des clés de cette unique abolition doit rester dédupliquée, sans compter une taxe supprimée à nouveau. SRU 202 modifiait des références POS/PLU et d'autres dispositions d'urbanisme ; son texte initial n'établit pas la filiation de la règle fiscale actuelle. La version historique LEGIARTI000006309738 de la concordance n'est pas dans les fichiers impots/urbanisme consultés ni identifiée dans les pièces disponibles ; la filiation demeure incertaine et ce volet SRU n'est pas déclaré achevé. Aucune modification des franchises TASCOM ou des dérogations littorales. L'empreinte fournie est recopiée exactement ; sa différence avec le SHA-256 brut de source_xml est signalée sans inventer sa convention d'origine."
    ),
    benefit_review=(
        "L'incorporation du prélèvement réellement payé au prix de revient du terrain et celle de la taxe d'aménagement au prix de revient de l'ensemble immobilier sont conservées dans leurs champs et effets fiscaux propres ; elles évitent de faire disparaître un coût effectivement supporté, sans promettre un avantage chiffré identique pour tout contribuable. Les sommes de l'ancien portefeuille L. 520 gardent ce traitement même payées après la suppression ; les futures opérations soumises à la taxe d'aménagement conservent le II. Aucun avantage ne dépend du b devenu sans objet ou du c déjà abrogé. L'article n'établit pas une taxe ni une réduction de son taux : la suppression du prélèvement de création s'opère à L. 520-1, sans priver les bénéficiaires anciens de l'incorporation de leurs coûts."
    ),
    substantive_impact={
        'version': 1,
        'classification': 'coordination_only',
        'assessment': "Les deux règles de prix de revient de la source officielle demeurent entières. La transition rend les renvois L. 520 utilisables pour les sommes anciennes après l'abolition proposée à leur véritable fondement ; elle ne supprime aucune taxe supplémentaire, ne reporte aucun paiement et ne baisse aucun taux. La préservation temporelle existait déjà dans le brouillon précédent.",
        'scope_limitations': "Aucun effet chiffré sur le résultat, la plus-value ou l'IS n'est établi pour les contribuables concernés. La taxe d'aménagement reste applicable. La qualification historique redevance/taxe et les conditions des lois et décrets cités par les notes restent à vérifier dans leurs textes extérieurs ; la filiation SRU détaillée n'est pas établie.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée : le texte ne crée ni déclaration de coût, option, justificatif spécial, registre ni échéance. Le paiement et les règles fiscales préexistantes restent les conditions d'incorporation ; la transition empêche un renvoi de recréer le prélèvement supprimé. Aucun solde de complexité ou de finances publiques global n'est présumé.",
        'effects': [{
            'kind': 'coordination',
            'measure_id': creation_tax_id,
            'description': "Conservation du traitement fiscal des sommes anciennes après la suppression du prélèvement de création de locaux en Ile-de-France, sans nouvelle suppression de taxe.",
            'before': "Le a du I incorpore la redevance payée sous L. 520-1 à L. 520-22 au prix de revient fiscal du terrain, sans transition explicite pour l'abolition future ; le II incorpore la taxe d'aménagement au coût de l'ensemble immobilier.",
            'after': "Les cinq alinéas restent entiers ; le renvoi L. 520 est explicitement réservé aux sommes légalement dues pour les faits anciens, même payées après la suppression. La taxe d'aménagement et son incorporation restent inchangées pour leur champ, sans nouveau taux ni nouvelle assiette.",
            'unit': 'other',
            'affected_population': "Contribuables déterminant le prix de revient fiscal d'un terrain ou ensemble immobilier après paiement des prélèvements visés, notamment ceux du portefeuille ancien de L. 520.",
            'conditions_and_transition': "Le fait générateur du prélèvement de création doit être antérieur à l'entrée en vigueur de sa loi de suppression ; paiement postérieur admis dans le coût selon le I, sans double emploi. Le II ne reçoit pas cette restriction temporelle.",
            'replacement_or_new_burdens': "Aucune formalité ou taxe de remplacement. Le texte ne prétend ni dispenser des obligations propres aux régimes conservés ni rétablir l'IS annuel sur les bénéfices conservés.",
            'source_quote': plain(old[1]),
            'proposed_quote': transition,
        }],
    },
)
out.append(a)

Path('answer.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
