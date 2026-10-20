import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = dict(
        proposed_xml=proposed_xml.strip(),
        reason=reason,
        review_notes=review_notes,
        status='rewrite_draft',
    )


add('L162-5-3', '''
<p>Pour favoriser la coordination des soins, tout assuré ou ayant droit âgé de seize ans ou plus déclare à l'organisme gestionnaire de son régime de base d'assurance maladie le nom du médecin traitant qu'il a choisi, avec l'accord de ce médecin. Pour un ayant droit mineur, ce choix nécessite l'accord d'au moins l'un des deux parents ou du titulaire de l'autorité parentale. Le médecin traitant peut être généraliste ou spécialiste. Ce choix peut porter sur un médecin hospitalier.</p>
<p>Pour les ayants droit âgés de moins de seize ans, au moins l'un des deux parents ou le titulaire de l'autorité parentale choisit le médecin traitant et déclare son nom à l'organisme gestionnaire.</p>
<p>Le médecin traitant peut exercer comme salarié dans les conditions prévues au a du 3° de l'article L. 4041-2 du code de la santé publique. Il peut également être salarié d'un centre de santé mentionné à l'article L. 6323-1 du même code ou d'un établissement ou service mentionné à l'article L. 312-1 du code de l'action sociale et des familles. Les médecins qui exercent la même spécialité au sein d'un cabinet médical situé dans les mêmes locaux ou dans un centre de santé mentionné à l'article L. 6323-1 du code de la santé publique peuvent être désignés conjointement médecins traitants. Un arrêté fixe les missions du médecin traitant salarié.</p>
<p>Le médecin traitant participe à la mise en place et à la gestion du dossier médical partagé prévu à l'article L. 161-36-1 du présent code.</p>
<p>Lorsqu'un assuré choisit un médecin traitant autre que son médecin référent, ce dernier perd, pour cet assuré, les avantages liés à l'adhésion à cette option conventionnelle. L'assuré perd également ces avantages.</p>
<p>La participation prévue au I de l'article L. 160-13 peut être majorée pour les assurés et les ayants droit qui n'ont pas choisi de médecin traitant ou qui consultent un autre médecin sans prescription de leur médecin traitant. Cette majoration ne s'applique pas aux patients âgés de moins de seize ans. Un décret fixe les autres cas dans lesquels elle ne s'applique pas, notamment lorsqu'un protocole de soins est mis en œuvre ou lorsque la consultation a lieu dans une structure de médecine humanitaire ou dans un centre de planification ou d'éducation familiale.</p>
<p>Les dispositions de l'alinéa précédent ne s'appliquent pas :</p>
<p>1° Lorsque, en cas d'urgence, la consultation a lieu auprès d'un médecin autre que celui déclaré à l'organisme gestionnaire du régime de base d'assurance maladie ;</p>
<p>2° Lorsque la consultation a lieu en dehors du lieu de résidence stable et durable de l'assuré social ou de l'ayant droit âgé de seize ans ou plus ;</p>
<p>3° Lorsqu'un militaire consulte sur prescription d'un médecin des armées ;</p>
<p>4° Lorsque, à l'occasion des soins qu'elle lui dispense, une sage-femme adresse le patient à un autre médecin ;</p>
<p>5° Pendant l'année qui suit le départ à la retraite ou le changement de département du médecin déclaré par les patients comme médecin traitant.</p>
''',
    "Réécriture à droit constant : les démarches de déclaration et les accords requis sont formulés avec un sujet explicite ; la majoration et ses exclusions sont présentées dans des phrases distinctes. Les douze alinéas et les cinq exceptions numérotées sont conservés. Aucune réforme de fond de policy.json ne vise ce parcours de soins.",
    "Le seuil de seize ans, l'année d'exemption du 5° et les conditions de désignation conjointe sont conservés. Incohérence de renvoi préexistante : L. 162-5-4 vise l'avant-dernier alinéa du présent article, qui correspond ici au 4°, alors que la règle de majoration figure au sixième alinéa ; une coordination explicite de L. 162-5-4 doit être examinée. Le renvoi du quatrième alinéa à L. 161-36-1 est conservé, mais cette cible est absente du corpus public fourni : sa validité et sa coordination avec les dispositions relatives au dossier médical partagé du code de la santé publique restent à contrôler, sans substituer de numéro. Le médecin référent et les avantages historiques de l'option sont maintenus.")

add('L162-5-4', '''
<p>Un décret fixe la durée pendant laquelle les dispositions prises en application du 18° de l'article L. 162-5, de l'avant-dernier alinéa de l'article L. 162-5-3 et du troisième alinéa de l'article L. 162-26 ne s'appliquent pas aux consultations assurées ou prescrites par un médecin généraliste qui s'installe pour la première fois en exercice libéral. Il fixe également la durée pendant laquelle ces mêmes dispositions ne s'appliquent pas aux consultations assurées ou prescrites par un médecin généraliste qui s'installe dans une zone définie par l'agence régionale de santé ou qui exerce dans un centre de santé nouvellement agréé situé dans une telle zone.</p>
''',
    "Réécriture à droit constant : les deux durées d'exemption relevant du décret sont distinguées, et la seconde phrase explicite les deux situations d'installation ou d'exercice dans une zone définie par l'agence régionale de santé. Aucun nouveau délai ni critère de zonage n'est créé ; aucune réforme de fond du projet n'est applicable.",
    "Le renvoi à l'avant-dernier alinéa de L. 162-5-3 est préexistant et problématique : dans la source assignée, cet alinéa est le 4° relatif à l'adressage par une sage-femme, tandis que la majoration figure au sixième alinéa. Il est conservé en attente d'une coordination explicite. Le troisième alinéa de L. 162-26 et le 18° de L. 162-5 ont été vérifiés dans le corpus et portent bien sur des majorations ou dépassements. La formulation source relative au généraliste « qui s'installe ou exerçant » est grammaticalement défectueuse ; la proposition retient le rattachement de la zone aux deux situations, à confirmer lors du contrôle de portée.")

