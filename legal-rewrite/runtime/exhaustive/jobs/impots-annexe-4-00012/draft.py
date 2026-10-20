import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
    }


add('50 duodecies A', '''
<p>1. La liste des matériels agricoles visés au b du 5° du 1 et et 2 du I de l'article 297 du code général des impôts comprend les matériels suivants :</p>
<p>a. Les tracteurs agricoles, y compris les tracteurs-treuils, les voitures automobiles conçues pour le transport exclusif de marchandises et les remorques susceptibles d'être attelées à ces véhicules ;</p>
<p>b. Les matériels à traction animale ou mécanique utilisés pour les usages suivants :</p>
<p>La préparation des surfaces cultivées ;</p>
<p>La fertilisation ;</p>
<p>Les semis et la plantation ;</p>
<p>L'entretien des cultures ;</p>
<p>Les récoltes ;</p>
<p>c. Les matériels destinés au traitement antiparasitaire ;</p>
<p>d. Les matériels mécaniques de manutention et les matériels de conservation des produits agricoles autres que les bâches ;</p>
<p>e. Les matériels d'irrigation, à l'exception des tuyaux d'arrosage en matière souple ;</p>
<p>f. Les matériels nécessaires à l'élevage du bétail, à l'exclusion des fils, piquets et accumulateurs utilisés pour l'électrification des clôtures, ainsi que les matériels nécessaires à l'aviculture et à l'apiculture ;</p>
<p>g. Les matériels servant à préparer les aliments du bétail ;</p>
<p>h. Les matériels de laiterie, de vinification et de cidrerie, ainsi que les matériels servant à élaborer les jus de fruits ;</p>
<p>i. Les moteurs à explosion et à combustion interne, les moteurs électriques de plus de 10 kg et les groupes électrogènes, ainsi que les générateurs à air chaud à usage agricole et les matériels de ventilation ;</p>
<p>j. Les pièces de rechange destinées aux matériels énumérés aux b, c, d, e, f, g et h ;</p>
<p>k. Les roues de rechange des véhicules mentionnés au a.</p>
<p>2. Pour bénéficier du taux prévu au b du 5° du 1 du I de l'article 297 du code général des impôts, les matériels doivent être affectés de manière permanente aux besoins de l'exploitation agricole.</p>
''', "Réécriture à droit constant : la liste est formulée avec des groupes nominaux homogènes et la condition d'affectation permanente est exprimée directement. Les catégories a à k et les usages du b sont conservés. Aucune réforme de fond de policy.json ne vise ce régime corse de TVA.", "Le renvoi du 1 comporte dans la source la séquence incohérente « b du 5° du 1 et et 2 du I » : elle est conservée expressément, sans choisir une portée nouvelle. L'article 297 sans suffixe n'a pas été trouvé dans impots.json du corpus fourni ; la cible doit être contrôlée avant toute correction. Le renvoi distinct du 2 reste intact. Contrôler le seuil strict de plus de 10 kg et les exclusions des d, e et f ; le j ne couvre ni le a ni le i ni le k.")

add('50 duodecies A bis', '''
<p>Les redevables déclarent et liquident la taxe prévue à l'article 300 bis du code général des impôts, qui frappe les exploitants de plateformes de mise en relation par voie électronique en vue de fournir certaines prestations de transport, aux dates suivantes :<br /><br />1° Les redevables de la taxe sur la valeur ajoutée soumis au régime réel normal d'imposition mentionné au 2 de l'article 287 du code général des impôts déclarent et liquident cette taxe en même temps qu'ils déposent la déclaration mentionnée au 1 du même article 287 au titre du mois de mars ou du premier trimestre de l'année suivant celle au cours de laquelle la taxe est devenue exigible ;<br /><br />2° Les redevables de la taxe sur la valeur ajoutée soumis au régime réel simplifié d'imposition prévu à l'article L. 162-1 du code des impositions sur les biens et services déclarent et liquident cette taxe en même temps qu'ils déposent la déclaration annuelle mentionnée au 3 de l'article 287 du code général des impôts au titre de l'exercice au cours duquel la taxe est devenue exigible ;<br /><br />3° Dans tous les autres cas, les redevables déclarent et liquident cette taxe au plus tard le 25 avril de l'année suivant celle au cours de laquelle elle est devenue exigible.</p>
''', "Réécriture à droit constant : chaque catégorie de redevables devient le sujet explicite de l'obligation de déclarer et de liquider. La distinction entre année suivante et exercice d'exigibilité est maintenue, avec les trois branches dans leur ordre. Aucune réforme de fond applicable n'est définie pour cette taxe dans policy.json.", "Conserver les renvois aux 1, 2 et 3 de l'article 287 et à l'article L. 162-1 du CIBS. Échéances maintenues : mars ou premier trimestre de l'année suivante, déclaration annuelle de l'exercice d'exigibilité, et 25 avril de l'année suivante. La note source renvoie aux conditions d'application de l'article 2 de l'arrêté du 3 juin 2022 (NOR : ECOE2210245A) ; cette réserve doit accompagner la mise en application, sans servir de date à une réforme future.")

add('50 terdecies-0', '''
<p>La partie forfaitaire de la taxe sur le chiffre d'affaires des exploitants agricoles, mentionnée au III de l'article 302 bis MB du code général des impôts, s'élève à 90 €.</p>
''', "Réécriture à droit constant : le montant est rattaché directement à la partie forfaitaire de la taxe, sans la construction incidente de la source. Le montant de 90 € demeure identique. Aucune réforme de fond ne vise cette taxe dans policy.json.", "Renvoi au III de l'article 302 bis MB conservé. La note source attribue la modification à l'article 52 de la loi n° 2005-1719 du 31 décembre 2005 ; cette indication historique ne fixe aucune entrée en vigueur nouvelle.")

