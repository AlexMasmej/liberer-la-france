import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

SOURCES = json.loads(Path('source.json').read_text())
FRAGMENTS = Path('fragments')
FRAGMENTS.mkdir(exist_ok=True)


def clean_xml(text):
    root = ET.fromstring('<root>' + text + '</root>')
    for element in root.iter():
        for name in list(element.attrib):
            if name not in ('rowspan', 'colspan') or not element.attrib[name].isdigit():
                del element.attrib[name]
    return ''.join(ET.tostring(element, encoding='unicode') for element in root).strip()


original = list(ET.fromstring('<root>' + SOURCES[0]['source_xml'] + '</root>'))
blocks = [clean_xml(ET.tostring(element, encoding='unicode')) for element in original]


def p(index, text):
    blocks[index] = '<p>' + text + '</p>'


p(0, "I. - Les équipements, matériaux et appareils mentionnés au 1 de l'article 200 quater du code général des impôts sont ceux énumérés ci-dessous :")
p(2, "2. L'acquisition porte sur les équipements et matériaux suivants :")
p(5, "b) Les matériaux d'isolation thermique suivants :")
p(6, '1° Pour les logements situés en métropole, les matériaux d’isolation thermique des parois opaques satisfont aux résistances thermiques « R » ci-dessous. Cette résistance est évaluée selon les normes NF EN 12664, NF EN 12667 ou NF EN 12939 pour les isolants non-réfléchissants et selon la norme NF EN 16012 pour les isolants réfléchissants :')
p(7, 'Pour les murs en façade ou en pignon, la résistance thermique est supérieure ou égale à 3,7 mètres carrés Kelvin par watt (m<sup>2</sup>. K/W) ;')
p(8, 'Pour les toitures-terrasses, la résistance thermique est supérieure ou égale à 4,5 m<sup>2</sup>. K/W ;')
p(9, 'Pour les rampants de toiture et les plafonds de combles, la résistance thermique est supérieure ou égale à 6 m<sup>2</sup>. K/W ;')
p(10, "Si la performance de l'ouvrage exige de protéger contre les transferts d'humidité les matériaux d'isolation thermique mentionnés au présent 1°, leur pose doit s'accompagner de l'installation d'un pare-vapeur ou d'un autre dispositif assurant un résultat équivalent.")
p(11, '1° bis Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à Mayotte et à La Réunion, les matériaux d’isolation thermique des parois opaques satisfont aux résistances thermiques « R » ci-dessous. Cette résistance est évaluée selon les normes NF EN 12664, NF EN 12667 ou NF EN 12939 pour les isolants non-réfléchissants et selon la norme NF EN 16012 pour les isolants réfléchissants :')
p(12, 'Pour les murs en façade ou en pignon, la résistance thermique est supérieure ou égale à 0,5 mètre carré Kelvin par watt (m<sup>2</sup>. K/W) ;')
p(13, 'Pour les toitures-terrasses, les rampants de toiture et les plafonds de combles, la résistance thermique est supérieure ou égale à 1,5 mètre carré Kelvin par watt (m<sup>2</sup>. K/W).')
p(14, "Si la performance de l'ouvrage exige de protéger contre les transferts d'humidité les matériaux d'isolation thermique mentionnés au présent 1° bis, leur pose doit s'accompagner de l'installation d'un pare-vapeur ou d'un autre dispositif assurant un résultat équivalent.")
p(15, "2° Les matériaux d'isolation thermique des parois vitrées satisfont aux conditions suivantes :")
p(16, 'Les fenêtres ou porte-fenêtres présentent soit un coefficient de transmission thermique (Uw) inférieur ou égal à 1,3 watt par mètre carré Kelvin (W/ m<sup>2</sup>. K) et un facteur de transmission solaire (Sw) supérieur ou égal à 0,3, soit un coefficient Uw inférieur ou égal à 1,7 watt par mètre carré Kelvin (W/ m<sup>2</sup>. K) et un facteur Sw supérieur ou égal à 0,36. Le facteur Sw est évalué selon la norme XP P 50-777 et le coefficient Uw selon la norme NF EN 14 351-1 ;')
p(17, 'Les fenêtres en toiture présentent un coefficient de transmission thermique (Uw) inférieur ou égal à 1,5 watt par mètre carré Kelvin (W/ m<sup>2</sup>. K) et un facteur de transmission solaire (Sw) inférieur ou égal à 0,36. Le facteur Sw est évalué selon la norme XP P 50-777 et le coefficient Uw selon la norme NF EN 14 351-1 ;')
p(18, 'Les doubles fenêtres résultent de la pose, sur la baie existante, d’une seconde fenêtre à double vitrage renforcé, dont le coefficient de transmission thermique (Uw) est inférieur ou égal à 1,8 W/ m<sup>2</sup>. K et le facteur de transmission solaire (Sw) supérieur ou égal à 0,32. Le facteur Sw est évalué selon la norme XP P 50-777 et le coefficient Uw selon la norme NF EN 14 351-1 ;')
p(23, "3. L'acquisition porte sur :")
p(24, "a) Les équipements de chauffage ou de fourniture d'eau chaude sanitaire qui fonctionnent au bois, à d'autres biomasses ou à l'énergie solaire thermique, dans les conditions suivantes :")
p(25, "1° Les équipements de production de chauffage ou de fourniture d'eau chaude sanitaire fonctionnant à l'énergie solaire sont dotés de capteurs solaires et installés avec un appoint intégré. Sont également visés les dispositifs solaires installés sur un appoint séparé, neuf ou existant, pour produire du chauffage ou de l'eau chaude sanitaire. Les capteurs doivent disposer d'une certification CSTBat, Solar Keymark ou équivalente. Ils peuvent être thermiques à circulation de liquide ou d'air, ou hybrides thermiques et électriques à circulation de liquide. La surface hors tout des capteurs installés est supérieure ou égale à 1 m2.<br /><br />a. Les équipements de production de chauffage fonctionnant à l'énergie solaire et les dispositifs solaires installés sur un appoint séparé, neuf ou existant, pour produire du chauffage présentent une efficacité énergétique saisonnière au moins égale aux seuils ci-dessous. Cette efficacité est définie selon le règlement (UE) n° 813/2013 de la commission du 2 août 2013 portant application de la directive 2009/125/CE du Parlement européen et du Conseil en ce qui concerne les exigences d'écoconception applicables aux dispositifs de chauffage des locaux et aux dispositifs de chauffage mixtes :")
p(26, "- 82 % lorsque l'efficacité énergétique saisonnière de l'appoint séparé est inférieure à 82 % ;<br /><br />- 90 % lorsque l'efficacité énergétique saisonnière de l'appoint est inférieure à 90 % ;<br /><br />- 98 % lorsque l'efficacité énergétique saisonnière de l'appoint est supérieure ou égale à 90 % et inférieure à 98 % ;<br /><br />- dans les autres cas, l'efficacité énergétique saisonnière requise dépasse d'au moins 5 points de pourcentage celle de l'appoint.")
p(27, "b. Les équipements de fourniture d'eau chaude sanitaire fonctionnant à l'énergie solaire et les dispositifs solaires installés sur un appoint séparé, neuf ou existant, pour produire de l'eau chaude sanitaire présentent une efficacité énergétique pour le chauffage de l'eau au moins égale aux valeurs du tableau suivant. Cette efficacité est définie par le règlement (UE) n° 814/2013 de la commission du 2 août 2013 portant application de la directive 2009/125/CE du Parlement européen et du Conseil en ce qui concerne les exigences d'écoconception applicables aux chauffe-eau et aux ballons d'eau chaude :")
p(29, "L'efficacité énergétique saisonnière mentionnée au a et l'efficacité énergétique pour le chauffage de l'eau mentionnée au b sont appréciées pour des conditions climatiques moyennes, au sens du règlement (UE) n° 813/2013 de la commission du 2 août 2013 précité.<br /><br />Pour les dispositifs solaires mentionnés aux a et b, l'installateur calcule l'efficacité énergétique saisonnière ou l'efficacité énergétique pour le chauffage de l'eau au moyen d'un logiciel dont les références sont rendues publiques sur le site internet du ministère chargé de l'énergie. Il utilise les données communiquées par le fabricant ou le distributeur, ou celles indiquées sur les composants séparés. Il remet au contribuable la fiche de résultats produite par le logiciel.<br /><br />Lorsque l'appoint assure à la fois le chauffage des locaux et celui de l'eau sanitaire, l'installateur renseigne son efficacité énergétique saisonnière dans le logiciel pour chacun des calculs mentionnés aux a et b. Pour les appoints soumis aux textes suivants, il retient la valeur indiquée sur la fiche produit : la directive 2009/125/CE du Parlement européen et du Conseil du 21 octobre 2009 établissant un cadre pour la fixation d'exigences en matière d'écoconception applicables aux produits liés à l'énergie ; la directive 2010/30/UE du Parlement européen et du Conseil du 19 mai 2010 concernant l'indication, par voie d'étiquetage et d'informations uniformes relatives aux produits, de la consommation en énergie et en autres ressources des produits liés à l'énergie, dans sa version antérieure à son abrogation par le règlement (UE) 2017/1369 du Parlement européen et du Conseil du 4 juillet 2017 établissant un cadre pour l'étiquetage énergétique et abrogeant la directive 2010/30/UE ; ou le règlement (UE) 2017/1369 du Parlement européen et du Conseil du 4 juillet 2017 établissant un cadre pour l'étiquetage énergétique et abrogeant la directive 2010/30/UE. Si l'efficacité énergétique saisonnière de l'appoint n'est pas connue, l'installateur utilise les valeurs conventionnelles du tableau suivant :")
p(31, "Pour les chaudières fonctionnant au bois ou à d'autres biomasses qui servent d'appoint, le critère requis porte sur l'indice d'efficacité énergétique au sens du règlement délégué (UE) 2015/1187 de la Commission du 27 avril 2015 complétant la directive 2010/30/UE du Parlement européen et du Conseil en ce qui concerne l'étiquetage énergétique des chaudières à combustible solide et des produits combinés constitués d'une chaudière à combustible solide, de dispositifs de chauffage d'appoint, de régulateurs de température et de dispositifs solaires. Si cet indice n'est pas connu, la valeur conventionnelle à utiliser est de 98 %.<br /><br />Pour les équipements mentionnés au a qui sont installés sur des planchers chauffants, l'efficacité énergétique saisonnière est calculée au moyen d'un logiciel en retenant, pour le ballon de stockage, un volume conventionnel de 2 000 litres et une classe d'efficacité énergétique A+. Les références du logiciel sont rendues publiques sur le site internet du ministère chargé de l'énergie.")

