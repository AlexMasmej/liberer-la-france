import json
from html import escape
from pathlib import Path


sources = json.loads(Path('source.json').read_text())


def xml(paragraphs):
    return '\n'.join('<p>' + escape(p, quote=False) + '</p>' for p in paragraphs)


def base(index):
    source = sources[index]
    return {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}


answer = []

a = base(0)
a.update(
    proposed_xml=xml([
        "I. — Lorsqu'un immeuble bâti à usage d'habitation ou à usage mixte professionnel et d'habitation, ou un immeuble non bâti constructible, situé dans une zone de bruit définie par un plan d'exposition au bruit est vendu ou loué, le vendeur ou le bailleur communique au futur acquéreur ou locataire un document l'informant de cette situation, selon les modalités du II.",
        "Ce document comporte :",
        "1° L'indication claire et précise de la zone concernée ;",
        "2° L'adresse du service d'information en ligne permettant de consulter le plan d'exposition au bruit ;",
        "3° La mention de la possibilité de consulter ce plan à la mairie de la commune où se situe l'immeuble.",
        "Les locations mentionnées au premier alinéa du présent I sont celles qui relèvent de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986.",
        "II. — Ce document est :",
        "1° Intégré au dossier de diagnostic technique annexé, selon le cas, à la promesse de vente ou, à défaut de promesse, à l'acte authentique de vente et au contrat de location, ou annexé à ces actes si la vente porte sur un immeuble non bâti ;",
        "2° Annexé à l'acte authentique de vente et, le cas échéant, au contrat préliminaire en cas de vente en l'état futur d'achèvement.",
        "Les obligations d'intégration ou d'annexion prévues aux 1° et 2° sont également satisfaites lorsque toutes les informations du I figurent de manière identifiable dans un autre document déjà intégré au dossier de diagnostic technique ou annexé à l'acte concerné, ou directement dans cet acte. Aucun document distinct ni aucune attestation supplémentaire ne sont alors exigés pour ces mêmes informations.",
        "Lorsque ces informations ont déjà été communiquées au même acquéreur dans la promesse de vente ou le contrat préliminaire, ou en annexe à l'un de ces actes, et qu'elles sont inchangées, aucune nouvelle annexion, reproduction, confirmation ni mention de leur remise n'est exigée dans l'acte authentique. Si elles ont changé, seules les informations devenues inexactes ou incomplètes sont actualisées dans cet acte ou dans une annexe, sans nouvelle reproduction des informations demeurées valables.",
        "III. — Les informations prévues au I n'ont qu'une valeur indicative, quel que soit le support admis au II. L'acquéreur ou le locataire ne peut s'en prévaloir à l'encontre du vendeur ou du bailleur.",
        "En cas de manquement à l'obligation prévue au II, l'acquéreur peut poursuivre la résolution du contrat ou demander au juge une diminution du prix.",
        "Les modalités de regroupement, de dispense de nouvelle annexion et d'actualisation prévues au II s'appliquent aux actes conclus à compter de l'entrée en vigueur de la loi, même lorsque la promesse ou le contrat préliminaire est antérieur. Elles ne régularisent pas les manquements commis lors de la conclusion d'actes antérieurs et ne portent pas atteinte aux recours qui en résultent.",
    ]),
    reason=(
        "Réforme de fond documentaire, et non simple réécriture : maintien des dispenses acquises de document séparé et de réannexion des informations inchangées déjà remises au même acquéreur. La seconde passe retire en outre le renvoi que le brouillon exigeait encore dans l'acte authentique et le renvoi aux informations antérieures lors d'une mise à jour partielle : aucune confirmation, mention de remise ou reproduction des éléments encore exacts n'est nécessaire. Cette coupe supplémentaire porte sur le brouillon ; elle n'est pas comptée comme une troisième obligation autonome de la source officielle supprimée. Les informations peuvent figurer directement dans l'acte ou dans un support déjà présent, sans attestation de remplacement. Le champ immobilier et locatif, les trois informations, les deux voies d'annexion sous ces dispenses, la valeur indicative et le recours spécial de l'acquéreur restent à droit constant. L'identification de la zone et l'accès au plan sont nécessaires au consentement sur une exposition durable au bruit ; la possibilité de consultation en mairie protège aussi les personnes sans accès numérique. Ni leur suppression ni celle du recours ne se justifient par la seule origine SRU alléguée. Aucune taxe, expertise acoustique nouvelle, autorisation ou déclaration administrative n'est instituée."
    ),
    review_notes=(
        "Source entière, notes vides et previous_draft entier relus ; I, II, III, listes 1° à 3° et 1° à 2° conservés. Le 2° du II continue de viser l'acte authentique de vente et, le cas échéant, le contrat préliminaire de VEFA ; il n'est pas rétréci aux seules ventes en VEFA. La dispense ne vaut que pour le même acquéreur effectivement informé et des données inchangées ; la seule publication du plan n'équivaut pas à cette communication. Les changements sont communiqués sans imposer de réannexer le reste. CCH L271-4 et L271-5, sources et notes lues en entier : coordonner le 10° du I de L271-4 et les modalités de son dossier afin qu'ils admettent expressément le support commun, l'information dans l'acte et la dispense de répétition, sans toucher aux autres diagnostics, aux restrictions aux logements ou locaux mixtes, ni aux sanctions propres. Le 10° n'entre pas dans la liste des durées de validité de L271-5 ; aucune durée n'est créée. Le III maintient la valeur indicative pour les seules informations de bruit, sans l'étendre à tout le contenu de l'acte. L'asymétrie source du recours spécial, réservé à l'acquéreur, demeure ; les recours locatifs autonomes ne sont pas retirés. Hors des cinq codes, l'article 3-3 de la loi 89-462 et les éventuels modèles réglementaires sont à confronter pour éviter un document séparé ou une annexion redondante ; ces textes ne sont pas fournis ici et ne sont pas présentés comme réécrits. Actes futurs couverts même après un avant-contrat ancien, recours pour manquements antérieurs préservés. SRU36 initial et sa piste LEGIARTI000006814938 lus : ils concernent L147-5, des possibilités de construire et de renouvellement urbain, non cette information contractuelle. L112-10 actuel, lu en entier, porte ces opérations et leurs conditions propres. La piste historique n'est présente que comme référence documentaire, pas comme article historique dans le corpus ; la filiation ne prouve donc pas une création SRU de L112-11. Aucun volet historique incertain ni l'examen des 209 articles n'est déclaré achevé. Aucune recette, économie nationale ou baisse d'impôt n'est revendiquée."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Obligation de produire un document de bruit distinct lorsque toutes les informations figurent déjà dans l'acte ou dans un document du dossier ou de ses annexes.",
        "Nouvelle annexion ou reproduction dans l'acte authentique des informations inchangées déjà communiquées au même acquéreur dans l'avant-contrat ; aucune mention ou attestation de remplacement n'est exigée.",
    ],
    substantive_impact={
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à l'ensemble de la source officielle, deux contraintes de support sont retirées dans leurs cas de redondance : document autonome et répétition à l'acte authentique. L'information elle-même reste obligatoire. Par rapport au previous_draft, le renvoi résiduel dans l'acte et le renvoi en cas d'actualisation partielle disparaissent aussi, sans comptage d'un gain supplémentaire par rapport au droit officiel.",
        'scope_limitations': "Sont seuls concernés les immeubles et baux définis au I. Le bénéfice de non-répétition suppose le même acquéreur et des informations inchangées ; un nouvel acquéreur doit être informé. Les autres diagnostics et les recours antérieurs restent distincts. La coordination de CCH L271-4 et des textes locatifs ou modèles extérieurs reste à réaliser ; aucun gain financier global ni achèvement de filiation SRU n'est établi.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée : ni formulaire, registre, attestation de remise, diagnostic, donnée ou délai nouveaux. L'actualisation ne porte que sur les informations déjà dues dont le contenu a changé ; elle remplace la répétition du document entier. Les supports communs restent facultatifs, les annexions ordinaires possibles et les recours existants maintenus. Le solde de complexité de l'ensemble des codes n'est pas chiffré.",
        'effects': [
            {
                'kind': 'obligation_merged',
                'measure_id': 'information-bruit-support-unique',
                'description': "Admission d'un support commun ou de l'information dans l'acte, sans état de bruit ni attestation distincts lorsque le contenu utile est déjà présent.",
                'before': "Pour les ventes ou locations du I, un document d'information comportant trois rubriques est intégré au dossier technique ou annexé aux actes visés au II ; aucune dispense expresse de support distinct ne figure dans la source.",
                'after': "Les mêmes trois rubriques peuvent figurer dans un document déjà intégré ou annexé, ou directement dans l'acte ; aucun document distinct ni attestation supplémentaire n'est dû.",
                'unit': 'legal_duty',
                'affected_population': "Vendeurs, bailleurs, acquéreurs et locataires des biens et locations relevant du I.",
                'conditions_and_transition': "Informations identifiables et complètes ; actes conclus dès l'entrée en vigueur, y compris après un avant-contrat antérieur ; manquements et recours antérieurs préservés.",
                'replacement_or_new_burdens': "Pas de pièce ou déclaration de remplacement ; le contenu informatif antérieurement obligatoire est maintenu.",
                'source_quote': "un document informant de cette situation est communiqué au futur acquéreur ou locataire dans les conditions prévues au II.",
                'proposed_quote': "Aucun document distinct ni aucune attestation supplémentaire ne sont alors exigés pour ces mêmes informations.",
            },
            {
                'kind': 'obligation_removed',
                'measure_id': 'information-bruit-support-unique',
                'description': "Dispense de nouvelle annexion à l'acte authentique des données inchangées déjà remises ; seules les données devenues inexactes ou incomplètes sont actualisées.",
                'before': "Le 2° du II exige l'annexion à l'acte authentique, ainsi que, le cas échéant, au contrat préliminaire de VEFA, sans dispense expresse lorsque le même acquéreur est déjà informé.",
                'after': "Aucune réannexion, reproduction, confirmation ou mention de remise pour les informations inchangées déjà communiquées au même acquéreur ; une mise à jour partielle ne fait pas reproduire le reste.",
                'unit': 'legal_duty',
                'affected_population': "Parties et rédacteurs d'un acte authentique précédé d'une promesse ou d'un contrat préliminaire avec le même acquéreur.",
                'conditions_and_transition': "Communication antérieure effective dans l'avant-contrat ou ses annexes ; absence de changement pour les données non répétées ; application aux actes futurs sans effacer un manquement passé.",
                'replacement_or_new_burdens': "Aucune attestation ni référence obligatoire à l'avant-contrat ne remplace l'annexion supprimée. La mise à jour reste limitée au contenu d'information déjà exigé.",
                'source_quote': "2° Annexé à l'acte authentique de vente et, le cas échéant, au contrat préliminaire en cas de vente en l'état futur d'achèvement.",
                'proposed_quote': "Lorsque ces informations ont déjà été communiquées au même acquéreur dans la promesse de vente ou le contrat préliminaire, ou en annexe à l'un de ces actes, et qu'elles sont inchangées, aucune nouvelle annexion, reproduction, confirmation ni mention de leur remise n'est exigée dans l'acte authentique.",
            },
        ],
    },
)
answer.append(a)

