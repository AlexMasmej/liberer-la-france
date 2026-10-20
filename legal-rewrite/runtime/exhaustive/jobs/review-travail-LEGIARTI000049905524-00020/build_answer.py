import json
import re
import html
from pathlib import Path
from xml.etree import ElementTree as ET

source = json.loads(Path('source.json').read_text())[0]
references = json.loads(Path('reference-targets.json').read_text())
previous = source['previous_draft']['proposed_xml']
root = ET.fromstring('<root>' + previous + '</root>')
rows = root.findall('.//tr')
assert len(rows) == 70

def cell(index, column=-1):
    return list(rows[index])[column]

def put(index, content, column=-1):
    target = cell(index, column)
    attributes = target.attrib.copy()
    target.clear()
    target.attrib.update(attributes)
    fragment = ET.fromstring('<fragment>' + content + '</fragment>')
    target.text = fragment.text
    for child in list(fragment):
        target.append(child)

def replace(index, old, new, column=-1):
    target = cell(index, column)
    content = ''.join(ET.tostring(c, encoding='unicode') for c in target)
    assert content.count(old) == 1, (index, old)
    put(index, content.replace(old, new), column)

# Les emplacements sont conservés, y compris ceux dont la prescription disparaît.
replace(1, '<p>Effectif permanent (2) (I) ;</p>', '')
replace(1, "<p>Effectif mensuel moyen de l'année considérée (3) (I) ;</p>", '')
replace(1, '<p>Effectif total au 31 décembre (1) (I) ;</p>',
        '<p>Effectif total au 31 décembre (1) (I) ; le présent i n’exige plus de décompte de l’effectif permanent ni d’effectif mensuel moyen ;</p>')
replace(1, "<p>Durée moyenne des contrats de travail temporaire pour les contrats antérieurs à la réforme ; pour les emplois nouveaux, durée moyenne des missions, distincte de la durée de l'emploi ;</p>", '')
replace(1, '<p>Nombre mensuel moyen de salariés temporaires (8) ;</p>',
        '<p>Nombre mensuel moyen de salariés temporaires (8) ; aucun calcul distinct de durée moyenne des contrats ou des missions n’est exigé.</p>')
replace(2, '<p>Nombre de salariés de moins de vingt-cinq ans embauchés.</p>', '')
replace(2, '<p>Nombre de mutations entre établissements (I) ;</p>', '')
replace(2, '<p>Nombre de décès (I).</p>',
        '<p>Nombre de décès (I). Aucun décompte isolé des embauches de salariés de moins de vingt-cinq ans ou des mutations entre établissements n’est exigé au titre du présent b.</p>')
replace(2, "<p>iii-Promotions : nombre de salariés promus dans une catégorie supérieure pendant l'année (11).</p>",
        '<p>iii-Promotions : les données du a du B du I du 2° sont utilisées sans relevé supplémentaire (11).</p>')
replace(5, '<p>Pourcentage de la masse salariale consacré à la formation continue ;</p>', '')
replace(5, '<p>Montants consacrés respectivement à la formation interne, à la formation assurée en application de conventions, aux versements aux organismes de recouvrement, aux versements aux organismes agréés et aux autres dépenses ; montant total ;</p>',
        '<p>Montant total consacré à la formation continue ; aucune ventilation supplémentaire entre formation interne, conventions, organismes de recouvrement, organismes agréés et autres dépenses, ni aucun ratio à la masse salariale n’est exigé au titre de cette rubrique ;</p>')

replace(6, '<p>Taux de fréquence des accidents du travail (I) ;</p>',
        '<p>Taux de fréquence des accidents du travail (I), exprimé par le rapport suivant :</p>')
replace(6, "<p>Nombre d'accidents du travail avec arrêt × 106 divisé par le nombre d'heures travaillées ;</p>", '')
replace(6, '<p>Taux de gravité des accidents du travail (I) ;</p>',
        '<p>Taux de gravité des accidents du travail (I), exprimé par le rapport suivant :</p>')
replace(6, "<p>Nombre de journées perdues × 10 ³ divisé par le nombre d'heures travaillées ;</p>",
        '<p>Aucun second calcul de ces taux avec un autre facteur d’échelle n’est exigé.</p>')
replace(6, '<p>ii-Répartition des accidents par élément matériel (28) :</p>',
        '<p>ii-Répartition des accidents par élément matériel (28) : les données des documents de prévention et de suivi des accidents sont utilisées dans leur nomenclature existante, sans recodage imposé par le présent article. Le recensement séparé selon les codes de l’arrêté du 10 octobre 1974 n’est plus exigé.</p>')
# ElementTree conserve les paragraphes adjacents sans créer de séparateur.
content = ''.join(ET.tostring(c, encoding='unicode') for c in cell(6))
start = content.index("<p>Nombre d'accidents liés à des risques graves")
end = content.index('<p>iii-Maladies professionnelles :</p>', start)
content = content[:start] + content[end:]
put(6, content)
replace(6, "<p>Nombre de déclarations par l'employeur de procédés de travail susceptibles de provoquer des maladies professionnelles (29).</p>", '')
replace(6, "<p>Nombre de salariés atteints d'affections pathologiques à caractère professionnel et caractérisation de ces affections ;</p>",
        '<p>Nombre de salariés atteints d’affections pathologiques à caractère professionnel et caractérisation de ces affections ; le nombre des déclarations de procédés de travail n’est plus exigé au titre du présent iii, sans dispense des déclarations légalement requises ;</p>')
replace(6, "<p>Taux de réalisation du programme de sécurité présenté l'année précédente ;</p>", '')
replace(6, '<p>Existence et nombre de plans spécifiques de sécurité.</p>',
        '<p>Le rapport et le programme annuels prévus à l’article L. 2312-27 restent accessibles. Le présent tableau n’impose ni taux distinct de réalisation du programme ni comptage des plans spécifiques de sécurité.</p>')
replace(6, '<p>Nombre de salariés à temps partiel (I), en distinguant ceux travaillant entre 20 et 30 heures (33) et les autres formes de temps partiel ;</p>',
        '<p>Nombre de salariés à temps partiel (33) (I), sans ventilation obligatoire dans une tranche de 20 à 30 heures ;</p>')
replace(6, "<p>ix-Transformation de l'organisation du travail : expériences visant à améliorer le contenu du travail (41).</p>",
        '<p>ix-Abrogé.</p>')
