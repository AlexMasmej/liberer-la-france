import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('54-0 B', [
    "Les capsules représentatives de droits mentionnées au II de l'article 302 M du code général des impôts doivent respecter la description des marques fiscales donnée au 2° du II de l'article 164 AM.",
    "Pour l'application des articles 50-0 C à 50-0 F, 54-0 A à 54-0 BX et 164 AM à 164 AW, le terme « capsules » désigne les marques fiscales imprimées directement sur des capsules composées d'une jupe ou d'une coiffe et d'une tête. Il désigne aussi les marques fiscales imprimées en séries sur des feuilles métalliques ou en autres matières, ou à l'unité sur des vignettes ou des timbres. Ces marques sont destinées à être apposées sur les têtes ou les coiffes, ou directement sur les systèmes de fermeture des bouteilles et des récipients.",
],
    "Réécriture à droit constant : l'obligation de conformité est formulée directement et la définition des capsules est répartie en phrases distinguant les supports et les modes d'apposition. Aucune réforme de fond de policy.json ne vise ce régime.",
    "Les deux alinéas, les trois plages d'articles et les modes d'impression sont conservés. Le 2° du II de l'article 164 AM figure dans le corpus local. L'article 302 M du CGI en est absent : le renvoi à son II est maintenu, sans lui substituer une disposition supposée équivalente. La formulation source « sur les têtes ou des coiffes » présente une maladresse syntaxique ; la proposition conserve les deux emplacements, sans modifier les supports admis.")

add('54-0 C', [
    "Les capsules doivent porter les mentions suivantes :",
    "a) Le numéro d'agrément de la personne responsable de l'embouteillage du produit. Le directeur régional des douanes et droits indirects territorialement compétent délivre ce numéro. Celui-ci comprend le mot « Récoltant » ou « Non récoltant », encadré, à gauche, par le numéro du département de la personne agréée et, à droite, par un numéro d'ordre d'enregistrement de l'administration. Le mot « Récoltant » peut être remplacé par la lettre « R » ; le mot « Non récoltant » peut être remplacé par la lettre « N » ou « E ». Les récoltants dont les syndicats viticoles, les groupements professionnels, les caves coopératives et leurs unions embouteillant leur récolte pour leur compte ou pour leurs adhérents bénéficient du mot \" Récoltant \" ou de la lettre \" R \".",
    "b) La marque du fabricant des capsules.",
    "Les mentions prévues au a sont inscrites dans la couronne de la capsule décrite au 2° du II de l'article 164 AM. Le fabricant choisit d'inscrire la mention prévue au b sur la jupe, sur la coiffe ou dans cette couronne.",
    "Les indications prévues au a doivent correspondre à celles qui figurent soit sur les étiquettes apposées sur les bouteilles ou les récipients, soit sur les bouteilles ou les récipients eux-mêmes. Ces indications doivent être apposées avant la livraison à l'utilisateur.",
    "Lorsqu'un négociant est autorisé à embouteiller des boissons alcooliques pour le compte d'un ou de plusieurs autres entrepositaires agréés, l'embouteilleur doit apposer sur les bouteilles ou les récipients des étiquettes indiquant le nom et l'adresse de l'entrepositaire agréé pour le compte duquel l'embouteillage a été effectué.",
],
    "Réécriture à droit constant : la délivrance et la composition du numéro sont exposées en phrases distinctes ; l'emplacement des mentions et l'obligation d'étiquetage identifient leurs responsables. La phrase source défectueuse sur les récoltants est conservée expressément, tandis que les autres prescriptions sont réécrites. Aucune réforme de fond n'est appliquée.",
    "Les six alinéas, les lettres a et b, les équivalences R/N/E et le renvoi au 2° du II de l'article 164 AM sont conservés. La phrase commençant par « Les récoltants dont les syndicats viticoles » est syntaxiquement défectueuse dans la source : l'articulation entre récoltants, syndicats, groupements, caves et unions et le rattachement de « pour leur compte ou pour leurs adhérents » doivent être clarifiés. Cette phrase est reprise sans trancher les catégories bénéficiaires. Le contrôle du renvoi à 164 AM confirme la présence de la couronne dans le corpus local.")