add('L162-5-10', '''
<p>Les organismes d'assurance maladie remboursent sur la base d'un tarif d'autorité les honoraires, les rémunérations et les frais accessoires des médecins qui n'adhèrent pas à la convention nationale des médecins ou qui ne sont pas régis par le règlement mentionné à l'article L. 162-14-2. Ce tarif d'autorité est fixé par arrêté interministériel.</p>
''',
    "Réécriture à droit constant : les organismes d'assurance maladie deviennent le sujet de la règle de remboursement. Les trois catégories de frais, les deux situations alternatives des médecins et le tarif d'autorité sont maintenus. Aucune réforme de fond n'est appliquée.",
    "La source est signalée ABROGE_DIFF, avec une fin de validité au 1er janvier 2027. La proposition réécrit la version assignée sans neutraliser cette abrogation différée ni inventer une entrée en vigueur de réforme. Le renvoi à L. 162-14-2 et la compétence de l'arrêté interministériel sont conservés.")

add('L162-5-11', '''
<p>I. - Pendant le stage qu'ils accomplissent en application du premier alinéa du II de l'article L. 632-2 du code de l'éducation, les étudiants en médecine générale facturent les soins qu'ils délivrent pour le compte du praticien agréé maître de stage ou de la structure agréée comme lieu de stage. Ils appliquent les règles de tarification fixées par la convention mentionnée à l'article L. 162-5 du présent code. Aucun dépassement de ces tarifs n'est autorisé. Les assurés qu'ils prennent en charge sont dispensés d'avancer les frais correspondant à la part prise en charge par les régimes obligatoires d'assurance maladie.</p>
<p>Par dérogation aux articles L. 161-36-2 et L. 161-36-3, les frais facturés en tiers payant ne donnent lieu à aucun versement au praticien ou à la structure agréée, ni pour la part prise en charge par les régimes obligatoires d'assurance maladie ni pour la participation prise en charge en application du 1° de l'article L. 861-3.</p>
<p>II. - Le centre hospitalier universitaire auquel sont rattachés les étudiants en dernière année du diplôme d'études spécialisées de médecine générale assure le paiement de leur rémunération.</p>
<p>III. - Un décret en Conseil d'Etat détermine les conditions d'application du présent article.</p>
''',
    "Réécriture à droit constant : les obligations de facturation, de tarification et de dispense d'avance sont décomposées ; le centre hospitalier universitaire est expressément désigné comme payeur de la rémunération. Les I à III et la dérogation au tiers payant sont conservés, sans réforme de fond.",
    "Le non-versement au praticien ou à la structure agréée concerne les deux parts désignées au deuxième alinéa ; il ne faut pas le transformer en suppression de la prise en charge des assurés. Les renvois à L. 161-36-2 et L. 161-36-3 ont été vérifiés dans le corpus. La note source indique l'entrée en vigueur immédiate de la rédaction issue de la loi n° 2025-1403 du 30 décembre 2025 ; cette indication historique n'est pas une date de réforme nouvelle. Le II vise seulement les étudiants en dernière année, sans restreindre à cette année le I.")

add('L162-5-13', '''
<p>I. - Les médecins mentionnés à l'article L. 162-5 ne peuvent facturer de dépassement de tarif pour les actes dispensés aux bénéficiaires du droit à la protection complémentaire en matière de santé, sauf en cas d'exigence particulière du patient, notamment pour une visite médicalement injustifiée, ou dans le cas prévu au 18° de l'article L. 162-5.</p>
<p>I bis. - Les médecins ne peuvent dépasser les tarifs mentionnés au I pour les actes dispensés aux personnes écrouées affiliées aux assurances maladie et maternité du régime général en application du premier alinéa de l'article L. 381-30.</p>
<p>I ter. - Les professionnels de santé ne peuvent pratiquer de dépassement d'honoraires pour les missions qu'ils réalisent dans le cadre de la mise en œuvre de la procédure prévue à la section 2 bis du chapitre Ier du titre Ier du livre Ier de la première partie du code de la santé publique.</p>
<p>II. - Lorsqu'elles autorisent des honoraires différents des tarifs qu'elles fixent, la ou les conventions médicales prévues à l'article L. 162-5 du présent code peuvent fixer soit un plafond de dépassement par acte, soit un plafond annuel des dépassements perçus par un praticien pour l'ensemble de son activité. Ce plafond annuel peut être déterminé en fonction du montant total des dépassements constatés l'année précédente.</p>
''',
    "Réécriture à droit constant : les interdictions sont formulées comme des obligations des professionnels ; les deux exceptions du I et les deux formes de plafonnement du II sont rendues plus lisibles. Les subdivisions I, I bis, I ter et II sont maintenues. Aucune réforme de fond n'est ajoutée.",
    "Les exceptions du I ne sont pas étendues au I bis ou au I ter. Le renvoi complet du I ter à la section 2 bis du code de la santé publique est conservé sans désigner autrement la procédure. Le II conserve une faculté conventionnelle, non une obligation de plafonner, ainsi que la référence à l'année précédente. La version source est applicable à compter du 20 août 2026 selon ses métadonnées ; aucune autre date n'est introduite.")