replace(6, "<p>Montant des dépenses consacrées à cette amélioration dans l'entreprise (42) ; taux de réalisation du programme de l'année précédente.</p>",
        '<p>Montant des dépenses consacrées à cette amélioration dans l’entreprise (42), sans calcul distinct d’un taux de réalisation du programme de l’année précédente.</p>')
put(9, '<p>c) Abrogé.</p>')
replace(13, '<p>Répartition des effectifs entre temps complet, temps partiel compris entre 20 et 30 heures et autres formes de temps partiel ;</p>',
        '<p>Répartition des effectifs entre temps complet et temps partiel ; aucune tranche obligatoire de 20 à 30 heures n’est reconstituée ;</p>')
replace(22, "<p>Maladies ayant donné lieu à un examen de reprise en application du 3° de l'article R. 4624-31 : nombre d'arrêts de travail et de journées d'absence.</p>",
        '<p>Le décompte supplémentaire des arrêts et journées d’absence au titre des maladies ayant donné lieu à un examen de reprise n’est plus exigé. Cette suppression ne modifie ni les examens de reprise légalement requis ni leurs dispenses.</p>')

put(36, '<p>a) Frais de personnel (24), cotisations sociales comprises ; évolutions salariales par catégorie et par sexe ; salaire de base minimum et salaire moyen ou médian (17) par sexe et par catégorie professionnelle.</p>'
    '<p>i-Abrogé. Aucun choix ni cumul d’indicateurs supplémentaires de montant des rémunérations n’est exigé au titre du présent i.</p>'
    '<p>ii-Abrogé. Aucun rapport supplémentaire de hiérarchie des rémunérations ni montant global des dix rémunérations les plus élevées n’est exigé au titre du présent ii.</p>'
    '<p>iii-Abrogé. Les pourcentages de salariés rémunérés au rendement ou payés au mois sur la base de l’horaire affiché ne sont plus exigés au titre du présent iii.</p>'
    '<p>iv-Abrogé. La charge salariale globale n’est pas présentée une seconde fois après les frais de personnel du a.</p>')
put(42, '<p>a) Représentants du personnel et délégués syndicaux :</p>'
    '<p>Composition des comités sociaux et économiques et des comités d’établissement, sans relevé de l’appartenance syndicale des personnes ; participation aux élections par collège et catégorie de représentants ; dates, signatures et objet des accords conclus pendant l’année ; nombre de bénéficiaires d’un congé d’éducation ouvrière (45).</p>'
    '<p>Les actes et données déjà accessibles sont utilisés sans recensement distinct. Le volume annuel des crédits d’heures utilisés et le nombre annuel de réunions avec les représentants du personnel ou les délégués syndicaux ne font pas l’objet d’un comptage obligatoire au titre de cette rubrique.</p>'
    '<p>b) Abrogé.</p><p>c) Abrogé.</p>')
replace(53, '<p>c) Résultats globaux de la production en valeur et en volume ;</p>',
        '<p>c) Abrogé.</p>')
put(54, '<p>8° Partenariats de sous-traitance :</p>')
put(55, '<p>A-Partenariats dans lesquels l’entreprise produit des services ou des produits pour une autre entreprise en qualité de sous-traitant.</p>')
put(56, '<p>B-Partenariats dans lesquels l’entreprise recourt à un sous-traitant pour bénéficier de services ou de produits. Les autres partenariats commerciaux ne sont pas soumis à un recensement obligatoire au titre du présent 8°.</p>')

# Notes attachées aux prescriptions retirées : pas de formule de remplacement.
for number in [2, 3, 18, 19, 20, 21, 22, 29, 41]:
    note = next(p for p in cell(69).findall('p') if (p.text or '').startswith(f'({number}) '))
    note.text = f'({number}) Abrogé.'
for number, text in {
    11: '(11) Les données sur les promotions sont celles du a du B du I du 2°, sans relevé supplémentaire.',
    28: '(28) La répartition par élément matériel est celle des documents existants de prévention et de suivi des accidents. Aucune conversion vers les codes de l’arrêté du 10 octobre 1974 n’est exigée.',
}.items():
    note = next(p for p in cell(69).findall('p') if (p.text or '').startswith(f'({number}) '))
    note.text = text

# Le renvoi vers l'autre article est limité aux subdivisions effectivement visées.
second = root.findall('p')[1]
second.text = 'Elle comporte aussi les informations sur la formation professionnelle et les conditions de travail prévues aux e et f du A du 1° de l’article R. 2312-8. Ce renvoi ne porte pas sur les autres subdivisions de cet article.'

# Réemploi opposable et respect des dispositions supérieures, sans nouveau registre.
tail = root.findall('p')[2:]
assert len(tail) == 4
tail[0].text = ('Les informations et documents exacts, à jour et déjà légalement disponibles sont réutilisés. Leur mise à disposition dans la base, ou leur accès direct depuis celle-ci pour tous les membres habilités, dispense de nouvelle saisie, de copie et de relevé distinct contenant les mêmes données. L’accès permet de les identifier et de les consulter effectivement ; il respecte les secrets protégés et les droits d’accès légalement prévus. Une information commune à plusieurs rubriques n’est produite qu’une fois ; elle reste identifiable dans chacune de ces rubriques. Les ventilations complémentaires maintenues par le tableau restent accessibles. Les durées de couverture et les perspectives prévues aux articles L. 2312-36 et R. 2312-10 ne sont pas réduites. Les informations nécessaires aux consultations et à l’égalité professionnelle prévues à l’article L. 2312-18 restent dues ; les suppressions du tableau retirent les seuls indicateurs supplémentaires qu’elles désignent et non les informations exigées sur un autre fondement. Aucun relevé, rapport ou registre de remplacement n’est imposé pour les indicateurs supprimés.')
tail[1].text = ('La suppression d’un relevé ou d’une ventilation par le présent article ne supprime aucun salaire, congé, repos, garantie de prévoyance ou de retraite, droit à participation, intéressement, aide, crédit d’impôt, réduction ou exonération. Ces avantages restent ouverts aux situations futures éligibles, y compris aux emplois de même objet relevant du contrat unique, dans les conditions des dispositions qui les régissent. Leur bénéfice n’est subordonné ni à la production d’un indicateur supprimé ni à une formalité de remplacement instituée par le présent article. Les droits et créances antérieurs restent conservés. Les consultations, négociations, déclarations, contrôles et mesures de prévention fondés sur une disposition autonome demeurent applicables. Les rubriques de prévoyance et de retraite complémentaire ne rétablissent aucun modèle ou état annuel de protection complémentaire supprimé sur son fondement propre.')
tail[2].text = ('Les mentions de contrats à durée déterminée concernent les données historiques et les contrats conclus avant l’entrée en vigueur de la loi instituant le contrat de travail unique. Elles ne permettent ni nouvelle conclusion ni renouvellement après cette entrée en vigueur. Pour les nouvelles relations de travail de droit privé, y compris l’intérim, le portage, l’insertion et l’alternance, la durée d’une mission, d’une saison, d’une formation, d’une convention ou d’une aide ne fixe pas le terme de l’emploi à durée indéterminée. Le présent article ne modifie ni le préavis individuel, ni le seuil ou le calcul de l’indemnité ordinaire de rupture, ni les indemnités spéciales, ni les autorisations et procédures collectives distinctes. Il ne modifie pas le régime propre des agents publics. Les informations sur les impôts, les bénéfices ou les aides ne créent aucun prélèvement, acompte ou déclaration fiscale et ne rétablissent ni impôt ordinaire annuel sur les bénéfices conservés ni taxe supprimée.')
tail[3].text = ('Les suppressions et allègements prévus au présent article s’appliquent aux mises à disposition effectuées à compter de l’entrée en vigueur de la loi portant la présente réforme, y compris pour des périodes antérieures. Les documents déjà régulièrement mis à disposition ne sont pas à refaire. Les informations historiques maintenues par le tableau restent accessibles pour les périodes qui les concernent. Les manquements antérieurs, droits et recours qui en résultent conservent leur régime, sous réserve de l’application de la loi répressive plus douce.')

