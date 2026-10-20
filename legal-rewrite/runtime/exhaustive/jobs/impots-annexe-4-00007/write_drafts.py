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


add('30-0 I', '''
<p>Pour les logements faisant l'objet de l'opération d'acquisition-amélioration prévue au b du 5° de l'article 279-0 bis A du code général des impôts, l'amélioration de la performance énergétique doit satisfaire aux conditions suivantes :</p>
<p>I. - Pour un logement situé en France métropolitaine, le bénéficiaire doit justifier qu'après les travaux d'amélioration, le logement relève de l'une des classes suivantes, au sens de l'article L. 173-1-1 du code de la construction et de l'habitation :</p>
<p>1° De la classe A ou B, lorsque le logement relevait de la classe D avant les travaux ;</p>
<p>2° De la classe A, B ou C, lorsque le logement relevait de la classe E, F ou G avant les travaux.</p>
<p>II. - Pour un logement situé dans les départements et régions d'outre-mer, le bénéficiaire doit justifier de la réalisation d'au moins un geste de travaux sur l'enveloppe du bâti et d'au moins un geste de travaux sur les équipements contribuant significativement aux économies d'énergie et, indirectement, à la réduction des émissions de gaz à effet de serre. Ces travaux doivent respecter les critères suivants :</p>
<p>1° Travaux sur l'enveloppe du bâti :</p>
<table><tbody>
<tr><th></th><th>Geste</th><th>Critères de performance</th></tr>
<tr><td rowspan="6">Toiture</td><td>Exigence globale</td><td>Sur l'ensemble de la toiture, facteur solaire Smax ≤ 0,03.</td></tr>
<tr><td rowspan="2">Pose d'une isolation</td><td>Si le logement est situé à une altitude inférieure ou égale à 600 m : résistance thermique R ≥ 1,5 m2. K/ W sur l'ensemble de la toiture.</td></tr>
<tr><td>Si le logement est situé à une altitude supérieure à 600 m : résistance thermique R ≥ 2,5 m2. K/ W sur l'ensemble de la toiture.</td></tr>
<tr><td>Mise en place d'une surtoiture</td><td>La surtoiture doit être ventilée et couvrir l'ensemble du plancher haut.</td></tr>
<tr><td>Remplacement des éléments de couverture</td><td>La couverture doit être de couleur claire ou moyenne sur la totalité de la toiture.</td></tr>
<tr><td>Hauts de La Réunion uniquement : exigence globale</td><td>Sur l'ensemble de la toiture, coefficient de transmission surfacique U ≤ 0,5 W/ m2. K.</td></tr>
<tr><td rowspan="5">Murs</td><td>Exigence globale</td><td>Pour tous les murs des pièces principales en contact avec l'extérieur, facteur solaire Smax ≤ 0,09.</td></tr>
<tr><td>Mise en place d'un bardage ventilé</td><td>Le bardage ventilé doit être ajouté sur au moins 50 % des parois.</td></tr>
<tr><td>Pose d'une isolation des murs donnant sur l'extérieur</td><td>Sur au moins 50 % des murs, résistance thermique R ≥ 0,5 m2. K/ W.</td></tr>
<tr><td>Mise en place de pare-soleil</td><td>Les débords doivent protéger au moins 50 % des parois. Le rapport d/ h entre le débord du pare-soleil (d) et sa hauteur (h) doit être ≥ 0,2.</td></tr>
<tr><td>Hauts de La Réunion uniquement : exigence globale</td><td>Sur l'ensemble des parois donnant sur l'extérieur, coefficient de transmission surfacique U ≤ 0,5 W/ m2. K.</td></tr>
<tr><td rowspan="2">Baies</td><td>Exigence globale</td><td>Le facteur solaire Smax doit être ≤ 0,8.</td></tr>
<tr><td>Hauts de La Réunion uniquement : changement de fenêtres, de portes-fenêtres et de fenêtres de toit</td><td>Le coefficient de transmission surfacique Uw doit être ≤ 3 W/ (m2. K).</td></tr>
</tbody></table>
<p>2° Travaux sur les équipements contribuant significativement aux économies d'énergie et, indirectement, à la réduction des émissions de gaz à effet de serre :</p>
<table><tbody>
<tr><th></th><th>Intervention</th><th>Exigences</th></tr>
<tr><td rowspan="5">Ventilation</td><td>Amélioration de la ventilation naturelle</td><td>Installer des ouvrants mobiles, des baies à galandage ou toute autre solution technique équivalente.<p>Chaque baie doit présenter une surface ouvrante supérieure à celle existant avant les travaux. Cette surface doit être modulable par des systèmes de fixation : dispositifs de blocage de la position ouverte par baïonnette, vérin ou autre système équivalent.</p></td></tr>
<tr><td rowspan="4">Mise en place ou remplacement de ventilateurs de plafond</td><td>Les brasseurs d'air plafonniers doivent être fixes, à pales, et remplir cumulativement les conditions suivantes :</td></tr>
<tr><td>(i) Avoir un diamètre d'au moins 1,32 mètre ;</td></tr>
<tr><td>(ii) Disposer d'au moins trois vitesses de fonctionnement ;</td></tr>
<tr><td>(iii) Présenter un niveau sonore inférieur ou égal à 45 dB (A) à vitesse maximale et inférieur ou égal à 35 dB (A) à vitesse minimale.</td></tr>
<tr><td rowspan="5">Eau chaude sanitaire</td><td rowspan="5">Installation ou remplacement de chauffe-eau solaire</td><td>Lorsque le système est soumis à l'étiquetage obligatoire issu du règlement délégué n° 12/2013, son efficacité énergétique pour le chauffage de l'eau doit atteindre les valeurs suivantes :</td></tr>
<tr><td>Pour le profil de soutirage M : ≥ 65 % ;</td></tr>
<tr><td>Pour le profil de soutirage L : ≥ 75 % ;</td></tr>
<tr><td>Pour le profil de soutirage XL : ≥ 80 % ;</td></tr>
<tr><td>Pour le profil de soutirage XXL : ≥ 85 %.</td></tr>
<tr><td rowspan="3">Aération</td><td>Ajout ou remplacement d'une ventilation mécanique contrôlée dans les pièces d'eau aveugles</td><td>Installer une ventilation mécanique contrôlée (VMC) simple flux autoréglable ou hygroréglable de type A ou B.</td></tr>
<tr><td>Hauts de La Réunion uniquement : ajout ou remplacement d'une ventilation</td><td rowspan="2">Installer une ventilation mécanique contrôlée (VMC) simple flux autoréglable ou hygroréglable de type A ou B.</td></tr>
<tr><td>mécanique contrôlée</td></tr>
<tr><td rowspan="2">Chauffage</td><td>Hauts de La Réunion uniquement : ajout ou remplacement du système de chauffage</td><td>Installer une chaudière à haute performance énergétique, une PAC, une chaudière ou un poêle à bois, ou un équipement de chauffage fonctionnant à l'énergie solaire.</td></tr>
<tr><td>Hauts de La Réunion uniquement : calorifugeage de l'installation de production ou de distribution de chauffage ou d'eau chaude sanitaire</td><td>Utiliser un isolant de classe supérieure ou égale à 1, telle que définie dans la norme NF EN 12828 + A1 mai 2014.</td></tr>
</tbody></table>
<p>Au sens du présent II, les logements situés dans les Hauts de La Réunion sont ceux qui se trouvent à La Réunion à une altitude supérieure à 600 mètres.</p>
<p>III. - Sur simple demande de l'administration, le bénéficiaire doit produire les justificatifs suivants :</p>
<p>1° Pour les logements mentionnés au I :</p>
<p>a) Avant la réalisation des travaux, un audit énergétique du bâtiment ou de la partie de bâtiment, réalisé conformément à l'article 8 de l'arrêté du 17 novembre 2020 relatif aux caractéristiques techniques et modalités de réalisation des travaux et prestations dont les dépenses sont éligibles à la prime de transition énergétique. Cet audit doit justifier qu'avant les travaux, le bâtiment ou la partie de bâtiment relève de la classe D, E, F ou G au sens de l'article L. 173-1-1 du code de la construction et de l'habitation ;</p>
<p>b) Après les travaux :</p>
<p>- soit une attestation de réalisation des travaux proposés dans l'audit pour atteindre le niveau de performance mentionné au I, accompagnée des factures ou notes des entreprises prestataires, ou tout autre moyen de preuve ;</p>
<p>- soit un diagnostic de performance énergétique du bâtiment ou de la partie de bâtiment, mentionné à l'article L. 126-26 du code de la construction et de l'habitation. Ce diagnostic doit satisfaire aux dispositions de l'arrêté du 31 mars 2021 relatif au diagnostic de performance énergétique pour les bâtiments ou parties de bâtiments à usage d'habitation en France métropolitaine et justifier que le niveau de performance mentionné au I est atteint ;</p>
<p>2° Pour les logements mentionnés au II, les factures ou notes des entreprises prestataires, ou tout autre moyen de preuve permettant d'établir la réalisation d'au moins deux gestes de travaux prévus au même II.</p>
''',
"Réécriture à droit constant des conditions de performance et des obligations de justification : le bénéficiaire et les moments de production des justificatifs sont explicités. Les deux tableaux sont intégralement repris avec leurs critères reformulés en exigences lisibles. Les mesures de policy.json ne modifient pas ce régime de TVA ; aucune voie de rénovation locative de vingt-quatre mois n'y est introduite.",
"Conserver les I à III, les 1° et 2°, les a et b et les deux branches du III, 1°, b. Tous les seuils, unités, profils et restrictions aux Hauts de La Réunion sont maintenus, ainsi que la distinction entre un geste sur l'enveloppe et un geste sur les équipements. La référence source au règlement délégué n° 12/2013 pour l'étiquetage appelle une vérification ; elle est conservée sans substitution conjecturale. La cellule relative à la VMC dans les Hauts de La Réunion est répartie sur deux lignes dans la source ; cette structure est conservée. Le III, 1°, a conserve l'ambiguïté source entre un audit préalable et sa production sur demande, sans créer un dépôt systématique préalable. La note historique renvoie à l'article 1er de l'arrêté du 5 juillet 2024, JO du 10 ; elle ne fixe aucune date de réforme nouvelle. La rénovation locative proposée relève notamment de la loi n° 89-462 et ne résulte pas du présent article.")

