import json
from pathlib import Path


drafts = {}


def add(number, xml, reason, review):
    drafts[number] = (xml.strip(), reason, review)


add('11', '''
<p>Lorsque le présentateur déclare encaisser des coupons pour le compte de tiers qu'il désigne, il doit produire, pour chaque bénéficiaire que le payeur ne connaît pas, les justifications prévues à l'article 9. Le payeur établit alors, au nom de chaque bénéficiaire, une pièce de paiement, le relevé prévu à l'article 14 et le certificat de crédit d'impôt. Le cas échéant, il conserve comme justificatif la liste prévue au 2 de l'article 57 de l'annexe II au code général des impôts, remise par le présentateur.</p>
<p>Lorsque les coupons sont présentés par une personne ou une société soumise au 1 de l'article 57 précité et, à ce titre, tenue de déclarer à l'administration les coupons qu'elle paie, ils peuvent faire l'objet d'une pièce distincte de paiement. Cette pièce est établie au nom de la personne ou de la société requérante, comme indiqué ci-dessus, sans production d'une liste annexe. Elle porte la mention « P. C. tiers » (pour le compte de tiers).</p>
''',
    "Réécriture à droit constant des deux modalités de présentation pour compte de tiers : les justificatifs dus pour chaque bénéficiaire inconnu, les documents établis par le payeur et la faculté propre aux présentateurs professionnels sont exprimés dans des phrases distinctes. Aucune réforme de fond n'est appliquée à ce régime documentaire.",
    "Renvois aux articles 9 et 14 et aux 1 et 2 de l'article 57 de l'annexe II conservés ; vérification effectuée dans le corpus pour l'article 9 et l'article 57. La pièce distincte reste facultative et la dispense ne concerne que la liste annexe dans le second alinéa. L'article 9 comporte un renvoi ancien au n° 19 de la liste de l'article 13, désormais subdivisée en I à III : cette incohérence du texte de renvoi appelle une coordination hors du présent article, sans correction implicite ici.")

add('12', '''
<p>Une femme mariée peut produire une pièce d'identité au nom de son mari. Les coupons sont alors considérés comme présentés pour le compte du mari. La pièce de paiement porte la mention « Mme X..., pour compte de M. X... », avec les nom, prénoms ou prénom usuel, et adresse du mari.</p>
<p>La même mention figure sur la pièce de paiement lorsque la femme produit une pièce d'identité personnelle et déclare présenter les coupons pour le compte de son mari.</p>
<p>Lorsque la femme produit une pièce d'identité à son propre nom sans déclarer présenter les coupons pour le compte de son mari, la pièce de paiement doit être établie uniquement à son nom.</p>
''',
    "Réécriture à droit constant des trois hypothèses, en distinguant pour chacune la pièce d'identité produite, la déclaration éventuelle et le nom porté sur la pièce de paiement. Aucune réforme de fond : la règle historique particulière aux femmes mariées est intégralement maintenue.",
    "Les trois alinéas et la formule d'identification du mari sont conservés. La présomption attachée à la pièce d'identité au nom du mari et le traitement différencié selon le sexe sont des particularités préexistantes ; leur éventuelle suppression ou neutralisation exige une décision de fond absente de policy.json.")

