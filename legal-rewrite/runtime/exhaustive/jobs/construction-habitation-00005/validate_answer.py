import collections
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path

sources=json.loads(Path('source.json').read_text())
answer=json.loads(Path('answer.json').read_text())
keys={'code_id','source_id','source_sha256','number','proposed_xml','reason','review_notes','status'}
allowed={'p','br','table','thead','tbody','tfoot','tr','th','td','b','strong','i','em','u','sup','sub','ul','ol','li','div','span','blockquote'}
assert len(answer)==len(sources)==24
assert len({x['source_id'] for x in answer})==24
for s,a in zip(sources,answer):
    assert set(a)==keys
    for k in ('code_id','source_id','source_sha256','number'): assert a[k]==s[k],(a['number'],k)
    assert a['status']=='rewrite_draft'
    assert isinstance(a['proposed_xml'],str) and a['proposed_xml'].strip()
    assert a['proposed_xml'].strip()!=s['source_xml'].strip()
    assert a['reason'] and a['review_notes']
    root=ET.fromstring('<root>'+a['proposed_xml']+'</root>')
    for node in root.iter():
        if node is root: continue
        assert node.tag in allowed,(a['number'],node.tag)
        for key,val in node.attrib.items():
            assert key in {'rowspan','colspan'} and re.fullmatch(r'[0-9]+',val)
    assert s['source_xml'].count('<p>')==a['proposed_xml'].count('<p>'),a['number']
    for tag in ('table','tr','th','td'):
        assert len(re.findall('<'+tag+r'(?:>|\s)',s['source_xml']))==len(re.findall('<'+tag+r'(?:>|\s)',a['proposed_xml']))
    digits=lambda v:collections.Counter(re.findall(r'\d+',unescape(v)))
    assert digits(s['source_xml'])==digits(a['proposed_xml']),(a['number'],digits(s['source_xml'])-digits(a['proposed_xml']),digits(a['proposed_xml'])-digits(s['source_xml']))
    enums=lambda v:re.findall(r'<p>\s*(\d+°)',v)
    assert enums(s['source_xml'])==enums(a['proposed_xml'])
    print(a['number'],'OK',len(list(root)),'alinéas',len(a['proposed_xml']),'caractères')
print('Contrôles structurels, identifiants, nombres et subdivisions : OK')
print('SHA256 source.json :',hashlib.sha256(Path('source.json').read_bytes()).hexdigest())
print('SHA256 answer.json :',hashlib.sha256(Path('answer.json').read_bytes()).hexdigest())
