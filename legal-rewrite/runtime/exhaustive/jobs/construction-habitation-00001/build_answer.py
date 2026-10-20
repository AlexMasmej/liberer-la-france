import json
from pathlib import Path

source = json.loads(Path('source.json').read_text())
drafts = {}

def add(number, paragraphs, reason, review):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review,
    }

historical = " La note source relative à l’article 8 de l’ordonnance n° 2020-71 du 29 janvier 2020 et à l’échéance du 1er juillet 2021 est une indication historique d’entrée en vigueur ; elle ne fixe pas la date du présent projet."

add('L134-4', [
    "Les ascenseurs doivent faire l’objet d’un contrôle technique périodique de leur état de fonctionnement et de la sécurité des personnes.",
    "Une personne qualifiée ou compétente dans ce domaine réalise le contrôle technique. Elle doit être assurée contre les conséquences de sa responsabilité professionnelle liée au contrôle des ascenseurs. Elle ne doit avoir aucun lien susceptible de compromettre son impartialité et son indépendance, ni avec le propriétaire qui fait appel à elle, ni avec une entreprise susceptible d’effectuer des travaux sur un ascenseur ou d’en assurer l’entretien. Si elle est une personne morale, aucune part de son capital ne doit être détenue par une telle entreprise.",
    "Toute personne disposant d’un titre d’occupation dans l’immeuble peut obtenir du propriétaire de l’ascenseur la communication du rapport de contrôle technique ou de ses conclusions. Les frais de communication sont à la charge du demandeur.",
    "Dans les établissements mentionnés aux articles L. 4111-1 à L. 4111-3 du code du travail, les articles L. 4711-1 à L. 4711-5 du même code s’appliquent au rapport de contrôle technique."
], "Réécriture à droit constant : les obligations de contrôle, d’assurance et d’indépendance sont formulées directement. Les quatre alinéas distinguent toujours le contrôle, les garanties du contrôleur, la communication aux occupants titulaires d’un titre et l’application du code du travail. Aucune réforme de fond n’est introduite.",
    "Renvois au code du travail vérifiés dans le corpus public fourni. Maintien de l’interdiction de toute participation, même partielle, d’une entreprise de travaux ou d’entretien au capital du contrôleur personne morale, ainsi que de la communication aux frais du demandeur." + historical)

add('L134-5', [
    "Un décret en Conseil d’État définit :",
    "1° Pour l’ensemble des ascenseurs :",
    "a) Les mesures minimales d’entretien de l’ascenseur, les modalités de leur exécution et les moyens de justifier leur mise en œuvre ;",
    "b) La nature et le contenu des clauses obligatoires des contrats d’entretien, ainsi que les obligations des parties au début et au terme du contrat ;",
    "c) Les conditions dans lesquelles le propriétaire peut assurer l’entretien de l’ascenseur par ses propres moyens ;",
    "2° Pour les ascenseurs mis sur le marché avant le 27 août 2000 :",
    "a) Les exigences de sécurité applicables ;",
    "b) La liste des dispositifs de sécurité à installer ou les mesures équivalentes à prendre, notamment en fonction des risques liés à l’installation de l’ascenseur, à son mode d’utilisation et à son environnement ;",
    "c) Les conditions permettant de déroger à l’obligation d’installer des dispositifs de sécurité pour tenir compte de contraintes techniques exceptionnelles, de l’accessibilité ou de nécessités liées à la conservation du patrimoine historique ;",
    "3° Pour les ascenseurs mis sur le marché après le 26 août 2000 :",
    "a) Les exigences essentielles de sécurité et de santé applicables à la mise sur le marché des ascenseurs et des composants de sécurité pour ascenseurs ;",
    "b) Les instructions qui doivent accompagner les ascenseurs et les composants de sécurité pour ascenseurs ;",
    "4° Les procédures d’évaluation de la conformité aux exigences essentielles de sécurité et de santé, la procédure de notification des organismes chargés du contrôle de conformité et les obligations de ces organismes ;",
    "5° Le contenu du contrôle technique, notamment la liste des dispositifs et des exigences de sécurité contrôlés, sa périodicité, les modalités d’information auxquelles il donne lieu et les critères de qualification ou de compétence exigés de la personne qui en est chargée."
], "Réécriture à droit constant de l’habilitation réglementaire : les objets du décret sont exprimés plus directement, sans modifier l’ordre des 1° à 5° ni des lettres a) à c). Les deux générations d’ascenseurs, les mesures équivalentes et les motifs limités de dérogation sont conservés. Aucune réforme de fond n’est ajoutée.",
    "Contrôler dans le décret l’ensemble des objets conservés : entretien, clauses contractuelles, moyens propres, sécurité, instructions, conformité, notification, information et compétence. Les bornes avant le 27 août 2000 et après le 26 août 2000 restent distinctes et complémentaires ; aucune extension des dérogations n’est proposée." + historical)

