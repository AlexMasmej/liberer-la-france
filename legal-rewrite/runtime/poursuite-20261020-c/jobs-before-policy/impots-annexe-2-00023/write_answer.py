import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


add('330', '''
<p>Le redevable bénéficie de l'exonération de taxe foncière sur les propriétés non bâties si la valeur locative totale des parcelles qu'il possède dans la commune n'excède pas 30 % de la valeur locative d'un hectare de terre de la meilleure catégorie existant dans cette commune.</p>
''', "Réécriture à droit constant : la taxe concernée et la condition ouvrant droit à l'exonération sont rattachées directement au redevable. Aucune réforme de fond de l'exonération n'est introduite.", "Le plafond de 30 % s'apprécie sur la valeur locative totale des parcelles possédées dans la commune, par comparaison avec un hectare de terre de la meilleure catégorie de cette même commune. Le seuil demeure inclusif.")

add('330 A', '''
<p>Les constructions nouvelles, les changements de consistance ou d'affectation des propriétés bâties ou non bâties et les changements d'utilisation des propriétés bâties mentionnées au I de l'article 1498 du code général des impôts doivent être déclarés à l'administration lorsqu'ils surviennent après le début des travaux d'évaluation. Ces déclarations sont effectuées dans les conditions prévues à l'article 1406 du même code.</p>
<p>Les propriétaires peuvent demander aux agents de l'administration de les aider à remplir les formulaires de déclaration.</p>
''', "Réécriture à droit constant : les événements à déclarer et leur condition temporelle sont distingués du renvoi aux modalités déclaratives ; l'aide facultative aux propriétaires est formulée directement. Aucune réforme de fond des obligations déclaratives n'est appliquée.", "Les deux alinéas et les renvois au I de l'article 1498 et à l'article 1406 du CGI sont conservés. Les changements d'utilisation restent limités aux propriétés bâties visées au I de l'article 1498 ; la condition de survenance après le début des travaux d'évaluation est maintenue.")

add('332', '''
<p>Le redevable qui occupe un immeuble à titre d'habitation principale est exonéré, pour cet immeuble, de taxe foncière sur les propriétés bâties si sa valeur locative n'excède pas 40 % de la valeur locative moyenne des locaux d'habitation de la commune. Le conseil municipal peut relever ce seuil d'exonération à 50 %.</p>
''', "Réécriture à droit constant : la qualité de l'occupant, l'immeuble exonéré et la condition de valeur locative sont explicitement reliés. La faculté de relèvement du seuil par le conseil municipal est conservée ; aucune réforme de fond n'est introduite.", "Les seuils inclusifs de 40 % et, sur décision du conseil municipal, de 50 % sont maintenus. La valeur locative moyenne s'apprécie selon l'article 332 A. La note source relative à l'article 16-I E 4° et VII E de la loi n° 2019-1479 du 28 décembre 2019 est historique et ne fixe aucune entrée en vigueur d'une réforme nouvelle.")

add('332 A', '''
<p>Par dérogation à l'article 310 H, la valeur locative moyenne utilisée, à compter de 1991, pour l'application de l'article 332 est celle retenue pour l'établissement des rôles de 1989. Cette valeur est majorée en 1990, puis chaque année, proportionnellement à la variation des valeurs locatives des logements résultant de l'application des articles 1518 et 1518 bis du code général des impôts.</p>
<p>Pour le Département-Région de Mayotte, la valeur locative moyenne communale utilisée pour l'application de l'article 332 au titre des impositions de 2014 est calculée à partir des valeurs locatives des locaux d'habitation autres qu'exceptionnels présents sur le territoire de la commune au 1er janvier 2014. À compter de 2015, cette moyenne est déterminée conformément à l'article 310 H.</p>
''', "Réécriture à droit constant : la référence aux rôles de 1989 et ses majorations successives sont exposées dans deux phrases ; le régime de Mayotte et son passage à la règle de l'article 310 H restent dans leur alinéa. Aucune réforme de fond n'est introduite.", "Les dates de 1989, 1990, 1991, 2014, du 1er janvier 2014 et de 2015 sont conservées avec leurs fonctions respectives. Le renvoi à l'article 310 H a été vérifié dans le corpus public : il prévoit un calcul annuel à partir des rôles de l'année précédente, hors locaux exceptionnels. Les renvois aux articles 332, 1518 et 1518 bis sont maintenus.")

add('333', '''
<p>Dans les départements de la Guadeloupe, de la Guyane, de la Martinique, de Mayotte et de la Réunion, la valeur locative des propriétés bâties et non bâties est déterminée selon les règles applicables dans les autres départements, sous réserve des adaptations prévues aux articles 333 A à 333 J.</p>
<p>Dans le Département-Région de Mayotte, par dérogation aux articles 333 A à 333 J, la date retenue pour déterminer la valeur locative est le 1er janvier 2012 pour les propriétés non bâties et pour les propriétés bâties autres que celles mentionnées au I de l'article 1498 du code général des impôts.</p>
''', "Réécriture à droit constant : le champ territorial est placé en tête et la date dérogatoire de Mayotte est reliée explicitement aux deux catégories de propriétés concernées. Aucune réforme de fond des évaluations foncières n'est introduite.", "Les cinq départements, les deux alinéas, la date du 1er janvier 2012 et les renvois aux articles 333 A à 333 J et au I de l'article 1498 du CGI sont conservés. La dérogation de Mayotte ne s'étend pas aux propriétés bâties visées par ce I.")

