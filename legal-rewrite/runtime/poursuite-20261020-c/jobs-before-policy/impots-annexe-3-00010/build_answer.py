import json
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
by_number = {a['number']: a for a in sources}
drafts = {}


def add(number, xml, reason, notes):
    a = by_number[number]
    drafts[number] = {
        'code_id': a['code_id'],
        'source_id': a['source_id'],
        'source_sha256': a['source_sha256'],
        'number': a['number'],
        'proposed_xml': xml.strip(),
        'reason': reason,
        'review_notes': notes,
        'status': 'rewrite_draft',
    }


add('41 tervicies C', '''
<p>Les moins-values mentionnées aux premier et dernier alinéas du 4 bis du VIII de l'article 167 bis du code général des impôts, imputables dans les conditions prévues à ce même 4 bis, sont suivies sur le formulaire mentionné au premier alinéa du 3 du IX de cet article. Le cas échéant, elles sont également suivies sur le formulaire mentionné au 2 du même IX.</p>
''',
    "Réécriture à droit constant : deux phrases distinguent le formulaire de suivi principal du formulaire éventuellement requis, dans le même alinéa. L'imputabilité reste rattachée au 4 bis. Les deux supports et le caractère éventuel du second sont conservés. Aucune réforme de fond du projet ne concerne cette formalité.",
    "Conserver ensemble les renvois aux premier et dernier alinéas du 4 bis du VIII, au premier alinéa du 3 du IX et au 2 du IX de l'article 167 bis. Le suivi ne crée aucune nouvelle possibilité d'imputation ; l'alinéa unique est maintenu.")

add('41 tervicies D', '''
<p>Le contribuable qui demande à exercer l'option prévue à l'avant-dernier alinéa du VIII bis de l'article 167 bis du code général des impôts utilise le formulaire prévu au premier alinéa du 3 du IX du même article. Il dépose ce formulaire l'année suivant celle au cours de laquelle survient le premier des événements prévus au VII de cet article.</p>
''',
    "Réécriture à droit constant : le contribuable est expressément chargé du dépôt et le point de départ de l'année de dépôt est formulé sans la tournure « premier de l'un ». L'option, le formulaire et le fait déclencheur restent identiques ; aucune réforme de fond n'est appliquée.",
    "Le dépôt reste exigé l'année suivant le premier événement du VII de l'article 167 bis, et non après chacun des événements. Le renvoi à l'avant-dernier alinéa du VIII bis est maintenu, ainsi que l'alinéa unique.")

add('41 tervicies E', '''
<p>Pour l'application des 2 et 3 du IX de l'article 167 bis du code général des impôts, le contribuable dépose le formulaire mentionné au premier alinéa du 3 du même IX, dûment renseigné, auprès du service des impôts des particuliers non résidents. Il le joint à la déclaration prévue au 1 de l'article 170 du même code et respecte le délai prévu à l'article 175 de ce code.<br/><br/>Le contribuable informe le service des impôts des particuliers non résidents des transferts de domicile fiscal intervenus après le transfert de son domicile fiscal hors de France, dans les conditions prévues au 5 du IX de l'article 167 bis précité.<br/><br/>Pour l'application du 4 du IX de l'article 167 bis précité, l'impôt en sursis de paiement redevient exigible si le contribuable n'a pas satisfait à ses obligations déclaratives dans les trente jours suivant la notification d'une mise en demeure adressée à lui-même ou, le cas échéant, à son représentant fiscal.</p>
''',
    "Réécriture à droit constant : les obligations de dépôt, d'information et de régularisation ont un sujet explicite. Les phrases séparent le destinataire, la déclaration jointe et le délai, sans modifier les trois alinéas utiles ni les conditions de rétablissement de l'exigibilité. Aucune réforme de fond n'est apportée.",
    "Le premier alinéa reste à la même place pour les renvois des articles 41 tervicies I, J et K. Maintien du service des particuliers non résidents, des articles 170, 1, et 175, du délai de trente jours après notification et de la possibilité de notifier au représentant fiscal. Le saut de ligne isolé après le texte source est purement typographique.")

add('41 tervicies F', '''
<p>Pour l'application du 5 du VIII de l'article 167 bis du code général des impôts, l'impôt acquitté hors de France est imputable dans les conditions prévues à ce même 5 si les deux conditions suivantes sont réunies :<br/><br/>a) Cet impôt est un impôt personnel sur le revenu assis sur les plus-values de cession de valeurs mobilières ou de droits sociaux ;<br/><br/>b) L'impôt mentionné au a est calculé à partir du prix ou de la valeur d'acquisition des titres concernés retenu pour l'application du premier alinéa du 2 du I de l'article 167 bis précité.<br/><br/>Le contribuable doit justifier du paiement effectif de cet impôt. Celui-ci est converti en euros au taux de change en vigueur à la date de ce paiement.</p>
''',
    "Réécriture à droit constant : le cumul des conditions a et b est annoncé explicitement. La preuve du paiement et la conversion monétaire sont exprimées dans deux phrases successives du même alinéa. Aucun élargissement du crédit d'impôt ni aucune réforme de fond n'est introduit.",
    "Maintien de l'assiette étrangère sur les seules plus-values de cession visées, du prix ou de la valeur d'acquisition retenu au premier alinéa du 2 du I de l'article 167 bis et du taux de change à la date du paiement effectif. Les lettres a et b et l'ordre des alinéas sont conservés.")

add('41 tervicies G', '''
<p>Lorsque les droits sociaux, valeurs, titres ou droits sur lesquels une plus-value latente a été constatée lors du transfert du domicile fiscal hors de France font l'objet d'un échange ou d'un apport relevant de l'article 150-0 B ou de l'article 150-0 B ter du code général des impôts, le contribuable renseigne le formulaire prévu au premier alinéa du 3 du IX de l'article 167 bis du même code. Sur ce formulaire, déposé l'année suivant celle de l'opération, il indique l'article du code général des impôts dont celle-ci relève, sa nature et sa date, le nombre de titres remis et de titres reçus et, le cas échéant, le montant de la soulte reçue.</p>
''',
    "Réécriture à droit constant : la condition tenant aux titres et aux opérations est conservée, puis les renseignements dus sont regroupés dans une seconde phrase. Le formulaire, l'année de dépôt et la soulte éventuelle sont maintenus. Aucune réforme de fond ne modifie ces opérations.",
    "Maintien de toutes les catégories de droits et titres, de la plus-value latente constatée au départ, des deux régimes 150-0 B et 150-0 B ter et du renvoi au premier alinéa du 3 du IX de l'article 167 bis. L'année de dépôt suit la réalisation de l'échange ou de l'apport ; l'alinéa unique est conservé.")

