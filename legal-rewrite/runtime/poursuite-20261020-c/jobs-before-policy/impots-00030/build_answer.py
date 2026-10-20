import html
import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    lines = [line.strip() for line in paragraphs.strip().splitlines() if line.strip()]
    drafts[number] = {
        'proposed_xml': '\n'.join('<p>' + html.escape(line, quote=False) + '</p>' for line in lines),
        'reason': reason,
        'review_notes': review_notes,
    }


add('199', '''
Sous réserve des traités de réciprocité, seuls les citoyens français et les personnes originaires de Saint-Pierre-et-Miquelon, de Nouvelle-Calédonie, de Polynésie française, des îles Wallis et Futuna et des Terres australes et antarctiques françaises bénéficient des dispositions de l'article 193 qui, pour calculer l'impôt sur le revenu, divisent le revenu imposable en un nombre de parts déterminé selon la situation et les charges de famille du contribuable.
''',
    "Réécriture à droit constant : les bénéficiaires sont placés en sujet de la règle de division du revenu imposable en parts. La réserve des traités et la liste territoriale sont conservées. Aucune réforme de fond du quotient familial n'est définie pour cet article par policy.json.",
    "Renvoi à l'article 193 conservé. La restriction selon la citoyenneté ou l'origine et la réserve des traités de réciprocité sont reprises telles qu'elles délimitent la source ; leur articulation avec les engagements internationaux appelle un contrôle de fond distinct, sans correction implicite dans cette réécriture.")

add('199 ter', '''
I a. Les bénéficiaires des revenus de capitaux mobiliers visés aux articles 108 à 119, 238 septies B et 1678 bis qui doivent, en application de la législation fiscale, déposer pour l'assiette de l'impôt sur le revenu une déclaration comprenant ces revenus imputent les sommes retenues sur ces revenus en vertu des articles 119 bis et 1678 bis sur l'impôt sur le revenu liquidé au vu de cette déclaration, dans les conditions fixées à l'article 193.
Les sommes retenues à la source sont restituées à tous les contribuables, qu'ils soient ou non tenus de déposer une déclaration pour l'assiette de l'impôt sur le revenu, dans la mesure où elles ne peuvent être imputées parce que le montant de l'impôt est inférieur à ces sommes ou que l'impôt n'est pas exigible. Un décret en Conseil d'Etat fixe les conditions de cette restitution. La restitution ne s'applique pas à la retenue à la source sur les intérêts des obligations émises à compter du 1er octobre 1984 qui bénéficient à des personnes ayant leur domicile fiscal ou étant établies hors du territoire de la République française, de Monaco ou d'un Etat dont l'institut d'émission est lié au Trésor français par un compte d'opération monétaire.
b. Pour les revenus de source étrangère visés aux articles 120 à 125, l'imputation ne peut dépasser le montant du crédit correspondant à l'impôt retenu à la source à l'étranger ou à la décote qui en tient lieu, tel que le prévoient les conventions internationales.
c. La retenue à la source temporairement prélevée par le Luxembourg et l'Autriche conformément à l'article 11 de la directive 2003/48/CE du Conseil du 3 juin 2003 en matière de fiscalité des revenus de l'épargne sous forme de paiements d'intérêts ouvre droit à un crédit d'impôt égal à cette retenue. Ce crédit est déduit de l'impôt sur le revenu après imputation, le cas échéant, des autres retenues à la source et crédits d'impôt mentionnés aux a et b. Il est déduit de l'impôt dû au titre de l'année au cours de laquelle les revenus définis au septième alinéa du 1 de l'article 242 ter, majorés des retenues à la source qu'ils ont supportées, sont déclarés et imposés. L'excédent éventuel est restitué.
I bis (Abrogé).
II. Les actionnaires des sociétés d'investissement ou des sociétés assimilées visées aux 1° bis et 1° bis A de l'article 208 et des sociétés de capital-risque visées au 3° septies du même article peuvent imputer tout ou partie des crédits d'impôt attachés aux produits et aux plus-values de cession du portefeuille de ces sociétés, dans les mêmes conditions que s'ils avaient perçu directement ces revenus.
Pour chaque exercice, la société calcule le montant total des crédits d'impôt imputables au titre des revenus qu'elle a encaissés et des plus-values qu'elle a réalisées.
Le droit à imputation de chaque actionnaire est proportionnel à sa part dans les dividendes et les plus-values distribués au titre du même exercice. Pour les dividendes, ce droit ne peut dépasser celui normalement attaché aux revenus distribués par les sociétés françaises ordinaires.
Pour déterminer l'assiette de l'impôt sur le revenu, le montant à imputer est ajouté au revenu net perçu par l'actionnaire.
Les sociétés d'investissement qui bénéficient du régime prévu aux 1° bis et 1° bis A de l'article 208 peuvent reporter sur les exercices suivants les crédits d'impôt qu'elles n'ont pas pu transférer à leurs actionnaires. Ce report concerne tout ou partie des crédits attachés aux produits de leur portefeuille encaissés et aux plus-values de cession réalisées au cours d'un exercice.
III (Abrogé).
''',
    "Réécriture à droit constant : explicitation de l'imputation, des causes de restitution et de l'ordre des crédits au c ; séparation des étapes de calcul pour les actionnaires sans déplacer les alinéas. Les exceptions, les plafonds et le report restent inchangés. Aucune réforme de fond n'est appliquée à ces retenues.",
    "Subdivisions I a, b, c, I bis, II et III et renvois conservés, notamment au septième alinéa du 1 de l'article 242 ter. Maintien du 1er octobre 1984 et du mécanisme historique Luxembourg/Autriche, dont la portée résiduelle doit être contrôlée sans suppression silencieuse. La note source vise le V de l'article 10 de l'ordonnance n° 2015-681 du 18 juin 2015 : application aux distributions mises en paiement à compter du 1er janvier 2015 ; ce champ temporel ne constitue pas une date de réforme future.")

