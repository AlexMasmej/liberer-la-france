import json
from pathlib import Path
from html import escape


sources = json.loads(Path('source.json').read_text())
drafts = {}


def article(index, paragraphs, reason, notes):
    xml = '\n'.join('<p>' + escape(p, quote=False).replace('\n', '<br />') + '</p>' for p in paragraphs)
    drafts[index] = dict(proposed_xml=xml, reason=reason, review_notes=notes)


article(0, [
    "I. – La société notifie l'option prévue aux II et III bis de l'article 208 C du code général des impôts, sur papier libre ou par voie électronique, au service des impôts auprès duquel elle souscrit sa déclaration de résultat.",
    "Lorsqu'elle notifie son option, la société d'investissements immobiliers cotée fournit la liste de ses filiales qui optent. Pour chacune, elle indique la dénomination, l'adresse du siège social, le numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce et la répartition du capital. Elle fournit chaque année cette liste mise à jour lors du dépôt de sa déclaration de résultat.",
    "Lorsqu'elles notifient leur option, puis lors du dépôt de leurs déclarations de résultats ultérieures, les filiales indiquent le nom, l'adresse du siège social et le numéro d'identification de la société d'investissements immobiliers cotée ou de la société de placement à prépondérance immobilière à capital variable. Ce numéro est celui défini au premier alinéa de l'article R. 123-221 du code de commerce.",
    "L'option souscrite dans les conditions du premier alinéa comporte l'engagement prévu au deuxième alinéa de l'article 221 bis du code général des impôts.",
    "II. – Les sociétés qui ont opté conformément au premier alinéa du I joignent à leur déclaration de résultat un état conforme au modèle établi par l'administration. Cet état présente, selon les opérations prévues aux deuxième, troisième et quatrième alinéas du II de l'article 208 C du code général des impôts, la décomposition de leur résultat fiscal et de celui des organismes mentionnés à l'article 8 du même code. Il indique également les obligations de distribution correspondantes et le respect des obligations antérieures."
], "Réécriture à droit constant : le redevable de la notification est explicité, les renseignements sur les filiales sont séparés de leur actualisation annuelle et le contenu de l'état fiscal est présenté en trois phrases. Aucune réforme de fond des exonérations immobilières ou de leurs obligations de distribution n'est introduite.",
    "Les cinq alinéas, les II et III bis de l'article 208 C et les autres renvois sont conservés. La note relative au décret n° 2022-1014 du 19 juillet 2022 est historique et ne fixe aucune entrée en vigueur future. Pour le réemploi des données prévu par policy.json, créer dans le livre des procédures fiscales, hors des cinq codes, une disposition législative sur la réutilisation des informations déclaratives légalement détenues par l'administration fiscale : elle doit encadrer les finalités et les destinataires, préserver les secrets protégés et organiser le droit de rectification. Un texte d'application doit préciser la validation et l'actualisation des données des déclarations et états fiscaux, notamment de la liste annuelle du présent article ; aucun numéro d'article nouveau n'est présumé et aucune dispense de déclaration n'est créée ici.")

article(1, [
    "I. – Pour le premier exercice d'application du régime d'exonération prévu au 3° nonies de l'article 208 du code général des impôts, les sociétés de placement à prépondérance immobilière à capital variable joignent à leur déclaration de résultat la copie de l'agrément délivré par l'Autorité des marchés financiers en application de l'article L. 214-35 du code monétaire et financier. Le cas échéant, elles joignent à la place de cette copie l'avis de réception de leur demande par cette autorité ; cet avis doit mentionner la date d'expiration du délai à compter de laquelle, en l'absence d'agrément exprès, l'agrément est réputé accordé. Elles joignent également la liste de leurs filiales qui optent dans les conditions du III bis de l'article 208 C du code général des impôts. Pour chaque filiale, cette liste indique la dénomination, l'adresse du siège social, le numéro d'identification attribué dans les conditions du premier alinéa de l'article R. 123-221 du code de commerce et la répartition du capital.",
    "II. – Les sociétés de placement à prépondérance immobilière à capital variable joignent à leur déclaration de résultat la liste actualisée prévue au I et un état conforme au modèle établi par l'administration. Cet état présente :",
    "1° La décomposition des sommes distribuables définies au I de l'article L. 214-69 du code monétaire et financier, selon les opérations prévues au II du même article ;",
    "2° Les obligations de distribution qui résultent des II et III du même article."
], "Réécriture à droit constant : l'agrément exprès et la pièce justificative de l'agrément tacite sont distingués dans des phrases séparées ; les mentions obligatoires de la liste et de l'état restent intégrales. Aucune modification du régime d'exonération n'est proposée.",
    "Maintien des I et II, des 1° et 2°, du champ du premier exercice et de la date d'expiration à mentionner en cas d'agrément tacite. La note de coordination de 2022 demeure historique. La disposition nouvelle de réemploi des informations déclaratives à créer dans le livre des procédures fiscales, hors des cinq codes et sans numéro présumé, doit être coordonnée avec l'actualisation de la liste du II, le droit de rectification et les secrets protégés. Le présent texte ne supprime pas les justificatifs d'agrément.")

