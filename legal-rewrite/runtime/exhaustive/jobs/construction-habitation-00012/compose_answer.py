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


add('L241-7', [
    "I.- Les personnes énumérées ci-dessous ne peuvent exercer habituellement, à quelque titre que ce soit, directement ou par personne interposée, pour leur compte ou pour celui d'autrui, les opérations mentionnées au décret n° 54-1123 du 10 novembre 1954. Ce décret est abrogé, à l'exception de ses dispositions relatives au conseil de surveillance, reproduites aux articles L. 214-6 à L. 214-9. Ces personnes ne peuvent pas davantage participer, en droit ou en fait, directement ou par personne interposée, à la fondation ou à la gestion des sociétés ou autres organismes mentionnés par ce décret :",
    "1. Les personnes auxquelles le chapitre VIII du titre II du livre Ier du code de commerce interdit d'exercer un commerce, ainsi que les personnes condamnées en application soit du décret du 14 juin 1938 sur les entreprises d'assurances, repris par le code des assurances (livre III, titre II, chapitre VIII et livre V, titre Ier, chapitre IV, section IV), soit des lois des 13 et 14 juin 1941 relatives à la réglementation et à l'organisation de la profession bancaire et des professions qui s'y rattachent (1), soit de la loi n° 52-332 du 24 mars 1952 relative aux entreprises de crédit différé, soit de l'article L. 241-6 ;",
    "2. Les personnes condamnées pour l'une des infractions suivantes : vol, abus de confiance, escroquerie, émission de chèques sans provision, soustraction commise par un dépositaire public, extorsion de fonds ou de valeurs, usure, atteinte au crédit de la nation ou recel de choses obtenues au moyen de l'une de ces infractions.",
    "L'interdiction s'applique également à toute personne condamnée pour tentative ou complicité de l'une des infractions mentionnées aux deux alinéas précédents.",
    "II.- Les infractions au I du présent article sont punies des peines prévues à l'article L. 241-6.",
    "III.- Le présent article ne fait pas obstacle à l'exécution des contrats en cours au 9 août 1957.",
],
    "Réécriture à droit constant : les deux interdictions et les personnes concernées sont exprimées directement ; la phrase sur l'abrogation partielle du décret est isolée dans le même alinéa. La tentative, la complicité, les peines par renvoi et la sauvegarde des contrats anciens sont conservées. Aucune réforme de fond n'est appliquée à ce régime.",
    "La note (1) de la source précise que les lois des 13 et 14 juin 1941 ont été abrogées par l'article 94 de la loi n° 84-46 du 24 janvier 1984. Cette référence historique et les autres références anciennes sont conservées ; leur actualisation exige un examen distinct du champ des interdictions, sans assimilation automatique à des infractions ou textes nouveaux. Le III reste limité aux contrats en cours au 9 août 1957. Les subdivisions I à III, les points 1 et 2 et l'emplacement de l'alinéa sur la tentative et la complicité sont maintenus."
)

add('L241-8', [
    "Toute personne tenue de conclure un contrat en application de l'article L. 231-1 ou de l'article L. 232-1 est punie de deux ans d'emprisonnement et de 300 000 euros d'amende si elle entreprend l'exécution des travaux sans avoir conclu un contrat écrit conforme aux articles L. 231-1, L. 231-2, L. 231-3, L. 231-9, L. 232-1 et L. 232-2, ou sans avoir obtenu la garantie de livraison définie à l'article L. 231-6.",
],
    "Réécriture à droit constant : le sujet et le fait sanctionné sont placés au présent, et la construction grammaticale du montant de l'amende est corrigée. Les deux manquements alternatifs, toutes les références et les deux peines sont maintenus. Aucune réforme de fond.",
    "Peines conservées : deux ans d'emprisonnement et 300 000 euros d'amende. La source écrit « une amende 300 000 euros » ; seul le mot de liaison manquant est rétabli. Le défaut de contrat conforme et le défaut de garantie demeurent deux hypothèses alternatives ; aucune faculté de prononcer une seule peine n'est ajoutée au texte de cet article."
)

