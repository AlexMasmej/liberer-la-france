import json
import re
from collections import Counter
from html import unescape
from pathlib import Path
from xml.etree import ElementTree as ET

sources = json.loads(Path('source.json').read_text())
answers = json.loads(Path('answer.json').read_text())
assert len(sources) == len(answers) == 24
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
fields = set('code_id source_id source_sha256 number proposed_xml reason review_notes status'.split())


def plain(text):
    return re.sub(r'\s+', ' ', unescape(re.sub(r'<[^>]+>', ' ', text))).strip()


def digit_tokens(text):
    # Dans les deux listes de références concernées, 4,5 signifie 4 et 5.
    normalized = plain(text).replace('aux 4,5 et 6', 'aux 4, 5 et 6')
    return Counter(re.findall(r'\d+(?:[-.,]\d+)*', normalized))


for index, (source, answer) in enumerate(zip(sources, answers)):
    assert set(answer) == fields
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert answer[key] == source[key], (index, key)
    assert answer['status'] == 'rewrite_draft'
    assert answer['reason'] and answer['review_notes']
    xml = answer['proposed_xml']
    assert isinstance(xml, str) and xml.strip()
    assert plain(xml) != plain(source['source_xml']), index
    tree = ET.fromstring('<root>' + xml + '</root>')
    for element in tree.iter():
        if element.tag == 'root':
            continue
        assert element.tag in allowed, (index, element.tag)
        for key, value in element.attrib.items():
            assert key in {'rowspan', 'colspan'} and re.fullmatch(r'[0-9]+', value), (index, key)
    original = digit_tokens(source['source_xml'])
    proposed = digit_tokens(xml)
    assert not (original - proposed), (index, original - proposed)
    # Une désignation « article précité » devient explicitement « article 18 quater ».
    assert proposed - original == (Counter({'18': 1}) if index == 19 else Counter()), index
    p_original = len(re.findall(r'<p(?:\s[^>]*)?>', source['source_xml']))
    p_proposed = len(tree.findall('p'))
    if index in {10, 11, 14}:
        assert p_original == 0 and p_proposed == 1
    elif index == 13:
        assert p_original == 0 and p_proposed == 4
    else:
        assert p_original == p_proposed
    assert source['source_xml'].count('<table') == xml.count('<table')
    print(index, source['number'], 'paragraphs', p_original, p_proposed,
          'digits_missing', dict(original - proposed), 'digits_added', dict(proposed - original),
          'tables', source['source_xml'].count('<table'), xml.count('<table'))

assert len({answer['source_id'] for answer in answers}) == 24
print('JSON, identifiants, statuts, intégralité structurelle et balises : contrôles réussis.')
