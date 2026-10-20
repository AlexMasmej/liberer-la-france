import json
from pathlib import Path


POLICY = "editorial_direction_2026_10_19"
sources = json.loads(Path("source.json").read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes, *, removed=None, repeal=None):
    item = {
        "proposed_xml": "".join(f"<p>{paragraph}</p>" for paragraph in paragraphs),
        "reason": reason,
        "review_notes": review_notes,
        "status": "rewrite_draft",
    }
    if removed is not None:
        item.update(
            change_type="normative_reduction",
            reform_policy_id=POLICY,
            removed_provisions=removed,
        )
    if repeal is not None:
        item.update(
            change_type="full_repeal",
            repeal_policy_id=POLICY,
            repeal_scope=repeal,
        )
    drafts[number] = item


add(
    "L1142-6",
    [
        "Les personnes mentionnées à l’article L. 1132-1 sont informées, par tout moyen, du texte des articles 225-1 à 225-4 du code pénal. Cette information est donnée dans les lieux de travail et dans les locaux où se fait l’embauche, ou à leur porte.",
    ],
    "Droit constant : la proposition antérieure est conservée après examen de la charge. Elle distingue le contenu de l’information de ses lieux de diffusion. Aucune coupe supplémentaire n’est retenue : l’information atteint aussi les candidats avant l’embauche et porte sur les interdictions pénales de discrimination. L’article permet déjà tout moyen de diffusion, sans imposer un formulaire, un dépôt ou une autorisation. Cette information préventive a une fonction propre, complémentaire de l’interdiction substantielle de L. 1132-1.",
    "Les destinataires de L. 1132-1, les lieux de travail et d’embauche et les quatre articles pénaux 225-1 à 225-4 sont conservés. La lecture de L. 1132-1 dans le corpus ne révèle pas une seconde obligation identique d’information à supprimer ici. Coordonner la diffusion des règles d’égalité avec la directive 2006/54/CE ; aucune formalité supplémentaire ni dérogation à la protection contre les discriminations n’est créée.",
)

add(
    "L1142-7",
    [
        "Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant cette abrogation. L’obligation autonome de prendre en compte un objectif de suppression des écarts de rémunération entre les femmes et les hommes cesse à cette date.",
        "Cette abrogation n’affecte ni l’obligation d’égalité de rémunération prévue à l’article L. 3221-2, ni l’interdiction des discriminations, ni les obligations de négociation, de correction et d’information prévues par les autres dispositions du présent code. Elle ne met pas fin aux engagements résultant d’accords collectifs ou de décisions de l’employeur.",
        "Les droits à réparation nés de faits antérieurs à cette entrée en vigueur et les actions qui s’y rapportent sont préservés. Les sanctions restent soumises aux règles d’application dans le temps des dispositions répressives plus douces.",
    ],
    "Réforme de fond : suppression de l’obligation générale de prise en compte d’un objectif, dont la formulation ne fixe aucune action propre. L. 3221-2 impose déjà l’égalité de rémunération pour un même travail ou un travail de valeur égale ; L. 2242-1 et L. 2242-3 organisent la négociation et les actions, et L. 1142-9 conserve les corrections. La seconde passe retire donc cette couche autonome au lieu de conserver sa reformulation antérieure. Les obligations concrètes et les créances salariales restent protégées.",
    "Ne pas étendre l’abrogation à L. 3221-2, L. 1132-1, L. 2242-1 ou L. 2242-3, ni aux indicateurs et sanctions maintenus dans ce lot. La note source concerne le déploiement historique au plus tard le 1er janvier 2019 au-delà de 250 salariés et le 1er janvier 2020 entre 50 et 250 salariés : elle ne fixe aucune date à la nouvelle abrogation. Les exigences européennes d’égalité de rémunération et de transparence demeurent à coordonner, notamment les directives 2006/54/CE et 2023/970 ; leur disparition n’est pas présumée.",
    repeal="Suppression pour l’avenir de l’obligation autonome de prendre en compte un objectif général de suppression des écarts de rémunération, sans supprimer l’égalité salariale, les actions correctrices, les engagements existants ni les droits à réparation antérieurs.",
)

