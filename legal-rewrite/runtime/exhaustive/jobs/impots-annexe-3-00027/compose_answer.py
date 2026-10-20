import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, xml, reason, notes):
    assert number not in drafts
    drafts[number] = (xml.strip(), reason, notes)


add('53 ter', '''
<p>Les employeurs agricoles qui ne sont pas visés à l'article 53 bis doivent acquitter la taxe sur les salaires au titre des traitements et salaires versés au personnel affecté aux établissements suivants :</p>
<p>1° Les établissements distincts, séparés de l'exploitation agricole, dans lesquels ils vendent des produits provenant des terrains qu'ils exploitent ou du bétail qu'ils y élèvent, entretiennent ou engraissent, dès lors que l'une des conditions suivantes est remplie :</p>
<p>a. Les ventes sont effectuées selon des méthodes commerciales, notamment en ce qui concerne l'agencement matériel et la recherche des débouchés ;</p>
<p>b. Les ventes ne portent pas exclusivement sur les produits mentionnés au 1° ;</p>
<p>c. Tout ou partie de ces produits a subi une préparation ou une manipulation qui en modifie le caractère et qui n'est pas nécessaire pour les rendre propres à la consommation ou à l'utilisation en l'état ;</p>
<p>2° Les établissements dans lesquels est effectuée la préparation ou la manipulation visée au c du 1.</p>
''',
"Droit constant : l'obligation de l'employeur est énoncée directement et les trois conditions alternatives d'assujettissement des établissements de vente sont explicitées. Les deux catégories d'établissements et les subdivisions a à c sont maintenues. Aucune réforme de fond n'est appliquée à la taxe sur les salaires agricole.",
"Conserver le renvoi à l'article 53 bis et la distinction entre les établissements de vente du 1° et ceux de préparation ou de manipulation du 2°. La condition du c exige à la fois une modification du caractère des produits et une opération non nécessaire à leur consommation ou utilisation en l'état ; les conditions a, b et c restent alternatives.")

add('53 quater', '''
<p>Les organismes professionnels et les autres employeurs agricoles établis dans les départements d'outre-mer ne sont pas soumis aux dispositions des articles 53 bis et 53 ter.</p>
''',
"Droit constant : les bénéficiaires de l'exclusion territoriale deviennent le sujet de la phrase. L'exclusion demeure limitée aux dispositions des articles 53 bis et 53 ter ; aucune réforme de fond.",
"Le champ vise les départements d'outre-mer, sans extension aux autres collectivités ultramarines. Cette exclusion des articles 53 bis et 53 ter n'est pas reformulée en exonération générale de toute taxe sur les salaires.")

add('54', '''
<p>Le demandeur doit présenter la demande prévue au dernier alinéa du VIII de l'article 235 ter ZG du code général des impôts dans le délai légal de réclamation fixé à l'article R. * 196-2 du livre des procédures fiscales.</p>
<p>Cette demande doit préciser :</p>
<p>1° Le nom ou la raison sociale du demandeur, ainsi que son adresse postale ;</p>
<p>2° Les références cadastrales du ou des terrains concernés : préfixe, section et numéro des parcelles.</p>
''',
"Droit constant : l'auteur de la demande et le caractère obligatoire du délai et des renseignements sont rendus explicites. Les deux rubriques d'identification sont conservées ; aucune réforme de fond.",
"Renvois maintenus au dernier alinéa du VIII de l'article 235 ter ZG du CGI et à l'article R. * 196-2 du LPF. Les trois composantes de la référence cadastrale et l'adresse postale restent exigées. L'article 55 règle séparément le destinataire et la pièce jointe.")

add('55', '''
<p>Le demandeur adresse la demande à la direction départementale ou, le cas échéant, régionale des finances publiques dont relève le service auprès duquel le contribuable doit remplir ses obligations déclaratives en matière de taxe d'archéologie préventive.</p>
<p>Il joint à cette demande une copie du titre de perception indiquant le montant de la redevance d'archéologie préventive acquittée en application de l'avant-dernier alinéa de l'article L. 524-4 du code du patrimoine.</p>
''',
"Droit constant : les formulations passives sont remplacées par les obligations du demandeur, en deux alinéas correspondant au destinataire et à la pièce justificative. Aucune réforme de fond.",
"Maintenir la distinction entre la taxe faisant l'objet des obligations déclaratives et la redevance déjà acquittée figurant sur le titre de perception. Le renvoi à l'avant-dernier alinéa de l'article L. 524-4 du code du patrimoine est conservé.")

add('58-0 A bis', '''
<p>I. – Pour l'application du 11° du III de l'article 234 nonies du code général des impôts, constituent des travaux de réhabilitation des logements les travaux de modification ou de remise en état du gros œuvre, ainsi que les travaux d'aménagement interne, qui équivalent, par leur nature, à une reconstruction. Cette définition comprend également les travaux d'amélioration indissociables de ces travaux.</p>
<p>II. – À la demande de l'administration, les contribuables doivent pouvoir justifier de la date d'achèvement du logement et des travaux de réhabilitation, du montant effectivement payé pour ces travaux et du montant de la subvention versée à ce titre par l'Agence nationale de l'habitat.</p>
''',
"Droit constant : la définition des travaux est scindée en deux phrases pour distinguer les travaux équivalant à une reconstruction de leurs améliorations indissociables. L'obligation de justification et les subdivisions I et II sont conservées. Aucune réforme de fond, notamment aucune extension à une voie nouvelle de rénovation locative.",
"Le critère d'équivalence à une reconstruction reste applicable aux travaux définis au I, et les améliorations doivent leur être indissociables. Conserver les dates d'achèvement du logement et des travaux, le paiement effectif et la subvention de l'Agence nationale de l'habitat. Le 11° du III de l'article 234 nonies demeure le fondement de ce régime distinct.")