add('L134-6', [
    "L’installation électrique se compose des matériels électriques fixes destinés à être sous tension ou à véhiculer un courant électrique.",
    "L’installation électrique doit satisfaire aux exigences suivantes :",
    "1° Sa conception et sa réalisation intègrent la sécurité des personnes afin de prévenir les risques de chocs électriques par contact direct ou indirect et les risques de brûlure, d’incendie ou d’explosion d’origine électrique ;",
    "2° Elle assure en toute sécurité le bon fonctionnement et la continuité de service ;",
    "3° Si elle est susceptible d’être raccordée au réseau de distribution d’électricité, elle est compatible avec les caractéristiques électriques de ce réseau."
], "Réécriture à droit constant : une phrase introductive annonce les trois exigences ; la condition de raccordement est placée au début du 3°, dans le même alinéa. La définition de l’installation, les risques à prévenir et la continuité de service sont conservés. Aucune réforme de fond.",
    "Maintien des seuls matériels électriques fixes dans la définition, des contacts directs et indirects et de la compatibilité requise dès que le raccordement est possible, sans attendre un raccordement effectif. Numérotation et place des trois exigences conservées." + historical)

add('L134-7', [
    "Lorsque l’installation intérieure d’électricité a été réalisée depuis plus de quinze ans, une évaluation de son état doit être produite pour apprécier les risques pour la sécurité des personnes dans les cas suivants :",
    "1° La vente de tout ou partie d’un immeuble à usage d’habitation, dans les conditions et selon les modalités prévues aux articles L. 271-4 à L. 271-6 ;",
    "2° La location d’un logement, dans les conditions fixées par l’article 3-3 de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986.",
    "Un décret en Conseil d’État fixe les modalités d’application du 1°."
], "Réécriture à droit constant : la répétition entre évaluation de l’état et évaluation des risques est supprimée ; les deux opérations déclenchant la production du document restent énumérées séparément. Le seuil de plus de quinze ans et le champ du décret sont conservés. Aucune réforme de fond.",
    "Articles L. 271-4 à L. 271-6 vérifiés dans le corpus : maintien du diagnostic électrique visé au 7° du I de L. 271-4 et de ses règles de validité et d’établissement. Le renvoi locatif à l’article 3-3 conserve ses deux références législatives complètes. Le décret mentionné au dernier alinéa ne concerne que le 1°." + historical)

add('L134-8', [
    "Les canalisations, appareils et matériels qui concourent à l’utilisation de gaz combustibles et qui sont installés, mis en service et utilisés dans un bâtiment doivent respecter les exigences essentielles de sécurité définies en application de l’article L. 557-4 du code de l’environnement. Ils doivent également être compatibles avec les exigences fonctionnelles du bâtiment, notamment en matière de sécurité contre les risques d’incendie, de ventilation et d’aération des locaux."
], "Réécriture à droit constant : la phrase unique est divisée en deux phrases distinguant la conformité des équipements aux exigences essentielles et leur compatibilité avec le bâtiment. Les deux obligations restent dans le même alinéa. Aucune réforme de fond.",
    "Renvoi à L. 557-4 du code de l’environnement conservé. La liste demeure non limitative avec « notamment » et garde séparément la ventilation et l’aération ; aucun allègement des exigences applicables au gaz n’est créé." + historical)