add('L162-5-14', '''
<p>L'assurance maladie prend en charge les frais de permanence des soins prévue à l'article L. 6314-1 du code de la santé publique, assurée par les médecins mentionnés au premier alinéa de l'article L. 6314-1. Elle prend également en charge les frais de régulation de médecine ambulatoire prévue au deuxième alinéa de l'article L. 6311-3 du même code, assurée par les médecins mentionnés au quatrième alinéa de l'article L. 6311-3. Cette prise en charge s'effectue sur la base des tarifs fixés pour les médecins conventionnés régis par les articles L. 162-5 et L. 162-14-1 du présent code. Les médecins concernés doivent respecter ces tarifs.</p>
<p>Pour l'application du II de l'article L. 1435-5 du code de la santé publique, et par dérogation au premier alinéa du présent article, le fonds défini à l'article L. 1435-8 du même code finance les frais des actes effectués dans le cadre de la permanence des soins prévue à l'article L. 6314-1 de ce code par les médecins mentionnés au premier alinéa de ce dernier article. Ce financement repose sur les tarifs fixés pour les médecins conventionnés régis par les articles L. 162-5 et L. 162-14-1 du présent code.</p>
''',
    "Réécriture à droit constant : le premier alinéa distingue la permanence des soins de la régulation de médecine ambulatoire ; le second désigne directement le fonds chargé du financement dérogatoire. Les deux alinéas, les catégories de médecins et les bases tarifaires sont conservés. Aucune réforme de fond ne concerne ce financement.",
    "La dérogation du second alinéa demeure limitée aux actes de permanence des soins et à l'application du II de L. 1435-5 ; elle n'est pas étendue à la régulation ambulatoire. Les références aux premier, deuxième et quatrième alinéas des articles du code de la santé publique sont conservées. La note source rattache l'entrée en vigueur immédiate à la loi n° 2025-1403 du 30 décembre 2025, sans fournir de date pour une réforme future.")

add('L162-5-14-2', '''
<p>L'assurance maladie prend en charge les frais de l'examen nécessaire à l'établissement du certificat de décès mentionné au premier alinéa de l'article L. 2223-42 du code général des collectivités territoriales, lorsque cet examen est réalisé au domicile du patient, aux horaires et dans les conditions fixés par décret. Cette prise en charge repose sur un forfait fixé par arrêté des ministres chargés de la santé et de la sécurité sociale. Les médecins doivent respecter les tarifs ainsi fixés.</p>
''',
    "Réécriture à droit constant : l'organisme chargé de la prise en charge, les conditions de l'examen et la fixation du forfait sont exposés dans trois phrases. L'attribut de présentation du div source est supprimé. Aucune réforme de fond n'est appliquée.",
    "Le domicile du patient et les horaires fixés par décret restent des conditions de prise en charge. Le forfait demeure fixé conjointement par les ministres chargés de la santé et de la sécurité sociale. Ne pas aligner silencieusement ce dispositif médical sur L. 162-12-5, qui prévoit un financement distinct pour l'examen dans le cadre des dispositions relatives aux infirmiers.")

add('L162-5-15', '''
<p>Chaque médecin qui exerce tout ou partie de ses fonctions, à titre libéral ou salarié, dans un établissement mentionné à l'article L. 162-22 du présent code est identifié par un numéro personnel distinct du numéro de la structure dans laquelle il exerce au moins une partie de son activité. Cette règle s'applique également aux médecins salariés d'un centre de santé mentionné à l'article L. 6323-1 du code de la santé publique.</p>
<p>Le décret prévu au premier alinéa de l'article L. 161-33 du présent code précise les cas dans lesquels le numéro personnel du médecin et, le cas échéant, le numéro de la structure dans laquelle l'acte, la consultation ou la prescription a été réalisé doivent figurer sur les documents transmis aux caisses d'assurance maladie pour obtenir le remboursement ou la prise en charge des soins dispensés par ces praticiens.</p>
''',
    "Réécriture à droit constant : l'identification individuelle est formulée pour chaque médecin, puis étendue explicitement aux médecins salariés des centres de santé comme dans la source. Les deux alinéas et la distinction entre identifiant personnel et identifiant de structure sont maintenus. Aucune réforme de fond n'est appliquée.",
    "Le champ comprend l'exercice libéral ou salarié, total ou partiel, dans les établissements visés, mais seulement les médecins salariés pour les centres de santé. Le caractère « le cas échéant » du numéro de structure au second alinéa est conservé. La note source fixe au 1er janvier 2024 l'entrée en vigueur de la rédaction concernée, conformément au VII de l'article 49 de la loi n° 2023-1250 du 26 décembre 2023 ; cette date reste une donnée historique.")