article(2, [
    "La société unipersonnelle d'investissement à risque respecte, pendant tout l'exercice et de manière constante, la condition d'exclusivité de son objet social prévue au 1 du I de l'article 208 D du code général des impôts.",
    "Pour apprécier cette condition, les titres reçus en échange d'actions ou de parts de sociétés répondant aux conditions du I de l'article 208 D sont retenus pour leur valeur d'inscription à l'actif de la société unipersonnelle d'investissement à risque. Sont exclus les titres reçus dans le cadre d'un apport de titres à une société. Les titres retenus sont pris en compte pendant deux ans à compter de l'échange ou, si elle est plus longue, jusqu'à la fin de la période pendant laquelle la société unipersonnelle d'investissement à risque s'est engagée à les conserver à son actif.",
    "Lorsque les actions ou parts de sociétés répondant aux conditions du I de l'article 208 D sont admises à la négociation sur un marché d'instruments financiers d'un Etat partie à l'accord sur l'Espace économique européen, elles continuent à être prises en compte pour apprécier la condition d'exclusivité du premier alinéa pendant cinq ans à compter de leur admission. Le fonctionnement de ce marché doit être assuré par une entreprise de marché, par un prestataire de services d'investissement autre qu'une société de gestion de portefeuille ou par tout autre organisme similaire étranger.",
    "Les sommes provenant de la cession d'actions ou de parts de sociétés répondant aux conditions du I de l'article 208 D ou du remboursement d'avances en compte courant consenties à ces sociétés, et qui ne sont pas réinvesties dans d'autres actifs, sont exclues du calcul de la limite de 5 % prévue au 4 du I du même article. Cette exclusion s'applique pendant deux ans à compter, selon le cas, de la cession des titres ou du remboursement des avances en compte courant."
], "Réécriture à droit constant : les conditions de prise en compte des titres échangés et cotés et le traitement des liquidités sont explicités, avec séparation de l'exception d'apport et des délais. Aucun changement de fond du régime des sociétés unipersonnelles d'investissement à risque n'est effectué.",
    "Conservation des quatre alinéas, notamment des deuxième et quatrième auxquels renvoie l'article 46 ter C. Contrôle des durées : deux ans pour l'échange ou engagement de conservation plus long, cinq ans après admission, deux ans pour les liquidités non réinvesties ; limite de 5 % inchangée. La qualification du marché et l'exception des sociétés de gestion de portefeuille sont maintenues.")

article(3, [
    "I. – La société unipersonnelle d'investissement à risque joint à sa déclaration de résultats un état sur papier libre permettant d'apprécier le respect de la condition d'objet social exclusif prévue à l'article 46 ter B. Pour chaque société dont elle détient, ou a détenu au cours de l'exercice, des actions ou des parts, cet état indique :",
    "a. La dénomination sociale, l'adresse du siège social et la date de création de cette société ;",
    "b. Pour chaque souscription en numéraire, la date, le nombre de titres et le montant souscrit ou, pour les titres reçus en échange dans les conditions du deuxième alinéa de l'article 46 ter B, la date de l'échange, le nombre de titres reçus et leur valeur d'inscription à l'actif ;",
    "c. Le nombre de titres cédés au cours de l'exercice et le montant des cessions ;",
    "d. A l'ouverture et à la clôture de l'exercice, le pourcentage de détention dans le capital de cette société, en droits financiers et en droits de vote ;",
    "e. Le montant brut des avances en compte courant consenties à ces sociétés.",
    "L'état prévu au premier alinéa indique également le montant des autres actifs et leur proportion dans l'actif brut comptable de la société unipersonnelle d'investissement à risque. Ces informations sont données avant et après prise en compte des sommes mentionnées au quatrième alinéa de l'article 46 ter B.",
    "II. – A partir de l'exercice au cours duquel elle devient imposable à l'impôt sur les sociétés, la société unipersonnelle d'investissement à risque joint à sa déclaration de résultats un état, établi sur papier libre, des bénéfices et réserves non distribués qui ont été exonérés de cet impôt.",
    "L'obligation prévue à l'alinéa précédent ne s'applique pas lorsque les bénéfices et réserves distribuables qui y sont mentionnés sont intégralement distribués."
], "Réécriture à droit constant : les rubriques de l'état sont formulées directement et la double présentation des autres actifs est explicitée. L'obligation après la fin de l'exonération et son exception de distribution totale restent distinctes. Aucune réforme de fond n'est introduite.",
    "Maintien des neuf alinéas et des lettres a à e ; les renvois aux deuxième et quatrième alinéas de l'article 46 ter B correspondent à leur position conservée. Les titres détenus puis cédés dans l'exercice, les droits financiers et de vote, le caractère brut des avances et les bénéfices et réserves exonérés sont tous conservés.")

article(4, [
    "La société unipersonnelle d'investissement à risque remet un état individuel à l'associé qui entend bénéficier de l'article 163 quinquies C bis du code général des impôts. Elle le remet au plus tard le 16 février de l'année civile suivant celle de la mise en paiement des revenus distribués. Cet état indique :",
    "a. La dénomination sociale et l'adresse de la société ;",
    "b. Les dates et les montants des revenus distribués à l'associé qui sont prélevés sur des bénéfices exonérés d'impôt sur les sociétés conformément à l'article 208 D du code général des impôts ;",
    "c. Le montant des cotisations et prélèvements sociaux prélevés en application du 8° du II de l'article L. 136-7 du code de la sécurité sociale et du II de l'article 16 de l'ordonnance n° 96-50 du 24 janvier 1996 modifiée relative au remboursement de la dette sociale.",
    "L'état précise que l'associé mentionné au premier alinéa est le souscripteur initial des actions de la société ou qu'il les a reçues par transmission à titre gratuit à la suite du décès de l'associé initial."
], "Réécriture à droit constant : la remise de l'état, son échéance et son contenu sont formulés en phrases directes. La qualité de souscripteur initial ou d'ayant reçu les titres à la suite du décès est conservée. Aucune réforme des prélèvements sur ces distributions n'est opérée.",
    "Echéance du 16 février, lettres a à c et renvois sociaux inchangés. La réforme de la CSG salariale privée ne s'étend pas à ces revenus de capitaux. La note relative à la loi n° 2009-1646 du 24 décembre 2009 est une coordination historique et ne constitue pas une date d'entrée en vigueur de la réforme projetée.")

