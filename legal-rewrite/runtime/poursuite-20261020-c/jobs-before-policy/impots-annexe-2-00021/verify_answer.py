import collections
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

source = json.loads(Path('source.json').read_text())
answer = json.loads(Path('answer.json').read_text())
keys = {'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status'}
allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
assert len(source) == len(answer) == 24

def norm(text):
    return ' '.join(text.split())

def table_signature(root):
    result = []
    for table in root.findall('.//table'):
        rows = []
        for tr in table.findall('.//tr'):
            rows.append([(cell.tag,norm(' '.join(cell.itertext())),{k:v for k,v in cell.attrib.items() if k in ('rowspan','colspan')}) for cell in tr])
        result.append(rows)
    return result

for s, a in zip(source, answer):
    assert set(a) == keys
    assert all(a[k] == s[k] for k in ['code_id','source_id','source_sha256','number'])
    assert a['status'] == 'rewrite_draft'
    assert a['reason'] and a['review_notes']
    assert isinstance(a['proposed_xml'],str) and a['proposed_xml'].strip()
    p = ET.fromstring('<root>'+a['proposed_xml']+'</root>')
    r = ET.fromstring('<root>'+s['source_xml']+'</root>')
    for node in p.iter():
        assert node.tag == 'root' or node.tag in allowed
        assert all(k in ('rowspan','colspan') and re.fullmatch(r'[0-9]+',v) for k,v in node.attrib.items())
    assert table_signature(r) == table_signature(p), s['number']+' table difference'
    st = norm(' '.join(r.itertext()))
    pt = norm(' '.join(p.itertext()))
    assert st != pt, s['number']+' identical text'
    nums = lambda x: collections.Counter(re.findall(r'\d+(?:[.,/-]\d+)*',x))
    removed = nums(st)-nums(pt)
    added = nums(pt)-nums(st)
    print(a['number'], 'tables', len(r.findall('.//table')), 'paragraphs',len(r.findall('p')),len(p.findall('p')), 'digits removed',dict(removed),'digits added',dict(added))
print('Structure, identifiers, complete tables and non-identical text: PASS')
