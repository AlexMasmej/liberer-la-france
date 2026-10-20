import json
from pathlib import Path


def paragraphs(*items):
    return "\n".join("<p>" + item + "</p>" for item in items)


drafts = []


def add(number, text, reason, notes):
    drafts.append(dict(number=number, proposed_xml=text, reason=reason, review_notes=notes))


add(
    "49 septies ZM",
    paragraphs(
        "Lorsque l'entreprise est titulaire, au 31 décembre d'une année, du label mentionné au 3° du III de l'article 244 quater O du code général des impôts, le taux majoré de crédit d'impôt prévu au II de cet article s'applique à l'ensemble des dépenses éligibles qu'elle a exposées au cours de cette année."
    ),
    "Réécriture à droit constant : la condition de détention du label est placée avant sa conséquence, afin de rendre explicite l'application du taux majoré à toutes les dépenses éligibles de l'année. Aucune réforme de fond du crédit d'impôt métiers d'art n'est introduite.",
    "Date d'appréciation du label au 31 décembre et renvois au II et au 3° du III de l'article 244 quater O conservés. Le corpus confirme ces subdivisions ; le terme d'application du dispositif figure dans l'article 244 quater O et n'est ni modifié ni prorogé ici. Un seul alinéa normatif est maintenu."
)

add(
    "49 septies ZN",
    paragraphs(
        "Sur l'impôt dû, les prélèvements non libératoires et les autres crédits d'impôt sont imputés avant le crédit d'impôt prévu à l'article 244 quater O du code général des impôts."
    ),
    "Réécriture à droit constant : l'ordre d'imputation est énoncé en désignant d'abord les imputations prioritaires. Aucune réforme de fond ni nouvelle priorité entre ces imputations préalables n'est créée.",
    "Le crédit d'impôt métiers d'art demeure imputé après les prélèvements non libératoires et tous les autres crédits d'impôt. Renvoi à l'article 244 quater O et alinéa unique conservés."
)

add(
    "49 septies ZO",
    paragraphs(
        "Pour l'application des articles 199 ter N, 220 P et 244 quater O du code général des impôts, les entreprises souscrivent une déclaration spéciale conforme au modèle établi par l'administration.",
        "Les personnes morales passibles de l'impôt sur les sociétés déposent cette déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts. Elles la déposent avec le relevé de solde mentionné à l'article 360. Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère dépose les déclarations spéciales pour le compte des sociétés du groupe. Elle joint ces déclarations, y compris la sienne, au relevé de solde relatif au résultat d'ensemble du groupe.",
        "Les autres entreprises joignent la déclaration spéciale à la déclaration annuelle de résultat qu'elles doivent déposer en application de l'article 53 A du code général des impôts.",
        "Lorsqu'une société de personnes ou un groupement mentionnés aux articles 8, 238 bis L, 239 quater, 239 quater B et 239 quater C du code général des impôts a engagé des dépenses ouvrant droit au crédit d'impôt prévu à l'article 244 quater O du même code, l'associé ou le membre dépose une déclaration spéciale. Il y indique la quote-part des crédits d'impôt provenant de chacune des sociétés de personnes ou de chacun des groupements assimilés dont il est associé ou membre. Toutefois, l'associé ou le membre personne physique est dispensé de cette déclaration s'il ne dispose d'aucun crédit d'impôt prévu à l'article 244 quater O autre que celui issu de sa participation dans la société de personnes ou le groupement assimilé."
    ),
    "Réécriture à droit constant : les modalités de dépôt sont distinguées selon le régime fiscal ; les obligations de la société mère et de l'associé sont formulées en phrases séparées dans leurs alinéas d'origine. L'exception applicable à la personne physique reste explicite. Aucune suppression de déclaration ni réforme de fond n'est introduite.",
    "Quatre alinéas maintenus. Tous les renvois, le lieu de dépôt, le relevé de solde, l'inclusion de la déclaration de la mère et la dispense conditionnelle de l'associé personne physique sont conservés. La proposition explicite que les dépenses sont engagées par la société ou le groupement, conformément au mécanisme de quote-part décrit par la source. L'article 360 reste le renvoi interne à l'annexe III."
)

add(
    "49 septies ZY",
    paragraphs(
        "Lorsque l'exercice est clos en cours d'année, les prêts avance mutation ne portant pas intérêt versés au titre de la dernière année civile écoulée servent au calcul du crédit d'impôt prévu à l'article 244 quater T du code général des impôts."
    ),
    "Réécriture à droit constant : la phrase identifie directement les prêts à retenir lorsque la clôture intervient en cours d'année. Aucune réforme de fond ni modification de la période de référence n'est apportée.",
    "Dernière année civile écoulée, catégorie de prêt et renvoi à l'article 244 quater T conservés. La note source, fondée sur l'article 3 du décret n° 2024-887 du 3 septembre 2024, réserve l'application aux offres de prêt avance mutation ne portant pas intérêt émises à compter du 1er septembre 2024 ; cette condition historique demeure applicable et ne constitue pas une date d'entrée en vigueur de la réécriture."
)

