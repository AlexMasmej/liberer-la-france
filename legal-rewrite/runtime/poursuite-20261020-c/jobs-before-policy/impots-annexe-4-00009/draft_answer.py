import json
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


add('49', '''
<p>L'article 276 du code général des impôts s'applique aux personnes ou sociétés mentionnées au I de l'article 284 de ce code, ainsi qu'à celles qui sont susceptibles de bénéficier des dispositions suivantes :</p>
<p>1° Le 10° du 4 de l'article 261 du même code ;</p>
<p>2° L'article 275 du même code, lorsqu'elles réalisent des exportations, des livraisons exonérées en vertu du I de l'article 262 ter du même code ou des livraisons dont le lieu est situé sur le territoire d'un autre État membre de l'Union européenne en application du 1° du I de l'article 258 A du même code ;</p>
<p>3° L'article 277 A du même code.</p>
''',
    "Réécriture à droit constant : le champ du cautionnement est exprimé directement et les trois catégories de bénéficiaires sont présentées dans leur ordre initial. Les conditions propres aux opérations mentionnées au 2° sont intégralement conservées. Aucune réforme de fond de policy.json ne vise ce cautionnement de TVA.",
    "Les trois subdivisions et les quatre alinéas sont conservés. La note source de l'article 2 de l'arrêté du 31 mai 2021 (NOR : CCPE2112747A) réserve l'application aux opérations dont le fait générateur de TVA intervient à compter du 1er juillet 2021 ; cette date historique n'est pas une date de réforme. Les renvois sont maintenus. Le corpus public signale notamment les articles 276 et 284 du CGI en état ABROGE_DIFF, avec une fin de version au 1er janvier 2027 : coordonner l'annexe avec les dispositions de recodification applicables sans anticiper un nouveau renvoi.")

add('50', '''
<p>Pour les redevables mentionnés à l'article 49, les droits susceptibles d'être mis à leur charge sont constitués de la taxe sur la valeur ajoutée et des impositions additionnelles à cette taxe éventuellement exigibles sur la vente, en l'état ou après transformation, à des destinations non exonérées, des matières ou produits reçus en franchise. Les pénalités susceptibles d'être mises à leur charge sont celles prévues au chapitre II du livre II du code général des impôts.</p>
''',
    "Réécriture à droit constant : la définition distingue les impositions susceptibles d'être exigibles des pénalités applicables. Les ventes en l'état et après transformation, les destinations non exonérées et les impositions additionnelles restent dans le champ. Aucune réforme de fond n'est appliquée.",
    "Le renvoi à l'article 49 et celui au chapitre II du livre II du CGI sont conservés, ainsi que le caractère éventuel des impositions. La coordination du cautionnement avec les textes auxquels renvoie l'article 49 doit suivre celle de cet article.")

add('50 bis', '''
<p>Les redevables mentionnés à l'article 49 peuvent choisir parmi les différents modes de cautionnement admis en matière de taxes sur le chiffre d'affaires.</p>
<p>Lorsque le cautionnement est personnel, la garantie demandée peut être fournie par une société de cautionnement constituée par un groupement professionnel ou interprofessionnel et spécialement agréé.</p>
''',
    "Réécriture à droit constant : les bénéficiaires du choix et la condition tenant au caractère personnel du cautionnement sont explicités dans deux alinéas. Le recours à une société issue d'un groupement professionnel ou interprofessionnel reste facultatif et soumis à l'agrément mentionné dans la source. Aucune réforme de fond n'est introduite.",
    "La source emploie « spécialement agréé » au masculin après une société constituée par un groupement. Le rattachement de l'agrément à la société ou au groupement est donc à contrôler ; la formulation finale de cette condition est conservée pour ne pas trancher silencieusement cette ambiguïté. Le renvoi à l'article 49 est maintenu.")