add('54-0 D', [
    "Le numéro d'agrément du responsable de l'embouteillage, porté sur la couronne, ainsi que la marque fiscale, l'indication de la contenance et, le cas échéant, le titre alcoométrique volumique, portés au centre de la couronne, doivent figurer sur un fond de la couleur suivante :",
    "a) Vert (Pantone 340 C) pour les vins tranquilles ou mousseux à appellation d'origine contrôlée et pour les vins doux naturels à appellation d'origine contrôlée. La couronne doit porter le nom « Champagne » pour les vins mousseux à appellation d'origine contrôlée « Champagne », et la mention « VDN » pour les vins doux naturels à appellation d'origine contrôlée ;",
    "b) Bleu (Pantone 285 C) pour tous les autres vins, y compris les boissons fiscalement assimilées au vin. Pour ces dernières, la couronne doit porter la mention BFAV ;",
    "c) Orange (Pantone 021 C) pour les produits intermédiaires bénéficiant d'une appellation d'origine contrôlée ;",
    "d) Gris (Pantone 402 C) pour les autres produits intermédiaires ;",
    "e) Les opérateurs peuvent remplacer les capsules vertes ou bleues par une capsule générique de couleur lie-de-vin (Pantone 209 C). Cette faculté est exclue pour les vins mousseux à appellation d'origine contrôlée « Champagne », les vins doux naturels à appellation d'origine contrôlée et les boissons fiscalement assimilées au vin, mentionnés aux a et b ;",
    "f) Jaune d'or (Pantone 1225 C) pour le cognac et l'armagnac ;",
    "g) Blanc (Pantone Gris 1C) pour les alcools.",
    "Le contraste entre la couleur du fond et celle des indications doit permettre de les lire aisément.",
],
    "Réécriture à droit constant : l'emplacement des indications, les mentions propres à certaines boissons et les exclusions de la capsule générique sont exprimés plus directement. Les sept lettres et tous les codes de couleur sont conservés. Aucune réforme de fond n'est appliquée.",
    "Contrôle des références 340 C, 285 C, 021 C, 402 C, 209 C, 1225 C et Gris 1C, des mentions Champagne, VDN et BFAV et des trois exclusions du e. Le libellé source « Blanc (Pantone Gris 1C) » est maintenu ; la concordance entre le nom de couleur et cette référence technique nécessite un contrôle, sans correction présumée. L'article 50-0 D et l'article 54-0 BX du corpus renvoient à ces caractéristiques : les lettres et l'ordre des alinéas normatifs sont préservés.")

add('54-0 E', [
    "Il est interdit d'utiliser les couleurs mentionnées à l'article 54-0 D pour les capsules et les supports qui portent un timbre d'une autre couleur.",
],
    "Réécriture à droit constant : la règle de couleur est formulée comme une interdiction explicite, avec le même renvoi. Aucune réforme de fond n'est appliquée.",
    "Le renvoi à l'article 54-0 D et la condition tenant à la couleur différente du timbre sont conservés. Les sauts de ligne sans contenu normatif sont remplacés par un seul paragraphe.")

add('54-0 G', [
    "Avant de fabriquer pour la première fois un type de capsule, le fabricant doit le faire agréer par l'administration des douanes et droits indirects. L'administration ne peut accorder cet agrément que si l'ouverture de la bouteille ou du récipient empêche de réutiliser la capsule. L'agrément bénéficie à tous les utilisateurs de ce type de capsule.",
],
    "Réécriture à droit constant : le moment de la demande, la condition d'agrément et sa portée sont exprimés dans trois phrases avec des sujets explicites. Aucune réforme de fond n'est appliquée.",
    "Le contrôle porte sur le caractère préalable à la première fabrication de chaque type, l'impossibilité de réutilisation après ouverture et l'effet de l'agrément pour tous les utilisateurs. Aucun agrément individuel supplémentaire n'est créé.")

add('54-0 H', [
    "Le fabricant doit effectuer sa déclaration de profession avant de fabriquer des marques fiscales, quel qu'en soit le support.",
    "Il joint à cette déclaration un état décrivant les locaux et précisant le type et le nombre des machines pouvant servir à fabriquer les marques fiscales ou les capsules.",
    "Le fabricant doit fournir une caution qui garantit le paiement des droits correspondant aux marques fiscales ou aux capsules produites.",
],
    "Réécriture à droit constant : les trois obligations du fabricant sont formulées directement et l'état joint à la déclaration est décrit par son contenu. Aucune réforme de fond n'est appliquée.",
    "Les trois alinéas normatifs restent distincts. Sont maintenus tous les supports, le type et le nombre des machines susceptibles de servir à la fabrication, ainsi que la caution couvrant les droits des marques ou capsules produites. Aucun montant de caution n'est ajouté.")