add('58 A', '''
<p>La personne morale ou l'organisme doit souscrire la déclaration spéciale prévue à l'article 234 quaterdecies du code général des impôts auprès du service des impôts du lieu où siège sa direction ou, à défaut, du lieu de son principal établissement.</p>
''',
"Droit constant : le déclarant est identifié et le rattachement territorial du service des impôts est formulé directement, avec maintien du rattachement subsidiaire. Aucune réforme de fond.",
"Le lieu du principal établissement ne s'applique qu'à défaut du siège de la direction. Le renvoi à l'article 234 quaterdecies du CGI est conservé ; aucune nouvelle formalité ni dispense n'est créée.")

add('58 Q', '''
<p>I. – En application du VIII de l'article 235 ter ZD du code général des impôts, le redevable transmet les informations suivantes, pour les opérations taxées comme pour les opérations exonérées :</p>
<p>a) Son nom ou sa raison sociale et, s'il en est doté, son code d'identification bancaire (code BIC), son numéro de taxe sur la valeur ajoutée intracommunautaire ou, à défaut, son numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce ;</p>
<p>b) L'adresse de son siège social ou de son principal établissement ;</p>
<p>c) Lorsque le dépositaire central qui tient le compte d'émission du titre est soumis au 3° du II de l'article L. 621-9 du code monétaire et financier, le code que ce dépositaire attribue à l'adhérent chargé du paiement de la taxe en application du VII de l'article 235 ter ZD du code général des impôts ;</p>
<p>d) Le code d'identification du titre de capital ou du titre assimilé (code ISIN) dont l'acquisition est soumise à la taxe ;</p>
<p>e) La date de la transaction ;</p>
<p>f) La date de règlement/livraison du titre de capital ou du titre assimilé ;</p>
<p>g) La référence que son système de gestion interne attribue aux acquisitions. Si une partie des transactions ne donne pas lieu à un transfert de propriété et que seule la position nette acheteuse de l'acquéreur est soumise à la taxe, il transmet la référence attribuée à cette position ;</p>
<p>h) La valeur des transactions, égale au nombre de titres multiplié par leur valeur unitaire d'acquisition.</p>
<p>Si une partie des transactions ne donne pas lieu à un transfert de propriété et que seule la position nette acheteuse de l'acquéreur est soumise à la taxe, le montant des acquisitions est égal au nombre de titres dont la propriété est transférée, multiplié par la valeur moyenne des titres ainsi acquis pendant la période au terme de laquelle cette position est calculée.</p>
<p>Pour un titre donné, la position nette acheteuse servant d'assiette à la taxe est calculée par acquéreur. Les acquisitions exonérées prévues au II de l'article 235 ter ZD du code général des impôts et les ventes associées à ces exonérations sont exclues du calcul.</p>
<p>Le redevable soustrait du nombre de titres d'une société soumise à la taxe au sens du I de l'article 235 ter ZD précité, acquis par un acquéreur pendant une période, le nombre de titres de cette société cédés par le même acquéreur pendant la même période.</p>
<p>Le résultat correspond au nombre de titres dont la propriété est transférée à l'acquéreur. Ce nombre est multiplié par le prix unitaire moyen des acquisitions non exonérées du titre pendant la période au terme de laquelle la position nette acheteuse est calculée.</p>
<p>La base d'imposition du redevable est la somme des positions nettes acheteuses calculées pour chaque titre et chaque acquéreur ;</p>
<p>i) Pour chaque acquisition exonérée en application du II de l'article 235 ter ZD du code général des impôts, la catégorie d'exonération applicable ;</p>
<p>j) Les éventuelles régularisations mentionnées au IV ;</p>
<p>k) Le montant de la taxe à acquitter au titre de la déclaration. Pour chaque acquisition, ce montant est arrondi au centime le plus proche.</p>
<p>II. – Par exception au I du présent article, les acquisitions exonérées en application du 9° du II de l'article 235 ter ZD du code général des impôts n'ont pas à être déclarées au dépositaire central.</p>
<p>III. – L'omission des informations mentionnées aux a, c et k du I entraîne le rejet de la déclaration.</p>
<p>IV. – Le redevable doit régulariser la taxe payée à tort ou omise par une imputation ou une rectification portée sur les déclarations ultérieures déposées auprès du dépositaire central avant le 31 décembre de la deuxième année suivant celle du paiement à tort ou de l'omission. Cette régularisation doit figurer dans une inscription déclarative distincte précisant notamment les opérations et la période auxquelles elle se rapporte.</p>
<p>Si le montant payé par le redevable dépasse la taxe due, l'excédent qui ne peut pas être imputé au cours du mois de sa constatation peut être imputé sur la taxe due le mois suivant ou remboursé par l'administration fiscale dans les conditions prévues à l'article R. * 196-1 du livre des procédures fiscales.</p>
''',
"Droit constant : les informations déclarées sont rattachées au redevable, le calcul de la position nette est exposé en phrases plus courtes et les modalités de régularisation sont formulées comme une obligation explicite. Les subdivisions I à IV, lettres a à k et alinéas de calcul sont conservés. Aucune réforme de fond de la taxe sur les transactions financières.",
"Maintenir l'exception déclarative du 9° du II de l'article 235 ter ZD, l'exclusion des opérations exonérées et ventes associées du calcul net, le calcul par titre et acquéreur, et l'arrondi par acquisition au centime. Le III relatif au rejet pour omission des informations a, c et k est repris dans sa formulation source pour ne pas modifier la portée de ce motif de rejet. Le délai reste avant le 31 décembre de la deuxième année, distinct du remboursement régi par R. * 196-1 du LPF. La note source relative au décret n° 2022-1014 du 19 juillet 2022 est historique et ne fixe aucune entrée en vigueur future. Les renvois de l'article 58 R au IV demeurent valables.")

