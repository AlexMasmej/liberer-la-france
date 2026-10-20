import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())


def base(index):
    source = sources[index]
    return {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}


def paragraphs(*texts):
    return '\n'.join('<p>' + text + '</p>' for text in texts)


def impact(classification, assessment, scope_limitations, new_burdens_review, effects):
    return dict(version=1, classification=classification, assessment=assessment,
                scope_limitations=scope_limitations, new_burdens_review=new_burdens_review,
                effects=effects)


division_measure = 'urbanisme-divisions-declaration-speciale-suppression'
bornage_measure = 'urbanisme-bornage-mentions-speciales-suppression'
answer = []

a = base(0)
# Conservation du corps antérieur, avec restitution explicite du lien entre
# l'exception rurale, l'opération dont elle relève et la clôture de celle-ci.
a['proposed_xml'] = sources[0]['previous_draft']['proposed_xml'].replace(
    "aux divisions effectuées avant la clôture d'une opération d'aménagement foncier rural relevant du titre II du livre Ier du code rural et de la pêche maritime",
    "aux divisions effectuées dans le cadre d'une opération d'aménagement foncier rural relevant du titre II du livre Ier du code rural et de la pêche maritime et avant la clôture de cette opération"
)
a['reason'] = (
    "Réforme de fond par rapport à la source officielle entière : suppression du dossier de déclaration préalable spécialement institué pour les divisions foncières dans les zones de protection, de son instruction préalable systématique et de la nullité fondée sur le seul défaut de ce dossier. Aucune déclaration, information, autorisation, attestation ou attente équivalente ne le remplace. La réduction déjà contenue dans previous_draft est conservée ; elle n'est pas une nouvelle coupe additionnelle. Après réexamen, une abrogation du pouvoir d'opposition restant n'est pas retenue : il ne vise que les divisions menaçant gravement les espaces naturels, les paysages ou les équilibres biologiques, y compris des divisions sans travaux que les seuls permis de travaux ne contrôlent pas. La nullité judiciaire limitée à la violation d'une opposition régulièrement notifiée assure l'effectivité de cette protection, sous prescription de cinq ans. Le zonage motivé et public en borne le champ. Le nouveau corps conserve les trois dispenses réglementaires pour les opérations futures ; le rattachement de la dispense rurale à l'opération d'aménagement foncier et à sa clôture est explicité. Les procédures autonomes des véritables lotissements, des travaux et de protection de l'environnement restent distinctes. Il n'est procédé à aucune nouvelle réécriture stylistique des parties déjà rédigées."
)
a['review_notes'] = (
    "Source de 1 385 caractères, notes sources vides et previous_draft lus intégralement ; aucun tableau ni compagnon documentaire assigné. Les quatre premiers alinéas conservent leurs objets respectifs : champ et zonage, opposition, nullité et prescription, habilitation réglementaire. Les trois motifs alternatifs de menace grave, la propriété et la jouissance, les ventes et locations simultanées ou successives, ainsi que l'exclusion des divisions soumises à permis d'aménager sont conservés. Les cinq ans courent toujours de la publication de l'acte, non de la découverte du défaut. Les actes antérieurs conservent leur régime civil, même en cas d'action ultérieure ; les décisions favorables acquises et les oppositions antérieures fondées sur les motifs de protection sont préservées. Les déclarations pendantes sur ce seul fondement prennent fin pour les actes nouveaux, sans nouveau dépôt ; aucune règle pénale temporelle plus favorable n'est écartée. Lecture intégrale des sources et notes de R115-1, R*421-23, R151-52, L421-4, L442-1, R*421-19, L610-1 et L480-4 dans urbanisme.json : retirer le seul b déclaratif de R*421-23 en préservant ses autres lettres, adapter R115-1 au zonage sans dépôt préalable et le seul 4° de R151-52, et restreindre le renvoi de L610-1 aux obligations subsistantes. Ces articles hors lot ne sont pas modifiés ici ; la dispense législative expresse interdit de rétablir le dépôt supprimé par leur intermédiaire. La publicité du zonage reste nécessaire à son opposabilité, sans nouvelle délibération pour les zones déjà régulièrement instituées ; le réexamen des circuits de publicité de R115-1 reste distinct. Les autres permis, déclarations et sanctions ne sont pas abolis. L'efficacité préventive du contrôle ciblé sans dossier systématique reste à apprécier, sans créer de collecte compensatoire ni supposer que tous les découpages sont des lotissements. SRU202 initial a été lu en entier : ses IV et V modifiaient les autorités de l'ancien L111-5-2, et non tout son régime. La piste historique LEGIARTI000006814684 est fournie comme concordance mais son texte historique intégral n'a pas été trouvé parmi les articles du corpus accessible : filiation complète non établie, volet SRU202 non déclaré achevé. La suppression est fondée sur la charge actuelle, pas sur une attribution globale à SRU. Aucun délai chiffré de déclaration ni gain financier n'est déduit de cette seule source."
)
a['status'] = 'rewrite_draft'
a['change_type'] = 'normative_reduction'
a['reform_policy_id'] = 'editorial_direction_2026_10_19'
a['removed_provisions'] = [
    "Déclaration préalable spéciale des divisions volontaires dans les zones de protection de L115-3 et instruction préalable systématique attachée à ce seul dépôt, sans demande ou information de remplacement.",
    "Possibilité de demander la nullité d'une vente ou location nouvelle pour le seul défaut de la déclaration spéciale supprimée, sans opposition régulièrement notifiée avant sa conclusion."
]
a['benefit_review'] = (
    "L'article ne prévoit ni taxe ni exonération fiscale. Les trois dispenses du b de R*421-23 restent ouvertes pour les opérations d'aménagement autorisées, les divisions réalisées dans le cadre d'un aménagement foncier rural avant sa clôture et les baux ruraux consentis à des preneurs agricoles. Elles deviennent des exclusions expresses de l'opposition spéciale et ne sont pas limitées aux opérations anciennes. Les non-oppositions et autres droits acquis demeurent protégés ; les dispenses autonomes des autres régimes ne sont pas supprimées."
)
a['substantive_impact'] = impact(
    'material_reduction',
    "La source entière permet d'imposer un dépôt préalable à une division foncière et d'en sanctionner l'absence par la nullité. La proposition retire effectivement ce dépôt dans son champ et limite la nullité au non-respect d'une opposition antérieure à l'acte. C'est une réduction matérielle déjà acquise dans le brouillon, conservée après seconde passe ; la précision de l'exception rurale n'est pas une seconde suppression. Aucun impôt n'est réduit et aucun coût national n'est chiffré.",
    "Le gain concerne les divisions relevant du seul contrôle spécial de L115-3 et les actes conclus à compter de l'entrée en vigueur, y compris les dossiers pendants. Les déclarations de lotissement et permis exigibles à un autre titre, le zonage, l'opposition pour menace grave, les recours et le régime civil des actes antérieurs subsistent. R115-1, R*421-23 b, R151-52 4° et L610-1 restent à coordonner hors de ce lot. La filiation complète à SRU202 et le solde global des coûts ne sont pas démontrés.",
    "Aucun dossier, registre, donnée, attestation ou délai nouveau n'est imposé aux parties : elles ne doivent ni solliciter ni attendre l'opposition. La motivation et la notification préalable encadrent l'exercice du pouvoir de police existant, sans le transformer en autorisation à obtenir ni créer de collecte compensatoire. Les zones déjà valablement publiées sont utilisables sans réitération. Le coût administratif du contrôle restant et le solde de l'ensemble des codes ne sont pas chiffrés.",
    [dict(
        kind='obligation_removed', measure_id=division_measure,
        description="Suppression du dépôt spécial préalable des divisions foncières et de la nullité pour son seul défaut ; maintien d'une opposition ciblée sans saisine obligatoire.",
        before="Dans les zones instituées par le conseil municipal, divisions volontaires en propriété ou jouissance par ventes ou locations, hors permis d'aménager : déclaration préalable spéciale et nullité possible en cas de violation. Aucun délai d'instruction chiffré n'est fixé par l'article source.",
        after="Pour les ventes et locations nouvelles, aucun dépôt, information, autorisation ou certificat au seul titre de L115-3. L'opposition pour menace grave doit être notifiée avant l'acte sans que les parties aient à l'attendre ; la nullité spéciale ne sanctionne que sa méconnaissance. Les contrôles autonomes demeurent.",
        unit='legal_duty',
        affected_population="Auteurs de divisions volontaires et parties aux ventes ou locations foncières dans les zones de protection délimitées par les communes.",
        conditions_and_transition="Actes conclus dès l'entrée en vigueur de la loi ; procédures déclaratives pendantes sur ce seul fondement terminées pour ces actes. Dispenses d'aménagement autorisé, d'aménagement foncier rural avant clôture et de bail rural professionnel conservées pour l'avenir. Actes antérieurs, droits favorables acquis et oppositions régulièrement notifiées préservés ; prescription de cinq ans inchangée.",
        replacement_or_new_burdens="Aucune formalité privée de remplacement. Maintien d'un pouvoir d'opposition déjà existant, désormais sans dépôt obligatoire ; pas de nouvelle taxe, ni délai de réponse imposé aux parties. Coût public net non évalué.",
        source_quote="Dans les parties de commune nécessitant une protection particulière en raison de la qualité des sites, des milieux naturels et des paysages, le conseil municipal peut décider, par délibération motivée, de soumettre, à l'intérieur de zones qu'il délimite, à la déclaration préalable prévue par l'article L. 421-4, les divisions volontaires, en propriété ou en jouissance, d'une propriété foncière, par ventes ou locations simultanées ou successives qui ne sont pas soumises à un permis d'aménager.",
        proposed_quote="Aucune déclaration, demande d'autorisation, information préalable ou attestation de non-opposition n'est exigée au seul titre du présent article."
    )]
)
answer.append(a)