add('54-0 I', [
    "Pour effectuer ses contrôles, le service des douanes et droits indirects dispose d'un libre accès à toutes les parties de l'établissement.",
    "Les travaux relatifs aux marques fiscales doivent être réalisés exclusivement sur des machines équipées de compteurs agréés par l'administration des douanes et droits indirects en application de l'article 164 AP.",
],
    "Réécriture à droit constant : le droit d'accès et l'obligation d'utiliser des machines équipées de compteurs agréés sont exprimés directement. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas et le renvoi à 164 AP sont conservés. Dans le corpus local, l'article 164 AP, dans sa version du 30 juin 2025, traite de l'agrément des matériels mécaniques et logiciels ; il ne décrit pas expressément les compteurs. Cette articulation préexistante doit être contrôlée sans supprimer l'exigence propre au présent article.")

add('54-0 J', [
    "Le fabricant conserve, sous sa responsabilité, les clichés, matrices, cylindres et autres matériels servant à confectionner les marques fiscales dans un magasin spécial. Les conditions de sécurité de ce magasin doivent empêcher toute utilisation frauduleuse de ces matériels.",
],
    "Réécriture à droit constant : la responsabilité du fabricant, le lieu de conservation et l'exigence de sécurité sont exposés en deux phrases. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique conserve les clichés, matrices, cylindres et autres matériels, le magasin spécial et l'obligation d'empêcher l'utilisation frauduleuse. Aucun dispositif de sécurité particulier n'est imposé en supplément.")

add('54-0 L', [
    "Une fois confectionnées, les marques fiscales doivent être déposées dans un magasin spécial.",
    "Leurs mouvements sont enregistrés au fur et à mesure dans une comptabilité matières tenue sur place. Cette comptabilité comporte :",
    "a) En entrée, le nombre de marques fiscales déposées dans le magasin spécial et le nombre de capsules qu'elles représentent, ventilé par destinataire et par catégorie (volume net exprimé en centilitres, couleur, distinction, pour les vins, entre vin tranquille et vin mousseux et, le cas échéant, titre alcoométrique volumique...) ;",
    "b) En sortie, par destinataire et par catégorie, le nombre de marques fiscales utilisées et expédiées, ainsi que les références du document mentionné au I de l'article 302 M du code général des impôts.",
    "Le fabricant tient cette comptabilité matières et les marques fiscales qu'il détient à la disposition des agents des douanes et droits indirects pour leurs contrôles.",
    "Chaque mois, le fabricant établit la balance des entrées et des sorties de la comptabilité matières. Il la transmet au service des douanes et droits indirects dont il dépend au plus tard le cinquième jour du mois suivant.",
],
    "Réécriture à droit constant : le dépôt, l'enregistrement progressif des mouvements, les informations d'entrée et de sortie, puis les obligations de contrôle et de transmission sont formulés avec des sujets explicites. Aucune réforme de fond n'est appliquée.",
    "Les six alinéas et les lettres a et b sont conservés. Le nombre de marques déposées reste distinct du nombre de capsules représentées ; les catégories restent ouvertes comme dans la source. Le délai demeure le cinquième jour du mois suivant, sans alignement sur d'autres déclarations douanières. L'article 302 M est absent du corpus local : son I reste visé, mais le fondement documentaire exige une vérification de coordination.")

