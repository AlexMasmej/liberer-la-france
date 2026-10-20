import json
import re
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
by_number = {item['number']: item for item in sources}
decisions = {}


def plain(xml):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]*>', ' ', xml))).strip()


def retain(number, reason, notes, assessment, limitations, burdens):
    decisions[number] = {
        'proposed_xml': None,
        'reason': reason,
        'review_notes': notes,
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
    }


retain(
    'L2342-10-1',
    "Maintien intégral après examen de l'obligation d'information : elle donne aux salariés et à leurs représentants accès aux résultats de la consultation transnationale, sans imposer un rapport distinct, un formulaire, un dépôt ou une périodicité supplémentaire. L2343-12 ne fait pas double emploi : il concerne le comité institué en l'absence d'accord, tandis que le présent article concerne celui institué par accord. Retirer cette information priverait les salariés de la restitution de leur représentation ; aucune réforme de fond ni réécriture stylistique n'est proposée.",
    "Renvoi L2342-10 lu intégralement dans le corpus : secret des procédés de fabrication et discrétion sur les informations confidentielles. Comparaison intégrale avec L2343-12 du lot. La restitution reste ouverte aux salariés futurs et n'est subordonnée ni à la forme ancienne de leur contrat ni à sa durée. Cadre européen à coordonner : directive 2009/38/CE, article 10 sur le rôle des représentants ; son texte consolidé n'est pas joint localement.",
    "Par rapport à la source officielle entière, aucune obligation n'est retirée : la restitution des résultats aux représentants locaux ou, à défaut, aux salariés est conservée avec ses limites de confidentialité.",
    "Aucun allègement chiffré ni gain de conformité n'est démontré. Le mode concret de restitution relève du dispositif applicable ; la consolidation européenne reste à vérifier sur une source primaire complète.",
    "Aucune charge nouvelle n'est identifiée : maintien de la même information et des mêmes destinataires, sans registre, attestation, calendrier ou transmission administrative ajouté."
)

retain(
    'L2342-10-2',
    "Maintien intégral du droit aux formations nécessaires au mandat sans perte de salaire, dont les conditions sont déterminées par l'accord. Cette prise en charge protège la compétence et l'indépendance des représentants ; elle ne constitue ni cotisation accessoire ni agrément retirable. Le dispositif de L2344-9 vise d'autres bénéficiaires, membres du groupe spécial et du comité sans accord : il ne supprime pas le besoin du présent fondement pour le comité conventionnel.",
    "L2344-9 et L2342-9 ont été lus dans le corpus. Préserver pour les titulaires futurs la nécessité de la formation, le maintien du salaire et le rôle de l'accord ; ne pas transformer la durée d'une formation en terme d'emploi ou appliquer le barème de rupture à une rémunération de formation. Coordination européenne : article 10 de la directive 2009/38/CE, consolidation non jointe.",
    "La source officielle entière reste applicable : la formation nécessaire demeure accessible sans perte de salaire. Aucun coût de formation ou salaire n'est présenté comme supprimé.",
    "Le coût effectif des formations et leur organisation ne sont pas chiffrés. Le maintien ne modifie pas les autres régimes de formation ni les conditions d'emploi.",
    "Aucune charge nouvelle n'est identifiée, car ni formation supplémentaire, ni justificatif, ni organisme agréé, ni condition de financement nouveau ne sont introduits."
)

retain(
    'L2342-11',
    "Maintien intégral de la voie conventionnelle permettant une ou plusieurs procédures d'information et de consultation au lieu d'un comité européen. Les modalités de réunion des représentants sont nécessaires à un avis collectif effectif ; supprimer cette faculté ou la réunion reviendrait à fermer une alternative d'organisation ou à vider la consultation de son contenu. Aucun comité supplémentaire, dépôt ni autorisation ne résulte de cet article.",
    "L2342-2 a été lu : l'accord écrit peut organiser soit un comité, soit une procédure. L2341-6 à L2341-8 ont été lus sur la consultation, l'information et les questions transnationales. Préserver le caractère non limitatif de « notamment » et le critère d'atteinte considérable. Cadre européen à confronter : directive 2009/38/CE, article 6, version consolidée absente des pièces.",
    "Aucune réduction nouvelle par rapport à la source entière : l'alternative négociée et les réunions nécessaires à la consultation sont maintenues, sans exiger la création d'un comité.",
    "Le nombre de procédures dépend de l'accord et n'est pas réduit arbitrairement. Aucun gain global de complexité, ni effet fiscal, n'est établi par ce maintien.",
    "Aucune charge nouvelle n'est identifiée : les modalités demeurent conventionnelles et aucun dossier, calendrier minimal, visa ou relevé de réunion supplémentaire n'est créé."
)

retain(
    'L2342-12',
    "Maintien intégral des deux protections de confidentialité applicables aux représentants et aux experts de la procédure conventionnelle : secret des procédés de fabrication et discrétion sur les informations confidentielles données comme telles par l'employeur. Elles rendent possible la communication d'informations sensibles sans ajouter déclaration ou contrôle préalable. L2342-10 concerne les membres d'un comité institué par accord et L2344-8 d'autres instances : leur voisinage ne crée pas une double formalité imposée aux mêmes destinataires par le présent article.",
    "Comparaison intégrale avec L2342-10 et L2344-8 du corpus. Les 1° et 2°, leurs objets et leurs qualifications sont conservés. Le maintien ne vaut pas reconnaissance du caractère confidentiel de toute information unilatéralement étiquetée : portée de la confidentialité et voies de contestation à contrôler dans le droit applicable. Cadre européen : article 8 de la directive 2009/38/CE, consolidation non jointe.",
    "Les deux obligations de la source entière sont conservées pour leur fonction de protection des informations ; aucune suppression de secret, déclaration ou autorisation n'est revendiquée.",
    "L'articulation avec le secret des affaires et le contrôle juridictionnel n'est pas réécrite dans ce lot. La consolidation européenne n'a pas été vérifiée sur un texte primaire joint.",
    "Aucune charge nouvelle n'est identifiée : mêmes personnes, mêmes informations protégées et aucune procédure de classement, attestation ou registre de confidentialité supplémentaire."
)