add('333 A', '''
<p>Sous réserve des articles 333 B à 333 H, la date retenue pour déterminer la valeur locative des propriétés bâties autres que celles mentionnées au I de l'article 1498 du code général des impôts est le 1er janvier 1975. Cette valeur est déterminée en application des dispositions suivantes :<br /><br />
1° Les articles 1494 à 1497, 1499 à 1503 et 1505 à 1508 du code général des impôts ;<br /><br />
2° L'article 310 K ;<br /><br />
3° Les articles 324 A à 324 X et 324 AE à 324 AJ de l'annexe III au même code.</p>
''', "Réécriture à droit constant : la date de référence est séparée de l'énumération des dispositions applicables. Les trois subdivisions et l'exclusion des propriétés visées au I de l'article 1498 sont conservées ; aucune réforme de fond n'est introduite.", "La date du 1er janvier 1975 et toutes les bornes des séries d'articles sont maintenues. La dérogation propre à Mayotte figurant à l'article 333 demeure applicable. La note source concernant la loi n° 2020-1721 du 29 décembre 2020, article 29-I-1°, retrace une modification historique et ne constitue pas une date de réforme future.")

add('333 B', '''
<p>Pour l'application du I de l'article 324 T et du II de l'article 324 U de l'annexe III au code général des impôts, les équivalences superficielles comprennent également, pour un climatiseur, 2 mètres carrés par pièce et annexe d'hygiène.</p>
''', "Réécriture à droit constant : le complément au barème est exprimé comme une règle complète d'équivalence superficielle, sans les points de suspension de la source. Aucune réforme de fond de la surface retenue n'est introduite.", "L'équivalence de 2 mètres carrés par pièce et annexe d'hygiène ainsi que les renvois au I de l'article 324 T et au II de l'article 324 U de l'annexe III sont conservés. Ces renvois ont été vérifiés dans le corpus public : ils concernent respectivement les équipements de la partie principale et ceux des dépendances, sous leurs conditions propres, notamment l'état de fonctionnement. Les points de suspension de la source n'ont pas été traités comme une partie de barème à inventer.")

add('333 D', '''
<p>La valeur locative des immobilisations industrielles est déterminée en appliquant les coefficients de révision des bilans fixés à l'article 21 de l'annexe III au code général des impôts.</p>
''', "Réécriture à droit constant : la tournure impersonnelle est remplacée par une règle de calcul directement rattachée aux immobilisations industrielles. Aucune réforme de fond des coefficients n'est introduite.", "Le champ des immobilisations industrielles et le renvoi à l'article 21 de l'annexe III au CGI sont conservés. Aucun coefficient nouveau ni aucune actualisation chiffrée n'est ajouté.")

add('333 E', '''
<p>Le centre national d'études spatiales de Kourou bénéficie de la déduction complémentaire accordée à certains établissements dans les conditions prévues à l'article 310 K.</p>
''', "Réécriture à droit constant : l'établissement bénéficiaire devient le sujet de la règle et le renvoi aux conditions de la déduction est conservé. Aucune réforme de fond du bénéfice de cette déduction n'est introduite.", "Le renvoi à l'article 310 K a été vérifié dans le corpus public : il prévoit la déduction complémentaire au taux de 50 % et renvoie lui-même à l'article 333 E. Le taux demeure porté par l'article 310 K, sans modification ni duplication dans le présent article.")

add('333 F', '''
<p>Pour les immobilisations acquises à la suite d'apports, de scissions ou de fusions de sociétés, l'article 1499 A du code général des impôts s'applique avec les adaptations de dates suivantes : la date de 1976 s'entend de 1979 et celle de 1973 s'entend de 1978.</p>
''', "Réécriture à droit constant : le champ des opérations est placé en tête et chaque date du régime général est directement associée à sa date dérogatoire. Le texte énonce la règle intégrale d'adaptation ; aucune réforme de fond n'est introduite.", "Les correspondances 1976 vers 1979 et 1973 vers 1978 sont conservées dans le même ordre. Le renvoi à l'article 1499 A a été vérifié dans le corpus public : 1976 concerne la limite temporelle des opérations et 1973 l'année de contribution foncière de référence. Ces dates historiques ne sont pas des dates d'entrée en vigueur de la réforme.")

