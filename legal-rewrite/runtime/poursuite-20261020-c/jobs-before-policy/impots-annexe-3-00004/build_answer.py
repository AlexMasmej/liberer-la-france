import json, re, xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
entries = {}

def add(number, xml, reason, notes):
    xml = xml.strip()
    Path('fragments', number.replace(' ', '_') + '.xml').write_text(xml + '\n')
    entries[number] = (xml, reason, notes)

add('10 duodecies', '''
<p>1. En cas de cession ou de cessation d'entreprise ou de décès de l'exploitant, la provision pour hausse des prix inscrite au dernier bilan entre dans le bénéfice immédiatement imposable, dans les conditions fixées par l'article 201 et le 2 de l'article 204 du code général des impôts.</p>
<p>Cette règle s'applique également lorsque l'entreprise a cédé la totalité de son stock et a changé d'objet ou de mode d'exploitation.</p>
<p>En cas de cession d'un établissement ou de cession ou de cessation d'une branche d'activité, la provision pour hausse des prix est rattachée aux bénéfices imposables de l'exercice en cours à la date de la cession ou de la cessation. Ce rattachement porte sur la part de la provision afférente aux matières, produits et approvisionnements qui se rapportent à l'établissement ou à la branche d'activité cédé ou abandonné.</p>
<p>2. Par dérogation au 1, la provision n'est pas rapportée aux bénéfices imposables lorsque l'exploitation du fonds se poursuit dans les conditions prévues aux articles 41 ou 210 du code général des impôts.</p>
<p>Le bénéfice du premier alinéa du présent 2 est subordonné à l'engagement des nouveaux exploitants, de la société absorbante ou nouvelle ou de la société bénéficiaire de l'apport de respecter les obligations suivantes :</p>
<p>a. Inscrire immédiatement à leur passif la provision qui figurait dans les écritures du précédent exploitant, des sociétés fusionnées ou de la société apporteuse et qui était afférente aux éléments transférés. Le montant des dotations de chaque exercice est distingué selon les modalités fixées à l'article 10 decies ;</p>
<p>b. Rattacher ultérieurement ces dotations à leurs bénéfices imposables dans les mêmes conditions que celles qui se seraient appliquées au précédent exploitant en vertu du douzième alinéa du 5° du 1 de l'article 39 du code général des impôts et de l'article 10 undecies.</p>
<p>Cet engagement est joint à la déclaration des résultats de l'exercice de cession, de cessation ou de décès.</p>
''', "Réécriture à droit constant : les événements d'imposition immédiate, la fraction rattachable en cas de cession partielle et les obligations de reprise sont explicités. Les subdivisions 1, 2, a et b sont conservées. Aucune réforme de fond de cette provision.", "Les huit alinéas sont maintenus. Le cumul de la cession de tout le stock et du changement d'objet ou de mode d'exploitation est conservé. Le renvoi au douzième alinéa du 5° du 1 de l'article 39 correspond au délai de reprise dans le corpus fourni. Les articles 41 et 210 ont des champs distincts ; l'article 210 conserve un champ historique, qui n'est ni élargi ni remplacé par l'article 210 A. Vérifier l'applicabilité temporelle lors de la coordination générale.")

add('10 terdecies', '''
<p>1. Les entreprises fournissent au service des impôts, avec la déclaration des résultats de chaque exercice, tous les renseignements utiles au calcul de la provision pour hausse des prix.</p>
<p>Elles indiquent notamment :</p>
<p>a. Les quantités de chaque matière, produit et approvisionnement présents à la clôture de l'exercice et pour lesquels elles entendent constituer une provision ;</p>
<p>b. La valeur unitaire d'inventaire de chaque élément à la clôture de cet exercice, ainsi que ses valeurs unitaires d'inventaire à l'ouverture et à la clôture de l'exercice précédent. Pour le premier et le deuxième exercices arrêtés après le 30 juin 1959, elles indiquent, à la place de ces deux dernières valeurs, son prix de revient unitaire au 30 juin 1959 et sa valeur unitaire d'inventaire à la clôture de l'exercice en cours à cette même date ;</p>
<p>c. Le montant de la dotation au compte « Provision » qu'elles peuvent pratiquer à la clôture de l'exercice considéré ;</p>
<p>d. Le montant de la dotation effectivement pratiquée ;</p>
<p>e. Le cas échéant, le montant de la dotation antérieure rapportée au bénéfice imposable.</p>
<p>2. Les entreprises dont la durée normale de rotation des stocks dépasse trois ans joignent à la déclaration des résultats du troisième exercice arrêté après le 30 juin 1959 une note présentant les différents éléments utilisés pour déterminer cette durée.</p>
''', "Réécriture à droit constant : l'obligation de déclaration et chaque donnée de calcul sont formulées directement ; la variante historique du b est explicitée dans le même alinéa. Aucune réforme de fond ni suppression des renseignements nécessaires au contrôle.", "Les 1 et 2 et les lettres a à e sont conservés, avec leurs huit alinéas. Au b, la mention « à cette dernière date » est explicitée comme visant le 30 juin 1959 ; la clôture de l'exercice en cours à cette date reste distincte du prix de revient à cette date. Les premier, deuxième et troisième exercices arrêtés après cette date et le seuil de trois ans sont maintenus. Ces règles historiques ne fixent aucune entrée en vigueur future.")

