import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

sources = json.loads(Path('source.json').read_text())
answers = []

def tables(index):
    root = ET.fromstring('<root>' + sources[index]['source_xml'] + '</root>')
    out = []
    for table in root.findall('.//table'):
        new = ET.Element('table')
        body = ET.SubElement(new, 'tbody')
        for row in table.findall('.//tr'):
            tr = ET.SubElement(body, 'tr')
            for cell in row:
                attrs = {k: v for k, v in cell.attrib.items() if k in ('rowspan', 'colspan')}
                item = ET.SubElement(tr, cell.tag, attrs)
                item.text = ' '.join(' '.join(cell.itertext()).split())
        out.append(ET.tostring(new, encoding='unicode'))
    return out

def add(index, xml, reason, notes):
    assert index == len(answers)
    source = sources[index]
    answers.append({**{k: source[k] for k in ('code_id', 'source_id', 'source_sha256', 'number')},
                    'proposed_xml': xml.strip(), 'reason': reason,
                    'review_notes': notes, 'status': 'rewrite_draft'})

add(0, '''
<p>Avant de transmettre au service des impôts l'engagement de gestion prévu à l'article 1395 B bis du code général des impôts, le propriétaire le fait viser par le préfet du lieu de situation des parcelles. Le préfet vérifie que cet engagement est conforme aux conditions et modalités définies aux articles 310-00 H et 310-00 H bis.</p>
<p>Le préfet veille au respect des engagements souscrits dans ce cadre. À cette fin, les agents des services de l'État et de ses établissements publics peuvent effectuer des vérifications sur place. Ils en informent le propriétaire et, le cas échéant, le preneur des parcelles concernées et leur proposent d'assister au contrôle.</p>
<p>Lorsqu'un contrôle révèle le non-respect d'une obligation prévue par l'engagement de gestion, ce constat est signalé au service des impôts du lieu de situation de la parcelle avant le 1er janvier de l'année qui suit celle du contrôle.</p>
''', "Réécriture à droit constant : les responsabilités du propriétaire et du préfet sont explicitées, puis les opérations de contrôle et le signalement sont présentés dans leur ordre d'exécution. Aucune réforme de fond n'est appliquée à cet engagement de gestion.",
"Les trois alinéas, les renvois aux articles 1395 B bis, 310-00 H et 310-00 H bis, l'information du preneur éventuel et l'échéance du signalement sont conservés. La graphie source « ler janvier » est normalisée en « 1er janvier ». La note relative à l'article 114-I de la loi n° 2016-1087 du 8 août 2016 est historique et ne fixe aucune entrée en vigueur nouvelle.")

