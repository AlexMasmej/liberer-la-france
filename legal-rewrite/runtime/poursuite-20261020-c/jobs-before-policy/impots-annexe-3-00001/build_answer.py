import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}
reasons = {}
notes = {}


def draft(number, paragraphs, reason, review):
    drafts[number] = paragraphs
    reasons[number] = reason
    notes[number] = review


draft('2 sexies', [
    "Lorsque le bail à construction dure entre dix-huit et trente ans, le revenu brut foncier correspondant à la valeur des constructions remises au bailleur sans indemnité à la fin du bail est calculé à partir de leur prix de revient. Ce prix est diminué d'une décote de 8 % pour chaque année de bail au-delà de la dix-huitième.",
],
    "Réécriture à droit constant : la condition de durée du bail, l'assiette du revenu brut foncier et le calcul de la décote sont exposés en deux phrases. Aucune réforme de fond n'est appliquée à ce régime.",
    "Durée de dix-huit à trente ans et décote de 8 % par année au-delà de la dix-huitième conservées. La remise sans indemnité en fin de bail reste la condition du calcul ; aucun plafonnement ou régime locatif nouveau n'est ajouté.")

draft('2 undecies', [
    "Les dépenses mentionnées au c bis du 2° du I de l'article 31 du code général des impôts sont les dépenses d'amélioration et de construction rendues obligatoires qui s'incorporent aux bâtiments d'exploitation rurale. Ces bâtiments doivent être affectés aux activités définies dans la nomenclature des installations classées pour la protection de l'environnement prévue à l'article L. 511-2 du code de l'environnement.",
    "Le bailleur joint les pièces suivantes à sa déclaration de revenus établie au titre de l'année du paiement de la dépense :",
    "1° Selon le cas, une copie de l'autorisation préfectorale prévue à l'article L. 512-1 du code de l'environnement ou une copie de la déclaration prévue à l'article L. 512-8 du même code, accompagnée du récépissé délivré par le préfet ;",
    "2° Les factures des dépenses effectuées. Elles doivent indiquer distinctement les travaux obligatoires, leur description précise et leur montant, ainsi que les immeubles sur lesquels ils sont réalisés.",
],
    "Réécriture à droit constant : les conditions tenant aux dépenses et à l'affectation des bâtiments sont distinguées ; l'obligation déclarative du bailleur et le contenu des deux catégories de justificatifs sont rendus explicites. Aucune réforme de fond.",
    "Conservation du c bis du 2° du I de l'article 31 du CGI et des articles L. 511-2, L. 512-1 et L. 512-8 du code de l'environnement. Le récépissé accompagne la déclaration, et les pièces se rattachent à l'année du paiement, non à celle de réalisation des travaux. Le régime des bâtiments agricoles n'est pas étendu aux logements.")

draft('2 duodecies', [
    "Les plafonds de loyer et de ressources du locataire applicables au premier alinéa du j du 1° du I de l'article 31 du code général des impôts sont fixés ci-après :",
    "a) Pour les baux conclus en 2022, le plafond de loyer mensuel hors charges est de 19,36 € par mètre carré en zone A, de 12,65 € en zone B et de 9,18 € en zone C. Ces plafonds sont révisés chaque année au 1er janvier selon les modalités prévues au premier alinéa de l'article L. 353-9-2 du code de la construction et de l'habitation et sont arrondis au centime d'euro le plus proche. Toutefois, pour les conventions conclues à compter du 1er janvier 2015 en application du premier alinéa du m du 1° du I de l'article 31 du code général des impôts, les plafonds de loyer sont ceux du 1 du I de l'article 2 terdecies D ou, le cas échéant, ceux fixés en application de son III, et, pour les logements situés en outre-mer, ceux du 1 du I de l'article 2 terdecies F ou, le cas échéant, ceux fixés en application de son III. Pour ces mêmes conventions, les logements situés en zone C sont soumis aux plafonds prévus au présent alinéa pour les logements situés en zone B2 du 1 du I de l'article 2 terdecies D. Les plafonds fixés par arrêté du représentant de l'État dans la région en application des III des articles 2 terdecies D et 2 terdecies F s'appliquent uniquement aux conventions conclues à compter de l'entrée en vigueur de l'arrêté.",
    "Les zones A, B et C utilisées pour l'application du présent article sont définies par arrêté des ministres chargés du budget et du logement.",
    "Pour apprécier le plafond de loyer, la surface retenue est la surface habitable au sens de l'article R. 156-1 du code de la construction et de l'habitation, augmentée de la moitié de la surface des annexes mentionnées aux articles D. 353-16 et D. 331-10 du même code. Cette augmentation est limitée à 8 mètres carrés par logement ;",
    "b) Les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'imposition établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location.",
    "Les plafonds annuels de ressources applicables aux baux conclus en 2022 figurent dans le tableau suivant :",
    "Ces plafonds sont révisés chaque année au 1er janvier selon l'évolution annuelle de l'indice des prix à la consommation hors tabac et sont arrondis à l'euro le plus proche. La variation retenue est celle constatée entre le 1er octobre de l'avant-dernière année et le 1er octobre de l'année précédente.",
    "Toutefois, pour les conventions conclues à compter du 1er janvier 2015 en application du premier alinéa du m du 1° du I de l'article 31 du code général des impôts, les plafonds annuels de ressources sont ceux du 2 du I de l'article 2 terdecies D et, pour les logements situés en outre-mer, ceux du 2 du I de l'article 2 terdecies F. Pour ces mêmes conventions, les logements situés en zone C sont soumis aux plafonds prévus au présent alinéa pour les logements situés en zone B2 du tableau annexé au a du 2 du I de l'article 2 terdecies D.",
    "Pour l'application du présent article, les personnes à charge sont celles mentionnées aux articles 196 à 196 B du code général des impôts.",
],
    "Réécriture à droit constant : les règles générales sont distinguées des règles propres aux conventions conclues depuis le 1er janvier 2015 ; la surface retenue, l'année des ressources et les indexations sont explicités. Le tableau est intégralement conservé. Aucune réforme de fond des avantages locatifs ou des plafonds.",
    "Les neuf alinéas et la deuxième phrase du premier alinéa du a sont maintenus à leur emplacement : les articles 2 terdecies B à H renvoient à ces unités. Montants de 2022, tableau complet, majorations, limite de 8 m² et dates d'indexation conservés sans actualisation discrétionnaire. La note source de 2010 et 2014 reste historique. Vérification locale : D. 331-10 du CCH renvoie encore à R. 111-2, tandis que le présent article et D. 353-16 visent R. 156-1 ; cette discordance préexistante appelle un contrôle du renvoi dans D. 331-10, sans modification silencieuse ici.")