add(
    "L1142-8",
    [
        "Dans les entreprises d’au moins cinquante salariés, l’employeur transmet chaque année aux services du ministère chargé du travail l’ensemble des indicateurs relatifs aux écarts de rémunération entre les femmes et les hommes et aux actions mises en œuvre pour les supprimer. Un décret définit la méthodologie et les modalités de cette transmission. Les informations déjà transmises à ces services ne sont pas transmises une seconde fois au titre du présent article, sauf rectification nécessaire. Par dérogation aux articles L. 311-6 et L. 312-1-2 du code des relations entre le public et l’administration, le ministère rend l’ensemble de ces indicateurs public sur son site internet, dans les conditions fixées par décret. La transmission des indicateurs libère l’employeur de son obligation de publication au titre du présent article ; aucune publication distincte sur un support de l’entreprise n’est exigée.",
        "Ces dispositions s’appliquent aux transmissions et publications exigibles à compter de l’entrée en vigueur de la loi qui les prévoit. Les informations déjà transmises pour une échéance en cours ne sont pas à transmettre de nouveau. Les manquements antérieurs restent soumis aux règles qui leur étaient applicables, sous réserve des règles relatives à l’application des sanctions plus douces. L’information du comité social et économique prévue par les autres dispositions du présent code est maintenue.",
    ],
    "Réforme de fond : une transmission annuelle unique alimente une publication ministérielle unique et libère l’employeur de la publication parallèle sur ses propres supports. La transmission existe déjà dans le dispositif réglementaire ; la proposition en fait le mode d’exécution de l’obligation légale et interdit sa répétition au même titre. Tous les indicateurs, la périodicité annuelle, le seuil de cinquante salariés, la méthodologie par décret et la publicité ministérielle dérogatoire sont maintenus. La seconde passe supprime donc un doublon réel de diffusion, sans supprimer la mesure des écarts ni l’accès du CSE.",
    "Coordonner D. 1142-4 et D. 1142-5 : retirer la publication sur le site de l’entreprise et l’information de substitution imposée à ce seul titre, organiser la réutilisation de la télédéclaration et conserver les échéances réglementaires non réformées. Coordonner aussi le point de départ du délai de correction défini à D. 1142-8 avec la transmission qui remplace la publication de l’employeur, sans remise à zéro des délais en cours ni allongement imputable au retard de publication du ministère. Adapter L. 2242-8 et R. 2242-2 à R. 2242-7 au fait que l’employeur ayant transmis les informations a satisfait à son obligation, même si le ministère tarde à les publier. L. 2312-18 et l’information du CSE restent applicables. Conserver la portée encadrée de la dérogation à L. 311-6 et L. 312-1-2 du CRPA, sans l’étendre à des données individuelles. La directive 2023/970 appelle une coordination sur le rapportage salarial, ses destinataires, ses échéances et la protection des données ; cet article n’en constitue pas une transposition complète. Les dispositions réglementaires du corpus portent une échéance de version au 1er mars 2029 : coordonner aussi leurs versions ultérieures sans modifier implicitement leurs autres règles.",
    removed=[
        "Publication annuelle distincte des mêmes indicateurs par l’employeur sur les supports de l’entreprise, en plus de leur publication sur le site du ministère chargé du travail.",
    ],
)