t = tables(1)
add(1, f'''
<p>Les critères de performance énergétique et environnementale mentionnés au I bis de l'article 1384 A du code général des impôts sont définis comme suit :<br /><br />
1° En France métropolitaine, la construction doit atteindre les résultats minimaux déterminés selon les modalités mentionnées dans l'annexe à l'article R. 172-4 du code de la construction et de l'habitation. Elle respecte les exigences suivantes :<br /><br />
a) Pour le coefficient Icénergie _ maxmoyen :<br /><br />
Lorsque la demande de permis de construire est déposée du 1er janvier 2024 au 31 décembre 2024, la valeur applicable est celle fixée au II du chapitre III de cette annexe pour les années 2025 à 2027 ;<br /><br />
Lorsque la demande de permis de construire est déposée à compter du 1er janvier 2025, la valeur applicable est celle fixée au même II à compter de 2028 ;<br /><br />
b) Pour le coefficient Icconstruction _ maxmoyen :<br /><br />
Lorsque l'ouverture du chantier intervient dans les conditions prévues au B du VII de l'article 65 de la loi n° 2022-1726 du 30 décembre 2022 et que la demande de permis de construire est déposée jusqu'au 31 décembre 2024, la valeur applicable est celle fixée au III du même chapitre III pour les années 2025 à 2027 ;<br /><br />
Lorsque la demande de permis de construire est déposée du 1er janvier 2025 au 31 décembre 2027, la valeur applicable est celle fixée au même III pour les années 2028 à 2030 ;<br /><br />
Lorsque la demande de permis de construire est déposée à compter du 1er janvier 2028, la valeur applicable est celle fixée au même III à compter de 2031 ;<br /><br />
Le respect de ces résultats minimaux est évalué selon la méthode de calcul prévue à l'article R. 172-6 du code de la construction et de l'habitation ;<br /><br />
2° En Guadeloupe, en Guyane, en Martinique, à La Réunion et à Mayotte, la construction doit atteindre les résultats minimaux déterminés par la réglementation applicable dans la collectivité concernée. Elle respecte également les critères de performance énergétique et environnementale suivants :<br /><br />
a) Sauf pour les constructions mentionnées aux b et d du présent 2°, les facteurs solaires des parois opaques horizontales et des parois opaques verticales des pièces principales en contact avec l'extérieur ne doivent pas dépasser, respectivement, les valeurs maximales Smax indiquées ci-dessous :<br /><br />
Pour les constructions dont l'ouverture du chantier intervient dans les conditions prévues au B du VII de l'article 65 de la loi n° 2022-1726 du 30 décembre 2022 et dont la demande de permis de construire est déposée jusqu'au 31 décembre 2027 :</p>
{t[0]}
<p>Pour les constructions dont la demande de permis de construire est déposée à compter du 1er janvier 2028 :</p>
{t[1]}
<p>b) Pour les constructions situées à La Réunion à une altitude supérieure à 600 mètres, les coefficients de transmission surfacique des parois opaques horizontales et des parois opaques verticales en contact avec l'extérieur ne doivent pas dépasser, respectivement, les valeurs maximales Umax indiquées ci-dessous :<br /><br />
Pour les constructions dont l'ouverture du chantier intervient dans les conditions prévues au B du VII de l'article 65 de la loi n° 2022-1726 du 30 décembre 2022 et dont la demande de permis de construire est déposée jusqu'au 31 décembre 2027 :</p>
{t[2]}
<p>Pour les constructions dont la demande de permis de construire est déposée à compter du 1er janvier 2028 :</p>
{t[3]}
<p>c) Sauf pour les constructions mentionnées au d du présent 2° et pour les baies des pièces de service dont la surface est inférieure à 0,5 m2, le facteur solaire S de chaque baie des logements en contact avec l'extérieur ne doit pas dépasser les valeurs maximales suivantes, selon le lieu de la construction et l'orientation de la façade :<br /><br />
Pour les constructions dont l'ouverture du chantier intervient dans les conditions prévues au B du VII de l'article 65 de la loi n° 2022-1726 du 30 décembre 2022 et dont la demande de permis de construire est déposée jusqu'au 31 décembre 2027 :</p>
{t[4]}
<p>Pour les constructions dont la demande de permis de construire est déposée à compter du 1er janvier 2028 :</p>
{t[5]}
<p>d) Pour les constructions situées en Guadeloupe, l'indicateur ICT de chaque logement est déterminé selon les modalités fixées par la délibération du conseil régional de la Guadeloupe CR/19-1155 du 31 octobre 2019 susvisée. Cet indicateur doit être inférieur :</p>
<p>– d'au moins 10 % au seuil ICT _ max déterminé selon les modalités fixées au chapitre V de cette même délibération, pour les constructions dont l'ouverture du chantier intervient dans les conditions prévues au B du VII de l'article 65 de la loi n° 2022-1726 du 30 décembre 2022 et dont la demande de permis de construire est déposée jusqu'au 31 décembre 2027 ;<br /><br />
– d'au moins 15 % au seuil ICT _ max déterminé selon les modalités fixées au chapitre V de cette même délibération, pour les constructions dont la demande de permis de construire est déposée à compter du 1er janvier 2028 ;</p>
<p>e) Chaque logement dispose d'un système de production d'eau chaude sanitaire qui couvre au moins 70 % des besoins de ce logement à partir d'une ou de plusieurs sources de chaleur renouvelable au sens du premier alinéa de l'article L. 211-2 du code de l'énergie. Ces systèmes ne peuvent être connectés au réseau électrique que pour alimenter les auxiliaires et les appoints intégrés ;<br /><br />
f) Toutes les robinetteries des logements sont équipées de mitigeurs munis de dispositifs hydro-économes. La chasse d'eau des WC comporte un mécanisme à double commande ;<br /><br />
3° Les critères de performance énergétique et environnementale qui ne sont pas mentionnés aux 1° et 2° du présent article doivent être au moins égaux à ceux prévus au titre VII du livre Ier du code de la construction et de l'habitation.</p>
''', "Réécriture à droit constant : chaque exigence est reliée explicitement à sa période de dépôt du permis, à sa localisation et, lorsque la source le prévoit, aux conditions d'ouverture du chantier. Les exceptions, la méthode de calcul et les six tableaux sont intégralement conservés. Les obligations relatives à l'eau chaude et aux équipements sont formulées directement. Aucune réforme de fond des performances ni de l'exonération fiscale n'est introduite.",
"Les subdivisions 1° à 3°, les lettres a à f, l'ordre des paragraphes et les six tableaux sont maintenus ; seuls les sauts de ligne et les attributs de présentation sont nettoyés. Les valeurs et cellules fusionnées des tableaux sont conservées. Incohérence préexistante : les a et b du 2° annoncent des exigences pour les parois horizontales et verticales, mais leurs tableaux applicables jusqu'au 31 décembre 2027 ne contiennent qu'une ligne pour les parois verticales. Aucune valeur horizontale n'est ajoutée. Les tirets des tableaux du c sont conservés sans leur attribuer de valeur. Le renvoi « susvisée » à la délibération guadeloupéenne est conservé bien que cette délibération ne soit pas citée auparavant dans cet article. Les dérogations locatives envisagées par policy.json ne sont pas étendues à cette exonération de taxe foncière.")