add('199 ter A', '''
Les porteurs de parts d'un fonds commun de placement peuvent imputer tout ou partie des crédits d'impôt attachés aux produits et aux plus-values de cession des actifs compris dans ce fonds.
Chaque année, le gérant du fonds calcule le montant total des crédits d'impôt imputables au titre des produits encaissés et des plus-values réalisées par le fonds.
Le droit à imputation de chaque porteur est proportionnel à sa quote-part dans la répartition effectuée au titre de l'année considérée. Il tient compte de la nature et de l'origine française ou étrangère des sommes ou valeurs réparties. Il ne peut dépasser le droit dont le porteur aurait bénéficié s'il avait directement perçu sa quote-part des mêmes produits ou directement réalisé la même plus-value.
Pour déterminer l'assiette de l'impôt sur le revenu ou de l'impôt sur les sociétés, le montant à imputer est ajouté au revenu net perçu par les porteurs de parts.
Un décret adapte les dispositions du présent code qui régissent la restitution des sommes correspondant aux crédits d'impôt non imputés.
''',
    "Réécriture à droit constant : le calcul annuel, la répartition entre porteurs et le plafond individuel sont formulés en phrases distinctes, dans les cinq alinéas d'origine. L'ajout du crédit au revenu net et l'habilitation réglementaire sont conservés. Aucune réforme de fond des fonds communs de placement n'est introduite.",
    "Conserver la prise en compte de la nature et de l'origine des sommes ou valeurs, ainsi que les deux impôts visés. La note source, article 17 III de la loi n° 2013-1278 du 29 décembre 2013 de finances pour 2014, prévoit l'application aux gains réalisés et aux distributions perçues à compter du 1er janvier 2013.")

add('199 ter-0 B', '''
Les porteurs de parts d'un fonds de placement immobilier mentionné à l'article 239 nonies peuvent imputer tout ou partie des crédits d'impôt attachés aux revenus et aux profits mentionnés à l'article L. 214-81 du code monétaire et financier compris dans ce fonds.
Chaque année, la société de gestion du fonds mentionnée à l'article L. 214-61 du même code calcule le montant total des crédits d'impôt imputables au titre des revenus encaissés et des profits réalisés par le fonds.
Le droit à imputation de chaque porteur est proportionnel à sa quote-part dans la distribution effectuée au titre de l'année considérée. Il tient compte de la nature et de l'origine française ou étrangère des revenus et des profits compris dans cette distribution. Il ne peut dépasser le droit dont le porteur aurait bénéficié s'il avait directement perçu sa quote-part des mêmes revenus et profits.
Pour déterminer l'assiette de l'impôt sur le revenu ou de l'impôt sur les sociétés, le montant à imputer est ajouté au revenu net perçu par les porteurs de parts.
''',
    "Réécriture à droit constant : clarification du rôle de la société de gestion et des deux limites du droit individuel, proportion de la distribution et plafond de perception directe. Les quatre alinéas sont maintenus. Aucune réforme de fond de ce régime immobilier n'est prévue dans policy.json.",
    "Renvois conservés aux articles 239 nonies du CGI, L. 214-81 et L. 214-61 du code monétaire et financier. Le dispositif porte sur les revenus et profits du fonds et conserve l'origine française ou étrangère ainsi que l'ajout à l'assiette des deux impôts.")

add('199 ter B', '''
I. – Le contribuable impute le crédit d'impôt pour dépenses de recherche défini à l'article 244 quater B sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle les dépenses de recherche retenues pour calculer ce crédit ont été exposées. L'excédent constitue pour l'entreprise une créance sur l'Etat d'un montant égal à cet excédent. Cette créance sert au paiement de l'impôt sur le revenu dû au titre des trois années suivant celle au titre de laquelle elle est constatée ; la fraction qui reste inutilisée à l'issue de cette période est remboursée.
La créance est inaliénable et incessible, sous réserve des cas et conditions prévus aux articles L. 214-169 à L. 214-190 et L. 313-23 à L. 313-35 du code monétaire et financier.
Lorsqu'une fusion ou une opération assimilée intervient pendant la période mentionnée à la dernière phrase du premier alinéa, la fraction de la créance que la société apporteuse n'a pas encore imputée est transférée à la société bénéficiaire de l'apport.
La fraction du crédit d'impôt recherche correspondant aux parts des personnes physiques autres que celles mentionnées au I de l'article 151 nonies ne peut être ni imputée ni restituée.
II. – Les entreprises suivantes ont droit au remboursement immédiat de la créance mentionnée au premier alinéa du I lorsqu'elles la constatent :
1° Les entreprises créées à compter du 1er janvier 2004, à l'exclusion de celles mentionnées au III de l'article 44 sexies, dont le capital est entièrement libéré et est détenu de manière continue à hauteur d'au moins 50 % :
a) Par des personnes physiques ;
b) Ou par une société dont au moins 50 % du capital est détenu par des personnes physiques ;
c) Ou par des sociétés de capital-risque, des fonds communs de placement à risques, des fonds professionnels spécialisés relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, des fonds professionnels de capital investissement, des sociétés de libre partenariat, des sociétés de développement régional, des sociétés financières d'innovation ou des sociétés unipersonnelles d'investissement à risque. Dans ce cas, aucun lien de dépendance au sens du 12 de l'article 39 ne doit exister entre les entreprises et ces sociétés ou ces fonds.
Ces entreprises peuvent demander le remboursement immédiat des créances constatées au titre de l'année de leur création et des quatre années suivantes ;
2° Les entreprises ayant fait l'objet d'une procédure de conciliation ou de sauvegarde, d'un redressement ou d'une liquidation judiciaires. Elles peuvent demander le remboursement de leur créance non utilisée à compter de la date de la décision ou du jugement ouvrant ces procédures ;
3° Les jeunes entreprises innovantes mentionnées à l'article 44 sexies-0 A ;
4° Les entreprises répondant à la définition des micro, petites et moyennes entreprises donnée à l'annexe I au règlement (UE) n° 651/2014 de la Commission du 17 juin 2014 déclarant certaines catégories d'aides compatibles avec le marché intérieur en application des articles 107 et 108 du traité.
Les entreprises créées depuis moins de deux ans qui demandent le remboursement immédiat de la créance de crédit d'impôt pour dépenses de recherche doivent joindre à leur demande les pièces justificatives attestant la réalité des dépenses de recherche.
III. – (Périmé).
IV. – (Abrogé).
''',
    "Réécriture à droit constant : désignation du contribuable qui impute le crédit, présentation du report sur trois ans et du remboursement du solde, puis clarification des catégories admises au remboursement immédiat. La condition d'absence de dépendance est isolée au sein du c, sans déplacement d'alinéa. Aucune suppression de niche ni autre réforme de fond non définie par policy.json n'est ajoutée.",
    "Maintien des trois années de report, du 1er janvier 2004, des seuils de 50 %, de l'année de création et des quatre suivantes, ainsi que de la justification renforcée avant deux ans. Conserver les deux séries de renvois financiers, le I de l'article 151 nonies et la référence historique à L. 214-37 antérieure à l'ordonnance de 2013. Les mentions III périmé et IV abrogé restent en place.")