add(
    "L1142-9",
    [
        "Dans les entreprises d’au moins cinquante salariés, lorsque les résultats obtenus au regard des indicateurs mentionnés à l’article L. 1142-8 sont inférieurs au niveau fixé par décret, la négociation sur l’égalité professionnelle prévue au 2° de l’article L. 2242-1 porte également sur les mesures adéquates et pertinentes de correction. Elle porte, s’il y a lieu, sur la programmation annuelle ou pluriannuelle de mesures financières de rattrapage salarial. À défaut d’accord prévoyant ces mesures, l’employeur les fixe par décision après consultation du comité social et économique. Aucun dépôt de cette décision n’est exigé au seul titre du présent article ; le dépôt d’un accord collectif ou du plan d’action mentionné à l’article L. 2242-3 reste régi par les dispositions qui lui sont applicables. L’autorité administrative peut présenter des observations sur les mesures prévues par l’accord ou par la décision de l’employeur.",
        "L’employeur soumis à l’obligation prévue au premier alinéa porte les mesures de correction à la connaissance des salariés par tout moyen, dans les conditions fixées par décret. Aucune communication externe distincte de ces mesures n’est exigée au titre du présent article.",
        "La suppression du dépôt autonome et de la communication externe s’applique aux formalités exigibles à compter de l’entrée en vigueur de la loi qui la prévoit, y compris pour les mesures déjà adoptées. Les dépôts déjà effectués n’ont pas à être réitérés. Les mesures de correction et les engagements pris avant cette date continuent de produire leurs effets. Les manquements aux formalités antérieurement exigibles restent soumis aux règles qui leur étaient applicables, sous réserve des règles relatives aux sanctions plus douces.",
    ],
    "Réforme de fond : suppression du dépôt administratif propre à la décision de correction et de sa communication externe obligatoire. Les dépôts requis pour un accord collectif ou le plan d’action général restent ceux de leurs régimes respectifs. La correction des écarts, le rattrapage financier éventuel, la négociation, la consultation préalable du CSE, les observations administratives et l’information des salariés sont conservés. Les deux premiers alinéas gardent leurs fonctions respectives ; la transition est ajoutée après eux. La seconde passe retire les formalités périphériques sans réduire les mesures correctrices.",
    "Coordonner D. 1142-6 et D. 1142-6-2 : supprimer la publicité externe propre aux corrections et ne plus subordonner l’information des salariés à un dépôt autonome supprimé. Maintenir la disponibilité des informations utiles au CSE, les pouvoirs généraux de contrôle et le dépôt du plan d’action de L. 2242-3 lorsqu’il est requis. Adapter l’application de L. 2242-8 et de R. 2242-2 à R. 2242-7 pour exclure une sanction fondée uniquement sur ces formalités supprimées. Le niveau réglementaire de déclenchement des corrections demeure propre à L. 1142-9 ; l’abrogation de L. 1142-9-1 ne l’élargit pas. La note source rendait ces dispositions applicables à la publication des indicateurs effectuée en 2022 ; cette date historique ne devient pas celle de la réforme. Coordonner avec les exigences d’information et d’évaluation conjointe des directives 2006/54/CE et 2023/970, sans supprimer un examen correctif imposé par le droit de l’Union.",
    removed=[
        "Dépôt administratif autonome de la décision unilatérale de correction dans les mêmes conditions que le plan d’action, sans supprimer les dépôts dus au titre d’un autre régime.",
        "Communication externe obligatoire des mesures de correction par l’employeur, en conservant leur communication aux salariés et les indicateurs publics de L. 1142-8.",
    ],
)