add(2, '''
<p>I. – Pour obtenir le certificat mentionné au I bis de l'article 1384 A du code général des impôts, le maître d'ouvrage transmet une attestation à la direction dans le ressort de laquelle se situe la construction : direction départementale des territoires, direction départementale des territoires et de la mer ou direction de l'environnement, de l'aménagement et du logement. Cette attestation est délivrée par un organisme accrédité pour cette activité de certification selon la norme NF EN ISO/CEI 17065 par le Comité français d'accréditation ou par tout autre organisme d'accréditation signataire de l'accord multilatéral pris dans le cadre de la coordination européenne des organismes d'accréditation, et ayant signé une convention à cet effet avec le ministre chargé de la construction.<br /><br />
L'attestation indique que le maître d'ouvrage a obtenu une certification de produit établissant, pour la construction, le respect de l'ensemble des critères de performance énergétique et environnementale définis à l'article 310-0 H. Elle indique également qu'il a pris toutes les dispositions nécessaires pour que la construction satisfasse à ces critères.<br /><br />
II. – Le directeur départemental des territoires, le directeur départemental des territoires et de la mer ou le directeur de l'environnement, de l'aménagement et du logement établit le certificat constatant que la construction respecte l'ensemble des critères de performance énergétique et environnementale définis à l'article 310-0 H.</p>
<p>III. – Le certificat est transmis au centre des impôts foncier du lieu de situation de la construction, accompagné de la déclaration mentionnée à l'article 1406 du code général des impôts.</p>
''', "Réécriture à droit constant : la transmission de l'attestation, son contenu, l'établissement du certificat et sa transmission au service fiscal sont distingués. La norme d'accréditation, l'accord multilatéral et la convention ministérielle sont conservés. Aucune réforme de fond n'affecte cette procédure.",
"Les I, II et III ainsi que les renvois aux articles 1384 A, 310-0 H et 1406 sont maintenus. Le II reste dans le premier paragraphe XML, comme dans la source. La formulation conserve la condition de convention sans réattribuer cette condition à une autre personne ; le rattachement grammatical de « ayant signé » dans la source appelle une vérification lors d'une éventuelle clarification réglementaire. Aucun signataire supplémentaire ni document nouveau n'est exigé.")

add(3, '''
<p>Si, après la délivrance du certificat mentionné à l'article 310-0 H bis, un contrôle réalisé par un agent assermenté de la direction départementale des territoires ou de la direction départementale des territoires et de la mer géographiquement compétente révèle que le maître d'ouvrage ne respecte pas l'un des critères figurant dans le certificat délivré en application du II du même article, cette direction doit signaler le constat au centre des impôts foncier du lieu de situation de la construction.</p>
''', "Réécriture à droit constant : les conditions du contrôle sont rapprochées et l'obligation de signalement de la direction est formulée directement. La qualité de l'agent et les directions compétentes sont maintenues. Aucune réforme de fond n'est introduite.",
"Le contrôle demeure postérieur à la délivrance du certificat et porte sur les critères du certificat prévu au II de l'article 310-0 H bis. La direction de l'environnement, de l'aménagement et du logement, mentionnée dans cet article de renvoi, n'est pas mentionnée par la source du présent article : cette différence de champ est conservée et appelle contrôle. La note relative au décret n° 2009-1484 du 3 décembre 2009, articles 20-I, 22 et 24, reste une indication historique.")

add(4, '''
<p>I. – Chaque année, la valeur locative moyenne communale prévue au IV de l'article 1411 du code général des impôts est calculée à partir des valeurs locatives des locaux d'habitation autres qu'exceptionnels. Sont retenus les locaux compris dans les rôles émis au titre de l'année précédente avant le 31 décembre de cette même année.</p>
<p>II. – (Sans objet).</p>
''', "Réécriture à droit constant : la règle de calcul annuelle est séparée de la sélection des locaux et des rôles à retenir. Le II sans objet est conservé. Aucune réforme de fond de la taxe d'habitation n'est appliquée.",
"Les subdivisions I et II, l'exclusion des locaux exceptionnels et le renvoi au IV de l'article 1411 sont conservés. La date limite reste « avant le 31 décembre » de l'année précédente : elle n'est pas remplacée par une échéance inclusive.")

add(5, '''
<p>Pour l'application de la cotisation foncière des entreprises et des taxes additionnelles, les règles suivantes s'appliquent :</p>
<p>– Le nombre de salariés est calculé pour l'ensemble de l'entreprise sur la période de référence définie à l'article 1467 A du code général des impôts. Les travailleurs à mi-temps ou saisonniers sont comptés à proportion de la durée de leur travail ;</p>
<p>– Les apprentis sous contrat sont les titulaires d'un contrat d'apprentissage conclu dans les conditions prévues aux articles L. 6221-1 à L. 6225-8 du code du travail. Les handicapés physiques sont les travailleurs handicapés reconnus par la commission des droits et de l'autonomie des personnes handicapées mentionnée à l'article L. 146-9 du code de l'action sociale et des familles ;</p>
<p>– Constitue un établissement toute installation qu'une entreprise utilise en un lieu déterminé. Constitue également un établissement une unité de production intégrée à un ensemble industriel ou commercial, lorsqu'elle peut être exploitée de manière autonome.</p>
''', "Réécriture à droit constant : les règles de décompte des salariés et les définitions sont formulées en phrases distinctes, en conservant les trois alinéas de l'énumération. Aucune réforme de fond de la cotisation foncière des entreprises n'est introduite.",
"Le périmètre de l'entreprise, le prorata des seuls travailleurs à mi-temps ou saisonniers et les références à 1467 A, L. 6221-1 à L. 6225-8 et L. 146-9 sont conservés. Le terme défini « handicapés physiques » est maintenu malgré son ancienneté pour ne pas modifier le champ fiscal. Les réformes des contrats et du temps partiel n'entraînent pas ici de nouveau mode de décompte.")

add(6, '''
<p>Pour toutes les opérations appartenant à une même catégorie définie au premier alinéa de l'article 1465 du code général des impôts, l'exonération prévue par cet article doit avoir la même quotité et la même durée.</p>
''', "Réécriture à droit constant : le champ de comparaison entre opérations est placé avant l'obligation d'identité de quotité et de durée. Aucune réforme de fond de l'exonération n'est introduite.",
"Le renvoi vise toujours les catégories du premier alinéa de l'article 1465 et ne crée pas une identité obligatoire entre catégories différentes. La quotité et la durée restent deux exigences distinctes.")