add(
    "49 septies ZZ",
    paragraphs(
        "Pour calculer, au titre d'une année, le crédit d'impôt prévu à l'article 244 quater T du code général des impôts, les prêts avance mutation ne portant pas intérêt sont retenus pour leur montant total dès le premier versement.",
        "La société de gestion mentionnée au dernier alinéa de l'article L. 312-1 du code de la construction et de l'habitation tient compte des éléments susceptibles de modifier le montant du crédit d'impôt lorsqu'elle établit l'attestation qui en présente le calcul. Ces éléments figurent sur l'attestation délivrée au plus tard le 31 mars suivant l'expiration de la période de six mois mentionnée au c du II de l'article D. 31-11-11 du même code. Cette période est celle dont dispose l'établissement de crédit, la société de financement ou la société de tiers-financement pour communiquer les informations relatives aux prêts faisant apparaître un avantage indûment perçu par l'emprunteur.",
        "Le remboursement anticipé mentionné au III de l'article 199 ter V du code général des impôts n'entraîne le reversement de la fraction correspondante du crédit d'impôt que si le montant cumulé des remboursements anticipés représente plus de 50 % du montant initial du prêt ne portant pas intérêt."
    ),
    "Réécriture à droit constant : la prise en compte intégrale dès le premier versement, l'établissement de l'attestation et la condition de reversement sont énoncés séparément. La longue phrase relative aux délais est scindée dans son alinéa. Aucune réforme de fond n'est appliquée à ce régime de prêt.",
    "Trois alinéas maintenus ; échéance du 31 mars, période de six mois, renvois et seuil strictement supérieur à 50 % conservés. Le montant cumulé est rapporté au montant initial du prêt. Incohérence terminologique préexistante à contrôler : la source parle de reversement en visant le III de l'article 199 ter V, alors que ce III, dans le corpus, prévoit l'impossibilité d'utiliser les fractions restant à imputer ; la proposition ne remplace pas silencieusement le reversement par l'arrêt d'imputation. Le dernier alinéa de L. 312-1 est bien son cinquième dans le corpus. Note source : application aux offres émises à compter du 1er septembre 2024, selon l'article 3 du décret n° 2024-887 du 3 septembre 2024 ; cette portée temporelle est conservée."
)

add(
    "49 septies ZZ bis",
    paragraphs(
        "Le crédit d'impôt accordé à l'établissement de crédit, à la société de financement ou à la société de tiers-financement en application de l'article 244 quater T du code général des impôts compense les intérêts non perçus sur un prêt avance mutation ne portant pas intérêt. Son montant est égal au montant du prêt multiplié par un taux S, le produit étant arrondi à l'euro le plus proche. Le taux S est calculé chaque trimestre en multipliant les deux termes suivants et en arrondissant le résultat à la quatrième décimale :",
        "1° La somme des différences de mensualités entre deux prêts de un euro, actualisées au moyen des facteurs définis aux quatrième et cinquième alinéas. Le premier est un prêt in fine dont la durée de différé est identique à celle du prêt avance mutation ne portant pas intérêt et qui est consenti au taux d'intérêt de référence i augmenté d'une prime p fixée à cent points de base. Le second est un prêt sans intérêt présentant les mêmes caractéristiques que le prêt avance mutation ne portant pas intérêt ;",
        "2° L'inverse de la moyenne des facteurs d'actualisation à six, dix-huit, trente, quarante-deux et cinquante-quatre mois.",
        "Pour chaque maturité t, exprimée en mois, le facteur d'actualisation β<sub>t</sub> est calculé selon la formule suivante à partir de z<sub>t</sub>. Cette valeur z<sub>t</sub> est la moyenne des taux d'intérêt annuels zéro-coupon du marché interbancaire de même maturité, observés entre le dixième jour du deuxième mois et le dixième jour du dernier mois du trimestre précédant l'offre de prêt :",
        "β<sub>t</sub> = (1 + z<sub>t</sub>)<sup>−t/12</sup>",
        "Le taux d'intérêt de référence i correspond au taux d'intérêt annuel de la courbe des zéros coupons du marché interbancaire à la maturité.",
        "Pour les calculs qui précèdent, la durée du prêt est arrondie au multiple inférieur de six mois.",
        "La société de gestion mentionnée au cinquième alinéa de l'article L. 312-1 du code de la construction et de l'habitation calcule ainsi le taux S. Ce taux s'applique aux prêts avance mutation ne portant pas intérêt dont l'offre est émise au cours d'un même trimestre."
    ),
    "Réécriture à droit constant : le calcul du montant et celui du taux S sont distingués ; les deux prêts de comparaison sont décrits dans des phrases séparées. La formule est présentée avec indices et exposant pour rendre son écriture mathématique lisible. Aucune réforme de fond des paramètres financiers n'est introduite.",
    "Les huit alinéas logiques de la source, dont plusieurs étaient séparés par des doubles sauts de ligne, restent dans le même ordre : les quatrième et cinquième portent toujours la définition des facteurs et la formule. Sont conservés les prêts de un euro, le prêt in fine et sa durée de différé, la prime de cent points de base, les maturités de six, dix-huit, trente, quarante-deux et cinquante-quatre mois, la fenêtre d'observation, l'arrondi à l'euro, celui à la quatrième décimale et l'arrondi de durée au multiple inférieur de six mois. La notation aplatie '(1 + zt)-t/12' est rendue par l'exposant −t/12 ; contrôler cette restitution mathématique sur l'édition typographique de référence avant adoption. La source ne précise pas davantage la maturité servant à lire i : aucune précision financière nouvelle n'est inventée. Cinquième et dernier alinéas de L. 312-1 coïncident dans le corpus. La note source maintient l'application aux offres émises à compter du 1er septembre 2024, en vertu de l'article 3 du décret n° 2024-887 du 3 septembre 2024."
)