a = base(1)
a['proposed_xml'] = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui l'abroge.",
    "Les promesses unilatérales de vente ou d'achat et les contrats réalisant ou constatant la vente conclus à compter de cette date ne sont plus soumis, sur le seul fondement du présent article, à l'obligation de mentionner si le descriptif d'un terrain destiné à la construction d'un immeuble à usage d'habitation ou à usage mixte d'habitation et professionnel résulte d'un bornage. Dans les mêmes conditions, aucune mention du descriptif résultant d'un bornage n'est exigée pour un lot de lotissement, un terrain issu d'une division effectuée à l'intérieur d'une zone d'aménagement concerté par la personne publique ou privée chargée de l'aménagement ou un terrain issu d'un remembrement réalisé par une association foncière urbaine. Aucun bornage préalable n'est exigé sur le seul fondement du présent article pour ces actes nouveaux.",
    "La validité et les effets des promesses et contrats conclus avant cette date, ainsi que les droits et recours qui en sont nés, restent régis par les dispositions antérieurement applicables, y compris dans les conditions transitoires prévues à l'article L. 115-5. Ce régime demeure applicable à une promesse antérieure même si l'acte authentique constatant la réalisation de la vente est signé après cette date. Les accords valablement conclus et les droits des parties et des tiers ne sont pas remis en cause.",
    "Le droit au bornage, les règles de délimitation de la propriété et les obligations de bornage ayant un fondement distinct demeurent applicables. Les obligations d'information, de conseil, de consentement et de responsabilité résultant d'autres dispositions ou des engagements valables des parties conservent leur régime propre. Aucune déclaration, attestation ou formalité de remplacement n'est exigée au titre de la présente abrogation."
)
a['reason'] = (
    "Réforme de fond : abrogation prospective des deux obligations spéciales de mention de bornage, y compris le descriptif nécessairement issu d'un bornage dans les trois catégories aménagées. L'abrogation déjà retenue dans previous_draft est conservée et son champ est explicité : elle ne laisse subsister aucune exigence de bornage préalable sur le seul fondement de cet article. La source officielle entière est donc supprimée pour les actes nouveaux ; aucune coupe supplémentaire de son dispositif ne reste possible. La précision de l'entrée en vigueur ne vise plus une loi indéterminée supprimant globalement les dispositions SRU. Les recours nés des anciennes promesses, le droit civil de faire borner sa propriété, les informations nécessaires au consentement et les responsabilités autonomes restent nécessaires et ne sont pas supprimés. Il ne s'agit ni d'un allègement fiscal ni d'une simple reformulation à droit constant."
)
a['review_notes'] = (
    "Lecture entière de la source, de previous_draft et de l'article 14 SRU initial ; notes sources vides, aucun tableau. L'article initial comporte déjà les deux obligations actuelles, générales puis propres aux lots de lotissement, divisions ZAC par aménageur et remembrements AFU, ainsi que le recours repris à L115-5. Le rapprochement des contenus est concordant avec la piste documentaire L111-5-3, LEGIARTI000006814687. Cette version historique n'est toutefois pas présente comme article source dans le corpus accessible : la piste seule ne prouve pas toutes les étapes historiques ni l'absence de tout ajout intermédiaire. La décision est justifiée par le contenu actuel intégral et par la coordination expresse SRU14 retenue dans coordination.json. L115-5 est abrogé et doté de sa transition dans ce même lot : le délai d'un mois après l'acte authentique et la régularisation restent disponibles pour les anciennes promesses, y compris si la vente est réalisée après la réforme. La disparition de la mention dans un acte nouveau n'efface donc pas le droit né d'une promesse antérieure. Recherche dans les sources des cinq codes et quatre annexes fournies : le renvoi actuel à L115-4 urbanisme est celui de L115-5 ; les références homonymes du CGI, du CSS et du travail concernent d'autres codes et ne sont pas modifiées. Les exigences notariales, civiles et techniques reposant sur des fondements distincts ne sont pas présentées comme abolies ; leur inventaire extérieur au corpus reste à vérifier. Pas de suppression d'exonération, d'aide ou de dérogation de construction, ni de date de promulgation inventée. L'examen de SRU14 ne vaut pas examen achevé des 209 articles."
)
a['status'] = 'rewrite_draft'
a['change_type'] = 'full_repeal'
a['repeal_policy_id'] = 'editorial_direction_2026_10_19'
a['repeal_scope'] = (
    "Pour les promesses et contrats nouveaux, suppression des mentions spéciales de bornage et de l'exigence de descriptif borné fondées exclusivement sur L115-4, dans le cas général et les trois catégories aménagées ; droits nés des actes antérieurs et bornage de fondement autonome préservés."
)
a['benefit_review'] = (
    "Aucun avantage fiscal, franchise, aide ou dérogation favorable n'est institué par cet article. Il impose des mentions protectrices de l'acquéreur, dont la suppression est expressément coordonnée avec L115-5 ; les droits nés des promesses antérieures restent ouverts après la réforme. Pour les actes futurs, le consentement éclairé, le conseil, la responsabilité et les droits de délimitation de la propriété restent protégés par leurs fondements autonomes. Aucune formalité de remplacement ne conditionne un avantage futur."
)
a['substantive_impact'] = impact(
    'material_reduction',
    "Par rapport aux deux alinéas officiels, suppression effective des mentions spéciales de bornage, dont le descriptif borné imposé dans les trois catégories aménagées. Le dispositif était déjà intégralement abrogé dans le brouillon ; le texte final précise son champ et sa transition sans compter une seconde réduction. Les obligations d'autres fondements ne sont pas prétendues supprimées et aucune économie nationale n'est chiffrée.",
    "Seuls les actes conclus à compter de l'entrée en vigueur sont dispensés au titre de L115-4. Une promesse antérieure conserve ses droits et recours, même si la vente est constatée ultérieurement. Les obligations autonomes de bornage, d'information, de délimitation et de responsabilité demeurent ; les textes extérieurs au corpus ne sont pas intégralement inventoriés. La nullité spéciale est coordonnée par L115-5 sans seconde mesure comptée.",
    "Aucune charge nouvelle n'est identifiée : aucun certificat, registre, dépôt, délai, justificatif ou déclaration ne remplace les mentions supprimées. Les règles civiles et engagements valables conservés existaient sur des fondements distincts ; leur maintien n'impose pas de nouvelle condition. Le coût net global des actes immobiliers et de l'ensemble des codes n'est pas évalué.",
    [dict(
        kind='obligation_removed', measure_id=bornage_measure,
        description="Suppression des mentions spéciales de bornage et du descriptif obligatoirement borné au seul titre de L115-4 pour les nouveaux actes concernés.",
        before="Toute promesse unilatérale de vente ou d'achat et tout acte de vente d'un terrain destiné à l'habitation ou à un usage mixte doivent indiquer si le descriptif résulte d'un bornage. Pour les lots de lotissement, divisions ZAC par aménageur et remembrements AFU, mention obligatoire du descriptif résultant du bornage, avec nullité spéciale de L115-5 en cas de défaut.",
        after="Aucune de ces mentions ni aucun bornage préalable ne sont exigés au seul titre de L115-4 pour les actes nouveaux ; aucune formalité équivalente de remplacement. Les obligations civiles ou techniques autonomes restent dans leur champ propre.",
        unit='legal_duty',
        affected_population="Parties aux promesses unilatérales et ventes de terrains destinés à l'habitation ou à un usage mixte, y compris lots de lotissement, divisions ZAC réalisées par l'aménageur et remembrements AFU.",
        conditions_and_transition="Actes conclus dès l'entrée en vigueur de la loi d'abrogation. Promesses et contrats antérieurs, droits des parties et tiers et recours historiques maintenus ; une réitération authentique ultérieure ne ferme pas le recours né de l'ancienne promesse, sous le délai et la régularisation de L115-5.",
        replacement_or_new_burdens="Aucune déclaration, attestation, formalité, taxe ou délai de remplacement. Droit au bornage, obligations autonomes et responsabilités conservés sans extension de leur champ.",
        source_quote="Toute promesse unilatérale de vente ou d'achat, tout contrat réalisant ou constatant la vente d'un terrain indiquant l'intention de l'acquéreur de construire un immeuble à usage d'habitation ou à usage mixte d'habitation et professionnel sur ce terrain mentionne si le descriptif de ce terrain résulte d'un bornage.",
        proposed_quote="Aucun bornage préalable n'est exigé sur le seul fondement du présent article pour ces actes nouveaux."
    )]
)
answer.append(a)

