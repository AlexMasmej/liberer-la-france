import json
from pathlib import Path


drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('93 H bis', [
    "Les sociétés émettrices et les banques chargées de centraliser les émissions peuvent être autorisées à payer sur états le droit de timbre de dimension afférent aux bulletins de souscription d'actions. L'autorisation n'est valable que pour une seule constitution de société ou une seule augmentation de capital. Toutefois, les établissements de crédit chargés de centraliser les émissions d'actions peuvent obtenir des autorisations permanentes dans les conditions de l'article 93 H quater.",
],
    "Réécriture à droit constant : les bénéficiaires de l'autorisation sont placés en sujet et la limitation à une opération est énoncée dans une phrase distincte. L'exception permettant une autorisation permanente est maintenue. Aucune réforme de fond de policy.json ne vise ce régime.",
    "Renvoi à l'article 93 H quater conservé et coordonné avec sa réécriture dans ce lot. La distinction entre banques bénéficiaires de l'autorisation ponctuelle et établissements de crédit susceptibles d'obtenir une autorisation permanente est conservée. La source maintient un dispositif de timbre de dimension ancien : son champ d'application résiduel doit être contrôlé, sans présumer son abrogation.")

add('93 H ter', [
    "Lorsque la société présente elle-même la demande, elle doit s'engager expressément :",
    "1° À acquitter les droits exigibles pour le compte des souscripteurs ;",
    "2° À porter sur les bulletins de souscription la formule visée à l'article 405 I de l'annexe III au code général des impôts ;",
    "3° À verser les droits au service des impôts compétent pour accorder l'autorisation dans les vingt jours suivant la clôture des opérations de centralisation de l'émission et, en tout état de cause, avant la déclaration de souscription et de versement prévue à l'article L. 225-6 du code de commerce ;",
    "4° À mentionner dans cette déclaration de souscription et de versement le nombre de bulletins souscrits, le montant des droits de timbre versés au Trésor, le service des impôts auquel ces droits ont été payés ainsi que la date et le numéro de la recette ;",
    "5° À déposer, à l'appui du versement de l'impôt, un état succinct indiquant le montant du capital émis, la date de clôture des opérations de centralisation de l'émission, le nombre de bulletins souscrits et le montant de l'impôt exigible.",
    "Lorsque les bulletins sont émis à l'occasion de la constitution d'une société nouvelle, les conditions suivantes s'ajoutent :",
    "- L'engagement des fondateurs doit être assorti d'un engagement solidaire d'un établissement de crédit ou du notaire appelé à recevoir la déclaration de souscription et de versement ;",
    "- La formule d'engagement doit désigner le service des impôts où les droits seront versés, en principe celui du futur siège social. Les droits doivent, en tout état de cause, être acquittés dans les six mois du dépôt des statuts au greffe.",
],
    "Réécriture à droit constant : la société est désignée comme auteur de la demande et des cinq engagements ; les conditions supplémentaires propres à la constitution d'une société sont rendues explicites. Les subdivisions 1° à 5° et les deux conditions finales restent à leur place. Aucune réforme de fond n'est applicable à cet article.",
    "Les délais de vingt jours, le paiement avant la déclaration et le délai maximal de six mois restent cumulativement applicables dans leurs champs respectifs. Les 3° et 4° sont conservés à leur emplacement car l'article 93 H quater les vise. Le contenu de l'article 405 I de l'annexe III a été vérifié dans le corpus public local : il prévoit la formule de paiement sur état. Le renvoi à L. 225-6 du code de commerce est conservé ; ce texte n'a pas été vérifié dans le corpus fourni. Aucun allègement des pièces ni des engagements solidaires n'est déduit de l'objectif général de simplification.")