add(
    "49 septies ZZ ter",
    paragraphs(
        "Sur l'impôt dû, les prélèvements non libératoires et les autres crédits d'impôt sont imputés avant le crédit d'impôt prévu à l'article 244 quater T du code général des impôts."
    ),
    "Réécriture à droit constant : la priorité des imputations préalables est exprimée directement. Aucune réforme de fond du crédit d'impôt ni de son rang d'imputation n'est introduite.",
    "Alinéa unique et renvoi à l'article 244 quater T conservés. Aucun ordre nouveau n'est fixé entre les prélèvements non libératoires et les autres crédits d'impôt. La note source maintient l'application aux offres de prêt avance mutation ne portant pas intérêt émises à compter du 1er septembre 2024, conformément à l'article 3 du décret n° 2024-887 du 3 septembre 2024."
)

add(
    "49 septies ZZ quater",
    paragraphs(
        "Pour l'application des articles 199 ter V, 220 Z octies et 244 quater T du code général des impôts, les établissements de crédit, les sociétés de financement et les sociétés de tiers-financement mentionnés au I de l'article 244 quater T du même code joignent une déclaration spéciale à la déclaration de résultat qu'ils déposent auprès du service des impôts dont ils dépendent.",
        "Toutefois, les personnes morales passibles de l'impôt sur les sociétés déposent la déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts. Elles la déposent avec le relevé de solde de l'exercice mentionné à l'article 360 de l'annexe III du même code. Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère joint les déclarations spéciales des sociétés membres du groupe au relevé de solde relatif au résultat d'ensemble du groupe. Ces sociétés sont dispensées de joindre leur déclaration spéciale à la déclaration de résultats qu'elles déposent en application du 1 de l'article 223 du même code."
    ),
    "Réécriture à droit constant : les obligations déclaratives sont formulées directement et la règle spéciale des personnes morales soumises à l'IS est scindée en phrases plus courtes. Le dépôt par la mère et la dispense des membres demeurent dans le même alinéa. Aucune nouvelle simplification de fond n'est présumée applicable.",
    "Deux alinéas maintenus. Renvois aux articles 199 ter V, 220 Z octies, 244 quater T, 218 A, 360 de l'annexe III, 223 A et 1 de l'article 223 conservés. Les trois catégories de prêteurs demeurent visées ; le dépôt groupé et la dispense corrélative restent inchangés. La source de cet article ne comporte pas de note d'application temporelle : aucune date de réforme n'est ajoutée."
)