add('41 tervicies H', '''
<p>Lorsqu'il paie l'impôt définitif, le contribuable fournit une copie des avis d'imposition établis en application de l'article 41 tervicies B. Il joint cette copie aux documents mentionnés au premier alinéa du 3 du IX de l'article 167 bis du code général des impôts.</p>
''',
    "Réécriture à droit constant de l'alinéa unique : deux phrases identifient la copie à fournir lors du paiement, puis les documents auxquels elle doit être jointe. L'obligation et son moment demeurent identiques. Aucune réforme de fond n'est applicable.",
    "Le corpus public de l'article 41 tervicies B prévoit bien une mise en recouvrement spécifique des impositions en sursis. Maintien du renvoi au premier alinéa du 3 du IX de l'article 167 bis et de l'exigence de copie lors du paiement définitif.")

add('41 tervicies I', '''
<p>Pour l'application du deuxième alinéa du 3 du IX de l'article 167 bis du code général des impôts, le contribuable demande la restitution de l'impôt déjà acquitté au moyen du formulaire prévu au premier alinéa du 3 du IX du même article. Il dépose ce formulaire l'année suivant celle de l'événement qui ouvre droit à restitution, selon les modalités prévues au premier alinéa de l'article 41 tervicies E.<br/><br/>Il précise la nature et la date de l'événement à l'origine de sa demande. Il joint au formulaire les éléments de calcul et les justificatifs correspondant au montant de la restitution demandée.</p>
''',
    "Réécriture à droit constant : le dépôt du formulaire est formulé comme une obligation distincte dans la première partie, et le contenu de la demande est rendu plus lisible dans la seconde. Le champ de la restitution et son calendrier restent inchangés ; aucune réforme de fond n'est appliquée.",
    "Conserver la distinction entre le deuxième alinéa du 3 du IX, qui fonde cette demande, et le premier alinéa du même 3, qui désigne le formulaire. La proposition conserve les deux alinéas utiles et le renvoi au premier alinéa de l'article 41 tervicies E ; le saut de ligne final sans texte est supprimé.")

add('41 tervicies J', '''
<p>Pour l'application du dernier alinéa du 3 du IX de l'article 167 bis du code général des impôts, le contribuable demande le dégrèvement de l'impôt en sursis de paiement ou la restitution de l'impôt acquitté au moyen du formulaire prévu au premier alinéa du 3 du IX du même article. Il dépose ce formulaire l'année suivant celle de l'événement qui ouvre droit au dégrèvement ou à la restitution, selon les modalités prévues au premier alinéa de l'article 41 tervicies E.<br/><br/>Il précise la nature et la date de l'événement à l'origine de sa demande. Il joint au formulaire les éléments de calcul et les justificatifs correspondant au montant du dégrèvement ou de la restitution demandé.</p>
''',
    "Réécriture à droit constant : le contribuable est explicitement chargé du dépôt ; la demande, le calendrier et les pièces sont exprimés dans des phrases plus courtes. Les deux voies, dégrèvement et restitution, demeurent distinctes. Aucune réforme de fond n'est introduite.",
    "Maintien du dernier alinéa du 3 du IX de l'article 167 bis comme fondement, du premier alinéa du même 3 pour le formulaire et du premier alinéa de l'article 41 tervicies E pour les modalités. Les justificatifs couvrent chacune des deux voies ; les deux alinéas utiles restent en place.")

add('41 tervicies K', '''
<p>Dans les cas prévus au VIII de l'article 167 bis du code général des impôts, le contribuable demande le dégrèvement de l'impôt en sursis de paiement au moyen du formulaire prévu au premier alinéa du 3 du IX du même article. Il dépose ce formulaire l'année suivant celle de l'événement qui ouvre droit au dégrèvement, selon les modalités prévues au premier alinéa de l'article 41 tervicies E.<br/><br/>Il précise la nature et la date de l'événement à l'origine de sa demande. Il joint au formulaire les éléments de calcul et les justificatifs correspondant au montant du dégrèvement demandé.</p>
''',
    "Réécriture à droit constant : les phrases distinguent la demande, le dépôt et les pièces, dans les deux alinéas existants. Le champ reste celui du seul dégrèvement prévu au VIII de l'article 167 bis ; aucune réforme de fond n'est apportée.",
    "Ne pas confondre ce dégrèvement avec les restitutions des articles 41 tervicies I et J. Maintien de l'année suivant l'événement, du formulaire prévu au premier alinéa du 3 du IX et des modalités du premier alinéa de l'article 41 tervicies E.")

add('41 tervicies L', '''
<p>Dans les cas prévus au 3 du IX de l'article 167 bis du code général des impôts, les garanties constituées en application du quatrième alinéa du V de cet article sont levées à concurrence de l'impôt acquitté ou du montant d'impôt dégrevé.<br/><br/>Dans les cas de dégrèvement prévus au VIII et au dernier alinéa du 3 du IX de l'article 167 bis précité, le contribuable obtient le remboursement des frais qu'il a supportés pour constituer les garanties. Ce remboursement intervient dans les conditions prévues aux articles R. * 208-3 à R. * 208-6 du livre des procédures fiscales, à concurrence du montant d'impôt dégrevé.</p>
''',
    "Réécriture à droit constant : la levée partielle des garanties est exprimée directement ; le second alinéa identifie le bénéficiaire du remboursement puis ses conditions et sa limite. Les hypothèses de paiement et de dégrèvement ne sont pas fusionnées. Aucune réforme de fond n'est introduite.",
    "La levée des garanties couvre l'impôt acquitté ou dégrevé ; le remboursement des frais reste limité aux cas de dégrèvement visés et à leur montant. Maintien du quatrième alinéa du V de l'article 167 bis et de la plage R. * 208-3 à R. * 208-6 du LPF, avec les deux alinéas utiles.")

