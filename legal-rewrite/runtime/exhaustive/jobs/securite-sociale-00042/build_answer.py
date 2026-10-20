import json
from html import escape
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
refs = json.loads(Path('reference-targets.json').read_text())
by_number = {a['number']: a for a in sources}
answers = {}


def put(number, paragraphs, reason, notes, removed=None, benefit=None):
    source = by_number[number]
    obj = {k: source[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    obj.update(
        proposed_xml=''.join('<p>' + escape(p, quote=False) + '</p>' for p in paragraphs),
        reason=reason,
        review_notes=notes,
        status='rewrite_draft',
    )
    if removed:
        obj.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if benefit:
        obj['benefit_review'] = benefit
    answers[number] = obj


put('L224-1', [
    "Le conseil ou les conseils d'administration des caisses nationales de l'assurance maladie, des allocations familiales et d'assurance vieillesse, ainsi que de l'Agence centrale des organismes de sécurité sociale, peuvent déléguer certaines de leurs attributions à des commissions comprenant des personnes qui n'appartiennent pas à ces conseils. Ces personnes doivent avoir la qualité de membre du conseil ou d'administrateur d'une caisse primaire d'assurance maladie, d'une caisse d'allocations familiales ou d'une union pour le recouvrement des cotisations de sécurité sociale et d'allocations familiales ou, pour les accidents du travail, de membre d'un comité technique national mentionné à l'article L. 422-1.",
    "Un décret en Conseil d'État fixe les règles de constitution de ces commissions et les modalités de désignation de leurs membres par le conseil ou les conseils d'administration des caisses nationales intéressées."
],
    "Réécriture à droit constant : la faculté de délégation et les qualités requises des membres extérieurs sont rendues explicites. La commission est facultative ; aucune autorisation individuelle, déclaration ou taxe n'est instituée ici. L'encadrement de la délégation est conservé pour protéger la représentation et la compétence des organes qui gèrent les fonds sociaux.",
    "Le renvoi à L. 422-1 identifie les comités techniques nationaux de prévention des risques professionnels ; il ne vise aucun régime de contrat de travail. R. 224-3, lu dans le corpus, interdit en principe la délégation aux commissions comprenant des membres extérieurs : son articulation avec la faculté législative spéciale de L. 224-1 doit être explicitée dans le décret, sans supprimer cette faculté. Ni mandat de membre de commission ni durée de ce mandat ne vaut durée d'emploi. Les règles de représentation paritaire restent à leur champ propre."
)

put('L224-3', [
    "Le directeur de chaque caisse nationale et le directeur de l'Agence centrale des organismes de sécurité sociale représentent leur organisme en justice et dans les actes de la vie civile. Chacun peut mandater à cette fin certains agents de son organisme."
],
    "Réécriture à droit constant : les titulaires de la représentation et le périmètre du mandat sont identifiés directement. Cette faculté de délégation facilite la gestion et l'accès au juge ; sa suppression ne retirerait aucune charge administrative inutile.",
    "Le mandat reste limité à des agents de la caisse ou de l'agence représentée. Il ne dispense pas du ministère d'avocat ou des autorisations organiques exigés par des dispositions distinctes ; la suppression particulière de l'autorisation centrale de pourvoi est portée par L. 225-1-1 proposé. Aucun nouveau formalisme du mandat n'est ajouté."
)

put('L224-4', [
    "Les représentants des caisses nationales des allocations familiales, de l'assurance maladie et d'assurance vieillesse, ainsi que ceux de l'Agence centrale des organismes de sécurité sociale, disposent d'un droit d'inspection sur les organismes qui relèvent de ces caisses ou de l'agence.",
    "Pour ces inspections, ils réutilisent les pièces et informations exactes et à jour auxquelles ils ont déjà légalement accès. Ils ne peuvent en exiger une nouvelle production lorsqu'elles permettent la même vérification. Cette dispense ne fait obstacle ni à une demande portant sur des éléments manquants, modifiés ou contradictoires, ni aux investigations nécessaires à la constatation d'une fraude. Elle n'étend pas les droits d'accès aux données et s'exerce dans le respect des secrets protégés et des garanties de la procédure.",
    "La dispense de nouvelle production s'applique aux demandes effectuées à compter de l'entrée en vigueur de la loi qui l'institue, y compris au cours des inspections déjà engagées."
],
    "Réforme de fond : retrait de la production répétée de pièces déjà légalement accessibles et suffisantes pour la même inspection. Le droit d'inspection de chaque réseau est maintenu, car il sert au contrôle de la gestion et à la prévention des irrégularités ; il n'est pas remplacé par une attestation générale.",
    "La dispense porte sur la répétition documentaire, sans créer de partage de données entre branches ou autorités. Les éléments incomplets, périmés ou incohérents restent demandables. Coordonner les instructions de contrôle et leurs listes de pièces pour les demandes futures, sans annuler les constatations ni les recours antérieurs.",
    removed=["L'obligation de produire de nouveau, pour la même vérification, les pièces exactes et à jour déjà légalement accessibles aux représentants chargés de l'inspection."]
)

put('L224-5', [
    "L'Union des caisses nationales de sécurité sociale est une union nationale au sens de l'article L. 216-3. Elle assure les tâches mutualisées de gestion des ressources humaines du régime général de sécurité sociale. Elle négocie et conclut les conventions collectives nationales prévues aux articles L. 123-1 et L. 123-2, dans les conditions prévues aux articles L. 224-5-1 et L. 224-5-3.",
    "Elle évalue et coordonne les politiques de formation du personnel et participe à leur mise en œuvre. Elle suit la gestion prévisionnelle de l'emploi, les effectifs, la masse salariale et les politiques de recrutement du régime général. Elle promeut la sécurité et la santé au travail.",
    "Sous réserve du 8° de l'article L. 225-1-1, elle peut exercer la fonction de centrale d'achat au sens du droit de la commande publique pour le compte des caisses nationales du régime général, de l'Agence centrale des organismes de sécurité sociale, des organismes locaux du régime général et de tout organisme d'un autre régime de sécurité sociale.",
    "L'État, les caisses nationales du régime général ou l'Agence centrale des organismes de sécurité sociale peuvent lui confier des missions relatives aux conditions de travail du personnel des organismes de sécurité sociale ou à tout sujet de fonctionnement d'intérêt commun, notamment les opérations immobilières. Elle peut également conclure avec les caisses nationales des autres régimes de sécurité sociale des conventions portant sur des travaux d'intérêt commun, notamment des opérations immobilières.",
    "Elle assure la gestion administrative et comptable du fonds mentionné à l'article L. 114-24."
],
    "Réécriture des missions mutualisées et coordination avec la suppression ciblée de l'agrément des accords nationaux dans L. 224-5-1. La centrale d'achat et les conventions interrégimes restent facultatives. Les missions de santé, de formation et de gestion du fonds sont conservées : leur effacement supprimerait des fonctions communes utiles plutôt qu'un doublon imposé aux usagers.",
    "L. 123-1 et L. 123-2, lus dans le corpus, distinguent le personnel ordinaire des agents de direction et du directeur comptable et financier ; leur agrément général est écarté seulement dans le champ national UCANSS par L. 224-5-1 proposé. Les renvois à L. 224-5-1 et L. 224-5-3 sont ajoutés pour cette coordination, non pour rétablir un agrément. L. 224-5-3 est une cible supplémentaire absente de la liste des targets mais son texte intégral est fourni dans le présent lot. La source cite le code des marchés publics ancien : la rédaction emploie le droit de la commande publique, sans inventer un numéro de concordance ni supprimer ses garanties. Réserve des achats bancaires du 8° de L. 225-1-1 maintenue. La note de 2022 décrit une entrée en vigueur passée, sans dater la réforme future."
)

put('L224-5-1', [
    "L'union est dotée d'un conseil d'orientation composé :",
    "– D'une part, de représentants des assurés sociaux désignés par les organisations syndicales nationales de salariés représentatives au sens de l'article L. 2121-1 du code du travail et, en nombre égal, de représentants des employeurs désignés par les organisations professionnelles nationales d'employeurs représentatives ;",
    "– D'autre part, du président et du vice-président des caisses nationales et de l'Agence centrale des organismes de sécurité sociale, lesquels ne peuvent appartenir au même collège.",
    "Le conseil d'orientation élit son président parmi ses membres.",
    "Le directeur de l'union et le président du comité exécutif des directeurs prévu à l'article L. 224-5-2 assistent à ses séances.",
    "Le conseil d'orientation définit les orientations générales de la gestion des ressources humaines du régime général de sécurité sociale. Dans ce cadre, il arrête le programme de la négociation collective sur proposition du comité exécutif des directeurs.",
    "Il donne son avis sur les orientations de la convention d'objectifs et de gestion mentionnée à l'article L. 224-5-5.",
    "Il donne son avis sur le rapport d'activité de l'union.",
    "Il nomme le directeur, le directeur comptable et financier et le directeur adjoint de l'union sur proposition du comité exécutif des directeurs.",
    "Il approuve le budget annuel de gestion administrative sur proposition du comité exécutif des directeurs.",
    "Il établit son règlement intérieur.",
    "Il adopte et modifie les statuts de l'union sur proposition du comité exécutif des directeurs.",
    "Par dérogation aux articles L. 123-1 et L. 123-2, les accords collectifs nationaux conclus par l'union ne sont pas soumis à agrément ministériel. Le conseil d'orientation peut s'y opposer à la majorité des trois quarts de ses membres désignés dans le mois suivant leur réception. Sous réserve de la date d'effet prévue par l'accord et des conditions de validité et de publicité qui lui sont applicables, l'accord devient exécutoire dès que le conseil décide expressément de ne pas s'y opposer ou, en l'absence d'une telle décision, à l'expiration de ce mois sans opposition. À la même majorité, le comité peut demander l'évocation d'un sujet pendant la négociation d'un accord collectif national.",
    "La suppression de l'agrément et la possibilité d'une exécution avant l'expiration du mois s'appliquent aux accords conclus à compter de l'entrée en vigueur de la loi qui les institue ainsi qu'aux accords antérieurs dont la demande d'agrément est encore en cours à cette date. Pour ces derniers, le délai d'opposition du conseil ne recommence pas à courir. Aucun nouvel agrément ni aucune déclaration équivalente ne sont requis. Les accords déjà applicables et les droits qui en résultent sont préservés."
],
    "Réforme de fond : suppression de l'agrément ministériel des accords nationaux UCANSS et de l'attente obligatoire d'un mois lorsque le conseil d'orientation renonce expressément à son opposition. La composition paritaire, la majorité des trois quarts, le pouvoir d'évocation, la négociation et les contrôles budgétaires internes sont maintenus. La réécriture précise les conditions d'exécution anticipée et la transition des demandes en cours.",
    "Dérogation législative expresse nécessaire aux agréments de L. 123-1 et L. 123-2, dont les textes ont été lus ; leurs champs extérieurs à ces accords nationaux ne sont pas supprimés. Ces deux renvois sont ajoutés ici et leurs cibles ne figurent pas parmi les targets imposées ; vérification effectuée dans le corpus public fourni. Maintenir la validité syndicale, le consentement, les majorités et les formalités de publicité autonomes ; ne pas rétablir les transmissions CPPNI supprimées par les coordinations de négociation collective. D. 224-7 3° concerne encore les accords locaux et n'est pas supprimé par cette dérogation nationale ; D. 224-7 5° et D. 224-8 deuxième alinéa gardent le mandat et le contrôle avant signature. La source attribue l'évocation au « comité » dans une disposition consacrée au conseil et dit « à la même majorité » : cette ambiguïté de désignation et d'assiette est signalée, sans transférer ce pouvoir au conseil ni changer silencieusement sa majorité. Le délai de réception doit être prouvable sans nouveau dossier ; les délais déjà consommés ne sont pas rouverts. L. 224-10 proposé réserve ce régime d'opposition distinct.",
    removed=[
        "L'agrément ministériel préalable conditionnant l'application des accords collectifs nationaux conclus par l'UCANSS, sans déclaration de remplacement.",
        "L'attente minimale d'un mois avant exécution lorsque le conseil d'orientation a déjà décidé expressément de ne pas exercer son droit d'opposition."
    ]
)

put('L224-5-2', [
    "L'union est dotée d'un comité exécutif des directeurs. Celui-ci comprend le directeur général de la Caisse nationale de l'assurance maladie, les directeurs de la Caisse nationale des allocations familiales, de la Caisse nationale d'assurance vieillesse, de la Caisse nationale de solidarité pour l'autonomie et de l'Agence centrale des organismes de sécurité sociale, ainsi que quatre directeurs d'organismes régionaux ou locaux de sécurité sociale du régime général désignés dans les conditions fixées par décret.",
    "Le comité exécutif peut s'adjoindre deux personnes qualifiées.",
    "Il élit son président parmi ses membres directeurs d'organismes. En cas de partage des voix, le président dispose d'une voix prépondérante.",
    "Le comité peut constituer des commissions en son sein.",
    "Le directeur de l'union assiste à ses séances.",
    "Le comité a notamment pour missions :",
    "1° D'élaborer le budget de gestion administrative et de prendre les décisions budgétaires, à l'exception de celles qui relèvent de l'article L. 224-5-1 ;",
    "2° De proposer au conseil d'orientation la nomination du directeur, du directeur adjoint et du directeur comptable et financier ;",
    "2° bis De déterminer les orientations pluriannuelles relatives aux missions de l'union et l'ensemble des moyens nécessaires à leur réalisation, en vue de la conclusion de la convention mentionnée à l'article L. 224-5-5 ;",
    "3° D'élaborer, après concertation avec les fédérations syndicales, le programme de la négociation collective qu'il propose au conseil d'orientation ;",
    "4° De mandater le directeur pour négocier et conclure les accords collectifs nationaux. Le directeur tient le comité informé de l'état des négociations ;",
    "5° De mettre en place, dans les conditions définies par négociation avec les fédérations signataires de la convention collective nationale, une instance nationale de concertation réunissant les caisses nationales et ces fédérations. Cette instance est consultée au moins une fois par an sur toutes les questions institutionnelles ayant un effet sur l'organisation du travail et l'emploi, notamment lors de l'élaboration des conventions d'objectifs et de gestion, des plans stratégiques de branche, des projets nationaux et des schémas directeurs informatiques."
],
    "Réécriture à droit constant des compétences exécutives et de leur articulation avec le conseil d'orientation. La concertation annuelle est conservée : elle garantit la représentation des salariés lors des transformations institutionnelles et ne se confond pas avec les rapports ou réunions CPPNI supprimés dans d'autres articles. Les commissions internes restent facultatives.",
    "Les quatre directeurs locaux ou régionaux, les deux personnes qualifiées, la voix prépondérante et le 2° bis sont maintenus. Le mandat de négociation ne vaut ni agrément ministériel ni terme d'emploi. Coordonner la mise en œuvre avec L. 224-5-1 proposé, qui retire l'agrément national sans supprimer la concertation ni le contrôle avant signature de D. 224-8. D. 224-5 et D. 224-6, lus, conservent leurs règles distinctes de désignation et de quorum ; leur lecture a fait apparaître dans D. 224-6 un renvoi aux commissaires du Gouvernement de D. 224-3, que le texte fourni de D. 224-3 ne mentionne plus. Cette incohérence réglementaire n'est pas corrigée silencieusement ici."
)

put('L224-5-3', [
    "Par dérogation aux articles L. 123-1 et L. 123-2, les décisions et les accords de l'Union des caisses nationales de sécurité sociale s'appliquent de plein droit lorsqu'ils assurent l'application automatique d'un accord collectif national.",
    "Dans les établissements de santé, les décisions et les accords de cette union ne sont pas opposables à l'autorité de tarification."
],
    "Réécriture à droit constant de deux dérogations : application de plein droit des actes d'exécution automatique d'un accord national et non-opposabilité à l'autorité de tarification des établissements de santé. Les supprimer rétablirait une contrainte ou modifierait le financement sanitaire ; aucun agrément ni justificatif nouveau n'est ajouté.",
    "La dérogation d'application automatique reste ouverte aux décisions et accords futurs répondant à cette condition, même après la suppression de l'agrément national dans L. 224-5-1. L. 123-1 et L. 123-2 ont été lus dans le corpus : ne pas étendre l'automaticité à des dispositions nouvelles négociées qui ne sont pas la simple application de l'accord national. La non-opposabilité tarifaire n'annule pas les droits salariaux applicables dans l'établissement.",
    benefit="L'application de plein droit, par dérogation à L. 123-1 et L. 123-2, évite une nouvelle procédure pour les décisions et accords qui exécutent automatiquement un accord collectif national : elle est conservée pour les actes futurs comme pour les actes existants. La non-opposabilité aux autorités de tarification des établissements de santé est aussi maintenue. Elle protège leur décision de financement, sans supprimer les droits conventionnels du personnel ni garantir un financement automatique. Aucun avantage, dispense ou dérogation du texte n'est fermé par la réforme de l'agrément national."
)

put('L224-5-4', [
    "Sous réserve des articles L. 224-5 à L. 224-5-3, l'Union des caisses nationales de sécurité sociale est régie par les dispositions du présent livre, notamment les articles L. 224-3, L. 224-10 et L. 281-3."
],
    "Réécriture à droit constant du champ des règles communes, sous réserve des dispositions spéciales de l'union. Ce rattachement assure la représentation et le contrôle des irrégularités graves ; il ne crée pas de dossier ou de prélèvement supplémentaire.",
    "L. 281-3, lu dans le corpus, porte sur la suspension, la dissolution et la révocation pour irrégularités graves, mauvaise gestion ou carence ; ces protections sont distinctes du délai général de tutelle retiré de L. 224-10. Le renvoi à L. 224-10 s'entend de sa rédaction proposée et ne rétablit ni l'agrément des accords nationaux ni le délai de vingt jours. D. 224-11 doit être coordonné pour ne pas qualifier toute délibération d'acte soumis à approbation."
)

put('L224-5-5', [
    "Une convention d'objectifs et de gestion conclue entre l'État et l'Union des caisses nationales de sécurité sociale détermine les orientations pluriannuelles de mise en œuvre des missions confiées à l'union.",
    "Elle détermine les moyens de fonctionnement de l'union et les règles de calcul et d'évolution de son budget. Elle prévoit les indicateurs associés aux objectifs et les conditions de conclusion des avenants en cours d'exécution, notamment pour tenir compte du renouvellement des conventions mentionnées à l'article L. 227-1.",
    "Elle est signée par le président du conseil d'orientation, le président du comité exécutif et le directeur de l'union.",
    "Les parties fixent sa durée pluriannuelle sans durée minimale légale. La convention et, le cas échéant, ses avenants sont transmis aux commissions parlementaires mentionnées à l'article LO 111-9.",
    "L'absence de durée minimale s'applique aux conventions conclues ou renouvelées à compter de l'entrée en vigueur de la loi qui l'institue. Les conventions en cours conservent leur durée et leurs engagements ; elles peuvent être modifiées selon leurs règles d'avenant."
],
    "Réforme de fond : suppression de la durée minimale de quatre ans, qui rigidifie la programmation sans être nécessaire à son caractère pluriannuel. Les moyens, les indicateurs, les trois signatures et le contrôle parlementaire sont maintenus ; aucune périodicité ou autorisation nouvelle ne remplace le minimum supprimé.",
    "La durée reste pluriannuelle et doit être fixée dans la convention. Le renvoi à L. 227-1 concerne le renouvellement des conventions des branches ; aucun alignement automatique de leurs durées n'est créé. Les commissions de LO 111-9 continuent de recevoir la convention et ses avenants. Les engagements financiers antérieurs ne sont pas résiliés par la suppression du plancher de quatre ans.",
    removed=["La durée minimale légale de quatre ans imposée à chaque convention d'objectifs et de gestion conclue avec l'UCANSS."]
)

put('L224-5-6', [
    "Les caisses nationales du régime général et l'Agence centrale des organismes de sécurité sociale peuvent chacune conclure avec l'Union des caisses nationales de sécurité sociale une convention précisant leurs objectifs et leurs engagements réciproques pour la réalisation des missions de l'union. Cette convention est signée, pour chaque caisse nationale ou pour l'agence centrale, par son directeur général ou son directeur et, pour l'union, par le président du comité exécutif et le directeur. Aucune transmission au ministre chargé de la sécurité sociale n'est exigée sur le seul fondement du présent article.",
    "Le caractère facultatif de la convention et la suppression de sa transmission s'appliquent à compter de l'entrée en vigueur de la loi qui les institue. Les conventions déjà conclues et les engagements qui en résultent demeurent applicables selon leurs stipulations. L'absence d'une convention distincte ne suspend pas les missions légales de l'union."
],
    "Réforme de fond : retrait de l'obligation de conclure une convention bilatérale avec chaque tête de réseau et de la transmission ministérielle correspondante. La convention reste possible pour des engagements spécifiques, avec ses signataires, tandis que les missions légales et la convention globale d'objectifs et de gestion continuent de s'appliquer.",
    "Coordination avec L. 224-5-5 : une convention bilatérale n'est plus un préalable obligatoire à l'exécution des missions déjà définies. Aucun dépôt, déclaration négative ni convention de remplacement n'est exigé. Les contrats existants ne sont pas caducs et leurs créances ne sont pas effacées. Les pouvoirs légaux de contrôle et d'accès aux documents demeurent distincts de la transmission systématique supprimée.",
    removed=[
        "La conclusion obligatoire d'une convention bilatérale séparée entre l'UCANSS et chacune des caisses nationales ou l'Agence centrale.",
        "La transmission systématique de chaque convention bilatérale au ministre chargé de la sécurité sociale sur ce fondement."
    ]
)

put('L224-6', [
    "Un décret précise, en tant que de besoin, les modalités spécifiques de tutelle et de fonctionnement de l'Union des caisses nationales de sécurité sociale, dans le respect des dispositions législatives qui lui sont applicables."
],
    "Réécriture de l'habilitation réglementaire à droit constant. La tutelle spécifique n'est pas abolie en bloc : elle encadre la gestion de fonds sociaux. L'habilitation ne permet pas de rétablir les agréments, transmissions ou délais supprimés par les dispositions législatives spéciales proposées.",
    "Coordonner notamment D. 224-11 et R. 224-5 avec L. 224-10 proposé, ainsi que les dispositions d'application des accords avec L. 224-5-1. D. 224-7 3° vise l'avis sur les accords locaux et ne relève pas de la dispense nationale. Aucun contrôle des comptes, quorum ou recours autonome n'est retiré par cette habilitation."
)

put('L224-7', [
    "Le personnel des caisses nationales de l'assurance maladie, des allocations familiales, d'assurance vieillesse et de solidarité pour l'autonomie, ainsi que de l'Agence centrale des organismes de sécurité sociale, comprend :",
    "1° Des agents régis par le statut général de la fonction publique ;",
    "2° Des agents soumis à un statut de droit public fixé par décret ;",
    "3° Des agents de droit privé régis par les conventions collectives applicables au personnel des organismes de sécurité sociale.",
    "Les activités et les personnels des échelons locaux et régionaux du service du contrôle médical du régime général restent régis, pour les périodes antérieures à leur transfert aux caisses locales et au plus tard jusqu'au 31 décembre 2025, par les dispositions antérieurement applicables. Les droits et les litiges afférents à ces périodes conservent ce régime."
],
    "Réécriture à droit constant de la liste des trois catégories de personnel. Cette distinction protège les statuts et les conventions applicables ; sa suppression créerait une incertitude sur les droits des agents, sans supprimer une formalité redondante.",
    "La réforme du contrat unique concerne les nouveaux contrats de droit privé dans son champ, sans transformer les agents publics des 1° et 2°. La source est en vigueur depuis le 1er octobre 2025 ; sa note maintient jusqu'au transfert, au plus tard le 31 décembre 2025, le régime antérieur des personnels locaux et régionaux du contrôle médical. Cette transition passée n'est ni prolongée ni utilisée comme date de la réforme future ; les droits et litiges afférents à cette période restent à leur régime. Aucun terme de mandat ou de formation n'est assimilé ici à un terme de contrat."
)

put('L224-8', [
    "Les agents des organismes de sécurité sociale nommés dans un emploi soumis à un statut de droit public ou, le cas échéant, de droit privé au sein d'un organisme mentionné au premier alinéa de l'article L. 224-7 peuvent choisir de rester rattachés au régime de la convention collective qui leur est applicable. Ils exercent cette option dans les conditions et limites fixées par un décret en Conseil d'État."
],
    "Réécriture à droit constant de l'option de maintien du rattachement conventionnel. Il s'agit d'une faculté favorable, conservée pour les nominations futures ; aucune autorisation nouvelle ni extinction du choix ne sont introduites. Le décret garde l'articulation nécessaire entre ce maintien et le statut du nouvel emploi.",
    "Le premier alinéa de L. 224-7 identifie les organismes nationaux et l'agence ; ses 1° à 3° distinguent les statuts. L'option ne convertit pas automatiquement un emploi public en contrat privé et ne remet pas à zéro l'ancienneté ni les droits conventionnels conservés. Les dispositions réglementaires d'exercice ne sont pas réputées abrogées par la réforme du contrat unique."
)

put('L224-9', [
    "Les articles L. 231-5 et L. 281-3 s'appliquent au conseil de la Caisse nationale de l'assurance maladie, au conseil de la Caisse nationale de solidarité pour l'autonomie et aux conseils d'administration de la Caisse nationale des allocations familiales, de la Caisse nationale d'assurance vieillesse et de l'Agence centrale des organismes de sécurité sociale, ainsi qu'aux membres de ces conseils d'administration."
],
    "Réécriture à droit constant du champ des contrôles et des incapacités consécutives aux révocations ou dissolutions. Ces règles répondent à une fonction de protection contre les irrégularités graves et la mauvaise gestion des fonds sociaux ; elles ne sont pas des autorisations ordinaires d'activité à supprimer.",
    "L. 231-5 et L. 281-3 ont été lus : le premier prévoit une impossibilité de nouvelle désignation pendant quatre ans après révocation ou dissolution, le second la suspension, la dissolution, l'administration provisoire et la révocation après avis. Le texte conserve la désignation exacte des membres des « conseils d'administration » au dernier membre de phrase ; il n'étend pas silencieusement cette dernière formule à tous les membres de conseils. L'articulation du champ personnel des membres des conseils CNAM et CNSA mérite une coordination expresse si une extension est voulue. La note d'entrée en vigueur du 14 mai 2022 ne date pas la réforme proposée."
)

put('L224-10', [
    "Les délibérations du conseil et de la commission des accidents du travail et des maladies professionnelles de la Caisse nationale de l'assurance maladie, du conseil de la Caisse nationale de solidarité pour l'autonomie, des conseils d'administration de la Caisse nationale des allocations familiales, de la Caisse nationale d'assurance vieillesse et de l'Agence centrale des organismes de sécurité sociale, ainsi que du conseil d'orientation et du comité exécutif des directeurs de l'Union des caisses nationales de sécurité sociale, sont exécutoires dès leur adoption, sous réserve des règles de publication ou de notification qui leur sont applicables. Restent soumises à leur régime propre les délibérations pour lesquelles une disposition législative ou réglementaire spéciale exige une approbation et les accords relevant du droit d'opposition prévu à l'article L. 224-5-1. Le seul rattachement à la tutelle prévue par le présent article ne constitue pas une exigence spéciale d'approbation.",
    "Les décisions de ces conseils, conseils d'administration, conseil d'orientation ou comité exécutif prises en application des conventions d'objectifs et de gestion, y compris celles relatives aux budgets de ces organismes, sont exécutoires dans les conditions du premier alinéa, sans attendre l'expiration d'un délai de vingt jours ni l'absence d'opposition ministérielle. Elles demeurent transmises aux ministres chargés de la sécurité sociale et du budget ainsi que, pour le conseil de la Caisse nationale de solidarité pour l'autonomie, au ministre chargé des personnes âgées et des personnes handicapées. Les contrôles et recours prévus par les autres dispositions applicables demeurent exercés dans leur champ.",
    "Si la convention n'est pas signée avant le 1er janvier de la première année de sa mise en œuvre, le premier alinéa reste applicable.",
    "Ces règles s'appliquent aux délibérations adoptées à compter de l'entrée en vigueur de la loi qui les institue. Les délibérations antérieures, les oppositions déjà formées et leurs recours demeurent régis par les règles antérieures. La transmission aux autorités de contrôle reste obligatoire dans les conditions applicables ; elle ne conditionne plus l'exécution des délibérations relevant du régime général du présent article."
],
    "Réforme de fond : suppression de l'attente générale d'une non-opposition de l'État et du délai suspensif de vingt jours pour les décisions prises dans le cadre des conventions d'objectifs et de gestion. La tutelle ne bloque plus par principe l'exécution. Les approbations spéciales, la transmission, la publicité, les recours et l'opposition paritaire aux accords UCANSS conservent leur fonction propre.",
    "Coordonner R. 224-5 et R. 225-5 : leur visa d'urgence pour l'exécution immédiate devient sans objet dans ce nouveau champ, mais les envois des procès-verbaux sous dix jours restent distincts et maintenus. R. 225-5 renvoie en outre à L. 226-4 : ce renvoi ancien est signalé, sans concordance inventée. D. 224-11 ne peut rétablir une approbation générale par son seul renvoi au présent article. Les approbations ayant un fondement spécial autonome restent requises. L. 224-5-1 est une cible ajoutée, dont la source entière et la proposition figurent dans le présent lot, et non un nouveau renvoi de contrat privé. La condition du 1er janvier reste au troisième alinéa. Les contrôles graves de L. 281-3 sont maintenus ; aucune économie chiffrée n'est présumée.",
    removed=[
        "Le caractère suspensif du délai général d'opposition des autorités de l'État avant l'exécution des délibérations non soumises à une approbation spéciale.",
        "Le délai obligatoire de vingt jours après réception ministérielle et le pouvoir d'opposition préalable fondé sur ce régime pour les décisions prises en application des conventions d'objectifs et de gestion."
    ]
)

put('L224-11', [
    "Les organismes nationaux peuvent prescrire aux organismes de base mentionnés au titre Ier du livre II les mesures nécessaires et proportionnées pour faire respecter l'article L. 224-13, pour remédier à des irrégularités ou pour corriger des défaillances de gestion qui compromettent la continuité du service ou l'équilibre financier de l'organisme. La seule recherche d'une amélioration d'opportunité de la gestion ne suffit pas à fonder une prescription obligatoire. Si ces prescriptions ne sont pas suivies, l'organisme national peut mettre en demeure l'organisme de base de prendre, dans un délai déterminé, les mesures de redressement utiles. En cas de carence, il peut se substituer à cet organisme et ordonner les mesures nécessaires au rétablissement de sa situation dans les limites précédemment définies.",
    "Cette limitation s'applique aux prescriptions, mises en demeure et décisions de substitution prises à compter de l'entrée en vigueur de la loi qui l'institue. Les décisions antérieures et leurs recours conservent leur régime."
],
    "Réforme de fond : retrait du pouvoir d'imposer toute mesure de simple amélioration de gestion sans manquement ni risque pour le service ou les finances. La direction nationale conserve les moyens de faire respecter L. 224-13 et de redresser une défaillance réelle, avec mise en demeure puis substitution en cas de carence.",
    "Le seuil de nécessité limite un pouvoir existant ; il ne crée pas un agrément local ni une déclaration de performance. Le respect des financements, budgets et systèmes d'information de L. 224-13 reste un fondement autonome de prescription. Le délai fixé dans la mise en demeure n'est pas assimilé au préavis d'un contrat de travail. Les pouvoirs distincts de contrôle et de sanction, ainsi que les recours, demeurent à leur champ propre.",
    removed=["Le pouvoir de prescrire obligatoirement toute mesure d'amélioration de la gestion sur un simple motif d'opportunité, sans manquement ni défaillance compromettant le service ou l'équilibre financier."]
)

put('L224-12', [
    "Les caisses nationales, l'Agence centrale des organismes de sécurité sociale et l'Union des caisses nationales de sécurité sociale peuvent conclure des marchés ou des accords-cadres pour leur propre compte, pour celui des organismes locaux et pour celui des agences régionales de santé. Les marchés subséquents à ces accords-cadres sont conclus par les caisses nationales, l'agence centrale, les organismes locaux ou les agences régionales de santé."
],
    "Réécriture à droit constant de la faculté d'achat mutualisé et de la désignation des organismes habilités à conclure les marchés subséquents. Cette souplesse est maintenue pour les achats futurs ; l'article n'impose ni achat centralisé ni autorisation préalable supplémentaire.",
    "La faculté d'agir pour le compte des agences régionales de santé et des organismes locaux demeure intégrale. Le texte ne modifie pas les règles autonomes de passation de la commande publique ni les contrats déjà conclus. Articuler avec la spécialité bancaire de L. 225-1-1 8° et les missions de centrale d'achat de L. 224-5, sans rendre obligatoire une procédure mutualisée."
)

put('L224-13', [
    "Les caisses nationales et l'Agence centrale des organismes de sécurité sociale financent les dépenses budgétaires prévues aux articles L. 225-6, L. 251-1, L. 251-6 et L. 251-8. Elles répartissent les dotations nécessaires à ce financement. Elles approuvent les budgets établis à cette fin par les organismes mentionnés au titre Ier du livre II, dans les conditions prévues à l'article L. 153-2. Elles établissent et mettent en œuvre des schémas directeurs informatiques pour coordonner les branches qu'elles gèrent ou l'organisation des organismes de recouvrement. Elles contrôlent la compatibilité de l'informatique locale avec ces schémas."
],
    "Réécriture à droit constant des responsabilités de financement, de répartition des dotations, d'approbation budgétaire et de coordination informatique. Ces contrôles protègent les fonds affectés et l'interopérabilité des réseaux ; aucune approbation locale supplémentaire ou demande de justificatif n'est créée.",
    "L. 225-6 et L. 153-2 ont été lus : financement des charges de gestion et approbation des budgets de base, avec réserve de la compétence tarifaire de l'État. Les articles L. 251-1, L. 251-6 et L. 251-8 ne sont pas présents dans le corpus public fourni, qui contient L. 251-6-1 mais pas ces trois cibles ; leur maintien dans la source révèle une concordance à documenter, sans substitution silencieuse. Aucun nouveau renvoi n'est inventé. L'approbation des budgets locaux fondée spécialement sur L. 153-2 reste distincte de l'attente générale de tutelle supprimée dans L. 224-10. Le contrôle de compatibilité informatique n'est pas transformé en agrément de chaque achat."
)

put('L224-14', [
    "Les caisses nationales mentionnées aux articles L. 221-2, L. 222-4, L. 223-2 et L. 223-6 mettent en œuvre ou coordonnent des contrôles du service des prestations destinés à détecter les fraudes et les comportements abusifs. Elles peuvent utiliser à cette fin des traitements automatisés de données relatives au service des prestations, dans le respect des règles de protection des données et des garanties applicables aux personnes contrôlées.",
    "Elles peuvent requérir la participation de leurs organismes régionaux et locaux à ces contrôles.",
    "Pour la même vérification, elles réutilisent les informations et pièces exactes et à jour auxquelles elles ont déjà légalement accès et n'en exigent pas une nouvelle déclaration ou production. Cette dispense ne fait obstacle ni à la recherche d'une fraude, ni à une demande portant sur des éléments manquants, modifiés ou contradictoires. Elle ne crée aucun droit d'accès supplémentaire et respecte les secrets protégés et le contradictoire.",
    "La dispense de nouvelle déclaration ou production s'applique aux demandes effectuées à compter de l'entrée en vigueur de la loi qui l'institue, y compris dans les contrôles en cours. Elle ne modifie ni les conditions de droit aux prestations, ni les exonérations ou dispenses, ni les voies de recours."
],
    "Réforme de fond : suppression des déclarations ou pièces demandées une seconde fois alors que les informations exactes sont déjà légalement accessibles pour la même vérification. La coordination des contrôles et la lutte contre les fraudes sont maintenues, avec les garanties relatives aux données et au contradictoire ; aucun contrôle automatisé nouveau n'est rendu obligatoire.",
    "Le renvoi à L. 223-6 désigne la CNSA comme établissement public ; sa règle propre de protection des salariés mandatés n'est pas une condition de contrôle des prestations. La faculté de traitement automatisé ne dispense pas des règles de protection des données ni d'un examen humain lorsqu'il est légalement requis. Les dispenses et droits aux prestations restent ouverts aux situations futures. Ne pas confondre les contrôles des prestations de cet article avec l'inspection de gestion de L. 224-4, dont la dispense documentaire a le même champ limité.",
    removed=["Les nouvelles déclarations ou productions de pièces déjà légalement accessibles, exactes et suffisantes pour la même vérification du service des prestations."]
)

put('L225-1', [
    "L'Agence centrale des organismes de sécurité sociale assure la gestion commune de la trésorerie des branches gérées par la Caisse nationale des allocations familiales, la Caisse nationale de l'assurance maladie, la Caisse nationale de solidarité pour l'autonomie et la Caisse nationale d'assurance vieillesse. Un décret pris sur le rapport des ministres intéressés fixe les conditions de cette gestion.",
    "L'agence individualise la trésorerie de chaque branche du régime général au moyen d'un suivi permanent en prévision et en réalisation comptable. Elle établit un état prévisionnel de la trésorerie de chaque branche.",
    "Un décret détermine les modalités d'application du présent article et les conditions de placement des excédents de trésorerie constatés globalement pour l'ensemble des branches mentionnées au premier alinéa."
],
    "Réécriture à droit constant : la gestion commune est distinguée du suivi individuel des branches. Les prévisions et la traçabilité comptable sont conservées pour garantir le paiement des prestations et l'affectation des fonds. Les supprimer ne constituerait pas une réduction justifiée de formalités imposées aux cotisants.",
    "Les quatre caisses, la constatation globale des excédents et l'état prévisionnel de chaque branche sont maintenus. D. 225-1, D. 225-2 et D. 225-3 ont été lus pour contrôler les circuits de trésorerie : la mutualisation n'autorise pas la confusion des comptes ni des soldes débiteurs interdits. La transition retraite ne peut prélever sur cette trésorerie un financement supposé disponible ; aucune ressource ou économie nouvelle n'est créée. La note du 1er janvier 2021 reste une donnée historique."
)

put('L225-1-1', [
    "L'Agence centrale des organismes de sécurité sociale est également chargée :",
    "1° De diriger et de contrôler les unions de recouvrement en matière de gestion de trésorerie ;",
    "2° De définir ses orientations de contrôle et de recouvrement des cotisations et contributions de sécurité sociale pour les travailleurs salariés et non salariés, ainsi que d'en coordonner et d'en vérifier l'application par les organismes locaux ;",
    "3° (Abrogé) ;",
    "3° bis D'assurer une application homogène des lois et règlements relatifs aux cotisations et contributions de sécurité sociale recouvrées par les organismes mentionnés aux articles L. 213-1 et L. 752-4 ;",
    "3° ter (Abrogé) ;",
    "3° quater D'harmoniser les positions prises par les organismes de recouvrement en application de l'article L. 243-6-1 ;",
    "3° quinquies D'engager et de coordonner des actions concertées de contrôle et de recouvrement menées par les organismes de recouvrement. Elle peut requérir leur participation à ces actions ;",
    "4° De recevoir, sauf disposition contraire, le produit des cotisations et contributions recouvrées par des tiers. Un décret en Conseil d'État fixe les garanties et sanctions applicables ; celles-ci ne s'appliquent pas à l'État ;",
    "5° De centraliser l'ensemble des sommes recouvrées par les organismes mentionnés aux articles L. 213-1 et L. 752-4.",
    "L'agence notifie et verse à chaque attributaire les sommes recouvrées qui lui reviennent.",
    "Par dérogation au deuxième alinéa du présent 5°, le versement correspond aux sommes dues par les redevables après application d'un taux forfaitaire fixé au regard du risque de non-recouvrement d'une partie de ces sommes :",
    "a) Pour les cotisations et contributions sociales mentionnées au 1° du I de l'article L. 213-1, à l'exception de celles qui sont affectées aux branches du régime général mentionnées à l'article L. 200-2 et de celles qui sont dues par les personnes relevant du régime spécial de sécurité sociale des marins ;",
    "b) Pour les versements mentionnés aux articles L. 2333-64 et L. 2531-2 du code général des collectivités territoriales ;",
    "c) Pour les cotisations mentionnées au 6° du I de l'article L. 213-1 du présent code, à l'exception de celle prévue à l'article L. 6331-48 du code du travail ;",
    "d) Pour la cotisation obligatoire et le prélèvement supplémentaire obligatoire mentionnés au 1° de l'article 12-2 de la loi n° 84-53 du 26 janvier 1984 portant dispositions statutaires relatives à la fonction publique territoriale, ainsi que pour la majoration mentionnée à l'article 12-2-1 de cette loi ;",
    "e) Pour la contribution mentionnée au 1° du I et, le cas échéant, pour celle mentionnée au III de l'article L. 2135-10 du code du travail ;",
    "f) Pour les cotisations ou contributions autres que celles d'origine légale ou conventionnelle prévues par la loi, mentionnées au 1° de l'article L. 133-5-7 du présent code.",
    "Le taux mentionné au troisième alinéa du présent 5° est fixé par attributaire ou catégorie d'attributaires, dans les conditions fixées par décret en Conseil d'État, par arrêté des ministres chargés de la sécurité sociale et du budget. Pour les cotisations ou contributions dont le recouvrement est transféré aux organismes mentionnés aux articles L. 213-1 et L. 752-4 du présent code à compter du 1er janvier 2020, il ne peut dépasser le taux moyen de non-recouvrement observé l'année précédant le transfert de compétence.",
    "Sans préjudice des troisième à dixième alinéas du présent 5°, l'agence applique aux sommes recouvrées par les organismes mentionnés aux articles L. 213-1 et L. 752-4 des frais de gestion déterminés dans les conditions prévues par décret en Conseil d'État.",
    "Un décret en Conseil d'État définit les modalités de mise à disposition des attributaires des informations nécessaires à l'exercice de leurs missions.",
    "5° bis De recevoir, pour le compte des régimes et fonds concernés, le produit global des impôts et taxes mentionnés à l'article L. 131-8 et de le répartir entre eux en application de cet article ;",
    "6° De contrôler les opérations immobilières des unions de recouvrement et la gestion de leur patrimoine immobilier ;",
    "7° De compenser la perte de cotisations sociales effectivement recouvrées qui résulte, pour les régimes mentionnés à l'article L. 921-4 du présent code et à l'article L. 6527-1 du code des transports, de la réduction dégressive prévue à l'article L. 241-13 du présent code. Cette compensation porte sur les cotisations dues à ces régimes par les employeurs relevant des organismes mentionnés aux articles L. 213-1 et L. 752-1, des organismes de recouvrement mentionnés à l'article L. 723-1 du code rural et de la pêche maritime et de ceux mentionnés à l'article L. 6527-2 du code des transports ;",
    "7° bis De compenser, dans la limite d'un montant fixé par arrêté des ministres chargés du travail, de la sécurité sociale et du budget, la perte de cotisations qui résulte, pour l'organisme mentionné au premier alinéa de l'article L. 5427-1 du code du travail, de la réduction dégressive prévue à l'article L. 241-13 du présent code. Cette compensation porte sur les cotisations dues à cet organisme par les employeurs relevant des organismes de recouvrement mentionnés aux articles L. 133-9, L. 213-1 et L. 752-1 du présent code, ainsi qu'aux a à f de l'article L. 5427-1 du code du travail. La différence entre cette perte de cotisations et le montant limite est déduite des sommes auxquelles s'applique le taux forfaitaire prévu au troisième alinéa du 5° du présent article ;",
    "8° D'exercer, pour les marchés publics de services bancaires, la fonction de centrale d'achat au sens du droit de la commande publique pour le compte des caisses nationales et des organismes locaux du régime général.",
    "Les organismes de recouvrement peuvent porter leurs litiges devant la Cour de cassation sans autorisation préalable de l'agence. Les règles de compétence, de représentation et de procédure juridictionnelle demeurent applicables. La suppression de cette autorisation s'applique aux recours formés à compter de l'entrée en vigueur de la loi qui la supprime, y compris dans les litiges en cours, sans rouvrir un délai de recours expiré.",
    "Les missions de centralisation, de versement et de compensation du présent article ne créent ni ne rétablissent une cotisation, une contribution ou une taxe supprimée. La contribution dédiée au financement du compte personnel de formation des titulaires d'un contrat à durée déterminée, comprise dans le renvoi du c du 5° au 6° du I de l'article L. 213-1, n'est plus due au titre des rémunérations correspondant aux périodes de travail courant à compter de l'entrée en vigueur de la loi instituant le contrat unique à durée indéterminée, même pour un contrat conclu auparavant. Les exclusions, exonérations, créances, régularisations, restitutions, prescriptions et recours des périodes antérieures restent régis par les règles alors applicables. Aucune contribution équivalente n'est due du seul fait d'un contrat unique, d'une mission ou d'une formation.",
    "Les compensations prévues aux 7° et 7° bis continuent de s'appliquer aux réductions légalement ouvertes pour les situations futures éligibles dans le contrat unique, dans les champs et limites de ces deux subdivisions. La durée d'une mission, d'une affectation ou d'une formation n'est pas un terme du contrat de travail. Les droits et les opérations afférents aux périodes antérieures demeurent régis par leurs règles propres."
],
    "Réforme de fond : suppression de l'autorisation centrale de pourvoi en cassation, sans formalité de remplacement, et coordination expresse de la disparition de la contribution CPF-CDD pour les rémunérations futures. Réécriture complète des missions et des six catégories du 5°. Les règles de reversement, de mutualisation du risque et de compensation des allègements sont conservées ; il ne s'agit pas d'impôts supplémentaires sur les redevables. Les frais de gestion financent une prestation de recouvrement identifiable et restent soumis aux exemptions réglementaires, sans taux nouveau.",
    "Les douze alinéas du 5° sont maintenus dans leur ordre : centralisation, notification, dérogation, a à f, plafond du taux, frais, informations. Les renvois aux troisième à dixième alinéas et celui du 7° bis au troisième restent donc cohérents. R. 225-1, R. 225-2, R. 225-2-1 et R. 225-2-2 ont été lus : préserver les dérogations de reversement en cas de reports autorisés, les exemptions de frais, les données protégées et les conventions financières autonomes. Les repères (1) de la source ne sont accompagnés d'aucune note (1) fournie : omission de ces seuls appels éditoriaux, sans modifier la règle du taux. Le renvoi ancien à l'article 26 de l'ordonnance de 2015 est remplacé par le droit de la commande publique sans numéro de concordance inventé ; les références de fonction publique territoriale de 1984 restent à coordonner avec la codification applicable. Les renvois différents à L. 752-4 au 5° et à L. 752-1 aux 7° et 7° bis sont conservés, sans les assimiler. Coordonner toute règle réglementaire ou instruction exigeant l'autorisation de cassation ; aucun texte précis non fourni n'est réputé réécrit. L. 241-13 proposé préserve des calculs plus favorables pour les affectations temporaires futures, sans CDD : la compensation les suit dans son champ sans montant inventé. Le 5° bis ne crée aucune recette de remplacement et applique les affectations temporelles de L. 131-8. Les contributions distinctes citées ne sont pas abolies par leur seul renvoi ; la C3S garde sa transition financée décidée séparément.",
    removed=[
        "L'autorisation préalable de l'Agence centrale exigée des organismes de recouvrement pour porter leurs litiges devant la Cour de cassation.",
        "L'exigibilité et la centralisation de la contribution CPF-CDD au titre des rémunérations des périodes de travail postérieures à l'entrée en vigueur du contrat unique, sans contribution de remplacement."
    ],
    benefit="La dispense de garanties et de sanctions pour l'État au 4° est conservée. Au 5°, les exclusions des branches du régime général, des marins et de la cotisation de L. 6331-48 restent intégrales ; le plafond lié au taux moyen de non-recouvrement de l'année précédant les transferts à compter du 1er janvier 2020 subsiste. Les exemptions réglementaires de frais de gestion de R. 225-2 et les modalités favorables de reversement lors de reports autorisés de R. 225-1 ne sont pas fermées. Les 7° et 7° bis conservent les compensations des réductions de cotisations, leur champ interrégimes, leur limite et la déduction du différentiel ; les réductions et calculs favorables de L. 241-13 restent accessibles aux futures situations éligibles dans le contrat unique sans nouveau CDD. La fonction de centrale d'achat du 8° reste ouverte. Les exonérations et restitutions CPF-CDD des périodes anciennes sont protégées ; pour les périodes nouvelles, la contribution entière disparaît, sans impôt équivalent. Les règles d'affectation du 5° bis n'étendent aucune assiette ni ne suppriment un avantage attaché à un impôt distinct."
)

put('L225-1-2', [
    "Lorsque la Caisse nationale d'assurance vieillesse conclut la convention financière prévue à l'article L. 222-6, l'Agence centrale des organismes de sécurité sociale peut conclure parallèlement une convention financière avec la personne morale chargée de la gestion du risque vieillesse du régime spécial. Les trois personnes morales peuvent toutefois réunir les stipulations de ces conventions dans une convention financière commune, signée par chacune d'elles.",
    "L'application du premier alinéa de l'article L. 222-6 reste subordonnée à la conclusion de la convention de l'agence ou, lorsqu'une convention commune est retenue, à sa signature par les trois parties. Dans ce dernier cas, aucune convention parallèle distincte n'est exigée.",
    "La convention de l'agence est soumise à l'approbation des ministres de tutelle des régimes de sécurité sociale concernés. Lorsque la convention est commune, une seule approbation par ces ministres vaut pour l'ensemble de ses stipulations, y compris celles relevant de l'article L. 222-6. Les exigences d'information préalable du Parlement prévues à cet article demeurent applicables.",
    "La faculté de convention commune s'applique aux conventions conclues à compter de l'entrée en vigueur de la loi qui l'institue, y compris aux négociations en cours. Les conventions déjà conclues et les droits qui en résultent demeurent applicables ; leur réunion ne peut intervenir que par accord des parties dans le respect des contrôles maintenus."
],
    "Réforme de fond : possibilité de remplacer les deux conventions financières parallèles d'un adossement par un acte commun tripartite et une approbation unique couvrant les deux volets. Les signatures, les stipulations financières, l'approbation des ministres des régimes concernés et l'information du Parlement sont maintenues, car l'opération engage des risques interrégimes durables.",
    "L. 222-6 a été lu intégralement dans le corpus : il vise les régimes spéciaux existant avant le 6 octobre 1945 et la partie équivalente aux prestations du régime général, avec information parlementaire avant signature. Ces limites ne sont pas étendues par la convention commune. Le présent texte écarte expressément la nécessité d'un second instrument prévue par son deuxième alinéa, sans supprimer la participation de l'agence ni l'approbation de fond ; coordonner la rédaction de L. 222-6 et les modèles réglementaires pour éviter une seconde signature ou approbation du même accord. Aucun financement ni équilibre actuariel n'est supposé acquis.",
    removed=[
        "L'exigence de deux instruments financiers parallèles distincts lorsque la CNAV, l'Agence centrale et le régime spécial signent une convention commune couvrant les deux volets.",
        "La répétition de l'approbation ministérielle pour chacun des deux volets réunis dans la même convention financière tripartite."
    ]
)

put('L225-1-3', [
    "Les régimes obligatoires de base autres que le régime général et les organismes et fonds mentionnés au 6° de l'article LO 111-4-1 peuvent déposer auprès de l'Agence centrale des organismes de sécurité sociale tout ou partie de leurs disponibilités, contre rémunération.",
    "Une convention fixe les modalités du dépôt. Elle n'est pas soumise à l'approbation des ministres de tutelle de l'agence, du régime, de l'organisme ou du fonds concerné, y compris lorsqu'une telle approbation est prévue par une disposition réglementaire pour cette même convention. Les contrôles budgétaires et comptables et les règles de sécurité des fonds demeurent applicables.",
    "Un décret en Conseil d'État précise les conditions d'application du présent article, sans rétablir une autorisation de dépôt, un agrément de la convention ou une déclaration équivalente.",
    "La suppression de l'approbation s'applique aux conventions conclues à compter de l'entrée en vigueur de la loi qui la prévoit. Les conventions signées auparavant et encore en attente d'approbation peuvent être exécutées dès cette entrée en vigueur si leurs autres conditions sont remplies, sans nouveau dépôt de dossier. Les stipulations de rémunération, les créances et les droits résultant des conventions antérieures sont préservés."
],
    "Réforme de fond : suppression de l'approbation ministérielle individuelle des conventions de dépôt de disponibilités. La convention et la rémunération du déposant sont maintenues, ainsi que les règles prudentielles et comptables ; aucune déclaration de remplacement n'est créée.",
    "Le champ source des régimes de base autres que le régime général et des organismes et fonds visés est conservé. Incohérence préexistante : dans le corpus fourni, le 6° de LO 111-4-1 traite de la situation financière des établissements de santé et médico-sociaux, et ne désigne pas une liste d'organismes et fonds pouvant déposer leurs disponibilités. Ce renvoi exige une concordance historique expresse ; il est conservé sans extension aux établissements ni substitution conjecturale d'un autre numéro. Coordonner D. 225-2, quatrième alinéa, qui impose encore une approbation de la convention organisant les comptes et reversements : elle ne doit pas rétablir l'approbation supprimée pour la même convention de dépôt. Les autres conventions de reversement ayant un objet autonome ne sont pas abolies en bloc. Les interdictions de comptes débiteurs de D. 225-3 demeurent. La rémunération est conservée pour les futurs dépôts ; aucun taux ni garantie financière nouvelle ne sont inventés. Le point-virgule isolé de la source est supprimé comme défaut matériel.",
    removed=["L'approbation préalable des ministres de tutelle de chaque convention de dépôt de disponibilités auprès de l'Agence centrale, y compris son rétablissement réglementaire pour la même convention."]
)

put('L225-1-4', [
    "Dans la limite des plafonds de ressources non permanentes fixés en application du e du 2° de l'article LO 111-3-4, l'Agence centrale des organismes de sécurité sociale peut consentir, contre rémunération :",
    "1° Des prêts et avances d'une durée inférieure à douze mois au régime d'assurance vieillesse des non-salariés agricoles et au régime d'assurance vieillesse du régime spécial de sécurité sociale dans les mines ;",
    "2° Des avances d'une durée inférieure à un mois aux régimes obligatoires de base autres que le régime général et aux organismes et fonds mentionnés au 6° de l'article LO 111-4-1 ;",
    "3° Sans préjudice de ses missions prévues aux 1° et 2°, des avances d'une durée inférieure à un mois aux organismes dont elle centralise des recettes ou pour le compte desquels elle recouvre tout ou partie des cotisations et contributions. L'inscription de ces organismes sur une liste ministérielle n'est pas requise. Ces avances portent intérêt à un taux égal à la somme d'un taux interbancaire de référence, retenu s'il est positif et adapté à la durée de l'avance, et d'une marge fixe qui ne peut excéder 200 points de base. Cette marge ne peut être majorée au seul motif que plusieurs avances sont consenties au cours d'une même année civile. Un arrêté des ministres chargés de la sécurité sociale et du budget fixe les taux de référence, le niveau de la marge et l'encours maximal des avances octroyées, sans rétablir cette majoration ni une liste préalable d'organismes autorisés.",
    "Une convention conclue entre l'agence et le régime, l'organisme ou le fonds concerné détermine les conditions de chaque avance mentionnée au présent article. Cette convention n'est pas soumise à l'approbation des ministres chargés de la sécurité sociale et du budget, y compris lorsqu'une disposition réglementaire prévoit cette approbation pour la même convention. Les plafonds organiques, les limites de durée, les conditions de rémunération ainsi que les contrôles budgétaires et comptables demeurent applicables.",
    "La suppression de la liste préalable, de la majoration pour réitération et de l'approbation ministérielle s'applique aux prêts et avances consentis à compter de l'entrée en vigueur de la loi qui la prévoit, sans nouvelle déclaration ou autorisation équivalente. Les prêts et avances antérieurement consentis conservent leurs stipulations jusqu'à leur terme, leurs créances et leurs voies de recours. Une convention-cadre antérieure ne peut rétablir les exigences supprimées pour une avance nouvelle."
],
    "Réforme de fond : suppression de la liste ministérielle préalable des organismes déjà objectivement éligibles au 3°, de la majoration de marge liée à la seule réitération des avances et de l'approbation ministérielle de chaque convention. La rémunération normale du financement public, le plafond de 200 points de base, les plafonds organiques et les durées strictement inférieures à douze ou à un mois sont conservés.",
    "Les 1°, 2° et 3° restent à leur place et leurs champs ne sont pas confondus. Le plafond de 200 points de base concerne la marge du 3°, non le taux interbancaire ni les rémunérations des 1° et 2° ; la faculté de doubler la marge en cas de réitération est effectivement retirée sans nouveau taux. La liste préalable disparaît seulement pour les organismes dont l'agence centralise les recettes ou assure le recouvrement. Incohérence préexistante au 2° : le 6° de LO 111-4-1 fourni traite de la situation financière des établissements de santé et médico-sociaux, non d'une liste des organismes et fonds éligibles. Le renvoi source est conservé dans l'attente d'une concordance historique explicite, sans extension du champ par conjecture. Le e du 2° de LO 111-3-4, lu, porte bien sur les organismes habilités à recourir aux ressources non permanentes et les limites de leurs besoins de trésorerie. Coordonner l'arrêté pris au titre du 3° et toute clause d'approbation réglementaire, notamment D. 225-2 pour la même convention d'avance. Les prévisions de trésorerie de D. 225-2-2 et les contrôles de fonds publics demeurent distincts et ne constituent pas une autorisation nouvelle. Aucun plafond organique ni échéance de remboursement n'est relevé ; aucun chiffrage de gain ou de coût public n'est inventé.",
    removed=[
        "L'inscription préalable sur une liste arrêtée par les ministres pour les organismes déjà éligibles aux avances du 3° en raison des recettes centralisées ou du recouvrement effectué pour leur compte.",
        "La faculté de majorer jusqu'au double la marge fixe d'intérêt au seul motif que plusieurs avances sont consenties pendant la même année civile.",
        "L'approbation des ministres chargés de la sécurité sociale et du budget exigée pour la convention déterminant les conditions de chaque avance."
    ]
)


reference_assessments = {
    'L224-1': {
        'L1234-1': "La source ne renvoie pas au préavis de licenciement : elle organise la délégation à des commissions. Le mandat d'un membre ne constitue pas un emploi ; les quinze jours et les règles des anciens contrats sont sans effet sur cette délégation.",
        'L1221-2': "L'appartenance à une commission de caisse n'est pas une embauche ni un CDD. Aucun terme d'emploi ne résulte de ce texte ; le contrat unique des nouvelles relations privées ne modifie pas les qualités requises des membres extérieurs.",
        'L1234-9': "L'article ne prévoit ni licenciement ni indemnité et ne vise aucune ancienneté salariée. Le seuil d'un an au terme effectif, le barème de 0,20 mois et les anciens droits restent étrangers à la délégation ; aucune indemnité n'est supprimée par ce texte.",
        'L422-1': "Le renvoi désigne les comités techniques nationaux compétents en prévention des risques professionnels. Leur rôle d'étude et d'extension des mesures de prévention justifie la qualité des membres extérieurs pour les accidents du travail ; il n'ouvre aucun régime de rupture privée."
    },
    'L224-5': {
        'L1234-1': "Les missions de ressources humaines de l'union ne fixent aucun préavis. Pour les salariés effectivement soumis au nouveau contrat privé, le préavis individuel est de quinze jours avec notification écrite selon les règles coordonnées ; les procédures collectives et protections ne sont pas supprimées.",
        'L1221-2': "Les politiques de recrutement et de formation ne peuvent ouvrir un nouveau CDD. Les futures embauches privées relevant du code du travail sont à durée indéterminée ; la fin d'une formation ou mission ne termine pas l'emploi, tandis que les agents publics restent à leur statut.",
        'L1234-9': "Les conventions négociées ne modifient pas ici la règle proposée : indemnité ordinaire patronale à partir d'un an mesuré au terme effectif, préavis exécuté ou non inclus, calculée sur toute l'ancienneté à 0,20 mois par année, fractions au prorata des mois complets, plafond légal de six mois. La cible réserve la faute grave, les indemnités plus favorables, les droits antérieurs et les indemnités spéciales ; aucune compétence d'agrément ne peut les effacer.",
        'L224-5-1': "Le nouveau renvoi vise le conseil d'orientation : il arrête le programme de négociation et peut s'opposer aux accords nationaux aux trois quarts de ses membres désignés. La vue fournie contient encore l'agrément ministériel ; la proposition de ce lot le supprime, avec une transition des demandes en cours, sans retirer les majorités, le consentement ni les droits conventionnels futurs.",
        'L225-1-1': "Le renvoi au seul 8° réserve la centrale d'achat des services bancaires à l'Agence centrale. Il ne vise ni les cotisations ni un contrat d'emploi ; la rédaction intégrale de ce lot maintient ce 8° et sa séparation avec les autres achats facultativement mutualisés par l'union."
    },
    'L224-5-1': {
        'L1234-1': "La nomination du directeur par le conseil ne fixe pas son préavis de salarié et ne convertit pas un mandat en contrat de travail. Le préavis de quinze jours n'est applicable qu'aux nouvelles relations privées de son champ ; aucun préavis de contrat ancien ou statut public n'est effacé ici.",
        'L1221-2': "Les mandats du conseil et la nomination des dirigeants ne constituent pas des cas de CDD. Les accords nationaux privés futurs doivent respecter le contrat unique sans fin automatique par mission ou formation ; leur dispense d'agrément ne constitue pas une dérogation permettant un nouveau CDD.",
        'L1234-9': "La compétence de nomination ne règle pas une indemnité de rupture. La suppression de l'agrément n'abolit ni les minima et droits antérieurs ni les indemnités spéciales ; pour le nouveau contrat, le seuil d'un an s'apprécie au terme, préavis inclus, et le calcul comprend la première année entière."
    },
    'L224-5-2': {
        'L1234-1': "Le mandat donné au directeur pour négocier et conclure un accord n'est pas la notification de rupture d'un contrat. La consultation institutionnelle annuelle et les protections collectives restent distinctes des quinze jours de préavis individuel et des anciens préavis conservés.",
        'L1221-2': "Ni le mandat de négociation ni la durée d'un projet institutionnel ne fixe un terme d'emploi. L'instance de concertation reste compétente pour les futurs contrats privés à durée indéterminée, sans que le comité puisse réintroduire un CDD par un programme de recrutement.",
        'L1234-9': "Le 2° porte sur une proposition de nomination, non sur l'indemnisation d'un licenciement. Aucune condition d'ancienneté ni exclusion d'indemnité n'en résulte ; le nouveau seuil au terme avec préavis et les règles antérieures ou spéciales continuent de relever de leurs textes propres.",
        'L224-5-1': "Les 1°, 2° et 3° distribuent les compétences avec le conseil d'orientation : celui-ci approuve le budget, nomme les dirigeants et arrête le programme. La proposition de ce lot préserve cette répartition et le veto aux trois quarts, tout en supprimant l'agrément ministériel national."
    },
    'L224-10': {
        'L1234-1': "L'exécution des délibérations de tutelle n'est pas le préavis de rupture d'un salarié. La suppression du délai de vingt jours et de l'opposition ministérielle générale ne dispense ni de la notification écrite de la rupture privée ni des quinze jours calendaires courant le lendemain de sa présentation ou réception dans le nouveau régime ; les anciens contrats et autorisations collectives ou spéciales gardent leur champ.",
        'L1221-2': "La délibération exécutoire dès son adoption ne permet aucune embauche nouvelle à durée déterminée. Le renvoi au conseil d'orientation concerne le contrôle des accords, sans créer un cas de CDD ni faire de la durée d'une convention d'objectifs le terme d'un emploi. Les relations privées nouvelles restent à durée indéterminée ; les statuts publics et contrats antérieurs ne sont pas convertis par cette règle de tutelle.",
        'L1234-9': "Ni la délibération budgétaire ni son exécution immédiate ne constituent un licenciement et ne règlent l'indemnité ordinaire. La proposition cible mesure le seuil d'un an au terme effectif, préavis inclus, puis calcule 0,20 mois sur l'ancienneté totale avec fractions en mois complets et plafond de six mois, sous ses exceptions. L'article de tutelle n'efface pas les composantes antérieures, minima plus favorables ou indemnités spéciales.",
        'L224-5-1': "Le renvoi réserve expressément le droit d'opposition du conseil d'orientation aux accords UCANSS, distinct de l'opposition générale de l'État supprimée ici. La vue fournie est la source officielle avec agrément ; la proposition du lot maintient le veto aux trois quarts pendant un mois, avec exécution anticipée seulement sur non-opposition expresse du conseil. Les conditions de validité et la date d'effet de l'accord subsistent."
    },
    'L224-14': {
        'L1234-1': "Les contrôles du service des prestations ne sont pas des licenciements. Le texte ne comporte pas de renvoi au préavis ; la suppression des productions documentaires répétées n'écarte aucune notification ni procédure collective relative à l'emploi des agents contrôleurs.",
        'L1221-2': "La participation des organismes régionaux et locaux aux contrôles n'est ni une embauche ni une mission mettant fin à l'emploi. Le contrat unique s'applique dans son propre champ privé ; la compétence de contrôle des prestations et les statuts publics demeurent distincts.",
        'L1234-9': "Aucune indemnité de rupture n'est prévue dans ce contrôle des prestations. Ni le seuil d'un an, mesuré au terme préavis compris, ni le barème patronal ni leurs exceptions ne constituent une condition d'accès aux prestations ou de dispense de pièces ; les assimiler serait erroné.",
        'L223-6': "Le renvoi identifie la CNSA, établissement public national administratif, comme caisse chargée des contrôles. Le second alinéa de L. 223-6 maintient la protection des salariés mandatés et l'avis du CSE prévu à L. 2421-3 ; le contrôle des prestations ne retire pas ces garanties distinctes."
    },
    'L225-1-1': {
        'L1234-1': "Les missions de recouvrement ne déterminent pas le préavis des salariés ni la date de rupture. Le nouveau préavis individuel de quinze jours dépend de sa notification et de son champ ; il ne supprime pas les procédures collectives ni les autorisations des salariés protégés ou les anciens droits.",
        'L1221-2': "Le renvoi du c du 5° à la formation professionnelle ne permet aucun nouveau CDD. La contribution CPF-CDD disparaît pour les périodes de travail futures, y compris sous ancien contrat ; missions et formations peuvent rester temporaires sans terme d'emploi ni contribution équivalente sur le contrat unique.",
        'L1234-9': "La compensation des réductions n'est pas une indemnité de licenciement. La cible prévoit zéro indemnité ordinaire avant un an au terme effectif, préavis inclus, puis 0,20 mois par année totale, fractions au prorata des mois complets et plafond légal de six mois, sous sa réserve de faute grave. Salaires, congés, réparations d'illégalité, indemnités plus favorables, composantes anciennes et indemnités spéciales ne sont pas effacés par la centralisation sociale.",
        'L133-9': "Le 7° bis inclut le recouvrement des employeurs de spectacles via l'organisme habilité. La cible maintient la voie postale ou télécopie pour les personnes dispensées de déclaration fiscale électronique ; la compensation n'en ferme ni la dispense ni l'accès futur et n'autorise pas un nouveau CDD de spectacle.",
        'L213-1': "Les a et c du 5° visent respectivement le 1° et le 6° du I : recouvrement social salarial et contributions d'emploi et formation, avec les exceptions conservées. La proposition cible supprime CPF-CDD pour les périodes futures, garde les droits anciens et les dispenses de pièces ; la centralisation suit ce champ sans restaurer la contribution.",
        'L241-13': "Les 7° et 7° bis compensent les pertes de cotisations des seuls régimes et attributaires qu'ils désignent. La proposition cible conserve la réduction, ses corrections, le calcul distinct plus favorable pour les affectations temporaires du contrat unique et les adaptations Mayotte ; aucune indemnité ou nouveau CDD n'est créé par ce calcul social.",
        'L131-8': "Le 5° bis renvoie aux affectations des impôts effectivement dus, avec fractions à la date du fait générateur. Les 29,05 %, 20,77 et 8,28 points et la minoration de 4,1 milliards en 2026 ne sont pas recalculés ici ; le régime coordonné de CSG privée à 6,6 % et sa compensation financée restent propres à la cible, sans recette de remplacement inventée."
    }
}

for number, obj in answers.items():
    key = obj['code_id'] + '|' + obj['source_id']
    required = refs['requirements'][key]
    if required:
        obj['reference_checks'] = []
        for target_key in required:
            target = refs['targets'][target_key]
            assessment = reference_assessments[number][target['number']]
            assert len(assessment) >= 80
            obj['reference_checks'].append(dict(
                target_key=target_key,
                view_sha256=target['view_sha256'],
                assessment=assessment,
            ))

assert len(answers) == len(sources) == 24
result = [answers[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