# Les trois tableaux sont conservés intégralement, avec leurs cellules fusionnées.
for start, end, name in [(0, 32, '18_bis_01.xml')]:
    (FRAGMENTS / name).write_text('\n'.join(blocks[start:end]) + '\n')

p(35, "5° Les équipements indépendants de chauffage ou de production d'eau chaude fonctionnant au bois ou à d'autres biomasses doivent respecter les conditions suivantes :")
p(36, 'a. Les appareils à granulés ou à plaquettes satisfont aux seuils suivants :')
p(40, 'b. Les appareils à bûches ou à d’autres biomasses satisfont aux seuils suivants :')
p(44, "Pour l'application des a et b, les mesures de l'émission de monoxyde de carbone et du rendement énergétique sont effectuées selon les référentiels des normes en vigueur suivants :")
p(46, "- pour les foyers fermés et les inserts de cheminées intérieures, la norme applicable est la norme NF EN 13229. Le montant du crédit d'impôt appliqué à leur acquisition et à leur pose est égal à 600 € toutes taxes comprises ;")
p(48, "L'émission de particules, exprimée en mg/Nm3, est mesurée selon la méthode A1 de l'annexe A de la norme CEN/TS 15883 ou selon une norme équivalente.")
p(49, "- pour les appareils de masse artisanaux de conception unitaire, les valeurs d'émissions et de rendement sont exprimées selon le référentiel de la norme NF EN 15544. Le dimensionnement de l'appareil, y compris sa chambre de combustion, son accumulateur de chaleur et son conduit de fumée, repose sur une note de calcul détaillée. Cette note est établie au moyen d'un logiciel de dimensionnement dont les références sont rendues publiques sur le site internet du ministère chargé de l'énergie.")
p(50, "6° Les chaudières fonctionnant au bois ou à d'autres biomasses doivent respecter les seuils de rendement énergétique et d'émissions de polluants de la classe 5 de la norme NF EN 303.5. Leur puissance est inférieure à 300 kW. Elles sont équipées d'un régulateur de l'une des classes IV, V, VI, VII ou VIII définies au paragraphe 6.1 de la communication de la Commission du 3 juillet 2014 dans le cadre du règlement (UE) n° 813/2013 de la Commission portant application de la directive 2009/125/CE du Parlement européen et du Conseil en ce qui concerne les exigences d'écoconception applicables aux dispositifs de chauffage des locaux et aux dispositifs de chauffage mixtes et du règlement délégué (UE) n° 811/2013 de la Commission complétant la directive 2010/30/UE du Parlement européen et du Conseil en ce qui concerne l'étiquetage énergétique des dispositifs de chauffage des locaux, des dispositifs de chauffage mixtes, des produits combinés constitués d'un dispositif de chauffage des locaux, d'un régulateur de température et d'un dispositif solaire et des produits combinés constitués d'un dispositif de chauffage mixte, d'un régulateur de température et d'un dispositif solaire (2014/C 207/02). Elles répondent également aux conditions suivantes :")
p(51, "a. Les chaudières à alimentation automatique sont associées à un silo, neuf ou existant, d'un volume minimal de 225 litres ;")
p(52, 'b. Les chaudières à alimentation manuelle sont associées à un ballon tampon, neuf ou existant.')
p(53, "b) Les pompes à chaleur spécifiques, telles que celles décrites ci-après, doivent respecter une intensité maximale au démarrage de 45 A en monophasé ou de 60 A en triphasé lorsque leur puissance est inférieure à 25 kW :")
p(54, "1° Les pompes à chaleur énumérées ci-dessous, avec ou sans appoint, présentent une efficacité énergétique saisonnière pour le chauffage supérieure ou égale à 126 % pour les modèles à basse température et à 111 % pour les modèles à moyenne et haute température ;")
p(55, "a. Pour les pompes à chaleur géothermiques eau/ eau et les pompes à chaleur air/ eau, l'efficacité énergétique saisonnière pour le chauffage est calculée selon le règlement (UE) n° 813/2013 de la commission du 2 août 2013 précité ;")
p(56, "b. Pour les pompes à chaleur géothermiques sol/ eau, l'efficacité énergétique saisonnière pour le chauffage est calculée selon le règlement (UE) n° 813/2013 de la commission du 2 août 2013 précité. Le calcul retient une température de 4° C du bain d'eau glycolée, conformément à la norme EN 15879-1, et une température de condensation de 35° C ;")
p(57, "c. Pour les pompes à chaleur géothermiques sol/ sol, l'efficacité énergétique saisonnière pour le chauffage est calculée selon le règlement (UE) n° 813/2013 de la commission du 2 août 2013 précité. Le calcul retient une température d'évaporation fixe de -5° C et une température de condensation de 35° C.")
p(58, "2° Les pompes à chaleur dédiées à la production d'eau chaude sanitaire présentent une efficacité énergétique pour le chauffage de l'eau au moins égale aux valeurs du tableau suivant. Cette efficacité est définie selon le règlement délégué (UE) n° 812/2013 de la Commission du 18 février 2013 complétant la directive 2010/30/UE du Parlement européen et du Conseil en ce qui concerne l'étiquetage énergétique des chauffe-eau, des ballons d'eau chaude et des produits combinés constitués d'un chauffe-eau et d'un dispositif solaire :")
p(60, "c) Les équipements de raccordement à un réseau de chaleur ou de froid alimenté majoritairement par des énergies renouvelables ou par une installation de cogénération comprennent les éléments suivants :")
p(61, "Le branchement privatif, composé de tuyaux et de vannes, qui raccorde le réseau de chaleur ou de froid au poste de livraison de l'immeuble ;")
p(62, "Le poste de livraison, ou sous-station, constitue l'échangeur entre le réseau de chaleur ou de froid et l'immeuble ;")
p(63, "Les matériels nécessaires à l'équilibrage et à la mesure de la chaleur ou du froid pour en assurer la répartition correcte. Selon le cas, ces matériels peuvent être installés avec le poste de livraison, dans les parties communes de l'immeuble collectif ou dans le logement ;")
p(66, "f) Les systèmes de charge pour véhicule électrique sont les bornes de recharge pour véhicules électriques dont les types de prise respectent la norme IEC 62196-2 et la directive 2014/94/UE du Parlement européen et du Conseil du 22 octobre 2014 sur le déploiement d'une infrastructure pour carburants alternatifs ;")
p(67, "g) Les équipements de ventilation mécanique contrôlée double flux sont autoréglables, en installation individuelle ou collective, ou modulés avec des bouches d'extraction hygroréglables, en installation individuelle seulement.")
p(68, "En installation individuelle, le système de ventilation dessert un seul logement. Le caisson de ventilation doit relever de la classe d'efficacité énergétique A ou d'une classe supérieure selon le règlement délégué (UE) n° 1254/2014 de la Commission du 11 juillet 2014 complétant la directive 2010/30/UE du Parlement européen et du Conseil en ce qui concerne l'étiquetage énergétique des unités de ventilation résidentielles. L'échangeur doit présenter une efficacité thermique supérieure à 85 %, mesurée selon la norme NF EN 13141-7. Cette efficacité est certifiée par un organisme établi dans l'Espace économique européen et accrédité selon la norme NF EN ISO/CEI 17065 par le comité français d'accréditation (COFRAC) ou par un autre organisme d'accréditation signataire de l'accord européen multilatéral pertinent dans le cadre de la coordination européenne des organismes d'accréditation. Un caisson de ventilation certifié NF 205 ou équivalent est réputé satisfaire à cette exigence d'efficacité thermique.")
p(69, 'En installation collective, le système dessert plusieurs logements et satisfait aux conditions suivantes :')
p(72, "- l'échangeur statique est collectif et présente une efficacité supérieure ou égale à 75 % selon les normes NF EN 308 ou NF EN 51-763. Un échangeur statique collectif est réputé satisfaire à cette exigence s'il est certifié Eurovent Certified Performance Echangeurs à plaques air-air (AAHE) ou Echangeur régénératif (AARE), ou s'il possède des caractéristiques de performance et de qualité équivalentes. Ces caractéristiques équivalentes sont établies par un organisme établi dans l'Espace économique européen et accrédité selon la norme NF EN ISO/CEI 17065 par le comité français d'accréditation (COFRAC) ou par un autre organisme d'accréditation signataire de l'accord européen multilatéral pertinent pris dans le cadre de la coordination européenne des organismes d'accréditation.")
p(73, "3 bis. La dépose concerne une cuve à fioul, un réservoir de fioul ou un stockage de fioul au sens de l'arrêté du 1er juillet 2004 fixant les règles techniques et de sécurité applicables au stockage de produits pétroliers dans les lieux non visés par la législation des installations classées ni la réglementation des établissements recevant du public, relevant de l'une des catégories suivantes :<br /><br />a) Non enterré en plein air, mentionné au titre IV de l'arrêté du 1er juillet 2004 précité ;<br /><br />b) A rez-de-chaussée ou en sous-sol d'un bâtiment, mentionné au titre V du même arrêté ;<br /><br />c) Enterré, mentionné au titre VI du même arrêté ;<br /><br />d) Autre, mentionné au titre VII du même arrêté ;<br /><br />L'abandon de la cuve, du réservoir ou du stockage de fioul doit respecter les exigences de l'article 28 du même arrêté.")
p(74, "4. Pour les logements situés en Guadeloupe, en Guyane, en Martinique, à Mayotte et à La Réunion, l'acquisition porte sur les équipements et matériaux suivants :")
p(76, 'b) Les équipements ou matériaux suivants protègent les parois opaques ou vitrées contre les rayonnements solaires :')
p(77, '1° Pour la toiture, les systèmes de protection des parois opaques sont les suivants :')
p(80, "2° Pour les murs donnant sur l'extérieur, les systèmes de protection des parois opaques sont les suivants :")
p(84, "3° Pour les baies donnant sur l'extérieur, les systèmes de protection des parois vitrées sont les suivants :")
(FRAGMENTS / '18_bis_02.xml').write_text('\n'.join(blocks[32:92]) + '\n')

