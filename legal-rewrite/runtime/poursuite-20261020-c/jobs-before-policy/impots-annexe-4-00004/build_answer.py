import json
import re
from pathlib import Path
from xml.etree import ElementTree as ET


sources = json.loads(Path('source.json').read_text())
drafts = {}


def put(number, xml, reason, notes):
    drafts[number] = (xml.strip(), reason, notes)


put('23 A', '''
<p>Les sociétés mentionnées à l'article 206 du code général des impôts doivent déposer une déclaration dans un délai d'un mois à compter de leur constitution définitive ou, le cas échéant, de la date à laquelle elles deviennent passibles de l'impôt sur les sociétés. Sous réserve des modalités de réutilisation des renseignements prévues à l'article 23 G, cette déclaration indique :</p>
<p>1° La raison sociale, la forme juridique, l'objet principal, la durée et le siège de la société, ainsi que le lieu de son principal établissement ;</p>
<p>2° La date de l'acte constitutif ;</p>
<p>3° Les nom, prénoms et domicile des dirigeants ou gérants et, lorsque le capital de la société n'est pas divisé en actions, ceux de chacun des associés ;</p>
<p>4° La nature et la valeur des biens mobiliers et immobiliers apportés à la société ;</p>
<p>5° Le nombre, la forme et le montant des titres, parts et droits suivants :</p>
<p>a. Les titres négociables émis, en distinguant les actions des obligations. Pour les actions, la déclaration précise la somme dont chaque titre est libéré ; pour les obligations, elle précise la durée de l'amortissement et le taux de l'intérêt ;</p>
<p>b. Les parts sociales, ou parts de capital, qui ne sont pas représentées par des titres négociables ;</p>
<p>c. Les autres droits de toute nature attribués aux associés dans le partage des bénéfices ou de l'actif social, que ces droits soient ou non constatés par des titres.</p>
''',
    "À droit constant, le débiteur de la déclaration et le point de départ du délai sont explicités ; les renseignements restent répartis entre les mêmes 1° à 5° et a à c. La seule coordination de fond est le renvoi à la réutilisation des données instituée à l'article 23 G en application de policy.json.",
    "Conserver le délai d'un mois et les deux faits déclencheurs alternatifs. La réutilisation prévue au nouvel alinéa de l'article 23 G ne dispense pas de déclarer l'existence de la société ni de fournir les renseignements manquants ou modifiés. Les catégories d'assujettissement de l'article 206 ne sont pas modifiées.")

put('23 B', '''
<p>Les sociétés mentionnées à l'article 23 A doivent déclarer, dans un délai d'un mois, chacun des changements suivants : la modification de leur raison sociale, de leur forme juridique, de leur objet, de leur durée, de leur siège ou du lieu de leur principal établissement ; l'augmentation, la réduction ou l'amortissement de leur capital ; la libération totale ou partielle de leurs actions ; l'émission, le remboursement ou l'amortissement d'emprunts représentés par des titres négociables ; le remplacement d'un ou plusieurs dirigeants ou gérants ou, lorsque leur capital n'est pas divisé en actions, d'un ou plusieurs associés. Les modalités de réutilisation des renseignements prévues à l'article 23 G s'appliquent à cette déclaration.</p>
''',
    "La longue énumération est ponctuée pour distinguer chaque événement déclarable, tout en conservant l'alinéa unique et le délai d'un mois. Le renvoi à l'article 23 G coordonne la simplification de fond relative aux données déjà détenues ; les événements à déclarer restent inchangés.",
    "La source présente une ponctuation défectueuse entre la libération des actions, les opérations sur emprunts et les remplacements de dirigeants ou d'associés. La proposition rend explicite leur lecture comme événements distincts, sans en supprimer aucun. Le bénéfice de la réutilisation ne supprime pas l'obligation de signaler un changement dans le délai prescrit.")

put('23 C', '''
<p>Pour l'application du 3° de l'article 23 A et de l'article 23 B, sont notamment considérés comme dirigeants, dans les sociétés anonymes, le président du conseil d'administration, le directeur général, qu'il soit ou non administrateur, et, le cas échéant, l'administrateur provisoirement délégué pour exercer les fonctions de président.</p>
''',
    "Réécriture à droit constant de la définition des dirigeants : la liste indicative est introduite directement et les fonctions ainsi que leurs qualifications sont conservées. Aucune réforme de fond n'est appliquée à cette définition.",
    "La liste reste non exhaustive grâce au mot « notamment ». Le directeur général demeure visé même s'il n'est pas administrateur ; le caractère provisoire de la délégation est maintenu. Renvois au 3° de l'article 23 A et à l'article 23 B conservés.")