add('30', '''
<p>1. Pour appliquer le a de l'article 279 du code général des impôts, la base soumise au taux réduit de la taxe sur la valeur ajoutée correspond aux trois quarts du prix de pension ou de demi-pension.</p>
<p>2. Pour le calcul prévu au 1, les prix de pension et de demi-pension sont, le cas échéant, retenus après déduction de la fraction correspondant aux prestations autres que la nourriture et le logement.</p>
<p>3 et 4. (Abrogés).</p>
''',
"Réécriture à droit constant : la règle des trois quarts et la déduction préalable des prestations étrangères à la nourriture et au logement sont exprimées en deux étapes, sans modification de l'assiette ni du taux applicable.",
"Les subdivisions 1, 2 et 3 et 4 sont maintenues. La quotité des trois quarts et le renvoi au a de l'article 279 sont conservés ; aucun taux chiffré n'est ajouté. Aucune réforme de fond de policy.json ne vise cette règle.")

add('32', '''
<p>a. Sous réserve des règles propres aux entreprises étrangères qui n'ont pas d'établissement en France, les redevables de la taxe sur la valeur ajoutée doivent souscrire les déclarations prescrites par l'article 286 et le 1 de l'article 287 du code général des impôts auprès du service de gestion désigné par les dispositions de la section 4 du chapitre Ier du titre VI du livre Ier de la partie réglementaire du code des impositions sur les biens et services. Ces déclarations portent sur l'ensemble de leurs opérations, à l'exception de celles mentionnées au 2° du 3 du I de l'article 257 du code général des impôts.</p>
<p>b. (Abrogé).</p>
<p>c. Alinéas périmés.</p>
''',
"Réécriture à droit constant : l'obligation déclarative, le service compétent et le périmètre des opérations sont distingués au sein du a. La réserve relative aux entreprises étrangères et l'exclusion d'opérations sont conservées ; aucune réforme de fond n'est introduite.",
"Les a, b et c restent à leur place. Les références aux articles 286, 287, 257 et au code des impositions sur les biens et services sont conservées. La note source rattache la rédaction aux articles 9-4° et 51-I du décret n° 2024-610 du 26 juin 2024 ; elle n'est pas une disposition d'entrée en vigueur d'une nouvelle réforme. Coordination avec l'article 35 proposé : ce dernier confie au service recevant les déclarations la transmission au service local, sans supprimer la déclaration initiale ni les règles propres aux entreprises étrangères. La note de l'article 286 consulté dans le corpus prévoit une recodification à compter du 1er janvier 2027, avec maintien de certaines dispositions jusqu'à leur reprise réglementaire ; le maintien des renvois devra être contrôlé lors de cette reprise, sans l'anticiper ici.")

add('35', '''
<p>Les redevables de la taxe sur la valeur ajoutée doivent souscrire les déclarations prévues aux 1° et 2° du I de l'article 286 du code général des impôts chaque fois que les conditions d'exercice de leur activité sont substantiellement modifiées.</p>
<p>Cette obligation s'applique notamment :</p>
<p>Lors de l'ouverture d'un établissement secondaire, d'une agence ou d'une succursale. Le service qui reçoit les déclarations en application de l'article 32 doit les transmettre au service dans le ressort duquel se situe cet établissement, cette agence ou cette succursale. Cette transmission tient lieu de déclaration auprès de ce dernier service, sans nouveau dépôt des mêmes informations par le redevable. Les rectifications communiquées par le redevable au service qui a reçu la déclaration sont également transmises au service destinataire. Ces transmissions sont effectuées dans le respect des secrets légalement protégés ;</p>
<p>Lors de toute modification de la forme juridique de l'entreprise.</p>
''',
"A droit constant, l'obligation de déclarer les modifications substantielles et ses deux exemples non exhaustifs sont rendus plus lisibles. Réforme de fond au troisième alinéa, en application de l'objectif de policy.json de supprimer les demandes en double et de corriger les données à la source : le second dépôt de la même déclaration d'ouverture est remplacé par une transmission obligatoire entre les services fiscaux. Les rectifications suivent le même circuit ; les secrets protégés sont maintenus.",
"Les quatre alinéas restent dans le même ordre ; la réforme est insérée dans l'alinéa qui imposait déjà la déclaration au service du nouvel établissement. Le renvoi aux 1° et 2° du I de l'article 286 est conservé ; le renvoi à l'article 32, existant et vérifié dans le lot, désigne le circuit de réception. Le redevable reste tenu de déclarer l'ouverture et toute autre modification substantielle ; seuls les dépôts répétés des mêmes informations auprès du second service sont supprimés. Le service local reçoit la déclaration et ses rectifications, sans dispense de contrôle ni levée du secret. Le droit de rectifier n'est pas réservé à ce seul circuit. La mise en œuvre appelle l'adaptation des formulaires et des échanges internes de la DGFiP, sans nouveau portail, délai ou date de promulgation inventés. L'article 286 a été lu dans le corpus public local : sa note annonce une recodification à compter du 1er janvier 2027 assortie de maintiens jusqu'à reprise réglementaire ; coordonner alors le support de cette obligation et les renvois à ses dispositions, sans supprimer par anticipation celles encore applicables.")