add('93 H quater', [
    "Lorsque l'établissement de crédit chargé de centraliser l'émission présente la demande, il doit l'appuyer de toutes justifications utiles quant à la qualité des pouvoirs du signataire. Il doit en outre s'engager expressément :",
    "1° À tenir un registre spécial indiquant, pour chaque émission qu'il centralise :",
    "a. Le numéro d'ordre spécialement affecté à l'émission dans le registre, selon une série ininterrompue à partir de la date de l'autorisation ;",
    "b. Le nom ou la raison sociale et le siège social de la société émettrice ;",
    "c. La date d'ouverture de la souscription ;",
    "d. Le montant du capital émis ;",
    "e. Le numéro du compte au crédit duquel figurent les sommes reçues des souscripteurs ;",
    "f. Le nombre de bulletins souscrits ;",
    "g. Le montant global des droits exigibles ;",
    "h. La date de clôture de la souscription ;",
    "i. La date du versement des droits au Trésor.",
    "2° À se porter fort, pour le compte des souscripteurs auxquels l'impôt incombe légalement, des droits et amendes de timbre exigibles sur les bulletins de souscription, et à acquitter ces droits et amendes sans conditions ni réserves.",
    "3° À effectuer le versement dans le délai prévu au 3° de l'article 93 H ter.",
    "4° À déposer, à l'appui de ce versement, un état en double exemplaire reproduisant les indications du registre spécial pour l'émission considérée. Cet état précise également le nom et l'adresse du notaire chargé de recevoir la déclaration de souscription et de versement.",
    "5° À porter ou à faire porter sur les bulletins de souscription la formule visée à l'article 405 I de l'annexe III au code général des impôts, complétée par la mention « N° (particulier à la souscription) du registre spécial tenu par (nom de l'établissement bancaire autorisé) ».",
    "6° À faire mentionner dans la déclaration de souscription et de versement les indications prévues au 4° de l'article 93 H ter.",
],
    "Réécriture à droit constant : les justifications de la demande sont séparées des engagements de l'établissement ; les informations du registre et de l'état sont présentées dans des phrases plus directes. Les six engagements, les lettres a à i et la qualification de porte-fort sont conservés. Aucune réforme de fond n'est introduite.",
    "Les renvois aux 3° et 4° de l'article 93 H ter restent opérants dans les propositions de ce lot. Le renvoi à 405 I de l'annexe III a été vérifié dans le corpus public local. La mention à apposer, la série ininterrompue à compter de l'autorisation, le double exemplaire et la prise en charge sans conditions ni réserves des droits et amendes sont conservés. La formulation source « qualité des pouvoirs du signataire » est maintenue sans lui substituer une nouvelle condition de capacité.")

add('93 H quater C', [
    "I. - Les redevables qui demandent à payer sur états le droit de timbre de dimension exigible sur les écrits autres que les bulletins de souscription d'actions doivent s'engager à tenir un registre, jour par jour. Ce registre indique, pour chaque acte :",
    "a. Le numéro d'ordre spécialement affecté à l'acte dans le registre, selon une série ininterrompue ;",
    "b. La date de l'acte ;",
    "c. La nature de l'acte ;",
    "d. Les noms et prénoms usuels des parties ;",
    "e. Pour les actes sous seings privés, le nombre d'originaux établis, à l'exclusion, le cas échéant, de ceux dispensés du droit de timbre de dimension ;",
    "f. Le nombre de feuillets du format de la demi-feuille de papier normal utilisés pour rédiger les minutes, brevets ou originaux soumis au droit de timbre ;",
    "g. Le montant de l'impôt correspondant ;",
    "h. Le nombre d'expéditions, de copies ou d'extraits soumis au droit de timbre ;",
    "i. Le nombre de feuillets du format de la demi-feuille de papier normal utilisés pour ces expéditions, copies ou extraits ;",
    "j. Le montant de l'impôt correspondant.",
    "Ce registre peut être fusionné avec les répertoires prévus par le code général des impôts pour certaines catégories de redevables. Il doit être présenté, au cours du mois de février de chaque année, au visa de l'agent chargé de la perception des droits de timbre.",
    "Le numéro d'ordre de chaque acte inscrit au registre doit être porté sur cet acte. Les colonnes correspondant aux indications mentionnées aux f, g, i et j doivent être totalisées chaque mois.",
    "II. - Devenu sans objet.",
],
    "Réécriture à droit constant : les obligations de tenue, de visa et de totalisation du registre sont formulées séparément ; les objets des renseignements sont explicités. Les I et II, les lettres a à j et les deux alinéas suivant l'énumération conservent leur ordre. Aucune réforme de fond ne concerne ce dispositif.",
    "Le visa en février, la tenue jour par jour, la numérotation ininterrompue, l'exclusion des originaux dispensés et le format de la demi-feuille sont maintenus. Les lettres f, g, i et j restent aux mêmes emplacements pour le renvoi de l'article 93 H quater D. La mention historique du II est conservée ; elle ne rend pas l'article entier éligible au statut retained_unchanged. Le champ résiduel du timbre de dimension appelle un contrôle distinct.")