put('23 D', '''
<p>Les sociétés dont le siège social est situé hors de France et qui exercent en France une activité les rendant passibles de l'impôt sur les sociétés doivent également indiquer, dans la déclaration prévue à l'article 23 A, le lieu de leur principal établissement en France ainsi que les nom, prénoms et adresse de leur représentant en France.</p>
<p>Si ce représentant est remplacé ou si le lieu de ce principal établissement change, ces sociétés doivent déclarer ce changement dans les conditions fixées à l'article 23 B.</p>
''',
    "Réécriture à droit constant des obligations propres aux sociétés dont le siège est hors de France : la double condition d'assujettissement et les deux changements à déclarer sont explicités. La simplification de fond de l'article 23 G s'applique par les déclarations des articles 23 A et 23 B, sans modifier le champ territorial.",
    "Maintien des deux alinéas et de l'exigence d'une activité en France rendant la société passible de l'impôt sur les sociétés. Le renvoi à l'article 23 B conserve le délai d'un mois. Aucun représentant supplémentaire ni établissement distinct n'est exigé.")

put('23 E', '''
<p>Les établissements et organismes publics ainsi que les personnes morales de toute nature, autres que les sociétés, mentionnés à l'article 206 du code général des impôts doivent, lorsqu'ils sont passibles de l'impôt sur les sociétés, produire les déclarations prévues aux articles précédents. Cette obligation ne porte que sur les renseignements compatibles avec la forme ou le statut de la collectivité concernée.</p>
<p>Toutefois, les établissements publics, associations et collectivités mentionnés au 5 de l'article 206 du même code sont dispensés de cette obligation.</p>
''',
    "À droit constant, la condition d'assujettissement et la limite tenant à la compatibilité des renseignements sont exprimées dans deux phrases du même alinéa. L'exemption du second alinéa est conservée. La réutilisation prévue à l'article 23 G constitue la seule simplification de fond commune à ces déclarations.",
    "Ne pas étendre les déclarations aux personnes non passibles de l'impôt sur les sociétés ni aux organismes dispensés par le 5 de l'article 206. L'ajout d'une phrase au premier alinéa ne déplace pas le second alinéa d'exemption.")

put('23 G', '''
<p>La personne morale adresse ou remet les déclarations prévues aux articles 23 A et suivants au service dont elle relève pour l'assiette de l'impôt sur les sociétés.</p>
<p>Pour les déclarations prévues aux articles 23 A à 23 E, ce service réutilise les renseignements à jour qu'il détient déjà légalement ou auxquels il peut légalement accéder et ne demande pas à la personne morale de les fournir de nouveau. Il met les renseignements ainsi réutilisés à la disposition de la personne morale afin qu'elle puisse les vérifier et, le cas échéant, en demander la rectification. La personne morale reste tenue de souscrire les déclarations et de déclarer, dans les délais prévus, les renseignements manquants et les changements intervenus. Cette réutilisation s'effectue dans le respect des secrets protégés par la loi.</p>
''',
    "Le premier alinéa est réécrit à droit constant en désignant la personne chargée de transmettre la déclaration. Le second met en œuvre la réforme de fond de policy.json sur les demandes en double : réutilisation de renseignements actuels légalement disponibles, vérification et rectification, maintien des déclarations et de leurs délais, respect des secrets protégés.",
    "Le premier alinéa et son champ « articles 23 A et suivants » sont conservés ; la nouvelle règle de réutilisation est limitée aux déclarations des articles 23 A à 23 E. Coordonner les formulaires et les procédures du service compétent, sans créer de nouveau portail. Tout accès à des données détenues ailleurs suppose une habilitation légale existante : cet alinéa ne lève aucun secret et n'autorise pas à lui seul une nouvelle interconnexion. Aucune suppression d'une obligation législative d'information n'est présumée.")