a = base(2)
a['proposed_xml'] = paragraphs(
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi qui l'abroge.",
    "L'absence, dans une promesse ou un contrat conclu à compter de cette date, d'une mention dont l'obligation a été supprimée par l'abrogation de l'article L. 115-4 ne permet plus d'exercer l'action spéciale en nullité prévue par le présent article.",
    "Pour une promesse ou un contrat conclu avant cette date, le bénéficiaire de la promesse de vente, le promettant de la promesse d'achat ou l'acquéreur du terrain conserve le droit d'agir en nullité pour l'absence de l'une ou l'autre mention alors exigée selon le cas, même si l'action est introduite ou si l'acte authentique constatant la réalisation de la vente est signé après cette date. L'action peut être intentée avant l'expiration du délai d'un mois à compter de cet acte authentique. La signature de cet acte authentique comportant la mention requise entraîne la déchéance du droit d'engager ou de poursuivre l'action en nullité de la promesse ou du contrat qui l'a précédé, fondée sur l'absence de cette mention.",
    "L'abrogation ne rouvre aucun délai expiré et ne remet pas en cause les décisions définitives, les accords valablement conclus ni les droits des tiers. Les autres actions qui disposent d'un fondement distinct demeurent régies par leurs conditions propres."
)
a['reason'] = (
    "Coordination de fond indispensable de l'abrogation de L115-4 : supprimer, pour les actes nouveaux, la nullité spéciale qui sanctionnait exclusivement l'absence des mentions retirées, sans recréer ces mentions par le recours. Cette abrogation était déjà retenue dans previous_draft ; aucune coupe supplémentaire ne peut viser le régime nouveau désormais entièrement supprimé. La transition maintient les trois titulaires de l'action, l'une ou l'autre mention selon le cas, le délai d'un mois après l'acte authentique et la déchéance par sa régularisation pour les promesses et contrats antérieurs, même lorsque l'acte ou l'action intervient ensuite. Supprimer aussi ces droits anciens ou les recours civils autonomes ne serait pas l'allègement de la formalité future décidé par l'auteur. La mesure est dédupliquée avec L115-4 et n'est pas comptée comme une seconde obligation supprimée."
)
a['review_notes'] = (
    "Source entière de 604 caractères, notes sources vides, previous_draft et article 14 SRU initial lus en entier ; aucun tableau. Le contenu du recours actuel correspond au dernier ensemble de dispositions de l'ancien L111-5-3 reproduit dans SRU14 ; la piste LEGIARTI000006814687 n'est pas disponible comme source historique autonome dans le corpus, ce qui interdit de présenter la chaîne historique entière comme vérifiée. L115-4 est abrogé dans ce même answer.json ; son renvoi est maintenu ici uniquement pour identifier la mention anciennement due, non pour créer une obligation future. Les trois titulaires sont conservés sans les fusionner : bénéficiaire d'une promesse de vente, promettant d'une promesse d'achat et acquéreur. Le délai est d'un mois, sans conversion en trente jours, et part de l'acte authentique constatant la réalisation de la vente. La signature d'un acte régularisé entraîne encore la déchéance de l'action fondée sur la seule mention manquante ; l'abrogation ne remplace pas cette déchéance par un droit irrévocable. Ancienne promesse et acte authentique postérieur : l'ancien droit reste ouvert jusqu'à son extinction selon ces règles ; les délais prescrits ne sont pas rouverts. Les actions pour vice du consentement, défaut d'information ou responsabilité ayant un fondement autonome ne sont pas supprimées. Ni cet article ni la suppression de la formalité ne valident automatiquement une vente irrégulière à un autre titre. Les renvois homonymes dans les autres codes ne concernent pas cet article d'urbanisme. Aucune relecture par un juriste ni aucun achèvement général du chantier SRU n'est déclaré."
)
a['status'] = 'rewrite_draft'
a['change_type'] = 'full_repeal'
a['repeal_policy_id'] = 'editorial_direction_2026_10_19'
a['repeal_scope'] = (
    "Suppression pour les promesses et contrats nouveaux de l'action spéciale en nullité attachée aux mentions de bornage abrogées de L115-4 ; maintien du recours, de son délai et de sa régularisation pour les actes antérieurs, sans extinction des autres fondements civils."
)
a['benefit_review'] = (
    "Le texte ne contient pas d'exonération fiscale mais un recours protecteur des parties. Pour les anciennes promesses et les anciens contrats, ce recours reste intégralement disponible avec ses trois titulaires, son délai d'un mois et sa régularisation, même lorsque l'acte authentique ou l'action est ultérieur. Pour les actes nouveaux, la seule action liée aux mentions expressément supprimées disparaît conformément à la décision SRU14 ; les actions civiles de fondement distinct restent ouvertes aux situations futures éligibles."
)
a['substantive_impact'] = impact(
    'coordination_only',
    "La source officielle institue le recours spécifique sanctionnant les mentions de L115-4. La proposition en retire l'application aux nouveaux actes parce que ces mentions sont supprimées, tout en conservant le régime exact des actes antérieurs. C'est la coordination de la même mesure de bornage, déjà acquise dans le brouillon, et non une deuxième formalité ou une deuxième taxe supprimée.",
    "La suppression du seul recours spécial porte sur les promesses et contrats nouveaux. Les droits nés des anciennes promesses ou contrats, y compris leur exercice après l'entrée en vigueur, le délai d'un mois, la régularisation par l'acte authentique et les actions civiles autonomes restent applicables. Le volume de contentieux et le solde net de complexité ne sont pas établis.",
    "Aucune charge nouvelle n'est identifiée : la transition ne crée aucun nouveau dépôt, délai ou justificatif, et reproduit les seules conditions du recours antérieur. Les parties à un acte nouveau n'ont pas à obtenir une attestation d'absence de recours. Aucun nouveau mécanisme de contrôle ni aucune obligation de remplacement n'est institué ; le solde global n'est pas chiffré.",
    [dict(
        kind='coordination', measure_id=bornage_measure,
        description="Extinction prospective de la nullité spéciale accessoire aux mentions abrogées de L115-4, avec maintien intégral du recours des actes antérieurs.",
        before="Bénéficiaire de promesse de vente, promettant de promesse d'achat ou acquéreur peuvent agir pour défaut d'une mention de L115-4 avant l'expiration d'un mois après l'acte authentique ; sa signature avec la mention requise entraîne la déchéance.",
        after="Aucune action spéciale pour défaut de la mention supprimée dans un acte nouveau. Les mêmes titulaires conservent le recours né des actes antérieurs, son délai d'un mois et sa déchéance en cas de régularisation, même après l'entrée en vigueur.",
        unit='legal_duty',
        affected_population="Bénéficiaires de promesses de vente, promettants de promesses d'achat et acquéreurs des terrains relevant antérieurement de L115-4.",
        conditions_and_transition="Abrogation dès l'entrée en vigueur pour les actes nouveaux ; régime antérieur maintenu pour les anciennes promesses et contrats, même si la réitération authentique ou l'action est ultérieure. Aucun délai expiré rouvert ; droits des tiers, décisions définitives et autres actions préservés.",
        replacement_or_new_burdens="Aucune formalité ou action spéciale de remplacement. La régularisation des actes anciens reste possible dans ses conditions historiques, sans mention obligatoire nouvelle créée pour les actes autonomes postérieurs.",
        source_quote="Le bénéficiaire en cas de promesse de vente, le promettant en cas de promesse d'achat ou l'acquéreur du terrain peut intenter l'action en nullité sur le fondement de l'absence de l'une ou l'autre mention mentionnée à l'article L. 115-4 selon le cas, avant l'expiration du délai d'un mois à compter de l'acte authentique constatant la réalisation de la vente.",
        proposed_quote="L'absence, dans une promesse ou un contrat conclu à compter de cette date, d'une mention dont l'obligation a été supprimée par l'abrogation de l'article L. 115-4 ne permet plus d'exercer l'action spéciale en nullité prévue par le présent article."
    )]
)
answer.append(a)

