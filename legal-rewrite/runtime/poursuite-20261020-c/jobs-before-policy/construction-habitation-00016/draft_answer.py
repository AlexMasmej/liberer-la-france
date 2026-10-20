import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


add('L261-11-1', '''
<p>Lorsque le contrat défini à l'article L. 261-11 prévoit une révision du prix, celle-ci ne peut être calculée qu'en fonction de la variation d'un indice national du bâtiment tous corps d'état. Cet indice mesure l'évolution du coût des facteurs de production dans le bâtiment et est publié par l'autorité administrative.</p>
<p>Pour chaque paiement ou dépôt, la révision est limitée à un pourcentage de la variation de cet indice.</p>
<p>Un décret en Conseil d'État définit l'indice et cette limite. Afin de tenir compte des frais fixes, de la valeur du terrain et des améliorations de productivité, cette limite doit être comprise entre 60 % et 80 % de la variation de l'indice.</p>
<p>L'indice de base utilisé pour calculer la révision est le dernier indice publié au jour de la signature du contrat. La variation retenue est obtenue en comparant cet indice au dernier indice publié avant la date de chaque paiement ou dépôt.</p>
''',
    "Réécriture à droit constant : les caractéristiques de l'indice sont réparties en deux phrases et le plafond applicable à chaque paiement ou dépôt est exprimé directement. Aucune réforme de fond.",
    "Quatre alinéas conservés. Renvoi à L. 261-11, fourchette de 60 % à 80 %, facteurs pris en compte et dates de publication des deux indices préservés. Ne pas transposer cette fourchette à L. 262-5, qui ne la prévoit pas.")

add('L261-12', '''
<p>Dans une vente en l'état futur d'achèvement, le vendeur ne peut exiger ni accepter de versement, de dépôt, de souscription ou d'acceptation d'effets de commerce avant la signature du contrat ni avant la date d'exigibilité de la créance.</p>
<p>Le contrat de vente à terme peut uniquement prévoir des dépôts de garantie effectués au fur et à mesure de l'avancement des travaux, sur un compte spécial ouvert au nom de l'acquéreur par un organisme habilité à cet effet. Dans la limite des sommes dues par l'acheteur, les fonds déposés sur ce compte sont incessibles, insaisissables et indisponibles, sauf pour le paiement du prix.</p>
''',
    "Réécriture à droit constant : les interdictions imposées au vendeur et les conditions des dépôts de garantie sont formulées plus directement, dans deux alinéas. Aucune réforme de fond.",
    "Distinction entre vente en l'état futur d'achèvement et vente à terme maintenue. Les deux bornes de l'interdiction, le titulaire du compte, l'habilitation de l'organisme et l'exception de paiement du prix sont conservés. Coordination répressive avec L. 263-1 inchangée.")

add('L261-13', '''
<p>Même en présence d'une stipulation contraire, les clauses de résolution de plein droit relatives aux obligations de versement ou de dépôt prévues aux articles L. 261-10 à L. 261-12 ne prennent effet qu'un mois après la date d'une sommation ou d'un commandement de payer resté infructueux.</p>
<p>Pendant ce délai d'un mois, le débiteur peut demander un délai de paiement conformément à l'article 1343-5 du code civil.</p>
<p>Les effets de ces clauses sont suspendus pendant les délais accordés dans les conditions prévues à l'article 1343-5 du code civil. Si le débiteur se libère dans les conditions fixées par le juge, les clauses sont réputées n'avoir jamais produit effet.</p>
''',
    "Réécriture à droit constant : le débiteur est désigné comme auteur de la demande de délai et les effets successifs de la clause sont formulés dans l'ordre de leur application. Aucune réforme de fond.",
    "Trois alinéas maintenus ; délai d'un mois courant depuis la date de la sommation ou du commandement, période de demande et renvois à l'article 1343-5 conservés. La réforme du traitement des impayés locatifs ne concerne pas cette résolution d'une vente.")