add('L241-9', [
    "Toute personne chargée de l'une des opérations mentionnées à l'article L. 241-8 est punie de deux ans d'emprisonnement et de 18 000 euros d'amende, ou de l'une de ces deux peines seulement, si elle n'a pas conclu par écrit un contrat de sous-traitance avant l'exécution des travaux de chacun des lots de l'immeuble ou si elle a conclu un contrat qui ne comporte pas l'énonciation prévue à l'avant-dernier alinéa de l'article L. 231-13.",
],
    "Réécriture à droit constant : remplacement de la formulation au futur par une phrase explicite désignant la personne responsable et les deux manquements sanctionnés. Le moment de conclusion du contrat, les peines et leur alternative sont conservés. Aucune réforme de fond.",
    "Le renvoi à l'avant-dernier alinéa de L. 231-13 est maintenu : dans le corpus public consulté, cet alinéa est le g relatif aux garanties de paiement. Toute modification de la structure de L. 231-13 devra préserver ce ciblage. La note source indique que le II de l'article 57 de la loi n° 2003-721 prévoyait l'entrée en vigueur de son I au 1er juillet 2004, reportée au 1er novembre 2004 par la loi n° 2004-804 ; ces dates historiques ne fixent aucune entrée en vigueur future."
)

add('L242-1', [
    "Pour l'application des articles L. 212-10, L. 213-1 et L. 222-1, un immeuble collectif est considéré comme un immeuble à usage d'habitation ou à usage professionnel et d'habitation si au moins 10 % de sa superficie est affectée à ces usages. Un décret en Conseil d'Etat détermine comment les locaux annexes sont décomptés pour apprécier cette condition.",
],
    "Réécriture à droit constant : la condition de superficie et la fonction du décret sont formulées plus directement, sans modifier la qualification de l'immeuble ni le seuil. Aucune réforme de fond.",
    "Le seuil de 10 %, les deux usages et les trois articles d'application sont conservés. Le décompte des locaux annexes reste renvoyé à un décret en Conseil d'Etat ; aucune méthode de calcul nouvelle n'est introduite."
)

add('L242-2', [
    "Des décrets en Conseil d'Etat précisent, en tant que de besoin, les conditions et les modalités d'application des titres précédents, notamment les points suivants :",
    "Les modalités de règlement du prix au fur et à mesure de l'avancement des travaux mentionnés au b de l'article L. 213-8, au e du sixième alinéa de l'article L. 222-3 et à l'article L. 232-1 ;",
    "Pour l'application du e de l'article L. 231-2, le pourcentage maximal du prix total exigible à chaque stade de la construction, en fonction du pourcentage des dépenses normalement effectuées à ce stade. Ces modalités laissent au bénéfice du maître de l'ouvrage, jusqu'à son entrée dans les lieux, un solde de garantie qui ne peut excéder 5 % du prix total, par dérogation à la loi n° 71-584 du 16 juillet 1971 tendant à réglementer les retenues de garantie en matière de marchés de travaux définis par l'article 1779-3° du code civil. En cas de litige, le maître de l'ouvrage conserve la faculté de consigner tout ou partie de ce solde de garantie ;",
    "Pour l'application de l'antépénultième et de l'avant-dernier alinéas de l'article L. 231-2, les modalités d'information du maître de l'ouvrage sur l'achèvement et la bonne exécution de la fabrication des éléments préfabriqués, ainsi que les modalités de règlement du prix en fonction de l'avancement des travaux de construction et de l'achèvement de la fabrication de ces éléments ;",
    "Les conditions dans lesquelles l'exécution du contrat de promotion immobilière est réputée avoir commencé ;",
    "La nature et les modalités des garanties énoncées au e du sixième alinéa de l'article L. 222-3 ;",
    "Les conditions et les modalités d'application des articles L. 231-1 à L. 231-13.",
],
    "Réécriture à droit constant : les objets des décrets restent répartis dans les mêmes alinéas ; la disposition sur les appels de prix et le solde de garantie est décomposée en phrases plus courtes dans son alinéa. Le plafond, la consignation, la préfabrication et tous les renvois sont conservés. Aucune réforme de fond.",
    "Incohérence préexistante conservée : le sixième alinéa, e, de L. 222-3 porte, dans le corpus public, sur le financement et le règlement ; la garantie de bonne exécution figure au h. Le renvoi du sixième alinéa du présent article ne doit donc pas être corrigé sans coordination expresse. Le renvoi du deuxième alinéa au e correspond en revanche au règlement du prix. Les positions antépénultième et avant-dernière de L. 231-2 visent bien, dans le corpus, la préfabrication et son paiement. Le plafond du solde reste de 5 %, sans devenir un taux obligatoire. La note source maintient la transition de l'article 2 de l'ordonnance n° 2019-395 du 30 avril 2019 : application aux contrats conclus à compter du premier jour du troisième mois suivant la publication du décret prévu à L. 242-2 dans sa rédaction issue du 4° de l'article 1er de cette ordonnance, et au plus tard du premier jour du neuvième mois suivant celui de la publication de l'ordonnance au Journal officiel de la République française. Cette transition historique n'est pas remplacée par une date future."
)

