import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
metadata = {}


def describe(number, reason, review_notes):
    metadata[number] = {'reason': reason, 'review_notes': review_notes}


describe(
    'L162-31-1',
    "Réécriture à droit constant : les finalités, chaque dérogation et ses limites restent dans leur subdivision d'origine. Les phrases distinguent les autorités d'autorisation, les avis simples et conformes, les fonctions des instances, l'accès aux données et les financements. Les durées et les listes de renvois sont conservées intégralement. Aucune réforme de fond de policy.json ne concerne ces expérimentations.",
    "Conserver la limite de cinq ans, le financement après échéance limité à dix-huit mois et le rapport au plus tard un an après la fin de chaque expérimentation. Les renvois aux III, V et VI de l'article 78 de la loi n° 2015-1702 et au V de l'article 54 de la loi n° 2017-1836 restent des références historiques opératoires, non des dates de la réforme proposée. La distinction entre avis national et avis conforme régional de la Haute Autorité de santé est maintenue. Les listes du II, y compris la présence de L. 162-23-6 au a et au e du 1°, sont conservées. Aucun déplacement des alinéas normatifs ; seule la faute d'accord « ceux couvert » est corrigée. Les règles de financement de ces expérimentations ne sont pas utilisées pour financer les baisses de prélèvements ou la transition des retraites."
)
describe(
    'L162-32',
    "Réécriture à droit constant : la subvention, les cotisations auxquelles elle se rapporte, la prise en charge agricole et la dispense d'avance de frais sont énoncées séparément avec leurs débiteurs explicites. Aucun changement de fond prévu par policy.json n'est appliqué au régime des centres de santé.",
    "Le renvoi historique à l'article 1031 du code rural est conservé tel qu'assigné ; sa correspondance dans la codification applicable aux assurances sociales agricoles appelle un contrôle, sans substitution inventée. La subvention ne concerne que les cotisations de L. 241-1 pour les catégories des sections 1 et 2 ; la dispense d'avance reste limitée à la part garantie par l'assurance maladie. Aucun taux de subvention n'est créé."
)
describe(
    'L162-32-1',
    "Réécriture à droit constant : les parties à l'accord et sa durée sont explicitées ; les longues dispositions relatives aux rémunérations, au conventionnement, à l'informatisation et aux aides sont scindées en phrases lisibles dans leurs alinéas d'origine. Tous les numéros, dont 4° bis, 6° bis et le 7° abrogé, sont conservés. Aucune réforme de fond de policy.json ne vise cet accord.",
    "La durée maximale reste de cinq ans et le délai d'examen ou de transposition des rémunérations autres que le paiement à l'acte reste de six mois. Le renvoi du 2° au premier alinéa de L. 162-32-2 est maintenu ; ce dernier porte sur l'approbation de l'accord et non expressément sur l'intégration des rémunérations : articulation préexistante à contrôler. L'interdiction de modifier les tarifs conventionnels, les conditions de zones du 4° bis, la consultation avant adaptation régionale des aides et le lien entre objectifs atteints et versement du 9° sont conservés."
)
describe(
    'L162-32-2',
    "Réécriture à droit constant : les effets de l'opposition, la reconduction, le maintien temporaire de l'accord et les trois cas de recours à l'arbitre sont formulés directement. Les autorités de désignation et le régime tarifaire subsidiaire restent distincts. Aucune modification de fond issue de policy.json.",
    "Le seuil d'opposition reste au moins la moitié dans l'une ou l'autre des deux catégories d'organisations, distinct de la majorité exigée pour s'opposer à la désignation de l'arbitre. Le délai d'arbitrage reste de six mois après le début des négociations. Les renvois aux quatre derniers alinéas du I de L. 162-14-2 et au 4° bis de L. 162-32-1 sont conservés. Articulation à contrôler entre les tarifs prévus ici pour les centres non adhérents et la base de remboursement aux tarifs d'autorité de L. 162-32-4 : ces formulations préexistantes ne sont pas harmonisées silencieusement. Les points d'extinction fondés respectivement sur la publication du remplacement et sur la conclusion et l'approbation du nouvel accord sont conservés."
)
describe(
    'L162-32-3',
    "Réécriture à droit constant : la violation des engagements, la faculté de mise hors convention, la procédure contradictoire et le maintien des autres mécanismes légaux sont rendus explicites. Les trois alinéas et leurs renvois sont maintenus. Aucune réforme de fond de policy.json.",
    "Le renvoi aux quatre derniers alinéas de L. 162-15-1 est conservé, sans le remplacer par une sélection de sanctions ; son étendue dépend du maintien de la structure de cet article. Préserver la possibilité d'observations et le cumul avec L. 133-4 et le chapitre V du titre IV du livre Ier. Vérifier l'articulation du tarif applicable au centre mis hors convention avec le remboursement des centres non adhérents prévu à L. 162-32-4 ; aucune assimilation des deux situations n'est opérée."
)
describe(
    'L162-32-4',
    "Réécriture à droit constant : les organismes qui remboursent, les sommes concernées et l'autorité qui fixe les tarifs d'autorité sont identifiés en deux phrases dans le même alinéa. Aucun changement de fond prévu par policy.json ne concerne ce remboursement.",
    "La base de remboursement demeure le tarif d'autorité fixé par arrêté interministériel pour chaque profession des sections 1, 2 et 3. Contrôler l'articulation avec les tarifs applicables aux centres non adhérents visés au dernier alinéa de L. 162-32-2 et avec les centres mis hors convention de L. 162-32-3 ; le texte assigné est conservé sur ce point sans supprimer cette distinction."
)
describe(
    'L162-33',
    "Réécriture à droit constant : l'habilitation à négocier, l'autorité de reconnaissance et les critères de représentativité sont répartis en trois phrases au sein de l'alinéa existant. Aucune réforme de fond de policy.json n'affecte ces critères.",
    "L'ancienneté minimale reste de deux ans à compter du dépôt légal des statuts. La note source relative à l'article 123 VII de la loi n° 2009-879 du 21 juillet 2009 conserve sa portée transitoire : les enquêtes liées aux échéances conventionnelles sont reportées jusqu'à la mise en place des unions régionales des professionnels de santé ; les organisations reconnues représentatives à l'entrée en vigueur de cette loi le restent jusqu'aux enquêtes suivantes. La rédaction proposée ne remet pas en cause ce maintien et ne relance aucun délai en 2026."
)
describe(
    'L162-34',
    "Réécriture à droit constant : le tribunal compétent devient le sujet de la phrase et le champ du litige est précisé sans modifier les conventions ni le règlement concernés. Aucune réforme de fond de policy.json.",
    "Le renvoi à L. 211-16 du code de l'organisation judiciaire et la compétence des tribunaux judiciaires spécialement désignés sont maintenus. La note source de l'article 36 de l'ordonnance n° 2019-964 du 18 septembre 2019 fixe l'entrée en vigueur au 1er janvier 2020 ; cette date historique ne vaut pas date d'une nouvelle réforme. La compétence administrative propre aux établissements thermaux de L. 162-41 reste distincte."
)
describe(
    'L162-34-1',
    "Réécriture à droit constant : la distinction entre identifiant du professionnel et identifiant de la structure est présentée en phrases courtes ; le contenu du décret et la finalité des documents sont explicités dans le second alinéa. Aucune réforme de fond de policy.json.",
    "Conserver le champ des centres de L. 6323-1 du code de la santé publique et le renvoi au premier alinéa de L. 161-33. L'obligation d'inscrire simultanément les deux numéros ne concerne que les cas fixés par ce décret ; elle n'est pas généralisée. L'identifiant de structure reste celui du lieu de réalisation de l'acte, de la consultation ou de la prescription."
)
describe(
    'L162-35',
    "Réécriture à droit constant : la condition tenant au dépassement de tarif et les personnes pouvant demander sa justification sont formulées en deux phrases ; l'examen par une commission reste dans le second alinéa. Aucune réforme de fond de policy.json.",
    "La justification reste une faculté à la requête d'un assuré, d'un service ou d'un organisme de sécurité sociale, sans sanction nouvelle ni interdiction générale des dépassements. Les qualifications conventionnelles de chaque catégorie sont maintenues selon la syntaxe de la source. Celle-ci ne désigne pas davantage la commission ni sa procédure ; aucun organe nouveau n'est inventé."
)
describe(
    'L162-36',
    "Réécriture à droit constant : l'obligation d'indiquer le prix effectivement payé, ses supports et la réduction éventuelle sont exprimés en phrases distinctes dans le premier alinéa. La conséquence de l'absence d'indications reste dans le second. Aucune réforme de fond de policy.json.",
    "L'obligation demeure applicable aux pharmacies de tout statut et à toute personne physique ou morale délivrant des produits ou articles remboursables au titre de l'assurance maladie ou maternité. Conserver le montant par produit ou article, les deux catégories de supports et, le cas échéant, le montant ou le taux de réduction. L'absence de ces mentions entraîne toujours l'absence de remboursement."
)
describe(
    'L162-37',
    "Réécriture à droit constant : la caisse destinataire du versement devient le sujet de la phrase, sans modifier les remises ni leur affectataire. Aucune réforme de fond de policy.json.",
    "Les deux renvois, L. 162-18 et L. 165-4, sont conservés. Le montant n'est ni réduit ni réaffecté au financement des baisses de prélèvements ou de la transition des retraites."
)
describe(
    'L162-38',
    "Réécriture à droit constant : l'autorité compétente, les prix et marges concernés et les critères de fixation sont exprimés en phrases séparées, sans déplacer la règle relative aux infractions. Aucune réforme de fond de policy.json.",
    "La fixation demeure facultative et prend la forme d'une décision des ministres chargés de l'économie, de la santé et de la sécurité sociale, sous réserve des dispositions conventionnelles. La note source renvoie au III de l'article 58 de la loi n° 2022-1616 du 23 décembre 2022 : entrée en vigueur selon les catégories, aux conditions et dates fixées par décret et au plus tard le 31 décembre 2025. Cette limite historique est conservée dans l'analyse temporelle, sans nouveau calendrier ni prix inventé."
)
describe(
    'L162-38-1',
    "Réécriture à droit constant : le contexte de vaccination, le payeur, les catégories de professionnels, le paiement direct aux centres et les deux régimes d'affiliation sont rendus plus lisibles dans leurs subdivisions d'origine. Le calcul des prélèvements, les bornes de l'abattement et le précompte sont intégralement conservés. Les baisses de CSG et les transferts vieillesse de policy.json ne sont pas étendus à ces affiliations particulières.",
    "La note de l'article 37 IV de la loi n° 2023-1250 du 26 décembre 2023 prévoit une entrée en vigueur au 1er janvier 2024 et l'application aux rémunérations perçues depuis le 1er octobre 2023 dans la campagne contre les papillomavirus humains. Elle ne permet pas, à elle seule, d'attribuer cette rétroactivité à l'ajout des infections invasives à méningocoques dans la version assignée du 28 février 2025. Garder cette distinction temporelle. Maintenir l'exclusion des professionnels déjà affiliés comme indépendants au titre d'une autre activité, le taux global fixé selon L. 642-4-2, les deux bornes de l'abattement par renvois au CGI et le précompte pour les organismes de L. 213-1 et L. 752-4. Aucun montant forfaitaire ou taux n'est créé."
)
describe(
    'L162-38-2',
    "Réécriture à droit constant : la compétence de l'arrêté est énoncée directement et les trois objets de sa réglementation sont formulés plus simplement dans leurs numéros respectifs. Aucune réforme de fond de policy.json.",
    "Conserver les quatre dérogations et le renvoi aux rendez-vous de prévention de L. 1411-6-2 du code de la santé publique. La facturation d'actes ou de prestations complémentaires reste soumise aux conditions de l'arrêté ; aucun droit inconditionnel à facturer ces compléments et aucun tarif ne sont ajoutés."
)
describe(
    'L162-38-3',
    "Réécriture à droit constant : le tarif des consultations devient l'objet principal de la phrase et le fondement dérogatoire est conservé. L'attribut de présentation de la source est supprimé. Aucune réforme de fond de policy.json.",
    "Les quatre articles auxquels il est dérogé et le renvoi à L. 1411-6-4 du code de la santé publique sont inchangés. L'arrêté reste celui des ministres chargés de la sécurité sociale et de la santé ; aucun tarif n'est chiffré."
)
describe(
    'L162-38-4',
    "Réécriture à droit constant : l'arrêté devient le sujet de l'obligation de fixer facturation et rémunération ; les personnes et le champ dérogatoire sont conservés. L'attribut de présentation de la source est supprimé. Aucune réforme de fond de policy.json.",
    "La source ne désigne pas les signataires de l'arrêté : aucune compétence ministérielle supplémentaire n'est inventée. Les renvois à L. 4211-4 du code de la santé publique et aux quatre articles dérogés sont conservés. La note source indique l'entrée en vigueur immédiate selon la formule exécutoire de la loi n° 2025-1403 du 30 décembre 2025 ; elle ne constitue pas une date d'entrée en vigueur de la présente réécriture."
)
describe(
    'L162-39',
    "Réécriture à droit constant : les parties et la durée de la convention sont exprimées en deux phrases ; les tarifs, le prix limite et les garanties procédurales sont clarifiés dans les subdivisions existantes. Aucune réforme de fond de policy.json.",
    "La durée reste de cinq ans au plus. Le 3° distingue les tarifs forfaitaires de responsabilité du prix limite de facturation par forfait ; le critère des facteurs de coûts d'exploitation reste rattaché à ce dernier. Le numéro 3°, visé par L. 162-40, est conservé, de même que la procédure permettant aux établissements de présenter leurs observations au 4°."
)
describe(
    'L162-40',
    "Réécriture à droit constant : le plafond de prix des soins thermaux pour les bénéficiaires concernés est formulé directement dans l'alinéa unique, sans modifier l'obligation des établissements. Aucune réforme de fond de policy.json.",
    "Le champ reste celui des bénéficiaires de la protection complémentaire de L. 861-3. Le plafond est toujours constitué par les tarifs forfaitaires de responsabilité du 3° de L. 162-39, sans substitution du prix limite de facturation ni montant nouveau."
)
describe(
    'L162-41',
    "Réécriture à droit constant : les conditions d'approbation et de publication, l'adhésion, l'absence de remboursement et la mise hors convention sont exprimées en phrases plus courtes, dans les cinq alinéas d'origine. Aucune réforme de fond de policy.json.",
    "Conserver les renvois aux trois premiers alinéas de L. 162-15 et à L. 162-15-2. La publication au Journal officiel reste le point de départ de l'entrée en vigueur. L'absence de remboursement des établissements non adhérents et la compétence de la juridiction administrative en cas de mise hors convention sont conservées ; elles ne sont pas assimilées aux règles des centres de santé ni à L. 162-34. Le délai d'adhésion reste fixé par la convention."
)
describe(
    'L162-42',
    "Réécriture à droit constant : le renvoi au régime arbitral et les deux modalités de désignation de l'arbitre sont formulés avec leurs sujets explicites. Aucune réforme de fond de policy.json.",
    "Le renvoi porte toujours sur le I de L. 162-14-2, sans extension au II. L'arbitre est choisi par l'Union nationale et au moins une organisation nationale représentative ; à défaut, il est désigné par le président du Haut Conseil pour l'avenir de l'assurance maladie. Aucun motif supplémentaire de substitution n'est ajouté."
)
describe(
    'L162-45',
    "Réécriture à droit constant : les agences qui décident, la forme forfaitaire de prise en charge, les destinataires du financement et l'objet de la décision sont explicités. Les quatre dérogations gardent leur numéro et leur portée. Aucune réforme de fond de policy.json ne modifie ce financement de coordination des soins.",
    "La note source précise l'article 5 I de l'ordonnance n° 2021-1554 du 1er décembre 2021, avec entrée en vigueur par décret au plus tard le 30 juin 2022 ; l'article 1 du décret n° 2022-801 du 12 mai 2022 l'a fixée au 14 mai 2022. Ces dates historiques ne sont pas de nouveaux délais. Les dispositifs de L. 6327-2 et L. 6327-6 du code de la santé publique, la prise en charge de tout ou partie des dépenses, le versement direct éventuel à la structure et la fixation éventuelle des prix aux assurés restent distincts. Les dérogations ne valent que dans la mesure nécessaire."
)
describe(
    'L162-46',
    "Réécriture à droit constant : la précision éventuelle des modalités d'application est distinguée de la fixation des modalités d'évaluation, sans déplacer l'alinéa. Les procédures financées et les actions bénéficiaires restent deux objets d'évaluation. Aucune réforme de fond de policy.json.",
    "Le décret demeure un décret en Conseil d'État et le champ reste celui de la présente section. La faculté liée à la nécessité concerne les précisions d'application ; le texte conserve la fixation des modalités d'évaluation des procédures de financement et des actions financées. Aucun indicateur chiffré ni économie nationale n'est ajouté."
)
describe(
    'L162-47',
    "Réécriture à droit constant du texte historique assigné : les fonctions de la mission, les critères de zonage, les consultations et les programmes sont formulés en phrases plus lisibles, en conservant les six numéros et tous les alinéas. Aucune modernisation implicite des institutions ni réforme de fond de policy.json n'est opérée.",
    "Point de portée temporelle majeur : source_state vaut ABROGE_DIFF et la borne valid_until est 2222-02-22 ; cette donnée technique ne constitue pas une date légale de maintien du dispositif. La note de l'article 128 IV de la loi n° 2009-879 du 21 juillet 2009 maintient, par dérogation au 1° du II de cet article de loi, le 2° dans sa rédaction antérieure et les décisions des missions régionales jusqu'à l'entrée en vigueur, dans chaque région, du premier schéma régional d'organisation des soins élaboré par l'agence régionale de santé. Pour appliquer ce 2°, le directeur général de l'agence régionale de santé est substitué à la mission. Ce maintien transitoire ne rétablit pas l'ensemble de l'article ; son applicabilité résiduelle requiert le contrôle de l'entrée en vigueur du schéma régional concerné. Les dénominations historiques, dont les conseils généraux, ne sont pas remplacées silencieusement. Incohérences internes préexistantes conservées et signalées : l'alinéa relatif aux avis vise des « propositions » au 2°, qui porte sur des zones, puis l'alinéa suivant vise les « projets de programme » des 3° et 4°, alors que le 3° porte sur la permanence des soins et que le programme de gestion du risque figure au 5°. Toute correction de ces renvois exige une coordination expresse hors de la réécriture stylistique. La révision du classement tous les cinq ans et la direction alternée par périodes d'une année sont conservées."
)

answer = []
for source in sources:
    number = source['number']
    if number == 'L162-31-1':
        xml = '\n'.join(Path(f'fragments/{number}-{i}.xml').read_text().strip() for i in range(1, 4))
    else:
        xml = Path(f'fragments/{number}.xml').read_text().strip()
    record = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    record.update(proposed_xml=xml, **metadata[number], status='rewrite_draft')
    answer.append(record)

assert len(answer) == len(sources) == 24
assert len(metadata) == 24
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