add(7, '''
<p>À défaut de délibération contraire, restent applicables les délibérations en vigueur au 1er janvier 1980 qui ont été prises en application de l'article 1465 du code général des impôts dans sa rédaction antérieure à la loi n° 80-10 du 10 janvier 1980.</p>
''', "Réécriture à droit constant : la réserve d'une délibération contraire est placée en tête, puis les deux conditions de maintien des délibérations anciennes sont rapprochées. Aucune réforme de fond ni extinction de ce régime transitoire n'est introduite.",
"La date du 1er janvier 1980 et la référence à la loi n° 80-10 du 10 janvier 1980 sont conservées avec leurs fonctions distinctes. Le maintien des délibérations anciennes ne vaut pas création d'une nouvelle exonération autonome.")

add(8, '''
<p>Le ministre du budget définit par arrêté les zones dans lesquelles l'aménagement du territoire justifie une exonération temporaire de cotisation foncière des entreprises pour les entreprises réalisant les opérations énumérées à l'article 1465 du code général des impôts (1).</p>
<p>(1) Voir l'annexe IV, article 121 quinquies DB bis ; les annexes I et IV à l'arrêté du 24 novembre 1980 (J. O. du 7 décembre) ; et l'annexe de l'arrêté du 24 novembre 1982 (J. O. du 24 mars 1983).</p>
''', "Réécriture à droit constant : l'autorité qui délimite les zones est explicitement désignée comme sujet ; la note de renvoi est ponctuée pour distinguer les textes cités. Aucune réforme de fond du zonage ou de l'exonération n'est introduite.",
"Les renvois et dates de la note (1) sont tous conservés. L'article 121 quinquies DB bis n'a pas été retrouvé sous ce numéro dans le fichier public impots-annexe-4.json fourni ; sa disponibilité et la portée actuelle des arrêtés anciens doivent être contrôlées. L'articulation entre ces zones anciennes et les zones d'aide à finalité régionale mentionnées à l'article 1465 du corpus appelle également contrôle. Aucun zonage n'est remplacé silencieusement. La note source concernant l'article 2-6.1.16 [3]° de la loi n° 2009-1673 du 30 décembre 2009 est historique.")

add(9, '''
<p>Pour les opérations non soumises à agrément, l'augmentation nette des bases d'imposition mentionnée au quatrième alinéa de l'article 1465 du code général des impôts est déterminée en retenant l'investissement net. Celui-ci est égal au prix de revient des immobilisations nouvelles diminué du prix de revient des immobilisations supprimées.</p>
''', "Réécriture à droit constant : la règle applicable aux opérations sans agrément est distinguée de la définition de l'investissement net. Aucune réforme de fond du calcul n'est introduite.",
"Le renvoi au quatrième alinéa de l'article 1465 est vérifié dans le corpus public fourni et conservé. Le calcul demeure une différence de prix de revient ; aucune référence à la valeur de marché ni aucun plancher n'est ajouté.")

add(10, '''
<p>Pendant une période d'exonération temporaire en cours, l'entreprise peut demander l'ouverture d'une nouvelle période pour les investissements qui remplissent les conditions requises. Ces investissements doivent avoir été réalisés à partir de la troisième année suivant celle de l'opération ayant motivé l'exonération en cours.</p>
''', "Réécriture à droit constant : la faculté de demander une nouvelle période est séparée de la condition de date des investissements. Aucune réforme de fond ni automaticité de l'exonération n'est introduite.",
"Le point de départ reste la troisième année suivant celle de l'opération initiale, et non la troisième année de l'exonération. L'article 1465 du CGI dans le corpus public indique que deux périodes d'exonération ne peuvent courir simultanément : l'articulation avec la demande d'ouverture autorisée ici pendant une période en cours appelle contrôle. La proposition ne tranche pas cette tension préexistante et ne crée pas de droit au cumul.")

add(11, '''
<p>Si le changement d'exploitant prend effet le 1er janvier, l'ancien exploitant doit souscrire la déclaration relative à l'année de ce changement.</p>
''', "Réécriture à droit constant : le déclarant et l'année concernée sont nommés directement dans une phrase plus courte. Aucune réforme de fond de l'obligation déclarative n'est introduite.",
"La déclaration reste à la charge de l'ancien exploitant lorsque le changement prend effet le 1er janvier. La règle n'est pas étendue aux changements prenant effet à une autre date.")

add(12, '''
<p>Pour les corrections de la valeur locative des immobilisations prévues au III de l'article 1478 du code général des impôts, tout mois commencé compte pour un mois entier.</p>
<p>Pour la correction de la valeur locative des immobilisations des établissements exerçant une activité saisonnière, prévue au V du même article 1478, toute semaine commencée compte pour une semaine entière. L'activité est saisonnière lorsque la durée annuelle d'ouverture de l'établissement est comprise entre douze et quarante et une semaines, que l'ouverture soit continue ou répartie sur plusieurs périodes.</p>
''', "Réécriture à droit constant : les deux règles d'arrondi sont formulées directement et la définition de l'activité saisonnière est allégée sans modifier ses bornes. Aucune réforme de fond de l'annualité de la cotisation n'est introduite.",
"Les deux alinéas et leurs renvois distincts aux III et V de l'article 1478 sont maintenus. La durée reste comprise entre douze et quarante et une semaines ; aucune exigence de continuité n'est ajoutée. L'arrondi mensuel et l'arrondi hebdomadaire ne sont pas confondus.")