add('13', '''
<p>À l'égard du payeur, la production des pièces suivantes établit valablement l'identité des présentateurs et des bénéficiaires de revenus, ainsi que leur domicile ou leur siège social :</p>
<p>I. – Personnes physiques</p>
<p>1° Carte nationale d'identité ou carte d'identité officielle délivrée par un État autre que la France, accompagnée, si nécessaire, de tout document probant comportant l'adresse ou le numéro d'identification fiscale ;</p>
<p>2° Carte photographique d'identité en cours de validité, délivrée aux membres de familles nombreuses pour les voyages en chemin de fer ;</p>
<p>3° Carte photographique d'abonnement aux chemins de fer, en cours de validité ;</p>
<p>4° Permis de chasse ;</p>
<p>5° Livret d'identité à coupons pour le paiement des pensions et retraites civiles et militaires de l'État, portant la photographie du bénéficiaire ;</p>
<p>6° Carte d'identité professionnelle à l'usage des voyageurs de commerce ;</p>
<p>7° Carte photographique d'invalidité en cours de validité, délivrée par les comités départementaux des mutilés et réformés de guerre ;</p>
<p>8° Carte d'identité délivrée par les préfectures aux grands mutilés pour les voyages à tarif réduit ;</p>
<p>9° Carte photographique de priorité dans les voitures de transport en commun, en cours de validité, délivrée aux mutilés de guerre par la préfecture ;</p>
<p>10° Carte photographique d'identité des officiers de l'armée active ;</p>
<p>11° Livret de solde pour officier marinier et marin ;</p>
<p>12° Livret professionnel maritime ;</p>
<p>13° Passeport français en cours de validité ou périmé depuis moins de cinq ans ;</p>
<p>14° Passeport étranger en cours de validité, accompagné, si nécessaire, de tout document probant comportant l'adresse ou le numéro d'identification fiscale ;</p>
<p>15° Carte photographique d'identité en cours de validité, instituée pour tous les étrangers résidant en France.</p>
<p>II. – Personnes morales ou organismes sans personnalité morale</p>
<p>1° Exemplaire des statuts ou tous documents constitutifs certifiés par le représentant légal de la société ou de l'organisme ;</p>
<p>2° Pour les associations, récépissé de la déclaration à la préfecture ou à la sous-préfecture ;</p>
<p>3° Récépissé de la déclaration d'existence prévue à l'article 23 A ou de la déclaration modificative prévue à l'article 23 B.</p>
<p>III. – Personnes physiques ou morales ou organismes sans personnalité morale</p>
<p>Attestation délivrée par le service des impôts ou par l'autorité administrative compétente du lieu de résidence fiscale. Cette attestation mentionne le domicile ou le siège social et le lieu d'imposition de la personne qu'elle désigne.</p>
''',
    "Réécriture à droit constant de la règle de preuve et de la présentation des justificatifs : la validité des pièces et les compléments éventuels sont formulés plus directement, sans modifier les trois catégories ni les dix-huit entrées numérotées. La liste des titres historiques est maintenue ; aucune réforme de fond ne la remplace par un dispositif nouveau.",
    "Conservation de la tolérance de moins de cinq ans pour le seul passeport français périmé, des compléments d'adresse ou d'identification fiscale aux I, 1° et 14°, et des renvois aux articles 23 A et 23 B. La note source fixe l'application à l'identification des présentateurs et bénéficiaires de revenus de capitaux mobiliers au 1er janvier 2004, en application du II de l'article 24 de la loi de finances rectificative pour 2003 ; elle ne date aucune réforme future. L'article 9 du même corpus vise encore un n° 19 de cette liste alors que l'attestation figure au III : incohérence de numérotation à coordonner dans l'article 9, non assigné. Aucun titre ancien n'a été écarté pour obsolescence supposée.")

add('13 bis', '''
<p>Les établissements payeurs mentionnés aux articles 75 et 76 de l'annexe II au code général des impôts sont également soumis aux dispositions des articles 8 à 13.</p>
''',
    "Réécriture à droit constant avec les établissements payeurs comme sujet explicite de l'assujettissement. Le champ de l'extension et les deux séries de renvois sont conservés ; aucune réforme de fond n'est introduite.",
    "Les articles 8 à 13 restent visés dans leur ensemble, sans extension à l'article 13 bis lui-même. Les établissements restent définis par les articles 75 et 76 de l'annexe II ; aucun raccordement au nouveau compte de retraite n'est créé.")

add('14', '''
<p>Les relevés transmis à la direction départementale ou, le cas échéant, régionale des finances publiques en application de l'article 57 de l'annexe II au code général des impôts portent sur :</p>
<p>1° Les coupons, les instruments représentatifs de coupons et les arrérages payés en espèces sur présentation aux guichets des caisses publiques ou des personnes ou sociétés mentionnées à l'article 57-1 de l'annexe II au code général des impôts ;</p>
<p>2° Les sommes inscrites à un compte de passage sur remise, aux guichets, de coupons et d'instruments représentatifs de coupons, ou sur présentation des titres ;</p>
<p>3° Les coupons et arrérages que les sociétés paient par correspondance aux porteurs de leurs propres titres, notamment par chèque ordinaire, chèque postal ou mandat-poste.</p>
<p>Pour les chèques-dividendes émis par une société dont le siège est situé en France métropolitaine, la société émettrice fournit les relevés.</p>
<p>Pour les chèques-dividendes émis par une société dont le siège est situé hors de France métropolitaine, l'établissement qui en assure le paiement fournit les relevés.</p>
''',
    "Réécriture à droit constant des trois catégories d'opérations déclarées et des deux règles désignant l'auteur des relevés de chèques-dividendes. La ponctuation des listes et les sujets des obligations sont explicités, sans modification de fond.",
    "Les trois numéros et les deux alinéas territoriaux restent dans le même ordre. Renvois à l'article 57 et à l'article 57-1 de l'annexe II conservés ; le second désigne le 1 de l'article 57, lu dans le corpus. La distinction porte sur la France métropolitaine, et non sur la France entière. La note source est une coordination liée à l'article 2 du décret n° 2012-430 du 29 mars 2012.")

add('16', '''
<p>Les relevés prévus à l'article 14 pour les paiements effectués au cours d'un mois sont transmis à la direction départementale ou, le cas échéant, régionale des finances publiques dans les dix premiers jours du mois suivant. Ils sont accompagnés d'un bordereau indiquant la désignation et l'adresse de l'établissement payeur, le mois concerné et le nombre de relevés. La direction en accuse réception.</p>
''',
    "Réécriture à droit constant en trois phrases distinguant le délai d'envoi, les mentions du bordereau et l'accusé de réception. Le délai mensuel et le contenu exigé demeurent identiques ; aucune réforme de fond n'est introduite.",
    "Délai conservé : les dix premiers jours du mois suivant celui des paiements. Les quatre informations du bordereau et le renvoi à l'article 14 sont maintenus. La note source rattache la désignation des directions à l'article 2 du décret n° 2012-430 du 29 mars 2012 ; aucune nouvelle date d'entrée en vigueur n'en est déduite.")