retain(
    'L2343-1',
    "Maintien intégral du mécanisme subsidiaire qui empêche qu'un refus de négocier ou l'absence d'accord neutralise la représentation transnationale. Les délais de six mois et de trois ans déterminent les carences ouvrant ce mécanisme ; les six mois suivants sont une échéance de constitution et de première réunion, pas un délai minimal d'attente à ajouter à chaque démarche. Leur suppression sans dispositif équivalent ferait disparaître une garantie essentielle de représentation. Aucun prélèvement, agrément ou justificatif redondant n'est identifié.",
    "L2342-4 et L2342-8 lus intégralement : demande écrite de cent salariés ou représentants dans deux entreprises ou établissements et deux Etats ; décision aux deux tiers d'arrêter ou de ne pas ouvrir les négociations, avec son régime propre de nouvelle demande. Conserver les 1° et 2°, les points de départ et la réserve de L2342-8. Cadre européen à coordonner : article 7 de la directive 2009/38/CE ; texte consolidé non joint. Le préavis individuel de quinze jours est étranger à ces délais collectifs.",
    "Aucune modification de la source officielle entière : les deux cas d'institution du comité et le délai maximal de sa mise en place restent protégés contre le blocage des négociations.",
    "Pas de baisse de durée de procédure revendiquée. Le maintien ne certifie pas la consolidation du cadre européen et ne tranche pas les litiges portant sur les dates de réception.",
    "Aucune charge nouvelle n'est identifiée : ni cas d'institution supplémentaire, ni pièce, déclaration, contrôle ou délai ajouté aux trois échéances de la source."
)

retain(
    'L2343-2',
    "Maintien intégral de la réunion annuelle et des onze thèmes d'information. Ils donnent un contenu économique et social à la consultation européenne, notamment avant des restructurations ; leur suppression retirerait l'information nécessaire à la défense des salariés. L'article ne commande pas onze rapports ni des réunions séparées par thème. La consultation de L2343-3 et le rapport de L2343-9 peuvent servir à cette même réunion annuelle : aucune obligation de double réunion n'est identifiée dans la source à supprimer artificiellement.",
    "Les onze rubriques, de la structure jusqu'aux licenciements collectifs, ont été lues et conservées sans fusion qui en réduise le champ. L2341-8 lu pour la compétence transnationale ; L2343-3 et L2343-9 lus en entier. Cadre européen : prescriptions subsidiaires de l'annexe I de la directive 2009/38/CE, à confronter à sa version consolidée non fournie. Pas d'assimilation de la réunion annuelle à un rapport de protection complémentaire visé par reporting_social.",
    "La fréquence annuelle et les onze catégories d'information de la source entière restent intactes. Aucun rapport multiple supposé, prélèvement ou coût de réunion n'est compté comme supprimé.",
    "Le contenu concret varie selon l'entreprise et les questions transnationales. Le coût de production de l'information et le solde national de conformité ne sont pas chiffrés.",
    "Aucune charge nouvelle n'est identifiée : pas de nouveau thème, modèle de rapport, ventilation, transmission externe ou fréquence supplémentaire."
)

retain(
    'L2343-3',
    "Maintien intégral de la consultation annuelle sur les 5° à 11° de L2343-2 et du droit d'obtenir une réponse motivée aux avis. L'information seule ne remplace pas la possibilité de discuter des décisions touchant l'emploi. La source n'exige pas que le rapport soit distinct de celui de L2343-9 ni que la réunion soit séparée de celle de L2343-2 ; une prétendue suppression d'un second rapport obligatoire ne serait donc pas démontrée. Aucun toilettage stylistique n'est produit.",
    "L2343-2 et L2343-9 lus intégralement : les thèmes 5° à 11° sont l'emploi, les investissements, les changements d'organisation ou de procédés, les transferts, les fusions, les réductions ou fermetures et les licenciements collectifs. Le droit à une réponse motivée et la rencontre avec l'employeur sont conservés. Référence européenne à coordonner : annexe I de la directive 2009/38/CE ; consolidation primaire non jointe.",
    "Aucune réduction par rapport à l'article officiel entier : la consultation et la réponse motivée restent nécessaires, avec le périmètre exact des sept thèmes visés.",
    "Aucune économie de rapport ou de réunion distincte n'est revendiquée faute d'obligation de séparation dans la source. Les consultations nationales conservent leur champ propre.",
    "Aucune charge nouvelle n'est identifiée : ni second rapport, ni consultation additionnelle, ni délai de réponse chiffré nouveau, ni justificatif supplémentaire."
)