add(
    "L1142-9-1",
    [
        "Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant cette abrogation. À compter de cette date, l’employeur n’est plus tenu, au seul titre du présent article, de fixer et de publier des objectifs de progression propres à chacun des indicateurs mentionnés à l’article L. 1142-8.",
        "Les objectifs et engagements inscrits dans un accord collectif, un plan d’action ou une décision de l’employeur continuent de produire leurs effets selon leurs règles propres. L’abrogation ne supprime ni les mesures de correction prévues à l’article L. 1142-9, ni les obligations résultant des articles L. 2242-1, L. 2242-3 et L. 3221-2.",
        "Les droits à réparation nés de faits antérieurs à cette entrée en vigueur et les actions qui s’y rapportent sont préservés. Les sanctions restent soumises aux règles d’application dans le temps des dispositions répressives plus douces.",
    ],
    "Réforme de fond : suppression de la fixation et de la publicité autonomes d’objectifs pour chaque indicateur à un seuil propre. Cette couche s’ajoute à la négociation générale sur l’égalité, aux objectifs déjà requis dans le plan d’action de L. 2242-3 et aux mesures de correction de L. 1142-9. La seconde passe retire cette obligation supplémentaire sans prétendre que ses seuils et son champ étaient identiques à ceux de la correction : les entreprises visées par ce seul seuil perdent effectivement cette obligation spécifique. L’égalité salariale et les engagements existants sont maintenus.",
    "Abroger ou réécrire D. 1142-6-1 pour l’avenir et retirer de D. 1142-6-2 la transmission des objectifs exigés au seul titre de L. 1142-9-1 et la justification de leur publicité. Conserver les parties de ces textes relatives aux mesures correctrices maintenues. Dans le corpus, D. 1142-6-1 prévoit un déclenchement à moins de 85 points et D. 1142-6 un déclenchement des corrections à moins de 75 points : ne pas fusionner ces deux seuils ni étendre silencieusement L. 1142-9. Les objectifs exigés par L. 2242-3 ou librement négociés ne sont pas abrogés. La note historique de 2022 reste attachée à la source et aux faits antérieurs. Les obligations de transparence et d’évaluation issues de la directive 2023/970 doivent être coordonnées indépendamment de cette suppression nationale.",
    repeal="Suppression pour l’avenir de l’obligation autonome de fixer et publier, au seuil réglementaire propre à cet article, des objectifs de progression pour chacun des indicateurs d’égalité salariale, avec maintien des corrections, des autres plans et des engagements existants.",
)

add(
    "L1142-10",
    [
        "Dans les entreprises d’au moins cinquante salariés, lorsque les résultats obtenus au regard des indicateurs mentionnés à l’article L. 1142-8 sont inférieurs au niveau fixé par décret, l’entreprise dispose de trois ans pour se mettre en conformité. Si ses résultats restent inférieurs à ce niveau à l’expiration de ce délai, l’employeur peut être soumis à une pénalité financière. Lorsqu’une pénalité lui est appliquée sur ce fondement, la pénalité financière prévue à l’article L. 2242-8 ne peut lui être appliquée.",
        "La pénalité prévue au premier alinéa ne peut dépasser 1 % des rémunérations et gains, au sens du premier alinéa de l’article L. 242-1 du code de la sécurité sociale et du premier alinéa de l’article L. 741-10 du code rural et de la pêche maritime, versés aux travailleurs salariés ou assimilés au cours de l’année civile précédant l’expiration du délai prévu au premier alinéa. L’autorité administrative en fixe le montant dans les conditions prévues par décret. Un délai supplémentaire d’un an peut être accordé à l’entreprise pour se mettre en conformité, en fonction de ses efforts en matière d’égalité salariale entre les femmes et les hommes et des motifs de sa défaillance.",
        "Le produit de cette pénalité est affecté à la branche mentionnée au 3° de l’article L. 200-2 du code de la sécurité sociale.",
    ],
    "Droit constant : la sanction du défaut persistant de résultat est maintenue après examen de sa fonction. La supprimer priverait le dispositif correctif conservé d’un moyen propre d’effectivité ; elle ne rémunère aucune formalité et n’est pas un prélèvement général sur l’activité. Le délai de trois ans, la faculté d’un an supplémentaire et le non-cumul avec L. 2242-8 limitent déjà la charge. La rédaction précise les sujets et la chronologie, conserve l’assiette et le plafond de 1 %, et rétablit les trois alinéas de la source, que la proposition antérieure avait dispersés en cinq.",
    "Contrôle des paramètres : au moins 50 salariés ; délai de 3 ans ; plafond de 1 % ; rémunérations et gains des salariés ou assimilés de l’année civile précédant l’expiration de ce délai ; prolongation possible d’un an ; exclusion du cumul avec L. 2242-8. Maintenir les renvois aux premiers alinéas de L. 242-1 CSS et L. 741-10 du code rural et au 3° de L. 200-2 CSS, sans substitution silencieuse. La note source porte sur l’entrée en vigueur au 1er janvier 2026 de dispositions de la loi n° 2025-199 du 28 février 2025, non sur une réforme future. Les garanties procédurales réglementaires, la proportionnalité et le recours contre la sanction restent applicables ; coordonner l’effectivité des sanctions avec les directives 2006/54/CE et 2023/970. La modification de L. 1142-8 ne remet pas à zéro les délais de correction en cours.",
)