add('L134-9', [
    "Lorsque l’installation intérieure de gaz en fonctionnement a été réalisée depuis plus de quinze ans, une évaluation de son état doit être produite pour apprécier les risques pour la sécurité des personnes dans les cas suivants :",
    "1° La vente de tout ou partie d’un immeuble à usage d’habitation, dans les conditions et selon les modalités prévues aux articles L. 271-4 à L. 271-6 ;",
    "2° La location d’un logement, dans les conditions fixées par l’article 3-3 de la loi n° 89-462 du 6 juillet 1989 tendant à améliorer les rapports locatifs et portant modification de la loi n° 86-1290 du 23 décembre 1986.",
    "Un décret en Conseil d’État fixe les modalités d’application du 1°."
], "Réécriture à droit constant : l’objet de l’évaluation et les deux cas de production sont énoncés directement. La rédaction conserve la condition d’une installation en fonctionnement, l’ancienneté de plus de quinze ans et le décret limité à la vente. Aucune réforme de fond.",
    "Articles L. 271-4 à L. 271-6 vérifiés dans le corpus : le diagnostic de gaz reste celui du 4° du I de L. 271-4, soumis aux règles de validité et d’établissement correspondantes. Maintien du renvoi locatif à l’article 3-3 avec les deux références législatives complètes. Ne pas supprimer la condition « en fonctionnement », propre au gaz." + historical)

add('L134-10', [
    "Les piscines privatives enterrées et non closes, qu’elles soient neuves ou existantes et à usage individuel ou collectif, doivent être équipées d’un dispositif de sécurité efficace destiné à prévenir le risque de noyade.",
    "La réglementation fixe les exigences fonctionnelles de ce dispositif. Elle détermine aussi comment le constructeur ou l’installateur informe le maître d’ouvrage des caractéristiques techniques et des conditions d’utilisation du dispositif retenu."
], "Réécriture à droit constant : le champ des piscines concernées est regroupé dans une phrase, puis le second alinéa distingue les exigences du dispositif et l’information du maître d’ouvrage. L’efficacité requise et les deux auteurs possibles de l’information sont conservés. Aucune réforme de fond.",
    "Les conditions « privatives », « enterrées » et « non closes » demeurent cumulatives. Conservation des piscines existantes comme neuves, des usages individuel et collectif, de la compétence réglementaire et de l’information sur le dispositif effectivement retenu." + historical)

add('L134-11', [
    "La conception, l’installation et le maintien en bon état de fonctionnement des portes et portails de garage automatiques ou semi-automatiques doivent éviter toute mise en danger des personnes lors d’une utilisation normale.",
    "Un décret en Conseil d’État fixe les modalités d’application du présent article. Il définit notamment les règles de sécurité, les mesures d’entretien nécessaires à leur respect et les modalités pratiques permettant de justifier l’exécution de cette obligation d’entretien."
], "Réécriture à droit constant : les trois étapes de protection des personnes deviennent le sujet de l’obligation ; le second alinéa distingue le renvoi au décret et son contenu. Les portes comme les portails et les deux modes d’automatisation restent couverts. Aucune réforme de fond.",
    "Maintien de la référence à une utilisation normale et de la justification effective de l’entretien. L’énumération des objets du décret demeure non limitative ; aucun responsable supplémentaire ni nouvelle périodicité n’est ajouté." + historical)