add('54-0 M', [
    "Les fabricants de capsules doivent conserver dans un magasin spécial les marques fiscales qu'ils reçoivent.",
    "Les mouvements de ces marques sont enregistrés au fur et à mesure dans une comptabilité matières tenue sur place. Cette comptabilité comporte :",
    "a) En entrée, le nombre de marques fiscales reçues dans le magasin spécial, y compris les retours, et le nombre de capsules qu'elles représentent, ventilé par destinataire et par catégorie (volume net exprimé en centilitres, couleur, distinction, pour les vins, entre vin tranquille et vin mousseux et, le cas échéant, titre alcoométrique volumique...) ;",
    "b) En sortie, par destinataire et par catégorie, le nombre de capsules expédiées, ainsi que les références du document mentionné au I de l'article 302 M du code général des impôts.",
    "Le fabricant tient cette comptabilité matières et les marques fiscales qu'il détient à la disposition des agents des douanes et droits indirects pour leurs contrôles.",
    "Chaque mois, le fabricant établit la balance des entrées et des sorties de la comptabilité matières. Il la transmet au service des douanes et droits indirects dont il dépend au plus tard le cinquième jour du mois suivant.",
    "Les obligations du présent article s'appliquent aussi à toute personne qui détient des capsules dans le cadre des livraisons destinées aux entrepositaires agréés et aux personnes habilitées définies à l'article 54-0 BW.",
],
    "Réécriture à droit constant : les opérations comptables et les responsabilités du détenteur sont précisées dans des phrases plus directes, en distinguant les marques reçues des capsules expédiées. Aucune réforme de fond n'est appliquée.",
    "Les sept alinéas, les lettres a et b, les retours, les catégories non exhaustives et le cinquième jour du mois suivant sont conservés. Le renvoi à 54-0 BW existe dans le corpus ; cet article habilite les syndicats viticoles ou groupements professionnels. L'extension aux autres détenteurs conserve la formulation et le champ de la source. L'article 302 M du CGI est absent du corpus local ; le renvoi à son I est maintenu et nécessite un contrôle de coordination.")

add('54-0 N', [
    "Les capsules, après leur fabrication, doivent être conservées dans un magasin spécial.",
    "Les inscriptions suivantes doivent être portées dans la comptabilité matières :",
    "a) Le nombre de capsules fabriquées, par destinataire et par catégorie, sur la base soit du duplicata du bon de sortie, soit, en cas de fabrication continue, d'une déclaration d'introduction ;",
    "b) Le nombre de capsules mises au rebut et détruites.",
    "Le fabricant doit informer, par tout moyen, le service des douanes et droits indirects dont il dépend des destructions de capsules, pour permettre au service d'en contrôler les conditions de réalisation.",
],
    "Réécriture à droit constant : les données à inscrire et le rôle du fabricant dans l'information du service sont exprimés directement. Les deux justificatifs comptables restent distingués selon les conditions de fabrication. Aucune réforme de fond n'est appliquée.",
    "Les cinq alinéas et les lettres a et b sont conservés. Le cas de fabrication continue reste attaché à la déclaration d'introduction. La mise au rebut et la destruction restent cumulées au b ; l'information du service demeure possible par tout moyen, sans nouveau délai ni autorisation préalable.")

add('54-0 O', [
    "Le fabricant de capsules doit inscrire dans sa comptabilité matières les quantités de capsules expédiées aux entrepositaires agréés utilisateurs et aux personnes habilitées mentionnées à l'article 54-0 BW, avec les références du document mentionné au I de l'article 302 M du code général des impôts. Il tient cette comptabilité à la disposition des agents des douanes et droits indirects lors de leurs contrôles. Il la transmet au service des douanes et droits indirects dont il dépend au plus tard le cinquième jour du mois suivant.",
],
    "Réécriture à droit constant : le fabricant est désigné comme responsable de l'inscription, de la mise à disposition et de la transmission de sa comptabilité. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique, les deux catégories de destinataires, la référence documentaire et l'échéance du cinquième jour du mois suivant sont maintenus. Le renvoi à 54-0 BW est présent dans le corpus local ; celui au I de l'article 302 M du CGI ne peut y être vérifié, cet article en étant absent. La source ne précise pas expressément la période à laquelle se rapporte « mois suivant » ; aucune période nouvelle n'est ajoutée.")

add('54-0 S', [
    "La fabrication des marques fiscales et des capsules ne peut commencer qu'après réception du bon de commande mentionné à l'article 54-0 AB. Leur expédition est réservée aux entrepositaires agréés et aux personnes habilitées mentionnés à l'article 54-0 BW.",
],
    "Réécriture à droit constant : le préalable à la fabrication et la restriction des destinataires sont exprimés séparément dans le même alinéa. Aucune réforme de fond n'est appliquée.",
    "Les renvois à 54-0 AB et à 54-0 BW sont conservés et leurs cibles figurent dans les sources ou le corpus local. La réception du bon reste antérieure à la fabrication et aucun autre destinataire n'est ajouté.")