put('23 H', '''
<p>Les personnes morales et associations mentionnées à l'article 223 du code général des impôts doivent joindre à leur déclaration de bénéfice ou de déficit un état relatif aux bénéfices répartis aux associés, actionnaires ou porteurs de parts ainsi qu'aux sommes ou valeurs mises à leur disposition au cours de la période retenue pour l'assiette de l'impôt sur les sociétés et présentant le caractère de revenus distribués au sens des articles 108 et suivants du même code. Cet état comporte :</p>
<p>1° Le montant global des distributions correspondant aux intérêts, dividendes, revenus et autres produits des actions et parts sociales payables aux associés, actionnaires ou porteurs de parts sur présentation ou remise de coupons ou d'instruments représentatifs de coupons ;</p>
<p>2° Le montant des distributions correspondant à des rémunérations ou avantages occultes ;</p>
<p>2° bis Le montant des revenus distribués aux associés, actionnaires ou porteurs de parts, en distinguant ceux qui sont éligibles à l'abattement de 40 % mentionné au 2° du 3 de l'article 158 du code général des impôts et ceux qui ne le sont pas ;</p>
<p>3° Pour les distributions autres que celles mentionnées aux 1° et 2°, un relevé de leurs bénéficiaires indiquant les noms, prénoms, qualités et domiciles de ces derniers, la nature et le montant des sommes versées à chacun ainsi que l'année de ces versements.</p>
''',
    "Réécriture à droit constant : les personnes tenues de joindre l'état sont placées en sujet ; la liste indique directement les montants et les renseignements attendus. La distinction entre distributions, avantages occultes, éligibilité à l'abattement et relevé nominatif est conservée, sans réforme de fond des revenus distribués.",
    "Numérotation 1°, 2°, 2° bis et 3° inchangée. Le 3° exclut seulement les distributions des 1° et 2°, comme dans la source, et non celles du 2° bis. L'abattement de 40 % et le renvoi au 2° du 3 de l'article 158 sont conservés ; aucune assimilation au nouveau taux normal d'IS n'est opérée.")

put('23 I', '''
<p>L'état prévu à l'article 23 H doit être établi sur les imprimés que fournit l'administration.</p>
''',
    "Réécriture à droit constant de la règle de forme, avec une formulation directe de l'obligation d'utiliser les imprimés administratifs. Aucune dématérialisation ni dispense nouvelle n'est créée.",
    "Le renvoi à l'article 23 H et la fourniture des imprimés par l'administration sont conservés. La réutilisation ajoutée à l'article 23 G pour les articles 23 A à 23 E n'est pas étendue à cet état.")

put('23 J', '''
<p>Lorsque le remploi consiste à souscrire au capital initial ou aux augmentations de capital de l'une des sociétés ci-dessous, les plus-values mentionnées au I de l'article 238 octies du code général des impôts peuvent bénéficier des dispositions de l'article 40 du même code :</p>
<p>Les sociétés immobilières d'investissement et les sociétés immobilières de gestion qui satisfont aux conditions de l'article 33 de la loi n° 63-254 du 15 mars 1963 ;</p>
<p>Les sociétés en nom collectif dont l'objet est la construction, en vue de leur vente, d'immeubles affectés à l'habitation pour les trois quarts au moins de leur superficie totale ;</p>
<p>Les sociétés civiles qui ont le même objet et relèvent de l'article 239 ter du code général des impôts.</p>
''',
    "Réécriture à droit constant : la condition de remploi par souscription est placée en tête ; les trois catégories de sociétés sont maintenues dans les mêmes alinéas avec leurs conditions. Aucune réforme de fond ni ouverture nouvelle du régime historique n'est proposée.",
    "Le corpus confirme que les dispositions conservées de l'article 40, bien qu'historiquement abrogé, servent à l'application de l'article 238 octies. Ces renvois ne sont donc pas supprimés. Conserver le seuil des trois quarts, la loi n° 63-254 du 15 mars 1963 et la condition propre à l'article 239 ter. Le présent article ne rouvre pas les périodes d'application du régime.")

put('23 K', '''
<p>Le remploi défini à l'article 23 J peut être réalisé sans qu'un pourcentage minimal de participation soit exigé.</p>
''',
    "Réécriture à droit constant de l'absence de seuil minimal de participation, en prenant le remploi comme sujet. Aucune réforme de fond n'est apportée au régime.",
    "L'absence de minimum concerne seulement le remploi défini à l'article 23 J ; elle ne supprime aucune autre condition de ce régime historique.")

