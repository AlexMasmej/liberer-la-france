"""Authored reconstruction of the two French CEM tables, with explicit provenance."""
from pathlib import Path
import hashlib, html, json, re

ROOT = Path(__file__).resolve().parents[3]
A = ROOT / 'legal-rewrite/attachments'
SOURCES = json.loads((A / 'rayonnements-optiques/source-reserved-snapshot.json').read_text())

def p(value):
    return '<p>' + value + '</p>'

def table(headers, rows):
    return '<table><thead><tr>' + ''.join('<th>' + x + '</th>' for x in headers) + '</tr></thead><tbody>' + ''.join('<tr>' + ''.join('<td>' + x + '</td>' for x in row) + '</tr>' for row in rows) + '</tbody></table>'

def text(value):
    return ' '.join(html.unescape(re.sub('<[^>]*>', ' ', value)).split())

def document(name, url, label):
    path = A / 'champs-electromagnetiques' / name
    return dict(path=str(path.relative_to(A)), sha256=hashlib.sha256(path.read_bytes()).hexdigest(), url=url, label=label)

jo = document('jo-20160806-texte27-copie-nextinpact.pdf', 'https://cdn2.nextinpact.com/medias/joe_20160806_0182_0027.pdf', 'Copie du JO du 6 août 2016, texte 27, hébergée par Next INpact ; signature non présente dans le fichier')
inrs = document('inrs-ed4204.pdf', 'https://www.inrs.fr/dam/inrs/CataloguePapier/ED/TI-ED-4204.pdf', 'INRS, ED 4204, octobre 2018, tableaux et explications, pages 2 à 4')
ue = document('directive-2013-35-ue-fr.pdf', 'https://op.europa.eu/o/opportal-service/download-handler?identifier=52fb4c35-e08c-11e2-9165-01aa75ed71a1&format=pdfa1a&language=fr&productionSystem=cellar&part=', 'Office des publications UE : directive 2013/35/UE, édition initiale ; erreurs A3 corrigées par rectificatif du 28 décembre 2013, non reprises ici')

def save(batch, ident, body, transcriptions, reason, review, docs):
    a = next(x for x in SOURCES if x['source_id'] == ident)
    row = {k:a[k] for k in ['code_id', 'source_id', 'source_sha256', 'number']}
    row.update(proposed_xml=body, reason=reason, review_notes=review, status='rewrite_draft')
    Path(__file__).with_name(batch + '.json').write_text(json.dumps([row], ensure_ascii=False, indent=2) + '\n')
    manifest = dict(code_id=a['code_id'], source_id=ident, expected_markers=len(transcriptions), documents=docs, media=[], transcriptions=[dict(marker=i+1, text=text(v), verified_visually=True, label='Tableau et notes entièrement reconstitués ; rédaction proposée, non transcription diplomatique') for i,v in enumerate(transcriptions)], documentary_recovery_complete=True, authenticated_jo_crosscheck_complete=False, provenance_notes=review)
    (A / 'records' / ('travail-' + a['number'].lower() + '.json')).write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(a['number'], len(body), 'caractères ;', len(transcriptions), 'tableaux et notes récupérés')