add('333 H', '''
<p>Pour la première révision quinquennale des évaluations foncières des propriétés bâties, les redevables de la contribution foncière des propriétés bâties souscrivent les déclarations prévues à l'article 1502 du code général des impôts dans les départements de la Guadeloupe, de la Martinique et de la Réunion. Dans le département de la Guyane, cette obligation incombe aux redevables de l'impôt locatif. Si la propriété bâtie n'est pas passible de la contribution foncière ou de l'impôt locatif, l'occupant des locaux souscrit la déclaration.</p>
<p>Pour la première évaluation des locaux dans le Département-Région de Mayotte, les redevables de l'impôt foncier sur les terrains ou de la contribution des patentes doivent souscrire les déclarations prévues à l'article 1502 du code général des impôts.</p>
<p>Pour les locaux à usage professionnel ou commercial, les déclarations prévues à l'alinéa précédent sont souscrites par le redevable de la contribution des patentes au 1er janvier 2013, conjointement avec les déclarations prévues au XVII de l'article 34 de la loi n° 2010-1658 du 29 décembre 2010 de finances rectificative pour 2010. Elles sont établies sur un modèle déclaratif unique, adapté par arrêté préfectoral sur proposition du directeur régional des finances publiques. Si la propriété bâtie n'est pas passible de la contribution des patentes, le propriétaire des locaux souscrit la déclaration.</p>
<p>Les déclarants peuvent être aidés, pour rédiger ces déclarations, par des agents désignés par le directeur départemental des finances publiques. Ces agents assurent la collecte des documents.</p>
<p>Le préfet fixe par arrêté les dates limites de souscription des déclarations, sur proposition du directeur départemental des finances publiques.</p>
''', "Réécriture à droit constant : les déclarants sont désignés comme sujets, les régimes territoriaux et les déclarants subsidiaires sont explicités, et le rôle de chaque autorité est formulé directement. Les cinq alinéas sont conservés ; aucune réforme de fond n'est introduite.", "Le renvoi de l'alinéa 3 à l'alinéa précédent reste en place. Sont maintenus la première révision quinquennale, la première évaluation à Mayotte, le 1er janvier 2013, l'article 1502 du CGI et le XVII de l'article 34 de la loi n° 2010-1658 du 29 décembre 2010 de finances rectificative pour 2010. Le directeur régional propose l'adaptation du modèle ; le directeur départemental désigne les agents et propose les échéances. Les rôles distincts de l'occupant et du propriétaire en l'absence d'assujettissement sont préservés.")

add('333 I', '''
<p>Pour les propriétés non bâties, la date de référence de la valeur locative est le 1er janvier 1975. Cette valeur est déterminée selon les articles 1509 à 1511 du code général des impôts.</p>
''', "Réécriture à droit constant : la date de référence et les règles d'évaluation sont présentées dans deux phrases au sein du même alinéa. Aucune réforme de fond n'est introduite.", "La date du 1er janvier 1975 et le renvoi aux articles 1509 à 1511 sont conservés, sous réserve de la dérogation de Mayotte à l'article 333. La note source relative à la loi n° 2020-1525 du 7 décembre 2020, article 9-3°, est historique et ne fixe aucune date de réforme nouvelle.")

add('333 J', '''
<p>Dans le département de la Guyane, les propriétés domaniales qui ne sont ni concédées ni exploitées ne font pas l'objet de travaux d'évaluation.</p>
<p>Cette absence de travaux d'évaluation s'applique aussi aux terrains cédés aux communes en application du 3° de l'article L. 5142-1 du code général de la propriété des personnes publiques, s'ils ne sont ni concédés ni exploités et tant qu'ils sont exonérés en application de l'article 1394 du code général des impôts.</p>
''', "Réécriture à droit constant : les biens exclus des travaux d'évaluation sont placés en sujet et les conditions cumulatives applicables aux terrains communaux sont rendues explicites. Aucune réforme de fond n'est introduite.", "Les deux alinéas, le champ de la Guyane, l'absence à la fois de concession et d'exploitation, et la durée limitée à celle de l'exonération des terrains communaux sont conservés. Les renvois au 3° de l'article L. 5142-1 du CG3P et à l'article 1394 du CGI sont maintenus. La note source sur l'article 108-XIX C-1 de la loi n° 2010-1657 du 29 décembre 2010 ne crée aucune date de réforme future.")

add('334 A', '''
<p>I. - Pour l'application du I de l'article 1518 ter du code général des impôts, la mise à jour annuelle des tarifs s'effectue en appliquant des coefficients d'évolution aux derniers tarifs publiés. Les tarifs ainsi mis à jour servent à établir les impositions de l'année suivante.<br /><br />
Dans chaque secteur d'évaluation et pour chaque catégorie, le coefficient d'évolution est égal à la moyenne des évolutions annuelles des loyers des trois années précédant l'année de la mise à jour.<br /><br />
Pour chaque catégorie du secteur d'évaluation, l'évolution annuelle des loyers est égale au rapport entre la moyenne des loyers de l'année et celle de l'année précédente. Seuls les loyers remplissant les conditions du II sont retenus pour ce calcul.<br /><br />
Si moins de quatre loyers remplissent les conditions du II, l'évolution annuelle des loyers est appréciée selon les modalités du III.<br /><br />
II. - Pour une année et un secteur d'évaluation donnés, sont retenus les loyers des locaux professionnels figurant dans les déclarations prévues à l'article 1498 bis et remplissant les conditions suivantes :<br /><br />
1° Le loyer concerne un local dont la surface et la catégorie n'ont pas changé depuis l'année précédente ;<br /><br />
2° Le montant du loyer n'est ni nul ni significativement éloigné du loyer moyen du secteur d'évaluation ;<br /><br />
3° Le montant du loyer n'a pas varié de plus de 10 % depuis l'année précédente.<br /><br />
Chaque loyer est exprimé en euros par mètre carré : il est égal au rapport entre le loyer annuel déclaré et la surface pondérée du local.<br /><br />
III. - Le coefficient d'évolution départemental mentionné aux deuxième et troisième alinéas du IV de l'article 1518 ter précité est égal à la moyenne des coefficients d'évolution départementaux annuels des trois années précédant l'année de la mise à jour.<br /><br />
Le coefficient d'évolution départemental annuel est égal au rapport entre la moyenne des loyers de l'année et celle de l'année précédente.<br /><br />
Sont retenus les loyers qui remplissent les conditions du II appréciées au niveau du département et qui relèvent des catégories regroupant le plus grand nombre de locaux professionnels et représentant, ensemble, plus de la moitié des locaux du département.<br /><br />
Le coefficient d'évolution départemental s'applique également aux valeurs locatives des propriétés bâties évaluées selon les modalités du III de l'article 1498 du code général des impôts.</p>
''', "Réécriture à droit constant : les opérations de moyenne et de rapport sont distinguées, les conditions de sélection des loyers sont formulées directement et le passage au calcul départemental est explicité. Les I à III et les 1° à 3° sont maintenus ; aucune réforme de fond des paramètres fiscaux n'est introduite.", "Sont conservés les trois années de référence, le basculement sous quatre loyers, le plafond de variation de 10 %, le critère strict de plus de la moitié des locaux et les renvois aux articles 1498, 1498 bis et 1518 ter. Le renvoi aux deuxième et troisième alinéas du IV de l'article 1518 ter a été vérifié dans le corpus : son troisième alinéa porte un coefficient particulier pour la métropole de Lyon, calculé sur le Rhône et la métropole. La source du présent article décrit pourtant un calcul au niveau du seul département ; cette articulation territoriale préexistante appelle une coordination réglementaire expresse, sans extension silencieuse du calcul proposé.")