put('23 L', '''
<p>Les contrats suivants sont dispensés de la déclaration prévue à l'article 49 B de l'annexe III au code général des impôts :</p>
<p>1° Les contrats de prêts dont le montant en principal n'excède pas 5 000 €, sous réserve du b du 2 de l'article 49 B précité ;</p>
<p>2° (Abrogé) ;</p>
<p>3° Les contrats de prêts conclus par l'État, les établissements publics et les collectivités locales ;</p>
<p>4° Les contrats de prêts dans la conclusion desquels un établissement de crédit enregistré par l'Autorité de contrôle prudentiel et de résolution intervient comme prêteur ou emprunteur ;</p>
<p>5° Les contrats de prêts réalisés par l'émission de bons de caisse par des banques ou par l'émission publique d'obligations.</p>
<p>Toutefois, la dispense prévue aux 1° à 5° ne s'applique pas aux bons ou titres mentionnés au 2° du III bis de l'article 125 A du code général des impôts lorsque leur détenteur communique son identité et son domicile fiscal à l'établissement qui assure le paiement de leurs intérêts ou leur remboursement.</p>
''',
    "Réécriture à droit constant des catégories de prêts dispensées : les modes d'intervention et d'émission sont exprimés plus directement. Le montant maximal, la réserve de cumul, l'emplacement abrogé et l'exception finale sont conservés. Aucune réforme de fond du régime des prêts n'est appliquée.",
    "Le b du 2 de l'article 49 B de l'annexe III, vérifié dans le corpus, impose la déclaration de tous les contrats cumulés au cours d'une année au nom d'un même débiteur ou créancier lorsque le total en principal dépasse le seuil : la réserve est maintenue. Le seuil de 5 000 € inclut l'égalité. La note source relative à l'article 24-I de la loi n° 2013-672 du 26 juillet 2013 est historique ; elle ne fixe aucune date d'entrée en vigueur du projet. Le 2° abrogé reste à sa place.")


# Chaque série est intégralement convertie en tableau, sans recalculer ses valeurs.
source_bis = next(a['source_xml'] for a in sources if a['number'] == '23 L bis')
bis_paras = ET.fromstring('<div>' + source_bis + '</div>')
bis_result = []
bis_series = []
for i, p in enumerate(bis_paras):
    value = ''.join(p.itertext())
    if i == 0:
        bis_result.append("<p>I. – Pour la réévaluation des immobilisations amortissables situées en France métropolitaine et dans les départements de la Guadeloupe, de la Guyane et de la Martinique, les coefficients correspondant aux indices représentatifs de l'évolution des prix mentionnés au I de l'article 238 bis J du code général des impôts sont fixés, pour chaque année et chaque catégorie de biens, comme suit :</p>")
    elif value.startswith('II.'):
        bis_result.append("<p>II. – Dans le département de la Réunion, les coefficients de réévaluation sont fixés, pour chaque année et chaque catégorie de biens, comme suit :</p>")
    elif value.startswith('a.'):
        bis_result.append('<p>a. Pour les constructions immobilières :</p>')
    elif value.startswith('b.'):
        bis_result.append('<p>b. Pour les autres immobilisations amortissables :</p>')
    else:
        pairs = re.findall(r'Années? (\d{4}(?: et antérieures)?)\s*:\s*([0-9]+(?:,[0-9]+)?)\.', value)
        assert len(pairs) == 63, (i, len(pairs))
        bis_series.append(pairs)
        rows = ''.join('<tr><td>' + year + '</td><td>' + coefficient + '</td></tr>' for year, coefficient in pairs)
        bis_result.append('<table><thead><tr><th>Année</th><th>Coefficient de réévaluation</th></tr></thead><tbody>' + rows + '</tbody></table>')
assert len(bis_series) == 4
put('23 L bis', '\n'.join(bis_result),
    "Réécriture à droit constant des règles d'application territoriale et des intitulés. Les quatre séries annuelles sont présentées dans quatre tableaux complets à deux colonnes, dans l'ordre I a, I b, II a, II b, pour faciliter la lecture des 252 coefficients sans en recalculer ni en omettre aucun. Aucune réforme de fond de la réévaluation historique n'est introduite.",
    "Anomalie préexistante : le coefficient des constructions immobilières pour 1972, au I a, est « 63 » dans la source, entre 1,72 pour 1971 et 1,47 pour 1973. Il est conservé à l'identique et nécessite un contrôle documentaire ; aucune correction conjecturale à 1,63 n'est effectuée. Au II a, les coefficients des constructions pour 1943 et 1944 sont respectivement 37,6 et 34,4, supérieurs aux valeurs 33,6 de 1942 : ils sont également conservés et à contrôler. Les quatre séries de 1914 et antérieures à 1976 sont intégrales, avec leurs décimales. Les champs territoriaux distincts et le renvoi au I de l'article 238 bis J sont maintenus ; les dates historiques de ce régime ne sont pas des dates du projet.")