add('50 terdecies', '''
<p>La redevance sanitaire d'abattage est calculée, pour chaque carcasse abattue, selon les tarifs en euros figurant dans le tableau suivant :</p>
<table><tbody>
<tr><td rowspan="2"><p>Catégorie de carcasse abattue</p></td><td><p>EN EUROS</p></td></tr>
<tr><td><p>Par carcasse abattue</p></td></tr>
<tr><td><p>A. - Ongulés domestiques</p></td><td></td></tr>
<tr><td><p>Bovins adultes</p></td><td><p>5</p></td></tr>
<tr><td><p>Jeunes bovins au sens du point 1 b de l'annexe VI ter du règlement (CE) n° 2074/2005 : bovins de moins de 8 mois, usuellement appelés veaux</p></td><td><p>2</p></td></tr>
<tr><td><p>Solipèdes et équidés</p></td><td><p>3</p></td></tr>
<tr><td><p>Ovins et caprins :</p><p>- poids de carcasse inférieur à 12 kilogrammes</p><p>- poids de carcasse de 12 kilogrammes ou plus</p></td><td><p></p><p>0,15</p><p>0,25</p></td></tr>
<tr><td><p>Porcins :</p><p>- poids de carcasse inférieur à 25 kilogrammes</p><p>- poids de carcasse de 25 kilogrammes ou plus</p></td><td><p></p><p>0,50</p><p>1</p></td></tr>
<tr><td><p>B. - Volailles et lagomorphes</p></td><td></td></tr>
<tr><td><p>Volailles de l'espèce Gallus et pintades</p></td><td><p>0,005</p></td></tr>
<tr><td><p>Canards et oies</p></td><td><p>0,01</p></td></tr>
<tr><td><p>Dindes</p></td><td><p>0,025</p></td></tr>
<tr><td><p>Lapins d'élevage</p></td><td><p>0,005</p></td></tr>
<tr><td><p>C. - Gibier ongulé d'élevage et gibier sauvage</p></td><td></td></tr>
<tr><td><p>Petit gibier à plumes</p></td><td><p>0,005</p></td></tr>
<tr><td><p>Petit gibier à poils</p></td><td><p>0,01</p></td></tr>
<tr><td><p>Ratites : autruche, émeu, nandou</p></td><td><p>0,5</p></td></tr>
<tr><td><p>Sanglier</p></td><td><p>1,5</p></td></tr>
<tr><td><p>Ruminants</p></td><td><p>0,5</p></td></tr>
</tbody></table>
''', "Réécriture à droit constant : l'unité de calcul est explicitée dans la phrase introductive et les libellés du tableau sont allégés. Toutes les catégories, les deux tranches de poids pour les ovins-caprins et les porcins, ainsi que tous les tarifs sont reproduits intégralement. Aucune baisse ni suppression de cette redevance n'est prévue par policy.json.", "Tableau intégral conservé, avec sections A, B et C : tarifs par carcasse, et non par tonne. Vérifier l'appariement 0,15/0,25 avec le seuil de 12 kg et 0,50/1 avec celui de 25 kg ; les valeurs égales aux seuils relèvent de la seconde tranche. Moins de 8 mois et renvoi au point 1 b de l'annexe VI ter du règlement (CE) n° 2074/2005 maintenus. Les montants décimaux et les espèces des trois sections restent ceux de la source.")

add('50 quaterdecies', '''
<p>La redevance sanitaire de découpage est calculée par tonne de viande selon les tarifs en euros figurant dans le tableau suivant :</p>
<table><tbody>
<tr><td rowspan="2"><p>Catégorie de viande</p></td><td><p>EN EUROS</p></td></tr>
<tr><td><p>Par tonne</p></td></tr>
<tr><td><p>Viandes d'ongulés domestiques</p></td><td><p>2</p></td></tr>
<tr><td><p>Viandes de volailles et de lapin d'élevage</p></td><td><p>1,5</p></td></tr>
<tr><td><p>Viandes de gibier d'élevage et sauvage :</p><p>- petit gibier à plumes et petit gibier à poils</p><p>- ratites : autruche, émeu, nandou</p><p>- sanglier et ruminants</p></td><td><p></p><p>1,5</p><p>3</p><p>2</p></td></tr>
</tbody></table>
''', "Réécriture à droit constant : le calcul par tonne de viande est explicite et les libellés du tableau sont simplifiés. Le tableau complet et ses cinq tarifs sont maintenus. Aucune réforme de fond de policy.json ne concerne cette redevance.", "Conserver l'unité par tonne et les cinq associations catégorie/tarif : ongulés domestiques 2 €, volailles et lapin d'élevage 1,5 €, petit gibier à plumes ou à poils 1,5 €, ratites 3 €, sanglier et ruminants 2 €. Les trois sous-catégories de gibier demeurent dans la même ligne du tableau.")

add('50 quaterdecies-0 A', '''
<p>La redevance sanitaire de première mise sur le marché des produits de la pêche et de l'aquaculture est calculée par tonne selon le tarif suivant :</p>
<table><tbody>
<tr><td>Les 50 premières tonnes dans le mois</td><td>1 €</td></tr>
<tr><td>Les tonnes suivantes</td><td>0,50 €</td></tr>
</tbody></table>
<p>Pour les opérations de première vente réalisées dans les halles à marée, la redevance sanitaire est calculée par tonne selon le tarif suivant :</p>
<table><tbody>
<tr><td>Les 50 premières tonnes dans le mois</td><td>0,50 €</td></tr>
<tr><td>Les tonnes suivantes</td><td>0,25 €</td></tr>
</tbody></table>
<p>En cas d'absence ou d'insuffisance de classement ou de calibrage, les opérations de première vente sont soumises au tarif majoré de la redevance sanitaire suivant, par tonne :</p>
<table><tbody>
<tr><td>Les 50 premières tonnes dans le mois</td><td>1 €</td></tr>
<tr><td>Les tonnes suivantes</td><td>0,50 €</td></tr>
</tbody></table>
<p>Pour les poissons des espèces mentionnées au II de l'article 267 quater F de l'annexe II au code général des impôts, le montant perçu ne peut dépasser 50 € par lot.</p>
''', "Réécriture à droit constant : les phrases introductives distinguent la première mise sur le marché, la première vente en halle à marée et le tarif majoré. Le plafond est exprimé comme une limite de perception. Les trois tableaux sont intégralement maintenus ; aucune réforme de fond n'est applicable à ces tarifs au titre de policy.json.", "Maintenir dans chacun des trois tableaux la tranche mensuelle des 50 premières tonnes puis les tonnes suivantes, et les couples de tarifs 1/0,50 €, 0,50/0,25 € et 1/0,50 €. Le tarif majoré suppose l'absence ou l'insuffisance de classement ou de calibrage. Le plafond de 50 € est par lot des espèces visées au II de l'article 267 quater F de l'annexe II, et non un plafond général ou mensuel.")

add('50 quaterdecies-0 A bis', '''
<p>La redevance sanitaire de transformation des produits de la pêche et de l'aquaculture est calculée au tarif de 0,50 € par tonne.</p>
''', "Réécriture à droit constant : la phrase énonce directement la règle de calcul de la redevance, en conservant son objet, son montant et son unité. Aucune réforme de fond de policy.json ne vise ce tarif.", "Le tarif demeure 0,50 € par tonne ; il ne se confond pas avec les tranches de première mise sur le marché ou de première vente prévues à l'article 50 quaterdecies-0 A.")

add('50 quaterdecies-0 A ter', '''
<p>La redevance sanitaire pour le contrôle de certaines substances et de leurs résidus est calculée selon les tarifs suivants :</p>
<table><tbody>
<tr><td>Lait</td><td>0,02 € par mètre cube</td></tr>
<tr><td>Ovoproduits</td><td>0,46 € par tonne d'œufs en coquille</td></tr>
</tbody></table>
''', "Réécriture à droit constant : la phrase introductive présente le calcul de la redevance et les libellés du tableau sont allégés. Le tableau conserve intégralement les deux produits, leurs tarifs et leurs unités. Aucune réforme de fond de policy.json ne vise cette redevance.", "Conserver la différence d'assiette : 0,02 € par mètre cube pour le lait ; 0,46 € par tonne d'œufs en coquille pour les ovoproduits. Ne pas convertir ce dernier tarif en tonne d'ovoproduits.")