article(5, [
    "Pour les organismes non lucratifs mentionnés au 5 de l'article 206 du code général des impôts, la base de l'impôt sur les sociétés dû à raison des immeubles dont ils se réservent la jouissance est déterminée selon les articles 41 F à 41 J."
], "Réécriture à droit constant : le champ des organismes et celui des immeubles sont placés avant la règle de détermination de la base. Aucune modification des charges déductibles ou de l'imposition de ces organismes n'est introduite.",
    "Renvois aux articles 41 F à 41 J et au 5 de l'article 206 conservés ; le champ reste limité aux immeubles dont les organismes se réservent la jouissance. La réforme du taux national normal de l'IS ne remplace pas les régimes particuliers de ces organismes.")

article(6, [
    "Les intérêts des sommes inscrites sur les livrets supplémentaires que les caisses d'épargne ont été autorisées à ouvrir par décret ne bénéficient pas de l'exonération prévue au a de l'article 208 ter du code général des impôts."
], "Réécriture à droit constant : les intérêts exclus de l'exonération deviennent le sujet de la phrase. Aucune réforme de fond du régime des livrets n'est introduite.",
    "L'exclusion reste circonscrite aux livrets supplémentaires autorisés par décret et le renvoi au a de l'article 208 ter demeure inchangé.")

article(7, [
    "Pour l'application de l'article 212 bis du code général des impôts, les entreprises joignent à leur déclaration de résultat de chaque exercice un état indiquant les charges financières nettes non admises en déduction du résultat de cet exercice en application des I, VI et VII du même article. Cet état assure également, en application du VIII de cet article, le suivi des charges financières nettes non admises en déduction au titre des exercices précédents et des capacités de déduction inemployées au titre des cinq exercices précédents."
], "Réécriture à droit constant : le contenu de l'état annuel et le suivi des reports sont séparés en deux phrases sans déplacer l'alinéa. Aucune modification du plafonnement des charges financières n'est proposée.",
    "Maintien des renvois aux I, VI, VII et VIII de l'article 212 bis. La période de cinq exercices ne concerne que les capacités de déduction inemployées ; aucune durée nouvelle n'est ajoutée au suivi des charges non déduites.")

article(8, [
    "La personne morale bénéficiaire des dividendes, intérêts ou redevances déclare l'engagement prévu au c du 2 de l'article 119 ter, au deuxième alinéa du 1 de l'article 119 quater et au 2 de l'article 182 B bis du code général des impôts. Elle adresse cette déclaration à la fois à l'établissement payeur en France des dividendes ou au débiteur ou à la personne qui assure le paiement des intérêts ou des redevances, et à la direction des impôts des non-résidents (service des impôts des entreprises étrangères). Elle la souscrit avant la date de la première mise en paiement suivant l'inscription en compte des titres de la société émettrice.",
    "La déclaration comporte les renseignements suivants :",
    "a. L'engagement prévu au c du 2 de l'article 119 ter, au deuxième alinéa du 1 de l'article 119 quater et au 2 de l'article 182 B bis du code général des impôts ;",
    "b. Le nombre et la nature des titres composant le capital de la société émettrice ;",
    "c. Le nombre et la nature des titres que la personne morale détient dans la société émettrice ;",
    "d. La répartition, en pourcentage, des droits de vote et des droits financiers que la personne morale détient dans la société émettrice ;",
    "e. Le numéro du compte de la personne morale tenu par l'émetteur ou par l'intermédiaire financier auprès duquel les titres sont inscrits ;",
    "f. La date d'acquisition des titres et, si elle est différente, leur date d'inscription en compte ;",
    "g. Le nom et l'adresse de la personne ou de l'organisme qui assure le paiement des dividendes, intérêts et redevances ;",
    "h. Le nom et l'adresse de la personne désignée comme représentant."
], "Réécriture à droit constant : la personne qui souscrit l'engagement est placée en tête et les destinataires et le délai sont énoncés séparément. Les huit rubriques déclaratives sont maintenues intégralement. Aucune réforme des exonérations entre sociétés associées n'est introduite.",
    "Conservation des lettres a à h, des trois fondements de l'engagement et de l'envoi aux deux catégories de destinataires. Le délai reste antérieur à la première mise en paiement suivant l'inscription en compte. Les articles 46 quater-0 FC et FD restent coordonnés sur la responsabilité du représentant et la durée de conservation.")