add('17', '''
<p>Les payeurs doivent organiser leurs écritures de manière à permettre à l'administration de vérifier l'exactitude des mentions figurant sur les relevés qu'ils fournissent. Ils conservent les pièces, livres et documents selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales, sauf lorsqu'une disposition légale impose une durée de conservation plus longue.</p>
''',
    "Réécriture à droit constant de l'obligation d'organiser les écritures et de conserver les justificatifs, avec une réserve finale explicite pour les durées légales plus longues. Aucune durée autonome ni réforme de fond n'est créée.",
    "Renvoi au I de l'article L. 102 B du livre des procédures fiscales et priorité des durées légales plus étendues conservés. Aucun nombre d'années n'est substitué au renvoi, afin de préserver la coordination avec ce livre hors du lot.")

add('17 A', '''
<p>1. Pour toute opération portant sur des coupons ou instruments représentatifs de coupons d'actions et de parts sociales de sociétés françaises et faisant l'objet du relevé prévu à l'article 57 de l'annexe II au code général des impôts, un document doit être établi. Il indique l'identité et le domicile réel ou le siège social du bénéficiaire, ainsi que la pièce éventuellement présentée pour les justifier. Il précise également les valeurs mobilières dont proviennent les revenus payés et le décompte des sommes mises en paiement, en indiquant, le cas échéant, la retenue opérée au profit du Trésor.</p>
<p>2. (Devenu sans objet).</p>
<p>3. Les pièces établies sont réparties en deux liasses : l'une regroupe les paiements aux personnes dont le domicile réel ou le siège social est situé en France ; l'autre regroupe les paiements aux personnes domiciliées ou ayant leur siège hors de France.</p>
<p>4. Ces liasses et l'état prévu à l'article 188 H sont conservés à la disposition de l'administration selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales.</p>
''',
    "Réécriture à droit constant de l'établissement du document, de ses mentions et du classement territorial des pièces. La phrase du 1 est scindée et les deux liasses sont définies directement. Les quatre subdivisions, y compris le 2 devenu sans objet, sont maintenues ; aucune réforme de fond.",
    "Renvois à l'article 57 de l'annexe II, à l'article 188 H et au I de l'article L. 102 B du livre des procédures fiscales conservés. Les mentions éventuelles du justificatif et de la retenue restent conditionnelles. Le 2 n'est ni renuméroté ni supprimé. Le renvoi au « I de l'article 17 A » contenu dans l'article 17 B ne correspond pas à la numérotation arabe « 1. » de la présente source ; anomalie signalée sans correction implicite.")

add('17 B', '''
<p>1. Les personnes et organismes mentionnés à l'article 41 duodecies A de l'annexe III au code général des impôts doivent établir les documents prévus au I de l'article 17 A lorsqu'ils paient des intérêts, arrérages et autres produits de fonds d'État, d'obligations françaises et d'autres valeurs assimilées.</p>
<p>Ces documents indiquent le prélèvement prévu à l'article 125 A du code général des impôts à la place de la retenue à la source prévue au 2 de l'article 119 bis du même code.</p>
<p>2. Les documents mentionnés au 1 qui constatent, au profit de personnes domiciliées ou ayant leur siège social hors de France, le paiement de revenus ayant supporté le prélèvement ne doivent pas mentionner simultanément des revenus ayant donné lieu à la retenue à la source.</p>
<p>3. Les pièces établies en application de l'article 17 A et du présent article sont réparties en deux liasses : l'une regroupe les paiements aux personnes dont le domicile réel ou le siège social est situé en France ; l'autre regroupe les paiements aux personnes domiciliées ou ayant leur siège hors de France.</p>
<p>Les documents sont regroupés séparément :</p>
<p>dans la première liasse, selon qu'ils mentionnent ou non des revenus ayant supporté le prélèvement ;</p>
<p>dans la seconde liasse, selon que les paiements ont été assujettis à la retenue à la source ou au prélèvement. Les relevés individuels mentionnant à la fois des revenus ayant donné lieu à la retenue à la source et des revenus ayant donné lieu au prélèvement font l'objet d'un classement spécial au sein de cette liasse.</p>
''',
    "Réécriture à droit constant avec l'obligation documentaire en proposition principale et des règles de classement formulées directement. Les trois subdivisions, la substitution de la mention du prélèvement à celle de la retenue et tous les cas de classement restent présents. Aucune réforme de fond ni nouveau taux de prélèvement.",
    "Renvois aux articles 41 duodecies A de l'annexe III, 125 A et 119 bis, 2, du CGI maintenus ; l'article 41 duodecies A a été lu dans le corpus. Deux difficultés préexistantes sont conservées et signalées : le renvoi au I de l'article 17 A alors que celui-ci comporte un « 1. » ; l'interdiction de documents mixtes au 2 pour les non-résidents, tandis que la dernière phrase du 3 prévoit le classement spécial de relevés mixtes dans la seconde liasse. Leur articulation doit être contrôlée sans supprimer l'une des règles. La baisse de CSG salariale ne concerne pas ces produits de capitaux.")