audit = [
    "II. - L'audit énergétique mentionné au l du 1 de l'article 200 quater du code général des impôts est réalisé selon les modalités et avec le contenu suivants :",
    "1. L'audit énergétique doit proposer des travaux dont l'une au moins des propositions permet d'atteindre un très haut niveau de performance énergétique du bâtiment. Ces propositions reposent sur les simulations définies ci-après pour les bâtiments à usage principal d'habitation en copropriété et pour les maisons individuelles.",
    "a) Les propositions de travaux comprennent les deux scénarios suivants :",
    "1° Un scénario réalisé en une seule étape, qui vise une baisse d'au moins 30 % des consommations d'énergie primaire. Si la consommation d'énergie primaire avant travaux dépasse 330 kWhEP/m2/an, ce scénario vise également une consommation après travaux inférieure à cette valeur. Les travaux préconisés doivent rester compatibles avec l'atteinte, à plus long terme, du niveau BBC rénovation défini au 2° de l'article 2 de l'arrêté du 29 septembre 2009 relatif au contenu et aux conditions d'attribution du label haute performance énergétique rénovation ;",
    "2° Un scénario qui permet d'atteindre ce niveau BBC rénovation en quatre étapes au maximum. L'ordre des étapes vise à maximiser les économies d'énergie dès les premières étapes, sans compromettre la faisabilité technique ou économique des suivantes et en tenant compte des éventuelles pathologies du bâtiment.",
    "b) Pour chaque étape des scénarios de travaux mentionnés aux 1° et 2° du a du présent 1, l'audit énergétique indique :",
    "1° La consommation annuelle d'énergie primaire du bâtiment après travaux, rapportée à sa surface hors œuvre nette et exprimée en kWhEP/m2SHON/an, pour chacun des usages suivants : chauffage, refroidissement, production d'eau chaude sanitaire, ventilation et éclairage ;",
    "2° La consommation annuelle totale d'énergie primaire du bâtiment après travaux pour l'ensemble de ces usages, exprimée en kWhEP/an et en kWhEP/m2SHON/an ;",
    "3° L'émission annuelle totale de gaz à effet de serre du bâtiment après travaux pour l'ensemble de ces usages, exprimée en kgCO2/ m2SHON/an ;",
    "4° Le classement énergétique du bâtiment résultant des travaux ;",
    "5° Le classement en gaz à effet de serre du bâtiment résultant des travaux ;",
    "6° Les économies d'énergie estimées, d'abord en énergie primaire puis en euros, par rapport à la situation de référence modélisée selon le 3 du présent II pour les bâtiments à usage principal d'habitation en copropriété et selon le 4 du présent II pour les maisons individuelles ;",
    "7° Le coût estimé des travaux, détaillé par action ;",
    "8° Les aides financières qui peuvent être mobilisées.",
    "c) Pour chaque type de travaux proposé, l'audit décrit les critères de performances minimales des équipements, matériaux ou appareils dont les entreprises ont besoin pour réaliser les travaux ;",
    "2. La personne chargée de réaliser l'audit énergétique établit un rapport de synthèse comprenant :",
    "a) La synthèse des constats et des préconisations ;",
    "b) L'état des lieux des différents postes de consommation d'énergie et des principaux défauts identifiés : situation et état du bâti, mode de chauffage et production de chaleur, gestion du chauffage et régulation, ventilation et étanchéité à l'air, coûts annuels d'exploitation. Cet état des lieux inclut le résultat du calcul énergétique prévu au 3 du présent II pour les bâtiments à usage principal d'habitation en copropriété et au 4 du présent II pour les maisons individuelles ;",
    "c) Les propositions de travaux décrites au 1 du présent II. Pour chaque scénario, le rapport précise les coûts prévisionnels, les économies d'énergie attendues, le temps de retour sur investissement et la cohérence globale des travaux ;",
    "d) Tous les éléments mentionnés au 1 du présent II ;",
    "e) Une liste de préconisations pour améliorer la performance et la gestion des équipements. Ces actions portent notamment sur l'équilibrage de l'installation, le désembouage des réseaux de distribution ou la purge des émetteurs de chaleur. Chaque préconisation s'accompagne d'une estimation du coût de sa mise en œuvre et des économies attendues ;",
    "f) Des recommandations incitant les occupants à adopter des comportements sobres en énergie ;",
    "g) Une annexe expliquant les différentes notions techniques ;",
    "h) Un renvoi vers les différents dispositifs locaux et nationaux d'accompagnement de la rénovation énergétique.",
    "Le rapport de synthèse doit être transmis au commanditaire de l'audit dans un délai d'un mois à compter de la date de la visite du bâtiment prévue au 3 du présent II pour les bâtiments à usage principal d'habitation en copropriété et au 4 du présent II pour les maisons individuelles ;",
    "3. Pour les bâtiments à usage principal d'habitation en copropriété, la réalisation de l'audit respecte les modalités suivantes :",
    "a) Le recueil des informations prévu aux articles 2, 3, 4 et 5 de l'arrêté du 28 février 2013 relatif au contenu et aux modalités de réalisation d'un audit énergétique ;",
    "b) Le recueil des données prévu aux articles 6 et 7 de l'arrêté du 28 février 2013 précité ;",
    "c) La modélisation du bâtiment prévue à l'article 8 du même arrêté ;",
    "4. Pour les maisons individuelles, la réalisation de l'audit respecte les modalités suivantes :",
    "a) Le propriétaire remet à la personne qui réalise l'audit les factures des travaux déjà réalisés, le cas échéant, les devis des travaux éventuellement envisagés et, s'il en dispose, le diagnostic de performance énergétique ;",
    "b) L'auditeur visite le site en présence du propriétaire, si possible pendant la saison de chauffe. Lors de la visite, il établit un descriptif des modes constructifs, des principales caractéristiques thermiques et géométriques du logement et de ses équipements énergétiques. Les occupants sont interrogés sur leurs habitudes d'utilisation et de gestion des différents équipements du logement, notamment l'ouverture des fenêtres, le puisage d'eau chaude et d'eau froide et la régulation des émetteurs. Ils sont aussi interrogés sur les dépenses annuelles liées à ces équipements et sur leur appréciation du confort thermique ;",
    "c) L'audit énergétique estime la consommation annuelle d'énergie de la maison pour le chauffage, le refroidissement, la production d'eau chaude sanitaire, l'éclairage et la ventilation.",
    "L'estimation repose sur les factures énergétiques transmises par le commanditaire de l'audit. Elle intègre des redressements climatiques et s'accompagne d'une analyse de l'évolution des consommations énergétiques au cours des trois dernières années ;",
    "d) L'audit énergétique établit un diagnostic des qualités architecturales et thermiques préexistantes de la maison et des défauts qui nécessitent des travaux d'amélioration de sa performance énergétique ;",
    "e) L'audit énergétique modélise la maison au moyen d'un logiciel de simulation énergétique. Les données d'entrée du modèle sont ajustées aux conditions réellement observées. Les conditions d'occupation des logements retenues dans la simulation sont notamment conformes à celles observées lors de la visite du site.",
    "La modélisation doit produire des consommations énergétiques simulées proches des consommations réelles. Elle doit aussi permettre de proposer des actions pertinentes d'amélioration de la performance énergétique de la maison. A cette fin, elle simule la réalisation de travaux sur les éléments constitutifs de l'enveloppe du bâtiment ainsi que sur les équipements de production d'eau chaude sanitaire, de ventilation et d'éclairage.",
]
p(92, '<br /><br />'.join(audit))
(FRAGMENTS / '18_bis_03.xml').write_text(blocks[92] + '\n')

