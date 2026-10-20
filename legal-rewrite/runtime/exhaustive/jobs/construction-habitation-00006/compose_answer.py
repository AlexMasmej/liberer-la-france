import json
from pathlib import Path


rewrites = {
    'L186-1': {
        'paragraphs': [
            "Lorsqu'un ascenseur ou un composant de sécurité présente des risques pour la sécurité ou la santé des personnes et, le cas échéant, pour la sécurité des biens, le ministre chargé de la construction peut mettre en demeure l'installateur, le fabricant ou, à défaut, le responsable de la mise sur le marché de remédier à cette situation et de mettre l'ascenseur ou le composant concerné en conformité dans un délai déterminé. Il recueille au préalable les observations de ces personnes.",
            "Si l'opérateur n'a pas mis en œuvre les mesures prescrites à l'expiration du délai fixé par la mise en demeure, le ministre chargé de la construction peut, par arrêté :",
            "1° Restreindre les conditions d'utilisation de l'ascenseur ou du composant de sécurité pour ascenseurs ;",
            "2° Suspendre la mise sur le marché du produit pour une durée maximale d'un an ou l'interdire, y compris lorsque cette mise sur le marché est effectuée à titre gratuit ;",
            "3° Ordonner le retrait du produit en tous lieux.",
            "En cas d'urgence ou de danger grave, le ministre chargé de la construction peut, à tout moment, prendre lui-même ou faire prendre les mesures de prévention nécessaires pour mettre fin à cette situation.",
            "L'opérateur désigné dans l'arrêté prévu au deuxième alinéa supporte les frais de mise en œuvre de ces mesures.",
        ],
        'reason': "Réécriture à droit constant : les personnes susceptibles d'être mises en demeure et la consultation préalable sont explicitées ; les trois pouvoirs de police, le pouvoir d'urgence et la charge des frais restent distincts. Aucune réforme de fond de policy.json ne vise ce dispositif.",
        'review_notes': "Sept alinéas et numéros 1° à 3° conservés ; le renvoi au deuxième alinéa reste exact. Maintien de la suspension maximale d'un an, de la mise sur le marché gratuite et des deux motifs alternatifs d'intervention immédiate. La note relative à l'ordonnance 2020-71 du 29 janvier 2020 et au 1er juillet 2021 décrit l'entrée en vigueur historique ; elle ne fixe aucune date de réforme nouvelle.",
    },
    'L186-2': {
        'paragraphs': [
            "I. - Sans préjudice de l'article L. 186-1, le ministre chargé de la construction peut mettre l'opérateur en demeure de mettre fin, dans un délai déterminé, à la non-conformité d'un ascenseur ou d'un composant de sécurité pour ascenseurs. Il recueille au préalable les observations de l'opérateur. Il exerce ce pouvoir en cas d'illégalités, d'omissions, d'erreurs ou d'incomplétudes affectant les marquages, déclarations, identifications, informations ou documentations requis, dans l'un des cas suivants :",
            "1° Le marquage CE a été apposé en méconnaissance de l'article 30 du règlement (CE) n° 765/2008 du Parlement européen et du Conseil du 9 juillet 2008 fixant les prescriptions relatives à l'accréditation et à la sécurité du marché pour la commercialisation des produits et abrogeant le règlement (CEE) n° 339/93 du Conseil, ou des dispositions réglementaires prises pour l'application de la section 1 du chapitre IV du titre III ;",
            "2° Le marquage CE n'a pas été apposé ;",
            "3° Le numéro d'identification de l'organisme notifié a été apposé en méconnaissance des dispositions réglementaires prises pour l'application de la section 1 du chapitre IV du titre III, ou n'a pas été apposé alors que ces dispositions l'exigeaient ;",
            "4° Aucune déclaration UE de conformité n'a été établie ;",
            "5° La déclaration UE de conformité a été établie de manière incorrecte ;",
            "6° La documentation technique mentionnée à l'annexe IV, parties A et B, et aux annexes VII, VIII et XI de la directive 2014/33/UE du Parlement et du Conseil du 26 février 2014 relative à l'harmonisation des législations des États membres concernant les ascenseurs et les composants de sécurité pour ascenseurs n'est pas disponible ou est incomplète ;",
            "7° Le nom, la raison sociale ou la marque déposée, ou l'adresse de l'installateur, du fabricant ou de l'importateur n'a pas été indiqué conformément aux dispositions réglementaires prises pour l'application de la section 1 du chapitre IV du titre III ;",
            "8° Les informations permettant d'identifier l'ascenseur ou le composant de sécurité pour ascenseurs n'ont pas été fournies conformément aux dispositions réglementaires prises pour l'application de la section 1 du chapitre IV du titre III ;",
            "9° Les documents prévus par les dispositions réglementaires prises pour l'application de la section 1 du chapitre IV du titre III n'accompagnent pas l'ascenseur ou le composant de sécurité pour ascenseurs, ou ne respectent pas les exigences applicables.",
            "II. - Si, à l'expiration du délai fixé par la mise en demeure, la mise en conformité n'est pas possible et que l'opérateur n'a pas pu mettre en œuvre les mesures prescrites, le ministre chargé de la construction peut, par arrêté :",
            "1° Ordonner que l'ascenseur ou le composant de sécurité pour ascenseurs soit utilisé à d'autres fins ;",
            "2° Ordonner que l'ascenseur ou le composant de sécurité pour ascenseurs soit réexpédié vers son pays d'origine ;",
            "3° Ordonner la destruction de l'ascenseur ou du composant de sécurité pour ascenseurs dans un délai déterminé.",
            "III. - L'opérateur responsable de la non-conformité supporte les frais de mise en œuvre de ces mesures.",
        ],
        'reason': "Réécriture à droit constant : l'ouverture du I sépare le pouvoir de mise en demeure, les observations préalables et les neuf cas de non-conformité documentaire. Le II exprime plus directement la condition d'impossibilité de mise en conformité, sans étendre les mesures aux autres cas. Aucune réforme de fond n'est appliquée.",
        'review_notes': "Maintien des I, II et III, des neuf cas du I, des trois mesures du II et de leur ordre. Références européennes, annexes et renvois réglementaires conservés. Le II demeure limité au cas où la mise en conformité est impossible ; le renvoi du 2° de L186-8 au II n'est pas déplacé. L'intitulé du règlement (CE) n° 765/2008 est reproduit avec la formule « sécurité du marché » fournie par la source : son exactitude bibliographique est à contrôler, sans correction silencieuse. La note d'entrée en vigueur au plus tard le 1er juillet 2021 reste historique.",
    },
    'L186-3': {
        'paragraphs': [
            "Tous les cinq ans, l'application des dispositions relatives à la sécurité des ascenseurs fait l'objet d'un bilan. Une évaluation est réalisée à partir de ce bilan et fait l'objet d'un compte rendu au Parlement.",
        ],
        'reason': "Réécriture à droit constant : la périodicité du bilan est placée en tête et la succession du bilan, de l'évaluation qui en découle et du compte rendu au Parlement est explicitée. Aucune autorité nouvelle n'est désignée et aucune réforme de fond n'est introduite.",
        'review_notes': "Périodicité de cinq ans et compte rendu de l'évaluation au Parlement conservés. La source ne désigne pas le responsable du bilan ou de l'évaluation ; la proposition ne crée pas cette attribution. La note de 2020 relative à une entrée en vigueur au plus tard le 1er juillet 2021 ne constitue pas une nouvelle échéance quinquennale.",
    },
    'L186-4': {
        'paragraphs': [
            "Les officiers et agents de police judiciaire sont habilités à rechercher et à constater les infractions prévues au présent chapitre et par les textes pris pour son application. Les fonctionnaires et agents publics commissionnés et assermentés à cet effet par le ministre chargé de la construction disposent de la même habilitation, dans les conditions prévues par décret en Conseil d'État.",
        ],
        'reason': "Réécriture à droit constant : deux phrases distinguent les officiers et agents de police judiciaire des fonctionnaires et agents publics spécialement habilités. Le commissionnement, l'assermentation et l'encadrement réglementaire sont conservés ; aucune réforme de fond n'est appliquée.",
        'review_notes': "Champ limité aux infractions du chapitre et de ses textes d'application. Les conditions spéciales de commissionnement et d'assermentation restent attachées aux fonctionnaires et agents publics concernés, sans les étendre aux officiers et agents de police judiciaire. Renvois à cet article dans L186-5 à L186-8 préservés. Note d'entrée en vigueur historique lue et non transformée en transition nouvelle.",
    },
    'L186-5': {
        'paragraphs': [
            "Pour rechercher et constater les infractions mentionnées à l'article L. 186-4, les agents mentionnés à cet article peuvent accéder, entre 8 heures et 20 heures, aux lieux utilisés exclusivement à des fins professionnelles par le fabricant ou par toute personne intervenant dans la mise sur le marché d'ascenseurs ou dans la mise à disposition sur le marché de composants de sécurité pour ascenseurs. Cet accès a lieu en présence de l'occupant ou de son représentant.",
            "Ces agents peuvent également accéder aux mêmes lieux en dehors de ces heures lorsqu'ils sont ouverts au public ou lorsque des activités de production, de fabrication, de conditionnement, de transport ou de commercialisation s'y déroulent.",
            "Lorsque ces lieux sont également à usage d'habitation, les contrôles ne peuvent avoir lieu qu'entre 8 heures et 20 heures. Si l'occupant s'y oppose, les agents doivent obtenir au préalable l'autorisation du juge des libertés et de la détention du tribunal de grande instance dans le ressort duquel les lieux sont situés.",
            "Le procureur de la République est informé à l'avance des opérations envisagées pour rechercher les infractions. Il peut s'y opposer.",
        ],
        'reason': "Réécriture à droit constant : les conditions d'accès sont séparées des catégories de lieux et la nécessité d'une autorisation préalable en cas d'opposition dans des locaux également habités est formulée explicitement. Aucune réforme de fond ne modifie les pouvoirs de contrôle ou leurs garanties.",
        'review_notes': "Quatre alinéas conservés. Plage de 8 heures à 20 heures, présence de l'occupant ou de son représentant, cinq catégories d'activités justifiant l'accès hors horaires et droit d'opposition du procureur préservés. La source désigne encore le « tribunal de grande instance » : dénomination maintenue, mais coordination de compétence et de dénomination avec le tribunal judiciaire à contrôler dans les textes d'organisation judiciaire. La note d'entrée en vigueur au plus tard le 1er juillet 2021 n'actualise pas cette dénomination.",
    },
    'L186-6': {
        'paragraphs': [
            "Pour accomplir leurs missions, les agents mentionnés à l'article L. 186-4 peuvent prélever des pièces ou des échantillons afin de réaliser des analyses ou des essais. Ils peuvent aussi exiger la communication de tout document nécessaire à ces missions.",
            "Lorsque des vérifications complémentaires sont nécessaires, ces agents peuvent consigner les ascenseurs ou les composants de sécurité pour ascenseurs susceptibles de faire l'objet des sanctions administratives prévues à l'article L. 186-1. Les biens consignés restent sous la garde de leur détenteur. Les agents habilités les identifient dans un procès-verbal ou un rapport.",
            "Le procureur de la République est immédiatement informé de la consignation. Celle-ci ne peut excéder quinze jours.",
            "Le président du tribunal de grande instance dans le ressort duquel les ascenseurs ou les composants de sécurité pour ascenseurs sont consignés, ou le magistrat qu'il délègue, peut proroger le délai de consignation par ordonnance motivée.",
            "Les agents habilités saisissent le magistrat sans formalité. Celui-ci statue dans les vingt-quatre heures, au vu de tous les éléments d'information de nature à justifier la mesure, par une ordonnance exécutoire à titre provisoire.",
            "L'ordonnance qui proroge la consignation est notifiée par tous moyens au détenteur des ascenseurs ou des composants de sécurité pour ascenseurs consignés.",
            "À tout moment, les agents qui ont procédé à la consignation, le procureur de la République, le président du tribunal de grande instance ou le magistrat qu'il délègue à cet effet peuvent ordonner la mainlevée de la mesure.",
        ],
        'reason': "Réécriture à droit constant : les pouvoirs de prélèvement et de communication sont distingués, puis chaque étape de la consignation est présentée avec son acteur, son délai et sa formalité. Aucune réforme de fond n'élargit la consignation ou la compétence de mainlevée.",
        'review_notes': "Sept alinéas conservés ; maintien des quinze jours, de la décision dans les vingt-quatre heures, de la motivation, de l'exécution provisoire et de la notification par tous moyens. Deux points préexistants sont signalés sans correction : les mentions du « tribunal de grande instance » appellent un contrôle de coordination avec le tribunal judiciaire ; L186-1 est qualifié ici de fondement de « sanctions administratives » alors qu'il décrit des pouvoirs de police de mise en conformité. Aucun plafond de prorogation absent de la source n'est ajouté. La note d'entrée en vigueur de 2020-2021 reste historique.",
    },
    'L186-7': {
        'paragraphs': [
            "Les infractions prévues au présent chapitre sont constatées au moyen de procès-verbaux. Ceux-ci font foi jusqu'à preuve contraire.",
            "Ces procès-verbaux sont adressés au procureur de la République dans les cinq jours suivant leur clôture. Dans le même délai, une copie est transmise au fabricant ou au responsable de la mise sur le marché ou de la mise à disposition sur le marché, ainsi qu'au ministre chargé de la construction.",
        ],
        'reason': "Réécriture à droit constant : la constatation par procès-verbal est distinguée de la force probante de cet acte ; les destinataires de l'original et de la copie sont ensuite présentés séparément. Aucune réforme de fond ne modifie le délai ou les transmissions.",
        'review_notes': "Deux alinéas conservés. Le délai de cinq jours court toujours à compter de la clôture et vaut aussi pour les copies. Maintien de la preuve contraire et de l'alternative entre fabricant et responsable de la mise sur le marché ou de la mise à disposition sur le marché, avec transmission au ministre. Note d'entrée en vigueur historique intégralement prise en compte.",
    },
    'L186-8': {
        'paragraphs': [
            "Chacun des faits suivants est puni d'une amende de 7 500 € :",
            "1° Mettre sur le marché ou mettre à disposition sur le marché un ascenseur ou un composant de sécurité pour ascenseurs sans la déclaration « UE » ou « CE » de conformité prévue à l'article L. 134-2 ;",
            "2° Mettre sur le marché ou mettre à disposition sur le marché un ascenseur ou un composant de sécurité pour ascenseurs en méconnaissance des prescriptions d'un arrêté du ministre chargé de la construction pris en application du II de l'article L. 186-2 ;",
            "3° Faire obstacle à l'exercice des fonctions des fonctionnaires et agents habilités en application de l'article L. 186-4.",
            "Un décret en Conseil d'État fixe les modalités d'application du présent article.",
        ],
        'reason': "Réécriture à droit constant : la peine commune est annoncée avec son montant, puis les trois comportements sanctionnés sont formulés directement à l'infinitif. Aucune réforme de fond ne modifie la peine ou les éléments des infractions.",
        'review_notes': "Cinq alinéas et numéros 1° à 3° conservés ; amende de 7 500 €, déclarations UE ou CE et renvois à L134-2, au II de L186-2 et à L186-4 maintenus. Le corpus local confirme la présence des deux déclarations dans L134-2. Le renvoi pénal au II de L186-2 n'est pas étendu à L186-1 ou au I de L186-2. La date de la note historique ne devient pas une date de réforme pénale.",
    },
    'L191-1': {
        'paragraphs': [
            "Le présent livre s'applique de plein droit en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, sous les réserves et dans les conditions définies au présent titre. Cette application s'entend également sous réserve des dispositions adoptées par ces collectivités dans les conditions prévues au troisième alinéa de l'article 73 de la Constitution.",
            "En Guyane et en Martinique, les références au département figurant dans le présent livre s'entendent de la collectivité territoriale.",
        ],
        'reason': "Réécriture à droit constant : l'application de plein droit et ses deux catégories de réserves sont énoncées séparément ; la règle de lecture propre à la Guyane et à la Martinique est formulée directement. Aucune réforme de fond n'est étendue à l'outre-mer par cet article.",
        'review_notes': "Deux alinéas et liste des cinq collectivités conservés. Renvoi précis au troisième alinéa de l'article 73 de la Constitution maintenu. La substitution territoriale du second alinéa reste limitée à la Guyane et à la Martinique. Note historique d'entrée en vigueur lue ; aucune nouvelle date n'est créée.",
    },
    'L192-1': {
        'paragraphs': [
            "Pour l'application de l'article L. 113-15 en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, les catégories de bâtiments et les zones dans lesquelles tout ou partie des obligations prévues aux articles L. 113-12 et L. 113-13 ne s'appliquent pas sont définies, au plus tard le 1er janvier 2022, par les programmations pluriannuelles de l'énergie mentionnées au I de l'article L. 141-5 du code de l'énergie. Ces précisions sont intégrées à ces programmations à l'initiative du Gouvernement ou du président de la collectivité, dans le cadre d'une procédure de révision simplifiée conforme au III de l'article L. 141-5 du même code et selon les modalités fixées par le décret mentionné à l'article L. 141-6 de ce code.",
        ],
        'reason': "Réécriture à droit constant : la substitution de mots est exprimée comme une règle territoriale complète, après vérification de L113-15 dans le corpus local. L'objet des précisions, le document qui les porte et la procédure d'intégration sont explicites. Aucune réforme de fond ni nouvelle échéance n'est introduite.",
        'review_notes': "Un seul alinéa conservé. Les cinq collectivités, le 1er janvier 2022, les initiatives alternatives du Gouvernement ou du président de la collectivité et les renvois au I et au III de L141-5 et à L141-6 du code de l'énergie sont maintenus. Le IV et le volet annexé cités dans les mots remplacés par la source sont précisément le régime général écarté pour ces territoires ; ils ne sont pas réintroduits dans la règle territoriale. L113-15 demeure le support du renvoi au b du paragraphe 6 de l'article 8 de la directive 2010/31/UE. L'échéance de 2022 et la note d'entrée en vigueur de 2021 sont historiques, sans report implicite.",
    },
    'L192-2': {
        'paragraphs': [
            "À Mayotte, pour la notification prévue au deuxième alinéa de l'article L. 126-7, les propriétaires et les titulaires de droits réels immobiliers sur les locaux sont identifiés d'après le livre foncier.",
        ],
        'reason': "Réécriture à droit constant : l'adaptation terminologique est transformée en règle complète d'identification des destinataires de la notification, après lecture de L126-7 dans le corpus local. Aucune réforme de fond ne modifie la notification ou le contrôle des équipements.",
        'review_notes': "L'adaptation du fichier immobilier au livre foncier reste limitée à Mayotte et au deuxième alinéa de L126-7. Les règles de notification au gérant ou au syndicat des copropriétaires contenues dans cet alinéa ne sont pas écartées. Le corpus présente L126-7 dans une version entrée en vigueur le 1er janvier 2023 ; la note historique propre à L192-2, relative au 1er juillet 2021, n'est pas utilisée pour modifier cette chronologie.",
    },
    'L192-3': {
        'paragraphs': [
            "Un décret en Conseil d'État peut adapter les règles de construction prises pour l'application de l'article L. 131-2 en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte aux situations particulières de ces collectivités.",
        ],
        'reason': "Réécriture à droit constant : le décret en Conseil d'État devient le sujet de la phrase, ce qui rend explicite l'instrument d'adaptation tout en conservant son caractère facultatif. Aucune réforme de fond ne crée de dispense de sécurité.",
        'review_notes': "Les cinq collectivités et le renvoi à L131-2 sont conservés. Le corpus local confirme que ce renvoi concerne la résistance des structures aux termites et autres insectes à larves xylophages ; l'habilitation n'est pas étendue à toutes les règles de construction. La note d'entrée en vigueur de 2020-2021 n'est pas une nouvelle habilitation datée.",
    },
    'L192-4': {
        'paragraphs': [
            "À Mayotte, pour l'application de l'article L. 134-5, les propriétaires et les entreprises concernés doivent installer les dispositifs de sécurité et satisfaire aux exigences de sécurité au plus tard le 1er juillet 2031.",
        ],
        'reason': "Réécriture à droit constant : les destinataires, les deux obligations de sécurité et leur date limite sont énoncés directement. Le délai particulier de Mayotte est conservé ; aucune réforme de fond ne reporte ou n'avance cette échéance.",
        'review_notes': "Échéance du 1er juillet 2031 et renvoi à L134-5 conservés. Le corpus local confirme que L134-5 porte sur les ascenseurs ; la proposition ne transforme pas le délai en dispense des obligations d'entretien ou des autres contrôles. Le 1er juillet 2021 mentionné dans la note concerne l'entrée en vigueur historique de l'article et reste distinct de l'échéance de 2031.",
    },
    'L192-5': {
        'paragraphs': [
            "À Mayotte, le délai prévu au premier alinéa de l'article L. 164-2 court à compter du 29 août 2008, au lieu de la date de publication de la loi n° 2005-102 du 11 février 2005 pour l'égalité des droits et des chances, la participation et la citoyenneté des personnes handicapées.",
        ],
        'reason': "Réécriture à droit constant : l'adaptation par remplacement de mots est formulée comme une règle de point de départ du délai, après lecture de L164-2 dans le corpus local. Aucune réforme de fond ne rouvre ce délai historique.",
        'review_notes': "Maintien de Mayotte, du premier alinéa de L164-2, du 29 août 2008 et de la référence complète à la loi du 11 février 2005. La durée, fixée par décret et plafonnée à dix ans par L164-2, n'est pas modifiée. La règle ne change pas le second alinéa de L164-2. La note d'entrée en vigueur au plus tard le 1er juillet 2021 n'est ni le point de départ de ce délai ni une réforme nouvelle.",
    },
    'L192-6': {
        'paragraphs': [
            "À Mayotte, pour l'application du I de l'article L. 165-1, le respect des exigences d'accessibilité s'apprécie au 28 août 2018, au lieu du 31 décembre 2014.",
        ],
        'reason': "Réécriture à droit constant : la substitution de dates est exprimée comme la règle d'appréciation des exigences d'accessibilité déclenchant l'élaboration d'un agenda. Aucune réforme de fond ne modifie les personnes concernées ou le contenu de l'agenda.",
        'review_notes': "Les deux dates, le champ de Mayotte et le renvoi au I de L165-1 sont conservés. La lecture de ce dernier dans le corpus confirme que la date sert à constater le défaut de conformité entraînant l'élaboration de l'agenda, et ne constitue pas un délai nouveau de dépôt. Aucun changement n'est apporté au II. Note historique d'entrée en vigueur prise en compte sans actualisation des dates.",
    },
    'L192-7': {
        'paragraphs': [
            "À Mayotte, le projet d'agenda d'accessibilité programmée mentionné au premier alinéa du I de l'article L. 165-2 doit être déposé avant le 28 février 2019. Cette échéance tient lieu du délai de douze mois suivant la publication de l'ordonnance n° 2014-1090 du 26 septembre 2014.",
        ],
        'reason': "Réécriture à droit constant : la règle de dépôt applicable à Mayotte est énoncée directement, avec identification de l'agenda concerné et du délai général auquel elle déroge. Aucune réforme de fond ne prolonge ce délai historique.",
        'review_notes': "Un alinéa conservé, avec le premier alinéa du I de L165-2, l'ordonnance du 26 septembre 2014, le délai de douze mois et la date du 28 février 2019. Le mot « avant » est conservé, sans le convertir en « au plus tard ». Les possibilités de prorogation figurant au deuxième alinéa du I de L165-2 restent régies par cet article. La note d'entrée en vigueur de 2021 ne rouvre pas le dépôt.",
    },
    'L200-1': {
        'paragraphs': [
            "L'habitat participatif est une démarche citoyenne dans laquelle des personnes physiques peuvent s'associer, le cas échéant avec des personnes morales, pour participer à la définition et à la conception de leurs logements et des espaces destinés à un usage commun. Cette démarche leur permet de construire ou d'acquérir un ou plusieurs immeubles destinés à leur habitation et, le cas échéant, d'assurer ensuite la gestion des immeubles construits ou acquis.",
            "L'habitat participatif favorise la construction et la mise à disposition de logements ainsi que la mise en valeur d'espaces collectifs, dans une logique de partage et de solidarité entre habitants. Ces objectifs sont poursuivis en partenariat avec les différents acteurs qui contribuent à l'amélioration et à la réhabilitation du parc de logements existant, public ou privé, et dans le respect des politiques menées aux niveaux national et local.",
        ],
        'reason': "Réécriture à droit constant : la définition distingue la participation à la conception, la construction ou l'acquisition et la gestion éventuelle ; le second alinéa sépare les objectifs des conditions de partenariat et de respect des politiques publiques. Aucune réforme de fond de l'habitat participatif n'est prévue par policy.json.",
        'review_notes': "Deux alinéas conservés, avec la participation éventuelle de personnes morales, l'acquisition comme alternative à la construction, la pluralité possible d'immeubles et la gestion facultative. Les espaces communs, le parc existant public ou privé et les deux niveaux de politiques publiques sont maintenus. Cette définition ne crée ni dispense des règles de construction ni exemption des obligations de logement social. La source ne comporte pas de note historique.",
    },
    'L200-2': {
        'paragraphs': [
            "Les sociétés d'habitat participatif peuvent adopter la forme de coopératives d'habitants ou de sociétés d'attribution et d'autopromotion, définies respectivement aux chapitres Ier et II du présent titre. Elles peuvent également recourir aux autres formes juridiques prévues par la loi.",
        ],
        'reason': "Réécriture à droit constant : les deux formes spécialement régies par le titre sont annoncées d'abord, puis la possibilité de choisir une autre forme légale est exprimée dans une phrase autonome. Aucune réforme de fond ne rend ces deux formes exclusives.",
        'review_notes': "Maintien des coopératives d'habitants, des sociétés d'attribution et d'autopromotion et des renvois aux chapitres Ier et II. La faculté de choisir d'autres formes juridiques est conservée. Aucun agrément, régime fiscal ou privilège nouveau n'est attaché à cette faculté. La source ne contient pas de note historique.",
    },
    'L200-3': {
        'paragraphs': [
            "Les personnes qui souhaitent participer à cette démarche peuvent s'associer au sein de sociétés d'habitat participatif. Lorsque la société prend la forme d'une coopérative d'habitants ou d'une société d'attribution et d'autopromotion, les personnes morales qui y adhèrent ne peuvent détenir plus de 30 % du capital social ou des droits de vote.",
        ],
        'reason': "Réécriture à droit constant : la faculté de constituer une société est séparée de la condition de participation des personnes morales, limitée aux deux formes expressément visées. Aucune réforme de fond ne modifie le plafond de détention.",
        'review_notes': "Un seul alinéa conservé ; seuil de 30 % et formulation « capital social ou droits de vote » maintenus. Aucun plafond individuel nouveau n'est ajouté et cette restriction n'est pas étendue aux autres formes juridiques permises par L200-2. Absence de note historique dans la source.",
    },
    'L200-4': {
        'paragraphs': [
            "Lorsqu'un organisme d'habitations à loyer modéré, une société d'économie mixte mentionnée à l'article L. 481-1 ou un organisme agréé mentionné à l'article L. 365-2 ou L. 365-4 détient, par dérogation aux articles L. 201-2 et L. 202-2, un droit de jouissance sur un ou plusieurs logements, le nombre de ces logements est fixé proportionnellement à sa participation au capital de la société.",
            " ",
            "Les organismes et sociétés titulaires de ce droit de jouissance peuvent donner les logements concernés en location dans le respect des dispositions qui leur sont applicables.",
        ],
        'reason': "Réécriture à droit constant : le nombre proportionnel est explicitement rattaché aux logements et le droit de les donner en location est formulé comme une faculté des organismes et sociétés bénéficiaires. Aucune réforme de fond ne modifie les régimes locatifs ou les obligations de logement social.",
        'review_notes': "Les cinq renvois L201-2, L202-2, L481-1, L365-2 et L365-4 ont été vérifiés dans le corpus local et sont conservés. Maintien des trois catégories de bénéficiaires, de la proportion au capital et du respect de leurs dispositions propres. Le paragraphe vide de la source reste intercalé pour ne pas modifier inutilement la présentation des alinéas. Aucun droit de location libre dérogeant aux régimes de ces organismes n'est créé. Aucune note historique dans la source.",
    },
    'L200-5': {
        'paragraphs': [
            "Par dérogation à l'article 1857 du code civil, les associés des sociétés civiles régies par le présent titre ne répondent des dettes sociales envers les tiers que dans la limite de leurs apports.",
        ],
        'reason': "Réécriture à droit constant : le champ des sociétés civiles et la limite de responsabilité des associés sont exprimés dans une phrase plus directe. Aucune réforme de fond ne modifie la responsabilité envers les tiers.",
        'review_notes': "Renvoi à l'article 1857 du code civil, limitation aux sociétés du présent titre constituées sous forme civile, dettes sociales, tiers et plafond des apports conservés. La règle n'est pas étendue aux autres formes de sociétés. La source ne comporte pas de note historique.",
    },
    'L200-6': {
        'paragraphs': [
            "Lorsqu'une société décide régulièrement de modifier ses statuts pour les adapter au présent titre, cette modification ne crée pas de personne morale nouvelle, quelle que soit la forme de la société.",
        ],
        'reason': "Réécriture à droit constant : la décision régulière d'adaptation des statuts devient la condition explicite de la continuité de la personne morale. Aucune réforme de fond ne crée un régime général de transformation des sociétés.",
        'review_notes': "Maintien de la régularité de la décision, de sa finalité d'adaptation au présent titre et de l'application à toute forme de société. Aucun effet fiscal ou contractuel supplémentaire n'est déduit de la continuité de la personnalité morale. Aucune note historique dans la source.",
    },
    'L200-7': {
        'paragraphs': [
            "L'objet de chaque société d'habitat participatif est limité aux opérations de construction ou de gestion d'un même ensemble immobilier réalisées dans le cadre d'un même programme. Ce programme peut comporter une ou plusieurs tranches.",
        ],
        'reason': "Réécriture à droit constant : la limitation de l'objet social est distinguée de la possibilité de réaliser le programme en plusieurs tranches. Aucune réforme de fond ne permet de regrouper plusieurs programmes ou ensembles immobiliers.",
        'review_notes': "Un seul alinéa conservé. Maintien de l'alternative construction ou gestion, de l'unité de programme et d'ensemble immobilier et de la possibilité d'une ou plusieurs tranches. Cette limitation demeure à articuler avec les activités et services autorisés par L200-8, sans modifier cet équilibre. La source ne comporte pas de note historique.",
    },
    'L200-8': {
        'paragraphs': [
            "Dans les conditions fixées par décret en Conseil d'État, les sociétés d'habitat participatif peuvent développer des activités et offrir des services à leurs associés et, à titre accessoire, à des tiers non associés. Elles tiennent une comptabilité séparée pour ces opérations.",
        ],
        'reason': "Réécriture à droit constant : l'encadrement par décret est placé en tête pour couvrir l'ensemble des activités et services ; la tenue de la comptabilité séparée est mise explicitement à la charge des sociétés. Aucune réforme de fond n'élargit l'activité auprès de tiers.",
        'review_notes': "Maintien du caractère accessoire pour les tiers non associés, du décret en Conseil d'État et de la comptabilité séparée pour toutes les opérations visées. Aucun plafond chiffré ni régime des seules sociétés d'attribution et d'autopromotion n'est importé dans cette disposition générale. La source ne comporte pas de note historique.",
    },
}


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 24
assert {a['number'] for a in sources} == set(rewrites)
answer = []
for source in sources:
    rewrite = rewrites[source['number']]
    separator = '\n<br />\n' if source['number'].startswith(('L186-', 'L191-')) else '\n'
    answer.append({
        key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')
    } | {
        'proposed_xml': separator.join('<p>' + p + '</p>' for p in rewrite['paragraphs']),
        'reason': rewrite['reason'],
        'review_notes': rewrite['review_notes'],
        'status': 'rewrite_draft',
    })

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