add('L242-3', [
    "Les contrats conclus avant le 31 décembre 1972 restent soumis aux titres Ier et II du décret n° 54-1123 du 10 novembre 1954 ainsi qu'au deuxième alinéa de l'article 80 de la loi n° 53-80 du 7 février 1953.",
    "Les références au deuxième alinéa de cet article 80 sont réputées viser, en tant que de raison, les dispositions du chapitre III du titre Ier du présent livre.",
],
    "Réécriture à droit constant : les contrats auxquels l'ancien droit continue de s'appliquer sont placés en tête de phrase, puis la règle de correspondance des références est exprimée directement. Aucune réforme de fond ni extension aux contrats récents.",
    "La borne reste strictement antérieure au 31 décembre 1972. Les titres Ier et II du décret, le deuxième alinéa de l'article 80 et la réserve « en tant que de raison » sont conservés. La règle ne permet pas d'appliquer indistinctement les dispositions nouvelles aux contrats anciens."
)

add('L242-4', [
    "I.- Entrent en vigueur le 31 décembre 1972 les dispositions des chapitres Ier, II et III du titre Ier, des titres II et III et des articles L. 241-1 à L. 241-5 du présent livre.",
    "II.- Les dispositions des chapitres Ier et III du titre Ier du présent livre s'appliquent, dès leur entrée en vigueur, aux sociétés constituées avant cette date. Toutefois, les sociétés coopératives de construction ne sont pas tenues de se conformer aux articles L. 213-2 à L. 213-9 pour les programmes ayant fait l'objet, avant cette date, du dépôt d'une demande de permis de construire ou de la déclaration préalable prévue à l'ancien article L. 430-3 du code de l'urbanisme.",
],
    "Réécriture à droit constant : la date d'entrée en vigueur et l'application aux sociétés préexistantes sont rendues plus lisibles, tout en conservant l'exception applicable à certains programmes coopératifs. Aucune réforme de fond.",
    "La date historique du 31 décembre 1972 n'est pas une date de la réforme proposée. Le I vise les chapitres Ier, II et III du titre Ier ; le II ne vise que les chapitres Ier et III. L'exception reste limitée aux programmes ayant fait l'objet du dépôt antérieur d'une demande de permis ou de la déclaration préalable de l'ancien L. 430-3 du code de l'urbanisme, et aux articles L. 213-2 à L. 213-9."
)

add('L251-1', [
    "Le bail à construction est le bail par lequel le preneur s'engage, à titre principal, à édifier des constructions sur le terrain du bailleur et à les maintenir en bon état d'entretien pendant toute la durée du bail.",
    "Seules les personnes ayant le droit d'aliéner peuvent consentir un bail à construction, dans les mêmes conditions et formes que l'aliénation.",
    "La durée du bail est comprise entre dix-huit et quatre-vingt-dix-neuf ans. Le bail ne peut être prolongé par tacite reconduction.",
    "Toutefois, par dérogation au troisième alinéa, le bail prend fin à la date de la vente lorsque le bail prévoit une possibilité d'achat du terrain par le preneur dans le cadre d'une opération d'accession sociale à la propriété, dans les conditions de la section 1 du chapitre III du titre IV du livre IV du présent code, et que le preneur lève cette option.",
],
    "Réécriture à droit constant : définition directe du bail, désignation explicite des personnes pouvant le consentir et clarification de la fin anticipée par achat du terrain. L'obligation principale, les durées, l'absence de tacite reconduction et toutes les conditions de l'accession sociale sont maintenues. Aucune réforme de fond.",
    "Les quatre alinéas sont maintenus, notamment le troisième sur la durée de dix-huit à quatre-vingt-dix-neuf ans et le quatrième sur l'option d'achat, visés par d'autres articles du lot. La fin du bail à la vente reste subordonnée à l'opération d'accession sociale définie par le renvoi complet ; elle n'est pas étendue à toute vente du terrain. La réserve historique de L. 251-9 demeure à prendre en compte."
)