p(93, "III. - Le bouquet de travaux mentionné au o du 1 de l'article 200 quater du code général des impôts est réalisé dans les conditions suivantes :")
p(94, "1. Le bouquet doit associer des travaux relevant d'au moins deux des quatre catégories suivantes : chauffage, production d'eau chaude sanitaire, ventilation et isolation de l'enveloppe de la maison.")
p(95, "2. Une ou plusieurs entreprises certifiées « offre globale » assurent la conception, la réalisation et le suivi du projet de rénovation globale. Cette certification est conforme au troisième alinéa du I de l'article 1er et à l'annexe II de l'arrêté du 1er décembre 2015 relatif aux critères de qualifications requis pour le bénéfice du crédit d'impôt pour la transition énergétique et des avances remboursables sans intérêt destinées au financement de travaux de rénovation afin d'améliorer la performance énergétique des logements anciens.")
p(96, "3. Après rénovation, les émissions annuelles de gaz à effet de serre, rapportées à la surface habitable de la maison, ne doivent pas dépasser leur valeur initiale avant travaux.")
p(97, "4. Le respect des exigences relatives aux consommations conventionnelles annuelles en énergie primaire avant et après travaux, mentionnées au o du 1 de l'article 200 quater précité, est justifié dans les conditions suivantes :")
p(98, "a) Avant les travaux, une personne répondant aux conditions du décret n° 2018-416 du 30 mai 2018 relatif aux conditions de qualification des auditeurs réalisant l'audit énergétique éligible au crédit d'impôt sur le revenu pour la transition énergétique prévues au dernier alinéa du 2 de l'article 200 quater du code général des impôts réalise un audit énergétique défini au II ;")
p(99, "b) Une liste indique les travaux préconisés par l'audit énergétique, leurs niveaux de performance et leur correspondance avec la liste des travaux réalisés. Elle est datée et signée par le bénéficiaire et le maître d'œuvre ;")
p(100, "c) Si les travaux réalisés diffèrent des travaux préconisés, l'audit énergétique doit être mis à jour à partir des travaux effectivement réalisés.")
(FRAGMENTS / '18_bis_04.xml').write_text('\n'.join(blocks[93:]) + '\n')