add('335', '''
<p>I. - L'actualisation des paramètres collectifs d'évaluation des locaux professionnels prévue au 1° du A du III de l'article 1518 ter du code général des impôts utilise les loyers figurant dans les déclarations prévues à l'article 1498 bis du même code. Elle repose sur les données cadastrales et géographiques disponibles correspondant à la situation du local au 1er janvier de l'année précédant celle de l'actualisation.<br /><br />
II. - L'actualisation des paramètres collectifs d'évaluation des locaux professionnels prévue au 2° du A du III de l'article 1518 ter du code général des impôts utilise les données d'une campagne déclarative générale adressée aux propriétaires de l'ensemble des locaux évalués conformément à l'article 1498 du même code. Elle prend en compte, le cas échéant, l'évolution du classement des locaux résultant d'une modification de l'article 310 Q.<br /><br />
III. - Pour les actualisations prévues aux I et II et pour l'application des articles 337 et 338, seules sont retenues les données relatives aux locaux professionnels loués qui remplissent les conditions suivantes :<br /><br />
1° Les caractéristiques des locaux ont été déclarées par les propriétaires ou constatées par l'administration depuis la mise en œuvre, au 1er janvier 2017, de la révision des valeurs locatives des locaux professionnels ;<br /><br />
2° Le montant du loyer annuel n'est ni nul ni égal à 1 euro ;<br /><br />
3° Le montant du loyer est inférieur à 4 000 euros par an et par mètre carré.<br /><br />
Dans chaque catégorie de locaux, les valeurs extrêmes correspondant aux locaux dont le montant du loyer est le plus faible ou le plus élevé sont exclues.<br /><br />
Chaque loyer est exprimé en euros par mètre carré : il est égal au rapport entre le loyer annuel déclaré et la surface pondérée du local définie au C du II de l'article 1498 du code général des impôts.</p>
''', "Réécriture à droit constant : les sources de données des deux actualisations sont présentées séparément et les critères de sélection et d'exclusion sont formulés de manière directe. Les subdivisions et leur ordre sont conservés ; aucune réforme de fond des évaluations n'est introduite.", "Les renvois au 1° et au 2° du A du III de l'article 1518 ter, aux articles 1498 bis, 1498, 310 Q, 337 et 338 sont maintenus. La référence au 1er janvier de l'année précédente et la date du 1er janvier 2017 sont conservées. Les loyers nuls ou égaux à 1 euro sont exclus ; le plafond de 4 000 euros par an et par mètre carré reste strict. L'exclusion des valeurs extrêmes n'est assortie d'aucun nombre de locaux ni traitement des ex aequo nouveau, que la source ne précise pas.")

add('336', '''
<p>I. - Dans chaque département, un avant-projet d'actualisation de la délimitation des secteurs d'évaluation et de détermination des tarifs est élaboré à partir des données retenues en application de l'article 335.<br /><br />
Cet avant-projet comprend :<br /><br />
1° Le découpage du département en secteurs d'évaluation déterminés selon l'article 337, présenté sous la forme d'une liste des communes et sections cadastrales pour chaque secteur ;<br /><br />
2° Une grille tarifaire établie conformément à l'article 338.<br /><br />
L'avant-projet est soumis à la commission départementale des valeurs locatives selon les modalités de l'article 1504 du code général des impôts.<br /><br />
II. - Conformément au c du 1 du I de l'article 1504 du code général des impôts, la commission départementale des valeurs locatives définit les parcelles auxquelles s'applique un coefficient de localisation et détermine ce coefficient.</p>
''', "Réécriture à droit constant : le contenu de l'avant-projet est précisé dans les deux subdivisions existantes et les deux décisions de la commission sur la localisation sont exprimées par des verbes distincts. Aucune réforme de fond de la procédure n'est introduite.", "Les I et II et les 1° et 2° du I sont conservés, ainsi que les renvois aux articles 335, 337, 338 et 1504 du CGI, notamment au c du 1 du I de ce dernier. La présentation par communes et sections cadastrales et la compétence de la commission pour les parcelles et le coefficient restent inchangées.")

