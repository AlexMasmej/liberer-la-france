import json
from pathlib import Path


drafts = {}


def add(number, proposed_xml, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        "proposed_xml": proposed_xml.strip(),
        "reason": reason,
        "review_notes": review_notes,
    }


add(
    "L256-10",
    """
<p>Pour tout projet de vente des droits réels immobiliers portant sur le bien faisant l'objet du bail réel solidaire d'activité au titre de l'article L. 256-4, l'avant-contrat mentionne expressément l'objet du contrat et son caractère indissociable du bail réel solidaire d'activité signé avec l'organisme de foncier solidaire. Il mentionne aussi expressément le caractère temporaire du droit réel immobilier, la nouvelle durée du bail si l'organisme de foncier solidaire agrée la transmission des droits réels immobiliers, les conditions dans lesquelles cet organisme délivre son agrément et les modalités de calcul du prix de vente ou de la valeur donnée prévues par le bail.</p>
<p>L'opérateur informe l'organisme de foncier solidaire de tout avant-contrat conclu dans les trente jours suivant sa signature. Il joint à sa demande l'avant-contrat et les pièces permettant d'établir que l'acquéreur remplit les conditions d'éligibilité.</p>
""",
    "Réécriture à droit constant : les mentions obligatoires de l'avant-contrat sont réparties entre deux phrases, puis l'obligation d'information de l'opérateur et les pièces à fournir sont exprimées directement. Aucune réforme de fond n'est appliquée à ce régime de locaux professionnels ou commerciaux.",
    "Deux alinéas de fond conservés, avec le délai de trente jours, son point de départ à la signature et le renvoi à L. 256-4. La mention de la « valeur donnée », présente dans un article relatif à la vente, est conservée sans en élargir le champ. L'agrément propre aux ventes de l'opérateur reste régi par L. 256-13 ; le délai de trente jours n'est pas assimilé au délai d'agrément de deux mois.",
)

add(
    "L256-11",
    """
<p>L'organisme de foncier solidaire ou l'opérateur assure la publicité préalable de tout projet de cession de droits réels immobiliers par le preneur, selon les modalités prévues à l'article L. 256-5.</p>
""",
    "Réécriture à droit constant : les personnes chargées de la publicité sont placées en sujet de l'obligation et le renvoi qui en fixe les modalités est maintenu. Aucune modification de fond.",
    "Renvoi à L. 256-5 vérifié dans le corpus : cet article distingue la publicité assurée par l'organisme et celle pouvant être assurée par l'opérateur. La rédaction ne crée ni nouveau délai ni nouvelle formalité. L. 256-9, hors lot, cite L. 256-11 à propos des conditions d'agrément, alors que cet article porte sur la publicité : incohérence préexistante à coordonner avec L. 256-12 et L. 256-14, sans correction silencieuse du corpus.",
)

add(
    "L256-12",
    """
<p>La vente ou la donation de droits réels portant sur le bien faisant l'objet du bail réel solidaire d'activité exige l'agrément de l'acquéreur ou du donataire par l'organisme de foncier solidaire.</p>
<p>L'organisme de foncier solidaire dispose de deux mois à compter de la date de transmission de l'offre préalable de cession ou de donation pour délivrer cet agrément. Pour se prononcer, il vérifie le respect des conditions prévues à la section 1 du présent chapitre et la conformité de l'offre avec le bail en vigueur. Il vérifie notamment le respect des stipulations relatives aux modalités de calcul du prix de vente ou d'évaluation des droits réels appartenant au vendeur ou au donateur. Le cas échéant, il vérifie aussi l'équilibre du plan de financement de l'acquisition, qui peut notamment ressortir d'une offre de crédit.</p>
<p>Le non-respect des règles énoncées aux alinéas précédents entraîne la nullité de la vente ou de la donation. Il appartient au cédant ou au donateur de prouver le contenu et la notification de l'offre préalable de vente ou de donation.</p>
""",
    "Réécriture à droit constant : la procédure d'agrément est présentée par étapes et les vérifications sont formulées avec un sujet explicite. La nullité et la charge de la preuve sont conservées ; aucune réforme de fond.",
    "Trois alinéas de fond conservés. Le délai reste de deux mois à compter de la transmission de l'offre, sans agrément tacite ajouté. L'équilibre financier n'est vérifié que le cas échéant et l'offre de crédit demeure un exemple de justification. L. 256-9, hors lot, rattache la nouvelle durée du bail à L. 256-12 alors que la prorogation figure à L. 256-14 ; cette incohérence préexistante appelle une coordination distincte.",
)