add('L162-5-16', '''
<p>Lorsqu'une prescription exécutée par des professionnels de santé exerçant en ville n'est pas exactement identifiée par le numéro personnel mentionné à l'article L. 162-5-15 et par le numéro de la structure, les organismes de sécurité sociale imputent les dépenses correspondantes qu'ils constatent sur leurs versements à l'établissement de santé ou au centre de santé dans lequel exerce le médecin prescripteur.</p>
''',
    "Réécriture à droit constant : la condition d'identification est placée en tête de phrase et les organismes de sécurité sociale sont désignés comme sujets de l'imputation. L'exécution en ville, les deux identifiants et les destinataires des versements sont conservés. Aucune réforme de fond n'est apportée.",
    "L'imputation porte sur les versements à l'établissement ou au centre du médecin prescripteur ; elle n'est transformée ni en facturation au patient ni en sanction du professionnel exécutant. Le défaut d'identification exacte par les deux numéros reste distinct de la seule absence du numéro personnel traitée à L. 162-5-17.")

add('L162-5-17', '''
<p>Les organismes de sécurité sociale ne prennent pas en charge les dépenses correspondant aux prescriptions de spécialités pharmaceutiques mentionnées aux articles L. 162-22-7 et L. 162-23-6 lorsque ces prescriptions ne sont pas identifiées par le numéro personnel mentionné à l'article L. 162-5-15.</p>
<p>Il est interdit de facturer ces dépenses au patient.</p>
''',
    "Réécriture à droit constant : le défaut d'identification devient une condition explicite de non-prise en charge et l'interdiction de facturer le patient est formulée directement. Les deux alinéas et les deux catégories légales de spécialités sont conservés. Aucune réforme de fond n'est appliquée.",
    "Les articles L. 162-22-7 et L. 162-23-6 ont été vérifiés dans le corpus : ils visent des spécialités prises en charge en sus des prestations d'hospitalisation. Aucun numéro de structure supplémentaire n'est exigé dans cet article. L'interdiction de faire supporter les dépenses au patient est intégralement maintenue.")

add('L162-5-18', '''
<p>Le pharmacien qui exécute une ordonnance comportant ou devant comporter le numéro personnel et le numéro de la structure mentionnés à l'article L. 162-5-15 doit reporter ces numéros sur les documents transmis aux caisses d'assurance maladie ou, le cas échéant, y signaler leur absence.</p>
<p>Le non-respect de cette obligation ou la transmission d'éléments erronés peut donner lieu au recouvrement de l'indu auprès du pharmacien, selon la procédure prévue à l'article L. 133-4.</p>
''',
    "Réécriture à droit constant : l'obligation du pharmacien de reporter les identifiants ou d'en signaler l'absence est explicitée ; la seconde phrase indique directement auprès de qui l'indu peut être recouvré. Les deux alinéas sont conservés sans réforme de fond.",
    "L'obligation couvre aussi l'ordonnance qui devrait comporter les numéros. Le recouvrement demeure une possibilité, pour manquement ou éléments erronés, dans les conditions de L. 133-4 ; il n'est pas rendu automatique. Coordination conservée avec l'identification prévue à L. 162-5-15.")

add('L162-8', '''
<p>Les chirurgiens-dentistes, les sages-femmes et les auxiliaires médicaux sont soumis aux dispositions de l'article L. 162-4 dans la mesure où elles les concernent.</p>
''',
    "Réécriture à droit constant : les trois professions deviennent le sujet de la règle d'application, avec maintien de la réserve « dans la mesure où elles les concernent ». Aucun élargissement de champ ni réforme de fond n'est introduit.",
    "Le renvoi à L. 162-4 est maintenu. La réserve de pertinence propre à chaque profession interdit de présenter le renvoi comme une extension indifférenciée de toutes les prescriptions de cet article.")

add('L162-8-1', '''
<p>Lorsqu'une sage-femme prescrit à une assurée âgée de moins de 26 ans un contraceptif mentionné au 21° de l'article L. 160-14 ou des examens de biologie médicale en vue d'une prescription contraceptive, elle doit dispenser cette assurée d'avancer les frais correspondant à la part des dépenses prise en charge par l'assurance maladie. Elle doit également lui accorder cette dispense pour les actes de pose, de changement ou de retrait d'un contraceptif. L'assurance maladie prend en charge cette dispense au moyen de l'identification électronique du praticien.</p>
''',
    "Réécriture à droit constant : les prescriptions ouvrant droit à la dispense d'avance de frais et les actes contraceptifs concernés sont exposés dans des phrases distinctes. Le seuil d'âge, la part financée et le moyen d'identification sont maintenus. Aucune réforme de fond n'est apportée.",
    "Le seuil strict de moins de 26 ans, le 21° de L. 160-14 et les actes de pose, de changement et de retrait sont conservés. La source vise le moyen d'identification électronique du praticien : cette formulation est maintenue sans la remplacer par celui de l'assurée. La note source fait état d'une entrée en vigueur au 1er janvier 2022 en application du II de l'article 85 de la loi n° 2021-1754 du 23 décembre 2021 ; elle n'établit aucune date de réforme future.")