draft('2 terdecies', [
    "Les plafonds de loyer et de ressources du locataire applicables au troisième alinéa du g du 1° du I de l'article 31 du code général des impôts sont fixés ci-après :",
    "a) Pour les baux conclus entre le 1er janvier et le 31 décembre 2026, le plafond de loyer mensuel hors charges est de 19,40 € par mètre carré en zone I bis, de 17,18 € en zone I, de 13,27 € en zone II et de 12,53 € en zone III. Ces plafonds sont relevés chaque année au 1er janvier selon les modalités applicables aux plafonds de loyer de l'article 2 duodecies.",
    "Les zones I bis à III utilisées pour l'application du présent article sont définies par arrêté des ministres chargés du budget et du logement. Pour apprécier le plafond de loyer, la surface retenue est celle prévue pour l'application de l'article 2 duodecies ;",
    "b) Les ressources du locataire sont appréciées selon les modalités prévues pour l'application de l'article 2 duodecies.",
],
    "Réécriture à droit constant : les montants sont présentés avec une unité et une période communes, puis les règles de zonage, de surface et de ressources sont formulées directement. Aucune réforme de fond.",
    "Quatre alinéas et subdivisions a et b conservés. Les quatre plafonds de 2026 et le renvoi à 2 duodecies sont maintenus ; le zonage I bis à III reste distinct du zonage A à C. La note relative au décret du 29 mars 1999 ne constitue pas une entrée en vigueur de la réforme.")

draft('2 terdecies A', [
    "Pour appliquer le troisième alinéa du h du 1° du I de l'article 31 du code général des impôts, dans sa rédaction en vigueur avant la publication de la loi n° 2006-872 du 13 juillet 2006 portant engagement national pour le logement, le plafond de loyer mensuel hors charges des baux conclus en 2026 est de 27,09 € par mètre carré en zone A, de 18,83 € en zone B et de 13,57 € en zone C. Ces plafonds sont relevés chaque année au 1er janvier selon les modalités applicables aux plafonds de loyer de l'article 2 duodecies.",
    "Les zones A, B et C utilisées pour l'application du présent article sont définies par arrêté des ministres chargés du budget et du logement. Pour apprécier le plafond de loyer, la surface retenue est celle prévue pour l'application de l'article 2 duodecies.",
],
    "Réécriture à droit constant : la phrase de fixation des plafonds et les renvois de calcul sont rendus plus directs, sans supprimer la référence à la rédaction historique du CGI. Aucune réforme de fond.",
    "Conserver le champ antérieur à la publication de la loi n° 2006-872 du 13 juillet 2006, les trois montants de 2026 et l'indexation annuelle. Le régime historique n'est pas assimilé à celui de l'article 2 terdecies B. La note de 2003 est une note de coordination historique.")