proposals = {'18 bis': ''.join((FRAGMENTS / f'18_bis_{i:02}.xml').read_text() for i in range(1, 5)).strip()}

sanitary = [
    'éviers et lavabos à hauteur réglable',
    'éviers et lavabos fixes utilisables par les personnes à mobilité réduite',
    'siphon déporté',
    'sièges de douche muraux',
    'cabines de douche intégrales pour personnes à mobilité réduite',
    'bacs à douche extra-plats et portes de douche',
    'receveurs de douche à carreler',
    "pompes de relevage ou pompes d'aspiration des eaux pour receveur extra-plat",
    'w.-c. surélevés',
    'w.-c. suspendus avec bâti support',
    "w.-c. équipés d'un système lavant et séchant",
    'robinetteries pour personnes à mobilité réduite',
    'mitigeurs thermostatiques',
    'miroirs inclinables pour personnes à mobilité réduite',
]
accessibility = [
    "systèmes de commande comprenant un détecteur de mouvements, de signalisation ou d'alerte",
    "dispositifs de fermeture, d'ouverture ou systèmes de commande des installations électriques, d'eau, de gaz et de chauffage",
    'éclairages temporisés couplés à un détecteur de mouvements',
    "systèmes de motorisation de volets, de portes d'entrée et de garage, de portails",
    'volets roulants électriques',
    "appareils élévateurs verticaux comportant une plate-forme aménagée en vue du transport d'une personne handicapée et élévateurs à déplacements inclinés spécialement conçus pour le déplacement d'une personne handicapée, définis à l'article 30-0 C",
    'mains courantes',
    "barres de maintien ou d'appui",
    'poignées ou barres de tirage de porte adaptées',
    'systèmes de transfert à demeure ou potences au plafond',
    'rampes fixes',
    'plans inclinés',
    'mobiliers à hauteur réglable',
    'revêtements podotactiles',
    'nez de marche contrastés et antidérapants',
    'revêtements de sol antidérapant',
    "protections d'angles",
    'garde-corps',
    'portes ou fenêtres adaptées, inversion ou élargissement de portes',
    'portes coulissantes',
    'boucles magnétiques',
]
proposals['18 ter'] = (
    "<p>Pour l'application du a du 1 de l'article 200 quater A du code général des impôts, les installations et équipements permettant d'adapter les logements à la perte d'autonomie ou au handicap sont les suivants :</p>\n"
    '<p>1° Les équipements sanitaires énumérés ci-dessous doivent être attachés à perpétuelle demeure :<br />'
    + ' ;<br />'.join(sanitary) + ' ;</p>\n'
    + "<p>2° Les équipements de sécurité et d'accessibilité énumérés ci-dessous doivent être attachés à perpétuelle demeure :<br />"
    + ' ;<br />'.join(accessibility) + '.</p>'
)