proposed = '\n'.join(ET.tostring(child, encoding='unicode') for child in root)
Path('proposed.xml').write_text(proposed)
assert len(ET.fromstring('<root>'+proposed+'</root>').findall('.//tr')) == 70

def plain(xml):
    value = re.sub(r'<[^>]+>', ' ', xml)
    return ' '.join(html.unescape(value).split())

source_text = plain(source['source_xml'])
proposed_text = plain(proposed)

def effect(kind, measure_id, description, before, after, unit,
           source_quote, proposed_quote, conditions=None, population=None):
    assert len(source_quote) >= 12 and source_quote in source_text, source_quote
    assert len(proposed_quote) >= 12 and proposed_quote in proposed_text, proposed_quote
    return {
        'kind': kind,
        'measure_id': measure_id,
        'description': description,
        'before': before,
        'after': after,
        'unit': unit,
        'affected_population': population or 'Employeurs d’au moins trois cents salariés sans accord de l’article L. 2312-21 et destinataires habilités de leur BDESE.',
        'conditions_and_transition': conditions or 'Mises à disposition à compter de l’entrée en vigueur de la loi portant la réforme, même pour une période antérieure ; documents déjà communiqués non refaits ; droits et recours antérieurs conservés, sous réserve de la loi répressive plus douce.',
        'replacement_or_new_burdens': 'Aucun relevé, registre, rapport ou justificatif de remplacement. Les informations maintenues et celles dues sur un fondement autonome restent accessibles ; le gain de temps effectif n’est pas chiffré.',
        'source_quote': source_quote,
        'proposed_quote': proposed_quote,
    }