add(
    "49 septies ZZ quinquies",
    paragraphs(
        "Pour chaque établissement de crédit, société de financement ou société de tiers-financement tenu de déposer une déclaration spéciale et lui ayant déclaré des prêts avance mutation ne portant pas intérêt, la société de gestion mentionnée au dernier alinéa de l'article L. 312-1 du code de la construction et de l'habitation transmet à la direction des grandes entreprises un état relatif au crédit d'impôt. Elle le transmet dans les quatre mois suivant la clôture de l'exercice de l'établissement ou de la société concerné.",
        "Cet état présente les éléments suivants :",
        "a) Le montant global des prêts avance mutation ne portant pas intérêt ainsi que des crédits d'impôt dégagés au cours des années antérieures et de l'année concernée ;",
        "b) Le suivi des crédits d'impôt ;",
        "c) Les crédits d'impôt ou fractions de crédit d'impôt reversés ou non imputés en raison du non-respect des conditions d'octroi des prêts avance mutation ne portant pas intérêt mentionnés au I de l'article 244 quater T du code général des impôts, du non-respect des conditions relatives à l'affectation du logement et à ses caractéristiques mentionnées au même I, ou de remboursements totaux ou partiels de ces prêts intervenant pendant leur durée. L'état indique également l'origine du reversement ou de l'arrêt d'imputation du crédit d'impôt."
    ),
    "Réécriture à droit constant : le périmètre des états à transmettre est placé en tête et le délai est isolé dans une phrase. Le contenu du c est organisé autour des causes du reversement ou de la non-imputation, sans supprimer l'information sur leur origine. Aucune réforme de fond du suivi fiscal n'est introduite.",
    "Cinq alinéas logiques, dont les lettres a, b et c, maintenus dans leur ordre. Délai de quatre mois propre à la clôture de chaque prêteur, destinataire direction des grandes entreprises, montants des années antérieures et de l'année concernée, trois catégories de prêteurs et tous les motifs de suivi conservés. Le renvoi au dernier alinéa de L. 312-1 correspond au cinquième dans le corpus. Note source : application aux offres émises à compter du 1er septembre 2024 selon l'article 3 du décret n° 2024-887 du 3 septembre 2024 ; cette condition historique demeure."
)

add(
    "49 septies ZZA",
    paragraphs(
        "Lorsque l'exercice est clos en cours d'année, les avances remboursables sans intérêt versées au titre de la dernière année civile écoulée servent au calcul du crédit d'impôt prévu à l'article 244 quater U du code général des impôts."
    ),
    "Réécriture à droit constant : les avances à retenir sont désignées directement après la condition tenant à la clôture de l'exercice. Aucune réforme de fond ni modification de l'année civile de référence n'est introduite.",
    "Alinéa unique conservé. Le renvoi reste celui de l'article 244 quater U et le calcul continue à porter sur les avances de la dernière année civile écoulée, sans assimilation aux prêts avance mutation ou aux prêts de primo-accession."
)

add(
    "49 septies ZZB",
    paragraphs(
        "Pour calculer, au titre d'une année, le crédit d'impôt prévu à l'article 244 quater U du code général des impôts, les avances remboursables sont retenues pour leur montant total dès le premier versement.",
        "L'organisme mentionné au cinquième alinéa de l'article L. 312-1 du code de la construction et de l'habitation tient compte des éléments susceptibles de modifier le montant du crédit d'impôt lorsqu'il établit l'attestation qui en présente le calcul. Ces éléments figurent sur l'attestation délivrée au plus tard le 31 mars suivant l'expiration de la période de six mois mentionnée au c du II de l'article D. 319-14 du même code. Cette période est celle dont dispose l'établissement de crédit, la société de financement ou la société de tiers-financement pour communiquer les informations relatives aux avances faisant apparaître un avantage indûment perçu par l'emprunteur. Par dérogation, les éléments qui modifient le montant du crédit d'impôt en raison de l'avantage indûment perçu mentionné à l'article D. 319-30 du même code figurent sur l'attestation délivrée au plus tard le 31 mars suivant l'expiration de la période de neuf mois mentionnée à la deuxième phrase de cet article."
    ),
    "Réécriture à droit constant : l'auteur et l'objet de l'attestation sont explicités ; la période de transmission est expliquée dans une phrase distincte et la dérogation de neuf mois est maintenue dans le même alinéa. Aucune réforme de fond des délais ni des avances concernées n'est introduite.",
    "Deux alinéas normatifs maintenus. Prise en compte totale dès le premier versement, 31 mars, périodes de six et neuf mois et renvoi à la deuxième phrase de D. 319-30 conservés. Le corpus confirme le délai de six mois au c du II de D. 319-14 et celui de neuf mois dans la deuxième phrase de D. 319-30. Note source : ces dispositions s'appliquent aux offres d'avances remboursables sans intérêt émises à compter du lendemain de la publication du décret n° 2024-299 du 29 mars 2024, en vertu du I de son article 6 ; cette condition est conservée sans inventer de date de publication."
)