add('41 quatervicies', '''
<p>1. Le contribuable qui réalise une opération relevant du régime de report d'imposition prévu à l'article 150-0 B ter du code général des impôts indique distinctement, sur la déclaration spéciale des plus-values prévue à l'article 74-0 F de l'annexe 2 au présent code, le montant de la plus-value réalisée lors de cette opération et les éléments nécessaires à son calcul.</p>
<p>Il indique également les informations suivantes :</p>
<p>a) La date de l'opération d'apport ;</p>
<p>b) La dénomination et l'adresse du siège social ou du principal établissement de la société bénéficiaire de l'apport ainsi que, le cas échéant, de la société ou du groupement interposé ayant réalisé l'apport de titres ;</p>
<p>c) La nature juridique des droits apportés ;</p>
<p>d) Le nombre de titres apportés et leur valeur réelle unitaire à la date de l'apport ;</p>
<p>e) Le nombre de titres reçus, leur valeur nominale et leur valeur réelle unitaire à la date de l'apport ;</p>
<p>f) La valeur globale des titres apportés à la date de l'apport ;</p>
<p>g) La valeur unitaire d'acquisition et la valeur globale d'acquisition des titres apportés ;</p>
<p>h) Le cas échéant, le montant de la soulte reçue immédiatement imposable ou de la soulte versée, ainsi que le montant de la plus-value d'apport dont l'imposition est reportée.</p>
<p>2. Dans un délai de trente jours à compter de la demande de l'administration, le contribuable fournit une attestation que la société bénéficiaire de l'apport a émise lors de celui-ci. Cette attestation précise que la société est informée que les titres apportés sont grevés d'une plus-value en report d'imposition en application de l'article 150-0 B ter précité.</p>
''',
    "Réécriture à droit constant : l'obligation déclarative principale et la production de l'attestation sont formulées plus directement. Les valeurs demandées sont désignées sans répétition inutile et l'attestation fait l'objet de deux phrases. Le 1, ses lettres a à h et le 2 sont conservés, sans réforme de fond.",
    "Maintien des onze alinéas, du délai de trente jours à compter de la demande, de l'émission de l'attestation lors de l'apport et des valeurs à la date de l'apport. Ne pas confondre la soulte reçue immédiatement imposable, la soulte versée et la plus-value reportée. Le renvoi à l'annexe 2 correspond à l'annexe II mentionnée dans les articles voisins.")

add('41 quatervicies A', '''
<p>1. Si, dans les trois années suivant la date de l'apport, délai calculé de date à date, les titres apportés sont affectés par l'un des événements mentionnés à la première phrase du 2° du I de l'article 150-0 B ter du code général des impôts, la société bénéficiaire de l'apport joint une attestation à sa déclaration de résultat de l'exercice au cours duquel cet événement survient. Elle y indique les informations suivantes :</p>
<p>a) La nature et la date de l'événement ayant affecté les titres apportés ;</p>
<p>b) Le nombre de titres affectés par cet événement et, le cas échéant, leur prix de cession à la date de l'événement ;</p>
<p>c) Le cas échéant, l'engagement de réinvestir le produit de la cession des titres concernés dans les conditions prévues au 2° du I de l'article 150-0 B ter précité, au plus tard à l'expiration d'un délai de trois ans à compter de la date de cession ou, le cas échéant, de la date de perception d'un complément de prix afférent à cette cession.</p>
<p>2. a) La société qui respecte son engagement de réinvestir le produit de la cession dans les conditions prévues au 2° du I de l'article 150-0 B ter précité joint à sa déclaration de résultat de chaque exercice au cours duquel elle effectue un réinvestissement une attestation précisant les informations suivantes :</p>
<p>1° Le montant réinvesti du produit de cession ou du complément de prix ;</p>
<p>2° La nature et la date du réinvestissement ;</p>
<p>3° Le cas échéant, la dénomination, la catégorie, la forme et l'adresse du siège de la société, du fonds ou de l'organisme bénéficiaire du réinvestissement.</p>
<p>b) Lorsque la société réinvestit le produit de la cession des titres en application du d du 2° du I de l'article 150-0 B ter du code général des impôts :</p>
<p>1° La société mentionnée au premier alinéa du a informe le fonds, la société ou l'organisme émetteur des parts ou actions souscrites que la souscription constitue un réinvestissement effectué en application de cette disposition ;</p>
<p>2° Elle joint, le cas échéant, à sa déclaration de résultat de chaque exercice au cours duquel elle a signé un bulletin de souscription en application des deuxième et troisième phrases du d du 2° du I de l'article 150-0 B ter précité, une copie de ce bulletin.</p>
<p>3. a) La société qui a respecté l'engagement de réinvestissement dans les conditions prévues au 2° du I de l'article 150-0 B ter du code général des impôts joint à sa déclaration de résultat de l'exercice au cours duquel expire le délai de conservation prévu au onzième alinéa du même 2° une attestation du fonds, de la société ou de l'organisme bénéficiaire du réinvestissement. Cette attestation certifie le respect de l'obligation de conservation des biens ou titres acquis ou souscrits.</p>
<p>b) La société qui a respecté l'engagement de réinvestissement dans les conditions prévues au d du 2° du I de l'article 150-0 B ter du code général des impôts joint à sa déclaration de résultat de l'exercice au cours duquel expire le délai de cinq ans prévu au même d une attestation indiquant les sommes effectivement versées au fonds, à la société ou à l'organisme bénéficiaire du réinvestissement.</p>
<p>4. La société joint une attestation à sa déclaration de résultat lorsqu'elle ne prend pas l'engagement mentionné au c du 1 ou lorsque le réinvestissement effectué ne remplit pas les conditions prévues au 2° du I de l'article 150-0 B ter précité. Elle joint cette attestation à la déclaration de l'exercice de cession des titres apportés si elle n'a pas pris l'engagement de réinvestissement, ou à celle de l'exercice au cours duquel une condition de réinvestissement n'est pas respectée. L'attestation précise que le produit de la cession des titres apportés n'est pas réinvesti conformément au 2° du I de l'article 150-0 B ter précité.</p>
<p>5. La société concernée transmet une copie des attestations mentionnées aux 1 à 4 au contribuable ayant réalisé l'apport des titres grevés d'une plus-value en report d'imposition ou, le cas échéant, au donataire de ces titres.</p>
''',
    "Réécriture à droit constant : chaque obligation d'attestation identifie la société tenue de l'accomplir et l'exercice de rattachement. Le 4 est décomposé en phrases pour distinguer absence d'engagement et manquement au réinvestissement. Les subdivisions, informations et transmissions sont intégralement maintenues. Aucune réforme de fond du projet n'est appliquée au régime d'apport-cession.",
    "Maintien des quinze alinéas et du premier alinéa du a du 2, visé par l'article 41 sexvicies. Le délai de trois ans pour réinvestir et le délai de cinq ans du d sont ceux de la source ; le renvoi au onzième alinéa du 2° correspond à la conservation dans le corpus de l'article 150-0 B ter. La note source rattache les modifications aux articles 106 de la loi 2019-1479 du 28 décembre 2019, 24-I-2° de la loi 2023-1322 du 29 décembre 2023 et 11-I A 1° a et 6° de la loi 2026-103 du 19 février 2026. Ces références historiques ne fixent aucune entrée en vigueur du projet ; les règles temporelles propres aux opérations antérieures restent à contrôler dans ces lois, sans extension automatique des paramètres actuels.")