add('L134-12', [
    "La conception et la construction des bâtiments doivent éviter les chutes accidentelles de hauteur des personnes lors d’un usage normal.",
    "Cette exigence s’applique également aux structures provisoires et démontables pendant toute leur durée d’utilisation."
], "Réécriture à droit constant : l’obligation est rattachée directement à la conception et à la construction ; la reprise « Il en va de même » est remplacée par un renvoi explicite à cette exigence. Les deux alinéas et le champ temporel des structures sont conservés. Aucune réforme de fond.",
    "La condition d’usage normal reste applicable à l’exigence reprise au second alinéa. La formulation « structures provisoires et démontables » est conservée sans élargissement ni réduction de catégorie." + historical)

add('L134-13', [
    "La conception, la construction et l’équipement des bâtiments à usage professionnel doivent respecter les règles destinées à assurer la santé et la sécurité des travailleurs chargés de leur entretien.",
    "Un décret en Conseil d’État fixe les modalités d’application du présent article."
], "Réécriture à droit constant : les opérations soumises aux règles de protection deviennent le sujet d’une obligation explicite. Le champ reste celui des bâtiments professionnels et des travailleurs chargés de leur entretien ; le renvoi au décret est maintenu. Aucune réforme de fond.",
    "Conserver conjointement la santé et la sécurité ainsi que les trois opérations : conception, construction et équipement. L’article ne détermine pas à lui seul les obligations générales de l’employeur prévues par le code du travail." + historical)

add('L141-1', [
    "L’implantation, la conception, la construction, l’exploitation et l’entretien des bâtiments doivent poursuivre l’objectif de sécurité des personnes :",
    "1° En contribuant à prévenir le départ d’un incendie ;",
    "2° Si un incendie survient, en permettant de limiter son développement, sa propagation et ses effets sur les personnes, et en facilitant l’intervention des secours."
], "Réécriture à droit constant : les cinq étapes de la vie du bâtiment sont regroupées comme sujet de l’objectif ; les deux axes de prévention et de limitation des conséquences demeurent numérotés. L’obligation de contribuer à prévenir un incendie n’est pas transformée en garantie d’absence d’incendie. Aucune réforme de fond.",
    "Maintien de l’objectif général auquel renvoient L. 141-2 et L. 141-3. Développement, propagation, effets sur les personnes et intervention des secours demeurent quatre composantes distinctes du 2°." + historical)

add('L141-2', [
    "Un décret en Conseil d’État définit les règles de sécurité destinées à assurer le respect de l’objectif général fixé à l’article L. 141-1 lors de la construction, de l’aménagement, de la modification ou du changement d’usage :",
    "1° Des bâtiments à usage d’habitation ;",
    "2° Des bâtiments à usage professionnel ;",
    "3° Des établissements recevant du public.",
    "Des règles spécifiques sont définies pour les immeubles de moyenne hauteur et de grande hauteur, quel que soit leur usage."
], "Réécriture à droit constant : l’autorité réglementaire et la finalité des règles sont exprimées dès le début. Les quatre types d’opérations, les trois catégories numérotées et le régime spécifique des immeubles de moyenne et de grande hauteur sont conservés. Aucune réforme de fond.",
    "Conserver la distinction entre « changement d’usage » ici et « changement de destination » à L. 145-1 et L. 146-1. Renvoi à L. 141-1 et subdivisions inchangés. Le dossier coordonné prévu par la réécriture de L. 423-1 du code de l’urbanisme ne supprime pas ces exigences." + historical)

