import json
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
drafts = {}


def add(number, paragraphs, reason, review_notes):
    assert number not in drafts
    drafts[number] = {
        'proposed_xml': ''.join('<p>' + p + '</p>' for p in paragraphs),
        'reason': reason,
        'review_notes': review_notes,
        'status': 'rewrite_draft',
    }


add('296', [
    "La personne morale adresse sa déclaration au service des impôts dont dépend le lieu où l'impôt sur les sociétés est établi.",
], "Réécriture à droit constant : le déclarant est nommé et la compétence du service destinataire est formulée directement. Aucune réforme de fond n'est appliquée à cette formalité.",
    "Le sujet est explicité à partir de l'article 295 de la présente annexe, consulté dans le corpus fourni. Le critère reste le lieu d'établissement de l'impôt, et non celui du siège de la personne morale.")

add('297', [
    "La personne morale souscrit la déclaration au plus tard dans les trois mois suivant la clôture du premier exercice au cours duquel elle est devenue passible de l'impôt sur les sociétés. Toutefois, si elle opte pour le régime des sociétés de capitaux dans les conditions prévues à l'article 239 du code général des impôts, elle produit la déclaration dans le délai fixé pour notifier cette option.",
    "Lorsque le changement de régime fiscal résulte d'un acte soumis à l'enregistrement dans un délai déterminé, la personne morale souscrit la déclaration dans ce même délai et la présente au même service des impôts.",
], "Réécriture à droit constant : les obligations de la personne morale sont exprimées à la forme active et les trois règles de délai sont distinguées dans les deux alinéas existants. Aucune réforme de fond.",
    "Conservation du délai de trois mois, de son rattachement à la clôture du premier exercice concerné, de l'exception de l'article 239 du CGI et de la règle particulière applicable à l'acte soumis à enregistrement. Aucun déplacement de l'alinéa relatif à cet acte.")

add('298', [
    "La personne morale inscrit chaque bien ou droit sur la déclaration pour sa valeur vénale estimée à la date d'ouverture de la première période d'imposition à l'impôt sur les sociétés.",
], "Réécriture à droit constant : la personne tenue de déclarer est désignée et l'inscription de chaque bien ou droit est formulée à la forme active. La valeur à retenir et sa date d'appréciation sont conservées ; aucune réforme de fond.",
    "La valeur reste la valeur vénale estimée à l'ouverture de la première période d'imposition, et non à la date de dépôt ou à celle de la clôture de l'exercice. Articulation conservée avec la déclaration de l'article 295.")

add('299', [
    "Lorsqu'elle dépose la déclaration, la personne morale acquitte les droits et taxes exigibles.",
    "Toutefois, si elle a présenté une demande régulière de paiement fractionné, elle n'acquitte que le premier versement lors de ce dépôt.",
], "Réécriture à droit constant : le redevable et le moment du paiement sont explicités, puis l'exception du paiement fractionné est énoncée à la forme active dans son alinéa d'origine. Aucune réforme de fond.",
    "L'exception demeure subordonnée à une demande régulière ; elle ne dispense pas du premier versement au dépôt. Aucun montant ni échéancier supplémentaire n'est créé.")

add('301', [
    "Pour les sociétés françaises comme pour les sociétés étrangères, les articles 295 à 299 ne s'appliquent qu'aux biens dont l'assiette est située en France : l'assiette matérielle pour les biens corporels et l'assiette juridique pour les biens incorporels.",
], "Réécriture à droit constant : le champ territorial est présenté avant les deux critères d'assiette, avec une correspondance explicite entre la nature du bien et le critère applicable. Aucune réforme de fond.",
    "Renvoi aux articles 295 à 299 et distinction entre sociétés françaises et étrangères conservés. La note relative à l'article 64-V de la loi n° 2008-776 du 4 août 2008 est une indication historique ; elle ne fixe aucune entrée en vigueur nouvelle.")