add('50-00 A', '''
<p>Pour l'application du a du 1° du I de l'article 286 J de l'annexe II au code général des impôts, les entrepositaires agréés sont dispensés de faire agréer leur comptabilité matières par le directeur régional des douanes et droits indirects lorsqu'ils la constituent au moyen des documents annexés à l'arrêté du 25 août 2000 (JO du 31 août 2000).</p>
<p>Dans ce cas, ils tiennent chaque compte de la comptabilité matières sous forme de colonnes. Au titre des renseignements particuliers prévus au IX de l'article 286 J précité, ces colonnes reprennent les informations mentionnées à l'article 50-00 C.</p>
<p>Pour établir la déclaration récapitulative mensuelle, les comptes font apparaître les lignes suivantes, en plus des informations prévues à l'article 50-00 G :</p>
<p>a) Une ligne « stock début de période » et une ligne « stock fin de période » ;</p>
<p>b) Une ligne « total » ;</p>
<p>c) Une ligne « solde ».</p>
''', "Réécriture à droit constant : les entrepositaires deviennent les sujets explicites de la dispense et de la tenue des comptes. Les informations en colonnes et les quatre lignes exigées pour la déclaration mensuelle sont précisées, avec maintien des a à c. Aucune réforme de fond n'est ajoutée au titre de policy.json.", "Maintenir les modèles de l'arrêté du 25 août 2000, publié le 31 août 2000, et les renvois au a du 1° du I et au IX de l'article 286 J de l'annexe II, ainsi qu'aux articles 50-00 C et 50-00 G. Le corpus local de l'article 286 J, notamment son I, 1°, c et son III, désigne le directeur interrégional pour les agréments, alors que la présente source mentionne le directeur régional : divergence préexistante conservée et à coordonner expressément, sans remplacement silencieux.")

add('50-00 B', '''
<p>I. – Le site d'exploitation mentionné à l'article 286 H de l'annexe II au code général des impôts comprend tout ou partie des chais ou locaux désignés dans les conditions suivantes :</p>
<p>a) Les entrepositaires agréés qui produisent des produits vitivinicoles désignent des chais ou locaux situés dans un même arrondissement ou dans les cantons limitrophes ;</p>
<p>b) Les autres entrepositaires agréés désignent des chais ou locaux situés dans une même commune de moins de 30 000 habitants.</p>
<p>II. – L'entrepositaire agréé indique au service des douanes et droits indirects le lieu où il tient la comptabilité matières, dénommé « siège du site d'exploitation ». Il désigne également tout ou partie des chais ou locaux auxquels cette comptabilité se rapporte.</p>
<p>III. – Le directeur régional des douanes et droits indirects dans la circonscription duquel se trouve le siège du site d'exploitation peut, sur demande des entrepositaires agréés, les autoriser à rattacher au site un ou plusieurs chais ou locaux situés au-delà des limites fixées au I.</p>
''', "Réécriture à droit constant : la définition du site distingue explicitement les deux catégories d'entrepositaires et leurs limites géographiques. La désignation du siège et la faculté d'autorisation sont formulées avec leurs acteurs. Les I à III sont conservés ; aucune réforme de fond de policy.json ne modifie ces limites.", "Seuil strictement inférieur à 30 000 habitants maintenu pour la commune du I, b ; les producteurs vitivinicoles relèvent de l'arrondissement ou des cantons limitrophes. Le rattachement hors limites reste soumis à une demande et à une autorisation facultative du directeur régional du siège. La désignation partielle des chais ou locaux est conservée aux I et II, sans extension générale du site.")

add('50-00 C', '''
<p>Pour l'application des articles 286 I et 286 J de l'annexe II au code général des impôts, les entrepositaires agréés inscrivent dans chaque compte de leur comptabilité matières, selon leur activité, notamment les informations suivantes :</p>
<p>1° La nature, le numéro et la date de départ ou de réception du document d'accompagnement mentionné aux articles 302 M et 302 M ter du code général des impôts ou des pièces justifiant les productions, les transformations, les détentions et les entrées et sorties de produits des chais ou locaux du site d'exploitation ;</p>
<p>2° La date des déclarations prévues aux articles 312, 343 et 416 du même code : mise en production d'alcool ; fabrication de mistelles, de vermouths, de vins de liqueur ou d'apéritifs à base de vin, de cidre ou de poiré ; fabrication de vins mousseux ; fabrication de vins doux naturels ;</p>
<p>3° La date des déclarations de récolte, de stocks et de production prévues à l'article 407 du même code ;</p>
<p>4° La date de prise en charge des produits alcooligènes mentionnés à l'article 338 du même code ;</p>
<p>5° La nature et la date de toute autre opération constituant une « entrée » ou une « sortie » au sens du B du IX de l'article 286 J de l'annexe II au code général des impôts ;</p>
<p>6° La date de la déclaration récapitulative mensuelle mentionnée au IV du même article 286 J ;</p>
<p>7° L'espèce, la qualité et la nature des produits mentionnés au III de l'article 302 G du code général des impôts et, le cas échéant :</p>
<p>a) Les mentions relatives aux comptes d'âge ou de vieillissement ;</p>
<p>b) Pour les transactions soumises à cette procédure, les références des contrats d'achat soumis au visa de l'établissement mentionné à l'article L. 621-1 du code rural et de la pêche maritime ;</p>
<p>c) Les références des déclarations de revendication des produits bénéficiant d'un signe d'origine, prévues par la réglementation en vigueur ;</p>
<p>d) Les numéros d'enregistrement des contrats d'achat et les numéros des déclarations de transactions soumis préalablement aux interprofessions, conformément aux accords interprofessionnels étendus ;</p>
<p>e) L'avis de blocage, l'engagement de garantie ou la mainlevée du porteur de warrant agricole ou du porteur de l'engagement de garantie.</p>
<p>8° La référence aux rhums traditionnels des départements d'outre-mer soumis au tarif prévu au 1° du I de l'article 403 du code général des impôts. Cette référence figure dans une rubrique intitulée « Rhums des DOM, article 403 (I, 1°) », subdivisée, selon le cas, par appellation d'origine ou par dénomination économique ou géographique.</p>
''', "Réécriture à droit constant : l'obligation d'inscription est attribuée explicitement aux entrepositaires et la liste des déclarations du 2° est rendue plus lisible. Le 8° sépare le contenu de l'information de son classement sous la rubrique obligatoire. Les 1° à 8° et les a à e du 7° sont maintenus ; aucune réforme de fond n'est introduite.", "Les informations restent requises selon l'activité et la liste conserve son caractère non exhaustif (« notamment »). Maintenir tous les renvois, en particulier les articles 302 M et 302 M ter, les articles 312, 343, 416, 407, 338 et 302 G du CGI, le B du IX et le IV de l'article 286 J, l'article L. 621-1 du code rural et le 1° du I de l'article 403. Les subdivisions de la rubrique des rhums demeurent alternatives selon le cas. La note historique vise l'article 4-1° de l'ordonnance n° 2015-1247 du 7 octobre 2015 et ne crée aucune transition nouvelle.")