add('10 quaterdecies', '''
<p>Pour l'application des dix-neuvième, vingtième, trente-troisième et trente-quatrième alinéas du 5° du 1 de l'article 39 du code général des impôts, les entreprises joignent à leur déclaration de résultat de chaque exercice un état conforme au modèle fourni par l'administration. Cet état assure le suivi des provisions pour dépréciation des titres de participation et des immeubles de placement qui ne sont pas admises en déduction.</p>
''', "Réécriture à droit constant : l'obligation de joindre l'état et son objet sont présentés en deux phrases dans le même alinéa. Aucun changement des provisions concernées ni réforme de leur déductibilité.", "Incohérence préexistante à coordonner : dans l'article 39 du corpus fourni, le trente-troisième alinéa du 5° du 1 traite du risque de change et les dispositions sur les immeubles de placement figurent aux trente-quatrième et trente-cinquième alinéas. Les quatre renvois de la source sont néanmoins conservés sans correction silencieuse. Les dix-neuvième et vingtième alinéas concernent bien les titres de participation. La note source relative à l'article 26-I [c] de la loi n° 2013-1278 du 29 décembre 2013 est historique.")

add('10 G-0 bis', '''
<p>Pour l'application de l'article 39 bis A du code général des impôts, la commission paritaire des publications et agences de presse donne un avis lorsqu'elle est saisie par les services fiscaux compétents ou les entreprises concernées. Cet avis porte sur le respect, par les publications et les services de presse en ligne, des critères prévus à l'article 17 de l'annexe II à ce code.</p>
''', "Réécriture à droit constant : la mission consultative et la condition de saisine sont exprimées directement ; une seconde phrase précise l'objet de l'avis. Aucune réforme de fond du régime de la presse.", "Les deux voies de saisine et les deux renvois sont conservés ; l'avis reste subordonné à une saisine et ne devient pas une décision d'agrément. L'article 17 de l'annexe II a été vérifié dans le corpus. La note de création cite l'article 1-1 du décret n° 97-1065 du 20 novembre 1997 et le décret n° 2009-1423 du 19 novembre 2009 : ces dates sont des références historiques, non le calendrier du projet.")

add('10 GA', '''
<p>Les établissements de crédit et les sociétés de financement bénéficient de l'application de l'article 39 octies A du code général des impôts lorsqu'ils sont enregistrés par l'Autorité de contrôle prudentiel et de résolution et habilités à réaliser des opérations de crédit ou de crédit-bail au profit des entreprises.</p>
''', "Réécriture à droit constant : les deux catégories d'organismes deviennent le sujet de la phrase et les conditions d'enregistrement et d'habilitation sont explicites. Aucun nouveau droit à provision ni réforme de fond.", "Le renvoi à l'article 39 octies A est conservé avec toutes les limites de ce texte, notamment les agréments et bornes historiques des investissements, vérifiés dans le corpus. La formulation n'ouvre pas le régime à de nouveaux investissements ni ne l'étend aux comptes de retraite du projet.")

add('10 GA bis', '''
<p>I. – Les éléments du bilan de départ mentionné au III de l'article 39 octies D du code général des impôts sont retenus pour la valeur qu'ils avaient, au regard de la législation fiscale française, à la date d'ouverture de l'exercice au cours duquel l'entreprise française acquiert le capital. Cette valeur est exprimée en monnaie locale.</p>
<p>Les immobilisations sont inscrites au bilan pour leur valeur d'origine. Pour chaque immobilisation amortissable, le compte d'amortissement est crédité du total des amortissements qui auraient été déductibles selon les règles fiscales françaises depuis la date à laquelle la filiale étrangère a acquis le bien.</p>
<p>Les immobilisations dont la durée d'utilisation n'est pas achevée continuent d'être amorties sur leur valeur d'origine, selon les mêmes modalités que celles retenues pour calculer les amortissements mentionnés au deuxième alinéa.</p>
<p>II. – Les éléments du bilan de départ et des bilans suivants qui correspondent à des établissements ou à des participations dans des filiales sont inscrits dans des comptes spéciaux lorsque ces établissements ou filiales remplissent les deux conditions suivantes : ils ont pour objet l'activité de commercialisation définie aux I et IV de l'article 39 octies D du code général des impôts et sont situés dans un État autre que celui du siège de la filiale mentionnée à cet article.</p>
<p>Les provisions et les charges à payer qui ne sont pas déductibles du résultat en application du code général des impôts sont inscrites séparément au passif du bilan de la filiale étrangère.</p>
''', "Réécriture à droit constant : la date et la monnaie d'évaluation, les amortissements reconstitués et les conditions de tenue des comptes spéciaux sont clarifiés, en conservant les cinq alinéas et les I et II. Aucune réforme de fond des règles d'évaluation.", "Le deuxième alinéa reste celui des amortissements reconstitués, visé au troisième alinéa. Les deux conditions du II sont cumulatives. La source vise une activité de commercialisation aux I et IV de l'article 39 octies D, alors que le IV du CGI fourni concerne des prestations de services : cette discordance terminologique préexistante est conservée et doit être coordonnée. Les limites historiques de l'article 39 octies D, dont la fermeture aux investissements postérieurs au 31 décembre 2003 pour le I et la date de demande d'agrément du IV, ne sont pas supprimées.")