add('301 A', [
    "Les fusions, scissions et apports partiels d'actif définis aux articles 301 B à 301 F bénéficient du régime spécial prévu aux articles 816 à 817 A du code général des impôts.",
], "Réécriture à droit constant : les opérations auxquelles s'applique le régime deviennent le sujet de la phrase et les deux ensembles de renvois sont maintenus. Aucune réforme de fond.",
    "Les articles 816, 817 et 817 A du CGI ont été consultés dans le corpus : l'article 816 prévoit l'enregistrement gratuit et l'article 817 A renvoie aux articles 301 A à 301 F. Le renvoi englobant 816 à 817 A est conservé ; il ne s'agit pas d'une coordination du taux normal d'IS.")

add('301 B', [
    "Constitue une fusion l'une des opérations suivantes :",
    "– soit la création d'une société relevant du statut fiscal des sociétés de capitaux par plusieurs sociétés qui lui transfèrent l'ensemble de leur actif et de leur passif ;",
    "– soit le transfert, par une ou plusieurs sociétés, de l'ensemble de leur actif et de leur passif à une société relevant du statut fiscal des sociétés de capitaux. Dans les deux cas, la ou les sociétés apporteuses sont dissoutes et les apports sont rémunérés dans les conditions prévues à l'article 301 F.",
], "Réécriture à droit constant : les deux formes de fusion sont rendues plus lisibles et une phrase distincte précise les conditions communes de dissolution et de rémunération. Ces conditions restent dans le troisième alinéa ; aucune réforme de fond.",
    "Les trois alinéas et les deux branches de la définition sont conservés. La dissolution et le renvoi à l'article 301 F s'appliquent toujours aux deux opérations ; le transfert porte sur l'ensemble de l'actif et du passif.")

add('301 C', [
    "I. – Est assimilée à une fusion l'opération par laquelle des droits représentant au moins 75 % du capital d'une société relevant du statut fiscal des sociétés de capitaux sont transférés à une société relevant du même statut, en voie de formation ou préexistante. Cette assimilation s'applique lorsque les deux sociétés ont leur siège de direction effective ou leur siège statutaire en France ou dans un autre État membre de l'Union européenne et que les apports sont rémunérés dans les conditions prévues à l'article 301 F.",
    "Lorsque le seuil de 75 % est atteint à la suite de plusieurs opérations, le régime spécial s'applique uniquement à l'opération qui permet d'atteindre ce seuil et aux opérations qui l'augmentent.",
    "II. – Dans le cas prévu au I, la société à laquelle les droits sont apportés doit, sous peine de perdre le bénéfice du régime spécial, les conserver pendant cinq ans à compter de la date de leur transfert, soit sous forme nominative, soit dans les conditions prévues au a du 1 de l'article 145 du code général des impôts. Les droits qu'elle a acquis antérieurement et qu'elle détient à cette même date doivent être conservés dans les mêmes conditions.",
    "Le bénéfice du régime spécial est maintenu si les droits sont compris, avant l'expiration de ce délai, dans une opération de fusion ou assimilée, de scission ou d'apport partiel d'actif, ou s'ils sont cédés dans le cadre de la liquidation de la société à laquelle ils ont été apportés.",
], "Réécriture à droit constant : la définition et ses conditions sont réparties en phrases plus courtes, puis les règles de franchissement du seuil, de conservation et de maintien du régime sont exprimées directement. Les I et II ainsi que leurs alinéas sont préservés ; aucune réforme de fond.",
    "Contrôle des deux occurrences de 75 %, du délai de cinq ans courant du transfert, de l'inclusion des droits déjà détenus et des deux formes de conservation. Les quatre catégories d'opérations dérogatoires, la cession lors de la liquidation, le renvoi au a du 1 de l'article 145 du CGI et celui à l'article 301 F sont maintenus.")

add('301 D', [
    "Constitue une scission l'opération par laquelle une société transfère, à compter d'une même date, l'ensemble de son actif et de son passif à plusieurs sociétés relevant du statut fiscal des sociétés de capitaux, en voie de formation ou préexistantes. Cette qualification suppose que la société apporteuse soit dissoute et que les apports soient rémunérés dans les conditions prévues à l'article 301 F.",
], "Réécriture à droit constant : la définition du transfert est séparée des conditions de dissolution et de rémunération, au sein du même alinéa. Aucune réforme de fond.",
    "La date commune d'effet, le transfert intégral de l'actif et du passif, la pluralité des sociétés bénéficiaires et leur statut fiscal sont conservés. Le renvoi à l'article 301 F n'est pas modifié.")