add('L162-8-2', '''
<p>Pendant et après la grossesse, l'assurée ou l'ayant droit peut déclarer le nom de sa sage-femme référente à l'organisme gestionnaire de son régime de base d'assurance maladie, afin de favoriser la coordination des soins en lien avec le médecin.<br /><br />Les modalités d'application du présent article sont fixées par voie réglementaire.</p>
''',
    "Réécriture à droit constant : le cadre temporel est placé en tête et l'organisme destinataire de la déclaration est exprimé plus directement. La faculté de déclaration, le lien avec le médecin et la compétence réglementaire sont conservés, sans réforme de fond.",
    "La déclaration reste facultative et concerne la période pendant et après la grossesse. L'ordre des deux alinéas matérialisés par les sauts de ligne est conservé. Aucun accord préalable supplémentaire du médecin ou de la sage-femme n'est ajouté.")

add('L162-9', '''
<p>Des conventions nationales définissent les rapports entre les organismes d'assurance maladie et les chirurgiens-dentistes, les sages-femmes et les auxiliaires médicaux. Elles sont conclues entre l'Union nationale des caisses d'assurance maladie et une ou plusieurs des organisations syndicales nationales les plus représentatives de chacune de ces professions.</p>
<p>Ces conventions déterminent :</p>
<p>1°) Les obligations respectives des caisses primaires d'assurance maladie, des chirurgiens-dentistes, des sages-femmes et des auxiliaires médicaux ;</p>
<p>2°) Les mesures que les partenaires conventionnels estiment appropriées pour garantir la qualité des soins dispensés aux assurés sociaux par les chirurgiens-dentistes, les sages-femmes ou les auxiliaires médicaux. Ces mesures portent notamment sur la sélection des thèmes des références professionnelles, l'opposabilité de ces références et les conditions de cette opposabilité ;</p>
<p>3°) La possibilité de mettre à la charge du chirurgien-dentiste, de la sage-femme ou de l'auxiliaire médical qui ne respecte pas les mesures prévues au 2° du présent article tout ou partie des cotisations mentionnées aux articles L. 621-2 et L. 645-2, ou une partie de la dépense des régimes d'assurance maladie correspondant aux honoraires perçus pour les soins dispensés en méconnaissance de ces mesures ;</p>
<p>4°) Pour les chirurgiens-dentistes, le cas échéant, les conditions visant à éviter que l'assuré social paie directement les honoraires ;</p>
<p>5°) Le cas échéant :</p>
<p>a) Les conditions particulières d'exercice favorisant la coordination des soins ;</p>
<p>b) Les conditions particulières d'exercice permettant la prise en charge globale des patients dans des réseaux de soins, ainsi que les modes de rémunération des professionnels mentionnés au 1° qui participent à ces réseaux ;</p>
<p>c) Les droits et obligations respectifs des professionnels mentionnés au 1°, des patients et des caisses, ainsi que les modalités d'évaluation associées aux formes d'exercice et aux modes de rémunération mentionnés aux a et b ci-dessus ;</p>
<p>6°) Le cas échéant, les modes de rémunération autres que le paiement à l'acte pour les activités de soins, ainsi que les modes de rémunération des activités non curatives des professionnels mentionnés au 1° ;</p>
<p>7°) Les mesures d'adaptation, notamment incitatives, des dispositions de l'article L. 162-14-1 et du présent article applicables aux chirurgiens-dentistes, aux sages-femmes et aux auxiliaires médicaux, en fonction du niveau de l'offre de soins dans chaque région, au sein des zones définies par l'agence régionale de santé en application de l'article L. 1434-4 du code de la santé publique. Ces modalités sont définies après concertation avec les organisations les plus représentatives des étudiants et des jeunes chirurgiens-dentistes, sages-femmes et auxiliaires médicaux ;</p>
<p>7° bis) Les propositions d'orientations pluriannuelles prioritaires en matière de développement professionnel continu relevant de l'article L. 4021-2 du code de la santé publique ;</p>
<p>8° Les conditions que doivent remplir les sages-femmes et les chirurgiens-dentistes pour être conventionnés, notamment celles qui concernent les modalités de leur exercice professionnel, leur formation et les zones d'exercice définies par l'agence régionale de santé en application de l'article L. 1434-4 du code de la santé publique.</p>
<p>9° Pour les masseurs-kinésithérapeutes, les conditions de prise en charge des actes résultant des renouvellements qu'ils établissent sur le fondement de l'article L. 4321-1 du code de la santé publique ;</p>
<p>10° Pour les orthophonistes, les modalités d'application du sixième alinéa de l'article L. 4341-1 du code de la santé publique ;</p>
<p>11° Les modalités de rémunération, au titre de leur participation à la permanence des soins, des professionnels de santé mentionnés au dernier alinéa de l'article L. 6314-1 du code de la santé publique.</p>
<p>Ces conventions fixent également les modalités d'application du 3°, notamment les conditions dans lesquelles le professionnel concerné présente ses observations.</p>
<p>Lorsqu'elle autorise un dépassement pour les soins visés au 3° de l'article L. 861-3, la convention nationale concernant les chirurgiens-dentistes en fixe le montant maximal applicable aux bénéficiaires du droit à la protection complémentaire en matière de santé mentionnés à l'article L. 861-1. En l'absence de convention, ou si celle-ci ne comporte pas de dispositions propres aux bénéficiaires de cette protection, un arrêté des ministres chargés de la santé et de la sécurité sociale fixe la limite de dépassement applicable à ces bénéficiaires.</p>
''',
    "Réécriture à droit constant : les parties aux conventions sont présentées dans deux phrases ; les domaines conventionnels et la garantie de présentation d'observations sont formulés plus directement. L'intégralité des 1° à 11°, du 7° bis et des a à c est maintenue dans le même ordre, ainsi que le plafonnement des dépassements pour la protection complémentaire. Aucune réforme de fond n'est introduite.",
    "Les dix-neuf alinéas sont conservés. Le 3° conserve l'alternative entre tout ou partie des cotisations et une partie de la dépense, sans étendre cette dernière à la totalité. Les mentions « le cas échéant », la concertation préalable du 7° et la faculté de dépassement encadrée au dernier alinéa sont maintenues. Les renvois au sixième alinéa de L. 4341-1 et au dernier alinéa de L. 6314-1 du code de la santé publique appellent un contrôle dans ce code, absent du corpus fourni. L'exclusion spéciale des infirmiers prévue à L. 162-12-4 est maintenue dans le lot.")

