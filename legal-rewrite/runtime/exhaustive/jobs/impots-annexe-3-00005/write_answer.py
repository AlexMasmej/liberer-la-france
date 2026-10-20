import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
drafts = {}

def add(number, proposed_xml, reason, review_notes):
    drafts[number] = (proposed_xml, reason, review_notes)

add('38 nonies', '''<p>1. Au jour de l'inventaire, les marchandises, matières premières, matières et fournitures consommables, emballages perdus, produits en stock et productions en cours sont évalués à leur coût de revient. Ce coût est déterminé comme suit :</p>
<p>a. Pour les biens acquis à titre onéreux, il correspond au prix d'achat, diminué des remises, rabais commerciaux et escomptes de règlement obtenus. Ce prix est augmenté des frais de transport, de manutention et des autres coûts directement engagés pour acquérir les biens, ainsi que des coûts d'emprunt dans les conditions prévues à l'article 38 undecies ;</p>
<p>b. Pour les biens produits par l'entreprise, il correspond au coût de production. Celui-ci comprend les coûts directement engagés pour la production, les frais indirects de production, variables ou fixes, ainsi que les coûts d'emprunt dans les conditions prévues à l'article 38 undecies. La quote-part de charges correspondant à la sous-activité ne peut pas être incorporée au coût de production.</p>
<p>Les coûts administratifs sont exclus du coût d'acquisition et du coût de production ainsi définis, sauf le coût des structures dédiées.</p>
<p>2. Le coût des stocks est déterminé en identifiant spécifiquement les coûts individuels. Ces coûts sont fournis par la comptabilité analytique ou, à défaut, déterminés par des calculs ou des évaluations statistiques.</p>''',
"Réécriture à droit constant : la date d'évaluation est placée en tête, les composantes du coût des biens acquis et produits sont exposées dans des phrases distinctes et la méthode d'identification des coûts est explicitée. Aucune réforme de fond n'est appliquée aux règles d'évaluation des stocks.",
"Maintien des subdivisions 1, a, b et 2, des cinq alinéas, du renvoi à l'article 38 undecies dans chacun des a et b, de l'exclusion des charges de sous-activité et de l'exception relative aux structures dédiées. Le recours aux calculs ou évaluations statistiques reste subsidiaire à la comptabilité analytique.")

add('38 decies', '''<p>L'entreprise doit constituer des provisions pour dépréciation lorsque le cours du jour, à la date de l'inventaire, est inférieur au coût de revient défini à l'article 38 nonies pour les biens suivants en stock à cette date : marchandises, matières premières, matières et fournitures consommables, produits intermédiaires, produits finis et emballages commerciaux perdus. Les provisions sont constituées à hauteur de la différence entre ce coût de revient et ce cours.</p>''',
"Réécriture à droit constant : l'obligation de l'entreprise précède sa condition d'application ; la portée de l'expression « à due concurrence » est rendue explicite par la différence entre coût de revient et cours du jour. Aucune modification du mode de dépréciation n'est proposée.",
"Liste intégrale des biens et date de référence conservées dans un seul alinéa. Renvoi maintenu à l'article 38 nonies ; la provision reste obligatoire et limitée à la baisse de valeur constatée.")

add('38 undecies', '''<p>L'entreprise choisit le traitement des coûts d'emprunt engagés pour acquérir ou produire une immobilisation corporelle ou incorporelle, ou un élément inscrit en stock ou en encours. Elle peut soit les inclure dans le coût d'origine de l'immobilisation ou du stock, soit les déduire en charge au titre de l'exercice au cours duquel les intérêts sont courus.</p>
<p>Le premier alinéa s'applique aux coûts d'emprunt attribuables à des éléments d'actif dont l'utilisation ou la cession exige une période de préparation ou de construction en principe supérieure à douze mois. Il concerne les coûts engagés jusqu'à la date d'acquisition ou de réception définitive du bien.</p>
<p>Le choix prévu au premier alinéa est irrévocable. Il s'applique à tous les coûts d'emprunt qui financent l'acquisition ou la production d'immobilisations, de stocks et d'encours.</p>''',
"Réécriture à droit constant : l'entreprise est désignée comme titulaire du choix ; la phrase relative aux actifs nécessitant une préparation longue est décomposée pour distinguer le champ des biens et la période de prise en compte des coûts. L'irrévocabilité et la portée générale de l'option sont maintenues, sans réforme de fond.",
"Trois alinéas conservés : les deux renvois au premier alinéa restent à leur place. Maintien de la durée en principe supérieure à douze mois, des intérêts courus et de la limite d'acquisition ou de réception définitive. La reformulation rattache l'exigence de préparation aux biens, sans transformer « en principe » en seuil absolu ni ouvrir un choix bien par bien.")

