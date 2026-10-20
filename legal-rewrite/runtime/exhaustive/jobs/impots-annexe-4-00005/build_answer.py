import json
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sources = json.loads((ROOT / 'source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }


add('23 M quater', '''
<p>Pour l'application du 3° du A du II de l'article 244 quater I du code général des impôts, les opérations concernées sont les suivantes :</p>
<p>1° La fabrication d'éoliennes terrestres et d'éoliennes en mer ainsi que, pour ces dernières, leur assemblage final ;</p>
<p>2° La fabrication des équipements suivants : mâts ; pales ; aimants permanents ; moyeux de rotor ; roulements principaux, à lacets et à pas variable ; boîtes de vitesses ; systèmes de transmission par entraînement direct ou avec multiplicateur, y compris le générateur ; fondations posées ou flottantes ; blocs d'acier ou structures en béton pour les fondations flottantes ; systèmes d'ancrages pour les fondations flottantes ; sous-stations électriques à terre ou en mer, y compris l'appareillage de commutation ; disjoncteurs ; relais de protection ; convertisseurs ; transformateurs, y compris les noyaux magnétiques, les bobines et les changeurs de prise en charge ; câbles dynamiques et électriques de raccordement, notamment inter-éoliens. Est également concerné l'assemblage des nacelles ;</p>
<p>3° L'extraction, la production, la transformation et la valorisation des matières premières critiques visées au c du 3° du A du II de l'article 244 quater I du code général des impôts, à savoir les terres rares, le fil d'aluminium et le cuivre.</p>
''',
    "Réécriture à droit constant : le rattachement au crédit d'impôt est explicité et la longue énumération du 2° est ponctuée par familles d'équipements ; l'assemblage des nacelles reste une opération distincte de leur fabrication. Aucune réforme de fond de policy.json ne vise cette liste.",
    "Les 1°, 2° et 3° sont maintenus dans leur ordre. Toutes les catégories et inclusions du 2°, ainsi que les trois matières du 3°, sont conservées. Les termes techniques de la source, notamment « roulements […] à lacets » et « changeurs de prise en charge », sont conservés sans correction technique implicite ; leur terminologie appelle un contrôle spécialisé. Articulation à conserver avec le 3° du A du II de l'article 244 quater I et le recyclage de l'article 23 M sexies. Aucun taux d'IS ni dispositif nouveau n'est introduit.")

add('23 M quinquies', '''
<p>Pour l'application du 4° du A du II de l'article 244 quater I du code général des impôts, les opérations concernées sont les suivantes :</p>
<p>1° La fabrication de pompes à chaleur, quelle que soit la technologie employée ;</p>
<p>2° La fabrication des équipements suivants : compresseurs à spirale et compresseurs rotatifs ; vannes à quatre voies ; échangeurs de chaleur résistant aux conditions de fonctionnement corrosives géothermiques ; pompes submersibles résistant à ces mêmes conditions ;</p>
<p>3° L'extraction, la production, la transformation et la valorisation des matières premières critiques visées au c du 4° du A du II de l'article 244 quater I du code général des impôts.</p>
''',
    "Réécriture à droit constant : le champ de chaque opération est présenté directement et les composants sont séparés par des points-virgules. La condition de résistance à la corrosion géothermique reste attachée aux échangeurs et aux pompes submersibles. Aucune réforme de fond n'est appliquée à ce régime distinct.",
    "Les trois subdivisions, l'absence de restriction technologique au 1° et les renvois au 4° du A du II de l'article 244 quater I sont conservés. L'article 23 M sexies complète le champ par le recyclage ; aucune matière première non nommée par la source n'est ajoutée.")

add('23 M sexies', '''
<p>Les opérations d'extraction, de production, de transformation et de valorisation des matières premières critiques visées au c des 1° à 4° du A du II de l'article 244 quater I du code général des impôts comprennent également le recyclage de ces matières.</p>
<p>Pour le recyclage des déchets de batteries et des rebuts de production prévu au 3° de l'article 23 M bis, seules sont éligibles les activités visant soit la récupération finale de matières premières recyclées sous forme de sels de métaux à l'issue d'un recyclage par lixiviation, soit la régénération des matières actives de cathode à l'issue d'un recyclage direct. La production de broyat noir (black mass) n'est éligible que si elle est associée à l'activité de recyclage des déchets de batteries et des rebuts de production définie à la phrase précédente.</p>
''',
    "Réécriture à droit constant : l'inclusion du recyclage est formulée directement et les deux voies éligibles de récupération ou de régénération sont distinguées par « soit […] soit ». Le lien obligatoire entre production de broyat noir et recyclage final est explicite. Aucune réforme de fond n'affecte ces critères.",
    "Les deux alinéas et leurs champs distincts sont conservés : recyclage général des matières visées aux 1° à 4°, puis restriction propre aux batteries et rebuts. Le renvoi au 3° de l'article 23 M bis a été vérifié dans le corpus public : ce 3° mentionne bien les déchets de batteries et les rebuts de production. Aucun recyclage intermédiaire autonome n'est rendu éligible.")

add('23 N', '''
<p>Pour l'application du 1° du 1 du II de l'article 257 du code général des impôts, la limite est de 73 € toutes taxes comprises.</p>
''',
    "Réécriture à droit constant de la phrase fixant le seuil : son champ d'application précède désormais le montant. Aucun changement de fond ni réévaluation du seuil n'est prévu par policy.json.",
    "Le seuil de 73 €, son caractère toutes taxes comprises et le renvoi complet sont conservés. La note source mentionne l'arrêté du 12 octobre 2005, article 3, alors que la version fournie prend effet le 12 juin 2021 : cette indication historique ne suffit pas à établir l'origine temporelle du montant actuel et reste à contrôler ; elle n'est pas utilisée comme date d'une réforme.")

add('23 O', '''
<p>Pour l'application du 5° de l'article 260 C du code général des impôts, les rémunérations suivantes sont assimilables à des intérêts ou à des agios :</p>
<p>la commission du plus fort découvert ;</p>
<p>la commission d'endos ;</p>
<p>la commission d'attente, d'engagement, d'ouverture ou de confirmation de crédit ;</p>
<p>la commission de caution, d'aval ou de ducroire ;</p>
<p>la commission d'acceptation ;</p>
<p>la commission de garantie de placement d'obligations ou de bonne fin d'augmentation de capital ;</p>
<p>la commission de garantie de bonne fin d'opérations immobilières ;</p>
<p>les frais de gestion réglementés perçus par les sociétés de crédit différé ;</p>
<p>la rémunération que perçoit l'intermédiaire placeur d'emprunts émis par voie d'adjudication.</p>
''',
    "Réécriture à droit constant : la phrase introductive énonce directement l'assimilation et chaque rémunération est présentée dans un alinéa lisible. La dernière rubrique explicite le bénéficiaire de la rémunération. Aucune réforme de fond ne porte sur cette exclusion de l'option à la TVA.",
    "Les neuf rubriques demeurent dans l'ordre de la source, sans numérotation ajoutée. Les termes bancaires, la restriction aux frais de gestion réglementés et le renvoi au 5° de l'article 260 C sont conservés ; l'assimilation reste limitée à l'application de ce renvoi.")

add('23 P', '''
<p>Pour l'application du 9° de l'article 260 C du code général des impôts, les opérations bancaires afférentes au financement d'exportations, de livraisons exonérées en vertu du I de l'article 262 ter du même code ou d'opérations situées hors de France sont les suivantes :</p>
<p>1° L'escompte d'effets de commerce ou de moyens de paiement représentant des créances sur l'étranger ;</p>
<p>2° La mobilisation des créances sur l'étranger ;</p>
<p>3° Le préfinancement d'exportations ou de livraisons exonérées en vertu du I de l'article 262 ter du code général des impôts, sous la forme de crédits mobilisables auprès de la Banque de France ;</p>
<p>4° Les cautions, avals et confirmations de crédits documentaires fournis en France et se rapportant à des exportations ou à des livraisons exonérées en vertu du I de l'article 262 ter du même code ;</p>
<p>5° Les prêts consentis aux acheteurs étrangers de biens d'équipement et d'autres produits français ;</p>
<p>6° Les achats fermes de créances sur des clients étrangers, effectués auprès d'entreprises françaises réalisant des exportations ou des livraisons exonérées en vertu du I de l'article 262 ter du même code.</p>
''',
    "Réécriture à droit constant : l'introduction rattache directement les six opérations à l'exclusion d'option et le 6° distingue plus clairement les créances achetées des entreprises cédantes. Aucun changement de fond ne modifie ce régime bancaire.",
    "Les six numéros et leurs conditions sont maintenus, notamment la mobilisation auprès de la Banque de France au 3°, la fourniture en France au 4° et le caractère ferme de l'achat au 6°. Les renvois au 9° de l'article 260 C et au I de l'article 262 ter sont conservés.")

add('24 bis', '''
<p>En application du d du 2° du I de l'article 262 du code général des impôts, la livraison est exonérée lorsque la valeur globale des biens, taxe sur la valeur ajoutée comprise, excède 100 € et que ces biens ont été acquis soit dans un magasin, soit, dans un délai de trois jours calendaires, dans plusieurs magasins disséminés dans une même ville et identifiés sous le même numéro de taxe sur la valeur ajoutée intracommunautaire.</p>
''',
    "Réécriture à droit constant : les conditions de valeur et de lieu d'achat sont exprimées explicitement, avec les deux possibilités d'acquisition séparées par « soit ». Aucune réforme de fond ne vise cette exonération des voyageurs.",
    "Le seuil reste strictement supérieur à 100 €, TVA comprise. Le délai de trois jours calendaires, la même ville et le même numéro de TVA intracommunautaire restent attachés aux achats dans plusieurs magasins ; ces restrictions ne sont pas étendues à l'achat dans un seul magasin. Le renvoi au d du 2° du I de l'article 262 est maintenu, sans déplacer l'unique alinéa.")

add('24 ter', '''
<p>Le bordereau de vente à l'exportation fait preuve de l'exportation lorsqu'il est dûment visé par le service douanier de sortie de l'Union européenne.</p>
''',
    "Réécriture à droit constant : la pièce justificative devient le sujet de la phrase et le visa douanier est énoncé comme condition de sa valeur probante. Aucune réforme de fond ne remplace cette formalité.",
    "Le bordereau, le visa régulier et le service douanier de sortie de l'Union européenne sont conservés. La note relative à l'article 1er de l'arrêté du 16 décembre 2014 est historique ; elle ne crée aucune nouvelle date d'application. Aucun autre mode de preuve n'est ajouté.")

add('24 A', '''
<p>Pour l'application du 9° du II de l'article 262 du code général des impôts, les transports de voyageurs effectués par trains internationaux sont les suivants (1) :</p>
<p>1° Les transports empruntant l'une des sections-frontières du réseau ferré national ci-après :<br />Calais-Fréthun-Fréthun-tunnel ;<br />Tourcoing-Mouscron ;<br />Baisieux-Tournai ;<br />Wannehain-Antoing ;<br />Haumont-Quevy le Petit ;<br />Jeumont-Erquelinnes ;<br />Thionville (Zoufftgen)-Bettembourg ;<br />Forbach-Saarbrücken ;<br />Wissembourg-Winden ;<br />Lauterbourg-Wörth (Berg (Pfaltz)) ;<br />Strasbourg Port du Rhin-Kehl ;<br />Bantzenheim (Chalampé)-Neuenburg (Baden) ;<br />Saint-Louis-Basel ;<br />Delle-Boncourt ;<br />Pontarlier-Les Verrières ;<br />Les Longevilles-Rochejean-Vallorbe ;<br />Longeray Léaz (Fort l'Ecluse)-La Plaine ;<br />Annemasse-Genève Eaux-Vives (Chêne-Bourg) ;<br />Vallorcine-le-Buet-Le Châtelard ;<br />Modane-Bardonecchia ;<br />Breil-sur-Roya-Coni ;<br />Menton-Vintimille ;<br />Cerbère-Port-Bou ;<br />Hendaye-Irùn ;<br />Perpignan-Figueras ;</p>
<p>2° Les transports de groupes en trafic international au départ et à destination de localités desservies par des aérodromes ouverts au trafic des passagers, lorsque l'effectif du groupe correspond au moins à la capacité d'une voiture-lits ou d'une voiture du chemin de fer ;</p>
<p>3° Les transports effectués dans le cadre de la liaison fixe transmanche (1).</p>
<p>(1) Modifications de l'arrêté.</p>
''',
    "Réécriture à droit constant : le champ est formulé directement, les sections-frontières sont présentées sans espacements superflus et le 2° distingue le trajet de la condition d'effectif. Les dénominations géographiques et la mention historique sont conservées. Aucune réforme de fond ne modifie ces exonérations.",
    "Les 25 sections-frontières sont toutes reproduites dans l'ordre de la source, sans modernisation silencieuse de leur dénomination, notamment « Haumont-Quevy le Petit » et « Pfaltz ». Les 1°, 2°, 3° et le renvoi au 9° du II de l'article 262 sont maintenus. Les doubles parenthèses de la source étaient des marques éditoriales autour de l'introduction et du 3° ; les appels (1) et la note « Modifications de l'arrêté » sont conservés, sans leur attribuer une date ou un effet nouveau.")

add('28-00 A', '''
<p>Pour l'application du 3° du 2 du IV de l'article 206 de l'annexe II au code général des impôts, un bien est de très faible valeur si sa valeur unitaire, toutes taxes comprises, n'excède pas 73 € par objet et par an pour un même bénéficiaire.</p>
''',
    "Réécriture à droit constant : la définition de la très faible valeur est exprimée sous la forme d'une condition directement applicable au bien. Aucun changement de fond ni nouveau montant n'est introduit.",
    "Le plafond inclusif de 73 € toutes taxes comprises et ses trois rattachements, par objet, par an et pour un même bénéficiaire, sont maintenus. Le renvoi au 3° du 2 du IV de l'article 206 de l'annexe II est conservé. Comme à l'article 23 N, la note source cite l'arrêté du 12 octobre 2005, article 3, alors que la version prend effet le 12 juin 2021 : la provenance temporelle de ce montant doit être contrôlée sans utiliser la note comme date d'une réforme.")


# Les données du tableau sont reproduites cellule par cellule. Seuls les
# attributs de présentation non autorisés sont retirés.
table_source = next(a for a in sources if a['number'] == '29 A')['source_xml']
table = ET.fromstring('<div>' + table_source + '</div>').find('table')
for element in table.iter():
    element.attrib.clear()
table_xml = ET.tostring(table, encoding='unicode').strip()
add('29 A', '''
<p>Les biens négociés sur un marché à terme international qui peuvent être stockés dans l'entrepôt fiscal visé au d du 2° du I de l'article 277 A du code général des impôts sont ceux figurant dans le tableau suivant :</p>
''' + table_xml,
    "Réécriture à droit constant de la règle d'admission au stockage : la phrase identifie directement les biens autorisés et l'entrepôt concerné. Le tableau, qui constitue une nomenclature technique, est intégralement conservé ; ses données ne sont pas présentées comme réécrites. Les seuls attributs retirés sont ceux de mise en page. Aucune réforme de fond ne modifie cette liste.",
    "Les 35 lignes de biens, les deux colonnes, tous les codes N.C., les mentions « Ex », les intervalles et la restriction « 1006 : uniquement le riz brut » sont conservés, ainsi que les cellules descriptives vides. Le double emploi de la plage 1201 à 1207 pour deux descriptions différentes est une particularité préexistante, non corrigée. Le rattachement au d du 2° du I de l'article 277 A a été vérifié dans le corpus. La note de ce dernier prévoit une abrogation au 1er janvier 2027 avec maintien transitoire de certaines dispositions : coordonner la reprise de cette liste dans le code des impositions sur les biens et services sans inventer ici d'article de remplacement. L'actualité des codes douaniers n'est pas rectifiée sur la seule base de leur ancienneté.")

add('29 B', '''
<p>Les autorités suivantes statuent sur les demandes d'autorisation d'ouverture d'un régime suspensif présentées en application du 2° du I de l'article 277 A du code général des impôts :</p>
<p>1° Le ministre chargé du budget, pour les entrepôts destinés à la fabrication de biens réalisée en commun par des entreprises dont l'une au moins n'a pas d'établissement en France, en exécution d'un contrat international fondé sur le partage de cette fabrication et la propriété indivise des biens produits entre les entreprises contractantes ;</p>
<p>2° Le directeur général des finances publiques, pour les entrepôts de stockage de biens négociés sur un marché à terme international ;</p>
<p>3° Pour le régime fiscal suspensif visé au a du 2° du I de l'article 277 A du code général des impôts :</p>
<p>a) Le service des impôts des entreprises dont relève le demandeur ou le directeur régional des douanes compétent, lorsque les lieux de stockage ou de mise en œuvre du régime se trouvent dans le ressort territorial de sa seule circonscription ;</p>
<p>b) Le service des impôts des entreprises dont relève le demandeur ou le directeur régional des douanes compétent pour le lieu de tenue de la comptabilité-matières ou des registres, lorsque les lieux de stockage ou de mise en œuvre du régime relèvent de plusieurs circonscriptions douanières.</p>
''',
    "Réécriture à droit constant : les autorités de décision deviennent les sujets des 1° et 2°, et les critères de compétence territoriale restent distingués au sein du 3°. Aucune réforme de fond ne modifie les compétences administratives ou les contrats internationaux visés.",
    "Les 1°, 2°, 3°, a) et b) restent à leur place. Le partage de fabrication, l'absence d'établissement en France d'au moins une entreprise et l'indivision demeurent cumulatifs au 1°. Le choix entre service fiscal et directeur des douanes est conservé tel qu'il figure dans la source ; aucun arbitrage de compétence n'est ajouté. Articulation vérifiée avec les a, d et e du 2° du I de l'article 277 A ; sa recodification annoncée au 1er janvier 2027 appelle une coordination de ces compétences, non une substitution de renvois non établis.")

add('29 C', '''
<p>Le registre des stocks et des mouvements de biens prévu au 1° du III de l'article 277 A du code général des impôts doit comporter les mentions suivantes :</p>
<p>a) La désignation du bien ;</p>
<p>b) Sa quantité, exprimée en masse nette, en volume ou en unité ;</p>
<p>c) Les éléments permettant d'identifier et de suivre le bien pendant toute la durée de son placement ;</p>
<p>d) La date d'entrée du bien sous le régime ;</p>
<p>e) L'adresse complète du lieu de provenance du bien ;</p>
<p>f) La date de sortie du bien du régime ;</p>
<p>g) L'adresse complète du lieu de destination du bien à sa sortie du régime ;</p>
<p>h) La fonction utilisée, si l'assujetti ayant obtenu l'ouverture d'un régime fiscal suspensif visé au a du 2° du I de l'article 277 A du code général des impôts a demandé l'application de plusieurs des fonctions visées aux a à e du 1 de l'article 85 E de l'annexe III.</p>
<p>À l'issue de ces opérations, le registre indique, pour chaque bien, les stocks détenus sous le régime suspensif. Le cas échéant, ces stocks sont indiqués par fonction mentionnée sur la déclaration d'ouverture d'un régime visé au a du 2° du I de l'article 277 A du code général des impôts.</p>
<p>Pour les régimes suspensifs visés aux a et e du 2° du I de l'article 277 A du code général des impôts, le registre doit également comporter les indications permettant de suivre et d'identifier les biens qui font l'objet de prestations de services.</p>
''',
    "Réécriture à droit constant : l'obligation de renseignement est explicite, les mentions sont harmonisées et le suivi des stocks par fonction est exprimé en deux phrases. Aucune réforme de fond ne supprime les informations nécessaires à la traçabilité.",
    "Les huit lettres a) à h) et les deux alinéas finaux restent dans l'ordre de la source ; les obligations supplémentaires liées aux services ne sont pas généralisées au régime du d. Renvois vérifiés à l'article 277 A, III, 1°, et à l'article 85 E de l'annexe III, 1, a à e. La note historique du 12 novembre 2010 (décret, article 1er-XI ; arrêté, article 1er-III A) est lue sans création d'une date nouvelle. Prévoir la coordination des renvois lors de la reprise réglementaire du III de l'article 277 A, maintenu transitoirement par les notes du corpus après la recodification de 2027.")

add('29 D', '''
<p>Le registre des opérations réalisées sous l'un des régimes suspensifs, prévu au 1° du III de l'article 277 A du code général des impôts, doit indiquer, pour chaque bien et pour chaque livraison, importation ou acquisition intracommunautaire :</p>
<p>a) La date de l'opération ;</p>
<p>b) Le montant de l'opération et, si ce montant est exprimé en devises, sa contre-valeur en euros ;</p>
<p>c) Le nom et l'adresse complète du fournisseur ainsi que, s'il y a lieu, son numéro d'identification à la TVA ;</p>
<p>d) Le nom et l'adresse complète du client ainsi que, s'il y a lieu, son numéro d'identification à la TVA ;</p>
<p>e) La désignation du bien et sa référence dans le registre visé à l'article 29 C ;</p>
<p>f) La fonction utilisée, si l'assujetti ayant obtenu l'ouverture d'un régime fiscal suspensif visé au a du 2° du I de l'article 277 A du code général des impôts a demandé l'application de plusieurs des fonctions visées aux a à e du 1 de l'article 85 E de l'annexe III.</p>
<p>Pour les prestations de services, le registre doit comporter les mentions prévues aux a, b, c, d et f, ainsi que la nature de l'opération. Il doit également indiquer, s'il y a lieu, la désignation du bien auquel la prestation se rapporte et sa référence dans le registre visé à l'article 29 C.</p>
''',
    "Réécriture à droit constant : le niveau de détail par bien et par opération est explicité, et les mentions relatives aux fournisseurs, aux clients et aux services sont formulées en phrases directes. Aucune réforme de fond ne modifie la tenue de ce registre.",
    "Les a) à f) sont maintenus. Pour les services, le renvoi reste limité aux a, b, c, d et f ; la désignation du bien et la référence au registre 29 C restent conditionnelles. La contre-valeur en euros n'est exigée que pour les montants en devises. Les renvois à l'article 277 A et à l'article 85 E ont été vérifiés dans le corpus ; coordonner leur reprise réglementaire lors de la recodification de 2027. Note historique conservée comme contexte seulement : décret du 12 novembre 2010, article 1er-XI, et arrêté du même jour, article 1er-IV B.")

add('29 E', '''
<p>Les registres visés aux articles 29 C et 29 D doivent être identifiés et tenus sur support papier ou informatique. Les mentions exigées y sont inscrites dans l'ordre chronologique des opérations.</p>
<p>Le contenu originel des informations inscrites doit être conservé.</p>
<p>Les registres doivent être conservés au lieu de situation ou d'utilisation des biens ou des installations indiqué dans la demande d'autorisation d'ouverture du régime suspensif.</p>
<p>Ils sont conservés selon les modalités et dans les délais prévus à l'article L. 102 B du livre des procédures fiscales.</p>
''',
    "Réécriture à droit constant : les obligations d'identification, d'inscription chronologique et de conservation sont formulées directement. Les quatre alinéas et la faculté de choisir un support papier ou informatique sont maintenus. Aucune réforme de fond ne réduit les garanties de conservation.",
    "Les renvois aux articles 29 C et 29 D et à l'article L. 102 B du livre des procédures fiscales sont conservés. Le lieu de conservation reste celui indiqué dans la demande ; aucun délai chiffré non fourni par la source n'est ajouté. La réutilisation des données prévue par policy.json ne dispense pas de leur conservation originelle.")

add('29 F', '''
<p>Les registres visés aux articles 29 C et 29 D doivent être présentés à tout agent de l'administration qui les demande. L'agent peut en obtenir une copie. Si l'assujetti ayant obtenu l'ouverture d'un régime fiscal suspensif visé au a du 2° du I de l'article 277 A du code général des impôts a demandé l'application de plusieurs des fonctions visées aux a à e du 1 de l'article 85 E de l'annexe III, la présentation des registres doit permettre d'identifier et d'isoler chaque fonction utilisée.</p>
<p>Les registres doivent être envoyés par voie dématérialisée à la demande de l'administration.</p>
''',
    "Réécriture à droit constant : le pouvoir de demander présentation et copie est exprimé en phrases distinctes, puis la condition de séparation des fonctions est explicitée. Aucune réforme de fond ne modifie les pouvoirs de contrôle.",
    "Les deux alinéas sont maintenus. La transmission dématérialisée reste subordonnée à une demande de l'administration. Les fonctions a à e du 1 de l'article 85 E de l'annexe III et le régime du a du 2° du I de l'article 277 A ne sont ni étendus ni déplacés. Note historique lue : décret du 12 novembre 2010, article 1er-XI, et arrêté du même jour, article 1er-VI. Coordonner le renvoi législatif à sa reprise lors de la recodification de 2027.")

add('29 G', '''
<p>Si l'assujetti ayant obtenu l'ouverture d'un régime fiscal suspensif visé au a du 2° du I de l'article 277 A du code général des impôts a demandé l'application de plusieurs des fonctions visées aux a à e du 1 de l'article 85 E de l'annexe III au même code, la comptabilité-matières qu'il a été autorisé à tenir en application du 1° du III de l'article 277 A doit retracer séparément les informations relatives aux biens pour chaque fonction utilisée. Cette comptabilité doit être présentée et envoyée par voie dématérialisée à la demande de l'administration.</p>
''',
    "Réécriture à droit constant : la condition de pluralité des fonctions précède clairement l'obligation de suivi distinct, et la règle de communication est formulée directement. Aucune réforme de fond ne transforme la comptabilité-matières autorisée en obligation générale.",
    "L'unique alinéa est conservé, avec les deux conditions tenant au régime autorisé et aux fonctions demandées. Les renvois au a du 2° du I et au 1° du III de l'article 277 A, ainsi qu'aux a à e du 1 de l'article 85 E de l'annexe III, sont maintenus. La note du 12 novembre 2010 (décret, article 1er-XI ; arrêté, article 1er-VII) reste historique. Les notes du corpus prévoient le maintien transitoire du III de l'article 277 A en attente de reprise réglementaire après la recodification de 2027 ; coordonner sans inventer un nouvel article.")

add('30-00 A', '''
<p>Pour l'application du 1 de l'article 279-0 bis du code général des impôts, les gros équipements sont les suivants :</p>
<p>1. Pour les systèmes de chauffage : les équipements collectifs suivants, lorsqu'ils sont situés dans un immeuble comportant plusieurs locaux : chaudière utilisée pour le chauffage ou la production d'eau chaude, cuve à fioul, citerne à gaz et pompe à chaleur ;</p>
<p>2. Les ascenseurs ;</p>
<p>3. Pour les installations sanitaires : les cabines hammam ou sauna prêtes à poser ;</p>
<p>4. Pour les systèmes de climatisation : tous les systèmes de climatisation ainsi que les pompes à chaleur de type air/air.</p>
''',
    "Réécriture à droit constant : chaque numéro est formulé comme une catégorie de gros équipements ; la condition d'immeuble à plusieurs locaux reste attachée aux équipements collectifs de chauffage. Aucune réforme de fond n'étend cette exclusion du taux prévu à l'article 279-0 bis.",
    "Les quatre numéros, les quatre équipements de chauffage et le champ intégral du 4 sont conservés. Le renvoi au 1 de l'article 279-0 bis a été vérifié dans le corpus public. Celui-ci exclut les travaux de rénovation énergétique visés à l'article 278-0 bis A ; ce dernier inclut désormais certaines pompes à chaleur air/air sous conditions. L'articulation avec la mention générale air/air du 4 et les textes techniques d'application doit être contrôlée sans supprimer cette rubrique ni créer une exonération. La recodification de ces articles annoncée pour 2027 appelle une coordination ultérieure.")

add('30-0 A', '''
<p>Les appareillages énumérés ci-après, pris en charge au titre des prestations définies aux articles L. 162-22-6 et L. 162-22-7 du code de la sécurité sociale, sont soumis au taux de 5,5 % de la taxe sur la valeur ajoutée en application du b du 2° du A de l'article 278-0 bis du code général des impôts :</p>
<p>– accès vasculaire implantable composé d'un réservoir sans septum et d'un ou de plusieurs cathéters, quels que soient le nombre de réservoirs et le nombre de cathéters ;</p>
<p>– anneaux valvulaires cardiaques ;</p>
<p>– armature valvulaire cardiaque pour autogreffe ;</p>
<p>– barrières antiadhérences d'origine synthétique ;</p>
<p>– chambre à cathéter implantable à double chambre pour abord veineux ;</p>
<p>– chambre à cathéter implantable monochambre pour abord artériel ;</p>
<p>– chambre à cathéter implantable monochambre pour abord intrarachidien, intrathécal ou péridural ;</p>
<p>– chambre à cathéter implantable monochambre pour abord péritonéal ;</p>
<p>– chambre à cathéter implantable monochambre pour abord veineux ;</p>
<p>– défibrillateurs cardiaques implantables avec stimulation atrio-bi-ventriculaire pour resynchronisation, dits « triple chambre » ;</p>
<p>– défibrillateurs cardiaques implantables à simple et à double chambre ;</p>
<p>– greffon tendineux ;</p>
<p>– greffons cornéens d'origine humaine ;</p>
<p>– greffons valvulaires cardiaques, conduits valvulaires ou fragments valvulaires ;</p>
<p>– implant digestif annulaire anastomotique biodégradable ;</p>
<p>– implant digestif de dérivation péritonéo-veineuse ;</p>
<p>– implant exovasculaire de gainage ;</p>
<p>– implant exovasculaire de ligature interne (CLIP) pour anévrisme cérébral ;</p>
<p>– implant neurologique de drainage sous-dural totalement interne ;</p>
<p>– implant neurologique de ponction de kystes arachnoidiens ;</p>
<p>– implant neurologique de réfection, de suspension ou d'enveloppement, inférieur ou égal à 20 cm<sup>2</sup> ;</p>
<p>– implant neurologique de réfection, de suspension ou d'enveloppement, supérieur à 20 cm<sup>2</sup> ;</p>
<p>– implant neurologique pour valve, connecteur, raccord ou adaptateur ;</p>
<p>– implant neurologique : valve d'hydrocéphalie préréglée pour la régulation de pression ;</p>
<p>– implant neurologique : valve d'hydrocéphalie préréglée pour la régulation de débit ;</p>
<p>– implant neurologique : valve d'hydrocéphalie programmable ;</p>
<p>– implant neurologique : valve d'hydrocéphalie standard et dérivation périphérique ;</p>
<p>– implant neurologique, valve d'hydrocéphalie, cathéter de drainage ;</p>
<p>– implant neurologique, valve d'hydrocéphalie, réservoir ;</p>
<p>– implant ophtalmologique cornéen ou kératoprothèse à support colonisable ;</p>
<p>– implant ophtalmologique de reconstruction orbitaire ;</p>
<p>– implant ophtalmologique intraoculaire de drainage antiglaucomateux ;</p>
<p>– implant ophtalmologique intraoculaire aniridien ;</p>
<p>– implant ophtalmologique intraoculaire : anneau capsulaire ;</p>
<p>– implant ophtalmologique intraorbitaire : bille ;</p>
<p>– implant ophtalmologique intraorbitaire : bille réhabitable ;</p>
<p>– implant ophtalmologique intraorbitaire : bille réhabitable enveloppée ;</p>
<p>– implant ophtalmologique intraorbitaire : entraîneur pour œil artificiel ;</p>
<p>– implant ophtalmologique lacrymal : bouchon ou clou-trou méatique ;</p>
<p>– implant ophtalmologique lacrymal canaliculo-nasal ; implant pour le traitement des larmoiements et implant pour lacorhinostomie ;</p>
<p>– implant ophtalmologique lacrymal : supplément pour traitement hydrophilisant ;</p>
<p>– implant ophtalmologique cristallinien monofocal ;</p>
<p>– implant ophtalmologique cristallinien multifocal ;</p>
<p>– implant ophtalmologique palpébral de suspension pour le traitement du ptosis ;</p>
<p>– implant ophtalmologique palpébral : plaque pour rétraction ;</p>
<p>– implant ophtalmologique palpébral : prothèse pour lagophtalmie ;</p>
<p>– implant ophtalmologique scléral ou vitréen colonisable pour indentation ; implant de type bande, corde, rail et roue pour indentation sclérale ;</p>
<p>– implant ophtalmologique scléral ou vitréen : éponge et bande pour cerclage, pli ; éponge et bande large ;</p>
<p>– implant ophtalmologique scléral ou vitréen : huile de silicone en flacon ou en seringue ;</p>
<p>– implant ophtalmologique scléral ou vitréen non colonisable pour indentation ; implant de type bande, corde, rail et roue pour indentation sclérale ;</p>
<p>– implant ORL pour l'oreille ;</p>
<p>– implant pleuropulmonaire de renfort, d'agrafage, pour résection parenchymateuse ;</p>
<p>– implant pour colposuspension, péri ou uréthrocervical ;</p>
<p>– implant testiculaire ne comportant aucun dérivé ou tissu d'origine biologique ou n'étant pas issu de tels dérivés ;</p>
<p>– implant urétéral à double crosse ;</p>
<p>– implant urétéral à simple crosse ;</p>
<p>– implants cristalliniens monofocaux issus de dérivés de tissus d'origine animale non viables ou en comportant ;</p>
<p>– implants d'expansion cutanée gonflable ne comportant aucun dérivé ou tissu d'origine biologique ou n'étant pas issus de tels dérivés ;</p>
<p>– implants d'origine synthétique pour chirurgie endoscopique, avec ou sans fixation intégrée ;</p>
<p>– implants d'ostéosynthèse divers et supplément : supplément pour traitement ostéoconducteur ; fiche pour fixateur externe ; agrafe, sauf pour main ou pied ; câble de cerclage à fils torsadés ; système d'ancrage tendineux ou ligamentaire, résorbable ou non ; système de fixation de type agrafe à crémaillère pour sternotomie ;</p>
<p>– implants d'ostéosynthèse sur mesure : lame plaque, plaque et clou centromédullaire réalisés sur mesure ;</p>
<p>– implants d'ostéosynthèse de type broche : broche classique ; broche filetée ou cannelée, autosécable ; broche résorbable ; embout de broche antimigration ;</p>
<p>– implants d'ostéosynthèse de type clou plaque : lisse ; adhérent ou à crénage ; adhérent ou à crénage sur la face osseuse ;</p>
<p>– implants d'ostéosynthèse de type clou centromédullaire ;</p>
<p>– implants d'ostéosynthèse pour la chirurgie des extrémités des membres, mains et pieds : plaque à petits fragments ; vis perforée ; vis (cheville) sécable ; agrafe ;</p>
<p>– implants d'ostéosynthèse de type lame plaque ou lame coudée lisse : lisse ; lisse et perforée ; adhérente ou à crénage ; adhérente ou à crénage sur la face osseuse ; adhérente ou à crénage, perforée ; adhérente ou à crénage sur la face osseuse, perforée ;</p>
<p>– implants d'ostéosynthèse de type plaque, sécable ou non : plaque diaphysaire ; plaque épiphysaire ; plaque à cotyle ou basin ; plaque à agrafe ronde, endocéphalique, extrémité supérieure humérus ; plaque-crochet trochantérienne ;</p>
<p>– implants d'ostéosynthèse de type vis et contre-vis : vis corticale et spongieuse, non autotaraudeuse ; vis à pas différents et autocompressive ; vis avec sa contre-vis adaptable sur un trou fileté ; vis perforée ; vis autotaraudeuse ; vis autocompressive ; vis résorbable ; vis adaptable sur un trou fileté d'un implant ;</p>
<p>– implants d'ostéosynthèse de type vis plaque : lisse ; avec système de blocage, lisse ; adhérente ou à crénage ; avec système de blocage, adhérente ou à crénage ;</p>
<p>– implants de drainage pour le traitement du glaucome issus de dérivés de tissus d'origine animale non viables ou en comportant ;</p>
<p>– implants de pontage ne comportant aucun dérivé ou tissu d'origine biologique ou n'étant pas issus de tels dérivés ;</p>
<p>– implants de pontage issus de dérivés, de tissus d'origine animale non viables ou en comportant ;</p>
<p>– implants de réfection de paroi d'origine synthétique, non tricotés et non tissés ;</p>
<p>– implants de réfection de paroi d'origine synthétique, tricotés ou tissés, enduits ou non enduits, non résorbables ;</p>
<p>– implants de réfection de paroi d'origine synthétique, tricotés ou tissés, enduits ou non enduits, résorbables ;</p>
<p>– implants de réfection de paroi issus de dérivés d'origine animale ;</p>
<p>– implants de soutènement sous-urétral ;</p>
<p>– implants de suture et de ligature internes mécaniques, résorbables ou non, pour la chirurgie conventionnelle ou l'endochirurgie : agrafage pour fixation d'implants avec système de pose (chargeur d'agrafes) non restérilisable, rechargeable ou non ; agrafage pour suture et anastomose linéaires ; agrafage pour suture circulaire avec système de pose non restérilisable et non rechargeable ; ligature interne ou clips des vaisseaux ou des conduits excréteurs avec système de pose (chargeur de clips) non restérilisable, rechargeable ou non, avec ou sans section ;</p>
<p>– implants digestifs pour gastroplastie ;</p>
<p>– plaques d'obturation et patchs, résorbables ou non résorbables, quelle que soit leur surface, ne comportant aucun dérivé ou tissu d'origine biologique ou n'étant pas issus de tels dérivés ;</p>
<p>– plaques d'obturation et patchs, résorbables ou non résorbables, quelle que soit leur surface, issus de dérivés, de tissus d'origine animale non viables ou en comportant ;</p>
<p>– produit visco-élastique utilisé en ophtalmologie pour la pose d'implants cristalliniens ne comportant aucun dérivé ou tissu d'origine biologique ou n'étant pas issus de tels dérivés ;</p>
<p>– produits visco-élastiques utilisés en ophtalmologie pour la pose d'implants cristalliniens issus de dérivés de tissus d'origine animale non viables ou en comportant ;</p>
<p>– sources radioactives implantables dites « Grains d'iode 125 » ;</p>
<p>– valves cardiaques à bille, à disque ou à double ailette ;</p>
<p>– valves fabriquées à partir de tissu d'origine animale autre que valvulaire cardiaque, montées ou non sur armature ;</p>
<p>– valves fabriquées à partir de valves cardiaques d'origine animale, montées ou non sur armature.</p>
''',
    "Réécriture à droit constant : la première phrase énonce directement le taux et son double rattachement ; plusieurs rubriques explicitent les relations entre l'implant, ses composants et ses variantes. Les longues énumérations d'ostéosynthèse et d'agrafage sont ponctuées pour distinguer les matériels. La nomenclature médicale, les désignations déjà claires et les restrictions d'origine biologique sont conservées sans prétendre les remplacer par des synonymes. Aucune réforme de fond ne vise ces appareillages.",
    "Les 87 rubriques et leur ordre sont conservés, notamment les deux seuils complémentaires à 20 cm², le taux de 5,5 %, l'iode 125, les exceptions main ou pied, les alternatives de résorbabilité, de colonisabilité et de recharge. La notation source « cathéter (s) » est explicitée par « un ou plusieurs cathéters », sans restriction du nombre de réservoirs ni de cathéters. Les formulations préexistantes « ne comportant aucun […] ou n'étant pas issus […] », « issus de dérivés, de tissus […] », « plaque à cotyle ou basin » et les types de lames coudées qualifiées de lisses puis d'adhérentes sont conservés ; leur cohérence terminologique doit être contrôlée, sans correction silencieuse de champ. La ponctuation de la rubrique d'agrafage sépare la suture circulaire et la ligature interne, que la source relie par une simple virgule ; cette lecture matérielle est à confirmer. Décalage préexistant vérifié dans le corpus : le renvoi source à L. 162-22-6 du CSS ne correspond à aucun article présent dans le corpus actif, tandis que le b du 2° du A de l'article 278-0 bis du CGI vise désormais L. 162-22 et L. 162-22-7. Le renvoi ancien reste apparent dans la proposition ; une coordination explicite de l'arrêté est nécessaire après contrôle du périmètre des prestations, sans substitution silencieuse. Les notes de l'article 278-0 bis annoncent pour 2027 une recodification avec maintien transitoire des a à g du 2° du A jusqu'à leur reprise réglementaire ; coordonner cette liste lors de cette reprise.")

add('30-0 B', '''
<p>Les équipements spéciaux énumérés ci-après relèvent du taux réduit de taxe sur la valeur ajoutée en application du c du 2° du A de l'article 278-0 bis du code général des impôts :</p>
<p>1. Pour les personnes handicapées motrices :</p>
<p>les commandes adaptées au contrôle de l'environnement et à la communication : commandes au souffle, commandes linguales, joysticks, défilement, contacteurs, casques et licornes ;</p>
<p>les appareils de communication à synthèse vocale et les désigneurs ;</p>
<p>les cartes électroniques et les logiciels spécifiques de communication ;</p>
<p>les claviers spéciaux pour ordinateurs et machines à écrire ;</p>
<p>les aides mécaniques ou électriques aux mouvements des bras et les tourne-pages automatiques ;</p>
<p>les matériels de transfert : élévateurs et releveurs hydrauliques ou électriques, lève-personnes ;</p>
<p>les systèmes de douche et de bain intégrant les éléments indispensables à leur accessibilité par des personnes handicapées, à l'exclusion des équipements médicaux ou à finalité thérapeutique ;</p>
<p>les fauteuils roulants et les scooters médicaux dont la vitesse est inférieure ou égale à dix kilomètres par heure ;</p>
<p>les appareils modulaires de verticalisation ;</p>
<p>les appareils de soutien partiel de la tête ;</p>
<p>les casques de protection pour enfants handicapés ;</p>
<p>2. Pour les personnes aveugles et malvoyantes :</p>
<p>les appareils ou objets permettant la lecture, l'écriture ou la reproduction de caractères ou de signes en relief (braille) ;</p>
<p>les téléagrandisseurs et les systèmes optiques télescopiques ;</p>
<p>les cartes électroniques et les logiciels spécialisés ;</p>
<p>les cannes de couleur de type « canne blanche », ainsi que les dispositifs d'assistance électronique ou optronique spécialement conçus pour leur être associés et destinés à faciliter la locomotion, le repérage spatial, la signalisation ou l'insertion dans l'environnement social de la personne déficiente visuelle ;</p>
<p>3. Pour les personnes sourdes et malentendantes :</p>
<p>les vibrateurs tactiles ;</p>
<p>les orthèses vibratoires (amplificateurs de voix) ;</p>
<p>les implants cochléaires ;</p>
<p>les logiciels spécifiques ;</p>
<p>4. Pour les personnes présentant d'autres handicaps :</p>
<p>les filtres respiratoires et les protections trachéales pour laryngectomisés ;</p>
<p>les appareils de photothérapie ;</p>
<p>les appareils de recueil de saignées ;</p>
<p>5. Pour l'ensemble des personnes handicapées, afin de faciliter la conduite des véhicules ou l'accès à ceux-ci :</p>
<p>les sièges orthopédiques (sièges pivotants, surélevés…) ;</p>
<p>les treuils, rampes et autres dispositifs permettant l'accès des personnes handicapées en fauteuil roulant ;</p>
<p>les commandes d'accélérateur à main (cercle, arc de cercle, secteur, manette, poignée tournante…) ;</p>
<p>les sélecteurs de vitesses sur planche de bord ;</p>
<p>les modifications de la position ou de la commande du frein principal ou du frein de secours ;</p>
<p>les modifications de la position ou de la commande des commutateurs de feux, de clignotants, d'avertisseur sonore ou d'essuie-glace ;</p>
<p>les dispositifs de commande groupée (frein principal, accélérateur…) ;</p>
<p>les permutations ou modifications de la position des pédales : pédales d'embrayage et de frein rapprochées ou communes, pédales surélevées, faux planchers ;</p>
<p>les modifications de la colonne de direction ;</p>
<p>les dispositifs de maintien du tronc par sangle ou par harnais ;</p>
<p>les dispositifs d'ancrage des fauteuils roulants à l'intérieur du véhicule ;</p>
<p>6. Pour l'ensemble des personnes en situation de handicap, afin de faciliter la pratique d'une activité sportive :</p>
<p>les appareils et équipements de mobilité adaptés (luges, skis, bateaux de paravoile…) ;</p>
<p>les appareils et équipements fixes de pratique sportive adaptée (banc de musculation, home-trainer, siège de lancer athlétique, selle adaptée pour la pratique de l'équitation…) ;</p>
<p>les matériels de fixation (plaque de lancer, matériel de fixation d'escrime…) ;</p>
<p>les matériels d'assistance et de pratique sportive adaptés aux personnes en situation de handicap moteur (flotteurs latéraux d'aviron, rampes de mise à cheval, massues d'athlétisme, filets de volley-ball assis…) ;</p>
<p>les matériels d'assistance et de pratique sportive adaptés aux personnes ayant une déficience visuelle (sonorisation pour guidage, matériel de cecifoot…).</p>
''',
    "Réécriture à droit constant : la règle de taux est formulée directement, les catégories de bénéficiaires sont nommées comme des personnes et les équipements sont présentés sous une syntaxe homogène. La condition de vitesse des fauteuils et scooters est rattachée directement aux matériels concernés. Aucune réforme de fond ne modifie la liste ni le taux par renvoi.",
    "Les six subdivisions, toutes les rubriques et les exemples non exhaustifs sont maintenus dans l'ordre. La limite reste inférieure ou égale à dix kilomètres par heure, sans extension aux autres équipements. L'exclusion des équipements médicaux ou thérapeutiques concerne toujours les systèmes de douche et de bain. Les conditions de conception et de destination des dispositifs associés aux cannes sont conservées. Le renvoi au c du 2° du A de l'article 278-0 bis n'est pas remplacé par un taux chiffré inventé. La dénomination source « orthèses vibratoires (amplificateurs de voix) » est maintenue sans rectification terminologique implicite.")

add('30-0 C', '''
<p>En application du f du 2° du A de l'article 278-0 bis du code général des impôts, le taux réduit de taxe sur la valeur ajoutée s'applique aux ascenseurs et matériels assimilés suivants, spécialement conçus pour le déplacement d'une personne handicapée :</p>
<p>1. Les appareils élévateurs verticaux installés à demeure, comportant une plate-forme aménagée pour transporter une personne handicapée debout ou en fauteuil roulant, avec ou sans accompagnateur, et répondant aux conditions suivantes :</p>
<p>a) Ils permettent le déplacement entre deux niveaux définis et, le cas échéant, un ou plusieurs niveaux intermédiaires ;</p>
<p>b) Leur vitesse n'excède pas 0,15 mètre par seconde ;</p>
<p>c) Ils sont équipés d'un frein de sécurité ou d'un autre dispositif d'arrêt d'urgence, ainsi que d'un dispositif protégeant l'accès de la gaine à chaque palier ;</p>
<p>d) Leur charge nominale est au moins égale à 200 kilogrammes. Toutefois, pour les appareils élévateurs manuels, elle ne doit pas excéder 200 kilogrammes.</p>
<p>2. Les élévateurs à déplacements inclinés spécialement conçus pour transporter une personne handicapée accompagnée ou non, installés à demeure, se déplaçant le long de guides inclinés, desservant des niveaux définis et circulant ou non le long d'une ou de plusieurs parois ou éléments de parois, qui répondent aux conditions suivantes :</p>
<p>a) Ils circulent le long d'un escalier ou d'un plan incliné ;</p>
<p>b) Ils sont équipés d'un plateau accessible au fauteuil roulant ou d'un siège ;</p>
<p>c) Leur inclinaison par rapport à l'horizontale n'excède pas 45° ;</p>
<p>d) Leur vitesse n'excède pas 0,15 mètre par seconde ;</p>
<p>e) Ils sont équipés d'un frein de sécurité ou d'un autre dispositif d'arrêt d'urgence, ainsi que d'un dispositif de maintien des personnes pendant le fonctionnement de l'appareil ;</p>
<p>f) Leur charge nominale n'excède pas 200 kilogrammes.</p>
''',
    "Réécriture à droit constant : les conditions de conception et d'installation sont formulées directement, et le 1, d) sépare la règle de charge de son exception pour les appareils manuels. La coquille « circulant au non » est explicitement traitée comme « circulant ou non », sans modification de fond recherchée. Aucune réforme de policy.json n'affecte ce régime.",
    "Les 1 et 2, les a) à d) du 1 et les a) à f) du 2 restent à leur place. Les deux plafonds de vitesse de 0,15 m/s et l'inclinaison maximale de 45° sont conservés. La charge est un minimum de 200 kg au 1, sauf appareils manuels pour lesquels 200 kg est un maximum ; au 2, elle reste un maximum de 200 kg. La source comporte « circulant au non » : la lecture « ou non » proposée ici est une correction matérielle signalée, à confirmer, non une coordination silencieuse. La note sur l'article 13-I A et J de la loi du 28 décembre 2011 reste historique ; le renvoi fiscal n'est pas modifié.")

add('30-0 D', '''
<p>Les prestations de rénovation énergétique visées au 3° du I de l'article 278-0 bis A du code général des impôts qui bénéficient du taux réduit de taxe sur la valeur ajoutée prévu au premier alinéa de l'article 278-0 bis du même code sont les suivantes :<br />
<br />1° Les prestations d'isolation thermique :<br />
<br />a) Des parois opaques, dans le respect des prescriptions du II de l'article 30-0 D bis ;<br />
<br />b) Des parois vitrées, dans le respect des prescriptions du III de l'article 30-0 D bis ;<br />
<br />c) Des portes d'entrée donnant sur l'extérieur, dans le respect des prescriptions du IV de l'article 30-0 D bis ;<br />
<br />d) Par l'installation de volets isolants respectant les prescriptions du V de l'article 30-0 D bis ;<br />
<br />e) Par l'installation de protections solaires mobiles respectant les prescriptions du VI de l'article 30-0 D bis ;<br />
<br />2° Les équipements de chauffage et de production d'eau chaude sanitaire utilisant une source d'énergie renouvelable et respectant les prescriptions de l'article 30-0 D ter ;<br />
<br />3° Les systèmes de ventilation mécanique contrôlée double flux, les systèmes de ventilation mécanique simple flux hygroréglable et les systèmes de ventilation hybride hygroréglable, dans le respect des prescriptions de l'article 30-0 D quater ;<br />
<br />4° Le calorifugeage des installations de production ou de distribution de chaleur ou d'eau chaude sanitaire, dans le respect des prescriptions de l'article 30-0 D quinquies ;<br />
<br />5° Les appareils de régulation du chauffage qui permettent le réglage manuel ou automatique et la programmation des équipements de chauffage ou de production d'eau chaude sanitaire, dans le respect des prescriptions de l'article 30-0 D sexies ;<br />
<br />6° Les appareils permettant d'individualiser les frais de chauffage ou d'eau chaude sanitaire dans un bâtiment équipé d'une installation centrale ou alimenté par un réseau de chaleur, dans le respect des prescriptions de l'article 30-0 D septies ;<br />
<br />7° Les brasseurs d'air plafonniers fixes respectant les prescriptions de l'article 30-0 D octies ;<br />
<br />8° Les prestations d'entretien et de réparation des chaudières à très haute performance énergétique, dans le respect des prescriptions de l'article 30-0 D nonies.</p>
<p>Pour les opérations ayant fait l'objet d'un devis daté, accepté par les deux parties et ayant donné lieu à un acompte encaissé avant le 1er janvier 2025, le taux de taxe sur la valeur ajoutée de 5,5 % demeure applicable aux travaux éligibles en application de l'article 30-0 D de l'annexe IV au code général des impôts dans sa rédaction en vigueur au 31 décembre 2024.</p>
''',
    "Réécriture à droit constant : le lien entre chaque prestation et ses prescriptions techniques est formulé directement, en conservant tous les numéros et lettres. La transition normative figurant dans les notes source est reprise intégralement à la fin afin de protéger le traitement des devis anciens. Aucune réforme de fond ni extension des dispositifs de logement proposés dans policy.json n'est introduite.",
    "Les huit catégories et les a) à e) du 1° sont conservés avec chacun de leurs renvois ; aucune catégorie de ventilation n'est omise. La transition reprend les conditions cumulatives de devis daté et accepté par les deux parties, et d'acompte encaissé avant le 1er janvier 2025, le taux de 5,5 % et la rédaction au 31 décembre 2024. Son ajout après le 8° ne déplace aucun alinéa existant. La note d'entrée en vigueur au 1er janvier 2025 de l'arrêté du 4 décembre 2024 reste une donnée historique : elle n'est pas érigée en date d'effet de la présente réécriture ni de toutes les modifications ultérieures de la version fournie. Le corpus de l'article 278-0 bis A contient ses propres exclusions et transitions, notamment pour les chaudières fossiles ; le 8° ne doit pas être interprété comme les écartant. Coordonner aussi la recodification de 2027 annoncée dans ce corpus sans inventer de renvoi de remplacement.")

add('30-0 D bis', '''
<p>I. – Pour l'application du 1° de l'article 30-0 D, un procédé d'isolation thermique associe un matériau isolant à des dispositifs de fixation et de protection. Ces dispositifs, tels que des revêtements, des parements ou, si nécessaire, des membranes continues, assurent la protection du matériau contre les dégradations liées à son exposition aux environnements extérieurs et intérieurs, notamment le rayonnement solaire, le vent, la pluie, la neige, les chocs, l'humidité ou le feu.</p>
<p>Lorsque la protection des matériaux d'isolation thermique contre les transferts d'humidité est nécessaire pour garantir la performance de l'ouvrage, leur pose doit être accompagnée de l'installation d'un pare-vapeur ou de tout autre dispositif permettant d'obtenir un résultat équivalent.</p>
<p>II. – L'isolation thermique des parois opaques visée au a du 1° de l'article 30-0 D doit mettre en œuvre un procédé conforme au I. Ce procédé comporte un ou plusieurs matériaux d'isolation thermique dont la résistance thermique totale (R) est au moins égale à la valeur fixée dans le tableau ci-dessous, exprimée en mètres carrés-kelvin par watt (m<sup>2</sup>.K/W). Cette résistance est évaluée, pour les isolants non-réfléchissants, selon la norme NF EN 12664, NF EN 12667 ou NF EN 12939, ou toute autre méthode équivalente, et, pour les isolants réfléchissants, selon la norme NF EN ISO 22097 ou toute autre méthode équivalente :</p>
<table>
<tbody>
<tr><th>Nature des parois opaques isolées</th><th>Résistance thermique totale R (m<sup>2</sup>.K/W)</th></tr>
<tr><td>Planchers bas sur sous-sol, sur vide sanitaire ou sur passage ouvert</td><td>Supérieure ou égale à 3</td></tr>
<tr><td>Murs donnant sur l'extérieur en façade ou en pignon</td><td>Supérieure ou égale à 3,7</td></tr>
<tr><td>Toitures-terrasses</td><td>Supérieure ou égale à 4,5</td></tr>
<tr><td>Rampants de toiture et plafonds de combles</td><td>Supérieure ou égale à 6</td></tr>
<tr><td>Planchers de combles perdus</td><td>Supérieure ou égale à 7</td></tr>
</tbody>
</table>
<p>La résistance thermique (R) doit être établie conformément aux prescriptions de l'annexe II à l'arrêté du 17 novembre 2020 relatif aux caractéristiques techniques et modalités de réalisation des travaux et prestations dont les dépenses sont éligibles à la prime de transition énergétique. La résistance thermique d'un produit certifié ACERMI ou QB23 est réputée satisfaire à cette exigence.</p>
<p>III. – L'isolation thermique des parois vitrées visée au b du 1° de l'article 30-0 D consiste soit à mettre en place une fenêtre, une fenêtre de toiture ou une porte-fenêtre avec vitrage isolant en remplacement d'une fenêtre, d'une fenêtre de toiture ou d'une porte-fenêtre existante, soit à installer des vitrages de remplacement à isolation renforcée. Les équipements utilisés doivent respecter les exigences suivantes :</p>
<p>1° Les fenêtres ou portes-fenêtres doivent présenter soit un coefficient de transmission thermique inférieur ou égal à 1,3 watt par mètre carré-kelvin et un facteur de transmission solaire supérieur ou égal à 0,3, soit un coefficient de transmission thermique inférieur ou égal à 1,7 watt par mètre carré-kelvin et un facteur de transmission solaire supérieur ou égal à 0,36 ;</p>
<p>2° Les fenêtres de toiture doivent présenter un coefficient de transmission thermique inférieur ou égal à 1,5 watt par mètre carré-kelvin et un facteur de transmission solaire inférieur ou égal à 0,36 ;</p>
<p>3° Les doubles-fenêtres, qui consistent à poser sur une baie existante une seconde fenêtre à double vitrage renforcé, doivent présenter un coefficient de transmission thermique inférieur ou égal à 1,8 watt par mètre carré-kelvin et un facteur de transmission solaire supérieur ou égal à 0,32 ;</p>
<p>4° Les vitrages de remplacement à isolation renforcée, également dénommés vitrages à faible émissivité, installés sur une menuiserie existante, doivent présenter un coefficient de transmission thermique du vitrage inférieur ou égal à 1,1 watt par mètre carré-kelvin.</p>
<p>Le coefficient de transmission thermique est évalué selon la norme NF EN 14351-1 + A2 ou toute autre méthode équivalente. Le facteur de transmission solaire est évalué selon la norme NF P50-777 ou toute autre méthode équivalente. Le coefficient de transmission thermique du vitrage est évalué selon la norme NF EN 1279 ou toute autre méthode équivalente.</p>
<p>IV. – L'isolation thermique des portes d'entrée donnant sur l'extérieur, visée au c du 1° de l'article 30-0 D, doit utiliser des équipements dont le coefficient de transmission thermique est inférieur ou égal à 1,7 watt par mètre carré-kelvin. Ce coefficient est évalué selon la norme NF EN 14351-1 + A2 ou toute autre méthode équivalente.</p>
<p>V. – Les volets isolants visés au d du 1° de l'article 30-0 D doivent être des volets extérieurs dont l'installation apporte, pour l'ensemble volet-lame d'air ventilé, une résistance thermique additionnelle strictement supérieure à 0,22 mètre carré-kelvin par watt.</p>
<p>VI. – Les protections solaires mobiles visées au e du 1° de l'article 30-0 D doivent être extérieures, se déployer dans le plan des baies vitrées et permettre le repliement total du tablier. Leur facteur de transmission de l'énergie solaire totale « gtot », évalué selon la norme NF EN ISO 52022-1 ou toute autre méthode équivalente, doit être inférieur à 0,15 pour un vitrage de type C au sens de la norme NF EN 14501. Cette exigence de facteur de transmission ne s'applique pas lorsque l'occultation permet de protéger la baie de tout rayonnement solaire direct et qu'elle relève de l'une des catégories suivantes : volet battant, jalousie accordéon, persienne coulissante, persienne repliable, volet coulissant.</p>
<p>Si la protection est installée sur une baie verticale, elle doit en outre satisfaire à au moins l'un des trois critères suivants :</p>
<p>a) Sa surface ajourée est supérieure à 30 % de la surface du tablier ;</p>
<p>b) La protection mobile est à projection ;</p>
<p>c) La protection mobile est un volet battant plein équipé d'un système d'entrebâillement.</p>
''',
    "Réécriture à droit constant : les procédés et leurs exigences sont exprimés par des sujets et obligations explicites ; les longues phrases sur les normes, les vitrages et les protections solaires sont scindées. Le tableau est intégralement reproduit. Les seuils inclusifs ou stricts, les méthodes équivalentes et l'exception au facteur solaire restent distincts. Aucune réforme de fond n'abaisse les performances ni ne crée une voie générale d'équivalence supplémentaire.",
    "Les I à VI, les 1° à 4° du III et les a) à c) du VI sont maintenus dans l'ordre, ainsi que l'alinéa de certification placé après le tableau. Contrôle des cinq lignes : R ≥ 3 ; 3,7 ; 4,5 ; 6 ; 7. Les couples de seuils du III restent inchangés, en particulier le facteur solaire ≤ 0,36 des fenêtres de toiture, distinct des minima des autres fenêtres. Le V impose strictement plus de 0,22 ; le VI impose moins de 0,15, sauf occultation répondant aux deux conditions cumulatives ; sur baie verticale un critère supplémentaire reste exigé même en cas d'exception. Tous les identifiants de normes, l'arrêté du 17 novembre 2020, son annexe II et les certifications ACERMI/QB23 sont conservés, notamment la référence source NF EN ISO 22097, sans substitution technique non vérifiée. La date du 1er janvier 2025 portée par la note de l'arrêté du 4 décembre 2024 est historique et ne date pas cette proposition. Le III ne reçoit aucune exigence nouvelle d'identité de nature entre l'équipement existant et son remplacement. L'articulation préexistante entre le remplacement indiqué en tête du III et l'ajout d'une seconde fenêtre au 3° appelle un contrôle, les deux dispositions étant conservées.")


if __name__ == '__main__':
    assert len(sources) == 23
    assert len(drafts) == 23
    assert set(drafts) == {a['number'] for a in sources}
    answer = []
    for source in sources:
        item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
        item.update(drafts[source['number']])
        answer.append(item)
    (ROOT / 'answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