add('54-0 T', [
    "La circulation des marques fiscales et des capsules doit être couverte par le document mentionné au I de l'article 302 M du code général des impôts.",
    "Le fabricant les expédie au destinataire dans des contenants qui en assurent la sécurité.",
    "Le document mentionné au premier alinéa doit indiquer le numéro d'ordre, le nombre et la catégorie des marques fiscales, ainsi que le nombre de capsules qu'elles représentent, ou le numéro d'ordre, le nombre et la catégorie des capsules contenues dans le ou les contenants. Il doit également indiquer le nom du fabricant et celui du destinataire.",
    "Les mêmes règles s'appliquent à la circulation des capsules retournées aux fournisseurs.",
],
    "Réécriture à droit constant : les obligations de circulation et de sécurité sont formulées directement et le contenu du document distingue les marques fiscales des capsules. Le régime des retours est maintenu. Aucune réforme de fond n'est appliquée.",
    "Les quatre alinéas et le renvoi interne au premier alinéa sont conservés. Les informations comprennent le numéro d'ordre, le nombre, la catégorie, le nombre de capsules représentées le cas échéant, et les deux noms. La rédaction conserve l'application à un ou plusieurs contenants et aux retours. L'article 302 M du CGI est absent du corpus local : le renvoi au I est conservé, avec un contrôle nécessaire du fondement documentaire.")

add('54-0 U', [
    "Les entrepositaires agréés doivent fournir une caution garantissant le paiement des droits correspondant aux capsules reçues, utilisées ou constatées manquantes lors des inventaires ou dans la comptabilité matières mentionnée à l'article 54-0 Y. Pour le vin, cette obligation s'applique sous réserve de l'article 54-0 BV.",
],
    "Réécriture à droit constant : la garantie exigée est exposée directement et la réserve applicable au vin est formulée dans une seconde phrase du même alinéa. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique, les trois situations couvertes par la caution et les deux modes de constatation des manquants sont conservés. Coordination vérifiée avec les articles 54-0 Y et 54-0 BV du lot : la réserve propre au vin n'est pas étendue aux produits intermédiaires ou aux alcools et ne supprime pas leur caution.")

add('54-0 V', [
    "La fourniture aux intéressés des capsules ou des feuilles métalliques ou en autres matières portant des marques fiscales est soumise aux conditions de l'article 54-0 AB.",
    "Les entrepositaires agréés peuvent toutefois être autorisés à imprimer eux-mêmes, sur les capsules qu'ils utilisent, la marque fiscale et les autres mentions prévues au 2° du II de l'article 164 AM. Cette impression doit être réalisée à l'aide de machines agréées par l'administration. Ces machines enregistrent, par tarif d'imposition, le volume et, le cas échéant, le titre alcoométrique volumique des boissons mises dans les bouteilles ou les récipients revêtus de capsules.",
],
    "Réécriture à droit constant : le régime ordinaire de fourniture et la faculté d'impression par l'entrepositaire sont distingués ; les fonctions exigées des machines sont exposées dans des phrases distinctes. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas, les supports métalliques ou autres, l'autorisation, l'agrément des machines et l'enregistrement par tarif sont conservés. Les renvois à 54-0 AB et au 2° du II de 164 AM ont des cibles identifiées dans le lot ou le corpus local. Le titre alcoométrique reste exigé seulement le cas échéant.")

add('54-0 X', [
    "Les entrepositaires agréés doivent utiliser des appareils qui assurent un sertissage ou une apposition efficace de la capsule. L'ouverture de la bouteille ou du récipient doit ainsi rendre impossible la réutilisation de cette capsule.",
],
    "Réécriture à droit constant : l'obligation est rattachée aux entrepositaires agréés et le résultat exigé à l'ouverture est énoncé dans une phrase distincte. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique conserve l'alternative entre sertissage et apposition efficace et l'exigence d'impossibilité de réemploi après ouverture. Le choix technique n'est pas restreint à un procédé particulier.")