add('38 terdecies', '''<p>Les articles 38 ter à 38 decies s'appliquent aux entreprises industrielles et commerciales passibles de l'impôt sur le revenu selon un régime de bénéfice réel, ainsi qu'aux personnes morales relevant de l'impôt sur les sociétés. Cette application reste soumise aux mesures dérogatoires qui peuvent être prises en faveur des entreprises soumises au contrôle de l'Etat et astreintes à des règles comptables particulières.</p>''',
"Réécriture à droit constant : les deux catégories de contribuables sont identifiées dans une première phrase et la réserve de dérogations dans une seconde. Aucun changement du champ des régimes réels ou de l'impôt sur les sociétés n'est introduit.",
"Un seul alinéa conservé, ainsi que l'intervalle 38 ter à 38 decies et les deux conditions cumulatives tenant au contrôle de l'Etat et aux règles comptables particulières. La possibilité de mesures dérogatoires n'est pas présentée comme l'existence d'une dérogation déjà accordée. La réforme du taux normal de l'IS prévue au CGI, article 219, ne modifie pas ce champ d'application.")

add('38 terdecies A', '''<p>Par dérogation à l'exigence de double exemplaire prévue au IV de l'article 38, les entreprises qui exercent une partie de leur activité à l'étranger doivent également fournir en un seul exemplaire les renseignements relatifs aux seules opérations qui concourent au résultat imposable en France. Elles utilisent des imprimés identiques à ceux mentionnés aux II et III de l'article 38.</p>''',
"Réécriture des obligations déclaratives avec une réforme de fond limitée : conformément à l'orientation de suppression des demandes en double définie par policy.json, le second exemplaire est supprimé. Le champ des entreprises, les renseignements portant uniquement sur le résultat imposable en France et les modèles des imprimés sont conservés à droit constant.",
"L'article 38, IV, de la même annexe, consulté dans le corpus public, exige aussi un double exemplaire : la dérogation expresse évite de laisser subsister cette exigence pour le dépôt visé ici. Coordonner les modèles et consignes de dépôt ainsi que la rédaction générale du IV de l'article 38 lors de la consolidation, sans modifier ce fichier hors lot. L'exemplaire unique ne dispense pas de fournir les données propres aux opérations imposables en France et ne supprime pas les contrôles. Aucun partage nouveau de données protégées ni aucune date future d'entrée en vigueur n'est institué.")

add('38 quaterdecies', '''<p>Les entreprises dont le siège se trouve hors du territoire de la République française ne fournissent que les renseignements relatifs à leurs exploitations situées en France.</p>''',
"Réécriture à droit constant : la périphrase définissant les renseignements à fournir est remplacée par une obligation directement adressée aux entreprises concernées. Aucune extension territoriale ni réforme de fond n'est proposée.",
"Maintien du critère du siège hors du territoire de la République française et de la limitation exclusive aux exploitations situées en France. Cette règle n'est pas confondue avec celle des entreprises exerçant partiellement à l'étranger à l'article 38 terdecies A.")