add(
    "49 septies ZZC",
    paragraphs(
        "Sur l'impôt dû, les prélèvements non libératoires et les autres crédits d'impôt sont imputés avant le crédit d'impôt prévu à l'article 244 quater U du code général des impôts."
    ),
    "Réécriture à droit constant : l'ordre d'imputation est exprimé en plaçant les imputations préalables en début de phrase. Aucune réforme de fond ni priorité nouvelle entre ces imputations n'est introduite.",
    "Alinéa unique et renvoi à l'article 244 quater U maintenus. Le crédit d'impôt correspondant aux avances remboursables sans intérêt demeure imputé après les prélèvements non libératoires et les autres crédits d'impôt."
)

add(
    "49 septies ZZD",
    paragraphs(
        "Pour l'application des articles 199 ter S, 220 Z et 244 quater U du code général des impôts, les établissements de crédit, les sociétés de financement et les sociétés de tiers-financement mentionnés au I de l'article 244 quater U du même code joignent une déclaration spéciale à la déclaration de résultat qu'ils déposent auprès du service des impôts dont ils dépendent.",
        "Toutefois, les personnes morales passibles de l'impôt sur les sociétés déposent la déclaration spéciale auprès du comptable de la direction générale des finances publiques du lieu d'imposition défini à l'article 218 A du code général des impôts. Elles la déposent avec le relevé de solde de l'exercice mentionné à l'article 360. Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère joint les déclarations spéciales des sociétés membres du groupe au relevé de solde relatif au résultat d'ensemble du groupe. Ces sociétés sont dispensées de joindre leur déclaration spéciale à la déclaration de résultats qu'elles déposent en application du 1 de l'article 223 du même code."
    ),
    "Réécriture à droit constant : le dépôt de la déclaration spéciale est décrit selon le régime fiscal, en phrases plus courtes. Le régime des groupes reste dans son alinéa, avec la dispense corrélative des membres. Aucune réforme de fond ni suppression supplémentaire de formalité n'est introduite.",
    "Deux alinéas normatifs maintenus. Les trois catégories de prêteurs et les renvois aux articles 199 ter S, 220 Z, 244 quater U, 218 A, 360, 223 A et 1 de l'article 223 sont conservés. L'article 360 est le renvoi interne à l'annexe III. Note source : application aux offres d'avances remboursables sans intérêt émises à compter du lendemain de la publication du décret n° 2024-299 du 29 mars 2024, conformément au I de son article 6 ; aucune date future n'en est déduite."
)

add(
    "49 septies ZZE",
    paragraphs(
        "Pour chaque établissement de crédit, société de financement ou société de tiers-financement tenu de déposer une déclaration spéciale et lui ayant déclaré des avances remboursables sans intérêt, l'organisme mentionné à l'article D. 319-12 du code de la construction et de l'habitation transmet au service chargé des grandes entreprises un état relatif au crédit d'impôt. Il le transmet dans les quatre mois suivant la clôture de l'exercice de l'établissement ou de la société concerné.",
        "Cet état présente les éléments suivants :",
        "a) Le montant global des avances remboursables sans intérêt ainsi que des crédits d'impôt dégagés au cours des années antérieures et de l'année concernée ;",
        "b) Le suivi des crédits d'impôt ;",
        "c) Les crédits d'impôt ou fractions de crédit d'impôt reversés ou non imputés en raison du non-respect des conditions d'octroi des avances remboursables mentionnées au I de l'article 244 quater U du code général des impôts, du non-respect des conditions relatives à l'affectation du logement et à ses caractéristiques mentionnées au même I, ou de remboursements totaux ou partiels d'avances remboursables sans intérêt intervenant pendant leur durée de remboursement. L'état indique également l'origine du reversement ou de l'arrêt d'imputation du crédit d'impôt."
    ),
    "Réécriture à droit constant : le champ des états est présenté avant l'obligation de transmission ; le délai et l'information sur l'origine des régularisations font l'objet de phrases distinctes. Les lettres a, b et c sont conservées. Aucune réforme de fond du suivi des avances n'est introduite.",
    "Cinq alinéas normatifs maintenus, avec le délai de quatre mois suivant chaque clôture, le service destinataire, le renvoi à D. 319-12, les montants des années antérieures et de l'année concernée et toutes les causes de reversement ou de non-imputation. Note source : application aux offres d'avances remboursables sans intérêt émises à compter du lendemain de la publication du décret n° 2024-299 du 29 mars 2024, en vertu du I de son article 6 ; cette portée temporelle est conservée."
)