add('L162-11', '''
<p>En l'absence de convention nationale, des conventions fixent les tarifs des honoraires et des frais accessoires dus aux chirurgiens-dentistes, aux sages-femmes et aux auxiliaires médicaux pour les soins dispensés aux assurés sociaux et à leurs ayants droit. Elles fixent également la participation au financement des cotisations prévue au 5° du I de l'article L. 162-14-1. Ces conventions sont conclues entre les caisses primaires d'assurance maladie et un ou plusieurs des syndicats les plus représentatifs de chacune de ces professions. Elles respectent la limite des tarifs fixés par arrêté interministériel.</p>
<p>Les conventions doivent respecter les clauses des conventions types établies par décret en Conseil d'Etat. Elles n'entrent en vigueur qu'après leur approbation par l'autorité administrative.</p>
<p>Dès leur approbation, les conventions s'appliquent à tous les membres des professions concernées qui exercent dans la circonscription de la caisse primaire. Sont toutefois exclus ceux qui ont fait savoir à la caisse, dans les conditions fixées par la convention type, qu'ils refusent d'être régis par la convention.</p>
<p>Lorsqu'un membre de l'une des professions concernées ne respecte pas ses engagements conventionnels, la caisse primaire d'assurance maladie peut décider de le placer hors de la convention dans les conditions prévues par la convention type.</p>
<p>En l'absence de convention conclue avec la caisse primaire, les chirurgiens-dentistes, les sages-femmes et les auxiliaires médicaux peuvent adhérer personnellement aux clauses de la convention type. Cette adhésion repose sur les tarifs fixés dans les conditions prévues au premier alinéa du présent article.</p>
''',
    "Réécriture à droit constant : chaque étape du régime départemental est formulée dans son alinéa d'origine, de la fixation des tarifs à l'adhésion personnelle. Les conditions d'approbation, l'exception de refus individuel et la faculté de placement hors convention sont explicitées. Aucune réforme de fond n'est appliquée.",
    "Les cinq alinéas et le renvoi final au premier alinéa sont conservés. La limite tarifaire interministérielle, le 5° du I de L. 162-14-1 et l'approbation administrative préalable sont maintenus. L'application aux auxiliaires médicaux reste soumise à l'exclusion des infirmiers par L. 162-12-4 ; le présent texte n'étend pas à ceux-ci les conventions départementales.")

add('L162-12', '''
<p>Des arrêtés interministériels fixent les tarifs servant de base au remboursement des honoraires des chirurgiens-dentistes, des sages-femmes et des auxiliaires médicaux lorsqu'il n'existe pas de convention ou que le professionnel n'a pas adhéré personnellement à la convention type.</p>
''',
    "Réécriture à droit constant : les arrêtés interministériels et leur objet sont placés en tête ; les deux situations alternatives déclenchant leur application sont exprimées explicitement. Aucun tarif ni réforme de fond n'est créé.",
    "L'absence de convention et l'absence d'adhésion personnelle restent reliées par une alternative. Le tarif constitue une base de remboursement des honoraires, sans être transformé en plafond des honoraires. L'exclusion des infirmiers à L. 162-12-4 est conservée.")

add('L162-12-1', '''
<p>Les infirmiers doivent réaliser leurs actes conformément aux dispositions prises pour l'application du titre II du livre IV du code de la santé publique. Ils doivent respecter la plus stricte économie compatible avec l'exécution des prescriptions.</p>
''',
    "Réécriture à droit constant : les obligations de conformité et d'économie sont séparées en deux phrases, sans réduire l'exigence de la plus stricte économie compatible avec les prescriptions. Aucun changement de fond n'est apporté.",
    "Le renvoi au titre II du livre IV du code de la santé publique figure déjà dans la version source datée du 5 janvier 1993. Son adéquation à la structure actuelle de ce code doit être contrôlée : le code de la santé publique n'est pas inclus dans le corpus fourni. Aucun intitulé ni numéro de remplacement n'est inventé. La portée se limite aux dispositions prises pour l'application de ce titre.")