add('L261-14', '''
<p>En cas de résolution, l'indemnité forfaitaire que le contrat met à la charge de la partie à laquelle la résolution est imputable ne peut dépasser 10 % du prix.</p>
<p>Les parties peuvent toutefois demander réparation du préjudice qu'elles ont effectivement subi.</p>
''',
    "Réécriture à droit constant : le plafond de l'indemnité est rattaché directement à la partie responsable de la résolution et la faculté de réparation est formulée à la voix active. Aucune réforme de fond.",
    "Deux alinéas maintenus. Le plafond de 10 % concerne l'indemnité contractuelle forfaitaire ; la faculté distincte de demander réparation du préjudice effectivement subi est conservée.")

add('L261-15', '''
<p>I.- La vente prévue à l'article L. 261-10 peut être précédée d'un contrat préliminaire. Par ce contrat, le vendeur s'engage à réserver à un acheteur un immeuble ou une partie d'immeuble en contrepartie d'un dépôt de garantie sur un compte spécial.</p>
<p>Le contrat préliminaire doit indiquer les éléments essentiels concernant la consistance de l'immeuble, la qualité de la construction et les délais d'exécution des travaux, ainsi que la consistance, la situation et le prix du local réservé.</p>
<p>Jusqu'à la conclusion du contrat de vente, les fonds déposés en garantie sont indisponibles, incessibles et insaisissables.</p>
<p>Les fonds sont restitués au déposant dans le délai de trois mois lorsque le contrat n'est pas conclu du fait du vendeur, lorsque la condition suspensive prévue à l'article L. 313-41 du code de la consommation n'est pas réalisée ou lorsque le contrat proposé présente une différence anormale par rapport aux prévisions du contrat préliminaire.</p>
<p>II.- Le contrat préliminaire peut prévoir que, si la vente est conclue, l'acquéreur se réserve l'exécution de travaux de finition ou d'installation d'équipements qu'il se procure lui-même. Le contrat doit alors comporter une clause en caractères très apparents par laquelle l'acquéreur accepte la charge, le coût et les responsabilités résultant de ces travaux. L'acquéreur réalise ces travaux après la livraison de l'immeuble.<br /><br />Dans ce cas, le contrat préliminaire précise :</p>
<p>1° Le prix du local réservé mentionné au deuxième alinéa du I, décomposé comme suit :</p>
<p>a) Le prix de vente convenu ;</p>
<p>b) Le coût des travaux dont l'acquéreur se réserve l'exécution, avec leur description et leur chiffrage par le vendeur ;</p>
<p>c) Le coût total de l'immeuble, égal à la somme du prix convenu et du coût des travaux mentionnés aux a et b du présent 1° ;</p>
<p>2° Le délai dans lequel l'acquéreur peut revenir sur sa décision de se réserver l'exécution des travaux mentionnés au premier alinéa du présent II.<br /><br />Lorsque l'acquéreur exerce la faculté prévue au 2°, le vendeur doit exécuter ou faire exécuter les travaux dont l'acquéreur s'était réservé l'exécution, aux prix et conditions indiqués dans le contrat préliminaire.<br /><br />Un décret en Conseil d'État précise les conditions d'application du présent II, notamment la nature des travaux dont l'acquéreur peut se réserver l'exécution.</p>
<p>III.- Toute autre promesse d'achat ou de vente est nulle.</p>
''',
    "Réécriture à droit constant : les engagements du vendeur et de l'acquéreur sont explicités et les phrases longues sur la réservation et les travaux sont scindées. Les subdivisions I à III et la décomposition du prix sont conservées. Aucune réforme de fond.",
    "Délai de restitution de trois mois, trois motifs de restitution, renvoi à L. 313-41 du code de la consommation, 1°, 2° et a à c préservés. Le point de départ du délai de restitution n'est pas précisé par la source : aucun n'est ajouté. Renvois au deuxième alinéa du I et au premier alinéa du II maintenus à leur emplacement, ainsi que les séparations internes par doubles sauts de ligne. Le contenu de la clause doit rester en caractères très apparents lors de la mise en forme des contrats. Coordination avec le e de L. 261-11 vérifiée dans le corpus.")