add('38 quindecies', '''<p>I. – L'entreprise indique dans l'état prévu au I de l'article 54 septies du code général des impôts la date de réalisation et la nature de l'opération, ainsi que le nom ou la dénomination et l'adresse des personnes physiques et morales concernées. Elle y porte également, pour chaque nature d'élément, les renseignements suivants :</p>
<p>1° Pour les biens non amortissables :</p>
<p>a) La valeur comptable ;</p>
<p>b) La valeur fiscale utilisée pour calculer le résultat imposable des cessions ultérieures ;</p>
<p>c) Le montant de la soulte éventuellement perçue lors de l'opération ;</p>
<p>d) Le montant de la soulte imposée lors de l'opération d'échange ou d'apport ;</p>
<p>e) La valeur d'échange ou d'apport des biens ;</p>
<p>2° Pour les biens amortissables :</p>
<p>a) Le montant des plus-values et moins-values réalisées lors de l'opération ;</p>
<p>b) La durée de réintégration de ces plus-values ;</p>
<p>c) Le montant des plus-values déjà réintégrées dans les résultats des exercices précédents ;</p>
<p>d) Le montant des plus-values réintégrées dans les résultats de l'exercice ;</p>
<p>e) Le montant des plus-values qui restent à réintégrer ;</p>
<p>3° Pour le mali technique de fusion :</p>
<p>a. La valeur brute à l'ouverture et à la fin de l'exercice ;</p>
<p>b. La diminution au cours de l'exercice ;</p>
<p>c. Le montant des dépréciations comptables à l'ouverture et à la fin de l'exercice ;</p>
<p>d. Les augmentations et diminutions des dépréciations comptables au cours de l'exercice.</p>
<p>II. – Pour chaque opération, l'entreprise souscrit un état au titre de chaque exercice aussi longtemps que subsistent, au titre de cette opération, des éléments auxquels est attaché un sursis d'imposition prévu par l'un des régimes mentionnés au I de l'article 54 septies du code général des impôts.</p>
<p>III. – (Sans objet)</p>
<p>IV. – Dans l'état prévu au deuxième alinéa de l'article 221 bis du code général des impôts, l'entreprise indique, pour chaque immobilisation réévaluée lors du premier exercice au titre duquel l'option a été exercée :</p>
<p>1° La valeur comptable ;</p>
<p>2° La valeur fiscale utilisée pour calculer le résultat imposable des cessions ultérieures ;</p>
<p>3° La valeur réévaluée.</p>''',
"Réécriture à droit constant : les introductions des I et IV et l'obligation périodique du II désignent explicitement l'entreprise et les informations qu'elle doit porter sur l'état. Les listes techniques, leur ordre et leurs subdivisions sont conservés ; aucune suppression d'état de suivi ni modification des régimes de sursis n'est proposée.",
"Les 24 alinéas, les I à IV, les deux séries a) à e), la série a. à d. du mali et les trois valeurs du IV sont conservés. Renvois au CGI, articles 54 septies, I, et 221 bis, deuxième alinéa, vérifiés dans le corpus. Le III reste sans objet : les notes source le rattachent à l'article 35-2° de la loi n° 2018-1317 du 28 décembre 2018 ; cette indication historique n'est pas une date de réforme future. Le suivi reste annuel et par opération tant que le sursis subsiste.")

add('38 quindecies A', '''<p>I. - Le contribuable souscrit, pour chaque bien, la déclaration prévue à l'article 54 octies du code général des impôts auprès du service chargé des grandes entreprises. Il respecte le délai fixé par cet article et utilise le modèle fixé par l'administration.</p>
<p>Si le bien fait l'objet d'une nouvelle opération de location, le contribuable souscrit la déclaration dans le mois qui suit la conclusion du nouveau contrat.</p>
<p>II. - La déclaration mentionnée au I contient les renseignements suivants :</p>
<p>a. L'identité de la société, de la copropriété ou du groupement qui consent la location ou la mise à disposition, ainsi que l'identité de ses associés, copropriétaires ou membres ;</p>
<p>b. La nature du bien et tout élément permettant de l'identifier distinctement ;</p>
<p>c. Le prix d'acquisition ou de revient et la date d'acquisition du bien donné en location ou mis à disposition ;</p>
<p>d. Pour chaque exercice jusqu'au terme du contrat de location ou de mise à disposition, un tableau établi suivant le modèle fixé par l'administration, qui indique le résultat prévisionnel de la société, de la copropriété ou du groupement.</p>''',
"Réécriture à droit constant : le déposant, le service destinataire, le modèle et les délais sont exprimés dans des phrases directes. Les données d'identification et le tableau prévisionnel restent intégralement exigés ; la simplification déclarative ne supprime pas ces renseignements propres à chaque bien.",
"Sept alinéas et subdivisions I, II, a à d maintenus. L'article 54 octies du CGI, consulté, fixe le délai initial d'un mois après le début de l'amortissement admis en déduction ; le renvoi à ce délai est conservé. Il reste distinct du délai d'un mois après le nouveau contrat prévu ici. Le tableau couvre chaque exercice jusqu'au terme du contrat, pour la location comme pour la mise à disposition.")

