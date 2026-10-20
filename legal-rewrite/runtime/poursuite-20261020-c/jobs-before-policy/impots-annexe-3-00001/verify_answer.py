import collections
import hashlib
import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def parse(fragment):
    return ET.fromstring('<root>' + re.sub(r'<br\s*/?>', '<br/>', fragment) + '</root>')


def plain(fragment):
    return ' '.join(html.unescape(re.sub(r'<[^>]*>', ' ', fragment)).split())


def tables(fragment):
    result = []
    for table in parse(fragment).findall('.//table'):
        rows = []
        for row in table.findall('.//tr'):
            rows.append([' '.join(' '.join(cell.itertext()).split()) for cell in row])
        result.append(rows)
    return result


source_path = Path('source.json')
source_bytes = source_path.read_bytes()
source_digest = hashlib.sha256(source_bytes).hexdigest()
sources = json.loads(source_bytes)
answers = json.loads(Path('answer.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
required = {'code_id', 'source_id', 'source_sha256', 'number', 'proposed_xml', 'reason', 'review_notes', 'status'}
assert len(sources) == len(answers) == 13
assert len({a['source_id'] for a in answers}) == 13

for source, answer in zip(sources, answers):
    number = source['number']
    assert set(answer) == required, number
    for field in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert source[field] == answer[field], (number, field)
    assert answer['status'] == 'rewrite_draft', number
    assert all(isinstance(answer[k], str) and answer[k] for k in ['proposed_xml', 'reason', 'review_notes'])
    proposed = answer['proposed_xml']
    root = parse(proposed)
    for element in root.iter():
        if element.tag == 'root':
            continue
        assert element.tag in allowed, (number, element.tag)
        assert all(k in {'rowspan', 'colspan'} and re.fullmatch(r'\d+', v) for k, v in element.attrib.items())
    assert plain(source['source_xml']) != plain(proposed), number
    source_numbers = collections.Counter(re.findall(r'\d+(?:,\d+)?', plain(source['source_xml'])))
    proposed_numbers = collections.Counter(re.findall(r'\d+(?:,\d+)?', plain(proposed)))
    assert source_numbers == proposed_numbers, (number, source_numbers - proposed_numbers, proposed_numbers - source_numbers)
    before = tables(source['source_xml'])
    after = tables(proposed)
    assert len(before) == len(after), number
    for index, (old, new) in enumerate(zip(before, after)):
        if number == '2 terdecies H' and index in {1, 2}:
            old_table = parse(source['source_xml']).findall('.//table')[index]
            columns = [[value.strip() for value in cell.itertext() if value.strip()] for cell in old_table.findall('.//tr')[-1]]
            expected = [list(row) for row in zip(*columns)]
            assert old[:2] == new[:2], (number, index, 'headers')
            assert expected == new[2:], (number, index, 'row/column mapping')
        else:
            assert old == new, (number, index)
    if number not in {'2 sexies', '2 undecies'}:
        assert len(parse(source['source_xml']).findall('./p')) == len(root.findall('./p')), number
    print(number + ': identifiants, structure, nombres et tableaux conformes ; texte réécrit.')

assert hashlib.sha256(source_path.read_bytes()).hexdigest() == source_digest
print('13/13 articles ; 9 tableaux intégraux ; aucune anomalie structurelle ou numérique détectée.')