proposals['18 ter A'] = """<p>Une borne de recharge pour véhicule électrique constitue un système de charge pilotable au sens du 1 de l'article 200 quater C du code général des impôts si elle satisfait aux trois conditions cumulatives suivantes :</p>
<p>1° La borne possède un point de recharge équipé d'un socle de prise de courant de type 2 ou d'un connecteur pour véhicules de type 2, tels que décrits à l'annexe II du règlement (UE) 2023/1804 du Parlement européen et du Conseil du 13 septembre 2023 sur le déploiement d'une infrastructure pour carburants alternatifs et abrogeant la directive 2014/94/ UE ;</p>
<p>2° La borne peut moduler temporairement la puissance électrique appelable sur le point de recharge mentionné au 1°, après réception et interprétation des signaux tarifaires transmis par les fournisseurs d'électricité et des signaux transmis par les gestionnaires du réseau de distribution au sens du premier alinéa de l'article L. 341-4 du code de l'énergie ;</p>
<p>3° La borne est connectée selon l'une des modalités suivantes :</p>
<p>a) Soit au compteur électrique mis à disposition par les gestionnaires du réseau de distribution au sens du premier alinéa de l'article L. 341-4 du code de l'énergie. Ce compteur doit pouvoir recevoir et interpréter les signaux tarifaires transmis par les fournisseurs d'électricité et les signaux transmis par les gestionnaires du réseau de distribution ;</p>
<p>b) Soit à un équipement intermédiaire fixe qui permet de transmettre un signal de modulation de puissance ;</p>
<p>c) Soit à internet.</p>"""