add('38 quindecies E', '''<p>Le locataire d'un fonds de commerce, d'un fonds artisanal ou de l'un de leurs éléments incorporels non amortissables, loué dans les conditions prévues au 3 de l'article L. 313-7 du code monétaire et financier, doit joindre à la déclaration de résultat de l'exercice de conclusion du contrat de crédit-bail une attestation délivrée par l'entreprise bailleresse.</p>
<p>Cette attestation indique :</p>
<p>L'identité et l'adresse du locataire ;</p>
<p>La date et la durée du contrat ;</p>
<p>Le prix convenu pour l'acceptation de la promesse unilatérale de vente prévue au contrat ;</p>
<p>Pour chaque échéance, le montant des loyers dus et la quote-part de ces loyers retenue pour fixer ce prix ;</p>
<p>Les modalités prévues en cas de résiliation du contrat ou de non-acceptation de la promesse unilatérale de vente.</p>
<p>L'attestation doit être établie sur papier libre en suivant le modèle fixé par l'administration.</p>''',
"Réécriture à droit constant : l'obligation de joindre l'attestation est rapprochée de la déclaration et de l'exercice concernés ; les informations contractuelles et les modalités de présentation sont formulées plus directement. Aucune réforme des contrats de crédit-bail n'est introduite.",
"Huit alinéas et cinq rubriques d'information conservés. Le champ reste celui des fonds et éléments incorporels non amortissables du 3 de l'article L. 313-7 du code monétaire et financier. Maintien de l'attestation délivrée par le bailleur, du modèle administratif et des deux hypothèses de résiliation ou de non-acceptation ; aucun montant ni droit nouveau n'est ajouté.")

add('38 quindecies F', '''<p>Lorsqu'il cède le contrat de crédit-bail ou le bien acquis à l'échéance de ce contrat, le locataire doit joindre à la déclaration de résultats de l'exercice en cours lors de la cession un état établi sur un document conforme au modèle fixé par l'administration. Cette obligation concerne les biens loués dans les conditions prévues aux 1 et 2 de l'article L. 313-7 du code monétaire et financier, ainsi qu'au 3 du même article pour les éléments incorporels amortissables d'un fonds de commerce ou d'un fonds artisanal.</p>''',
"Réécriture à droit constant : le fait déclenchant la déclaration est exposé avant le champ des biens, qui est précisé dans la seconde phrase du même alinéa. Aucun élargissement de l'obligation ni réforme de fond n'est proposé.",
"Alinéa unique conservé. Les deux cessions restent visées : celle du contrat et celle du bien acquis à son échéance. Les renvois aux 1 et 2 de l'article L. 313-7 et au seul champ des éléments incorporels amortissables de son 3 sont maintenus ; les éléments non amortissables relèvent du régime distinct de l'article 38 quindecies E.")

add('38 quindecies G', '''<p>Pour l'application de l'article 39 duodecies A du code général des impôts, l'acquéreur des droits afférents à un contrat de crédit-bail conclu dans les conditions prévues au 2 de l'article L. 313-7 du code monétaire et financier doit joindre un état à la déclaration de résultats de l'exercice en cours lors de l'acquisition. Cet état est établi sur un document conforme au modèle fixé par l'administration. Il indique notamment les renseignements nécessaires pour répartir le prix d'acquisition des droits entre la fraction représentant les constructions et celle représentant le terrain.</p>''',
"Réécriture à droit constant : l'obligation de joindre l'état, sa présentation et son contenu sont distingués en trois phrases dans le même alinéa. Le prix ventilé reste celui des droits acquis, sans modification du régime fiscal du crédit-bail.",
"Renvois à l'article 39 duodecies A du CGI et au 2 de l'article L. 313-7 du code monétaire et financier conservés. Maintien de l'exercice de l'acquisition et du caractère non exhaustif des renseignements requis (« notamment »). Aucune clé chiffrée de ventilation entre terrain et constructions n'est créée.")