add('50 sexies B', '''
<p>I. – Avant l'accès aux lieux où sont organisés les spectacles mentionnés au I de l'article 290 quater du code général des impôts, toute entrée doit donner lieu à la remise d'un billet extrait d'un carnet à souches ou d'un distributeur automatique. À défaut de remise d'un billet, l'entrée doit, avant cet accès, être enregistrée et conservée dans un système informatisé.</p>
<p>II. – Les exploitants de spectacles qui utilisent un système de billetterie informatisée, avec ou sans impression de billets, doivent respecter les obligations du cahier des charges annexé à l'arrêté du 8 mars 1993.</p>
<p>III. – L'entrée doit être contrôlée manuellement ou électroniquement. Tout billet imprimé doit rester en possession du spectateur. Si ce billet comporte deux parties, l'une est laissée au spectateur et l'autre est retenue au contrôle.</p>
<p>Chaque partie du billet et, lorsque des carnets sont utilisés, la souche doivent porter les mentions suivantes, de manière apparente ou sous forme d'informations codées :</p>
<p>1° Le nom de l'exploitant ;</p>
<p>2° Le numéro d'ordre du billet ;</p>
<p>3° La catégorie de la place à laquelle le billet donne droit ;</p>
<p>4° Le prix global payé par le spectateur ou, le cas échéant, la mention de gratuité ;</p>
<p>5° Le nom du fabricant ou de l'importateur lorsque l'exploitant utilise des carnets ou des fonds de billets préimprimés.</p>
<p>Lorsque les billets comportent des mentions codées, le système doit permettre de restituer ces informations en clair.</p>
<p>Les billets extraits d'un carnet à souches ou émis sur des fonds de billets préimprimés doivent suivre une numérotation en série ininterrompue. Ils doivent être utilisés dans l'ordre de cette numérotation.</p>
<p>Outre les mentions prévues ci-dessus, les billets pris en abonnement ou en location doivent indiquer la séance pour laquelle ils sont valables.</p>
<p>Les billets émis au moyen d'un système informatisé doivent porter un identifiant unique, mémorisé dans ce système.</p>
<p>Un billet ne peut être utilisé que pour la catégorie de places qu'il indique.</p>
<p>IV. – La réglementation de l'industrie cinématographique fixe les obligations relatives aux mentions des billets d'entrée dans les établissements de spectacles cinématographiques, ainsi qu'à leur fourniture et à leur utilisation.</p>
<p>(2e à 6e alinéas supprimés)</p>
''',
    "Réécriture à droit constant : la délivrance ou l'enregistrement préalable, le contrôle d'entrée et les exigences de traçabilité sont formulés en obligations distinctes. Toutes les mentions, les règles de numérotation, l'identifiant unique et le régime particulier du cinéma sont conservés. Aucune réforme de fond ne vise la billetterie.",
    "Les I à IV, les 1° à 5° et l'ordre des alinéas sont maintenus, notamment les deuxième à septième alinéas du III visés par l'article 50 sexies C. La mention des alinéas supprimés est conservée. L'arrêté du 8 mars 1993 et le renvoi au I de l'article 290 quater restent inchangés ; le corpus signale ce dernier article en état ABROGE_DIFF, ce qui appelle une coordination de référence lorsque la recodification prendra effet.")

add('50 sexies C', '''
<p>Pour chaque représentation, les exploitants de spectacles peuvent utiliser des carnets spéciaux comportant, pour chaque catégorie de places, autant de billets que de places susceptibles d'être occupées.</p>
<p>Chaque billet et sa souche doivent indiquer, en plus des mentions prévues aux deuxième à septième alinéas du III de l'article 50 sexies B, le numéro de la place et la séance pour laquelle le billet est valable. Les billets correspondant à des places gratuites ou à prix réduit doivent être annulés et rester attachés à leur souche. Les carnets de chaque représentation doivent contenir les billets non délivrés ; l'exploitant doit les enliasser et les conserver.</p>
''',
    "Réécriture à droit constant : le caractère facultatif des carnets spéciaux et leur composition sont clarifiés. Les mentions supplémentaires et les obligations d'annulation, de rattachement à la souche, d'enliassement et de conservation sont rendues explicites. Aucune réforme de fond n'est introduite.",
    "Les deux alinéas sont maintenus. Le renvoi aux deuxième à septième alinéas du III de l'article 50 sexies B demeure exact dans la proposition de cet article. La règle source d'annulation des billets de places gratuites ou à prix réduit est conservée sans la transformer en exclusion de ces places.")

add('50 sexies D', '''
<p>Pour les représentations occasionnelles, les exploitants peuvent utiliser des cartes d'entrée munies d'un coupon détachable. La carte et le coupon doivent comporter les mentions exigées pour les billets et être utilisés dans les mêmes conditions que ces billets.</p>
''',
    "Réécriture à droit constant : le recours facultatif aux cartes d'entrée est rattaché aux exploitants et les exigences communes à la carte et au coupon sont formulées directement. Le champ reste limité aux représentations occasionnelles. Aucune réforme de fond n'est appliquée.",
    "Le coupon détachable, les mentions de billetterie et leurs conditions d'utilisation sont tous conservés. La coordination reste celle des règles de billets de la même section ; aucun renvoi nouveau n'est créé.")