add('L261-16', '''
<p>Est réputée non écrite toute clause qui contrevient aux articles L. 261-11 à L. 261-15 du présent code ou aux articles 1642-1 et 1646-1 du code civil, reproduits aux articles L. 261-5 et L. 261-6 du présent code.</p>
''',
    "Réécriture à droit constant : la sanction de la clause contraire est placée en tête de phrase et les deux ensembles de dispositions protégées sont distingués. Aucune réforme de fond.",
    "Un alinéa conservé. Tous les renvois et la sanction de clause réputée non écrite sont maintenus ; cette sanction n'est pas transformée en nullité du contrat. Correspondance des articles 1642-1 et 1646-1 avec L. 261-5 et L. 261-6 vérifiée dans le corpus.")

add('L261-22', '''
<p>Un décret en Conseil d'État fixe, en tant que de besoin, les modalités d'application du présent chapitre. Il détermine notamment les conditions dans lesquelles les personnes tenues à garantie en application des articles 1792 et 1792-4-1 du code civil et des articles L. 261-5 et L. 261-6 du présent code peuvent être obligées de se prémunir contre les conséquences pécuniaires de cette garantie.</p>
''',
    "Réécriture à droit constant : la règle générale d'application et l'objet particulier du décret sont exposés en deux phrases dans le même alinéa. Aucune réforme de fond.",
    "Les quatre renvois et le caractère éventuel de l'obligation de couverture sont conservés. La note de l'article 8 de l'ordonnance n° 2020-71 du 29 janvier 2020 a été lue : entrée en vigueur par décret et au plus tard le 1er juillet 2021. Il s'agit d'une donnée historique, non d'une date d'entrée en vigueur du projet.")

add('L262-1', '''
<p>Toute personne qui vend un immeuble bâti ou une partie d'immeuble bâti doit conclure avec l'acquéreur un contrat soumis au présent chapitre lorsque les conditions suivantes sont réunies : le bien est à usage d'habitation ou à usage professionnel et d'habitation, ou est destiné, après travaux, à l'un de ces usages ; le vendeur s'engage à réaliser, directement ou indirectement, des travaux sur ce bien dans un délai fixé par le contrat ; il perçoit des sommes d'argent de l'acquéreur avant la livraison des travaux.</p>
<p>Le vendeur transfère immédiatement à l'acquéreur ses droits sur le sol et la propriété des constructions existantes. L'acquéreur devient propriétaire des ouvrages à venir au fur et à mesure de leur exécution. Il doit en payer le prix à mesure de l'avancement des travaux.</p>
<p>Le présent chapitre ne s'applique pas aux travaux d'agrandissement ou de restructuration complète de l'immeuble qui sont assimilables à une reconstruction.</p>
<p>Le contrat mentionné au premier alinéa est soumis aux dispositions relatives à la vente d'immeubles existants, notamment à celles du titre VI du livre III du code civil, sous réserve des articles L. 262-2 à L. 262-11 du présent code.</p>
''',
    "Réécriture à droit constant : les conditions cumulatives du régime de vente à rénover sont séparées par des points-virgules dans le premier alinéa ; les transferts de propriété et l'obligation de paiement ont des sujets explicites. Aucune réforme de fond.",
    "Quatre alinéas maintenus, notamment le premier auquel renvoient L. 262-2, L. 262-3, L. 262-4 et L. 262-9. Usages mixtes et futurs, intervention indirecte, exclusion des agrandissements ou restructurations complètes assimilables à une reconstruction et renvois conservés. La voie de rénovation locative de vingt-quatre mois de policy.json ne relève pas de cette vente : elle nécessite notamment des dispositions dans la loi n° 89-462 du 6 juillet 1989, articles 6 et 20-1 sur la décence et les travaux, et leur articulation avec L. 173-1-1 du CCH et le décret n° 2002-120 du 30 janvier 2002. Ses conditions de contrôle et de compensation énergétique doivent y être définies, sans étendre ici ce dispositif aux ventes ni aux contrats anciens.")