draft('2 terdecies B', [
    "Les plafonds de loyer mensuel par mètre carré, hors charges, applicables au troisième alinéa du h du 1° du I de l'article 31 du code général des impôts sont fixés comme suit :",
    "a. Pour les logements autres que ceux mentionnés au b, les plafonds applicables aux baux conclus en 2026 sont de 27,09 € en zone A, de 18,83 € en zone B 1, de 15,41 € en zone B 2 et de 11,28 € en zone C ;",
    "b. Pour les logements acquis ou construits à compter du 1er janvier 2011, ainsi que pour ceux acquis par des sociétés civiles de placement immobilier, en tout ou partie au moyen de souscriptions réalisées à compter de cette date, les plafonds applicables aux baux conclus en 2026 sont de 26,93 € en zone A bis, de 19,97 € dans le reste de la zone A, de 16,10 € en zone B 1, de 13,15 € en zone B 2 et de 9,14 € en zone C.",
    "Les plafonds des a et b sont révisés chaque année au 1er janvier selon les modalités du premier alinéa du a de l'article 2 duodecies.",
    "Pour les baux conclus en 2026 portant sur des logements situés outre-mer qui ouvrent droit à la réduction d'impôt de l'article 199 septvicies du code général des impôts, les plafonds de loyer mensuel hors charges sont calculés à partir des montants du cinquième alinéa de l'article 2 terdecies C, majorés :",
    "– d'un quart dans les départements d'outre-mer, à Saint-Barthélemy et à Saint-Martin ;",
    "– d'un cinquième en Polynésie française, en Nouvelle-Calédonie, à Saint-Pierre-et-Miquelon et dans les îles Wallis et Futuna.",
    "Les montants obtenus après ces majorations sont arrondis au centime d'euro le plus proche.",
    "Pour l'application des deuxième et troisième alinéas, les zones A, A bis, B 1, B 2 et C sont définies par arrêté des ministres chargés du budget et du logement. La surface habitable retenue pour apprécier les plafonds de loyer de ces alinéas est celle prévue au troisième alinéa du a de l'article 2 duodecies. Pour les plafonds de loyer du cinquième alinéa, la surface habitable retenue est celle définie au III de l'article 46 AG terdecies.",
],
    "Réécriture à droit constant : les catégories de logements et la date des souscriptions sont précisées dans une syntaxe plus lisible ; le calcul des plafonds ultramarins et les deux règles de surface sont distingués. Aucune réforme de fond.",
    "Les neuf alinéas restent dans le même ordre, notamment le cinquième et les renvois aux deuxième et troisième. Maintien de tous les plafonds de 2026, de la date du 1er janvier 2011, des majorations d'un quart et d'un cinquième et de l'arrondi au centime. Le cinquième alinéa de 2 terdecies C conserve bien les montants ultramarins visés ; la surface du III de 46 AG terdecies demeure distincte de celle de 2 duodecies. Notes de 2006 et 2010 historiques.")

draft('2 terdecies C', [
    "Les plafonds de loyer et de ressources du locataire applicables au l du 1° du I de l'article 31 du code général des impôts sont fixés ci-après :",
    "a. Les plafonds de loyer mensuel hors charges sont calculés en retenant les quatre cinquièmes des plafonds mentionnés ci-après, puis en arrondissant le résultat au centime d'euro le plus proche :",
    "- au a de l'article 2 terdecies B, pour les baux conclus en 2026 portant sur des logements autres que ceux mentionnés au b de cet article ;",
    "- au b de l'article 2 terdecies B, pour les baux conclus en 2026 portant sur les logements mentionnés à ce b.",
    "Pour les baux conclus en 2026 portant sur des logements situés outre-mer qui ouvrent droit à la réduction d'impôt de l'article 199 septvicies du code général des impôts, le plafond de loyer mensuel hors charges, par mètre carré de surface habitable, est de 12,71 € dans les départements d'outre-mer, à Saint-Barthélemy et à Saint-Martin, et de 15,99 € en Polynésie française, en Nouvelle-Calédonie, à Saint-Pierre-et-Miquelon et dans les îles Wallis et Futuna. Ces plafonds sont relevés chaque année au 1er janvier selon les modalités du 1 de l'article 46 AG duodecies.",
    "b. Les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'impôt sur le revenu établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location.",
    "Les plafonds annuels de ressources applicables aux baux conclus en 2026 figurent dans le tableau suivant :",
    "Ces plafonds sont révisés chaque année au 1er janvier selon les modalités applicables aux plafonds de ressources de l'article 2 duodecies.",
    "Pour les baux conclus en 2026 portant sur des logements situés outre-mer qui ouvrent droit à la réduction d'impôt de l'article 199 septvicies du code général des impôts, les plafonds de ressources des locataires figurent dans le tableau suivant :",
    "Ces plafonds sont relevés chaque année au 1er janvier selon les modalités du 1 de l'article 46 AG duodecies.",
    "Pour l'application du présent article, les personnes à charge sont celles mentionnées aux articles 196 à 196 B du code général des impôts.",
    "Les zones A, A bis, B 1, B 2 et C utilisées pour l'application du présent article sont définies par arrêté des ministres chargés du budget et du logement. Pour apprécier les plafonds de loyer du premier alinéa du a, la surface habitable retenue est celle prévue au troisième alinéa du a de l'article 2 duodecies. Pour apprécier ceux du quatrième alinéa du a, la surface habitable retenue est celle définie au III de l'article 46 AG terdecies.",
],
    "Réécriture à droit constant : le calcul aux quatre cinquièmes, les règles ultramarines et la définition des ressources sont exposés plus directement. Les deux tableaux sont reproduits en totalité et les douze alinéas restent en place. Aucune réforme de fond.",
    "Contrôle des plafonds de 2026, des deux tableaux et de leurs majorations, des quatre cinquièmes et des arrondis. Le cinquième alinéa, visé par 2 terdecies B, demeure celui des loyers ultramarins ; le quatrième alinéa du a et les renvois de surface ne sont pas déplacés. Les montants ultramarins de ressources, notamment 28 625 € pour une personne seule et 52 935 € pour un couple dans la seconde colonne territoriale, sont ceux de la source et sont conservés sans lissage. La note de 2006 reste historique.")