effects = [
    effect('obligation_removed', 'bdese-decomptes-effectifs-supplementaires',
           'Retrait de deux agrégats supplémentaires de personnel, sans retirer l’effectif total ni ses répartitions utiles.',
           'Effectif permanent à temps plein et en CDI sur toute l’année, plus effectif mensuel moyen calculé par somme des douze effectifs de fin de mois divisée par 12.',
           'Aucun de ces deux agrégats n’est exigé par le i du a du A du 1° ; effectif au 31 décembre et répartitions conservés. Les séries mensuelles de R2312-21 gardent leur fondement propre.',
           'legal_duty', 'Effectif permanent (2) (I) ;',
           'le présent i n’exige plus de décompte de l’effectif permanent ni d’effectif mensuel moyen'),
    effect('obligation_removed', 'bdese-duree-moyenne-missions',
           'Suppression de la durée moyenne des contrats de travail temporaire, sans recréer une durée moyenne obligatoire des missions pour les emplois nouveaux.',
           'Calcul de la durée moyenne des contrats de travail temporaire, en plus du nombre mensuel moyen de salariés temporaires.',
           'Seul le nombre mensuel moyen est conservé ici ; ni durée de contrat ni durée moyenne de mission supplémentaire. La fin d’une mission ne termine pas l’emploi nouveau.',
           'legal_duty', 'Durée moyenne des contrats de travail temporaire ;',
           'aucun calcul distinct de durée moyenne des contrats ou des missions n’est exigé.'),
    effect('obligation_removed', 'bdese-embauches-jeunes-mutations',
           'Retrait de deux comptages isolés qui ne conditionnent aucun droit à l’emploi ou à une aide.',
           'Décompte distinct des embauches de moins de vingt-cinq ans et des mutations d’un établissement à un autre, ces dernières figurant dans les départs.',
           'Ces deux comptages ne sont plus imposés par le b ; l’âge des effectifs, les embauches, départs et données d’égalité demeurent.',
           'legal_duty', 'Nombre de mutations d’un établissement à un autre (I) ;'.replace('d’un', "d'un"),
           'Aucun décompte isolé des embauches de salariés de moins de vingt-cinq ans ou des mutations entre établissements n’est exigé au titre du présent b.'),
    effect('obligation_merged', 'bdese-releves-stages-promotions',
           'Une seule production pour l’évolution des stagiaires et pour les promotions, avec les répartitions maintenues.',
           'Évolution des stagiaires dans une ligne autonome et nombre au a ii ; promotions au b iii et indicateurs plus détaillés au 2° I B a.',
           'Stagiaires et évolution réunis au a ii ; données de promotions du 2° I B a réutilisées au b iii, sans second relevé.',
           'legal_duty', "Nombre de salariés promus dans l'année dans une catégorie supérieure (11) ;",
           'iii-Promotions : les données du a du B du I du 2° sont utilisées sans relevé supplémentaire (11).'),
    effect('obligation_removed', 'bdese-nomenclatures-sans-minima',
           'Conservation de la coupe antérieure des nomenclatures minimales de qualification et d’âge ; aucune suppression supplémentaire revendiquée pour ce seul maintien.',
           'Trois ou quatre postes minimum de qualification en I, cinq ou six en II, et quatre catégories d’âge minimum, dont les moins de vingt-cinq ans.',
           'Catégories habituelles de l’entreprise, sans ces minima ; moins de vingt-cinq ans et ventilation femmes-hommes maintenus. Les deux niveaux de comparaison des rémunérations au 2° demeurent.',
           'legal_duty', 'I.-Une structure de qualification détaillée, en trois ou quatre postes minimum, est requise.',
           'I.-La ventilation par qualification utilise les catégories habituellement retenues dans l’entreprise, sans nombre minimal de postes à reconstituer.'.replace('l’entreprise', "l'entreprise")),
    effect('obligation_removed', 'bdese-nationalite-affiliation-syndicale',
           'Conservation de la suppression des ventilations selon nationalité et du relevé d’appartenance syndicale, sans supprimer la composition du CSE ni les données par sexe.',
           'Ventilation français/étrangers de l’effectif et des incapacités permanentes ; indication, s’il y a lieu, de l’appartenance syndicale dans la composition des comités.',
           'Nationalité retirée des deux relevés ; composition des comités conservée sans relevé de l’appartenance syndicale des personnes.',
           'legal_duty', "Répartition de l'effectif total au 31/12 selon la nationalité (I) : français/ étrangers ;",
           'sans relevé de l’appartenance syndicale des personnes'),
    effect('obligation_removed', 'bdese-financement-formation-agrege',
           'Suppression du ratio de dépenses de formation à la masse salariale et de la ventilation supplémentaire par circuit de financement.',
           'Pourcentage de masse salariale et montants séparés formation interne, conventions, recouvrement, organismes agréés, autres, total.',
           'Montant total conservé, sans ratio ni cette ventilation ; bénéficiaires, heures rémunérées/non rémunérées, types d’actions, congés et informations du e de R2312-8 restent dus.',
           'legal_duty', 'Pourcentage de la masse salariale afférent à la formation continue ;',
           'aucune ventilation supplémentaire entre formation interne, conventions, organismes de recouvrement, organismes agréés et autres dépenses, ni aucun ratio à la masse salariale n’est exigé au titre de cette rubrique'),
    effect('obligation_removed', 'bdese-taux-accidents-sans-double-calcul',
           'Retrait du second calcul des taux de fréquence et de gravité sous une autre échelle.',
           'Deux expressions successives pour chaque taux : rapports simples, puis mentions × 106 et × 10 ³. Le premier facteur présente une ambiguïté typographique.',
           'Rapports simples déjà présents dans la source conservés ; second calcul non exigé. Aucun facteur de conversion ni seuil de prévention nouveau.',
           'legal_duty', "Nombre d'accidents de travail avec arrêt × 106 divisé par nombre d'heures travaillées ;",
           'Aucun second calcul de ces taux avec un autre facteur d’échelle n’est exigé.'),
    effect('obligation_removed', 'bdese-accidents-sans-recodage-1974',
           'Retrait du tableau de recensement séparé en six groupes de codes matériels anciens ; maintien de l’analyse par élément matériel dans sa nomenclature existante.',
           'Six groupes imposés : 32 à 40 ; 02 ; 09 à 30 ; 01,03,04,06,07,08 ; 05 ; autres cas, avec référence à l’arrêté du 10 octobre 1974.',
           'Répartition existante des documents de prévention et de suivi, y compris pour les données par sexe du 2° I D ; aucune conversion ni tableau séparé selon les anciens groupes.',
           'legal_duty', 'Nombre d’accidents liés à l’existence de risques graves-codes 32 à 40 ;'.replace('d’accidents', "d'accidents").replace('l’existence', "l'existence"),
           'Le recensement séparé selon les codes de l’arrêté du 10 octobre 1974 n’est plus exigé.'),
    effect('obligation_removed', 'bdese-comptages-documentaires-prevention',
           'Suppression du nombre de déclarations de procédés, du comptage des plans spécifiques et des deux taux de réalisation supplémentaires.',
           'Nombre de déclarations de procédés susceptibles de provoquer une maladie, existence/nombre des plans spécifiques, taux de réalisation des programmes de sécurité et d’amélioration des conditions de travail.',
           'Ces quatre comptages ou ratios ne sont plus exigés par ce tableau ; maladies, risques, dépenses, formations et rapport/programme annuels autonomes restent accessibles.',
           'legal_duty', 'Existence et nombre de plans spécifiques de sécurité ;',
           'Le présent tableau n’impose ni taux distinct de réalisation du programme ni comptage des plans spécifiques de sécurité.'),
    effect('obligation_removed', 'bdese-tranche-temps-partiel-supprimee',
           'Suppression coordonnée de la tranche statistique de 20 à 30 heures aux deux emplacements du tableau.',
           'Distinction des temps partiels entre 20 et 30 heures et des autres formes, au 1° A f v et par sexe au 2° I A b.',
           'Effectifs à temps partiel et répartition femmes-hommes maintenus sans cette tranche ; aucun volume contractuel, minimum conventionnel ou droit au retour à temps plein n’est supprimé.',
           'legal_duty', '-entre 20 et 30 heures (33) ;',
           'Répartition des effectifs entre temps complet et temps partiel ; aucune tranche obligatoire de 20 à 30 heures n’est reconstituée ;'),
    effect('obligation_removed', 'bdese-statistiques-organisation-production',
           'Retrait du descriptif obligatoire d’expériences d’organisation, de son effectif associé et des statistiques supplémentaires de production.',
           'Présentation des expériences d’organisation avec nombre de salariés concernés ; évolution de productivité et utilisation des capacités si mesurables ; production globale en valeur et volume.',
           '1° A f ix, 1° B c, 7° F c et note 41 abrogés ; investissements, R&D, chiffre d’affaires, résultat et affectation maintenus. Les consultations sur des projets concrets gardent leur fondement.',
           'legal_duty', 'c) L’évolution de la productivité et le taux d’utilisation des capacités de production, lorsque ces éléments sont mesurables dans l’entreprise ;'.replace('L’évolution', "L'évolution").replace('d’utilisation', "d'utilisation").replace('l’entreprise', "l'entreprise"),
           'Aucun relevé, rapport ou registre de remplacement n’est imposé pour les indicateurs supprimés.'),
    effect('obligation_removed', 'bdese-decompte-reprise-redondant',
           'Suppression du sous-décompte d’arrêts et journées de maladie associé à un renvoi erroné au 3° de R4624-31.',
           'Décompte général maladie plus sous-décompte des « maladies » ayant donné lieu à examen de reprise selon le 3° de R4624-31, lequel vise les accidents du travail.',
           'Sous-décompte supprimé ; nombres généraux d’arrêts et journées, accidents, maladies professionnelles et examens médicaux conservés ; visites et dispenses autonomes inchangées.',
           'legal_duty', "-maladies ayant donné lieu à un examen de reprise du travail en application du 3° de l'article R. 4624-31 :",
           'Le décompte supplémentaire des arrêts et journées d’absence au titre des maladies ayant donné lieu à un examen de reprise n’est plus exigé.'),
    effect('obligation_removed', 'bdese-indicateurs-salariaux-supplementaires',
           'Suppression complète des quatre séries statistiques supplémentaires du 4° A a i à iv, au-delà du simple choix d’un indicateur du brouillon antérieur.',
           'Choix de deux indicateurs de montant dans un groupe, rapport de hiérarchie, total des dix rémunérations les plus élevées, deux pourcentages de mode de paiement et charge salariale globale ; notes 18 à 22, dont formule 19 ambiguë et grille d’au moins six tranches.',
           'i à iv et notes 18 à 22 abrogés ; frais de personnel, cotisations, salaire minimum, salaire moyen ou médian par sexe/catégorie, évolution salariale, tous les indicateurs d’égalité maintenus. Aucun calcul salarial de remplacement.',
           'legal_duty', "i-Montant des rémunérations (17) : Choix de deux indicateurs dans l'un des groupes suivants :",
           'i-Abrogé. Aucun choix ni cumul d’indicateurs supplémentaires de montant des rémunérations n’est exigé au titre du présent i.'),
    effect('obligation_removed', 'bdese-releves-relations-professionnelles',
           'Suppression des comptages annuels de crédits d’heures et réunions et maintien de la coupe des relevés de communication interne et de différends.',
           'Crédits d’heures et réunions annuels ; heures de réunions du personnel, systèmes d’accueil, information et entretiens ; relevé des différends et de leur solution.',
           'Plus de ces comptages ou relevés au 5° A ; composition, participation électorale, accords et bénéficiaires du congé d’éducation ouvrière maintenus ; droits syndicaux, rémunération et recours autonomes conservés.',
           'legal_duty', 'Volume global des crédits d’heures utilisés pendant l’année considérée ;'.replace('d’heures', "d'heures").replace('l’année', "l'année"),
           'Le volume annuel des crédits d’heures utilisés et le nombre annuel de réunions avec les représentants du personnel ou les délégués syndicaux ne font pas l’objet d’un comptage obligatoire au titre de cette rubrique.'),
    effect('obligation_removed', 'bdese-partenariats-limites-sous-traitance',
           'Restriction du recensement supplétif aux partenariats de sous-traitance correspondant au thème législatif.',
           'Tout partenariat de production ou d’acquisition de services/produits, sans distinction explicite de la sous-traitance.',
           'Deux sens de la sous-traitance conservés ; pas d’inventaire général des autres partenariats commerciaux. Les informations nécessaires à une consultation autonome restent dues.',
           'legal_duty', 'B-Partenariats conclus pour bénéficier des services ou des produits d’une autre entreprise ;'.replace('d’une', "d'une"),
           'Les autres partenariats commerciaux ne sont pas soumis à un recensement obligatoire au titre du présent 8°.'),
    effect('obligation_merged', 'bdese-reemploi-documents',
           'Mise à disposition unique de données exactes déjà disponibles, sans nouvelle saisie, copie ni rapport identique ; accès effectif et ventilations nécessaires maintenus.',
           'Liste des informations que la base doit comporter, sans dispense explicite de nouvelle saisie et de copies dans cet article. Le droit général de mise à disposition existe déjà à L2312-18 : il n’est pas présenté comme créé ici.',
           'Dispense réglementaire expresse de saisie, copie et relevé identiques, notamment entre thèmes ; pas de remplacement des indicateurs supprimés. Aucun gain chiffré attribué à cette seule explicitation.',
           'legal_duty', 'la base de données économiques, sociales et environnementales prévue à l’article L. 2312-18 comporte les informations prévues dans le tableau ci-dessous.'.replace('l’article', "l'article"),
           'dispense de nouvelle saisie, de copie et de relevé distinct contenant les mêmes données.'),
    effect('relief_preserved', 'bdese-preservation-avantages-sociaux-fiscaux',
           'Conservation des avantages auxquels les informations du tableau se rapportent, pour les situations antérieures et les futurs bénéficiaires éligibles, sans nouveau justificatif.',
           'Information sur aides, crédits, exonérations, compléments salariaux de congé, formation, épargne salariale, prévoyance et activités sociales ; cet article n’est pas leur fait générateur ni leur régime d’octroi.',
           'Ces droits et les rubriques qui en rendent compte demeurent ; les indicateurs supprimés ne deviennent pas des conditions de bénéfice. Aucun élargissement fiscal général ni suppression de prestation n’est revendiqué.',
           'other', 'C-Exonérations et réductions de cotisations sociales ;',
           'Ces avantages restent ouverts aux situations futures éligibles, y compris aux emplois de même objet relevant du contrat unique, dans les conditions des dispositions qui les régissent.'),
    effect('coordination', 'contrat-unique-duree-indeterminee',
           'Coordination statistique avec l’absence de nouveaux CDD ; les fins de mission, formation ou aide sont distinctes d’une rupture du contrat.',
           'Rubriques CDI/CDD, fins de CDD, contrats temporaires et apprentissage sans distinction prospective liée à la réforme.',
           'Données des anciens contrats et des périodes historiques maintenues ; aucune nouvelle conclusion ou renouvellement de CDD autorisé ; nouveaux emplois privés à durée indéterminée. Ce n’est pas une seconde abolition du régime.',
           'regime', "Nombre de fins de contrats de travail à durée déterminée (I) ;",
           'Elles ne permettent ni nouvelle conclusion ni renouvellement après cette entrée en vigueur.',
           conditions='Contrats privés conclus à compter de l’entrée en vigueur de la loi instituant le contrat unique ; anciens contrats et données historiques à leur régime propre. Préavis, indemnités, ancienneté et procédures spéciales non redéfinis par cet article.'),
]