add('L251-2', [
    "Les parties fixent par convention leurs droits de propriété respectifs sur les constructions existantes et sur celles qui sont édifiées. En l'absence de convention, le bailleur devient propriétaire de ces constructions à la fin du bail et bénéficie des améliorations.",
],
    "Réécriture à droit constant : la liberté de répartition conventionnelle et la règle applicable à défaut de convention sont formulées dans deux phrases directes. Les constructions existantes et nouvelles demeurent toutes visées. Aucune réforme de fond.",
    "La propriété du bailleur en fin de bail reste une règle supplétive. Aucune indemnité, date de transfert différente ou restriction aux seules constructions nouvelles n'est ajoutée."
)

add('L251-3', [
    "Le preneur tient du bail à construction un droit réel immobilier.",
    "Ce droit, comme les constructions édifiées sur le terrain loué, peut être hypothéqué. Le droit peut être saisi selon les formes prescrites pour la saisie immobilière.",
    "Le preneur peut céder tout ou partie de ses droits ou en faire apport à une société. Les cessionnaires ou la société sont tenus des mêmes obligations que le cédant. Celui-ci en demeure garant jusqu'à l'achèvement de l'ensemble des constructions que le preneur s'est engagé à édifier en application de l'article L. 251-1.",
    "Le preneur peut consentir les servitudes passives indispensables à la réalisation des constructions prévues par le bail.",
],
    "Réécriture à droit constant : les effets du droit réel, la transmission des obligations et la durée de la garantie du cédant sont exposés dans des phrases distinctes. Les possibilités de cession, d'apport, d'hypothèque et de constitution de servitudes sont conservées. Aucune réforme de fond.",
    "Les quatre alinéas restent en place : L. 251-6 vise le quatrième, L. 251-8 les troisième et quatrième, et L. 251-9 le troisième. La garantie du cédant porte sur les obligations transmises jusqu'à l'achèvement de l'ensemble des constructions promises, sans ajout d'une solidarité nouvelle. Le terme « indispensables » continue de limiter les servitudes autorisées."
)

add('L251-4', [
    "Le preneur supporte toutes les charges, taxes et impôts relatifs aux constructions comme au terrain.",
    "Le preneur doit maintenir les constructions en bon état d'entretien et effectuer les réparations de toute nature. Il n'est pas tenu de reconstruire les bâtiments détruits par cas fortuit ou force majeure ni, pour les bâtiments qui existaient lors de la conclusion du bail, ceux détruits par un vice de construction antérieur au bail. Il répond de l'incendie des bâtiments existants comme de ceux qu'il a édifiés.",
    "Sauf stipulation contraire du bail, le preneur peut démolir les bâtiments existants en vue de les reconstruire.",
],
    "Réécriture à droit constant : les charges et les obligations matérielles du preneur sont énoncées expressément ; les deux causes de dispense de reconstruction sont distinguées. La responsabilité en cas d'incendie et la faculté supplétive de démolition restent dans leurs alinéas. Aucune réforme de fond.",
    "La dispense fondée sur un vice de construction antérieur ne concerne que les bâtiments existant à la conclusion du bail ; celle fondée sur le cas fortuit ou la force majeure n'est pas ainsi restreinte. La démolition reste orientée vers la reconstruction et soumise aux stipulations contraires du bail. Aucune dispense d'entretien ou de réparation n'est ajoutée."
)