draft('2 terdecies D', [
    "I. – Les règles suivantes s'appliquent pour la mise en œuvre du premier alinéa du III de l'article 199 novovicies du code général des impôts :",
    "1. Pour les baux conclus en 2026, le plafond de loyer mensuel par mètre carré, hors charges, est de 19,71 € en zone A bis, de 14,64 € dans le reste de la zone A, de 11,80 € en zone B 1 et de 10,26 € en zone B 2 et en zone C. Ces plafonds sont révisés chaque année au 1er janvier selon les modalités du premier alinéa du a de l'article 2 duodecies.",
    "Les plafonds de loyer de l'alinéa précédent sont multipliés par un coefficient calculé selon la formule suivante :",
    "0,7 + 19/ S,",
    "où S désigne la surface du logement. Le coefficient obtenu est arrondi à la deuxième décimale la plus proche, sans pouvoir dépasser 1,2.",
    "Pour l'application du présent 1, la surface retenue est celle prévue au dernier alinéa du a de l'article 2 duodecies ;",
    "2. Les règles relatives aux plafonds de ressources sont fixées ci-après :",
    "a) Les plafonds annuels de ressources des locataires applicables aux baux conclus en 2026 figurent dans le tableau suivant :",
    "Ces plafonds sont révisés chaque année au 1er janvier selon les modalités du troisième alinéa du b de l'article 2 duodecies ;",
    "b) Les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'impôt sur le revenu établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location. Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du même code.",
    "II. – Pour l'application du I, les zones A, A bis, B 1, B 2 et C sont définies à l'article D. 304-1 du code de la construction et de l'habitation.",
    "III. – Pour la mise en œuvre du second alinéa du III de l'article 199 novovicies du code général des impôts, les plafonds de loyer du premier alinéa du 1 du I peuvent être réduits lorsqu'ils ne sont pas sensiblement inférieurs aux loyers pratiqués dans le parc privé. Cette réduction est soumise aux conditions et modalités suivantes :",
    "1. Pour chaque commune ou ensemble de communes appartenant à une même zone, les plafonds de loyer réduits doivent être compris entre le niveau des loyers pratiqués dans le parc locatif privé et les plafonds applicables aux logements financés dans les conditions des articles D. 331-17 à D. 331-21 du code de la construction et de l'habitation. Le niveau des loyers du parc locatif privé est apprécié par tous moyens, notamment à partir des informations des observatoires et bases de données disponibles ou de celles figurant dans les programmes locaux de l'habitat prévus aux articles L. 302-1 et L. 302-4-1 du même code.",
    "2. Le représentant de l'État dans la région soumet son projet d'arrêté à l'avis des organismes, collectivités et établissements suivants :",
    "1° Le comité régional de l'habitat et de l'hébergement mentionné à l'article L. 364-1 du code de la construction et de l'habitation ;",
    "2° Les communes et les établissements publics de coopération intercommunale disposant d'un programme local de l'habitat exécutoire, ainsi que les départements ayant conclu avec l'État la convention prévue à l'article L. 301-5-2 du code de la construction et de l'habitation, sur le territoire desquels la réduction est envisagée. Ces collectivités et établissements disposent de deux mois pour émettre leur avis. À l'expiration de ce délai, ils sont réputés s'être prononcés.",
    "3. Les plafonds de loyer réduits sont multipliés par le coefficient défini au 1 du I.",
    "4. Les plafonds de loyer réduits sont révisés chaque année au 1er janvier selon les conditions du premier alinéa du 1 du I.",
    "5. L'arrêté fixant des plafonds de loyer réduits s'applique aux logements dont l'acte authentique d'acquisition est signé après son entrée en vigueur. Pour les logements que le contribuable fait construire, il s'applique lorsque la demande de permis de construire est déposée après son entrée en vigueur.",
],
    "Réécriture à droit constant : les calculs, les ressources et les conditions de réduction locale des loyers sont formulés avec des sujets explicites. Les deux critères temporels d'application de l'arrêté sont distingués dans le même alinéa. Le tableau complet et les dix-neuf alinéas sont maintenus. Aucune réforme de fond.",
    "Maintien des montants de 2026, du tableau, de la formule 0,7 + 19/S, de l'arrondi à deux décimales et du maximum de 1,2. Les subdivisions I à III, 1 à 5, a et b, 1° et 2° et leurs positions restent stables pour les renvois depuis 2 duodecies et 2 terdecies F à H. Le délai consultatif de deux mois demeure un avis réputé rendu, sans transformer le silence en avis favorable. Les actes ou dépôts doivent rester postérieurs à l'entrée en vigueur de l'arrêté. Note de 2012 historique.")