retain(
    'L2343-4',
    "Maintien intégral de la procédure exceptionnelle d'information et de consultation, du droit des représentants directement concernés à participer et de la faculté de faire intervenir un responsable au niveau de décision approprié. Cette faculté évite déjà une présence personnelle inutile du seul chef d'entreprise. Le rapport et la réunion demandée par les représentants sont nécessaires pour traiter rapidement les décisions qui affectent considérablement les salariés ; ils ne doublonnent pas une information annuelle susceptible d'être trop tardive.",
    "Les six alinéas ont été relus, y compris les exemples non limitatifs, le bureau ou à défaut le comité, la réunion à leur demande, les meilleurs délais, l'avis à l'issue ou dans un délai raisonnable, les prérogatives patronales et la représentation dotée d'un pouvoir de décision. Renvoi L2343-7 vérifié dans le lot. Coordination européenne : annexe I de la directive 2009/38/CE, consolidation non jointe. Ne pas convertir le préavis individuel en délai de cette procédure collective.",
    "La source entière est conservée : consultation exceptionnelle et souplesse de représentation de l'employeur demeurent, sans nouveau circuit préalable ni retrait d'un droit de participation.",
    "Le délai raisonnable n'est pas remplacé par quinze jours. Les autorisations de rupture de salariés protégés et les autres procédures collectives ne sont pas traitées par cet article.",
    "Aucune charge nouvelle n'est identifiée : maintien des mêmes circonstances, participants, rapport et facultés de représentation, sans déclaration, visa ni échéance supplémentaire."
)

retain(
    'L2343-5',
    "Maintien intégral de la composition du comité, du caractère consultatif de l'assistance du chef d'entreprise et de l'information des niveaux de direction sur les désignations. L'identification des interlocuteurs rend la représentation et la consultation opérantes. La mention de deux personnes choisies par le chef ne démontre pas, à elle seule, une obligation autonome de recruter deux salariés ou de créer deux emplois ; sa reformulation ne serait pas une économie établie. La composition représentative n'est pas supprimée pour fabriquer une réduction.",
    "Conserver les 1° et 2°, les deux personnes à voix seulement consultative et les représentants des établissements ou entreprises du groupe. L2344-2 à L2344-7 et R2344-1 ont été lus sur la désignation, la répartition et le recours. La portée exacte de l'assistance prévue au 1° ne doit pas être transformée en hypothèse de deux postes obligatoires. Cadre européen : composition et information de la direction dans l'annexe I de la directive 2009/38/CE, consolidation non jointe.",
    "Aucune modification de la source officielle entière : composition et information des directions sont maintenues. Aucune suppression fictive de deux emplois ou de deux mandats n'est comptée.",
    "La pratique de l'assistance patronale n'est pas documentée. Aucun coût de personnel, gain de siège ou effet sur les règles de désignation n'est établi.",
    "Aucune charge nouvelle n'est identifiée : aucun membre, destinataire administratif, document de nomination ou régime de rémunération supplémentaire n'est imposé."
)

retain(
    'L2343-6',
    "Maintien intégral de la possibilité d'adapter la composition du comité par accord interne lorsque la structure ou la dimension du groupe change. Il s'agit déjà d'une souplesse négociée, sans autorisation administrative, délai minimal ou dépôt spécial prescrit par cet article. Supprimer l'accord ne supprimerait pas une formalité redondante : cela retirerait la garantie que l'employeur et les représentants consentent à l'adaptation de leur représentation.",
    "L2343-8 a été lu sur les adaptations pouvant figurer dans le règlement intérieur ; les objets ne sont pas identiques, car le présent article règle l'accord sur la composition. L2344-1 et R2344-1 lus pour la répartition des sièges. Préserver la limitation aux changements de structure ou de dimension et la participation des deux parties, sans création d'un pouvoir unilatéral de l'employeur.",
    "Aucun changement par rapport à la source entière : l'adaptation conventionnelle de la composition reste possible. Aucune autorisation déjà absente n'est présentée comme supprimée.",
    "Le maintien n'étend pas l'accord à une réduction unilatérale des sièges et ne réécrit pas les règles européennes d'adaptation de la représentation.",
    "Aucune charge nouvelle n'est identifiée : l'accord existant demeure la voie facultative et aucun vote additionnel, formulaire, dépôt ou délai d'opposition nouveau n'est créé."
)

retain(
    'L2343-7',
    "Maintien intégral de la personnalité civile, de la présidence, du secrétariat et du bureau d'au maximum cinq membres doté de moyens réguliers. La personnalité permet l'action du comité, notamment en justice ; le secrétaire et le bureau rendent praticable la représentation transnationale entre les réunions. Ces organes ne sont pas des rapports ou des agréments redondants. Le maximum de cinq est conservé avec les moyens du bureau, sans élargissement coûteux ni suppression d'une garantie d'autonomie.",
    "R2343-1 lu intégralement : désignation majoritaire du secrétaire parmi les membres et élection du bureau parmi les membres. L2343-4, L2343-11, L2343-13 à L2343-15 vérifiés dans le lot pour les missions et moyens. Le présent texte ne doit pas effacer la faculté de représentation patronale propre à L2343-4. Cadre européen : comité restreint et moyens dans l'annexe I de la directive 2009/38/CE, consolidation non jointe.",
    "Aucune réduction par rapport aux quatre alinéas de la source officielle : la capacité civile et les organes nécessaires du comité sont conservés avec le plafond de cinq membres du bureau.",
    "Aucun financement forfaitaire ni gain de nombre de membres n'est calculé. Les règles de représentation de la direction et les pouvoirs judiciaires demeurent à leur champ propre.",
    "Aucune charge nouvelle n'est identifiée : pas de nouvel organe, d'élection supplémentaire, de registre, de budget minimal chiffré ou de rapport périodique ajouté."
)