article(9, [
    "La déclaration prévue à l'article 46 quater-0 FB est accompagnée d'une reconnaissance du représentant désigné. Celui-ci y reconnaît qu'en cas de non-respect de l'engagement prévu au même article, il est responsable du paiement des retenues à la source ou du prélèvement mentionnés au 1 de l'article 119 ter et au premier alinéa du 1 de l'article 119 quater du code général des impôts.",
    "Cette règle s'applique également à l'exonération de retenue à la source sur les paiements de redevances prévue à l'article 182 B bis du code général des impôts."
], "Réécriture à droit constant : le représentant et le fait déclenchant sa responsabilité sont explicités ; l'extension aux redevances reste dans le second alinéa. Aucun changement de fond des garanties de paiement n'est proposé.",
    "La reconnaissance accompagne la déclaration ; la responsabilité reste subordonnée au non-respect de l'engagement. Les renvois aux articles 46 quater-0 FB, 119 ter, 119 quater et 182 B bis sont conservés.")

article(10, [
    "Le délai de deux ans de conservation des titres prévu au c du 2 de l'article 119 ter et au deuxième alinéa du 1 de l'article 119 quater du code général des impôts court à compter de leur inscription en compte. Toutefois, s'il est établi que leur date d'acquisition est différente, le délai court à compter de cette date d'acquisition.",
    "Cette règle s'applique également à l'exonération de retenue à la source sur les paiements de redevances prévue à l'article 182 B bis du code général des impôts."
], "Réécriture à droit constant : le point de départ de principe et le point de départ dérogatoire sont énoncés dans deux phrases. Aucune modification de la durée de conservation ou du champ de l'exonération n'est introduite.",
    "Délai de deux ans, preuve d'une date d'acquisition différente et extension aux redevances inchangés ; les deux alinéas restent en place.")

article(11, [
    "I. – Les bénéfices placés sous le régime d'exonération conditionnelle prévu à l'article 238 octies du code général des impôts ne peuvent bénéficier du régime de l'article 209 quater D du même code qu'après avoir été réinvestis selon les modalités de l'article 238 octies. Après ce réinvestissement, ils peuvent être affectés à un sous-compte distinct de la réserve spéciale des profits de construction.",
    "Les délais de quatre et sept ans prévus à l'article 209 quater D se calculent de la clôture de l'exercice de réalisation des profits concernés à la clôture de l'exercice au titre duquel la distribution a eu lieu. La date de réalisation de ces profits n'entre pas en compte pour l'exigibilité du prélèvement prévu à l'article 95 de la loi de finances pour 2004 (n° 2003-1311 du 30 décembre 2003).",
    "II. – L'article 238 octies ne s'applique plus aux profits réalisés à compter du 1er janvier 1972."
], "Réécriture à droit constant : la condition de réinvestissement préalable et la faculté d'affectation à la réserve sont distinguées ; les délais et la borne historique sont formulés directement. Aucune réforme de fond de ces profits historiques n'est proposée.",
    "Maintien des I et II, des délais de quatre et sept ans, de leur calcul entre clôtures et de la règle spéciale d'exigibilité. Le 1er janvier 1972, la loi de finances pour 2004 et le 30 décembre 2003 sont des références historiques conservées, sans extension aux profits nouveaux ni assimilation à une exonération générale des bénéfices réinvestis.")

article(12, [
    "L'état prévu au dernier alinéa du a septies du I de l'article 219 du code général des impôts comporte les renseignements suivants :",
    "1° Pour l'entreprise cédante : sa dénomination, l'adresse de son siège social et le numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce ;",
    "2° Pour les moins-values réalisées au cours de l'exercice : la dénomination de la société dont les titres sont cédés ; le nombre de titres, leur date et leur valeur d'acquisition, ainsi que leur date et leur valeur de cession ; le montant de la moins-value en report ; le cas échéant, la mention de l'utilisation de la méthode du coût unitaire moyen pondéré ; la dénomination de l'entreprise cessionnaire, l'adresse de son siège social et, le cas échéant, son numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce ; la nature du lien de dépendance entre l'entreprise cédante et l'entreprise cessionnaire ;",
    "3° Pour les moins-values placées en report au titre d'exercices antérieurs : la dénomination de la société dont les titres sont cédés ; le nombre de titres, leur date d'acquisition et leur date de cession ; le montant de la moins-value en report ; la dénomination de l'entreprise cessionnaire, l'adresse de son siège social et, le cas échéant, son numéro d'identification défini au premier alinéa de l'article R. 123-221 du code de commerce ; la nature du lien de dépendance entre l'entreprise cédante et l'entreprise cessionnaire ;",
    "4° Pour les moins-values placées en report au titre d'exercices antérieurs dont le report prend fin pendant l'exercice : la dénomination de la société dont les titres sont cédés ; le nombre de titres et leur date d'acquisition ; le montant et le régime de la moins-value dont le report prend fin ; la nature et la date de l'événement mettant fin au report d'imposition."
], "Réécriture à droit constant : les trois catégories de moins-values sont conservées et leurs renseignements sont séparés par des points-virgules pour distinguer titres, montants et identité des parties. Aucune modification du régime de report ou des taux d'IS n'est introduite.",
    "Maintien des 1° à 4° et de tous les renseignements, y compris la méthode du coût unitaire moyen pondéré et les mentions conditionnelles du numéro d'identification. Le renvoi au a septies du I de l'article 219 concerne un régime particulier, conservé par coordination.json ; il ne justifie pas de lui appliquer un nouveau taux. La note de 2022 reste historique.")