add('17 C', '''
<p>Pour chaque versement d'intérêts, d'arrérages ou de produits de toute nature de bons et autres titres de créances, de dépôts, de cautionnements ou de comptes courants, les personnes et organismes mentionnés à l'article 17 B doivent établir une pièce de paiement. Ils y indiquent :</p>
<p>le montant et la date des sommes payées ;</p>
<p>l'identité et le domicile du débiteur, lorsque celui-ci n'est pas l'établissement payeur ;</p>
<p>le montant du prélèvement opéré ou, à défaut, l'identité et le domicile réel ou le siège social du bénéficiaire des revenus, ainsi que la pièce éventuellement présentée pour les justifier.</p>
''',
    "Réécriture à droit constant en plaçant d'abord le fait générateur de l'obligation documentaire : chaque versement. Les trois groupes de mentions sont conservés, avec la condition propre au débiteur et l'alternative liée au prélèvement. Aucune réforme de fond.",
    "Le renvoi à l'article 17 B, tous les produits énumérés et l'alternative du dernier alinéa sont maintenus. L'identification du débiteur demeure exigée seulement lorsqu'il diffère de l'établissement payeur ; aucun cumul systématique n'est imposé entre le montant du prélèvement et les mentions prévues à défaut.")

add('17 C bis', '''
<p>Lorsque les personnes mentionnées au II de l'article 117 quater du code général des impôts paient des revenus sur lesquels est opéré le prélèvement forfaitaire prévu au I du même article, elles doivent fournir à l'administration, à sa demande, les documents justifiant le paiement de ces revenus et le prélèvement opéré.</p>
''',
    "Réécriture à droit constant sous la forme d'une condition suivie de l'obligation de fournir les justificatifs. Le champ des personnes, le prélèvement concerné et le déclenchement sur demande de l'administration sont inchangés ; aucune réforme de fond.",
    "Distinction conservée entre le II de l'article 117 quater pour les personnes et le I pour le prélèvement. La note source se rapporte à l'article 9-I B de la loi n° 2012-1509 du 29 décembre 2012. Aucun régime de CSG salariale ou de retraite n'est transposé à ces revenus.")

add('17 D', '''
<p>Les documents, états et pièces tenus ou établis en application des articles 17 B, 17 C et 17 C bis doivent rester à la disposition de l'administration. Leur conservation s'effectue selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales.</p>
''',
    "Réécriture à droit constant en séparant l'obligation de mise à disposition et les modalités de conservation. Les trois catégories de supports et tous les renvois sont maintenus ; aucune réforme de fond.",
    "Renvois aux articles 17 B, 17 C, 17 C bis et au I de l'article L. 102 B du livre des procédures fiscales conservés. La note source rattache les modifications à l'article 1er, 5° et 8°, de l'arrêté du 28 août 2018 sur le transfert des obligations déclaratives et de paiement en matière de prélèvement et de retenue à la source sur les revenus de capitaux mobiliers ; elle ne fixe aucune échéance nouvelle.")

add('17 D bis', '''
<p>Pour l'application du 7° du II de l'article 150 U du code général des impôts et du 1° du A du I de l'article 150 VE du même code, sous réserve du VI de ce dernier article, sont considérées comme présentant un déséquilibre important entre l'offre et la demande de logements les communes classées dans les zones A bis, A et B1. Ces zones sont définies par l'arrêté prévu au premier alinéa de l'article D. 304-1 du code de la construction et de l'habitation.</p>
''',
    "Réécriture à droit constant de la définition des communes, avec une phrase distincte pour le texte de zonage et un antécédent explicite pour la réserve du VI. Les trois zones et le champ des deux dispositifs de plus-values sont maintenus ; aucune réforme de fond.",
    "Renvois au 7° du II de l'article 150 U, au 1° du A du I et au VI de l'article 150 VE conservés. Le VI de l'article 150 VE, lu dans le corpus, exclut de son 1° du A du I les cessions de terrains, biens ou droits situés en Corse : la réserve reste attachée à ce dispositif. L'article D. 304-1 a également été lu : il renvoie à un arrêté et inclut A bis dans A. L'énumération expresse A bis, A et B1 est néanmoins conservée telle qu'assignée, sans alignement sur les zonages distincts des articles 18-0 bis B et 18-0 bis C.")