add('301 E', [
    "Constitue un apport partiel d'actif l'opération par laquelle une société apporte à une société relevant du statut fiscal des sociétés de capitaux, en voie de formation ou préexistante, l'ensemble des éléments constituant une ou plusieurs branches complètes et autonomes d'activité. Cette qualification suppose que l'opération n'entraîne pas la dissolution de la société apporteuse et qu'elle soit rémunérée dans les conditions prévues à l'article 301 F.",
], "Réécriture à droit constant : l'objet de l'apport est formulé plus directement et les conditions d'absence de dissolution et de rémunération sont isolées dans une seconde phrase du même alinéa. Aucune réforme de fond.",
    "Les qualifications de branche complète et autonome, la possibilité d'une ou de plusieurs branches et le statut fiscal de la bénéficiaire sont maintenus. Absence de dissolution et rémunération selon l'article 301 F restent cumulatives.")

add('301 F', [
    "La rémunération des apports mentionnés aux articles 301 B à 301 E consiste en l'attribution de droits représentatifs du capital de la société bénéficiaire. Toutefois, une autre forme de règlement est admise dans la limite de 10 % de la valeur nominale des droits attribués.",
    "Dans les situations prévues au II de l'article L. 236-3 du code de commerce, la condition d'attribution de droits représentatifs du capital de la société bénéficiaire prévue à l'alinéa précédent ne s'applique pas.",
], "Réécriture à droit constant : le mode de rémunération, la tolérance de règlement sous une autre forme et l'exception légale sont formulés directement. Les deux alinéas sont conservés ; aucune réforme de fond.",
    "Le plafond de 10 % reste calculé sur la valeur nominale des droits attribués, et non sur la valeur des apports. Le renvoi au II de l'article L. 236-3 du code de commerce est conservé sans substitution : ce code n'est pas inclus dans le corpus fourni et son articulation actuelle reste à contrôler. L'exception ne supprime expressément que la condition d'attribution de droits.")

add('301 J', [
    "Lorsqu'une fusion relève du neuvième alinéa du b de l'article 885 I bis du code général des impôts, la personne qui a bénéficié du régime prévu par cet article fournit une attestation de la société bénéficiaire mentionnée à l'article 301 F. Cette attestation certifie la conservation des titres reçus en contrepartie de l'opération. Elle est fournie jusqu'à l'année qui suit celle du terme de l'engagement collectif de conservation.",
], "Réécriture à droit constant : le fait déclencheur, l'auteur de l'attestation, son objet et la durée de l'obligation sont présentés en trois phrases dans l'alinéa existant. Aucune réforme de fond ni extension à un autre régime de conservation de titres.",
    "L'article 885 I bis du CGI n'est pas présent dans le corpus fourni. Le renvoi historique au neuvième alinéa de son b est maintenu, ainsi que le renvoi à l'article 301 F ; la survie de l'obligation pour les engagements anciens nécessite un contrôle de la version historique et des dispositions transitoires applicables. Aucun remplacement par un dispositif actuel ni nouvelle périodicité n'est inventé.")

add('302', [
    "Outre les mentions prescrites par l'article 67 du code de procédure civile, les huissiers doivent faire figurer distinctement les indications suivantes au bas de l'original et des copies de chaque exploit :",
    "1° Le nombre de feuilles de papier utilisées pour les copies de l'original comme pour les copies des pièces signifiées ;",
    "2° Le montant des droits de timbre dus en fonction de la dimension de ces feuilles.",
], "Réécriture à droit constant : l'obligation de mention est exprimée directement et les deux éléments à indiquer sont formulés plus simplement. La numérotation 1° et 2° est maintenue ; aucune réforme de fond.",
    "Le vocabulaire historique « huissiers », le renvoi à l'article 67 du code de procédure civile et le dispositif de timbre lié à la dimension du papier sont conservés. Leur applicabilité actuelle et l'articulation avec le statut des commissaires de justice doivent être contrôlées dans les textes historiques, procéduraux et statutaires hors du corpus ; aucune actualisation silencieuse n'est opérée.")