add('93 H quater D', [
    "Le montant des droits est versé, à l'expiration de chaque mois, au comptable des impôts qui a accordé l'autorisation de paiement sur états. Ce versement intervient dans les vingt premiers jours du mois suivant.",
    "Le versement doit être accompagné d'un état indiquant :",
    "a) Les numéros du premier et du dernier acte inscrits au registre au cours du mois considéré ;",
    "b) Le nombre de ces actes ;",
    "c) Le total mensuel des colonnes correspondant aux indications mentionnées aux f, g, i et j du I de l'article 93 H quater C.",
    "Cet état doit être certifié conforme aux écritures et fourni en double exemplaire. Le premier exemplaire est rendu au déposant après apposition de l'acquit du comptable des impôts. Le service conserve le second exemplaire à l'appui de la recette des droits de timbre.",
],
    "Réécriture à droit constant : l'échéance mensuelle et le délai de versement sont énoncés dans deux phrases ; la destination de chaque exemplaire de l'état est précisée séparément. Les lettres a) à c) sont conservées. Aucune réforme de fond n'est appliquée.",
    "Le délai des vingt premiers jours du mois suivant et le comptable désigné par l'autorisation sont maintenus. Le renvoi au I et aux lettres f, g, i et j de l'article 93 H quater C a été contrôlé avec la proposition correspondante. La certification, le double exemplaire et l'acquit restent exigés.")

add('93 H quater E', [
    "Les redevables doivent conserver les registres prescrits par l'article 93 H quater C ainsi que tous les autres documents nécessaires à la vérification de l'état fourni à l'appui du versement des droits de timbre. Cette conservation s'effectue selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales.",
],
    "Réécriture à droit constant : les redevables sont désignés comme responsables de la conservation et le renvoi fixant ses modalités est isolé dans une seconde phrase. Aucune réforme de fond n'est introduite.",
    "Les deux catégories de documents et les renvois à l'article 93 H quater C et au I de L. 102 B du livre des procédures fiscales sont conservés. Le livre des procédures fiscales n'a pas été vérifié dans le corpus fourni ; aucune durée autonome de conservation n'est ajoutée.")

add('93 H quinquies', [
    "L'officier ministériel appose les timbres mobiles constatant le paiement du droit de timbre de dimension exigible sur les copies d'exploits en marge de la première page de l'original de l'exploit à conserver en minute.",
    "Pour tous les autres actes ou écrits, les timbres mobiles servant au paiement du droit de timbre de dimension sont collés sur la première page de chaque feuille.",
],
    "Réécriture à droit constant : l'officier ministériel devient le sujet de la première obligation ; la règle propre aux autres actes est introduite explicitement au second alinéa. Aucune réforme de fond ne vise ces modalités.",
    "La différence entre l'apposition en marge de la première page de l'original conservé en minute et le collage sur la première page de chaque feuille est maintenue. Les qualifications historiques d'officier ministériel et d'exploit sont conservées ; leur actualisation et le champ résiduel du droit ne sont pas présumés.")

add('121 KA', [
    "Par dérogation à toute disposition contraire, les régies de recettes des préfectures et sous-préfectures peuvent utiliser des machines à timbrer pour timbrer tous les documents donnant lieu à la perception de droits de timbre.",
    "Les passeports et les titres de voyages délivrés aux réfugiés ou apatrides peuvent notamment être timbrés par ce procédé lorsqu'ils sont soumis aux droits de timbre mentionnés au III de la section II du chapitre II du titre IV de la première partie du livre premier du code général des impôts.",
],
    "Réécriture à droit constant : les régies sont placées en sujet et la portée dérogatoire de l'autorisation est exprimée directement. L'exemple des passeports et titres de voyages et son renvoi sont conservés. Aucune réforme de fond n'est appliquée.",
    "La liste demeure illustrative et ne limite pas l'autorisation générale. Le renvoi hiérarchique au CGI est conservé intégralement. La note source a été lue : l'article 51 du décret n° 2024-610 du 26 juin 2024 fixe l'entrée en vigueur au 1er janvier 2025. Il s'agit d'une date historique du texte source, sans effet sur le calendrier des réformes proposées.")