add('10 GA ter', '''
<p>Les résultats de la filiale étrangère mentionnés au III de l'article 39 octies D du code général des impôts correspondent aux pertes subies et aux bénéfices réalisés au titre de l'activité définie au I du même article, dans l'État où se situe le siège de cette filiale.</p>
<p>Les plus-values et les moins-values résultant de la cession d'immobilisations sont exclues du calcul de ces pertes ou bénéfices.</p>
<p>Sont également exclus les résultats des opérations réalisées par les établissements ou les filiales mentionnés au II de l'article 10 GA bis, ainsi que les charges ou les produits résultant de leur détention.</p>
<p>Les résultats mentionnés au premier alinéa sont convertis en euros au taux de change en vigueur à la clôture de l'exercice de la filiale étrangère.</p>
''', "Réécriture à droit constant : les deux exclusions sont formulées directement et la règle de conversion est allégée. Les quatre alinéas et le champ territorial et matériel des résultats restent identiques ; aucune réforme de fond.", "Les exclusions des plus-values comme des moins-values et des charges comme des produits sont préservées. La date de conversion est celle de la clôture de la filiale étrangère, non celle de l'entreprise française. Le premier alinéa reste la cible du dernier alinéa ; les renvois au III et au I de l'article 39 octies D et au II de l'article 10 GA bis sont maintenus.")

add('10 GA quater', '''
<p>Les entreprises qui constituent des provisions en application de l'article 39 octies A du code général des impôts joignent à la déclaration de résultats de chaque exercice les documents suivants :</p>
<p>Pour les filiales situées dans un État qui n'est pas membre de la Communauté européenne, un bilan dont la traduction est certifiée par un traducteur juré ;</p>
<p>Pour chaque filiale située dans un État de la Communauté européenne, outre le bilan de départ établi dans les conditions de l'article 10 GA bis :</p>
<p>a) Un bilan et un compte de résultats issus des comptes sociaux, certifiés par un commissaire aux comptes de l'État d'implantation ;</p>
<p>b) Un bilan et un compte de résultats déterminés dans les conditions prévues à l'article 10 GA ter ;</p>
<p>c) Des états détaillant les immobilisations, les amortissements et les provisions figurant au bilan de la filiale étrangère défini au b ;</p>
<p>d) Un état détaillé des rectifications apportées au résultat étranger pour le rendre conforme au code général des impôts ;</p>
<p>e) Un état présentant la répartition du capital à la clôture de chaque exercice de la filiale.</p>
<p>Ces renseignements sont présentés sur des documents conformes au modèle établi par l'administration.</p>
''', "Réécriture à droit constant : les pièces exigées et leurs certifications sont exprimées plus directement, sans déplacer les lettres a à e ni les deux branches géographiques. Aucune réforme de fond du suivi des provisions.", "Les neuf alinéas sont conservés. La traduction certifiée du bilan hors Communauté européenne reste distincte de la certification des comptes sociaux du a. Le renvoi du b à l'article 10 GA ter et l'exigence supplémentaire du bilan de départ sont maintenus. L'appellation historique « Communauté européenne » est conservée pour éviter une modification implicite du champ de régimes anciens. L'extension aux établissements et filiales de l'article 39 octies D reste portée par l'article 10 GA sexies.")

add('10 GA quinquies', '''
<p>Les établissements et les filiales mentionnés aux I et IV de l'article 39 octies D du code général des impôts sont soumis aux règles des articles 10 GA bis et 10 GA ter.</p>
''', "Réécriture à droit constant : les établissements et filiales sont placés en sujet de la règle d'application. Les deux articles applicables et les deux subdivisions du CGI sont conservés ; aucune réforme de fond.", "L'application aux établissements comme aux filiales reste limitée aux I et IV de l'article 39 octies D. Ce renvoi ne rouvre pas les régimes historiques aux investissements nouveaux et ne vise pas les dispositifs de capitalisation de retraite du projet.")

add('10 GA sexies', '''
<p>I. – Les établissements et les filiales mentionnés aux I et IV de l'article 39 octies D du code général des impôts sont soumis aux dispositions de l'article 10 GA quater relatives aux filiales situées dans un État de la Communauté européenne.</p>
<p>II. – Pour les établissements et les filiales mentionnés au I, les documents prévus au a de l'article 10 GA quater doivent, en outre, être certifiés par un traducteur juré.</p>
''', "Réécriture à droit constant : les destinataires de l'extension documentaire et le caractère supplémentaire de la certification par traducteur juré sont explicites. Les I et II restent distincts ; aucune réforme de fond.", "Le renvoi vise seulement la branche de l'article 10 GA quater relative à la Communauté européenne, puis les documents de son a. La certification par traducteur juré s'ajoute à celle du commissaire aux comptes. L'appellation historique et les limites du régime de l'article 39 octies D sont préservées.")