add(
    "L1142-11",
    [
        "Dans les entreprises qui emploient au moins mille salariés pour le troisième exercice consécutif, l’employeur transmet chaque année aux services du ministère chargé du travail les éventuels écarts de représentation entre les femmes et les hommes parmi les cadres dirigeants au sens de l’article L. 3111-2 du présent code, d’une part, et parmi les membres des instances dirigeantes définies à l’article L. 23-12-1 du code de commerce, d’autre part.",
        "Par dérogation aux articles L. 311-6 et L. 312-1-2 du code des relations entre le public et l’administration, le ministère rend ces écarts publics sur son site internet dans les conditions fixées par décret. Leur transmission libère l’employeur de son obligation de publication au titre du présent article ; aucune publication distincte sur un support de l’entreprise n’est exigée. Les informations déjà transmises à ces services ne sont pas transmises une seconde fois au même titre, sauf rectification nécessaire. Ces modalités s’appliquent aux transmissions et publications exigibles à compter de l’entrée en vigueur de la loi qui les prévoit, sans nouvelle transmission des informations déjà reçues pour l’échéance en cours. Les manquements antérieurs restent soumis aux règles qui leur étaient applicables, sous réserve des règles relatives aux sanctions plus douces. L’information du comité social et économique prévue par les autres dispositions du présent code est maintenue.",
        "Dans chacun des deux ensembles mentionnés au premier alinéa, la proportion de personnes de chaque sexe doit être d’au moins 30 %.",
    ],
    "Réforme de fond : suppression de la publication propre à l’entreprise, doublant celle du ministère ; la transmission déjà prévue par le dispositif réglementaire devient le mode unique d’exécution de cette obligation. Le calcul annuel séparé pour les cadres dirigeants et les membres des instances dirigeantes, la condition d’au moins mille salariés pour le troisième exercice consécutif et le minimum de 30 % pour chaque sexe sont maintenus. Les trois alinéas normatifs de la source restent dans leur ordre : le quota demeure au dernier alinéa, cible explicite de L. 1142-13. La réduction porte sur la diffusion, sans supprimer la représentation équilibrée.",
    "Coordonner D. 1142-16, D. 1142-17 et D. 1142-19 : supprimer le support de publication propre à l’entreprise et les mentions de ses modalités de publication devenues inutiles, conserver la télédéclaration unique, le calcul de D. 1142-15, les explications d’incalculabilité et l’information du CSE. Ne pas transférer à l’employeur un défaut de publication imputable au ministère après transmission. La source assignée est la version du 1er mars 2026 au 1er mars 2029 (ABROGE_DIFF) : la suppression du doublon doit aussi être coordonnée avec la version suivante, sans figer le seuil de 30 % au-delà de la période de cette version ni supprimer les paliers prévus aux II et III de l’article 14 de la loi n° 2021-1774. L. 1142-13 conserve son renvoi au dernier alinéa. Les obligations distinctes de représentation dans les organes sociaux et celles relevant de la directive 2022/2381 ne sont pas supprimées ni réputées satisfaites par ce seul article.",
    removed=[
        "Publication annuelle séparée par l’employeur des écarts de représentation sur un support de l’entreprise en plus de la publication assurée par le ministère chargé du travail.",
    ],
)