add(
    "L256-13",
    """
<p>Pour tout projet de vente des droits réels immobiliers portant sur le bien faisant l'objet du bail réel solidaire d'activité au titre de l'article L. 256-4, l'organisme de foncier solidaire dispose de deux mois à compter de la date de transmission de l'avant-contrat pour délivrer son agrément. Pour se prononcer, il vérifie le respect des conditions définies à la section 1 du présent chapitre et la conformité de l'avant-contrat avec le bail initial conclu entre l'opérateur et cet organisme. Il vérifie notamment le respect des stipulations relatives aux modalités de calcul du prix de vente ou d'évaluation des droits réels immobiliers appartenant à l'opérateur. Le cas échéant, il vérifie aussi l'équilibre du plan de financement de l'acquisition, qui peut notamment ressortir d'une offre de crédit.</p>
<p>Le non-respect des règles énoncées au premier alinéa du présent article entraîne la nullité de la vente. Il appartient à l'opérateur de prouver le contenu et la notification de l'offre préalable de vente.</p>
""",
    "Réécriture à droit constant : les critères de l'agrément de la vente par l'opérateur sont répartis en phrases courtes, sans confondre cette procédure avec celle de L. 256-12. Aucune modification de fond.",
    "Deux alinéas conservés ; le premier reste intégralement visé par la nullité du second. Maintien des deux mois à compter de la transmission de l'avant-contrat et des renvois à L. 256-4 et à la section 1. La source impose au second alinéa la preuve d'une « offre préalable de vente » alors que le premier porte sur l'avant-contrat : terminologie préexistante conservée et à harmoniser seulement par coordination expresse avec L. 256-10.",
)

add(
    "L256-14",
    """
<p>La délivrance de cet agrément proroge de plein droit la durée du bail. Cette prorogation permet à tout nouveau preneur de bénéficier d'un droit réel dont la durée est égale à celle prévue au contrat initial.</p>
""",
    "Réécriture à droit constant : la condition de prorogation et sa portée sont énoncées dans deux phrases. Le caractère automatique de la prorogation et sa durée de référence sont préservés ; aucune réforme de fond.",
    "Un seul alinéa conservé. La rédaction maintient « cet agrément » sans lui substituer un renvoi qui pourrait restreindre la portée du texte. La durée reste celle du contrat initial, et non la durée résiduelle. Coordination à examiner dans L. 256-9, hors lot, qui renvoie à L. 256-12 pour la nouvelle durée du bail.",
)

add(
    "L256-15",
    """
<p>Lorsque l'agrément est refusé à l'occasion d'une cession ou d'une donation, l'organisme de foncier solidaire peut désigner un acquéreur qui remplit les conditions prévues à la section 1 du présent chapitre.</p>
<p>Les conditions d'acquisition doivent respecter les modalités de calcul du prix de vente stipulées dans le bail. Le cas échéant, l'acquéreur désigné par l'organisme de foncier solidaire doit également acquérir le fonds compris dans la même cession ou donation. Si les parties au bail ne parviennent pas à un accord dans les six mois suivant la demande du cédant, elles peuvent résilier conventionnellement le bail réel solidaire d'activité. Le preneur est alors indemnisé de la valeur de ses droits réels immobiliers ainsi que, le cas échéant, du fonds existant, dans les conditions prévues par le bail.</p>
<p>L'indemnisation du fonds comprend notamment sa valeur marchande, déterminée selon les usages de la profession.</p>
""",
    "Réécriture à droit constant : la désignation facultative d'un acquéreur, les conditions d'acquisition et la résiliation conventionnelle sont distinguées par des phrases autonomes. Les droits à indemnisation sont maintenus ; aucune réforme de fond.",
    "Trois alinéas conservés. Maintien du délai de six mois à compter de la demande du cédant, de l'acquisition éventuelle du fonds et de sa valeur marchande déterminée selon les usages professionnels. L'absence d'accord ne devient pas une résiliation automatique : celle-ci reste conventionnelle, à distinguer du mécanisme de L. 256-16.",
)