add('54-0 Y', [
    "Les entrepositaires agréés sont comptables des droits représentés par les capsules qu'ils reçoivent.",
    "Ils doivent inscrire les mouvements des capsules qu'ils détiennent, reçoivent, utilisent et expédient avec les bouteilles et les récipients sur lesquels elles sont apposées, à la fois dans la comptabilité matières prévue aux articles 286 I et 286 J de l'annexe II au code général des impôts et dans la déclaration mensuelle mentionnée à ces articles.",
],
    "Réécriture à droit constant : la seconde phrase identifie directement l'inscription des mouvements dans les deux supports obligatoires. La qualité juridique de comptable des droits est conservée au premier alinéa, avec une relative explicitant les capsules reçues. Aucune réforme de fond n'est appliquée.",
    "Les deux alinéas et les quatre opérations sont maintenus. La qualification « sont comptables des droits » est conservée pour ne pas la réduire à une simple tenue matérielle des comptes. Les articles 286 I et 286 J de l'annexe II sont présents dans le corpus local et prévoient la comptabilité et les déclarations mensuelles. Leurs propres échéances ne sont pas transposées aux transmissions des fabricants des articles 54-0 L, M et O.")

add('54-0 Z', [
    "Aucune remise des droits représentés par les marques fiscales et les capsules perdues ou volées et détériorées ou détruites sans constatation du service des douanes et droits indirects ne peut être accordée.",
    "La restitution ou la remise des droits ne peut être autorisée que pour les bouteilles ou les récipients défectueux ou cassés. Pour l'obtenir, l'entrepositaire agréé doit présenter au service des douanes et droits indirects les bouteilles, goulots ou récipients revêtus de capsules intactes. Après vérification, les capsules correspondantes sont détruites.",
    "Les capsules représentatives de droits des bouteilles et des récipients de vin expédiés hors de France sont réputées détruites. La restitution ou la remise des droits est accordée après constatation, par le service des douanes et droits indirects, de la preuve de la sortie du produit de la Communauté européenne, ou après présentation d'un des documents mentionnés à l'article 302 M du code général des impôts, pris en charge par le destinataire.",
],
    "Réécriture à droit constant : les conditions de restitution ou de remise et les justificatifs sont exposés en phrases plus directes, en conservant la destruction après vérification et le cas du vin expédié hors de France. La coordination ambiguë du premier alinéa est maintenue pour ne pas étendre une remise. Aucune réforme de fond n'est appliquée.",
    "Les trois alinéas, la condition de capsules intactes, les bouteilles, goulots et récipients, ainsi que les deux voies justificatives du dernier alinéa sont conservés. Le premier alinéa coordonne « perdues ou volées et détériorées ou détruites sans constatation » : la portée de « et » et le rattachement de l'absence de constatation sont ambigus dans la source ; la proposition ne transforme pas cette phrase en autorisation de remise. La référence historique à la Communauté européenne est maintenue. L'article 302 M est absent du corpus local : le document et sa prise en charge par le destinataire restent exigés, sans remplacement de renvoi.")

add('54-0 AA', [
    "Les entrepositaires agréés et les personnes habilitées mentionnées à l'article 54-0 BW ne peuvent détenir dans leurs entrepôts que des capsules établies à leur nom ou au nom des personnes pour lesquelles ils réalisent l'embouteillage. Il est interdit de vendre, de céder ou d'échanger des capsules.",
],
    "Réécriture à droit constant : les noms admis sur les capsules détenues sont formulés positivement et les trois modes de transmission interdits sont exprimés par des verbes. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique, la restriction à la détention dans les entrepôts, les deux possibilités de désignation et les interdictions de vente, cession et échange sont conservés. Le renvoi à 54-0 BW est présent dans le corpus. La rédaction ne crée pas de dérogation pour les transferts gratuits.")