retain(
    'L2343-8',
    "Maintien intégral du règlement intérieur et de sa faculté d'organiser les conséquences des changements de structure ou de dimension. Ce cadre interne règle les modalités de fonctionnement sans imposer un agrément administratif, une transmission ou un nouveau rapport. L'examen des changements à la réunion annuelle est une possibilité qui évite déjà une réunion autonome ; le supprimer ou le réécrire comme une nouveauté ne démontrerait aucun allègement.",
    "L2343-6 lu pour les modifications de composition décidées par accord et L2343-2 pour la réunion annuelle. Les deux alinéas, les deux possibilités exprimées par « peut » et l'objet interne du règlement restent intacts. Référence européenne à confronter : dispositions subsidiaires de l'annexe I de la directive 2009/38/CE, texte consolidé non joint.",
    "La source entière reste applicable : cadre interne nécessaire et adaptations facultatives demeurent. Aucune réunion supplémentaire prétendument obligatoire n'est comptée comme supprimée.",
    "La teneur des règlements déjà adoptés n'est pas dans les sources ; aucune modification automatique de leurs clauses ni économie administrative globale n'est démontrée.",
    "Aucune charge nouvelle n'est identifiée : aucune homologation, déclaration, révision annuelle, publicité ou pièce normalisée ne vient s'ajouter au règlement existant."
)

retain(
    'L2343-9',
    "Maintien intégral de la convocation annuelle par le président, du rapport sur l'évolution et les perspectives d'activité et de l'information des responsables locaux. Le rapport est le support matériel de la consultation, non un état statistique sans destinataire utile. L'information des responsables locaux permet l'articulation transnationale. L'article n'exige ni rapports différents pour L2343-2 et L2343-3, ni envoi à une administration ; aucune duplication légalement imposée n'est démontrée.",
    "L2343-2 et L2343-3 ont été lus intégralement pour le support commun possible ; L2343-10 conserve ses règles de fixation d'ordre du jour avec la dérogation proposée dans ce lot. Cadre européen à coordonner : réunion annuelle sur rapport d'activité et perspectives, avec information des directions locales, annexe I de la directive 2009/38/CE ; consolidation non jointe. Ni reporting_social ni la suppression de la liste annuelle L2262-6 ne visent ce rapport de consultation.",
    "Aucune réduction au regard de la source officielle entière : les trois alinéas nécessaires à la réunion annuelle sont conservés, sans création ni suppression revendiquée d'un second rapport.",
    "Les coûts réels du rapport et de sa circulation ne sont pas établis. Le maintien ne préjuge pas des documents qui peuvent satisfaire simultanément plusieurs besoins d'information.",
    "Aucune charge nouvelle n'est identifiée : mêmes auteurs, contenu et destinataires ; ni modèle annuel, ni certification, ni dépôt administratif supplémentaire."
)

retain(
    'L2343-11',
    "Maintien intégral du droit de réunion préparatoire sans présence de la direction, ouvert aux représentants ou au bureau élargi. Cette préparation indépendante rend le consentement et la consultation effectifs ; elle ne peut être supprimée comme un doublon de la réunion avec l'employeur. L'article confère un droit et n'impose pas une réunion préparatoire systématique, un rapport, une autorisation ou un calendrier supplémentaire.",
    "L2343-4 et son droit de participation des membres directement concernés ont été relus ; L2343-7 vérifié pour le bureau. La réduction facultative des délais de L2343-10 proposée dans le lot reste subordonnée à un temps suffisant pour cette préparation. Cadre européen : réunion sans direction, annexe I de la directive 2009/38/CE, version consolidée non jointe. Les frais et rémunérations des réunions conservent leurs fondements propres.",
    "Aucune suppression par rapport à la source entière : la faculté de préparation autonome et l'élargissement du bureau sont préservés, y compris pour les futurs représentants.",
    "Le maintien ne transforme pas cette faculté en séance obligatoire et ne chiffre pas un coût de réunion évité. Il reste distinct des délais de rupture individuelle.",
    "Aucune charge nouvelle n'est identifiée : aucun ordre du jour, procès-verbal, délai, autorisation de réunion ou déclaration supplémentaire n'est introduit."
)

retain(
    'L2343-12',
    "Maintien intégral de la restitution aux représentants locaux ou, à défaut, à tous les salariés de la teneur et des résultats de la consultation du comité sans accord. La confidentialité est conservée. L2342-10-1 vise le comité créé par accord : ces champs alternatifs ne créent pas une double déclaration à retirer. La restitution est nécessaire à l'utilité de la représentation européenne pour les salariés concernés et n'impose aucun rapport formel distinct.",
    "L2344-8 a été lu sur le secret et la discrétion des membres du comité sans accord et des experts. L2342-10-1 a été comparé intégralement, sans fusion des deux champs. Aucune limitation aux contrats ou représentants antérieurs n'est introduite. Coordination européenne à examiner : article 10 de la directive 2009/38/CE, consolidation non jointe.",
    "La source officielle entière est maintenue : information des salariés représentés, destinataire subsidiaire et limites de confidentialité demeurent. Aucun dépôt redondant n'est supprimé fictivement.",
    "Le mode de restitution et ses coûts ne sont pas documentés. Le maintien n'introduit pas de rapport périodique distinct et ne certifie pas la consolidation du droit de l'Union.",
    "Aucune charge nouvelle n'est identifiée : ni destinataire administratif nouveau, ni modèle, ni périodicité, ni justificatif de diffusion supplémentaire."
)