add('199 ter B bis', '''
I. – Le contribuable impute le crédit d'impôt en faveur de la recherche collaborative défini à l'article 244 quater B bis sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'organisme de recherche et de diffusion des connaissances a facturé les dépenses de recherche retenues pour calculer ce crédit. L'excédent constitue pour l'entreprise une créance sur l'Etat d'un montant égal à cet excédent. Cette créance sert au paiement de l'impôt sur le revenu dû au titre des trois années suivant celle au titre de laquelle elle est constatée ; la fraction qui reste inutilisée à l'issue de cette période est remboursée.
La créance est inaliénable et incessible, sous réserve des cas et conditions prévus aux articles L. 214-169 à L. 214-190 et L. 313-23 à L. 313-35 du code monétaire et financier.
Lorsqu'une fusion ou une opération assimilée intervient pendant la période mentionnée à la dernière phrase du premier alinéa du présent I, la fraction de la créance que la société apporteuse n'a pas encore imputée est transférée à la société bénéficiaire de l'apport.
La fraction du crédit d'impôt en faveur de la recherche collaborative correspondant aux parts des personnes physiques autres que celles mentionnées au I de l'article 151 nonies ne peut être ni imputée ni restituée.
II. – Les entreprises suivantes ont droit au remboursement immédiat de la créance mentionnée au premier alinéa du I du présent article lorsqu'elles la constatent :
1° Les entreprises nouvelles, à l'exclusion de celles mentionnées au III de l'article 44 sexies, dont le capital est entièrement libéré et est détenu de manière continue à hauteur d'au moins 50 % :
a) Par des personnes physiques ;
b) Ou par une société dont au moins 50 % du capital est détenu par des personnes physiques ;
c) Ou par des sociétés de capital-risque, des fonds communs de placement à risques, des fonds professionnels spécialisés relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, des fonds professionnels de capital investissement, des sociétés de libre partenariat, des sociétés de développement régional, des sociétés financières d'innovation ou des sociétés unipersonnelles d'investissement à risque. Dans ce cas, aucun lien de dépendance au sens du 12 de l'article 39 du présent code ne doit exister entre les entreprises et ces sociétés ou ces fonds.
Ces entreprises peuvent demander le remboursement immédiat des créances constatées au titre de l'année de leur création et des quatre années suivantes ;
2° Les entreprises ayant fait l'objet d'une procédure de conciliation ou de sauvegarde, d'un redressement ou d'une liquidation judiciaires. Elles peuvent demander le remboursement de leur créance non utilisée à compter de la date de la décision ou du jugement ouvrant ces procédures ;
3° Les jeunes entreprises innovantes mentionnées à l'article 44 sexies-0 A ;
4° Les entreprises répondant à la définition des micro, petites et moyennes entreprises donnée à l'annexe I au règlement (UE) n° 651/2014 de la Commission du 17 juin 2014 déclarant certaines catégories d'aides compatibles avec le marché intérieur en application des articles 107 et 108 du traité.
''',
    "Réécriture à droit constant : explicitation du fait générateur fondé sur la facturation par l'organisme, du report et des conditions de remboursement immédiat. Les alinéas matérialisés par des doubles br dans la source deviennent des paragraphes dans le même ordre. Aucune réforme de fond ni condition propre au crédit de recherche ordinaire n'est transposée.",
    "Préserver la distinction entre dépenses facturées ici et dépenses exposées à l'article 199 ter B. Maintien du délai de trois ans, des seuils de 50 %, de l'année de création et des quatre suivantes, des renvois financiers et de la référence historique à L. 214-37. La note source, III de l'article 69 de la loi n° 2021-1900 du 30 décembre 2021, limite l'application aux dépenses facturées au titre de contrats de collaboration conclus à compter du 1er janvier 2022 ; elle ne permet pas d'étendre le dispositif aux contrats antérieurs.")