add('L162-12-2', '''
<p>Une convention nationale définit les rapports entre les organismes d'assurance maladie et les infirmiers, dans le respect des règles déontologiques fixées par le code de la santé publique. Elle est conclue pour une durée maximale de cinq ans entre une ou plusieurs organisations syndicales les plus représentatives des infirmiers et l'Union nationale des caisses d'assurance maladie.</p>
<p>Cette convention détermine notamment :</p>
<p>1° Les obligations respectives des caisses primaires d'assurance maladie et des infirmiers, ainsi que les conditions de prise en charge des actes effectués par un infirmier remplaçant un infirmier conventionné, de ceux effectués par les infirmiers conventionnés dans les établissements et les structures d'hébergement de toute nature, et de ceux effectués par les infirmiers en pratique avancée, le cas échéant sans adressage préalable par un médecin ;</p>
<p>1° bis Les orientations pluriannuelles prioritaires en matière de développement professionnel continu relevant de l'article L. 4021-2 du code de la santé publique ;</p>
<p>2° (Abrogé) ;</p>
<p>3° Les conditions que les infirmiers doivent remplir pour être conventionnés, notamment celles qui concernent la durée minimale d'expérience professionnelle acquise en équipe de soins généraux au sein d'un service organisé, les sanctions éventuellement prononcées à leur encontre pour des faits liés à l'exercice de leur profession, le suivi d'actions de formation et la zone d'exercice définie par l'agence régionale de santé en application de l'article L. 1434-4 du code de la santé publique ;</p>
<p>4° Le financement des instances nécessaires à la mise en œuvre de la convention et de ses annexes annuelles ;</p>
<p>5° Les mesures que les partenaires conventionnels estiment appropriées pour garantir la qualité des soins infirmiers dispensés aux assurés sociaux. Ces mesures portent notamment sur la sélection des thèmes des références professionnelles, l'opposabilité de ces références et les conditions de cette opposabilité ;</p>
<p>6° Le cas échéant :</p>
<p>a) Les conditions particulières d'exercice favorisant la coordination des soins ;</p>
<p>b) Les conditions particulières d'exercice permettant la prise en charge globale des patients dans des réseaux de soins, ainsi que les modes de rémunération des infirmiers qui participent à ces réseaux ;</p>
<p>c) Les droits et obligations respectifs des infirmiers, des patients et des caisses, ainsi que les modalités d'évaluation associées aux formes d'exercice et aux modes de rémunération mentionnés aux a et b ci-dessus ;</p>
<p>7° Le cas échéant, les modes de rémunération autres que le paiement à l'acte pour les activités de soins, ainsi que les modes de rémunération des activités non curatives des infirmiers ;</p>
<p>8° Les mesures d'adaptation, notamment incitatives, des dispositions de l'article L. 162-14-1 et du présent article applicables aux infirmiers, en fonction du niveau de l'offre de soins dans chaque région, au sein des zones définies par l'agence régionale de santé en application de l'article L. 1434-4 du code de la santé publique. Ces modalités sont définies après concertation avec les organisations les plus représentatives des étudiants et des jeunes infirmiers ;</p>
<p>9° Les conditions de facturation des indemnités kilométriques, comprenant notamment une définition nationale de l'agglomération.</p>
''',
    "Réécriture à droit constant : l'objet et la durée de la convention sont exposés séparément ; les conditions de conventionnement et les domaines de négociation sont rendus plus lisibles. Les quinze alinéas, le 1° bis, l'emplacement abrogé du 2° et les a à c sont conservés. Aucune réforme de fond n'est appliquée aux infirmiers.",
    "La durée maximale reste de cinq ans. Le 1° conserve les trois catégories d'actes et réserve l'absence éventuelle d'adressage préalable aux actes des infirmiers en pratique avancée. L'expérience en équipe de soins généraux au sein d'un service organisé, les sanctions, la formation, le zonage et la concertation avec les étudiants et jeunes infirmiers sont maintenus. Le 5° reste au même rang pour le renvoi de L. 162-12-3 ; le 9° conserve la définition nationale de l'agglomération sans en inventer le contenu.")

