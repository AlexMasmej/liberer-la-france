import hashlib
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET

source_path = Path('source.json')
sources = json.loads(source_path.read_text())
answer_path = Path('answer.json')
answer = json.loads(answer_path.read_text())
assert len(sources) == len(answer) == 3
assert len({x['source_id'] for x in answer}) == 3
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
required = set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())
report = []
for source, proposed in zip(sources, answer):
    for field in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert source[field] == proposed[field], (source['number'], field)
    assert required <= proposed.keys()
    assert proposed['status'] == 'rewrite_draft'
    assert isinstance(proposed['proposed_xml'], str) and proposed['proposed_xml']
    assert proposed['proposed_xml'] != source['source_xml']
    assert proposed['reason'] and proposed['review_notes']
    root = ET.fromstring('<root>' + proposed['proposed_xml'] + '</root>')
    for element in root.iter():
        assert element.tag == 'root' or element.tag in allowed
        for name, value in element.attrib.items():
            assert name in ('rowspan', 'colspan') and value.isdigit()
    assert not re.search(r'https?://|```|<script|<a\b|texte inchangé', proposed['proposed_xml'], re.I)
    source_root = ET.fromstring('<root>' + source['source_xml'] + '</root>')
    if proposed.get('change_type') == 'normative_reduction':
        assert proposed['reform_policy_id'] == 'editorial_direction_2026_10_19'
        assert proposed['removed_provisions']
        assert all(len(x) >= 30 for x in proposed['removed_provisions'])
        assert not {'repeal_policy_id', 'repeal_scope'} & proposed.keys()
    elif proposed.get('change_type') == 'full_repeal':
        assert proposed['repeal_policy_id'] == 'editorial_direction_2026_10_19'
        assert len(proposed['repeal_scope']) >= 30
        assert ''.join(root.itertext()).startswith(('Le présent article est abrogé', 'Abrogé'))
    else:
        assert set(proposed) == required
    report.append({
        'number': source['number'],
        'identifiers_match': True,
        'source_characters': len(source['source_xml']),
        'source_notes_characters': len(source['source_notes_xml']),
        'proposed_characters': len(proposed['proposed_xml']),
        'source_blocks': len(source_root),
        'proposed_blocks': len(root),
        'source_tables': len(source_root.findall('.//table')),
        'proposed_tables': len(root.findall('.//table')),
        'change_type': proposed.get('change_type', 'rewrite_at_constant_law'),
        'xml_valid': True,
    })

p207 = answer[0]['proposed_xml']
s207 = ET.fromstring('<root>' + sources[0]['source_xml'] + '</root>')
r207 = ET.fromstring('<root>' + p207 + '</root>')
assert len(s207) == 58 and len(r207) == 62
for index, (old, new) in enumerate(zip(s207, r207)):
    old_text, new_text = ''.join(old.itertext()), ''.join(new.itertext())
    old_nums = set(re.findall(r'\d+', old_text))
    new_nums = set(re.findall(r'\d+', new_text))
    # The conventional expression "20 p. 100" becomes "20 %".
    if index == 52:
        old_nums.discard('100')
    assert old_nums <= new_nums, (index, old_nums - new_nums)
    old_label = re.match(r'^\s*((?:\d+°?|[a-d])(?:\s+(?:bis|ter|quater|quinquies))?)', old_text)
    new_label = re.match(r'^\s*((?:\d+°?|[a-d])(?:\s+(?:bis|ter|quater|quinquies))?)', new_text)
    if old_label:
        assert new_label and old_label[1] == new_label[1], (index, old_label, new_label)
assert 'au moins 20 %' in p207 and 'plus de 50 %' in p207
assert '1er janvier 2005' in p207 and '1er janvier 2006' in p207
assert "avant déduction des ristournes" in p207
assert "aux neuvième et onzième alinéas" in p207

p231 = answer[1]['proposed_xml']
assert answer[1]['change_type'] == 'normative_reduction'
assert '<table' not in p231
for threshold in ('100 mètres carrés', '2 500 mètres carrés', '5 000 mètres carrés', '500 mètres carrés'):
    assert threshold in p231
for kept in ('1er mars', '31 décembre 2003', 'quatre ans', 'L. 462-1', '1764', '1599 quater C', '1384 F'):
    assert kept in p231
for removed_rate in ('26,11', '12,98', '21,99', '10,94', '12,03', '7,25', '5,82', '5,26', '8,96', '4,66', '2,39', '4,69', '1,23', '2,96', '1,61', '0,85'):
    assert removed_rate not in p231
assert len(ET.fromstring('<root>' + sources[1]['source_xml'] + '</root>').findall('.//table')) == 4

p261 = answer[2]['proposed_xml']
assert len(ET.fromstring('<root>' + p261 + '</root>')) == 13
assert p261.count('au moins trois') == 2
assert 'trente nuitées' in p261 and 'reconduction' in p261
assert p261.count('même non personnalisée') == 2
assert all(term in p261 for term in ('b bis.', 'L. 633-1', "n'ouvre pas droit à déduction", 'd. (Sans objet).'))

Path('verification.json').write_text(json.dumps({
    'article_count': len(answer),
    'answer_sha256': hashlib.sha256(answer_path.read_bytes()).hexdigest(),
    'source_file_sha256': hashlib.sha256(source_path.read_bytes()).hexdigest(),
    'checks': report,
    'scope': 'Contrôles de structure et invariants après relecture comparative des textes ; aucun avis juridique externe.',
}, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'file': str(answer_path), 'article_count': len(answer), 'checks': report}, ensure_ascii=False, indent=2))