add('36', '''
<p>Lorsqu'un redevable de la taxe sur la valeur ajoutée cesse son activité, il doit déclarer cette cessation dans les trente jours au service qui a reçu les déclarations mentionnées à l'article 32.</p>
''',
"Réécriture à droit constant : la cessation d'activité est placée en tête de la phrase et le redevable, le délai et le destinataire de la déclaration sont expressément identifiés. Aucune réforme de fond.",
"Délai de trente jours et renvoi à l'article 32 conservés. Aucun point de départ distinct de la cessation ni dispense de déclaration ne sont ajoutés.")

add('37', '''
<p>La comptabilité ou le livre spécial prescrit au 3° du I de l'article 286 du code général des impôts doit notamment présenter séparément les éléments suivants :</p>
<p>Les opérations qui ne sont pas soumises à la taxe sur la valeur ajoutée ;</p>
<p>Les opérations réalisées en suspension de cette taxe ;</p>
<p>Pour chaque acquisition de biens, de services et de travaux : son montant, la taxe sur la valeur ajoutée correspondante, ainsi que le nom et l'adresse du fournisseur ;</p>
<p>Pour chaque opération ayant donné lieu à une facture ou à un document en tenant lieu qui mentionne la taxe sur la valeur ajoutée : le montant net de l'opération, le montant de la taxe facturée au taux exigible, ainsi que le nom et l'adresse du client.</p>
''',
"Réécriture à droit constant : la présentation séparée des catégories d'opérations et des informations à enregistrer est clarifiée, avec une liste de même portée. Aucune information comptable n'est supprimée ni ajoutée et aucune réforme de fond n'est appliquée.",
"Les cinq alinéas logiques sont conservés. Maintien du caractère non exhaustif de la liste, du renvoi au 3° du I de l'article 286 et de la distinction entre opérations non soumises et opérations en suspension de TVA. Le montant de TVA reste celui facturé au taux exigible.")

add('39', '''
<p>Les dates limites de déclaration et de paiement mentionnées aux 1 et 3 de l'article 287 du code général des impôts sont fixées selon les conditions prévues à l'article D. 161-11 du code des impositions sur les biens et services et à la section 5 du chapitre Ier du titre VI du livre Ier de la partie réglementaire de ce même code.</p>
''',
"Réécriture à droit constant : la notion d'échéances est exprimée comme les dates limites de déclaration et de paiement, en conservant l'intégralité des textes qui en déterminent les conditions. Aucune réforme de fond.",
"Les deux fondements du calendrier demeurent cumulatifs : article D. 161-11 et section 5 du chapitre Ier du titre VI du livre Ier de la partie réglementaire du code des impositions sur les biens et services. La note source fixe l'entrée en vigueur au 1er janvier 2025 en application de l'article 51 du décret n° 2024-610 du 26 juin 2024 ; cette date historique n'est pas transposée à une réforme future.")

add('40', '''
<p>1. Sur la déclaration prévue au 1 de l'article 287 du code général des impôts, les assujettis à la taxe sur la valeur ajoutée doivent indiquer le coefficient de taxation qu'ils appliquent pendant l'année en cours. Ce coefficient est calculé dans les conditions prévues au 3 du III de l'article 206 de l'annexe II au code général des impôts.</p>
<p>2. Les entreprises soumises aux dispositions du 2° du 3 du III de l'article 206 de l'annexe II au code général des impôts doivent déclarer cette situation au service des impôts dans les quinze jours.</p>
<p>Les entreprises assujetties à la taxe sur la valeur ajoutée doivent, dans les mêmes conditions, déclarer les modifications qui entraînent la création d'un secteur exonéré.</p>
''',
"Réécriture à droit constant : la mention du coefficient appliqué et son mode de calcul sont distingués, et l'objet de la déclaration prévue au 2 est rendu explicite. Le délai et l'obligation relative aux secteurs exonérés sont conservés. Aucune réforme de fond.",
"Subdivisions 1 et 2 et troisième alinéa maintenus. Délai de quinze jours et renvois au 1 de l'article 287, au 3 du III et au 2° du 3 du III de l'article 206 de l'annexe II conservés. Aucun point de départ supplémentaire du délai n'est ajouté à la source.")

add('41', '''
<p>Les entreprises doivent déclarer le coefficient de taxation qu'elles retiennent à titre provisoire pour les biens et services mentionnés au 3 du III de l'article 206 de l'annexe II au code général des impôts. Elles le déclarent à l'appui de la déclaration prévue au 1 de l'article 287 du code général des impôts, qu'elles déposent avant le 25 du mois suivant celui de leur création ou de leur prise de position d'assujetties.</p>
''',
"Réécriture à droit constant : l'obligation de déclarer le coefficient provisoire est énoncée avant son support et son échéance, dans le même alinéa. Aucune réforme de fond ni modification du champ des biens et services.",
"Un seul alinéa est conservé, avec l'échéance strictement antérieure au 25, et non au plus tard le 25. Les deux événements visés, création et prise de position d'assujetties, ainsi que les renvois aux articles 206 de l'annexe II et 287 du CGI restent inchangés.")

add('41-0 bis', '''
<p>1. Pour chaque membre constitué en secteur distinct d'activité conformément au 6° du I de l'article 209 de l'annexe II au code général des impôts, l'assujetti unique mentionné à l'article 256 C du même code doit communiquer à l'administration les informations suivantes, sur un formulaire annexé à sa déclaration de chiffre d'affaires :</p>
<p>a) Les informations de la déclaration prévue au 1 de l'article 287 du code général des impôts, ainsi que les coefficients de taxation mentionnés aux articles 40 et 41 ;</p>
<p>b) Le montant total du chiffre d'affaires correspondant aux livraisons de biens et aux prestations de services que le membre réalise au bénéfice d'autres membres de l'assujetti unique et qui auraient été imposables à la taxe sur la valeur ajoutée en l'absence d'assujetti unique.</p>
<p>2. Le représentant de l'assujetti unique doit transmettre à l'administration le formulaire mentionné au 1 dans les mêmes délais et selon les mêmes modalités que la déclaration prévue au 1 de l'article 287 du code général des impôts.</p>
''',
"Réécriture à droit constant : les informations sont présentées sous les mêmes lettres et la transmission est attribuée explicitement au représentant de l'assujetti unique. Le périmètre contrefactuel du chiffre d'affaires interne est conservé. Aucune réforme de fond.",
"Maintien des 1, a, b et 2 et de tous les renvois, notamment aux coefficients des articles 40 et 41. La note source prévoit l'entrée en vigueur au 1er janvier 2023 selon l'article 2 de l'arrêté du 22 septembre 2022, NOR ECOE2225510A ; aucune nouvelle date n'est déduite de cette note.")