add('50 sexies E', '''
<p>Lorsqu'un spectateur souhaite changer de place après la délivrance de son billet et que ce changement augmente le prix, un billet supplémentaire doit lui être délivré pour constater le complément de prix. Ce billet doit être établi dans les mêmes conditions que les autres billets et indiquer le montant du supplément encaissé.</p>
<p>L'obligation de mentionner le supplément de prix ne s'applique pas aux billets d'entrée dans les établissements de spectacles cinématographiques.</p>
<p>Lorsqu'un billet a été imprimé par une caisse automatisée ou un système informatisé dans les conditions prévues à l'article 50 sexies B et que le spectateur souhaite ensuite changer de catégorie de place, son billet doit être annulé. Un nouveau billet correspondant à la place souhaitée doit lui être délivré.</p>
''',
    "Réécriture à droit constant : les conséquences du changement de place sont distinguées selon l'augmentation de prix et le mode d'émission du billet. L'exception cinématographique reste limitée à la mention du supplément de prix. Aucune réforme de fond n'est introduite.",
    "Les trois alinéas et le renvoi à l'article 50 sexies B sont conservés. Le troisième alinéa continue de viser tout changement de catégorie après impression automatisée ou informatisée, sans le limiter aux changements entraînant un supplément.")

add('50 sexies F', '''
<p>I. – Les fabricants, importateurs ou marchands doivent déclarer les livraisons de billets ou de cartes d'entrée qu'ils effectuent aux exploitants de spectacles. Leur déclaration doit préciser :</p>
<p>1° Les noms et adresses des exploitants destinataires ;</p>
<p>2° Le nombre et les numéros des fonds de billets livrés.</p>
<p>II. – Les détenteurs ou propriétaires de logiciels de billetterie doivent déclarer leurs livraisons de billets ou de cartes d'entrée aux exploitants de spectacles qui utilisent leur logiciel. Leur déclaration doit préciser :</p>
<p>1° Les noms et adresses des exploitants de spectacles destinataires ;</p>
<p>2° Pour chaque catégorie de places, le nombre de billets ou de cartes d'entrée livrés, ainsi que les numéros des billets.</p>
<p>Les personnes soumises aux obligations déclaratives du présent article doivent adresser leurs déclarations au service des impôts dont elles dépendent dans les huit jours suivant les livraisons.</p>
<p>Les exploitants de spectacles qui achètent leurs billets directement à l'étranger sont considérés comme des importateurs. Ils sont soumis aux déclarations prévues au présent article.</p>
''',
    "Réécriture à droit constant : chaque catégorie de déclarants est reliée à ses livraisons et aux informations exigées. Le destinataire de la déclaration, le délai et l'assimilation à un importateur sont formulés en phrases directes. Aucune réforme de fond ni suppression de déclaration n'est introduite.",
    "Les I et II et leurs 1° et 2° sont maintenus. Le délai de huit jours suivant les livraisons est conservé. Le I continue de viser les fonds de billets et le II les quantités par catégorie de places et les numéros des billets, sans ajout de numéros de cartes absent de la source.")

add('50 sexies G', '''
<p>Les exploitants de spectacles sont comptables des billets qu'ils reçoivent ou impriment. À toute réquisition des agents des impôts, ils doivent présenter les coupons de contrôle et les billets non utilisés.</p>
<p>Les agents des impôts peuvent accéder aux lieux où sont organisés les spectacles pour y effectuer toutes les vérifications utiles.</p>
<p>Les caisses automatisées et les systèmes informatisés doivent comporter des dispositifs permettant aux agents des impôts chargés du contrôle de vérifier à tout moment que les matériels sont utilisés conformément aux cahiers des charges et que la réglementation en vigueur est respectée.</p>
''',
    "Réécriture à droit constant : la responsabilité des exploitants, la présentation des pièces et les pouvoirs de vérification sont énoncés séparément. Les dispositifs de contrôle permanent des caisses et systèmes conservent leurs deux finalités. Aucune réforme de fond n'est appliquée.",
    "Les trois alinéas sont maintenus. La présentation sur réquisition porte toujours sur les coupons de contrôle et les billets non utilisés ; les vérifications techniques restent possibles à tout moment et couvrent les cahiers des charges comme la réglementation.")