add('302 A', [
    "Le remboursement du droit de timbre des copies ne peut être alloué en taxe pour un montant supérieur à la valeur des timbres mobiles apposés en application des dispositions qui précèdent. Les officiers ministériels ne peuvent demander ni se faire payer, à ce titre, une somme supérieure à cette même valeur.",
], "Réécriture à droit constant : la limite applicable à l'allocation en taxe et celle opposable aux officiers ministériels sont distinguées en deux phrases du même alinéa. Aucune réforme de fond.",
    "Le plafond reste la valeur des timbres mobiles effectivement apposés selon les dispositions précédentes. La référence au mécanisme historique de timbre des copies est conservée ; son applicabilité doit être examinée avec celle de l'article 302, sans créer de nouveau droit ou tarif.")

add('306-0 F', [
    "I. – Les organismes d'assurance et assimilés ne peuvent se libérer des sommes, rentes ou valeurs quelconques qu'ils doivent, en raison du décès de l'assuré, à chaque bénéficiaire désigné au contrat et qui relèvent de l'article 990 I du code général des impôts qu'après avoir déclaré à l'administration fiscale les éléments mentionnés aux I et II de l'article 370 C. Cette déclaration doit être faite dans les soixante jours suivant le jour où ils ont eu connaissance du décès de l'assuré. Elle comprend également, pour chaque contrat et chaque bénéficiaire, les éléments suivants :",
    "a. L'assiette retenue pour le prélèvement ;",
    "b. Le montant de chacun des abattements pratiqués ;",
    "c. Le montant du prélèvement acquitté sur les sommes, rentes ou valeurs dues à chaque bénéficiaire ;",
    "d. La date de souscription et le numéro de police du ou des avenants prévus à l'article L. 112-3 du code des assurances qui sont de nature à transformer l'économie même du contrat ;",
    "e. Pour la fraction rachetable de chaque contrat mentionné au I de l'article 990 I du code général des impôts, la part de la valeur de rachat au jour du décès de l'assuré correspondant aux sommes, rentes ou valeurs dues à raison des primes versées à compter du 13 octobre 1998 ; pour la fraction rachetable de chaque contrat comportant une clause de paiement différé du capital par l'assureur au bénéficiaire, la valeur de rachat déterminée au jour du versement des sommes, rentes ou valeurs quelconques ;",
    "f. Pour la fraction non rachetable de chaque contrat mentionné au I de l'article 990 I du code général des impôts, le produit du montant du capital-décès dû, diminué de la valeur de rachat au jour du décès de l'assuré, par le taux de mortalité correspondant à l'âge de l'assuré lors de son décès dans la table de mortalité applicable à cette date ; pour les contrats non rachetables, la prime annuelle ou le montant de la prime unique versée à la souscription du contrat, lorsque cette souscription est intervenue à compter du 13 octobre 1998.",
    "II. – Les organismes déclarent les éléments mentionnés au I dans les conditions prévues aux V à VII de l'article 370 C.",
    "III. – (Sans objet).",
], "Réécriture à droit constant : la déclaration préalable au paiement, son délai et son contenu sont répartis en phrases distinctes ; les assiettes et les calculs des fractions rachetable et non rachetable sont reformulés sans les modifier. Les I à III et les lettres a à f restent en place. Aucune réforme de fond du prélèvement ou des contrats d'assurance.",
    "Conservation des soixante jours à compter de la connaissance du décès, des deux occurrences du 13 octobre 1998, de l'évaluation au versement pour le capital différé et de la formule capital-décès diminué de la valeur de rachat, multiplié par le taux de mortalité. Pour le contrat non rachetable, la condition de date porte toujours sur la souscription. L'article 370 C a été consulté : son VII prévoit des déclarations complémentaires pour les éléments connus ultérieurement ; le renvoi intégral aux V à VII est maintenu. Le champ de l'article 990 I reste distinct du nouveau compte de retraite envisagé par policy.json.")