proposals['18 quater'] = """<p>I. – Pour l'application du 6° du I de l'article 199 undecies C du code général des impôts, sont retenues les dépenses d'acquisition, d'installation et de pose des éléments suivants :</p>
<p>1. Les dispositifs constructifs, équipements ou matériaux d'isolation thermique ayant pour finalité essentielle de protéger contre le rayonnement solaire les parois opaques en contact avec l'extérieur et/ou les baies en contact avec l'extérieur, ou d'assurer une ventilation naturelle de confort thermique. Ils visent à limiter le recours à la climatisation et répondent aux conditions suivantes :</p>
<p>a) En Guadeloupe, en Martinique, en Guyane et à La Réunion, ils respectent les exigences des articles 5 (1°), 6 et 10 de l'arrêté du 17 avril 2009 définissant les caractéristiques thermiques minimales des bâtiments d'habitation neufs dans les départements de la Guadeloupe, de la Martinique, de la Guyane et de La Réunion ;</p>
<p>b) A Mayotte, ils respectent les exigences du 1 de la partie B de l'annexe 1 de l'arrêté préfectoral n° 192 PM/ SG/ DE/08 du 15 octobre 2008 relatif aux subventions par l'Etat pour la construction, l'acquisition et l'amélioration de logements locatifs sociaux ;</p>
<p>c) En Nouvelle-Calédonie, en Polynésie française, à Saint-Martin, à Saint-Barthélemy et dans les îles Wallis et Futuna, sont notamment concernés les éléments suivants :</p>
<p>1° Surtoiture ventilée ;</p>
<p>2° Isolation thermique ;</p>
<p>3° Bardage ventilé ;</p>
<p>4° Pare-soleil horizontaux ;</p>
<p>5° Brise-soleil verticaux ;</p>
<p>6° Protections solaires mobiles extérieures dans le plan des baies ;</p>
<p>7° Ventilateurs de plafond ;</p>
<p>2. Les matériaux d'isolation thermique destinés à maîtriser les besoins en chauffage répondent aux conditions suivantes :</p>
<p>a) Pour les bâtiments d'habitation construits à La Réunion à une altitude supérieure à 800 mètres, ils respectent les exigences de l'article 5 (2°) de l'arrêté du 17 avril 2009 définissant les caractéristiques thermiques minimales des bâtiments d'habitation neufs dans les départements de la Guadeloupe, de la Martinique, de la Guyane et de La Réunion ;</p>
<p>b) A Saint-Pierre-et-Miquelon, les matériaux sont ceux visés aux 1°, 2° et 4° du b du 2 du I de l'article 18 bis dans sa rédaction en vigueur au 31 décembre 2019 ;</p>
<p>3. Les appareils de régulation de chauffage sont ceux visés au c du 2 du I de l'article 18 bis dans sa rédaction en vigueur au 31 décembre 2019 ;</p>
<p>4. Les équipements de production d'énergie utilisant une source d'énergie renouvelable sont ceux visés au a du 3 du I de l'article 18 bis dans sa rédaction en vigueur au 31 décembre 2019. Pour les systèmes de fourniture d'électricité à partir de l'énergie solaire, les installations ne doivent pas être reliées au réseau du service public d'électricité en Guadeloupe, en Martinique, en Guyane, à La Réunion, à Mayotte, à Saint-Pierre-et-Miquelon, à Saint-Martin et à Saint-Barthélemy ;</p>
<p>5. Les pompes à chaleur, autres que air/ air, ont pour finalité essentielle la production de chaleur ou d'eau chaude sanitaire et sont celles visées au b du 3 du I de l'article 18 bis dans sa rédaction en vigueur au 31 décembre 2019. Est également pris en compte le coût de la pose de l'échangeur souterrain des pompes à chaleur géothermiques ;</p>
<p>6. Les équipements de raccordement à un réseau de chaleur sont ceux visés au c du 3 du I de l'article 18 bis dans sa rédaction en vigueur au 31 décembre 2019. Le réseau est alimenté majoritairement par des énergies renouvelables ou par une installation de cogénération.</p>
<p>Pour l'application du présent article, une baie en contact avec l'extérieur est une ouverture ménagée dans une paroi extérieure au logement et servant à l'éclairage, au passage ou à l'aération.</p>
<p>II. – Une facture détaillée doit justifier les dépenses mentionnées au I. Elle précise leur nature exacte, leur coût et leur conformité aux critères techniques exigés.</p>"""

proposals['23 bis'] = """<p>Pour l'application du 3° quinquies de l'article 208 du code général des impôts, les revenus suivants sont assimilés aux bénéfices provenant des contrats de crédit-bail conclus avec l'exploitant public avant le 1er janvier 1993 :</p>
<p>1° Les profits que les sociétés agréées pour le financement des télécommunications retirent du placement à vue ou à court terme des sommes en instance d'emploi, lorsque ce placement peut être qualifié d'opération de trésorerie accessoire. Cette condition est réputée remplie pour la fraction des placements dont la valeur nominale, pour chaque exercice, ne dépasse pas la moitié des dépenses annuelles de gestion, augmentée du montant des dividendes mis en paiement au cours de l'exercice et du montant de l'augmentation de capital libérée par les actionnaires pendant cet exercice et l'exercice précédent ;</p>
<p>2° Les intérêts que l'exploitant public verse au titre des avances sur marchés consenties par les sociétés agréées aux constructeurs, fournisseurs et autres ayants droit avant la livraison des immeubles et équipements.</p>"""

proposals['23 ter'] = """<p>Les personnes morales mentionnées au 2 de l'article 218 A du code général des impôts sont imposées aux lieux suivants :</p>
<p>Les sociétés ou personnes morales qui exercent leur activité en France dans un ou plusieurs établissements sont imposées au lieu de leur principal établissement ;</p>
<p>Les sociétés ou personnes morales qui exercent une activité en France sans y avoir d'établissement sont imposées au service des impôts des entreprises étrangères ;</p>
<p>Les sociétés et personnes morales qui disposent en France de propriétés immobilières, données ou non en location, et n'y exercent aucune activité autre qu'immobilière sont imposées au lieu de situation de ces biens. Lorsque cette règle conduit à plusieurs lieux d'imposition, l'impôt est établi au service des impôts des entreprises étrangères.</p>"""

reasons = {
    '18 bis': "Réécriture à droit constant : les conditions d'isolation, de chauffage, de recharge et de ventilation sont formulées avec des sujets explicites ; les longues phrases relatives aux calculs énergétiques sont scindées. Les obligations de l'installateur, le contenu de l'audit, ses deux scénarios, son rapport et le suivi du bouquet de travaux sont explicités. Les trois tableaux sont reproduits intégralement et les subdivisions, alinéas, mentions d'abrogation, seuils et références techniques sont conservés. Aucune réforme de fond de policy.json ne vise directement ces critères du crédit d'impôt pour la transition énergétique.",
    '18 ter': "Réécriture à droit constant : la disposition introductive désigne directement les installations et équipements concernés ; chaque subdivision énonce explicitement l'exigence d'attache à perpétuelle demeure. La présentation ligne par ligne rend les deux listes complètes plus lisibles sans déplacer les alinéas numérotés ni modifier les catégories ou le renvoi aux élévateurs. Aucune réforme de fond prévue par policy.json ne modifie ce régime d'adaptation du logement.",
    '18 ter A': "Réécriture à droit constant : la borne est le sujet explicite des trois conditions cumulatives. Les caractéristiques du point de recharge, la réception et l'interprétation des signaux et les trois possibilités alternatives de connexion sont distinguées ; la capacité exigée du compteur est formulée dans une phrase propre. Aucun nouveau critère ni réforme de fond n'est ajouté au régime de l'article 200 quater C.",
    '18 quater': "Réécriture à droit constant : les dépenses admissibles, les exigences territoriales et les conditions propres à chaque catégorie d'équipements sont énoncées directement. Les phrases sur le raccordement électrique, les pompes à chaleur et la facture justificative sont scindées ; le coût de pose de l'échangeur souterrain reste expressément couvert. Les renvois historiques sont conservés. Aucune mesure de policy.json ne supprime ni n'étend cette réduction d'impôt outre-mer.",
    '23 bis': "Réécriture à droit constant : les deux catégories de revenus assimilés sont désignées directement ; les sociétés et l'exploitant public sont les sujets des phrases. La condition de trésorerie accessoire et le calcul de la fraction de placements réputée la remplir sont rendus plus lisibles, sans changer la moitié des frais de gestion ni les montants qui s'y ajoutent. Le régime des contrats antérieurs au 1er janvier 1993 reste distinct de la réforme du taux normal de l'IS.",
    '23 ter': "Réécriture à droit constant : chaque catégorie de personne morale est le sujet d'une règle explicite de lieu d'imposition. La règle immobilière et son exception en présence de plusieurs lieux sont formulées dans deux phrases. Aucun changement de service compétent ni de rattachement territorial n'est introduit ; la part territoriale d'IS envisagée dans policy.json ne constitue pas une nouvelle règle de lieu d'imposition.",
}