add('41 bis', '''
<p>Le registre des biens prévu au 1 du I de l'article 286 quater du code général des impôts doit permettre d'identifier l'expédition ou le transport de biens vers le territoire d'un autre Etat membre de la Communauté européenne, lorsque ces biens y sont destinés à une utilisation temporaire ou à des travaux dans les conditions prévues aux a et b du III de l'article 256 du code général des impôts. A cette fin, il comporte les mentions suivantes :</p>
<p>a) La désignation des biens ou matériaux ;</p>
<p>b) Leur quantité, exprimée en poids, en volume ou en unités ;</p>
<p>c) Leur lieu de destination ;</p>
<p>d) La date de l'expédition ou du transport ;</p>
<p>e) La date de leur retour ;</p>
<p>f) La nature de l'opération ;</p>
<p>g) Le cas échéant, le numéro d'assujetti à la taxe sur la valeur ajoutée qui identifie le prestataire établi dans un autre Etat membre auquel les biens ont été expédiés en vue de travaux.</p>
''',
"Réécriture à droit constant : la finalité d'identification du registre est séparée de l'énumération de ses mentions, et les biens auxquels se rapportent les données sont explicités. Aucune réforme de fond.",
"Les lettres a à g, la condition propre au g et les renvois au 1 du I de l'article 286 quater et aux a et b du III de l'article 256 sont conservés. La dénomination historique Communauté européenne est maintenue sans élargissement territorial ni modification des régimes d'utilisation temporaire et de travaux.")

add('41 bis A', '''
<p>Dans le régime des stocks sous contrat de dépôt, le registre des biens prévu au 2 du I de l'article 286 quater du code général des impôts doit comporter les informations suivantes, selon la personne qui le tient :</p>
<p>1° Pour le registre tenu par l'assujetti qui transfère les biens :</p>
<p>a) L'indication que le bien est expédié ou transporté à partir du territoire métropolitain, ainsi que la date de cette expédition ou de ce transport ;</p>
<p>b) Le numéro d'identification à la taxe sur la valeur ajoutée de l'assujetti destinataire des biens, attribué par l'Etat membre vers lequel les biens sont expédiés ou transportés ;</p>
<p>c) L'Etat membre de destination de l'expédition ou du transport, le numéro d'identification à la taxe sur la valeur ajoutée attribué à l'entrepositaire par cet Etat, la date d'arrivée des biens dans l'entrepôt et l'adresse de l'entrepôt où ils sont stockés à leur arrivée ;</p>
<p>d) La valeur des biens arrivés dans l'entrepôt, leur description et leur quantité ;</p>
<p>e) Le cas échéant, le numéro d'identification à la taxe sur la valeur ajoutée de l'assujetti qui remplace l'assujetti auquel les biens sont destinés, dans les conditions prévues au 4 du III bis de l'article 256 du code général des impôts. Ce numéro est celui attribué par l'Etat membre vers lequel les biens sont expédiés ou transportés ;</p>
<p>f) Le montant imposable, la description et la quantité des biens livrés, la date de la livraison des biens mentionnés au 3° du I de l'article 262 ter du même code, ainsi que le numéro d'identification à la taxe sur la valeur ajoutée de l'acquéreur ;</p>
<p>g) Le montant imposable, la description et la quantité des biens, la date à laquelle survient l'une des conditions mentionnées au 5 du III bis de l'article 256 du code général des impôts, ainsi que la justification correspondante ;</p>
<p>h) La valeur, la description et la quantité des biens renvoyés mentionnés au 3 du III bis du même article 256, ainsi que la date de leur renvoi ;</p>
<p>2° Pour le registre tenu par l'assujetti auquel les biens sont destinés à être livrés :</p>
<p>a) Le numéro individuel d'identification à la taxe sur la valeur ajoutée, mentionné à l'article 286 ter du code général des impôts, de l'assujetti qui transfère les biens sous le régime des stocks sous contrat de dépôt ;</p>
<p>b) La description des biens qui lui sont destinés et leur quantité ;</p>
<p>c) La date d'arrivée dans l'entrepôt des biens qui lui sont destinés ;</p>
<p>d) Le montant imposable, la description et la quantité des biens qui lui sont livrés, ainsi que la date de leur acquisition intracommunautaire, conformément au deuxième alinéa du 3° du I de l'article 256 bis du même code ;</p>
<p>e) La description et la quantité des biens enlevés de l'entrepôt sur ordre de l'assujetti qui les transfère sous le régime des stocks sous contrat de dépôt, ainsi que la date de cet enlèvement ;</p>
<p>f) La description et la quantité des biens détruits ou manquants, ainsi que la date de destruction, de perte ou de vol des biens précédemment arrivés à l'entrepôt, ou la date à laquelle leur destruction ou leur absence a été constatée.</p>
<p>Lorsque les biens sont expédiés ou transportés sous le régime des stocks sous contrat de dépôt chez un entrepositaire autre que l'assujetti auquel ils sont destinés à être livrés, le registre de cet assujetti ne doit pas comporter les informations mentionnées aux c, e et f du présent 2° ;</p>
<p>3° Pour le registre tenu par l'entrepositaire des biens, lorsque celui-ci est distinct de l'assujetti auquel les biens sont destinés à être livrés :</p>
<p>a) L'Etat membre de départ de l'expédition ou du transport des biens ;</p>
<p>b) La date d'arrivée dans l'entrepôt des biens destinés à être livrés à l'assujetti ;</p>
<p>c) Le numéro individuel d'identification à la taxe sur la valeur ajoutée, mentionné à l'article 286 ter du code général des impôts, de l'assujetti destinataire des biens. Ce numéro est celui attribué par l'Etat membre vers lequel les biens sont expédiés ou transportés ;</p>
<p>d) La description et la quantité des biens arrivés dans l'entrepôt, ainsi que la date de leur enlèvement sur ordre de l'assujetti qui les transfère sous le régime des stocks sous contrat de dépôt ;</p>
<p>e) La description et la quantité des biens détruits ou manquants, ainsi que la date de destruction, de perte ou de vol des biens précédemment arrivés à l'entrepôt, ou la date à laquelle leur destruction ou leur absence a été constatée.</p>
''',
"Réécriture à droit constant : chaque registre est rattaché explicitement à celui qui le tient, les données de départ, d'arrivée, de livraison et de renvoi sont exprimées plus directement, et les numéros attribués par l'Etat de destination sont précisés dans la même subdivision. L'exclusion des mentions c, e et f dans le cas d'un entrepositaire distinct reste impérative. Aucune réforme de fond.",
"Les trois ensembles et toutes leurs lettres sont conservés : 1° a à h, 2° a à f et son alinéa d'exclusion, 3° a à e. Maintien des renvois aux articles 286 quater, 286 ter, 256, 256 bis et 262 ter, avec leurs subdivisions exactes. Les informations de valeur et de montant imposable, ainsi que les dates réelles ou de constatation de destruction, perte ou vol, restent distinctes. Le découpage en p reprend les alinéas matérialisés par les br de la source, sans changer l'ordre des mentions.")