add('L262-2', '''
<p>Jusqu'à la réception des travaux, le vendeur d'un immeuble à rénover conserve la qualité de maître d'ouvrage.</p>
<p>La réception de l'ensemble des travaux intervient à une date unique. Cette date marque le point de départ des garanties mentionnées au dernier alinéa.</p>
<p>Pour les travaux mentionnés au premier alinéa de l'article L. 262-1, le vendeur est tenu par les garanties prévues aux articles 1792, 1792-2 et 1792-3 du code civil, dès lors que ces travaux entrent dans le champ d'application de ces articles.</p>
''',
    "Réécriture à droit constant : la qualité du vendeur, l'unicité de la réception et le point de départ des garanties sont exposés en phrases courtes. Aucune réforme de fond.",
    "Trois alinéas conservés ; renvois au premier alinéa de L. 262-1 et au dernier alinéa du présent article maintenus. Les garanties demeurent conditionnées au champ des articles 1792, 1792-2 et 1792-3 du code civil. La note de l'article 8 de l'ordonnance n° 2020-71 du 29 janvier 2020 prévoit une entrée en vigueur par décret au plus tard le 1er juillet 2021 ; cette date historique n'est pas utilisée pour le projet.")

add('L262-3', '''
<p>La livraison résulte d'un procès-verbal établi entre le vendeur et l'acquéreur.</p>
<p>Les vices de construction ou défauts de conformité apparents qui affectent les travaux mentionnés au premier alinéa de l'article L. 262-1 doivent être dénoncés dans l'acte de livraison des travaux ou dans le délai d'un mois suivant cette livraison. L'action en réparation des vices ou défauts ainsi dénoncés peut être engagée dans le délai d'un an suivant la livraison.</p>
''',
    "Réécriture à droit constant : la répétition sur l'établissement du procès-verbal est supprimée et les deux délais sont rattachés explicitement à la livraison. Aucune réforme de fond.",
    "Deux alinéas maintenus. Le délai de dénonciation d'un mois et le délai d'action d'un an courent tous deux à partir de la livraison, non de la réception visée à L. 262-2. Renvoi au premier alinéa de L. 262-1 et caractère apparent des vices ou défauts conservés.")

add('L262-4', '''
<p>Le contrat mentionné au premier alinéa de l'article L. 262-1 doit être conclu par acte authentique, à peine de nullité.</p>
<p>Le contrat précise :</p>
<p>a) La description et les caractéristiques de l'immeuble ou de la partie d'immeuble vendu ainsi que, le cas échéant, la superficie de la partie privative du lot ou de la fraction du lot, en application de l'article 46 de la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis ;</p>
<p>b) La description des travaux à réaliser, en distinguant, le cas échéant, ceux qui concernent les parties communes et ceux qui concernent les parties privatives ;</p>
<p>c) Le prix de l'immeuble ;</p>
<p>d) Le délai de réalisation des travaux ;</p>
<p>e) La justification de la garantie financière d'achèvement des travaux fournie par le vendeur ;</p>
<p>f) Les justifications des assurances de responsabilité et de dommages souscrites par le vendeur pour les travaux, lorsque ceux-ci relèvent des articles 1792-2 et 1792-3 du code civil, en application des articles L. 241-2 et L. 242-1 du code des assurances.</p>
<p>Le contrat doit aussi comporter les indications utiles sur la consistance et les caractéristiques techniques des travaux. Ces indications figurent en annexe ou par référence à des documents déposés chez un notaire.</p>
<p>Le contrat doit également préciser si le prix est révisable et, s'il l'est, les modalités de sa révision.</p>
<p>Le règlement de copropriété est communiqué à chaque acquéreur avant la signature du contrat. Il lui est, en tout état de cause, remis lors de cette signature.</p>
<p>Si les dispositions du présent article ne sont pas respectées, seul l'acquéreur peut invoquer la nullité du contrat, avant la livraison.</p>
''',
    "Réécriture à droit constant : les mentions obligatoires restent ordonnées de a à f ; les modalités de documentation et de communication sont exprimées plus directement et la nullité est rattachée à son seul bénéficiaire. Aucune réforme de fond.",
    "Douze alinéas maintenus, avec les lettres e et f visées par L. 262-9 à leur place. Date et numéro de la loi sur la copropriété, article 46, renvois assurantiels et borne de la livraison conservés. Point de contrôle préexistant : le f vise 1792-2 et 1792-3, alors que L. 262-2 vise aussi 1792 ; la correspondance de ce champ avec les assurances obligatoires demande vérification, sans ajout ni suppression silencieux d'un renvoi. Note historique lue : article 8 de l'ordonnance n° 2020-71 du 29 janvier 2020, entrée en vigueur par décret au plus tard le 1er juillet 2021 ; aucune date nouvelle n'en est déduite.")