retain(
    'L2343-13',
    "Maintien intégral du libre choix des experts par le comité ou son bureau et de la prise en charge des frais d'un expert par l'entreprise ou la dominante. L'expertise contribue à une consultation éclairée face à des données économiques transnationales ; supprimer la prise en charge rendrait cette assistance inaccessible à certains représentants. Le texte ne prévoit ni agrément, ni déclaration, ni financement obligatoire de tous les experts choisis : aucune de ces charges ne peut être réputée supprimée.",
    "Relire les deux alinéas ensemble : assistance possible par plusieurs experts, mais prise en charge légale des frais de l'intervention d'un expert. Articulation avec L2343-14 vérifiée pour les dépenses générales et avec L2344-8 pour la confidentialité. Cadre européen : assistance et financement dans l'annexe I de la directive 2009/38/CE, consolidation non jointe. Les engagements conventionnels plus favorables ne sont pas fermés pour l'avenir.",
    "Aucun changement par rapport à la source entière : libre assistance et financement d'un expert restent applicables. Aucune baisse de dépense d'expertise ni de prélèvement n'est revendiquée.",
    "Le tarif, le volume des expertises et les éventuels accords plus favorables ne sont pas fournis ; aucun gain financier ou plafonnement supplémentaire n'est démontré.",
    "Aucune charge nouvelle n'est identifiée : aucun agrément d'expert, plafond tarifaire, justificatif spécial, expert supplémentaire financé ou accord préalable nouveau n'est imposé."
)

retain(
    'L2343-14',
    "Maintien intégral du financement du fonctionnement et des moyens nécessaires du comité, avec la liste des frais de réunion, interprétariat, séjour et déplacement et la réserve des conventions différentes. Ces dépenses permettent une représentation effective au-delà des frontières ; il ne s'agit pas d'une taxe accessoire ni d'une déclaration en double. Les supprimer transférerait les frais aux représentants et fragiliserait leur accès aux travaux. L'option conventionnelle existante reste ouverte.",
    "Les trois alinéas ont été relus, notamment « nécessaires », la dominante du groupe, le comité et son bureau et « sauf s'il en a été convenu autrement ». L2343-13 maintient séparément le financement d'un expert. La dispense consensuelle de certaines traductions écrites de L2343-17 proposée dans ce lot ne retire pas la prise en charge de l'interprétariat nécessaire aux réunions. Cadre européen : dépenses et moyens dans l'annexe I de la directive 2009/38/CE, consolidation non jointe.",
    "Aucune réduction par rapport à la source entière : financement et souplesse conventionnelle demeurent. Aucun transfert des frais vers les salariés n'est présenté comme une économie.",
    "Les montants des moyens nécessaires et les coûts réels ne sont pas établis. Le maintien ne promet ni budget forfaitaire nouveau ni baisse nette de dépense nationale.",
    "Aucune charge nouvelle n'est identifiée : mêmes débiteurs et catégories de dépenses, sans relevé périodique, minimum budgétaire, procédure de validation ou droit d'accès aux données nouveau."
)

retain(
    'L2343-15',
    "Maintien intégral du temps nécessaire au secrétaire et aux membres du bureau, de la limite de cent vingt heures annuelles par personne sauf circonstances exceptionnelles, du paiement à échéance normale, de l'absence d'imputation des séances et du recours au juge par l'employeur contestant l'usage. Ces droits garantissent un mandat effectif et le recours juridictionnel ; les supprimer ne serait pas le retrait d'une formalité administrative. Le plafond ordinaire demeure sans hausse ni baisse arbitraire.",
    "Contrôle des quatre alinéas : 120 heures annuelles pour chacun, exception de circonstances exceptionnelles, séances du comité et réunions du bureau non déduites, saisine du juge judiciaire par l'employeur. L2343-16 maintient la rémunération du temps de réunion des autres membres. Ni le seuil de 40 heures des nouveaux contrats ni l'indemnité ordinaire de rupture ne modifient ces garanties de mandat. Les droits valent également pour les futurs titulaires.",
    "La source officielle entière reste applicable : temps de délégation, rémunération, exception, exclusion des réunions du décompte et contrôle du juge sont maintenus sans allègement revendiqué.",
    "Aucun nombre d'heures réellement consommées ni coût salarial n'est documenté. Les dispositifs de temps de travail et de rupture du contrat conservent leur champ distinct.",
    "Aucune charge nouvelle n'est identifiée : pas d'heure supplémentaire de délégation, relevé obligatoire, justificatif de mission, autorisation préalable ou procédure contentieuse ajouté."
)

retain(
    'L2343-16',
    "Maintien intégral de la qualification du temps de réunion comme temps de travail et de son paiement à échéance normale. Ce droit évite que l'exercice du mandat européen soit financé par une perte de salaire. Il ne double pas le crédit de cent vingt heures : L2343-15 précise précisément que les séances n'y sont pas imputées pour le secrétaire et le bureau. Aucun prélèvement, agrément, délai minimal ni document redondant n'est prévu par cet article.",
    "L2343-15 a été comparé en entier : crédit de délégation et temps de séance ont des objets distincts. Préserver la rémunération de tous les membres et son échéance, sans limitation aux mandats ou contrats anciens. Ne pas traiter ce salaire comme l'indemnité ordinaire de rupture dont la première année est réformée. Cadre européen de protection des représentants à coordonner, notamment article 10 de la directive 2009/38/CE, consolidation non jointe.",
    "Aucune modification de la source officielle entière : le salaire du temps de réunion reste dû à échéance normale. Aucun gain de cotisation ou de coût de rupture n'est imputé à ce maintien.",
    "Le volume des réunions et leur coût ne sont pas chiffrés. Les règles générales de décompte du travail et les autres protections des représentants ne sont pas réécrites ici.",
    "Aucune charge nouvelle n'est identifiée : maintien du salaire existant sans registre, état mensuel, justificatif de présence spécial ou échéance de paiement nouvelle."
)