add('121 KB', [
    "Toute machine destinée à timbrer les documents donnant lieu à la perception de droits de timbre dans les régies de recettes des préfectures et sous-préfectures doit avoir reçu l'agrément du directeur général des impôts.",
    "La demande d'agrément est adressée au directeur général des impôts, à Paris. Elle doit préciser que l'appareil est proposé exclusivement pour le recouvrement des droits de timbre perçus par les régies de recettes des préfectures et sous-préfectures.",
    "L'appareil doit être soumis à l'examen du conseil technique des postes et télécommunications. Le directeur général des impôts statue après avoir recueilli l'avis de ce conseil.",
    "La machine ne peut être mise en vente qu'après cet agrément.",
],
    "Réécriture à droit constant : les étapes de demande, d'examen et de décision sont formulées dans des phrases distinctes, sans modifier les quatre alinéas ni le préalable à la vente. Aucune réforme de fond n'est applicable.",
    "L'exclusivité de la destination de l'appareil, l'envoi à Paris, l'examen obligatoire et l'avis préalable sont maintenus. La source désigne le directeur général des impôts et le conseil technique des postes et télécommunications ; ces dénominations anciennes appellent une vérification des textes de succession de compétences, sans substitution silencieuse d'autorité.")

add('121 KC', [
    "Toutes les parties des machines mises en service doivent être conformes aux modèles agréés par l'administration. Les clichés produisant les empreintes de timbrage doivent être conformes aux types fixés par une instruction prise sous le double timbre du ministre de l'intérieur et du ministre de l'économie et des finances (1).",
    "Le constructeur dépose un spécimen complet de chaque type de machine, avec ses accessoires, au service des recherches et du contrôle technique des télécommunications, 3, avenue de la République à Issy-les-Moulineaux. Ce dépôt ne donne lieu à aucune rétribution.",
    "(1) Instruction interministérielle du 23 juillet 1969 (J.O. du 26).",
],
    "Réécriture à droit constant : les obligations de conformité de la machine et des clichés sont séparées ; le constructeur devient le sujet de l'obligation de dépôt. La référence historique figurant dans le corps de la source est conservée. Aucune réforme de fond n'est introduite.",
    "Le spécimen complet, les accessoires, l'adresse avec son numéro 3 et l'absence de rétribution sont maintenus. La référence au 23 juillet 1969 et à sa publication au J.O. du 26 est historique. Le service et l'adresse anciens nécessitent un contrôle de leur actualité ; aucune relocalisation ni nouvelle autorité n'est inventée. Cette instruction reste celle visée par les articles 121 KF et 121 KI du lot.")

add('121 KD', [
    "Pendant la fabrication des machines, l'administration des postes et télécommunications fait procéder à toutes les vérifications et à tous les essais qu'elle juge utiles. Ces vérifications et essais visent notamment à s'assurer de la qualité des métaux employés pour construire les divers organes de la machine (cémentation, trempe, etc.).",
],
    "Réécriture à droit constant : le futur est remplacé par le présent normatif et la finalité des contrôles est exprimée dans une seconde phrase, au sein du même alinéa. Le pouvoir d'appréciation de l'administration est conservé. Aucune réforme de fond n'est appliquée.",
    "Les contrôles en cours de fabrication et les exemples de cémentation et de trempe sont maintenus. La source conserve la dénomination ancienne de l'administration des postes et télécommunications ; l'autorité qui lui aurait succédé doit être vérifiée par les textes de compétence, sans correction implicite.")

add('121 KE', [
    "Avant toute mise en service, chaque machine doit être présentée au service des recherches et du contrôle technique des télécommunications. Ce service la soumet individuellement à des essais, à des épreuves et à un poinçonnement. Un poinçon millésimé est apposé sur chaque machine pour attester ce contrôle et autoriser sa mise en service dans un délai de deux ans. Après vérification et poinçonnement, le service délivre pour chaque machine un bulletin de contrôle indiquant que les compteurs ont été ramenés à zéro.",
],
    "Réécriture à droit constant : la présentation préalable, le contrôle individuel, son attestation et la délivrance du bulletin sont distingués en quatre phrases dans le même alinéa. Aucune réforme de fond n'est introduite.",
    "Le délai de deux ans est conservé comme délai de mise en service et non comme durée maximale d'utilisation. La source ne précise pas expressément son point de départ ; aucun point de départ nouveau n'est ajouté. Le millésime du poinçon et l'indication de remise à zéro restent exigés. Le renvoi au bulletin à l'article 121 KG reste opérant ; le contrôle de mise à zéro prévu à l'article 121 KF est également maintenu. La dénomination historique du service est conservée pour contrôle.")