add('58 R', '''
<p>I. – Le dépositaire central soumis au 3° du II de l'article L. 621-9 du code monétaire et financier comptabilise les opérations liées à la collecte de la taxe dans un journal spécifique intégré à ses livres comptables. Les coûts et les produits de ces opérations font chaque année l'objet d'une reddition des comptes, que l'administration peut auditer.</p>
<p>II. – Le dépositaire central vire les montants de taxe collectés, avant le 6 du mois suivant les acquisitions taxées, sur le compte Banque de France qu'il a ouvert pour cette collecte. Ces montants sont ensuite déposés auprès de l'Agence France Trésor jusqu'à leur reversement au service chargé des grandes entreprises, avant le 25 du même mois.</p>
<p>III. – La déclaration prévue au IX de l'article 235 ter ZD du code général des impôts est établie chaque mois selon le modèle de l'administration.</p>
<p>Pour chaque redevable, le dépositaire central transmet par voie dématérialisée les informations suivantes :</p>
<p>a) Le nom ou la raison sociale du redevable et, s'il en est doté, son code d'identification bancaire (code BIC), son numéro de taxe sur la valeur ajoutée intracommunautaire ou, à défaut, son numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce ;</p>
<p>b) L'adresse du siège social ou du principal établissement du redevable ;</p>
<p>c) La période d'imposition ;</p>
<p>d) La base imposable et le montant de la taxe due et acquittée au titre du mois concerné ;</p>
<p>e) La date de dépôt de la déclaration et de paiement auprès du dépositaire central ;</p>
<p>f) Le montant mensuel des opérations exonérées, regroupées par motif d'exonération ;</p>
<p>g) Le montant mensuel et le motif des régularisations mentionnées au IV de l'article 58 Q.</p>
<p>IV. – 1. Avant le 25 du second mois suivant l'acquisition du titre de capital ou du titre assimilé, le dépositaire central dresse la liste des redevables dont les déclarations présentent les caractéristiques suivantes :</p>
<p>a) L'assiette taxable est incohérente avec le montant de la taxe déclaré ou acquitté ;</p>
<p>b) Aucune acquisition n'est déclarée sur les trente titres les plus fréquemment déclarés comme acquis, en moyenne sur le mois précédent, par les redevables ;</p>
<p>c) Pour les livraisons de titres effectuées dans les livres du dépositaire central par ses adhérents directs redevables, le montant des achats payés par le redevable au cours du mois dépasse celui des acquisitions déclarées.</p>
<p>Pour chaque redevable inscrit sur cette liste, le dépositaire central indique le ou les motifs d'inclusion mentionnés aux a, b et c.</p>
<p>2. Avant le 25 du second mois suivant l'acquisition du titre de capital ou du titre assimilé, le dépositaire calcule les indicateurs suivants, pour chaque redevable et en moyenne pour l'ensemble des redevables :</p>
<p>a) Le taux de variation du nombre et du montant des acquisitions déclarées par rapport au mois précédent. Les redevables qui ont déposé une déclaration le mois précédent et n'en déposent aucune pour le mois courant sont considérés comme ayant réduit leurs acquisitions déclarées de 100 % ;</p>
<p>b) La part des acquisitions exonérées dans l'ensemble des acquisitions déclarées, en nombre et en montant, ainsi que la part relative de chaque motif d'exonération dans les acquisitions exonérées ;</p>
<p>c) La variation du taux d'exonération, en nombre et en montant, par rapport au mois précédent.</p>
<p>3. Le dépositaire central recoupe les opérations qui lui sont déclarées avec celles connues des plates-formes de négociation et des chambres de compensation avec lesquelles il a préalablement conclu une convention à cette fin, quel que soit leur lieu d'établissement.</p>
<p>V. – Lors du dépôt de la déclaration prévue au IX de l'article 235 ter ZD du code général des impôts, le dépositaire central transmet au service chargé des grandes entreprises les informations mentionnées aux 1 et 2 du IV du présent article.</p>
<p>VI. – Le dépositaire central soumis au 3° du II de l'article L. 621-9 du code monétaire et financier remet à la direction générale des finances publiques, au plus tard le 31 mars de chaque année, un rapport sur les diligences accomplies pendant l'année écoulée au titre du dispositif de contrôle mentionné au IV du présent article et sur les résultats de ce contrôle.</p>
<p>VII. – Le dépositaire central soumis au 3° du II de l'article L. 621-9 du code monétaire et financier tient à la disposition de la direction générale des finances publiques, sous forme dématérialisée, toutes les données collectées et tous les documents élaborés dans l'exercice de ses missions. Il les conserve pendant le délai prévu à l'article L. 102 B du livre des procédures fiscales.</p>
<p>Les fonctionnaires titulaires des corps de catégorie A ou B de cette direction sont autorisés à accéder à ces données et documents. Sur simple demande, ils peuvent les consulter et en prendre copie par tout moyen et sur tout support.</p>
<p>VIII. – Le dépositaire central ne peut utiliser les informations reçues en application du VIII de l'article 235 ter ZD du code général des impôts que pour les transmettre, brutes ou retraitées, à la direction générale des finances publiques.</p>
<p>Le dépositaire central soumis au 3° du II de l'article L. 621-9 du code monétaire et financier prend les mesures techniques nécessaires pour assurer la sécurité, l'intégrité et la confidentialité des données collectées, ainsi que leur protection contre l'indexation par les moteurs de recherche. Pour le traitement de données mis en œuvre en application du VII, il respecte la loi n° 78-17 du 6 janvier 1978 modifiée relative à l'informatique, aux fichiers et aux libertés et accomplit les formalités nécessaires auprès de la Commission nationale de l'informatique et des libertés.</p>
''',
"Droit constant : les obligations comptables, les mouvements de fonds, les contrôles et la protection des données sont rédigés avec un responsable explicite et des phrases plus courtes. Toutes les subdivisions I à VIII, les listes d'informations et les indicateurs sont maintenus. Aucune réforme de fond ni réutilisation nouvelle des données n'est introduite.",
"Échéances conservées : virements avant le 6, reversement avant le 25 du même mois, contrôles des 1 et 2 du IV avant le 25 du second mois, rapport au plus tard le 31 mars. Maintien des trente titres, de la baisse conventionnelle de 100 %, des calculs en nombre et montant, de la convention préalable de recoupement et des agents titulaires A ou B. Les 1 et 2 du IV restent les seules informations visées au V. Les renvois aux articles 58 Q, 235 ter ZD et L. 102 B du LPF sont conservés. La note historique sur le décret n° 2022-1014 du 19 juillet 2022 et le renvoi source aux formalités CNIL sont maintenus comme contexte de contrôle, sans actualisation silencieuse du régime de protection des données.")