add('337', '''
<p>I. - Le département est divisé en secteurs d'évaluation correspondant à des zones géographiques où le marché locatif est homogène.<br /><br />
Le nombre et le périmètre géographique de ces secteurs sont identiques pour toutes les catégories de locaux mentionnées à l'article 310 Q.<br /><br />
II. - Les secteurs d'évaluation sont déterminés selon la méthode suivante :<br /><br />
1° La catégorie de locaux la plus représentée dans le département est celle qui regroupe le plus grand nombre de locaux professionnels parmi les catégories des sous-groupes I, II et IV de l'article 310 Q.<br /><br />
Si plusieurs catégories appartenant à des sous-groupes différents comptent le même nombre maximal de locaux, est retenu le sous-groupe dont le numéro de classement à l'article 310 Q est le plus faible. En cas d'égalité entre plusieurs catégories de ce sous-groupe, est retenue celle dont le numéro de classement à l'article 310 Q est le plus faible ;<br /><br />
2° Le loyer moyen départemental, exprimé en euros par mètre carré, est calculé comme suit :<br /><br />
a) La somme des loyers des locaux de la catégorie la plus représentée dans le département est divisée par le nombre de ces locaux ;<br /><br />
b) Les locaux dont le loyer est inférieur au dixième du rapport calculé au a ou supérieur à dix fois ce rapport sont exclus.<br /><br />
Le loyer moyen départemental est égal à la somme des loyers des locaux retenus après l'exclusion prévue au b, divisée par le nombre de ces locaux ;<br /><br />
3° Les locaux retenus en application du 1° sont répartis en neuf tranches. Chaque tranche correspond à un intervalle délimité par une borne inférieure et une borne supérieure :</p>
<div><p><br />
- le premier intervalle comprend les locaux dont le loyer en euros par mètre carré est compris entre le loyer le plus faible et 30 % du loyer moyen départemental, arrondi à la décimale inférieure ;<br /><br />
- le deuxième intervalle comprend les locaux dont le loyer est compris entre 30 % du loyer moyen départemental, arrondi à la décimale supérieure, et 50 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le troisième intervalle comprend les locaux dont le loyer est compris entre 50 % du loyer moyen départemental, arrondi à la décimale supérieure, et 70 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le quatrième intervalle comprend les locaux dont le loyer est compris entre 70 % du loyer moyen départemental, arrondi à la décimale supérieure, et 90 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le cinquième intervalle comprend les locaux dont le loyer est compris entre 90 % du loyer moyen départemental, arrondi à la décimale supérieure, et 110 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le sixième intervalle comprend les locaux dont le loyer est compris entre 110 % du loyer moyen départemental, arrondi à la décimale supérieure, et 130 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le septième intervalle comprend les locaux dont le loyer est compris entre 130 % du loyer moyen départemental, arrondi à la décimale supérieure, et 150 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le huitième intervalle comprend les locaux dont le loyer est compris entre 150 % du loyer moyen départemental, arrondi à la décimale supérieure, et 170 % de ce loyer moyen, arrondi à la décimale inférieure ;<br /><br />
- le neuvième intervalle comprend les locaux dont le loyer est compris entre 170 % du loyer moyen départemental, arrondi à la décimale supérieure, et le loyer le plus élevé ;</p></div>
<p><br />
4° Le nombre de secteurs d'évaluation est déterminé en regroupant les neuf tranches définies au 3°, afin que chacune comprenne un nombre suffisant de locaux. Ce nombre est suffisant si la tranche comprend à la fois au moins 10 % du nombre total de locaux de la catégorie la plus représentée dans le département et au moins vingt locaux de cette catégorie. Si nécessaire, les intervalles définis au 3° sont regroupés en partant du premier intervalle pour obtenir un nombre suffisant de locaux par secteur d'évaluation.<br /><br />
III. - 1. Chaque commune est rattachée à un secteur d'évaluation en fonction de son loyer moyen communal. Le cas échéant, le rattachement s'effectue à l'échelle de la section cadastrale de commune, en fonction du loyer moyen de cette section. Ce dernier est le loyer moyen communal calculé au niveau de la section cadastrale de commune.<br /><br />
Le loyer moyen communal et, le cas échéant, celui de la section cadastrale sont calculés selon les modalités des 2 et 3 ;<br /><br />
2. Si la commune compte au moins quatre loyers de la catégorie de locaux la plus représentée dans le département, le loyer moyen communal est égal à la somme des loyers des locaux de cette catégorie dans la commune, divisée par le nombre de ces locaux.<br /><br />
Si au moins 75 % de ces locaux ont un loyer par mètre carré compris entre 70 % et 130 % du loyer moyen communal, ou si le nombre de ces locaux est inférieur ou égal à trente-neuf, la commune entière est rattachée à l'un des secteurs d'évaluation définis au II, en fonction de son loyer moyen communal.<br /><br />
Si moins de 75 % de ces locaux ont un loyer par mètre carré compris entre 70 % et 130 % du loyer moyen communal et si ces locaux sont au moins quarante, un loyer moyen est calculé pour chaque section cadastrale. Il est égal à la somme des loyers des locaux de cette catégorie dans la section cadastrale, divisée par leur nombre. Chaque section est rattachée à l'un des secteurs d'évaluation définis au II en fonction de son loyer moyen ;<br /><br />
3. Si la commune ou la section cadastrale de commune compte moins de quatre loyers de la catégorie la plus représentée dans le département, le rattachement à un secteur d'évaluation s'effectue comme suit :<br /><br />
1° Pour la commune, le loyer moyen communal est égal à la moyenne des loyers moyens communaux des communes limitrophes du même département. Ces loyers moyens sont pondérés par les longueurs des limites territoriales de ces communes ;<br /><br />
2° Pour la section cadastrale de commune, le loyer moyen de la section cadastrale est égal à la moyenne des loyers moyens communaux calculés au niveau des sections cadastrales de commune limitrophes de la commune. Ces loyers moyens sont pondérés par les longueurs des limites territoriales de ces sections cadastrales de commune.</p>
''', "Réécriture à droit constant : les calculs sont explicités comme des divisions, les départages en cas d'égalité et les conditions alternatives ou cumulatives de rattachement sont distingués. Les neuf intervalles, leurs arrondis et toutes les subdivisions sont intégralement maintenus, sans résumé. Aucune réforme de fond de la sectorisation n'est introduite.", "Contrôle des neuf tranches : bornes 30 %, 50 %, 70 %, 90 %, 110 %, 130 %, 150 % et 170 %, avec arrondi inférieur aux bornes hautes et supérieur aux bornes basses intermédiaires. Sont maintenus le dixième et le décuple, le cumul d'au moins 10 % et vingt locaux, le seuil de quatre loyers, les 75 %, l'intervalle 70 %-130 %, les seuils trente-neuf/quarante et les renvois à l'article 310 Q. Deux imprécisions préexistantes sont conservées et signalées : le II, 3° vise les locaux retenus au 1° sans dire expressément qu'il s'agit des locaux filtrés au 2° ; le III, 3°, 2° vise les sections limitrophes de la commune et les longueurs de leurs limites territoriales, sans préciser les seuls segments communs ni le traitement de l'absence de données voisines. Les pondérations ne sont donc pas redéfinies silencieusement. Les blocs et renvois internes restent dans l'ordre de la source.")