put('23 L quater', '''
<p>Pour l'application de la deuxième phrase du quinzième alinéa du I de l'article 199 undecies B, du troisième alinéa du I de l'article 217 undecies, du a du 2 du I de l'article 244 quater W et du 1° du 2 du A du I de l'article 244 quater Y du code général des impôts, les véhicules de tourisme mentionnés à l'article L. 421-2 du code des impositions sur les biens et services sont strictement indispensables à l'exercice d'une activité aquacole, agricole, sylvicole ou minière lorsqu'il s'agit de véhicules neufs sans lesquels l'entreprise ne pourrait pas poursuivre cette activité.</p>
''',
    "Réécriture à droit constant : les dispositifs concernés sont annoncés avant la définition, dont les conditions cumulatives de nouveauté et de nécessité stricte sont conservées. Aucune réforme de fond des investissements outre-mer n'est appliquée.",
    "Conserver intégralement les quatre renvois fiscaux, notamment la deuxième phrase du quinzième alinéa du I de l'article 199 undecies B et le troisième alinéa du I de l'article 217 undecies. Les quatre activités restent limitativement citées ; une simple utilité du véhicule ne remplace pas l'impossibilité de poursuivre l'activité sans lui. Le renvoi au code des impositions sur les biens et services est conservé sans modification de ce code hors lot.")

put('23 L quinquies', '''
<p>Pour l'application du e du 1 du I de l'article 244 quater X et des d du 1°, e du 2° et b du 3° du D du I de l'article 244 quater Y du code général des impôts, les dépenses retenues sont celles mentionnées au I de l'article 18 quater. Elles doivent être justifiées selon les modalités du II de ce même article.</p>
''',
    "Réécriture à droit constant : le champ des dépenses et l'obligation de justification sont exprimés directement, dans le même alinéa. Les subdivisions des renvois sont conservées et aucune réforme de fond n'est apportée aux crédits d'impôt concernés.",
    "Les dépenses restent celles du I de l'article 18 quater et leurs justificatifs ceux du II. Les renvois distincts aux d du 1°, e du 2° et b du 3° du D du I de l'article 244 quater Y ne sont ni fusionnés ni renumérotés.")


platform_note = "Dans le corpus fourni, l'article 242 bis du CGI, applicable depuis le 1er janvier 2023 selon sa note, ne comporte plus de 1°, 2° ou 3°. Le renvoi hérité de la source nécessite donc une coordination expresse avec le texte législatif applicable ; il est conservé et n'est pas remplacé par un renvoi conjectural. "

put('23 L sexies', '''
<p>I. – Pour l'application du 1° de l'article 242 bis du code général des impôts, l'entreprise mentionnée au premier alinéa de cet article communique une information à l'occasion de chaque transaction réalisée par l'intermédiaire d'une plateforme de mise en relation par voie électronique. Elle la communique au vendeur, au prestataire ou aux parties à l'échange ou au partage d'un bien ou d'un service, lorsque ces personnes ont perçu des sommes à l'occasion des transactions. Cette information porte sur les régimes fiscaux et la réglementation sociale applicables à ces sommes, sur les obligations déclaratives et de paiement qui en résultent auprès de l'administration fiscale et des organismes de recouvrement des cotisations sociales, ainsi que sur les sanctions encourues en cas de manquement à ces obligations.</p>
<p>II. – Les sites internet édités par l'entreprise mentionnée au I indiquent des liens hypertexte directs ou indirects vers les sites de l'administration fiscale et des organismes de sécurité sociale qui donnent accès aux informations mentionnées au I. L'obligation du I est réputée satisfaite lorsque les messages envoyés aux parties aux transactions mentionnées au I présentent ces liens hypertexte de manière lisible.</p>
<p>La liste de ces liens est publiée au Bulletin officiel des finances publiques-impôts (BOFiP-Impôts).</p>
''',
    "Réécriture à droit constant : la phrase du I est divisée pour distinguer l'entreprise obligée, les destinataires ayant perçu des sommes et le contenu de l'information. Le II conserve l'accès par liens, la règle de satisfaction de l'obligation et la publication de leur liste. Aucune réforme de fond des plateformes n'est introduite.",
    platform_note + "L'obsolescence concerne ici le renvoi au 1°, tandis que le premier alinéa du texte législatif fourni conserve une obligation d'information. Les I et II et le dernier alinéa sont maintenus. Aucun lien effectif n'est inséré dans le proposed_xml ; l'obligation juridique de proposer des liens demeure intégrale.")