add('121 KF', [
    "Le préfet décide de toute installation de machine dans une régie de recettes de préfecture ou de sous-préfecture, après avis du ministère de l'intérieur. Avant l'installation, il notifie sa décision au directeur des services fiscaux du lieu d'utilisation en indiquant les éléments d'identification définis dans l'instruction interministérielle prévue à l'article 121 KC.",
    "L'installation ne peut avoir lieu qu'en présence du représentant de ce directeur. Ce représentant doit sceller le capot et s'assurer de la mise à zéro des compteurs de la machine. Le représentant du trésorier-payeur général arrête simultanément la comptabilité du régisseur.",
],
    "Réécriture à droit constant : le préfet et les deux représentants sont désignés comme sujets de leurs décisions et opérations ; les deux alinéas d'origine sont maintenus. Aucune réforme de fond ne concerne l'article.",
    "L'avis ministériel, la notification antérieure à l'installation, le renvoi à 121 KC, la présence du représentant, le scellement, la mise à zéro et l'arrêté simultané de la comptabilité sont conservés. La source utilise encore les titres de directeur des services fiscaux et de trésorier-payeur général : la coordination des compétences administratives appelle un contrôle distinct. La note source mentionne une modification en conséquence de l'article 1er du décret n° 88-199 du 29 février 1988 ; elle est historique et n'est pas une date d'entrée en vigueur d'une réforme future.")

add('121 KG', [
    "Le retrait d'une machine dont le fonctionnement est signalé comme défectueux et son remplacement ne peuvent être effectués qu'en présence d'un représentant du service des impôts. Ce représentant est seul compétent pour desceller la machine retirée et sceller la nouvelle machine. Après retrait et réparation, le poinçonnage est effectué par les agents techniques de l'administration des postes et télécommunications. Eux seuls sont qualifiés pour apprécier si les réparations indispensables ont été effectuées et pour délivrer le bulletin de contrôle visé à l'article 121 KE.",
],
    "Réécriture à droit constant : les opérations réservées au représentant fiscal et celles réservées aux agents techniques sont énoncées dans des phrases distinctes, sans déplacer l'alinéa. Les deux compétences exclusives sont préservées. Aucune réforme de fond n'est appliquée.",
    "Le renvoi au bulletin de l'article 121 KE est conservé et contrôlé avec sa proposition. La présence lors du retrait et du remplacement, le déscellement, le scellement et le poinçonnage après réparation demeurent distincts. Les dénominations administratives anciennes sont maintenues, sous réserve du contrôle des textes de succession de compétences.")

add('121 KH', [
    "Les règles applicables aux documents revêtus de timbres mobiles ou timbrés à l'extraordinaire s'appliquent également aux documents portant des empreintes de machines à timbrer.",
],
    "Réécriture à droit constant : la phrase désigne d'abord les règles de référence puis les documents auxquels elles s'étendent. L'assimilation juridique est intégralement conservée. Aucune réforme de fond n'est introduite.",
    "Les deux procédés de référence, timbres mobiles et timbrage à l'extraordinaire, sont maintenus. Aucune dispense ni nouvelle condition de validité n'est déduite de l'emploi d'une machine ; l'article 121 KI conserve la conséquence des empreintes non conformes.")

add('121 KI', [
    "Tout document qui porte une empreinte de timbrage non conforme aux types fixés par l'instruction interministérielle précitée est réputé non timbré.",
],
    "Réécriture à droit constant : le futur est remplacé par le présent normatif et la condition est exprimée par une proposition explicite. La conséquence juridique demeure identique. Aucune réforme de fond n'est applicable.",
    "L'instruction précitée correspond à celle mentionnée à l'article 121 KC ; ce rattachement a été contrôlé dans le lot. La fiction de document non timbré est conservée sans ajouter de régularisation, de sanction ni de délai.")