add('L141-3', [
    "Lorsqu’une solution d’effet équivalent au sens de l’article L. 112-6 est utilisée pour un bâtiment à construire, à modifier ou à aménager, le respect de l’objectif général de sécurité des personnes fixé à l’article L. 141-1 doit être justifié par des études d’ingénierie de sécurité incendie. Ces études doivent établir que les exigences fonctionnelles définies par voie réglementaire sont satisfaites.",
    "Un décret en Conseil d’État fixe les modalités d’application du présent article."
], "Réécriture à droit constant : la condition de recours à une solution d’effet équivalent est placée en tête, puis deux phrases distinguent le moyen de preuve et ce qu’il doit démontrer. Cette voie technique existante répond à l’orientation de solutions équivalentes avec sécurité démontrée ; elle n’est pas présentée comme une réforme nouvelle et aucune dispense n’est créée.",
    "Définition de L. 112-6 et proposition déjà rédigée vérifiées dans le corpus : la procédure de justification de la section 3 reste applicable par ce renvoi. Maintien cumulatif de l’objectif de L. 141-1, des études d’ingénierie et des exigences fonctionnelles réglementaires. L’accessibilité et la salubrité demandent leurs démonstrations propres ; cette preuve incendie ne s’y substitue pas." + historical)

add('L141-4', [
    "Lorsqu’ils affectent le niveau de sécurité contre les risques d’incendie, les mesures d’entretien des bâtiments, les aménagements qui y sont effectués et les modifications qui leur sont apportées doivent être consignés et rester disponibles pendant toute la vie de l’ouvrage. Sont notamment concernées les mesures d’entretien relatives à l’utilisation d’une solution d’effet équivalent."
], "Réécriture à droit constant : la condition relative au niveau de sécurité est placée en tête et s’applique aux trois catégories d’interventions. Une seconde phrase précise, dans le même alinéa, que l’entretien d’une solution d’effet équivalent est inclus. La traçabilité sur toute la vie de l’ouvrage est conservée ; aucune réforme de fond.",
    "L’article impose à la fois la consignation et la disponibilité, sans les réduire à la durée des travaux ou de l’exploitation par un titulaire donné. Aucun responsable de conservation ou support documentaire nouveau n’est désigné par la réécriture." + historical)

add('L142-1', [
    "Dès le début d’un incendie dans un logement ou une unité de vie, un dispositif de détection de fumée doit permettre d’alerter automatiquement les occupants. Cette exigence s’applique aussi lorsque le logement ou l’unité de vie se situe dans un immeuble de moyenne hauteur ou de grande hauteur."
], "Réécriture à droit constant : deux phrases distinguent l’alerte automatique dès le début de l’incendie et son application aux immeubles de moyenne ou de grande hauteur. L’ensemble reste dans l’unique alinéa source. Aucune réforme de fond.",
    "Maintien du logement et de l’unité de vie, de l’automaticité et du déclenchement dès le début de l’incendie. La répartition des obligations d’installation et d’entretien demeure renvoyée au décret prévu à L. 142-4." + historical)

add('L142-2', [
    "Les propriétaires doivent mettre en œuvre, dans les parties communes des bâtiments à usage d’habitation, des mesures de sécurité destinées à prévenir le risque d’incendie et à éviter que le feu se propage des locaux à risques vers les circulations et les dégagements."
], "Réécriture à droit constant : les propriétaires sont placés en tête comme débiteurs explicites de l’obligation. Les deux objectifs des mesures et le sens de la propagation à éviter sont conservés dans l’unique alinéa. Aucune réforme de fond.",
    "Le champ reste limité aux parties communes des bâtiments d’habitation ; l’obligation n’est pas transférée aux occupants. Les circulations et les dégagements restent tous deux visés." + historical)