add('41 ter', '''
<p>Pour chaque donneur d'ordre, la nature et les quantités de matériaux et de produits transformés mentionnées au 1 du II de l'article 286 quater du code général des impôts, relatif au registre spécial des façonniers, doivent être appréciées à leur date d'entrée et à leur date de sortie. Le registre doit indiquer les stocks détenus à l'issue de ces opérations.</p>
<p>Lorsque des biens destinés à un travail à façon sont expédiés à partir d'un autre Etat membre de la Communauté européenne par un assujetti identifié à la taxe sur la valeur ajoutée dans cet Etat, ou pour son compte, le registre mentionné au premier alinéa doit comporter le numéro d'identification à la taxe sur la valeur ajoutée du donneur d'ouvrage.</p>
''',
"Réécriture à droit constant : les moments d'appréciation des quantités et la mention des stocks sont formulés séparément, et l'expédition par l'assujetti ou pour son compte est rendue plus lisible. Aucune réforme de fond.",
"Deux alinéas conservés, avec le renvoi au premier alinéa et au 1 du II de l'article 286 quater. Les termes donneur d'ordre et donneur d'ouvrage, distincts dans la source, sont maintenus. L'identification TVA dans l'Etat de départ reste une condition de la seconde obligation.")

add('41 quater', '''
<p>Les registres mentionnés au 3 du II de l'article 286 quater du code général des impôts et aux articles 41 bis et 41 ter doivent être tenus sur papier ou sur support informatique et être identifiés. Ils doivent retracer, dans l'ordre chronologique des opérations, les mouvements des biens, matériaux et produits transformés.</p>
<p>Les informations enregistrées doivent être conservées dans leur contenu d'origine.</p>
<p>Les registres doivent être conservés dans chaque établissement, lieu de dépôt ou lieu de stockage des biens, matériaux ou produits transformés.</p>
<p>Les modalités et les délais de conservation sont ceux prévus à l'article L. 102 B du livre des procédures fiscales.</p>
''',
"Réécriture à droit constant : les exigences de support, d'identification, de chronologie, d'intégrité et de conservation sont exprimées comme des obligations distinctes. Aucun nouveau support, délai ou lieu de conservation n'est institué.",
"Les quatre alinéas et les renvois aux articles 286 quater, 41 bis, 41 ter et L. 102 B sont maintenus. La source ne vise pas expressément l'article 41 bis A ; aucune extension silencieuse du champ des registres n'est opérée. Aucune réforme de fond de policy.json ne modifie ici l'archivage.")

add('41 quinquies', '''
<p>Sur toute demande d'un agent de l'administration, les registres mentionnés au 3 du II de l'article 286 quater du code général des impôts et aux articles 41 bis et 41 ter doivent lui être présentés. Cet agent peut en obtenir copie.</p>
<p>A la demande de l'administration, les registres tenus sur support informatique doivent être restitués sur papier.</p>
<p>(Abrogé).</p>
''',
"Réécriture à droit constant : le pouvoir de demander les registres et celui d'en obtenir copie sont exprimés en deux phrases, sans modifier leur portée. La restitution sur papier reste subordonnée à la demande de l'administration. Aucune réforme de fond.",
"Les trois alinéas, y compris la mention finale d'abrogation, sont conservés. La source vise 41 bis et 41 ter, sans mention expresse de 41 bis A ; ce périmètre est maintenu. La note source rend ces dispositions applicables aux opérations dont le fait générateur de TVA intervient à compter du 1er juillet 2021, selon l'article 2 de l'arrêté du 31 mai 2021, NOR CCPE2112747A. Ce critère temporel n'est pas remplacé par une date de dépôt ou de paiement.")

add('41 quinquies A', '''
<p>Pour chaque opération, les registres prévus au 9 de l'article 298 sexdecies F et au X de l'article 298 sexdecies G du code général des impôts doivent indiquer :</p>
<p>a) L'Etat membre de consommation où les biens sont livrés ou les services fournis ;</p>
<p>b) Le type de services fournis ou la description et la quantité des biens livrés ;</p>
<p>c) La date de livraison des biens ou de fourniture des services ;</p>
<p>d) La base d'imposition et la devise dans laquelle elle est exprimée ;</p>
<p>e) Chaque augmentation ou réduction ultérieure de cette base ;</p>
<p>f) Le taux de taxe sur la valeur ajoutée appliqué ;</p>
<p>g) Le montant de taxe sur la valeur ajoutée dû et la devise dans laquelle il est exprimé ;</p>
<p>h) La date et le montant des paiements reçus ;</p>
<p>i) Tout acompte reçu avant la livraison des biens ou la fourniture des services ;</p>
<p>j) Si une facture est émise, les informations qu'elle contient ;</p>
<p>k) Pour les services, les informations utilisées pour déterminer le lieu où le preneur est établi, a son domicile ou réside habituellement ; pour les biens, les informations utilisées pour déterminer les lieux de départ et d'arrivée de l'expédition ou du transport à destination de l'acquéreur ;</p>
<p>l) Tout élément de preuve relatif à un éventuel retour des biens, y compris la base d'imposition et le taux de taxe sur la valeur ajoutée appliqué.</p>
<p>L'assujetti doit transmettre ces registres à l'administration par voie électronique dans un délai de vingt jours à compter de la date de la demande. S'il ne les a pas transmis dans ce délai de vingt jours, l'administration lui rappelle par voie électronique son obligation de les présenter.</p>
''',
"Réécriture à droit constant : les données de chaque opération sont présentées dans des alinéas identifiés, avec des formulations plus directes pour les devises, les factures et la localisation. L'assujetti est explicitement tenu de transmettre les registres et la relance reste électronique. Aucune réforme de fond.",
"Lettres a à l et alinéa final conservés dans l'ordre. Les mentions d'acompte, de corrections de base et d'éléments de preuve de retour sont intégralement maintenues. Délai de vingt jours et renvois au 9 de l'article 298 sexdecies F et au X de l'article 298 sexdecies G inchangés. La note source conserve l'application aux faits générateurs de TVA intervenant à compter du 1er juillet 2021, selon l'article 2 de l'arrêté du 31 mai 2021, NOR CCPE2112747A ; aucune date nouvelle n'est créée.")