add('10 H', '''
<p>Le remploi prévu à l'article 40 du code général des impôts ne peut pas financer l'acquisition des biens meubles ou immeubles de caractère somptuaire énumérés ci-dessous, sauf si ces biens sont acquis dans l'intérêt de l'ensemble du personnel de l'entreprise :</p>
<p>1° Les terrains de chasse ou de pêche et toutes les autres immobilisations correspondantes ;</p>
<p>2° Les résidences de plaisance ou d'agrément, à l'exception des immeubles classés dans les conditions prévues à l'article 1er de la loi du 31 décembre 1913 sur les monuments historiques ;</p>
<p>3° Les yachts ou les bateaux de plaisance à voile ou à moteur ;</p>
<p>4° Les voitures de tourisme, pour la fraction de leur prix d'acquisition qui dépasse 3 049 € ;</p>
<p>5° Les bijoux et les objets d'art, à l'exception des objets mobiliers classés dans les conditions prévues à l'article 14 de la loi du 31 décembre 1913 précitée, modifié par l'article unique de la loi n° 46-985 du 10 mai 1946 ;</p>
<p>6° Les terrains ou les locaux destinés à la pratique de sports et les installations correspondantes.</p>
''', "Réécriture à droit constant : l'interdiction de remploi et son exception pour l'ensemble du personnel sont formulées directement ; les six catégories restent énumérées. Aucune réforme de fond ni exonération nouvelle du réinvestissement.", "Le seuil de 3 049 € ne concerne que la fraction du prix des voitures qui le dépasse. Les deux exceptions patrimoniales et les références aux articles 1er et 14 de la loi du 31 décembre 1913 et à la loi n° 46-985 du 10 mai 1946 sont conservées ; leur coordination avec le code du patrimoine est à contrôler sans substitution implicite. Le corpus confirme le caractère historique de l'article 40, dont les dispositions conservées servent à l'application de l'article 238 octies. Aucun régime général nouveau de remploi n'est créé.")

add('10 H-0 bis', '''
<p>Les états prévus aux b, c et d du IV de l'article 41 du code général des impôts sont établis selon les modèles fixés par l'administration. Ils indiquent notamment les noms et adresses des bénéficiaires concernés, ainsi que la dénomination commerciale et l'adresse de l'entreprise transmise. Pour tous les biens immobilisés compris dans la transmission, ils détaillent, par nature d'élément, les informations nécessaires au suivi des plus-values en report d'imposition.</p>
''', "Réécriture à droit constant : les données d'identification et les informations de suivi sont réparties en phrases courtes dans l'alinéa unique. Aucune réforme de fond du report d'imposition.", "Les trois états visés aux b, c et d du IV de l'article 41 sont conservés, de même que la totalité des biens immobilisés transmis et le classement par nature d'élément. Le renvoi a été vérifié dans le corpus ; aucun état ni bénéficiaire supplémentaire n'est ajouté.")

add('10 H bis', '''
<p>L'article 238 octies du code général des impôts ne s'applique plus aux profits de construction provenant de la cession d'immeubles lorsque le permis de construire a été délivré, ou la déclaration qui en tient lieu déposée, après le 31 décembre 1971.</p>
''', "Réécriture à droit constant : les deux événements qui excluent l'application du régime sont formulés avec des verbes explicites. Aucune réforme de fond des profits de construction.", "La date du 31 décembre 1971 et son caractère strictement postérieur sont maintenus. Pour le permis, la date pertinente reste sa délivrance ; pour la déclaration, elle reste son dépôt. La règle historique n'est pas appliquée à une date future de réforme.")

add('10 K', '''
<p>Les établissements hôteliers ou thermaux relèvent du 1 de l'article 42 septies du code général des impôts dans les conditions fixées par l'article 21 du décret n° 97-663 du 29 mai 1997, pris pour l'application de l'article 34 de la loi n° 95-1347 du 30 décembre 1995 de finances rectificative pour 1995.</p>
''', "Réécriture à droit constant : les établissements concernés deviennent le sujet de la phrase et l'articulation avec le décret d'application est allégée. Aucune réforme de fond du régime des subventions.", "Les deux catégories d'établissements et les renvois au 1 de l'article 42 septies, à l'article 21 du décret n° 97-663 et à l'article 34 de la loi n° 95-1347 sont intégralement conservés. La note source rattache la modification à ce décret de 1997 ; elle ne constitue ni une date de réforme future ni une suppression d'aide au titre de policy.json. Les textes hors corpus demeurent à vérifier lors de la consolidation.")

# Article 21 : fragments textuels rédigés et deux tableaux complets, sans attribut de présentation.
a21 = next(a for a in sources if a['number'] == '21')
root = ET.fromstring('<root>' + a21['source_xml'] + '</root>')
tables = root.findall('table')
assert len(tables) == 2
parts = [('21_01_intro.xml', '<p>Pour la révision des bilans des exercices clos le 29 décembre 1959, les coefficients applicables sont ceux des tableaux suivants :</p>\n<p>a. Pour les biens situés dans la métropole ou dans les départements de la Guadeloupe, de la Guyane et de la Martinique :</p>')]
for i, table in enumerate(tables):
    for node in table.iter():
        node.attrib.clear()
        if node.text and node.text.strip() == '1914 et antér':
            node.text = '1914 et années antérieures'
    parts.append((f'21_0{2+i*2}_table.xml', ET.tostring(table, encoding='unicode').strip()))
    if i == 0:
        parts.append(('21_03_b.xml', '<p>b. Pour les biens situés dans le département de la Réunion :</p>'))