add(13, '''
<p>Pour l'application de l'article 1478 du code général des impôts, la suspension par un redevable de son activité dans un établissement pendant au moins douze mois consécutifs est considérée comme une cessation d'activité suivie d'une création d'établissement.</p>
''', "Réécriture à droit constant : la portée fiscale de la qualification est annoncée avant la condition de durée et ses effets. Aucune réforme de fond de la cessation d'activité n'est introduite.",
"Le seuil de douze mois consécutifs, son caractère minimal, le périmètre de l'établissement et le renvoi à l'article 1478 sont conservés. Aucune cessation générale de l'entreprise n'est déduite de cette règle.")

add(14, f'''
<p>Pour déterminer la base d'imposition à la taxe foncière sur les propriétés bâties des locaux d'habitation loués sous le régime de la loi n° 48-1360 du 1er septembre 1948 modifiée, les coefficients prévus au 1 du III de l'article 1496 du code général des impôts sont fixés par le tableau suivant. Ils s'appliquent à compter du 1er janvier 1979 et jusqu'à la prochaine actualisation des valeurs locatives foncières des propriétés bâties :</p>
{tables(14)[0]}
''', "Réécriture à droit constant : le champ des logements est présenté avant la période d'application des coefficients. Le tableau complet des sept catégories est conservé. Aucune réforme de fond des baux anciens ni des valeurs locatives n'est introduite.",
"Les coefficients 2,83 ; 2,49 ; 2,14 ; 1,93 ; 1,75 ; 1,00 ; et 1,93 sont maintenus dans leur ordre. Les renvois au 1 du III de l'article 1496 et à l'article 34 de la loi du 1er septembre 1948 sont conservés. La date du 1er janvier 1979 est une borne historique d'application, sans présumer réalisée l'actualisation qui mettrait fin à cette règle.")

add(15, '''
<p>L'usine marémotrice de la Rance, située à Saint-Malo et à La Richardais (Ille-et-Vilaine), bénéficie de la déduction complémentaire prévue au dernier alinéa de l'article 1499 du code général des impôts (1).</p>
<p>Cette déduction complémentaire est appliquée au taux de 50 %.</p>
<p>(1) Voir également l'article 333 E.</p>
''', "Réécriture à droit constant : l'établissement bénéficiaire est placé en sujet et le taux est rattaché explicitement à sa déduction complémentaire. La note de renvoi est conservée. Aucune réforme de fond du taux ou du champ n'est introduite.",
"Le taux de 50 %, les deux communes et le renvoi au dernier alinéa de l'article 1499 sont conservés. Le renvoi à l'article 333 E est vérifié dans le corpus public : ce dernier applique les dispositions de l'article 310 K au Centre national d'études spatiales de Kourou. La note sur la loi n° 2020-1721 du 29 décembre 2020, article 29-I-1°, ne constitue pas une date de réforme nouvelle.")

add(16, '''
<p>Le coefficient départemental moyen d'augmentation des bases d'imposition des immobilisations industrielles prévu à l'article 1499 A du code général des impôts est calculé en divisant un numérateur par un dénominateur. Le numérateur est le total des bases d'imposition des établissements industriels à la taxe foncière sur les propriétés bâties de 1974. Le dénominateur est le total des bases d'imposition de ces mêmes établissements à la contribution foncière des propriétés bâties établie en 1973, diminué du revenu net des outillages et installations exonérés par le 11° de l'article 1382 du même code.</p>
''', "Réécriture à droit constant : le calcul est présenté sous la forme explicite d'un rapport dont le numérateur et le dénominateur sont identifiés. Aucune réforme de fond du coefficient historique n'est introduite.",
"Les années 1974 et 1973 conservent leurs rôles respectifs. La diminution du revenu net des outillages et installations s'applique au dénominateur. Les renvois aux articles 1499 A et 1382, 11°, sont maintenus. L'article 1499 A du corpus confirme le contexte des apports, scissions ou fusions antérieurs à 1976 ; ce champ n'est pas étendu par la proposition.")

add(17, '''
<p>I. – La valeur locative de locaux, établissements ou installations de caractère industriel ou commercial est évaluée selon les II à IV lorsque ces biens se situent dans différentes communes, présentent des caractéristiques analogues et sont affectés au transport public par voie ferrée, à la production ou à la distribution publique d'énergie électrique, de gaz ou d'eau potable, ou à la radiodiffusion et à la télévision.</p>
<p>II. – Pour chacun des secteurs d'activité mentionnés au I, les immobilisations présentant des caractéristiques analogues sont regroupées en catégories.</p>
<p>III. – La valeur locative des immobilisations de chaque catégorie est calculée en appliquant un tarif fixé par arrêté du ministre de l'économie et des finances et du ministre de l'intérieur, publié au Journal officiel. Ce tarif est établi en fonction de la valeur locative d'immobilisations de référence particulièrement représentatives de la catégorie par leurs caractéristiques techniques, leur importance et l'année de leur mise en service (1).</p>
<p>IV. – Pour évaluer la valeur locative des immobilisations de référence, les règles applicables sont celles des établissements industriels ou celles des locaux commerciaux.</p>
<p>(1) Arrêté du 22 mai 1974 (J. O. du 9 juin) et arrêté du 9 janvier 1976 (J. O. du 6 février).</p>
''', "Réécriture à droit constant : les conditions de l'évaluation commune sont réunies au I, puis le classement, la fixation du tarif et l'évaluation des références sont exprimés plus directement. Aucune réforme de fond de l'évaluation n'est introduite.",
"Les I à IV et la note (1) restent à leur place. Tous les secteurs sont conservés, y compris la qualification de distribution publique et le couple radiodiffusion et télévision. Les critères techniques, l'importance, l'année de mise en service et les deux autorités ministérielles sont maintenus, de même que les arrêtés des 22 mai 1974 et 9 janvier 1976 et leurs indications de publication.")