add('41 quinquies B', '''
<p>Pour chaque opération, le registre prévu au X de l'article 298 sexdecies H du code général des impôts doit indiquer :</p>
<p>a) L'Etat membre de consommation où les biens sont livrés ;</p>
<p>b) La description des biens livrés et leur quantité ;</p>
<p>c) La date de livraison des biens ;</p>
<p>d) La base d'imposition et la devise dans laquelle elle est exprimée ;</p>
<p>e) Chaque augmentation ou réduction ultérieure de cette base ;</p>
<p>f) Le taux de taxe sur la valeur ajoutée appliqué ;</p>
<p>g) Le montant de taxe sur la valeur ajoutée dû et la devise dans laquelle il est exprimé ;</p>
<p>h) La date et le montant des paiements reçus ;</p>
<p>i) Si une facture est émise, les informations qu'elle contient ;</p>
<p>j) Les informations utilisées pour déterminer les lieux de départ et d'arrivée de l'expédition ou du transport des biens à destination de l'acquéreur ;</p>
<p>k) Une preuve relative à un éventuel retour des biens, y compris la base d'imposition et le taux de taxe sur la valeur ajoutée appliqué ;</p>
<p>l) Le numéro de commande ou le numéro unique de l'opération ;</p>
<p>m) Le numéro unique de l'envoi, lorsque l'assujetti intervient directement à la livraison.</p>
<p>L'assujetti doit transmettre ce registre à l'administration par voie électronique dans un délai de vingt jours à compter de la date de la demande. S'il n'a pas transmis les registres demandés dans ce délai de vingt jours, l'administration lui rappelle par voie électronique son obligation de présenter ce registre.</p>
''',
"Réécriture à droit constant : les mentions du registre sont ordonnées dans les mêmes subdivisions et les modalités de transmission sont exprimées par une obligation explicite de l'assujetti. Le numéro d'envoi reste conditionné à son intervention directe à la livraison. Aucune réforme de fond.",
"Lettres a à m maintenues. Ne pas importer la mention d'acompte du régime distinct de l'article 41 quinquies A. Maintien du X de l'article 298 sexdecies H, du délai de vingt jours et du rappel électronique. La note source vise les faits générateurs de TVA intervenant à compter du 1er juillet 2021, conformément à l'article 2 de l'arrêté du 31 mai 2021, NOR CCPE2112747A ; cette application temporelle est conservée.")

add('41 quinquies C', '''
<p>Pour chaque opération, le registre prévu à l'article 286 quinquies du code général des impôts doit indiquer :</p>
<p>1° Le nom, l'adresse postale et l'adresse électronique ou le site internet du fournisseur dont les opérations sont facilitées par l'interface électronique. Lorsque les données suivantes sont disponibles, il doit également indiquer :</p>
<p>a) Le numéro individuel d'identification à la taxe sur la valeur ajoutée du fournisseur ou prestataire, mentionné à l'article 286 ter du code général des impôts, ou, à défaut d'une telle identification, son numéro fiscal national ;</p>
<p>b) Son numéro de compte bancaire ou de compte virtuel ;</p>
<p>2° La description des biens, leur valeur, le lieu d'arrivée de leur expédition ou de leur transport, ainsi que le moment de leur livraison. Le numéro de commande ou le numéro unique de l'opération doit aussi figurer au registre, si ces données sont disponibles ;</p>
<p>3° La description des services, leur valeur et les informations permettant d'établir le lieu et le moment de la prestation. Le numéro de commande ou le numéro unique de l'opération doit aussi figurer au registre, si ces données sont disponibles.</p>
''',
"Réécriture à droit constant : les informations obligatoires sont distinguées de celles dont l'inscription dépend de leur disponibilité, au sein des mêmes subdivisions. Les alternatives d'identification et de coordonnées restent intactes. Aucune réforme de fond.",
"Maintien des 1°, a et b, 2° et 3° et des renvois aux articles 286 quinquies et 286 ter. Le numéro fiscal national ne se substitue au numéro TVA qu'à défaut d'identification TVA. Aucun délai de transmission des régimes voisins n'est ajouté. La note source prévoit l'application aux faits générateurs de TVA intervenant à compter du 1er juillet 2021, selon l'article 2 de l'arrêté du 31 mai 2021, NOR CCPE2112747A.")

add('41 quinquies D', '''
<p>Pour chaque opération, le registre prévu au VI de l'article 298 sexdecies I du code général des impôts doit indiquer :</p>
<p>a) Le nom et l'adresse de la personne physique à laquelle les biens sont destinés ;</p>
<p>b) La description des biens livrés et leur quantité ;</p>
<p>c) La date de livraison des biens ;</p>
<p>d) La base d'imposition définie à l'article 292 du code général des impôts et la devise dans laquelle elle est exprimée ;</p>
<p>e) Chaque augmentation ou réduction ultérieure de cette base ;</p>
<p>f) Une preuve relative à un éventuel retour des biens ;</p>
<p>g) Le montant de taxe sur la valeur ajoutée dû et la devise dans laquelle il est exprimé ;</p>
<p>h) La date à laquelle la taxe sur la valeur ajoutée a été reversée ;</p>
<p>i) Le numéro de la déclaration en douane de mise en libre pratique concernée.</p>
''',
"Réécriture à droit constant : les mentions sont formulées plus directement et la date à enregistrer au h est explicitement celle du reversement effectué. Aucune obligation de déclaration, aucun délai ni taux nouveau ne sont ajoutés.",
"Lettres a à i et renvois au VI de l'article 298 sexdecies I et à l'article 292 conservés. Le destinataire reste une personne physique ; la preuve de retour ne reçoit pas les mentions supplémentaires des régimes A ou B. La note source vise les faits générateurs de TVA intervenant à compter du 1er juillet 2021, conformément à l'article 2 de l'arrêté du 31 mai 2021, NOR CCPE2112747A.")