article(13, [
    "Pour l'application des premier et deuxième alinéas du I de l'article 220 quinquies du code général des impôts, les règles suivantes s'appliquent :",
    "1° Le déficit d'un exercice correspond au résultat fiscal déclaré passible de l'impôt sur les sociétés au taux normal prévu au deuxième alinéa du I de l'article 219 du code général des impôts ;",
    "1° bis : Le bénéfice d'un exercice correspond au bénéfice fiscal déclaré qui a été soumis à l'impôt sur les sociétés aux taux prévus au deuxième alinéa et au b du I de l'article 219 du code général des impôts, sans distinction entre ces taux. En sont exclues la fraction distribuée, celle qui a donné lieu à un impôt payé au moyen de crédits d'impôt et celle qui a été retenue pour déterminer le crédit d'impôt prévu à l'article 220 quater du même code ;",
    "2° Pour déterminer la fraction non distribuée du bénéfice défini au 1° bis, le montant des distributions prélevées sur ce bénéfice est déduit de celui-ci ;",
    "3° Seule la fraction du déficit qui n'a pas pu être imputée sur le bénéfice de l'exercice précédant l'exercice déficitaire reste reportable dans les conditions du I de l'article 209 du code général des impôts."
], "Réécriture à droit constant : les définitions du déficit et du bénéfice, les fractions exclues et le reliquat reportable sont formulés directement. Les taux demeurent désignés par renvoi à l'article 219 ; la présente réécriture ne fixe aucun taux nouveau et ne modifie pas les règles historiques de calcul de la créance.",
    "Les subdivisions 1°, 1° bis, 2° et 3° restent en place. Le renvoi au deuxième alinéa du I de l'article 219 suivra la réforme du taux national normal, selon sa transition, sans recalcul automatique des créances historiques ni assimilation du taux réduit du b. Incohérences préexistantes à contrôler : le 1° bis exclut déjà la fraction distribuée alors que le 2° prévoit de déduire les distributions ; l'article 220 quinquies du corpus exclut aussi les bénéfices dont l'impôt a été payé au moyen de réductions d'impôt, tandis que le présent 1° bis ne mentionne que les crédits d'impôt ; le renvoi à l'article 220 quater demeure dans la source mais cet article est absent du corpus fourni. Ces points sont signalés sans correction silencieuse. La part territoriale projetée exige une disposition législative nouvelle précisant son éventuelle prise en compte pour le report en arrière et l'imputation ou le remboursement des créances.")

article(14, [
    "I. – L'entreprise qui détient plusieurs créances ne peut les imputer sur l'impôt sur les sociétés que dans l'ordre de leur apparition.",
    "II. – Dès qu'une créance est cédée à titre de garantie à un établissement de crédit ou à une société de financement, l'entreprise ne peut plus l'imputer sur l'impôt sur les sociétés qu'elle doit."
], "Réécriture à droit constant : l'entreprise devient le sujet des règles d'imputation et l'effet de la cession en garantie est formulé directement. Aucun changement de fond de l'ordre des créances ni de leur cessibilité n'est introduit.",
    "Maintien des I et II, de l'ordre d'apparition des créances et de l'interdiction d'imputation dès la date de cession en garantie aux deux catégories d'établissements visées. Toute part territoriale future de l'IS nécessite ses propres règles législatives d'imputation ; elle n'est pas réputée créée par ce texte.")

article(15, [
    "I. – L'entreprise qui exerce l'option prévue au premier alinéa du I de l'article 220 quinquies du code général des impôts joint au relevé de solde de l'exercice au titre duquel elle exerce cette option une déclaration conforme au modèle fixé par l'administration.",
    "Si la société qui dépose cette déclaration a fait l'objet d'un rachat dans les conditions de l'article 220 quater du code général des impôts, elle joint un document attestant le montant du crédit d'impôt obtenu par la société constituée pour le rachat. Le montant attesté est celui du crédit d'impôt obtenu au titre de l'exercice suivant celui au cours duquel a été réalisé le bénéfice sur lequel le déficit est reporté en arrière.",
    "II. – Paragraphe supprimé (1)."
], "Réécriture à droit constant : la déclaration jointe au relevé de solde est formulée directement et le justificatif propre au rachat est expliqué en deux phrases. Le repère du II supprimé est conservé ; aucune réforme de fond ni nouvelle obligation déclarative n'est ajoutée.",
    "Maintien des trois alinéas, de l'exercice de l'option et de l'exercice auquel se rapporte le crédit d'impôt du rachat. Le renvoi à l'article 220 quater est préexistant mais cet article est absent du corpus fourni : contrôler son maintien pour les situations historiques sans supprimer l'obligation par déduction. La source conserve l'appel « (1) » après le II supprimé sans fournir de note correspondante dans source_notes_xml ; cet appel est maintenu et cette lacune est signalée.")

article(16, [
    "Pour l'application du II de l'article 217 quinquies du code général des impôts, les entreprises qui pratiquent la déduction prévue au premier alinéa de ce II joignent à la déclaration de résultats de l'exercice concerné un état conforme au modèle établi par l'administration. Cet état indique les éléments permettant de déterminer le montant de la déduction pratiquée et les modalités juridiques de l'émission d'actions à l'origine de cette déduction."
], "Réécriture à droit constant : le fait qui déclenche le dépôt de l'état et les deux catégories de renseignements sont énoncés en deux phrases. Aucune modification de la déduction relative aux actions n'est proposée.",
    "Renvois au II et à son premier alinéa de l'article 217 quinquies conservés, ainsi que le rattachement à l'exercice de la déduction. Aucun élargissement aux options ou attributions qui ne relèvent pas de cette déduction.")