retain(
    'L2343-18',
    "Maintien intégral du réexamen après quatre ans du choix entre comité subsidiaire et négociation d'un accord, du pouvoir de négociation des membres, de la convocation dans les six mois et de la continuité du comité. Ce réexamen protège une alternative conventionnelle favorable et la continuité de la représentation ; sa suppression fermerait une voie de négociation. La source n'impose pas explicitement une réunion matériellement distincte de la réunion annuelle : aucun doublon de séance n'est tenu pour acquis.",
    "L2343-1, L2342-2 et L2342-9 ont été lus intégralement. Vérifier les quatre ans depuis l'institution, puis les six mois depuis ce terme ; l'instance demeure jusqu'à renouvellement ou remplacement. Il s'agit de la durée d'une organisation représentative, pas d'un terme d'emploi ou d'un CDD réintroduit. Cadre européen à coordonner : réexamen quadriennal dans l'annexe I de la directive 2009/38/CE ; version consolidée non jointe.",
    "Les quatre alinéas de la source officielle sont maintenus : choix de négocier, compétence des membres et absence de vide de représentation demeurent. Aucune seconde réunion obligatoire n'est fictivement supprimée.",
    "Aucun effet budgétaire ni raccourcissement de négociation n'est démontré. Le maintien ne confond pas renouvellement de l'instance et renouvellement du contrat d'un salarié.",
    "Aucune charge nouvelle n'est identifiée : pas de réexamen supplémentaire, nouvelle saisine, dossier de renouvellement ou délai de carence ajouté."
)

retain(
    'L2343-19',
    "Maintien intégral de la faculté d'aménager par accord le fonctionnement du comité de groupe lorsqu'un comité européen existe, sous réserve d'un vote favorable du comité de groupe. Cette faculté permet déjà de réduire des chevauchements tout en protégeant le consentement de l'instance concernée. Supprimer le vote supprimerait une garantie collective ; supprimer l'article retirerait l'outil d'aménagement. Aucune autorisation administrative ni rapport récurrent ne s'y ajoute.",
    "L2342-2 a été lu pour le premier accord possible ; L2334-1 à L2334-3 lus pour le fonctionnement propre du comité de groupe. L'accord européen ne supprime pas automatiquement l'instance nationale et l'accord passé au sein du groupe demeure une seconde voie. Le vote favorable et le caractère facultatif sont conservés pour les accords futurs ; ne pas importer les suppressions du circuit CPPNI de L2232 dans cet objet différent.",
    "Aucune réduction nouvelle par rapport à la source entière : l'aménagement conventionnel existant est maintenu avec le consentement du comité de groupe, sans fusion imposée des deux instances.",
    "Aucun accord concret ni doublon effectivement retiré n'est fourni. Le maintien d'une faculté d'aménagement ne prouve donc pas une baisse de réunions ou de dépenses.",
    "Aucune charge nouvelle n'est identifiée : mêmes deux voies d'accord et même vote favorable, sans homologation, dépôt particulier, rapport ou majorité additionnelle."
)

retain(
    'L2344-1',
    "Maintien intégral de l'habilitation réglementaire de répartition des sièges et de la possibilité d'associer sans droit de vote des salariés d'autres Etats. La représentation proportionnée exige une règle commune ; renvoyer à un décret n'est pas imposer un agrément à chaque entreprise. L'association facultative conserve une ouverture favorable sans modifier les équilibres de vote. Aucune déclaration, pièce redondante, taxe ou délai minimal n'est imposé par cet article.",
    "L2341-1 et R2344-1 ont été lus en entier : seuil d'entreprise de 1000 salariés et établissements de 150 dans au moins deux Etats ; échelle d'un à dix sièges par Etat suivant les dix tranches d'effectif. Ne pas lire dix sièges comme un plafond global du comité. Le premier alinéa mentionne aussi des minima et maxima : ne pas inventer de bornes globales absentes du règlement consulté. L2344-2 à L2344-7 lus pour la désignation et le recours. Cadre européen : répartition des sièges, directive 2009/38/CE, article 5 et annexe I, consolidation non jointe.",
    "Aucune réduction au regard de la source officielle entière : habilitation et association facultative de salariés hors des Etats visés demeurent, avec exclusion de leur droit de vote.",
    "Le lot ne modifie pas le barème réglementaire ni les seuils européens. Il ne démontre aucun gain de siège, de coût électoral ou de délai et ne certifie pas la consolidation européenne.",
    "Aucune charge nouvelle n'est identifiée : pas de siège obligatoire additionnel, élection nouvelle, agrément par entreprise ou déclaration d'association supplémentaire."
)