add('38 quindecies H', '''<p>I. - Pour chaque opération de location immobilière réalisée dans les conditions prévues au 2 de l'article L. 313-7 du code monétaire et financier, l'entreprise bailleresse doit conserver à l'appui de sa comptabilité, pendant toute la durée du contrat, un état récapitulant les conditions générales et un tableau. Ce tableau indique, pour chaque loyer, la quote-part retenue pour fixer le prix de cession éventuelle de l'immeuble à l'issue du contrat.</p>
<p>II. - L'état récapitulatif mentionné au I indique :</p>
<p>a) L'identité et l'adresse du locataire ;</p>
<p>b) La date de conclusion et la durée du contrat ;</p>
<p>c) Le prix convenu pour l'acquisition de l'immeuble à l'issue du contrat ou les informations permettant de le déterminer ;</p>
<p>d) Le prix des éléments non amortissables et des éléments amortissables figurant à l'actif du bilan de l'entreprise bailleresse, ainsi que les frais d'acquisition de l'immeuble ;</p>
<p>e) Le lieu de situation de l'immeuble.</p>
<p>Le bailleur doit établir un état récapitulatif modifié lorsque l'économie du contrat change en raison de modifications de la situation du preneur ou des biens pris en crédit-bail.</p>
<p>III. - Le tableau mentionné au I indique, pour chaque échéance, la quote-part du loyer retenue pour fixer le prix de cession éventuelle de l'immeuble à l'issue du contrat, ou les informations permettant de déterminer cette quote-part. Il précise l'affectation de celle-ci au financement respectif des frais d'acquisition, des éléments amortissables et des éléments non amortissables.</p>
<p>IV. - Le bailleur délivre au locataire un exemplaire de l'état récapitulatif et du tableau mentionnés aux II et III à la prise d'effet du contrat et des avenants éventuels.</p>''',
"Réécriture à droit constant : les obligations de conservation, de mise à jour et de remise sont directement attribuées au bailleur. Le contenu du tableau est réparti entre l'identification de la quote-part et son affectation, sans retrancher d'information ni modifier les droits attachés au contrat.",
"Dix alinéas, I à IV et a) à e) conservés. La conservation couvre toute la durée du contrat ; la remise intervient à la prise d'effet du contrat et des avenants éventuels. Au III, les informations permettant de déterminer la quote-part restent une alternative à son indication directe ; les trois affectations financières sont toutes maintenues. L'exemplaire remis au locataire constitue une information contractuelle, distincte du double dépôt administratif supprimé à l'article 38 terdecies A.")

add('38 quindecies I', '''<p>Le locataire d'un immeuble loué dans les conditions prévues au 2° de l'article 1er de la loi n° 66-455 du 2 juillet 1966 relative aux entreprises pratiquant le crédit-bail doit conserver, à l'appui de sa comptabilité et pendant toute la durée de la location, les documents mentionnés au IV de l'article 38 quindecies H que lui délivre l'entreprise bailleresse, ainsi qu'un tableau récapitulatif. Ce tableau indique, pour chaque échéance, la quote-part non déductible pour déterminer son bénéfice imposable. En cas de cession du contrat, le locataire remet une copie de ces documents au cessionnaire.</p>''',
"Réécriture à droit constant : le contenu du tableau est précisé dans une phrase distincte et le locataire est désigné comme responsable de la remise au cessionnaire. Les documents, leur durée de conservation et le champ historique du texte sont maintenus, sans réforme du crédit-bail.",
"Alinéa unique et renvoi au IV de l'article 38 quindecies H conservés. La source vise encore le 2° de l'article 1er de la loi n° 66-455 du 2 juillet 1966, alors que les articles H et J visent le code monétaire et financier : cette discordance de références nécessite une coordination historique à vérifier ; elle n'est pas corrigée silencieusement. La date de 1966 reste celle de la loi citée et ne fixe aucune entrée en vigueur future.")

add('38 quindecies J', '''<p>Lorsqu'il cède le contrat de crédit-bail ou acquiert le bien pris en location, le locataire d'un bien loué dans les conditions prévues au 2 de l'article L. 313-7 du code monétaire et financier doit joindre un état à la déclaration de résultats de l'exercice en cours lors de la cession ou de l'acquisition. Cet état indique, pour chaque échéance de la période de location, le montant de la quote-part des loyers qui n'a pas été déduite pour déterminer le résultat imposable. Il distingue, le cas échéant, la quote-part afférente aux éléments non amortissables de celle relative aux éléments amortissables.</p>''',
"Réécriture à droit constant : les deux événements déclenchant le dépôt, le montant déclaré et sa ventilation sont énoncés dans trois phrases. Les quotes-parts non déduites restent suivies pour chaque échéance ; aucune réforme des déductions n'est proposée.",
"Alinéa unique conservé. Maintien du 2 de l'article L. 313-7 du code monétaire et financier, de l'exercice en cours lors de l'événement et de la ventilation conditionnelle entre éléments amortissables et non amortissables. La cession visée est celle du contrat, tandis que l'acquisition porte sur le bien pris en location.")