add(18, f'''
<p>La modulation prévue au III de l'article 1501 du code général des impôts est fixée selon le nombre pondéré d'équipements et de services offerts, en appliquant le barème suivant :</p>
{tables(18)[0]}
''', "Réécriture à droit constant : la relation entre le nombre pondéré d'équipements et la modulation est formulée directement. Les cinq lignes du barème sont conservées intégralement. Aucune réforme de fond du tarif des ports de plaisance n'est introduite.",
"Les tranches de 0 à 20, de 21 à 40, de 41 à 60, de 61 à 80 et de 81 à 100 restent associées à −40 %, −20 %, 0 %, +20 % et +40 %. La pondération demeure déterminée par les articles 310 O et 310 P ; aucun équipement supplémentaire n'est créé ici. Le renvoi au III de l'article 1501 est conservé.")

add(19, '''
<p>Pour calculer le nombre d'équipements et de services mentionné à l'article 310 N, sont retenus les équipements et services suivants lorsqu'ils sont présents dans les limites administratives portuaires. Chaque alinéa compte pour un :</p>
<p>a) L'accès à l'ensemble des bassins à toute heure pour les navires présentant un tirant d'eau maximum supérieur à un mètre ou un tirant d'air maximum supérieur à trois mètres ;</p>
<p>b) La mise à disposition d'un site et d'aménagements dont les profondeurs nécessaires à la navigation peuvent être maintenues sans opérations de dragage pour en garantir l'exploitation ;</p>
<p>c) La mise à disposition, pour les plaisanciers, d'emplacements réservés au stationnement des véhicules terrestres à moteur ;</p>
<p>d) La présence de commerces ;</p>
<p>e) La présence d'équipements de sûreté ;</p>
<p>f) La réalisation de prestations de gardiennage ;</p>
<p>g) La réalisation de prestations de collecte des eaux usées des navires ;</p>
<p>h) La présence d'une station d'avitaillement ;</p>
<p>i) La mise à disposition d'une aire de carénage ;</p>
<p>j) La présence de moyens de levage dont la capacité est supérieure à 30 tonnes.</p>
''', "Réécriture à droit constant : le mode de décompte est séparé du critère de localisation et les prestations sont décrites plus directement. Les dix lettres et les libellés techniques nécessaires sont conservés. Aucune réforme de fond des équipements pris en compte n'est introduite.",
"Chaque alinéa a à j reste compté pour un, quel que soit le nombre d'équipements correspondants. Les seuils strictement supérieurs à un mètre, trois mètres et 30 tonnes sont conservés, ainsi que l'alternative « ou » entre les tirants d'eau et d'air, l'accès à toute heure à tous les bassins et la condition d'absence de dragage. Le périmètre demeure celui des limites administratives portuaires.")

add(20, f'''
<p>Pour déterminer la pondération mentionnée à l'article 310 N, la capacité moyenne d'accueil d'un poste d'amarrage de chaque port de plaisance est retenue selon le barème suivant :</p>
{tables(20)[0]}
<p>La capacité moyenne d'accueil d'un poste d'amarrage est le rapport, exprimé en mètres, entre la somme des longueurs des navires pouvant stationner sur chaque poste d'amarrage et le nombre total de postes d'amarrage du port de plaisance. Sont exclus de ce calcul les dispositifs permanents d'amarrage par un corps mort ou directement par ancre présents dans la rade du port, ainsi que les postes situés dans les zones d'échouage.</p>
<p>Le nombre pondéré d'équipements et de services offerts mentionné à l'article 310 N se calcule en multipliant le nombre de services et d'équipements effectivement offerts, mentionnés à l'article 310 O, par le coefficient de pondération fixé dans le tableau annexé au premier alinéa.</p>
''', "Réécriture à droit constant : la moyenne d'accueil est définie comme un rapport explicite, puis le calcul du nombre pondéré est formulé comme une multiplication. Le tableau et toutes les exclusions sont conservés. Aucune réforme de fond de la pondération n'est introduite.",
"Les cinq tranches et les coefficients 2, 4, 6, 8 et 10 sont conservés, avec les mêmes bornes inclusives ou exclusives de 8, 10, 14 et 18 mètres. Les exclusions des corps morts, ancres dans la rade et zones d'échouage sont maintenues. Le tableau reste rattaché au premier alinéa et les renvois aux articles 310 N et 310 O sont conservés ; seule une balise div vide de présentation est supprimée.")