article(17, [
    "I. – Au 1 du I de l'article 223 quinquies C du code général des impôts, sont visées les personnes morales qui établissent des comptes consolidés en application d'une obligation légale.",
    "II. – Le groupe réunit une personne morale définie au I, les filiales intégrées dans les états financiers consolidés et leurs succursales.",
    "Appartient également au groupe toute filiale ou succursale exclue du périmètre de consolidation pour le seul motif que son intérêt est négligeable au regard de l'objectif défini à l'article L. 233-21 du code de commerce. La personne morale déclarante reporte les agrégats qui s'y rapportent.",
    "Une déclaration imposée par une réglementation étrangère est similaire à celle prévue à l'article 223 quinquies C du code général des impôts si elle contient les mêmes informations et couvre l'ensemble du groupe.",
    "III. – Pour chaque Etat ou territoire d'implantation du groupe, la déclaration prévue à l'article 223 quinquies C comprend les données agrégées suivantes pour l'exercice considéré :",
    "1° Le chiffre d'affaires issu des transactions intragroupe ;",
    "2° Le chiffre d'affaires issu des transactions avec des parties indépendantes ;",
    "3° Le chiffre d'affaires total ;",
    "4° Le bénéfice ou la perte avant impôts sur les bénéfices ;",
    "5° Les impôts sur les bénéfices acquittés ;",
    "6° Les impôts sur les bénéfices dus ;",
    "7° Le capital social ;",
    "8° Les bénéfices non distribués à la fin de l'exercice ;",
    "9° Le nombre d'employés en équivalent temps plein ;",
    "10° Les actifs corporels, hors trésorerie et équivalents de trésorerie.",
    "IV. – Les données du III sont déclarées en euros ou dans la monnaie utilisée pour les comptes consolidés, à l'exception du nombre d'employés prévu au 9°.",
    "V. – 1. Pour chaque Etat ou territoire d'implantation, la déclaration identifie toutes les entités qui y sont établies, y compris les succursales rattachées à une personne morale située dans un autre Etat ou territoire.",
    "2. Si une entité est établie dans un Etat ou territoire autre que celui où elle a été constituée, la déclaration mentionne également l'Etat ou territoire de constitution.",
    "3. Les principales activités de chaque entité sont indiquées en les choisissant dans la liste suivante :",
    "a) Recherche et développement ;",
    "b) Détention ou gestion de droits de propriété intellectuelle ;",
    "c) Achats ou approvisionnements ;",
    "d) Fabrication ou production ;",
    "e) Vente, commercialisation ou distribution ;",
    "f) Services administratifs, de gestion ou de soutien ;",
    "g) Fourniture de services à des parties indépendantes ;",
    "h) Financement interne du groupe ;",
    "i) Services financiers réglementés ;",
    "j) Assurance ;",
    "k) Détention d'actions ou d'autres instruments de fonds propres ;",
    "l) Activités dormantes ;",
    "m) Autres.",
    "VI. – Pour établir la déclaration prévue à l'article 223 quinquies C, la personne morale tenue à son dépôt utilise des données issues des états financiers consolidés, des comptes sociaux de chaque entité ou des comptes de gestion internes. Elle indique dans la déclaration les sources de données retenues. Elle les utilise de manière cohérente d'une année sur l'autre, sauf si des circonstances particulières, exposées à l'administration, justifient un changement.",
    "VII. – Les données prévues au V se rapportent à l'exercice de la tête de groupe.",
    "Pour les filiales et les succursales, la déclaration présente de manière cohérente :",
    "a) Soit les informations de leur exercice qui s'achève le même jour que celui de la tête de groupe ou au cours des douze mois précédant cette date ;",
    "b) Soit les informations relatives à l'exercice de la tête de groupe.",
    "VIII. – 1. La personne morale visée au 1 du I de l'article 223 quinquies C indique sur sa déclaration de résultat qu'elle est tenue à l'obligation déclarative prévue par cet article.",
    "2. La personne morale visée au 2 du même I indique sur sa déclaration de résultat qu'elle a été désignée pour accomplir cette obligation ou qu'une autre entité assure le dépôt. Dans ce dernier cas, elle précise l'identité et la localisation de cette entité.",
    "IX. – Pour satisfaire aux obligations de l'article 223 quinquies C, la personne morale communique un support informatique dont les caractéristiques sont fixées par la direction générale des finances publiques."
], "Réécriture à droit constant : les définitions, l'inclusion des entités non significatives, le choix des sources et les obligations de dépôt sont formulés directement. Les dix agrégats et les treize catégories d'activités sont intégralement conservés ; leurs libellés techniques restent stables. Aucune réforme du champ de la déclaration pays par pays n'est introduite.",
    "Maintien des I à IX, des subdivisions du V et du VIII et de tous les alinéas. L'exception monétaire du 9°, les douze mois du VII et la justification des changements de sources sont conservés. Point préexistant à contrôler : le premier alinéa du VII renvoie au V, relatif aux entités et activités, alors que les agrégats sont énumérés au III ; ce renvoi n'est pas corrigé silencieusement. La disposition nouvelle de réemploi des informations déclaratives à créer dans le livre des procédures fiscales, hors des cinq codes et sans numéro présumé, doit préserver les secrets, le droit de rectification et les règles d'échange international. Coordonner cette disposition et son texte d'application avec l'article 223 quinquies C et le présent article, sans présumer de suppression de données ou de dépôt.")