add('50-00 D', '''
<p>Lorsque la comptabilité matières, notamment sous forme de registres vitivinicoles, est tenue selon une procédure informatisée, le système informatique respecte les prescriptions suivantes :</p>
<p>1° Tenue de la comptabilité matières et des registres vitivinicoles.</p>
<p>La comptabilité matières et les registres vitivinicoles informatisés sont tenus selon une ou plusieurs suites chronologiques sans interruption.</p>
<p>Le système informatique comporte un compteur qui enregistre les entrées d'informations dans la comptabilité matières et dans les registres vitivinicoles.</p>
<p>Ce compteur attribue à chaque entrée d'informations un numéro dans une série croissante sans interruption et la date de cette entrée. Le numéro et la date sont reproduits dans la comptabilité matières et dans les registres vitivinicoles.</p>
<p>L'utilisateur ne peut pas accéder à ce compteur. Il lui est interdit de le remettre à zéro.</p>
<p>Dès que l'utilisateur valide la saisie des informations sur la machine émettrice, ces informations ne peuvent plus être annulées ni modifiées.</p>
<p>2° Enregistrement des entrées d'information.</p>
<p>Le système informatique enregistre aussi automatiquement, dans un fichier et par ordre chronologique, chaque entrée d'informations dans la comptabilité matières et dans les registres vitivinicoles, afin d'en conserver la trace.</p>
<p>Le numéro attribué à chaque entrée d'informations par le compteur d'enregistrement, conformément au troisième alinéa du 1°, est le même que celui de l'opération mémorisée par le système.</p>
<p>3° Dispositions en vue de l'exercice des contrôles.</p>
<p>Le système informatique comporte des fonctions d'interrogation en temps réel. Elles permettent aux agents des douanes et droits indirects de visualiser, d'éditer, ou de visualiser et d'éditer à tout moment les informations nécessaires pour vérifier la cohérence entre les deux éléments suivants :</p>
<p>a) Les fichiers informatiques relatifs au traitement mis en œuvre pour l'application du présent article ;</p>
<p>b) L'édition de la comptabilité matières et des registres vitivinicoles.</p>
<p>Lorsque les informations transmises ou reçues comportent des mentions codées, le système permet de les restituer en clair.</p>
<p>4° Sécurités.</p>
<p>Des procédures garantissent l'authenticité de toutes les opérations gérées par le système informatique, dans les conditions prévues par un arrêté du ministre chargé du budget.</p>
<p>5° Conservation des informations.</p>
<p>En cas de changement d'un élément matériel ou logiciel du système informatique, toutes les mesures utiles sont prises pour assurer la conservation et la restitution des informations.</p>
<p>À toute réquisition des agents des douanes et droits indirects, les entrepositaires agréés leur permettent de vérifier, à tout moment, que les systèmes informatiques respectent les prescriptions du présent article et comportent les sécurités qu'elles prévoient.</p>
''', "Réécriture à droit constant : les prescriptions informatiques sont exprimées par des verbes directs, avec distinction du compteur, du fichier de traçabilité, des contrôles, de l'authenticité et de la conservation. Les cinq subdivisions et leurs alinéas sont conservés, y compris le renvoi au troisième alinéa du 1°. Aucune réforme de fond de policy.json ne modifie ces garanties.", "Le troisième alinéa du 1° demeure celui qui attribue le numéro et la date : le renvoi du 2° conserve donc sa cible. Maintenir l'inaccessibilité du compteur, l'interdiction de remise à zéro et l'impossibilité d'annuler ou de modifier après validation. Les fonctions de contrôle conservent la possibilité de visualiser et/ou d'éditer à tout moment ; la restitution en clair et la conservation lors des changements matériels ou logiciels restent obligatoires. La prescription d'authenticité demeure renvoyée à un arrêté du ministre chargé du budget, sans créer un arrêté fictif.")

add('50-00 E', '''
<p>Pour l'application du V de l'article 286 I de l'annexe II au code général des impôts, les registres vitivinicoles qui tiennent lieu de comptabilité matières peuvent prendre la forme d'annotations au verso des déclarations de récolte et de stocks mentionnées à l'article 407 du même code, sous les conditions suivantes :</p>
<p>1° Les annotations comportent les mentions exigées par la réglementation communautaire et les informations mentionnées au 1° du II de l'article 286 I précité ;</p>
<p>2° Les annotations sont lisibles ;</p>
<p>3° Elles retracent la totalité des opérations réalisées par l'entrepositaire agréé.</p>
''', "Réécriture à droit constant : les trois conditions sont énoncées comme des exigences complètes portant explicitement sur les annotations. La faculté d'utiliser le verso des déclarations demeure soumise à ces conditions cumulatives. Aucune réforme de fond de policy.json ne concerne ce dispositif.", "Les renvois au V et au 1° du II de l'article 286 I de l'annexe II, ainsi qu'à l'article 407 du CGI, restent identiques. Maintenir l'exigence de totalité des opérations et les mentions communautaires, sans transformer cette faculté en dispense d'information. La note historique relative à l'article 4-1° de l'ordonnance n° 2015-1247 du 7 octobre 2015 ne fixe pas une entrée en vigueur future.")

add('50-00 F', '''
<p>Pour l'application du VII de l'article 286 I de l'annexe II au code général des impôts, les registres vitivinicoles peuvent être réunis sur un document unique si les conditions suivantes sont remplies :</p>
<p>1° Les opérations réalisées par l'entrepositaire agréé pendant une campagne viticole sont suffisamment limitées pour que chaque type d'opérations puisse être enregistré sur un seul feuillet ;</p>
<p>2° La page de garde du registre indique le nombre de feuillets affecté à chaque type d'opérations.</p>
''', "Réécriture à droit constant : la faculté de regroupement est présentée avec deux conditions lisibles, sans changer le périmètre d'une campagne viticole ni la règle d'un feuillet par type d'opérations. Les 1° et 2° sont maintenus. Aucune réforme de fond applicable n'est prévue par policy.json.", "Renvoi au VII de l'article 286 I de l'annexe II conservé. Le volume limité d'opérations s'apprécie par type sur une campagne viticole, et non globalement sur un feuillet unique ; le nombre de feuillets par type reste indiqué en page de garde.")