draft('2 terdecies E', [
    "Pour appliquer le deuxième alinéa du IV de l'article 199 novovicies du code général des impôts, dans sa rédaction en vigueur au 31 décembre 2017, les zones géographiques caractérisées par un déséquilibre entre l'offre et la demande de logements, autres que celles du premier alinéa de ce IV, correspondent aux communes classées en zone B 2. Cette zone est définie à l'article D. 304-1 du code de la construction et de l'habitation.",
    "Pour appliquer le quatrième alinéa du IV de l'article 199 novovicies du code général des impôts, dans sa rédaction en vigueur au 31 décembre 2017, les zones géographiques autres que celles des premier et deuxième alinéas de ce IV correspondent aux communes classées en zone C. Cette zone est définie à l'article D. 304-1 du code de la construction et de l'habitation.",
],
    "Réécriture à droit constant : chaque catégorie géographique et son renvoi au zonage sont exprimés en deux phrases, en conservant les deux alinéas et la rédaction historique de référence. Aucune réforme de fond.",
    "Date du 31 décembre 2017 conservée dans chacun des deux alinéas. La zone B 2 reste liée au deuxième alinéa du IV et la zone C au quatrième ; les exclusions des autres alinéas du IV sont maintenues. La note de 2019 est historique et n'étend pas ces règles aux investissements d'un autre régime.")

draft('2 terdecies F', [
    "I. - Les plafonds de loyer et de ressources du locataire prévus au 2° du XII de l'article 199 novovicies du code général des impôts sont déterminés selon les règles suivantes :",
    "1. Pour les baux conclus en 2026, le plafond de loyer mensuel par mètre carré, hors charges, est de 12,21 € en Guadeloupe, en Guyane, en Martinique, à La Réunion, à Mayotte, à Saint-Martin et à Saint-Pierre-et-Miquelon. Il est de 14,46 € en Nouvelle-Calédonie, en Polynésie française et dans les îles Wallis et Futuna.",
    "Les plafonds de loyer de l'alinéa précédent sont multipliés par le coefficient défini au 1 du I de l'article 2 terdecies D.",
    "Pour l'application du présent 1, la surface retenue est celle prévue au III de l'article 46 AG terdecies.",
    "2. Les plafonds annuels de ressources des locataires applicables aux baux conclus en 2026 figurent dans le tableau suivant :",
    "Pour l'application du présent 2, les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'impôt sur le revenu établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location. Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du même code.",
    "II. - Les plafonds de loyer du premier alinéa du 1 du I et les plafonds de ressources du 2 du même I sont révisés chaque année au 1er janvier. En Guadeloupe, en Guyane, en Martinique, à La Réunion, à Mayotte, à Saint-Martin et à Saint-Pierre-et-Miquelon, cette révision suit les modalités des 1° des 1 et 1 bis de l'article 46 AG duodecies. En Polynésie française, en Nouvelle-Calédonie et dans les îles Wallis et Futuna, elle suit celles du 2° du 1 et des 2° et 3° du 1 bis du même article.",
    "III. - En Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, les plafonds de loyer du premier alinéa du 1 du I peuvent être réduits dans les conditions et selon les modalités du III de l'article 2 terdecies D, sous les réserves suivantes :",
    "1° Les plafonds de loyer réduits sont révisés chaque année au 1er janvier selon les conditions du II du présent article ;",
    "2° Pour la consultation prévue au 1° du 2 du III de l'article 2 terdecies D, le conseil départemental de l'habitat et de l'hébergement mentionné à l'article L. 364-1 du code de la construction et de l'habitation remplace le comité régional de l'habitat et de l'hébergement.",
],
    "Réécriture à droit constant : les groupes territoriaux et leurs règles d'indexation sont distingués, et les renvois au coefficient, à la surface et à la procédure locale sont formulés directement. Le tableau entier et les dix alinéas sont maintenus. Aucune réforme de fond.",
    "Les deux loyers de 2026, toutes les ressources et majorations du tableau et les deux catégories territoriales sont conservés. Le dernier alinéa du 1 du I reste celui de la surface, visé notamment par 2 terdecies H et D. 321-27 du CCH. Le III reste limité aux cinq départements cités, sans extension à Saint-Martin ou Saint-Pierre-et-Miquelon. Le renvoi d'indexation de Saint-Pierre-et-Miquelon aux 1° des 1 et 1 bis de 46 AG duodecies est celui de la source ; l'article de renvoi ne cite pas ce territoire dans ces 1° et le cite dans ses 2° : discordance préexistante à contrôler, non corrigée ici. Note de 2013 historique.")