add('L262-5', '''
<p>Lorsque le contrat défini à l'article L. 262-1 prévoit une révision du prix, celle-ci ne peut être calculée qu'en fonction de la variation d'un indice national du bâtiment tous corps d'état. Cet indice mesure l'évolution du coût des facteurs de production dans le bâtiment et est publié par l'autorité administrative.</p>
<p>Pour chaque paiement ou dépôt, la révision est limitée à un pourcentage de la variation de cet indice.</p>
<p>Un décret en Conseil d'État définit l'indice et cette limite.</p>
<p>L'indice de base utilisé pour calculer la révision est le dernier indice publié au jour de la signature du contrat. La variation retenue est obtenue en comparant cet indice au dernier indice publié avant la date de chaque paiement ou dépôt.</p>
''',
    "Réécriture à droit constant : les caractéristiques de l'indice sont détachées de la condition de révision et la limite applicable à chaque échéance est exprimée directement. Aucune réforme de fond.",
    "Quatre alinéas et renvoi à L. 262-1 conservés. Les deux dates de publication des indices restent distinctes. La source ne fixe pas la fourchette de 60 % à 80 % figurant à L. 261-11-1 : aucune fourchette n'est ajoutée au régime de vente à rénover.")

add('L262-6', '''
<p>Lorsque l'acquéreur cède les droits qu'il tient d'une vente d'immeuble à rénover, le cessionnaire lui est substitué de plein droit dans les obligations de l'acquéreur envers le vendeur.</p>
<p>Si la vente était assortie d'un mandat, ce mandat se poursuit entre le vendeur et le cessionnaire.</p>
<p>Le présent article s'applique à toute mutation entre vifs, qu'elle soit volontaire ou forcée, ainsi qu'à toute mutation à cause de mort.</p>
''',
    "Réécriture à droit constant : la cession est exposée comme une situation concrète et le champ des mutations est présenté sans ellipse. Aucune réforme de fond.",
    "Trois alinéas maintenus. Substitution de plein droit dans les obligations, poursuite du mandat et mutations volontaires, forcées ou à cause de mort conservées ; aucune condition de consentement supplémentaire n'est ajoutée.")

add('L262-7', '''
<p>La garantie d'achèvement des travaux prend la forme d'une caution solidaire donnée par un établissement de crédit, une société de financement ou une entreprise d'assurance agréée à cet effet.</p>
<p>Les conditions de mise en œuvre de cette garantie sont celles prévues aux deuxième à avant-dernier alinéas de l'article L. 261-10-1.</p>
''',
    "Réécriture à droit constant : la forme de la garantie et les conditions de sa mise en œuvre sont formulées dans deux phrases directes, sans modifier les catégories de garants. Aucune réforme de fond.",
    "Deux alinéas conservés. Le renvoi aux deuxième à avant-dernier alinéas de L. 261-10-1 a été vérifié dans le corpus : il comprend la défaillance financière, l'administrateur ad hoc et l'exigibilité du solde au profit du garant. Le premier alinéa et le dernier alinéa de cet article ne sont pas inclus dans ce renvoi. L'agrément reste attaché à l'entreprise d'assurance.")