add('38 quindecies K', '''<p>Les documents mentionnés aux articles 38 quindecies H à 38 quindecies J doivent être établis sur papier libre en suivant les modèles que fixe l'administration.</p>''',
"Réécriture à droit constant : la phrase exprime directement l'obligation de présentation et le rôle de l'administration dans la fixation des modèles. Aucun changement de support ni de contenu des documents n'est institué.",
"Maintien de l'intervalle complet H à J et du papier libre. Une éventuelle dématérialisation exigerait une disposition propre ; l'orientation générale de simplification ne suffit pas à supprimer ici les modèles ou les documents contractuels.")

add('38 sexdecies-00 A', '''<p>Pour chaque exercice, le contribuable qui choisit la comptabilité super-simplifiée prévue à l'article 302 septies A ter A du code général des impôts exerce cette option sur la déclaration de résultats prévue à l'article 53 A du même code.</p>''',
"Réécriture à droit constant : le contribuable est explicitement désigné comme titulaire de l'option et la périodicité de celle-ci est placée en tête. La déclaration servant de support demeure la même, sans réforme de fond.",
"Numéro d'article « 38 sexdecies-00 A » recopié sans modification. Maintien des deux renvois au CGI, articles 302 septies A ter A et 53 A, et de l'option au titre de chaque exercice. La note historique de l'article 302 septies A ter A consulté ne devient pas une date d'entrée en vigueur nouvelle.")

add('38 sexdecies-00 B', '''<p>Pour l'application du premier alinéa du 2 de l'article 302 septies A ter A du code général des impôts, les exploitants exercent chaque exercice l'option pour la déduction forfaitaire des dépenses de carburant en joignant un état à leur déclaration de résultats. Cet état indique également :</p>
<p>Le type et l'immatriculation de chaque véhicule concerné ;</p>
<p>Le nombre total de kilomètres parcourus, en distinguant ceux effectués pour les besoins de l'entreprise ;</p>
<p>Le montant forfaitaire des frais de carburant ;</p>
<p>Les modalités de comptabilisation de ces frais.</p>''',
"Réécriture à droit constant : le dépôt de l'état joint à la déclaration est présenté comme la modalité d'exercice de l'option annuelle ; la désignation des véhicules est allégée sans réduire les renseignements exigés. Aucun barème ni montant forfaitaire nouveau n'est fixé.",
"Cinq alinéas et les quatre rubriques conservés. Le renvoi reste précisément le premier alinéa du 2 de l'article 302 septies A ter A du CGI ; cet alinéa concerne les carburants et non la dispense de justification du second alinéa. Le kilométrage total et sa part professionnelle restent distincts. Ne pas confondre ce régime avec celui des exploitants agricoles à l'article 38 sexdecies RB bis.")

add('38 sexdecies A', '''<p>Pour apprécier les limites prévues à l'article 69 du code général des impôts, les recettes comprennent toutes les sommes encaissées au cours de l'année civile. S'y ajoute la valeur des produits prélevés dans l'exploitation et alloués soit au personnel salarié, soit au propriétaire du fonds en paiement du fermage.</p>
<p>Sont toutefois exclues les opérations portant sur les éléments de l'actif immobilisé, les opérations effectuées dans le cadre de l'entraide agricole, les subventions et primes d'équipement, les redevances qui trouvent leur origine dans le droit de propriété et les recettes accessoires provenant d'activités sans caractère agricole.</p>
<p>Un abattement de 30 % s'applique en outre aux recettes provenant d'élevages pour lesquels le pourcentage moyen du bénéfice brut par rapport aux recettes est inférieur à 20 %. Le ministre chargé du budget fixe par arrêté la liste des élevages qui peuvent bénéficier de cet abattement (article 4 M de l'annexe IV au présent code).</p>''',
"Réécriture à droit constant : les recettes incluses, les exclusions et l'abattement sont présentés dans les trois alinéas d'origine, avec des phrases plus courtes. Le renvoi explicatif de la note source à l'article 4 M de l'annexe IV est intégré au troisième alinéa. Aucun changement des limites ou des pourcentages n'est proposé.",
"Maintien de l'année civile, des deux catégories de produits alloués, de toutes les exclusions, de l'abattement de 30 % et de la condition strictement inférieure à 20 %. La note source vise l'article 4 M de l'annexe IV, consulté : il renvoie expressément au troisième alinéa du présent article et énumère les élevages en série éligibles. Ce troisième alinéa n'est donc ni déplacé ni scindé ; la liste et ses seuils propres ne sont pas remplacés par un élargissement à tous les élevages.")