draft('2 terdecies G', [
    "Les règles suivantes s'appliquent pour la mise en œuvre du o du 1° du I de l'article 31 du code général des impôts :",
    "1° Les plafonds de loyer sont déterminés selon les règles suivantes :",
    "a) Pour les logements loués dans le cadre d'une convention mentionnée à l'article L. 321-4 du code de la construction et de l'habitation, les plafonds de loyer mensuel par mètre carré, hors charges, sont ceux du 1 du I de l'article 2 terdecies D. Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à La Réunion ou à Mayotte, ils sont ceux du 1 du I de l'article 2 terdecies F applicables à ces collectivités.",
    "Pour l'application du premier alinéa, les logements situés en zone C sont soumis aux plafonds prévus à cet alinéa pour les logements situés en zone B2 du 1 du I de l'article 2 terdecies D. La zone C est celle définie à l'article D. 304-1 du code de la construction et de l'habitation ;",
    "b) Pour les logements loués dans le cadre d'une convention mentionnée à l'article L. 321-8 du code de la construction et de l'habitation, les plafonds de loyer mensuel par mètre carré, hors charges, applicables aux baux conclus en 2026 figurent dans le tableau suivant :",
    "Ces plafonds sont révisés chaque année au 1er janvier selon les modalités du premier alinéa du a de l'article 2 duodecies.",
    "Les zones A, A bis, B1, B2 et C utilisées au présent b sont définies à l'article D. 304-1 du code de la construction et de l'habitation ;",
    "c) Pour l'application du présent 1, la surface retenue est celle prévue au dernier alinéa du a de l'article 2 duodecies ;",
    "d) En application de l'article D. 321-27 du code de la construction et de l'habitation, les conventions mentionnées aux articles L. 321-4 et L. 321-8 du même code peuvent fixer un loyer maximum inférieur aux plafonds des a et b du présent 1 ;",
    "2° Les plafonds de ressources sont déterminés selon les règles suivantes :",
    "a) Pour les logements loués dans le cadre d'une convention mentionnée à l'article L. 321-4 du code de la construction et de l'habitation, les plafonds annuels de ressources des locataires sont ceux du a du 2 du I de l'article 2 terdecies D. Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à La Réunion ou à Mayotte, ils sont ceux du 2 du I de l'article 2 terdecies F applicables à ces collectivités.",
    "Les logements situés en zone C sont soumis aux plafonds annuels de ressources prévus au premier alinéa pour les logements situés en zone B2 du tableau annexé au a du 2 du I de l'article 2 terdecies D. La zone C est celle définie à l'article D. 304-1 du code de la construction et de l'habitation ;",
    "b) Pour les logements loués dans le cadre d'une convention mentionnée à l'article L. 321-8 du code de la construction et de l'habitation, les plafonds annuels de ressources des locataires sont ceux des annexes I et II de l'arrêté pris en application de l'article R. 441-1 du même code ;",
    "c) Pour l'application du présent 2, les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'impôt sur le revenu établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location. Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du même code.",
],
    "Réécriture à droit constant : les règles des conventions intermédiaires et sociales sont distinguées ; les renvois de plafonds et les conditions de ressources sont formulés avec des sujets explicites. Le tableau de loyers est intégralement conservé ainsi que les quatorze alinéas. Aucune réforme de fond.",
    "Montants sociaux et très sociaux de 2026, égalité des plafonds de zone C avec ceux de zone B2, champ ultramarin limité aux cinq départements et faculté d'un loyer conventionnel inférieur maintenus. La source numérote 1° et 2° mais utilise aussi les renvois « présent 1 » et « présent 2 » ; H vise pareillement le a du 2 : ces désignations préexistantes sont maintenues et signalées pour harmonisation éventuelle coordonnée. Le c du 1° renvoie à la surface de 2 duodecies pour tous les logements, tandis que D. 321-27 du CCH prévoit une surface particulière pour les cinq départements d'outre-mer par renvoi à 2 terdecies F : contrôler cette articulation préexistante sans modifier le renvoi ici. Ne pas substituer le tableau de H au renvoi aux annexes de l'arrêté pris pour R. 441-1. Note de 2017 historique.")