a = base(3)
a['proposed_xml'] = None
a['status'] = 'retained_unchanged'
a['classification'] = 'retained_necessary'
a['reason'] = (
    "Maintien intégral de la source officielle après examen de ses deux branches territoriales et du brouillon antérieur. L'article définit le champ commun des protections et des dérogations littorales ; aucune taxe, déclaration de propriétaire, agrément de travaux ou pièce répétée n'y est imposé. La demande du 2° est une faculté communale d'adhésion, non une obligation individuelle ; la supprimer modifierait le consentement territorial à un régime de protections et d'avantages. Le décret en Conseil d'État rend la liste juridiquement identifiable et l'avis du conservatoire apporte l'examen spécialisé des équilibres économiques et écologiques : aucun doublon établi ne justifie de supprimer ces garanties de délimitation. La conservation intégrale garde aussi le champ nécessaire aux dérogations favorables, pour les opérations futures comme antérieures. Le changement de mots du previous_draft n'apportait aucune réduction : il n'est pas reconduit comme une réécriture. Aucune simplification matérielle n'est revendiquée pour cet article."
)
a['review_notes'] = (
    "Source entière de 563 caractères et previous_draft lus ; notes sources vides, aucun tableau ni compagnon. Maintien sans modification des espaces terrestres, maritimes et lacustres, du renvoi à L321-2 environnement au 1°, et de toutes les conditions du 2° : communes participant aux équilibres économiques et écologiques littoraux, demande auprès de l'autorité administrative compétente de l'État, liste fixée par décret en Conseil d'État après avis du conservatoire de l'espace littoral et des rivages lacustres. Les deux branches ne sont pas réduites aux seules communes riveraines de la mer. Lecture entière des sources et notes de L121-2, L121-3, L122-1-1, L121-28 à L121-30, R121-7, R121-8, R121-36, L104-2, R151-52 et R141-6-1 : aucune fermeture du schéma de plage, de son approbation ou de ses dérogations pour les nouvelles opérations recevables. Restent notamment le champ des équipements antérieurs au 5 janvier 1986, l'enquête et l'avis nécessaires, l'évaluation environnementale, l'annexion au PLU et les adaptations ultramarines. Le renvoi général de R141-6-1 n'est pas rétréci au seul 1°. La dérogation autonome de L122-1-1, pour certains secteurs des communes riveraines d'un plan d'eau intérieur de plus de 1 000 hectares hors bande des cent mètres, n'est pas neutralisée. L321-2 environnement n'est pas fourni comme article source dans le corpus des cinq codes ; sa teneur intégrale et la liste réglementaire extérieure des communes restent à vérifier, sans correction de champ inventée. Les renvois L341-16 et R122-17 I 50° environnement restent expressément hors suppression ; ils ne sont pas présentés comme réécrits ou vérifiés intégralement ici. SRU202 initial a été lu en entier : son XXII supprimait une ancienne qualification de l'ancien L146-1, il ne crée pas à lui seul tout le dispositif actuel. Le texte historique LEGIARTI000006814910 manque parmi les sources du corpus ; sa simple concordance ne clôt pas la filiation, et ce volet historique comme l'examen des 209 articles ne sont pas déclarés achevés. Aucun renvoi incohérent du présent article n'a été identifié dans le contexte local ; les lacunes documentaires demeurent signalées."
)
a['benefit_review'] = (
    "L'article ne crée pas d'avantage fiscal ; il délimite le champ d'un chapitre comportant des protections mais aussi des dispenses et dérogations favorables. Le maintien intégral des 1° et 2° conserve le fondement territorial des régimes de L121-2, du schéma de plage et de ses possibilités de maintien ou reconstruction sous leurs conditions propres, y compris pour les opérations futures. La dérogation autonome de L122-1-1 n'est ni restreinte ni écartée. Aucune clôture de procédure, attestation ou restriction d'accès nouvelle n'est ajoutée."
)
a['substantive_impact'] = impact(
    'retained_necessary',
    "La source officielle entière est maintenue : aucun prélèvement, dossier privé ou délai minimal n'est retiré. La définition territoriale, l'adhésion communale facultative, le décret de liste et l'avis spécialisé constituent le fondement commun des protections et dérogations littorales, sans doublon démontré. Le brouillon antérieur était une reformulation à droit constant ; aucun gain ni nouvelle réécriture n'est compté.",
    "Le maintien porte seulement sur L121-1 et ne valide pas l'ensemble des contraintes littorales ni les autres textes SRU. La teneur intégrale de L321-2 environnement, les textes de liste extérieurs et la chaîne historique complète de L146-1 restent à vérifier. Les dérogations et procédures de plage ainsi que L122-1-1 gardent leur régime propre ; aucun bilan national de coût ou de complexité n'est établi.",
    "Aucune charge nouvelle n'est identifiée puisque aucun nouveau corps normatif n'est produit : la source reste intégralement applicable, sans nouvelle donnée, formalité, condition, autorisation ni délai. La demande communale facultative et l'avis existants sont maintenus dans leur champ, sans être étendus aux propriétaires ou aux dossiers individuels.",
    []
)
answer.append(a)