add('38 sexdecies C', '''<p>Le bénéfice d'une exploitation agricole soumise à un régime réel d'imposition est déterminé et imposé conformément à l'article 72 du code général des impôts et à la présente section, sous réserve des règles prévues aux articles 38 sexdecies JC, 38 sexdecies JD, 38 sexdecies RB et 38 sexdecies RB bis.</p>''',
"Réécriture à droit constant : la règle de détermination et d'imposition du bénéfice est énoncée avant les régimes qui y dérogent. Tous les renvois et la réserve d'application sont conservés, sans réforme du champ agricole.",
"Alinéa unique et quatre réserves conservés. Les articles JC et JD concernent l'évaluation sous option, RB les obligations du régime simplifié et RB bis l'option relative aux carburants ; ils ont été consultés dans le corpus, ainsi que le CGI, article 72. Aucune simplification prévue pour un autre régime n'est étendue automatiquement aux exploitations agricoles.")

add('38 sexdecies D', '''<p>I. - L'exploitant doit inscrire à l'actif du bilan les immeubles bâtis ou non bâtis dont il est propriétaire et qu'il utilise pour les besoins de l'exploitation.</p>
<p>Il peut toutefois demander à conserver les terres dans son patrimoine privé. Cette option porte sur toutes les terres dont il est propriétaire ou qu'il acquiert au cours de l'exercice. Elle est tacitement reconduite pour l'exercice suivant, sauf renonciation expresse de l'exploitant. Celui-ci joint l'option ou la renonciation à la déclaration des résultats de l'exercice auquel elle s'applique.</p>
<p>L'exploitant peut inscrire à l'actif la maison d'habitation dont il est propriétaire, à condition qu'elle fasse partie de l'exploitation et qu'elle ne présente pas le caractère d'une maison de maître.</p>
<p>II. - Peuvent être traités comme des immobilisations amortissables les équidés et les bovidés utilisés comme animaux de trait ou affectés exclusivement à la reproduction, ainsi que les chevaux de course mis à l'entraînement et les chevaux de concours soumis à un entraînement en vue de la compétition, âgés de deux ans au moins au sens de la réglementation des courses.</p>
<p>Tous les autres animaux doivent être compris dans les stocks, y compris ceux qui sont nés dans l'exploitation.</p>''',
"Réécriture à droit constant : les obligations d'inscription, l'option pour le patrimoine privé et les conditions propres à la maison d'habitation sont adressées directement à l'exploitant. La distinction entre animaux pouvant être immobilisés et animaux obligatoirement stockés est conservée ; aucune réforme de fond n'est appliquée.",
"Cinq alinéas et I/II conservés. L'option reste globale pour les terres possédées ou acquises pendant l'exercice, reconductible tacitement et assortie d'une renonciation expresse. Les conditions cumulatives de la maison d'habitation, l'affectation exclusive à la reproduction, l'âge de deux ans au moins et la référence à la réglementation des courses sont maintenus. La place finale de la condition d'âge reprend celle de la source : sa portée entre les catégories d'équidés doit être contrôlée avant toute clarification de fond, sans étendre ici la faculté d'immobilisation.")

add('38 sexdecies E', '''<p>Pour les matériels et équipements utilisés par les entreprises agricoles, l'amortissement peut être pratiqué selon un système dégressif, dans les conditions fixées au 1 de l'article 39 A du code général des impôts et par les dispositions réglementaires prises pour son application (annexe II, articles 22 à 25).</p>
<p>Ce régime s'applique également aux bâtiments d'exploitation qui remplissent les conditions prévues au 2° du 2 de l'article 39 A du même code.</p>''',
"Réécriture à droit constant : le champ des matériels et équipements utilisés par les entreprises agricoles est placé en tête de la règle et l'extension aux bâtiments est énoncée dans une phrase simple. Le renvoi de la note source aux articles 22 à 25 de l'annexe II est intégré sans ajouter de catégorie de biens ni modifier les conditions de l'amortissement.",
"Deux alinéas conservés. Maintien des références distinctes au 1 et au 2° du 2 de l'article 39 A du CGI. Les articles 22 à 25 de l'annexe II cités par la note ont été consultés ; leur renvoi ne vaut pas suppression de leurs exclusions et modalités. Aucun coefficient dégressif, taux fiscal ou seuil d'éligibilité nouveau n'est créé.")