removed = [
    '1° A a i et notes 2-3 : retrait du décompte de l’effectif permanent et de l’effectif mensuel moyen, leurs définitions et leur calcul n’étant plus requis par ce tableau.',
    '1° A a ii : suppression du calcul de durée moyenne des contrats de travail temporaire, sans imposer une durée moyenne des missions en remplacement.',
    '1° A b i-ii : suppression des décomptes isolés des embauches de moins de vingt-cinq ans et des mutations entre établissements.',
    '1° A b iii et note 11 : suppression du relevé autonome de promotions, remplacé par la réutilisation des données plus détaillées du 2° I B a déjà exigées.',
    '1° A d : maintien de la suppression du second relevé d’évolution des stagiaires, réuni au 1° A a ii avec leur nombre.',
    '1° A a i, 1° A f i et 5° A a : maintien de la suppression des ventilations par nationalité et du relevé de l’appartenance syndicale des personnes.',
    'Notes I, II et 4 : maintien de la suppression des minima de trois/quatre ou cinq/six postes de qualification et de quatre catégories d’âge ; moins de vingt-cinq ans et sexe conservés.',
    '1° A e i : suppression du pourcentage de masse salariale consacré à la formation et de la ventilation par mode de financement ; montant total, bénéficiaires et heures maintenus.',
    '1° A f i : suppression des deux calculs supplémentaires des taux d’accidents avec facteurs × 106 et × 10 ³ ; premiers rapports simples de la source conservés.',
    '1° A f ii et note 28, également utilisés au 2° I D : suppression du tableau imposant les six groupes de codes matériels de l’arrêté du 10 octobre 1974 et du recodage correspondant ; répartition existante maintenue.',
    '1° A f iii et note 29 : retrait du décompte des déclarations de procédés susceptibles de provoquer des maladies professionnelles ; aucune suppression des déclarations elles-mêmes.',
    '1° A f iv et x : retrait des taux distincts de réalisation des programmes de sécurité et d’amélioration des conditions de travail et du comptage des plans spécifiques.',
    '1° A f v et 2° I A b : suppression de la ventilation supplémentaire dans la tranche de 20 à 30 heures ; le décompte des temps partiels et les données par sexe demeurent.',
    '1° A f ix et note 41 : suppression du descriptif obligatoire des expériences de transformation de l’organisation du travail et de leur nombre de salariés concernés.',
    '1° B c et 7° F c : suppression des indicateurs supplémentaires de productivité, utilisation des capacités et production globale en valeur et volume.',
    '2° I D : retrait du sous-décompte d’arrêts et journées d’absence attribué aux maladies avec examen de reprise sous le renvoi erroné au 3° de R4624-31 ; autres données de maladie et suivi médical maintenues.',
    '4° A a i et notes 18-20 : suppression du choix et du cumul d’indicateurs salariaux supplémentaires, de la base statistique de décembre à 35 heures, de la formule ambiguë et de la grille minimale.',
    '4° A a ii et note 21 : suppression des rapports supplémentaires de hiérarchie salariale et du montant global des dix rémunérations les plus élevées ; indicateurs d’égalité du 2° conservés.',
    '4° A a iii et note 22 : suppression des pourcentages de salariés payés au rendement et d’ouvriers/employés payés au mois sur horaire affiché.',
    '4° A a iv : retrait de la seconde présentation de charge salariale globale, déjà comprise dans les frais de personnel du même a.',
    '5° A a : suppression du comptage annuel des crédits d’heures utilisés et des réunions avec les représentants ou délégués syndicaux ; droits et actes de représentation maintenus.',
    '5° A b-c et notes 46-48 : maintien de la suppression des relevés de communication interne, périodicité des entretiens, différends et solutions.',
    '8° A-B : suppression du recensement général des partenariats commerciaux autres que la sous-traitance ; maintien des deux sens de la sous-traitance.',
    'Ensemble du tableau : dispense expresse de transcription, copie ou relevé distinct de données identiques déjà légalement accessibles ; aucune suppression de ventilation maintenue ni d’accès effectif.',
]

