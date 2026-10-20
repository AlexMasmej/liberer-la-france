import collections
import json
import re
import runpy
from pathlib import Path
from xml.etree import ElementTree as ET

sources = json.loads(Path('source.json').read_text())
drafts = {}
for file in ('draft_01.py', 'draft_02.py', 'draft_03.py'):
    part = runpy.run_path(file)['drafts']
    assert not (drafts.keys() & part.keys())
    drafts.update(part)
assert len(sources) == len(drafts) == 24
assert set(drafts) == {s['number'] for s in sources}

allowed = set('p br table thead tbody tfoot tr th td b strong i em u sup sub ul ol li div span blockquote'.split())
answer = []
report = []
for s in sources:
    d = drafts[s['number']]
    obj = {k: s[k] for k in ('code_id','source_id','source_sha256','number')}
    obj.update(d)
    obj['status'] = 'rewrite_draft'
    assert set(obj) == set(('code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status'))
    assert all(isinstance(v, str) and v for v in obj.values())
    root = ET.fromstring('<root>' + obj['proposed_xml'] + '</root>')
    for node in root.iter():
        if node.tag == 'root':
            continue
        assert node.tag in allowed, (s['number'],node.tag)
        assert all(k in ('rowspan','colspan') and re.fullmatch(r'[0-9]+',v) for k,v in node.attrib.items())
    assert obj['proposed_xml'].strip() != s['source_xml'].strip()
    old_root = ET.fromstring('<root>' + re.sub(r'<br\s*>','<br />',s['source_xml']) + '</root>')
    old_text = ' '.join(old_root.itertext())
    new_text = ' '.join(root.itertext())
    old_nums = collections.Counter(re.findall(r'\d+',old_text))
    new_nums = collections.Counter(re.findall(r'\d+',new_text))
    report.append({
        'article':s['number'],
        'source_chars':len(s['source_xml']),
        'proposed_chars':len(obj['proposed_xml']),
        'source_paragraphs':len(old_root.findall('.//p')),
        'proposed_paragraphs':len(root.findall('.//p')),
        'source_tables':len(old_root.findall('.//table')),
        'proposed_tables':len(root.findall('.//table')),
        'numbers_removed':dict(old_nums-new_nums),
        'numbers_added':dict(new_nums-old_nums),
        'source_identifiers_copied':all(obj[k] == s[k] for k in ('code_id','source_id','source_sha256','number')),
    })
    answer.append(obj)
Path('answer.json').write_text(json.dumps(answer, ensure_ascii=False, indent=2) + '\n')
Path('validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
print('Validated',len(answer),'articles;',Path('answer.json').stat().st_size,'bytes')