add('58 S', '''
<p>I. – Le seuil prévu au II de l'article 235 ter ZD bis du code général des impôts est d'une demi-seconde.</p>
<p>Pour apprécier son dépassement, il est tenu compte du temps de latence qui sépare habituellement deux événements affectant un titre donné. Ce temps correspond à la durée entre une instruction d'achat ou de vente du titre et une instruction visant à modifier ou à annuler cette instruction d'achat ou de vente.</p>
<p>II. – Le seuil prévu au IV de l'article 235 ter ZD bis du code général des impôts est de 80 %.</p>
''',
"Droit constant : la définition du temps de latence est isolée dans une seconde phrase et rattachée explicitement au dépassement du premier seuil. Les deux seuils et les subdivisions sont conservés ; aucune réforme de fond.",
"Conserver distinctement la demi-seconde du II de l'article 235 ter ZD bis et les 80 % de son IV. Le temps de latence reste apprécié à titre habituel, pour un titre donné, entre l'ordre initial et sa modification ou son annulation.")

add('64 bis', '''
<p>L'impôt acquitté hors de France mentionné au sixième alinéa du I de l'article 238 bis-0 I du code général des impôts est converti au taux de change en vigueur à la date de clôture de l'exercice de l'entreprise française. Il s'agit de l'impôt éventuellement imputable sur l'impôt sur les sociétés dû par cette entreprise au titre des résultats provenant de la gestion ou de la disposition des actifs transférés ou des biens acquis en remploi. L'entreprise française doit prouver que cet impôt a été effectivement payé.</p>
''',
"Droit constant : la règle de conversion, l'identification de l'impôt concerné et la preuve du paiement sont distinguées en trois phrases au sein du même alinéa. Aucune réforme de fond du régime d'imputation ni du taux de l'impôt sur les sociétés.",
"L'imputation demeure éventuelle : le texte ne crée pas de crédit d'impôt automatique. Le taux de change est celui de la clôture de l'exercice de l'entreprise française, et non celui du paiement étranger. Le renvoi reste au sixième alinéa du I de l'article 238 bis-0 I, sans coordination chiffrée avec le taux national normal de l'article 219.")

add('64 ter', '''
<p>L'entreprise française établit sur un document conforme au modèle fixé par l'administration l'état qu'elle joint à sa déclaration de résultats en application des troisième et quatrième alinéas du I de l'article 238 bis-0 I du code général des impôts.</p>
''',
"Droit constant : l'entreprise devient le sujet de l'obligation d'utiliser le modèle administratif, sans modifier l'état à joindre ni ses fondements. Aucune réforme de fond.",
"Les renvois visent les troisième et quatrième alinéas du I de l'article 238 bis-0 I du CGI. L'état joint à la déclaration demeure distinct de la déclaration et des documents régis par l'article 64 quater.")

add('64 quater', '''
<p>La déclaration des résultats provenant de la gestion ou de la disposition des actifs transférés ou des biens acquis en remploi, mentionnée au cinquième alinéa du I de l'article 238 bis-0 I du code général des impôts, doit être accompagnée de tous les documents exigés des entreprises par l'article 38.</p>
<p>Le déclarant établit cette déclaration sur un document conforme au modèle fixé par l'administration.</p>
''',
"Droit constant : l'exhaustivité des pièces jointes est formulée directement et l'auteur de l'établissement de la déclaration est explicité. Les deux alinéas sont conservés ; aucune réforme de fond.",
"Conserver le renvoi au cinquième alinéa du I de l'article 238 bis-0 I et à l'article 38 de la présente annexe. L'obligation porte sur l'ensemble des documents exigés, sans réduction à un état récapitulatif.")

add('65', '''
<p>Pour l'application de l'article 248 C du code général des impôts, sont des intermédiaires agréés les personnes et établissements suivants :</p>
<p>a. Les prestataires de services d'investissement autres que les sociétés de gestion de portefeuille ;</p>
<p>b. La société anonyme Natexis ou toute société qu'elle contrôle au sens de l'article L. 233-3 du code de commerce ;</p>
<p>c. La Banque de France ;</p>
<p>d. Les établissements de crédit ;</p>
<p>e. La Caisse centrale des banques populaires et les banques populaires agréées par leur banque fédérale ;</p>
<p>f. La Caisse centrale de crédit coopératif ;</p>
<p>g. La Caisse centrale de crédit mutuel et les caisses départementales et interdépartementales de crédit mutuel ;</p>
<p>h. La Caisse des dépôts et consignations ;</p>
<p>i. L'organe central du crédit agricole et les caisses régionales de crédit agricole mutuel ;</p>
<p>j. Le Crédit foncier communal d'Alsace et de Lorraine ;</p>
<p>k. Le Crédit foncier de France.</p>
''',
"Droit constant : la phrase d'ouverture exprime directement la qualité d'intermédiaire agréé résultant de l'inscription sur la liste. Les dénominations et les onze entrées a à k sont reprises sans substitution institutionnelle ; la réécriture porte sur la formulation du champ de la liste. Aucune réforme de fond.",
"Les dénominations historiques, notamment Natexis et les caisses centrales, sont celles de la source : leur concordance institutionnelle actuelle appelle un contrôle distinct, sans remplacement silencieux par des successeurs supposés. Maintenir l'exclusion des sociétés de gestion de portefeuille au a et la notion de contrôle de L. 233-3 au b.")

add('65 A', '''
<p>Les animaux suivants sont des animaux de boucherie et de charcuterie :</p>
<p>Équidés : chevaux et juments, mulets, mules et bardots, ânes et ânesses, baudets, étalons ;</p>
<p>Bovidés : bœufs et taureaux, vaches, veaux, bouvillons, taurillons et génisses ;</p>
<p>Ovidés : béliers et moutons, brebis et agneaux gris, agneaux de lait ;</p>
<p>Suidés : porcs mâles et femelles, cochons de lait ;</p>
<p>Caprins : boucs et chèvres, ainsi que les chevreaux dont le poids de viande nette après l'abattage dépasse 7 kilogrammes.</p>
''',
"Droit constant : la définition est énoncée directement et le critère de poids des chevreaux est rapproché de la viande nette après abattage. Les cinq catégories et tous les animaux énumérés sont conservés ; aucune réforme de fond.",
"Le seuil reste strictement supérieur à 7 kilogrammes de viande nette après abattage et concerne les chevreaux, sans être étendu aux boucs ou aux chèvres. Les catégories zoologiques et les désignations historiques sont maintenues.")