add('199 ter C', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater C sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle les rémunérations retenues pour calculer ce crédit ont été versées. L'excédent constitue pour le contribuable une créance sur l'Etat d'un montant égal à cet excédent. Cette créance sert au paiement de l'impôt sur le revenu dû au titre des trois années suivant celle au titre de laquelle elle est constatée ; la fraction qui reste inutilisée à l'issue de cette période est remboursée.
La créance est inaliénable et incessible, sous réserve des cas et conditions prévus aux articles L. 313-23 à L. 313-35 du code monétaire et financier. Dans ces cas, elle ne peut faire l'objet de plusieurs cessions ou nantissements partiels auprès d'un ou de plusieurs cessionnaires ou créanciers.
Lorsque la créance a été cédée ou nantie en application du deuxième alinéa de l'article L. 313-23 du même code avant la liquidation de l'impôt sur le revenu sur lequel le crédit correspondant s'impute, son montant est celui du crédit d'impôt avant imputation. Cette règle s'applique à condition que l'administration ait été préalablement informée de la cession ou du nantissement.
Lorsqu'une fusion ou une opération assimilée intervient pendant la période mentionnée à la dernière phrase du premier alinéa du présent I, la fraction de la créance que la société apporteuse n'a pas encore imputée est transférée à la société bénéficiaire de l'apport.
II. – Les entreprises suivantes ont droit au remboursement immédiat de la créance mentionnée au premier alinéa du I lorsqu'elles la constatent :
1° Les entreprises répondant à la définition des micro, petites et moyennes entreprises donnée à l'annexe I au règlement (UE) n° 651/2014 de la Commission du 17 juin 2014 déclarant certaines catégories d'aides compatibles avec le marché intérieur en application des articles 107 et 108 du traité ;
2° Les entreprises nouvelles, à l'exclusion de celles mentionnées au III de l'article 44 sexies, dont le capital est entièrement libéré et est détenu de manière continue à hauteur d'au moins 50 % :
a) Par des personnes physiques ;
b) Ou par une société dont au moins 50 % du capital est détenu par des personnes physiques ;
c) Ou par des sociétés de capital-risque, des fonds communs de placement à risques, des fonds professionnels spécialisés relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, des fonds professionnels de capital investissement, des sociétés de libre partenariat, des sociétés de développement régional, des sociétés financières d'innovation ou des sociétés unipersonnelles d'investissement à risque. Dans ce cas, aucun lien de dépendance au sens du 12 de l'article 39 ne doit exister entre les entreprises et ces sociétés ou ces fonds.
Ces entreprises peuvent demander le remboursement immédiat des créances constatées au titre de l'année de leur création et des quatre années suivantes ;
3° Les jeunes entreprises innovantes mentionnées à l'article 44 sexies-0 A ;
4° Les entreprises ayant fait l'objet d'une procédure de conciliation ou de sauvegarde, d'un redressement ou d'une liquidation judiciaire. Elles peuvent demander le remboursement de leur créance non utilisée à compter de la date de la décision ou du jugement ouvrant ces procédures.
''',
    "Réécriture à droit constant : clarification des étapes de calcul de la créance, de la cession avant liquidation et du remboursement immédiat. Les conditions de détention et les catégories d'entreprises restent à leur place. Le régime du crédit de l'article 244 quater C n'est pas remplacé par l'allègement employeur envisagé dans policy.json.",
    "Maintien des trois années de report, de l'interdiction de cessions ou nantissements partiels multiples, de l'information préalable de l'administration, des seuils de 50 % et des quatre années après la création. La note source indique que les mots « des trois derniers alinéas » au c du 2° du II deviennent sans objet, en conséquence de l'article 37-I-1° a de la loi n° 2018-1317 du 28 décembre 2018 ; ces mots ne figurent déjà plus dans le texte fourni. La référence à L. 214-37 dans sa rédaction antérieure à l'ordonnance de 2013 est maintenue.")


add('199 ter D', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater E sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle les biens éligibles sont acquis, créés ou loués. Lorsque l'exercice au cours duquel ces biens sont acquis, créés ou loués ne coïncide pas avec l'année civile, le crédit est imputé sur l'impôt sur le revenu dû au titre de l'année de clôture de cet exercice. L'excédent du crédit sur l'impôt dû au titre de cette année sert au paiement de l'impôt sur le revenu dû au titre des neuf années suivantes. A l'issue de cette période, le solde non utilisé est remboursé dans la double limite de 50 % du crédit d'impôt et de 300 000 €.
Toutefois, le solde non utilisé peut, à la demande du redevable, être remboursé à compter de la cinquième année, dans la double limite de 35 % du crédit d'impôt et de 300 000 €.
La créance sur l'Etat correspondant au crédit d'impôt non utilisé est inaliénable et incessible, sous réserve des cas et conditions prévus aux articles L. 313-23 à L. 313-35 du code monétaire et financier. Cette créance n'est pas imposable.
Lors d'une opération mentionnée au deuxième alinéa du III de l'article 244 quater E, la fraction de la créance non encore imputée est transférée au bénéficiaire de la transmission.
Lorsqu'une fusion ou une opération assimilée bénéficie du régime prévu à l'article 210 A et intervient au cours de la période visée à la deuxième phrase du premier alinéa, la fraction de la créance que la société absorbée ou apporteuse n'a pas encore imputée est transférée, pour sa valeur nominale, à la ou aux sociétés bénéficiaires des apports.
En cas de scission ou d'apport partiel d'actif, la créance est transmise à la ou aux sociétés bénéficiaires des apports en proportion de l'actif net réel apporté.
II. – Les entreprises suivantes ont droit au remboursement immédiat de la créance mentionnée au premier alinéa du I lorsqu'elles la constatent :
1° Les entreprises, à l'exclusion de celles mentionnées au III de l'article 44 sexies, dont le capital est entièrement libéré et est détenu de manière continue à hauteur d'au moins 50 % :
a) Par des personnes physiques ;
b) Ou par une société dont au moins 50 % du capital est détenu par des personnes physiques ;
c) Ou par des sociétés de capital-risque, des fonds communs de placement à risques, des fonds professionnels spécialisés relevant de l'article L. 214-37 du code monétaire et financier dans sa rédaction antérieure à l'ordonnance n° 2013-676 du 25 juillet 2013 modifiant le cadre juridique de la gestion d'actifs, des fonds professionnels de capital investissement, des sociétés de libre partenariat, des sociétés de développement régional, des sociétés financières d'innovation ou des sociétés unipersonnelles d'investissement à risque. Dans ce cas, aucun lien de dépendance au sens du 12 de l'article 39 ne doit exister entre les entreprises et ces sociétés ou ces fonds.
Ces entreprises peuvent demander le remboursement immédiat des créances constatées au titre de l'année de leur création et des quatre années suivantes ;
2° Les entreprises ayant fait l'objet d'une procédure de conciliation ou de sauvegarde, d'un redressement ou d'une liquidation judiciaires. Elles peuvent demander le remboursement de leur créance non utilisée à compter de la date de la décision ou du jugement ouvrant ces procédures ;
3° Les jeunes entreprises innovantes mentionnées à l'article 44 sexies-0 A ;
4° Les entreprises répondant à la définition des micro, petites et moyennes entreprises donnée à l'annexe I au règlement (UE) n° 651/2014 de la Commission du 17 juin 2014 déclarant certaines catégories d'aides compatibles avec le marché intérieur en application des articles 107 et 108 du traité.
''',
    "Réécriture à droit constant : clarification de l'année d'imputation, des deux plafonds cumulatifs de remboursement et des transferts de créance. Les conditions de remboursement immédiat sont rendues plus directes, sans changer les alinéas, les catégories ni les taux. Aucune réforme de fond de l'investissement en Corse n'est définie pour cet article.",
    "Contrôle des neuf années, de la cinquième année, des limites de 50 % ou 35 % et de 300 000 €, des seuils de détention de 50 % et des quatre années après la création. Ambiguïté préexistante conservée au cinquième alinéa du I : le renvoi à la « deuxième phrase du premier alinéa » vise une phrase relative à l'exercice non civil, alors que les neuf années de report figurent à la troisième phrase. Une correction de ce renvoi exige une coordination explicite. Le deuxième alinéa du III de l'article 244 quater E, vérifié dans le corpus local, vise les transmissions sous les régimes des articles 41, 151 octies, 151 octies A, 210 A ou 210 B ; son renvoi est conservé.")