add(21, '''
<p>Pour l'application du deuxième alinéa du I de l'article 1498 du code général des impôts, les propriétés bâties visées au premier alinéa du même I sont réparties entre les sous-groupes et catégories ci-après :</p>
<p>Sous-groupe I : magasins et lieux de vente :</p>
<p>Catégorie 1 : boutiques et magasins situés sur rue.</p>
<p>Catégorie 2 : commerces dépourvus d'accès direct sur la rue.</p>
<p>Catégorie 3 : magasins faisant partie d'un ensemble commercial.</p>
<p>Catégorie 4 : magasins de grande surface dont la surface principale est comprise entre 400 et 2 500 m2.</p>
<p>Catégorie 5 : magasins de très grande surface dont la surface principale est supérieure ou égale à 2 500 m2.</p>
<p>Catégorie 6 : stations-service, stations de lavage et assimilables.</p>
<p>Catégorie 7 : marchés.</p>
<p>Sous-groupe II : bureaux et locaux divers assimilables :</p>
<p>Catégorie 1 : locaux à usage de bureaux présentant un agencement ancien.</p>
<p>Catégorie 2 : locaux à usage de bureaux présentant un agencement récent.</p>
<p>Catégorie 3 : locaux assimilables à des bureaux et présentant des aménagements spécifiques.</p>
<p>Sous-groupe III : lieux de dépôt ou de stockage et parcs de stationnement :</p>
<p>Catégorie 1 : lieux de dépôt à ciel ouvert et terrains utilisés à des fins commerciales ou industrielles.</p>
<p>Catégorie 2 : lieux de dépôt couverts.</p>
<p>Catégorie 3 : parcs de stationnement à ciel ouvert.</p>
<p>Catégorie 4 : parcs de stationnement couverts.</p>
<p>Catégorie 5 : installations spécifiques de stockage.</p>
<p>Sous-groupe IV : ateliers et autres locaux assimilables :</p>
<p>Catégorie 1 : ateliers artisanaux.</p>
<p>Catégorie 2 : locaux affectés à une activité de transformation, de manutention ou de maintenance.</p>
<p>Catégorie 3 : chenils, viviers et autres locaux assimilables.</p>
<p>Sous-groupe V : hôtels et locaux assimilables :</p>
<p>Catégorie 1 : hôtels de catégorie « confort », classés 4 étoiles et plus ou offrant un confort identique.</p>
<p>Catégorie 2 : hôtels de catégorie « supérieur », classés 2 ou 3 étoiles ou offrant un confort identique.</p>
<p>Catégorie 3 : hôtels de catégorie « standard », classés 1 étoile ou offrant un confort identique.</p>
<p>Catégorie 4 : foyers d'hébergement, centres d'accueil et auberges de jeunesse.</p>
<p>Catégorie 5 : hôtels-clubs, villages de vacances et résidences hôtelières.</p>
<p>Sous-groupe VI : établissements de spectacles, de sports et de loisirs :</p>
<p>Catégorie 1 : salles de spectacles et locaux assimilables.</p>
<p>Catégorie 2 : établissements ou terrains réservés à la pratique d'un sport ou à des spectacles sportifs.</p>
<p>Catégorie 3 : salles de loisirs diverses.</p>
<p>Catégorie 4 : terrains de camping confortables, classés 3 étoiles et plus ou offrant un confort identique.</p>
<p>Catégorie 5 : terrains de camping ordinaires, classés 1 ou 2 étoiles ou offrant un confort identique.</p>
<p>Catégorie 6 : établissements de détente et de bien-être.</p>
<p>Catégorie 7 : centres de loisirs, centres de colonies de vacances et maisons de jeunes.</p>
<p>Sous-groupe VII : établissements d'enseignement et locaux assimilables :</p>
<p>Catégorie 1 : écoles et institutions privées exploitées sans but lucratif.</p>
<p>Catégorie 2 : établissements d'enseignement à but lucratif.</p>
<p>Sous-groupe VIII : cliniques et établissements du secteur sanitaire et social :</p>
<p>Catégorie 1 : cliniques et établissements hospitaliers.</p>
<p>Catégorie 2 : centres médico-sociaux, centres de soins, crèches et haltes-garderies.</p>
<p>Catégorie 3 : maisons de repos et maisons de retraite (médicalisées ou non).</p>
<p>Catégorie 4 : centres de rééducation, centres de thalassothérapie et établissements thermaux.</p>
<p>Sous-groupe IX : carrières et établissements industriels non évalués selon la méthode comptable :</p>
<p>Catégorie 1 : établissements industriels nécessitant un outillage important, à l'exception des carrières et établissements assimilés.</p>
<p>Catégorie 2 : carrières et établissements assimilables.</p>
<p>Sous-groupe X : établissements présentant des caractéristiques exceptionnelles :</p>
<p>Catégorie 1 : locaux dont les caractéristiques sortent de l'ordinaire et qui ne relèvent, de ce fait, d'aucune des catégories précédentes.</p>
''', "Réécriture à droit constant : l'introduction précise la répartition des propriétés, les critères de surface et de classement sont exprimés en phrases lisibles et les descriptions complexes sont simplifiées. Les intitulés techniques simples restent conservés. Les dix sous-groupes et les trente-neuf catégories sont reproduits intégralement dans le même ordre. Aucune réforme de fond de la nomenclature n'est introduite.",
"Les numéros de sous-groupes et de catégories ainsi que les 50 paragraphes sont maintenus. Incohérence préexistante conservée : dans le sous-groupe I, la catégorie 4 comprend une surface principale « comprise entre 400 et 2 500 m2 », tandis que la catégorie 5 commence à une surface « supérieure ou égale à 2 500 m2 » ; le cas de 2 500 m2 appelle une clarification. Les étoiles, équivalences de confort, buts lucratifs ou non, exclusions et caractères spécifiques des locaux sont conservés. La date de validité fournie pour cette source est le 1er juillet 2026 ; aucune date de promulgation future n'en est déduite.")