for filename, xml in parts:
    Path('fragments', filename).write_text(xml + '\n')
add('21', '\n'.join(Path('fragments', filename).read_text().strip() for filename, _ in parts), "Réécriture à droit constant de la règle introductive et des deux champs territoriaux ; l'abréviation de la première période est développée. Les deux tableaux sont reproduits intégralement, avec toutes les années, coefficients et cellules vides. Aucune réforme de fond ni actualisation des coefficients historiques.", "Contrôle cellule par cellule des deux tableaux : chacun conserve 13 lignes et 8 colonnes, soit 46 couples année-coefficient et les cellules finales vides. Les séries territoriales restent distinctes, notamment 243 contre 121,5 pour 1914 et les années antérieures. Les virgules décimales, les zéros de 1,20 et les coefficients de 1959 sont conservés. La clôture du 29 décembre 1959, les lettres a et b et les quatre territoires du a restent identiques ; aucune conversion ni indexation nouvelle. Seuls les attributs de présentation interdits ont été retirés.")

add('38', '''
<p>I. – La déclaration prévue aux articles 53 A et 302 septies A bis du code général des impôts et ses annexes bis et ter comportent les renseignements suivants :</p>
<p>a. La récapitulation des éléments qui concourent à la détermination du résultat et le montant des recettes nettes soumises à la contribution mentionnée à l'article 234 nonies du code général des impôts ;</p>
<p>b. Le nom et l'adresse du ou des comptables ou experts chargés de tenir la comptabilité ou d'en contrôler les résultats généraux, avec l'indication de leur appartenance ou non au personnel salarié de l'entreprise ;</p>
<p>c. Le cas échéant, le nom et l'adresse du centre de gestion agréé auquel le contribuable a adhéré ;</p>
<p>d. Les renseignements nécessaires à l'établissement et au contrôle de l'impôt.</p>
<p>I bis. – (Sans objet).</p>
<p>II. – Les contribuables mentionnés à l'article 53 A du code général des impôts joignent à la déclaration et aux annexes mentionnées au I le bilan, le compte de résultat, le tableau des immobilisations, le tableau des amortissements, le tableau des provisions et l'état des échéances des créances et des dettes.</p>
<p>Ils joignent également :</p>
<p>1° La liste des personnes qui détiennent au moins 10 % de leur capital, établie selon le modèle fourni par l'administration. Cette liste précise, pour chacune d'elles, le nombre de parts ou d'actions et le taux de détention. Elle indique, pour les personnes morales, leur dénomination, leur adresse et leur numéro d'identification au répertoire national des établissements (numéro SIRET) et, pour les personnes physiques, leurs nom, prénoms, adresse, date et lieu de naissance ;</p>
<p>2° La liste de leurs filiales et de leurs participations, établie selon le modèle fourni par l'administration, avec, pour chacune d'elles, le taux de détention et le numéro d'identification au répertoire national des établissements (numéro SIRET) ;</p>
<p>3° Lorsqu'ils sont soumis à l'obligation prévue au II de l'article 1586 octies du code général des impôts, le tableau de calcul de la valeur ajoutée définie à l'article 1586 sexies de ce code, établi selon le modèle fourni par l'administration ;</p>
<p>4° Des informations détaillées sur les points suivants :</p>
<p>a. Les dérogations aux prescriptions comptables ;</p>
<p>b. Les modifications des méthodes d'évaluation et de la présentation des comptes annuels ;</p>
<p>c. Les produits à recevoir et les charges à payer ;</p>
<p>d. Les produits et les charges inscrits au bilan sous les postes de comptes de régularisation.</p>
<p>Les contribuables qui ont la qualité de commerçant produisent, à la demande de l'administration, les éléments de l'annexe comptable qui ne sont pas énumérés ci-dessus.</p>
<p>Les contribuables mentionnés au premier alinéa du présent II joignent en outre à la déclaration le tableau de détermination du résultat fiscal, l'état des déficits et des provisions non déductibles, l'état des renseignements divers, le tableau des éléments soumis au régime fiscal des plus-values et moins-values et, le cas échéant, le tableau des écarts de réévaluation.</p>
<p>III. – Les contribuables mentionnés à l'article 302 septies A bis du code général des impôts joignent à la déclaration et aux annexes mentionnées au I le bilan et le compte de résultats simplifiés, les tableaux des immobilisations, des amortissements et des éléments soumis au régime fiscal des plus-values et moins-values, le relevé des provisions, le relevé des provisions non déductibles, l'état des déficits et, le cas échéant, le tableau des écarts de réévaluation.</p>
<p>Les personnes morales joignent également :</p>
<p>1° La liste des personnes qui détiennent au moins 10 % de leur capital, établie selon le modèle fourni par l'administration. Cette liste précise, pour chacune d'elles, le nombre de parts ou d'actions et le taux de détention. Elle indique, pour les personnes morales, leur dénomination, leur adresse et leur numéro d'identification au répertoire national des établissements (numéro SIRET) et, pour les personnes physiques, leurs nom, prénoms, adresse, date et lieu de naissance ;</p>
<p>2° La liste de leurs filiales et de leurs participations, établie selon le modèle fourni par l'administration, avec, pour chacune d'elles, le taux de détention et le numéro d'identification au répertoire national des établissements (numéro SIRET).</p>
<p>IV. – Les déclarations et les documents qui y sont joints sont transmis au service des impôts du siège de la direction de l'entreprise ou, à défaut, du lieu du principal établissement. Ils sont transmis par voie électronique dans les cas prévus à l'article 1649 quater B quater du code général des impôts ; dans les autres cas, un seul exemplaire est remis.</p>
<p>Par dérogation aux règles de compétence du service destinataire prévues au premier alinéa :</p>
<p>1° Les personnes physiques qui exercent une activité professionnelle dans la Principauté de Monaco déposent leur déclaration auprès du service désigné par le ministre chargé du budget ;</p>
<p>2° Les sociétés dont l'objet est la construction d'immeubles en vue de la vente et dont l'activité porte sur un seul immeuble ou groupe d'immeubles souscrivent cette déclaration auprès du service des impôts du lieu de situation des constructions.</p>
<p>Le service délivre un récépissé à la demande du contribuable.</p>
<p>Pour satisfaire aux obligations des I à III, l'administration réutilise les renseignements et documents qu'elle détient déjà légalement lorsque leur utilisation à cette fin est autorisée et respecte les secrets protégés par la loi. Elle les met à la disposition du contribuable, qui les vérifie et, si nécessaire, les corrige ou les complète avant le dépôt de sa déclaration. Cette réutilisation satisfait à l'obligation de fournir les mêmes renseignements et documents dès lors qu'ils sont complets, à jour et se rapportent au même objet et à la même période ; l'administration n'en demande alors pas une nouvelle production. Elle prend en compte les corrections dans les données dont elle assure la tenue. Le contribuable reste tenu de déposer sa déclaration et de fournir les renseignements et documents manquants ou qui ne peuvent pas être légalement réutilisés.</p>
''', "Réécriture à droit constant des rubriques et pièces des I à III : sujets explicites, listes complètes et phrases plus courtes. Réforme de fond au IV conforme à l'orientation « Déclarer une fois, corriger à la source » : réutilisation des données déjà légalement détenues avec vérification, correction et compléments, suppression des demandes identiques satisfaites et du double exemplaire résiduel. Le dépôt électronique est coordonné avec l'article 1649 quater B quater existant. Aucun changement d'assiette ou de taux.", "Les 27 alinéas d'origine sont conservés dans leur ordre, avec un alinéa ajouté à la fin du IV ; son premier alinéa reste la cible de la dérogation, expressément limitée à la compétence du service destinataire pour ne pas écarter la transmission électronique. Toutes les pièces, le seuil d'au moins 10 %, les identifications SIRET, les personnes soumises à chaque liste et les deux services dérogatoires sont maintenus. L'ancien double exemplaire est incohérent avec le dépôt électronique du II de l'article 1649 quater B quater vérifié dans le corpus : coordination explicite, et un seul exemplaire dans les autres cas au titre de la simplification. Le III conserve l'exigence de bilan de la source : l'articulation préexistante avec la dispense du VI de l'article 302 septies A bis doit être précisée sans supprimer cette dispense légale. Le dernier alinéa constitue une réforme nouvelle, limitée aux obligations des I à III ; vérifier les habilitations d'échange, le secret fiscal et les droits de rectification au regard du livre des procédures fiscales, du code des relations entre le public et l'administration et des règles de protection des données, hors des cinq codes. Adapter les modèles et les procédures existants ; aucune dérogation générale aux secrets ni aucun nouveau portail. Les renvois à la CVAE sont conservés sans anticiper une extinction ou modifier son calendrier.")