add('50 sexies H', '''
<p>Dès la fin de chaque journée ou représentation, les exploitants de spectacles doivent établir un relevé indiquant, pour chaque catégorie de places, le nombre de billets émis, le prix de la place et la recette correspondante.</p>
<p>Pour les billets qui ne sont pas émis au moyen d'un système informatisé, ce relevé doit également indiquer, pour chaque catégorie de places, les numéros du premier et du dernier billet délivrés.</p>
<p>Tout registre ou document comportant les indications exigées ci-dessus tient lieu de relevé.</p>
<p>Les exploitants doivent conserver les relevés selon les modalités prévues au I de l'article L. 102 B du livre des procédures fiscales et les tenir à la disposition des agents des impôts.</p>
''',
    "Réécriture à droit constant : le moment d'établissement et le contenu du relevé sont précisés avant les exigences supplémentaires propres aux billets non informatisés. Les documents équivalents et la conservation demeurent prévus. Aucune réforme de fond n'est introduite.",
    "Les quatre alinéas sont maintenus. L'alternative « journée ou représentation », le détail par catégorie et le renvoi au I de l'article L. 102 B du LPF sont conservés. Aucune durée de conservation différente n'est ajoutée.")

add('50 sexies I', '''
<p>I. – Toute personne qui utilise un système de billetterie informatisée doit respecter le cahier des charges annexé à l'arrêté du 8 mars 1993 modifié.</p>
<p>II. – Ces utilisateurs doivent déclarer la mise en service d'un système informatisé de billetterie ou de caisse enregistreuse à la direction des services fiscaux dont ils dépendent, au plus tard lors de sa première utilisation.</p>
<p>Pour décrire le système utilisé, la déclaration doit comporter les mentions suivantes :</p>
<p>1° Le nom du logiciel, son numéro de version et, le cas échéant, sa date, ainsi que l'identité de son concepteur ou le nom du progiciel ;</p>
<p>2° La configuration informatique ;</p>
<p>3° Le système d'exploitation ;</p>
<p>4° Le langage de programmation ;</p>
<p>5° Le format du logiciel source ou exécutable fourni par le concepteur ;</p>
<p>6° La description fonctionnelle du système ;</p>
<p>7° Le fac-similé d'un billet, d'un coupon de gestion et d'un relevé de recettes ;</p>
<p>8° Les sécurités mises en œuvre.</p>
<p>Les utilisateurs doivent porter les modifications du système à la connaissance de l'administration dans les conditions prévues au premier alinéa.</p>
''',
    "Réécriture à droit constant : les obligations de conformité, de déclaration initiale et d'information sur les modifications sont rattachées aux utilisateurs. Les huit rubriques descriptives et la limite de première utilisation sont conservées. Aucune réforme de fond n'est appliquée.",
    "Les I et II, les 1° à 8° et l'ordre des alinéas sont maintenus. La source renvoie en fin d'article au « premier alinéa » sans préciser s'il s'agit du premier alinéa du II : ambiguïté conservée et à contrôler. La dénomination historique « direction des services fiscaux » et l'arrêté du 8 mars 1993 modifié sont conservés, sans désigner un service successeur non vérifié.")

add('50 sexies J', '''
<p>Au titre du 2 de l'article 298 sexdecies F et du II de l'article 298 sexdecies G du code général des impôts, les informations à fournir sont les suivantes :</p>
<p>a. La raison sociale ;</p>
<p>b. L'adresse physique et, si elle est différente, l'adresse postale ;</p>
<p>c. La ou les adresses électroniques ;</p>
<p>d. Le nom de la personne physique à contacter dans l'entreprise ;</p>
<p>e. Le numéro de téléphone et l'adresse électronique de cette personne ;</p>
<p>f. La description de l'activité ;</p>
<p>g. Le numéro d'identification fiscal national ;</p>
<p>h. Le cas échéant, une déclaration attestant que l'entreprise n'a pas établi le siège de son activité économique sur le territoire de l'Union européenne et qu'elle n'y dispose pas d'un établissement stable.</p>
''',
    "Réécriture à droit constant : l'obligation d'information est annoncée directement et les coordonnées du contact sont reliées à la personne physique identifiée. Les huit rubriques et les deux éléments de l'attestation éventuelle sont conservés. Aucune réforme de fond ne vise ce régime de commerce électronique.",
    "Les lettres a à h et les renvois au 2 de l'article 298 sexdecies F et au II de l'article 298 sexdecies G sont maintenus. La note source de l'article 2 de l'arrêté du 31 mai 2021 (NOR : CCPE2112747A) fixe l'application aux opérations dont le fait générateur de TVA intervient à compter du 1er juillet 2021. Le corpus signale les deux articles de renvoi en état ABROGE_DIFF ; leur coordination future doit être vérifiée sans inventer de référence de remplacement.")