add(
    "L1142-13",
    [
        "Dans les entreprises qui emploient au moins mille salariés pour le troisième exercice consécutif, lorsque l’entreprise ne respecte pas l’obligation prévue au dernier alinéa de l’article L. 1142-11, la négociation sur l’égalité professionnelle prévue au 2° de l’article L. 2242-1 porte également sur les mesures adéquates et pertinentes de correction. À défaut d’accord prévoyant ces mesures, l’employeur les fixe par décision après consultation du comité social et économique de l’entreprise. Aucun dépôt de cette décision n’est exigé au seul titre du présent article ; le dépôt d’un accord collectif ou du plan d’action mentionné au premier alinéa de l’article L. 2242-3 reste régi par les dispositions qui lui sont applicables. L’autorité administrative peut présenter des observations sur les mesures prévues par l’accord ou par la décision de l’employeur. Ces mesures sont présentées à l’organe chargé de l’administration ou de la surveillance de l’entreprise ainsi qu’au comité social et économique de l’entreprise.",
        "La suppression du dépôt autonome s’applique aux formalités exigibles à compter de l’entrée en vigueur de la loi qui la prévoit, y compris pour les décisions déjà prises. Les décisions déjà déposées n’ont pas à l’être de nouveau. Les mesures de correction et les engagements antérieurs continuent de produire leurs effets. Les manquements à cette formalité antérieurement exigible restent soumis aux règles qui leur étaient applicables, sous réserve des règles relatives aux sanctions plus douces.",
    ],
    "Réforme de fond : suppression du dépôt administratif autonome de la décision de correction, en laissant subsister les dépôts imposés au titre d’un accord collectif ou du plan d’action général. La seconde passe distingue cette formalité de la négociation, de la consultation préalable du CSE et de la présentation des mesures définitives aux organes de l’entreprise, qui restent utiles au contrôle effectif de la correction. Les observations administratives et le champ de mille salariés pendant trois exercices sont conservés. Le premier alinéa reste le siège de l’ensemble du dispositif permanent.",
    "Le dernier alinéa de L. 1142-11 reste celui du quota dans la proposition de ce lot ; ne pas le déplacer lors de l’assemblage. Le renvoi au premier alinéa de L. 2242-3 n’impose plus ici un dépôt autonome, mais le dépôt du plan d’action qui relève de cet autre article demeure. Coordonner les éventuels textes d’application et les versions ultérieures de L. 1142-11, sans supprimer ses paliers. La phrase source « qui sont présentées » peut laisser hésiter entre les mesures et les observations ; comme la proposition antérieure, la rédaction retient les mesures comme objet de la présentation. Cette ambiguïté préexistante est signalée, sans faire disparaître la faculté d’observations administratives. La note source fixe l’entrée en vigueur historique au 1er mars de la cinquième année suivant la publication de la loi n° 2021-1774, soit la version applicable au 1er mars 2026 ; cette date ne vaut pas date de la nouvelle réforme. Ne pas assimiler ce régime à celui, distinct, des organes sociaux visé par la directive 2022/2381.",
    removed=[
        "Dépôt administratif autonome de la décision de correction des écarts de représentation dans les mêmes conditions que le plan d’action de L. 2242-3, sans supprimer le dépôt dû au titre de ce plan ou d’un accord collectif.",
    ],
)