add('38 A', '''
<p>Les entreprises présentent hors taxes le compte de résultat prévu à l'article 38.</p>
''', "Réécriture à droit constant : les entreprises deviennent le sujet explicite de l'obligation de présentation hors taxes. Aucune réforme de fond.", "L'exigence « hors taxes » et le renvoi à l'article 38 de la présente annexe sont conservés. Ce renvoi ne vise pas l'article 38 du CGI.")

add('38 B', '''
<p>Pour l'application du 9 de l'article 38 du code général des impôts, les entreprises joignent à la déclaration de leurs résultats de chaque exercice un état établi sur un document conforme au modèle fixé par l'administration.</p>
<p>Pour chaque participation, cet état indique notamment le prix d'acquisition, la valeur réelle, la valeur d'équivalence et le montant de la dépréciation définie au dix-septième alinéa du 5° du 1 de l'article 39 de ce code.</p>
''', "Réécriture à droit constant : le contenu de l'état est formulé avec chaque participation en tête de phrase ; l'obligation déjà directement rédigée du premier alinéa est conservée. Aucune réforme de fond de l'évaluation ou de la dépréciation.", "Les deux alinéas, la périodicité annuelle et les quatre données par participation sont conservés. Le 9 de l'article 38 et le dix-septième alinéa du 5° du 1 de l'article 39 du CGI ont été vérifiés dans le corpus. La note de modification liée à l'article 26-I [c] de la loi n° 2013-1278 du 29 décembre 2013 est historique.")