add('17 E', '''
<p>I. – Les assureurs doivent délivrer chaque année un certificat aux souscripteurs des contrats ou avenants d'augmentation d'assurance en cas de vie ou en cas de décès souscrits auprès d'eux, lorsque les primes de ces contrats ou avenants peuvent ouvrir droit à la réduction d'impôt prévue à l'article 199 septies du code général des impôts. Ce certificat permet aux souscripteurs de bénéficier de cette réduction ;</p>
<p>II. – Le certificat prévu au I est établi selon un modèle publié par l'administration et comporte les indications suivantes :</p>
<p>– la désignation de l'assureur ;</p>
<p>– les nom, prénoms et adresse du souscripteur ;</p>
<p>– le numéro du contrat ;</p>
<p>– la date d'effet et la durée du contrat ou de l'avenant ;</p>
<p>– le montant des primes venues à échéance au cours de l'année civile.</p>
<p>Il précise également :</p>
<p>1. Pour les contrats ou avenants mentionnés au 1° de l'article 199 septies précité :</p>
<p>a) La nature du contrat : contrat à « primes périodiques », à « prime unique » ou « à versements libres » ;</p>
<p>b) Le montant des primes représentatif de l'opération d'épargne, en distinguant :</p>
<p>1° Le montant des primes payées au titre de contrats à primes périodiques conclus ou prorogés avant le 20 septembre 1995 ;</p>
<p>2° Le montant des primes payées au titre de contrats à primes périodiques conclus ou prorogés du 20 septembre 1995 au 31 décembre 1995 ;</p>
<p>3° Le montant des primes payées au titre de contrats à primes périodiques conclus ou prorogés du 1er janvier 1996 au 4 septembre 1996.</p>
<p>2. Pour les contrats ou avenants prévus au 2° de l'article 199 septies, les nom et prénoms du bénéficiaire du capital ou de la rente viagère ;</p>
<p>III. – Lorsque les contrats d'assurance en cas de décès mentionnés au 2° de l'article 199 septies sont souscrits sous la forme de contrats collectifs, l'organisme souscripteur délivre à ses adhérents le certificat décrit au II.</p>
<p>IV. – Pour bénéficier de la réduction d'impôt sur le revenu, le contribuable doit pouvoir présenter le certificat décrit au II à la demande de l'administration.</p>
''',
    "Réécriture à droit constant de l'obligation annuelle des assureurs, du contenu du certificat et de sa présentation à l'administration. Les subdivisions I à IV, les sous-listes et toutes les périodes historiques des contrats sont maintenues. Aucune réforme de fond : les contrats d'assurance ne sont pas assimilés au nouveau compte de capitalisation collective.",
    "Dates préservées : avant le 20 septembre 1995 ; du 20 septembre au 31 décembre 1995 ; du 1er janvier au 4 septembre 1996. Le montant des primes venues à échéance reste distinct des montants de primes payées dans les sous-listes. Incohérence préexistante vérifiée dans l'article 199 septies du corpus : son I, 1° vise l'assurance décès au profit de bénéficiaires handicapés et son I, 2° l'assurance en cas de vie ou la rente différée pour l'assuré handicapé ; le présent article rattache pourtant des données d'épargne anciennes au 1° et qualifie de décès les contrats du 2° au III. Renvois et mentions maintenus pour ne pas réaffecter silencieusement les régimes ; coordination historique de l'article 17 E avec l'article 199 septies nécessaire.")

add('17 ter', '''
<p>Pour être réputé ouvert à la visite au sens de l'article 41 I de l'annexe III au code général des impôts, un immeuble doit être ouvert aux visites du public au moins :</p>
<p>Soit cinquante jours par an, dont vingt-cinq jours non ouvrables, entre les mois d'avril et de septembre inclus ;</p>
<p>Soit quarante jours au cours des mois de juillet, août et septembre.</p>
<p>La durée minimale prévue aux deuxième et troisième alinéas peut être réduite lorsqu'une ou plusieurs conventions organisent des visites de l'immeuble par des groupes d'élèves de l'enseignement primaire ou secondaire, des groupes d'enfants mineurs encadrés par des structures d'accueil collectif à caractère éducatif mentionnées à l'article L. 227-4 du code de l'action sociale et des familles ou des groupes d'étudiants de l'enseignement supérieur. Ces conventions sont conclues entre le propriétaire et les établissements d'enseignement publics ou privés sous contrat d'association avec l'État, ou les structures précitées. La réduction correspond au nombre de jours pendant lesquels l'immeuble accueille ces visites entre le 1er septembre de l'année précédente et le 31 août suivant, dans la limite de dix jours par année civile. Chaque visite doit comprendre au moins vingt participants.</p>
''',
    "Réécriture à droit constant des deux durées alternatives et du mécanisme de réduction pour les visites de groupes. Le dernier alinéa est décomposé en phrases distinguant les publics, les cocontractants, le calcul et la condition d'effectif, sans déplacement de l'alinéa. Aucune réforme de fond.",
    "Quatre alinéas conservés, notamment les deuxième et troisième visés par le dernier. Seuils conservés : cinquante jours dont vingt-cinq non ouvrables d'avril à septembre inclus, ou quarante jours de juillet à septembre ; réduction plafonnée à dix jours par année civile ; au moins vingt participants par visite. Période de comptage maintenue du 1er septembre précédent au 31 août suivant. Renvois à l'article 41 I de l'annexe III et à l'article L. 227-4 du CASF conservés ; articulation de l'article 41 I avec l'article 41 F vérifiée dans le corpus.")