# R4453-3 : reproduction sémantique complète de la matrice française et de ses sept notes.
# Les bornes imprimées du JO français (dont le double 400 Hz) restent explicites.
v = 'V·m<sup>−1</sup>'
wkg = 'W·kg<sup>−1</sup>'
w = 'W·m<sup>−2</sup>'
headers3 = ['Fréquence f', 'Effets biophysiques directs', 'Effets sensoriels : tête', 'Effets sensoriels : membres', 'Effets sur la santé : corps entier', 'Effets sur la santé : tête et tronc', 'Effets sur la santé : membres']
rows3 = [
 ['0 Hz ≤ f &lt; 1 Hz (2)', 'Non thermiques', '2 T', '8 T', '8 T', '—', '—'],
 ['1 Hz ≤ f &lt; 10 Hz (3)', 'Non thermiques', '0,7/f ' + v, '—', '1,1 ' + v, '—', '—'],
 ['10 Hz ≤ f &lt; 25 Hz (3)', 'Non thermiques', '0,07 ' + v, '—', '1,1 ' + v, '—', '—'],
 ['25 Hz ≤ f ≤ 400 Hz (3)', 'Non thermiques', '0,0028 f ' + v, '—', '1,1 ' + v, '—', '—'],
 ['400 Hz ≤ f &lt; 3 kHz (3)', 'Non thermiques', '—', '—', '1,1 ' + v, '—', '—'],
 ['3 kHz ≤ f &lt; 100 kHz (3)', 'Non thermiques', '—', '—', '3,8 × 10<sup>−4</sup> f ' + v, '—', '—'],
 ['100 kHz ≤ f &lt; 10 MHz (3) (4) (5)', 'Non thermiques et thermiques', '—', '—', '3,8 × 10<sup>−4</sup> f ' + v + ' (non thermiques) ; 0,4 ' + wkg + ' (thermiques)', '10 ' + wkg, '20 ' + wkg],
 ['10 MHz ≤ f &lt; 0,3 GHz (4)', 'Thermiques', '—', '—', '0,4 ' + wkg, '10 ' + wkg, '20 ' + wkg],
 ['0,3 GHz ≤ f &lt; 6 GHz (4) (6)', 'Thermiques', '10 mJ·kg<sup>−1</sup>', '—', '0,4 ' + wkg, '10 ' + wkg, '20 ' + wkg],
 ['6 GHz ≤ f ≤ 300 GHz (7)', 'Thermiques', '—', '—', '50 ' + w, '—', '—'],
]
notes3 = [
 '(1) f est exprimée en hertz.',
 '(2) De 0 à 1 Hz, les limites portent sur l’induction magnétique externe, en teslas.',
 '(3) De 1 Hz à 10 MHz, les limites portent sur la valeur crête spatiale du champ électrique interne, en volts par mètre.',
 '(4) De 100 kHz à 6 GHz, les limites relatives à la santé portent sur l’énergie moyenne absorbée par le corps entier ou localement par la tête, le tronc ou les membres. Elles sont exprimées en débit d’absorption spécifique, en watts par kilogramme.',
 '(5) De 100 kHz à 10 MHz, les effets thermiques et non thermiques se produisent simultanément : les limites des deux types d’effets sont prises en compte.',
 '(6) De 0,3 à 6 GHz, la limite sensorielle porte sur l’énergie absorbée par unité de masse de tissus biologiques. Elle est exprimée en absorption spécifique, en joules par kilogramme.',
 '(7) De 6 à 300 GHz, la limite relative à la santé porte sur la densité de puissance, en watts par mètre carré.',
]
restored3 = table(headers3, rows3) + ''.join(map(p, notes3))
body3 = p('L’exposition professionnelle aux champs électromagnétiques respecte chacune des valeurs limites applicables dans le tableau ci-dessous. Les colonnes distinguent les effets sensoriels, les effets sur la santé et les parties du corps exposées.') + restored3
review3 = 'Source française et notes lues. La matrice et ses sept notes ont été contrôlées visuellement sur la page 2 de la copie du JO du 6 août 2016, texte 27, PDF portant les métadonnées DILA mais hébergé chez Next INpact et sans signature PDF. Les seuils non thermiques sont confrontés à INRS ED 4204 (2018) et au document médical Sometrav (2017). Le tableau français prévaut sur la directive initiale, dont A3 présente deux erreurs corrigées en décembre 2013 : 0,07 constant et 0,0028 f sont ici correctement restitués, et non les fractions erronées du PDF initial. Le double rattachement imprimé de 400 Hz et l’inclusion de 300 GHz dans le tableau français de 2016 sont conservés. Aucune durée de moyennage, restriction ou règle européenne non reproduite dans le tableau français n’est ajoutée. Aucun seuil supprimé ou réduit. Le document français a été confronté à une copie du JO, pas à un téléchargement authentifié actuel ; validation juridique et contrôle d’authenticité restent à faire.'
save('003', 'LEGIARTI000032980606', body3, [restored3], 'Réécrit la règle d’exposition et déplie entièrement les cellules fusionnées du tableau français pour rendre chaque fréquence et chaque partie du corps lisibles, sans modifier les seuils ni les sept notes.', review3, [jo, inrs, ue])