agenda_paragraphs = [
    "L'ordre du jour de la réunion annuelle du comité d'entreprise européen est arrêté par le président et le secrétaire. Il est communiqué aux membres du comité quinze jours au moins avant la séance.",
    "A défaut d'accord sur le contenu de l'ordre du jour, celui-ci est fixé par le président et communiqué aux membres du comité dix jours au moins avant la date de la réunion.",
    "Les délais de quinze jours et de dix jours prévus aux deux premiers alinéas peuvent être réduits par l'accord libre, exprès et unanime du président et des représentants des salariés au comité pour la réunion concernée, si les informations et documents nécessaires sont disponibles et si les représentants disposent d'un temps suffisant pour les examiner, se réunir sans la direction et préparer la consultation. Le silence ne vaut pas accord. Cette réduction ne vaut ni accord sur le contenu de l'ordre du jour ni renonciation aux droits d'information et de consultation prévus aux articles L. 2341-6 et L. 2341-7.",
    "Le troisième alinéa s'applique aux ordres du jour communiqués à compter de l'entrée en vigueur de la loi. Les communications antérieures et les droits qui en résultent restent régis par les dispositions antérieures.",
]
decisions['L2343-10'] = {
    'proposed_xml': ''.join('<p>' + value + '</p>' for value in agenda_paragraphs),
    'reason': "Réforme de fond ciblée : retirer le caractère incompressible des délais de quinze ou dix jours de communication de l'ordre du jour lorsque le président et tous les représentants des salariés acceptent librement et expressément une réunion plus proche et disposent réellement du temps et des documents nécessaires. Les deux alinéas sources sont maintenus comme règle par défaut ; le pouvoir de fixation subsidiaire du président ne s'étend pas à une réduction unilatérale des délais. La préparation sans direction et les droits d'information et de consultation restent entiers. La transition réserve les communications antérieures. Aucun nouveau délai chiffré ni régime de préavis individuel n'est introduit.",
    'review_notes': "L2341-6, L2341-7 et L2343-11 ont été lus en entier : dialogue, évaluation approfondie et préparation autonome restent les conditions effectives de l'option. L2343-9 est inchangé ; aucun autre article du corpus travail consulté ne renvoie expressément à L2343-10. Il s'agit de délais de communication d'un ordre du jour collectif, non des quinze jours calendaires de rupture du contrat unique. Les jours ne sont pas qualifiés dans la source ; aucune conversion en jours ouvrables n'est faite. Respecter les stipulations conventionnelles autonomes applicables et les recours, sans faire du silence une acceptation ni créer un formulaire de renonciation. Cadre européen à coordonner : information et consultation utiles de la directive 2009/38/CE ; version consolidée et éventuelles modifications non jointes localement, conformité actuelle non attestée. La réduction n'est possible que pour une réunion déterminée, pas par renonciation générale anticipée.",
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Suppression conditionnelle du minimum incompressible de quinze jours avant la réunion annuelle, lorsque tous les intéressés consentent expressément à sa réduction dans les conditions protectrices du nouvel alinéa.",
        "Suppression conditionnelle du minimum incompressible de dix jours en cas de désaccord sur le contenu de l'ordre du jour, sans permettre au président de réduire seul ce délai ni assimiler l'accord de calendrier à un accord sur le contenu.",
    ],
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à la source officielle entière, les minima de quinze et dix jours cessent d'être absolus : une réduction librement et unanimement acceptée devient possible pour une réunion identifiée. Le gain est un assouplissement de calendrier collectif, non une suppression de consultation, de salaire ou de prélèvement.",
        'scope_limitations': "Les minima restent applicables sans accord valable ou sans préparation suffisante. Aucun nombre uniforme de jours gagnés, coût net ou effet global n'est démontré. Les communications antérieures et les obligations conventionnelles autonomes restent à leur régime ; le cadre européen consolidé reste à vérifier.",
        'new_burdens_review': "Aucune charge nouvelle autonome n'est identifiée : l'accord libre et unanime ne conditionne que l'option nouvelle de réduction, sans modifier la voie existante ni imposer registre, attestation ou dépôt. La disponibilité des informations et le temps suffisant reprennent les garanties de L2341-6, L2341-7 et L2343-11. La recherche d'un accord peut avoir un coût pratique non chiffré ; aucun solde global des codes n'est affirmé.",
        'effects': [{
            'kind': 'deadline_reduced',
            'measure_id': 'cee-ordre-du-jour-delais-assouplis',
            'description': "Dérogation consensuelle aux deux minima de communication de l'ordre du jour annuel du comité européen sans accord, avec préparation effective garantie.",
            'before': "Ordre du jour arrêté conjointement : au moins quinze jours avant la séance ; ordre du jour fixé par le président faute d'accord sur son contenu : au moins dix jours avant la réunion. La source ne prévoit pas de faculté expresse de réduction et ne qualifie pas les jours.",
            'after': "Mêmes minima par défaut ; pour la réunion concernée, délai inférieur possible sans nouveau minimum chiffré avec accord libre, exprès et unanime du président et des représentants des salariés, informations disponibles et temps de préparation suffisant. Aucun délai de rupture individuelle n'est modifié.",
            'unit': 'other',
            'affected_population': "Président et représentants des salariés des comités d'entreprise européens institués en l'absence d'accord soumis au chapitre III.",
            'conditions_and_transition': "Ordres du jour communiqués à compter de l'entrée en vigueur de la loi ; communications antérieures sous droit antérieur. Ni silence, ni seul pouvoir patronal de fixation du contenu ne valent consentement à la réduction. Préparation autonome et information-consultation effectives demeurent.",
            'replacement_or_new_burdens': "Pas de délai de remplacement, formulaire, dépôt ou registre ; accord requis seulement pour utiliser l'option. Le temps nécessaire à sa recherche n'est pas chiffré.",
            'source_quote': plain(by_number['L2343-10']['source_xml']),
            'proposed_quote': agenda_paragraphs[2],
        }],
    },
}