reviews = {
    '18 bis': "Point préexistant à contrôler : au I, 3, a, 1°, a, les cas d'efficacité de l'appoint inférieure à 82 % et inférieure à 90 % se chevauchent ; les quatre branches et leurs valeurs sont conservées sans inventer une borne inférieure au deuxième cas. Les trois tableaux, les seuils stricts ou inclusifs, les normes, le montant de 600 € TTC et les valeurs conventionnelles sont maintenus. Le I, 3, f conserve la directive 2014/94/UE : l'article 18 ter A relève du régime distinct des bornes pilotables de l'article 200 quater C et cite son abrogation par le règlement (UE) 2023/1804 ; une actualisation du renvoi ancien exigerait un examen temporel distinct. Le corpus de l'article 200 quater mentionne des dépenses payées jusqu'au 31 décembre 2020 ; la note source fixe l'entrée en vigueur des présentes dispositions au 1er janvier 2021 en application du III de l'article 6 de l'arrêté du 3 juin 2020. Cette articulation temporelle doit être contrôlée sans rouvrir le crédit d'impôt ni supprimer les règles historiques. Le II conserve les unités SHON, les renvois aux arrêtés de 2009 et 2013 et les passages internes séparés par des br ; aucune subdivision ni aucun alinéa n'est déplacé. Les textes techniques extérieurs ne sont pas modifiés par cette proposition.",
    '18 ter': "Les 14 entrées sanitaires et les 21 entrées de sécurité et d'accessibilité sont conservées, y compris les alternatives internes et l'attache à perpétuelle demeure. Le renvoi à l'article 30-0 C a été vérifié dans le corpus public fourni : il définit les appareils élévateurs verticaux et les élévateurs à déplacements inclinés. Les trois alinéas et les 1° et 2° restent en place. Les conditions personnelles, temporelles et financières du crédit d'impôt restent celles de l'article 200 quater A, dont le corpus prévoit des échéances au 31 décembre 2025 ; la présente liste technique ne les prolonge pas. Aucune note source particulière.",
    '18 ter A': "Conserver le caractère cumulatif des 1°, 2° et 3°, puis le caractère alternatif des a), b) et c). Les deux mentions du type 2, le double flux de signaux et les deux renvois au premier alinéa de l'article L. 341-4 du code de l'énergie sont maintenus. Le règlement (UE) 2023/1804 du 13 septembre 2023 et la référence à la directive 2014/94/UE abrogée sont conservés. Ne pas appliquer ces conditions à l'ancien régime du I, 3, f de l'article 18 bis. Les conditions et échéances du crédit d'impôt demeurent dans l'article 200 quater C ; le corpus fourni mentionne le 31 décembre 2025, sans prolongation par cette proposition. Aucune note source particulière.",
    '18 quater': "Les cinq renvois à l'article 18 bis visent expressément sa rédaction en vigueur au 31 décembre 2019 ; ils ne sont pas remplacés par les critères actuels. Cette version historique n'est pas une source assignée dans ce lot : son contenu doit rester la référence pour l'application des renvois. Sont conservés le seuil strictement supérieur à 800 mètres à La Réunion, les territoires propres à chaque branche, l'exclusion des pompes air/air, la condition d'absence de raccordement électrique pour les huit territoires énumérés et la facture détaillée. Le 6° du I de l'article 199 undecies C a été vérifié dans le corpus fourni. La note source relate une modification de conséquence de l'article 1er-I C 2° de l'arrêté du 1er mars 2019 ; elle n'est pas traitée comme une date d'entrée en vigueur d'une réforme nouvelle. Aucun changement de fond ou coordination de taux d'IS n'est requis ici.",
    '23 bis': "Le renvoi au 3° quinquies de l'article 208 a été vérifié dans le corpus fourni : le régime vise bien les contrats conclus avec l'exploitant public avant le 1er janvier 1993. Le seuil conserve la moitié des dépenses annuelles de gestion, à laquelle s'ajoutent intégralement les dividendes mis en paiement pendant l'exercice et l'augmentation de capital libérée pendant l'exercice et le précédent. Le 2° conserve les constructeurs, fournisseurs et autres ayants droit ainsi que la condition d'antériorité à la livraison. La réforme du taux national normal de l'IS à l'article 219 ne modifie pas cette assimilation liée à une exonération particulière. Aucune note source particulière.",
    '23 ter': "Le renvoi au 2 de l'article 218 A a été vérifié dans le corpus fourni ; il vise les personnes morales exerçant une activité ou possédant des biens en France sans y avoir leur siège social. L'ordre et les quatre alinéas sont conservés, ainsi que le principal établissement, les deux cas de compétence du service des impôts des entreprises étrangères et les biens loués ou non. La part territoriale d'IS de zéro à cinq points demeure à créer : ses règles d'assiette, de vote, de répartition entre entreprises multi-sites et de péréquation doivent être fixées par des dispositions législatives propres, coordonnées avec l'article 219, puis par les textes territoriaux et d'application nécessaires. Le présent article de lieu d'imposition ne suffit pas à les établir et aucun renvoi nouveau n'est inventé. Aucune note source particulière.",
}

answer = []
for source in SOURCES:
    number = source['number']
    xml = clean_xml(proposals[number])
    if number != '18 bis':
        (FRAGMENTS / (number.replace(' ', '_') + '.xml')).write_text(xml + '\n')
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': number,
        'proposed_xml': xml,
        'reason': reasons[number],
        'review_notes': reviews[number],
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