draft('2 terdecies H', [
    "Les règles suivantes fixent les plafonds de loyer et de ressources prévus au 3° du A du I de l'article 199 tricies du code général des impôts :",
    "I. - 1. Les plafonds de loyer mensuel sont établis par commune et, à Paris, Lyon et Marseille, par arrondissement.",
    "Pour les baux conclus ou renouvelés en 2022, ces plafonds sont calculés à partir d'une estimation du loyer de marché hors charges, déterminée selon la méthode suivante :",
    "a) Dans les communes ou arrondissements couverts par les observatoires locaux des loyers mentionnés à l'article 16 de la loi n° 89-462 du 6 juillet 1989, l'estimation du loyer de marché hors charges correspond aux loyers médians, exprimés en euros par mètre carré, payés par les locataires ayant emménagé dans leur logement depuis moins d'un an. Les observatoires des loyers calculent ces loyers médians à partir des données de 2018 pour chaque zone du territoire d'observation et les publient sur leur site internet. Ces loyers médians sont révisés selon la variation de l'indice de référence des loyers entre le troisième trimestre 2017 et le troisième trimestre 2021, publié par l'Institut national de la statistique et des études économiques au 1er décembre 2021.",
    "Lorsqu'une commune relève de plusieurs zones mentionnées à l'alinéa précédent, son loyer de marché hors charges de référence est estimé à partir de la moyenne des loyers médians de ces zones, déterminés selon ce même alinéa. Cette moyenne est pondérée par le nombre de logements de la commune en stock dans le parc de chacune de ces zones.",
    "b) Dans les communes non couvertes par un observatoire local des loyers, l'estimation du loyer de marché hors charges est calculée à partir de l'indicateur des loyers-appartements, exprimé en euros par mètre carré, établi pour les appartements-type de 49 mètres carrés mis en location au troisième trimestre 2018. Cet indicateur sert à établir la carte des loyers publiée sur le site internet du ministère chargé du logement. Il est révisé selon la variation de l'indice de référence des loyers entre le troisième trimestre 2017 et le troisième trimestre 2021, publié par l'Institut national de la statistique et des études économiques au 1er décembre 2021. Après cette révision, un forfait de charges locatives de 1,3 euro par mètre carré est retranché.",
    "Pour les baux conclus ou renouvelés en 2023, les plafonds de loyer sont calculés à partir de l'estimation du loyer de marché hors charges déterminée au a ou au b du présent 1. Ils sont actualisés au 1er janvier 2023 selon les modalités de la deuxième phrase du premier alinéa du a de l'article 2 duodecies.",
    "Pour les baux conclus, reconduits ou renouvelés en 2024 et au cours des années paires suivantes, les plafonds de loyer sont définis annuellement au 1er janvier de chaque année à partir d'une nouvelle estimation des loyers de marché hors charges, selon la méthode des a et b du présent 1. Un arrêté conjoint des ministres chargés du logement et de l'économie fixe les données à retenir, notamment leur année de collecte, ainsi que les modalités de leur actualisation, s'il y a lieu.",
    "Pour les baux conclus, reconduits ou renouvelés en 2025 et au cours des années impaires suivantes, les plafonds de loyer calculés à partir de l'estimation du loyer de marché hors charges de l'alinéa précédent sont actualisés selon les modalités de la deuxième phrase du premier alinéa du a de l'article 2 duodecies.",
    "2. L'estimation du loyer de marché définie au 1 du présent I est diminuée d'une décote qui dépend de l'affectation du logement à la location intermédiaire, sociale ou très sociale. Cette décote est fixée à :",
    "- 15 % lorsque le logement est affecté à la location intermédiaire dans le cadre de la convention mentionnée à l'article L. 321-4 du code de la construction et de l'habitation ;",
    "- 30 % lorsque le logement est affecté à la location sociale dans le cadre de la convention mentionnée à l'article L. 321-8 du même code ;",
    "- 45 % lorsque le logement est affecté à la location très sociale dans le cadre de la convention mentionnée au même article L. 321-8.",
    "3. Les plafonds de loyer hors charges résultant du 2 du présent I sont arrondis au centime d'euro le plus proche. Leurs valeurs, pour chaque commune et arrondissement et pour chacune des locations intermédiaire, sociale et très sociale, sont publiées chaque année par arrêté conjoint des ministres chargés du logement et de l'économie.",
    "4. Par dérogation aux 1 et 2 du présent I, les plafonds de loyer mensuel applicables à Mayotte en 2026 figurent dans le tableau suivant :",
    "Ces plafonds de loyer sont actualisés chaque année au 1er janvier selon les modalités de la deuxième phrase du premier alinéa du a de l'article 2 duodecies.",
    "5. Les plafonds de loyer définis aux 3 et 4 du présent I sont multipliés par un coefficient calculé selon la formule suivante :",
    "0,7 + 19/ S,",
    "où S désigne la surface habitable du logement exprimée en mètres carrés. Le coefficient obtenu est arrondi à la deuxième décimale la plus proche, sans pouvoir dépasser 1,2.",
    "6. Pour déterminer les plafonds de loyer et appliquer le 5 du présent I, la surface habitable du logement, exprimée en mètres carrés, est celle prévue au dernier alinéa du a de l'article 2 duodecies. Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, la surface retenue est celle prévue au dernier alinéa du 1 du I de l'article 2 terdecies F.",
    "II. - Les plafonds de ressources sont déterminés selon les règles suivantes :",
    "1. Pour les logements loués en location intermédiaire dans le cadre d'une convention mentionnée à l'article L. 321-4 du code de la construction et de l'habitation, les plafonds annuels de ressources des locataires sont ceux du a du 2 de l'article 2 terdecies G.",
    "2. Pour les logements loués dans le cadre d'une convention mentionnée à l'article L. 321-8 du code de la construction et de l'habitation, les plafonds annuels de ressources des locataires applicables aux baux conclus en 2026 figurent dans les tableaux suivants :",
    "a) Pour les logements affectés à la location sociale :",
    "b) Pour les logements affectés à la location très sociale :",
    "Ces plafonds sont révisés chaque année au 1er janvier selon les modalités du troisième alinéa du b de l'article 2 duodecies. Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à La Réunion ou à Mayotte, la révision suit les modalités du II de l'article 2 terdecies F applicables à ces collectivités.",
    "3. Pour l'application du présent II, les ressources retenues pour le locataire correspondent au revenu fiscal de référence défini au 1° du IV de l'article 1417 du code général des impôts. Il s'agit du revenu figurant sur l'avis d'impôt sur le revenu établi au titre de l'avant-dernière année précédant celle de la signature du contrat de location. Les personnes à charge sont celles mentionnées aux articles 196 à 196 B du même code.",
],
    "Réécriture à droit constant : les méthodes d'estimation et d'actualisation sont décomposées en phrases plus courtes au sein des mêmes alinéas ; le calcul des décotes et du coefficient est rendu explicite. Les deux tableaux de ressources sont présentés avec une ligne par composition de foyer, sans suppression de données ; le tableau de Mayotte est intégralement conservé. Aucune réforme de fond.",
    "Les vingt-sept alinéas et les subdivisions I, II, 1 à 6, a et b sont conservés. Contrôle des millésimes 2017, 2018, 2021 à 2026, de la distinction conclusion/renouvellement puis reconduction à compter de 2024, des 49 m², du forfait de 1,3 euro, des décotes de 15 %, 30 % et 45 %, de la formule et du maximum de 1,2. Les tirets des trois décotes sont des marques d'énumération : il s'agit de diminutions, non de majorations. Les 84 valeurs de ressources des deux tableaux, leurs six colonnes territoriales et les trois plafonds de Mayotte sont conservés. Le renvoi à la deuxième phrase du premier alinéa du a de 2 duodecies vise toujours la révision des loyers. Le régime fiscal de cet article ne crée pas la voie de rénovation locative de vingt-quatre mois prévue par policy.json : celle-ci appelle notamment une disposition dans l'article 6 de la loi n° 89-462 du 6 juillet 1989 et une coordination du décret n° 2002-120 du 30 janvier 2002 relatif au logement décent, pour les exigences énergétiques, les travaux contrôlés et la compensation des surcoûts, hors du présent lot. Note de 2022 historique.")