add('41 quinvicies', '''
<p>1. Pour l'application du II de l'article 150-0 B ter du code général des impôts, le donateur transmet au donataire les éléments mentionnés à l'article 41 quatervicies qui permettent à ce dernier de déclarer la plus-value en report d'imposition afférente aux titres transmis.</p>
<p>Si la donation intervient dans les trois ans suivant la date de l'apport, délai calculé de date à date, le donateur communique à la société bénéficiaire de l'apport l'identité et l'adresse du donataire.</p>
<p>2. Sur le formulaire prévu à l'article 74-0 F de l'annexe II au présent code, souscrit au titre de l'année de la transmission, le donateur indique l'identité et l'adresse du donataire, la date de la transmission, le nombre de titres transmis et le montant de la plus-value en report d'imposition afférente à ces titres.</p>
<p>3. Sur le formulaire prévu à l'article 74-0 F de l'annexe II précité, souscrit au titre de l'année de la transmission, le donataire indique l'identité et l'adresse du donateur, le nombre de titres transmis, la date de la transmission, le montant de la plus-value en report d'imposition afférente à ces titres, la dénomination et l'adresse du siège social ou du principal établissement de la société dont les titres sont transmis, ainsi que les éléments mentionnés au premier alinéa du 1. Le cas échéant, il transmet à l'administration, à sa demande, l'attestation mentionnée au 2 de l'article 41 quatervicies.</p>
''',
    "Réécriture à droit constant : les obligations respectives du donateur et du donataire sont rendues plus directes ; le formulaire et l'année déclarative sont placés en tête des 2 et 3. La transmission d'informations, la condition de trois ans et l'attestation sur demande sont intégralement conservées, sans réforme de fond.",
    "Les quatre alinéas restent en place, notamment le premier alinéa du 1 visé au 3. Le délai de trois ans se calcule de date à date ; les formulaires sont souscrits au titre de l'année de transmission. Le donataire demeure tenu de déclarer tous les renseignements du 3, y compris la société concernée et les éléments reçus du donateur.")

add('41 sexvicies', '''
<p>1. La société de gestion d'un fonds commun de placement à risque ou d'un fonds professionnel de capital investissement, le gérant d'une société de libre partenariat ou la société de capital-risque mentionnés au d du 2° du I de l'article 150-0 B ter du code général des impôts souscrivent une déclaration détaillée permettant d'apprécier le quota d'investissement de 75 % prévu à ce même d. Cette déclaration est établie sur la base de l'inventaire semestriel au cours duquel expire le délai de cinq ans fixé au même d. Ils l'adressent au service des impôts auprès duquel ils souscrivent leur déclaration de résultats.</p>
<p>2. La déclaration prévue au 1 est adressée dans les quatre mois suivant la clôture de l'exercice comptable correspondant. Pour chaque investissement retenu dans le calcul du quota de 75 % prévu au d du 2° du I de l'article 150-0 B ter précité, elle indique les éléments suivants :</p>
<p>a) La dénomination de la société ou de l'entité, l'adresse de son siège social et, si elle est différente, celle de son siège de direction effective ;</p>
<p>b) L'activité principale de la société ;</p>
<p>c) La capitalisation boursière de la société, si ses titres sont admis à la négociation sur un marché d'instruments financiers d'un Etat partie à l'accord sur l'Espace économique européen dont le fonctionnement est assuré par une entreprise de marché ou un prestataire de services d'investissement ;</p>
<p>d) Pour les titres acquis dans les conditions prévues au d du 2° du I de l'article 150-0 B ter précité, les éléments permettant d'apprécier le respect de la condition de contrôle ou de détention d'une participation minimale dans la société émettrice des titres ;</p>
<p>e) En cas d'investissement dans des sociétés mentionnées au premier alinéa du 1° quater du II de l'article 163 quinquies B du code général des impôts ou dans des entités mentionnées au 1° quinquies du même II, les états mentionnés, respectivement, aux 1° et 2° du II de l'article 171 AW de l'annexe II au code général des impôts. Ces états font apparaître les éléments permettant d'apprécier le quota d'investissement mentionné au d du 2° du I de l'article 150-0 B ter.</p>
<p>3. Dans le même délai de quatre mois, le fonds, la société ou l'organisme émetteur des parts ou actions souscrites communique une attestation à la société mentionnée au premier alinéa du a du 2 de l'article 41 quatervicies A. Cette attestation indique si, à l'expiration du délai de cinq ans mentionné au d du 2° du I de l'article 150-0 B ter précité, le quota d'investissement de 75 % en titres éligibles prévu au même d est respecté, sur la base de l'inventaire semestriel au cours duquel ce délai expire. Elle indique également le pourcentage de l'actif du fonds, de la société ou de l'organisme constitué par ces titres.</p>
<p>4. La société mentionnée au premier alinéa du a du 2 de l'article 41 quatervicies A transmet une copie de l'attestation mentionnée au 3 au contribuable ayant réalisé l'apport des titres grevés d'une plus-value en report d'imposition ou, le cas échéant, au donataire de ces titres.</p>
''',
    "Réécriture à droit constant : la déclaration détaillée, sa base d'inventaire, son destinataire et l'attestation sont exposés en phrases plus courtes. Les informations par investissement et la chaîne de transmission de l'attestation demeurent complètes. La condition de participation est clarifiée comme une participation dans la société émettrice. Aucune réforme de fond du projet ne modifie le quota.",
    "Maintien des neuf alinéas, des lettres a à e, du quota de 75 %, du délai de cinq ans et des quatre mois suivant la clôture de l'exercice correspondant. Conserver la distinction entre gestionnaire déclarant au 1 et organisme émetteur de l'attestation au 3. Le renvoi au premier alinéa du a du 2 de l'article 41 quatervicies A reste opérant ; les états des 1° et 2° du II de l'article 171 AW restent respectivement rattachés aux sociétés et entités désignées au e. L'option historique de l'article 41 septvicies n'est pas supprimée.")