add('50-00 G', '''
<p>I. – Pour l'application du III de l'article 286 I et du IV de l'article 286 J de l'annexe II au code général des impôts, l'entrepositaire agréé établit, pour chacun de ses entrepôts fiscaux suspensifs des droits d'accises, une déclaration récapitulative mensuelle distincte.</p>
<p>Lorsqu'aucune opération de production, de transformation, d'entrée ou de sortie de produits n'a été réalisée dans l'entrepôt fiscal suspensif des droits d'accises, l'entrepositaire agréé adresse au service des douanes et droits indirects une déclaration mensuelle portant la mention « Néant ». Il y indique le stock théorique en début de période et le stock théorique en fin de période.</p>
<p>1° Pour chaque compte de la comptabilité matières, la déclaration récapitulative mensuelle comporte les renseignements suivants :</p>
<p>a) Les noms, la dénomination ou la raison sociale, ainsi que l'adresse du siège social ou du principal établissement ;</p>
<p>b) Le numéro d'identification de l'entrepôt fiscal suspensif des droits d'accises ;</p>
<p>c) L'adresse de l'entrepôt fiscal suspensif des droits d'accises auquel se rapporte la déclaration mensuelle ;</p>
<p>d) Le lieu de tenue de la comptabilité matières ;</p>
<p>e) L'année concernée par la déclaration ;</p>
<p>f) Le mois concerné par la déclaration ;</p>
<p>g) La date et le lieu d'établissement de la déclaration, ainsi que la signature du déclarant accompagnée du cachet de son entreprise ;</p>
<p>h) La raison sociale de la caution ou, le cas échéant, la mention « Dispense ».</p>
<p>2° La déclaration récapitulative mensuelle comporte, le cas échéant, les indications suivantes :</p>
<p>a) Les mentions relatives aux comptes d'âge ou de vieillissement ;</p>
<p>b) Pour les transactions soumises à cette procédure, les références des contrats d'achat soumis au visa de l'établissement mentionné à l'article L. 621-1 du code rural et de la pêche maritime ;</p>
<p>c) (Abrogé)</p>
<p>d) Les numéros d'enregistrement des contrats d'achat et les numéros des déclarations de transactions soumis préalablement aux interprofessions, conformément aux accords interprofessionnels étendus ;</p>
<p>e) L'avis de blocage, l'engagement de garantie ou la mainlevée du porteur de warrant agricole ou du porteur de l'engagement de garantie.</p>
<p>3° La déclaration récapitulative mensuelle indique le stock en début de période, le stock en fin de période, le total des entrées et des sorties de produits du mois précédent et le solde, selon les distinctions suivantes :</p>
<p>a) Les entrepositaires agréés qui produisent des alcools, des produits intermédiaires et des produits mentionnés à l'article 438 du code général des impôts présentent ces informations par appellation d'origine ou par dénomination de produits ;</p>
<p>b) Les autres entrepositaires agréés les présentent par nature de produit, par tarif d'imposition ou selon ces deux critères, sous réserve des règlements ou accords interprofessionnels prévus notamment en application des articles L. 632-1 à L. 632-7 du code rural et de la pêche maritime.</p>
<p>II. – 1° Conformément au III de l'article 302 D du code général des impôts, l'entrepositaire agréé liquide l'impôt sur la déclaration récapitulative mensuelle prévue au I.</p>
<p>En plus des renseignements prévus au 1° du I, la déclaration comporte les informations suivantes, nécessaires à la liquidation et au paiement de l'impôt :</p>
<p>a) Le régime fiscal de la déclaration, identifié par la lettre A pour les accises au titre de l'article 302 D précité ou par la lettre D pour la douane en cas d'option pour le régime de l'article 1698 C du même code ;</p>
<p>b) La désignation commerciale des produits imposables, le nombre et le type de récipients, leur volume nominal, le titre alcoométrique volumique (% vol.) et le degré alcoométrique pour les bières ; pour les déclarations d'apposition de capsules ou de marques représentatives de droits indirects, la nature et le nombre de ces capsules ou marques ;</p>
<p>c) Les quantités imposables, réparties par nature de produits ;</p>
<p>d) Les tarifs d'imposition applicables ;</p>
<p>e) Le montant des droits à acquitter, réparti par nature de produits et par tarif d'imposition, ainsi que le montant global de ces droits ;</p>
<p>f) Le moyen de paiement utilisé : numéraire, chèque, virement ou obligation cautionnée ;</p>
<p>2° La déclaration comporte deux cases et une colonne réservées à l'administration. Elles portent les codes taxes, les informations de réception de la déclaration de liquidation, à savoir la date et le numéro, et celles de sa prise en recette : montant, date et numéro de caisse, visa du service des douanes et droits indirects et nature de la garantie dont bénéficie l'entrepositaire agréé.</p>
<p>3° Lorsque l'entrepositaire agréé demande le bénéfice de la compensation au titre de l'article 286 M de l'annexe II au code général des impôts, une sous-rubrique est créée pour chaque catégorie de produit concerné. Y sont inscrits, d'une part, les quantités de produits qui ont déjà supporté l'impôt et qui sont replacées en suspension de droits dans l'entrepôt fiscal suspensif des droits d'accises et, d'autre part, en écriture négative, le montant des droits correspondants.</p>
<p>4° À l'expiration des trois mois suivant le dépôt de la demande, si un crédit d'impôt subsiste faute de compensation, ce crédit est remboursé au bénéficiaire, à sa demande.</p>
<p>III. – Pour l'application du III de l'article 111 H quater de l'annexe III au code général des impôts, l'entrepositaire agréé établit, à l'expiration du délai d'information prévu à l'article 302 P du code général des impôts, un relevé des documents d'accompagnement non apurés mentionnés au I de l'article 302 M et à l'article 302 M ter du même code. Ce document est dénommé « relevé de non-apurement ».</p>
<p>Le relevé de non-apurement respecte le modèle figurant à l'annexe I de l'arrêté du 28 juillet 2011 (JO du 6 août 2011).</p>
<p>L'entrepositaire agréé établit un relevé de non-apurement distinct pour chacun de ses entrepôts fiscaux suspensifs des droits d'accises.</p>
<p>Il le transmet au service des douanes et droits indirects dont il dépend, selon les mêmes modalités et dans les mêmes conditions que la déclaration récapitulative mensuelle.</p>
<p>Lorsqu'un document d'accompagnement non apuré est établi sur papier, un exemplaire de ce document est annexé au relevé de non-apurement.</p>
<p>En plus des renseignements prévus au 1° du I, le relevé de non-apurement comporte les renseignements suivants :</p>
<p>a) Le numéro du document d'accompagnement ;</p>
<p>b) La date de départ du document ;</p>
<p>c) Le nom ou la raison sociale et l'adresse du destinataire ;</p>
<p>d) Le numéro d'identification du destinataire.</p>
<p>Lorsque toutes ses opérations ont été apurées, l'entrepositaire agréé porte la mention « Pas de défaut d'apurement » sur la déclaration récapitulative mensuelle.</p>
''', "Réécriture à droit constant : les obligations de l'entrepositaire sont exprimées directement, les informations de liquidation et les modalités de compensation sont clarifiées, et la procédure de non-apurement est déroulée par acteur. L'intégralité des I à III, de leurs subdivisions, de la mention abrogée et des renseignements est conservée. Aucune réforme de fond n'est ajoutée sur ces accises au titre de policy.json.", "Conserver la déclaration distincte par entrepôt, y compris la déclaration « Néant » avec les deux stocks théoriques, et le c abrogé du 2° du I. Maintenir tous les renvois : annexe II, articles 286 I, 286 J et 286 M ; CGI, articles 438, 302 D, 1698 C, 302 P, 302 M et 302 M ter ; annexe III, article 111 H quater ; code rural, articles L. 621-1 et L. 632-1 à L. 632-7. Le remboursement du II, 4° reste soumis à demande après trois mois suivant le dépôt de la demande de compensation, sans confusion avec un crédit d'impôt nouveau. Conserver les lettres A et D, les deux cases et la colonne administratives, le modèle de l'arrêté du 28 juillet 2011 (JO du 6 août 2011), et l'annexion seulement des documents non apurés établis sur papier.")

add('50-00 H', '''
<p>Les agents de la direction générale de la concurrence, de la consommation et de la répression des fraudes peuvent également mettre en œuvre les dispositions des articles 50-00 C à 50-00 G qui concernent les registres vitivinicoles.</p>
''', "Réécriture à droit constant : la compétence complémentaire des agents est énoncée à la voix active et son champ reste limité aux dispositions relatives aux registres vitivinicoles. Aucune réforme de fond de policy.json ne modifie cette compétence.", "Conserver la portée cumulative du mot « également » et la plage de renvoi 50-00 C à 50-00 G. La compétence n'est pas étendue à toutes les dispositions douanières de ces articles indépendamment des registres vitivinicoles.")