add(
    "49 septies ZZF",
    paragraphs(
        "Lorsque l'exercice est clos en cours d'année, les prêts ne portant pas intérêt versés au titre de la dernière année civile écoulée servent au calcul du crédit d'impôt prévu à l'article 244 quater V du code général des impôts."
    ),
    "Réécriture à droit constant : les prêts à retenir sont identifiés directement après la condition de clôture en cours d'année. Aucune réforme de fond ni modification de la période de référence n'est introduite.",
    "Alinéa unique, dernière année civile écoulée et renvoi à l'article 244 quater V conservés. Ce crédit d'impôt de primo-accession n'est pas assimilé aux régimes des articles 244 quater T ou 244 quater U."
)

add(
    "49 septies ZZG",
    paragraphs(
        "Pour calculer, au titre d'une année, le crédit d'impôt prévu à l'article 244 quater V du code général des impôts, les prêts ne portant pas intérêt sont retenus pour leur montant total dès le premier versement.",
        "Les établissements de crédit ou les sociétés de financement déclarent les éléments susceptibles de modifier le montant du crédit d'impôt à l'organisme mentionné au cinquième alinéa de l'article L. 312-1 du code de la construction et de l'habitation. Ils effectuent cette déclaration au plus tard le 31 mars de l'année suivant celle du premier versement des prêts ne portant pas intérêt. L'organisme utilise ces éléments pour établir l'attestation de calcul du crédit d'impôt qu'il délivre à ces établissements ou sociétés.",
        "Par exception, les événements mentionnés aux II et III de l'article 199 ter T du code général des impôts sont déclarés dans les trois mois suivant leur déclaration par l'emprunteur à l'établissement de crédit ou à la société de financement, ou suivant l'expiration du délai laissé à l'emprunteur pour justifier de certaines conditions du prêt en application de l'arrêté mentionné à l'article D. 31-10-4 du code de la construction et de l'habitation. Ces événements sont alors pris en compte pour établir l'attestation le 31 mars suivant."
    ),
    "Réécriture à droit constant : le déclarant, le destinataire, le délai normal et l'utilisation des éléments déclarés sont formulés en phrases distinctes dans leur alinéa. Les deux points de départ du délai exceptionnel restent explicites. Aucune réforme de fond du calendrier n'est introduite.",
    "Trois alinéas maintenus. Montant total dès le premier versement, échéance normale du 31 mars suivant l'année du premier versement, délai exceptionnel de trois mois et attestation du 31 mars suivant conservés. Renvois aux II et III de l'article 199 ter T, au cinquième alinéa de L. 312-1 et à l'arrêté mentionné à D. 31-10-4 maintenus. La note source indique une modification de conséquence de l'article 5, II, 3° du décret n° 2019-873 du 21 août 2019 ; cette mention historique ne fixe pas une entrée en vigueur future."
)

add(
    "49 septies ZZI",
    paragraphs(
        "Sur l'impôt dû, les prélèvements non libératoires et les autres crédits d'impôt sont imputés avant le crédit d'impôt prévu à l'article 244 quater V du code général des impôts."
    ),
    "Réécriture à droit constant : la phrase énonce directement les imputations qui précèdent celle du crédit d'impôt. Aucune réforme de fond ni modification de son rang n'est introduite.",
    "Alinéa unique et renvoi à l'article 244 quater V conservés. Aucun ordre nouveau n'est fixé entre les différentes imputations qui précèdent le crédit d'impôt de primo-accession."
)

add(
    "49 septies ZZJ",
    paragraphs(
        "Pour l'application des articles 199 ter T, 220 Z ter et 244 quater V du code général des impôts, les établissements de crédit et les sociétés de financement mentionnés au I de l'article 244 quater V du même code joignent une déclaration spéciale à la déclaration de résultat qu'ils déposent auprès du service des impôts dont ils dépendent.",
        "Toutefois, les personnes morales passibles de l'impôt sur les sociétés déposent la déclaration spéciale auprès du comptable de la direction générale des finances publiques avec le relevé de solde de l'exercice. Pour les sociétés relevant du régime des groupes de sociétés prévu à l'article 223 A du code général des impôts, la société mère joint les déclarations spéciales des sociétés membres du groupe au relevé de solde relatif au résultat d'ensemble du groupe. Ces sociétés sont dispensées de joindre leur déclaration spéciale à la déclaration de résultats qu'elles déposent en application du 1 de l'article 223 du même code."
    ),
    "Réécriture à droit constant : les obligations de dépôt sont formulées directement et les pronoms renvoyant aux sociétés du groupe sont clarifiés. La dispense liée au dépôt par la mère est maintenue. Aucune réforme de fond ni extension à d'autres prêteurs n'est introduite.",
    "Deux alinéas et tous les renvois conservés. Seuls les établissements de crédit et sociétés de financement restent visés, sans ajout des sociétés de tiers-financement présentes dans d'autres régimes. La source ne renvoie ici ni à l'article 218 A ni à l'article 360 : ces renvois ne sont pas ajoutés par alignement sur les articles voisins."
)