add('L162-12-2-1', '''
<p>Pour favoriser la coordination des soins, l'assuré ou l'ayant droit âgé de seize ans ou plus, atteint d'une affection mentionnée au 3° de l'article L. 160-14 qui nécessite des soins infirmiers, peut déclarer à l'organisme gestionnaire de son régime de base d'assurance maladie le nom de l'infirmier référent qu'il a choisi avec l'accord de cet infirmier. Pour un ayant droit mineur, ce choix nécessite l'accord d'au moins l'un des deux parents ou du titulaire de l'autorité parentale.<br /><br />Plusieurs infirmiers peuvent être désignés conjointement infirmiers référents s'ils exercent au sein d'un cabinet situé dans les mêmes locaux, d'un même centre de santé mentionné à l'article L. 6323-1 du code de la santé publique ou d'une même maison de santé mentionnée à l'article L. 6323-3 de ce code.<br /><br />L'infirmier référent exerce une mission de prévention, de suivi et de recours, en lien étroit avec le médecin traitant et le pharmacien correspondant.<br /><br />Pour les ayants droit âgés de moins de seize ans, au moins l'un des deux parents ou le titulaire de l'autorité parentale peut déclarer à l'organisme gestionnaire du régime de base d'assurance maladie le nom de l'infirmier référent qu'il a choisi avec l'accord de cet infirmier.<br /><br />Les modalités d'application du présent article sont fixées par voie réglementaire.</p>
''',
    "Réécriture à droit constant : les accords nécessaires, la désignation conjointe et les missions de l'infirmier référent sont exprimés directement. Les cinq alinéas matérialisés par les sauts de ligne restent dans leur ordre d'origine. Aucune réforme de fond n'est apportée.",
    "Les deux tranches d'âge, l'affection nécessitant des soins infirmiers visée au premier alinéa, l'accord de l'infirmier et les accords parentaux requis sont conservés. Le quatrième alinéa ne répète pas la condition d'affection du premier : cette dissymétrie préexistante est maintenue, sans étendre silencieusement la condition aux moins de seize ans. La désignation conjointe reste limitée aux locaux ou structures communs indiqués dans la source. Les liens avec le médecin traitant et le pharmacien correspondant ne sont pas transformés en autorisation préalable.")

add('L162-12-3', '''
<p>La convention nationale prévoit la possibilité de mettre à la charge de l'infirmier qui ne respecte pas les mesures prévues au 5° de l'article L. 162-12-2 une partie de la dépense des régimes d'assurance maladie correspondant aux honoraires qu'il a perçus pour les soins dispensés en méconnaissance de ces mesures.</p>
<p>Elle fixe les modalités d'application de l'alinéa précédent, notamment les conditions dans lesquelles le professionnel concerné présente ses observations.</p>
''',
    "Réécriture à droit constant : le rattachement des honoraires aux soins dispensés en méconnaissance des mesures de qualité est clarifié, et la garantie de présentation d'observations est conservée dans un alinéa distinct. Aucune réforme de fond n'est introduite.",
    "La convention doit prévoir une possibilité de mise à charge ; l'imputation n'est pas rendue automatique. Seule une partie de la dépense est visée. Le renvoi au 5° de L. 162-12-2 et celui au premier alinéa du présent article demeurent opérants, les subdivisions et alinéas correspondants étant conservés.")

add('L162-12-4', '''
<p>Les infirmiers ne sont pas soumis aux dispositions des articles L. 162-9 à L. 162-12.</p>
''',
    "Réécriture à droit constant : les infirmiers deviennent le sujet de l'exclusion, sans changer la plage des articles exclus. Aucune réforme de fond n'est apportée.",
    "L'exclusion vise les articles L. 162-9 à L. 162-12, et non les articles L. 162-12-1 et suivants. Elle demeure la coordination du régime conventionnel propre aux infirmiers avec les règles générales des autres professions.")

add('L162-12-5', '''
<p>Par dérogation aux articles L. 162-12-2 et L. 162-14-1, l'assurance maladie ou la branche mentionnée au 5° de l'article L. 200-2 du présent code prend en charge les frais de l'examen nécessaire à l'établissement du certificat de décès mentionné au premier alinéa de l'article L. 2223-42 du code général des collectivités territoriales. Un arrêté des ministres chargés de la santé et de la sécurité sociale fixe les conditions de cette prise en charge.</p>
''',
    "Réécriture à droit constant : le payeur est désigné directement, puis la compétence ministérielle pour fixer les conditions est isolée dans une seconde phrase. L'alinéa unique et les deux dérogations sont conservés ; l'attribut de présentation source est supprimé. Aucune réforme de fond n'est appliquée.",
    "Le 5° de L. 200-2 a été vérifié dans le corpus et désigne la branche Autonomie. L'alternative de financement est conservée sans créer de critère de répartition. Le texte ne reçoit ni la condition de domicile ni celle d'horaire prévues pour les médecins à L. 162-5-14-2. Le renvoi au premier alinéa de L. 2223-42 et l'arrêté conjoint des deux ministres sont maintenus.")

add('L162-12-8', '''
<p>Les masseurs-kinésithérapeutes doivent réaliser leurs actes conformément aux dispositions du titre III du livre IV du code de la santé publique et aux mesures prises pour leur application. Ils doivent respecter la plus stricte économie compatible avec l'exécution des prescriptions.</p>
''',
    "Réécriture à droit constant : les obligations de conformité et d'économie sont distinguées en deux phrases, avec maintien du titre visé et de ses mesures d'application. Aucune réforme de fond n'est apportée.",
    "Le renvoi au titre III du livre IV du code de la santé publique figure dans la version source datée du 27 juillet 1994. Son adéquation à la structure actuelle de ce code doit être contrôlée hors du corpus fourni ; aucun renvoi de substitution n'est inventé. Contrairement à L. 162-12-1, la source vise à la fois les dispositions du titre et leurs mesures d'application : cette différence est conservée.")


assert len(sources) == 24
assert set(drafts) == {a['number'] for a in sources}
answer = []
for source in sources:
    record = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    record.update(drafts[source['number']])
    answer.append(record)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