add('50-00 I', '''
<p>I. – Conformément au I de l'article 302 H ter du code général des impôts, le destinataire enregistré établit une déclaration qui comporte les éléments suivants :</p>
<p>a. Au titre des renseignements généraux :</p>
<p>1° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du destinataire enregistré ;</p>
<p>2° Le numéro d'identification attribué au destinataire enregistré par l'administration des douanes et droits indirects lors de son agrément ;</p>
<p>3° L'année et le mois concernés par la déclaration ;</p>
<p>4° La date et le lieu d'établissement de la déclaration, ainsi que la signature du déclarant accompagnée du cachet de son entreprise ;</p>
<p>5° Le nom, la dénomination ou la raison sociale de la caution ou, le cas échéant, la mention « Dispense » ;</p>
<p>6° Le moyen de paiement utilisé : numéraire, chèque, virement ou autre.</p>
<p>Deux cases sont en outre réservées à l'administration dans la déclaration. Elles portent les informations de réception de la déclaration, à savoir la date et le numéro, et celles de sa prise en recette : montant, date, références internes et visa du service des douanes et droits indirects.</p>
<p>b. En cas de réception d'alcool ou de boissons alcooliques, la déclaration comporte, en plus des renseignements prévus au a :</p>
<p>1° La désignation des produits soumis à accise, répartis par catégorie fiscale ;</p>
<p>2° Les quantités imposables de produits par catégorie fiscale, exprimées, selon le cas, en volume d'alcool pur ou en volume effectif et, pour les bières, par degré alcoométrique ;</p>
<p>3° Les tarifs d'imposition applicables ;</p>
<p>4° Le montant des droits d'accise à acquitter, réparti par nature de produit et par tarif d'imposition, ainsi que le montant global de ces droits ;</p>
<p>La déclaration comporte aussi une colonne réservée à l'administration pour les codes taxes. Elle respecte le modèle figurant à l'annexe I de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>c. En cas de réception de tabacs manufacturés, la déclaration comporte, en plus des renseignements prévus au a :</p>
<p>1° Le numéro d'identification attribué au destinataire par l'administration des douanes et droits indirects lors de son agrément en tant que fournisseur agréé ;</p>
<p>2° La désignation des produits soumis à accise, répartis par catégorie fiscale ;</p>
<p>3° Selon le cas, le nombre d'unités de produit ou le nombre de grammes ;</p>
<p>4° Le montant des droits d'accise à acquitter par nature de produit, en distinguant les droits dus au taux normal de ceux dus, le cas échéant, au titre du minimum de perception, ainsi que le montant global de ces droits ;</p>
<p>La déclaration respecte le modèle figurant à l'annexe II de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>II. – Pour l'application de l'article 111 H sexdecies de l'annexe III au code général des impôts, le destinataire enregistré mentionné au I de l'article 302 H ter du même code joint à la déclaration prévue au I un état récapitulatif des livraisons mensuelles effectuées, établi par opérateur. Pour chaque opérateur livré, il indique le nom, la dénomination ou la raison sociale, le numéro d'assujetti à la taxe sur la valeur ajoutée et l'adresse. Il récapitule, pour chacun d'eux, les quantités réceptionnées par nature de produit et par tarif d'imposition. Ces quantités sont exprimées, selon le cas, en volume d'alcool pur ou en volume effectif pour les alcools ou les boissons alcooliques, par degré alcoométrique pour les bières et en nombre d'unités ou en grammes pour les tabacs manufacturés.</p>
<p>III. – Les déclarations et l'état récapitulatif prévus aux I et II, les pièces justificatives nécessaires à leur établissement et à la tenue de la comptabilité des livraisons de produits soumis à accise prévue au I de l'article 302 H ter, ainsi que cette comptabilité elle-même, sont conservés dans les conditions et selon les modalités fixées à l'article L. 102 B du livre des procédures fiscales.</p>
''', "Réécriture à droit constant : les informations communes et celles propres aux alcools et aux tabacs sont distinguées par des phrases plus directes. Le II est découpé en phrases pour rendre lisibles l'identification des opérateurs et les unités de quantité. Les I à III et toutes leurs subdivisions sont conservés ; aucune réforme de fond de policy.json ne vise ces obligations.", "Maintenir les modèles des annexes I et II de l'arrêté du 30 août 2011 (JO du 1er septembre 2011), les renvois aux articles 302 H ter, 302 U bis, 302 V bis, 111 H sexdecies de l'annexe III et L. 102 B du LPF. Deux cases administratives communes, et colonne codes taxes au b, conservées. Le II parle dans la source de livraisons effectuées, d'opérateurs livrés puis de quantités réceptionnées : cette articulation est maintenue et doit être vérifiée sans remplacer silencieusement les réceptions par des livraisons. Les articles 302 H ter, 302 U bis et 302 V bis sont signalés ABROGE_DIFF dans le corpus local ; l'articulation temporelle avec les textes de recodification des accises nécessite un contrôle distinct, sans suppression de ces renvois dans ce brouillon.")

add('50-00 J', '''
<p>I. – Conformément au II de l'article 302 H ter du code général des impôts, le destinataire enregistré qui reçoit à titre occasionnel des produits soumis à accise, en suspension de droits et en provenance d'un autre État membre de l'Union européenne, établit une déclaration avant leur expédition. Cette déclaration comporte notamment les informations suivantes :</p>
<p>1° Le nom, la dénomination ou la raison sociale, le numéro d'assujetti à la taxe sur la valeur ajoutée et l'adresse du destinataire des produits ;</p>
<p>2° Le nom, la dénomination ou la raison sociale, l'adresse et, le cas échéant, le numéro d'accise de l'expéditeur des produits soumis à accise, établi dans un autre État membre de l'Union européenne ;</p>
<p>3° La désignation des marchandises par catégorie fiscale et leur espèce ; pour les alcools et les boissons alcooliques, le titre alcoométrique volumique, le volume effectif et le volume d'alcool pur ; pour les tabacs manufacturés, le nombre d'unités ou de grammes ;</p>
<p>4° La date et le lieu d'établissement de la déclaration, ainsi que la signature du destinataire accompagnée du cachet de son entreprise ;</p>
<p>5° L'adresse et le visa du service des douanes et droits indirects territorialement compétent ;</p>
<p>6° Les références de la consignation effectuée ;</p>
<p>7° La période pendant laquelle l'autorisation est valable ;</p>
<p>8° Le numéro d'identification attribué par l'administration des douanes et droits indirects lors de l'agrément en tant que destinataire enregistré et, le cas échéant, en tant que fournisseur agréé.</p>
<p>Cette déclaration est transmise au service des douanes et droits indirects territorialement compétent. Elle respecte les modèles figurant aux annexes III et IV de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>II. – Le destinataire enregistré à titre occasionnel transmet au service des douanes et droits indirects territorialement compétent une déclaration de réception des produits soumis à accise. Il y indique notamment la date de réception et les quantités reçues, ainsi que les informations requises au I.</p>
<p>La déclaration respecte les modèles figurant aux annexes III et IV de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>III. – Les déclarations prévues aux I et II et les pièces justificatives nécessaires à leur établissement sont conservées dans les conditions et selon les modalités fixées à l'article L. 102 B du livre des procédures fiscales.</p>
''', "Réécriture à droit constant : l'établissement avant expédition et la déclaration de réception sont exprimés par des phrases distinctes. Le 3° regroupe les caractéristiques par famille de produits, sans retrancher d'information. Les I à III, les huit rubriques et le caractère non exhaustif de la liste sont conservés ; aucune réforme de fond de policy.json n'est appliquée à ce régime occasionnel.", "Maintenir le champ des réceptions occasionnelles en suspension de droits depuis un autre État membre, le visa du service compétent, les références de consignation et la période de validité de l'autorisation. Modèles des annexes III et IV de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) maintenus pour les deux déclarations. Les renvois à 302 H ter, 302 U bis et 302 V bis sont conservés malgré leur état ABROGE_DIFF dans le corpus local ; contrôler séparément la transition des recodifications. La conservation reste régie par L. 102 B du LPF, sans délai inventé.")