add('68', '''
<p>Pour les prestations de transport visées au 4° de l'article 259 A du code général des impôts et réalisées en partie en France et en partie hors de France, les transporteurs doivent justifier le prix correspondant au transport effectué en France. Si ce prix n'est pas déterminé, ils le calculent en multipliant le prix du transport par le rapport entre la longueur du trajet effectué en France et la longueur totale du transport.</p>
''',
"Droit constant : l'obligation de justification et la méthode de calcul subsidiaire sont formulées avec le transporteur pour sujet. La règle proportionnelle de territorialisation du prix est conservée ; aucune réforme de fond.",
"La clé de calcul porte sur les longueurs du transport, sans recours au temps de trajet ni à un forfait. Elle ne s'applique que si le prix du transport effectué en France n'est pas déterminé. Le champ reste celui du 4° de l'article 259 A du CGI.")

add('70 sexies', '''
<p>Les activités exercées par les établissements de crédit, les prestataires de services d'investissement changeurs, escompteurs et remisiers constituent des activités bancaires ou financières pour l'application de l'article 260 B du code général des impôts.</p>
<p>Les opérations qui se rattachent aux activités énumérées au premier alinéa relèvent également de cette définition lorsqu'elles sont réalisées par d'autres personnes et constituent l'activité principale de ces personnes.</p>
''',
"Droit constant : la définition est rédigée avec les activités pour sujet, puis l'extension aux autres personnes est exprimée dans un second alinéa en conservant la condition d'activité principale. Aucune réforme de fond de l'option à la TVA.",
"La source ne comporte pas de virgule entre « prestataires de services d'investissement » et « changeurs » : cette ambiguïté d'énumération est conservée et doit être contrôlée, sans ajout silencieux de ponctuation qui en fixerait la portée. La condition d'activité principale vise les personnes du second alinéa. Coordination conservée avec les exclusions de l'article 70 septies.")

add('70 septies', '''
<p>Par dérogation à l'article 70 sexies, les opérations qui ne se rattachent pas spécifiquement au commerce des valeurs et de l'argent, ainsi que les opérations de crédit-bail, sont exclues de l'application de l'article 260 B du code général des impôts.</p>
''',
"Droit constant : les deux catégories d'opérations exclues sont placées au centre de la phrase, avec maintien de la dérogation à l'article 70 sexies. Aucune réforme de fond.",
"Les opérations de crédit-bail constituent une exclusion distincte ; elles ne sont pas soumises à la condition de non-rattachement au commerce des valeurs et de l'argent. Les deux renvois sont maintenus.")

add('71', '''
<p>Pour l'application du f du 1° de l'article 261 C du code général des impôts, les organismes énumérés ci-dessous sont regardés comme présentant des caractéristiques similaires à celles des organismes de placement collectif en valeurs mobilières mentionnés au paragraphe 2 de l'article 1er de la directive 2009/65/CE du Parlement européen et du Conseil du 13 juillet 2009 portant coordination des dispositions législatives, réglementaires et administratives concernant certains organismes de placement collectif en valeurs mobilières (OPCVM) :</p>
<p>1. Les fonds ouverts à des investisseurs non professionnels, qui regroupent :</p>
<p>a) Les fonds d'investissement à vocation générale régis par les articles L. 214-24-24 à L. 214-26-2 du code monétaire et financier ;</p>
<p>b) Les fonds de capital investissement régis par les articles L. 214-27 à L. 214-32-1 du code monétaire et financier et constitués sous la forme de fonds communs de placement à risques, de fonds communs de placement dans l'innovation ou de fonds d'investissement de proximité ;</p>
<p>c) Les organismes de placement collectif immobilier régis par les articles L. 214-33 à L. 214-85 du code monétaire et financier et constitués sous la forme de sociétés professionnelles de placement à prépondérance immobilière à capital variable, de fonds de placement immobilier et d'organismes de placement collectif immobilier à compartiments ;</p>
<p>d) Les sociétés civiles de placement immobilier, les sociétés d'épargne forestière et les groupements forestiers d'investissement régis par les articles L. 214-86 à L. 214-125 du code monétaire et financier ;</p>
<p>e) Les sociétés d'investissement à capital fixe régies par les articles L. 214-127 à L. 214-138 du code monétaire et financier ;</p>
<p>f) Les fonds de fonds alternatifs régis par les articles L. 214-139 à L. 214-142 du code monétaire et financier ;</p>
<p>2. Les fonds ouverts à des investisseurs professionnels, qui regroupent :</p>
<p>a) Les fonds professionnels à vocation générale régis par les articles L. 214-143 à L. 214-147 du code monétaire et financier ;</p>
<p>b) Les organismes professionnels de placement collectif immobilier régis par les articles L. 214-148 à L. 214-151 du code monétaire et financier ;</p>
<p>c) Les fonds professionnels spécialisés régis par les articles L. 214-154 à L. 214-158 du code monétaire et financier ;</p>
<p>d) Les fonds professionnels de capital investissement régis par les articles L. 214-159 à L. 214-162 du code monétaire et financier ;</p>
<p>e) Les sociétés de libre partenariat régies par les articles L. 214-162-1 à L. 214-162-12 du code monétaire et financier ;</p>
<p>3. Les fonds d'épargne salariale régis par les articles L. 216-163 à L. 214-166 du code monétaire et financier et constitués sous la forme de fonds communs de placement d'entreprise ou de sociétés d'investissement à capital variable d'actionnariat salarié ;</p>
<p>4. Les organismes de financement régis par les articles L. 214-166-1 à L. 214-190-3 du code monétaire et financier, qui regroupent :</p>
<p>a) Les organismes de titrisation constitués sous la forme de fonds communs de titrisation ou de sociétés de titrisation ;</p>
<p>b) Les organismes de financement spécialisé constitués sous la forme de fonds de financement spécialisé ou de sociétés de financement spécialisé ;</p>
<p>5. Les sociétés qui ont opté pour le régime fiscal des sociétés de capital-risque prévu au 3° septies de l'article 208 du code général des impôts.</p>
''',
"Droit constant : la portée de la liste est formulée directement, puis chaque catégorie est rattachée à son régime et à ses formes juridiques. Les cinq subdivisions et toutes leurs lettres sont maintenues. Aucune réforme de fond ni extension automatique de l'exonération de gestion à la future capitalisation collective.",
"Anomalie préexistante au 3 : le renvoi commence à L. 216-163 et se termine à L. 214-166. La référence L. 216-163 est conservée exactement, sans correction supposée en L. 214-163 ; elle nécessite un contrôle dans le code monétaire et financier, non fourni dans les cinq codes du corpus. Toutes les autres bornes de renvoi, la directive 2009/65/CE et le 3° septies de l'article 208 sont maintenus. Le futur régime de capitalisation ne reçoit pas ici une qualification fiscale nouvelle.")