add('199 ter E', '''
Le contribuable impute le crédit d'impôt défini à l'article 244 quater F sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'entreprise a engagé les dépenses. La part du crédit qui dépasse l'impôt dû au titre de cette année lui est restituée.
''',
    "Réécriture à droit constant : le contribuable est désigné comme auteur de l'imputation et l'excédent restituable est défini directement. Le fait générateur demeure l'engagement des dépenses par l'entreprise. Aucune réforme de fond de ce crédit n'est introduite.",
    "Renvoi à l'article 244 quater F conservé. Ne pas substituer une condition de paiement ou de facturation à l'engagement des dépenses ; l'excédent est restitué au titre de la même année sans création d'un report.")

add('199 ter I', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater J sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'établissement de crédit ou la société de financement a versé des avances remboursables dans les conditions prévues à cet article, à hauteur d'un cinquième de son montant. Le reste est imputé par fractions égales sur l'impôt sur le revenu dû au titre des quatre années suivantes. Pour l'année du versement et chacune des quatre années suivantes, la part de la fraction du crédit qui dépasse l'impôt dû est restituée.
II. – 1. Si, pendant la durée de remboursement de l'avance et tant qu'elle n'est pas intégralement remboursée, il apparaît que les conditions d'octroi mentionnées au I de l'article 244 quater J n'ont pas été respectées, l'établissement de crédit ou la société de financement reverse le crédit d'impôt. Par exception, lorsque le bénéficiaire ne respecte pas les conditions de justification des ressources qu'il a déclarées, l'Etat exige du bénéficiaire le remboursement de l'avantage indûment perçu. Cet avantage ne peut dépasser le montant du crédit d'impôt majoré de 25 %. Un décret en Conseil d'Etat définit les modalités de restitution de l'avantage indu par le bénéficiaire de l'avance remboursable sans intérêt.
2. Si, pendant la durée de remboursement de l'avance et tant qu'elle n'est pas intégralement remboursée, les conditions d'octroi relatives à l'affectation du logement et à ses caractéristiques, mentionnées au I de l'article 244 quater J, cessent d'être respectées, l'établissement de crédit ou la société de financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
3. L'établissement de crédit ou la société de financement peut prévoir dans son offre d'avance remboursable sans intérêt de rendre l'avance exigible auprès des bénéficiaires dans les cas mentionnés aux 1 et 2, selon des modalités définies par décret en Conseil d'Etat.
III. – Si l'avance remboursable mentionnée à l'article 244 quater J est remboursée par anticipation pendant la durée d'imputation du crédit d'impôt, l'établissement de crédit ou la société de financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
''',
    "Réécriture à droit constant : décomposition de l'imputation sur cinq années et désignation explicite du débiteur du reversement, avec maintien de l'exception portant sur les ressources déclarées. Les subdivisions et les distinctions entre octroi, maintien et remboursement anticipé sont conservées. Aucune réforme de fond ni extension aux prêts nouveaux n'est décidée ici.",
    "Conserver un cinquième puis quatre fractions égales, la majoration de 25 %, les deux décrets en Conseil d'Etat et les renvois au I de l'article 244 quater J. La note source prévoit un décret d'application, notamment pour les obligations déclaratives, et vise les avances émises entre le 1er février 2005 et le 31 décembre 2009. Décalage temporel à contrôler : l'article 244 quater J du corpus local porte une note d'entrée en vigueur au 1er janvier 2026, issue du XI de l'article 42 de la loi n° 2026-103 du 19 février 2026. La présente réécriture ne résout pas ce décalage et ne prolonge pas tacitement le champ historique indiqué dans la source assignée.")

add('199 ter K', '''
Le contribuable impute le crédit d'impôt défini à l'article 244 quater L sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'entreprise a respecté les conditions prévues à cet article. La part du crédit qui dépasse l'impôt dû au titre de cette année lui est restituée.
''',
    "Réécriture à droit constant : formulation active de l'imputation et identification directe de l'excédent à restituer. L'année de respect des conditions demeure l'année de référence. Aucune réforme de fond n'est apportée au crédit défini par l'article 244 quater L.",
    "Renvoi à l'article 244 quater L maintenu. La réécriture conserve le critère propre à cet article, le respect des conditions par l'entreprise, et ne lui substitue pas un critère de dépenses engagées ou payées.")

add('199 ter N', '''
Le contribuable impute le crédit d'impôt défini à l'article 244 quater O sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle les dépenses définies à cet article ont été exposées. La part du crédit qui dépasse l'impôt dû au titre de cette année lui est restituée.
''',
    "Réécriture à droit constant : désignation du contribuable qui impute le crédit et formulation directe de la restitution du surplus. Le rattachement aux dépenses exposées est préservé. Aucune réforme de fond du crédit de l'article 244 quater O n'est introduite.",
    "Renvoi à l'article 244 quater O et année d'exposition des dépenses conservés. Aucun report ni nouveau délai de remboursement n'est créé.")

add('199 ter S', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater U sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'établissement de crédit, la société de financement ou la société de tiers-financement a versé des avances remboursables dans les conditions prévues à cet article, à hauteur d'un cinquième de son montant. Le reste est imputé par fractions égales sur l'impôt sur le revenu dû au titre des quatre années suivantes. Pour l'année du versement et chacune des quatre années suivantes, la part de la fraction du crédit qui dépasse l'impôt dû est restituée.
II. – 1. Si, pendant la durée de remboursement de l'avance et tant qu'elle n'est pas intégralement remboursée, il apparaît que les conditions d'octroi mentionnées aux I, VI bis et VI ter de l'article 244 quater U n'ont pas été respectées, l'établissement de crédit, la société de financement ou la société de tiers-financement reverse le crédit d'impôt.
Par exception :
a) Lorsque le devis ou la facture concernant tout ou partie des travaux financés ne permet pas de justifier les informations du descriptif mentionné au 5 du même I, l'entreprise qui réalise ces travaux est redevable d'une amende égale à 10 % du montant des travaux non justifié. Le montant de l'amende ne peut dépasser celui du crédit d'impôt. Un décret fixe les modalités d'application du présent a ;
b) Lorsque le bénéficiaire ne justifie pas de la réalisation ou de l'éligibilité des travaux dans le délai prévu au 5 dudit I, et hors les cas mentionnés au a du présent 1, l'Etat exige du bénéficiaire le remboursement de l'avantage indûment perçu. Cet avantage ne peut dépasser le montant du crédit d'impôt majoré de 25 %. Un décret définit les modalités de restitution de l'avantage indu par le bénéficiaire de l'avance remboursable sans intérêt.
2. Si, pendant la durée de remboursement de l'avance et tant qu'elle n'est pas intégralement remboursée, les conditions d'octroi relatives à l'affectation du logement, mentionnées au I de l'article 244 quater U, cessent d'être respectées, l'établissement de crédit, la société de financement ou la société de tiers-financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
3. L'établissement de crédit, la société de financement ou la société de tiers-financement peut prévoir dans son offre d'avance remboursable sans intérêt de rendre l'avance exigible auprès des bénéficiaires dans les cas mentionnés au premier alinéa du 1 et au 2, selon des modalités définies par décret.
III. – Si l'avance remboursable mentionnée à l'article 244 quater U est remboursée par anticipation pendant la durée d'imputation du crédit d'impôt, l'établissement de crédit, la société de financement ou la société de tiers-financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
''',
    "Réécriture à droit constant : séparation de l'échéancier d'imputation et mise en évidence des responsables respectifs du reversement, de l'amende et de la restitution de l'avantage indu. Les exceptions a et b ainsi que le renvoi au premier alinéa du 1 restent à leur emplacement. Aucune réforme de fond du financement des travaux n'est ajoutée.",
    "Contrôle d'un cinquième puis des quatre années suivantes, des taux de 10 % et 25 % et du plafond de l'amende égal au crédit. Les renvois aux I, VI bis et VI ter, au 5 du I et au premier alinéa du 1 sont préservés ; le III reste limité au remboursement anticipé pendant l'imputation. La note source, A du II de l'article 87 de la loi n° 2025-127 du 14 février 2025, vise le 1° du I de cet article et les offres émises à compter du 1er avril 2024 ; ne pas transformer cette règle particulière en nouvelle date générale du dispositif.")