add('50-0 A', '''
<p>I. – Conformément au I de l'article 302 U bis du code général des impôts, la personne qui livre des produits soumis à accise déjà mis à la consommation dans un autre État membre de l'Union européenne, celle qui les détient ou celle à qui ils sont destinés établit une déclaration avant leur expédition. Cette déclaration comporte notamment les informations suivantes :</p>
<p>1° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du déclarant ;</p>
<p>2° Le nom, la dénomination ou la raison sociale, le numéro d'assujetti à la taxe sur la valeur ajoutée et l'adresse du destinataire des produits, ainsi que, le cas échéant, le numéro d'identification attribué par l'administration des douanes et droits indirects lors de son agrément en tant que fournisseur agréé ;</p>
<p>3° Le nom, la dénomination ou la raison sociale, l'adresse et le numéro d'assujetti à la taxe sur la valeur ajoutée du fournisseur des produits soumis à accise, établi dans un autre État membre de l'Union européenne ;</p>
<p>4° La désignation des marchandises par catégorie fiscale et leur espèce ; pour les alcools et les boissons alcooliques, le titre alcoométrique volumique, le volume effectif et le volume d'alcool pur ; pour les tabacs manufacturés, le nombre d'unités ou de grammes ;</p>
<p>5° La date et le lieu d'établissement de la déclaration, ainsi que la signature du déclarant accompagnée, le cas échéant, du cachet de son entreprise.</p>
<p>Cette déclaration respecte les modèles figurant aux annexes V et VI de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>II. – Le service des douanes et droits indirects établit l'attestation de consignation des droits dus par un opérateur mentionné au I de l'article 302 U bis pour la réception en France de produits déjà mis à la consommation dans un autre État membre de l'Union européenne. Cette attestation respecte les modèles figurant aux annexes V et VI de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>L'attestation comporte notamment les informations suivantes :</p>
<p>1° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du déclarant ;</p>
<p>2° Le nom, la dénomination ou la raison sociale, le numéro d'assujetti à la taxe sur la valeur ajoutée et l'adresse du destinataire des produits, ainsi que, le cas échéant, le numéro d'identification attribué par l'administration des douanes et droits indirects lors de son agrément en tant que fournisseur agréé ;</p>
<p>3° Le nom, la dénomination ou la raison sociale, l'adresse et le numéro d'assujetti à la taxe sur la valeur ajoutée du fournisseur des produits soumis à accise, établi dans un autre État membre de l'Union européenne ;</p>
<p>4° La désignation des marchandises par catégorie fiscale et leur espèce ; pour les alcools et les boissons alcooliques, le titre alcoométrique volumique, le volume effectif et le volume d'alcool pur ; pour les tabacs manufacturés, le nombre d'unités ou de grammes ;</p>
<p>5° L'adresse du service des douanes et droits indirects qui certifie la consignation préalable des droits dus ;</p>
<p>6° La date et les références de la consignation effectuée ;</p>
<p>7° La date et le lieu d'établissement de l'attestation, ainsi que le visa du service des douanes et droits indirects territorialement compétent.</p>
<p>L'attestation est établie en deux exemplaires. L'un d'eux est destiné à l'opérateur mentionné au I de l'article 302 U bis. Cet opérateur l'adresse à l'expéditeur, fournisseur des produits soumis à accise établi dans un autre État membre de l'Union européenne. L'expéditeur joint l'attestation au document qui accompagne les produits.</p>
<p>III. – La personne qui a effectué la déclaration préalable prévue au I transmet au service des douanes et droits indirects territorialement compétent une déclaration de réception des produits soumis à accise. Elle y indique notamment la date de réception et les quantités reçues par le destinataire, ainsi que les informations requises au I.</p>
<p>La déclaration respecte les modèles figurant aux annexes V et VI de l'arrêté du 30 août 2011 (JO du 1er septembre 2011) relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>IV. – Les déclarations et l'attestation prévues aux I à III, ainsi que les pièces justificatives nécessaires à leur établissement, sont conservées dans les conditions et selon les modalités fixées à l'article L. 102 B du livre des procédures fiscales.</p>
''', "Réécriture à droit constant : les auteurs de la déclaration préalable, de l'attestation et de la déclaration de réception sont explicités. Le circuit de l'exemplaire transmis à l'expéditeur est découpé en phrases courtes et les caractéristiques des produits sont présentées par famille. Les I à IV et toutes les informations requises demeurent ; aucune réforme de fond de policy.json ne vise ce régime.", "Ne pas confondre ces produits déjà mis à la consommation avec la suspension de droits de l'article 50-00 J. Maintenir l'établissement avant expédition, les deux exemplaires de l'attestation, sa transmission par l'opérateur à l'expéditeur et sa jonction au document d'accompagnement. Les annexes V et VI de l'arrêté du 30 août 2011 (JO du 1er septembre 2011), le caractère non exhaustif des rubriques, la réserve « le cas échéant » pour le cachet et les renvois au I de 302 U bis et à L. 102 B du LPF sont conservés. Les renvois à 302 H ter, 302 U bis et 302 V bis nécessitent un contrôle temporel avec les textes de recodification : ces articles sont signalés ABROGE_DIFF dans le corpus local, sans que cela justifie une correction silencieuse.")