add('72', '''
<p>Les journaux et écrits périodiques qui présentent un lien direct avec l'actualité, apprécié au regard de l'objet de la publication, doivent remplir les conditions suivantes pour bénéficier des avantages fiscaux prévus à l'article 298 septies du code général des impôts :</p>
<p>I. – Ils doivent présenter un contenu original composé d'informations ayant fait l'objet d'un traitement journalistique, notamment pour leur recherche, leur collecte, leur vérification et leur mise en forme. Le caractère journalistique de ce traitement est réputé établi lorsque le traitement est réalisé par des journalistes professionnels au sens de l'article L. 7111-3 du code du travail ou apporté par des agences de presse agréées au sens de l'ordonnance du 2 novembre 1945. Par exception, ce caractère peut être apprécié au regard de l'objet de la publication, en tenant compte de sa périodicité, de la composition de l'équipe rédactionnelle et de la taille de l'entreprise éditrice.</p>
<p>II. – Ils doivent remplir les conditions suivantes :</p>
<p>1° Présenter un caractère d'intérêt général pour la diffusion de la pensée : instruction, éducation, information, récréation du public ;</p>
<p>2° Respecter les obligations de la loi du 29 juillet 1881 sur la liberté de la presse, notamment :</p>
<p>a) Indiquer le nom et le domicile de l'imprimeur qui imprime effectivement la publication ;</p>
<p>b) Avoir un directeur de la publication dont le nom est imprimé sur tous les exemplaires.</p>
<p>3° Paraître régulièrement au moins une fois par trimestre, sans intervalle de plus de quatre mois entre deux parutions ;</p>
<p>4° Être effectivement vendus au public, au numéro ou par abonnement, à un prix marqué présentant un lien réel avec les coûts. La livraison du journal ou du périodique ne doit pas s'accompagner de la fourniture, gratuite ou payante, de marchandises ou de prestations de services sans lien avec l'objet principal de la publication.</p>
<p>Un arrêté conjoint des ministres chargés du budget, de la communication et des postes précise, en tant que de besoin, les modalités d'application de cette disposition ;</p>
<p>5° Ne pas consacrer plus des deux tiers de leur surface aux annonces classées, à la publicité et aux annonces judiciaires et légales. Les annonces classées ne doivent pas dépasser la moitié de la surface totale ;</p>
<p>5° bis Respecter l'obligation d'informer le lecteur de l'identification des publicités publiées, en application du dernier alinéa de l'article 10 de la loi n° 86-897 du 1er août 1986 portant réforme du régime juridique de la presse ;</p>
<p>6° Ne pouvoir être assimilés, même s'ils présentent l'apparence de journaux ou de revues, à aucune des catégories de publications suivantes :</p>
<p>a) Feuilles d'annonces, tracts, guides, prospectus, catalogues, almanachs, répertoires, index, lexiques ;</p>
<p>b) Ouvrages publiés par livraison, dont la publication couvre une période limitée ou qui constituent le complément ou la mise à jour d'ouvrages déjà parus. Toutefois, le complément ou la mise à jour peut bénéficier des avantages fiscaux pour la partie qui, au cours d'une année, n'augmente pas le nombre de pages de l'ouvrage au 31 décembre de l'année précédente ;</p>
<p>c) Publications dont l'objet principal est la recherche ou le développement des transactions d'entreprises commerciales, industrielles, bancaires, d'assurances ou d'autre nature, et qui sont en réalité leurs instruments de publicité ou de communication, ou qui apparaissent comme l'accessoire d'une activité commerciale ou industrielle ;</p>
<p>d) Publications dont l'objet principal est de publier des horaires, des programmes, des modèles, plans ou dessins, ou des cotations. Ne sont toutefois pas exclues les publications ayant pour objet essentiel l'insertion à titre d'information des programmes de radiodiffusion et de télévision, et des cotes de valeurs mobilières ;</p>
<p>e) Publications dont l'objet principal est d'informer sur la vie interne d'un groupement, quelle que soit sa forme juridique, ou qui constituent pour ce groupement un instrument de publicité ou de propagande ;</p>
<p>f) Publications dont le prix est compris dans une cotisation à une association ou à un groupement quelconque ;</p>
<p>7° Pour les suppléments, les numéros spéciaux ou hors série de journaux ou de publications périodiques, remplir en outre les conditions suivantes :</p>
<p>a) Le supplément doit remplir les mêmes conditions de fond et de forme que la publication principale. Il doit porter la mention « supplément », suivie du titre et de la date ou du numéro de la publication à laquelle il se rattache.</p>
<p>Pour l'application du présent article, est un supplément à un journal ou à un écrit périodique toute publication détachée qui paraît périodiquement, constitue une addition due à l'abondance des sujets traités ou est destinée à compléter ou à illustrer le texte d'une publication. Le supplément ne peut être vendu isolément ni faire l'objet d'un abonnement séparé ;</p>
<p>b) Le numéro spécial ou hors série doit remplir les mêmes conditions de fond et de forme que la publication principale et porter la mention « numéro spécial » ou « hors-série ». Il peut toutefois être consacré à un thème unique si le sujet présente un lien manifeste avec le contenu habituel de la publication principale, dans la limite d'un numéro par an pour les publications trimestrielles et de deux numéros par an pour celles qui paraissent à des intervalles plus courts.</p>
<p>Pour l'application du présent article, un numéro spécial ou hors-série d'un journal ou d'un écrit périodique est une publication proposée au public en dehors de la parution normale, à l'occasion d'un événement ou d'une manifestation importante.</p>
<p>8° Ne pas être susceptibles de choquer le lecteur par une représentation dégradante de la personne humaine portant atteinte à sa dignité et à la décence ou présentant la violence sous un jour favorable.</p>
<p>III. – Les publications d'associations ou de groupements peuvent bénéficier des avantages fiscaux prévus à l'article 298 septies du code général des impôts si elles remplissent les conditions du II, présentent un lien direct avec l'actualité et comportent un contenu original.</p>
''',
"Droit constant : les conditions de contenu journalistique, de parution, de vente et de publicité sont rendues plus lisibles par des phrases distinctes, sans déplacer les alinéas. Les I à III, toutes les conditions du II et les définitions des suppléments et hors-série sont conservés. Aucune réforme de fond des avantages fiscaux de la presse.",
"Conserver les exigences distinctes du I et le régime du III pour les associations et groupements. Contrôles de seuils : une parution au moins par trimestre et au plus quatre mois d'intervalle ; plafond global des deux tiers et plafond propre aux annonces classées de la moitié ; référence au 31 décembre pour les pages ; un numéro thématique annuel pour les trimestriels, deux pour les publications plus fréquentes. Les exclusions du 6°, leurs exceptions et les interdictions de vente ou d'abonnement séparés des suppléments demeurent intégrales. Le 5° bis, les lettres du 6° et les alinéas du 7° restent à leur place pour les renvois, notamment ceux de l'article 73. L'ordonnance du 2 novembre 1945 et les autres références historiques ne sont pas traitées comme des dates de réforme future.")