add(
    "49 septies ZZK",
    paragraphs(
        "Pour chaque établissement de crédit ou société de financement tenu de déposer une déclaration spéciale et lui ayant déclaré des prêts ne portant pas intérêt, l'organisme mentionné au cinquième alinéa de l'article L. 312-1 du code de la construction et de l'habitation transmet au service chargé des grandes entreprises un état relatif au crédit d'impôt. Il le transmet dans les quatre mois suivant la clôture de l'exercice de l'établissement ou de la société concerné.",
        "Cet état présente les éléments suivants :",
        "a) Le montant global des prêts ne portant pas intérêt ainsi que des crédits d'impôt dégagés au cours des années antérieures et de l'année concernée ;",
        "b) Le suivi des crédits d'impôt ;",
        "c) Les crédits d'impôt ou fractions de crédit d'impôt reversés ou non imputés en raison du non-respect des conditions des prêts mentionnées au chapitre X du titre Ier du livre III du code de la construction et de l'habitation, du non-respect des conditions de maintien des prêts mentionnées à l'article L. 31-10-6 du même code, ou de remboursements anticipés de prêts ne portant pas intérêt. L'état indique également l'application de la majoration de 40 % mentionnée aux II et III de l'article 199 ter T du code général des impôts et l'origine du reversement ou de l'arrêt d'imputation."
    ),
    "Réécriture à droit constant : le périmètre et le délai de transmission sont explicités ; au c, les causes des régularisations sont distinguées de la mention de la majoration et de leur origine. Les lettres et l'ordre des alinéas restent identiques. Aucune réforme de fond n'est introduite.",
    "Cinq alinéas maintenus. Délai de quatre mois, destinataire, montants des années antérieures et de l'année concernée, remboursements anticipés et majoration de 40 % sont conservés, ainsi que tous les renvois. Le corpus de l'article 199 ter T confirme deux mécanismes distincts aux II et III : majoration du reversement et somme calculée sur les fractions restant à imputer ; la rédaction conserve le renvoi global de la source sans les confondre ni les réécrire. Le champ reste limité aux établissements de crédit et sociétés de financement."
)

add(
    "49 septies ZZL",
    paragraphs(
        "Dans les départements d'outre-mer, les investissements productifs neufs ouvrant droit au crédit d'impôt prévu au I de l'article 244 quater W du code général des impôts consistent en l'acquisition ou la création d'immobilisations corporelles neuves et amortissables. Ces immobilisations sont affectées à des activités relevant des secteurs éligibles en application du I de l'article 199 undecies B du même code."
    ),
    "Réécriture à droit constant : la définition de l'investissement et la condition d'affectation aux activités éligibles sont réparties en deux phrases dans le même alinéa. Aucune réforme de fond du crédit d'impôt outre-mer ni exonération nouvelle des bénéfices réinvestis n'est introduite.",
    "Champ limité aux départements d'outre-mer, investissements productifs neufs, acquisitions ou créations et caractère à la fois corporel, neuf et amortissable conservés. Les deux renvois aux I des articles 244 quater W et 199 undecies B sont maintenus."
)

add(
    "49 septies ZZM",
    paragraphs(
        "Pour déterminer le crédit d'impôt prévu au I de l'article 244 quater W du code général des impôts, il est tenu compte du montant des aides publiques ou, si l'investissement consiste à acquérir ou à construire des logements neufs, des subventions publiques. Sont prises en compte celles qui sont obtenues ou demandées et non encore accordées à la date de clôture de l'exercice de réalisation de l'investissement. Si nécessaire, le montant du crédit d'impôt est régularisé au titre de l'exercice au cours duquel intervient la décision relative à leur octroi et à leur montant."
    ),
    "Réécriture à droit constant : la catégorie d'aide à prendre en compte, la date d'appréciation et l'éventuelle régularisation sont présentées en trois phrases dans l'alinéa d'origine. Aucune réforme de fond du traitement des aides publiques n'est introduite.",
    "Distinction entre aides publiques et subventions publiques pour l'acquisition ou la construction de logements neufs conservée. Sont toujours visés tant les montants obtenus que ceux demandés et non encore accordés à la clôture de l'exercice de réalisation. La régularisation éventuelle reste rattachée à l'exercice de la décision d'octroi et de montant, sans suppression rétroactive d'aide ni modification des contrats en cours."
)