put('23 L septies', '''
<p>L'identification de l'opérateur de plateforme prévue au a du 2° de l'article 242 bis du code général des impôts repose sur les éléments suivants :</p>
<p>1° Sa raison sociale ;</p>
<p>2° Son lieu d'établissement au 1er janvier de l'année au cours de laquelle le document mentionné est transmis ;</p>
<p>3° Son numéro d'identification mentionné au premier alinéa de l'article R. 123-221 du code de commerce.</p>
''',
    "Réécriture à droit constant des trois éléments d'identification, avec explicitation de l'année de référence du lieu d'établissement. Aucune donnée supplémentaire ni réforme de fond n'est créée.",
    platform_note + "Le renvoi concerné est le a du 2°. Le lieu d'établissement reste celui du 1er janvier, et non celui de la date de transmission. Le renvoi au premier alinéa de l'article R. 123-221 du code de commerce est conservé. La note sur les articles 3-3° et 45 du décret n° 2022-1014 du 19 juillet 2022 est historique.")

put('23 L octies', '''
<p>L'identification de l'utilisateur prévue au b du 2° de l'article 242 bis du code général des impôts repose sur les éléments suivants :</p>
<p>1. Pour les personnes physiques :</p>
<p>a) Le nom de famille ou d'usage ;</p>
<p>b) Les prénoms ;</p>
<p>c) L'adresse de résidence ;</p>
<p>d) Le numéro de téléphone ;</p>
<p>e) L'adresse électronique ;</p>
<p>f) La date de naissance ;</p>
<p>g) Lorsque le montant total brut des transactions réalisées par l'utilisateur au titre de l'année considérée atteint ou dépasse 1 000 euros, l'opérateur de plateforme doit satisfaire à l'une des deux obligations suivantes :</p>
<p>1° Vérifier le nom de famille ou d'usage, les prénoms et la date de naissance de l'utilisateur, notamment au moyen d'une copie d'une pièce d'identité présentée par celui-ci ;</p>
<p>2° Indiquer à l'administration le numéro d'inscription de l'utilisateur au fichier de simplification des procédures d'imposition (SPI), après en avoir vérifié la structure, le format et l'algorithme.</p>
<p>2. Pour une personne morale ou une personne physique agissant à titre professionnel :</p>
<p>a) La raison sociale ;</p>
<p>a bis) Le nom commercial de l'utilisateur ou le nom d'utilisateur tel qu'il est communiqué sur la plateforme en ligne ;</p>
<p>b) Le lieu d'établissement connu de l'opérateur à la date de transmission du document ;</p>
<p>c) Le numéro de taxe sur la valeur ajoutée intracommunautaire ou, à défaut, les numéros d'identification définis à l'article R. 123-221 du code de commerce ou, pour une entreprise non résidente, le numéro d'immatriculation auprès de l'administration fiscale de son pays de résidence ;</p>
<p>d) L'adresse électronique ;</p>
<p>e) L'adresse de localisation de la ressource internet de l'utilisateur professionnel ou, à défaut, l'identifiant fourni par l'opérateur de plateforme en ligne.</p>
''',
    "Réécriture à droit constant : les rubriques sont isolées et l'alternative du g entre vérification d'identité et transmission du SPI est formulée comme deux obligations au choix. Tous les renseignements des personnes physiques et des utilisateurs professionnels sont maintenus, y compris a bis et e. Aucune réforme de fond du contrôle d'identité n'est introduite.",
    platform_note + "Le renvoi concerné est le b du 2°. Le seuil de 1 000 euros s'applique dès l'égalité ; les deux voies du g sont alternatives. Les numéros 1. et 2., les lettres et les 1° et 2° restent à leur place. Les personnes physiques agissant à titre professionnel restent expressément visées au 2., sans ajout d'une exclusion au 1. Le lieu d'établissement du 2. b est apprécié à la transmission, contrairement à celui de l'opérateur dans l'article 23 L septies. La note sur le décret n° 2022-1014 du 19 juillet 2022 est historique.")

put('23 L nonies', '''
<p>Pour préciser le montant total brut prévu au d du 2° de l'article 242 bis du code général des impôts, l'opérateur de plateforme peut faire apparaître séparément le montant des transactions mentionnées au deuxième alinéa du 3° de cet article et le montant des autres transactions.</p>
''',
    "Réécriture à droit constant de la faculté de ventiler le montant brut entre deux catégories de transactions. La formulation conserve son caractère facultatif et n'applique aucune réforme de fond aux déclarations des plateformes.",
    platform_note + "Les renvois concernés sont le d du 2° et le deuxième alinéa du 3°. La faculté prévue ici n'est pas confondue avec l'obligation de distinction fiscale de l'article 23 L nonies A.")

