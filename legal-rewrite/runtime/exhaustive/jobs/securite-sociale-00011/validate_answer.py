import collections
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

source = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
assert len(source) == len(answer) == 24
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
for a, b in zip(source, answer):
    assert set(b) == {'code_id', 'source_id', 'source_sha256', 'number', 'proposed_xml', 'reason', 'review_notes', 'status'}
    for key in ('code_id', 'source_id', 'source_sha256', 'number'):
        assert a[key] == b[key], (a['number'], key)
    assert b['status'] == 'rewrite_draft'
    assert all(isinstance(b[k], str) and b[k].strip() for k in ('proposed_xml', 'reason', 'review_notes'))
    root = ET.fromstring('<root>' + b['proposed_xml'] + '</root>')
    for element in root.iter():
        if element is root:
            continue
        assert element.tag in allowed, (a['number'], element.tag)
        assert all(k in ('rowspan', 'colspan') and re.fullmatch(r'[0-9]+', v) for k, v in element.attrib.items())
    assert a['source_xml'].strip() != b['proposed_xml'].strip()
    def plain(value):
        return re.sub(r'<[^>]+>', ' ', value)
    def digits(value):
        return collections.Counter(re.findall(r'\d+(?:[,.]\d+)?(?:-\d+)*', plain(value)))
    missing = digits(a['source_xml']) - digits(b['proposed_xml'])
    p_source = len(re.findall(r'<p\b[^>]*>\s*\S', a['source_xml']))
    p_answer = len(list(root.iter('p')))
    print(a['number'], 'paragraphs', p_source, p_answer, 'chars', len(a['source_xml']), len(b['proposed_xml']), 'missing_numeric_tokens', dict(missing))
    assert a['source_xml'].count('<table') == b['proposed_xml'].count('<table')
print('Structure, identifiers, statuses, allowed XML and table counts: OK')