add('41 septvicies', '''
<p>I. - Les fonds, sociétés et organismes mentionnés au d du 2° du I de l'article 150-0 B ter du code général des impôts qui ont été constitués avant le 29 décembre 2023 peuvent opter pour le quota d'investissement prévu à ce même d dans sa rédaction issue du I de l'article 24 de la loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024.</p>
<p>Cette option est irrévocable. Elle est exercée par la société de gestion du fonds, le gérant ou la société de gestion de la société de libre partenariat, la société de capital-risque ou l'organisme lors du dépôt de la déclaration détaillée prévue au 1 de l'article 41 sexvicies au titre de l'expiration du délai de cinq ans suivant la signature de la première souscription réalisée, après la constitution du fonds, de la société ou de l'organisme, au titre du d du 2° du I de l'article 150-0 B ter du code général des impôts. L'auteur de l'option joint à cette déclaration une attestation mentionnant l'application des dispositions prévues par le d du 2° du même article 150-0 B ter dans sa rédaction issue du I de l'article 24 de la loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024.</p>
<p>II. - En l'absence d'option, le quota de 75 % prévu au d du 2° du I de l'article 150-0 B ter du code général des impôts dans sa rédaction antérieure à l'article 24 de la loi n° 2023-1322 du 29 décembre 2023 de finances pour 2024 est apprécié en retenant la valeur liquidative des titres éligibles au numérateur et la valeur liquidative du fonds, de la société ou de l'organisme au dénominateur.</p>
''',
    "Réécriture à droit constant : l'irrévocabilité, l'auteur de l'option, son échéance et sa forme sont répartis en phrases lisibles au sein du même alinéa. Le calcul sans option distingue clairement numérateur et dénominateur. Le régime historique et le choix offert aux véhicules anciens sont conservés ; aucune réforme de fond n'est introduite.",
    "Maintien des trois alinéas et des I et II, de la constitution avant le 29 décembre 2023, de l'option irrévocable, du délai de cinq ans après la première souscription postérieure à la constitution et du quota de 75 %. Les deux rédactions historiques de l'article 150-0 B ter restent distinctes. La formule source « d du 2° du même article » dans l'attestation omet de répéter le I : cette imprécision préexistante est conservée et signalée, le premier alinéa et le contexte identifiant le I.")

add('41 novovicies', '''
<p>I. - Pour l'application du IV de l'article 93 quater du code général des impôts, les nouveaux propriétaires formulent la demande de report d'imposition de la plus-value. Toutefois, si les immeubles appartiennent à une société mentionnée à l'article 8 du même code, la demande est formulée par les associés qui souhaitent bénéficier du report de la plus-value imposable à leur nom.</p>
<p>II. - Les nouveaux propriétaires ou, le cas échéant, les associés qui demandent le report indiquent sur la déclaration prévue à l'article 97 du code général des impôts le montant de la plus-value concernée. Ils joignent à cette déclaration :</p>
<p>a) Une note annexe précisant le nom ou la raison sociale et l'adresse des parties à l'acte, le lieu de situation de l'immeuble dont la propriété est transférée, la date du transfert et le montant de la plus-value dont le report d'imposition est demandé ;</p>
<p>b) Un extrait ou une copie de l'acte comportant la demande de report d'imposition de la plus-value.</p>
<p>III. - Lorsqu'un événement met fin au report d'imposition, la plus-value est mentionnée sur la déclaration prévue à l'article 170 du code général des impôts, souscrite au titre de l'année au cours de laquelle cet événement survient.</p>
''',
    "Réécriture à droit constant : le I distingue par deux phrases le propriétaire direct et les associés d'une société de l'article 8. Les pièces et l'année de déclaration à la fin du report sont formulées plus directement. Les subdivisions et l'intégralité des renseignements restent inchangées ; aucune réforme de fond n'est appliquée.",
    "Maintien des cinq alinéas, des I à III, des lettres a et b, et des articles 93 quater, IV, 8, 97 et 170. Pour une société de l'article 8, seuls les associés qui demandent le report de leur propre plus-value présentent la demande. L'extrait ou la copie de l'acte doit toujours contenir cette demande ; le saut de ligne final sans texte est supprimé.")

add('41-00 A', '''
<p>Les personnes morales ou groupements de droit ou de fait dont le chiffre d'affaires hors taxes ou le total de l'actif brut inscrit au bilan atteint au moins 400 millions d'euros à la clôture de l'exercice joignent à la déclaration prévue aux articles 172, 172 bis ou 223 du code général des impôts les listes suivantes :</p>
<p>1° La liste des personnes ou groupements de personnes de droit ou de fait détenant au moins 10 % de leur capital. Pour chaque détenteur, cette liste indique le nombre de parts ou d'actions et le taux de détention. Elle précise, pour les personnes morales, leur dénomination et leur adresse ainsi que, pour celles établies en France, leur numéro d'identification au répertoire national des établissements (numéro SIRET). Pour les personnes physiques, elle précise les nom, prénoms, adresse, date et lieu de naissance ;</p>
<p>2° La liste des personnes morales ou groupements de personnes de droit ou de fait qui détiennent indirectement, à la clôture de l'exercice, plus de la moitié de leur capital ou des droits de vote, ainsi que des personnes ou groupements interposés dans la chaîne des participations, quel que soit leur taux de détention. Cette liste indique leur dénomination, leur adresse, leur taux de détention et, pour ceux établis en France, leur numéro d'identification au répertoire national des établissements (numéro SIRET) ;</p>
<p>3° La liste des personnes morales ou groupements de personnes de droit ou de fait dont elles détiennent directement ou indirectement, à la clôture de l'exercice, plus de la moitié du capital ou des droits de vote, ainsi que des personnes ou groupements interposés dans la chaîne des participations, quel que soit leur taux de détention. Cette liste indique leur dénomination, leur adresse, leur taux de détention et, pour ceux établis en France, leur numéro d'identification au répertoire national des établissements (numéro SIRET) ;</p>
<p>4° (Périmé).</p>
''',
    "Réécriture à droit constant : le seuil de déclenchement est formulé directement et chaque liste sépare son périmètre des informations d'identification requises. Les participations amont et aval restent distinguées ; le 4° périmé est maintenu à sa place. Aucune réforme de fond ni dispense déclarative nouvelle n'est créée.",
    "Maintien des cinq alinéas, du seuil alternatif de 400 millions d'euros de chiffre d'affaires hors taxes ou d'actif brut, du seuil inclusif de 10 % au 1° et du seuil strict de plus de la moitié aux 2° et 3°. Les interposés sont déclarés quel que soit leur taux. La source associe l'intitulé « répertoire national des établissements » au SIRET : cette formulation est conservée sans correction silencieuse. La réutilisation administrative souhaitée par policy.json ne supprime pas à elle seule ces listes ni les protections attachées aux données ; une éventuelle dispense nécessiterait une coordination expresse des obligations des articles 172, 172 bis et 223.")