add(
    "L256-16",
    """
<p>Les droits réels portant sur le bien faisant l'objet du bail réel solidaire sont transmis à l'ayant droit en cas de décès du preneur, de transfert du patrimoine affecté d'une personne physique ou d'apport en société de ce patrimoine dans les conditions prévues à l'article L. 526-17 du code de commerce. Ils lui sont également transmis en cas de transfert universel du patrimoine professionnel d'une personne physique dans les conditions prévues à la section 4 du chapitre VI du titre II du livre V du même code.</p>
<p>Pour les personnes morales, les droits sont également transmis en cas de fusion ou de scission de sociétés, de transmission universelle du patrimoine d'une société réalisée dans les conditions prévues à l'article 1844-5 du code civil, d'apport d'une partie de l'actif d'une société réalisé dans les conditions prévues aux articles L. 236-6-1, L. 236-22 et L. 236-24 du code de commerce ou de dissolution de sociétés à associé unique.</p>
<p>Si l'ayant droit ne remplit pas les conditions requises, il dispose de douze mois à compter de l'événement mentionné à l'un des deux alinéas précédents pour céder les droits réels portant sur le bien faisant l'objet du bail réel solidaire d'activité. L'acquéreur doit remplir les conditions précitées et être agréé par l'organisme de foncier solidaire. Cet organisme peut proroger le délai pour une durée correspondant aux délais nécessaires à la régularisation de la cession des droits réels immobiliers par acte notarié. Si la cession n'intervient pas dans ces délais, le bail réel solidaire d'activité est résilié. L'organisme de foncier solidaire indemnise alors l'ayant droit de la valeur de ses droits réels immobiliers ainsi que, le cas échéant, du fonds existant, à hauteur du préjudice causé par le défaut d'agrément et dans les conditions prévues par le bail.</p>
<p>L'indemnisation du fonds comprend notamment sa valeur marchande, déterminée selon les usages de la profession.</p>
""",
    "Réécriture à droit constant : les transmissions des personnes physiques et morales restent dans leurs alinéas respectifs, tandis que le délai de cession, sa prorogation et les effets de son dépassement sont exprimés séparément. Aucune réforme de fond ni suppression des régimes patrimoniaux historiques.",
    "Quatre alinéas conservés, avec douze mois, la prorogation limitée aux délais de régularisation notariée, la résiliation et les limites de l'indemnisation. Les références à L. 526-17, L. 236-6-1, L. 236-22 et L. 236-24 du code de commerce, à sa section 4 du chapitre VI du titre II du livre V et à l'article 1844-5 du code civil sont conservées ; leur état et leurs transitions doivent être contrôlés dans ces codes, absents du corpus autorisé. Le premier alinéa de la source dit « bail réel solidaire », sans « d'activité » : cette discordance avec le chapitre est signalée et conservée. Les « conditions » de l'ayant droit ne sont pas redéfinies ; leur articulation avec la section 1 et L. 256-6 reste à contrôler.",
)

add(
    "L256-17",
    """
<p>L'organisme de foncier solidaire bénéficie, à l'occasion de toute cession ou donation, d'un droit de préemption à son profit, mentionné dans le bail réel solidaire d'activité. Il peut ainsi racheter les droits réels immobiliers portant sur le bien faisant l'objet du bail ou les faire acquérir par un bénéficiaire qui remplit les conditions définies à la section 1 du présent chapitre. Il fait connaître sa décision d'exercer ce droit dans les deux mois suivant la transmission de l'offre préalable de cession ou de donation. En cas de refus de l'agrément, ce délai est prorogé d'un mois.</p>
<p>Le preneur est indemnisé de la valeur de ses droits réels immobiliers, dans le respect des modalités de calcul du prix de vente stipulées dans le bail et de la valeur maximale mentionnée à l'article L. 256-6, ainsi que, le cas échéant, du fonds existant. Cette indemnisation est accordée à hauteur du préjudice causé par le défaut d'agrément et dans les conditions prévues par le bail.</p>
<p>L'indemnisation du fonds comprend notamment sa valeur marchande, déterminée selon les usages de la profession.</p>
""",
    "Réécriture à droit constant : le titulaire du droit de préemption, les modalités de son exercice et les éléments de l'indemnisation sont énoncés plus directement. Aucun délai ni plafond n'est modifié ; aucune réforme de fond.",
    "Trois alinéas conservés. Maintien des deux mois à compter de la transmission de l'offre, de la prorogation d'un mois en cas de refus d'agrément et du renvoi à L. 256-6. La source rattache l'indemnisation au « préjudice causé par le défaut d'agrément » alors que la préemption est ouverte à toute cession ou donation : articulation préexistante à contrôler, sans créer une condition supplémentaire de préemption. Les limites d'indemnisation du deuxième alinéa conservent leur portée commune aux droits et, le cas échéant, au fonds.",
)