article(18, [
    "Les œuvres cinématographiques de longue durée éligibles, au titre de leurs dépenses de production, au crédit d'impôt prévu aux articles 220 sexies et 220 F du code général des impôts sont définies au 1° de l'article 6 du décret n° 99-130 du 24 février 1999 relatif au soutien financier de l'industrie cinématographique.",
    "Pour les dépenses de production d'œuvres cinématographiques, les entreprises de production déléguées admises au bénéfice du crédit d'impôt prévu aux articles 220 sexies et 220 F du code général des impôts sont celles définies au 5° de l'article 6 du même décret.",
    "Pour les dépenses de production d'œuvres audiovisuelles, les entreprises de production déléguées admises au bénéfice du crédit d'impôt prévu aux articles 220 sexies et 220 F sont celles définies au II de l'article 3 du décret n° 95-110 du 2 février 1995 relatif au soutien financier à la production, à la préparation et à la distribution d'œuvres audiovisuelles."
], "Réécriture à droit constant : les trois règles de définition sont présentées en distinguant les œuvres éligibles, les producteurs cinématographiques et les producteurs audiovisuels. Aucune modification de fond du crédit d'impôt ni de ses bénéficiaires n'est introduite.",
    "Conservation des trois alinéas, des 1° et 5° de l'article 6 du décret du 24 février 1999 et du II de l'article 3 du décret du 2 février 1995. Ces décrets extérieurs aux codes du corpus fourni n'ont pas pu être vérifiés dans leur intégralité ; contrôler leur articulation avec les textes de soutien cinématographique et audiovisuel sans substituer un renvoi supposé. Les dates restent celles des textes historiques cités.")

article(20, [
    "Pour déterminer les dépenses prévues au d du 1 du III de l'article 220 sexies du code général des impôts, sont retenues les dotations aux amortissements fiscalement déductibles des immobilisations détenues par l'entreprise de production déléguée et directement affectées à la réalisation de l'œuvre cinématographique ou audiovisuelle ouvrant droit au crédit d'impôt. Seules les dotations correspondant à la période d'utilisation effective de l'immobilisation pour réaliser l'œuvre éligible sont prises en compte."
], "Réécriture à droit constant : les conditions tenant aux immobilisations et la limitation à leur durée d'utilisation effective sont formulées en deux phrases directes. Aucune réforme de fond de l'amortissement ou de l'assiette du crédit d'impôt n'est introduite.",
    "Renvoi au d du 1 du III de l'article 220 sexies conservé. Les conditions de détention, d'affectation directe et de déductibilité fiscale sont cumulativement maintenues ; la durée retenue ne devient pas la durée totale de production.")

article(21, [
    "I. – Les artistes-interprètes et les artistes de complément visés au b du 1 et au b du 2 de l'article 46 quater-0 YM comprennent les catégories suivantes :",
    "a. Les acteurs des rôles principaux et secondaires des œuvres de fiction ; les artistes-interprètes qui interviennent dans le spectacle adapté pour les œuvres d'adaptation audiovisuelle de spectacles ; les artistes-interprètes qui assurent le commentaire ou la postsynchronisation des œuvres documentaires et d'animation. Dans les œuvres de fiction, un rôle principal requiert la présence à l'écran de l'artiste-interprète dans la moitié au moins des scènes de l'œuvre ; un rôle secondaire comporte au moins quatre cachets ;",
    "b. Les artistes musiciens engagés pour réaliser l'enregistrement sonore de leur interprétation ou de leur exécution d'œuvres musicales destinées à être incorporées aux œuvres cinématographiques ou audiovisuelles ;",
    "c. Les artistes du spectacle que les usages professionnels, notamment les conventions et accords collectifs de la production cinématographique ou audiovisuelle, qualifient d'artistes de complément, ainsi que les artistes-interprètes dont les rôles comportent moins de quatre cachets.",
    "II. – Les personnels visés au c du 1 et au c du 2 de l'article 46 quater-0 YM comprennent les catégories suivantes :",
    "1° Pour les œuvres cinématographiques ou audiovisuelles de fiction, les œuvres cinématographiques ou audiovisuelles documentaires et les œuvres d'adaptation audiovisuelle de spectacles :",
    "a. Les techniciens de la production chargés des fonctions suivantes : réalisation ; préparation et assistance de réalisation ; technique et qualité artistique des prises de vues ; technique et qualité artistique des enregistrements sonores ; création artistique et exécution des décors ; création artistique des costumes, perruques et accessoires vestimentaires ; confection des costumes et accessoires vestimentaires ; habillage et entretien des costumes ; maquillage de composition des acteurs ; confection des perruques et postiches et exécution des coiffures ; accessoires de plateau et de décor ; assemblage artistique et technique des images et des sons ; préparation et réalisation des effets spéciaux de tournage, y compris les cascades ; direction artistique et développement ; direction et gestion administrative, technique et comptable de la production ;",
    "b. Les ouvriers de la production chargés de la machinerie, de l'éclairage ou de la construction des décors ;",
    "2° Pour les œuvres cinématographiques ou audiovisuelles d'animation :",
    "a. Les techniciens de la production chargés des fonctions suivantes : réalisation ; assistance de réalisation, direction artistique et direction d'écriture de l'œuvre cinématographique ou audiovisuelle ; direction artistique et développement ; direction et gestion administrative, technique et comptable de la production ;",
    "b. Les collaborateurs chargés de la préparation de l'animation qui assurent les fonctions suivantes : création du scénarimage ; conception et modélisation des personnages ; conception et modélisation des décors ; feuilles d'exposition ;",
    "c. Les collaborateurs chargés de la fabrication de l'animation qui assurent les fonctions suivantes : mise en place de l'animation ; exécution de l'animation ; mise en place des décors ; exécution des décors ; traçage-gouachage, colorisation, rendu et éclairage ; assemblage numérique ; effets spéciaux ; assemblage artistique et technique des images et du son."
], "Réécriture à droit constant : les catégories d'artistes et de personnels sont formulées directement et les fonctions sont énumérées sans les répétitions de construction de la source. L'intégralité des métiers, des genres d'œuvres et des seuils de rôle est conservée. Aucune réforme de fond du périmètre des personnels éligibles n'est introduite.",
    "Maintien des I et II, des a à c du I, des 1° et 2° du II et de leurs lettres. Contrôle des seuils : moitié au moins des scènes pour les rôles principaux, au moins quatre cachets pour les rôles secondaires et moins de quatre cachets au c. Les listes de fonctions restent intégrales, y compris cascades, perruques, feuilles d'exposition et traçage-gouachage. La source vise collectivement au I le b du 2 de l'article 46 quater-0 YM, qui ne mentionne que les artistes-interprètes et non les artistes de complément ; cette différence de champ préexistante est conservée et doit être contrôlée sans élargissement silencieux de l'assiette de l'animation.")