add('17 quater', '''
<p>I. – Les conditions d'ouverture de l'immeuble doivent être déclarées avant le 1er février de chaque année auprès du service des impôts des particuliers dont dépend la résidence principale du déclarant :</p>
<p>a) Par la personne physique propriétaire de l'immeuble ou par l'une des personnes physiques titulaires de droits réels, qui agit au nom et pour le compte des autres titulaires de ces droits ;</p>
<p>b) À défaut, par l'une des personnes physiques associées de la société propriétaire de l'immeuble, agissant en son nom et pour son compte.</p>
<p>II. – La déclaration prévue au I contient les informations suivantes :</p>
<p>1° L'identité du propriétaire de l'immeuble :</p>
<p>a) Pour les personnes physiques, les nom, prénoms, date et lieu de naissance du propriétaire ou des titulaires de droits réels immobiliers et, le cas échéant, leur numéro fiscal ;</p>
<p>b) Pour les personnes morales, la raison sociale et le numéro SIRET ;</p>
<p>2° Le nom, les adresses physique et électronique et le numéro de téléphone du déclarant ;</p>
<p>3° Le nom de l'immeuble, s'il en possède un, son adresse et ses références cadastrales ;</p>
<p>4° Les horaires et dates d'ouverture au public, les zones ouvertes au public et le nombre total de jours d'ouverture, en précisant les jours non ouvrables ;</p>
<p>5° Le cas échéant, le tarif des visites individuelles selon les publics ;</p>
<p>6° Les manifestations ou ouvertures particulières du monument ;</p>
<p>7° Les moyens de communication utilisés pour informer le public.</p>
<p>Le déclarant date et signe la déclaration.</p>
<p>III. – Lorsque la réduction prévue au dernier alinéa de l'article 17 ter est appliquée, une copie de la ou des conventions conclues entre le propriétaire et les établissements ou structures concernés est jointe à la déclaration.</p>
<p>IV. – Un récépissé est délivré au déclarant à la suite de la déclaration.</p>
<p>V. – Les personnes mentionnées au I doivent diffuser auprès du public les conditions d'ouverture de l'immeuble par tous moyens appropriés.</p>
''',
    "Réécriture à droit constant de la procédure déclarative : identification du déclarant et du service compétent, liste des informations, signature, conventions annexées, récépissé et publicité. Les subdivisions I à V, a et b, et 1° à 7° sont conservées dans leur ordre. Aucune réforme de fond ni nouvelle transmission de données.",
    "Échéance conservée avant le 1er février de chaque année. Le déclarant subsidiaire du I, b reste une personne physique associée de la société propriétaire ; la formule « agissant en son nom et pour son compte » est conservée, son rattachement à la société ou à l'associé devant être contrôlé pour lever l'ambiguïté préexistante. La référence à « sa résidence principale » est explicitée comme celle du déclarant. Toutes les données d'identification et de contact, le caractère éventuel du numéro fiscal et du tarif, la copie des conventions, le récépissé et la diffusion au public sont maintenus. Coordination interne conservée avec le dernier alinéa de l'article 17 ter et l'article 17 quinquies.")

add('17 quinquies', '''
<p>Pour l'application du I de l'article 41 F de l'annexe III au code général des impôts, le contribuable joint à la déclaration des revenus de l'année considérée le récépissé de la déclaration prévue à l'article 17 quater.</p>
''',
    "Réécriture à droit constant à la voix active, en désignant le contribuable comme auteur de la jonction du récépissé à sa déclaration de revenus. La pièce, l'année et les renvois restent identiques ; aucune réforme de fond.",
    "Renvois au I de l'article 41 F de l'annexe III et à l'article 17 quater conservés. Les articles 41 F et 41 I ont été lus dans le corpus pour vérifier le lien avec l'ouverture au public. La note source cite l'article 26-I [l] et XI-3 de la loi n° 2013-1278 du 29 décembre 2013 et indique que les mots « et de l'article 41 H » sont devenus sans objet : ce renvoi n'est pas réintroduit.")

add('18-0 bis', '''
<p>Les équipements mentionnés au huitième alinéa du 6 de l'article 199 undecies A du code général des impôts sont les suivants :</p>
<p>1. Les équipements de chauffage et de fourniture d'eau chaude qui utilisent l'énergie solaire ;</p>
<p>2. Les systèmes de fourniture d'électricité produite à partir de l'énergie solaire, éolienne ou hydraulique, ou de la biomasse ;</p>
<p>3. Les pompes à chaleur ;</p>
<p>4. Les équipements de chauffage ou de production d'eau chaude qui utilisent le bois ou d'autres biomasses, tels que les poêles, les foyers fermés, les inserts des cheminées intérieures et les chaudières.</p>
''',
    "Réécriture à droit constant de l'introduction et des quatre catégories d'équipements, en exprimant directement l'énergie utilisée et en clarifiant les énumérations. Les catégories, leurs liaisons et les exemples sont conservés ; aucune réforme de fond.",
    "Renvoi au huitième alinéa du 6 de l'article 199 undecies A et numéros 1 à 4 conservés. Le 1 conserve le chauffage et la fourniture d'eau chaude ; le 4 conserve l'alternative chauffage ou production d'eau chaude et sa liste non exhaustive d'exemples. La note source est une coordination consécutive à l'article 38-I [6°] de la loi n° 2009-594 du 27 mai 2009. Aucun régime locatif ni délai de rénovation nouveau n'est ajouté.")