add('50-0 A bis', '''
<p>I. – Le demandeur qui souhaite obtenir la qualité de représentant fiscal transmet sa demande d'agrément au directeur interrégional des douanes et droits indirects dans la circonscription duquel se trouve le lieu de tenue de sa comptabilité des livraisons.</p>
<p>Il joint à sa demande un modèle de la comptabilité des livraisons et toute pièce justifiant l'existence de la caution prévue à l'article 302 V bis du code général des impôts.</p>
<p>Le directeur interrégional des douanes et droits indirects accorde la qualité de représentant fiscal et attribue à celui-ci un numéro d'identification.</p>
<p>II. – Lorsque le vendeur désigne un représentant fiscal conformément à l'article 302 V bis, un mandat est établi. Ce mandat est exclusif et rédigé en français. Il est signé par une personne habilitée à engager le représentant fiscal et accepté par le vendeur. Il comporte obligatoirement les informations suivantes :</p>
<p>1° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du représentant fiscal ;</p>
<p>2° Le numéro d'identification attribué au représentant fiscal par l'administration des douanes et droits indirects lors de son agrément ;</p>
<p>3° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du vendeur ;</p>
<p>4° La période pendant laquelle le mandat est valable ;</p>
<p>5° L'indication du caractère exclusif du mandat ;</p>
<p>6° Les formalités que le représentant fiscal est habilité à accomplir au nom du vendeur.</p>
<p>Avant toute démarche concernant le vendeur, le représentant fiscal adresse l'original du mandat au service des douanes et droits indirects compétent.</p>
<p>III. – Conformément à l'article 302 V bis du code général des impôts, le représentant fiscal établit une déclaration pour chaque vendeur qu'il représente. Cette déclaration comporte les éléments suivants :</p>
<p>a. Au titre des renseignements généraux :</p>
<p>1° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du représentant fiscal ;</p>
<p>2° Le numéro d'identification attribué au représentant fiscal par l'administration des douanes et droits indirects lors de son agrément ;</p>
<p>3° Le nom, la dénomination ou la raison sociale, ainsi que l'adresse du vendeur ;</p>
<p>4° L'année et le mois concernés par la déclaration ;</p>
<p>5° La date et le lieu d'établissement de la déclaration, ainsi que la signature du déclarant.</p>
<p>La déclaration comporte aussi deux cases réservées à l'administration. Elles portent les informations de réception de la déclaration, à savoir la date et le numéro, et les informations relatives à la liquidation des droits.</p>
<p>b. En plus des renseignements prévus au a, la déclaration comporte :</p>
<p>1° La désignation des produits soumis à accise, répartis par catégorie fiscale ;</p>
<p>2° Les quantités imposables de produits par catégorie fiscale, exprimées, selon le cas, en volume d'alcool pur ou en volume effectif et, pour les bières, par degré alcoométrique ;</p>
<p>3° Les tarifs d'imposition applicables ;</p>
<p>4° Le montant des droits d'accise à acquitter, réparti par nature de produit et par tarif d'imposition, ainsi que le montant global de ces droits ;</p>
<p>La déclaration comporte aussi une colonne réservée à l'administration pour les codes taxes.</p>
<p>Elle respecte le modèle figurant à l'annexe VII de l'arrêté du 30 août 2011 relatif aux déclarations et à l'attestation prévues aux articles 302 H ter, 302 U bis et 302 V bis du code général des impôts concernant les mouvements de produits soumis à accise dans l'Union européenne.</p>
<p>IV. – La déclaration prévue au III, la comptabilité des livraisons de produits soumis à accise prévue à l'article 302 V bis, ainsi que les pièces justificatives nécessaires à leur établissement, sont conservées dans les conditions et selon les modalités fixées à l'article L. 102 B du livre des procédures fiscales.</p>
''', "Réécriture à droit constant : la demande d'agrément, les exigences du mandat exclusif et la déclaration par vendeur sont formulées en identifiant leurs acteurs et en raccourcissant les phrases. Toutes les rubriques des I à IV et leurs subdivisions sont maintenues. Aucune réforme de fond de policy.json ne vise la représentation fiscale de ce régime.", "Compétence du directeur interrégional du lieu de tenue de la comptabilité maintenue. Le mandat reste exclusif, en français, signé par la personne habilitée à engager le représentant fiscal et accepté par le vendeur : cette répartition de signature et d'acceptation, telle que la prévoit la source, n'est pas inversée. Original transmis avant toute démarche ; déclaration distincte par vendeur ; deux cases et une colonne administratives ; modèle de l'annexe VII de l'arrêté du 30 août 2011 et conservation selon L. 102 B du LPF maintenus. La note source vise les articles 1er et 3 de l'arrêté du 20 décembre 2019, sans fixer une date nouvelle. Contrôler l'articulation temporelle des renvois aux articles 302 H ter, 302 U bis et 302 V bis, signalés ABROGE_DIFF dans le corpus local, avec la recodification des accises.")

add('50-0 B', '''
<p>I. – Pour l'application de l'article 285 A de l'annexe II au code général des impôts, le demandeur présente sa demande d'agrément au statut d'acheteur-revendeur à la direction régionale des douanes et droits indirects territorialement compétente. Il utilise un formulaire conforme au modèle établi par l'administration, qui comporte les mentions suivantes :</p>
<p>a La dénomination ou la raison sociale du demandeur ou de son représentant légal ;</p>
<p>b La désignation du siège social du demandeur ;</p>
<p>c La mention de l'autorisation d'exploitation d'un comptoir de vente ;</p>
<p>d L'engagement du demandeur à respecter les obligations dont dépendent l'octroi et le maintien du statut d'acheteur-revendeur, sous peine de retrait de ce statut ;</p>
<p>e La date et la signature du demandeur ;</p>
<p>f La décision par laquelle l'administration accorde le statut d'acheteur-revendeur de tabacs manufacturés, datée et signée ;</p>
<p>g La désignation détaillée et la localisation des lieux de vente, ainsi que leurs modalités d'ouverture et de fonctionnement. Le plan des lieux de vente est annexé au formulaire. Toute modification des plans, de la localisation ou des modalités d'ouverture et de fonctionnement des lieux de vente est signalée à la direction régionale des douanes et droits indirects territorialement compétente.</p>
<p>II. – Le directeur régional des douanes et droits indirects peut retirer l'agrément de l'acheteur-revendeur si celui-ci ne remplit plus les conditions requises, manque à ses obligations ou commet une infraction aux dispositions du code général des impôts. Le retrait ne peut intervenir qu'à l'expiration d'un délai de trente jours à compter de la date figurant sur l'avis de réception du courrier recommandé invitant l'intéressé à présenter ses observations sur le retrait envisagé.</p>
<p>Le titulaire du statut d'acheteur-revendeur peut, à tout moment, mettre fin à son activité en adressant une lettre recommandée avec demande d'avis de réception à la direction régionale des douanes et droits indirects compétente. Cette cessation prend effet huit jours francs à compter de la réception de la lettre par l'administration.</p>
''', "Réécriture à droit constant : l'auteur et le destinataire de la demande sont explicites ; les obligations de signalement du g et la procédure contradictoire de retrait sont réparties en phrases lisibles. Les I et II, les lettres a à g, les trois motifs alternatifs de retrait et les deux délais sont conservés. Aucune réforme de fond de policy.json ne modifie cet agrément.", "Maintenir les trente jours à compter de la date figurant sur l'avis de réception du courrier recommandé invitant aux observations, et les huit jours francs pour la cessation volontaire à compter de la réception de la lettre par l'administration. Aucun retrait automatique n'est instauré. Le corpus local de l'article 285 A de l'annexe II, dans sa version du 7 novembre 2025, vise les comptoirs et boutiques de vente à bord et le statut prévu à L. 3512-14-5 du code de la santé publique, alors que le c de la présente source ne cite que le comptoir : coordination des formulaires à contrôler expressément ; ce brouillon n'étend pas silencieusement les mentions exigées. Le plan annexé et le signalement de toute modification sont conservés.")


if __name__ == '__main__':
    assert len(sources) == len(drafts) == 21
    result = []
    for source in sources:
        draft = drafts[source['number']]
        record = {k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')}
        record.update(draft)
        record['status'] = 'rewrite_draft'
        result.append(record)
    Path('answer.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'answer.json : {len(result)} articles, {sum(len(x["proposed_xml"]) for x in result)} caractères de texte XML proposé')
