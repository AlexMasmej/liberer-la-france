import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes, *, removed=None, repeal=None, benefit=None):
    row = {
        'proposed_xml': ''.join(f'<p>{p}</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }
    if removed:
        row.update(change_type='normative_reduction',
                   reform_policy_id='editorial_direction_2026_10_19',
                   removed_provisions=removed)
    if repeal:
        row.update(change_type='full_repeal',
                   repeal_policy_id='editorial_direction_2026_10_19',
                   repeal_scope=repeal)
    if benefit:
        row['benefit_review'] = benefit
    drafts[number] = row


add('144 bis', [
    "I. – Les soumissions cautionnées portant sur les rhums et tafias hors contingent et établies sous le régime du décret n° 51-77 du 10 janvier 1951 restent régies par ce décret.",
    "II. – Lorsqu'un rhum traditionnel des départements d'outre-mer, imputé sur le contingent prévu à l'article 362 du code général des impôts et préalablement importé en France métropolitaine, est réexporté ou réexpédié vers un autre État membre de l'Union européenne, le contingent d'origine est abondé à due concurrence. Cet abondement ne modifie pas l'évolution du contingent attribué à la distillerie.",
    "III. – Les certificats d'exportation préalable relatifs aux livraisons à l'étranger de rhums traditionnels des départements d'outre-mer effectuées sous le régime du décret n° 48-1590 du 8 octobre 1948 restent régis par ce décret.",
    "IV. – Le ministre chargé du budget fixe par arrêté les conditions d'application du présent article.",
],
    "Réécriture à droit constant des quatre subdivisions : les opérations ouvrant droit au réabondement sont exprimées directement et les deux régimes historiques restent identifiés. L'article maintient un avantage de contingent et des règles de continuité ; il ne crée ni taxe ni déclaration nouvelle à supprimer. L'habilitation d'application n'est pas transformée en agrément supplémentaire.",
    "Renvoi vérifié : CGI 362 maintient un contingent annuel de 153 000 hectolitres d'alcool pur, l'exemption de soulte et la limite de 90 % vol. Ces chiffres appartiennent au texte de renvoi et ne sont pas modifiés ici. Dates des décrets conservées : 10 janvier 1951 et 8 octobre 1948. Annexe IV 52 quater et annexe II 289, 57°, lus intégralement : ils organisent les certificats d'exportation préalable. Leur articulation avec le champ historique du III et leurs conditions propres, dont la validité de six mois dans 52 quater, nécessitent une coordination séparée ; aucune suppression de ces textes hors lot n'est présentée comme réalisée.",
    benefit="Le réabondement à due concurrence du contingent d'origine est maintenu pour toute réexportation ou réexpédition future remplissant les conditions du II. Les situations régies par les deux décrets anciens et les droits attachés à leurs certificats restent protégés, sans extinction ni nouvelle condition de délai dans cet article.")

add('169-0 A', [
    "Le certificat attestant que le rhum traditionnel des départements d'outre-mer répond à la définition du 1° du I de l'article 403 du code général des impôts peut être établi sur tout support permettant d'en vérifier l'authenticité. Le modèle fixé par l'administration peut être utilisé, sans être obligatoire. Le certificat comporte notamment les informations suivantes :",
    "a) Les noms de l'expéditeur et du destinataire, la période contingentaire, le département d'origine, le pays de destination, la désignation des marchandises et les quantités expédiées ;",
    "b) L'attestation de qualité et d'origine visée par l'autorité compétente.",
    "L'administration ou un organisme agréé par elle peut délivrer le certificat. L'agrément de l'organisme est publié au Bulletin officiel des douanes. Aucune pièce distincte reproduisant les données du certificat n'est exigée lorsque l'administration dispose déjà légalement de ces données exactes et à jour.",
    "Ces règles s'appliquent aux certificats délivrés à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris pour des expéditions antérieures. Les certificats déjà délivrés conservent leur validité dans les conditions qui leur sont applicables et n'ont pas à être refaits.",
],
    "Réforme de fond : le modèle administratif devient facultatif et l'engagement général de l'exportateur à respecter des règles déjà obligatoires est supprimé. La production en double de données déjà légalement disponibles est écartée. À droit constant, les informations du a), le visa de qualité et d'origine, les deux catégories d'émetteurs et la publication de l'agrément sont conservés : ces derniers éléments assurent l'authenticité d'une preuve ouvrant accès au régime fiscal du rhum, sans nouvelle déclaration de substitution.",
    "Le 1° du I de CGI 403 n'est pas présent dans l'édition du corpus fournie. Son absence ne prouve pas à elle seule la disparition du régime : vérifier la concordance avec le code des impositions sur les biens et services et les règles européennes applicables au rhum traditionnel, hors lot. Aucun nouveau numéro de renvoi n'est inventé. L'agrément conservé concerne l'organisme certificateur, non une autorisation de chaque expédition. Les rubriques a) et b) restent à leur place ; seul l'engagement général est retiré du b).",
    removed=[
        "Conformité obligatoire à un modèle administratif exclusif pour le certificat relatif au rhum traditionnel.",
        "Engagement formel distinct de l'exportateur portant sur le respect général de règles déjà applicables.",
        "Production séparée de pièces répétant des données exactes et à jour déjà légalement détenues par l'administration.",
    ],
    benefit="Le certificat continue d'établir les conditions du régime favorable du rhum traditionnel. Toutes les données de provenance, de destination, de période et de quantité ainsi que l'attestation visée sont conservées. L'accès futur à cet avantage reste ouvert ; les certificats antérieurs ne sont ni invalidés ni soumis à une réédition.")

add('171', [
    "Pour l'application du 2° des I et II de l'article 435 du code général des impôts, sont considérés comme mousseux les vins, boissons ou produits fermentés qui remplissent l'une des conditions suivantes : être présentés dans des bouteilles fermées par un bouchon « champignon » maintenu par des attaches ou des liens ; présenter une surpression due à l'anhydride carbonique en solution égale ou supérieure à 3 bar.",
],
    "Réécriture à droit constant : les deux critères alternatifs de classement sont rendus explicites. L'article ne prescrit pas ce conditionnement à tous les opérateurs et n'institue pas de formalité autonome. Supprimer l'un des critères modifierait la classification d'accise sans coordination européenne établie ; aucun taux ni champ fiscal n'est donc changé.",
    "Le seuil de 3 bar demeure inclusif et le critère du bouchon reste alternatif, sans cumul des deux conditions. CGI 435 n'a pas été retrouvé dans le corpus fourni : concordance à établir avec la législation actuelle des accises et ses définitions européennes, sans substitution silencieuse de renvoi.")

add('172', [
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. Aucune déclaration préalable de congélation des vins en vue de leur concentration partielle n'est exigée sur son fondement après cette date, y compris pour des opérations déjà engagées. Aucun dépôt tardif ou de régularisation de cette déclaration n'est exigé après cette date.",
    "Les déclarations antérieurement souscrites conservent leur valeur probante. Les droits à décharge et les réclamations relatifs aux pertes de volume restent ouverts dans les conditions des articles 174 et 178, sans condition tirée du dépôt de la déclaration supprimée. Les règles de production, les contrôles et les obligations de traçabilité ayant un fondement autonome demeurent applicables. Les sanctions non définitives restent soumises aux règles d'application de la loi répressive plus douce.",
],
    "Abrogation de fond de la déclaration spéciale préalable, applicable sans distinction de lieu, d'opérateur ou de pourcentage. La preuve matérielle des volumes et les contrôles suffisent à la fonction fiscale identifiée ; une annonce préalable générale n'est pas nécessaire à cette preuve et fait double emploi avec la traçabilité de production. Aucune déclaration, autorisation ou transmission de remplacement n'est créée. La décharge favorable est expressément maintenue et coordonnée.",
    "Coordination opératoire dans le présent lot : 173 abrogé, 174 sans complément déclaratif ni registre spécial, 175 déclenché par les opérations et non par une déclaration, 176 dispense sans autorisation et 178 décharge sans déclaration préalable. Annexe II 286 H et 286 I, sources et notes lues : la comptabilité matières et les registres vitivinicoles ont des fondements distincts, en partie européens. Leur réexamen ne résulte pas automatiquement de cette abrogation. La suppression vise uniquement la déclaration nationale de cet article et n'abroge aucun acte européen. Aucune remise générale de droits d'accise antérieurs n'est décidée.",
    repeal="Suppression de la déclaration préalable spéciale de congélation des vins aux fins de concentration partielle, pour tous lieux, opérateurs et pourcentages visés par la source, sans déclaration ni autorisation de remplacement.")

add('173', [
    "Le présent article est abrogé à compter de l'entrée en vigueur de la loi portant la présente réforme. Les rubriques spéciales de la déclaration de concentration des vins et leur transmission au service des douanes et droits indirects ne sont plus exigées sur ce fondement, y compris pour compléter ou régulariser après cette date une déclaration relative à des opérations antérieures.",
    "Les déclarations déjà souscrites conservent leur valeur probante. La suppression de leurs rubriques ne supprime ni la décharge prévue à l'article 178 ni les moyens de preuve admis par les articles 174 et 178. Les obligations de traçabilité ayant un fondement autonome demeurent applicables. Les sanctions non définitives restent soumises aux règles d'application de la loi répressive plus douce.",
],
    "Abrogation de fond de la liste de renseignements exigés pour la déclaration supprimée à l'article 172. Les rubriques d'identité, de vins et de programmation des travaux n'ont plus de dépôt spécial à alimenter. Elles ne sont pas transférées dans une déclaration équivalente ; seules les données techniques nécessaires à la preuve des pertes restent utilisables dans les pièces ordinaires prévues à l'article 174.",
    "Les 1° à 4° disparaissent avec l'intégralité de l'obligation déclarative : identité et domicile, quantité/couleur/richesse acquise et en puissance, catégorie/appellation, lieu/date/heure/durée probable. Ce n'est pas un résumé d'une norme maintenue. Les références à cet article dans les articles 174 et 176 sont effectivement retirées par leur réécriture. Aucune nouvelle obligation de programmation ou de déclaration ne résulte des pièces ordinaires de preuve.",
    repeal="Suppression des quatre rubriques obligatoires et du contenu de la déclaration spéciale de concentration des vins devenue inutile après l'abrogation de l'article 172, sans nouveau dépôt équivalent.")

add('174', [
    "À la fin des travaux de concentration des vins par le froid, le volume et la richesse alcoolique totale des vins obtenus sont établis à partir des pièces de production ou de la comptabilité matières déjà tenue. Aucun complément à une déclaration de concentration ni aucun relevé quotidien spécial n'est exigé sur le fondement du présent article.",
    "Lorsque la concentration porte successivement sur des vins de coupage, des vins de pays et des vins déclarés sous une appellation d'origine, les pièces de production ou la comptabilité matières déjà tenue permettent de distinguer, pour chacune de ces catégories, le volume et la richesse alcoolique totale des vins mis en œuvre et des vins obtenus après concentration. Pour les vins déclarés sous appellation d'origine, elles distinguent les lots en traitement, appellation par appellation. Aucun registre spécial, modèle administratif, cote ou paraphe n'est exigé sur ce fondement.",
    "Les différentes catégories de vins, en attente de traitement ou déjà traités, sont conservées dans des cuves, foudres ou récipients distincts. Ceux-ci portent des étiquettes rédigées en caractères indélébiles permettant d'identifier les vins.",
    "Ces règles s'appliquent à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux opérations en cours et à la preuve de pertes antérieures. Les informations déjà régulièrement consignées peuvent être utilisées sans nouvelle transcription. Les règles de traçabilité ayant un fondement autonome demeurent applicables.",
],
    "Réforme de fond : suppression du complément de déclaration, du relevé journalier déclenché par des travaux de plus de cinq jours et du registre administratif coté et paraphé. Les données de production déjà tenues remplacent le support spécial, sans nouvelle transmission. Les quantités et richesses d'entrée/sortie, la distinction par catégorie et appellation ainsi que la séparation et l'identification physiques sont maintenues pour prouver les pertes réelles et éviter substitutions et confusions d'origine.",
    "Les trois alinéas matériels restent dans leur ordre ; un alinéa de transition est ajouté. Le champ reste la concentration par le froid, expressément identifiée dans la subdivision source. Le seuil de plus de cinq jours disparaît avec l'obligation quotidienne qu'il déclenchait : aucune condition de fond maintenue n'est omise. La richesse alcoolique totale, les trois catégories, les lots par appellation et les étiquettes indélébiles demeurent. À articuler avec les registres autonomes de l'annexe II 286 I et les prescriptions européennes de production, sans prétendre les avoir abrogés. Les pièces de preuve ne constituent ni une nouvelle déclaration ni une autorisation de concentration.",
    removed=[
        "Complément obligatoire de la déclaration spéciale de concentration à la fin des travaux ou à la fin de chaque journée lorsque les travaux durent plus de cinq jours.",
        "Tenue d'un registre propre aux opérations successives conforme à un modèle administratif, fourni par l'opérateur et coté et paraphé par le chef de service local.",
        "Transcription obligatoire dans ce registre spécial de données d'entrée, de sortie et d'appellation déjà établies dans les pièces ordinaires de production ou la comptabilité matières.",
    ])

add('175', [
    "Du commencement des opérations de concentration des vins par le froid jusqu'à l'expiration d'un délai de quinze jours compté de la date de cessation des travaux, le préparateur est soumis, dans ses ateliers, magasins, caves et celliers, aux vérifications des agents des douanes et droits indirects et des agents de la répression des fraudes. Il leur présente tous les vins qu'il détient et qui sont en attente de traitement, en cours de traitement ou déjà traités. Les agents peuvent prélever gratuitement des échantillons de ces vins.",
    "Pour les opérations commencées à compter de l'entrée en vigueur de la loi portant la présente réforme, le commencement des opérations suffit à l'application du présent article, sans déclaration ni autorisation préalable. Pour les opérations commencées auparavant, les vérifications restent possibles jusqu'à l'expiration du délai de quinze jours compté de la date de cessation des travaux, sans nouveau dépôt. Les pouvoirs de contrôle ayant un autre fondement demeurent applicables avec leurs garanties propres.",
],
    "Réforme de fond de coordination : le dépôt préalable supprimé ne déclenche plus une période spéciale de vérification avant le début des travaux. Le contrôle est rattaché aux opérations elles-mêmes, sans formalité de substitution. Le délai de quinze jours après cessation, les lieux, les catégories de vins à présenter et le prélèvement gratuit d'échantillons sont maintenus pour contrôler la réalité des pertes et prévenir la fraude.",
    "La période spéciale commence au début effectif des opérations, et non à une déclaration, sans délai minimal d'attente ni obligation de conserver les vins sur place pendant quinze jours ajoutée au texte. Le délai de quinze jours reste expressément compté de la date de cessation, sans déplacement du point de départ. Le champ demeure la concentration par le froid de la subdivision source. Les quatre catégories de locaux et les trois états des vins sont conservés. Cette coordination n'étend ni les pouvoirs d'accès ni les contrôles autonomes prévus par d'autres textes ; leurs garanties procédurales demeurent. Pour les opérations anciennes, la fin de la période de contrôle n'est ni réouverte ni repoussée.",
    removed=[
        "Déclenchement des vérifications spéciales de concentration dès le dépôt de la déclaration préalable, avant même le commencement des travaux pour les opérations nouvelles.",
    ])

add('176', [
    "Les opérations de congélation des vins en vue de leur concentration partielle sont dispensées de la déclaration préalable spéciale de concentration, sans autorisation personnelle du service des douanes et droits indirects. Cette dispense ne peut être subordonnée à la tenue d'un registre spécial, à une inscription préalable à la fabrication, à une cote ou à un paraphe.",
    "Cette dispense s'applique à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux opérations en cours et aux opérateurs qui ne bénéficiaient pas d'une autorisation antérieure. Les autorisations déjà accordées et les inscriptions déjà effectuées n'ont pas à être renouvelées ou reproduites. Les contrôles prévus à l'article 175 et les règles de preuve des articles 174 et 178 restent applicables ; aucun retrait de la dispense générale ne peut être prononcé sur le seul fondement du présent article. Les obligations directement issues du droit de l'Union européenne demeurent applicables dans leur champ propre.",
],
    "Réforme de fond favorable : la dispense devient générale et de plein droit, en coordination avec l'abrogation de 172. Sont supprimés l'autorisation personnelle, le registre de substitution coté et paraphé, l'inscription avant fabrication et le retrait de cette dispense pour abus. La répression des fraudes et les preuves techniques subsistent sur leurs fondements propres ; aucun agrément n'est remplacé par une déclaration.",
    "Ne pas abroger purement et simplement cet article favorable en laissant planer un doute sur la dispense : son fondement autonome est explicité pour les futurs opérateurs. Le renvoi à 172, désormais abrogé, est retiré ; son champ de congélation aux fins de concentration partielle est repris sans étendre la dispense à des déclarations européennes autonomes ou à d'autres procédés. Les pièces ordinaires de 174 ne reconstituent pas le registre préalable de cet article et ne doivent pas être exigées sous ce format par un texte d'application. Le bénéfice fiscal de 178 ne devient pas dépendant d'une autorisation de dispense.",
    removed=[
        "Autorisation personnelle préalable des douanes conditionnant la dispense de déclaration de concentration.",
        "Inscription avant toute fabrication dans un registre de substitution fourni par l'opérateur, coté et paraphé par le service local.",
        "Présentation obligatoire de ce registre spécial et pouvoir de retirer la dispense administrative en cas d'abus sur ce seul fondement.",
    ],
    benefit="L'avantage identifié est la dispense de déclaration préalable, autrefois réservée aux concentrateurs autorisés. Il est maintenu et étendu de plein droit à tous les opérateurs futurs et aux opérations en cours. Sa jouissance n'exige plus ni autorisation ni registre préalable ; les abus restent contrôlables sans rétablir cette charge générale.")

add('178', [
    "La perte de volume des vins soumis à une concentration par le froid est admise en décharge pour l'assiette du droit de circulation lorsque l'opération est effectuée régulièrement et dans les limites fixées. La réalité et le volume de la perte peuvent être établis par les pièces mentionnées à l'article 174 ou par tout autre élément probant. Le bénéfice de la décharge ne peut être subordonné à une déclaration préalable de concentration, à une autorisation personnelle de dispense ou à la tenue d'un registre spécial de substitution.",
    "Ces règles de preuve s'appliquent à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux demandes et réclamations relatives à des opérations antérieures non définitivement réglées. Elles ne ferment aucun droit à décharge pour des opérations futures éligibles. Les règles de prescription et les décisions définitives demeurent applicables.",
],
    "Réforme de fond : suppression de la déclaration régulière comme condition de la décharge et ouverture de la preuve aux pièces déjà tenues ou à tout élément probant. À droit constant, la régularité de l'opération, ses limites et la déduction de la perte de volume pour l'assiette restent maintenues. La suppression des formalités de 172 à 176 ne doit pas entraîner la disparition de cet avantage.",
    "La décharge concerne le volume effectivement perdu et non une exonération de toute la production. La mention du froid explicite le champ de la subdivision source, sans retirer une décharge autonome applicable à un autre procédé. Les limites techniques et les règles de production ne sont ni augmentées ni supprimées. Renvoi à 174 vérifié et coordonné. Le droit de circulation et ses anciens renvois législatifs doivent être mis en concordance avec la législation actuelle des accises hors lot ; l'absence de CGI 435/438 dans le corpus n'autorise pas à supprimer la décharge. Aucun taux de perte nouveau ni remboursement automatique hors prescription n'est créé.",
    removed=[
        "Condition de déclaration préalable régulière de la concentration pour bénéficier de la décharge de la perte de volume des vins traités.",
        "Opposabilité de l'absence d'autorisation de dispense ou de registre spécial comme motif formel de refus de cette décharge.",
    ],
    benefit="La décharge des pertes de volume pour l'assiette du droit de circulation demeure pour toute concentration régulièrement effectuée dans les limites applicables, y compris à l'avenir. Les demandes anciennes non définitives profitent de la preuve simplifiée, sans suppression des prescriptions ni remise en cause des décisions définitives. Aucun prélèvement de remplacement n'est institué.")

add('178-0 bis', [
    "Les entrepositaires agréés, les destinataires enregistrés, les expéditeurs enregistrés, les importateurs et les personnes réalisant des acquisitions intracommunautaires, redevables du droit de circulation dans les conditions de l'article 302 D du code général des impôts, bénéficient du tarif prévu au a bis du 2° de l'article 438 du même code pour les vins qui y sont visés et sont obtenus conformément au règlement (CE) n° 1234/2007 du Conseil du 22 octobre 2007, lorsque l'alcool du produit résulte entièrement d'une fermentation et que le produit n'a subi aucun enrichissement, même autorisé par les A et B de l'annexe XV bis de ce règlement. Aucun dépôt préalable distinct auprès du bureau de déclaration des douanes et droits indirects ne conditionne ce bénéfice.",
    "Ces conditions peuvent être établies par tout élément probant. Tout document qui en atteste le respect et émane d'une autorité administrative chargée du contrôle des modes de production et d'élaboration des produits vitivinicoles dans l'État de production est admis comme justificatif. Les données et pièces exactes, à jour et déjà légalement disponibles pour l'administration sont réutilisées sans nouvelle production par l'intéressé. Les documents directement exigés par le droit de l'Union européenne demeurent requis dans leur champ propre, sans dépôt national supplémentaire au seul titre du présent article.",
    "Ces règles de preuve s'appliquent à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris aux demandes et réclamations en cours, sans rouvrir les prescriptions expirées ni remettre en cause les décisions définitives. Les justificatifs déjà délivrés demeurent recevables.",
],
    "Réforme de fond : le bénéfice du tarif dépend des caractéristiques réelles du vin et non d'un dépôt justificatif préalable. L'exclusivité d'une pièce émanant de l'autorité de l'État de production est levée, tout en garantissant sa recevabilité ; les doubles productions sont supprimées. Les catégories d'opérateurs, l'absence totale d'enrichissement, l'origine entièrement fermentaire de l'alcool et le champ du tarif demeurent. Les exigences européennes directement applicables ne sont pas effacées par une dispense nationale.",
    "CGI 302 D et 438 sont absents du corpus fourni ; leur concordance actuelle doit être établie, de même que celle du règlement 1234/2007 et de son annexe XV bis. Aucune substitution de numéro ou élargissement tacite aux produits enrichis n'est effectué. Le régime de preuve est effectivement modifié : une pièce officielle reste suffisante mais n'est plus la seule admissible sur ce fondement national. Vérifier séparément les certifications imposées directement pour les mouvements d'accise dans l'Union ; elles ne sont pas déclarées abrogées. Les deux alinéas matériels restent suivis d'une transition.",
    removed=[
        "Justification préalable distincte auprès du bureau de déclaration des douanes comme condition d'accès au tarif des vins visés.",
        "Exclusivité d'un justificatif émanant de l'autorité administrative de contrôle de l'État de production lorsque d'autres preuves établissent les mêmes conditions.",
        "Nouvelle remise de pièces exactes et à jour déjà légalement disponibles pour l'administration fiscale ou douanière.",
    ],
    benefit="Le tarif favorable reste ouvert à tous les opérateurs énumérés et à toutes les productions futures qui respectent les conditions de fermentation intégrale et d'absence d'enrichissement. Les preuves officielles de l'État de production demeurent recevables. Le retrait du dépôt préalable et l'admission d'autres preuves ne ferment aucun avantage existant et ne créent aucune taxe équivalente.")

add('178-0 bis A', [
    "Pour l'application des taux réduits du droit spécifique mentionnés du cinquième au huitième alinéa du a du I de l'article 520 A du code général des impôts, est une petite brasserie indépendante une brasserie établie dans un État membre de l'Union européenne qui remplit cumulativement les conditions suivantes :",
    "1° Elle produit moins de 200 000 hectolitres de bière par an ;",
    "2° Elle est juridiquement et économiquement indépendante de toute autre brasserie ;",
    "3° Ses installations sont physiquement distinctes de celles de toute autre brasserie ;",
    "4° Elle ne produit pas sous licence.",
    "Lorsque deux ou plusieurs petites brasseries coopèrent et que leur production annuelle totale ne dépasse pas 200 000 hectolitres, elles peuvent être traitées comme une seule petite brasserie indépendante.",
],
    "Réécriture à droit constant : les quatre critères cumulatifs et le traitement favorable des brasseries coopérantes sont formulés directement. Cet article définit l'accès à des taux réduits, sans imposer de dossier ou d'autorisation supplémentaire. Les formalités sont supprimées dans 178-0 bis B ; les critères de fond liés au régime européen des petites brasseries restent maintenus, sans nouveau taux ni restriction.",
    "Conserver la différence de bornes de la source : production individuelle strictement inférieure à 200 000 hectolitres, production agrégée des coopérantes ne dépassant pas 200 000 hectolitres. Aucun alignement silencieux. CGI 520 A n'est pas présent dans l'édition du corpus ; vérifier la concordance des alinéas et la législation d'accise actuelle, notamment le régime de la directive 92/83/CEE, sans prétendre que les critères européens sont supprimables par ce seul règlement national. La faculté de traitement commun et les quatre numéros sont conservés.",
    benefit="Les taux réduits restent accessibles à toute brasserie future éligible et la faculté de traiter des petites brasseries coopérantes comme une seule demeure. Sont conservés les seuils exacts, l'indépendance juridique et économique, les installations distinctes et l'absence de licence. Aucun agrément ni déclaration de reconnaissance n'est ajouté par cet article.")

add('178-0 bis B', [
    "I. – La production annuelle d'une petite brasserie indépendante correspond à la bière produite pendant les douze mois de son exercice commercial, après déduction du taux annuel forfaitaire de pertes prévu à l'article 50-0 L de l'annexe IV au code général des impôts.",
    "Pour l'application des taux réduits du droit spécifique mentionnés du cinquième au huitième alinéa du a du I de l'article 520 A du même code, le volume retenu est celui effectivement produit au cours des douze mois de l'exercice commercial précédent.",
    "II. – Les quantités produites au sens du premier alinéa du I sont déterminées à partir de la comptabilité matières déjà tenue. Aucune déclaration annuelle distincte de production ni transmission systématique de ces quantités n'est exigée au titre du présent article. Les éléments nécessaires à leur contrôle restent accessibles au service des douanes et droits indirects territorialement compétent selon les règles de contrôle applicables.",
    "III. – Pour une brasserie nouvellement créée, les taux réduits mentionnés du cinquième au huitième alinéa du a du I de l'article 520 A du code général des impôts s'appliquent sur la base des quantités qu'elle envisage de produire. L'estimation est établie à partir des données professionnelles dont elle dispose, sans déclaration prévisionnelle distincte au service des douanes.",
    "Le montant du droit spécifique acquitté au titre du premier exercice est, s'il y a lieu, réajusté après sa clôture lors de la prochaine liquidation normalement exigible de ce droit, sans déclaration spéciale de production. Un réajustement à la baisse ne peut être différé du seul fait de l'absence de liquidation ultérieure ; il donne lieu, selon les règles applicables, à compensation ou à remboursement.",
    "IV. – Pour la demande de compensation ou de remboursement prévue à l'article 286 M de l'annexe II au code général des impôts, le service des douanes et droits indirects compétent utilise les éléments exacts et à jour dont il dispose déjà légalement pour vérifier le taux du droit spécifique acquitté ou supporté pour les bières concernées. L'entrepositaire agréé ne présente, sur demande du service, que les justificatifs nécessaires qui ne sont pas déjà disponibles.",
    "Les simplifications des II à IV s'appliquent aux transmissions et demandes à compter de l'entrée en vigueur de la loi portant la présente réforme, y compris lorsqu'elles concernent un exercice antérieur ou déjà commencé. Les déclarations déjà déposées n'ont pas à être refaites ; aucun dépôt tardif de la déclaration annuelle ou prévisionnelle supprimée n'est exigé sur ce fondement. Les droits légalement dus, les taux réduits, compensations et remboursements, les prescriptions et les recours relatifs aux exercices antérieurs demeurent préservés, sous réserve de l'application de la loi répressive plus douce aux sanctions non définitives.",
],
    "Réforme de fond : suppression de la déclaration annuelle au dixième jour suivant la clôture, de la déclaration prévisionnelle séparée des brasseries nouvelles et des justificatifs de remboursement déjà détenus. Les données nécessaires sont réemployées dans la comptabilité existante et les liquidations ordinaires ; aucun agrément ni déclaration de production de remplacement n'est créé. À droit constant, les deux périodes de douze mois, la déduction forfaitaire de pertes, l'accès immédiat des brasseries nouvelles aux taux réduits, le réajustement du premier exercice et les restitutions restent maintenus.",
    "Subdivisions I à IV et ordre des six alinéas matériels conservés ; transition finale ajoutée. Le dixième jour du mois suivant la clôture disparaît avec le dépôt annuel, sans nouvelle échéance de production. Le réajustement à la baisse reste possible même sans liquidation ultérieure, selon les voies ordinaires de compensation ou remboursement : pas de créance bloquée par la suppression du dépôt. Annexe IV 50-0 L lue en entier, tableau compris : la bière conserve le taux de pertes de 1 % des quantités sorties ; le renvoi est maintenu, sans inventer une autre assiette de pertes. Annexe II 286 M lue en entier : la demande de compensation/remboursement, son ressort, son délai propre de trois mois et la compétence du directeur interrégional restent distincts et ne sont pas supprimés ici. CGI 520 A manque au corpus : concordance à établir. Annexe II 289, 69°, vise un certificat des petits producteurs relevant du CIBS : son éventuelle exigence européenne n'est pas réputée supprimée par la fin des déclarations nationales de production. La note du décret du 9 août 2017 n'est pas une date de réforme. La tenue de quantités annuelles sert au taux réduit d'accise et ne rétablit pas l'ancien IS annuel.",
    removed=[
        "Déclaration annuelle distincte des quantités produites à transmettre aux douanes au plus tard le dixième jour du mois suivant la clôture de la comptabilité matières.",
        "Transmission d'une déclaration prévisionnelle de production par les brasseries nouvellement créées pour accéder aux taux réduits.",
        "Dépôt de la déclaration annuelle comme support obligatoire du réajustement du droit spécifique du premier exercice.",
        "Présentation systématique de justificatifs du taux acquitté ou supporté pour les remboursements et compensations lorsque ces preuves sont déjà légalement disponibles.",
    ],
    benefit="Sont maintenus la déduction du taux forfaitaire de pertes, les taux réduits sur la production de référence de l'exercice précédent, leur application prévisionnelle dès la création d'une brasserie et les droits à compensation ou remboursement. Le réajustement du premier exercice reste possible dans les deux sens. Ces avantages restent ouverts aux futurs producteurs éligibles, sans dépôt annuel ou prévisionnel distinct.")

add('183', [
    "Les poinçons de maître et de responsabilité ainsi que les poinçons de garantie sont conformes aux modèles fixés par décret. Cette obligation s'applique aux poinçons de garantie utilisés par les professionnels habilités par une convention avec l'administration des douanes et droits indirects dans les conditions de l'article L. 832-4 du code de commerce, par les organismes de contrôle agréés dans les conditions du II du même article et par les services de la garantie. Les marquages au laser respectent les mêmes modèles.",
    "Les poinçons ou les marquages au laser sont apposés sur les ouvrages dans les conditions déterminées par l'administration.",
],
    "Réécriture à droit constant : les catégories de poinçons, les utilisateurs et l'application des modèles au laser sont distingués pour faciliter la lecture. Les règles communes de marquage ont une fonction essentielle d'identification du responsable et de prévention de la fraude sur le titre des métaux ; leur suppression rendrait la garantie illisible. Aucun nouveau contrôle préalable, agrément ni justificatif n'est ajouté.",
    "Renvois à L. 832-4 du code de commerce et à son II maintenus exactement ; le code de commerce n'est pas dans le corpus fourni, leur portée doit être vérifiée hors lot avant adoption. La convention des professionnels et l'agrément des organismes ne sont pas confondus. Les modèles et conditions d'apposition restent distincts des dispenses de l'article 186 ter, lesquelles demeurent applicables. Deux alinéas conservés.")

add('184', [
    "Les poinçons de garantie métalliques utilisés par les professionnels habilités, les organismes de contrôle agréés et les bureaux de garantie comportent un signe caractéristique particulier fixé par la Monnaie de Paris. Ce signe est changé chaque fois que cela est nécessaire.",
],
    "Réécriture à droit constant : les utilisateurs et l'autorité qui fixe le signe sont exprimés directement. Le signe distinctif et son renouvellement nécessaire protègent contre les contrefaçons de garantie ; il n'existe ici ni déclaration périodique ni renouvellement à échéance fixe à supprimer. Aucun changement systématique ou coût nouveau n'est institué.",
    "La règle ne vise que les poinçons de garantie métalliques et non un remplacement automatique de tous les marquages au laser. La Monnaie de Paris reste compétente ; le renouvellement demeure lié à sa nécessité et aucun délai ou tarif n'est ajouté. Coordination avec les modèles de 183 et la fabrication de 186.")

add('186', [
    "La Monnaie de Paris fabrique tous les poinçons de garantie métalliques et en conserve les matrices. Elle les adresse aux bureaux de garantie, aux professionnels habilités et aux organismes de contrôle agréés.",
],
    "Réécriture à droit constant : la fabrication, la conservation des matrices et les destinataires sont rattachés explicitement à la Monnaie de Paris. La maîtrise des matrices et de la fabrication permet d'authentifier les poinçons et de prévenir leur contrefaçon ; elle est maintenue avec la fonction essentielle de garantie. L'article ne crée pas de dossier, de déclaration ou de redevance autonome à supprimer.",
    "Champ limité aux poinçons métalliques de garantie : ni poinçons de maître supplémentaires ni fabrication des marquages au laser ne sont ajoutés. Les trois catégories de destinataires demeurent. Aucun tarif de fourniture, coût ou économie budgétaire n'est fixé par la proposition.")

add('186 bis', [
    "Les ouvrages d'or aux titres légaux de 585 millièmes et de 375 millièmes portent, respectivement, les poinçons de titre ou le marquage au laser conformes au tableau annexé au décret n° 95-612 du 5 mai 1995.",
    "Le fabricant d'un ouvrage à l'un de ces deux titres peut aussi y indiquer le titre en millièmes. Cette indication ne dispense pas de l'apposition du poinçon de garantie ou du marquage au laser, qui seul fait foi du titre.",
],
    "Réécriture à droit constant des deux alinéas : les deux titres et leur correspondance avec les modèles sont conservés, ainsi que la faculté d'une indication supplémentaire. La marque officielle protège l'acquéreur contre une fausse déclaration de teneur ; elle n'est pas supprimée. Aucune mention supplémentaire obligatoire n'est créée et les dispenses légales de garantie ne sont pas retirées.",
    "Chiffres inchangés : 585 et 375 millièmes ; décret n° 95-612 du 5 mai 1995. Le tableau est incorporé par renvoi, il ne figure pas dans source_xml et aucun source_companions n'est fourni : ses dessins ne sont ni inventés ni prétendus reproduits. Maintenir la concordance de ce décret avec les modèles de 183 et le régime actuel du code de commerce, dont la dispense de faible poids conservée par 186 ter. La mention volontaire ne devient jamais une preuve officielle concurrente.",
    benefit="La faculté pour les fabricants d'ajouter le titre en millièmes est maintenue pour les deux titres légaux et pour les fabrications futures. Elle n'est pas transformée en obligation. Les exemptions de garantie fondées sur le faible poids restent dans leur champ propre ; la réécriture n'écarte pas l'article 186 ter.")

add('186 ter', [
    "Pour l'application du 2° de l'article L. 833-2 du code de commerce, sont dispensés d'attestation de la garantie du titre les ouvrages contenant de l'or ou du platine dont le poids est inférieur à 3 grammes et les ouvrages contenant de l'argent dont le poids est inférieur à 30 grammes.",
],
    "Réécriture à droit constant favorable : la dispense est formulée directement à partir des seuils réglementaires, sans changer les métaux concernés ni les bornes. Cette disposition réduit une obligation de garantie et doit être conservée ; elle n'est assortie d'aucune demande ou attestation de dispense nouvelle.",
    "Seuils stricts maintenus : moins de 3 grammes pour l'or ou le platine ; moins de 30 grammes pour l'argent. Le poids exactement égal au seuil n'est pas ajouté à la dispense. Le 2° de L. 833-2 du code de commerce reste le fondement de renvoi ; son texte n'est pas dans le corpus autorisé et doit être confronté hors lot. Il s'agit de dispense d'attestation de garantie, non d'une suppression générale des titres légaux ou des obligations autonomes d'information.",
    benefit="La dispense d'attestation de garantie du titre est intégralement conservée pour les ouvrages futurs et présents remplissant les seuils de poids : moins de 3 grammes pour ceux contenant or ou platine, moins de 30 grammes pour ceux contenant argent. Elle reste ouverte de plein droit, sans agrément, certificat de dispense ni fermeture aux nouveaux fabricants.")

add('187', [
    "Sauf lorsque le professionnel bénéficie d'une délégation de poinçon de garantie, la garantie du titre est attestée par un bureau de garantie choisi par le professionnel ou par un organisme de contrôle agréé.",
    "Le ministre chargé du budget fixe le nombre et les circonscriptions des bureaux de garantie. Ces circonscriptions ne limitent pas le choix du professionnel prévu au premier alinéa.",
    "La liberté de choix s'applique aux demandes présentées à compter de l'entrée en vigueur de la loi portant la présente réforme. Les demandes déjà déposées continuent d'être instruites par le service saisi et les attestations régulièrement délivrées conservent leur validité.",
],
    "Réforme de fond : suppression du rattachement territorial obligatoire à un bureau pour obtenir l'attestation. Le professionnel peut choisir un bureau sans nouveau dossier d'autorisation de choix. La délégation favorable et la possibilité d'un organisme agréé restent maintenues ; le nombre et la répartition des bureaux demeurent une compétence d'organisation interne. La vérification du titre, utile contre la fraude, n'est pas supprimée.",
    "La réforme porte uniquement sur le bureau délivrant l'attestation, sans changer les compétences des autorités de recours ou des contrôleurs. Le texte de 207, lu dans le corpus, conserve notamment ses autorités territoriales propres pour le nouvel essai. Les deux alinéas sources restent dans leur ordre et une transition est ajoutée. Vérifier les actes fixant les circonscriptions et les règles de réception des ouvrages hors des cinq codes, afin qu'ils ne rétablissent pas l'exclusivité territoriale supprimée. Ni nouvel agrément ni nouvelle redevance ne sont instaurés.",
    removed=[
        "Obligation pour le professionnel dépourvu de délégation de s'adresser exclusivement au bureau de garantie de son ressort territorial pour l'attestation du titre.",
    ],
    benefit="La délégation de poinçon de garantie continue à dispenser son bénéficiaire du passage par le bureau ou l'organisme pour l'attestation dans son champ légal. Le recours à un organisme agréé reste ouvert. Les futurs demandeurs gagnent le choix d'un bureau de garantie et les attestations antérieures ne perdent pas leur validité.")

add('189', [
    "Le bureau de garantie choisit l'essai au touchau ou, lorsqu'il l'estime nécessaire, un essai à la coupelle, par la voie humide ou par toute autre méthode en vigueur assurant un niveau de sécurité et de fiabilité équivalent. Ces autres essais sont réalisés auprès du service commun des laboratoires du ministère de l'économie, des finances et de l'industrie. L'essai au touchau n'est pas un préalable obligatoire à leur réalisation.",
    "Cette règle s'applique aux essais entrepris à compter de l'entrée en vigueur de la loi portant la présente réforme. Les essais antérieurement réalisés conservent leur valeur ; un essai supplémentaire ne peut être imposé au seul motif qu'il n'a pas été précédé d'un essai au touchau.",
],
    "Réforme de fond : suppression de l'essai au touchau comme passage obligé cumulatif avant une autre méthode. Le bureau peut retenir directement l'essai nécessaire, au lieu de multiplier les opérations. À droit constant, le recours au laboratoire public pour ces autres essais, leur appréciation par le bureau et l'exigence de sécurité et de fiabilité équivalentes sont maintenus. Aucune autorisation ou preuve supplémentaire n'est créée.",
    "Les quatre voies de la source sont conservées : touchau, coupelle, voie humide, autre méthode en vigueur d'un niveau équivalent. Le texte ne privatise pas l'expertise du laboratoire et ne supprime pas un contre-essai justifié par une contestation de titre dans 203 et 204. L'intitulé ancien du ministère est maintenu comme désignation de la source ; vérifier l'organisation administrative actuelle hors corpus, sans inventer de nouvel établissement. Le caractère systématique de l'essai au touchau dans la première phrase source est expressément écarté, y compris comme simple condition de forme opposée à un résultat antérieur.",
    removed=[
        "Essai systématique au touchau comme préalable obligatoire, même lorsqu'un autre essai offrant une sécurité et une fiabilité équivalentes est directement retenu.",
    ])

add('190', [
    "L'essai peut aussi être réalisé sur les prélèvements de métal effectués par le service des douanes et droits indirects pendant la fabrication.",
],
    "Réécriture à droit constant : la possibilité d'utiliser les prélèvements effectués en cours de fabrication est exprimée sans tournure impersonnelle. Cette faculté évite de prélever à nouveau l'ouvrage fini et contribue à la fiabilité du contrôle ; elle n'impose pas un prélèvement systématique. Aucune obligation autonome ou taxe n'est créée par cet article.",
    "La faculté reste celle du service des douanes et droits indirects et porte sur des prélèvements pendant la fabrication. Aucun échantillonnage périodique obligatoire, agrément de fabrication ou délai d'attente n'est introduit. Les méthodes d'essai sont celles de 189, coordonné dans le lot.")

add('191', [
    "Les professionnels peuvent demander aux bureaux de garantie de déterminer le titre des lingots, apprêts ou composants entrant dans leurs fabrications. Aucune rémunération n'est due pour les déterminations effectuées à compter de l'entrée en vigueur de la loi portant la présente réforme.",
    "Les rémunérations légalement nées de déterminations effectuées avant cette date restent soumises aux règles antérieures pour leur liquidation, leur recouvrement, leur restitution, leur prescription et leur contestation. La suppression de la rémunération pour l'avenir n'ouvre pas droit à un remboursement général des sommes antérieurement dues.",
],
    "Réforme de fond : suppression de la rémunération accessoire d'une détermination de titre demandée volontairement, ainsi que de l'habilitation à en fixer le tarif. Le service facultatif rendu aux professionnels demeure et aucun prélèvement de substitution n'est instauré. Les vérifications obligatoires distinctes ne sont pas modifiées par cette gratuité et les créances de prestations déjà effectuées sont préservées.",
    "Annexe IV 56 J bis lue intégralement : elle fixe actuellement 38 euros par opération pour l'or et le platine, 15 euros pour l'argent, avec perception douanière aux produits divers du budget. Sa proposition antérieure du corpus conserve ces tarifs : elle est incompatible avec la présente décision nouvelle et doit être reprise pour retirer tarifs et perception pour les prestations nouvelles, avec la même transition. Ce fichier hors lot n'est pas modifié. Le fait de rattachement est la détermination effectuée, non la date de paiement ou de dépôt de la demande. Aucun rendement budgétaire ni financement compensatoire n'est inventé ; le coût public du service gratuit reste à documenter.",
    removed=[
        "Rémunération obligatoire du bureau de garantie pour la détermination facultative du titre des lingots, apprêts ou composants entrant dans les fabrications professionnelles.",
        "Habilitation du ministre chargé des finances à fixer par arrêté les tarifs de cette rémunération pour les prestations nouvelles.",
    ],
    benefit="La faculté de faire déterminer par un bureau de garantie le titre des lingots, apprêts et composants reste ouverte à tous les professionnels futurs. La rémunération de ce service disparaît pour toutes les déterminations nouvelles ; aucun autre tarif ou prélèvement de remplacement n'est créé. Les restitutions et recours sur les anciennes sommes demeurent.")

add('203', [
    "Lorsqu'un ouvrage d'or, d'argent ou de platine présente un titre au moins égal au plus bas titre légal applicable au métal concerné, mais ne correspond exactement à aucun des titres légaux, il est marqué au titre légal immédiatement inférieur à celui constaté par l'essai. Si le propriétaire le souhaite, l'ouvrage est, à la place, brisé ou exporté. Le propriétaire peut toutefois demander un nouvel essai.",
],
    "Réécriture à droit constant : le traitement normal au titre immédiatement inférieur est distingué des options du propriétaire et de son droit à un nouvel essai. Aucune destruction automatique n'est créée. Le marquage exact protège contre la vente sous un titre excessif, tandis que les trois possibilités favorables au propriétaire sont conservées ; aucune formalité inutile n'est ajoutée.",
    "La source vise les ouvrages qui ne sont pas au-dessous du plus bas titre légal et qui ne correspondent exactement à aucun titre légal. La proposition ne doit pas conduire à comparer un métal aux minima des autres métaux : le minimum pertinent est celui qui lui est applicable. L'absence de titre exact déclenche le marquage immédiatement inférieur, non un titre fiscal nouveau. Les alternatives de bris, d'exportation et de nouvel essai sont maintenues. À distinguer de 205, relatif notamment à l'ouvrage réellement inférieur au minimum, et du recours autonome de 207.")

add('204', [
    "En cas de contestation du titre d'un ouvrage, une prise d'essai peut être effectuée sur cet ouvrage et adressée au service commun des laboratoires du ministère de l'économie, des finances et de l'industrie.",
],
    "Réécriture à droit constant : l'objet du prélèvement et la destination de la prise d'essai sont explicités. Il s'agit d'une faculté d'expertise en cas de contestation, utile au contradictoire et à la fiabilité du titre, sans prélèvement automatique ni autorisation nouvelle. Sa suppression diminuerait les moyens de contestation du propriétaire.",
    "Le caractère facultatif, le prélèvement sur l'ouvrage contesté et le laboratoire destinataire sont conservés. Articulation avec le nouvel essai de 203 et les conséquences de 205. Vérifier hors corpus la désignation administrative actuelle du laboratoire, sans modifier silencieusement l'intitulé de la source ni prétendre que ce recours ferme l'accès au juge.")

add('205', [
    "Le titre définitif de l'ouvrage est déterminé d'après le résultat de l'essai réalisé par le service commun des laboratoires du ministère de l'économie, des finances et de l'industrie. Si un marquage est nécessaire, il est conforme à ce résultat. Lorsque le titre est inférieur au minimum légal, l'ouvrage est brisé ou exporté.",
],
    "Réécriture à droit constant : le résultat de laboratoire, le titre définitif et les conséquences du résultat sont exposés en trois phrases. La règle évite qu'un ouvrage inférieur au minimum soit mis en circulation avec une garantie trompeuse et maintient l'alternative d'exportation. Ni destruction systématique des ouvrages conformes ni nouvelle taxe ne sont ajoutées.",
    "Le titre définitif résulte de l'essai de laboratoire ; le marquage n'intervient que s'il y a lieu. L'alternative bris/exportation reste limitée à un titre inférieur au minimum légal, sans inventer un nouveau seuil. La source ne précise pas qui choisit cette alternative ni les conditions d'exportation : cette lacune est signalée, non comblée par une autorisation nouvelle. Le caractère définitif du titrage ne doit pas être interprété comme abolissant les voies de recours autonomes. Les droits au nouvel essai de 203 et à la contestation de 204 demeurent dans leur champ.")


assert len(drafts) == len(sources) == 24
answer = []
for source in sources:
    number = source['number']
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[number])
    if source.get('benefit_check_required'):
        assert len(item.get('benefit_review', '')) >= 100, number
    answer.append(item)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