add('38 ter', '''
<p>Le stock comprend les éléments qui appartiennent à l'entreprise à la date de l'inventaire et dont la vente, en l'état ou à l'issue d'un processus de production à venir ou en cours, permet de réaliser un bénéfice d'exploitation. Il s'agit de l'ensemble des marchandises, des matières premières, des matières et fournitures consommables, des productions en cours, des produits intermédiaires, des produits finis, des produits résiduels et des emballages non destinés à être récupérés.</p>
<p>Les productions en cours sont les biens ou les services en cours de formation dans un processus de production.</p>
<p>Les produits intermédiaires sont ceux qui ont atteint un stade d'achèvement et sont destinés à entrer dans une nouvelle phase du cycle de production.</p>
<p>Les produits finis sont ceux qui ont atteint le stade d'achèvement définitif du cycle de production.</p>
<p>Les produits résiduels comprennent les déchets et les rebuts de fabrication.</p>
<p>Les emballages commerciaux comprennent les emballages perdus, destinés à être livrés avec leur contenu sans consignation ni reprise, et les emballages récupérables, que la clientèle peut conserver provisoirement et que le livreur s'engage à reprendre dans des conditions déterminées. En principe, seuls les emballages perdus sont inclus dans les stocks ; les emballages récupérables constituent normalement des immobilisations. Toutefois, les emballages récupérables peuvent être assimilés à des stocks lorsqu'ils ne sont pas commodément identifiables.</p>
''', "Réécriture à droit constant : les deux conditions d'appartenance au stock sont explicitées, les définitions sont allégées et la règle des emballages est divisée en phrases courtes. Les six alinéas sont conservés ; aucune réforme de fond.", "Toutes les catégories de stock sont maintenues, y compris les services en cours de formation et les produits résiduels. La propriété est appréciée à la date de l'inventaire et les processus futurs comme en cours restent inclus. L'exception d'assimilation des emballages récupérables non commodément identifiables demeure facultative ; la qualification normale d'immobilisation n'est pas rendue absolue.")

add('38 quater', '''
<p>Les entreprises appliquent les définitions du plan comptable général, sauf lorsqu'elles sont incompatibles avec les règles de détermination de l'assiette de l'impôt.</p>
''', "Réécriture à droit constant : l'obligation et la réserve de compatibilité fiscale sont formulées directement. Aucune réforme de fond des normes comptables ou fiscales.", "La réserve demeure limitée à l'incompatibilité avec les règles d'assiette ; la phrase n'autorise pas à écarter librement le plan comptable général.")

add('38 quinquies', '''
<p>1. Les immobilisations sont inscrites au bilan pour leur valeur d'origine.</p>
<p>La valeur d'origine est déterminée comme suit :</p>
<p>a. Pour les immobilisations acquises à titre onéreux, elle correspond au coût d'acquisition. Ce coût comprend le prix d'achat, diminué des remises, rabais commerciaux et escomptes de règlement obtenus, et augmenté des coûts directement engagés pour mettre le bien en état d'utilisation ainsi que des coûts d'emprunt dans les conditions prévues à l'article 38 undecies.</p>
<p>Sous réserve du VII de l'article 209 du code général des impôts, l'entreprise choisit soit de porter à l'actif du bilan les droits de mutation, honoraires ou commissions et frais d'acte liés à l'acquisition, en les ajoutant au coût d'acquisition de l'immobilisation concernée, soit de les déduire immédiatement en charges. Elle exerce ce choix distinctement pour les titres immobilisés et les titres de placement, d'une part, et pour les autres immobilisations acquises, d'autre part. Ce choix est irrévocable.</p>
<p>Pour les biens acquis moyennant le paiement d'une rente viagère, le prix d'achat est le prix stipulé ou, à défaut, la valeur réelle du bien estimée au jour de l'acquisition.</p>
<p>Pour les biens acquis en échange d'un ou de plusieurs biens, le prix d'achat correspond à la valeur vénale ;</p>
<p>b. Pour les immobilisations acquises à titre gratuit, la valeur d'origine correspond à la valeur vénale ;</p>
<p>c. Pour les immobilisations apportées à l'entreprise par des tiers, elle correspond à la valeur d'apport ;</p>
<p>d. Pour les immobilisations créées par l'entreprise, elle correspond au coût d'acquisition des matières ou fournitures consommées, augmenté de toutes les charges directes ou indirectes de production ainsi que des coûts d'emprunt dans les conditions prévues à l'article 38 undecies.</p>
<p>Les coûts administratifs sont exclus des coûts d'acquisition et de production définis ci-dessus, à l'exception du coût des structures dédiées.</p>
<p>2. La valeur d'origine des immobilisations définie au 1 est augmentée des coûts engagés pour remplacer les composants mentionnés à l'article 15 bis de l'annexe II. La valeur nette comptable du composant remplacé est comptabilisée en charges.</p>
''', "Réécriture à droit constant : chaque mode d'acquisition est relié explicitement à sa valeur d'origine ; le calcul du coût et l'option irrévocable sont rendus plus lisibles. Les 1 et 2, les lettres a à d et les onze alinéas sont conservés. Aucune réforme de fond des amortissements ou des coûts d'entrée.", "Le quatrième alinéa du 1 reste celui de l'option, cible de l'article 38 septies. Les titres immobilisés et de placement constituent ensemble une catégorie d'option, distincte des autres immobilisations. La réserve du VII de l'article 209, vérifiée dans le corpus, préserve le traitement spécifique des frais d'acquisition des titres de participation. L'article 38 undecies et l'article 15 bis de l'annexe II ont été vérifiés ; l'option sur les coûts d'emprunt, l'exception pour les structures dédiées et la sortie en charges du composant remplacé sont conservées. Aucun avantage fiscal nouveau pour les bénéfices réinvestis.")