a = base(1)
a.update(
    proposed_xml=xml([
        "Le plan d'exposition au bruit est établi par l'autorité administrative compétente de l'État, après consultation :",
        "1° Des communes intéressées ;",
        "2° De l'Autorité de contrôle des nuisances aéroportuaires pour les aérodromes mentionnés à l'article L. 6360-1 du code des transports ;",
        "3° De la commission consultative de l'environnement compétente, lorsqu'elle existe, pour les autres aérodromes.",
        "Ces consultations sont engagées simultanément par l'autorité administrative compétente de l'État. La saisine de l'Autorité de contrôle des nuisances aéroportuaires et le cours du délai dont elle dispose pour rendre son avis ne sont pas subordonnés à la réception des avis des communes. Ces avis lui sont transmis dès qu'ils sont disponibles, sans nouvelle saisine ni recommencement de ce délai. Les délais propres aux consultations maintenues et les effets de leur expiration demeurent applicables.",
        "Pour les aérodromes mentionnés au 2°, aucun avis distinct de la commission consultative de l'environnement sur le projet de plan n'est requis pour l'établissement ou la révision du plan. Sa consultation sur les valeurs d'indices servant à délimiter les zones de bruit et ses missions de suivi demeurent régies par leurs dispositions propres.",
        "Le plan est soumis à une enquête publique réalisée conformément au chapitre III du titre II du livre Ier du code de l'environnement.",
        "Il est tenu à la disposition du public.",
        "Ces dispositions s'appliquent aux procédures engagées à compter de l'entrée en vigueur de la loi et, pour les étapes non accomplies, aux procédures en cours à cette date. Les consultations restant à engager le sont simultanément ; les avis déjà recueillis demeurent utilisables, sans nouvelle saisine ni recommencement des délais déjà ouverts. Aucun avis de la commission supprimé par le présent article ne reste exigible du seul fait que sa saisine est antérieure. Les plans approuvés conservent leurs effets ; les actes accomplis avant l'entrée en vigueur de la loi et les recours qui s'y rapportent demeurent régis par les dispositions qui leur étaient applicables. Ces dispositions ne reportent pas l'abrogation différée du présent article prévue par les textes antérieurs et n'emportent aucune remise en vigueur après cette abrogation.",
    ]),
    reason=(
        "Réduction de fond supplémentaire : le brouillon avait seulement parallélisé tous les avis ; la présente rédaction supprime réellement l'avis obligatoire distinct de la commission environnementale sur le projet pour les aérodromes soumis à l'ACNUSA. Il ne devient ni déclaration ni condition de recevabilité. Ce choix ne présente pas les deux objets comme identiques : la commission conserve sa consultation amont sur les valeurs des indices de bruit et son suivi ; l'avis indépendant de l'ACNUSA examine le projet, avec avis communaux, enquête publique et accès au plan maintenus. Ce second examen collégial obligatoire n'est donc pas retenu comme une étape indispensable dans ce seul champ. Pour les autres aérodromes, l'avis de la commission reste nécessaire, faute d'avis ACNUSA de substitution dans le dispositif. La suppression de l'enchaînement des consultations déjà acquise est conservée ; elle ne réduit pas les délais propres des avis maintenus. Le renvoi fiscal devenu incohérent est remplacé expressément par celui déjà employé depuis 2025 par R112-14 ; il s'agit d'un choix de coordination avec le périmètre réglementaire actuel, dont l'équivalence historique exacte reste à vérifier, et non d'une nouvelle baisse de prélèvement. La compétence de l'État, l'enquête et l'accès public sont maintenus à droit constant."
    ),
    review_notes=(
        "Source entière, ses deux notes et previous_draft entier lus. R112-6 à R112-17 et L112-5 à L112-15 lus dans le corpus, sources et notes comprises. Coordonner impérativement R112-13 et R112-14 : notification commune sans attente des deux mois communaux pour saisir l'ACNUSA ; retirer, dans le 1° de R112-14 et ses règles de saisine, le second avis obligatoire de commission pour les aérodromes du 2° législatif. Le délai de deux mois de la commission subsiste pour les autres aérodromes, ainsi que les deux mois communaux, les quatre mois de l'ACNUSA, les avis réputés favorables et le point de départ de dernière saisine en cas de plusieurs départements dans son champ. Aucune réduction forfaitaire du délai total n'est annoncée. R112-11 conserve son avis amont sur Lden, limite extérieure de C et, le cas échéant, de B ; R112-9 conserve l'examen au moins quinquennal et la faculté de proposer une révision. Ces objets différents ne sont pas qualifiés de doublons exacts. La suppression porte seulement sur le second avis du projet dans le champ ACNUSA et doit aussi s'appliquer aux saisines pendantes, sans recommencer les autres consultations. Maintien de l'enquête, de la motivation et de l'approbation de R112-15/16, de la publicité de R112-17, des compétences et accords ministériels distincts et des protections de défense de R112-6/15 ; ces autorisations distinctes ne sont pas supprimées par la mise en parallèle. Hors des cinq codes, les règles environnementales d'enquête et de participation citées par R112-15, notamment R571-59 et suivants, L123-19-8, L123-19-9 et R123-46, et les missions de l'ACNUSA restent à confronter. Aucun avis autonome d'autorité environnementale, évaluation ou participation imposé par le droit supérieur n'est supprimé au titre du second avis national ici retiré ; cette réserve ne vaut pas constat de conformité européenne. Incohérence documentaire explicite : le corps vise CGI1609 quatervicies A ; sa note attribue à tort ce numéro au CIBS et indique L422-31, L422-49 à L422-56 ; R112-14 depuis 2025 et L112-7 actuel emploient L6360-1 transports. Le nouveau 2° retient ce dernier renvoi de façon expresse, au lieu de maintenir le renvoi fiscal incohérent. Les articles cibles du CGI, du CIBS et des transports ne sont pas fournis dans le corpus autorisé ; l'identité historique des champs, et donc une éventuelle différence de population entre ces références, ne sont pas établies. Cette concordance reste un point de contrôle précis, pas un volet achevé. La source est ABROGE_DIFF avec fin de version au 1er janvier 2027 ; le texte de succession ou d'abrogation n'est pas joint. Le corps n'ajourne pas cette échéance ; une application après celle-ci exige une coordination expresse sur le support alors applicable, non réputée réalisée ici. SRU202 entier et piste LEGIARTI000006814934 lus : III et XXIV portent sur les documents d'urbanisme et l'annexion dans L147-3, pas la preuve d'une création de toutes les consultations ou de la règle transitoire actuelle. La version historique citée manque comme article source dans le corpus et n'a pas été réputée lue. Ni cette filiation ni les autres volets SRU202 ou les 209 articles ne sont déclarés achevés."
    ),
    status='rewrite_draft',
    change_type='normative_reduction',
    reform_policy_id='editorial_direction_2026_10_19',
    removed_provisions=[
        "Avis obligatoire distinct de la commission consultative de l'environnement sur le projet de plan pour les aérodromes soumis à l'avis de l'ACNUSA, y compris la collecte préalable de cet avis par celle-ci.",
        "Enchaînement obligatoire des consultations imposant d'attendre les avis communaux avant de saisir l'ACNUSA ou la commission compétente, dans la procédure d'application à coordonner.",
    ],
    substantive_impact={
        'version': 1,
        'classification': 'material_reduction',
        'assessment': "Par rapport à la source officielle entière, l'avis préalable distinct de la commission sur le projet cesse d'être obligatoire dans le champ ACNUSA. C'est une consultation effectivement retirée, alors que le brouillon la maintenait en parallèle. La conduite simultanée déjà proposée est conservée, sans compter un deuxième gain pour le même avis ni annoncer une diminution des durées propres des avis maintenus. Aucun prélèvement n'est concerné.",
        'scope_limitations': "La commission conserve l'avis du 3°, son rôle amont sur les indices et son suivi ; son second avis sur le projet n'est plus garanti dans le champ du 2°. L'enquête publique demeure mais n'est pas présentée comme juridiquement identique à ce second avis collégial. Les renvois réglementaires doivent être coordonnés. Le périmètre L6360-1 est celui du règlement actuel ; sa concordance historique avec le renvoi fiscal source n'est pas démontrée faute des textes cibles. L'abrogation différée au 1er janvier 2027 borne ce support ; la succession et la conformité aux exigences supérieures distinctes ne sont pas réputées vérifiées.",
        'new_burdens_review': "Aucune formalité, autorisation, donnée ou durée minimale nouvelle n'est identifiée. La simultanéité impose à l'État une organisation différente de saisines déjà obligatoires, en nombre réduit ; la transmission des avis communaux existait déjà dans R112-14. Aucune déclaration ne remplace l'avis supprimé. L'alignement du renvoi sur le règlement actuel nécessite toutefois le contrôle de périmètre indiqué : aucune absence d'extension de population n'est présumée démontrée. Le coût net administratif et le solde de l'ensemble des codes ne sont pas chiffrés.",
        'effects': [
            {
                'kind': 'obligation_removed',
                'measure_id': 'peb-consultations-sans-double-avis',
                'description': "Suppression de l'avis distinct obligatoire de la commission sur le projet de plan dans le champ ACNUSA, avec maintien de la consultation amont sur les indices et des consultations essentielles restantes.",
                'before': "L'ACNUSA devait recueillir au préalable l'avis de la commission compétente sur le projet pour les aérodromes désignés par le renvoi fiscal du 2° ; cette étape s'ajoutait à l'avis amont sur les indices de R112-11.",
                'after': "Pour les aérodromes du nouveau 2°, désignés par le renvoi L6360-1 déjà employé dans R112-14, l'avis distinct de la commission sur le projet n'est plus requis ; avis ACNUSA et communal maintenus, consultations conduites simultanément et délais propres inchangés. La commission reste consultée pour les autres aérodromes et conserve ses missions distinctes.",
                'unit': 'legal_duty',
                'affected_population': "Autorité administrative établissant ou révisant le plan, ACNUSA et commissions environnementales ; riverains et communes conservent l'enquête et les consultations restantes.",
                'conditions_and_transition': "Application aux nouvelles procédures et étapes non accomplies des procédures en cours ; avis déjà recueillis utilisables, aucune saisine pendante ne maintient l'avis supprimé, plans approuvés et recours antérieurs protégés. Pas de prorogation de l'abrogation différée ; concordance historique des catégories d'aérodromes à vérifier.",
                'replacement_or_new_burdens': "Aucun visa, dépôt ou déclaration de remplacement. La mise en parallèle réorganise les saisines existantes ; elle ne supprime ni les consultations amont distinctes ni l'enquête publique.",
                'source_quote': "2° De l'Autorité de contrôle des nuisances aéroportuaires pour les aérodromes mentionnés au I de l'article 1609 quatervicies A du code général des impôts, qui recueille au préalable l'avis de la commission consultative de l'environnement compétente ;",
                'proposed_quote': "Pour les aérodromes mentionnés au 2°, aucun avis distinct de la commission consultative de l'environnement sur le projet de plan n'est requis pour l'établissement ou la révision du plan.",
            },
            {
                'kind': 'coordination',
                'measure_id': 'peb-consultations-sans-double-avis',
                'description': "Remplacement explicite du renvoi fiscal incohérent par la catégorie employée par R112-14 actuel pour la saisine de l'ACNUSA ; aucune seconde suppression d'obligation ou de taxe comptée.",
                'before': "Référence législative au I de CGI1609 quatervicies A, note source annonçant une substitution CIBS et règlement actuel visant transports L6360-1.",
                'after': "Le 2° vise expressément L6360-1 transports, comme R112-14 depuis 2025. L'équivalence historique des populations de ces références reste à contrôler sur les textes cibles non joints.",
                'unit': 'other',
                'affected_population': "Aérodromes relevant du renvoi utilisé pour la consultation obligatoire de l'ACNUSA.",
                'conditions_and_transition': "Coordination du même dispositif consultatif, dans sa période d'application ; aucune remise en vigueur du support après son abrogation différée.",
                'replacement_or_new_burdens': "Pas de taxe ni de déclaration nouvelles. La différence éventuelle de périmètre par rapport à l'ancien renvoi fiscal n'est pas établie et reste explicitement signalée.",
                'source_quote': "pour les aérodromes mentionnés au I de l'article 1609 quatervicies A du code général des impôts",
                'proposed_quote': "pour les aérodromes mentionnés à l'article L. 6360-1 du code des transports",
            },
        ],
    },
)
answer.append(a)