put('23 L nonies A', '''
<p>Au sein du montant total brut prévu au d du 2° de l'article 242 bis du code général des impôts, l'opérateur de plateforme doit faire apparaître séparément le montant des transactions imposables en France au sens des articles 258 à 259 D du même code.</p>
''',
    "Réécriture à droit constant : le caractère obligatoire de l'identification séparée des transactions imposables en France est explicité. Le champ territorial est toujours défini par les mêmes articles et aucune réforme de fond n'est ajoutée.",
    platform_note + "Le renvoi concerné est le d du 2°. Les articles 258 à 259 D sont conservés. La note source de l'article 2 de l'arrêté du 30 décembre 2019 fixe l'application aux transactions réalisées à compter du 1er janvier 2020 ; cette portée historique est conservée et ne constitue pas une date d'entrée en vigueur du projet.")

put('23 L decies', '''
<p>Les coordonnées bancaires mentionnées au e du 2° de l'article 242 bis du code général des impôts sont présentées au format du code d'identification des banques (BIC) et du numéro de compte bancaire international (IBAN).</p>
<p>L'entreprise est réputée connaître ces coordonnées lorsqu'elle verse directement les sommes à l'utilisateur ou lorsqu'elle recourt à un prestataire de services pour effectuer ce versement.</p>
''',
    "Réécriture à droit constant : la règle de format et la présomption de connaissance sont présentées dans leurs deux alinéas, avec l'entreprise comme sujet du second. Les versements directs et ceux réalisés par un prestataire demeurent couverts, sans réforme de fond.",
    platform_note + "Le renvoi concerné est le e du 2°. Maintenir les deux formats BIC et IBAN et les deux cas de connaissance réputée ; le recours à un prestataire n'écarte pas cette présomption.")

put('23 L undecies', '''
<p>Pour l'application du troisième alinéa du 3° de l'article 242 bis du code général des impôts :</p>
<p>1. Le seuil relatif au total annuel des montants perçus par un même utilisateur sur une plateforme est fixé à 3 000 euros.</p>
<p>2. Le seuil relatif au nombre annuel de transactions réalisées par un même utilisateur sur une plateforme est fixé à 20.</p>
''',
    "Réécriture à droit constant des deux valeurs de référence en explicitant leur nature de seuils. Leur appréciation annuelle pour un même utilisateur sur une plateforme est maintenue ; aucun seuil nouveau ni réforme de fond n'est introduit.",
    platform_note + "Le renvoi concerné est le troisième alinéa du 3°. Conserver 3 000 euros et 20 transactions, ainsi que les subdivisions 1. et 2. Cet article ne redéfinit pas les conditions de combinaison des seuils, qui relèvent du texte législatif auquel la source renvoie.")

put('23 L duodecies', '''
<p>Le demandeur de l'agrément mentionné au I de l'article 49 septies H de l'annexe III au code général des impôts joint à sa demande les pièces justificatives suivantes :</p>
<p>a) Une fiche, conforme au format établi par l'administration, présentant l'organisme et l'opération de recherche et développement qu'il a réalisée au cours de l'année précédant la demande ;</p>
<p>b) Une photocopie des diplômes et des curriculum vitae de cinq chercheurs au maximum parmi ceux affectés à l'opération de recherche et développement présentée ;</p>
<p>c) Un extrait d'immatriculation au registre du commerce et des sociétés ou tout autre document justifiant de l'existence de l'organisme qui demande l'agrément.</p>
<p>L'administration réutilise les pièces et renseignements à jour qu'elle détient déjà légalement ou auxquels elle peut légalement accéder et ne demande pas au demandeur de les produire de nouveau. Elle lui permet de vérifier les renseignements ainsi réutilisés et, le cas échéant, d'en demander la rectification. Le demandeur fournit les pièces ou renseignements manquants ou qui doivent être actualisés. Cette réutilisation s'effectue dans le respect des secrets protégés par la loi.</p>
''',
    "Les pièces a à c sont réécrites à droit constant en identifiant le demandeur et en distinguant le contenu de la fiche de son format. Le dernier alinéa applique la réforme de fond de policy.json sur la suppression des demandes en double, avec données à jour, accès légal, vérification, rectification et maintien des compléments nécessaires.",
    "Le corpus confirme que le I de l'article 49 septies H de l'annexe III impose une demande et des justificatifs de travaux de l'année précédente et renvoie leur liste à un arrêté conjoint. Coordonner les modèles de demande et de renouvellement avec la réutilisation des pièces, sans supprimer les conditions d'agrément ni changer les durées ou délais de l'article 49 septies H. La limite de cinq chercheurs au maximum est conservée. Ce dernier article vise aussi des experts scientifiques ou techniques alors que la liste source est rédigée pour un organisme : cette différence de rédaction préexistante reste à examiner, sans extension inventée. La nouvelle disposition n'autorise aucune levée de secret ni accès nouveau dépourvu de base légale.")