add('38 sexdecies GB', '''<p>Lorsque le régime d'imposition de l'apporteur diffère de celui de la société bénéficiaire de l'apport, la valeur comptable des stocks apportés dans les conditions mentionnées au sixième alinéa du I de l'article 151 octies du code général des impôts est déterminée, selon le cas, conformément à l'article 38 sexdecies O ou à l'article 38 sexdecies OE.</p>
<p>Les stocks apportés sont repris à cette même valeur dans les inventaires suivants, dans la mesure où ils n'ont pas encore été vendus.</p>''',
"Réécriture à droit constant : la différence de régimes d'imposition est placée en tête comme condition d'application ; la règle de maintien de valeur est directement rattachée aux stocks encore invendus. Aucun changement de méthode d'évaluation ni réforme de fond n'est proposé.",
"Deux alinéas et renvois aux articles 38 sexdecies O et OE conservés, ces deux articles ayant été consultés. Incohérence préexistante relevée : la source vise le sixième alinéa du I de l'article 151 octies du CGI ; dans le corpus fourni, le sixième porte sur l'option d'imposition de la plus-value à long terme des immobilisations amortissables et la règle relative aux stocks figure au septième. Le renvoi source est maintenu ; sa correction exige une coordination explicite. La valeur n'est figée que pour les stocks apportés restant invendus.")

add('38 sexdecies H', '''<p>Les stocks sont évalués selon les règles fixées aux articles 38 nonies et 38 decies, sous réserve des dispositions des articles 38 sexdecies I, 38 sexdecies O et 38 sexdecies OE.</p>''',
"Réécriture à droit constant : la règle générale d'évaluation précède les trois réserves, afin de rendre la lecture plus directe. Aucun changement de méthode, d'option ou de régime d'imposition n'est introduit.",
"Alinéa unique et cinq références conservés. Les règles de coût et de dépréciation des articles 38 nonies et 38 decies restent coordonnées avec la méthode forfaitaire de l'article I et les règles de changement de régime des articles O et OE, consultés dans le corpus.")

add('38 sexdecies I', '''<p>I. - Le prix de revient des produits de l'exploitation compris dans les stocks peut être fixé forfaitairement en appliquant au cours du jour à la clôture de l'exercice une décote correspondant au bénéfice brut susceptible d'être réalisé lors de la vente. L'exploitant apprécie cette décote sous le contrôle de l'administration.</p>
<p>II. - Pour les produits en cours de fabrication, le prix de revient peut être fixé forfaitairement par référence à des coûts standard ou à tout autre élément statistique.</p>''',
"Réécriture à droit constant : l'exploitant est explicitement désigné comme responsable de l'appréciation de la décote ; la règle applicable aux produits en cours de fabrication est introduite par son champ. Aucune décote chiffrée ni nouvelle faculté fiscale n'est créée.",
"Deux alinéas et subdivisions I et II maintenus. La méthode demeure facultative ; le cours retenu est celui du jour de clôture, la décote correspond au bénéfice brut susceptible d'être réalisé et reste contrôlée par l'administration. Ne pas lui substituer les taux distincts de l'article 38 sexdecies JC applicable sous option.")

assert len(sources) == 24
assert len(drafts) == 24
assert set(drafts) == {a['number'] for a in sources}
answer=[]
for a in sources:
    xml, reason, notes = drafts[a['number']]
    answer.append({**{key:a[key] for key in ['code_id','source_id','source_sha256','number']},
                   'proposed_xml':xml, 'reason':reason, 'review_notes':notes, 'status':'rewrite_draft'})
Path('answer.json').write_text(json.dumps(answer,ensure_ascii=False,indent=2)+'\n')
print('Wrote answer.json:',len(answer),'articles;',sum(len(a['proposed_xml']) for a in answer),'XML characters')