add('121 KJ', [
    "Après chaque arrêté mensuel de ses écritures comptables, chaque régisseur autorisé à employer une ou plusieurs machines doit adresser une fiche au service des impôts du lieu d'utilisation dans un délai de cinq jours à compter de la date de cet arrêté. Cette fiche indique, pour chacune des machines :",
    "1° La désignation de la régie de recettes ;",
    "2° Les éléments d'identification de la machine prévus par l'instruction interministérielle ;",
    "3° Le montant total des droits de timbre à verser à ce service pour les empreintes apposées avec cette machine depuis le précédent arrêté et, éventuellement, le montant par catégorie.",
],
    "Réécriture à droit constant : le déclenchement du délai et le contenu de la fiche sont formulés dans deux phrases ; l'objet du montant à déclarer est rendu plus lisible au 3°. Les trois subdivisions sont conservées. Aucune réforme de fond n'est introduite.",
    "Le délai de cinq jours court toujours à compter de la date de l'arrêté mensuel. La fiche comporte les renseignements pour chaque machine, y compris lorsque plusieurs sont autorisées. La période depuis le précédent arrêté et le caractère éventuel de la ventilation par catégorie sont conservés. Le renvoi à l'instruction interministérielle est maintenu.")

add('121 KK', [
    "Les régisseurs de recettes des préfectures et sous-préfectures doivent assister à toute installation ou à tout retrait de machines. Ils ne peuvent ni effectuer ni accepter que soient effectuées, sur une machine en service, des réparations ayant une répercussion sur le mécanisme des compteurs ou sur celui d'apposition des empreintes. Ils ne peuvent modifier, de quelque manière que ce soit, aucune partie du mécanisme ou des compteurs. Ils doivent signaler toute machine dont le fonctionnement est défectueux au constructeur et au service des impôts auquel elle est rattachée, en vue de son retrait.",
],
    "Réécriture à droit constant : les interdictions sont formulées avec une construction parallèle et le double destinataire du signalement est exprimé directement. Les quatre obligations et interdictions restent dans le même alinéa. Aucune réforme de fond ne concerne ce régime.",
    "La présence à l'installation comme au retrait, l'interdiction d'effectuer ou d'accepter certaines réparations et l'interdiction générale de modifier le mécanisme ou les compteurs sont conservées. Le signalement demeure adressé au constructeur et au service fiscal, en vue du retrait, en cohérence avec 121 KF et 121 KG.")

add('121 KL', [
    "Les agents des impôts et ceux du Trésor doivent pouvoir, sans avis préalable, inspecter les machines, relever les compteurs et consulter les bandes de contrôle. Toutes facilités doivent leur être données à ces fins.",
],
    "Réécriture à droit constant : les agents et les trois opérations de contrôle sont placés au début de la phrase ; l'obligation de leur donner toutes facilités est conservée expressément. Aucune réforme de fond n'est appliquée.",
    "L'absence d'avis préalable et les deux catégories d'agents sont maintenues, ainsi que l'inspection, le relevé et la consultation. La source ne désigne pas expressément le débiteur de l'obligation de facilitation ; aucun débiteur exclusif nouveau n'est inventé. Les appellations administratives restent celles de la source.")

add('121 KL bis', [
    "Les organismes qui délivrent à leurs clients des formules de chèques ne répondant pas aux caractéristiques de barrement d'avance et de non-transmissibilité par voie d'endossement mentionnées à l'article 85 de la loi n° 78-1239 du 29 décembre 1978, ou, s'il y a lieu, les organismes centralisateurs auxquels ils sont rattachés doivent déposer un état en double exemplaire au service des impôts dont ils relèvent, dans les quarante-cinq jours du trimestre suivant celui de cette délivrance. Cet état indique le nombre de formules de chèques soumises au droit de timbre et délivrées au cours du trimestre précédent ainsi que le total des droits exigibles.",
    "Le montant des droits doit être versé au service compétent lors du dépôt de cet état.",
    "L'un des exemplaires de l'état, certifié conforme aux écritures de l'organisme intéressé, est rendu au déposant après apposition de l'acquit du comptable des impôts. Le service conserve l'autre exemplaire à l'appui de la recette des droits de timbre.",
],
    "Réécriture à droit constant : le contenu de l'état est détaché de la longue phrase définissant les organismes et le délai ; le paiement et le sort des exemplaires sont énoncés directement. Les trois alinéas sont préservés. Aucune réforme de fond n'est introduite.",
    "Le délai de quarante-cinq jours du trimestre suivant la délivrance, la déclaration du trimestre précédent et le paiement au dépôt sont maintenus. Le double exemplaire, la certification et l'acquit restent prévus. Le renvoi à l'article 85 de la loi n° 78-1239 du 29 décembre 1978 est conservé, sans vérification externe de cette loi. L'obligation complémentaire d'identification de 121 KL ter reste coordonnée avec le même champ de formules.")