add('73', '''
<p>Les publications énumérées ci-dessous peuvent bénéficier des avantages fiscaux prévus à l'article 298 septies du code général des impôts si elles remplissent les conditions des 1°, 2° et 3° du II de l'article 72, ne relèvent d'aucune des catégories mentionnées aux a, b, c, d et e du 6° du II de cet article et présentent un lien avec l'actualité. La publicité et les annonces ne doivent pas dépasser 20 % de leur surface totale :</p>
<p>1° Les publications d'anciens combattants, de mutilés ou de victimes de guerre ;</p>
<p>2° Les publications d'information professionnelle éditées par les organisations syndicales représentatives de salariés ;</p>
<p>3° Les publications dont l'objet essentiel est de promouvoir une action ou une philosophie politique, à condition qu'elles ne soient éditées ni par une personne morale de droit public ni pour son compte ;</p>
<p>4° Les publications éditées par les sociétés mutuelles régies par le code de la mutualité ou par les groupements constitués et fonctionnant conformément à ce code ;</p>
<p>5° Les publications à diffusion nationale ou internationale, éditées par des organismes à but non lucratif, dont l'objet est de contribuer, à titre manifestement désintéressé, à la lutte, par des actions ou programmes, contre les atteintes ou menaces graves à la dignité, à la santé et à la vie humaines. Elles doivent être destinées à un public large et diversifié et faire appel au soutien du lecteur ;</p>
<p>6° Les journaux scolaires publiés ou imprimés sous la direction et la responsabilité des instituteurs ou des professeurs, afin d'éduquer les enfants et d'informer les parents d'élèves et les écoles correspondantes sur la vie et le travail de l'école.</p>
''',
"Droit constant : les conditions communes sont exposées avant la liste dans deux phrases, et les conditions propres aux publications politiques et humanitaires sont formulées plus directement. Les six catégories et leurs qualifications sont conservées. Aucune réforme de fond.",
"Le lien avec l'actualité n'est pas transformé en lien direct. Le plafond demeure 20 % pour la publicité et les annonces. Le renvoi d'exclusion ne vise que les lettres a à e du 6° du II de l'article 72, sans ajouter le f ni les autres conditions du II non mentionnées. Maintenir la non-édition par ou pour une personne morale de droit public au 3° et toutes les conditions cumulatives du 5°.")

add('73 A', '''
<p>Pour bénéficier de l'exonération prévue au I de l'article 262 du code général des impôts, le transporteur qui achemine des marchandises vers un port ou un aéroport en vue de leur transbordement à destination d'un État n'appartenant pas à la Communauté européenne ou des collectivités et départements d'outre-mer doit présenter une attestation certifiant la destination des produits. Cette attestation doit être délivrée par le propriétaire de la marchandise, l'expéditeur ou le commissionnaire de transports et visée par le service des impôts dont relève son auteur.</p>
<p>Le premier alinéa s'applique également au transport de marchandises vers un port ou un aéroport en vue de leur transbordement à destination d'un territoire d'un autre État membre de la Communauté mentionnée au 1° de l'article 256-0 du code général des impôts.</p>
''',
"Droit constant : la présentation de l'attestation est distinguée de ses conditions de délivrance et de visa. Le second alinéa conserve l'extension aux territoires mentionnés par le CGI. Aucune réforme de fond de l'exonération de transport.",
"Conserver le transbordement, les trois auteurs possibles de l'attestation et le visa du service des impôts dont ils relèvent. Les termes historiques « Communauté européenne » et « collectivités et départements d'outre-mer » restent ceux du périmètre source ; aucune substitution de champ territorial. Le rattachement grammatical de « mentionnée au 1° » à « Communauté » est ambigu dans la source et reste conservé : le 1° de l'article 256-0 du corpus définit les autres États membres et énumère les territoires exclus, tandis que son 2° définit la Communauté. La portée territoriale du renvoi appelle donc un contrôle, sans correction silencieuse. La note source relative aux articles 5 et 8 de la loi n° 2003-276 du 28 mars 2003 est historique. Les renvois au I de l'article 262 et au 1° de l'article 256-0 sont maintenus.")