add('L251-5', [
    "Le prix du bail peut être constitué, en tout ou partie, par la remise au bailleur d'immeubles, de fractions d'immeubles ou de titres donnant vocation à la propriété ou à la jouissance de ces immeubles, aux dates et dans les conditions convenues.",
    "Lorsqu'un loyer périodique payable en espèces est stipulé, il est affecté d'un coefficient révisable par périodes de trois ans calculées à partir de l'achèvement des travaux. La première révision intervient toutefois au plus tard à l'expiration des six premières années du bail.",
    "Les variations du coefficient sont proportionnelles à celles du revenu brut des immeubles. Le revenu de référence pour cette variation est celui de la première année civile suivant l'année d'achèvement des travaux.",
    "Le président du tribunal judiciaire connaît des contestations relatives à l'application des deux alinéas précédents.",
    "En cas de perte des bâtiments, le loyer demeure au taux atteint à la date de cette perte jusqu'à l'éventuelle reconstruction des bâtiments détruits.",
],
    "Réécriture à droit constant : les formes du prix et les règles de révision sont exprimées plus directement, avec maintien des périodes, du revenu de référence et du juge compétent. La règle en cas de perte des bâtiments est intégralement conservée. Aucune réforme de fond.",
    "Les cinq alinéas restent en place, en particulier le quatrième, visé comme avant-dernier alinéa par L. 251-8. Périodes de trois ans, première révision au plus tard à six ans et revenu de la première année civile suivant l'année d'achèvement sont maintenus. La note source rattache l'entrée en vigueur au 1er janvier 2020 à l'article 36 de l'ordonnance n° 2019-964 du 18 septembre 2019. Incohérence préexistante avec L. 251-9 : le quatrième alinéa actuel concerne le juge compétent et non les revenus du preneur limités par la loi ; aucune réécriture de fond de ce renvoi historique n'est effectuée."
)

add('L251-6', [
    "A l'expiration du bail, s'éteignent les servitudes passives autres que celles mentionnées au quatrième alinéa de l'article L. 251-3, les privilèges, les hypothèques et les autres charges nées du chef du preneur, notamment les baux et les titres d'occupation de toute nature portant sur les constructions. Les contrats de bail de locaux d'habitation sont toutefois exceptés de cette extinction.",
    "Toutefois, lorsque le bail prévoit une possibilité d'achat du terrain par le preneur dans le cadre d'une opération d'accession sociale à la propriété et que le preneur lève l'option conformément au quatrième alinéa de l'article L. 251-1, les privilèges et hypothèques du chef du preneur inscrits avant la levée de l'option ne s'éteignent pas à l'expiration du bail. Ils conservent leurs effets jusqu'à leur date d'extinction sur l'immeuble devenu la propriété du constituant. Ils s'étendent de plein droit au terrain et peuvent garantir les prêts consentis pour son acquisition.",
    "Si le bail prend fin par résiliation judiciaire ou amiable, les privilèges et hypothèques mentionnés au premier alinéa ne s'éteignent qu'à la date initialement convenue pour l'expiration du bail, à condition d'avoir été inscrits, selon le cas, avant la publication de la demande en justice tendant à cette résiliation ou avant la publication de l'acte ou de la convention qui la constate.",
],
    "Réécriture à droit constant : la règle d'extinction et ses exceptions sont séparées en phrases dans leurs trois alinéas d'origine. La survie des sûretés lors de l'achat du terrain et les conditions d'antériorité de leur inscription en cas de résiliation sont maintenues. Aucune réforme de fond.",
    "Maintien de l'exception des baux d'habitation et de celle des servitudes indispensables visées au quatrième alinéa de L. 251-3. Dans le deuxième alinéa, seuls les privilèges et hypothèques inscrits avant la levée d'option bénéficient de la règle prévue ; leur extension de plein droit au terrain et la possibilité de garantir son acquisition sont conservées. Dans le troisième alinéa, les deux événements de publication restent distincts, et l'extinction demeure fixée au terme initialement convenu. Aucune substitution terminologique de sûretés n'est réalisée sans coordination."
)

add('L251-7', [
    "Lorsque les constructions sont détruites par cas fortuit ou force majeure pendant la durée du bail, le juge peut, à la demande de l'une ou l'autre partie, prononcer la résiliation du bail. Il statue également sur les indemnités qui peuvent être dues.",
],
    "Réécriture à droit constant : le juge, la demande d'une partie et les causes de destruction sont désignés explicitement dans deux phrases. Le caractère facultatif de la résiliation et le règlement des indemnités sont conservés. Aucune réforme de fond.",
    "La destruction doit intervenir pendant le bail et résulter d'un cas fortuit ou de la force majeure. La résiliation n'est ni automatique ni unilatérale ; la formulation ne préjuge pas de l'existence ou du montant d'une indemnité."
)