add('18-0 bis B', '''
<p>I. – Pour l'application de l'article 199 septvicies et de l'avant-dernier alinéa du h du 1° du I de l'article 31 du code général des impôts, sont considérées comme présentant un déséquilibre entre l'offre et la demande de logements les communes classées dans les zones A, B1 et B2. Ces zones sont délimitées conformément à l'annexe à l'arrêté du 29 avril 2009 relatif au classement des communes par zone applicable à certaines aides au logement.</p>
<p>II. – Pour l'application du III de l'article 199 septvicies du code général des impôts, les plafonds de loyer sont ceux prévus à l'article 2 terdecies B de l'annexe III au même code.</p>
<p>III. – Pour l'application du V de l'article 199 septvicies du code général des impôts, les plafonds de loyer et de ressources des locataires sont ceux prévus à l'article 2 terdecies C de l'annexe III au même code.</p>
''',
    "Réécriture à droit constant de la définition territoriale et des deux renvois aux plafonds, avec une phrase distincte pour l'arrêté de zonage. Les subdivisions I à III et la différence entre les plafonds des III et V de l'article 199 septvicies sont maintenues. Aucune réforme de fond des investissements ou contrats anciens.",
    "Zones A, B1 et B2 et arrêté du 29 avril 2009 conservés, sans substitution du zonage des articles 17 D bis ou 18-0 bis C. Renvois à l'avant-dernier alinéa du h du 1° du I de l'article 31, aux III et V de l'article 199 septvicies et aux articles 2 terdecies B et C de l'annexe III maintenus. La note source vise l'article 110-I A 3° de la loi n° 2023-1322 du 29 décembre 2023 ; elle ne justifie pas une nouvelle date de réforme. Les avantages anciens ne sont pas supprimés au titre du réexamen général des aides de policy.json.")

add('18-0 bis C', '''
<p>Pour l'application du IV de l'article 199 novovicies du code général des impôts, sont considérées comme présentant un déséquilibre important entre l'offre et la demande de logements les communes classées dans les zones A et B1 définies à l'article D. 304-1 du code de la construction et de l'habitation.</p>
''',
    "Réécriture à droit constant de la définition des communes en plaçant la qualification avant l'énumération des zones. Le caractère important du déséquilibre et le champ du IV de l'article 199 novovicies sont conservés ; aucune réforme de fond.",
    "Zones A et B1 et renvois au IV de l'article 199 novovicies et à l'article D. 304-1 du CCH conservés. Ce dernier, lu dans le corpus, inclut la zone A bis dans la zone A ; aucune zone B2 n'est ajoutée par alignement sur l'article 18-0 bis B. La note source cite l'article 5-II-3° du décret n° 2019-873 du 21 août 2019.")