add('L142-3', [
    "Lorsque des matières explosives ou inflammables sont entreposées dans un local attenant à un bâtiment d’habitation collectif ou compris dans celui-ci, le maire peut, par arrêté motivé, mettre en demeure la personne responsable de la gestion ou de la jouissance du local si cet entreposage méconnaît les règles de sécurité applicables au local ou s’il est réalisé dans des conditions de nature à créer des risques sérieux pour la sécurité des occupants. La mise en demeure lui impose de prendre, dans le délai fixé par le maire, toutes les mesures nécessaires pour se conformer aux règles de sécurité applicables ou mettre fin au danger. Si la personne tenue de ces mesures ne les exécute pas, le maire les fait exécuter d’office aux frais de cette personne. Si nécessaire, il peut interdire l’accès au local jusqu’à la réalisation des mesures.",
    "Le non-respect de l’arrêté pris en application du premier alinéa est puni d’une amende de 3 750 €."
], "Réécriture à droit constant : le premier alinéa est divisé en phrases successives pour distinguer les deux motifs alternatifs d’intervention, la mise en demeure motivée, le délai, l’exécution d’office aux frais du responsable et l’interdiction d’accès. Le second alinéa conserve l’incrimination et l’amende. Aucune réforme de fond.",
    "Maintien des matières explosives ou inflammables, des locaux attenants ou inclus, du bâtiment d’habitation collectif et de la personne responsable de la gestion ou de la jouissance. Le seuil des risques reste « sérieux ». Le renvoi au premier alinéa et le montant de 3 750 € sont conservés." + historical)

add('L142-4', [
    "Un décret en Conseil d’État fixe les modalités d’application du présent chapitre. Il précise notamment les personnes tenues d’installer le dispositif de détection de fumée et celles tenues de l’entretenir. Il détermine les caractéristiques techniques de ce dispositif et les conditions de son installation, de son entretien et de son fonctionnement."
], "Réécriture à droit constant : la formule sur les personnes auxquelles incombent les obligations est remplacée par l’indication directe de ce que le décret doit préciser. Son champ reste l’ensemble du chapitre et sa liste d’objets demeure non limitative. Aucune réforme de fond.",
    "Ne pas attribuer ici ces obligations au seul propriétaire ou au seul occupant : leur répartition relève du décret. Conservation distincte de l’installation, de l’entretien et du fonctionnement, ainsi que des caractéristiques techniques." + historical)

add('L143-1', [
    "L’article L. 122-3 s’applique aux travaux qui créent, aménagent ou modifient un établissement recevant du public."
], "Réécriture à droit constant : le renvoi devient le sujet de la phrase et les trois opérations sont exprimées par des verbes directs. Le texte ne crée ni autorisation supplémentaire ni exemption. Aucune réforme de fond.",
    "L. 122-3 et sa proposition déjà rédigée vérifiés dans le corpus : le renvoi conserve tout ce régime, notamment la déclaration dérogatoire pour certains établissements de moins de 300 mètres carrés, les dispenses de vérification sans incidence, le permis tenant lieu d’autorisation, l’autorisation intérieure complémentaire et l’exception concernant la perte totale de qualité d’ERP en quartier prioritaire. Ces éléments ne sont pas redéfinis ici." + historical)

add('L143-2', [
    "Un décret peut imposer aux propriétaires, aux constructeurs et aux exploitants de bâtiments et d’établissements ouverts au public des mesures complémentaires de sauvegarde et de sécurité ainsi que des moyens d’évacuation et de défense contre l’incendie. Ces mesures complémentaires doivent tenir compte de l’accessibilité."
], "Réécriture à droit constant : le décret et les personnes concernées sont placés avant les mesures qu’il peut imposer. La faculté réglementaire, les moyens d’évacuation et de défense et l’exigence d’accessibilité sont conservés dans le même alinéa. Aucune réforme de fond.",
    "Maintien des trois catégories de destinataires et des bâtiments comme des établissements ouverts au public. La source prévoit un décret, sans imposer ici un décret en Conseil d’État ; cette distinction est respectée. Coordination avec le renvoi de L. 122-3 conservée." + historical)