# R4453-4 : les deux tableaux français sont dépliés sans modifier leurs domaines.
headers4 = ['Fréquence f', 'Effets', 'Champ électrique E efficace (2) (3)', 'Champ magnétique B efficace : VA basse (4) (6)', 'Champ magnétique B efficace : VA haute (4) (6)', 'Champ magnétique localisé aux membres (4)', 'Courant induit dans une extrémité I efficace (5)']
bl = ['2 × 10<sup>5</sup>/f<sup>2</sup>', '2,5 × 10<sup>4</sup>/f', '10<sup>3</sup>', '10<sup>3</sup>', '3 × 10<sup>5</sup>/f', '3 × 10<sup>5</sup>/f', '3 × 10<sup>5</sup>/f', '10<sup>2</sup>']
bands = ['1 Hz ≤ f &lt; 8 Hz', '8 Hz ≤ f &lt; 25 Hz', '25 Hz ≤ f &lt; 50 Hz', '50 Hz ≤ f &lt; 300 Hz', '300 Hz ≤ f &lt; 1,64 kHz', '1,64 kHz ≤ f &lt; 2,5 kHz', '2,5 kHz ≤ f &lt; 3 kHz', '3 kHz ≤ f &lt; 100 kHz']
electric = ['2 × 10<sup>4</sup>']*3 + ['10<sup>6</sup>/f']*2 + ['6,1 × 10<sup>2</sup>']*3
rows4 = []
for i, band in enumerate(bands):
    high = '3 × 10<sup>5</sup>/f' if i < 7 else '10<sup>2</sup>'
    member = '9 × 10<sup>5</sup>/f' if i < 7 else '3 × 10<sup>2</sup>'
    rows4.append([band, 'Non thermiques', electric[i]+' '+v, bl[i]+' µT', high+' µT', member+' µT', '—'])