add('306-0 F bis', [
    "I. – Le patrimoine immobilier des sociétés mentionnées aux d et e du 1 du I bis de l'article 990 I du code général des impôts et l'actif des organismes de placement collectif mentionnés au même e sont constitués d'immeubles bâtis remplissant les conditions prévues aux a à c de l'article 279-0 bis A du même code, d'immeubles bâtis financés dans les conditions prévues aux articles D. 331-17 à D. 331-21 du code de la construction et de l'habitation ou de droits réels portant sur ces derniers immeubles.",
    "II. – Pour la société émettrice des titres mentionnés au b du 2° du 2 du I bis de l'article 990 I du code général des impôts, le nombre de salariés, le chiffre d'affaires et le total de bilan sont appréciés selon les conditions définies aux articles 1er, 3, 5 et 6 de l'annexe I au règlement (CE) n° 800/2008 de la Commission du 6 août 2008 déclarant certaines catégories d'aide compatibles avec le marché commun en application des articles 87 et 88 du traité.",
    "Si la société émettrice des titres a pour objet principal de détenir des participations dans d'autres sociétés, ces conditions sont appréciées au niveau de cette société et de chacune des sociétés dans lesquelles elle détient des participations.",
    "Pour apprécier les conditions mentionnées au premier alinéa du II, les données retenues sont celles du dernier exercice comptable précédant la date d'acquisition des titres, déposé au greffe du tribunal de commerce ou rendu public par un dispositif équivalent. Ces données sont calculées sur une base annuelle.",
    "II bis. – Pour l'application du c du 2° du 2 du I bis de l'article 990 I du code général des impôts, constituent des actifs relevant de l'économie sociale et solidaire les titres émis par les entreprises agréées « entreprise solidaire d'utilité sociale » en application de l'article L. 3332-17-1 du code du travail, ainsi que les parts ou actions d'organismes de placement collectif comprenant au moins 5 % de titres émis par ces entreprises.",
    "III. – La proportion d'investissement prévue au neuvième alinéa du 2 du I bis de l'article 990 I du code général des impôts s'apprécie en rapportant la valeur des titres mentionnés au 1° et aux a à c du 2° du 2 du I bis de l'article 990 I du même code à la valeur totale des actifs composant chaque unité de compte du contrat. La valeur des titres est calculée d'après leur dernière valeur connue, hors frais d'assurance.",
    "Après le premier versement de primes, ce rapport doit être au moins égal à 33 %.",
    "Une opération d'arbitrage entre unités de compte, de rachat partiel ou de versement de nouvelles primes ne peut diminuer ce rapport que s'il était supérieur à 33 % avant l'opération. Dans ce cas, le rapport ne peut devenir inférieur à 33 % du fait de l'opération.",
    "Si le rapport était inférieur à 33 % avant une telle opération, celle-ci ne peut pas le diminuer.",
    "Lorsque le rapport devient inférieur à 33 % en dehors des opérations mentionnées ci-dessus, le contrat est réputé respecter la proportion d'investissement.",
    "Un contrat qui permet d'acquérir des engagements exprimés en euros ou donnant lieu à des provisions de diversification est réputé respecter ce taux si et seulement si l'ensemble des primes versées est affecté à des engagements exprimés en unités de compte remplissant les conditions du présent III.",
    "IV. – Les organismes ou sociétés mentionnés aux 3 et 4 du I bis de l'article 990 I du code général des impôts tiennent à la disposition de l'administration fiscale tout document justifiant la valeur retenue, dans les conditions du présent article, pour déterminer la proportion d'investissement prévue au neuvième alinéa du 2 du I bis de l'article 990 I du code général des impôts. S'ils n'ont pas la personnalité morale, cette obligation incombe à leur gérant ou à leur représentant à l'égard des tiers.",
], "Réécriture à droit constant : les catégories immobilières, l'appréciation des caractéristiques des sociétés et le calcul de la proportion d'investissement sont exprimés plus directement. Les différents cas de variation du rapport sont conservés chacun dans son alinéa, ainsi que les I, II, II bis, III et IV. Aucune réforme de fond des contrats d'assurance ou des règles d'investissement.",
    "Le seuil de 5 %, les cinq occurrences de 33 %, la dernière valeur connue hors frais d'assurance, la base annuelle et l'exercice antérieur à l'acquisition sont conservés. À 33 % exactement, l'opération ne peut pas diminuer le rapport : le mot « supérieur » est maintenu. Les droits réels du I portent toujours sur les seuls derniers immeubles mentionnés. Le renvoi au neuvième alinéa du 2 du I bis de l'article 990 I a été vérifié dans le corpus ; les articles D. 331-17 et D. 331-21 y sont présents. L'espacement de « 3,5 » est normalisé en « 3, 5 » dans la liste d'articles du règlement n° 800/2008, sans substitution d'un autre règlement ; la portée temporelle de cette référence européenne ancienne reste à contrôler hors du corpus. La note du décret n° 2019-873 du 21 août 2019 est historique, sans effet nouveau sur les contrats anciens.")