add('L143-3', [
    "I. - Dans le cadre de leurs compétences respectives et sans préjudice des pouvoirs généraux des autorités de police, le maire ou le représentant de l’État dans le département peuvent ordonner la fermeture d’un établissement recevant du public qui ne respecte pas les règles de sécurité propres à ce type d’établissement. La fermeture est ordonnée par arrêté, après avis de la commission de sécurité compétente, jusqu’à l’exécution des travaux de mise en conformité.",
    "Cet arrêté ne peut être pris qu’après une mise en demeure restée sans effet, adressée à l’exploitant ou au propriétaire, de réaliser les aménagements et travaux prescrits ou de fermer l’établissement dans le délai imparti.",
    "II. - L’arrêté de fermeture mentionné au I peut prévoir une astreinte journalière à la charge de l’exploitant ou du propriétaire si celui-ci n’exécute pas la décision de fermeture dans le délai fixé par cet arrêté.",
    "Si l’arrêté de fermeture concerne un immeuble en indivision, l’astreinte est appliquée dans les conditions fixées à l’article L. 541-2-1.",
    "III. - Un arrêté prononce l’astreinte mentionnée au II.",
    "Son montant ne peut dépasser 500 € par jour de retard. Il est modulé selon la nature de l’infraction aux règles de sécurité et les conséquences, pour la sécurité du public, de la non-exécution de l’arrêté de fermeture.",
    "L’astreinte court à partir du lendemain de la date de fermeture fixée par l’arrêté mentionné au I. Elle cesse à la fermeture effective de l’établissement ou à l’exécution complète des travaux de mise en conformité requis. Le recouvrement est engagé par trimestre échu.",
    "Lors de la liquidation trimestrielle de l’astreinte, l’autorité administrative peut accorder une exonération partielle ou totale de son produit si le redevable établit que l’inexécution de l’intégralité de ses obligations résulte de circonstances qui ne sont pas de son fait. Le total des sommes recouvrées ne peut dépasser le montant de l’amende prévue au V.",
    "Si le maire prononce l’astreinte, elle est recouvrée selon les règles applicables aux produits communaux, au bénéfice de la commune où se trouve l’établissement visé par l’arrêté. À défaut, elle est recouvrée par l’État.",
    "IV. - Le prononcé et la liquidation de l’astreinte n’empêchent pas l’autorité administrative de faire procéder d’office à la fermeture de l’établissement si l’arrêté de fermeture n’a pas été exécuté dans les conditions qu’il fixe. Cette fermeture d’office intervient à défaut d’exécution spontanée et après une mise en demeure du propriétaire ou de l’exploitant restée infructueuse. L’astreinte cesse alors à la date de fermeture effective.",
    "Le propriétaire ou l’exploitant doit payer les frais engagés par l’autorité administrative pour fermer l’établissement, auxquels s’ajoute, le cas échéant, le montant de l’astreinte.",
    "V. - Le propriétaire ou l’exploitant qui ne ferme pas l’établissement malgré une mise en demeure du maire ou du représentant de l’État dans le département de se conformer à l’arrêté pris en application du I est puni d’une amende de 10 000 €.",
    "VI. - À Paris, le préfet de police exerce les pouvoirs que le présent article attribue au maire ou au représentant de l’État dans le département."
], "Réécriture à droit constant des six subdivisions : les conditions de fermeture et de mise en demeure, le prononcé et le calcul de l’astreinte, sa liquidation, son recouvrement et la fermeture d’office sont répartis en phrases plus courtes au sein de leurs alinéas d’origine. Les garanties, plafonds, frais, sanctions et la compétence parisienne restent inchangés. Aucune réforme de fond.",
    "Renvoi à L. 541-2-1 vérifié : incohérence préexistante à examiner, car cet article vise expressément les arrêtés pris sur le fondement de L. 184-1 ou L. 511-11 et les astreintes de L. 184-3 ou L. 511-15, sans viser L. 143-3. Le renvoi est conservé, sans correction implicite ; son adaptation éventuelle exige une coordination expresse de L. 541-2-1 avec L. 143-3. Conserver 500 € par jour, le départ au lendemain, les deux causes alternatives de cessation, la liquidation et le recouvrement trimestriels, le plafond total renvoyant à l’amende de 10 000 € du V, ainsi que les deux mises en demeure procédurales. La formule « À défaut » au III, sur le recouvrement par l’État, est conservée ; sa portée n’est pas tranchée par la réécriture. Les 13 alinéas et les subdivisions I à VI sont conservés." + historical)