both_b = '10<sup>2</sup> µT (non thermiques) ; 2 × 10<sup>6</sup>/f µT (thermiques)'
rows4 += [
 ['100 kHz ≤ f &lt; 1 MHz (7)', 'Non thermiques et thermiques', '6,1 × 10<sup>2</sup> '+v+' (les deux types d’effets)', both_b, both_b, '3 × 10<sup>2</sup> µT (non thermiques)', '—'],
 ['1 MHz ≤ f &lt; 10 MHz (7)', 'Non thermiques et thermiques', '6,1 × 10<sup>2</sup> '+v+' (non thermiques) ; 6,1 × 10<sup>8</sup>/f '+v+' (thermiques)', both_b, both_b, '3 × 10<sup>2</sup> µT (non thermiques)', '—'],
 ['10 MHz ≤ f &lt; 110 MHz', 'Thermiques', '61 '+v, '0,2 µT', '0,2 µT', '—', '100 mA'],
 ['110 MHz ≤ f &lt; 400 MHz', 'Thermiques', '61 '+v, '0,2 µT', '0,2 µT', '—', '—'],
 ['400 MHz ≤ f &lt; 2 GHz', 'Thermiques', '3 × 10<sup>−3</sup> f<sup>1/2</sup> '+v, '10<sup>−5</sup> f<sup>1/2</sup> µT', '10<sup>−5</sup> f<sup>1/2</sup> µT', '—', '—'],
 ['2 GHz ≤ f &lt; 300 GHz', 'Thermiques', '1,4 × 10<sup>2</sup> '+v, '4,5 × 10<sup>−1</sup> µT', '4,5 × 10<sup>−1</sup> µT', '—', '—'],
]
notes4 = [
 '(1) f est exprimée en hertz.',
 '(2) Les valeurs d’action du champ électrique sont des intensités de champ électrique, en volts par mètre.',
 '(3) De 1 à 400 Hz, pour le champ électrique, le respect de la valeur d’action permet de respecter les limites sensorielles et sanitaires de l’article R. 4453-3.',
 '(4) Les valeurs d’action du champ magnétique sont des inductions magnétiques, en microteslas.',
 '(5) La valeur d’action des courants induits est exprimée en milliampères.',
 '(6) De 1 à 400 Hz, pour le champ magnétique, la valeur d’action basse permet de respecter les limites sensorielles pour une exposition localisée de la tête. La valeur d’action haute permet de respecter les limites sanitaires de l’article R. 4453-3.',
 '(7) De 100 kHz à 10 MHz, les effets thermiques et non thermiques des champs électriques et magnétiques se produisent simultanément : les valeurs d’action des deux types d’effets et des deux types de champs sont prises en compte.',
]
restored4a = table(headers4, rows4) + ''.join(map(p, notes4))
headers4b = ['Fréquence f (1)', 'Interférences avec les dispositifs actifs implantés : induction statique (2)', 'Attraction et projection dans le champ périphérique d’une source intense (&gt; 100 mT) : induction statique (2)', 'Limitation des décharges d’étincelles : champ électrique efficace (3)', 'Courant de contact d’état stable (4)']
rows4b = [
 ['0 Hz ≤ f &lt; 1 Hz', '0,5 mT', '3 mT', '—', '1 mA'],
 ['1 Hz ≤ f &lt; 25 Hz', '—', '—', '2 × 10<sup>4</sup> '+v, '1 mA'],
 ['25 Hz ≤ f &lt; 2,5 kHz', '—', '—', '5 × 10<sup>5</sup>/f '+v, '1 mA'],
 ['2,5 kHz ≤ f &lt; 3 kHz', '—', '—', '5 × 10<sup>5</sup>/f '+v, '0,4 f mA'],
 ['3 kHz ≤ f &lt; 100 kHz', '—', '—', '1,7 × 10<sup>2</sup> '+v, '0,4 f mA'],
 ['100 kHz ≤ f &lt; 10 MHz', '—', '—', '1,7 × 10<sup>2</sup> '+v, '40 mA'],
 ['10 MHz ≤ f ≤ 110 MHz', '—', '—', '—', '40 mA'],
]
notes4b = [
 '(1) f est exprimée en hertz. Pour le seul calcul de la valeur d’action du courant de contact entre 2,5 et 100 kHz, f est exprimée en kilohertz.',
 '(2) Les valeurs d’action du champ magnétique statique sont des inductions magnétiques, en milliteslas.',
 '(3) Les valeurs d’action limitant les décharges d’étincelles sont des intensités de champ électrique, en volts par mètre.',
 '(4) Les valeurs d’action des courants de contact sont exprimées en milliampères.',
]
restored4b = table(headers4b, rows4b) + ''.join(map(p, notes4b))
body4 = p('Les niveaux qui déclenchent les actions de prévention prévues à la section 5 du présent chapitre sont fixés par les deux tableaux suivants. Chaque niveau est appliqué au type d’exposition et au risque indiqués dans sa colonne.') + p('1° Effets biophysiques directs des champs électromagnétiques :') + restored4a + p('2° Certains effets indirects des champs électromagnétiques :') + restored4b
review4 = 'Source française et notes lues. Les deux tableaux absents du XML sont reconstruits intégralement : 14 bandes directes et sept notes ; sept bandes indirectes et quatre notes. Vérification visuelle de la page 3 de la copie du JO du 6 août 2016 (Next INpact, non signée), puis confrontation des valeurs au document INRS ED 4204 d’octobre 2018, pages 2 à 4, postérieur au rectificatif du 8 avril 2017. Le rectificatif est identifié sur Légifrance, NOR ETST1611714Z, mais son fac-similé n’a pas été récupéré ; la concordance graphique exacte avec lui reste à vérifier. Les deux renvois des notes directes (3) et (6) sont expressément actualisés vers R. 4453-3 conformément à l’article 2 du décret 2021-1091, texte officiel consulté sur Légifrance (JORFARTI000043947126). Les valeurs sont celles du tableau français, et non une substitution de toutes les règles européennes : pour le courant de contact, f passe en kilohertz de 2,5 à 100 kHz ; les deux types d’effets et de champs restent cumulatifs de 100 kHz à 10 MHz. La borne supérieure française f < 300 GHz du tableau direct est conservée même si INRS présente ailleurs ≤ 300 GHz. Les champs magnétiques thermiques communs aux colonnes basse et haute sont répétés, sans créer de seuil distinct. Aucune réduction de protection. Récupération documentaire complète, confrontation au fac-similé français authentifié actuel et validation juridique encore requises.'
save('004', 'LEGIARTI000043948605', body4, [restored4a, restored4b], 'Réécrit intégralement les deux tableaux et les onze notes en dépliant toutes les cellules fusionnées, sépare risques directs et indirects et applique la correction de renvois de 2021, sans alléger les seuils techniques.', review4, [jo, inrs, ue])