add('50 sexies K', '''
<p>L'assujetti ou l'intermédiaire mentionné au II de l'article 298 sexdecies H du code général des impôts fournit, au titre de ce même II, les informations suivantes le concernant :<br/><br/>
a) La raison sociale ;<br/><br/>
b) L'adresse physique et, si elle est différente, l'adresse postale ;<br/><br/>
c) La ou les adresses électroniques ainsi que, sauf pour les intermédiaires, le site internet ;<br/><br/>
d) Le nom de la personne physique à contacter dans l'entreprise ;<br/><br/>
e) Le numéro de téléphone et l'adresse électronique de cette personne ;<br/><br/>
f) La description de l'activité, sauf pour les intermédiaires ;<br/><br/>
g) Le numéro individuel d'identification à la taxe sur la valeur ajoutée mentionné à l'article 286 ter du code général des impôts ou, à défaut de cette identification, le numéro fiscal national.<br/><br/>
Pour chaque assujetti qu'il représente, l'intermédiaire doit également transmettre le numéro individuel d'identification de taxe sur la valeur ajoutée mentionné au 3 du III du même article 298 sexdecies H. Il doit le faire avant que l'assujetti commence à bénéficier du régime particulier.</p>
''',
    "Réécriture à droit constant : le fournisseur des informations et leur objet sont placés en tête de l'article. Les exceptions propres aux intermédiaires et l'antériorité de la transmission pour chaque assujetti représenté sont énoncées clairement. Aucune réforme de fond n'est introduite.",
    "Les lettres a à g et les séparations par sauts de ligne sont conservées. L'exception des intermédiaires au c) concerne seulement le site internet, et celle du f) la description d'activité. Le numéro de l'article 286 ter et celui du 3 du III de l'article 298 sexdecies H restent distincts. La note de l'article 2 de l'arrêté du 31 mai 2021 (NOR : CCPE2112747A) vise les opérations dont le fait générateur de TVA intervient à compter du 1er juillet 2021. Les deux articles de renvoi sont signalés ABROGE_DIFF dans le corpus ; coordination future à vérifier.")

add('50 sexies L', '''
<p>1. L'administration des douanes réalise l'audit dans les locaux du demandeur, à partir des grilles d'audit définies au 3 du présent article.<br/><br/>
2. Lorsque tout ou partie de ses locaux se trouve hors du territoire français, le demandeur doit prouver, par tout moyen, que les conditions figurant dans les grilles d'audit sont remplies.<br/><br/>
3. Les grilles d'audit mentionnées à l'article 202 G de l'annexe II au code général des impôts figurent en annexe à l'arrêté du 18 janvier 2021 pris pour l'application de l'article 202 G de l'annexe II au code général des impôts relatif aux grilles d'audit pour l'agrément d'opérateur de détaxe. Elles permettent à l'administration des douanes de vérifier le respect des critères requis pour devenir opérateur de détaxe et de prendre sa décision d'agrément.</p>
''',
    "Réécriture à droit constant : l'administration chargée de l'audit et le demandeur tenu de prouver la conformité de ses locaux étrangers sont explicitement désignés. Le support des grilles et leur fonction dans l'agrément sont distingués. Aucune réforme de fond n'est appliquée.",
    "Les subdivisions 1 à 3, le contrôle dans les locaux et la preuve par tout moyen sont conservés. Le renvoi à l'article 202 G de l'annexe II a été vérifié dans le corpus public : il prévoit l'audit sur grilles publiées par arrêté. La note source mentionne les modifications consécutives à l'article 1er de l'arrêté du 18 janvier 2021 (JO du 28 février) ; elle ne fournit aucune date de réforme nouvelle.")