reference_assessments = {
    'L1234-1': 'Cible lue dans ses versions officielle et proposée. Aucun renvoi direct à L1234-1 ne figure dans le tableau : la pertinence tient aux statistiques de départs. La vue proposée substitue quinze jours calendaires au barème lié à l’ancienneté pour les contrats nouveaux, conserve le barème antérieur et distingue les procédures collectives et autorisations. Le tableau ne calcule aucun préavis et n’en fixe ni date de notification ni point de départ ; la règle de départ au lendemain de présentation/réception de la notification écrite demeure celle de L1234-3 identifié par coordination.json, dont le texte n’est pas fourni parmi ces cibles. Une durée moyenne de mission n’est pas utilisée comme préavis ; le décompte de départs ne transforme pas une procédure collective en procédure de quinze jours.',
    'L1221-2': 'Les deux alinéas officiels autorisent encore les CDD dans les cas du titre IV ; la proposition fournie exclut leur nouvelle conclusion et leur renouvellement et distingue emploi et mission/formation. Les 1° A a-b, 2° I A a-d et la disposition finale du présent article rattachent explicitement les CDD aux contrats antérieurs et aux périodes historiques. Apprentis, insertion et intérim ne servent pas à rétablir un terme de l’emploi. Aucune ancienneté n’est réinitialisée par une phase pédagogique ou une mission ; aucune aide future de même objet n’est réservée aux seuls anciens CDD. La source et la proposition cibles sont distinguées, sans présenter le contrat unique comme du droit en vigueur.',
    'L1234-9': 'La source entière et sa note de 2017 sont lues : droit antérieur à huit mois, sauf faute grave. La vue proposée fixe, pour le contrat unique, le seuil d’un an au terme effectif avec préavis exécuté ou non inclus sous réserve de fin d’essai, 0,20 mois par année totale, mois complets au prorata et plafond de six mois ; elle conserve l’exception de faute grave et les droits conventionnels ou spéciaux. Elle distingue la composante acquise des anciens contrats et ne retire pas la première année après atteinte du seuil. R2312-9 ne comporte pas de renvoi direct à cet article et n’institue aucun relevé d’indemnité de rupture : ses nombres de départs ne changent ni l’initiative patronale exigée, ni le seuil, ni le salaire de référence, ni la notification ou les réparations d’illégalité. Aucun de ces paramètres n’est réécrit indirectement.',
    'R2312-8': 'Source et proposition de la cible lues en entier, tableau et note inclus. Le deuxième alinéa de R2312-9 vise uniquement e et f du A du 1°, et non le a relatif aux effectifs ni le 8° relatif aux partenariats. Le e proposé conserve orientations, contrôles, bilans agrégés de formation et congés, abondements et entretiens, alternance et CPF ; le f conserve les données de temps partiel et le programme annuel de prévention, avec les protections de même objet des salariés en contrat unique. Le renvoi est maintenu à ces subdivisions exactes : retirer le détail supplémentaire du financement au tableau R2312-9 ne supprime pas ces données. Aucun seuil d’ancienneté ou de notification de rupture ne résulte de ces e/f ; durée de formation, mission ou aide et durée de l’emploi restent distinctes. Les conditions propres aux aides futures et les anciens contrats restent à leur champ. La proposition de R2312-8, sans IS annuel rétabli ni nouveaux CDD, n’est pas assimilée au droit officiel.',
}
checks = []
for key in references['requirements'][source['code_id']+'|'+source['source_id']]:
    target = references['targets'][key]
    checks.append({'target_key': key, 'view_sha256': target['view_sha256'],
                   'assessment': reference_assessments[target['number']]})