add(
    "49 septies ZZN",
    paragraphs(
        "Le crédit d'impôt prévu au I de l'article 244 quater W du code général des impôts ne peut pas être imputé sur l'impôt résultant de la reprise de crédits d'impôt antérieurement obtenus au titre de cet article ou de l'article 244 quater X du même code, de réductions d'impôt antérieurement pratiquées au titre des articles 199 undecies B et 244 quater Y du même code, ou de déductions fiscales antérieurement pratiquées au titre de l'article 217 undecies du même code. Il ne peut pas non plus être imputé sur l'impôt résultant de la majoration du revenu global effectuée en application des vingt-troisième, vingt-cinquième et vingt-sixième alinéas du I de l'article 199 undecies B du même code."
    ),
    "Réécriture à droit constant : les catégories de reprises sont rendues explicites et l'interdiction relative à la majoration du revenu global est isolée dans une seconde phrase. Aucune réforme de fond ni nouvelle possibilité d'imputation n'est introduite.",
    "Alinéa unique maintenu. Toutes les catégories de reprise, leur caractère antérieur et les articles 244 quater W, 244 quater X, 199 undecies B, 244 quater Y et 217 undecies sont conservés. Les rangs vingt-troisième, vingt-cinquième et vingt-sixième du I de l'article 199 undecies B sont repris sans déplacement. Point préexistant à contrôler : dans le corpus consulté, ces alinéas traitent de reprises de réduction d'impôt, sans énoncer expressément une majoration du revenu global ; la terminologie et les cibles de la source sont conservées, sans correction implicite."
)

add(
    "49 septies ZZO",
    paragraphs(
        "Un arrêté du ministre chargé du budget définit, pour l'application du a du 2 du I de l'article 244 quater W du code général des impôts, les véhicules strictement indispensables à l'activité de l'exploitant."
    ),
    "Réécriture à droit constant : l'acte réglementaire et son auteur deviennent le sujet de la phrase, ce qui rend la compétence immédiatement lisible. Aucune réforme de fond de la notion de véhicule indispensable n'est introduite.",
    "Alinéa unique, compétence du seul ministre chargé du budget, qualification de véhicules strictement indispensables et renvoi au a du 2 du I de l'article 244 quater W conservés. Le champ des activités reste celui de la disposition législative de renvoi ; aucun élargissement à tous les véhicules professionnels n'est créé."
)

add(
    "49 septies ZZP",
    paragraphs(
        "Pour l'application du b du 1° du 4 du I de l'article 244 quater W du code général des impôts, le loyer ne dépasse pas le plafond mentionné au 1° du 1 de l'article 46 AG duodecies et les ressources du locataire ne dépassent pas les plafonds mentionnés au 2 du même article.",
        "Les sommes mentionnées au VI de l'article 46 AG sexdecies entrent, pour leur montant réel et justifié, dans le prix de revient mentionné au 4 du II de l'article 244 quater W du code général des impôts."
    ),
    "Réécriture à droit constant : le renvoi applicable au loyer est distingué de celui applicable aux ressources ; la seconde règle désigne directement les sommes incorporées au prix de revient. Aucune réforme de fond des plafonds ou de l'assiette n'est introduite.",
    "Deux alinéas logiques conservés, la source les séparant par un double saut de ligne. Les renvois au b du 1° du 4 du I et au 4 du II de l'article 244 quater W, au 1° du 1 et au 2 de l'article 46 AG duodecies, et au VI de l'article 46 AG sexdecies sont conservés. La condition de montant réel et justifié demeure. Les plafonds restent définis par renvoi, sans taux ou montant nouveau. La note source renvoie aux conditions d'application de l'article 2 du décret n° 2023-470 du 16 juin 2023 : ce texte n'étant pas reproduit dans le lot, son champ temporel doit être contrôlé lors de la coordination finale ; aucune date ni condition non fournie n'est inventée."
)


source = json.loads(Path("source.json").read_text())
assert len(source) == len(drafts) == 24
answer = []
for article, draft in zip(source, drafts):
    assert article["number"] == draft["number"]
    draft["proposed_xml"] = (
        draft["proposed_xml"]
        .replace("qu'ils déposent auprès du service des impôts", "qu'ils doivent déposer auprès du service des impôts")
        .replace("qu'elles déposent en application du 1 de l'article 223", "qu'elles doivent déposer en application du 1 de l'article 223")
        .replace("de l'établissement ou de la société concerné", "de l'établissement ou de la société en cause")
    )
    result = {key: article[key] for key in ("code_id", "source_id", "source_sha256", "number")}
    result.update({key: draft[key] for key in ("proposed_xml", "reason", "review_notes")})
    result["status"] = "rewrite_draft"
    answer.append(result)
Path("answer.json").write_text(json.dumps(answer, ensure_ascii=False, indent=2) + "\n")