add(
    "L256-18",
    """
<p>À l'expiration du bail, l'organisme de foncier solidaire devient propriétaire des droits réels immobiliers du preneur après avoir indemnisé celui-ci de la valeur de ces droits. L'indemnisation est versée dans les conditions prévues par le bail et dans la limite de la valeur maximale mentionnée à l'article L. 256-6.</p>
""",
    "Réécriture à droit constant : le transfert à l'expiration du bail et l'indemnisation préalable sont exprimés avec des sujets explicites. Le plafond et les conditions contractuelles restent inchangés ; aucune réforme de fond.",
    "Un alinéa conservé. Le transfert demeure postérieur à l'indemnisation et la valeur maximale reste celle de L. 256-6. Aucun droit à indemnisation du fonds n'est ajouté à ce dispositif d'expiration.",
)

add(
    "L256-19",
    """
<p>Est nul tout bail réel solidaire d'activité conclu en violation de l'un des articles L. 256-1, L. 256-2, L. 256-3, L. 256-4, L. 256-6 et L. 256-7.</p>
""",
    "Réécriture à droit constant : la sanction est exprimée directement pour chaque bail qui méconnaît les dispositions énumérées. La liste des articles concernés n'est pas modifiée ; aucune réforme de fond.",
    "Les six références sont conservées expressément. L. 256-5 n'est pas ajouté à cette liste et les nullités particulières de L. 256-12 et L. 256-13 restent distinctes.",
)

add(
    "L256-20",
    """
<p>Le bail réel solidaire d'activité est soumis aux dispositions des articles L. 255-6, L. 255-7-1 et L. 255-9 du présent code.</p>
<p>Pour l'application de ces articles, l'expression « bail réel solidaire » désigne également, s'il y a lieu, le « bail réel solidaire d'activité », et l'expression « logement » désigne le « local à usage commercial ou professionnel ».</p>
""",
    "Réécriture à droit constant : l'applicabilité des trois articles est énoncée en prenant le bail pour sujet ; les adaptations de vocabulaire sont conservées dans le deuxième alinéa. Aucune réforme de fond.",
    "Deux alinéas et les trois renvois conservés, y compris la réserve « s'il y a lieu ». Renvois vérifiés dans le corpus : résiliation et reconduction à L. 255-6, copropriété à L. 255-7-1, saisie et sûretés à L. 255-9. Aucune assimilation générale entre logement et local professionnel n'est créée hors de ces dispositions.",
)

add(
    "L256-21",
    """
<p>Les modalités d'application du présent chapitre sont déterminées par décret en Conseil d'État.</p>
""",
    "Réécriture à droit constant de la disposition d'application : la compétence du décret en Conseil d'État est maintenue sans ajout de matière réglementaire ni de délai. Aucune réforme de fond.",
    "Un alinéa conservé. L'exigence d'un décret en Conseil d'État et le champ de l'ensemble du chapitre sont maintenus. La brièveté de la disposition limite la portée de la clarification rédactionnelle.",
)

add(
    "L261-1",
    """
<p>Conformément à l'article 1601-1 du code civil :</p>
<p>Dans une vente d'immeuble à construire, le vendeur s'engage à édifier un immeuble dans le délai fixé par le contrat.</p>
<p>Cette vente peut prendre la forme d'une vente à terme ou d'une vente en l'état futur d'achèvement.</p>
""",
    "Réécriture à droit constant : la définition met directement en relation le contrat, l'obligation de construire et le délai convenu, puis distingue les deux formes de vente. Le texte est reformulé sans le présenter comme une citation littérale du code civil ; aucune réforme de fond.",
    "Renvoi à l'article 1601-1 conservé, ainsi que les deux alinéas de fond après l'introduction. La coordination rédactionnelle avec le code civil, hors des cinq codes du corpus, doit porter précisément sur son article 1601-1 si une identité de rédaction entre les deux codes est recherchée. Le régime des ventes à construire n'est pas assimilé à celui des transformations de bureaux ou de la rénovation locative évoquées dans policy.json.",
)

add(
    "L261-2",
    """
<p>Conformément à l'article 1601-2 du code civil :</p>
<p>Dans une vente à terme, le vendeur s'engage à livrer l'immeuble à son achèvement. L'acheteur s'engage à en prendre livraison et à en payer le prix à la date de livraison. La constatation de l'achèvement par acte authentique entraîne de plein droit le transfert de propriété. Ce transfert produit ses effets rétroactivement au jour de la vente.</p>
""",
    "Réécriture à droit constant : les engagements respectifs du vendeur et de l'acheteur, le fait générateur du transfert de propriété et sa rétroactivité sont distingués dans des phrases autonomes, au sein du même alinéa. Aucune réforme de fond ; la reformulation ne se présente pas comme une citation du code civil.",
    "Renvoi à l'article 1601-2 conservé. Le prix reste payable à la livraison et le transfert exige toujours la constatation authentique de l'achèvement, avec effet rétroactif au jour de la vente. Une éventuelle harmonisation de la reproduction dans le CCH appelle une coordination rédactionnelle de l'article 1601-2 du code civil, hors corpus.",
)