add(
    "L1143-1",
    [
        "Pour assurer l’égalité professionnelle entre les femmes et les hommes, les mesures d’égalité des chances prévues à l’article L. 1142-4 peuvent être réunies dans un plan pour l’égalité professionnelle négocié dans l’entreprise.",
        "Ces mesures peuvent être préparées à partir des informations déjà disponibles. Le présent article n’impose ni l’utilisation d’un jeu de données déterminé, ni une collecte de données ou un rapport distincts de ceux requis par les autres dispositions du présent code.",
        "Cette simplification s’applique à la préparation des plans à compter de l’entrée en vigueur de la loi qui la prévoit. Les plans en cours et les engagements qu’ils comportent continuent de produire leurs effets. Les obligations d’information et de consultation du comité social et économique résultant des autres dispositions du présent code sont maintenues.",
    ],
    "Réforme de fond : suppression de la prescription documentaire particulière renvoyant obligatoirement, même à titre non exclusif, aux données du 1° bis de L. 2323-8. La préparation du plan peut réutiliser les informations disponibles sans rapport spécial. La faculté de négocier ce plan est maintenue : elle sert notamment de support aux mesures temporaires autorisées par L. 1142-4 et n’est pas une obligation de conclure un plan supplémentaire. La seconde passe ne se borne donc pas à substituer un numéro de renvoi à un autre ; elle retire la contrainte propre au jeu de données sans supprimer la justification des mesures d’égalité des chances.",
    "Incohérence préexistante : la source et le précédent projet renvoient encore au 1° bis de L. 2323-8, issu du dispositif du comité d’entreprise ; cet article ne figure pas dans le corpus courant consulté. La suppression est assumée comme réforme de fond, sans inventer un numéro de remplacement. L. 2312-18 et, dans son champ supplétif, le 2° de L. 2312-36 conservent leurs données et obligations propres ; aucune de leurs exigences n’est abrogée par la dispense de rapport distinct au seul titre du présent article. Maintenir les conditions de L. 1142-4, notamment le caractère temporaire et la finalité des mesures, et coordonner le régime des actions positives avec la directive 2006/54/CE. Ne pas confondre ce plan facultatif avec le plan d’action annuel obligatoire de L. 2242-3. Les droits et obligations antérieurs des plans en cours sont expressément conservés.",
    removed=[
        "Obligation propre au plan facultatif de prendre notamment en considération le jeu de données désigné par le 1° bis de l’ancien article L. 2323-8, sans supprimer les données et consultations imposées par les autres régimes.",
    ],
)

add(
    "L1143-2",
    [
        "Si la négociation n’aboutit pas à un accord, l’employeur peut mettre en œuvre le plan pour l’égalité professionnelle après avoir consulté le comité social et économique et recueilli son avis.",
    ],
    "Droit constant : la proposition antérieure est conservée après réexamen. Le plan demeure facultatif, l’échec de la négociation permet une décision de l’employeur et aucun avis favorable du CSE n’est exigé. La consultation préalable et le recueil de l’avis sont maintenus parce que le plan peut porter des mesures temporaires différenciées autorisées par L. 1142-4 ; les représentants des salariés doivent pouvoir en examiner la justification et les effets. Cette participation utile ne se confond pas avec le pouvoir d’opposition administrative de L. 1143-3, supprimé dans ce lot.",
    "Conserver les deux conditions cumulatives : négociation achevée sans accord, puis consultation et avis du CSE avant mise en œuvre. La proposition ne crée ni accord obligatoire du comité ni délai nouveau. Coordonner l’application immédiate du plan après ces conditions avec l’abrogation de L. 1143-3 et de son dispositif réglementaire D. 1143-6. Les règles générales de consultation restent applicables ; les aides financières et les contrats pour la mixité des emplois ont leurs propres conditions, qui ne sont pas supprimées ici.",
)