draft('2 terdecies I', [
    "Pour appliquer le deuxième alinéa du V de l'article 199 tricies du code général des impôts, les conditions fixées au I de cet article sont appréciées en tenant compte des montants suivants :\n1° Le loyer que l'organisme locataire paie au bailleur ;\n2° Le loyer que la personne occupant le logement paie, le cas échéant, à cet organisme ;\n3° Les ressources de la personne occupant le logement.",
],
    "Réécriture à droit constant : les payeurs et bénéficiaires des deux loyers sont explicités, et la prise en compte des ressources de l'occupant est maintenue. L'énumération 1° à 3° reste dans l'alinéa unique. Aucune réforme de fond.",
    "Renvois au deuxième alinéa du V et au I de l'article 199 tricies conservés. Les deux loyers demeurent distincts et la réserve « le cas échéant » ne concerne que celui payé à l'organisme par l'occupant ; aucune condition propre aux anciens régimes n'est substituée à celles du I.")


def paragraph(text):
    return '<p>' + html.escape(text, quote=False).replace('\n', '<br>') + '</p>'


def compact_table(source_table, transpose=False):
    # Table values are public statutory data, preserved rather than paraphrased.
    root = ET.fromstring(re.sub(r'<br\s*/?>', '<br/>', source_table))
    rows = root.findall('.//tr')
    result = []
    for index, row in enumerate(rows):
        cells = list(row)
        if transpose and index == len(rows) - 1:
            columns = []
            for cell in cells:
                values = [v.strip() for v in cell.itertext() if v.strip()]
                assert len(values) == 7, values
                columns.append(values)
            for values in zip(*columns):
                result.append('<tr>' + ''.join('<td>' + html.escape(v, quote=False) + '</td>' for v in values) + '</tr>')
            continue
        row_parts = []
        for cell in cells:
            attrs = ''.join(' ' + k + '="' + v + '"' for k, v in cell.attrib.items())
            assert all(k in {'rowspan', 'colspan'} and v.isdigit() for k, v in cell.attrib.items())
            value = ' '.join(' '.join(cell.itertext()).split())
            row_parts.append('<' + cell.tag + attrs + '>' + html.escape(value, quote=False) + '</' + cell.tag + '>')
        result.append('<tr>' + ''.join(row_parts) + '</tr>')
    return '<table><tbody>' + ''.join(result) + '</tbody></table>'


answers = []
for source in sources:
    number = source['number']
    paras = drafts[number]
    if number in {'2 sexies', '2 undecies'}:
        proposed = '\n'.join(map(paragraph, paras))
    else:
        blocks = re.findall(r'<p>.*?</p>|<table>.*?</table>', source['source_xml'], re.S)
        assert len(paras) == sum(block.startswith('<p>') for block in blocks), number
        parts = []
        para_index = 0
        table_index = 0
        for block in blocks:
            if block.startswith('<p>'):
                parts.append(paragraph(paras[para_index]))
                para_index += 1
            else:
                parts.append(compact_table(block, transpose=(number == '2 terdecies H' and table_index in {1, 2})))
                table_index += 1
        proposed = '\n'.join(parts)
    answers.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': number,
        'proposed_xml': proposed,
        'reason': reasons[number],
        'review_notes': notes[number],
        'status': 'rewrite_draft',
    })

assert len(answers) == 13
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print('answer.json :', len(answers), 'articles ;', sum(len(a['proposed_xml']) for a in answers), 'caractères de texte proposé avec balises.')