article(22, [
    "Pour l'application des articles 220 sexies et 220 F du code général des impôts, les entreprises déclarent les réductions et crédits d'impôt dans le format établi par l'administration. Elles respectent les mêmes délais que pour la déclaration annuelle de résultat qu'elles doivent souscrire en application de l'article 223 du même code.",
    "Lorsqu'elle dépose la déclaration du résultat d'ensemble du groupe, la société mère d'un groupe au sens de l'article 223 A du même code déclare les réductions et crédits d'impôt pour le compte de toutes les sociétés du groupe, y compris ceux qui la concernent."
], "Réécriture à droit constant : le format et le délai de déclaration sont distingués ; le dépôt par la société mère est formulé directement en conservant le compte de toutes les sociétés. Aucune réforme de fond des crédits ou de l'intégration fiscale n'est introduite.",
    "Maintien des deux alinéas et des renvois aux articles 220 sexies, 220 F, 223 et 223 A. Le calendrier reste celui de la déclaration annuelle, et celui du résultat d'ensemble pour la société mère ; aucune nouvelle échéance ni dispense de déclaration n'est créée.")

article(23, [
    "Le crédit d'impôt en faveur des entreprises de production cinématographique et des entreprises de production audiovisuelle s'impute sur l'impôt dû après l'imputation des prélèvements non libératoires et des crédits d'impôt non restituables."
], "Réécriture à droit constant : l'ordre des imputations est rendu explicite en précisant l'opération à laquelle le mot « après » se rapporte. Aucune modification de fond du crédit d'impôt ou de sa restitution n'est introduite.",
    "Les deux catégories d'entreprises et la priorité des prélèvements non libératoires et des crédits d'impôt non restituables sont conservées. Aucune règle d'imputation sur une part territoriale future de l'IS n'est présumée ; cette articulation relève de la disposition législative créant cette part et de la coordination de l'article 220 F.")

drafts[19] = {
    'proposed_xml': '\n'.join(Path(p).read_text().strip() for p in [
        'fragments/46-quater-0-YM-fiction.xml',
        'fragments/46-quater-0-YM-animation.xml',
    ]),
    'reason': "Réécriture intégrale à droit constant : les dépenses sont formulées directement, les longues séries techniques sont ponctuées et les conditions de rémunération, de cotisations obligatoires et d'emploi permanent sont explicitées. Les deux branches, fiction-documentaire-spectacle et animation, ainsi que le d bis consacré aux spectacles, restent distinctes et complètes. Aucune réforme de fond de l'assiette, aucun plafond nouveau et aucune suppression d'aide ne sont introduits.",
    'review_notes': "Les 29 alinéas et toutes les subdivisions sont conservés, notamment l'alinéa distinct qui complète le 2° du d du 1 et le d bis avec ses 1°, 2° et trois composantes du coût plateau. Maintien de tous les postes techniques, de l'exclusion des lieux d'habitation, de la limitation des charges aux cotisations obligatoires et des périodes d'emploi ou d'amortissement. Pour chacune des deux branches, les plafonds restent de 200 et 500 euros par trajet et par personne, de 30 euros par repas et par personne et de 270 ou 200 euros par nuitée selon le département. La condition de tournage à l'étranger pour des raisons artistiques liées au scénario et aux décors naturels ou historiques est intégralement conservée. Contrôler l'articulation des compléments de droits artistiques des a et b avec le d bis, sans en déduire un double décompte. La proposition de réexamen des aides n'identifie pas ce crédit comme supprimé ; aucun retrait ni modification des contrats existants n'est donc introduit."
}


assert len(sources) == 24
assert set(drafts) == set(range(24))
answer = []
for index, source in enumerate(sources):
    item = {key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')}
    item.update(drafts[index])
    item['status'] = 'rewrite_draft'
    answer.append(item)

Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