add('41 septies', '''
<p>Les entreprises qui utilisent un système de télétransmission des factures dans les conditions prévues à l'article 96 G de l'annexe III au code général des impôts doivent recourir à un système qui respecte les spécifications suivantes :</p>
<p>I. - Sont des utilisateurs les entreprises, fournisseurs ou clients qui émettent des factures télétransmises, eux-mêmes ou par l'intermédiaire d'un tiers ou d'un client mandaté à cet effet, ainsi que ceux qui reçoivent des factures télétransmises. La qualité d'utilisateur ne dépend pas de la personne qui a reçu les factures en leur nom et pour leur compte.</p>
<p>II. - Le système de télétransmission doit assurer au moins les fonctions suivantes :</p>
<p>a) Vérifier, à l'émission comme à la réception, que la structure du message est conforme aux mentions obligatoires d'une facture ;</p>
<p>b) Constituer chaque jour et archiver une liste récapitulative, séquentielle et exhaustive des messages émis et/ou reçus et des anomalies éventuellement détectées lors des contrôles ;</p>
<p>c) Archiver les factures émises et reçues ;</p>
<p>d) Restituer, à la demande de l'administration, la facture et la liste récapitulative sur écran ou sur tout support informatique, en langage clair ;</p>
<p>e) Permettre l'accès immédiat aux données dématérialisées lorsque l'administration le demande.</p>
<p>III. - 1. Les logiciels de télétransmission des factures peuvent utiliser une ou plusieurs structures de messages. Ils ne doivent ni les modifier ni les altérer.</p>
<p>Le message doit contenir toutes les mentions obligatoires d'une facture prévues par les dispositions législatives ou réglementaires en vigueur.</p>
<p>Des codes stables peuvent être utilisés, par exemple pour désigner des produits ou des personnes, à condition qu'ils soient déchiffrés automatiquement à l'aide d'une table de correspondance intégrée à la fonction de restitution.</p>
<p>2. A la demande de l'administration, les messages factures doivent pouvoir être restitués sur écran, sur support informatique ou sur papier. La restitution doit comprendre toutes les informations émises et reçues, obligatoires comme facultatives.</p>
<p>La restitution doit pouvoir être sélective, notamment selon les informations que la liste récapitulative doit contenir.</p>
<p>Les données doivent être restituées de manière lisible, en mode caractères et dans un langage clair et intelligible.</p>
<p>3. A l'émission comme à la réception, le système doit contrôler que la structure du message est conforme aux mentions obligatoires.</p>
<p>Si une anomalie est détectée à l'émission, le message rejeté ne doit être ni émis, ni archivé, ni inscrit sur la liste récapitulative.</p>
<p>Si une anomalie est détectée à la réception, elle doit être inscrite sur la liste récapitulative et les messages concernés doivent être archivés.</p>
<p>IV. - 1. La liste récapitulative mentionnée au III de l'article 96 G de l'annexe III au code général des impôts doit être constituée sous forme informatique au fur et à mesure de l'émission ou de la réception de chaque message.</p>
<p>Elle doit contenir au moins les informations suivantes :</p>
<p>a) Le numéro et la date de la facture ;</p>
<p>b) La date et l'heure de constitution du message ;</p>
<p>c) Les montants hors taxes et toutes taxes de la transaction, ainsi que le code monnaie si la facture n'est pas libellée en euros ;</p>
<p>d) Les éléments d'identification de l'émetteur ou du récepteur fournis par le système de télétransmission : code, nom ou dénomination sociale, numéro SIRET, adresse et qualité de fournisseur ou de client ;</p>
<p>e) Le libellé des anomalies éventuellement survenues lors de chaque transmission ;</p>
<p>f) La version du logiciel utilisé.</p>
<p>2. Abrogé.</p>
<p>V. - Les entreprises, fournisseurs et clients doivent constituer un fichier des partenaires avec lesquels ils échangent des factures par voie télématique.</p>
<p>Pour chaque partenaire, ce fichier doit indiquer :</p>
<p>a) Sa qualité d'émetteur et/ou de récepteur ;</p>
<p>b) L'archivage des factures sous forme dématérialisée ou sur papier ;</p>
<p>c) La ou les dates d'entrée dans la phase de dématérialisation avec ce partenaire et, le cas échéant, la ou les dates de sortie.</p>
<p>VI. - 1. Les messages factures émis par l'entreprise, par un tiers ou par un client mandaté à cet effet, ainsi que la liste récapitulative et le fichier des partenaires, doivent être accessibles et conservés dans leur forme et leur contenu d'origine, dans l'ordre chronologique de leur émission.</p>
<p>Les messages factures reçus, quelle que soit la personne qui les a reçus au nom et pour le compte de l'entreprise, ainsi que la liste récapitulative et le fichier des partenaires, doivent être accessibles et conservés dans leur forme et leur contenu d'origine, dans l'ordre chronologique de leur réception.</p>
<p>2. Le système de télétransmission doit alimenter automatiquement les fichiers informatiques qui conservent les messages factures, la liste récapitulative et le fichier des partenaires. Seules les informations issues directement de ce système peuvent alimenter ces fichiers.</p>
<p>3. L'entreprise doit conserver la documentation sur les conditions d'utilisation du logiciel de télétransmission, ou guide utilisateur. Les agents de l'administration doivent pouvoir la consulter sur le lieu de la dématérialisation.</p>
<p>L'entreprise doit également prendre toutes les dispositions nécessaires pour garantir aux agents de l'administration l'accès à la documentation informatique, notamment celle qui concerne le développement de l'architecture du logiciel de télétransmission, son analyse fonctionnelle et organique et son exploitation.</p>
''',
"Réécriture à droit constant : les fonctions du système et les obligations des entreprises sont exprimées par des verbes directs. Les règles de restitution, de traitement des anomalies et de conservation sont rendues plus lisibles sans fusionner les émissions et les réceptions. Tous les éléments de la liste récapitulative et du fichier des partenaires sont repris. Aucune réforme de fond.",
"Les I à VI, leurs subdivisions chiffrées et leurs lettres, ainsi que chacun des alinéas, sont conservés. L'article 96 G de l'annexe III a été vérifié dans le corpus public local : il prévoit bien le régime des messages structurés et la liste récapitulative. Maintien de la différence de traitement des anomalies : message rejeté non émis, non archivé et non tracé à l'émission ; anomalie tracée et messages archivés à la réception. Maintien des informations facultatives dans la restitution, des données originelles, de la chronologie et de l'alimentation automatique par les seules données du système. Aucun délai de conservation chiffré ni régime distinct de plateforme agréée n'est ajouté.")