add('L262-8', '''
<p>L'acquéreur paie le prix en fonction de l'état d'avancement des travaux.</p>
<p>Avant la date d'exigibilité de la créance, le vendeur ne peut exiger ni accepter de versement, de dépôt, de souscription ou d'acceptation d'effets de commerce.</p>
''',
    "Réécriture à droit constant : le paiement est exprimé par un verbe direct et la borne temporelle de l'interdiction est placée au début du second alinéa. Aucune réforme de fond.",
    "Deux alinéas maintenus. Toutes les formes de remise visées par la source sont conservées ; aucune dérogation aux paiements exigibles n'est créée. Coordination avec l'incrimination de L. 263-1 préservée.")


add('L262-9', '''
<p>Toute promesse de vente d'un bien immobilier soumis au premier alinéa de l'article L. 262-1 doit indiquer les éléments essentiels concernant les caractéristiques du bien, la description et le délai de réalisation des travaux, ainsi que le prix du bien. Elle doit aussi comporter l'engagement du vendeur de produire, lors de la signature de l'acte authentique de vente, les justifications de la garantie d'achèvement des travaux et des assurances prévues respectivement aux e et f de l'article L. 262-4. Ces indications et cet engagement sont exigés à peine de nullité.</p>
''',
    "Réécriture à droit constant : les mentions descriptives, l'engagement documentaire du vendeur et la sanction commune sont exposés dans des phrases distinctes du même alinéa. Aucune réforme de fond.",
    "Un alinéa conservé. La nullité demeure attachée à l'ensemble des mentions et de l'engagement exigés. Renvois au premier alinéa de L. 262-1 et aux e et f de L. 262-4 préservés ; les justificatifs doivent être produits à la signature de l'acte authentique, sans anticipation imposée par la réécriture.")

add('L262-10', '''
<p>Les règles fixées par le présent chapitre sont d'ordre public.</p>
''',
    "Réécriture à droit constant de cette disposition brève : la formule désigne directement les règles du chapitre comme étant d'ordre public. Aucune réforme de fond.",
    "L'unique alinéa conserve le caractère d'ordre public de l'ensemble du chapitre, sans exception nouvelle.")

add('L262-11', '''
<p>Les modalités d'application du présent chapitre sont fixées par décret en Conseil d'État.</p>
''',
    "Réécriture à droit constant : les modalités d'application sont placées en sujet de la phrase, en conservant la compétence du décret en Conseil d'État. Aucune réforme de fond.",
    "Un alinéa conservé. Le niveau du texte d'application reste un décret en Conseil d'État ; aucune habilitation nouvelle ni date d'entrée en vigueur n'est ajoutée.")

add('L263-1', '''
<p>Le fait d'exiger ou d'accepter un versement en violation des articles L. 261-12, L. 261-15 et L. 262-8 est puni de deux ans d'emprisonnement et de 9 000 euros d'amende, ou de l'une de ces deux peines seulement.</p>
<p>Pour l'application du présent article, les dépôts de fonds sur un compte bancaire ouvert au nom du déposant ne constituent pas des versements si le déposant peut en disposer à tout moment, sans aucune restriction.</p>
''',
    "Réécriture à droit constant : l'infraction est formulée à partir du comportement sanctionné et l'exclusion des dépôts librement disponibles devient une condition explicite. Aucune réforme de fond.",
    "Deux alinéas conservés. Peines de deux ans et 9 000 euros, possibilité d'une seule peine, trois renvois et double condition d'un compte au nom du déposant et d'une disponibilité sans restriction maintenus. Aucun durcissement pénal n'est introduit.")