for number, height in [('L145-1', 'moyenne'), ('L146-1', 'grande')]:
    other = 'L. 146-1' if number == 'L145-1' else 'L. 145-1'
    add(number, [
        f"Les travaux créant, aménageant ou modifiant un immeuble de {height} hauteur, ou changeant sa destination, nécessitent une autorisation préalable de l’autorité chargée de la police de la sécurité. Cette autorité vérifie la conformité des travaux aux règles prévues à l’article L. 141-2.",
        "Si ces travaux sont soumis à permis de construire, le permis tient lieu de cette autorisation à condition que l’autorité chargée de la police de la sécurité ait donné son accord à sa délivrance.",
        "L’autorisation n’est pas exigée si les travaux n’ont pas d’incidence sur le niveau de sécurité de l’immeuble contre l’incendie."
    ], f"Réécriture à droit constant : le premier alinéa distingue l’autorisation préalable et son contrôle ; les deux suivants énoncent directement la substitution du permis sous condition d’accord et la dispense sans incidence sur la sécurité incendie. Le régime des immeubles de {height} hauteur est conservé, sans réforme de fond.",
        f"Coordination maintenue avec L. 141-2 et avec le régime parallèle de {other}. La réécriture déjà présente de L. 423-1 du code de l’urbanisme prévoit un dossier coordonné et une transition de six mois ; elle conserve les compétences et délais propres. Aucun second délai ni nouvelle transition n’est ajouté ici : le permis ne vaut autorisation de sécurité qu’avec l’accord requis. Conserver les trois alinéas, le changement de destination et la dispense strictement liée à l’absence d’incidence sur le niveau de sécurité contre l’incendie." + historical)

add('L151-1', [
    "Les bâtiments doivent être conçus, construits, équipés et aménagés ou rénovés de manière à ne pas porter atteinte à la santé des personnes qui s’y trouvent dans des conditions normales d’occupation et d’usage. Leur environnement doit, le cas échéant, être pris en compte pour satisfaire à cette exigence."
], "Réécriture à droit constant : l’obligation de concevoir, construire, équiper et aménager ou rénover sans porter atteinte à la santé est formulée directement ; la prise en compte éventuelle de l’environnement fait l’objet d’une seconde phrase dans le même alinéa. La protection reste celle de toutes les personnes présentes dans les conditions normales d’occupation et d’usage. Aucune réforme de fond.",
    "La voie de rénovation locative limitée à vingt-quatre mois annoncée par policy.json ne peut résulter d’une dérogation générale à cet objectif sanitaire. Sa création requiert des dispositions expresses hors du lot, notamment dans la loi n° 89-462 du 6 juillet 1989 (articles 6 et 20-1 sur la décence et ses recours), et la coordination du décret n° 2002-120 du 30 janvier 2002 relatif au logement décent. Ces textes doivent définir le champ des logements éligibles, le point de départ et la durée maximale de vingt-quatre mois, les travaux et leur contrôle, la compensation des surcoûts énergétiques et les garanties des locataires, sans extension automatique aux baux antérieurs ni aux logements indignes. Aucun renvoi à un dispositif inexistant n’est introduit dans le texte proposé." + historical)

assert len(source) == len(drafts) == 24
answer = []
for a in source:
    d = drafts[a['number']]
    answer.append({
        'code_id': a['code_id'],
        'source_id': a['source_id'],
        'source_sha256': a['source_sha256'],
        'number': a['number'],
        **d,
        'status': 'rewrite_draft'
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles,', sum(len(a['proposed_xml']) for a in answer), 'caractères de texte proposé')