add(
    "L1143-3",
    [
        "Le présent article est abrogé à compter de l’entrée en vigueur de la loi portant cette abrogation. À compter de cette date, l’autorité administrative ne peut plus s’opposer à l’application d’un plan pour l’égalité professionnelle sur le fondement du présent article, y compris lorsqu’elle a été saisie avant cette date sans avoir encore notifié sa décision.",
        "Les décisions d’opposition notifiées avant cette entrée en vigueur demeurent soumises aux règles de fond et de recours qui leur étaient applicables. Leur abrogation ou leur annulation relève des règles applicables à ces décisions.",
        "Les plans restent soumis aux conditions de l’article L. 1142-4 et, lorsqu’il s’applique, de l’article L. 1143-2, ainsi qu’aux autres obligations légales et conventionnelles. L’abrogation ne limite ni les pouvoirs généraux de contrôle de l’inspection du travail, ni les actions en justice, ni les droits à réparation relatifs aux plans antérieurs ou nouveaux.",
    ],
    "Réforme de fond : suppression du pouvoir d’opposition administrative propre au plan, et donc de la procédure réglementaire d’examen préalable susceptible d’en bloquer l’application. Le contrôle général de légalité, la consultation du CSE, les conditions des actions positives et les recours sont conservés. La seconde passe retire effectivement ce filtre administratif plutôt que de reformuler sa réserve. Les saisines pendantes sont closes quant à ce pouvoir pour l’avenir ; les décisions déjà notifiées et leurs recours restent régis par leurs règles propres.",
    "Abroger D. 1143-6 pour les nouvelles décisions et les saisines encore pendantes : il prévoit un avis écrit et motivé dans les deux mois suivant la saisine. Les dispositions historiques et territoriales figurant dans ses notes ne constituent pas une date de réforme future. Maintenir L. 1142-4, L. 1143-1, L. 1143-2 et les voies de contestation. D. 1143-5 concerne une étude aidée par l’État et ses consultations ; D. 1143-7 et suivants organisent un contrat d’aide distinct : ne pas abolir ces conditions de financement par assimilation à l’opposition supprimée. Les exigences européennes relatives aux actions positives et à la non-discrimination continuent de s’appliquer ; aucune validation automatique de la légalité matérielle du plan n’est créée.",
    repeal="Suppression pour l’avenir du pouvoir administratif spécifique d’opposition à l’application des plans pour l’égalité professionnelle et de la procédure préalable correspondante, y compris pour les saisines pendantes sans décision notifiée, avec maintien des contrôles généraux et des recours.",
)

add(
    "L1144-1",
    [
        "Dans un litige relatif à l’application des articles L. 1142-1 et L. 1142-2, le candidat à un emploi, à un stage ou à une période de formation, ou le salarié, présente des éléments de fait laissant supposer une discrimination directe ou indirecte fondée sur le sexe, la situation de famille ou la grossesse.",
        "Au vu de ces éléments, il appartient au défendeur de prouver que sa décision repose sur des éléments objectifs étrangers à toute discrimination.",
        "Le juge forme sa conviction après avoir ordonné, si nécessaire, toutes les mesures d’instruction qu’il estime utiles.",
    ],
    "Droit constant : maintien du partage de la preuve et des pouvoirs du juge, avec des phrases plus directes et les trois alinéas d’origine. Le réexamen du doublon apparent avec L. 1134-1 ne justifie pas une abrogation isolée : ce dernier vise les dispositions de son chapitre II, alors que le présent article couvre expressément L. 1142-1 et L. 1142-2. Supprimer cette règle sans coordination complète fragiliserait le recours contre la discrimination. La proposition conserve le seuil probatoire allégé, les trois motifs, tous les demandeurs et l’ordre entre instruction et formation de la conviction.",
    "L. 1134-1 a été lu dans le corpus : son champ textuel ne doit pas être réputé étendu automatiquement aux articles L. 1142-1 et L. 1142-2. Préserver la discrimination directe et indirecte, le sexe, la situation de famille et la grossesse, ainsi que la candidature à un emploi, à un stage ou à une période de formation. La charge de justification reste sur la partie défenderesse dès présentation d’éléments laissant supposer la discrimination, sans exiger une preuve complète du demandeur. Coordonner avec les règles de preuve de la directive 2006/54/CE et celles de la directive 2023/970, sans affaiblir leurs garanties ni étendre ce partage de preuve à la procédure pénale de L. 1146-1. Aucun délai ni plafond de réparation nouveau n’est introduit.",
)


assert len(sources) == len(drafts) == 12
answer = []
for source in sources:
    item = {
        key: source[key]
        for key in ("code_id", "source_id", "source_sha256", "number")
    }
    item.update(drafts[source["number"]])
    answer.append(item)

Path("answer.json").write_text(
    json.dumps(answer, ensure_ascii=False, indent=2) + "\n"
)