add('306 F', [
    "Le directeur départemental ou, le cas échéant, régional des finances publiques prend les décisions relatives à l'agrément du représentant que l'assureur étranger désigne en application de l'article 1004 du code général des impôts.",
], "Réécriture à droit constant : l'autorité qui prend la décision et l'assureur qui désigne le représentant sont les sujets explicites des propositions. Aucune réforme de fond de la compétence ou de l'agrément.",
    "La compétence départementale ou, le cas échéant, régionale est conservée. L'article 1004 du CGI, consulté dans le corpus, vise les assureurs étrangers établis hors de l'Espace économique européen ; le renvoi demeure déterminant pour ce champ, sans extension à tous les assureurs étrangers.")

add('310 G', [
    "I. – L'acquéreur, le donataire, l'héritier ou le légataire qui souhaite bénéficier de l'exonération de droits et taxes prévue à l'article 1131 du code général des impôts dépose une offre de donation à l'État auprès du service des impôts compétent pour enregistrer l'acte constatant la mutation ou la déclaration de succession. L'offre précise le ou les biens concernés et, le cas échéant, les conditions auxquelles elle est soumise. Le service en délivre récépissé.",
    "L'offre doit être présentée dans le délai prévu pour enregistrer l'acte constatant la mutation ou la déclaration de succession.",
    "II. – Le service des impôts transmet l'offre de donation à une commission dont la composition est fixée par arrêté conjoint du Premier ministre, du ministre chargé de la culture et du ministre chargé du budget.",
    "Avant de se prononcer, la commission recueille l'avis du ministre intéressé par l'affectation éventuelle des biens offerts. Ce ministre est invité à désigner un représentant qui participe, avec voix consultative, aux travaux de la commission relatifs à cette offre.",
    "La commission consulte, selon le cas, le ou les organismes compétents pour l'acquisition d'œuvres d'art, de livres, d'objets de collection ou de documents de haute valeur artistique ou historique.",
    "Elle donne un avis sur l'intérêt artistique ou historique du bien offert ainsi que sur sa valeur.",
    "Au vu de cet avis, le ministre compétent propose au ministre de l'économie et des finances d'accorder ou de refuser l'agrément.",
    "La décision est notifiée au demandeur par pli recommandé avec demande d'avis de réception.",
    "III. – Si l'agrément est accordé, le demandeur dispose du délai fixé par la décision pour accepter les conditions auxquelles cet agrément est subordonné.",
    "Le demandeur notifie son acceptation au ministre de l'économie et des finances par pli recommandé avec demande d'avis de réception.",
    "IV. – L'offre est considérée comme refusée si aucune décision n'a été notifiée dans le délai d'un an à compter de la date de son récépissé.",
], "Réécriture à droit constant : les démarches du demandeur, du service et de la commission sont formulées à la forme active et les longues phrases sont divisées sans déplacer les alinéas. Deux défauts grammaticaux de la source sont explicitement signalés dans les notes de contrôle. Aucune réforme de fond de la donation ou de l'agrément.",
    "Les I à IV et leurs onze alinéas, le délai légal de dépôt, le délai d'acceptation fixé par la décision et le refus après un an sans décision notifiée sont maintenus. La source contient « du documents » et « sur l'intérêt artistique ou historique que sur la valeur » : la proposition lit respectivement « de documents » et « sur l'intérêt artistique ou historique du bien offert ainsi que sur sa valeur » ; cette restitution de l'objet double de l'avis nécessite confirmation matérielle. L'article 1131 du CGI a été consulté et conserve la nécessité de l'agrément puis de l'acceptation. Les notes retracent les renouvellements de la commission en 2009, 2014 et 2015, ce dernier jusqu'au 8 juin 2020 ; elles ne permettent pas de constater son renouvellement ultérieur. La continuité de la commission et sa composition restent à contrôler dans les textes hors du corpus, sans renouvellement fictif.")