add(
    "L261-3",
    """
<p>Conformément à l'article 1601-3 du code civil :</p>
<p>Dans une vente en l'état futur d'achèvement, le vendeur transfère immédiatement à l'acquéreur ses droits sur le sol et la propriété des constructions existantes. L'acquéreur devient propriétaire des ouvrages à venir au fur et à mesure de leur exécution et doit en payer le prix à mesure de l'avancement des travaux.</p>
<p>Jusqu'à la réception des travaux, le vendeur conserve les pouvoirs de maître de l'ouvrage.</p>
""",
    "Réécriture à droit constant : le transfert immédiat, l'acquisition progressive des ouvrages et l'échelonnement du prix sont explicités avec leurs sujets. Les pouvoirs du vendeur restent dans un alinéa distinct ; aucune réforme de fond ni citation présentée comme littérale.",
    "Deux alinéas de fond et l'introduction conservés. Le vendeur conserve les pouvoirs de maître de l'ouvrage jusqu'à la réception, et non seulement jusqu'à la livraison. Renvoi à l'article 1601-3 du code civil maintenu ; cet article, hors corpus, est le point précis d'une éventuelle coordination rédactionnelle de la reproduction. Aucun changement aux garanties de L. 261-10-1 et L. 261-11.",
)

add(
    "L261-4",
    """
<p>Conformément à l'article 1601-4 du code civil :</p>
<p>Lorsque l'acquéreur cède les droits qu'il tient d'une vente d'immeubles à construire, le cessionnaire est substitué de plein droit à l'acquéreur dans ses obligations envers le vendeur.</p>
<p>Si la vente comporte un mandat, ce mandat se poursuit entre le vendeur et le cessionnaire.</p>
<p>Ces règles s'appliquent à toute mutation entre vifs, qu'elle soit volontaire ou forcée, ainsi qu'à toute mutation à cause de mort.</p>
""",
    "Réécriture à droit constant : la substitution du cessionnaire est formulée en identifiant les parties, puis le maintien du mandat et le champ des mutations sont clarifiés sans changer les alinéas. Aucune réforme de fond ; la rédaction n'est pas présentée comme une citation littérale.",
    "Les trois alinéas de fond sont conservés après le renvoi introductif à l'article 1601-4 du code civil. Maintien de la substitution de plein droit et des mutations volontaires, forcées et à cause de mort. L'article 1601-4 du code civil, hors corpus, constitue la coordination rédactionnelle précise à examiner pour conserver une reproduction identique dans les deux codes.",
)

add(
    "L261-5",
    """
<p>Conformément à l'article 1642-1 du code civil :</p>
<p>Le vendeur d'un immeuble à construire ne peut être déchargé des vices de construction ou des défauts de conformité alors apparents que lorsque les travaux ont été reçus et que le délai d'un mois suivant la prise de possession par l'acquéreur a expiré.</p>
<p>Si le vendeur s'engage à réparer, le contrat ne peut être résolu ni le prix diminué à ce titre.</p>
""",
    "Réécriture à droit constant : les deux conditions cumulatives empêchant de décharger le vendeur sont rendues explicites, et la conséquence de son engagement de réparer est exprimée directement. Aucune réforme de fond ; les guillemets de citation sont supprimés pour ne pas attribuer cette reformulation au code civil.",
    "Maintien de la réception et du délai d'un mois après la prise de possession, ainsi que de la limitation aux vices ou défauts alors apparents. Les deux conditions de la décharge restent cumulatives. Renvoi à l'article 1642-1 conservé ; coordination rédactionnelle éventuelle à cet article du code civil, hors corpus. Le délai d'action distinct de L. 261-7 n'est pas modifié.",
)