put('23 M bis', '''
<p>Les opérations relevant du 1° du A du II de l'article 244 quater I du code général des impôts sont les suivantes :</p>
<p>1° La fabrication de cellules de batteries utilisant les électrochimies suivantes : LFP, LMP, LMFP, LMO, LNMO, NMC, NCA, NMx, LCO, Na-ion, Zinc, LTO, lithium-soufre, lithium solide et semi-solide. Cette fabrication peut être associée, sur le même site, à la fabrication de modules de batteries d'une capacité équivalente ;</p>
<p>2° La fabrication des matériaux actifs de cathode, des matériaux actifs d'anode, dont le graphite artificiel, des électrolytes, des collecteurs et feuillards de cuivre, d'aluminium, de nickel et de carbone, ainsi que des séparateurs ;</p>
<p>3° L'extraction, la production, la transformation et la valorisation des matières premières critiques mentionnées au c du 1° du A du II de l'article 244 quater I du code général des impôts, à savoir le graphite naturel, le lithium, le nickel, le manganèse et le cobalt, ainsi que le recyclage des déchets de batteries et des rebuts de production.</p>
''',
    "Réécriture à droit constant : la condition d'association des cellules et des modules est isolée dans une phrase du 1° ; les matériaux, matières premières et opérations de recyclage sont intégralement énumérés. Aucune réforme de fond du crédit d'impôt pour l'industrie verte n'est introduite.",
    "Toute l'énumération des électrochimies, avec la dernière formulation « lithium solide et semi-solide », est conservée dans son ordre et sa graphie. L'association aux modules reste facultative, sur le même site et à capacité équivalente. Le graphite artificiel du 2° reste distinct du graphite naturel du 3°. Aucune suppression d'aide n'est déduite du seul objectif de réexamen des niches figurant dans policy.json.")

put('23 M ter', '''
<p>Les opérations relevant du 2° du A du II de l'article 244 quater I du code général des impôts sont les suivantes :</p>
<p>1° La fabrication de cellules photovoltaïques, qui peut être associée à la fabrication de modules photovoltaïques d'une capacité équivalente, ainsi que la fabrication de capteurs thermiques, uniquement lorsque ces capteurs sont destinés à des modules solaires hybrides. La fabrication de ces capteurs peut être associée à la fabrication de modules solaires hybrides (PVT) d'une capacité équivalente ;</p>
<p>2° La fabrication du polysilicium de qualité photovoltaïque, des lingots de silicium de qualité photovoltaïque, des plaquettes photovoltaïques, du verre solaire, des traqueurs solaires, y compris pilotables, des structures porteuses spécifiques aux traqueurs et des onduleurs ;</p>
<p>3° L'extraction, la production, la transformation et la valorisation des matières premières critiques mentionnées au c du 2° du A du II de l'article 244 quater I du code général des impôts, à savoir le silicium, le germanium et le cuivre.</p>
''',
    "Réécriture à droit constant : le 1° distingue la filière photovoltaïque de la fabrication des capteurs thermiques destinés aux modules hybrides et explicite les associations de fabrication possibles. Les listes techniques des 2° et 3° sont intégralement conservées. Aucune réforme de fond des investissements éligibles n'est proposée.",
    "Le 1° source contient l'accord défectueux « qui peuvent être associée », dont l'antécédent est ambigu. La proposition rattache la seconde faculté d'association à la fabrication des capteurs thermiques ; cette clarification syntaxique est à contrôler au regard du dispositif d'origine. La destination obligatoire de ces capteurs aux modules hybrides et les deux conditions de capacité équivalente sont conservées. Aucune condition de même site, propre à l'article 23 M bis, n'est ajoutée ici. Le polysilicium et les lingots gardent leur qualification de qualité photovoltaïque ; les trois matières premières restent le silicium, le germanium et le cuivre.")


assert len(sources) == len(drafts) == 24
assert set(drafts) == {s['number'] for s in sources}
Path('fragments').mkdir(exist_ok=True)
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    filename = re.sub(r'\s+', '_', source['number']) + '.xml'
    Path('fragments', filename).write_text(xml + '\n')
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles ; {sum(len(a["proposed_xml"]) for a in answer)} caractères XML proposés')