add('310 G bis', [
    "Lorsque le ministre chargé du budget envisage, en application des I et V de l'article 1378 octies du code général des impôts, de suspendre les avantages fiscaux attachés aux dons, legs et versements effectués au profit d'un organisme, il informe cet organisme par lettre recommandée avec demande d'avis de réception postale.",
    "L'organisme dispose de trente jours pour présenter ses observations écrites et, s'il le demande, ses observations orales. Il peut se faire assister par la personne de son choix.",
    "Au vu des éléments du dossier et, le cas échéant, des observations présentées, le ministre chargé du budget décide de suspendre ou de maintenir les avantages fiscaux mentionnés au premier alinéa dans un délai de six mois à compter de la réception de la déclaration ou du rapport prévus respectivement aux I et V de l'article 1378 octies du code général des impôts.",
    "L'arrêté de suspension indique les motifs de la décision et les conditions dans lesquelles l'organisme peut demander le rétablissement des avantages fiscaux suspendus. Il est notifié par lettre recommandée avec demande d'avis de réception postale.",
    "Si le ministre décide de ne pas suspendre les avantages fiscaux mentionnés au premier alinéa, sa décision est notifiée par lettre simple.",
], "Réécriture à droit constant : la notification initiale, les observations de l'organisme et la décision du ministre sont exprimées directement ; l'assistance et les observations orales sont distinguées sans changer leurs conditions. Les cinq alinéas sont conservés. Aucune réforme de fond.",
    "Conservation des trente jours, des six mois à compter de la réception de la déclaration ou du rapport, et de la distinction entre notification recommandée et lettre simple. Les I et V de l'article 1378 octies du CGI ont été consultés. L'arrêté de suspension reste au quatrième alinéa, expressément visé par l'article 310 G quater ; aucun déplacement ni confusion avec la condamnation du II de l'article 1378 octies.")

add('310 G ter', [
    "La demande de rétablissement des avantages fiscaux attachés aux dons et legs, mentionnée aux 1 et 2 du IV de l'article 1378 octies du code général des impôts, est adressée à la direction générale des finances publiques par lettre recommandée avec demande d'avis de réception postale.",
    "La direction générale des finances publiques transmet cette demande à la Cour des comptes pour avis dans un délai d'un mois à compter de sa réception.",
], "Réécriture à droit constant : l'objet de la demande est placé avant son fondement et le service chargé de la transmission est nommé. Les deux alinéas et le délai de saisine pour avis sont conservés ; aucune réforme de fond.",
    "Le délai d'un mois court de la réception de la demande. Le IV de l'article 1378 octies du CGI, consulté dans le corpus, distingue l'avis du 1 et l'avis conforme du 2, avec leurs effets propres du silence après six mois ; le renvoi préserve cette distinction. La source du présent article ne mentionne que les dons et legs, alors que le IV vise aussi les versements : cette différence préexistante est signalée sans élargissement silencieux.")

add('310 G quater', [
    "Lorsque le ministre chargé du budget rétablit les avantages fiscaux suspendus, sa décision est notifiée à l'organisme par lettre simple dans les trois mois suivant la réception de l'avis de la Cour des comptes ou, le cas échéant, l'expiration du délai de six mois mentionné au IV de l'article 1378 octies du code général des impôts.",
    "La décision qui abroge l'arrêté de suspension prévu au quatrième alinéa de l'article 310 G bis est publiée au Journal officiel de la République française.",
], "Réécriture à droit constant : le délai de notification est formulé plus directement et la décision publiée est désignée par une proposition explicite. Les deux alinéas sont préservés ; aucune réforme de fond.",
    "Conservation du délai de trois mois et de ses deux points de départ, de la lettre simple et de la publication au Journal officiel. Le quatrième alinéa de l'article 310 G bis reste celui de l'arrêté de suspension dans la proposition correspondante. Le renvoi au IV de l'article 1378 octies, vérifié dans le corpus, conserve les règles propres aux avis et au silence de la Cour des comptes.")