add('121 KL ter', [
    "Les organismes mentionnés à l'article 121 KL bis doivent relever l'identité des personnes auxquelles les formules ont été délivrées et les numéros de ces formules. Ils doivent conserver ces renseignements selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales.",
],
    "Réécriture à droit constant : les numéros sont rattachés explicitement aux formules et les organismes sont désignés comme responsables de la conservation. Aucune réforme de fond n'est appliquée.",
    "Les deux renseignements obligatoires et le renvoi à 121 KL bis sont conservés. Le renvoi au I de L. 102 B du livre des procédures fiscales est maintenu sans lui substituer une durée chiffrée ; le texte de ce livre n'a pas été vérifié dans le corpus fourni.")

add('121 KM', [
    "Les débitants de tabac et les distributeurs auxiliaires établis en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte perçoivent une remise uniforme égale à 5 % du prix de vente des timbres mobiles de toute nature qu'ils vendent.",
    "La remise est liquidée et payée à mesure que les débitants de tabac et les distributeurs auxiliaires établis en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte effectuent leurs versements auprès des comptables de la direction générale des finances publiques, à condition qu'elle atteigne au moins 15 €.",
    "Les débitants de tabac et les distributeurs auxiliaires établis en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte qui participent à l'encaissement des timbres dématérialisés perçoivent une remise uniforme de 6 % calculée sur le prix de vente de ces timbres.",
    "Les conditions de liquidation et de paiement de cette remise sont prévues par un protocole d'agrément conclu entre la direction générale des finances publiques et les débitants de tabac ou les distributeurs auxiliaires établis en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte.",
],
    "Réécriture à droit constant : le calcul des deux remises et leurs modalités de paiement sont formulés plus directement, en conservant les quatre alinéas et les désignations territoriales de chaque catégorie de bénéficiaires. Aucune réforme de fond ne vise les taux de remise de cet article.",
    "Les 5 % des timbres mobiles, le seuil de paiement d'au moins 15 €, les 6 % des timbres dématérialisés et le protocole d'agrément sont conservés. Le seuil de 15 € n'est pas étendu à la remise sur les timbres dématérialisés. La source ne précise pas par une formule distributive si le complément « établis en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte » qualifie les seuls distributeurs auxiliaires ou également les débitants de tabac : son rattachement est conservé sans arbitrer cette ambiguïté de champ. Aucun nouveau taux fiscal n'est créé.")

add('121 KM bis', [
    "Les comptables directs du Trésor peuvent vendre les timbres mobiles fiscaux de la série unique.",
],
    "Réécriture à droit constant : l'habilitation à vendre est exprimée par une permission directe, sans changer les bénéficiaires ni les timbres concernés. Aucune réforme de fond n'est introduite.",
    "L'habilitation reste limitée aux comptables directs du Trésor et aux timbres mobiles fiscaux de la série unique. La dénomination ancienne des comptables est conservée ; une éventuelle coordination de compétences nécessite son texte propre.")

add('121 KM ter', [
    "Les recettes des douanes et droits indirects peuvent vendre les timbres fiscaux suivants :",
    "a. Timbres mobiles de la série unique ;",
    "b. Timbres travailleurs étrangers ;",
    "c. (sans objet) ;",
    "d. Timbres-amendes.",
],
    "Réécriture à droit constant : l'habilitation à vendre est formulée directement, avec maintien intégral des quatre lettres et des catégories de timbres. Les intitulés techniques de la liste ne sont pas remplacés artificiellement. Aucune réforme de fond n'est appliquée.",
    "La lettre c reste sans objet à son emplacement ; les lettres suivantes ne sont pas renumérotées. Les catégories historiques de timbres et les recettes habilitées sont conservées pour contrôle de leur champ actuel. La mention sans objet ne constitue pas un emplacement explicitement « Réservé. » et ne justifie pas le statut retained_unchanged.")


source = json.loads(Path('source.json').read_text())
assert len(source) == len(drafts) == 24
assert {a['number'] for a in source} == set(drafts)
answer = []
for article in source:
    record = {key: article[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    record.update(drafts[article['number']])
    answer.append(record)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answer), 'articles')
