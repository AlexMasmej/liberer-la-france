import xml.etree.ElementTree as ET

drafts = {}

def nomenclature(source_xml):
    root = ET.fromstring('<div>' + source_xml + '</div>')
    tables = root.findall('table')
    for table in tables:
        for node in table.iter():
            node.attrib = {key: value for key, value in node.attrib.items()
                           if key in ('rowspan', 'colspan') and value.isdecimal()}
        table.tail = None
    return [ET.tostring(table, encoding='unicode') for table in tables]

def add_nomenclature(source_xml):
    tables = nomenclature(source_xml)
    drafts['41 undecies'] = (
        '<p>I. - Dans sa demande de remboursement, le requérant classe les biens et les services acquis selon les codes du tableau suivant :</p>\n'
        + tables[0]
        + '\n<p>Si le requérant utilise le code 10, il doit préciser la nature des biens livrés et des services fournis.</p>\n'
        + '<p>II. - Pour les dépenses figurant dans le tableau suivant, le requérant utilise, dans sa demande de remboursement, les sous-codes spécifiques qui y sont indiqués :</p>\n'
        + tables[1],
        "Réécriture à droit constant des règles d'utilisation de la nomenclature : le requérant est désigné comme responsable du classement et de la précision exigée sous le code 10. Les deux tableaux réglementaires sont conservés intégralement, avec leurs libellés de classement, codes, sous-codes, seuils et exclusions ; ces libellés normalisés ne sont pas présentés comme reformulés. Aucune réforme de fond.",
        "Deux tableaux complets conservés : 10 codes principaux, 39 sous-codes, cellules sans sous-code pour les codes 4, 8 et 10 et regroupements rowspan. Les seuils de 3,5 tonnes, le partage supérieur / inférieur ou égal, les exclusions relatives aux passagers payants et les distinctions entre assujetti, employé et autres personnes sont inchangés. Les discontinuités de numérotation sont maintenues. Différence préexistante de libellé au code 3 : le I exclut les « biens et services » des codes 1 et 2, le II les « marchandises et biens » ; ne pas harmoniser leur portée sans arbitrage. Renvoi de l'article 41 decies, II, 8°, préservé.")

drafts['42'] = ('''
<p>Les personnes qui vendent des bâtiments utilisés par des compagnies de navigation de la marine marchande ou par des pêcheurs professionnels, destinés à la navigation maritime et soumis à la formalité de la francisation, ainsi que celles qui vendent des bateaux utilisés à la navigation de commerce sur les fleuves internationaux et inscrits en douane comme tels, doivent conserver à l'appui de leur comptabilité l'un des justificatifs suivants :</p>
<p>soit l'indication du numéro et de la date de l'acte de francisation ou d'inscription dans un bureau de douane ;</p>
<p>soit, si ce titre n'a pas encore été délivré, le duplicata de la demande de francisation (formule 300 A ou 300 B, selon le cas) ou de l'inscription en douane, visé par le service des douanes. Les vendeurs doivent réclamer ce document à leurs acheteurs.</p>
''',
"Réécriture à droit constant : le champ des ventes est organisé en deux catégories, puis les justificatifs alternatifs sont introduits explicitement. L'obligation de réclamer le document à l'acheteur est formulée avec son responsable. Aucune réforme de fond.",
"Les deux catégories de navires, la condition de francisation ou d'inscription et les deux branches de justification sont conservées, avec les formules 300 A et 300 B. La terminologie historique de francisation et les références à ces formules restent celles de la source de 1979 ; leur articulation avec les formalités contemporaines doit être contrôlée dans les textes maritimes et douaniers hors du présent lot. Aucun remplacement par un justificatif supposé équivalent n'est opéré.")

drafts['43'] = ('''
<p>a. Les personnes qui réparent ou transforment les bâtiments et bateaux visés à l'article 42 doivent faire apparaître distinctement dans leur comptabilité les fournitures d'articles nécessaires à ces opérations.</p>
<p>b. Elles doivent mentionner sur leurs factures le nom du bâtiment ou du bateau, ainsi que les numéros et la date de francisation ou d'inscription correspondants.</p>
''',
"Réécriture à droit constant : les obligations comptables et les mentions de facture sont formulées par des verbes directs, avec maintien des deux lettres. Aucune réforme de fond.",
"Le a et le b restent en place pour préserver notamment le renvoi de l'article 44 à l'article 43-b. Distinction des fournitures en comptabilité, nom du navire, numéros et date de francisation ou d'inscription conservés. Même contrôle de coordination maritime et douanière que pour l'article 42, sans substitution silencieuse à la terminologie source.")

drafts['44'] = ('''
<p>Les personnes qui vendent des produits destinés à être incorporés dans les bâtiments visés à l'article 42 ou des engins et filets de pêche destinés à la pêche maritime doivent respecter les obligations prévues à l'article 43-b.</p>
''',
"Réécriture à droit constant : le champ des deux catégories de ventes et l'obligation par renvoi sont exprimés directement. Aucune réforme de fond.",
"Les produits incorporés restent limités aux bâtiments de l'article 42 et les engins et filets restent rattachés à la pêche maritime. Le renvoi exact à l'article 43-b est conservé : les obligations comptables distinctes du a ne sont pas étendues à ces vendeurs.")

drafts['45'] = ('''
<p>Les personnes qui effectuent les opérations mentionnées aux 2° à 7° du II de l'article 262 du code général des impôts doivent faire figurer sur leurs factures la qualité de leurs acheteurs qui justifie la franchise.</p>
''',
"Réécriture à droit constant : la mention de facture est exprimée par une obligation directe, en rattachant la justification de la franchise à la qualité des acheteurs. Aucune réforme de fond.",
"Le champ exact des 2° à 7° du II de l'article 262 et le terme source « franchise » sont conservés. Aucune extension à d'autres opérations, ni attestation supplémentaire, n'est introduite.")

drafts['46'] = ('''
<p>Lorsqu'un bateau cesse d'être affecté à la navigation privilégiée définie à l'article 42, ce changement d'affectation doit être déclaré au service des douanes auprès duquel sa francisation ou son inscription a été effectuée.</p>
<p>Une déclaration doit également être déposée au préalable dans un bureau de douane lorsque des articles d'équipement ou de gréement, y compris les engins et filets de pêche, doivent être débarqués pour recevoir une affectation non privilégiée.</p>
''',
"Réécriture à droit constant : le changement d'affectation et le débarquement sont formulés dans deux phrases plus directes, en maintenant les destinataires et le caractère préalable propre au second cas. Aucune réforme de fond.",
"Les deux alinéas sont conservés : le premier désigne le service de francisation ou d'inscription, le second un bureau de douane et exige une déclaration préalable. Équipement, gréement, engins et filets de pêche restent inclus. La source n'identifie pas le déclarant ; aucun débiteur nouveau n'est inventé. Terminologie maritime historique à coordonner avec l'article 42 et les textes douaniers hors du lot.")