add(
    "L261-6",
    """
<p>Conformément à l'article 1646-1 du code civil, applicable, en vertu de l'article 14 de la loi n° 78-12 du 4 janvier 1978, aux contrats relatifs aux chantiers dont la déclaration réglementaire d'ouverture a été établie après le 1er janvier 1979 :</p>
<p>À compter de la réception des travaux, le vendeur d'un immeuble à construire est tenu des mêmes obligations que les architectes, entrepreneurs et autres personnes liées au maître de l'ouvrage par un contrat de louage d'ouvrage en application des articles 1792, 1792-1, 1792-2 et 1792-3 du code civil.</p>
<p>Les propriétaires successifs de l'immeuble bénéficient de ces garanties.</p>
<p>La vente ne peut être résolue ni le prix diminué à ce titre si le vendeur s'engage à réparer les dommages définis aux articles 1792, 1792-1 et 1792-2 du code civil et à assumer la garantie prévue à l'article 1792-3 du même code.</p>
""",
    "Réécriture à droit constant : le débiteur des garanties et leurs bénéficiaires sont explicités, et les renvois anciennement formulés comme « du présent code » à l'intérieur de la citation sont rattachés expressément au code civil. La condition historique de la note source est intégrée à l'introduction sans déplacer les alinéas de fond. Aucune réforme de fond.",
    "Trois alinéas de fond conservés après l'introduction. La note de la loi n° 78-12 du 4 janvier 1978, article 14, est reprise avec sa date strictement postérieure au 1er janvier 1979 : ce n'est pas une date d'entrée en vigueur d'une réforme future. Maintien du point de départ à la réception, des quatre garanties et du cumul entre réparation des dommages et garantie de l'article 1792-3. L'article 1646-1 et les articles 1792 à 1792-3 du code civil sont hors corpus ; une harmonisation de la reproduction appelle une coordination rédactionnelle de l'article 1646-1, sans réécrire ici le droit des contrats antérieurs.",
)

add(
    "L261-7",
    """
<p>Conformément à l'article 1648 du code civil :</p>
<p>L'acquéreur doit intenter l'action résultant des vices rédhibitoires dans les deux ans suivant la découverte du vice.</p>
<p>Dans le cas prévu à l'article 1642-1 du code civil, l'action doit être introduite, à peine de forclusion, dans l'année suivant la date à laquelle le vendeur peut être déchargé des vices ou des défauts de conformité apparents.</p>
""",
    "Réécriture à droit constant : l'auteur de l'action et le point de départ de chaque délai sont exprimés directement, en conservant la distinction entre les deux actions. Les paragraphes vides de mise en page sont retirés ; aucune réforme de fond ni citation présentée comme littérale.",
    "Deux alinéas de fond conservés après l'introduction. Maintien des deux ans à compter de la découverte du vice et du délai d'un an, à peine de forclusion, à compter de la possibilité de décharger le vendeur dans le cas de l'article 1642-1. Ce dernier délai n'est pas calculé directement à partir de la réception ou de la prise de possession. Coordination rédactionnelle éventuelle à l'article 1648 du code civil, hors corpus, et articulation conservée avec L. 261-5.",
)

add(
    "L261-8",
    """
<p>Conformément à l'article 2380 du code civil :</p>
<p>Lorsqu'une vente d'immeuble à construire est conclue à terme conformément à l'article 1601-2 du code civil, le privilège du vendeur ou celui du prêteur de deniers prend rang à la date de l'acte de vente si l'inscription est prise avant l'expiration des deux mois suivant la constatation de l'achèvement de l'immeuble par acte authentique.</p>
""",
    "Réécriture à droit constant de la source fournie : la condition tenant à la vente à terme et le point de départ du délai d'inscription sont exprimés dans une phrase plus directe. Les références et la qualification de privilège sont conservées ; aucune réforme de fond.",
    "Maintien des références à 2380 et 1601-2 du code civil, du rang à la date de l'acte de vente et de l'inscription avant l'expiration du délai de deux mois suivant la constatation authentique de l'achèvement. La référence à l'article 2380 et la terminologie des privilèges immobiliers appellent un contrôle prioritaire de concordance et de droit transitoire dans le code civil, absent du corpus autorisé ; aucune référence de remplacement ni requalification en hypothèque n'est inventée. Toute correction éventuelle doit viser précisément L. 261-8 et les dispositions civiles de sûretés applicables à la date de l'acte.",
)

add(
    "L261-9",
    """
<p>Dès lors qu'un local d'un immeuble a été vendu à terme ou en l'état futur d'achèvement, la vente après achèvement de tout local compris dans cet immeuble est soumise à l'article 1646-1 du code civil, reproduit à l'article L. 261-6 du présent code.</p>
<p>Toutefois, les acquéreurs successifs ne peuvent exercer l'action éventuellement née de cet article que contre le vendeur originaire.</p>
""",
    "Réécriture à droit constant : la condition déclenchant l'application des garanties aux ventes après achèvement et la restriction de l'action au vendeur originaire sont exprimées directement. Aucune réforme de fond.",
    "Deux alinéas conservés. La vente antérieure d'un seul local suffit ; la règle continue de couvrir les ventes après achèvement d'un local du même immeuble. Les renvois à l'article 1646-1 du code civil et à L. 261-6 ainsi que la restriction au vendeur originaire sont maintenus. Tenir compte de la condition historique reprise à L. 261-6.",
)