add('338', '''
<p>I. - Dans chaque département, une grille tarifaire présente, pour chaque secteur d'évaluation, les tarifs de toutes les catégories de locaux, à l'exception de la catégorie relevant du sous-groupe des établissements présentant des caractéristiques exceptionnelles.<br /><br />
II. - La grille tarifaire comprend quatre parties :<br /><br />
1° La première présente, par secteur d'évaluation, les tarifs des catégories de locaux pour lesquelles au moins quatre loyers sont retenus dans le secteur ;<br /><br />
2° La deuxième présente, par secteur d'évaluation, les tarifs des catégories de locaux pour lesquelles un à trois loyers sont retenus dans le secteur ;<br /><br />
3° La troisième présente, par secteur d'évaluation, les tarifs des catégories auxquelles appartiennent des locaux dans le secteur, mais pour lesquelles aucun loyer n'est retenu ;<br /><br />
4° La quatrième présente, par secteur d'évaluation, les tarifs des catégories auxquelles aucun local du secteur n'appartient.<br /><br />
III. - Pour les première et deuxième parties de la grille, le tarif de chaque catégorie dans chaque secteur d'évaluation est calculé après exclusion des locaux dont les loyers sont inférieurs au dixième ou supérieurs à dix fois le loyer moyen de la catégorie dans ce secteur. Il est égal à la somme des loyers retenus, divisée par le nombre de locaux de la catégorie retenus après cette exclusion.<br /><br />
Pour les troisième et quatrième parties, l'administration propose des tarifs selon les modalités du 2 du B du II de l'article 1498 du code général des impôts, afin de permettre l'évaluation des locaux.</p>
''', "Réécriture à droit constant : les quatre parties de la grille sont décrites selon le nombre de loyers ou de locaux, puis le calcul des tarifs est décomposé entre exclusion des valeurs et moyenne. Les subdivisions sont conservées ; aucune réforme de fond tarifaire n'est introduite.", "Les seuils d'au moins quatre loyers, d'un à trois loyers et d'absence de loyer ou de local sont maintenus. L'exclusion reste strictement sous le dixième ou au-dessus du décuple du loyer moyen. Le dénominateur demeure celui des locaux après exclusion. La catégorie des établissements exceptionnels reste hors grille ; le renvoi au 2 du B du II de l'article 1498 du CGI est conservé.")

add('339', '''
<p>Les projets établis par les commissions départementales des valeurs locatives en application des a et b du 1 du I de l'article 1504 du code général des impôts et les avis émis par les commissions communales ou intercommunales des impôts directs dans les conditions du 3 du I du même article doivent être motivés lorsqu'ils s'écartent de l'avant-projet élaboré par l'administration. Ils doivent alors tenir compte de la situation particulière du marché locatif local.</p>
''', "Réécriture à droit constant : l'obligation de motivation est formulée directement et la prise en compte du marché locatif local figure dans une seconde phrase, sous la même condition de divergence avec l'avant-projet. Aucune réforme de fond des pouvoirs des commissions n'est introduite.", "Le même alinéa conserve les deux catégories de documents, les commissions compétentes et les renvois aux a et b du 1 du I et au 3 du I de l'article 1504 du CGI. La prise en compte du marché local et la motivation sont toutes deux exigées en cas d'écart avec l'avant-projet.")