add('50 sexies M', '''
<p>Au titre du III de l'article 298 sexdecies J, les informations requises sont les suivantes :<br/><br/>
a) La raison sociale du propriétaire du bien ;<br/><br/>
b) L'adresse physique du propriétaire du bien et, si elle est différente, son adresse postale ;<br/><br/>
c) Le numéro d'identification fiscal national du propriétaire du bien ;<br/><br/>
d) Le numéro de taxe sur la valeur ajoutée intracommunautaire du propriétaire du bien ou celui de son représentant fiscal au sein de l'Union européenne ;<br/><br/>
e) La date à laquelle le propriétaire du bien a été informé de ses obligations en matière de taxe sur la valeur ajoutée ;<br/><br/>
f) L'identifiant douanier EORI du propriétaire du bien ou de l'opérateur économique qui a accompli les formalités douanières d'importation ;<br/><br/>
g) Le numéro de référence porté sur la déclaration en douane d'importation du bien ;<br/><br/>
h) L'État ou le territoire de provenance du bien ;<br/><br/>
i) La nature et la quantité numéraire du bien ;<br/><br/>
j) La durée de détention du bien ;<br/><br/>
k) Le lieu et la date de livraison du bien.</p>
''',
    "Réécriture à droit constant : la liste des renseignements est introduite directement ; les adresses, l'opérateur ayant accompli les formalités et les données de livraison sont formulés plus lisiblement. Les onze rubriques et les alternatives d'identification restent intégrales. Aucune réforme de fond n'est introduite.",
    "Les lettres a à k et leurs séparations sont conservées. L'expression source « quantité numéraire » au i) est inhabituelle ; elle est maintenue et son sens doit être contrôlé sans lui substituer une autre unité. Le III de l'article 298 sexdecies J, vérifié dans le corpus, habilite la fixation de ces informations par arrêté ; cet article est signalé ABROGE_DIFF et appelle une coordination de référence lors de sa recodification.")

add('50 septies', '''
<p>L'exonération de taxe sur la valeur ajoutée prévue au 2° du II de l'article 291 du code général des impôts pour les biens importés définitivement dans le cadre des franchises fiscales communautaires s'applique dans les cas et selon les modalités fixés aux articles 50 octies à 50 octies C.</p>
<p>Pour l'application de ces dispositions, les termes suivants sont définis comme suit :</p>
<p>1° Biens personnels :</p>
<p>Les biens affectés à l'usage personnel des intéressés ou aux besoins de leur foyer qui, par leur nature comme par leur quantité, ne révèlent pas de préoccupation d'ordre commercial et ne sont pas destinés à l'exercice d'une activité économique au sens de l'article 256 A du code général des impôts.</p>
<p>2° Résidence normale :</p>
<p>Le lieu où une personne demeure habituellement pendant au moins 185 jours par année civile en raison de ses attaches personnelles et professionnelles. Pour une personne sans attaches professionnelles, il s'agit du lieu où elle demeure habituellement pendant cette même durée en raison d'attaches personnelles révélant des liens étroits avec l'endroit où elle habite.</p>
<p>Toutefois, lorsqu'une personne a ses attaches professionnelles dans un lieu différent de celui de ses attaches personnelles et séjourne, de ce fait, alternativement dans des pays différents, sa résidence normale est située au lieu de ses attaches personnelles, à condition qu'elle y retourne régulièrement. Ce retour régulier n'est pas exigé si la personne séjourne sur le territoire de la Communauté pour y exécuter une mission d'une durée déterminée. La fréquentation d'une université ou d'une école n'entraîne pas le transfert de la résidence normale ;</p>
<p>3° Alcools et boissons alcooliques :</p>
<p>Les produits soumis aux droits d'accises mentionnés aux articles 402 bis, 403, 438 et au a du I de l'article 520 A du code général des impôts ;</p>
<p>4° Tabacs manufacturés :</p>
<p>L'ensemble des produits définis aux articles 275 A à 275 G de l'annexe II au code général des impôts.</p>
''',
    "Réécriture à droit constant : le champ des franchises et les définitions sont clarifiés, notamment la durée de résidence et la dérogation fondée sur les attaches personnelles. Les limites non commerciales et économiques ainsi que l'absence de transfert liée aux études sont conservées. Aucune réforme de fond de policy.json ne vise ces franchises.",
    "Les 1° à 4° et l'emplacement des alinéas sont maintenus. Le seuil de 185 jours par année civile et l'exception au retour régulier sont conservés. Les articles 402 bis, 403, 438 et 520 A du CGI et 275 A à 275 G de l'annexe II ne figurent pas dans les fichiers publics correspondants fournis pour contrôle : les définitions d'accises et de tabacs appellent une coordination vérifiée avec les textes qui les ont repris, sans renvoi de remplacement inventé. Les articles 291 et 256 A sont signalés ABROGE_DIFF dans le corpus avec fin de version au 1er janvier 2027. Les références communautaires historiques sont maintenues.")