add('73 B', '''
<p>Pour les bateaux visés au 2° du II de l'article 262 du code général des impôts, les prestations de services effectuées pour leurs besoins directs sont les suivantes :</p>
<p>– pilotage ;</p>
<p>– remorquage ;</p>
<p>– amarrage ;</p>
<p>– utilisation des installations portuaires ;</p>
<p>– opérations d'entretien du navire et du matériel de bord ;</p>
<p>– gardiennage et services de prévention et de lutte contre l'incendie ;</p>
<p>– visites de sécurité, examens de carènes, expertises techniques ;</p>
<p>– assistance et sauvetage du navire ;</p>
<p>– opérations des courtiers conducteurs et interprètes de navires ;</p>
<p>– opérations des consignataires, gérants de navires et agents maritimes ;</p>
<p>– expertises portant sur l'évaluation des dommages subis par les navires et des indemnités d'assurances destinées à réparer le préjudice qui en résulte.</p>
''',
"Droit constant : le champ des bateaux et le lien avec leurs besoins directs sont placés en tête de la définition, et la dernière prestation est reformulée. Les onze entrées techniques sont maintenues dans leur ordre ; leurs autres désignations sont reprises sans changement. Aucune réforme de fond.",
"Le renvoi au 2° du II de l'article 262 du CGI et la condition de besoins directs sont conservés. La liste ne se confond pas avec celle des prestations à la cargaison de l'article 73 C ; l'expertise couvre les dommages et les indemnités d'assurances.")

add('73 C', '''
<p>Pour les bateaux visés au 2° du II de l'article 262 du code général des impôts, les prestations de services effectuées pour les besoins directs de leur cargaison sont les suivantes :</p>
<p>Chargement et déchargement du bateau ;</p>
<p>Manutention de la marchandise accessoire au chargement et au déchargement du bateau ;</p>
<p>Location de matériel pour le chargement et le déchargement du bateau ;</p>
<p>Location de contenants et de matériel de protection de la marchandise ;</p>
<p>Gardiennage de la marchandise ;</p>
<p>Stationnement et traction des wagons de marchandises sur les voies de quai ;</p>
<p>Magasinage de la marchandise nécessaire au transport par voie d'eau, dans la limite des quinze jours précédant son embarquement ou suivant son débarquement ;</p>
<p>Usage des halles à marée pour la vente aux enchères des produits de la pêche maritime ;</p>
<p>Embarquement et débarquement des passagers et de leurs bagages ;</p>
<p>Location de matériels et d'équipements nécessaires aux opérations d'embarquement et de débarquement des passagers et de leurs bagages ;</p>
<p>Usage des gares maritimes.</p>
<p>Expertises portant sur l'évaluation des dommages subis par les passagers et les marchandises, ainsi que des indemnités d'assurances destinées à réparer le préjudice qui en résulte.</p>
''',
"Droit constant : la phrase d'ouverture précise directement le champ de la liste, la limite de magasinage est resserrée sans être modifiée et la dernière prestation est reformulée. Les douze entrées, y compris celles relatives aux passagers, demeurent dans leur ordre et en alinéas distincts. Aucune réforme de fond.",
"Le magasinage reste nécessaire au transport par voie d'eau et limité aux quinze jours avant l'embarquement ou après le débarquement. La source classe aussi des prestations aux passagers et les gares maritimes dans une liste intitulée besoins de la cargaison : cette discordance de champ est conservée et signalée, sans suppression ni reclassement des alinéas. Maintenir les expertises des dommages et indemnités d'assurances en dernière entrée.")

add('73 D', '''
<p>Pour les aéronefs visés au 4° du II de l'article 262 du code général des impôts, les prestations de services effectuées pour leurs besoins directs sont les suivantes :</p>
<p>– atterrissage et décollage ;</p>
<p>– usage des dispositifs d'éclairage ;</p>
<p>– stationnement, amarrage et abri des aéronefs ;</p>
<p>– usage des installations aménagées pour la réception des passagers et des marchandises ;</p>
<p>– usage des installations destinées à l'avitaillement des aéronefs ;</p>
<p>– opérations techniques afférentes à l'arrivée, au stationnement et au départ des aéronefs ;</p>
<p>– opérations de nettoyage, d'entretien et de réparation de l'aéronef et des matériels et équipements de bord ;</p>
<p>– gardiennage et service de prévention et de lutte contre l'incendie ;</p>
<p>– visites de sécurité, expertises techniques ;</p>
<p>– relevage et sauvetage des aéronefs ;</p>
<p>– opérations des consignataires d'aéronefs et agents aériens.</p>
<p>– expertise portant sur l'évaluation des dommages subis par les aéronefs et des indemnités d'assurances destinées à réparer le préjudice qui en résulte.</p>
''',
"Droit constant : la phrase d'ouverture relie directement les aéronefs concernés à leurs besoins directs, et la formulation de la dernière expertise est clarifiée. Les douze prestations techniques demeurent intégrales et dans le même ordre ; leurs autres désignations sont reprises sans changement. Aucune réforme de fond.",
"Le renvoi reste au 4° du II de l'article 262 du CGI. Conserver notamment les installations d'avitaillement, les opérations techniques aux trois phases, les matériels et équipements de bord et la dernière expertise des dommages et indemnités d'assurances. L'alinéa final reste inclus dans la liste malgré le point qui termine l'entrée précédente dans la source.")


assert len(sources) == len(drafts) == 24
assert {s['number'] for s in sources} == set(drafts)
answer = []
for source in sources:
    xml, reason, notes = drafts[source['number']]
    answer.append({
        'code_id': source['code_id'],
        'source_id': source['source_id'],
        'source_sha256': source['source_sha256'],
        'number': source['number'],
        'proposed_xml': xml,
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