add('L251-8', [
    "Sont d'ordre public les dispositions des troisième et quatrième alinéas de l'article L. 251-3 et celles de l'avant-dernier alinéa de l'article L. 251-5.",
],
    "Réécriture à droit constant : l'énoncé d'ordre public est placé en tête et la liaison entre les dispositions visées est simplifiée. Le périmètre exact des renvois est maintenu. Aucune réforme de fond.",
    "Les troisième et quatrième alinéas de L. 251-3 et l'avant-dernier, soit le quatrième, de L. 251-5 restent à leur emplacement dans les propositions du lot. Le présent article ne rend pas d'ordre public l'ensemble du chapitre."
)

add('L251-9', [
    "Les dispositions du troisième alinéa de l'article L. 251-1 et du troisième alinéa de l'article L. 251-3, dans leur rédaction issue des articles 47 et 48 de la loi n° 75-1328 du 31 décembre 1975, ne s'appliquent pas aux baux à construction conclus avant le 3 janvier 1976.",
    "Les dispositions du quatrième alinéa de l'article L. 251-5 relatives au cas où les revenus du preneur sont limités par des dispositions législatives s'appliquent aux baux en cours au 31 décembre 1977.",
],
    "Réécriture à droit constant : les alinéas et les baux concernés par chaque règle transitoire sont désignés directement. Les rédactions historiques et les deux dates d'application sont conservées. Aucune réforme de fond ni application rétroactive nouvelle.",
    "Incohérence préexistante : le quatrième alinéa de L. 251-5 fourni dans le lot traite de la compétence du président du tribunal judiciaire, sans règle sur les revenus du preneur limités par la loi. Le deuxième alinéa est conservé dans sa portée historique ; la rédaction ancienne qu'il vise doit être identifiée avant toute correction ou abrogation coordonnée. Le premier alinéa reste lié aux rédactions issues des articles 47 et 48 de la loi n° 75-1328, sans remplacement par une référence générale au droit actuel. Les bornes avant le 3 janvier 1976 et en cours au 31 décembre 1977 ne sont pas déplacées."
)

add('L252-1', [
    "Le bail à réhabilitation est un contrat soumis au présent chapitre. Par ce contrat, un organisme d'habitations à loyer modéré, une société d'économie mixte dont l'objet est de construire ou de donner à bail des logements, une collectivité territoriale, un organisme de foncier solidaire ou un organisme bénéficiant de l'agrément relatif à la maîtrise d'ouvrage prévu à l'article L. 365-2 s'engage à réaliser, dans un délai déterminé, des travaux d'amélioration sur l'immeuble du bailleur. Il s'engage également à maintenir cet immeuble en bon état d'entretien et de réparations de toute nature, en vue de le louer à usage d'habitation pendant la durée du bail.",
    "Le contrat précise la nature et les caractéristiques techniques des travaux ainsi que leur délai d'exécution.",
    "A la fin du bail, le bailleur bénéficie des améliorations réalisées sans devoir d'indemnisation.",
    "Seules les personnes ayant le droit d'aliéner peuvent consentir un bail à réhabilitation, dans les mêmes conditions et formes que l'aliénation. Ce bail est conclu pour une durée d'au moins douze ans et ne peut être prolongé par tacite reconduction.",
    "Le présent article s'applique aux immeubles soumis ou non au statut de la copropriété prévu par la loi n° 65-557 du 10 juillet 1965 fixant le statut de la copropriété des immeubles bâtis. Lorsque l'immeuble est soumis à ce statut, il peut s'appliquer à un ou plusieurs lots.",
],
    "Réécriture à droit constant : la définition du contrat et les engagements du preneur sont répartis en phrases plus courtes dans le premier alinéa ; les catégories de preneurs, le contenu du contrat, le sort des améliorations et la durée restent inchangés en substance. Aucune réforme de fond.",
    "Les cinq catégories de preneurs et la restriction d'objet propre aux sociétés d'économie mixte sont conservées, comme les cinq alinéas. Le délai déterminé des travaux et la durée minimale de douze ans du bail restent distincts. La voie de rénovation locative de vingt-quatre mois envisagée par policy.json ne réduit pas la durée de ce régime spécial. Elle exige une disposition distincte dans la loi n° 89-462 du 6 juillet 1989 organisant ses rapports avec la décence locative, le contrôle des travaux et la compensation des surcoûts énergétiques, ainsi que les textes d'application correspondants ; cet article ne crée pas ces mécanismes. La possibilité de viser un ou plusieurs lots de copropriété est maintenue."
)