add('41-0 A', '''
<p>I. - Pour l'application du III de l'article 151 septies du code général des impôts, les travaux agricoles et forestiers sont ceux énumérés ci-dessous :</p>
<p>1° Travaux agricoles :</p>
<p>a) Labours, préparation et entretien des sols de cultures ;</p>
<p>b) Semis et plantations ;</p>
<p>c) Entretien et traitement des cultures et plantations ;</p>
<p>d) Récoltes.</p>
<p>2° Travaux forestiers :</p>
<p>a) Préparation et entretien des sols ;</p>
<p>b) Plantations et replantations ;</p>
<p>c) Exploitation des bois : abattage, ébranchage, élagage, éhouppage et travaux qui précèdent ou suivent normalement ces opérations, notamment le débroussaillement et le nettoyage des coupes ;</p>
<p>d) Travaux de façonnage, de conditionnement du bois, de sciage et de carbonisation, lorsqu'ils sont effectués sur le parterre de la coupe ;</p>
<p>e) Enlèvement jusqu'aux aires de chargement.</p>
<p>II. - 1° Les matériels agricoles ou forestiers au sens du III de l'article 151 septies du même code sont les biens d'équipement affectés exclusivement à la réalisation des travaux énumérés au I ;</p>
<p>2° Les entrepreneurs de travaux agricoles ou forestiers sont ceux qui réalisent à titre principal les travaux énumérés au I pour le compte de tiers exploitants agricoles ou forestiers. Cette activité doit procurer à l'entreprise plus de 50 % de ses recettes annuelles.</p>
<p>III. - Pour l'application du III de l'article 151 septies précité, les recettes prises en compte correspondent au montant total des recettes de l'entreprise.</p>
''',
    "Réécriture à droit constant : les définitions des matériels et des entrepreneurs sont exprimées directement, et la condition de lieu des travaux forestiers est rapprochée des opérations concernées. Les intitulés techniques utiles sont conservés. Les I à III, leurs numéros et lettres et la totalité des activités restent présents, sans réforme de fond.",
    "Maintien des quinze alinéas, de l'affectation exclusive des équipements, de l'exercice à titre principal pour des tiers exploitants et du seuil strict de plus de 50 % des recettes annuelles. La condition du parterre de la coupe ne s'applique qu'au d du 2° du I ; l'enlèvement reste limité aux aires de chargement. L'ensemble des recettes de l'entreprise reste retenu au III.")

add('41-00 A bis', '''
<p>I. - Pour calculer la taxe exceptionnelle prévue au 2 du V de l'article 151 septies A du code général des impôts, le tarif annexé au premier alinéa de l'article 719 du même code est appliqué au montant brut des indemnités compensatrices dues par les compagnies d'assurances en cas de cessation de mandat. Il s'agit des indemnités dues en vertu des statuts réglementant la profession d'agent général d'assurances, approuvés dans les conditions prévues à l'article L. 540-2 du code des assurances.</p>
<p>Si l'indemnité compensatrice est versée sous forme de rente, le tarif mentionné au premier alinéa est appliqué au capital représentatif de cette rente.</p>
<p>II. - Les crédits d'impôts et les prélèvements ou retenues non libératoires de l'impôt sur le revenu sont imputés sur la taxe exceptionnelle.</p>
<p>III. - Pour l'établissement de la taxe exceptionnelle, les agents généraux d'assurance indemnisés accomplissent, au titre de l'année au cours de laquelle l'indemnité est acquise, les obligations suivantes :</p>
<p>1° Indiquer le montant brut total des indemnités mentionnées au I sur la déclaration prévue à l'article 170 du code général des impôts ;</p>
<p>2° Joindre à la déclaration mentionnée à l'article 97 ou à l'article 170 du code général des impôts, déposée dans les conditions prévues à l'article 202 du même code, les pièces suivantes :</p>
<p>a. Un état établi sur papier libre indiquant le montant brut des indemnités compensatrices mentionnées au I, les noms et adresses des compagnies d'assurances qui les versent, la date de conclusion du ou des mandats d'agents d'assurances indemnisés et la date de cessation de ces mandats ;</p>
<p>b. Le document mentionné au IV. Si la compagnie d'assurances n'a pas pu l'établir au moment du dépôt de la déclaration prévue à l'article 97 ou à l'article 170 du code général des impôts, l'agent joint un engagement de le produire auprès du service des impôts dont il dépend ;</p>
<p>c. Le document attestant la date d'entrée en jouissance des droits acquis par l'agent indemnisé dans le régime de retraite de base auquel il est affilié. Si ce document n'a pas pu être établi au moment du dépôt de la déclaration prévue à l'article 97 ou à l'article 170 du code général des impôts, l'agent joint un engagement de le produire auprès du service des impôts dont il dépend.</p>
<p>IV. - Les compagnies d'assurances redevables de l'indemnité compensatrice établissent sur papier libre un document indiquant :</p>
<p>1° Le nom et l'adresse du nouvel agent qui poursuit l'activité de l'agent indemnisé ;</p>
<p>2° Le lieu où ce nouvel agent exerce son activité professionnelle ;</p>
<p>3° La date à laquelle le nouvel agent reprend l'activité.</p>
<p>La compagnie fournit ce document à l'agent général d'assurances indemnisé le mois suivant la reprise de l'activité par le nouvel agent.</p>
''',
    "Réécriture à droit constant : le calcul de la taxe distingue l'assiette brute de l'indemnité et le capital représentatif d'une rente. Les obligations documentaires séparent la pièce attendue de l'engagement admis lorsqu'elle n'a pas pu être établie. Les auteurs des obligations et le délai de transmission sont explicites. Aucune réforme de fond n'est appliquée à ce régime d'agents d'assurances.",
    "Maintien des quatorze alinéas, des I à IV, des 1° à 3° et des lettres a., b. et c. Le tarif de l'article 719 n'est pas remplacé par un taux inventé. L'année d'acquisition de l'indemnité reste distincte de celle d'un paiement éventuel. Le document est dû le mois suivant la reprise, sans transformation en délai de trente jours. Les engagements de produire ne sont admis que si les documents n'ont pas pu être établis lors du dépôt. Les dispositions de retraite du projet ne s'étendent pas automatiquement à cette indemnité ni à ce régime professionnel.")