add('310 G quinquies', [
    "Si le ministre chargé du budget rejette la demande de rétablissement des avantages fiscaux suspendus, sa décision doit être motivée et notifiée à l'organisme par lettre recommandée avec demande d'avis de réception postale. La notification intervient dans les trois mois suivant la réception de l'avis de la Cour des comptes ou, le cas échéant, l'expiration du délai de six mois prévu au IV de l'article 1378 octies du code général des impôts.",
], "Réécriture à droit constant : l'obligation de motivation et de notification est distinguée du délai applicable, en deux phrases dans l'alinéa existant. Aucune réforme de fond.",
    "Les trois mois, leurs deux points de départ, la motivation et le recommandé avec avis de réception postale sont conservés. Le renvoi au IV de l'article 1378 octies du CGI, consulté dans le corpus, n'est pas remplacé par une règle uniforme d'avis, afin de conserver la distinction entre ses 1 et 2.")

add('310-00 H', [
    "L'engagement de gestion prévu à l'article 1395 B bis du code général des impôts oblige à conserver le caractère humide des parcelles et à les maintenir en nature de prés et prairies naturels, d'herbages, de pâturages, de landes, de marais, de pâtis, de bruyères et de terres vaines et vagues. Dans les zones mentionnées au II de cet article, cet engagement impose aussi de respecter les mesures de conservation des zones humides définies dans les chartes et documents de gestion ou d'objectifs approuvés.",
], "Réécriture à droit constant : la portée obligatoire de l'engagement et les mesures supplémentaires propres aux zones du II sont exprimées par des verbes directs. La liste des natures de terrain et l'alinéa sont conservés ; aucune réforme de fond de l'exonération ou de la protection des zones humides.",
    "Tous les types de terrains et le caractère approuvé des chartes et documents sont maintenus. L'article 1395 B bis du CGI a été consulté : son III réserve l'exonération du I aux propriétaires ayant transmis l'engagement avant l'entrée en vigueur de la loi n° 2026-103 du 19 février 2026. Le renvoi demeure soumis à cette limitation, sans ouvrir de nouveaux droits. La note relative à la loi n° 2016-1087 du 8 août 2016 est historique.")

add('310-00 H bis', [
    "L'engagement de gestion prévu à l'article 1395 B bis du code général des impôts doit comporter les indications suivantes :",
    "1° L'identité et l'adresse du redevable de la taxe foncière sur les propriétés non bâties mentionné à l'article 1400 du même code et, le cas échéant, l'identité et l'adresse du preneur des parcelles concernées par l'engagement ;",
    "2° Les références cadastrales des parcelles, leurs natures de culture et de propriété définies dans l'instruction ministérielle du 31 décembre 1908, ainsi que la superficie des parcelles pour laquelle l'exonération de taxe foncière sur les propriétés non bâties est demandée ;",
    "3° Les mesures de conservation à mettre en œuvre pour respecter les engagements prévus à l'article 310-00 H.",
], "Réécriture à droit constant : les renseignements exigés sont présentés directement et l'identité ainsi que l'adresse du preneur sont explicitées pour lever l'anaphore. L'introduction et les 1° à 3° sont conservés ; aucune réforme de fond.",
    "Conservation de la mention éventuelle du preneur, du renvoi à l'article 1400 du CGI, des données cadastrales, des natures de culture et de propriété, de la superficie et des mesures de conservation. La référence au 31 décembre 1908 est maintenue. L'article 1395 B bis, consulté dans le corpus, comporte désormais au III une limitation aux engagements transmis avant l'entrée en vigueur de la loi n° 2026-103 du 19 février 2026 ; le présent article ne crée pas d'accès nouveau à l'exonération. La note relative à la loi du 8 août 2016 ne constitue pas une transition nouvelle.")


assert len(sources) == len(drafts) == 24
answer = []
for source in sources:
    answer.append({
        **{key: source[key] for key in ('code_id', 'source_id', 'source_sha256', 'number')},
        **drafts[source['number']],
    })
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
print(f'answer.json : {len(answer)} articles')