add('L252-1-1', [
    "Lorsque le bail à réhabilitation porte sur un ou plusieurs lots d'un immeuble soumis au statut de la copropriété, le preneur est de droit le mandataire commun prévu au second alinéa de l'article 23 de la loi n° 65-557 du 10 juillet 1965 précitée, par dérogation à cet article. Il peut recevoir plus de trois délégations de vote des bailleurs, par dérogation au troisième alinéa du I de l'article 22 de cette loi.",
    "Pendant toute la durée du bail à réhabilitation, le preneur supporte seul l'ensemble des provisions prévues aux articles 14-1 et 14-2-1 de cette loi.",
    "Avant de voter sur les décisions relatives à des travaux de toute nature qui ne sont pas mis à sa charge par le contrat de bail à réhabilitation et dont la prise en charge n'est pas prévue dans ce bail ou dont le paiement ne lui incombera pas à titre définitif, le preneur, en sa qualité de mandataire commun, doit disposer d'un mandat exprès du bailleur.",
    "Le bail à réhabilitation précise la répartition des charges à la fin du bail, le sort des avances et provisions appelées pendant sa durée et celui des régularisations de charges intervenant après sa fin. Ces clauses ne sont pas opposables au syndicat des copropriétaires.",
],
    "Réécriture à droit constant : les dérogations de représentation, la charge des provisions, le mandat préalable et les clauses de fin de bail sont exprimés avec des sujets explicites. Les conditions cumulatives ou alternatives de l'alinéa relatif aux travaux sont conservées dans leur ordre. Aucune réforme de fond.",
    "Les quatre alinéas et les renvois aux articles 23, 22, 14-1 et 14-2-1 de la loi n° 65-557 sont maintenus. La possibilité de plus de trois délégations reste limitée aux délégations des bailleurs. Le troisième alinéa conserve l'articulation préexistante des travaux non mis à charge, de la prise en charge non prévue et du paiement non définitif, sans la réduire à un seul critère ; toute explicitation de leur articulation logique appelle un contrôle distinct. Les clauses de répartition restent inopposables au syndicat. La note source renvoie aux conditions et dates d'entrée en vigueur du VI de l'article 171 de la loi n° 2021-1104 du 22 août 2021 ; ce renvoi transitoire reste à appliquer, sans nouvelle date de réforme déduite de la date de la loi."
)

add('L252-2', [
    "Le preneur dispose d'un droit réel immobilier, qui peut être hypothéqué et saisi selon les formes prescrites pour la saisie immobilière.",
    "Ce droit peut être cédé malgré toute convention contraire. La cession exige l'accord du bailleur et ne peut bénéficier qu'à l'un des organismes mentionnés au premier alinéa de l'article L. 252-1. Elle doit porter sur la totalité de l'immeuble loué. Le cédant reste garant de l'exécution du bail par le cessionnaire.",
],
    "Réécriture à droit constant : la cessibilité du droit et les conditions de la cession sont formulées séparément, sans modifier les sûretés possibles ni la garantie du cédant. Aucune réforme de fond.",
    "Maintien des deux alinéas et du renvoi au premier alinéa de L. 252-1. L'accord du bailleur, la qualité du cessionnaire et la cession de la totalité de l'immeuble loué restent exigés ensemble ; la faculté de céder n'autorise pas une cession partielle. Le terme de la garantie du cédant n'est pas raccourci par analogie avec le bail à construction."
)

add('L252-3', [
    "Le bail à réhabilitation ne prend effet que si le preneur a conclu une convention prévue à l'article L. 831-1 dont la date d'expiration est la même que celle du bail.",
    "Les occupants présents lors de la conclusion du bail à réhabilitation relèvent des articles L. 353-7 et L. 353-16 du présent code.",
],
    "Réécriture à droit constant : la condition de prise d'effet du bail et la protection par renvoi des occupants déjà présents sont énoncées directement. L'identité des dates d'expiration et les deux articles applicables sont conservés. Aucune réforme de fond.",
    "La condition porte sur une convention de l'article L. 831-1 conclue par le preneur et expirant exactement avec le bail, sans simple exigence de durée minimale. Les articles L. 353-7 et L. 353-16 restent applicables aux occupants présents à la conclusion du bail ; aucun élargissement ou retrait de cette catégorie n'est opéré."
)