add('50 octies', '\n'.join(
    (ROOT / 'fragments' / f'50-octies-{i:02}.xml').read_text().strip()
    for i in range(1, 4)
),
    "Réécriture intégrale à droit constant, rédigée en trois fragments assemblés : les conditions générales des franchises sont séparées des conditions particulières et les longues phrases des 8°, 10°, 15°, 26° et 33° sont clarifiées à l'intérieur de leurs alinéas. Toutes les catégories de biens, les montants, quantités, âges, alternatives, exclusions et réserves sont conservés. Les intitulés brefs déjà explicites demeurent sans substitution artificielle. Aucune réforme de fond de policy.json ne vise ces franchises de TVA.",
    "Les 1° à 33°, le 10° bis, les 1 à 4 du 10°, les lettres et chaque alinéa sont maintenus. La source ne comporte pas de tableau. Sont notamment conservés les seuils de 22 € et 45 €, les plafonds voyageurs de 430/300/150 €, les plafonds frontaliers de 75/40 €, toutes les quantités de tabac, d'alcool et de carburant, les 6 mois pour les chevaux et les plafonds de 13 000/6 000 €. Au 6°, l'alternative source entre valeur globale et limites quantitatives est conservée ; son articulation avec les textes européens est à contrôler. Au 10°, 4, la source exclut les moins de 17 ans des franchises a, b et c, ce qui inclut la franchise générale a malgré les montants prévus pour les moins de 15 ans, mais ne mentionne pas le d relatif au vin et à la bière : cette incohérence de renvoi est conservée et signalée. Le seuil d'alcool éthylique est strictement supérieur à 80 % au 6° et de 80 % ou plus au 10° : distinction maintenue. Les références au règlement n° 918/83, à sa modification n° 274/2008 et à l'arrêté du 16 septembre 2004 sont anciennes et demandent un contrôle de concordance avec les textes européens applicables, sans remplacement conjectural. Le corpus signale plusieurs articles du CGI cités en état ABROGE_DIFF, dont 273, 261 E, 291, 292 et 293 avec fin de version au 1er janvier 2027 ; coordonner les références lors de la recodification. La note source de l'article 2 de l'arrêté du 31 mai 2021 (NOR : CCPE2112752A) fixe l'application aux opérations dont l'exigibilité de TVA intervient à compter du 1er juillet 2021, et non d'après le fait générateur. Cette portée historique est maintenue.")

add('50 octies A', '''
<p>I. – Les biens spécialement conçus pour l'éducation, l'emploi ou la promotion sociale des aveugles et des autres personnes physiquement ou mentalement handicapées sont également exonérés, à condition de remplir cumulativement les conditions suivantes :</p>
<p>1° Être importés par des institutions ou organisations dont l'activité principale est l'éducation des personnes handicapées ou l'assistance à ces personnes et qui sont agréées par l'administration des douanes et droits indirects pour recevoir ces objets en exonération ; et</p>
<p>2° Être adressés à une telle institution ou organisation à titre gratuit et sans aucune intention d'ordre commercial de la part du donateur.</p>
<p>II. – L'exonération s'applique aussi aux pièces de rechange, éléments ou accessoires spécifiques adaptés aux objets concernés, ainsi qu'aux outils destinés à leur entretien, à leur contrôle, à leur calibrage ou à leur réparation. Ces pièces, éléments, accessoires ou outils doivent être importés en même temps que les objets. Une importation ultérieure ouvre également droit à l'exonération s'ils sont reconnaissables comme destinés à des objets précédemment admis en exonération ou qui seraient susceptibles d'en bénéficier au moment où l'exonération est demandée pour ces pièces, éléments, accessoires spécifiques ou outils.</p>
<p>III. – Les biens admis en exonération doivent être utilisés exclusivement pour l'éducation, l'emploi ou la promotion sociale des aveugles et des autres personnes handicapées.</p>
<p>IV. – Les articles 77 et 78 du règlement (CEE) n° 918/83 du 28 mars 1983, modifié par le règlement (CE) n° 274/2008 du Conseil du 17 mars 2008 et mentionné à l'article 50 octies, s'appliquent en matière de taxe sur la valeur ajoutée aux biens exonérés au titre du présent article.</p>
''',
    "Réécriture à droit constant : le cumul des conditions de destinataire, d'agrément, de gratuité et d'absence d'intention commerciale est explicité. La phrase relative aux pièces et outils distingue l'importation simultanée de l'importation ultérieure, sans changer les objets éligibles. Aucune réforme de fond n'est appliquée.",
    "Les I à IV et les 1° et 2° sont maintenus. L'importation ultérieure reste admise pour des objets antérieurement exonérés ou susceptibles de l'être au moment de la demande concernant les pièces et outils. L'usage exclusif et les renvois aux articles 77 et 78 du règlement n° 918/83, modifié par le règlement n° 274/2008, sont conservés. Contrôler la concordance de ces références européennes anciennes avec les textes applicables, en coordination avec l'article 50 octies.")