add('41-0 A bis', '''
<p>I. - L'état à produire en application du sixième alinéa du II de l'article 151 octies du code général des impôts comporte les renseignements suivants :</p>
<p>a) Le nom de l'apporteur, son adresse à la date de production de l'état et l'adresse du siège de la direction de l'entreprise à laquelle les éléments d'actif apportés étaient affectés ou du lieu de son principal établissement ;</p>
<p>b) A la date de production de l'état, la forme, la dénomination sociale, le numéro SIRET et l'adresse du principal établissement ou du siège de la direction de la société bénéficiaire de l'apport ainsi que, si elle est différente, l'adresse de son siège social ;</p>
<p>c) La date de l'apport ;</p>
<p>d) Le nombre de titres reçus en rémunération de l'apport et leur valeur à cette date, correspondant à la valeur des apports ;</p>
<p>e) Pour chaque élément non amortissable apporté, les renseignements visés aux a, b et e du 1° du I de l'article 38 quindecies, le montant de la plus-value ou de la moins-value réalisée lors de l'apport et son régime fiscal à cette date ;</p>
<p>f) En cas de cession de tout ou partie des éléments non amortissables apportés, la nature du ou des biens cédés et la date de leur cession par la société bénéficiaire de l'apport ;</p>
<p>g) En cas de cession à titre onéreux, de rachat ou d'annulation de tout ou partie des droits sociaux reçus en rémunération de l'apport, la nature et la date de l'opération ainsi que le nombre de titres concernés ;</p>
<p>h) En cas de transmission à titre gratuit, les nom et adresse du ou des bénéficiaires ;</p>
<p>i) En cas de transformation de la société bénéficiaire de l'apport, la date de l'opération et la nouvelle forme adoptée par cette société.</p>
<p>II. - Le bénéficiaire de la transmission mentionné au premier alinéa du a du I de l'article 151 octies du code général des impôts qui prend l'engagement prévu à ce même a est également soumis aux obligations du I.</p>
''',
    "Réécriture à droit constant : la liste des renseignements est allégée et les dates auxquelles les identifications doivent être appréciées sont explicites. Le II désigne directement le bénéficiaire tenu de produire l'état. Toutes les opérations, valeurs et hypothèses des a à i sont maintenues ; aucune réforme de fond n'est introduite.",
    "Maintien des onze alinéas et des lettres a à i. Le sixième alinéa du II de l'article 151 octies du corpus prévoit l'état de suivi ; le premier alinéa du a du I prévoit l'engagement du bénéficiaire d'une transmission gratuite. Les adresses et données du b restent celles de la production de l'état, tandis que les valeurs du d et le régime fiscal du e restent ceux de l'apport. Conserver les renseignements des a, b et e du 1° du I de l'article 38 quindecies.")

add('41-0 A bis A', '''
<p>I. - L'état à produire en application du V de l'article 151 octies B du code général des impôts comporte les renseignements suivants :</p>
<p>a) Le nom et l'adresse de l'apporteur, ainsi que l'adresse du siège de la direction de l'entreprise apporteuse ou du lieu de son principal établissement ;</p>
<p>b) La forme, la dénomination sociale, le numéro SIRET et l'adresse du principal établissement ou du siège de la direction de la société bénéficiaire de l'apport ainsi que, si elle est différente, l'adresse de son siège social ;</p>
<p>c) La date de l'apport ;</p>
<p>d) Le nombre de titres apportés et leur prix de revient fiscal chez l'apporteur ;</p>
<p>e) La forme, la dénomination sociale, le numéro SIRET et l'adresse du principal établissement ou du siège de la direction de la société dont les titres sont apportés ;</p>
<p>f) Le nombre de titres reçus en rémunération de l'apport et leur valeur à cette date, correspondant à la valeur de l'apport ;</p>
<p>g) Le montant de la plus-value réalisée lors de l'apport dont l'imposition est reportée ;</p>
<p>h) En cas de cession des titres apportés, le nombre de titres cédés et la date de leur cession par la société bénéficiaire de l'apport ;</p>
<p>i) En cas de cession à titre onéreux, de rachat ou d'annulation de tout ou partie des droits sociaux reçus en rémunération de l'apport, la nature et la date de l'opération ainsi que le nombre de titres concernés ;</p>
<p>j) En cas de transmission à titre gratuit, par l'apporteur, des droits sociaux reçus en rémunération de l'apport dans le cadre d'une opération visée à l'article 41 du code général des impôts, les nom et adresse du bénéficiaire qui a pris l'engagement d'acquitter l'impôt sur la plus-value en report ;</p>
<p>k) En cas de fusion ou de scission de la société dont les droits ou parts ont été apportés ou de la société bénéficiaire de l'apport, sans remise en cause du report, le nombre de titres reçus ainsi que la forme, la dénomination sociale, le numéro SIRET et l'adresse du principal établissement ou du siège de la société ou des sociétés dont les titres ont été remis à l'échange ;</p>
<p>l) En cas de transformation de la société bénéficiaire de l'apport, la date de l'opération et la nouvelle forme adoptée par cette société.</p>
<p>II. - Le bénéficiaire de la transmission mentionné au 2° du IV de l'article 151 octies B du code général des impôts qui prend l'engagement prévu à ce même 2° est également soumis aux obligations du I.</p>
''',
    "Réécriture à droit constant : la liste est formulée de manière plus directe, les valeurs sont rattachées explicitement à l'apport et le II identifie la personne soumise aux mêmes obligations. Les douze lettres et toutes les hypothèses de cession, transmission, échange ou transformation demeurent. Aucune réforme de fond n'est appliquée.",
    "Maintien des quatorze alinéas, des I et II et des lettres a à l. Le prix de revient fiscal des titres apportés au d reste distinct de la valeur des titres reçus au f. Le j reste subordonné à une opération de l'article 41 et à l'engagement d'acquitter l'impôt. Le k reste limité aux fusions ou scissions sans remise en cause du report et couvre les deux sociétés possibles ; le renvoi au 2° du IV de l'article 151 octies B est conservé.")