add('L263-2', '''
<p>Est punie des peines prévues aux articles 314-1 et 314-10 du code pénal toute personne qui détourne tout ou partie des sommes qu'elle a reçues ou acceptées, à l'occasion d'une vente soumise au présent titre, sous la forme d'un ou de plusieurs versements, dépôts ou souscriptions d'effets de commerce.</p>
''',
    "Réécriture à droit constant : le comportement de détournement est rapproché des sommes reçues ou acceptées, sans interrompre la phrase par une longue incise. Aucune réforme de fond.",
    "Un alinéa conservé. Renvois à 314-1 et 314-10 du code pénal, champ du présent titre, détournement total ou partiel et trois formes de remise maintenus. Le montant des peines n'est pas reconstitué dans cet article.")

add('L263-3', '''
<p>Les personnes condamnées en application des articles L. 263-1 et L. 263-2, ainsi que celles auxquelles il est interdit, en application de l'article L. 241-7, de procéder aux opérations mentionnées aux articles L. 214-6 à L. 214-9, ne peuvent procéder habituellement aux opérations soumises au présent chapitre. Cette interdiction s'applique à titre quelconque, directement ou par personne interposée, pour leur compte ou pour celui d'autrui.</p>
''',
    "Réécriture à droit constant : les catégories de personnes visées deviennent le sujet de la phrase et les modalités d'intervention interdites sont énoncées dans une seconde phrase du même alinéa. Aucune réforme de fond.",
    "Un alinéa et tous les renvois conservés. Deux difficultés préexistantes sont signalées sans correction : le texte vise les opérations du « présent chapitre », alors que ce chapitre porte sur les dispositions communes ; L. 214-6 à L. 214-9 concernent le conseil de surveillance, tandis que L. 241-7 rattache l'interdiction aux opérations de l'ancien décret n° 54-1123 du 10 novembre 1954. Ces contenus ont été vérifiés dans le corpus. Le remplacement éventuel de ces renvois exige une coordination expresse, non réalisée ici.")

add('L271-1', '''
<p>Pour tout acte ayant pour objet la construction ou l'acquisition d'un immeuble à usage d'habitation, la souscription de parts donnant vocation à l'attribution en jouissance ou en propriété d'immeubles d'habitation, la vente d'immeubles à construire ou la location-accession à la propriété immobilière, l'acquéreur non professionnel peut se rétracter dans un délai de dix jours. Ce délai court à compter du lendemain de la première présentation de la lettre lui notifiant l'acte.</p>
<p>L'acte est notifié à l'acquéreur par lettre recommandée avec demande d'avis de réception ou par un autre moyen offrant des garanties équivalentes pour déterminer la date de réception ou de remise. L'acquéreur exerce son droit de rétractation dans les mêmes formes.</p>
<p>Si l'acte est conclu par l'intermédiaire d'un professionnel mandaté pour prêter son concours à la vente, il peut être remis directement au bénéficiaire du droit de rétractation. Le délai de rétractation court alors à compter du lendemain de cette remise. La remise doit être attestée selon les modalités fixées par décret.</p>
<p>Si le contrat constatant ou réalisant la convention est précédé d'un contrat préliminaire ou d'une promesse synallagmatique ou unilatérale, les trois alinéas précédents s'appliquent uniquement à ce contrat préliminaire ou à cette promesse.</p>
<p>Si le contrat constatant ou réalisant la convention est dressé en la forme authentique sans être précédé d'un contrat préliminaire ou d'une promesse synallagmatique ou unilatérale, l'acquéreur non professionnel dispose d'un délai de réflexion de dix jours à compter de la notification ou de la remise du projet d'acte. Cette notification ou cette remise obéit aux mêmes modalités que celles prévues aux premier et troisième alinéas pour le délai de rétractation. L'acte authentique ne peut en aucun cas être signé pendant ce délai de dix jours.</p>
<p>Les actes mentionnés au présent article doivent présenter, de manière lisible et compréhensible, les informations sur les conditions et les modalités d'exercice du droit de rétractation ou de réflexion.<br /><br />Tout manquement à l'obligation d'information prévue à l'avant-dernier alinéa est passible d'une amende administrative d'un montant maximal de 3 000 euros pour une personne physique et de 15 000 euros pour une personne morale. Cette amende est prononcée dans les conditions prévues au chapitre II du titre II du livre V du code de la consommation.</p>
''',
    "Réécriture à droit constant : les points de départ des délais sont isolés dans des phrases courtes, le titulaire du droit est explicite et les cas de contrat préalable ou d'acte authentique sont exposés directement. Aucune réforme de fond.",
    "Tous les actes visés, les deux délais de dix jours, les formes de notification et de rétractation, le mandat professionnel et l'interdiction de signer pendant la réflexion sont conservés. Maintien de l'ordre des alinéas, des renvois aux trois précédents, aux premier et troisième et à l'avant-dernier ; le double saut de ligne séparant information et sanction est conservé comme dans la source. Plafonds de 3 000 et 15 000 euros et procédure du code de la consommation maintenus. La rédaction source du délai de réflexion combine « à compter de la notification ou de la remise » et les modalités des premier et troisième alinéas : cette articulation est conservée sans déplacer silencieusement le point de départ.")