add('50 octies B', '''
<p>Lorsque l'exonération est subordonnée au respect de limites ou de conditions, l'intéressé doit prouver à l'administration des douanes et droits indirects, à la satisfaction de celle-ci, que ces limites ou conditions ont été respectées.</p>
''',
    "Réécriture à droit constant : l'intéressé est directement désigné comme responsable de la preuve et le contrôle de l'administration est maintenu. La règle continue de couvrir tous les cas d'exonération soumis à des limites ou conditions. Aucune réforme de fond n'est introduite.",
    "La charge de la preuve et l'exigence de satisfaction de l'administration des douanes et droits indirects sont conservées. Aucun mode de preuve exclusif, délai ou critère supplémentaire n'est créé.")

add('50 octies C', '''
<p>Les dispositions qui précèdent ne remettent pas en cause les exonérations, privilèges et immunités que la France accorde à l'importation dans le cadre des accords internationaux mentionnés à l'article 143, sous f à i), de la directive (CE) n° 2006/112 du 28 novembre 2006 du Conseil des communautés européennes et à l'article 91 de la directive (CEE) n° 83/181 modifiée du Conseil du 28 mars 1983.</p>
''',
    "Réécriture à droit constant : la clause de sauvegarde est exprimée directement et les avantages maintenus sont rattachés à la France et aux accords internationaux visés. Les deux références européennes sont conservées intégralement. Aucune réforme de fond n'est appliquée.",
    "Le champ reste celui des exonérations, privilèges et immunités accordés à l'importation dans les accords mentionnés. Les renvois à l'article 143, sous f à i), de la directive n° 2006/112 du 28 novembre 2006 et à l'article 91 de la directive n° 83/181 modifiée du 28 mars 1983 sont conservés. Contrôler la concordance de la seconde référence ancienne et la dénomination historique de l'auteur de la première directive ; aucun texte de remplacement n'est présumé.")

add('50 decies', '''
<p>1. Sous réserve des dispositions du 2, les œuvres d'art originales, timbres, objets de collection ou d'antiquité repris aux numéros 97-04, 97-05 et 97-06 du tarif des droits de douane d'importation sont exonérés de taxe sur la valeur ajoutée lorsqu'ils sont destinés :</p>
<p>1° À l'Établissement public de la Réunion des musées nationaux et du Grand Palais des Champs-Élysées ;</p>
<p>2° Aux musées de l'État, des départements et des communes ;</p>
<p>3° Aux fondations, associations et autres établissements qui justifient de leur agrément par le ministre chargé des affaires culturelles.</p>
<p>2. Pour bénéficier de l'exonération, une attestation signée par le directeur de l'établissement doit être produite à l'appui de la déclaration d'importation. Elle doit certifier que les objets importés sont destinés à cet établissement et comporter les engagements suivants :</p>
<p>1° Ne céder ces objets, à titre onéreux ou gratuit, qu'après avoir acquitté la taxe sur la valeur ajoutée auprès du service des douanes ;</p>
<p>2° Présenter au bureau des douanes d'importation, dans un délai de trente jours, un certificat de prise en charge des objets dans l'inventaire de l'établissement destinataire.</p>
<p>3. La taxe sur la valeur ajoutée n'est toutefois pas due lorsque la cession est faite au bénéfice de l'un des établissements mentionnés au 1.</p>
''',
    "Réécriture à droit constant : le bénéfice de l'exonération est présenté avec ses destinataires, puis les pièces et engagements nécessaires. Les conditions de cession distinguent le paiement préalable et l'exception en faveur d'un établissement éligible. Aucune réforme de fond n'est introduite.",
    "Les subdivisions 1 à 3 et leurs 1° à 3° ou 1° et 2° sont maintenues. Les positions tarifaires 97-04, 97-05 et 97-06, le délai de trente jours, la signature du directeur et le certificat d'inventaire sont conservés. La réserve du 3 demeure applicable aux cessions à titre onéreux ou gratuit. La note historique vise le décret n° 2011-52 du 13 janvier 2011, articles 1er et 27. La nomenclature tarifaire et la dénomination de l'établissement doivent être contrôlées dans les textes de coordination applicables, sans modification silencieuse.")


def write_answer():
    assert len(sources) == len(drafts) == 21
    assert {a['number'] for a in sources} == set(drafts)
    result = []
    for source in sources:
        record = {key: source[key] for key in
                  ('code_id', 'source_id', 'source_sha256', 'number')}
        record.update(drafts[source['number']])
        result.append(record)
    (ROOT / 'answer.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    write_answer()