add('340', '''
<p>L'année de l'actualisation prévue au III de l'article 1518 ter du code général des impôts, les dispositions du I de ce même article ne s'appliquent pas pour établir les impositions de l'année suivante.</p>
''', "Réécriture à droit constant : l'année de suspension est placée en tête et distinguée de l'année des impositions concernées. Aucune réforme de fond du calendrier n'est introduite.", "Les renvois aux I et III de l'article 1518 ter du CGI sont conservés. La suspension vaut l'année de l'actualisation pour les impositions de l'année suivante, sans prolongation ni nouvelle date calendaire. La règle reste articulée à la mise à jour annuelle prévue à l'article 334 A.")

add('368', '''
<p>I. - La direction générale des finances publiques met en œuvre un traitement automatisé de données à caractère personnel dénommé « Registre des trusts ».<br /><br />
II. - Les informations traitées proviennent du traitement dénommé « Base nationale des données patrimoniales ». Elles sont les suivantes :<br /><br />
1° La dénomination et l'adresse du trust ;<br /><br />
2° Les dates de constitution et d'extinction du trust ;<br /><br />
3° La date et la nature de la déclaration de trust mentionnée à l'article 1649 AB du code général des impôts ;<br /><br />
4° Les éléments d'identification du constituant, du bénéficiaire, de l'administrateur du trust et du bénéficiaire effectif si celui-ci diffère de ces personnes.<br /><br />
Pour le constituant, le bénéficiaire et le bénéficiaire effectif, les éléments d'identification sont les nom, prénoms, adresse, date et lieu de naissance, nationalité et, le cas échéant, date de décès.<br /><br />
Pour l'administrateur, les éléments d'identification sont les nom, prénoms, adresse, date et lieu de naissance.<br /><br />
Pour une personne morale, les éléments d'identification sont la dénomination sociale, l'adresse du siège social ou de l'établissement et le numéro SIREN.<br /><br />
III. - Les informations mentionnées au II sont conservées pendant dix ans après la date d'extinction du trust.<br /><br />
IV. - Chaque consultation du traitement automatisé effectuée pour accéder aux données traitées est enregistrée. L'enregistrement comprend l'identification du consultant, la date, l'heure et l'objet de la consultation. Ces informations sont conservées pendant trois ans.</p>
''', "Réécriture à droit constant : l'autorité responsable est placée en sujet, les données d'identification sont distinguées par personne concernée et la traçabilité des consultations est décrite directement. Les I à IV et les 1° à 4° sont conservés ; aucune réforme de fond de la collecte ou de l'accès n'est introduite.", "Les deux dénominations de traitements, le renvoi à l'article 1649 AB et la condition d'identification du bénéficiaire effectif distinct sont conservés. Le registre ne reçoit aucune donnée supplémentaire ; la date de décès n'est pas ajoutée aux données propres à l'administrateur. Les dix ans courent après l'extinction du trust ; les informations de consultation demeurent conservées trois ans. Aucun accès public ou nouveau destinataire n'est créé.")

add('369', '''
<p>L'administrateur dépose à la recette des non-résidents la déclaration mentionnée au I de l'article 1649 AB du code général des impôts dans le mois qui suit la constitution, la modification ou l'extinction d'un trust défini à l'article 792-0 bis du même code.</p>
<p>La déclaration est rédigée en français sur un imprimé conforme au modèle établi par l'administration. Elle comporte les indications suivantes :</p>
<p>1° Pour identifier le ou les constituants ou bénéficiaires réputés constituants : nom et prénom ou raison sociale, numéro SIREN, adresse, date et lieu de naissance, nationalité et, s'il y a lieu, date et lieu de décès ;</p>
<p>2° Pour identifier le ou les bénéficiaires effectifs : nom et prénom ou raison sociale, numéro SIREN, adresse, date et lieu de naissance, nationalité et, s'il y a lieu, date et lieu de décès ;</p>
<p>3° Pour identifier l'administrateur du trust : nom et prénom ou dénomination sociale, numéro SIREN, adresse, date et lieu de naissance ;</p>
<p>4° Pour identifier le trust : dénomination et adresse ;</p>
<p>5° Pour préciser les termes du trust : contenu de l'acte de trust et des éventuelles stipulations complémentaires qui régissent son fonctionnement, notamment son caractère révocable ou irrévocable, discrétionnaire ou non, ainsi que les règles d'attribution des biens ou droits placés dans le trust et de leurs produits ;</p>
<p>6° La nature et la date de l'événement à l'origine de l'obligation déclarative ;</p>
<p>7° Le cas échéant, la consistance, au jour de l'événement mentionné au 6°, des biens ou droits placés dans le trust, ainsi que celle des biens, droits ou produits transmis, attribués ou sortis du trust du fait de cet événement ;</p>
<p>8° Pour chaque bien ou droit placé dans le trust et mentionné dans la déclaration au titre du 7°, les renseignements suivants sur les personnes qui le placent dans le trust : nom et prénom ou raison sociale, adresse, date et lieu de naissance et, s'il y a lieu, de décès, ainsi que nationalité ;</p>
<p>9° Pour chaque bien, droit ou produit transmis, attribué ou sorti du trust et mentionné dans la déclaration au titre du 7°, les renseignements suivants sur les personnes auxquelles ce bien, droit ou produit est transmis, attribué ou sorti du trust concerné : nom et prénom ou raison sociale, adresse, date et lieu de naissance, nationalité et, s'il y a lieu, date et lieu de décès.</p>
<p>Pour l'application du présent article, constitue une modification du trust tout changement de ses termes, de son mode de fonctionnement, de son constituant, de son bénéficiaire réputé constituant, de son bénéficiaire effectif ou de son administrateur, ainsi que tout décès de l'un d'entre eux. Constituent également une modification toute nouvelle entrée ou toute sortie de biens ou droits du trust, toute transmission ou attribution de biens, droits ou produits du trust et, plus généralement, toute modification de droit ou de fait susceptible d'affecter l'économie ou le fonctionnement du trust concerné.</p>
''', "Réécriture à droit constant : le débiteur de l'obligation déclarative est explicité, les rubriques indiquent directement leur objet et la définition des modifications est divisée en deux phrases sans réduction de son champ. Les neuf rubriques et leur ordre sont conservés ; aucune réforme de fond de la déclaration n'est introduite.", "Le délai d'un mois, le dépôt à la recette des non-résidents et les renvois au I de l'article 1649 AB et à l'article 792-0 bis du CGI sont conservés. La qualité de déclarant de l'administrateur a été vérifiée dans l'article 1649 AB du corpus public. Tous les champs d'identification, les indications facultatives de décès, les termes complémentaires et les flux du 7° au 9° sont maintenus, ainsi que la date d'appréciation au jour de l'événement. L'expression préexistante du 9° « personnes auxquelles [...] est [...] sorti du trust » demeure juridiquement peu précise ; elle n'est pas remplacée par une catégorie nouvelle de destinataires.")