add('L271-2', '''
<p>Lors de la conclusion d'un acte mentionné à l'article L. 271-1, nul ne peut recevoir de l'acquéreur non professionnel un versement avant l'expiration du délai de rétractation, directement ou indirectement, à quelque titre ou sous quelque forme que ce soit. Cette interdiction s'applique sous réserve des dispositions législatives expresses contraires prévues notamment pour les contrats d'acquisition ou de construction d'un immeuble neuf d'habitation, la souscription de parts donnant vocation à l'attribution en jouissance ou en propriété d'immeubles d'habitation et les contrats préliminaires de vente d'immeubles à construire ou de location-accession à la propriété immobilière. Si les parties fixent le montant d'un versement et conviennent de l'effectuer après l'expiration de ce délai, l'acte est conclu sous la condition suspensive de la remise de cette somme à la date convenue.</p>
<p>Toutefois, si l'un des actes mentionnés à l'alinéa précédent est conclu par l'intermédiaire d'un professionnel mandaté pour prêter son concours à la vente, un versement de l'acquéreur peut être reçu par un professionnel disposant d'une garantie financière affectée au remboursement des fonds déposés. Si l'acquéreur se rétracte, le professionnel dépositaire doit lui restituer les fonds dans un délai de vingt et un jours à compter du lendemain de la date de cette rétractation.</p>
<p>Lorsque l'acte est dressé en la forme authentique, aucune somme ne peut être versée pendant le délai de réflexion de dix jours.</p>
<p>Le fait d'exiger ou de recevoir un versement ou un engagement de versement en violation des alinéas précédents est puni de 30 000 euros d'amende.</p>
''',
    "Réécriture à droit constant : l'interdiction de versement, les exceptions législatives et la condition suspensive sont séparées en phrases distinctes dans le premier alinéa ; l'obligation de restitution désigne son débiteur. Aucune réforme de fond.",
    "Quatre alinéas conservés. Liste non exhaustive des dérogations législatives, garantie financière du professionnel, restitution dans les vingt et un jours à compter du lendemain de la rétractation, réflexion de dix jours et amende de 30 000 euros maintenues. La sanction vise aussi l'engagement de versement. Coordination avec les actes et délais de L. 271-1 et avec l'exception de L. 271-3 conservée.")

add('L271-3', '''
<p>Les ventes par adjudication réalisées en la forme authentique sont exclues du champ d'application de la présente section.</p>
''',
    "Réécriture à droit constant : les ventes exclues sont placées en sujet de la phrase et le champ de l'exception est formulé directement. Aucune réforme de fond.",
    "Un alinéa conservé. L'exclusion vise uniquement les ventes réunissant les deux conditions d'adjudication et de forme authentique ; elle porte sur toute la section, sans extension à d'autres ventes.")


def write_answer():
    assert len(drafts) == len(sources) == 24
    answer = []
    for source in sources:
        xml, reason, notes = drafts[source['number']]
        item = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
        item.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
        answer.append(item)
    Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    write_answer()