add(
    "L261-10",
    """
<p>Tout contrat qui porte sur le transfert de propriété d'un immeuble ou d'une partie d'immeuble à usage d'habitation ou à usage professionnel et d'habitation et oblige l'acheteur à effectuer des versements ou des dépôts de fonds avant l'achèvement de la construction doit, à peine de nullité, prendre la forme d'une vente à terme ou d'une vente en l'état futur d'achèvement. Ces contrats sont prévus aux articles 1601-2 et 1601-3 du code civil, reproduits aux articles L. 261-2 et L. 261-3 du présent code. Le contrat doit également respecter les articles L. 261-11 à L. 261-14.</p>
<p>La personne qui s'engage à édifier ou à faire édifier un immeuble ou une partie d'immeuble à usage d'habitation ou à usage professionnel et d'habitation doit conclure un contrat conforme au premier alinéa lorsqu'elle procure, directement ou indirectement, le terrain ou le droit d'y construire à la personne tenue d'effectuer les versements ou les dépôts de fonds définis à cet alinéa. Cette obligation ne s'applique pas si le terrain ou le droit est procuré à une société régie par les chapitres Ier, II (sections I et II) et III du titre Ier du présent livre, ou si la personne qui le procure est un organisme d'habitations à loyer modéré agissant comme prestataire de service.</p>
""",
    "Réécriture à droit constant : les deux formes de contrat obligatoires sont nommées, puis les obligations liées à la fourniture du terrain et leurs deux exceptions sont rendues plus lisibles. La sanction de nullité et les champs d'usage sont conservés ; aucune réforme de fond.",
    "Deux alinéas conservés, avec les renvois aux articles 1601-2 et 1601-3, à L. 261-2, L. 261-3 et L. 261-11 à L. 261-14, ainsi qu'aux chapitres Ier, II (sections I et II) et III du titre Ier du livre II. Le régime vise l'habitation et l'usage mixte professionnel et d'habitation, sans extension aux seuls locaux professionnels. Les exceptions restent limitées à la société désignée et à l'organisme HLM agissant comme prestataire de service. Les réformes de transformation de bureaux ne suppriment pas ces garanties.",
)

add(
    "L261-10-1",
    """
<p>Avant de conclure un contrat prévu à l'article L. 261-10, le vendeur doit souscrire soit une garantie financière d'achèvement de l'immeuble, soit une garantie financière de remboursement des versements effectués si le contrat est résolu faute d'achèvement.</p>
<p>L'acquéreur peut mettre en œuvre la garantie financière d'achèvement lorsque le vendeur est financièrement défaillant. Cette défaillance se caractérise par le fait que le vendeur ne dispose pas des fonds nécessaires à l'achèvement de l'immeuble.</p>
<p>Le garant financier de l'achèvement de l'immeuble peut faire désigner un administrateur ad hoc par ordonnance sur requête. Cet administrateur dispose des pouvoirs du maître de l'ouvrage et a pour mission de faire réaliser les travaux nécessaires à l'achèvement de l'immeuble. Il peut effectuer toutes les opérations qui y concourent et réceptionner l'ouvrage au sens de l'article 1792-6 du code civil. Réputé constructeur au sens de l'article 1792-1 du même code, il dispose à ce titre d'une assurance de responsabilité en application de l'article L. 241-2 du code des assurances. Le garant prend en charge sa rémunération.</p>
<p>Lorsque la garantie financière d'achèvement est mise en œuvre, seul le garant peut exiger de l'acquéreur le paiement du solde du prix de vente. Cette règle s'applique même si le vendeur fait l'objet d'une procédure au titre du livre VI du code de commerce.</p>
<p>Un décret en Conseil d'État fixe les conditions d'application du présent article, notamment la nature de la garantie financière d'achèvement ou de remboursement.</p>
""",
    "Réécriture à droit constant : l'obligation préalable du vendeur, les conditions de mise en œuvre par l'acquéreur et les pouvoirs de l'administrateur sont explicités. L'exclusivité du garant pour réclamer le solde et le renvoi réglementaire sont maintenus ; aucune réforme de fond.",
    "Les cinq alinéas de fond, dont trois étaient séparés par des doubles sauts de ligne à l'intérieur d'un même élément p, sont conservés dans leur ordre. Maintien du choix entre les deux garanties avant le contrat, de la défaillance financière, de l'ordonnance sur requête, de l'assurance et de la rémunération à la charge du garant. Renvois à L. 261-10, aux articles 1792-6 et 1792-1 du code civil, à L. 241-2 du code des assurances et au livre VI du code de commerce conservés. Aucune dérogation liée aux solutions techniques équivalentes n'est introduite dans cette garantie financière.",
)