add('369 A', '''
<p>L'administrateur d'un trust défini à l'article 792-0 bis du code général des impôts doit déposer à la recette des non-résidents, au plus tard le 15 juin de chaque année, la déclaration mentionnée au premier alinéa de l'article 1649 AB.</p>
<p>La déclaration est rédigée en français sur un imprimé conforme au modèle établi par l'administration. Elle comporte les indications suivantes :</p>
<p>1° Pour identifier le ou les constituants ou bénéficiaires réputés constituants : nom et prénom ou raison sociale, numéro SIREN, adresse, date et lieu de naissance, nationalité et, s'il y a lieu, date et lieu de décès ;</p>
<p>2° Pour identifier le ou les bénéficiaires effectifs : nom et prénom ou raison sociale, numéro SIREN, adresse, date et lieu de naissance, nationalité et, s'il y a lieu, date et lieu de décès ;</p>
<p>3° Pour identifier l'administrateur du trust : nom et prénom ou dénomination sociale, numéro SIREN, adresse, date et lieu de naissance ;</p>
<p>4° Pour identifier le trust : dénomination et adresse ;</p>
<p>5° Pour préciser les termes du trust : contenu de l'acte de trust et des éventuelles stipulations complémentaires qui régissent son fonctionnement, notamment son caractère révocable ou irrévocable, discrétionnaire ou non, ainsi que les règles d'attribution des biens ou droits placés dans le trust et de leurs produits ;</p>
<p>6° Si au moins l'un des constituants, bénéficiaires réputés constituants ou bénéficiaires effectifs a son domicile fiscal en France, l'inventaire détaillé des biens, droits et produits capitalisés placés dans le trust, qu'ils soient situés en France ou hors de France, et leur valeur vénale au 1er janvier de l'année ;</p>
<p>7° Si aucun des constituants, bénéficiaires réputés constituants ou bénéficiaires effectifs n'a son domicile fiscal en France, l'inventaire détaillé des biens, droits et produits capitalisés situés en France et placés dans le trust, et leur valeur vénale au 1er janvier de l'année.</p>
<p>L'administrateur est dispensé de fournir les informations prévues au 5° si la déclaration prévue au premier alinéa de l'article 1649 AB du code général des impôts a déjà été déposée.</p>
<p>La déclaration mentionnée au premier alinéa est accompagnée, le cas échéant, du paiement du montant correspondant au prélèvement prévu à l'article 990 J du code général des impôts.</p>
''', "Réécriture à droit constant : les rubriques déclaratives sont formulées selon leur objet, le champ de l'inventaire est distingué selon la domiciliation fiscale et la dispense est exprimée directement. Les sept rubriques et les deux derniers alinéas sont maintenus ; aucune réforme de fond des obligations ni du prélèvement n'est introduite.", "L'échéance annuelle du 15 juin, les évaluations au 1er janvier, la recette des non-résidents et les renvois aux articles 792-0 bis, 1649 AB et 990 J du CGI sont conservés. Tous les champs d'identification sont maintenus ; la dispense reste limitée au 5°. Le renvoi préexistant au « premier alinéa » de l'article 1649 AB est conservé : dans la version du corpus, ce premier alinéa introduit l'ensemble des obligations du I, et la valeur vénale figure précisément au 3° du I. Cette désignation ancienne, également utilisée pour la dispense, mérite une coordination expresse plutôt qu'une substitution silencieuse. Le présent article n'est pas étendu à des comptes de retraite ou à d'autres structures d'épargne.")

add('369 B', '''
<p>Pour l'application de l'article 1649 AB, la date retenue pour apprécier le domicile fiscal est le 1er janvier de chaque année.</p>
''', "Réécriture à droit constant : la règle est formulée en désignant expressément la date d'appréciation. Aucune réforme de fond de la domiciliation fiscale n'est introduite.", "Le renvoi à l'article 1649 AB et la date du 1er janvier de chaque année sont conservés. Cette date n'est pas remplacée par celle du dépôt ou de l'événement déclaré.")


assert len(sources) == len(drafts) == 24
assert {s['number'] for s in sources} == set(drafts)
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles, {sum(len(a["proposed_xml"]) for a in answer)} caractères proposés')