add('41-0 A bis B', '''
<p>L'état à produire en application du cinquième alinéa de l'article 151 octies C du code général des impôts comporte les renseignements suivants :</p>
<p>a) L'adresse du siège de la direction ou du principal établissement de la société ou de l'organisme transformé, sa forme, sa dénomination sociale et le numéro d'identification qui lui a été attribué dans les conditions du premier alinéa de l'article R. 123-221 du code de commerce ;</p>
<p>b) La liste des associés de la société ou de l'organisme transformé à la date de la transformation ;</p>
<p>c) La date de la transformation ;</p>
<p>d) L'adresse du principal établissement ou du siège de la direction de l'association d'avocats, sa dénomination et le numéro d'identification qui lui a été attribué dans les conditions du premier alinéa de l'article R. 123-221 du code de commerce ;</p>
<p>e) La liste des associés et la proportion de leurs droits dans l'association, à la date de la transformation et au 31 décembre de l'année d'imposition. Le cas échéant, l'état mentionne aussi les événements qui ont fait varier cette proportion au cours de l'année d'imposition ;</p>
<p>f) Le nom et l'adresse de l'associé déclarant, le nombre de parts qu'il détenait dans la société ou l'organisme transformé et la plus-value ou moins-value constatée lors de la transformation ;</p>
<p>g) Le montant, la nature et l'origine des plus-values dont le report d'imposition est maintenu au nom de l'associé déclarant lors de la transformation.</p>
''',
    "Réécriture à droit constant : l'obligation de produire l'état est formulée directement et le e distingue les deux dates de photographie des droits et les événements de l'année. Les informations d'identification techniques sont conservées sans substitutions artificielles. Les lettres a à g et tous les renseignements restent présents, sans réforme de fond.",
    "Maintien des huit alinéas utiles, du 31 décembre, de la photographie à la transformation et des deux renvois au premier alinéa de l'article R. 123-221 du code de commerce. Le cinquième alinéa de l'article 151 octies C du corpus rend applicable le premier alinéa du V de l'article 151 octies B. La note historique source cite « l'article 3-3° et 45 de la décret n° 2022-1014 du 19 juillet 2022 » : formulation grammaticalement défectueuse signalée, sans correction de sa portée ni insertion normative. Le saut de ligne final sans texte est supprimé.")

add('41-0 A ter', '''
<p>I. - Pour l'application du II de l'article 151 nonies du code général des impôts, les bénéficiaires de la transmission joignent à leur déclaration de revenus les deux états prévus au 2 du II et au VI du même article, établis selon les modèles fixés par l'administration. Ces états indiquent la date de la transmission, les noms et adresses des bénéficiaires concernés, la dénomination sociale et l'adresse de la société dont les droits ou parts sont transmis, le nombre et le pourcentage des droits ou parts transmis, la nature des droits des bénéficiaires sur ces droits ou parts et les informations nécessaires au suivi des plus-values en report d'imposition.</p>
<p>L'état prévu au 2 du II de l'article 151 nonies précité indique en outre le montant des plus-values réalisées lors de la transmission dont l'imposition est reportée.</p>
<p>L'état prévu au VI de l'article 151 nonies précité indique également les opérations réalisées ou les événements survenus au cours de l'année qui sont de nature à mettre fin au report d'imposition ou à le transmettre à un nouveau bénéficiaire, ainsi que le montant des plus-values qui demeurent en report d'imposition.</p>
<p>II. - Pour l'application des III et IV de l'article 151 nonies du code général des impôts, l'état prévu au VI du même article est établi selon un modèle fixé par l'administration. Il indique les nom et adresse du bénéficiaire du report d'imposition, la dénomination sociale et l'adresse de la société dont les droits ou parts sont détenus, le nombre de droits ou parts détenus et la nature de l'opération ou de l'événement qui a entraîné le report d'imposition. Il indique aussi les opérations réalisées ou les événements survenus au cours de l'année qui sont de nature à mettre fin au report d'imposition ou à le transmettre à un nouveau bénéficiaire, le montant des plus-values qui demeurent en report d'imposition et les informations nécessaires à leur suivi.</p>
''',
    "Réécriture à droit constant : le premier alinéa désigne directement les bénéficiaires tenus de joindre les deux états ; le II sépare les informations d'identification et d'origine du report de celles du suivi annuel. Les informations communes et les compléments propres à chaque état restent complets. Aucune réforme de fond n'est introduite.",
    "Maintien des quatre alinéas et des I et II. Au I, le nombre et le pourcentage des droits transmis et la nature des droits des bénéficiaires restent exigés. Au II, le nombre de droits détenus et l'origine du report restent distincts de ces données de transmission. Les modèles administratifs, les montants encore reportés et les événements susceptibles de mettre fin au report ou de le transmettre sont conservés dans les deux cadres.")

add('41 A', '''
<p>Les versements à fonds perdus qui remplissent les conditions de l'article 41 B peuvent être compris, quel que soit leur montant, dans les charges déductibles pour l'établissement de l'impôt sur le revenu ou de l'impôt sur les sociétés s'ils bénéficient à des organismes habilités à collecter les versements des employeurs destinés à satisfaire à l'obligation de participer à la construction instituée par l'article L. 313-1 du code de la construction et de l'habitation (1). Ces versements doivent être effectués par des entreprises industrielles et commerciales, par des contribuables exerçant une profession non commerciale ou par des entreprises agricoles ayant opté pour le régime de l'imposition d'après le bénéfice réel.</p>
<p>(1) Voir code de la construction et de l'habitation, articles R. 313-1 à R. 313-40.</p>
''',
    "Réécriture à droit constant : les versements sont placés en sujet, puis les catégories de contributeurs admises sont énoncées dans une seconde phrase du même alinéa. La déduction quel que soit le montant, l'habilitation du collecteur et l'option agricole pour le bénéfice réel restent intégrales. Aucune réforme de fond ni exonération générale des bénéfices réinvestis n'est créée.",
    "Maintien des deux alinéas, dont le renvoi explicatif (1), de l'article 41 B et de l'article L. 313-1 du CCH. Les trois catégories d'auteurs de versements sont alternatives, conformément au champ de la source. Le renvoi historique aux articles R. 313-1 à R. 313-40 est conservé ; sa portée dans la numérotation réglementaire du CCH doit être vérifiée avant insertion. Aucun taux d'impôt ni droit de mutation n'est modifié ici.")


assert len(drafts) == len(sources) == 24
answer = [drafts[a['number']] for a in sources]
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