answer = {
    **{k: source[k] for k in ['code_id','source_id','source_sha256','number']},
    'proposed_xml': proposed,
    'reason': 'Seconde passe de fond sur la source officielle entière, distincte du seul toilettage du précédent brouillon. Le tableau supplétif reste opératoire pour les entreprises d’au moins trois cents salariés, avec ses dix thèmes et ses emplacements. Les coupes antérieures compatibles sont conservées ; s’y ajoutent le retrait des agrégats d’effectif permanent et moyen, de la durée moyenne des missions, de deux comptages d’embauches/mutations, des détails de financement de formation, des doubles taux d’accidents et recodages de 1974, des comptages de documents de prévention, de la tranche statistique 20-30 heures, des expériences d’organisation et statistiques de production. Les quatre séries salariales supplémentaires sont supprimées entièrement plutôt que de laisser le choix d’un seul indicateur. Le sous-décompte médical fondé sur un renvoi erroné et les comptages de réunions/crédits d’heures sont retirés ; les partenariats sont limités à la sous-traitance. Ces obligations de présentation n’ont pas de fonction essentielle distincte démontrée après maintien des données d’emploi, de rémunération effective, d’égalité, de risque et des consultations autonomes. À droit constant demeurent les garanties, conditions et chiffres des informations maintenues, les aides, la confidentialité et les droits d’accès. Les informations communes sont produites une seule fois. Le contrat unique et les transitions sont coordonnés sans modifier ici le préavis ou les indemnités. Aucun impôt, cotisation ou prestation n’est supprimé par cet article purement informatif ; aucune économie nationale chiffrée n’est alléguée.',
    'review_notes': 'Lecture intégrale des 40 461 caractères de source_xml, des 70 lignes du tableau et des notes I, II et 1 à 52 ; source_notes_xml est vide. Aucun source_companions ni sru_context n’est présent. Le previous_draft de 36 835 caractères a été lu entièrement ; le champ proposed_xml supérieur lui est identique après décodage des entités HTML. La proposition conserve les 70 lignes, les lettres, les subdivisions et les emplacements des notes, en marquant les prescriptions retirées comme abrogées. Les passages maintenus ont été comparés par rubrique à la source ; le 10° et ses six lignes de données environnementales n’ont subi aucune coupe de fond. Les nombres maintenus comprennent notamment trois cents salariés, 31 décembre, congés de plus de six mois, dix plus hautes rémunérations au seul indicateur d’égalité, deux niveaux de comparaison salariale, quatre semaines, une semaine, trente secondes/quinze ou trente actions/900 heures et cinq ou trente degrés/900 heures. Le retrait des séries salariales supprime leur ancienne base statistique de 35 heures, sans changer les seuils des heures supplémentaires. Retirer la tranche 20-30 heures ne modifie ni durée contractuelle ni plancher spécial ni avantage conventionnel. Les cibles requises sont toutes couvertes par reference_checks avec leurs empreintes exactes ; leurs propositions sont des projets, pas le droit en vigueur. Sources publiques complémentaires lues dans le corpus fourni : L2312-18, L2312-21, L2312-36, R2312-10, L2312-27, L2312-28, L2312-30, R2312-21, D4163-2, R4431-2 avec sa note, R4624-31 avec sa note de 2026, R4223-13 à 15, L3123-1, L5212-5 et R2242-2, notes comprises. L2312-18, dans sa version de 2025, impose notamment les indicateurs d’égalité et le bilan d’actions de formation après entretiens/reconversion : ils restent dus sur leur fondement autonome, même s’ils ne sont pas tous détaillés dans le tableau source. L2312-36 et R2312-10 maintiennent les deux années antérieures, l’année en cours et les perspectives des trois années suivantes ; L2312-28/30 maintiennent le bilan social et les informations utiles. Le rapport annuel et le programme de prévention de L2312-27 demeurent, avec les obligations autonomes qui s’y attachent ; les nouveaux renvois explicites à L2312-27, L2312-36 et R2312-10 ne figurent pas comme cibles dans reference-targets.json, mais leurs textes entiers ont été lus dans le corpus. R2312-21 conserve une présentation mensuelle dans l’information trimestrielle : sa proposition existante a été lue, elle n’est pas modifiée ni comptée comme article traité dans ce lot. Les suppressions de moyennes et relevés ici n’emportent donc pas disparition de toutes les données sous-jacentes ni preuve d’un gain administratif chiffré. Incohérence de la source résolue par une coupe explicite : le 2° I D rattache des maladies au 3° de R4624-31, qui vise au moins trente jours d’accident du travail ; le 4° vise maladie/accident non professionnel d’au moins soixante jours. Le sous-décompte est retiré, sans réattribuer silencieusement le renvoi ni supprimer la visite ou la dispense introduite en 2026 après visite de préreprise dans les trente jours et absence de besoin d’aménagement, sous les réserves de cet article. Les nombres généraux d’arrêts, journées et examens demeurent. Les doubles expressions des taux d’accidents sont supprimées en conservant les rapports simples de la source, sans interpréter × 106 comme une puissance ; la formule 19 ambiguë disparaît avec sa série, sans formule de remplacement. Autres incohérences ou lacunes préexistantes signalées : licenciements économiques incluant retraite/préretraite ; exclusion générale des congés en note 15 en regard des lignes maternité/congés autorisés ; formulation statistique « plus de 80 à 85 db », conservée sans fusionner les seuils distincts 80/85/87 dB(A) de R4431-2. Les renvois externes de la source à L225-102/L225-102-1 et R225-105 du code de commerce, au rapport fiscal L232-6 et aux textes environnementaux conservent leur objet source ; leurs concordances et changements de calendrier extérieurs au corpus fourni ne sont pas affirmés vérifiés ni remplacés par des références inventées. Une coordination des textes de commerce et des obligations européennes de durabilité reste à documenter hors des cinq codes ; aucune dispense européenne n’est déduite de cette rédaction. L1234-3 est identifié dans coordination.json pour le point de départ du préavis, sans nouveau renvoi normatif ni prétendue lecture de son texte absent des quatre cibles. Préavis et indemnités ne sont pas réglementés par R2312-9 : ni le seuil d’un an au terme effectif préavis inclus, ni 0,20 mois sur toute l’ancienneté avec fractions en mois complets et plafond de six mois, ni anciens droits ou indemnités spéciales ne sont altérés. L’information fiscale demeure distincte de l’exigibilité de l’IS à la distribution, des anciennes créances et de la suppression programmée de CVAE ; aucun effet fiscal de ces réformes n’est compté une seconde fois ici. Les modèles de protection complémentaire supprimés et les transmissions collectives déjà retirées ne sont pas rétablis. Les allègements s’appliquent aux communications futures, même sur périodes anciennes, sans réfection des documents déjà communiqués ; droit répressif plus doux réservé. Ce travail ne constitue ni relecture par un juriste ni audit indépendant.',
    'status': 'rewrite_draft',
    'change_type': 'normative_reduction',
    'reform_policy_id': 'editorial_direction_2026_10_19',
    'removed_provisions': removed,
    'benefit_review': 'R2312-9 n’institue directement ni taxe ni exonération : il oblige à informer le CSE sur des droits et avantages fondés ailleurs. L’examen intégral distingue ces droits de leur présentation. Sont conservés au 7° A-D les aides publiques de l’Union, de l’État, des collectivités et organismes compétents, les réductions d’impôt, exonérations/réductions de cotisations et crédits d’impôt, avec leur objet et leur emploi ; le crédit d’impôt famille et les dépenses éligibles restent au 2° II B c. Aucune de ces rubriques ne rétablit un IS annuel sur bénéfices conservés, une CVAE supprimée ou une condition fiscale de remplacement. Au 1° A b iv, les indemnités de chômage partiel et intempéries restent distinguées des heures non indemnisées ; supprimer des statistiques d’embauche n’écarte aucune aide à l’insertion, à l’alternance ou à l’emploi de personnes handicapées. Les congés de formation rémunérés/non rémunérés, refus, heures de formation, abondements, CPF et protections de même objet du renvoi R2312-8 e/f restent accessibles. La durée d’apprentissage ou d’accompagnement ne met pas fin au contrat nouveau. Les compléments salariaux de maternité, paternité et adoption, congés familiaux/parentaux, repos compensateurs, congés annuels et jours fériés, temps partiel choisi et retour au temps plein restent dans leurs rubriques et à leurs conditions propres. Les congés de plus de six mois restent observés ; aucune exclusion d’indemnité ou de salaire n’est tirée d’un comptage supprimé. Au 4° B-C et 6° B sont maintenus participation, intéressement, réserve, actionnariat salarié, dividendes, primes, avantages en nature, garanties de prévoyance et retraite complémentaire, niveaux de garantie par catégorie ; au 5° B demeurent les prestations complémentaires maladie/décès/vieillesse et concours logement, transport, restauration, loisirs, vacances, équipements et financement du CSE. Les congés d’éducation ouvrière et leurs bénéficiaires restent au 5° A a. Les retraites/préretraites et systèmes légaux/conventionnels restent distingués sans changement de leurs droits ni transformation de cotisations en baisse fictive. Les dispenses favorables de présentation sont préservées : confidentialité de l’indicateur salarial par coefficient en petit effectif, faculté d’employer les catégories pertinentes et données connues de travailleurs extérieurs, stages de plus d’une semaine seulement, départs d’essai seulement s’ils sont comptés dans les départs, choix des unités d’absence et tranches maladie, substitution de la somme des heures travaillées à l’horaire moyen, dernière période de référence pour congés, indicateurs de volume d’émissions seulement disponibles et bilans seulement dus par les entreprises assujetties. Les conditions propres à ces facilités ne sont pas durcies. L’accès aux données de santé reste soumis aux secrets ; retirer le sous-décompte de reprise ne retire aucune visite utile ni dispense favorable de R4624-31. Les clauses finales protègent expressément les avantages antérieurs et les situations futures éligibles, y compris de même objet en contrat unique, sans indicateur ou attestation de remplacement comme condition de bénéfice. Aucun avantage n’est limité aux anciens CDD ; aucune aide, garantie ou exonération n’est déclarée éteinte au seul motif du retrait d’un relevé. Les statistiques de production, modes de rémunération, nationalité et comptage de documents supprimés sont des obligations d’information, non des prestations ou exonérations à retirer. Le maintien des autres informations de santé et d’égalité est nécessaire pour la prévention et le contrôle des discriminations ; leurs droits ne sont pas remplacés par un simple énoncé d’intention.',
    'reference_checks': checks,
    'substantive_impact': {
        'version': 1,
        'classification': 'material_reduction',
        'assessment': 'Comparée à la source officielle entière, la proposition retire effectivement plusieurs séries statistiques et comptages, dont les quatre séries salariales supplémentaires, les nomenclatures imposées, les ratios doublonnés et l’inventaire de partenariats hors sous-traitance. Elle conserve les coupes du brouillon et réalise des suppressions supplémentaires identifiées, sans retirer les protections d’égalité, santé, formation ou avantages sociaux/fiscaux. La coordination du contrat unique n’est pas comptée comme seconde abolition du CDD ; cet article ne réduit aucun taux ni assiette de prélèvement.',
        'scope_limitations': 'Allègement limité au contenu supplétif de R2312-9 dans les entreprises d’au moins trois cents salariés sans accord pertinent. Les accords, obligations autonomes, bilan social, informations mensuelles/trimestrielles et droit de l’Union ne sont pas abrogés. Les mises à disposition futures bénéficient de la coupe même pour une période ancienne ; anciens manquements et recours sont réservés. Les économies de temps ou de coût, le solde net de l’ensemble des codes et les concordances du code de commerce ne sont pas démontrés. Aucun rendement fiscal ni solde public national n’est calculé.',
        'new_burdens_review': 'Aucune charge nouvelle n’est identifiée : ni nouveau registre, portail, donnée, rapport, attestation, agrément, délai ni condition d’accès à un avantage. La réutilisation des documents, la répartition matérielle existante des accidents et les renvois entre rubriques portent sur des informations déjà requises ; elles évitent saisies et recodages et n’imposent aucun outil technique nouveau. Les réserves d’accès effectif, d’actualité, de confidentialité et de droits autonomes correspondent aux exigences déjà applicables, sans formalité de certification ajoutée. Le solde quantitatif de complexité de tous les codes reste inconnu.',
        'effects': effects,
    },
}
Path('answer.json').write_text(json.dumps([answer], ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'output_file':'answer.json','article_count':1,'proposed_characters':len(proposed),'effects':len(effects)}, ensure_ascii=False))