add('18-0 bis E', '''
<p>I. – Pour l'application du II de l'article 199 tricies du code général des impôts aux logements situés en France métropolitaine, le contribuable doit justifier du respect des exigences suivantes :</p>
<p>A. – Pour les baux conclus ou renouvelés au plus tard le 31 décembre 2027 :</p>
<p>1° Soit une consommation conventionnelle d'énergie primaire du logement inférieure à 331 kWh/m2/an, évaluée pour les usages de chauffage, de production d'eau chaude sanitaire et de refroidissement. Cette possibilité s'applique lorsque le contribuable dispose d'une évaluation énergétique réalisée avant le 30 juin 2021 et en cours de validité au sens de l'article D. 126-19 du code de la construction et de l'habitation ;</p>
<p>2° Soit, dans les autres situations, un niveau de performance au moins égal à la classe E au sens de l'article L. 173-1-1 du même code ;</p>
<p>B. – Pour les baux conclus ou renouvelés à compter du 1er janvier 2028, un niveau de performance au moins égal à la classe D au sens de l'article L. 173-1-1 du code de la construction et de l'habitation.</p>
<p>II. – Le respect des exigences de performance énergétique prévues au I est justifié :</p>
<p>a) Dans les situations prévues au 1° du A du I, par un diagnostic de performance énergétique ou une évaluation énergétique établi selon une méthode de calcul conventionnelle conforme aux dispositions des arrêtés du 15 septembre 2006, dans leur version en vigueur au 30 juin 2021, relatifs respectivement aux méthodes et procédures applicables au diagnostic de performance énergétique pour les bâtiments existants proposés à la vente en France métropolitaine et au diagnostic de performance énergétique pour les bâtiments existants proposés à la vente en France métropolitaine ;</p>
<p>b) Dans les autres cas, par un diagnostic de performance énergétique conforme à l'arrêté du 31 mars 2021 relatif au diagnostic de performance énergétique pour les bâtiments ou parties de bâtiments à usage d'habitation en France métropolitaine, quels que soient l'année de construction et le type du bâtiment.</p>
<p>Cette évaluation énergétique ou ce diagnostic de performance énergétique :</p>
<p>– est réalisé par une personne répondant soit aux conditions de l'article L. 271-6 du code de la construction et de l'habitation, soit à celles du décret n° 2018-416 du 30 mai 2018 relatif aux conditions de qualification des auditeurs réalisant l'audit énergétique éligible au crédit d'impôt sur le revenu pour la transition énergétique prévues au dernier alinéa du 2 de l'article 200 quater du code général des impôts ;</p>
<p>– doit être en cours de validité, selon le cas, à la date d'enregistrement de la demande de conventionnement par l'Agence nationale de l'habitat, à la conclusion du bail si celle-ci intervient après la conclusion de la convention avec cette agence, ou lors du renouvellement du bail.</p>
<p>III. – Le contribuable doit produire, sur simple demande, les justificatifs prévus au II.</p>
''',
    "Réécriture à droit constant de l'arbre de conditions énergétiques, des moyens de preuve et de leur validité. Les subdivisions I à III, A et B, 1° et 2°, a et b, ainsi que les deux conditions finales de qualification et de validité sont conservées dans leur ordre. Les phrases sont scindées sans changer les seuils ni les dates. Aucune réforme de fond du régime fiscal et aucune dérogation nouvelle à la décence locative.",
    "Contrôle des paramètres : consommation strictement inférieure à 331 kWh/m2/an ; évaluation réalisée avant le 30 juin 2021 ; classe E jusqu'aux baux conclus ou renouvelés au plus tard le 31 décembre 2027 ; classe D à compter du 1er janvier 2028. Renvois au II de l'article 199 tricies, aux articles D. 126-19, L. 173-1-1 et L. 271-6 du CCH et au dernier alinéa du 2 de l'article 200 quater maintenus. D. 126-19, lu dans le corpus, limite au 31 décembre 2024 au plus tard la validité des DPE antérieurs à juillet 2021 : le maintien du cas historique au I, A, 1° ne proroge pas ces diagnostics et appelle un contrôle pour les évaluations concernées. Le II, a reprend les deux objets d'arrêtés du 15 septembre 2006 figurant dans la source, dont les intitulés se recouvrent ; anomalie rédactionnelle conservée, à vérifier dans les arrêtés sans substitution conjecturale. La voie de rénovation locative de vingt-quatre mois de policy.json exige des dispositions dans la loi n° 89-462 du 6 juillet 1989, notamment son article 6, et ses textes d'application sur la décence : elle ne modifie pas, à elle seule, les conditions distinctes de cette réduction d'impôt. Les trois dates d'appréciation et les deux voies de qualification du professionnel sont maintenues.")

add('18-0 bis F', '''
<p>I. – Pour l'application du II de l'article 199 tricies du code général des impôts aux logements situés en Guadeloupe, en Martinique, en Guyane, à La Réunion et à Mayotte, le contribuable doit justifier que le logement respecte les conditions du I de l'article 01 quater. Ces conditions doivent être remplies, selon le cas, à la date d'enregistrement de la demande de conventionnement par l'Agence nationale de l'habitat, à la conclusion du bail si celle-ci intervient après la conclusion de la convention avec cette agence, ou lors du renouvellement du bail.</p>
<p>II. – Sur simple demande, le contribuable doit produire toutes les factures ou notes émises par les entreprises prestataires, ou tout autre moyen de preuve compatible avec les règles de la procédure écrite, permettant d'établir que le logement satisfait aux conditions prévues au I.</p>
''',
    "Réécriture à droit constant en séparant l'obligation de conformité et les dates auxquelles elle s'apprécie, puis en plaçant la demande de justificatifs en tête du II. Les territoires et les moyens de preuve sont intégralement maintenus. Aucune réforme de fond ni transposition des classes énergétiques métropolitaines.",
    "Les cinq territoires, les trois dates d'appréciation et l'alternative entre factures ou notes et autres preuves écrites compatibles sont conservés. Le I de l'article 01 quater a été lu dans le corpus : il vise au moins une amélioration mentionnée à l'article 2 de l'arrêté du 25 mai 2011 modifié satisfaisant les exigences de ses articles 3 à 6 ; le renvoi « 01 quater » est repris exactement. La future voie de rénovation locative de vingt-quatre mois relève de la loi n° 89-462 du 6 juillet 1989, notamment son article 6, et des textes de décence, avec une articulation territoriale à prévoir ; elle n'est pas étendue implicitement à cette condition fiscale particulière.")


sources = json.loads(Path('source.json').read_text())
assert len(sources) == 22
assert {a['number'] for a in sources} == set(drafts)
answer = []
for source in sources:
    xml, reason, review = drafts[source['number']]
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': source['number'],
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': review,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