add('199 ter T', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater V sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'établissement de crédit ou la société de financement a versé des prêts ne portant pas intérêt, à hauteur d'un cinquième de son montant. Le reste est imputé par fractions égales sur l'impôt sur le revenu dû au titre des quatre années suivantes. Pour l'année du versement et chacune des quatre années suivantes, la part de la fraction du crédit qui dépasse l'impôt dû est restituée.
II. – Si, pendant la durée du prêt et tant qu'il n'est pas intégralement remboursé, il apparaît que les conditions mentionnées au chapitre X du titre Ier du livre III du code de la construction et de l'habitation n'ont pas été respectées, l'établissement de crédit ou la société de financement reverse la différence entre le crédit d'impôt correspondant au prêt effectivement octroyé et celui correspondant au prêt qui aurait dû être octroyé à l'emprunteur. Le montant reversé est majoré de 40 % si l'établissement ou la société n'a pas spontanément déclaré, dans le délai fixé par décret, l'événement justifiant ce reversement à la société de gestion mentionnée à l'article L. 31-10-14 du même code.
III. – Pendant la durée du prêt et tant qu'il n'est pas intégralement remboursé, l'établissement de crédit ou la société de financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer si les conditions de maintien du prêt mentionnées à l'article L. 31-10-6 du code de la construction et de l'habitation cessent d'être respectées ou si le prêt est remboursé par anticipation. Si l'établissement ou la société ne déclare pas spontanément ces événements, dans le délai fixé par décret, à la société de gestion mentionnée à l'article L. 31-10-14 du même code, il reverse en outre une somme égale à 40 % du montant des fractions de crédit d'impôt restant à imputer.
''',
    "Réécriture à droit constant : présentation de l'imputation annuelle en étapes et formulation active des reversements. La distinction entre la différence de crédit au II et les fractions restant à imputer au III est conservée, avec leurs sanctions propres. Aucune réforme de fond du prêt n'est définie dans policy.json.",
    "Maintien d'un cinquième puis de quatre années, des deux taux de 40 % et de leurs assiettes distinctes. Renvois conservés au chapitre X du titre Ier du livre III du CCH, à L. 31-10-6 et à L. 31-10-14. La note source mentionne les coordinations résultant des articles 8 [14°] et 36 de l'ordonnance n° 2013-544 du 27 juin 2013 ; elle ne fixe pas une entrée en vigueur de la réforme projetée.")

add('199 ter U', '''
L'entreprise impute le crédit d'impôt défini à l'article 244 quater W sur l'impôt sur le revenu dû au titre de l'exercice au cours duquel survient l'événement prévu au IV du même article. La part du crédit qui dépasse l'impôt dû au titre de cet exercice lui est restituée.
Lorsque la créance a été cédée ou nantie en application du deuxième alinéa de l'article L. 313-23 du code monétaire et financier avant la liquidation de l'impôt sur le revenu sur lequel le crédit correspondant s'impute, le montant du crédit avant imputation constitue une créance sur l'Etat. Cette règle s'applique à condition que l'administration ait été préalablement informée de la cession ou du nantissement.
La créance est inaliénable et incessible, sous réserve des cas et conditions prévus aux articles L. 313-23 à L. 313-35 du même code. Dans ces cas, elle ne peut faire l'objet de plusieurs cessions ou nantissements partiels auprès d'un ou de plusieurs cessionnaires ou créanciers.
Lorsque la créance a été cédée ou nantie dans les conditions du deuxième alinéa et que le crédit d'impôt fait l'objet d'une reprise dans les conditions du VIII de l'article 244 quater W, cette reprise est effectuée auprès :
1° Des entreprises mentionnées au 1 du I du même article 244 quater W, dans la limite du prix de cession ou du nantissement de la créance ;
2° Du cessionnaire ou du bénéficiaire du nantissement de la créance, dans la limite de la différence entre le montant du crédit d'impôt et le prix d'acquisition ou du nantissement de la créance.
Un décret fixe, en cas de construction d'immeuble, les modalités de cession et de nantissement de la créance.
''',
    "Réécriture à droit constant : mise au premier plan de l'entreprise et des conditions de constitution de la créance avant imputation, puis clarification des deux limites de reprise. Les sept alinéas et les deux débiteurs visés sont maintenus. Aucune réforme de fond de l'investissement outre-mer n'est introduite.",
    "Renvois au IV, au VIII et au 1 du I de l'article 244 quater W, au deuxième alinéa de L. 313-23 et à L. 313-23 à L. 313-35 conservés. La source emploie les expressions « prix de cession ou du nantissement » et « prix d'acquisition ou du nantissement » : leur portée en matière de nantissement mérite contrôle, sans substitution d'une nouvelle assiette. La première note source mentionne le 1er juillet 2014 sous réserve européenne ; la seconde précise que l'article 67 de la loi n° 2014-1655 du 29 décembre 2014 a modifié le III de l'article 21 de la loi n° 2013-1278 et retient les investissements réalisés à compter du 1er janvier 2015. Ces deux étapes historiques ne sont pas confondues.")

add('199 ter V', '''
I. – Le contribuable impute le crédit d'impôt défini à l'article 244 quater T sur l'impôt sur le revenu dû au titre de l'année au cours de laquelle l'établissement de crédit, la société de financement ou la société de tiers-financement a versé des prêts avance mutation ne portant pas intérêt dans les conditions prévues au même article 244 quater T, à hauteur d'un cinquième de son montant. Le reste est imputé par fractions égales sur l'impôt sur le revenu dû au titre des quatre années suivantes. Pour l'année du versement et chacune des quatre années suivantes, la part de la fraction du crédit qui dépasse l'impôt dû est restituée.
II. – A. – Si, pendant la durée du prêt avance mutation ne portant pas intérêt et tant qu'il n'est pas intégralement remboursé, il apparaît que les conditions d'octroi mentionnées au I de l'article 244 quater T n'ont pas été respectées, l'établissement de crédit, la société de financement ou la société de tiers-financement reverse le crédit d'impôt.
Par exception :
1° Lorsque le devis ou la facture concernant tout ou partie des travaux financés ne permet pas de justifier les informations du descriptif mentionné au 5 du I de l'article 244 quater U, l'entreprise qui réalise ces travaux est redevable d'une amende égale à 10 % du montant des travaux non justifié. Le montant de l'amende ne peut dépasser celui du crédit d'impôt. Un décret fixe les modalités d'application du présent 1° ;
2° Lorsque le bénéficiaire ne justifie pas de la réalisation ou de l'éligibilité des travaux dans le délai prévu au 5 du I de l'article 244 quater U, et hors les cas mentionnés au 1° du présent A, l'Etat exige du bénéficiaire le remboursement de l'avantage indûment perçu. Cet avantage ne peut dépasser le montant du crédit d'impôt majoré de 25 %. Un décret définit les modalités de restitution de l'avantage indu par le bénéficiaire du prêt avance mutation ne portant pas intérêt.
B. – Si, pendant la durée du prêt avance mutation ne portant pas intérêt et tant qu'il n'est pas intégralement remboursé, les conditions d'octroi relatives à l'affectation du logement, mentionnées au C du I de l'article 244 quater T, cessent d'être respectées, l'établissement de crédit, la société de financement ou la société de tiers-financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
C. – L'établissement de crédit, la société de financement ou la société de tiers-financement peut prévoir dans son offre de prêt avance mutation ne portant pas intérêt de rendre ce prêt exigible auprès des bénéficiaires dans les cas mentionnés au premier alinéa du A et au B du présent II, selon des modalités définies par décret.
III. – En cas de remboursement anticipé du prêt avance mutation ne portant pas intérêt mentionné à l'article 244 quater T, l'établissement de crédit, la société de financement ou la société de tiers-financement ne peut plus utiliser les fractions de crédit d'impôt restant à imputer.
''',
    "Réécriture à droit constant : décomposition de l'imputation et explicitation des débiteurs du reversement et des exceptions relatives aux travaux. La structure II A, B et C et le III sont maintenus, sans ajouter au III la restriction temporelle propre à l'article 199 ter S. Aucune réforme de fond de ce prêt n'est introduite.",
    "Maintien d'un cinquième puis de quatre années, des taux de 10 % et 25 %, du plafond de l'amende et des renvois au 5 du I de l'article 244 quater U, au C du I de l'article 244 quater T et au premier alinéa du A. La note source, B du II de l'article 87 de la loi n° 2025-127 du 14 février 2025, vise le 2° du I de cet article et les offres d'avance remboursable ne portant pas intérêt émises à compter du 1er avril 2024. Son articulation avec la note de l'article 244 quater T du corpus local, qui vise les prêts avance mutation émis du 1er septembre 2024 au 31 décembre 2027, doit être contrôlée ; aucune de ces dates n'est étendue par la réécriture.")


add('199 quater', '''
Les indemnités et les pensions mentionnées aux 1 et 5 de l'article 12 de la décision du Parlement européen 2005/684/CE du 28 septembre 2005 portant adoption du statut des députés au Parlement européen ouvrent droit, lorsqu'elles sont soumises à l'impôt européen mentionné au même article 12, à un crédit d'impôt destiné à éviter leur double imposition. Ce crédit est égal au montant de l'impôt européen acquitté, sans pouvoir dépasser l'impôt dû en France sur ces indemnités et pensions.
''',
    "Réécriture à droit constant : distinction en deux phrases du champ des indemnités et pensions et du calcul plafonné du crédit contre la double imposition. Aucune réforme de fond de leur imposition ou de leur revalorisation n'est appliquée.",
    "Maintien des 1 et 5 de l'article 12 de la décision 2005/684/CE du 28 septembre 2005 et du plafond égal à l'impôt français sur les mêmes revenus. La note source, II de l'article 35 de la loi n° 2022-1726 du 30 décembre 2022, prévoit l'application aux indemnités et pensions perçues à compter du 1er janvier 2022. Le projet de transition des retraites ne modifie pas ce mécanisme distinct.")

add('199 quater A', '''
Les contribuables fiscalement domiciliés hors de France sont libérés de l'impôt sur le revenu dû au titre des sommes qui ont supporté la retenue prévue au 2 de l'article 119 bis.
''',
    "Réécriture à droit constant : les contribuables bénéficiaires deviennent le sujet de la règle libératoire, dont le champ reste limité aux sommes ayant supporté la retenue. Aucune réforme de fond de l'imposition des non-résidents n'est introduite.",
    "Renvoi au 2 de l'article 119 bis maintenu. La libération ne concerne que l'impôt sur le revenu dû au titre des sommes ayant effectivement supporté cette retenue et les contribuables fiscalement domiciliés hors de France.")

add('199 quater C', '''
Les versements de cotisations aux organisations syndicales représentatives de salariés et de fonctionnaires au sens de l'article L. 2121-1 du code du travail, ainsi qu'aux associations professionnelles nationales de militaires représentatives au sens de l'article L. 4126-8 du code de la défense, ouvrent droit à un crédit d'impôt sur le revenu.
Le crédit d'impôt est calculé au taux de 66 % sur les cotisations versées, retenues dans la limite de 1 % du revenu brut désigné à l'article 83, après déduction des cotisations et contributions mentionnées aux 1° à 2° ter du même article.
Les bénéficiaires de traitements et salaires admis à justifier du montant de leurs frais réels ne peuvent pas bénéficier de ce crédit d'impôt.
La part du crédit d'impôt qui dépasse l'impôt dû est remboursée.
Pour bénéficier du crédit d'impôt au titre des cotisations versées, le contribuable doit pouvoir présenter, à la demande de l'administration fiscale, un reçu du syndicat ou de l'association nationale professionnelle de militaires indiquant le montant et la date du versement.
''',
    "Réécriture à droit constant : clarification du calcul sur cotisations plafonnées, formulation directe de l'exclusion liée aux frais réels et de la condition de présentation d'un reçu à la demande de l'administration. Les cinq alinéas et le remboursement de l'excédent sont conservés. Aucune réforme de fond du crédit syndical n'est introduite.",
    "Contrôle des 66 %, du plafond de 1 % et de sa base, après les seules déductions visées aux 1° à 2° ter de l'article 83. Les renvois à L. 2121-1 du code du travail et L. 4126-8 du code de la défense restent inchangés. La coordination CSG de l'article 154 quinquies ne justifie pas de réécrire ici les catégories de cotisations déductibles de la base du plafond.")

add('199 quater F', '''
Les contribuables ayant leur domicile fiscal en France bénéficient d'une réduction d'impôt sur le revenu pour les enfants à leur charge qui poursuivent des études secondaires ou supérieures pendant l'année scolaire en cours au 31 décembre de l'année d'imposition.
La réduction d'impôt est fixée aux montants suivants :
61 € par enfant qui fréquente un collège ;
153 € par enfant qui fréquente un lycée d'enseignement général et technologique ou un lycée professionnel ;
183 € par enfant qui suit une formation d'enseignement supérieur.
Ces montants sont divisés par deux lorsque l'enfant est réputé à charge égale de l'un et l'autre de ses parents (1).
Pour bénéficier de la réduction, le contribuable doit indiquer dans sa déclaration des revenus, pour chaque enfant concerné, ses nom et prénom ainsi que le nom de l'établissement scolaire et la classe qu'il fréquente ou le nom de l'établissement supérieur dans lequel il est inscrit.
Les dispositions du 5 du I de l'article 197 s'appliquent à cette réduction.
''',
    "Réécriture à droit constant : formulation directe des conditions de scolarité et des mentions que le contribuable doit déclarer. Les huit alinéas, les trois montants et la règle de partage entre parents sont conservés. Aucune réforme de fond des frais de scolarité n'est introduite.",
    "Maintien du 31 décembre, des 61 €, 153 € et 183 €, de la division par deux et du renvoi au 5 du I de l'article 197. L'appel (1) est conservé ; la note source précise que la disposition correspondante s'applique pour l'imposition des revenus des années 2003 et suivantes.")

add('199 septies', '''
I. – Les primes mentionnées aux 1° et 2° ouvrent droit, lorsqu'elles ne sont pas prises en compte pour évaluer les revenus des différentes catégories, à une réduction d'impôt sur le revenu égale à 25 % de leur montant. Elles sont retenues dans la limite d'un plafond global de versements annuels de 1 525 €, majoré de 300 € par personne à charge :
1° Les primes des contrats d'assurance en cas de décès qui garantissent le versement d'un capital ou d'une rente viagère à un enfant de l'assuré, à tout autre parent de l'assuré en ligne directe ou collatérale jusqu'au troisième degré, ou à une personne réputée à sa charge en application de l'article 196 A bis. Ces bénéficiaires doivent être atteints d'une infirmité les empêchant soit d'exercer une activité professionnelle dans des conditions normales de rentabilité, soit d'acquérir une instruction ou une formation professionnelle d'un niveau normal ;
2° Les primes des contrats d'assurance d'une durée effective d'au moins six ans dont l'exécution dépend de la durée de la vie humaine, lorsque ces contrats sont destinés à garantir à l'assuré le versement d'un capital en cas de vie ou d'une rente viagère dont la jouissance est effectivement différée d'au moins six ans, quelle que soit la date de souscription. L'assuré doit être atteint, lors de la conclusion du contrat, d'une infirmité l'empêchant d'exercer une activité professionnelle dans des conditions normales de rentabilité ;
3° Un arrêté du ministre de l'économie et des finances définit les justificatifs exigés pour bénéficier de la réduction d'impôt.
II. – Les personnes qui n'ont pas leur domicile fiscal en France au sens de l'article 4 B sont exclues de la réduction d'impôt prévue au I. Les dispositions du 5 du I de l'article 197 s'appliquent à cette réduction.
''',
    "Réécriture à droit constant : séparation du taux et du plafond global, puis distinction des garanties et des conditions d'infirmité au sein de chacun des 1° et 2°. Les cinq alinéas, le 3° réglementaire et l'exclusion des non-résidents sont maintenus. Le projet de capitalisation des retraites n'est pas appliqué à ces contrats d'assurance distincts.",
    "Contrôle des 25 %, de 1 525 €, de 300 € par personne à charge, du troisième degré et des deux exigences de six ans au 2° : durée effective du contrat et différé effectif de jouissance de la rente. Conserver l'infirmité à la conclusion au 2° et la mention « quelle que soit la date de la souscription », sans transition inventée. Renvois aux articles 196 A bis, 4 B et 197, I, 5 conservés. La structure préexistante place au 3° une disposition réglementaire sous une introduction relative aux primes ; cette particularité est conservée sans renumérotation.")


assert len(sources) == 21
assert len(drafts) == 21
assert set(drafts) == {s['number'] for s in sources}
answer = []
for source in sources:
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        **drafts[source['number']],
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