add('38 sexies', '''
<p>Pour les immobilisations dont la dépréciation n'est pas irréversible, les entreprises constituent des provisions pour dépréciation dans les conditions prévues au 5° du 1 de l'article 39 du code général des impôts.</p>
''', "Réécriture à droit constant : les entreprises deviennent le sujet explicite et le caractère réversible de la dépréciation est exprimé directement. Aucune réforme de fond de la déductibilité.", "La règle reste limitée aux immobilisations qui ne se déprécient pas de manière irréversible et soumise à toutes les conditions du 5° du 1 de l'article 39. Elle ne crée pas de provision automatique indépendante de ces conditions.")

add('38 septies', '''
<p>Les valeurs mobilières qui constituent des titres de placement sont inscrites au bilan pour leur valeur d'origine, augmentée des droits de mutation, honoraires ou commissions et frais d'acte liés à leur acquisition, sous réserve de l'option mentionnée au quatrième alinéa du 1 de l'article 38 quinquies.</p>
<p>À la fin de chaque exercice, l'entreprise estime la valeur de ces titres.</p>
<p>Elle évalue les titres cotés au cours moyen du dernier mois de l'exercice et les titres non cotés à leur valeur probable de négociation.</p>
<p>Sont considérées comme des titres cotés les valeurs inscrites admises aux négociations sur un marché réglementé.</p>
<p>Pour chaque catégorie de titres de même nature, les plus-values ou moins-values issues de cette estimation sont appréciées par rapport à la valeur d'origine globale de l'ensemble de ces titres.</p>
<p>L'entreprise ne comptabilise pas les plus-values. Elle inscrit les moins-values au compte de provisions.</p>
<p>Toutefois, lorsque certains titres cotés subissent une baisse anormale qui apparaît momentanée, l'entreprise peut, sous sa responsabilité, exclure de la provision tout ou partie de la moins-value constatée sur ces titres. Cette exclusion n'est possible que dans la mesure où une compensation peut être établie avec les plus-values normales constatées sur d'autres titres.</p>
''', "Réécriture à droit constant : l'entreprise est désignée pour les opérations d'évaluation et de comptabilisation ; l'exception de baisse anormale est divisée en deux phrases. Les sept alinéas sont conservés ; aucune réforme de fond de l'évaluation du portefeuille.", "Le quatrième alinéa du 1 de l'article 38 quinquies conserve son rang dans la proposition correspondante. Le cours moyen porte sur le dernier mois entier de l'exercice, non sur sa seule clôture. La catégorie de même nature, l'absence de comptabilisation des plus-values et la responsabilité de l'entreprise restent inchangées. L'exception exige cumulativement une baisse anormale d'apparence momentanée et une compensation établie avec des plus-values normales sur d'autres titres ; aucune compensation générale nouvelle. L'expression préexistante « valeurs inscrites admises » est conservée sans modifier le périmètre du marché réglementé.")

add('38 octies', '''
<p>Les cessions de titres en portefeuille sont réputées concerner d'abord les titres de même nature acquis ou souscrits à la date la plus ancienne.</p>
<p>Les plus-values ou moins-values résultant de ces cessions sont calculées à partir de la valeur d'origine pour laquelle les titres étaient inscrits au bilan.</p>
''', "Réécriture à droit constant : la priorité des titres les plus anciens et la base du calcul des résultats de cession sont formulées plus directement. Les deux alinéas sont conservés ; aucune réforme de fond.", "La priorité vise les titres de même nature et couvre à la fois les acquisitions et les souscriptions. La base reste la valeur d'origine inscrite au bilan ; aucune méthode de coût moyen ni valeur de marché n'est substituée.")

assert len(entries) == len(sources) == 24
answer=[]
for source in sources:
    xml, reason, notes = entries[source['number']]
    item={k:source[k] for k in ('code_id','source_id','source_sha256','number')}
    item.update(proposed_xml=xml, reason=reason, review_notes=notes, status='rewrite_draft')
    answer.append(item)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print('Articles écrits :',len(answer))
print('Caractères proposés :',sum(len(a['proposed_xml']) for a in answer))