add(
    "L261-11",
    """
<p>Le contrat est conclu par acte authentique et doit préciser :</p>
<p>a) La description de l'immeuble ou de la partie d'immeuble vendu ;</p>
<p>b) Le prix et ses modalités de paiement ;</p>
<p>c) Le délai de livraison ;</p>
<p>d) Pour une vente en l'état futur d'achèvement, prévue à l'article 1601-3 du code civil et reproduite à l'article L. 261-3 du présent code, la justification de la garantie financière prescrite à l'article L. 261-10-1. Le garant établit l'attestation de garantie, qui est annexée au contrat ;</p>
<p>e) La description des travaux dont l'acquéreur se réserve l'exécution, lorsque la vente est précédée d'un contrat préliminaire comportant la clause prévue au II de l'article L. 261-15 et que l'acquéreur n'a pas demandé au vendeur d'exécuter ou de faire exécuter ces travaux.</p>
<p>Toutefois, si la vente porte sur une partie d'immeuble, le contrat peut se limiter, pour les indications prévues aux a à d du présent article, à celles qui sont propres à cette partie. Les précisions relatives aux parties d'immeuble non concernées par la vente doivent alors figurer soit dans un document annexé à l'acte, soit dans un document déposé au rang des minutes d'un notaire auquel l'acte fait référence.</p>
<p>Le contrat doit également indiquer si le prix est révisable et, s'il l'est, préciser les modalités de révision.</p>
<p>Il doit en outre comporter les indications utiles sur la consistance et les caractéristiques techniques de l'immeuble, soit en annexe, soit par référence à des documents déposés chez un notaire.</p>
<p>Le règlement de copropriété est remis à chaque acquéreur lors de la signature du contrat et doit lui être communiqué avant cette signature.</p>
<p>Si le vendeur a obtenu, avant la conclusion de la vente, le bénéfice d'un prêt spécial du Crédit foncier de France ou du Comptoir des entrepreneurs, le contrat doit indiquer que l'acheteur a été mis en mesure de prendre connaissance, dans les conditions fixées par décret, des documents relatifs à l'équilibre financier de l'opération sur lesquels s'est fondée la décision de prêt. Le non-respect des dispositions du présent article entraîne la nullité du contrat. Seul l'acquéreur peut invoquer cette nullité, et uniquement avant l'achèvement des travaux.</p>
""",
    "Réécriture à droit constant : les pièces et mentions exigées sont exprimées plus directement, avec un sujet explicite pour l'attestation et une distinction claire entre communication préalable et remise du règlement de copropriété. La liste a à e, les exceptions et les garanties historiques sont conservées ; aucune réforme de fond.",
    "Onze alinéas et les lettres a à e conservés, notamment la limitation de l'exception aux seuls a à d. Maintien des renvois à l'article 1601-3, à L. 261-3, L. 261-10-1 et au II de L. 261-15, vérifié dans le corpus. La nullité reste réservée à l'acquéreur avant l'achèvement ; elle n'est pas limitée au seul prêt spécial. La note source de l'article 3 de l'ordonnance n° 2013-890 du 3 octobre 2013 fixe l'application de cette ordonnance aux opérations dont la demande de permis de construire est déposée à compter du 1er janvier 2015 : cette condition historique reste à appliquer aux dispositions issues de cette ordonnance, sans l'étendre indistinctement au e ou à tout l'article dans sa version de 2018. Elle est consignée ici sans ajout d'alinéa normatif ni invention de transition future. Les références au Crédit foncier de France et au Comptoir des entrepreneurs sont conservées pour les opérations susceptibles d'en relever.",
)


def main():
    sources = json.loads(Path("source.json").read_text())
    assert len(sources) == len(drafts) == 24
    assert set(drafts) == {source["number"] for source in sources}
    answer = []
    for source in sources:
        item = {key: source[key] for key in ("code_id", "source_id", "source_sha256", "number")}
        item.update(drafts[source["number"]])
        item["status"] = "rewrite_draft"
        answer.append(item)
    Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