# La motivation et la notification étaient déjà exigées dans le circuit
# déclaratif supprimé ; leur maintien ne constitue pas une obligation nouvelle.
answer[0]['review_notes'] += (
    " Lecture intégrale supplémentaire de L424-3, R*424-5 et R*424-10 avec leurs notes : l'opposition à la déclaration était déjà motivée et notifiée. La motivation et la notification reprises dans le nouveau contrôle ne créent donc pas un second acte ou un nouveau dossier ; leur intervention avant la vente limite le pouvoir d'opposition. Les règles de notification déjà allégées dans les coordinations générales ne sont pas rétablies à leur ancienne forme postale exclusive."
)
answer[0]['substantive_impact']['new_burdens_review'] = (
    "Aucune charge nouvelle n'est identifiée : aucun dossier, registre, donnée, attestation ou délai nouveau n'est imposé aux parties, qui ne doivent ni solliciter ni attendre l'opposition. La motivation et la notification existaient déjà pour l'opposition à déclaration selon L424-3 et R*424-10 ; leur conservation encadre le même pouvoir sans ajouter d'acte, de collecte compensatoire ou d'autorisation à obtenir. Les zones déjà valablement publiées restent utilisables sans réitération. Le coût administratif du contrôle restant et le solde de l'ensemble des codes ne sont pas chiffrés."
)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