a = base(2)
a.update(
    proposed_xml=None,
    reason=(
        "Maintien intégral nécessaire de la source officielle, sans nouvelle reformulation ni gain de simplification revendiqué. Le previous_draft ne modifiait que la rédaction ; il n'est pas repris comme une réforme. L'article reconnaît directement les anciens plans établis selon la directive d'aménagement national pendant l'attente de leur révision et évite de devoir les réétablir pour leur seule reconnaissance juridique. Après examen, il ne crée ni taxe, cotisation, agrément, déclaration, justificatif, autorisation ou délai minimal ; il n'impose pas davantage une révision périodique. Aucune donnée fournie ne démontre que tous les plans visés ont été révisés, de sorte que supprimer cette transition pourrait retirer sans justification leur fondement à des protections contre le bruit ou susciter une nouvelle procédure d'établissement. La reconnaissance maintient aussi le bénéfice des adaptations et opérations admissibles de la section, au lieu de lui substituer une interdiction absolue. La décision de coupes ne justifie donc aucune suppression supplémentaire de cet article."
    ),
    review_notes=(
        "Source entière de 286 caractères, notes vides et previous_draft entier lus puis comparés. Proposed_xml est null pour reproduction intégrale depuis la source ; aucun texte stylistique antérieur n'est compté comme réécrit. Le plan reconnu reste celui établi en application de la directive d'aménagement national relative à la construction dans les zones de bruit des aérodromes, jusqu'à sa révision : il ne s'agit pas d'une directive de l'Union. L112-5 à L112-16 et R112-6 à R112-17 ont été lus dans le corpus, sources et notes comprises ; R112-7 assure distinctement la continuité du plan pendant sa révision jusqu'à publicité de l'approbation. Les adaptations des indices de L112-8, le régime spécifique de L112-9 et les constructions ou opérations admises aux 1° à 5° de L112-10 restent ouverts dans leurs conditions propres, y compris aux situations futures éligibles. Le maintien ne ressuscite ni quota SRU, ni prélèvement de carence, ni nouveau dossier, et ne dépend pas de l'avis de commission supprimé au 2° de L112-16. Aucun renvoi entrant propre à L112-17 n'a été relevé dans les sources urbanisme et CCH ; les mentions homonymes du CRPA ne sont pas confondues avec cet article. SRU202 initial et sa piste documentaire ont été lus intégralement ; ses III et XXIV changent la terminologie et l'annexion dans L147-3, sans établir l'origine SRU de la présente reconnaissance transitoire. LEGIARTI000006814934 n'est pas fourni comme article historique dans le corpus ; ses occurrences documentaires ne prouvent pas son contenu. Les compléments autorisés ne fournissent pas cette version. La filiation reste incertaine, sans affirmation d'achèvement de ce volet ou de l'examen des 209 articles. Aucun audit de tous les plans encore concernés ni des obligations environnementales supérieures distinctes n'est prétendu réalisé."
    ),
    status='retained_unchanged',
    classification='retained_necessary',
    substantive_impact={
        'version': 1,
        'classification': 'retained_necessary',
        'assessment': "La totalité de la source officielle est maintenue pour assurer la reconnaissance des anciens plans dans l'attente de leur révision. Cet article ne fixe aucune nouvelle procédure à accomplir ; sa suppression risquerait au contraire d'exiger un réétablissement ou de retirer le support de protections et de possibilités de construire encadrées. Aucun changement normatif, réduction de prélèvement ou simplification nouvelle n'est revendiqué.",
        'scope_limitations': "Seuls les plans issus de la directive nationale désignée par la source sont concernés, jusqu'à leur révision. L'inventaire des plans encore soumis à cette transition et sa filiation historique complète ne sont pas fournis. Le maintien ne modifie pas les effets propres du plan ni les autres régimes de bruit, d'évaluation ou de participation.",
        'new_burdens_review': "Aucune charge nouvelle n'est identifiée parce que le texte officiel est conservé sans ajout : pas de registre, données, certificat, renouvellement, délai ou condition supplémentaire. La reconnaissance des plans ne subordonne pas leur continuité à une formalité nouvelle. Aucun solde global de complexité ou d'économies n'est chiffré.",
        'effects': [],
    },
)
answer.append(a)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