add('54-0 AB', [
    "La fabrication et la livraison des marques fiscales et des capsules représentatives de droits aux entrepositaires agréés et aux personnes habilitées mentionnées à l'article 54-0 BW nécessitent la présentation d'un bon de commande établi en deux exemplaires. Ce bon doit notamment indiquer :",
    "1° Le nom et l'adresse du fournisseur des marques fiscales ou des capsules ;",
    "2° Le nom, l'adresse et le numéro d'agrément du client ;",
    "3° Le nombre de marques fiscales ou de capsules commandées, par volume net exprimé en centilitres, par couleur des capsules, par type de vin (vin tranquille ou vin mousseux) pour les vins et, le cas échéant, par titre alcoométrique volumique.",
    "Le service local des douanes et droits indirects dont dépend l'entrepositaire agréé ou la personne habilitée mentionnée à l'article 54-0 BW doit viser et dater le bon de commande. Il remet un exemplaire à l'entrepositaire agréé ou à la personne habilitée, qui l'envoie à son fournisseur, et conserve l'autre exemplaire.",
    "Le bon de commande doit être apuré par une ou plusieurs livraisons dans les douze mois qui suivent son visa.",
],
    "Réécriture à droit constant : les conditions préalables à la fabrication et à la livraison, les renseignements du bon et le rôle du service sont formulés explicitement. Le délai d'apurement conserve son point de départ. Aucune réforme de fond n'est appliquée.",
    "Les six alinéas et les subdivisions 1°, 2° et 3° sont conservés. Le bon demeure en deux exemplaires, sa liste d'indications reste non exhaustive et son apurement doit intervenir en une ou plusieurs livraisons dans les douze mois suivant le visa. Le renvoi à 54-0 BW et les coordinations avec 54-0 S et 54-0 V sont maintenus.")

add('54-0 AC', [
    "Les fabricants, les entrepositaires agréés, les personnes habilitées mentionnées à l'article 54-0 BW et les débitants de boissons ne peuvent ni reprendre à leurs clients des capsules ayant déjà servi ni utiliser de telles capsules.",
],
    "Réécriture à droit constant : les deux comportements interdits sont exprimés dans une construction parallèle dont tous les destinataires sont nommés. Aucune réforme de fond n'est appliquée.",
    "Les quatre catégories de personnes, le renvoi à 54-0 BW et les deux interdictions, reprise auprès du client et utilisation de capsules déjà employées, sont maintenus dans l'alinéa unique.")

add('54-0 AG', [
    "L'apposition de capsules représentatives de droits est autorisée sur les bouteilles ou les récipients de boissons destinés à l'exportation ou à une livraison vers un autre État membre de la Communauté européenne.",
],
    "Réécriture à droit constant : la faculté d'apposition est formulée comme une autorisation explicite, sans changer les destinations admises. Aucune réforme de fond n'est appliquée.",
    "L'alinéa unique conserve l'exportation et la livraison vers un autre État membre comme deux destinations distinctes. La désignation historique « Communauté européenne » est maintenue ; aucune nouvelle obligation d'apposition n'est créée.")

add('54-0 BV', [
    "Les entrepositaires agréés qui ont la qualité de récoltant peuvent :",
    "a) Détenir en droits acquittés les capsules destinées à être apposées sur les bouteilles ou les récipients de vin, lorsque ces capsules sont commandées collectivement par l'intermédiaire des personnes habilitées mentionnées à l'article 54-0 BW ;",
    "b) Acquitter, à la première mise en circulation des bouteilles et des récipients de produits intermédiaires et d'alcools munis de capsules représentatives de droits, le droit de consommation ainsi que, le cas échéant, la cotisation sur les boissons alcooliques prévue à l'article L. 245-7 du code de la sécurité sociale et toute autre taxe exigible. Dans ce cas, ils doivent fournir une caution garantissant le paiement des droits correspondant aux capsules sorties des chais.",
],
    "Réécriture à droit constant : la faculté des récoltants est exposée en conservant deux lettres distinctes pour le vin et pour les produits intermédiaires et alcools. Le fait déclenchant le paiement et la caution sont énoncés directement. Aucune réforme de fond n'est appliquée.",
    "Les trois alinéas et les lettres a et b sont conservés. Le a reste limité au vin et aux commandes collectives via 54-0 BW. Le b conserve la première mise en circulation, toutes les taxes exigibles et la caution des capsules sorties des chais ; il reste coordonné avec la réserve de 54-0 U. L'article L. 245-7 du CSS existe dans le corpus local et vise les boissons d'une teneur en alcool supérieure à 18 % ; la réserve « le cas échéant » est maintenue. L'appellation « droit de consommation » demeure celle de la source : sa coordination avec la nomenclature de l'accise employée par l'article 164 AM du corpus nécessite un contrôle, sans substitution de fondement fiscal.")


def write_answer():
    assert len(sources) == len(drafts) == 24
    assert {a['number'] for a in sources} == set(drafts)
    output = []
    for source in sources:
        entry = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
        entry.update(drafts[source['number']])
        output.append(entry)
    Path('answer.json').write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    write_answer()