language_paragraphs = [
    "Les documents communiqués aux représentants des salariés comportent une version en français.",
    "Par dérogation au premier alinéa, les représentants des salariés peuvent, par leur accord libre, exprès et unanime portant sur des documents identifiés, accepter de recevoir ces documents dans une autre langue qu'ils maîtrisent, sans version en français. Chacun d'eux peut, à tout moment, retirer son accord ou demander une version en français ; celle-ci est alors communiquée à l'ensemble des représentants sans frais et en temps utile pour leur permettre d'examiner les informations et de préparer la consultation. Le silence ne vaut pas acceptation. La dérogation cesse pour les documents concernés dès la désignation d'un nouveau représentant, sauf accord de celui-ci dans les mêmes conditions.",
    "Les obligations prévues à l'article L. 1321-6 demeurent applicables.",
    "Les deuxième et troisième alinéas s'appliquent aux documents communiqués à compter de l'entrée en vigueur de la loi. Les documents communiqués antérieurement restent soumis aux dispositions antérieures.",
]
decisions['L2343-17'] = {
    'proposed_xml': ''.join('<p>' + value + '</p>' for value in language_paragraphs),
    'reason': "Réforme de fond : retirer l'obligation de produire systématiquement une version française pour les seuls documents identifiés que tous les représentants acceptent librement et expressément de recevoir dans une autre langue effectivement maîtrisée. La règle française de la source est conservée par défaut. Chaque représentant conserve, sans frais et à tout moment, la faculté d'obtenir la version française pour tous, en temps utile ; le silence et l'arrivée d'un nouveau représentant ne permettent pas de prolonger une dispense non acceptée. Le renvoi ajouté à L1321-6 réserve des obligations légales autonomes déjà existantes, sans les élargir. Les communications antérieures restent à leur régime. Il ne s'agit ni d'une suppression des moyens d'interprétariat ni d'une réduction du salaire.",
    'review_notes': "L1321-6 lu intégralement dans le corpus : règlement intérieur, documents comportant des obligations pour le salarié ou nécessaires à l'exécution du travail, avec ses exceptions propres relatives aux documents reçus de l'étranger ou destinés à des étrangers. La nouvelle option ne déroge pas à ce régime distinct. L2341-6, L2341-7, L2343-11 et L2343-14 lus : compréhension, préparation et interprétariat nécessaire restent protégés ; la demande d'une seule personne rétablit la version française pour tous. Aucun autre renvoi exprès à L2343-17 n'a été relevé dans le corpus travail consulté. Examiner l'articulation extérieure avec la loi n° 94-665 du 4 août 1994 relative à l'emploi de la langue française, dont le texte intégral n'est pas joint ; aucune réécriture de cette loi n'est prétendue. Le cadre européen d'information-consultation intelligible doit être confronté à la directive 2009/38/CE consolidée et à ses éventuelles modifications, non jointes. La dispense ne vaut pas renonciation générale pour les documents futurs non identifiés.",
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': [
        "Suppression de l'obligation automatique de produire une version française pour les documents identifiés unanimement acceptés dans une autre langue maîtrisée, sous réserve des obligations légales autonomes et du rétablissement de la version française à la demande d'un seul représentant.",
    ],
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à la source officielle entière, une version française cesse d'être systématiquement obligatoire pour un sous-ensemble de documents unanimement accepté dans une langue maîtrisée. Le droit individuel de rétablir gratuitement la version française demeure effectif ; le volume de traductions réellement évitées et leur coût ne sont pas chiffrés.",
        'scope_limitations': "Aucune dispense sans consentement de tous, pour une personne ne maîtrisant pas la langue, pour un document non identifié ou lorsque L1321-6 impose le français. Les communications antérieures, l'interprétariat de réunion et les autres textes sur la langue restent à leur champ ; leur coordination extérieure n'est pas déclarée achevée.",
        'new_burdens_review': "Aucune charge nouvelle autonome n'est identifiée : l'unanimité et la maîtrise de la langue conditionnent seulement une dispense facultative, sans attestation linguistique, registre ou dépôt imposé. La fourniture gratuite sur demande reste incluse dans l'obligation française initiale plus large ; le renvoi à L1321-6 préserve un droit existant. Le coût pratique du recueil des accords et le solde global de complexité ne sont pas chiffrés.",
        'effects': [{
            'kind': 'obligation_removed',
            'measure_id': 'cee-traduction-francaise-option-consentie',
            'description': "Retrait conditionnel de la production automatique d'une version française, sans fermeture du droit de l'obtenir et sans dispense des obligations linguistiques autonomes.",
            'before': "Tous les documents communiqués aux représentants des salariés doivent comporter une version française ; l'article ne prévoit aucune acceptation substitutive d'une autre langue.",
            'after': "Version française toujours obligatoire par défaut. Dispense seulement pour des documents identifiés avec accord libre, exprès et unanime des représentants maîtrisant l'autre langue ; une demande individuelle rétablit la version pour tous, gratuitement et en temps utile. L1321-6 reste applicable.",
            'unit': 'legal_duty',
            'affected_population': "Entreprises et représentants des salariés des comités d'entreprise européens institués sans accord auxquels s'applique L2343-17.",
            'conditions_and_transition': "Documents communiqués à compter de l'entrée en vigueur de la loi ; droit antérieur pour les communications précédentes. Pas de consentement tacite ; retrait possible à tout moment ; nouveau représentant tenu de consentir pour que la dispense se poursuive sur les documents concernés.",
            'replacement_or_new_burdens': "Aucun agrément, test de langue, attestation, registre ou déclaration de remplacement. La traduction rétablie sur demande et le respect de L1321-6 ne dépassent pas les obligations antérieures ; coûts de coordination des consentements non mesurés.",
            'source_quote': plain(by_number['L2343-17']['source_xml']),
            'proposed_quote': language_paragraphs[1],
        }],
    },
}


assert len(sources) == 24
assert set(decisions) == set(by_number)
answer = []
for source in sources:
    identity = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    answer.append({**identity, **decisions[source['number']]})
(ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'articles': len(answer), 'rewritten': sum(x['status'] == 'rewrite_draft' for x in answer), 'retained': sum(x['status'] == 'retained_unchanged' for x in answer)}, ensure_ascii=False))