add(22, '''
<p>Les usines de traitement des combustibles nucléaires et les centrales nucléaires entrent dans le champ de l'abattement d'un tiers appliqué à la valeur locative des usines nucléaires en vertu de l'article 1518 A du code général des impôts.</p>
''', "Réécriture à droit constant du contenu source : les deux catégories d'usines sont placées en sujet pour expliciter le champ de l'abattement. Aucune réforme de fond ni suppression de cette disposition n'est introduite.",
"L'abattement d'un tiers et les deux catégories d'usines sont conservés. Incohérence préexistante : l'article 1518 A du CGI présent dans le corpus public fourni ne mentionne plus les usines nucléaires ; il traite des aéroports et d'installations ou matériels bénéficiant d'autres réductions. Le fondement et l'applicabilité actuelle de cette règle doivent donc être contrôlés. Le renvoi source est maintenu sans lui substituer une référence supposée.")

add(23, '''
<p>Pour les produits extraits chaque année, les tonnages nets servant au calcul de la redevance communale des mines l'année suivante sont déterminés selon les règles ci-après :</p>
<p>Pour la houille et les lignites, sont retenus les tonnages de combustible marchand livrés dans l'année, y compris la consommation des exploitations concernées et les livraisons à leur personnel ;</p>
<p>Pour les minerais de fer, la pyrite, les schistes bitumineux ou carbobitumineux, les calcaires et grès bitumineux ou asphaltiques, la bauxite et la fluorine, sont retenus les tonnages de produits marchands livrés dans l'année par la mine, après préparation mécanique s'il y a lieu, soit à ses usines annexes de traitement chimique ou physique, soit directement à d'autres consommateurs ;</p>
<p>Pour les minerais divers imposés d'après la quantité de métal, de métalloïde ou d'oxyde contenu, le tonnage retenu est calculé à partir des tonnages et des teneurs des minerais devenus marchands après la préparation mécanique effectuée dans les usines annexes aux exploitations, avant le traitement métallurgique. Toutefois, pour les minerais aurifères, l'évaluation repose sur la quantité de métal précieux effectivement extraite par le traitement métallurgique.</p>
<p>Pour le chlorure de sodium, la redevance est calculée selon les règles suivantes :</p>
<p>a) Pour le sel extrait par abattage, sont retenus les tonnages nets livrés dans l'année par la mine à ses usines annexes ou directement à d'autres consommateurs, sous forme de sel tout venant, trié, égrugé ou trié et égrugé ;</p>
<p>b) Pour le sel extrait en dissolution par sondage puis raffiné, sont retenus les tonnages nets de sel raffiné livrés dans l'année par l'atelier d'évaporation de la mine, soit à des usines annexes de la mine, soit directement à d'autres consommateurs ;</p>
<p>c) Pour le sel extrait en dissolution par sondage sans raffinage ultérieur, sont retenus les tonnages de chlorure de sodium contenu dans les dissolutions livrées dans l'année par la mine à ses usines annexes ou directement à d'autres consommateurs.</p>
<p>Pour les hydrocarbures, la redevance est calculée d'après les tonnages de produits livrés dans l'année par la mine lorsqu'ils sont liquides, et d'après leurs volumes lorsqu'ils sont gazeux. Sont compris la consommation des exploitations concernées, les livraisons à leur personnel et les livraisons à leurs usines annexes de traitement chimique ou physique autre que le dégazolinage et la désulfuration. Le gaz réinjecté dans le gisement producteur ou brûlé dans les torches est exclu. Pour les hydrocarbures gazeux, la redevance peut être établie soit sur le gaz naturel brut livré en cet état, soit sur les produits hydrocarburés issus du dégazolinage ou de la désulfuration du gaz naturel brut.</p>
<p>Pour le gaz carbonique, la redevance est calculée d'après le volume de gaz livré aux utilisateurs dans l'année.</p>
''', "Réécriture à droit constant : chaque produit est associé directement à l'assiette à retenir ; les règles des minerais aurifères et des hydrocarbures sont divisées en phrases distinctes. Tous les produits, modes de préparation, livraisons internes et exclusions sont conservés. Aucune réforme de fond de la redevance minière n'est introduite.",
"Les dix alinéas et les lettres a, b et c sont conservés, avec simple normalisation de leur ponctuation. Le décalage entre l'année des extractions et l'année de calcul de la redevance est maintenu. Les quantités de métal précieux effectivement extraites, les trois formes d'extraction du sel, les tonnages liquides, les volumes gazeux, l'exclusion du gaz réinjecté ou brûlé et l'alternative d'assiette des gaz issus du traitement sont maintenus. Aucune taxe nouvelle ni aucun taux ne sont ajoutés.")

assert len(answers) == len(sources) == 24
Path('answer.json').write_text(json.dumps(answers, ensure_ascii=False, indent=2) + '\n')
print('answer.json:',len(answers),'articles')