add('L252-4', [
    "I.- Un an avant l'expiration du bail à réhabilitation, le preneur rappelle au bailleur et au locataire les dispositions des II et III du présent article.",
    "II.- Six mois avant l'expiration du bail à réhabilitation, le bailleur occupant peut informer le preneur de son intention de prolonger ce bail, par lettre recommandée avec demande d'avis de réception.",
    "Dans le même délai, le bailleur non occupant peut proposer au locataire un nouveau bail prenant effet au terme du bail à réhabilitation.",
    "La notification doit reproduire les dispositions du présent II et de l'article L. 252-5.",
    "III.- Trois mois avant l'extinction du bail à réhabilitation, le preneur propose au locataire qui n'a pas conclu de nouveau bail avec le bailleur et qui remplit les conditions de ressources fixées par décret la location d'un logement correspondant aux besoins et aux possibilités de ce locataire.",
    "Le manquement du preneur à cette obligation ne peut être opposé au bailleur.",
    "Au terme du bail à réhabilitation, le preneur doit restituer au bailleur l'immeuble libre de location et d'occupation.",
],
    "Réécriture à droit constant : les qualités de bailleur occupant ou non occupant sont exprimées directement, les obligations de notification et de restitution sont rendues explicites et l'offre de relogement est reformulée. Les subdivisions, les sept alinéas et tous les délais sont maintenus. Aucune réforme de fond.",
    "Le I, déjà clair, est conservé dans l'article réécrit afin de préserver le rappel exact des II et III. Les échéances restent un an, six mois et trois mois avant le terme, sans ajout de la locution « au moins ». Au III, les besoins et possibilités sont ceux du locataire ; l'offre reste subordonnée à l'absence de nouveau bail et aux ressources réglementaires. Le II ne donne pas au bailleur un droit unilatéral à la prolongation : il permet de notifier son intention. L'inopposabilité du manquement et la restitution libre d'occupation demeurent, sans autoriser d'expulsion privée."
)

add('L252-5', [
    "A l'expiration du bail à réhabilitation, le locataire est déchu de tout titre d'occupation sur le logement s'il n'a ni conclu le contrat de location proposé par le bailleur ni accepté l'offre de relogement faite par le preneur.",
],
    "Réécriture à droit constant : la date de perte du titre est placée au début et les deux conditions sont formulées à la suite de la conséquence. Leur caractère cumulatif reste inchangé. Aucune réforme de fond.",
    "La perte de tout titre suppose à la fois l'absence de conclusion du contrat proposé et l'absence d'acceptation de l'offre de relogement. Elle intervient à l'expiration du bail à réhabilitation. La reproduction de cet article dans la notification prévue par L. 252-4 reste requise ; aucune procédure d'expulsion privée n'est créée."
)

add('L252-6', [
    "Les dispositions du présent chapitre sont d'ordre public.",
],
    "Réécriture à droit constant, limitée par la brièveté de la règle : le sujet est explicité comme étant l'ensemble des dispositions du chapitre. La portée d'ordre public reste intégrale. Aucune réforme de fond.",
    "Cette règle vise le chapitre II relatif au bail à réhabilitation, sans extension aux autres chapitres du titre V. La reformulation ne crée aucune faculté de dérogation conventionnelle."
)

add('L253-1', [
    "Une convention peut établir l'usufruit d'un logement ou d'un ensemble de logements au profit d'une personne morale, pour une durée d'au moins quinze années, en vue de la location de ce logement ou de cet ensemble de logements.",
],
    "Réécriture à droit constant : la convention est placée en sujet et la durée minimale est exprimée directement. Le bénéficiaire personne morale, l'objet de l'usufruit et la finalité locative sont conservés. Aucune réforme de fond.",
    "La durée minimale reste de quinze années et l'usufruit conventionnel reste constitué au profit d'une personne morale. Cette durée n'est alignée ni sur le bail à construction ni sur le bail à réhabilitation. Aucune règle nouvelle de renouvellement ou de terme n'est introduite."
)


assert len(sources) == len(drafts) == 24
assert {r['number'] for r in sources} == set(drafts)
answer = []
for source in sources:
    row = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
    row.update(drafts[source['number']])
    answer.append(row)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
