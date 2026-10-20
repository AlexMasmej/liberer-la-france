import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path


sources = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
fields = set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())
assert len(sources) == len(answer) == 24
assert len({a['source_id'] for a in answer}) == 24


def text(xml):
    return re.sub('<[^>]+>', '', xml)


def numbered_subdivisions(xml):
    return re.findall(r'(?:^|<p>)\s*((?:[IVX]+\.|[a-z]\)|[0-9]+°))', xml)


for source, proposal in zip(sources, answer):
    assert set(proposal) == fields
    for key in ['code_id', 'source_id', 'source_sha256', 'number']:
        assert source[key] == proposal[key], (source['number'], key)
    assert proposal['status'] == 'rewrite_draft'
    assert proposal['reason'] and proposal['review_notes']
    xml = proposal['proposed_xml']
    assert xml and xml != source['source_xml'].strip()
    root = ET.fromstring('<root>' + xml + '</root>')
    for element in root.iter():
        if element.tag == 'root':
            continue
        assert element.tag in allowed
        for name, value in element.attrib.items():
            assert name in ['rowspan', 'colspan'] and re.fullmatch(r'[0-9]+', value)
    assert collections.Counter(re.findall(r'\d+', text(source['source_xml']))) == collections.Counter(re.findall(r'\d+', text(xml))), source['number']
    original_paragraphs = len(re.findall('<p[ >]', source['source_xml']))
    proposed_paragraphs = len(root.findall('p'))
    if original_paragraphs:
        assert original_paragraphs == proposed_paragraphs, source['number']
    assert numbered_subdivisions(source['source_xml']) == numbered_subdivisions(xml), source['number']
    for tag in ['table', 'thead', 'tbody', 'tfoot', 'tr', 'th', 'td']:
        assert len(re.findall('<' + tag + r'(?:\s|>)', source['source_xml'])) == len(root.findall('.//' + tag)), (source['number'], tag)
    assert text(xml).count('(Périmé)') == text(source['source_xml']).count('(Périmé)'), source['number']
    assert text(xml).count('(Alinéa disjoint)') == text(source['source_xml']).count('(Alinéa disjoint)'), source['number']
    print(source['number'], ': OK')

print('24 articles : identifiants, champs, balises, chiffres, subdivisions, paragraphes, mentions historiques et tableaux contrôlés.')