add('41 septies A', '''
<p>I.-0. - Les accords de reconnaissance multilatéraux mentionnés au premier alinéa du 5° du I de l'article 242 nonies B de l'annexe II au code général des impôts s'entendent de tous les accords applicables à la certification ISO/IEC/27001 établis dans le cadre :</p>
<p>1° De l'autorité internationale de coopération sur l'accréditation dénommée « Global Accreditation Cooperation Incoporated » ;</p>
<p>2° Du forum international d'accréditation dénommé « International Accreditation Forum ».</p>
<p>I. - L'audit de conformité mentionné au c du 6° du I de l'article 242 nonies B et au 1° du I de l'article 242 nonies C de l'annexe II au code général des impôts doit vérifier les points suivants :</p>
<p>1° En matière d'interopérabilité des échanges :</p>
<p>a) Le respect, par la plateforme agréée, du socle minimum de formats prévu au 1° du I de l'article 41 septies C ;</p>
<p>b) Le raccordement effectif de la plateforme agréée à l'annuaire central mentionné au III de l'article 289 bis du code général des impôts, à la solution de l'administration mentionnée à l'article 242 nonies G de l'annexe II au même code et à la solution mutualisée prévue au premier alinéa de l'article L. 2192-5 du code de la commande publique ;</p>
<p>c) Le raccordement effectif de la plateforme à au moins une autre plateforme agréée.</p>
<p>Au sens du présent 1°, le raccordement désigne les modalités d'interconnexion des plateformes qui reposent sur une convention d'interopérabilité bilatérale ou sur un protocole d'échange en réseau ;</p>
<p>2° En matière d'authentification : l'existence et le fonctionnement normal du dispositif par lequel la plateforme agréée vérifie l'identité et la qualité de l'utilisateur et sécurise l'accès à ses services, conformément à l'article 242 nonies F de l'annexe II au code général des impôts ;</p>
<p>3° En matière d'émission et de transmission de factures électroniques :</p>
<p>a) L'existence et le bon fonctionnement des moyens utilisés par la plateforme agréée pour garantir la conformité des factures aux conditions du V de l'article 289 du code général des impôts, notamment lorsque la facture est convertie dans l'un des formats du socle minimum prévu au 1° du I de l'article 41 septies C ;</p>
<p>b) La capacité de la plateforme agréée à garantir le respect des conditions du VII de l'article 289 précité par l'assujetti au nom et pour le compte duquel elle agit, en accomplissant, selon le cas, les actions suivantes :</p>
<p>- contribuer à la documentation de la piste d'audit fiable de ses utilisateurs ;</p>
<p>- satisfaire aux exigences de transmission des factures assorties d'une signature électronique ;</p>
<p>- tenir et conserver, en matière d'échange de données informatisé, une liste récapitulative séquentielle de tous les messages émis et reçus et de leurs anomalies éventuelles, par utilisateur, ainsi qu'un fichier des partenaires avec lesquels des factures électroniques sont échangées ;</p>
<p>c) La mise en œuvre correcte des contrôles prévus à l'article 242 nonies K de l'annexe II au code général des impôts ;</p>
<p>d) Le respect des formats requis au 1° du I de l'article 41 septies C et des normes de facturation mentionnées au même I ;</p>
<p>e) L'utilisation, par la plateforme agréée, de l'un des protocoles de communication sécurisés mentionnés à l'article 41 septies I ;</p>
<p>f) L'existence et la mise en œuvre effective des moyens qui permettent d'assurer l'adressage des factures électroniques ;</p>
<p>g) L'existence et la mise en œuvre effective des moyens qui permettent de gérer les statuts de traitement obligatoires des factures électroniques ;</p>
<p>4° En matière de recueil, par la plateforme agréée, des données de transaction et de paiement mentionnées aux articles 242 nonies M et 242 nonies P de l'annexe II au code général des impôts :</p>
<p>a) La capacité effective de la plateforme à distinguer les données transmises respectivement au titre des articles 242 nonies J, 242 nonies M et 242 nonies P de l'annexe II au code général des impôts ;</p>
<p>b) La mise en œuvre correcte des contrôles prévus à l'article 242 nonies N et au II de l'article 242 nonies P de l'annexe II au même code ;</p>
<p>c) L'intégrité des données reçues d'un assujetti lorsqu'elles sont agrégées par numéro d'identification prévu à l'article R. 123-221 du code de commerce, ou par un numéro équivalent ;</p>
<p>5° En matière de transmission à l'administration des données de facturation, de transaction et de paiement :</p>
<p>a) La fiabilité des traitements informatiques et l'intégrité des données exigées, notamment en cas d'extraction ou de conversion dans un format du socle minimal ;</p>
<p>b) La mise en œuvre effective et correcte des contrôles prévus aux articles 242 nonies K et 242 nonies N et au II de l'article 242 nonies P de l'annexe II au code général des impôts ;</p>
<p>c) Le respect des formats de transmission requis ;</p>
<p>d) Le respect des délais de transmission mentionnés au II de l'article 41 septies H et aux articles 41 septies M et 41 septies P ;</p>
<p>6° En matière de traitement et de conservation des données : leur stockage dans des conditions qui garantissent leur conservation technique et l'absence de corruption, conformément au règlement (UE) 2016/679 du Parlement européen et du Conseil du 27 avril 2016 relatif à la protection des personnes physiques à l'égard du traitement des données à caractère personnel et à la libre circulation de ces données, et abrogeant la directive 95/46/ CE (règlement général sur la protection des données) ;</p>
<p>7° En matière de traçabilité : l'existence de contrôles, leur mise en œuvre correcte et la conservation des preuves correspondantes concernant :</p>
<p>a) Les accès à la plateforme agréée ;</p>
<p>b) L'utilisation de l'annuaire à la seule fin d'adressage des factures électroniques et la conservation des extractions de cet annuaire pendant une durée limitée, conforme au règlement (UE) 2016/679 précité ;</p>
<p>c) Les processus de traitement des factures et des données de facturation, de transaction et de paiement ;</p>
<p>8° En matière d'actualisation des informations d'adressage dans l'annuaire central mentionné au III de l'article 289 bis du code général des impôts : la tenue correcte, le suivi et l'archivage des accords formels signés par les assujettis qui ont désigné la plateforme agréée pour recevoir leurs factures électroniques.</p>
<p>II. - L'audit de conformité doit porter sur les périodes suivantes :</p>
<p>1° Pour l'obtention du numéro d'immatriculation prévue à l'article 242 nonies B de l'annexe II au code général des impôts, au moins un mois d'activité couvrant les fonctionnalités décrites aux 6° et 7° du I du même article 242 nonies B. Cette période doit être postérieure à la notification de la délivrance du numéro d'immatriculation ;</p>
<p>2° Pour le renouvellement de ce numéro prévu à l'article 242 nonies C de l'annexe II au même code, les trois années qui suivent la notification de la délivrance ou du renouvellement du numéro d'immatriculation.</p>
<p>III. - L'audit de surveillance mentionné à l'article 242 nonies C bis de l'annexe II au code général des impôts doit vérifier que les points de conformité mentionnés au I restent respectés. A cette fin, la plateforme agréée doit communiquer les modifications substantielles intervenues depuis la remise du dernier rapport d'audit de conformité ou de surveillance à la personne mentionnée au c du 6° du I de l'article 242 nonies B de l'annexe II au code général des impôts.</p>
<p>L'audit de surveillance doit porter sur au moins un mois d'activité compris dans les six derniers mois de la période auditée.</p>
<p>Les périodes sur lesquelles porte l'audit de surveillance sont les suivantes :</p>
<p>1° Pour l'audit mentionné au deuxième alinéa de l'article 242 nonies C bis de l'annexe II au code général des impôts, la deuxième année suivant la notification de la délivrance du numéro d'immatriculation ;</p>
<p>2° Pour le premier audit mentionné au troisième alinéa du même article 242 nonies C bis, la première année suivant la notification du renouvellement du numéro d'immatriculation ;</p>
<p>3° Pour le second audit mentionné au troisième alinéa du même article 242 nonies C bis, la deuxième année suivant la notification du renouvellement du numéro d'immatriculation.</p>
''',
"Réécriture à droit constant : les points à vérifier sont formulés directement comme objets de l'audit, les acteurs sont explicités et les conditions d'interconnexion, de traitement des données et de période auditée sont clarifiées. Les huit domaines de conformité et l'intégralité des contrôles, formats, garanties et échéances sont maintenus. Aucune réforme de fond ni nouvelle obligation de plateforme n'est créée.",
"Numérotation source I.-0., puis I, II et III, et ordre de tous les alinéas maintenus. Les renvois du III à l'article 242 nonies C bis constituent une discordance préexistante : aucun article portant ce numéro n'a été trouvé dans impots-annexe-2.json du corpus public local. Dans ce corpus, les audits de surveillance après délivrance et après renouvellement figurent respectivement au d du 6° du I de l'article 242 nonies B et au IV de l'article 242 nonies C. Une coordination expresse de ces renvois et des alinéas cités est nécessaire ; aucune substitution silencieuse n'est faite. Autre point à contrôler : le II, 2° porte sur trois années complètes suivant la délivrance ou le renouvellement, alors que le I de l'article 242 nonies C impose une demande de renouvellement au plus tard cinq mois avant l'expiration ; l'articulation temporelle reste celle de la source. L'audit initial postérieur à la délivrance est conservé, en cohérence avec le rapport à produire dans l'année prévu au c du 6° du I de l'article 242 nonies B. Maintien d'au moins un mois d'activité et de la fenêtre des six derniers mois pour la surveillance. La graphie source « Global Accreditation Cooperation Incoporated » et l'identifiant ISO/IEC/27001 sont conservés ; la dénomination de l'organisme appelle un contrôle. Les références à 41 septies C, H, M et P ont été consultées localement. Les transitions propres aux plateformes antérieurement immatriculées, mentionnées dans les notes de l'article 242 nonies C, restent à coordonner dans leur texte d'origine ; aucune date historique n'est utilisée comme date de réforme nouvelle.")


assert len(sources) == len(drafts) == 21
answer = []
for source in sources:
    draft = drafts[source['number']]
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        **draft,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
